---
id:              marginalia-024
title:           "铁轨铺在火车前面：发布周期的政治经济学——从 CPU 跑分到 SOTA"
date:            2026-09-06
published:       2026-09-06
kind:            research memo（研究备忘）
sources:
  - "Mollick, E. 2006. 'Establishing Moore's Law.' IEEE Annals of the History of Computing. doi:10.1109/mahc.2006.45；Lécuyer, C. 2020. 'Driving Semiconductor Innovation.' Enterprise & Society"
  - "Mack, C. 2003. 'The End of the Semiconductor Industry as We Know It'（lithoguru.com，'not a law, an act of will'）；IEEE Spectrum 2020（node 命名虚构化）；Intel 2021 新闻稿与 8-K（'stopped matching the actual gate-length metric in 1997'）；ASML 路线图 PPT（OFweek 2024 转述：N3 实际半节距 23nm）"
  - "Corrocher & Paganuzzi 2025, 'Planned obsolescence and smartphone replacement.' Telecommunications Policy；Smart Analytics Global 2026（Apple Upgrade 与 34 个月替换周期）；IMF WP/20/70"
  - "Nieborg, D. 2014. 'Prolonging the Magic: the political economy of the 7th generation console game.' doi:10.7557/23.6155；Kretschmer & Claussen 2016（backward compatibility）"
  - "VR 失败组：vr.org（Reality Labs 累亏 $88B，2026-Q2）；CNBC 'VR winter' 2026-01-24；stratrix.com Vision Pro 平台注读法"
  - "Scaling Laws：Kaplan et al. 2020（arXiv:2001.08361）；Hoffmann et al. 2022（Chinchilla）；Pearce & Song 2024（arXiv:2406.12907）；Lilian Weng 2026-06；boxcars.ai 定律命名竞赛"
  - "理论：Slade, Made to Break (2006)；Packard, The Waste Makers (1960)；Cowen, The Deadly Life of Logistics (2014)；Tsing, supply chain capitalism；Lipovetsky, The Empire of Fashion；Porter, Trust in Numbers (1995)；Dourish, The Stuff of Bits (2017)"
initial-prompt: "把 scope 扩大到整个技术谱系：智能手机宣称 CPU/GPU/续航提升，Apple 如何说服，高通与华为的对抗话语；为什么这套流程能持续？物质性上提供了什么？文化动力与利益在哪？VR/AR 为什么没起来？发布周期——手机一年、主机一世代、AI 数月——背后与物流链后勤性权力、资金流、回报周期、硅谷期待的关系。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           53
---

# 铁轨铺在火车前面：发布周期的政治经济学——从 CPU 跑分到 SOTA

> 研究备忘：发布周期不是技术属性而是制度——由物流链与后勤性权力、资金流与回报周期、对「进步」的期待共同决定的时间节奏。本条 = 五平台矩阵 + 想法提纲 + 核验材料。旧版论证文见 git 历史。引用已于 2026-09-07 全量搜索核验（29 项引用 + 3 条金句全部追到实体，零死链），记录见文末。

## 五平台节奏矩阵

| 平台 | 节奏 | 协调装置 | 物质吞吐 | 收益结构 |
|---|---|---|---|---|
| PC/CPU | 18–24 月（tick-tock） | Moore's Law + ITRS roadmap | 晶圆/光刻机/稀土 | 卖芯片毛利 |
| 智能手机 | 一年（Apple 定节奏） | 秋季发布会 + 运营商合约 + 以旧换新 | 全球物流链/电子垃圾 | 硬件+服务+金融（HaaS） |
| 游戏主机 | 5–7 年「世代」 | 世代叙事（Next Gen）+ 独占游戏 | 大批量单一配置 | 亏本卖硬件+软件抽成 |
| VR/AR | 无稳定节奏（失败） | 缺席 | 高摩擦硬件、低复购 | 未找到 |
| AI 模型 | 大版本分化/小版本加速 | benchmark 排行榜（自动公开） | GPU/电力/数据中心（最重） | API/订阅/融资飞轮 |

## 核心想法

1. **节奏 = 自我实现的预言**（概念源头：Merton 1948；Mollick 把摩尔定律作为其技术史实例）：摩尔定律是「把铁轨铺在火车前面」的意志行动——发布周期的承诺反过来规定技术必须抵达的速率。
2. **撞墙后定律靠两种会计操作存活**：改周期（tick-tock→P.A.O.）+ 改度量（node 命名与物理脱钩）；AI 侧平行结构（大版本分化 + 小版本加密）。
3. **两种物质性**：具身产品（atoms，有状态、迁移贵、节奏被最慢层锁死）vs 信息表征（bits，stateless、替代近零成本、节奏由最快层决定）；Memory 功能把 bits 重新原子化 = 移植手机的留存经济学。
4. **失败案例检验命题**：VR 有全部硬件条件但无可复利物质依赖，转不成节拍。
5. **后勤倒挂**：发布最轻（翻转权重）× 后勤最重（GW 级电力、百万卡集群）——这是 AI 需要 Scaling Law 作资本叙事的原因。

## 想法 × 材料

### 想法 1 · 自我实现的预言（半导体解剖）

- **[Mollick 2006, IEEE Annals of the History of Computing](https://doi.org/10.1109/mahc.2006.45)**——"Establishing Moore's Law." 28(3): 62–75。Ethan Mollick，**发表时单位 MIT Sloan**（Wharton 是 2016 年后现任，引用 2006 时勿写）。摘要即定性 "evolved into a self-fulfilling prophecy"。全文镜像：[gwern.net](https://gwern.net/doc/economics/experience-curve/2006-mollick.pdf)。
- **[Lécuyer 2022, Enterprise & Society](https://www.cambridge.org/core/journals/enterprise-and-society/article/abs/driving-semiconductor-innovation-moores-law-at-fairchild-and-intel/58A6DBCC19D454A2BB20E1333A9D12C6)**——"Driving Semiconductor Innovation: Moore's Law at Fairchild and Intel." 23(1): 133–163（在线 2020-09-07，刊期 2022-03）。Christophe Lécuyer（Sorbonne Université）。「多用途工具：驱动工艺、卖芯片、压垮对手」与摘要逐点吻合。
- **金句出处（已锁定）**：
  - 「把铁轨铺在火车前面」= Gordon Moore 1997 原话："It really becomes a question of putting the track ahead of the train to stay on plan." 一手出处：Ed Korczynski 对 Moore 的访谈，*Solid State Technology* 40(7), July 1997, p. 364（经 Misa 2019, doi:10.2478/host-2019-0005, 脚注 7 转引）。
  - 「摩尔定律不是定律，是意志的行动」= **Chris A. Mack**："Moore's Law is not a law, it is an act of will."（Mack 2011, "Fifty Years of Moore's Law," *IEEE Trans. Semiconductor Manufacturing* 24(2): 202–207, doi:10.1109/TSM.2010.2096437；2003 年 Solid State Technology 文为分号版本。**此句不在 2003 SPIE PDF 内**。）
  - 「我们让它成真，因为我们希望它成真」= **旧版误挂 Gordon Moore**——该句是 **Mack 自己写的**（"We make Moore's Law happen because we want it to be true"，2003 SPIE 文内）。Moore 的实录近似语："the industry made it a self-fulfilling prophesy"（*A Conversation with Gordon Moore*, Intel 访谈实录，[Stanford 镜像 PDF](https://large.stanford.edu/courses/2012/ph250/lee1/docs/Excepts_A_Conversation_with_Gordon_Moore.pdf)）。
- **[Mack 2003: The End of the Semiconductor Industry as We Know It](https://lithoguru.com/scientist/litho_papers/2003_The_End_of_the_Semiconductor_Industry_as_We_Know_It.pdf)**——首发即 Proc. SPIE 5040（Optical Microlithography XVI, Plenary Address）, pp. xxi–xxxi；作者时任职 KLA-Tencor FINLE Division, Austin。

### 想法 2 · 两种会计操作（改周期 + 改度量）

- **[Intel 新闻稿 2021-07-26](https://www.intc.com/news-events/press-releases/detail/1486/intel-accelerates-process-and-packaging-innovations)**——原话（主语是「业界」）："the industry acknowledged that traditional nanometer-based process node naming stopped matching the actual gate-length metric in 1997"；同稿含 Intel 7 改名与 20A "angstrom era"。
- **[Ars Technica 2016-03-23](https://arstechnica.com/information-technology/2016/03/intel-retires-tick-tock-development-model-extending-the-life-of-each-process/)**（Ars Staff）——tick-tock 退役，改 "Process, Architecture, Optimization"，每代约三年。
- **[IEEE Spectrum 2020-07-21](https://spectrum.ieee.org/a-better-way-to-measure-progress-in-semiconductors)**（Samuel K. Moore，半导体编辑；印刷版题名 **"The Node is Nonsense"**，2020-08）——命名与物理脱钩（原文口径 "about two decades"，自 90 年代中算起约三十年；引用时用「二十多年起」更稳）。PDF 镜像：[UC Davis](https://www.ece.ucdavis.edu/~bbaas/116/docs/paper.spectrum.better.meas.progress.semi.pdf)。
- **[OFweek 2024-06-17：ASML 掀老底](https://ee.ofweek.com/2024-06/ART-8500-2800-30637775.html)**——N3 金属半节距 23nm、A10(1nm)→18nm（维科号匿名聚合稿）。
- **黄汉森「制程节点已经变成了一种营销游戏」**：Hot Chips 2019 发言的中文报道——[快科技](https://news.mydrivers.com/1/646/646865.htm)、[界面新闻](https://www.jiemian.com/article/3774568.html)。单独引用，勿挂 OFweek 条目。
- Scaling Laws 平行结构：**[Kaplan et al. 2020](https://arxiv.org/abs/2001.08361)**（"Scaling Laws for Neural Language Models", arXiv:2001.08361, 10 人, OpenAI——Kaplan 兼 Johns Hopkins）；**[Hoffmann et al. 2022](https://arxiv.org/abs/2203.15556)**（"Training Compute-Optimal Large Language Models", arXiv:2203.15556, 22 人, Google DeepMind；后刊 NeurIPS 2022）；**[Pearce & Song 2024](https://arxiv.org/abs/2406.12907)**（"Reconciling Kaplan and Chinchilla Scaling Laws", arXiv:2406.12907, Pearce: Microsoft Research, Song: MIT；刊于 TMLR 2024）；[Lilian Weng, "Scaling Laws, Carefully"](https://lilianweng.github.io/posts/2026-06-24-scaling-laws/)（2026-06-24）；[BoxCars AI 三定律命名](https://blog.boxcars.ai/p/the-three-laws-driving-the-ai-revolution)（Tabrez Syed, 2024-09-19）。

### 想法 3 · 手机侧：节奏与消费

- **[Corrocher & Paganuzzi 2025, Telecommunications Policy](https://doi.org/10.1016/j.telpol.2025.103022)**——"Planned obsolescence and smartphone replacement: Empirical evidence on the Italian market." 49(8): Article 103022（两人均 Bocconi University；在线 2025-07-08）。
- **[Smart Analytics Global: Can Apple Upgrade Leasing Program Shorten the U.S. Smartphone Replacement Cycle?](https://smartanalyticsglobal.com/apple-upgrade-hardware-as-a-service-us-smartphone-replacement-cycle/)**（2026-07-28，Linda Sui）——95% 新 iPhone 走月付、>80% 以旧换新、实际替换周期约 34 个月（三点逐字核实）。
- **[IMF WP/20/70](https://www.imf.org/en/publications/wp/issues/2020/05/29/global-smartphones-sales-may-have-peaked-49361)**——Mongardini, Joannes & Aneta Radzikinski. 2020-05. "Global Smartphone Sales May Have Peaked: What Next?" doi:10.5089/9781513545851.001.a001.

### 想法 4 · 主机对照与 VR 失败组

- **[Nieborg 2014, Eludamos](https://doi.org/10.7557/23.6155)**——"Prolonging the Magic: The political economy of the 7th generation console game." *Eludamos. Journal for Computer Game Culture* 8(1): 47–63。David B. Nieborg，发表时 University of Amsterdam / MIT 博士后（Toronto 是现任）。
- **[Kretschmer & Claussen 2016, Strategy Science](https://doi.org/10.1287/stsc.2015.0009)**——"Generational Transitions in Platform Markets—The Role of Backward Compatibility." 1(2): 90–104（LMU Munich）。**旧版挂的 DOI（stsc.2022.0177）是别人的论文**——那篇是 Cox, Crosby & McKenzie, "Don't Look Back? Backward Compatibility in the Video Gaming Industry," *Strategy Science* 8(3): 387–404 (2023)，可作补充文献单列。
- **[spacebar.news: Game consoles are now smartphones, and that's okay](https://www.spacebar.news/consoles-are-now-smartphones/)**（2024-09-12，Corbin Davenport）——mid-gen refresh（PS5 Pro）与手机逻辑融合。
- VR 失败组：**[vr.org: Reality Labs Lost $4.62 Billion in Q2…](https://vr.org/articles/meta-reality-labs-q2-2026-earnings-loss-widens-88-billion)**（2026-07-31，Sam Whitfield）——累计亏损约 $88B（自 2020 分部披露起）；**[CNBC: Meta's Reality Labs cuts sparked fears of a 'VR winter'](https://www.cnbc.com/2026/01/24/metas-reality-labs-cuts-sparked-fears-of-a-vr-winter.html)**（2026-01-24，Jonathan Vanian）——裁员约 1000 人；IDC：XR 头显 2025 出货 −42.8% 至 390 万、AI 眼镜 +211.2% 至 1060 万（正文的「降四成/增两倍」即此）；**[stratrix: Was Vision Pro Ever Aimed at Consumers?](https://www.stratrix.com/decision-forks/apple-vision-pro-a-3-500)**（2026-07-17）——"The headset wasn't the product. It was the cover charge"（开发者平台注读法）。

## 理论源（书目核验 + 概念归属）

- **Mann, Michael**（时在 London School of Economics）. 1984. "The Autonomous Power of the State: Its Origins, Mechanisms and Results." *European Journal of Sociology / Archives Européennes de Sociologie* 25(2): 185–213. doi:10.1017/S0003975600004239.——**「后勤性权力」的源头**：infrastructural power 的定义（p. 189）"the capacity of the state to actually penetrate civil society, and to implement **logistically** political decisions throughout the realm"。Cowen 2014 是物流谱系学的当代化研究；"logistical power" 是批判物流研究的领域通用词（Neilson 2013、Kanngieser & Labban 2018 等），并非 Cowen 专属概念。
- **Merton, Robert K.**（Columbia University）. 1948. "The Self-Fulfilling Prophecy." *The Antioch Review* 8(2): 193–210. doi:10.2307/4609267.——「自我实现预言」概念的提出处。
- **计划性报废概念链**：London, Bernard. 1932. *Ending the Depression Through Planned Obsolescence*. New York: 自出版小册子（[Gutenberg #72003](https://www.gutenberg.org/ebooks/72003)）→ Brooks Stevens 1954 年 Minneapolis 广告会议演讲使词流行，定义句："Instilling in the buyer the desire to own something a little newer, a little better, a little sooner than is necessary."（转引见 Adamson, Glen. 2003. *Industrial Strength Design: How Brooks Stevens Shaped Your World*. Cambridge, MA: The MIT Press）→ Packard 1960 大众化；完整谱系记载于 Slade 2006。
- Slade, **Giles**. 2006. *Made to Break: Technology and Obsolescence in America*. Cambridge, MA: Harvard University Press.（注意名是 Giles 非 Gilles）
- Packard, Vance. 1960. *The Waste Makers*. New York: David McKay Company.
- Cowen, **Deborah**. 2014. *The Deadly Life of Logistics: Mapping Violence in Global Trade*. Minneapolis: University of Minnesota Press.（注意是 Deborah Cowen，非 Tyler Cowen；副题按出版社官方页为 *Mapping Violence in Global Trade*）
- Tsing, Anna Lowenhaupt（UC Santa Cruz）. 2009-04. "Supply Chains and the Human Condition." *Rethinking Marxism* 21(2): 148–176. doi:10.1080/08935690902743088.
- Lipovetsky, Gilles. 1994. *The Empire of Fashion: Dressing Modern Democracy*. Trans. Catherine Porter. Princeton, NJ: Princeton University Press.（法文原著 1987）
- Porter, Theodore M.（UCLA）. 1995. *Trust in Numbers: The Pursuit of Objectivity in Science and Public Life*. Princeton, NJ: Princeton University Press.
- Dourish, Paul（UC Irvine）. 2017. *The Stuff of Bits: An Essay on the Materialities of Information*. Cambridge, MA: The MIT Press.

## 参考资料

（全部引用已内联于「想法 × 材料」并附链接，均经 2026-09-07 核验。本站相关：[018](../018-sota-spectacle/note.zh.md) / [019](../019-tokenmaxxing/note.zh.md) / [020](../020-ai-as-utility/note.zh.md) / [022](../022-gravity-of-models/note.zh.md)。）

## 核验记录（2026-09-07）

- 29 项引用 + 3 条金句全部追到实体，零死链（19 个直链批检全 200；ScienceDirect/IEEE 对脚本 403/202 反爬软墙，浏览器可达）。
- 已修正 3 处关键错误：①「我们让它成真，因为我们希望它成真」系 **Chris Mack** 的句子（2003/2011 三处皆其署名），非 Gordon Moore——Moore 实录为 "the industry made it a self-fulfilling prophesy"；②「act of will」金句不在 2003 SPIE PDF 内，正确出处是 Mack 2011（IEEE TSM 24(2):202–207）；③ Kretschmer & Claussen 旧挂 DOI 是 Cox 等 2023 的论文，正确 DOI 为 10.1287/stsc.2015.0009。
- 补全要素：Mollick 发表时单位 MIT Sloan；Lécuyer 全题含副标题、刊期 23(1):133–163（2022）；Nieborg 期刊 Eludamos 8(1):47–63；Corrocher & Paganuzzi 全题+Article 103022；IMF WP 标题与作者；Spectrum 印刷版题名 "The Node is Nonsense"；「铁轨」金句一手出处锁定 Korczynski 1997。
- **概念归属核验（2026-09-07 第二轮）**：「后勤性权力」源头 = **Michael Mann 1984**（infrastructural power,p.189 定义含 "implement logistically"）,Cowen 为当代化研究、副题更正为 *Mapping Violence in Global Trade*;自我实现预言 = **Merton 1948**（Antioch Review 8(2):193–210）;计划性报废 = **London 1932 → Stevens 1954**（Gutenberg #72003 与 Adamson 2003 已核）。ITRS「九百多家公司」不在 Mollick 2006(全文零命中),真实口径为 ITRS 2003 版 936 家参与公司（经 3D InCites 2015 访谈转引）,本中文矩阵未带该数字故不涉及。
