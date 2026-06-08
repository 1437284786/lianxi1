# 缺失资料清单

> 本文件依据 `product-master-data.json` 中各产品 `missing_fields` 内的 `pending` 项生成，数据快照日期：2026-06-08。未来重新生成或人工更新时，应先修改主数据并同步 `last_updated`。

## 汇总

| 优先级 | 每个产品待确认项数 | 涉及产品数 | 当前状态 |
|---|---:|---:|---|
| P0 | 10 | 4 | 待确认 |
| P1 | 8 | 4 | 待确认 |
| P2 | 8 | 4 | 待确认 |

## P0：必须立即确认

| 所属产品 | 缺失字段 | JSON 字段 | 优先级 | 对后续工作的影响 | 建议收集部门 | 当前状态 |
|---|---|---|---|---|---|---|
| 一级棕刚玉 (`bfa-grade-1`) | 化学成分 | `chemical_composition` | P0 | 无法制作可靠规格书、报价或开展产品分级 | 技术部／质检部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 粒度 | `grit_sizes` | P0 | 无法匹配客户规格、标准和应用 | 生产部／质检部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 执行标准 | `standards` | P0 | 无法确认合规性或生成规范化产品页面 | 技术部／质检部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 产能 | `production_capacity` | P0 | 无法评估供货能力和客户订单可行性 | 生产部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 包装 | `packaging` | P0 | 无法报价、核算物流或回答采购询盘 | 包装部／仓储物流部／销售部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 主要应用 | `applications` | P0 | 无法进行产品定位和客户行业匹配 | 技术部／销售部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 一级与二级实际差异 | `grade_differences` | P0 | 无法建立可信分级、差异化定位和推荐逻辑 | 技术部／生产部／质检部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 产品照片 | `documents.product_photos` | P0 | 无法制作产品页、目录或客户资料 | 市场部／生产部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 检测报告 | `documents.test_reports` | P0 | 无法验证参数或建立海外客户信任 | 质检部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 英文名称 | `product_name_en` | P0 | 无法统一对外命名、建站和制作出口资料 | 技术部／外贸部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 化学成分 | `chemical_composition` | P0 | 无法制作可靠规格书、报价或开展产品分级 | 技术部／质检部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 粒度 | `grit_sizes` | P0 | 无法匹配客户规格、标准和应用 | 生产部／质检部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 执行标准 | `standards` | P0 | 无法确认合规性或生成规范化产品页面 | 技术部／质检部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 产能 | `production_capacity` | P0 | 无法评估供货能力和客户订单可行性 | 生产部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 包装 | `packaging` | P0 | 无法报价、核算物流或回答采购询盘 | 包装部／仓储物流部／销售部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 主要应用 | `applications` | P0 | 无法进行产品定位和客户行业匹配 | 技术部／销售部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 一级与二级实际差异 | `grade_differences` | P0 | 无法建立可信分级、差异化定位和推荐逻辑 | 技术部／生产部／质检部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 产品照片 | `documents.product_photos` | P0 | 无法制作产品页、目录或客户资料 | 市场部／生产部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 检测报告 | `documents.test_reports` | P0 | 无法验证参数或建立海外客户信任 | 质检部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 英文名称 | `product_name_en` | P0 | 无法统一对外命名、建站和制作出口资料 | 技术部／外贸部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 化学成分 | `chemical_composition` | P0 | 无法制作可靠规格书、报价或开展产品分级 | 技术部／质检部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 粒度 | `grit_sizes` | P0 | 无法匹配客户规格、标准和应用 | 生产部／质检部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 执行标准 | `standards` | P0 | 无法确认合规性或生成规范化产品页面 | 技术部／质检部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 产能 | `production_capacity` | P0 | 无法评估供货能力和客户订单可行性 | 生产部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 包装 | `packaging` | P0 | 无法报价、核算物流或回答采购询盘 | 包装部／仓储物流部／销售部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 主要应用 | `applications` | P0 | 无法进行产品定位和客户行业匹配 | 技术部／销售部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 一级与二级实际差异 | `grade_differences` | P0 | 无法建立可信分级、差异化定位和推荐逻辑 | 技术部／生产部／质检部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 产品照片 | `documents.product_photos` | P0 | 无法制作产品页、目录或客户资料 | 市场部／生产部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 检测报告 | `documents.test_reports` | P0 | 无法验证参数或建立海外客户信任 | 质检部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 英文名称 | `product_name_en` | P0 | 无法统一对外命名、建站和制作出口资料 | 技术部／外贸部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 化学成分 | `chemical_composition` | P0 | 无法制作可靠规格书、报价或开展产品分级 | 技术部／质检部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 粒度 | `grit_sizes` | P0 | 无法匹配客户规格、标准和应用 | 生产部／质检部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 执行标准 | `standards` | P0 | 无法确认合规性或生成规范化产品页面 | 技术部／质检部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 产能 | `production_capacity` | P0 | 无法评估供货能力和客户订单可行性 | 生产部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 包装 | `packaging` | P0 | 无法报价、核算物流或回答采购询盘 | 包装部／仓储物流部／销售部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 主要应用 | `applications` | P0 | 无法进行产品定位和客户行业匹配 | 技术部／销售部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 一级与二级实际差异 | `grade_differences` | P0 | 无法建立可信分级、差异化定位和推荐逻辑 | 技术部／生产部／质检部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 产品照片 | `documents.product_photos` | P0 | 无法制作产品页、目录或客户资料 | 市场部／生产部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 检测报告 | `documents.test_reports` | P0 | 无法验证参数或建立海外客户信任 | 质检部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 英文名称 | `product_name_en` | P0 | 无法统一对外命名、建站和制作出口资料 | 技术部／外贸部 | 待确认 |

## P1：建立独立站前确认

| 所属产品 | 缺失字段 | JSON 字段 | 优先级 | 对后续工作的影响 | 建议收集部门 | 当前状态 |
|---|---|---|---|---|---|---|
| 一级棕刚玉 (`bfa-grade-1`) | 核心卖点 | `selling_points` | P1 | 独立站产品页缺乏可验证的差异化信息 | 技术部／销售部／市场部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 生产工艺 | `production_process` | P1 | 无法解释品质来源和建立技术可信度 | 生产部／技术部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 质量控制 | `production_process.quality_control` | P1 | 无法说明稳定性、检验机制和风险控制 | 质检部／生产部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 认证 | `certifications` | P1 | 无法展示合规能力或筛选有认证要求的客户 | 质量部／行政部／外贸部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 出口经验 | `export_markets` | P1 | 无法形成出口背书或准确评估国际履约经验 | 外贸部／财务部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 应用案例 | `documents.application_cases` | P1 | 无法提供实际应用证据和客户信任素材 | 销售部／技术部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 产品视频 | `documents.product_video` | P1 | 独立站和客户开发缺少可视化证明 | 市场部／生产部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | FAQ | `documents.FAQ` | P1 | 无法统一询盘回复并覆盖客户常见异议 | 销售部／技术部／客服 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 核心卖点 | `selling_points` | P1 | 独立站产品页缺乏可验证的差异化信息 | 技术部／销售部／市场部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 生产工艺 | `production_process` | P1 | 无法解释品质来源和建立技术可信度 | 生产部／技术部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 质量控制 | `production_process.quality_control` | P1 | 无法说明稳定性、检验机制和风险控制 | 质检部／生产部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 认证 | `certifications` | P1 | 无法展示合规能力或筛选有认证要求的客户 | 质量部／行政部／外贸部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 出口经验 | `export_markets` | P1 | 无法形成出口背书或准确评估国际履约经验 | 外贸部／财务部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 应用案例 | `documents.application_cases` | P1 | 无法提供实际应用证据和客户信任素材 | 销售部／技术部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 产品视频 | `documents.product_video` | P1 | 独立站和客户开发缺少可视化证明 | 市场部／生产部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | FAQ | `documents.FAQ` | P1 | 无法统一询盘回复并覆盖客户常见异议 | 销售部／技术部／客服 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 核心卖点 | `selling_points` | P1 | 独立站产品页缺乏可验证的差异化信息 | 技术部／销售部／市场部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 生产工艺 | `production_process` | P1 | 无法解释品质来源和建立技术可信度 | 生产部／技术部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 质量控制 | `production_process.quality_control` | P1 | 无法说明稳定性、检验机制和风险控制 | 质检部／生产部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 认证 | `certifications` | P1 | 无法展示合规能力或筛选有认证要求的客户 | 质量部／行政部／外贸部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 出口经验 | `export_markets` | P1 | 无法形成出口背书或准确评估国际履约经验 | 外贸部／财务部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 应用案例 | `documents.application_cases` | P1 | 无法提供实际应用证据和客户信任素材 | 销售部／技术部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 产品视频 | `documents.product_video` | P1 | 独立站和客户开发缺少可视化证明 | 市场部／生产部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | FAQ | `documents.FAQ` | P1 | 无法统一询盘回复并覆盖客户常见异议 | 销售部／技术部／客服 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 核心卖点 | `selling_points` | P1 | 独立站产品页缺乏可验证的差异化信息 | 技术部／销售部／市场部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 生产工艺 | `production_process` | P1 | 无法解释品质来源和建立技术可信度 | 生产部／技术部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 质量控制 | `production_process.quality_control` | P1 | 无法说明稳定性、检验机制和风险控制 | 质检部／生产部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 认证 | `certifications` | P1 | 无法展示合规能力或筛选有认证要求的客户 | 质量部／行政部／外贸部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 出口经验 | `export_markets` | P1 | 无法形成出口背书或准确评估国际履约经验 | 外贸部／财务部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 应用案例 | `documents.application_cases` | P1 | 无法提供实际应用证据和客户信任素材 | 销售部／技术部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 产品视频 | `documents.product_video` | P1 | 独立站和客户开发缺少可视化证明 | 市场部／生产部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | FAQ | `documents.FAQ` | P1 | 无法统一询盘回复并覆盖客户常见异议 | 销售部／技术部／客服 | 待确认 |

## P2：开展广告前确认

| 所属产品 | 缺失字段 | JSON 字段 | 优先级 | 对后续工作的影响 | 建议收集部门 | 当前状态 |
|---|---|---|---|---|---|---|
| 一级棕刚玉 (`bfa-grade-1`) | 目标国家 | `commercial_data.target_countries` | P2 | 无法设置广告地域、语言和预算 | 管理层／外贸部／市场部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 目标行业 | `commercial_data.target_industries` | P2 | 无法设计广告受众、落地页和转化路径 | 管理层／销售部／市场部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 最小起订量 | `commercial_data.minimum_order_quantity` | P2 | 无法筛选询盘或设置有效广告报价条件 | 销售部／生产部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 价格范围 | `commercial_data.price_range` | P2 | 无法规划广告价值主张和线索资格标准 | 销售部／财务部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 交货周期 | `lead_time` | P2 | 无法回答采购关键问题或承诺交付 | 生产部／销售部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 样品政策 | `commercial_data.sample_policy` | P2 | 无法设计广告线索转化和客户测试流程 | 销售部／外贸部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 主要竞争优势 | `commercial_data.competitive_advantages` | P2 | 无法形成广告主张和竞品差异表达 | 技术部／销售部／市场部 | 待确认 |
| 一级棕刚玉 (`bfa-grade-1`) | 客户常用搜索词 | `commercial_data.customer_search_terms` | P2 | 无法建立可靠的 Google Ads 关键词结构 | 销售部／市场部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 目标国家 | `commercial_data.target_countries` | P2 | 无法设置广告地域、语言和预算 | 管理层／外贸部／市场部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 目标行业 | `commercial_data.target_industries` | P2 | 无法设计广告受众、落地页和转化路径 | 管理层／销售部／市场部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 最小起订量 | `commercial_data.minimum_order_quantity` | P2 | 无法筛选询盘或设置有效广告报价条件 | 销售部／生产部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 价格范围 | `commercial_data.price_range` | P2 | 无法规划广告价值主张和线索资格标准 | 销售部／财务部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 交货周期 | `lead_time` | P2 | 无法回答采购关键问题或承诺交付 | 生产部／销售部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 样品政策 | `commercial_data.sample_policy` | P2 | 无法设计广告线索转化和客户测试流程 | 销售部／外贸部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 主要竞争优势 | `commercial_data.competitive_advantages` | P2 | 无法形成广告主张和竞品差异表达 | 技术部／销售部／市场部 | 待确认 |
| 二级棕刚玉 (`bfa-grade-2`) | 客户常用搜索词 | `commercial_data.customer_search_terms` | P2 | 无法建立可靠的 Google Ads 关键词结构 | 销售部／市场部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 目标国家 | `commercial_data.target_countries` | P2 | 无法设置广告地域、语言和预算 | 管理层／外贸部／市场部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 目标行业 | `commercial_data.target_industries` | P2 | 无法设计广告受众、落地页和转化路径 | 管理层／销售部／市场部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 最小起订量 | `commercial_data.minimum_order_quantity` | P2 | 无法筛选询盘或设置有效广告报价条件 | 销售部／生产部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 价格范围 | `commercial_data.price_range` | P2 | 无法规划广告价值主张和线索资格标准 | 销售部／财务部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 交货周期 | `lead_time` | P2 | 无法回答采购关键问题或承诺交付 | 生产部／销售部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 样品政策 | `commercial_data.sample_policy` | P2 | 无法设计广告线索转化和客户测试流程 | 销售部／外贸部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 主要竞争优势 | `commercial_data.competitive_advantages` | P2 | 无法形成广告主张和竞品差异表达 | 技术部／销售部／市场部 | 待确认 |
| 煅烧棕刚玉 (`calcined-bfa`) | 客户常用搜索词 | `commercial_data.customer_search_terms` | P2 | 无法建立可靠的 Google Ads 关键词结构 | 销售部／市场部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 目标国家 | `commercial_data.target_countries` | P2 | 无法设置广告地域、语言和预算 | 管理层／外贸部／市场部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 目标行业 | `commercial_data.target_industries` | P2 | 无法设计广告受众、落地页和转化路径 | 管理层／销售部／市场部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 最小起订量 | `commercial_data.minimum_order_quantity` | P2 | 无法筛选询盘或设置有效广告报价条件 | 销售部／生产部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 价格范围 | `commercial_data.price_range` | P2 | 无法规划广告价值主张和线索资格标准 | 销售部／财务部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 交货周期 | `lead_time` | P2 | 无法回答采购关键问题或承诺交付 | 生产部／销售部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 样品政策 | `commercial_data.sample_policy` | P2 | 无法设计广告线索转化和客户测试流程 | 销售部／外贸部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 主要竞争优势 | `commercial_data.competitive_advantages` | P2 | 无法形成广告主张和竞品差异表达 | 技术部／销售部／市场部 | 待确认 |
| 镀铱刚玉／表面处理刚玉 (`surface-treated-bfa`) | 客户常用搜索词 | `commercial_data.customer_search_terms` | P2 | 无法建立可靠的 Google Ads 关键词结构 | 销售部／市场部 | 待确认 |

## 当前最优先需要企业补充的 10 项资料

以下十项均为 P0，建议先完成当前生产的一级和二级棕刚玉，再补充未来产品：

1. 一级、二级棕刚玉的完整化学成分范围、典型值、检测方法和报告。
2. 一级、二级棕刚玉可生产粒度清单，以及各粒度对应标准和检测方法。
3. FEPA、JIS、ANSI、国标或企业标准的实际执行情况、编号和版本。
4. 两类当前产品的月产能、最大月供货能力和产线约束。
5. 可用袋型、净重、托盘方式、20/40 尺柜装载量和定制包装能力。
6. 两类产品经企业验证的主要应用、推荐粒度、客户类型和应用依据。
7. 一级与二级产品在原料、成分、工艺、性能、用途和价格上的真实差异。
8. 可对外使用的产品、颗粒、包装和生产现场照片及其使用授权。
9. COA、出厂检验、第三方检测等报告样本、报告编号和有效状态。
10. 依据已确认技术指标确定两类产品的正式英文名称和牌号表达。

## 更新规则

- 只有获得可追溯的企业资料并完成核验后，才能将对应 JSON 状态由 `pending` 改为 `confirmed`。
- 行业参考资料应独立记录为 `reference_only`，并注明“行业参考，不代表本企业数据”。
- 若字段确认不适用，应使用 `not_applicable`，同时记录判断依据。
- 每次更新主数据后，应重新核对本清单并更新快照日期。
