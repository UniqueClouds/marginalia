---
id: marginalia-002
title: "像 Dourish 那样写作：一位批判 HCI 学者 21 篇文本的语料分析（2004–2026）"
date: 2026-08-15
published: 2026-08-15
kind: analysis（分析笔记）
sources:
  - "本地 Zotero 库（zotero.sqlite + HTTP API :23119）→ ZCodeProject/zotero_copy.sqlite（201MB）—— 20 篇 Dourish 原文，2004–2026，含 2 本 MIT Press 专著（约 32.4 万词）"
  - "《The Stuff of Bits》(2017)，EPUB 提取 —— 584 段（约 8.35 万词），应邀补入的第 21 种"
  - "ZCodeProject/dourish_analysis/ —— paras.json、corpus_meta.json、12 个 quotes_*.txt 母题引文、管线脚本"
  - "对照语料：25 篇同时期其他领域论文（约 39.3 万词）"
initial-prompt: "在我的 Zotero 里检索 Paul Dourish 的论文，定量且可核验地分析他的语言/风格特征。"
agent: ZCode CLI
model: GLM（智谱）
issue: 3
---

# 像 Dourish 那样写作

> 一个学者的"声音"可以测量吗？21 篇文本、约 40.8 万词之后：可以——那是一个数得出来、且二十年稳定的签名。

## 随想

风格建议通常靠感觉。我想要相反的东西：取批判 HCI 里最有辨识度的文体之一——Paul Dourish——从一手文本出发去测量它，而且管线里每一句引文都要能被机器在语料中核验。

## 语料

- **20 篇**取自本地 Zotero（在约 5.6k 篇期刊文章里按作者检索；剔除中英对照版；均带 PDF 附件），2004–2026，含两本 MIT Press 专著；清洗后约 **32.4 万词**。
- **+1**：《The Stuff of Bits》（2017），从 EPUB 提取——584 段、约 **8.35 万词**。
- **对照**：25 篇同时期其他领域论文，约 39.3 万词，作 keyness 基线。

## 方法

PyMuPDF 版面块提取 → 去参考文献 → 段落语料（`paras.json`）→ 词频与 2–5 元 n-gram 文档频率 → 对对照语料的对数比值 keyness → **60+ 修辞模式正则** → 段落 TF-IDF 聚成 **8 个复现母题（M1–M8）** → `verify_quotes.py` 把报告中每条引文（还原连字符/弯引号后）在语料里逐条回找并标 PASS/FAIL。另有独立模块给《The Stuff of Bits》打签名分（`sob_stats.py`：约 30 种签名模式密度对基线；`sob_sim.py`：段落级 TF-IDF 相似度）。

## 可测量的签名

- 词表：**practice ×1,041**、**data ×1,022** 领衔。
- 否定—重述：**"not simply/just/only/merely … but" 298 处、见于 18 篇**；**"rather than" 267 处、见于 19 篇**——大约**每 350 词一次**。
- **"ways in which" ×252**（14 篇）；量化复数群 697 次；**"that is / in other words" 约 172 处**。
- 设问：独著理论文里约**每 200 词一问**。
- 同一个句法模板——*非 X 之属性，乃互动之成就*——从 **context（2004）** 经 *emotion*、*data* 一路走到 *beauty*，跨度二十年；句级自我回炉的 TF-IDF 相似度最高达 **0.97**。
- 《Stuff of Bits》签名："that is" 为基线 **2.45 倍**；*materiality* **14.98 倍**；*everyday* **0.12 倍**。

两个样本句（均 2004 年，语料内核验通过）：

> "what I want to do here is to reconsider context, not as a representational problem but as an interactional problem."

> "Embodiment is not a property of systems, technologies, or artifacts; it is a property of interaction."

## 产出

1. **分析报告** —— `Dourish_语言特征分析报告.md`（约 40KB），全部引文经核验。
2. **可复用管线** —— 脚本 + JSON 中间产物 + 12 个母题引文文件。
3. **`dourish-style` 技能** —— 修稿工作流：Register A/B、食谱 P1–P10；红线：*绝不照抄原句*，只复现机制。已作为 artifact 发布：[artifact.zh.md](artifact.zh.md)。
4. **第一个实验** —— 用该语域改写我自己的 OSS 立场论文（附变更表）。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | Zotero（`zotero.sqlite`，API :23119）→ `zotero_copy.sqlite`（201MB）；`dourish_analysis/`；技能位于 `~/.zcode/skills/dourish-style/` |
| 初始 prompt | "在我的 Zotero 里检索 Paul Dourish 的论文，定量且可核验地分析他的语言/风格特征。" |
| 时间 | 分析 2026-08-15 20:56 → 21:35 · 笔记发布 2026-08-15 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| Issue | [#3](https://github.com/UniqueClouds/marginalia/issues/3) |
