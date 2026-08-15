# Big Data & Society 学科论文的语言风格分析
**——基于 Zotero「各学科 Classic Papers / Big Data & Society」子库 27 篇原文的语料库分析（2004–2021）**

---

## 0. 语料与方法

### 0.1 语料来源
Zotero 库「各学科 Classic Papers → Big Data & Society」子库共 30 个条目，其中 29 篇有 PDF。剔除 1 篇无 PDF（Gillespie "The politics of 'platforms'"，正文分析以库内其余论文为准）、剔除 1 部专著（Keen《The cult of the amateur》，文体不一致）、剔除中文翻译段落（Burrell、Kitchin 等多篇 PDF 内附中文摘要/全文对照版），**最终可用 27 篇期刊论文、21.2 万词**。

| 维度 | 数值 |
|---|---|
| 论文数 / 词数 | 27 篇 / 211,858 词 |
| 主要来源 | *Big Data & Society* 16 篇、*New Media & Society* 10 篇 |
| 年份跨度 | 2004–2021（75% 集中在 2010s） |
| 篇均长度 | 7,847 词（四学科中最短） |
| 作者-年份引用 | 27/27 篇（36.0 次/万词，四学科最高） |

代表篇目：Burrell《How the machine 'thinks'》、Kitchin《Big Data, new epistemologies and paradigm shifts》与《What makes Big Data, Big Data?》（Kitchin & McArdle）、Iliadis & Russo《Critical data studies: An introduction》、Lyon《Surveillance, Snowden, and Big Data》、Seaver《Algorithms as culture》、Leonelli《What difference does quantity make?》、Sadowski《When data is capital》、Mittelstadt et al.《The ethics of algorithms》、Burrows & Savage《After the crisis?》、Ananny & Crawford《Seeing without knowing》、Plantin et al.《Infrastructure studies meet platform studies》以及 digital divide 系列（Selwyn 2004; Van Deursen & Van Dijk 2014）。

### 0.2 分析方法
与 Dourish 分析同一套管线：PyMuPDF 版面块提取段落 → 去参考文献/水印/中文段 → 词频与 n-gram（含文档频率）→ 对数比值 keyness（本学科 vs 其余三学科联合语料）→ 修辞动块正则统计 → 人工精读归类。所有引文经脚本归一化核验。

---

## 1. 总体节奏：长句、重分号、零缩写

| 指标 | BDS | 四学科排位 |
|---|---|---|
| 平均句长 | **26.8 词** | 第 1（HCI 23.7 / SOC 23.6 / SE 18.8） |
| 长句占比（>30 词） | **33.1%** | 第 1（SE 仅 15.3%） |
| 短句占比（<10 词） | 17.4% | 最低 |
| 句长 P50 / P90 | 20 / 44 词 | P90 四学科最长 |
| 分号 /万词 | **46.3** | 并列第 1（与 SOC 44.2 同档；SE 23.3） |
| 破折号 /万词 | 16.8 | 中 |
| 缩写词（don't 等） | **0.0** | 四学科唯一为零 |

**第一个结论：这是四学科中节奏最"重"的文体**——句子最长、分号最密、完全拒绝口语缩写。Sage 期刊的书面语规范加上批判理论的从句嵌套习惯，造成一种"每句话都在背负论点重量"的散文质感。对比之下社会学虽同样爱分号，但它允许缩写词（7.4/万词）；BDS 一篇里连一个 "don't" 都找不到。

## 2. 人称与语态：第三人称化的批判者

| 指标 | BDS | HCI | SOC | SE |
|---|---|---|---|---|
| we /万词 | 37.8 | 91.5 | 52.2 | 103.0 |
| I /万词 | 11.6 | 16.8 | 15.8 | 8.8 |
| the authors /万词 | 0.9 | 1.8 | 0.7 | 1.5 |
| be+V-ed 被动式 /万词 | **83.5** | 72.1 | 64.7 | 82.2 |

- **we 频率四学科最低**（37.8/万词，不到 SE 的一半）。文章多以 "This article..." 为主语自我指涉（21/27 篇出现 "this article"，而 "this paper" 仅 8/27 篇——期刊文体的直接指纹）。
- 但**第一人称单数 "I" 不低**（11.6/万词，仅次于 HCI）：独著论文里批判学者惯用 "In this article, I draw a distinction..."（Burrell）这样的第一人称直接亮相——"我"在场，"我们"缺席，因为这里没有实验室、没有团队作业可以归属。
- **被动语态四学科最高**（83.5/万词）。「Opacity is produced by...」「decisions...are increasingly delegated to algorithms」——施动者被悬置，正是批判分析的句法对应物：机制无名地运行，这正是论文要揭露的东西。

## 3. 词汇场与引用谱系（keyness，vs 其余三学科）

### 3.1 概念词汇场
高关键性词几乎构成一部批判数据研究词典：**opacity（349/百万词，其他学科≈0）、surveillance（918/M）、transparency、datafication、assemblage、epistemology（2.3/万词，四学科最高）、algorithmic、platform(s)、data justice、neoliberalism、extraction**。

语域标签词（moves 统计）：critique/critical 出现于 **21/27 篇**（7.0/万词，四学科最高）；power 出现于 **25/27 篇**（6.3/万词，最高）；inequality、discrimination、ethics、surveillance 构成第二梯队。**"increasingly"（3.6/万词）是其他学科的 2–7 倍**——"X is increasingly delegated to algorithms" 这种进行时式的现代性焦虑是 BDS 最独特的时间副词症候：

> "decisions and choices previously left to humans are increasingly delegated to algorithms, which may advise, if not decide, about how data should be interpreted and what actions should be taken as a result."
> —— Mittelstadt, Allo, Taddeo, Wachter & Floridi (2016), *The ethics of algorithms: Mapping the debate*, Introduction

### 3.2 引用谱系（人名 keyness）
被引最多的思想来源是：**Kitchin、Cukier、Pasquale、boyd/crawford（Hidden Biases）、Leonelli、Floridi、Gitelman（"Raw Data Are an Oxymoron"）、Gillespie、Nissenbaum、Benkler、Andrejevic、Lyon、Snowden（事件本身成为被引对象）**。谱系横跨 STS、传播学、法 学与社会学，几乎不引统计方法论文献——与 SOC 形成鲜明对照。

引用风格：author-date 括注 36.0 次/万词（四学科第一）；**et al. 23.1 次/万词（四学科第一，SOC 仅 6.4）**——典型的"理论拉扯"写法：一个句子里并置三四位学者再逐一回应。

## 4. 高频短语与签名句式

### 4.1 否定—重述骨架："not simply X, but Y"
| 模式 | BDS（次/万词） | HCI | SOC | SE |
|---|---|---|---|---|
| not simply/just/only/merely...but | **2.9** | 1.5 | 1.6 | 0.8 |
| rather than | **5.1** | 3.5 | 3.3 | 2.0 |
| but rather | **1.1** | 0.6 | 0.5 | 0.2 |

三种否定—重述句式**全部居四学科之首**（约每 120 词一次）。这是批判文体的核心引擎：先复述主流理解（数据是客观的 / 算法是中立的 / 平台是中性的），再以 not...but / rather 重述之：

> "Rather than treat Big Data as only scientifically empirical and therefore largely neutral phenomena, CDS advocates the view that Big Data should be seen as always-already constituted within wider data assemblages."
> —— Iliadis & Russo (2016), *Critical data studies: An introduction*, Abstract

> "These are challenges not just of reading and comprehending code, but being able to understand the algorithm in action, operating on data..."
> —— Burrell (2016), *How the machine 'thinks'*, 论代码规模造成的 opacity

> "data is not a substitute for money, but is rather elevated and put 'on the same level as financial capital'"
> —— Sadowski (2019), *When data is capital: Datafication, accumulation, and extraction*（转引 Oracle & MIT Technology Review 报告）

### 4.2 概念劳动短语
"the cultural work of X""the politics of X""the social life of X" 这类**把抽象名词变成动词性偏正结构**的标题/短语公式在本库高频复现（标题层面见 §6）。词汇上：assemblage（5/27 篇，四学科几乎独有）、always-already、rendered visible/invisible、enacted、performativity、datafication。

### 4.3 三分法枚举
批判学者爱在摘要里给出编号分类学，把混乱现象一刀切成三：

> "In this article, I draw a distinction between three forms of opacity: (1) opacity as intentional corporate or state secrecy, (2) opacity as technical illiteracy, and (3) an opacity that arises from the intrinsic characteristics of machine learning algorithms..."
> —— Burrell (2016), *How the machine 'thinks'*, Abstract

（Kitchin 的 Big Data 特征清单——volume/velocity/variety/veracity——是同一动作的另一形态。）

## 5. 修辞动块：开篇、概念、呼吁

### 5.1 宣言式开头（manifesto openings）
不铺垫文献，第一句直接下断言，是本库最显眼的签名：

> "Data are a form of power."
> —— Iliadis & Russo (2016), *Critical data studies: An introduction*, Introduction 首句

> "This article considers the issue of opacity as a problem for socially consequential mechanisms of classification and ranking..."
> —— Burrell (2016), *How the machine 'thinks'*, Abstract 首句

### 5.2 现实事件钩子（news hook）
Snowden 泄密、剑桥分析、单条推文疯传——时事作为论文引擎：

> "The Snowden revelations about National Security Agency surveillance, starting in 2013, along with the ambiguous complicity of internet companies and the international controversies that followed provide a perfect segue into contemporary conundrums of surveillance and Big Data."
> —— Lyon (2014), *Surveillance, Snowden, and Big Data*, Abstract

### 5.3 田野场景开场（ethnographic scene-setting）
Seaver 用会议提问的戏剧化场景开启方法论论文，然后安一个自嘲式小节标题 "Terminological anxiety"：

> "At a conference on the social study of algorithms in 2013, a senior scholar stepped up to the audience microphone: 'With all this talk about algorithms,' he said, 'I haven't heard anybody talk about an actual algorithm. Bubble sort, anyone?'"
> —— Seaver (2017), *Algorithms as culture*, 开篇 "Terminological anxiety" 节

（对照：Dourish 的轶事开场传统在批判数据研究里被完整继承。）

### 5.4 对计算机科学的规训性呼吁
结论段惯用 "we need / there is a need to / calls for"，向（计算）学科喊话。epistemology 一词 9/27 篇在用——为数据科学"补认识论课"是这批论文的共同自我任务：

> "just as data are not generated free from theory, neither can they simply speak for themselves free of human bias or framing. As Gould (1981: 166) notes, 'inanimate data can never speak for themselves, and we always bring to bear some conceptual framework...'"
> —— Kitchin (2014), *Big Data, new epistemologies and paradigm shifts*, 论 data-driven empiricism

### 5.5 卷首引语（epigraph）
Kitchin 摘要前直接排一句 "Revolutions in science have often been preceded by revolutions in measurement. — Sinan Aral (cited in Cukier, 2010)"——格言式 epigraph 是 Sage 批判刊物的装饰语法（对照：ACM 会议论文完全没有这一格式空间）。

## 6. 标题风格：概念杠杆 + 冒号副标题

| 特征 | 比例（n=30） | 四学科对比 |
|---|---|---|
| 含冒号 | **63%** | 最高（SE 仅 30%） |
| >10 词 | **60%** | 最长 |
| 直接疑问句 | 0% | 唯一为零 |
| 动词/分词开头 | 23% | 最高 |
| 带引号 | 17% | 次高 |
| 篇首 The/A/An | 20% | — |

两大公式：
1. **"The X of Y" 概念杠杆**：*The politics of 'platforms'*、*The ethics of algorithms: Mapping the debate*、*The cultural work of microwork*、*The agenda-setting power of fake news*——把日常物翻译成政治/文化分析对象，标题本身就是"概念化"动作。
2. **引用口语做副标题**：*How the machine 'thinks'*、*'This is why we can't have nice things'*——把民间话语加引号后并入分析，制造批判距离。

## 7. 风格画像总结

**Big Data & Society 的声音：一个写长句的公共知识分子。** 句子最长、分号最密、零缩写；以 "This article" 而非 "we" 自我指涉，却允许批判学者以 "I" 亲自下场；被动语态最多；否定—重述句式（not X but Y / rather than）密度四学科第一；词汇场由 opacity/surveillance/power/critique/assemblage 构成；以宣言断言或时事钩子开场，以对学科的规训性呼吁收尾；标题爱用 "The X of Y" 概念杠杆和最长冒号副标题。

**若要模仿该文体（写作配方）**：
1. 开篇下断言："Data are a form of power."，不写 "In recent years, researchers have become interested in..."；
2. 主语用 "This article"，独著可 "I"；被动句悬置施动者；
3. 每个论点做一次 not...but / rather than 重述；关键概念放进 scare quotes（26 次/万词的弯引号密度）；
4. 摘要里给一个编号三分法；引言挂一条格言 epigraph 或一条时事钩子；
5. 引用并回应学者时用 author-date 密集括注 + et al.；长句用分号缝合，永不用缩写；
6. 标题用 "The X of Y: 动名词短语" 结构。

---

## 附录 A：局限说明
1. 1 篇（Gillespie 2010）无 PDF 未入语料；Gillespie 本人作为被引对象仍高频出现。
2. 部分论文 PDF 附中文对照全文（如 Burrell 2016），已按 CJK 字符占比剔除中文段落（详见管线 05_cjk_clean.py 日志）。
3. 词频统计含少量 Sage/JSTOR 水印噪声，已过滤；OCR 错误（fi 连字丢失）已按映射表归并。
4. 本库 27 篇均为期刊论文，规模小于其他三科，docfreq 分母较小，篇数指标解读需谨慎。

## 附录 B：语料清单（27 篇入语料，按年份）
Selwyn 2004；Wright & Street 2007；Burrows & Savage 2014；Kitchin 2014；Leonelli 2014；Lyon 2014；Van Deursen & Van Dijk 2014；Irani 2015；Hogan 2015；Burrell 2016；Iliadis & Russo 2016；Kitchin & McArdle 2016；Metcalf & Crawford 2016；Mittelstadt, Allo, Taddeo, Wachter & Floridi 2016；Seaver 2017；Taylor 2017；Ananny & Crawford 2018；Cunningham 2018；Fardouly, Willburger & Vartanian 2018；Felzmann et al. 2018；Kleis Nielsen & Ganter 2018；Lee 2018；Plantin, Lagoze, Edwards & Sandvig 2018；Vargo, Guo & Amazeen 2018；Sadowski 2019；Gruzd & Mai 2020；Proferes et al. 2021。
（另：Gillespie 2010 无 PDF 未入语料；Keen 2007 为专著未入语料。）完整键值与词数见 `discipline_style_analysis/corpus_meta.json`。
