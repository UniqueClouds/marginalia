---
id:              marginalia-023
title:           "当 Nature 学会标题党：顶刊的媒体化与 taste 重定向"
date:            2026-09-06
published:       2026-09-06
kind:            research memo（研究备忘）
sources:
  - "Weingart, P. 2022. 'Trust or attention? Medialization of science revisited.' Public Understanding of Science. doi:10.1177/09636625211070888"
  - "Moorhead, Fleerackers & Maggio. 2023. '''It's my job''': a qualitative study of the mediatization of science.' JCOM 22(04)A05"
  - "Väliverronen, E. 2021. 'Mediatisation of science and the rise of promotional culture.' Routledge. doi:10.4324/9781003039242-8"
  - "Sumner et al. BMJ 2014（doi:10.1136/bmj.g7015）与 PLOS ONE 2016（doi:10.1371/journal.pone.0168217）；Vinkers et al. BMJ 2015（doi:10.1136/bmj.h6467）"
  - "Communications Psychology 2025, 'Scientific publications that use promotional language in the abstract receive more citations.' s44271-025-00293-8"
  - "Leidecker-Sandmann et al. PLOS ONE 2023（doi:10.1371/journal.pone.0280016）；Frontiers in Research Metrics & Analytics 2026（战略文本脱钩，frma.2026.1893522）"
  - "中文材料：腾讯新闻 CNS 发文榜系列（2025-09-27 等）；『中文 AI 三大顶会』社区调查（unifuncs.com/s/gr2npwic）"
initial-prompt: "把 Nature/Science 与量子位、机器之心做类比：科学期刊让自己的 taste 服从快速迭代的技术与想象中的受众，录取 topic 发生大量偏向，投稿随之偏向——一种非技术的、文化/商业消费层面的重定向。类似 popcorn 文化？xxxzation？"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           52
---

# 当 Nature 学会标题党：顶刊的媒体化与 taste 重定向

> 研究备忘：核心命题——顶刊正在让收稿品味（taste）服从「快速迭代的技术节奏」与「想象中的受众」，topic 分布随之偏向（LLM 化），投稿重定向；与自媒体构成媒介化连续谱。本条 = 想法提纲 + 核验材料 + 媒介化理论源卡片。旧版论证文见 git 历史。引用已于 2026-09-07 全量搜索核验，记录见文末。

## 核心想法

1. **反向证据（戏称的结构）**：自媒体被叫作「中文 AI 三大顶会」= 公众感知里顶刊与流量媒体在做同一件事；Hovy「LLM popcorn」+ 67% LLM 标题是英文侧对应物。
2. **理论总锚 = 科学的媒介化**：Weingart 1998 开山（science–media coupling）→ 2022 再访（imagined publics；参与脱轨为营销）；Väliverronen 补「推介文化」中层概念。
3. **期刊是主动一环**：Moorhead 等 2023——期刊压力（journal pressures）是科学家媒介化的三因素之一；顶刊一手包办 embargo/新闻稿/推广。
4. **taste 重定向有计量证据且呈正反馈**：宣传词 +1% → 引用 +9–14%（13.6 万摘要）；正面词 40 年 +880%；夸大主要来自大学与期刊自己的新闻稿（OR 6.5–56）且不带来更多新闻采用 = 「自适应但无效」。
5. **研究设计 = 三级转码链**：顶刊新闻稿 → 国际媒体 → 中文自媒体，测每级 hype 增幅；Leidecker-Sandmann 的 MSM≥100 框架可直接迁移；中文侧（CNS 榜、三大顶会话语）无人研究 = gap。

## 想法 × 材料

### 想法 1 · 反向证据

- **[腾讯新闻：西湖大学四天内连发 3 篇顶刊，实现 CNS 大满贯](https://news.qq.com/rain/a/20250927A00HI500)**（2025-09-27）——顶刊发文做成高校积分榜的样本。
- **[unifuncs: AI 三大顶会调查](https://unifuncs.com/s/gr2npwic)**——「中文 AI 三大顶会」（机器之心/量子位/新智元）戏称的聚合页。注意：此页是 AI 生成聚合（二手），原始锚是知乎问题「如何评价中文 AI 三大顶会：机器之心、量子位、新智元？」。
- Hovy「LLM popcorn」与 67%：一手记录见 **[018 想法 3](../018-sota-spectacle/note.zh.md)**（Gubelmann 逐字："LLM exhaustion and nausea (67% of Papers have ``LLM'' in title)"）。

### 想法 2 & 3 · 媒介化理论链（源卡片见下）

- Weingart 1998 / 2022；Moorhead, Fleerackers & Maggio 2023；Väliverronen 2021。

### 想法 4 · 计量证据

- **[Stavrova, Kleinberg, Evans & Ivanović 2025, Communications Psychology](https://www.nature.com/articles/s44271-025-00293-8)**——136,615 篇摘要（1991–2023；PNAS 84,603 / Science 25,142 / Nature 26,870）：宣传词 +1%（约 2 词）→ 年引用 +9–14%、Altmetric +3–6%（139 词词典）。作者单位：Stavrova（Lübeck/Tilburg）、Kleinberg（UCL）、Evans（Allstate）、Ivanović（Ipsos）。可补：性别差异发现（宣传语言扩大男性作者引用优势）。
- **[Vinkers, Tijdink & Otte 2015, BMJ](https://doi.org/10.1136/bmj.h6467)**——PubMed 摘要正面词 2.0%（1974–80）→ 17.5%（2014），相对 +880%；「robust」「novel」「innovative」「unprecedented」相对频率最高 +15,000%（约 150 倍）。单位：UMC Utrecht / VU Medical Center Amsterdam。
- **[Sumner et al. 2014, BMJ](https://doi.org/10.1136/bmj.g7015)**——12 人（Cardiff University 为主；Venetis 在 Wollongong、Boy 在 Swansea Swansea University 通讯）：夸大主要来源是大学新闻稿，OR 6.5（建议类）/ 20（因果类）/ 56（动物推人类）；且夸大不增加新闻采用。姊妹篇：[Sumner et al. 2016, PLOS ONE](https://doi.org/10.1371/journal.pone.0168217)（期刊新闻稿 OR 2.4–11；caveats 不降低采用率）——OR 6.5–56 属 2014 BMJ 篇，引用时分开。
- **[Wang & Sun 2026, Frontiers in Research Metrics and Analytics](https://www.frontiersin.org/journals/research-metrics-and-analytics/articles/10.3389/frma.2026.1893522/full)**——"Strategic decoupling between grant and publication language in AI and cancer research: a cross-national LLM-assisted analysis"（华南农业大学生命科学学院；400 对 NSFC/NIH-NSF 摘要对；AI r=0.78、癌免 r=0.56；提出 strategic textual decoupling 与 hidden cognitive tax）。

### 想法 5 · 研究设计模板

- **[Leidecker-Sandmann, Koppers & Lehmkuhl 2023, PLOS ONE](https://doi.org/10.1371/journal.pone.0280016)**——"Correlations between the selection of topics by news media and scientific journals"（KIT / Science Media Center Germany）：Altmetric MSM≥100 筛 983 篇高曝光论文，链接 185,166 篇同主题 PubMed 文献；59% 案例报道后同主题发文增多（p<0.01）；publicity effect vs earmark hypothesis 无法区分——框架可迁移为「LLM 选题重定向」检验。

## 理论源卡片

### Weingart · 媒介化两篇

**1998 开山**：Peter Weingart（Bielefeld University；2015–2020 兼 Stellenbosch 大学南非科学传播讲席）. 1998-12. "Science and the media." *Research Policy* 27(8): 869–879. doi:10.1016/S0048-7333(98)00096-1
- 摘要原文："The traditional view of the popularization of science…is being challenged in the new arrangement between science and the media."
- 三个标志案例（摘要原文）："pre-publication of results in the media, the role of media prominence in relation to scientific reputation, and the cassandra syndrome…"（同行评审前先见媒体 / 媒体可见度兑换声望 / 为注意力发动灾难话语）
- 不可逆判断："The coupling with its problematic consequences seems inescapable given the increased dependency on public support…"

**2022 再访**：Peter Weingart. 2022-04-01. "Trust or attention? Medialization of science revisited." *Public Understanding of Science* 31(3): 288–296. doi:10.1177/09636625211070888
- "A closer look reveals the self-referentiality of institutional communication deriving its rationale from 'imagined publics'."
- "The politically sponsored 'engagement of the public' has been derailed to become marketing, branding and public relations exercises."
- 后果："…conflicts between faculty and management and possibly a loss of trust in science."（标题之问：换来 attention，押上 trust）

### Moorhead, Fleerackers & Maggio 2023 · 期刊压力

**引用**：Laura L. Moorhead（San Francisco State University）、Alice Fleerackers（Simon Fraser University，当时）、Lauren A. Maggio（Uniformed Services University of the Health Sciences）。2023-08-07. "'It's my job': a qualitative study of the mediatization of science within the scientist-journalist relationship." *Journal of Science Communication (JCOM)* 22(04): A05. doi:10.22323/2.22040205.（[PDF](https://jcom.sissa.it/article/1266/galley/2693/download/)）

**大纲**：
1. 原命题是 journal pressures 为三因素之一（career status / journal pressures / institutional context）："The need to please journals was an important force shaping scientists' interactions with journalists."
2. 受访者原话（Sci_10，逐字）："I was at, you know, a big R1 university, and the culture was sort of if your paper wasn't in Science or Nature — or maybe PNAS — like, you did not tell the press department. Like, they only cared about high-impact articles."（「期刊自身也有媒介化」是本词条的引申读法，原文未以此命题）
3. "journals directly shaped scientists' interactions with journalists by setting embargoes, preparing and publicizing press releases, and promoting new studies. Again, 'high impact' journals appeared to play an outsized role."
4. 方法：19 位科学家访谈（取自 8 家媒体 400 篇报道提及的研究）；在 Olesk (2021) 框架上新增第三模式 affiliation of media logic；四类 persona（Constrained Communicator / Ambivalent Media Source / Strategist / Media Enthusiast）。

### Väliverronen 2021 · 推介文化

**引用**：Esa Väliverronen（University of Helsinki）. 2021-02-28. "Mediatisation of science and the rise of promotional culture." Chapter 8 in *Routledge Handbook of Public Communication of Science and Technology*, 3rd ed., eds. Massimiano Bucchi & Brian Trench. Abingdon: Routledge. ISBN 9781003039242. **doi:10.4324/9781003039242-8-8**（旧版 DOI 末尾少「-8」，未注册）。OA：[Taylor & Francis](https://www.taylorfrancis.com/chapters/oa-edit/10.4324/9781003039242-8/mediatisation-science-rise-promotional-culture-esa-v%C3%A4liverronen)、[OAPEN](https://library.oapen.org/handle/20.500.12657/49683)
- 核心论证："from 'publish or perish' to 'promote yourself or perish'"（引 Wernick 1991、Davis 2013）。

## 参考资料

（全部引用已内联于上并附链接，均经 2026-09-07 核验。命名资源：mediatization / tabloidization / heteronomization / popcornization；Bourdieu 异治极接 [009 · Homologies](../009-homology-without-fractal/note.zh.md)；评审侧接 [021 · Best Paper 的随机性](../021-best-paper-lottery/note.zh.md)。）

## 核验记录（2026-09-07）

- 12/12 项实存且内容属实，0 编造。
- 已修正 4 处：Väliverronen DOI 改为 10.4324/9781003039242-8-8（旧 DOI 未注册）并补书名编者；Moorhead 受访者原话按英文逐字更正（含 "— or maybe PNAS —"）；Sumner 团队单位 Cardiff（非 Exeter）；OR 6.5–56 归属 2014 BMJ 篇。
- 补入：Weingart 1998（Research Policy 27(8):869–879）、JCOM DOI、Comms Psych 四作者全名+单位、Frontiers 作者与机构背景。
- 访问注意：SAGE 对 curl 反爬（DOI 正常解析）；unifuncs 为 AI 聚合页（二手，原始锚为知乎问题）。
