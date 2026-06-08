#!/usr/bin/env python3
"""Validate Phase 2 intake CSVs without network access or data modification."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INTAKE_DIR = REPO_ROOT / "internal-data-intake"

ALLOWED_PRODUCTS = {
    "bfa-grade-1",
    "bfa-grade-2",
    "calcined-bfa",
    "surface-treated-bfa",
}
CURRENT_PRODUCTS = {"bfa-grade-1", "bfa-grade-2"}
WORKFLOW_STATUSES = {
    "not_started",
    "collecting",
    "received",
    "under_review",
    "approved",
    "rejected",
    "not_applicable",
}
DATA_STATUSES = {
    "confirmed",
    "pending",
    "reference_only",
    "not_applicable",
    "unverified",
    "conflicting",
}
CONFIDENTIALITY_LEVELS = {"public", "internal", "confidential", "restricted"}
YES_VALUES = {"yes", "true", "1"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EVIDENCE_ID_RE = re.compile(r"^INT-[A-Z0-9]+-\d{4}-\d{3,}$")

REQUIRED_HEADERS = {
    "p0-master-checklist.csv": [
        "gap_id", "product_id", "data_category", "requested_item",
        "required_evidence", "responsible_department", "priority", "status",
        "source_file", "source_date", "applicable_grit_or_batch", "approved_by",
        "approval_date", "confidentiality_level", "target_repository_file", "notes",
    ],
    "evidence-register.csv": [
        "evidence_id", "evidence_type", "file_name", "document_title", "product_id",
        "grit_or_batch", "date_issued", "issuer", "department", "confidentiality_level",
        "verification_status", "approved_by", "approval_date", "related_gap_ids",
        "target_data_fields", "notes",
    ],
    "document-inventory.csv": [
        "inventory_id", "document_type", "product_id", "file_name", "document_title",
        "version_or_batch", "date_issued", "department", "confidentiality_level",
        "storage_location", "intake_status", "evidence_id", "notes",
    ],
    "product-evidence-matrix.csv": [
        "matrix_id", "product_id", "data_field", "applicable_grit",
        "applicable_batch_or_period", "data_value", "evidence_ids", "data_status",
        "approval_status", "approved_by", "approval_date", "confidentiality_level",
        "external_marketing_allowed", "related_gap_ids", "target_repository_file", "notes",
    ],
}

errors: list[str] = []
warnings: list[str] = []


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def read_csv(name: str) -> tuple[list[str], list[dict[str, str]]]:
    path = INTAKE_DIR / name
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(REPO_ROOT)}")
        return [], []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        missing = [header for header in REQUIRED_HEADERS[name] if header not in headers]
        if missing:
            errors.append(f"{name}: missing required headers: {', '.join(missing)}")
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    return headers, rows


def validate_date(value: str, location: str) -> None:
    if not value:
        return
    if not DATE_RE.fullmatch(value):
        errors.append(f"{location}: date must use YYYY-MM-DD, got {value!r}")
        return
    try:
        date.fromisoformat(value)
    except ValueError:
        errors.append(f"{location}: invalid calendar date {value!r}")


def validate_unique(rows: list[dict[str, str]], field: str, file_name: str, allow_blank: bool = False) -> set[str]:
    values: list[str] = []
    for line_no, row in enumerate(rows, 2):
        value = row.get(field, "")
        if not value:
            if not allow_blank:
                errors.append(f"{file_name}:{line_no}: {field} is required")
            continue
        values.append(value)
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    for value in duplicates:
        errors.append(f"{file_name}: duplicate {field} {value!r}")
    return set(values)


def validate_product(value: str, location: str, required: bool = True) -> None:
    if not value:
        if required:
            errors.append(f"{location}: product_id is required")
        return
    if value not in ALLOWED_PRODUCTS:
        errors.append(f"{location}: illegal product_id {value!r}")


def validate_confidentiality(value: str, location: str) -> None:
    if value not in CONFIDENTIALITY_LEVELS:
        errors.append(f"{location}: illegal confidentiality_level {value!r}")


_, checklist = read_csv("p0-master-checklist.csv")
_, evidence = read_csv("evidence-register.csv")
_, inventory = read_csv("document-inventory.csv")
_, matrix = read_csv("product-evidence-matrix.csv")

gap_ids = validate_unique(checklist, "gap_id", "p0-master-checklist.csv")
evidence_ids = validate_unique(evidence, "evidence_id", "evidence-register.csv", allow_blank=False)
validate_unique(inventory, "inventory_id", "document-inventory.csv")
validate_unique(matrix, "matrix_id", "product-evidence-matrix.csv")

for line_no, row in enumerate(checklist, 2):
    loc = f"p0-master-checklist.csv:{line_no}"
    validate_product(row.get("product_id", ""), loc)
    if row.get("product_id") not in CURRENT_PRODUCTS:
        errors.append(f"{loc}: P0 current-product checklist may only contain grade 1/2 products")
    if row.get("priority") != "P0":
        errors.append(f"{loc}: priority must be P0")
    if row.get("status") not in WORKFLOW_STATUSES:
        errors.append(f"{loc}: illegal workflow status {row.get('status')!r}")
    validate_confidentiality(row.get("confidentiality_level", ""), loc)
    validate_date(row.get("source_date", ""), f"{loc} source_date")
    validate_date(row.get("approval_date", ""), f"{loc} approval_date")
    if row.get("status") == "approved" and (not row.get("approved_by") or not row.get("approval_date")):
        errors.append(f"{loc}: approved record requires approved_by and approval_date")
    source_path = row.get("source_file", "").split("#", 1)[0]
    if source_path and not (REPO_ROOT / source_path).exists():
        errors.append(f"{loc}: source_file does not exist: {source_path}")
    target_path = row.get("target_repository_file", "")
    if target_path and not (REPO_ROOT / target_path).exists():
        errors.append(f"{loc}: target_repository_file does not exist: {target_path}")

for line_no, row in enumerate(evidence, 2):
    loc = f"evidence-register.csv:{line_no}"
    validate_product(row.get("product_id", ""), loc)
    validate_confidentiality(row.get("confidentiality_level", ""), loc)
    validate_date(row.get("date_issued", ""), f"{loc} date_issued")
    validate_date(row.get("approval_date", ""), f"{loc} approval_date")
    evidence_id = row.get("evidence_id", "")
    if evidence_id and not EVIDENCE_ID_RE.fullmatch(evidence_id):
        errors.append(f"{loc}: evidence_id must match INT-<TYPE>-YYYY-NNN, got {evidence_id!r}")
    status = row.get("verification_status", "")
    if status == "approved" and (not row.get("approved_by") or not row.get("approval_date")):
        errors.append(f"{loc}: approved evidence requires approved_by and approval_date")
    for gap_id in split_ids(row.get("related_gap_ids", "")):
        if gap_id not in gap_ids:
            errors.append(f"{loc}: unknown related gap_id {gap_id!r}")

for line_no, row in enumerate(inventory, 2):
    loc = f"document-inventory.csv:{line_no}"
    validate_product(row.get("product_id", ""), loc)
    validate_confidentiality(row.get("confidentiality_level", ""), loc)
    validate_date(row.get("date_issued", ""), f"{loc} date_issued")
    evidence_id = row.get("evidence_id", "")
    if evidence_id and evidence_id not in evidence_ids:
        errors.append(f"{loc}: unknown evidence_id {evidence_id!r}")
    if row.get("intake_status") == "received" and (not row.get("file_name") or not evidence_id):
        errors.append(f"{loc}: received document requires file_name and registered evidence_id")

for line_no, row in enumerate(matrix, 2):
    loc = f"product-evidence-matrix.csv:{line_no}"
    validate_product(row.get("product_id", ""), loc)
    validate_confidentiality(row.get("confidentiality_level", ""), loc)
    validate_date(row.get("approval_date", ""), f"{loc} approval_date")
    if row.get("data_status") not in DATA_STATUSES:
        errors.append(f"{loc}: illegal data_status {row.get('data_status')!r}")
    if row.get("approval_status") not in WORKFLOW_STATUSES:
        errors.append(f"{loc}: illegal approval_status {row.get('approval_status')!r}")
    linked_evidence = split_ids(row.get("evidence_ids", ""))
    for evidence_id in linked_evidence:
        if evidence_id not in evidence_ids:
            errors.append(f"{loc}: unknown evidence_id {evidence_id!r}")
    linked_gaps = split_ids(row.get("related_gap_ids", ""))
    if not linked_gaps:
        errors.append(f"{loc}: at least one related_gap_id is required")
    for gap_id in linked_gaps:
        if gap_id not in gap_ids:
            errors.append(f"{loc}: unknown related gap_id {gap_id!r}")
    if row.get("data_status") == "confirmed" and not linked_evidence:
        errors.append(f"{loc}: confirmed data requires at least one evidence_id")
    if row.get("data_status") == "confirmed" and row.get("approval_status") != "approved":
        errors.append(f"{loc}: confirmed data requires approval_status approved")
    if row.get("approval_status") == "approved" and (not row.get("approved_by") or not row.get("approval_date")):
        errors.append(f"{loc}: approved matrix record requires approved_by and approval_date")
    if row.get("confidentiality_level") in {"confidential", "restricted"} and row.get("external_marketing_allowed", "").lower() in YES_VALUES:
        errors.append(f"{loc}: confidential/restricted record cannot be marked for external marketing")
    if row.get("external_marketing_allowed", "").lower() in YES_VALUES:
        if row.get("data_status") != "confirmed" or row.get("approval_status") != "approved":
            errors.append(f"{loc}: external marketing requires confirmed data and approved status")
    target_path = row.get("target_repository_file", "")
    if target_path and not (REPO_ROOT / target_path).exists():
        errors.append(f"{loc}: target_repository_file does not exist: {target_path}")

# Validate any confirmed records already stored in the intake matrix, not public reference data.
# The product master is parsed only to catch malformed JSON and illegal product identifiers; it is not modified.
product_master = REPO_ROOT / "product-data/product-master-data.json"
try:
    product_data = json.loads(product_master.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"product-data/product-master-data.json: cannot parse: {exc}")
else:
    def walk(value: object) -> None:
        if isinstance(value, dict):
            product_id = value.get("product_id")
            if isinstance(product_id, str) and product_id not in ALLOWED_PRODUCTS:
                errors.append(f"product-data/product-master-data.json: illegal product_id {product_id!r}")
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(product_data)

counts = Counter(row.get("product_id") for row in checklist)
status_counts = Counter(row.get("status") for row in checklist)
print("Phase 2 intake validation")
print(f"- checklist rows: {len(checklist)} ({dict(sorted(counts.items()))})")
print(f"- checklist statuses: {dict(sorted(status_counts.items()))}")
print(f"- evidence records: {len(evidence)}")
print(f"- document inventory rows: {len(inventory)}")
print(f"- product-evidence matrix rows: {len(matrix)}")
if warnings:
    print("Warnings:")
    for warning in warnings:
        print(f"- {warning}")
if errors:
    print("Errors:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("OK: all Phase 2 intake checks passed.")
