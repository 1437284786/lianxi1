# 棕刚玉产品国际市场定位与产品分级方案

> **成果性质：初步定位与待验证框架，不是最终商业承诺。** 本模块处于 Phase 1，只能用于内部产品定位、企业资料采集和管理层决策准备；不得直接转为报价、交期、广告、正式网站文案或客户技术承诺。

## 1. 范围与生命周期边界

| 产品 | product_id | 生命周期/供货状态 | 本模块处理方式 |
|---|---|---|---|
| 一级棕刚玉 | `bfa-grade-1` | 当前生产、当前可销售 | 可建立条件式定位；技术规格、应用适配和最终英文名仍为 `pending` |
| 二级棕刚玉 | `bfa-grade-2` | 当前生产、当前可销售 | 可建立条件式定位；不得推断为 recycled/reclaimed 或全球统一低等级 |
| 煅烧棕刚玉 | `calcined-bfa` | 未来产品；设备升级后才可能销售 | 仅建立产品开发与验证门槛，不进入当前供货目录 |
| 表面处理棕刚玉 | `surface-treated-bfa` | 未来产品；技术升级与商业批准后才可能销售 | 暂称 `Surface-treated Brown Fused Alumina`；不得称 `Iridium-coated Corundum` |

来源边界：当前/未来状态来自 `product-data/product-master-data.json`；应用、术语、标准与竞争资料只引用 `public-research/` 的 `source_id`，均不代表我方能力。

## 2. 文件导航

- [管理层摘要](executive-summary.md)
- [产品分级](product-tiering.md)
- [国际命名](international-naming.md)
- [应用—客户矩阵](application-customer-matrix.csv)
- [客户画像](customer-personas.md)
- [价值主张](value-propositions.md)
- [竞争定位](competitor-positioning.md)
- [产品组合策略](product-portfolio-strategy.md)
- [证据地图](evidence-map.csv)
- [假设与缺口](assumptions-and-gaps.md)
- [待管理层决策](decision-required.md)

## 3. 状态与证据规则

### 数据状态

本模块沿用仓库允许的数据状态：`confirmed`、`pending`、`reference_only`、`not_applicable`、`unverified`、`conflicting`。其中：

- `confirmed` 仅用于“企业已确认当前生产一级、二级产品”等已有内部事实；
- `reference_only` 仅表示公开资料支持行业中存在某应用、术语或产品做法；
- `pending` 表示我方参数、适配性、命名或商业能力待内部确认；
- `unverified`/`conflicting` 用于无法复核或公开资料冲突的事项。

### 卖点成熟度标签

`value-propositions.md` 按任务要求使用 `confirmed`、`supported_by_public_research`、`hypothesis`、`pending_internal_validation` 作为**卖点成熟度标签**。后 3 项不是仓库数据状态；对应数据状态分别仍按 `reference_only` 或 `pending` 管理。

### 置信度

CSV 中 `confidence` 只使用 `high`、`medium`、`low`，表示本次定位判断的证据充分程度，不等于企业数据状态。

## 4. 使用方法

1. 先查 [证据地图](evidence-map.csv) 的 `conclusion_id`。
2. 凡是我方能力，必须回到企业受控文件或产品主数据字段；公开来源不能代替企业数据。
3. 凡是应用建议，必须经过样品、客户规格、内部技术审核或客户试用后才可升级为外部表述。
4. 粒度没有企业或客户依据时统一写 `pending`；公开供应商粒度仅可在备注中作为研究线索。
5. 当前产品与未来产品必须在目录、询盘、样品、报价和交期处理中保持分离。

## 5. 本次明确不包含

目标国家排名、价格策略、网站建设、正式营销文案、Google Ads、真实账户、企业参数回填及任何尚未批准的产品承诺。
