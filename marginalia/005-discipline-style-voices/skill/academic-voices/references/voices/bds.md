# Voice: Big Data & Society（批判数据研究 / Sage 批判刊）

基线：27 篇（BDS 16 + NM&S 10），21.2 万词，2004–2021。报告：`ZCodeProject/学科风格分析_1_BigDataSociety.md`。
画像：**写长句的公共知识分子**——文章在说话（"This article"），批判学者以 "I" 亲自下场，机制以被动句无名运行。

## 目标密度（每千词；voice_check.py --voice bds）

| 指标 | 基线 | 说明 |
|---|---|---|
| 平均句长 | 26.8 词 | 四学科最长；>30 词长句占 33% |
| 分号 | 4.63 | 长句靠分号缝合论点 |
| not simply...but | 0.29 | 四学科最高（学科级批判引擎） |
| rather than | 0.51 | 同上 |
| increasingly | 0.36 | 独有的现代性进行时（他科 0.05–0.12） |
| 被动 be+V-ed | 8.35 | 四学科最高 |
| we / I | 3.8 / 1.16 | we 最低；独著文允许高密度 I |
| this article vs this paper | 0.32 vs 0.10 | 期刊自称 "this article" |
| 缩写词 | **0.00** | 全库零 don't/can't——绝不口语化 |
| 弯引号 | 2.6 | 关键概念加 scare quotes |
| might / may / suggest | 0.69 / 1.56 / 0.74 | — |

## 词汇场
opacity, surveillance, datafication, assemblage, platform(s), algorithmic, epistemology, critique/critical（7.0/万词）, power（6.3/万词，25/27 篇）, inequality, extraction, transparency, "cooked"/"raw" data。引用格式：author-date 括注（36/万词，四学科最高）+ 高频 et al.（2.3/万词）——一句话里并置三四位学者再逐一回应。

## 结构仪式
- **开篇**：宣言断言（"Data are a form of power."）或时事钩子（Snowden/一条推文/一次争议），或格言 epigraph；**不写** "In recent years..." 式铺垫。
- **摘要**："(1)...(2)...(3)..." 编号三分法给出分类学；自称 "This article argues/examines..."。
- **正文**：场景化小节标题（如 "Terminological anxiety"）允许；民族志材料保留原始语流。
- **收尾**：对学科的规训性呼吁（"What is needed, then, is not X but Y"）。

## 改写配方（B1–B6）

**B1 宣言句开场**（intro 首句 / 小节首句）
- before: "In recent years, algorithmic systems have attracted significant scholarly attention."
- after: "Algorithms are a form of power. The question is not whether they discriminate, but in which of three ways."

**B2 否定—重述**（thesis / 定义 / 纠偏）
- before: "Data are not neutral."
- after: "Data are never raw, but always cooked — rendered intelligible by the practices that collect and circulate them."

**B3 increasingly 时间性**（现代性焦虑句）
- before: "More and more decisions are made by algorithms now."
- after: "Decisions once left to human discretion are increasingly delegated to computational systems that few can inspect."

**B4 编号三分法**（摘要 / 概念节）
- 模板：`I distinguish three forms of X: (1) X as [世俗理解], (2) X as [技术具身], and (3) X as [结构性效果].`

**B5 学者拉扯句**（related work / 讨论）
- 模板：`Where [Name] (Year) treats X as [立场A], [Name] (Year) insists on [立场B]; I argue instead that X is best approached as [重述].`

**B6 规训呼吁收尾**（conclusion 末段）
- 模板：`What is needed, then, is not [more/better X] but [认识论/伦理重述].`

## 标题公式
- **"The X of Y" 概念杠杆**：The politics of X / The cultural work of X / The ethics of X: 动名词短语
- 最长冒号副标题（63% 含冒号，60% 超 10 词）；引用口语入题（How the machine 'thinks'）
- 反模式：疑问句标题（本库为零）、动词分词开头堆叠、短标题

## 反模式（改稿时删除）
- "We present..." / "In this paper, we..."（换 "This article..."）
- 缩写词（don't → do not）与口语比喻
- 短促碎句连排（P50=20 词起步；两个短论点用分号并成一 句）
- 数字方括号引用 [12]（换 author-date）
- design implications / RQ 列表 / threats to validity（这些是 HCI/SE 仪式，BDS 不用）
- "plays a crucial role"、"shed light on"
