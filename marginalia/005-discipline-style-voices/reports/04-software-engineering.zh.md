# Software Engineering（ICSE/FSE/TSE/MSR）学科论文的语言风格分析
**——基于 Zotero「各学科 Classic Papers / Software Engineering」子库 114 篇原文的语料库分析（1987–2023）**

---

## 0. 语料与方法

### 0.1 语料来源
Zotero 库「各学科 Classic Papers → Software Engineering」子库共 136 个条目，**114 篇入语料、116.7 万词（四学科篇数最多）**。未入语料：19 篇仅有 IEEE/ACM 网页快照无 PDF（多为早年 TSE 论文，如 DECOR、Measuring and modeling programming experience 等）；3 篇中文翻译版/词数不足。含子库「peer review」小类的审稿研究若干。

| 维度 | 数值 |
|---|---|
| 论文数 / 词数 | 114 篇 / 1,166,765 词 |
| 主要来源 | ICSE/FSE/SIGSOFT 系会议（约半数）+ TSE 13 篇 + EMSE 7 篇 + MSR/ASE 等 |
| 年份跨度 | 1987–2023（Royce 1987 瀑布模型原文在内；主体是 2005–2020） |
| 篇均长度 | 10,235 词 |
| 引用样式 | 数字方括号 [n]：88.1 次/万词（106/114 篇）；TSE 近年混用 author-date |

内容构成：经验软件工程主力军（code review、OSS 贡献、缺陷预测、挖掘软件仓库、开发者生产力）+ 测试/程序分析经典（mutation、regression testing、symbolic execution、fault localization）+ 软件工程中的 AI（SE4ML、sentiment analysis）。与 HCI 子库的交界地带（developer studies）有少量重叠作者（Bird、Herbsleb、Devanbu）。

### 0.2 分析方法
同 Dourish 管线；引文经归一化脚本核验。

---

## 1. 总体节奏：短句、直给、几乎不用破折号

| 指标 | SE | 四学科排位 |
|---|---|---|
| **平均句长** | **18.8 词** | **最短**（BDS 26.8） |
| 句长 P50 / P90 / P99 | 16 / 34 / 68 | 全线最短 |
| 长句占比（>30 词） | **15.3%** | **最低**（BDS 33.1%） |
| 短句占比（<10 词） | **28.7%** | **最高** |
| 段落中位长度 | 102 词 | 第 2 短 |
| 破折号 /万词 | **7.1** | **最低**（SOC 的 1/5） |
| 弯引号 /万词 | **30.3** | 最低（SOC 55.9） |
| 缩写词 | 1.2 | 次低 |

**第一个结论：SE 是四学科中唯一的"工程报告体"**。句子最短、插入语最少、修饰最少。近三成句子不足 10 词——"We report our findings.""Table 3 summarizes the results.""This is expected."这类干句高频滚动。信息的组织单元不是论证链而是**清单与表格**。

## 2. 人称与语态："我们"密度冠军 + 高被动并存

| 指标 | SE | BDS | HCI | SOC |
|---|---|---|---|---|
| **we /万词** | **103.0** | 37.8 | 91.5 | 52.2 |
| **our /万词** | **40.5** | 13.4 | 34.4 | 18.1 |
| I /万词 | **8.8** | 11.6 | 16.8 | 15.8 |
| be+V-ed 被动式 /万词 | 82.2 | 83.5 | 72.1 | 64.7 |

- **we 与 our 双第一**：SE 论文是团队作业说明书——"our approach""our dataset""our tool" 是所有权宣言。we+动词搭配高度集中于工具动词：**we use (414) > we found (362) > we used (288) > we present (184) > we describe (119) > we conducted (98) > we analyzed (84)**。
- **I 最低**：几乎没有独著理论文，"我"的声音让位于"我们构建了 X"。
- **被动与主动并用**：方法步骤用被动（"The commits were extracted..."），贡献声明用主动（"We present Tarantula"）——工序与人责分工明确。

## 3. 词汇场与引用谱系

### 3.1 概念词汇场（keyness vs 其余三学科）
SE 词场是物件清单：**bug（2127/百万词，断层第一）、defect(s)（1342/M 合计）、fault(s)、refactoring、patch、clone、commit(s)（10.0/万词）、repository/repositories（10.4/万词）、test suite、mutation、code smell、pull request、developer(s)（39.1/万词，101/114 篇）**。工具与数据集专名高度密集：**Bugzilla、Eclipse、GCC、GitHub、JEdit、PostgreSQL、FindBugs、PMD、Tarantula、Hipikat、GHTorrent**—— artefact 命名即学问的一部分。

### 3.2 引用谱系（人名 keyness）
**Mockus（100/M，Apache/开山系）、Herbsleb、Bird、Zimmermann、Zeller、Weimer、Rothermel、Gousios、Kalliamvakou、Steinmacher、Harman、Lo/Nagappan/Zimmermann 组合**。谱系明显"内部循环"：ICSE 引 ICSE，近十年的高被引是上一代 MSR/ICSE 论文——与 BDS/SOC 动辄跨引百年前经典（Durkheim、Weber）形成结构差异：**SE 几乎不与死者对话**（Royce 1987 已是古董级）。

引用密度：et al. 12.7 次/万词（次高）——SE 的 [n] 数字引用把姓名压进方括号，et al. 只在行文复述时出现。

## 4. 高频短语与签名句式

| 模式 | SE | 排位 |
|---|---|---|
| not simply...but | **0.8** | **最低**（BDS 的 1/4） |
| rather than | 2.0 | 最低 |
| there is/are | 10.3 | 与他科持平 |
| **a set of** | **2.6** | **第一**（集合思维："a set of metrics/commits/projects"） |
| 问句 /万词 | **8.5** | **第一**（但性质见 §5.1） |

SE 不做"否定—重述"的概念劳动——它的修辞动作是**枚举与划分**（a set of、two types of、three categories），不是概念翻转（not X but Y）。

## 5. 修辞动块：一整套可复制的论文仪式

### 5.1 问句标题与"为什么"开场
SE 问句密度四学科第一，但它的问句不是 BDS 的批判设问，而是**操作性问题**——把工程痛点直接抛上标题：

> "In contrast to programming, which is a construction process, debugging is a search process—a search which can involve all of the program's code, its runs, its states, or even its history. Debugging is particularly nasty because the original assumptions of the program's authors cannot be trusted."
> —— Weiß, Premraj, Zimmermann & Zeller (2007), *How Long Will It Take to Fix This Bug?*, Introduction（"nasty" 这种口语判词在 SE 罕见，Zeller 是文体异端）

标题问句群：*Who should fix this bug?*（Anvik et al.）、*How Long Will It Take to Fix This Bug?*、*Why do developers use trivial packages?*、*Are mutants a valid substitute for real faults in software testing?*、*Fair and balanced?: bias in bug-fix datasets*、*Measure it? Manage it? Ignore it?*。

### 5.2 "To understand X, we did Y" 公式
经验 SE 的标准摘要发动机——目的状语从句开头：

> "To understand developers' typical tools, activities, and practices and their satisfaction with each, we conducted two surveys and eleven interviews. We found that many problems arose because developers were forced to invest great effort recovering implicit knowledge by exploring code and interrupting teammates."
> —— LaToza, Venolia & DeLine (2006), *Maintaining mental models*, Abstract（一句话完成：目的+方法+规模+发现）

### 5.3 规模开场（scale-first openings）
数据集规模本身就是新闻，常做第一句：

> "With over 10.6 million repositories hosted as of January 2014, GitHub is currently the largest code hosting site in the world."
> —— Kalliamvakou et al. (2014), *The promises and perils of mining GitHub*, Introduction

### 5.4 贡献清单仪式（contribution bullets）
引言末尾固定一个显式列表，且爱标"original"：

> "In contrast to previous work (see Section 8), the present paper makes the following original contributions:"
> —— Weiß et al. (2007)（随后是项目符号列表）

"main/key/three contributions" 动块 21/114 篇；"To the best of our knowledge, this is the first..." 出现于 16/114 篇——**首发权声明**是 SE 的产权仪式：

> "To the best of our knowledge, this study is the first attempt to systematically characterize the phenomenon of companies' withdrawal."
> —— Zhang et al. (2022), *Turnover of Companies in OpenStack*

### 5.5 RQ 编号与 Threats to Validity 自首
**RQ1/RQ2... 研究问题编号**出现于 45/114 篇（其他三科合计仅 15 篇）；**Threats to validity** 章节 48/114 篇（其他三科合计 4 篇）——SE 论文必须在结尾按 construct/internal/external validity 三段"自首"：

> "RQ1: Why do open source projects fail?"
> —— Coelho & Valente (2017), *Why modern open source projects fail*

> "Construct validity. The first threat is related to the risk of survey respondents misunderstanding the survey questions. To mitigate this threat, we discussed the questions with experienced researchers..."
> —— Li et al. (2021), *Are you still working on this? An empirical study on pull request abandonment*（TSE）

### 5.6 未来工作（future work）
80/114 篇（**70%，四学科最高**）以 future work 收尾，且句式高度模板化：

> "For future work, we plan to conduct a large scale survey of data scientists to quantify the working styles and tasks observed in this study and to shed light onto the challenges associated with data science work."
> —— Kim, Zimmermann, DeLine & Begel (2016), *The emerging role of data scientists on software development teams*, §Future Work

### 5.7 定义式开场（definitional openings）
与 HCI 的 "We present" 相对，SE 综述/实践类爱用下定义开题：

> "Code review is a common software engineering practice employed both in open source and industrial contexts. Review today is less formal and more 'lightweight' than the code inspections performed and studied in the 70s and 80s."
> —— Bacchelli & Bird (2013), *Expectations, Outcomes, and Challenges of Modern Code Review*, Abstract

### 5.8 破格者：On the naturalness of software
语料里文学性最强的 SE 论文（CACM Research Highlights 版式）：先引 Knuth 名言，再以连珠设问立论——

> "Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do."（引 Knuth）
> "Do we program as we speak? Is our code largely simple, repetitive, and predictable? Is code natural?"
> —— Hindle, Barr, Gabel, Su & Devanbu (2016), *On the naturalness of software*

（这一篇的存在证明：当 SE 论文想上 CACM 封面时，它会借用 HCI/BDS 的修辞武器——epigraph、设问、类比。）

## 6. 标题风格：最短、最少冒号、最多问号

| 特征 | 比例（n=136） | 四学科对比 |
|---|---|---|
| >10 词 | **33%** | **最短** |
| 含冒号 | **30%** | **最低**（BDS 63%） |
| **完整问句** | **8%** | **第一** |
| 动词/分词开头 | 16% | 次高（Mining.../Understanding.../Tracking...） |
| 带引号 | 10% | 低 |

SE 标题直给："名词短语 + 可选问号"。但近年经验 SE 也学会玩标题：*Why we refactor? confessions of GitHub contributors*（"confessions"）、*Don't touch my code!*（感叹号）、*"It's not a bug, it's a feature"*、*Hey, you have given me too many knobs!*、*Do developers feel emotions?*——与 HCI 标题文化合流的迹象（同一批人也在 CHI 发表）。

## 7. 风格画像总结

**SE 的声音：一个写清单的工程师。** 句子四学科最短（P50=16 词），破折号与 scare quotes 最少；we/our 双冠军，动词全是工具动词（use/found/present/describe/conducted）；名词场全是可数实体（bugs, commits, repositories, developers）；论文按固定仪式组装：To understand X 开头 → 规模开场 → 贡献清单 → RQ 编号 → 表格与阈值 → Threats to Validity 自首 → future work 收尾（70% 篇幅必有）；标题最短、问号最多、冒号最少。它不做概念翻转（not X but Y 全场最低），它的修辞动作是枚举、划分、命名（工具名、数据集名、metric 名）。

**若要模仿该文体（写作配方）**：
1. 摘要公式："To understand X, we conducted/interviewed/mined... We found that..."（一句话方法+规模+发现）；
2. 引言末尾列 "This paper makes the following contributions:" 项目符号 3 条，各配 [n] 引用；
3. 研究问题写成 RQ1/RQ2/RQ3，每条一问句，结果节按 RQ 逐一回答；
4. 方法节写工序（被动句），数据节写规模（"over N commits/projects"）；
5. 结果用表格+效应值，句子短到 16 词以内；避免破折号插入语与概念性 scare quotes；
6. 结尾三段式：Threats to Validity（construct/internal/external 三小节+缓解措施）→ Related Work → Future Work（"we plan to..."）；
7. 标题：短名词短语或工程痛点问句，工具/数据集命名要有记忆点。

---

## 附录 A：局限说明
1. 19 篇无 PDF（IEEE 网页快照）未入语料，TSE 经典（DECOR、软件成本估计综述、O-O metrics 系列等）缺席，词场统计对"测试/度量"线略有低估。
2. 子库含极少数非 SE 语境论文（如 Chun & Sauder《The logic of quantification》），保留入语料但影响可忽略。
3. ICSE/FSE 双栏与 TSE 单栏混排，段落统计有版式差异；句子级指标不受影响。
4. 部分近年论文引言含 "This article has been accepted..." 等刊物水印句，已过滤主要模式。

## 附录 B：语料构成（114 篇节选代表 + 分布）
- 经典与度量：Royce 1987（瀑布原文）；Kuhn, Wallace & Gallo 2004（fault interactions）；Basili 系（O-O metrics 验证在无 PDF 组）；Meyers? 未入
- 代码评审：Bacchelli & Bird 2013；McIntosh et al. 2016；Rigby & German 2014；Tsay, Dabbish & Herbsleb 2014；Bogart et al. 2016（API 断裂）
- OSS/社区：Kalliamvakou et al. 2014；Steinmacher 系；Barcomb et al. 2019；Guizani et al. 2021；Zhang et al. 2022（OpenStack 退出）；Bird et al.（email networks、open borders）
- 缺陷与测试：Just et al. 2014（mutants）；Parnin & Orso 2011（automated debugging）；Weimer 系（genetic programming repair 在 Gousios 语料）；Jones/Facebook 系（backport?）；Seo et al.（Google build errors）；Dietz et al.（integer overflow）
- 开发者研究：LaToza et al. 2006；Ko et al.（information needs）；Meyer 等（work life）；Parnin（static analysis 两篇）；Murgia et al.（emotions）；Vassallo et al. 2020
- SE×AI：Amershi et al. 2019（SE4ML case study）；Guzman et al.（sentiment）；Xia/Lo 系
（完整 114 篇键值与词数见 `discipline_style_analysis/corpus_meta.json`。）
