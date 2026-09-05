# Marginalia（书页边注）

> 🌐 **网站：** <https://uniqueclouds.github.io/marginalia/> — 全部内容物在线阅读（push 自动部署）


> *mar·gin·a·li·a*（名词）——写在书页边上的批注；读者留下的痕迹。

[Yunqi Chen](https://github.com/UniqueClouds) 的科研随想与读文献随想精选——由 AI 辅助分析蒸馏出来的笔记，全部中英双语（[English](README.md) / 中文）。

**这个仓库刻意保持稀疏。** 它背后的工作目录里有原始语料、私人草稿和未完成的工作；默认**所有内容都被 git ignore**，只有显式加入白名单的、精选过的笔记才会被提交。不会有随手的提交——每条随想都按 **一个 issue → 一个 pull request → 一个 squash commit** 的仪式发布。

## 一条随想如何诞生

1. **Issue** —— 随想本身：什么触发了它、数据从哪里来、最初的 prompt/想法是什么。
2. **Pull request** —— 蒸馏后的双语笔记（`note.en.md` + `note.zh.md`），与 issue 互相引用，并在下方索引加一行。
3. **Commit** —— 每条随想恰好在 `main` 上落一个 squash commit，提交历史读起来就像目录。

## 溯源格式

每篇笔记开头都带完整溯源信息——不收来历不明的随想：

```yaml
---
id:              marginalia-NNN
title:           标题
date:            分析完成的时间
published:       笔记提交的时间
kind:            musing | analysis | proposal | survey
sources:         随想所依据的本地语料 / 文件 / 工具
initial-prompt:  开启这场对话的最初请求（想法）
agent:           ZCode CLI
model:           对话背后的模型
issue:           N
---
```

## 索引

| # | 条目 | 日期 | Issue → PR |
|---|------|------|------------|
| 001 | [编码代理有品味吗？29,787 条 Discord 消息里的美/丑代码话语](marginalia/001-code-taste-discord/note.zh.md) · [EN](marginalia/001-code-taste-discord/note.en.md) | 2026-08-15 | [#1](https://github.com/UniqueClouds/marginalia/issues/1) |
| 002 | [像 Dourish 那样写作：21 篇文本的语料分析（2004–2026）](marginalia/002-writing-like-dourish/note.zh.md) · [EN](marginalia/002-writing-like-dourish/note.en.md) | 2026-08-15 | [#3](https://github.com/UniqueClouds/marginalia/issues/3) |
| 003 | [NOTUGLY-S：学"不丑"而非"美"——NLP × 程序分析提案](marginalia/003-notugly-s/note.zh.md) · [EN](marginalia/003-notugly-s/note.en.md) | 2026-08-15 | [#2](https://github.com/UniqueClouds/marginalia/issues/2) |
| 004 | [CHI/ACL 是故事会吗？从社区吐槽到可测量的构念](marginalia/004-storytelling-quantified/note.zh.md) · [EN](marginalia/004-storytelling-quantified/note.en.md) | 2026-08-15 | [#7](https://github.com/UniqueClouds/marginalia/issues/7) |
| 005 | [四种学科的声音：BDS/HCI/Sociology/SE 经典论文的语言风格测量（314 篇/330 万词）](marginalia/005-discipline-style-voices/note.zh.md) · [EN](marginalia/005-discipline-style-voices/note.en.md) | 2026-08-15 | [#11](https://github.com/UniqueClouds/marginalia/issues/11) |
| 006 | [Spotify Podcast Guide 2026 · 英文播客推荐清单（47 节目 / 77 集精选，全部官方链接）](marginalia/006-podcast-guide/artifact.zh.md) · [English](marginalia/006-podcast-guide/artifact.en.md) | 2026-08-17 | [#13](https://github.com/UniqueClouds/marginalia/issues/13) |
| 007 | [科学写作里 nuance 的兴衰：识别、计量与本机语料的一次试测（314 篇/330 万词）](marginalia/007-nuance-rises-and-falls/note.zh.md) · [EN](marginalia/007-nuance-rises-and-falls/note.en.md) | 2026-08-17 | [#14](https://github.com/UniqueClouds/marginalia/issues/14) |
| 008 | [「How to Scale Your Model」摘记：把 LLM 训练从玄学拆成 roofline 公算法（JAX-ML scaling book）](marginalia/008-llm-scaling-book/note.zh.md) · [EN](marginalia/008-llm-scaling-book/note.en.md) | 2026-08-17 | [#15](https://github.com/UniqueClouds/marginalia/issues/15) |
| 009 | [Homologies in fields of cultural production — 读记：借了边界，没借分形](marginalia/009-homology-without-fractal/note.zh.md) · [EN](marginalia/009-homology-without-fractal/note.en.md) | 2026-08-17 | [#17](https://github.com/UniqueClouds/marginalia/issues/17) |
| 010 | [组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 — 读记：被悬置的「成功 vs 病症」二分](marginalia/010-organizational-inertia/note.zh.md) · [EN](marginalia/010-organizational-inertia/note.en.md) | 2026-08-18 | [#22](https://github.com/UniqueClouds/marginalia/issues/22) |
| 011 | [Awesome Auditable AI — 读记：188 条 / 9 节 / 132 arXiv，一份 curated list 把 AI agent 可审计性从口号变成可靠性工程](marginalia/011-auditable-agents-atlas/note.zh.md) · [EN](marginalia/011-auditable-agents-atlas/note.en.md) | 2026-08-17 | [#26](https://github.com/UniqueClouds/marginalia/issues/26) |
| 012 | [Wikipedia 编辑史与讨论页的大规模时序分析 —— 调研：部件已齐，联合尚缺](marginalia/012-wikipedia-temporal-analysis/note.zh.md) · [EN](marginalia/012-wikipedia-temporal-analysis/note.en.md) | 2026-08-18 | [#28](https://github.com/UniqueClouds/marginalia/issues/28) |
| 013 | [常人方法学（Ethnomethodology）—— 调研：来源、与民族志的异同、发展脉络](marginalia/013-ethnomethodology/note.zh.md) · [EN](marginalia/013-ethnomethodology/note.en.md) | 2026-08-21 | [#30](https://github.com/UniqueClouds/marginalia/issues/30) |
| 015 | [UCI Informatics 系的质性 HCI 版图——调研:谁在做质性、STS 与健康信息](marginalia/015-uci-informatics-qualitative/note.zh.md) · [EN](marginalia/015-uci-informatics-qualitative/note.en.md) | 2026-09-05 | [#39](https://github.com/UniqueClouds/marginalia/issues/39) |
| 014 | [扫描书高保真夹心 OCR——把普特南和罗蒂变成「原版一模一样+全文可检索」的 PDF](marginalia/014-sandwich-ocr-books/note.zh.md) · [EN](marginalia/014-sandwich-ocr-books/note.en.md) | 2026-08-22 | [#37](https://github.com/UniqueClouds/marginalia/issues/37) |
| 016 | [92617 公寓办公桌选购——调研:升降桌的深度与预算不可兼得](marginalia/016-apartment-desk-shopping/note.zh.md) · [EN](marginalia/016-apartment-desk-shopping/note.en.md) | 2026-09-05 | [#43](https://github.com/UniqueClouds/marginalia/issues/43) |
| 017 | [Ways of Knowing in HCI——读记:十八种认识法与各自的问责制](marginalia/017-ways-of-knowing-in-hci/note.zh.md) · [EN](marginalia/017-ways-of-knowing-in-hci/note.en.md) | 2026-09-05 | [#45](https://github.com/UniqueClouds/marginalia/issues/45) |

## 制品（Artifacts）

随想条目的原样伴随物——工作中的技能、原始文档、完整报告——以出生语言**原样发布**，不作翻译。各自住在所属条目目录里，但单独走自己的 PR；制品不需要 issue。

| 制品 | 条目 | PR |
|---|---|---|
| `dourish-style` 润色技能（已被 `academic-voices` 取代） | [002](marginalia/002-writing-like-dourish/artifact.zh.md) | [#9](https://github.com/UniqueClouds/marginalia/pull/9) |
| 故事会量化原始文档——调研 + 提案 v2 | [004](marginalia/004-storytelling-quantified/docs/storytelling-survey.zh.md) | [#10](https://github.com/UniqueClouds/marginalia/pull/10) |
| 四学科风格五份完整报告 | [005](marginalia/005-discipline-style-voices/reports/05-cross-discipline.zh.md) | [#12](https://github.com/UniqueClouds/marginalia/pull/12) |
| `academic-voices` 技能——五种实测风格、密度基线 + voice 分类器 | [005](marginalia/005-discipline-style-voices/artifact.zh.md) | [#13](https://github.com/UniqueClouds/marginalia/pull/13) |
| `ocr_pipeline` 扫描书夹心 OCR——图像零重编码 + 字符级不可见文字层 | [014](marginalia/014-sandwich-ocr-books/note.zh.md) | [#36](https://github.com/UniqueClouds/marginalia/pull/36) |

## 语言

每篇**笔记**都存在两份——`*.en.md` 与 `*.zh.md`，内容相同，互不将就；**artifact**（技能、原始文档）则原样收录，保留出生语言：切换到 [English README](README.md)。

## 许可

本仓库及[网站](https://uniqueclouds.github.io/marginalia/)的内容物——条目笔记、报告、播客清单——均按 **[知识共享署名-非商业性使用 4.0 国际 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)** 提供：署名即可用于任何非商业目的，商业使用需先取得许可。底层语料本身不在仓库中分发，仍受各自原始来源管辖（每条条目的 `sources` 字段已注明）。
