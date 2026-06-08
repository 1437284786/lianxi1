# 棕刚玉公开研究数据库：来源真实性与结论可追溯性审计报告

**审计日期：2026-06-08**
**数据状态：`reference_only`**
**声明：行业或竞争对手参考，不代表本企业实际产品数据。**

## 1. 执行摘要

本次审计没有扩充大量来源，而是逐条检查原有 29 条来源的 URL、标题、机构身份、页面类型和正文，并重新核对结构化数据及 Markdown 的关键结论。

审计发现并修复了三项标准记录问题：

1. 原 `SRC-003` URL 指向无关的 ISO 10816-4 燃气轮机振动标准，现改为 ISO 8486-2:2007 正确官方记录。[SRC-003]
2. 原 `SRC-005` 使用已撤销的 ISO 6344-3:2013，现更新为 ISO 6344-3:2021，范围为 P240–P5000。[SRC-005]
3. 原 GB/T 2481.1-1998 已废止，现更新为 2026-02-01 实施的 GB/T 2481.1-2025。[SRC-028]

29 条来源中，26 条通过 GET 正常取得目标内容；SRC-011、SRC-012、SRC-013 持续返回 HTTP 503，已从 `partially_verified` 降为 `unverified`，相关精确竞争对手参数已删除。

## 2. 产品命名研究

公开企业页面同时使用 **Brown Fused Alumina**、**Brown Fused Aluminum Oxide** 和 **Brown Aluminum Oxide**；BFA 是常见缩写。[SRC-008][SRC-019][SRC-020][SRC-029]

建议：

- 主名称：**Brown Fused Alumina (BFA)**；
- 美国市场可接受同义词：**Brown Fused Aluminum Oxide**；
- 所有销售名称均应附用途、粒度体系、处理方式和可验证规格。

## 3. 一级和二级棕刚玉

Haixu 页面公开使用 A/B/C Grade 并给出企业自定义范围，证明供应商分级确实存在。[SRC-020] 但 ISO/FEPA 来源没有提供“一级/二级 BFA”的统一国际定义。

因此：

- `Premium-grade BFA` 只是建议性营销描述，必须附明确规格；
- `Secondary-grade BFA` 当前为 `unverified` 分类；
- 在内部确认物料来源前，不得使用 recycled、reclaimed、by-product 等词。

## 4. 化学指标

以下仅是多个指定供应商页面的交叉观察，不是行业标准：

| 项目 | 可追溯公开值 | 来源与限制 |
|---|---|---|
| Al2O3 | KORUND 94.5–97%；Minex 95.20%；Bosai ≥95% | [SRC-017][SRC-019][SRC-021]；范围/典型/最小值不可视为同一统计口径 |
| TiO2 | Blastrite 2.7%；Minex 2.90%；Bosai ≤3.20% | [SRC-017][SRC-018][SRC-019] |
| Fe2O3 | Blastrite 0.1%；Minex 0.20%；Bosai ≤0.30% | 同上；不等于磁性物 |
| SiO2 | Blastrite 0.7%；Minex 1.30%；Bosai ≤1.20% | 同上；“no free silica”不等于总 SiO2 为零 |
| CaO/MgO | Blastrite 0.1%/0.2% | [SRC-018]；单一产品 typical 值 |
| BTCAL | Al2O3 95.61、TiO2 2.55、SiO2 0.90、Fe2O3 0.23、MgO 0.32 wt% | [SRC-023]；单一热处理商业产品 |

ISO 9285 是分析方法入口，不是统一成分限值。[SRC-006]

## 5. 物理性能

供应商页面直接支持的常见记录包括：莫氏硬度 9、比重/真密度约 3.9–4.0 g/cm³，以及随粒度变化的堆积密度。[SRC-008][SRC-017][SRC-018][SRC-021] 所有数值均为指定企业产品参考。

审计后作出以下限制：

- 堆积密度必须绑定粒度、粒形和方法；
- 熔点 2050°C 与 2250°C 来自两家供应商页面，保持 `partially_verified/low`，不再概括为行业范围；[SRC-016][SRC-020]
- 已删除“热处理后普遍变蓝并提高韧性”的泛化结论；只保留 BTCAL TDS 对其单一产品的热处理和高韧性声明；[SRC-023]
- 磁性物、pH、耐火度没有形成可审计的行业统一范围，保持 `unverified`。

## 6. 粒度和标准

经官方记录确认：

- ISO 8486-1:1996：F4–F220，固结磨具粗磨粒；[SRC-002]
- ISO 8486-2:2007：F230–F2000，固结磨具微粉；[SRC-003]
- ISO 6344-2:2021：P12–P220，涂附磨具粗磨粒；[SRC-004]
- ISO 6344-3:2021：P240–P5000，涂附磨具微粉；[SRC-005]
- GB/T 2481.1-2025：F4–F220，现行中国固结磨具粗磨粒标准。[SRC-028]

JIS 只从供应商官网间接得知，未取得 JISC 官方记录，因此保持 `unverified`。ANSI B74.12 由 Washington Mills 技术资料声明，状态为 `partially_verified`。[SRC-010][SRC-022]

本库不提供 F/P/JIS/ANSI/Mesh 精确换算关系。

## 7. 应用行业

直接有来源支持的用途包括：

- 固结磨具、砂轮和涂附磨具；[SRC-008][SRC-009][SRC-015][SRC-023]
- 喷砂、除锈、氧化皮清除和表面处理；[SRC-010][SRC-017][SRC-018]
- 精密铸件清理；[SRC-010]
- 耐火材料；[SRC-008][SRC-019][SRC-021]
- 研磨、抛光和 lapping；[SRC-008][SRC-017]
- 层压材料相关行业。[SRC-008][SRC-022]

原应用矩阵中的替代材料、采购关注点、一级/二级适用判断及大量通用粒度推荐没有逐项来源，已改为“Research lead only”。地坪、防滑和水刀切割保持 `unverified`。

## 8. 煅烧和热处理产品

Washington Mills 资料明确列出 heat-treated BFA；BTCAL TDS明确称产品在回转窑高温热处理和磁选，并提供产品专属化学/物理数据。[SRC-009][SRC-023]

由于 DOMILL 和 Runbao 页面本次无法访问，原来引用其 1050°C/1350°C 工艺及性能描述已从确定性结论中删除。`Calcined BFA` 只有在确认是 BFA 成品的后处理时使用；否则建议使用更宽泛的 `Heat-treated BFA`。

## 9. 表面处理产品

公开可验证的商业表达包括：red iron oxide coated、silane coated、supplier-described ceramic coating 和中文“镀衣磨料”。[SRC-008][SRC-009][SRC-014][SRC-016][SRC-023]

这些来源只证明产品类别和企业声明。不同包覆材料、添加量和性能不可互相外推。

## 10. “镀铱刚玉”专项复核

河南东风官方页面明确声称“镀衣磨料不是镀铱磨料，不含化学元素铱”，并描述为有机或无机陶瓷结合剂及辅料包覆。[SRC-014] 另一企业页面中文使用“镀铱”，但英文写作 `Ceramic coated Brown Fused Alumina`，未提供 Ir 配方、专利、论文或元素分析。[SRC-016]

审计结论：

```text
推荐暂定英文：Surface-treated Brown Fused Alumina
verification_status：unverified
备注：具体包覆材料和工艺必须由企业技术部门确认
禁止作为正式名称：Iridium-coated Corundum
```

单一供应商页面不足以证明行业通用名称，也不足以证明元素铱存在。

## 11. 主要生产国家和区域

- USGS 2018 历史资料把中国列为熔融氧化铝主要产能国；该数据不是 BFA 专项，也不是当前市场份额。[SRC-027]
- USGS 2024 报告记录美国 fused aluminum oxide 净进口依赖度超过 95%，并提供 2019–2022 进口来源数据；同样不是 BFA 专项。[SRC-025]
- 欧盟委员会 2026 年页面记录中国熔融氧化铝进口贸易措施、欧盟总量估计及欧盟生产国；其范围宽于 BFA。[SRC-026]
- Blastrite 页面能证明企业在南非有加工/供应业务，不能证明南非 BFA 产量。[SRC-018]

原“中国河南强产业集群”“各区域成本优势”等结论证据不足，已降级或删除。

## 12. 竞争对手身份审计

| 企业 | 审计后身份 |
|---|---|
| Washington Mills | 官方页面明确的 BFA manufacturer |
| DOMILL | 页面持续 503；身份和参数均 unverified |
| Runbao | 页面持续 503；身份和参数均 unverified |
| USEM | 工业矿物颗粒/粉体 manufacturer，同时是 Elfusa distributor/representative；BTCAL 不能简单归为 USEM 自产 |
| Bosai Europe | Bosai 集团欧洲销售实体/供应商；页面称产品来自中国 own production |
| Blastrite | 颗粒磨料 manufacturer and distributor；未证明其自行电熔 ALCAB BFA |
| Minex | 表面处理系统集成商和磨料供应商，不是 BFA manufacturer |
| Haixu | 企业自称 manufacturer/supplier；保持 partially_verified |
| KORUND | 磨料供应商；页面未证明其为电熔炉生产商 |

## 13. 海外搜索词

产品名、用途名和采购意图关键词属于研究假设，不是产品性能事实。`terminology-and-keywords.md` 已明确：这些词只用于搜索和内容研究，不证明市场规模、客户偏好或转化效果，也不能直接建立广告活动。

## 14. 冲突和不确定性

1. “镀铱/镀衣”文字冲突且无 Ir 证据；
2. 熔点供应商值冲突；
3. `B.D.` 在 Bosai 页面未定义，3.85 g/ccm 更接近颗粒/真密度量级，不能擅自改名；
4. 一级/二级、A/B/C 是供应商或企业分级，不是统一国际分类；
5. JIS 官方标准记录未核实；
6. DOMILL、Runbao 页面无法访问；
7. 大多数市场统计合并全部 fused aluminum oxide，而非 BFA。

## 15. 对我方定位的审计后启示

以下只是内部研究方向，不是我方参数：

- 用可检验规格替代“一级/二级”单独标签；
- 对煅烧/包覆产品写明真实工艺和目标性能；
- 不把供应商 typical 值变成我方 guarantee；
- 对外资料区分 F、P、Mesh 和 mm 段砂；
- 在技术确认前统一把“镀铱”称为 `Surface-treated Brown Fused Alumina`。

## 16. 必须内部确认的数据

一级/二级真实定义和物料来源、各粒度化学限值、粒度标准版本、密度/粒形/磁性物方法、煅烧制度、包覆材料、是否含 Ir、应用试验、包装、认证和法规状态。完整清单见 `unresolved-questions.md`。

## 17. 后续建议

1. 合法取得关键标准现行文本；
2. 对所谓“镀铱”进行配方核实和元素分析；
3. 获取可访问的 DOMILL/Runbao 官方替代页面或 TDS 后再恢复其数据；
4. 对竞争对手参数按“企业—产品—粒度—方法”重新建模；
5. 真实企业数据继续留在受控 `product-data` 流程，本公开库不得回填。

## 18. 审计统计

- 原始来源：29；
- GET 正常取得目标内容：26；
- 访问失败：3（SRC-011、SRC-012、SRC-013，HTTP 503）；
- confidence：high 18、medium 11、low 0；
- source verification_status：verified 26、partially_verified 0、unverified 3、conflicting 0；
- 标准来源纠正：SRC-003、SRC-005、SRC-028；
- 竞争对手身份/参数修正：9 家均复核，2 家访问失败后删除精确参数，多家由 producer/manufacturer 改为 supplier/integrator/group sales entity。

完整逐来源审计表和命令见 `source-audit.md`。

[SRC-002]: https://www.iso.org/standard/15695.html
[SRC-003]: https://www.iso.org/standard/42206.html
[SRC-004]: https://www.iso.org/standard/78220.html
[SRC-005]: https://www.iso.org/standard/78219.html
[SRC-006]: https://www.iso.org/standard/16940.html
[SRC-008]: https://www.washingtonmills.com/BFA
[SRC-009]: https://www.washingtonmills.com/sites/default/files/pdfs/brochures/Bonded_line_card_email.pdf
[SRC-010]: https://www.washingtonmills.com/sites/default/files/2023-04/BLASTITE.pdf
[SRC-014]: https://www.ycdf.com.cn/products/Coated-Grains/
[SRC-015]: https://www.ycdf.com.cn/Coated-Abrasives/
[SRC-016]: https://www.hngangyu.com/gwdszgy/100.html
[SRC-017]: https://www.minexgroup.eu/en/blasting/abrasive-media/brown-fused-alumina
[SRC-018]: https://blastrite.com/products/aluminium-oxide/
[SRC-019]: https://www.bosaieurope.de/en/our-products/corundum/index.html
[SRC-020]: https://brownalumina.com/product/brown-fused-alumina/
[SRC-021]: https://www.korund.pl/en/products/brown-fused-alumina/
[SRC-022]: https://usminerals.com/home
[SRC-023]: https://usminerals.com/files/produtosAtualizadosPDF/BFA%20-%20Brown%20Fused%20Alumina%20-%20Bonded%20%26%20Industrial%20Abrasives%20-%20BTCAL-R.pdf
[SRC-025]: https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-abrasives.pdf
[SRC-026]: https://policy.trade.ec.europa.eu/news/commission-acts-against-unfairly-traded-imports-fused-alumina-2026-01-16_en
[SRC-027]: https://pubs.usgs.gov/myb/vol1/2018/myb1-2018-abrasives.pdf
[SRC-028]: https://std.samr.gov.cn/gb/search/gbDetailed?id=3B46A026CC16469CE06397BE0A0AEEB8
[SRC-029]: https://www.washingtonmills.com/sites/default/files/2025-05/Brown%20Fused%20Aluminum%20Oxide_US%20SDS%20%5BEN%5D.pdf
