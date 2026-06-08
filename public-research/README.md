# 棕刚玉行业公开资料库

> **数据性质：`reference_only`**
> **统一声明：行业或竞争对手参考，不代表本企业实际产品数据。**

本目录仅保存截至 **2026-06-08** 从公开互联网采集的棕刚玉（Brown Fused Alumina, BFA）行业、标准、应用与竞争对手参考资料。它与 `product-data/` 中的企业真实产品主数据严格隔离。

## 安全边界

- 不得把本目录任何化学、物理、粒度或应用参数复制为我方 `confirmed` 产品参数。
- 未修改、也不应由本研究流程修改 `product-data/product-master-data.json`。
- 单个供应商的典型值只代表其公开页面/产品，不构成行业标准。
- 标准全文如需付费，应合法购买；本目录只记录公开摘要、目录、编号和适用范围。
- “镀铱刚玉”暂用英文 **Surface-treated Brown Fused Alumina**，状态为“名称和工艺待技术确认”；不得直接译成 `Iridium-coated Corundum`。
- URL、产品可用性、标准状态和贸易措施会变化，商业使用前必须重新验证。

## 文件说明

| 文件 | 用途 |
|---|---|
| `industry-reference-data.json` | 机器可读的产品、成分、物性、粒度、应用、区域、术语与来源数据 |
| `competitor-database.csv` | 9 家公开可识别生产商/供应商及其公开产品信息 |
| `standards-reference.md` | FEPA、ISO、ANSI、JIS、中国 GB/T、Mesh 与段砂体系说明 |
| `application-industries.md` | 主要应用、产品选择逻辑与采购关注点 |
| `terminology-and-keywords.md` | 中英文术语、误译风险与海外搜索词 |
| `public-sources.csv` | 29 条公开来源登记表 |
| `unresolved-questions.md` | 冲突、失败页面和必须内部确认的问题 |
| `research-report.md` | 审计后综合研究报告与下一阶段建议 |
| `source-audit.md` | 29 条来源逐条真实性审计、纠错和命令记录 |

## 联网验证（正式研究前完成）

| 网页标题 | 域名 | 页面类型 | 访问结果 | 后续研究适用性 |
|---|---|---|---|---|
| Home \| FEPA - Federation of European Producers of Abrasives | `fepa-abrasives.org` | 行业协会官网首页 | HTTP 200，标题与正文可读取 | 适合；优先用于 FEPA 粒度体系和标准化说明 |
| ISO 35:1989 - Natural rubber latex concentrate — Determination of mechanical stability | `iso.org` | 国际标准机构标准记录页 | HTTP 200，标题与正文可读取 | 仅用于验证 ISO 网站连通性；该页面主题与棕刚玉无关，不作为研究结论来源 |
| Brown Fused Aluminum Oxide \| Washington Mills | `washingtonmills.com` | 生产商官方产品页 | HTTP 200，标题与正文可读取 | 适合；用于产品命名、产品系列与应用研究 |

验证命令采用 `curl -L` 的只读 GET 请求，未使用 POST、登录、验证码绕过或付费墙绕过。

## 数据使用建议

1. 先按 `source_id` 回查 `public-sources.csv`。
2. 对关键参数至少采用“标准/协会 + 两家独立供应商”交叉验证。
3. 报价和规格书中必须写清：化学限值、粒度体系及版本、粒形/堆积密度测试方法、磁性物测试方法、水分和包装。
4. 对一级/二级、煅烧、镀衣等中文商业名称建立企业内部技术定义后，再确定稳定英文名称。

## 2026-06-08 来源审计

已逐条复核 29 条来源：26 条可取得目标内容，3 条 HTTP 503 并降为 `unverified`；纠正了 ISO 8486-2、ISO 6344-3 和 GB/T 2481.1 的错误/过期记录。详见 `source-audit.md`。
