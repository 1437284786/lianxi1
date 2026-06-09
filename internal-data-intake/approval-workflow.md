# Phase 2 企业数据批准流程

## 1. 角色与职责

| 角色 | 最低职责 |
|---|---|
| 资料接收人 | 检查文件可读性、保密级别、产品和批次标识；不得判断技术真实性 |
| 数据登记人 | 更新文件清单和证据登记，分配唯一 `evidence_id` |
| 数据提取人 | 原样提取字段、单位、方法、适用范围，不补值、不外推 |
| 责任部门核实人 | 核实文件真实性、技术含义、适用产品/粒度/批次和是否仍有效 |
| 授权批准人 | 决定是否批准写回、批准范围和是否允许外部营销 |
| 数据维护人 | 在批准后更新 `product-data/` 和受影响的定位文件，保留版本链 |

Codex 可以协助结构化提取和一致性检查，但不能担任企业核实人或批准人。

## 2. 八步工作流

### 第 1 步：资料接收

- 仅接收企业实际提供的文件或记录；记录接收日期、提供部门和保密级别。
- 检查是否标明产品、粒度、批次/时间范围、文件版本和出具方。
- 客户资料先匿名化；原始受限文件应放在企业受控存储，不提交公开仓库。
- P0 状态可从 `not_started` 更新为 `collecting`；文件实际可读后才可更新为 `received`。

### 第 2 步：文件登记

- 在 `document-inventory.csv` 填写真实文件元数据和受控位置；`intake_status` 只能使用 `not_received`、`received`、`under_review`、`accepted`、`rejected`、`expired`、`superseded`，记录存在时不得留空。
- 按 `INT-<类型>-YYYY-NNN` 分配 `evidence_id`，例如 `INT-COA-2026-001`。
- 在 `evidence-register.csv` 登记证据类型、文件名、产品、批次、出具方、保密等级和关联缺口；`verification_status` 只能使用 `received`、`under_review`、`verified`、`approved`、`rejected`、`expired`、`superseded`，证据记录存在时不得留空。
- 不得登记不存在的文件，不得把需求占位当作证据。

### 第 3 步：数据提取

- 在 `product-evidence-matrix.csv` 逐字段录入原始值、单位、值类型、测试方法、抽样方法、适用粒度、批次/时间范围、工厂/产线和有效期。
- `value_type` 不得留空，只能使用 `single_batch_result`、`typical_value`、`internal_control_limit`、`guaranteed_specification`、`capability_statement`、`qualitative_statement`、`pending`；没有真实数据的占位记录使用 `pending`。
- `typical_value`、`guaranteed_specification`、`single_batch_result` 和 `internal_control_limit` 必须分开；不得把单批结果改写为保证规格。
- 化学成分和物理检测数值一旦录入，必须同时填写 `unit` 和 `test_method`；未知的单位、方法、工厂/产线或有效期保持空白，不得推测。
- 多份证据存在差异时保留各记录并标记 `conflicting`，不得选择更有利的值。
- 提取后 P0 状态更新为 `under_review`，数据状态仍为 `pending`。

### 第 4 步：技术或责任部门核实

责任部门至少核实：

1. 文件是否真实、完整且为现行版本；
2. 产品、粒度、批次、时间范围和工厂是否匹配；
3. 单位、测试方法、抽样方法和保证/典型属性是否正确；
4. 是否可代表长期能力，或仅代表单批/单次测试；
5. 是否涉及配方、客户身份、价格、成本等受限内容；
6. 是否需要补充证据、重测或裁决冲突。

### 第 5 步：管理或授权人员批准

- 授权人填写 `approved_by` 和 ISO 日期 `approval_date`；`valid_from`、`valid_until` 如填写也必须使用合法的 `YYYY-MM-DD`，且结束日期不得早于开始日期。
- 批准应说明：批准的数据值、适用范围、有效期/复审条件、保密级别，以及是否允许外部营销。`guaranteed_specification` 必须关联真实证据、处于 `approved` 状态并记录批准人。
- 证据不足或不适用时分别使用 `rejected` 或 `not_applicable`，并记录理由。
- 只有完成核实和批准的记录，P0 状态才可设为 `approved`。`external_marketing_allowed` 只能为 `yes` 或 `no`；设为 `yes` 时必须同时满足 `data_status=confirmed`、`approval_status=approved`、`confidentiality_level=public`，并存在证据、批准人和批准日期。

### 第 6 步：批准后更新 `product-data/`

- 只有 `approved` 记录才可进入 `product-data/` 的回填评估。
- 满足 `DATA_POLICY.md` 的证据和批准条件后，目标字段才可使用 `confirmed`。
- 未批准资料、行业参考、竞争对手值和 Codex 推断不得写入 `product-master-data.json`。
- 回填时同步更新 `last_updated`、证据引用、适用范围和缺失信息清单。

### 第 7 步：同步定位文件

产品定义、分级、命名、应用边界、供货能力等重要数据更新后，应复核并按需更新 `market-positioning/`。原有 `pending` 或 hypothesis 只有在企业证据支持并完成批准后才能升级；不得自动改写为最终定位。

### 第 8 步：旧版数据与失效管理

- 旧版证据、旧值和旧批准不得删除；应保留版本、替代证据、失效日期和失效原因。
- 文件过期、标准换版、工艺变更、批次范围变化或批准撤回时，应重新审核相关字段。
- 新旧证据冲突时使用 `conflicting`，待责任部门裁决后记录理由和受影响文件。
- 对外资料使用前必须检查其引用的批准记录是否仍有效。

## 3. 状态转换

`not_started → collecting → received → under_review → approved`

允许的例外：

- 任一审核阶段可转为 `rejected`，但必须记录原因；
- 经责任部门确认确实不适用后可转为 `not_applicable`；
- `approved` 数据发生变更或失效时，新增版本重新审核，不静默覆盖旧记录。
