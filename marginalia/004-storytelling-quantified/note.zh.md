---
id: marginalia-004
title: "CHI/ACL 是故事会吗？从社区吐槽到可测量的构念"
date: 2026-08-15
published: 2026-08-15
kind: survey + proposal（调研+提案笔记）
sources:
  - "ZCodeProject/CHI_ACL_故事会量化_调研.md —— 叙事量化证据调研（2026-08-15）"
  - "ZCodeProject/AI论文显隐叙事主义_提案v2.md —— 显/隐叙事主义提案 v2（2026-08-15）"
  - "外部证据链：Hillier 等 2016（PLOS ONE）；Qiu 等 2024（JAMA）；Peng 2024（PNAS）；Stavrova 2025（HSSC）；Vincent-Lamarre & Larivière 2021（QSS）；Vinkers 2015；Kobak 2025"
initial-prompt: "社区都说 CHI/ACL 是故事会——把它量化：有人测过论文里的叙事吗？然后把它变成一个研究提案。"
agent: ZCode CLI
model: GLM（智谱）
issue: 7
---

# CHI/ACL 是故事会吗？

> 一句社区吐槽、一堆没人串起来的定量研究、一个把叙事主义拆成"文本说什么"与"图表做什么"的提案。

## 命题，及其出处

"CHI/ACL 是故事会"——顶会论文靠讲故事而非实质发表。吐槽有具名出处：知乎《ACL 为什么叫故事汇》（2023）、Wobbrock 对 CHI 拒稿文化的批评、Nacke 公开教 CHI"叙事弧"写作。它从来没有过的东西：一次测量。这个空白就是本条随想。

## 已经存在的证据（只要肯眯眼看）

- **Hillier 等 2016**（PLOS ONE）：732 篇气候科学摘要，众包打 6 个叙事元素 → 合成指数；PCA 首主成分承载 **76.5%** 方差；4 个元素与引用正相关（与影响因子混淆，**R² = 0.62**）。
- **Qiu 等 2024**（JAMA）：11,535 份基金申请；宣传语预测中标，**OR = 1.47**。
- **Peng 2024**（PNAS）：高宣传语摘要获资助几率约 **2 倍**。
- **Stavrova 2025**（HSSC）：13 万篇摘要；hype 预测引用——且男性回报更高。
- 反例：**Vincent-Lamarre & Larivière 2021**（QSS）——被录用的 AI 会议论文可读性反而*更低*。
- 背景漂移：**Vinkers 2015**——摘要正面词数十年涨 **9 倍**；**Kobak 2025**——2024 年生物医学摘要 **≥13.5%** 带 LLM 痕迹。

## 提案：显性 vs. 隐性叙事主义

- **显性** —— 语言表层（v1 五维：hook、第一人称、感官语言、appeal、连词、hype 词）。
- **隐性** —— 结构-视觉层：无人称 CARS 步骤、master narratives、图表装置（teaser 图、hero chart、caption 微叙事）、**叙事否认**（否认差 = 视觉修辞强度 − 显性解释标记），以及 artifact 层（基准选角、指标即情节、基线人物表、消融道德剧）。L3：场域意识形态。
- 统一构念：**叙事深度梯度**——叙事藏得越深，回报越高。

## 方法速写（v2）

RQ1–9：显隐分离 · 修辞演化 · 回报分解 · CHI 对 ACL 场域对比 · LLM 断点 · 访谈 · 否认溢价 · artifact 叙事性 · 污名边界。假设包括：显性叙事性在引言达峰、隐性在结果部分；否认差随技术性递增并带录用溢价。

双轨：多模态大样本普查 + 批判民族志，保持自反性。图表管线刻意**全本地**：Docling + GROBID 抽取 → ArXivCap（640 万图）热身 → ACL（约 5 万篇）+ OpenReview + CHI；三级标注（SigLIP 图类型 → Qwen2.5-VL-7B 结构化 → 语义 VL），500 图金标；全程 DuckDB；约 25 万图 ≈ 3 GPU·天。再配 arXiv v1↔camera-ready 差分与社区话语两条辅助信号。

## 值得记住的人

**Sophie Qiu = Huilian Sophie Qiu（邱惠莲）**——CMU 2022 博士，现于西北大学与 Brian Uzzi 合作（JAMA 2024、IC2S2 2025）。理论锚点：**Dourish & Gómez Cruz 2018**——对，就是[随想 002](../002-writing-like-dourish/note.zh.md)里被解剖文体的那个 Dourish；圈子真小。网里还有：Birhane 2022；Espeland & Sauder 2007（反应性）；Segel & Heer 2010 与 Hullman & Diakopoulos 2011（叙事可视化）。

## 下一步

M1–M5：编码方案 + 500 图金标 → 25 万图普查 → 回报分解 → 访谈 → 成文。三个出口：P1 测量（IC2S2 / QSS / Metascience）、P2 主文（CHI / CSCW）、P3 批判（BD&S）。精读 DiagramBank 以划清竞品边界。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | `CHI_ACL_故事会量化_调研.md`；`AI论文显隐叙事主义_提案v2.md`；外部证据链见 frontmatter |
| 初始 prompt | "社区都说 CHI/ACL 是故事会——把它量化：有人测过论文里的叙事吗？然后把它变成一个研究提案。" |
| 时间 | 调研+提案 2026-08-15 · 笔记发布 2026-08-15 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| Issue | [#7](https://github.com/UniqueClouds/marginalia/issues/7) |
