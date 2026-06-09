# Phase 2 企业真实数据采集模块

## 1. 模块目的

本目录是 Phase 2“企业真实数据补充”的 P0 采集、证据登记、审核和回填入口。当前仅优先处理在产的 `bfa-grade-1`（一级棕刚玉）和 `bfa-grade-2`（二级棕刚玉）；`calcined-bfa`（煅烧棕刚玉）与 `surface-treated-bfa`（表面处理棕刚玉）仅在进度看板保留状态，不得作为当前可销售产品。

本模块不保存未经授权的机密原件，不因公开资料存在相似值而认定企业数据已收到或已批准，也不直接修改 `product-data/product-master-data.json`。

## 2. 文件职责

| 文件 | 用途 |
|---|---|
| `p0-master-checklist.csv` | 一级、二级 P0 缺口、责任部门、证据要求和采集状态主清单 |
| `evidence-register.csv` | 已实际收到的内部证据索引；无真实文件时保持仅表头 |
| `document-inventory.csv` | 应收文件类型与收件状态；需求占位不代表文件存在 |
| `product-evidence-matrix.csv` | 产品—字段—适用粒度/批次—证据—批准—外部使用权限矩阵 |
| `approval-workflow.md` | 接收、核实、批准、回填和版本失效流程 |
| `ingestion-guide.md` | 企业准备、命名、匿名化和导入资料的方法 |
| `confidentiality-rules.md` | 四级保密规则和公开仓库边界 |
| `progress-dashboard.md` | 按 P0 清单状态展示的非虚构进度看板 |
| `department-questionnaires/` | 五个责任部门的定向问卷 |
| `scripts/validate-phase2-intake.py` | 离线、只读的一致性校验脚本 |

## 3. 状态体系

P0 工作流状态仅允许：`not_started`、`collecting`、`received`、`under_review`、`approved`、`rejected`、`not_applicable`。这些是任务/审核状态，不替代项目数据状态。

各采集文件另有严格枚举：

- `evidence-register.csv.verification_status`：`received`、`under_review`、`verified`、`approved`、`rejected`、`expired`、`superseded`；有证据记录时不得留空。
- `document-inventory.csv.intake_status`：`not_received`、`received`、`under_review`、`accepted`、`rejected`、`expired`、`superseded`；任何库存记录均不得留空。
- `product-evidence-matrix.csv.external_marketing_allowed`：只能为 `yes` 或 `no`，不得留空。
- `product-evidence-matrix.csv.value_type`：只能为 `single_batch_result`、`typical_value`、`internal_control_limit`、`guaranteed_specification`、`capability_statement`、`qualitative_statement`、`pending`，不得留空。

写回产品数据时仍只使用 `DATA_POLICY.md` 规定的数据状态：`confirmed`、`pending`、`reference_only`、`not_applicable`、`unverified`、`conflicting`。只有存在可追溯证据、完成责任部门核实并由授权人批准的数据，才可使用 `confirmed`。

## 4. 当前基线

- P0 主清单共 45 项：一级 22 项，二级 23 项；二级多出的项目是来源及 `virgin/recycled/reprocessed` 属性核实。
- 所有项目初始状态均为 `not_started`，不得把行业值、竞争对手值或口头猜测标为 `received` 或 `approved`。
- `evidence-register.csv` 当前没有证据记录；`document-inventory.csv` 的记录均为“应收需求占位”。
- `product-evidence-matrix.csv` 只建立字段关系；45 条占位记录的 `data_value`、`unit`、方法、工厂/产线和有效期均为空，`value_type` 为 `pending`，数据状态保持 `pending`，批准状态保持 `not_started`，外部营销权限为 `no`。

## 5. 操作顺序

1. 按部门问卷准备资料，并按 `ingestion-guide.md` 脱敏和命名。
2. 在受控存储接收原件；公开仓库只记录允许公开的内容或不泄密的索引。
3. 真实文件进入 `document-inventory.csv`，分配内部 `evidence_id` 后登记至 `evidence-register.csv`。
4. 在 `product-evidence-matrix.csv` 提取数据并限定产品、粒度、批次/时间范围。
5. 按 `approval-workflow.md` 完成核实和批准。
6. 只有批准后，另开任务更新 `product-data/`；关键定位数据变化时同步更新 `market-positioning/`。
7. 运行 `python internal-data-intake/scripts/validate-phase2-intake.py`，检查无误后提交审核。

## 6. 输入来源与边界

P0 清单基于：

- `market-positioning/assumptions-and-gaps.md`；
- `market-positioning/decision-required.md`；
- `product-data/missing-information.md`；
- `public-research/unresolved-questions.md` 仅用于识别必须由企业确认的问题，不用于填企业值。

本模块不开展新的公开市场研究、竞争对手研究或目标国家排名。
