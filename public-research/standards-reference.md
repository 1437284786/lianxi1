# 粒度与标准体系审计后参考

> `reference_only` — 行业或竞争对手参考，不代表本企业实际产品数据。标准信息仅来自机构公开目录/摘要，未复制付费标准表格。

## 1. 已由权威来源核实的范围

| 体系 | 当前公开记录 | 范围与用途 | 审计状态 |
|---|---|---|---|
| 固结磨具粗磨粒 | ISO 8486-1:1996 | 电熔氧化铝和碳化硅 F4–F220；用于固结磨具及公开摘要所述一般工业用途 | verified [SRC-002] |
| 固结磨具微粉 | ISO 8486-2:2007 | 电熔氧化铝和碳化硅 F230–F2000；用于固结磨具、一般工业及游离抛光磨粒 | verified [SRC-003] |
| 涂附磨具粗磨粒 | ISO 6344-2:2021 | 电熔氧化铝和碳化硅 P12–P220；用于涂附磨具 | verified [SRC-004] |
| 涂附磨具微粉 | ISO 6344-3:2021 | 电熔氧化铝和碳化硅 P240–P5000；用于涂附磨具 | verified [SRC-005] |
| 中国固结磨具粗磨粒 | GB/T 2481.1-2025 | F4–F220；2026-02-01 实施并替代 GB/T 2481.1-1998 | verified [SRC-028] |

### 本次纠错

- 原 `SRC-003` URL 实际是 ISO 10816-4 燃气轮机振动标准，现已改为 ISO 8486-2:2007 的正确官方记录 `https://www.iso.org/standard/42206.html`。
- 原记录使用 ISO 6344-3:2013（P240–P2500），该版已经撤销；现改为 ISO 6344-3:2021（P240–P5000）。
- 原 GB/T 2481.1-1998 已于 2026-02-01 废止；现改为现行 GB/T 2481.1-2025。

## 2. FEPA F 与 P

FEPA 官网把 bonded abrasives 与 F 系列、coated abrasives 与 P 系列分别列示，并链接相应标准体系。[SRC-001] 本数据库据 ISO 官方摘要记录：

- F：F4–F220 粗磨粒；F230–F2000 微粉。
- P：P12–P220 粗磨粒；P240–P5000 微粉。

F/P 是粒度分布等级，不是单一平均粒径。不能因为数字相同就把 F46 与 P46、F220 与 P220 视为完全相同，也不能在没有现行标准表格时给出精确一一换算。

## 3. JIS、ANSI 与中国其他标准

### JIS

USEM 官网声称可遵循 JIS，但本次审计没有取得 JISC 官方标准编号、版本和公开摘要。因此，本数据库只保留“供应商声称具备 JIS 供货能力”的线索，状态为 `unverified`；不提供精确 JIS 范围或换算。[SRC-022]

### ANSI

Washington Mills 的 BLASTITE 技术资料声称符合 ANSI B74.12，USEM 官网也声称遵循 ANSI。[SRC-010][SRC-022] 这些资料只能证明企业声明，不能替代标准正文。采购文件必须写明具体 ANSI 文件、版本、产品范围和验收方法。

### GB/T

本轮只直接核实了 GB/T 2481.1-2025（F4–F220）的官方记录。[SRC-028] GB/T 2481.2-2020、GB/T 9258.2-2025、GB/T 9258.3-2025 等虽在官方相近标准列表中出现，但未作为独立来源登记，因此本文件不展开其精确要求。

## 4. Mesh、Grit、段砂、细粉和微粉

- `Grit` 在本项目中通常指一个带分布要求的磨料等级，如 F46 或 P80。
- `Mesh` 是筛网/筛孔表达；具体含义取决于筛系、通过/截留符号和公差。
- Bosai 页面公开列出 0–1、1–3、3–6、6–10 mm 等 BFA 规格；Haixu 页面同时列出 mesh/mm 等商业规格。[SRC-019][SRC-020]
- 这些企业规格能够证明市场存在段砂和筛下粉表达，但不能建立 Mesh↔FEPA↔JIS↔ANSI 的权威换算。

## 5. 化学与喷砂相关标准入口

- ISO 9285:1997 的公开摘要说明其是电熔氧化铝的化学分析方法标准；它不规定行业统一成分限值。[SRC-006]
- ISO 11126-7:2018 的公开摘要列出熔融氧化铝喷砂介质涉及的粒度、表观/堆积密度、莫氏硬度、水分、电导率和水溶性氯化物等要求类别；本数据库没有复制其数值表。[SRC-007]

## 6. 合规使用规则

1. 合同中写明标准编号、年份、产品用途和抽样/验收方式。
2. 不把供应商自称“FEPA/JIS/ANSI”直接当作第三方认证。
3. 不制作无版本、无容差的万能换算表。
4. 需要标准限值时，应合法购买或通过授权渠道取得现行文本。

[SRC-001]: https://fepa-abrasives.org/abrasives/standards/
[SRC-002]: https://www.iso.org/standard/15695.html
[SRC-003]: https://www.iso.org/standard/42206.html
[SRC-004]: https://www.iso.org/standard/78220.html
[SRC-005]: https://www.iso.org/standard/78219.html
[SRC-006]: https://www.iso.org/standard/16940.html
[SRC-007]: https://www.iso.org/standard/66713.html
[SRC-010]: https://www.washingtonmills.com/sites/default/files/2023-04/BLASTITE.pdf
[SRC-019]: https://www.bosaieurope.de/en/our-products/corundum/index.html
[SRC-020]: https://brownalumina.com/product/brown-fused-alumina/
[SRC-022]: https://usminerals.com/home
[SRC-028]: https://std.samr.gov.cn/gb/search/gbDetailed?id=3B46A026CC16469CE06397BE0A0AEEB8
