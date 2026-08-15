---
id: marginalia-002-artifact
title: "Artifact：dourish-style 润色技能"
date: 2026-08-15
published: 2026-08-15
kind: artifact（制品）
sources:
  - "C:/Users/yunqi/.zcode/skills/dourish-style/ —— 原样快照（SKILL.md + references/ + scripts/）"
initial-prompt: "与随想 002 同一条线：语料分析完成后，把发现打包成可复用的润色技能。"
agent: ZCode CLI
model: GLM（智谱）
issue: 无（artifact 直接走 PR，按发布者要求）
---

# Artifact：`dourish-style` 技能

> 工作中 ZCode 代理技能的原样快照，蒸馏自[21 篇文本的语料分析](note.zh.md)——不只发布发现，把工具也发布出来。

## 它是什么

一个把英文学术手稿向 Paul Dourish 的批判 HCI/STS/CSCW 语域修稿的技能，带硬性护栏：

1. **绝不把他语料里的句子抄进用户稿子**——只用模式与模板；语料例句仅供校准。
2. **绝不改动论点、证据、引用或术语**——只在措辞/节奏/论证框架上工作；若改写会改变句义，标记出来而不是动手。
3. **绝不编造轶事、引语或田野细节。**
4. 强度匹配会议（STS/CSCW/CHI 批判论文用全套；技术会议只做句级）。

## 里面有什么

| 文件 | 作用 |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | 工作流：定范围 → 诊断 → 修稿 → 报告；Register A（practice/everyday/encounter）vs B（materiality/format/infrastructure）；强度分级；标题门诊 |
| [`skill/references/patterns.md`](skill/references/patterns.md) | 食谱 P1–P10（not-X-but-Y、ways-in-which、paraphrase 对、复数量词、hedging 校准……） |
| [`skill/references/motifs.md`](skill/references/motifs.md) | 八个复现论证母题，供深度模式重构 |
| [`skill/references/style-guide.md`](skill/references/style-guide.md) | 语域词汇表 + 应删除的反模式 |
| [`skill/scripts/dourish_style_check.py`](skill/scripts/dourish_style_check.py) | 诊断脚本：约 29 种签名模式密度对语料基线；把欠用模式打印成"机会" |

## 校准目标（来自语料）

"not simply X but Y" ≈ 0.9 次/千词（6000 词论文约 5–6 处，集中在引言/贡献/讨论）· "rather than" ≈ 0.8 · "the ways in which" ≈ 1.0 · "that is," ≈ 0.3 · hedging 词合计 ≈ 1.5 · 设问约每 200 词一处、只在理论文引言/讨论、绝不在方法/结果 · 超基线 2.5 倍即过度风格化，回退。

## 怎么用

把 `skill/` 文件夹放进 ZCode 兼容的技能目录（如 `~/.zcode/skills/dourish-style/`），提到 "Dourish" 或要求 HCI/STS 风格润色即可触发；也可把 `SKILL.md` 当独立 prompt 指南喂给任意代理。文件内的路径保持作者原样（本副本是快照；本地原件可能继续演化）。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | `~/.zcode/skills/dourish-style/` 原样拷贝（40 KB，5 个文件），2026-08-15 由随想 002 的语料分析产出 |
| 初始 prompt | "语料分析完成后，把发现打包成可复用的润色技能。" |
| 时间 | 构建 2026-08-15 21:28–21:35 · 发布 2026-08-15 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| 所属条目 | [随想 002](note.zh.md) · [issue #3](https://github.com/UniqueClouds/marginalia/issues/3) |
