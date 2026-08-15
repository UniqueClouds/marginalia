# Human-Computer Interaction（CHI/CSCW）学科论文的语言风格分析
**——基于 Zotero「各学科 Classic Papers / Human Computer Interaction」子库 94 篇原文的语料库分析（2003–2025）**

---

## 0. 语料与方法

### 0.1 语料来源
Zotero 库「各学科 Classic Papers → Human Computer Interaction」子库共 96 个条目，94 篇入语料（2 篇 PDF 为纯中文翻译版剔除：Capel & Brereton 2023 HCAI 地图、Stack Overflow vs ChatGPT 一文；另剔除水印/目录段落）。**94 篇、81.8 万词，四学科中规模第二**。

| 维度 | 数值 |
|---|---|
| 论文数 / 词数 | 94 篇 / 817,868 词 |
| 主要来源 | CHI（约 70 篇）、CSCW/PACMHCI、UbiComp/TOCHI 等 ACM 系 |
| 年份跨度 | 2003–2025（近六成集中在 2015–2023） |
| 篇均长度 | 8,701 词 |
| 引用样式 | 数字方括号 [n]：90.1 次/万词，**94/94 篇全部使用**；author-date 仅 0.5 次/万词 |

内容构成：经典实证 HCI（打字、中断、邮件、多任务）+ 批判/理论 HCI（Feminist HCI、Postcolonial Computing、Critical Race Theory for HCI、probes 系列）+ 2018 年后的 AI/HCAI 浪潮（data cascades、explainability、GAI 协作）。这条"实证—批判—AI"的内部光谱本身就是报告的重要背景：**HCI 语料是四学科中内部风格方差最大的**。

### 0.2 分析方法
同 Dourish 管线：版面块段落提取 → 清洗 → 词频/n-gram/keyness（vs 其余三学科）→ 修辞动块统计 → 精读归类 → 引文脚本核验。

---

## 1. 总体节奏：中庸句长 + 高频段落实换

| 指标 | HCI | 四学科排位 |
|---|---|---|
| 平均句长 | 23.7 词 | 第 2 |
| 句长 P50 / P90 | 20 / 39 | 中 |
| 长句占比（>30 词） | 23.0% | 第 2 |
| 短句占比（<10 词） | 16.0% | 第 2 低 |
| 段落中位长度 | 91 词 | **最短**（SOC 139、BDS 165；部分系 CHI 双栏版式切分，但短段落也是真实文风） |

HCI 的节奏感来自**段落切换频率**而非句子内部：引言立 scene → 相关工作铺陈 → 方法逐小节 → 发现逐条 → discussion 升华，标准 CHI 模板把文章切成很碎的节。句长居中：它比 SE 讲究铺陈（引用堆叠、从句），但没有 BDS 的理论长句负担。

## 2. 人称与语态：最热闹的"我们"

| 指标 | HCI | BDS | SOC | SE |
|---|---|---|---|---|
| we /万词 | 91.5 | 37.8 | 52.2 | 103.0 |
| our /万词 | 34.4 | 13.4 | 18.1 | 40.5 |
| I /万词 | 16.8* | 11.6 | 15.8 | 8.8 |
| be+V-ed 被动式 /万词 | 72.1 | 83.5 | 64.7 | 82.2 |

*I 的高频有相当部分来自**访谈引语**——HCI 大量直接引用参与者原话（"I always assumed that I wasn't really that close to [her]" 直接进了标题）。

- "This paper" 自指 **82/94 篇**（"this article" 仅 5 篇）——会议文体指纹。
- "we" + 动词的搭配表勾勒出全部研究动作：**we found (218) > we used (134) > we conducted (100) > we present (85) > we describe (64) ≈ we argue (64) > we observe (48) > we report (47)**。注意 we argue 与 we found 几乎并驾齐驱——实证与论证双轮驱动是 HCI 区别于纯 SE 的特征。

## 3. 词汇场与引用谱系

### 3.1 概念词汇场（keyness vs 其余三学科）
HCI 独有词场极为清晰：**human-AI / human-centered (127/M) / XAI (202/M) / high-stakes / LLM / prompt / sensemaking / data cascades / folk theories / trust & reliance / cognitive load**；老一批经典则贡献 **probes (319/M，几乎独有)、affordances (3.5/万词，四学科最高)、seamful、inspirational bits、empathy、experience**。批判支线的词场与 BDS 高度重叠：feminism (117/M)、intersectionality、critical design、misgendering、postcolonial——"critique/critical" 出现于 69/94 篇，密度 6.5/万词与 BDS (7.0) 几乎持平，这解释了为什么 Dourish 会被两边同时引用。

### 3.2 引用谱系（人名 keyness）
**Gaver、Sengers、Bardzell & Bardzell、Stolterman、Dourish、Suchman 谱系（Harrison/Tatar/ Sengers 的 meta 常客）、Irani、Ehsan、Bansal（HITL-AI）、Weisz、Liao、Sambasivan**。HCI 的谱系是"设计研究 + 批判理论 + 认知科学"三线并存：引 Hutchinson 与引 Heidegger 的可能是同一篇文章。

引用格式上 ACM 数字引用 [44] 高密度内嵌，造成 HCI 正文里**每句话都可能挂 1–3 个方括号**——"文献堆叠句"成为其视觉签名：

> "A substantial body of research in human-computer interaction has focused on interruption and attention management on the computer [1, 3, 4, 6, 8, 9, 13, 14, 16, 18]."
> —— Jin & Dabbish (2009), *Self-interruption on the computer*, Introduction

## 4. 高频短语与签名句式

| 模式 | HCI（次/万词） | 排位 |
|---|---|---|
| hedge: may / might / suggest | **16.6 / 7.6 / 8.8** | 三项全部四学科第一 |
| not simply...but | 1.5 | 第 2（BDS 2.9） |
| rather than | 3.5 | 第 2 |
| 存在句 there is/are | 10.0 | 与 SOC/SE 持平 |
| p< 检验报告 | 5.4 | **第一**（SE 1.5、SOC 1.4） |

- **模糊限制语全学科最密**（may/might/suggest 三项第一）：HCI 的知识主张永远留有余地——"may help"、"suggests that"，因为它的证据是 12–30 人的用户研究，而它的话语对象是要据此做设计的社群。
- **"In this paper, we present..." 是全库最高频的论文开场公式**（"In this paper" 193 次于 71 篇；"we present" 34/94 篇）。摘要第一句直接报菜名：

> "We present the notion of 'bridging concepts' as a particular form of intermediary knowledge in HCI research, residing between theory and practice. We argue that bridging concepts address the challenge of facilitating exchange between theory and practice in HCI..."
> —— Dalsgaard & Dindler (2011), *Between theory and practice: bridging concepts in HCI research*, Abstract

> "We present a qualitative study of mobile communication via WeChat in Southern China, focusing on the rapid proliferation of emoji and stickers and the lessening dependence on text."
> —— Zhou, Hentschel & Kumar (2017), *Goodbye text, hello emoji*, Abstract

## 5. 修辞动块：CHI 论文的仪式清单

### 5.1 "revisit" 姿态：对经典温柔造反
HCI 实证文爱用 revisit / revisit-the-present-understanding 框架，把新数据放进老问题：

> "This paper revisits the present understanding of typing, which originates mostly from studies of trained typists using the ten-finger touch typing system. Our goal is to characterise the majority of present-day users who are untrained and employ diverse, self-taught techniques."
> —— Feit, Weir & Oulasvirta (2016), *How We Type*, Abstract

> "We are concerned that the current understanding mostly originates from an era when typing was much more homogenous than today."
> —— 同文, Introduction

### 5.2 参与者与伦理的仪式化细节
HCI 对"人"的登记是四学科中最细的：招募渠道、报酬金额、母语、利手都有：

> "We recruited participants through a combination of developer communities, distribution lists, professional networks, and personal contacts, using snowball and purposive sampling [89] that was iterative until saturation."
> —— Sambasivan et al. (2021), *"everyone wants to do the model work, not the data work"*, §Method

> "Each participant received a thank you gift in the form of a gift card, with amounts localised in consultation with regional experts (100 USD for the US, 27 USD for India, 35 USD for East and West African countries)."
> —— 同文（注意：连报酬的"区域公平性"都要交代——这是 CHI 伦理审查文化的语言痕迹）

量化上：participants/subjects 合计 24.7 次/万词，四学科第一；"we recruited / IRB / informed consent / compensation" 动块 14+ 篇高频出现。SE 论文也做访谈，但极少这样逐项登记"人"的属性。

### 5.3 三角验证叙事（triangulation narration）
"先访谈、再问卷、再部署"的顺序句法：

> "Second, we conducted a survey to triangulate our interview and field study results. Within the survey, we asked participants in a short text response if there were any pain points we had missed: no new pain points were identified through these responses."
> —— Chattopadhyay et al. (2020), *What's Wrong with Computational Notebooks?*

### 5.4 "Design implications" 作为贡献出口
实证发现必须折算成对设计者的建议，这是 HCI 独有的贡献货币（design implications 13/94 篇、implications for design 5/94 篇，其他学科近乎为零）：

> "Yet one of the most valorized outcomes of scientific research in HCI is its implications for design. But design is an intervention, an intentional effort to create change."
> —— Bardzell & Bardzell (2011), *Towards a feminist HCI methodology*（批判支线则反过来审视这个格式本身）

### 5.5 开场钩子：新闻语 / 参与者语录 / 反问
- 新闻钩子：WeChat 论文以 Emojicon 新闻稿开篇（"Emoji-mania is in full force..."）再引出研究问题；
- 参与者语录直接做标题：*"everyone wants to do the model work, not the data work"*、*"I always assumed that I wasn't really that close to [her]"*、*"'It's Reducing a Human Being to a Percentage'"*；
- 问题驱动开场："We need to better understand the phenomenon of self-interruption, because it is a driver of multitasking behavior and contributor to fragmented attention."（Dabbish et al. 2011）

## 6. 标题风格：四学科最会玩标题的

| 特征 | 比例（n=96） | 四学科对比 |
|---|---|---|
| 含冒号 | 55% | 次高 |
| **带引号** | **19%** | **第一** |
| **疑问/How-Why 开头** | **24%** | 第一（4% 完整问句 + 20% how/why/what 开头） |
| >10 词 | 52% | 次长 |
| 动词/分词开头 | 14% | 中 |

样例即可见其文娱精神：
- **文学戏仿/俗语改写**：*Why Johnny Can't Prompt*（2023）；*Old wine in new bottles or novel challenges*（2011）；*He says, she says*（2007）；*If not now, when?*（2004）
- **交错配列**：*Goodbye text, hello emoji*（2017）；*Is seeing believing?*（Cosley et al.）；*Gender Recognition or Gender Reductionism?*（2018）
- **第一人称自白**：*Am I wasting my time organizing email?*；*I did that!*；*Why do I keep interrupting myself?*；*First I "like" it, then I hide it*
- **参与者原话**：*"everyone wants to do the model work, not the data work"*
- 大词自问：*What is interaction?*（Hornbæk & Oulasvirta 2017）；*What is "critical" about critical design?*；*What is Human-Centered about Human-Centered AI?*

CHI 标题允许出现任何其他工科会议都会毙掉的东西：第一人称、感叹号、双关、参与者脏话级别的口语。标题是 CHI 论文的"第二摘要"，兼做情绪动员。

## 7. 风格画像总结

**HCI 的声音：一个兴奋的工坊主持人。** "We" 密度极高（91.5/万词）且动词丰富（found/conducted/present/describe/argue）；摘要以 "We present..." 开门见山；证据永远是"我们做了什么"的流水叙事 + 三角验证；对参与者的登记细致到报酬与利手；hedges 三项全学科第一（对小样本永远诚实）；p 值与引语并陈，统计和故事各占一半；发现必须折算成 design implications；标题敢用第一人称、引号和俗语。内部同时存在一条批判支线（Bardzell/Irani/Keyes/Dourish 系），其词场与句式（not X but Y、scare quotes）直接继承自 BDS 风格家族。

**若要模仿该文体（写作配方）**：
1. 摘要第一句："We present/describe a study of X..."；正文自指一律 "this paper"；
2. 方法节按"参与者→程序→分析"分小节，逐项交代 N、招募渠道、报酬、伦理审查；
3. 发现用 "We found that... (P1)" + 参与者原话双轨呈现，引语保真不清洗；
4. 每个强主张配一个 hedge（may/suggest），每个统计结论给出 p 值；
5. Discussion 末尾必设 "Design Implications" 小节，把发现翻译给设计者；
6. 标题冒号前放一个钩子（问句/引语/俗语改写），冒号后放研究内容；
7. 引用用 [n] 数字堆叠；相关工作节按主题分组而非逐篇罗列。

---

## 附录 A：局限说明
1. 2 篇仅有中文翻译版 PDF（HCAI 地图 2023、SO vs ChatGPT 2023）已剔除；Zotero 条目仍在库中。
2. CHI 双栏版式使段落统计偏碎（中位 91 词含切分伪差），句子级指标不受影响。
3. 子库内部异质性大（经典实证 vs 批判理论 vs HCAI），本文按主流趋势概括，批判支线单独标注。
4. 水印（ACM 版权页）、卷首作者地址块已过滤；连字丢失已归并。

## 附录 B：语料构成（94 篇节选代表 + 分布）
- 经典实证：Adamczyk & Bailey 2004（中断时机）；Jin & Dabbish 2009（自我中断）；Mark, Gudith & Klocke 2008（中断代价）；Feit et al. 2016（How We Type）；Whittaker et al. 2011（email refinding）；Kittur et al.（Wikipedia×2、Mechanical Turk×2）
- 批判/理论：Bardzell 2010（Feminist HCI）；Bardzell & Bardzell 2011（feminist methodology）+ 2012（critical design）；Irani et al. 2010（postcolonial）；Irani & Silberman 2013（Turkopticon）；Boehner et al. 2007（probes）；Hornbæk & Oulasvirta 2017（What is interaction?）；Ogbonnaya-Ogburu et al. 2020（CRT for HCI）；Keyes 2018（Misgendering Machines）
- 社计算/GAM：Burke, Kraut & Marlow 2011；Bernstein et al. 2013；Eslami et al. 2015/2016（folk theories）；Starbird et al. 2018（disinformation as work）
- AI/HCAI 浪潮：Amershi et al. 2019（Guidelines）；Sambasivan et al. 2021（data cascades）；Bansal et al. 2021；Buçinca et al. 2021；Ehsan et al. 2021；Chen et al. 2023；Zamfirescu-Pereira et al. 2023（Why Johnny Can't Prompt）
（完整 94 篇键值、年份、词数见 `discipline_style_analysis/corpus_meta.json`。）
