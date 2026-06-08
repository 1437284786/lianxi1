# 棕刚玉产品技术档案模块

## 模块用途

本模块用于持续收集、整理、核验和维护企业磨料产品资料，当前覆盖一级棕刚玉和二级棕刚玉，并为未来的煅烧棕刚玉、镀铱刚玉／表面处理刚玉预留结构化档案。资料将作为以下工作的统一数据基础：

- 产品资料收集与跨部门协作；
- 产品分类、中文名称和英文名称标准化；
- 国际市场定位与后续目标市场研究；
- 独立站产品页面建设；
- SEO 关键词规划；
- Google Ads 落地页建设；
- 客户询盘回复；
- 产品规格书、TDS、COA 和报价资料制作。

本模块只建立产品技术档案和资料采集基础，不包含网站、目标国家分析或 SEO 文案。

## 当前产品范围

| product_id | 中文名称 | 英文工作名称 | 状态 |
|---|---|---|---|
| `bfa-grade-1` | 一级棕刚玉 | Brown Fused Alumina (Grade 1, Technical Designation Pending) | 当前生产；技术命名待确认 |
| `bfa-grade-2` | 二级棕刚玉 | Brown Fused Alumina (Grade 2, Technical Designation Pending) | 当前生产；技术命名待确认 |
| `calcined-bfa` | 煅烧棕刚玉 | Calcined Brown Fused Alumina | 未来计划；设备和技术升级待完成 |
| `surface-treated-bfa` | 镀铱刚玉／表面处理刚玉 | Surface-treated Brown Fused Alumina | 未来计划；名称及技术待确认 |

> 一级和二级产品不能仅以 “First Grade” 和 “Second Grade” 作为最终英文名称。最终名称必须依据已确认的化学成分、执行标准、工艺和用途确定。

## 数据管理原则

1. 所有未经确认的数据必须标注为“待确认”或在 JSON 中使用 `{"value": null, "status": "pending"}`。
2. 不允许自行编造任何企业技术参数。
3. 不允许用行业常见值替代企业真实数据。
4. 如确需记录行业参考值，必须与企业数据分开，并明确标注：**“行业参考，不代表本企业数据”**；JSON 状态使用 `reference_only`。
5. 每项数据应尽可能记录来源，包括责任部门、文件名、报告编号、批次和日期。
6. 每次修改产品数据时必须同步更新 `last_updated`。
7. 产品中英文名称应以本模块为唯一命名基准，并保持跨文件一致。
8. “镀铱刚玉”是内部暂定名称。在包覆材料、处理工艺和检测报告确认前，不得使用 `Iridium-coated Corundum` 或 `Iridium-coated Brown Fused Alumina` 对外宣传。
9. 结构化数据应保持 UTF-8 编码和机器可读格式，便于后续程序生成页面、规格书和业务资料。

## 文件说明

| 文件 | 用途 |
|---|---|
| [`product-questionnaire.md`](product-questionnaire.md) | 面向生产、技术、质检、销售、外贸等部门的中文资料采集表 |
| [`product-master-data.json`](product-master-data.json) | 四类产品的结构化主数据和状态记录 |
| [`product-comparison.md`](product-comparison.md) | 一级与二级棕刚玉的待核验对比框架 |
| [`missing-information.md`](missing-information.md) | 从主数据 `pending` 状态整理的分级缺失资料清单 |
| [`terminology.md`](terminology.md) | 中英文术语、适用场景和禁用翻译规范 |
| [`templates/product-profile-template.md`](templates/product-profile-template.md) | 单个产品档案模板 |
| [`templates/chemical-composition-template.csv`](templates/chemical-composition-template.csv) | 化学成分批量采集模板 |
| [`templates/particle-size-template.csv`](templates/particle-size-template.csv) | 粒度与标准批量采集模板 |
| [`templates/packaging-template.csv`](templates/packaging-template.csv) | 包装与装柜数据批量采集模板 |

## 推荐维护流程

1. 使用问卷向各责任部门采集资料，并要求提供来源文件。
2. 将已核验数据录入 `product-master-data.json`，状态改为 `confirmed`。
3. 如仅记录行业资料，使用 `reference_only`，不得混入企业产品值。
4. 不适用字段使用 `not_applicable`，不得用空字符串代替。
5. 更新对比表、缺失清单和对应 CSV；更新所有受影响记录的日期。
6. 发布或对外使用前，由技术／质检和外贸负责人共同复核名称、参数、标准及证书有效性。
