# 来源真实性与结论可追溯性审计

**审计日期：2026-06-08**
**范围：仅 `public-research/`；未修改企业产品主数据。**

## 1. 审计统计

| 指标 | 结果 |
|---|---:|
| 原始来源数量 | 29 |
| GET 正常取得目标内容 | 26 |
| 访问失败 | 3 |
| high | 18 |
| medium | 11 |
| low | 0 |
| verified | 26 |
| partially_verified | 0 |
| unverified | 3 |
| conflicting | 0 |

`verification_status` 在来源表中表示“URL、发布者和页面内容是否能核验”；具体产品结论另有记录级状态。可访问不等于高可信度。

## 2. 逐来源审计结果

| ID | GET | 标题/发布者检查 | 类型与身份 | 处理 |
|---|---:|---|---|---|
| SRC-001 | 200 | FEPA 标题一致 | 行业协会官网 | verified/high |
| SRC-002 | 200 | ISO 8486-1 标题一致 | 标准机构记录 | verified/high |
| SRC-003 | 200 | 原 URL 实为 ISO 10816-4，与记录不符 | 标准机构记录 | **改为正确 ISO 8486-2 URL 42206** |
| SRC-004 | 200 | ISO 6344-2:2021 一致 | 标准机构记录 | verified/high |
| SRC-005 | 200 | 原 2013 版已撤销 | 标准机构记录 | **更新为 ISO 6344-3:2021/P240–P5000** |
| SRC-006 | 200 | ISO 9285 一致 | 标准机构记录 | verified/high；仅支持分析方法 |
| SRC-007 | 200 | ISO 11126-7 一致 | 标准机构记录 | verified/high；未复制数值表 |
| SRC-008 | 200 | Washington Mills BFA 产品页一致 | 制造商技术产品页 | verified/high |
| SRC-009 | 200 | 官方 PDF 可提取，2007 年版 | 制造商产品册 | verified/high；提示时效 |
| SRC-010 | 200 | BLASTITE 官方 PDF 一致 | 制造商技术资料 | verified/high |
| SRC-011 | 503 | 无法重新取得标题/正文 | 声称企业产品页 | **unverified/medium；访问失败** |
| SRC-012 | 503 | 无法重新取得 PDF | 声称企业 TDS | **unverified/medium；访问失败** |
| SRC-013 | 503 | 无法重新取得标题/正文 | 声称企业产品页 | **unverified/medium；访问失败** |
| SRC-014 | 200 | 河南东风标题/发布者一致 | 企业产品页 | verified/medium |
| SRC-015 | 200 | 河南东风应用页一致 | 企业应用页 | verified/medium |
| SRC-016 | 200 | 中文“镀铱”、英文 ceramic coated 均在页内 | 企业产品页 | verified/medium；Ir 结论 unverified |
| SRC-017 | 200 | Minex 标题一致 | 集成商/供应商产品页 | verified/medium；不是制造商证据 |
| SRC-018 | 200 | Blastrite ALCAB 页面一致 | 制造/分销企业产品页 | verified/medium；不证明自行电熔 |
| SRC-019 | 200 | Bosai Europe 页面一致 | 集团销售实体技术页 | verified/high |
| SRC-020 | 200 | Haixu 产品页一致 | 企业产品页 | verified/medium；A/B/C 为自定义 |
| SRC-021 | 200 | KORUND 产品页一致 | 供应商产品页 | verified/medium；不证明炉产身份 |
| SRC-022 | 200 | 实际标题为 Home - USEM | 企业普通官网 | verified/medium；修正集团/子公司边界 |
| SRC-023 | 200 | BTCAL PDF 可提取 | 官方 TDS | verified/high |
| SRC-024 | 200 | USGS 页面一致 | 政府统计门户 | verified/high |
| SRC-025 | 200 | USGS 2024 PDF 可提取 | 政府报告 | verified/high |
| SRC-026 | 200 | 欧委会标题/日期一致 | 政府新闻/贸易措施 | verified/high |
| SRC-027 | 200 | USGS 2018 年鉴 PDF 可提取 | 政府历史报告 | verified/high |
| SRC-028 | 200（修正后） | 原 1998 版已废止 | 政府标准记录 | **更新为 GB/T 2481.1-2025** |
| SRC-029 | 200 | Washington Mills SDS 标题/日期一致 | 官方 SDS | verified/high |

未发现 B2B 平台被标为官方 TDS，也未发现重复 URL。SRC-011/012 属同一不可访问企业域名但内容类型不同，不作为重复来源删除。SRC-014/015 页面联系方式引用 `domill.cn`，可能与 DOMILL 属同一企业体系，因此不能把它们当作彼此独立的交叉证据。同一发布者的产品页、TDS、SDS也只算同一企业证据链。

## 3. 删除或改写的结论

- 删除依赖 SRC-011/012/013 的精确化学范围、粒度、1050°C/1350°C 工艺和性能结论。
- 删除固结/树脂磨具的通用粒度推荐和一级/二级适配判断。
- 删除应用矩阵中无逐项来源的替代材料、采购关注点和“yes/conditional”结论。
- 将地坪、防滑、水刀切割改为 `unverified` 研究问题。
- 将“中国河南产业集群”“区域成本优势”等改为证据不足，不再作为确定事实。
- 把熔点冲突保留为两个供应商值，不再写成行业范围。
- 把热处理韧性描述限定到 BTCAL 单一产品的供应商声明。
- 把海外关键词明确为研究假设，不作为客户偏好或市场规模事实。

## 4. 竞争对手身份修正

- DOMILL、Runbao：访问失败，删除精确参数并改为 unverified supplier identity。
- USEM：区分 USEM 自身制造/分销角色与 Elfusa/Curimbaba 产品来源。
- Bosai Europe：改为集团欧洲销售实体/供应商，不直接写成中国炉产主体。
- Blastrite：保留“颗粒磨料制造和分销”，但不声称其自行电熔 ALCAB。
- Minex：改为系统集成商和磨料供应商。
- KORUND：改为供应商，未证实为电熔炉生产商。
- Haixu：制造商身份仅来自企业自述，状态 partially_verified。

## 5. “镀铱刚玉”结论

没有 reviewed source 提供 Iridium 配方、元素检测、专利或论文证据。来源之间只证明中文用字冲突和陶瓷/结合剂包覆描述。因此保持：

```text
recommended_english: Surface-treated Brown Fused Alumina
verification_status: unverified
note: 具体包覆材料和工艺必须由企业技术部门确认
```

## 6. 实际执行命令

- `curl -L --max-time 45 --connect-timeout 12 --retry 1 -A 'Mozilla/5.0 public-source-audit/1.0' URL`
  - 结果：修正 URL 后 26 个来源返回目标内容，3 个来源 HTTP 503。
- Python + `pypdf`：提取官方 PDF 标题和正文，用于核验 Washington Mills、USEM/Elfusa、USGS 文档。
- `python -m json.tool public-research/industry-reference-data.json`
- Python `csv.DictReader`：检查 CSV 列数、ID、枚举、日期和引用关系。
- Python 递归检查：所有 JSON 外部记录含 `reference_only` 和统一声明。
- `rg`：检查 `Iridium-coated Corundum`、`Diamond Sand`、`confirmed` 的使用语境。
- `sha256sum product-data/product-master-data.json` 与 `git diff -- product-data/product-master-data.json`：确认企业主数据未修改。

## 7. 仍存在的不确定性

- 三个 503 来源是否只是临时防爬或内容已删除；
- JIS 的准确官方标准编号和现行范围；
- ANSI B74.12 的现行版本和供应商具体符合范围；
- 一级/二级 BFA 的企业内部定义；
- 包覆材料、包覆量和是否含 Ir；
- 各供应商 typical 值的测试方法和批次代表性；
- fused aluminum oxide 总类统计中 BFA 的具体份额。
