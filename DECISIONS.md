# 项目决策日志

## 使用说明

- 本文件记录影响多个模块、阶段依赖、数据边界或外部承诺的重要决策。
- 新决策不得静默改写历史记录；如需变更，应新增决策并把旧决策状态改为 `superseded`，同时引用替代它的 `decision_id`。
- 决策证据应优先引用仓库文件、企业受控文件编号或公开资料 `source_id`，不得创建虚假证据。
- 决策状态建议使用 `proposed`、`active`、`superseded`、`rejected`。

## 决策模板

```yaml
decision_id: DEC-YYYY-NNN
date: YYYY-MM-DD
decision: 决策内容
reason: 作出该决策的原因
evidence:
  - 文件、企业受控资料编号或 source_id
affected_files:
  - path/to/file
status: proposed | active | superseded | rejected
approved_by: 姓名／角色／待批准
```

## 已记录决策

### DEC-2026-001

- **decision_id**：`DEC-2026-001`
- **date**：2026-06-08
- **decision**：企业真实数据与公开参考数据必须分开存储、标记和使用。
- **reason**：公开行业值、标准入口和竞争对手参数不能证明本企业的实际规格或供货能力，混用会产生错误产品承诺。
- **evidence**：[`product-data/README.md`](product-data/README.md)、[`public-research/README.md`](public-research/README.md)、[`public-research/source-audit.md`](public-research/source-audit.md)。
- **affected_files**：`product-data/**`、`public-research/**`、所有后续营销和销售资料。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-002

- **decision_id**：`DEC-2026-002`
- **date**：2026-06-08
- **decision**：当前生产产品与未来计划产品必须分开处理；未来产品不得形成当前供货承诺。
- **reason**：煅烧和表面处理产品仍依赖设备、工艺与技术确认，不能与一级、二级当前产品混同。
- **evidence**：[`product-data/product-master-data.json`](product-data/product-master-data.json)、[`product-data/README.md`](product-data/README.md)。
- **affected_files**：`product-data/**`、产品定位、网站、推广、报价和销售资料。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-003

- **decision_id**：`DEC-2026-003`
- **date**：2026-06-08
- **decision**：“镀铱刚玉”的正式英文名称保持待技术确认；在确认包覆材料、工艺和是否含 Ir 前，不使用 `Iridium-coated Corundum`。
- **reason**：现有公开来源只证明中文用字与表面包覆描述存在冲突，没有足够证据证明产品含元素铱。
- **evidence**：[`public-research/unresolved-questions.md`](public-research/unresolved-questions.md) 中 SRC-014、SRC-016 的冲突记录；[`public-research/source-audit.md`](public-research/source-audit.md)；[`product-data/terminology.md`](product-data/terminology.md)。
- **affected_files**：产品主数据、术语、产品定位、网站、SEO、广告、TDS、报价和客户沟通资料。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-004

- **decision_id**：`DEC-2026-004`
- **date**：2026-06-08
- **decision**：目标国家分析必须建立在产品定位与产品分级基础上。
- **reason**：没有明确产品等级、应用、客户画像和价值主张，就无法一致地判断需求、竞争、贸易壁垒和推广难度。
- **evidence**：[`ROADMAP.md`](ROADMAP.md) Phase 1 与 Phase 3 的依赖关系；[`public-research/research-report.md`](public-research/research-report.md) 的审计后启示。
- **affected_files**：目标国家研究、市场评分、进入优先级和预算文件。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-005

- **decision_id**：`DEC-2026-005`
- **date**：2026-06-08
- **decision**：独立站建设不得早于产品定位和目标市场定位。
- **reason**：过早建设会固化未经确认的名称、受众、页面结构和营销承诺，造成返工与合规风险。
- **evidence**：[`ROADMAP.md`](ROADMAP.md) Phase 4 的输入、依赖项和完成条件；[`product-data/missing-information.md`](product-data/missing-information.md)。
- **affected_files**：网站信息架构、页面、内容、SEO、设计和开发文件。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-006

- **decision_id**：`DEC-2026-006`
- **date**：2026-06-08
- **decision**：所有重要修改通过任务分支和 Pull Request 审核后进入 `main`。
- **reason**：项目长期迭代且数据风险高，需要保留差异、检查、审批和回滚记录。
- **evidence**：[`AGENTS.md`](AGENTS.md) 的文件修改规则。
- **affected_files**：整个仓库。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）

### DEC-2026-007

- **decision_id**：`DEC-2026-007`
- **date**：2026-06-08
- **decision**：Phase 1 产品定位与分级框架标记为“基本完成”，Phase 2 企业真实数据补充成为当前主阶段；Phase 2 核心数据批准前，Phase 3 目标国家筛选继续保持未开始并受阻塞。
- **reason**：`market-positioning/` 已完成并合并，但最终产品名称、分级逻辑和应用定位仍包含 `pending` 与 hypothesis，需要一级、二级棕刚玉的企业证据支持。提前排名国家、建设正式网站或投放推广会把未批准假设转化为业务承诺。
- **evidence**：[`market-positioning/assumptions-and-gaps.md`](market-positioning/assumptions-and-gaps.md)、[`market-positioning/decision-required.md`](market-positioning/decision-required.md)、[`product-data/missing-information.md`](product-data/missing-information.md)、[`internal-data-intake/p0-master-checklist.csv`](internal-data-intake/p0-master-checklist.csv)。
- **affected_files**：`PROJECT_STATUS.md`、`ROADMAP.md`、`internal-data-intake/**`、后续 `product-data/**` 与 `market-positioning/**` 回填任务。
- **status**：`active`
- **approved_by**：项目任务要求（2026-06-08）
