---
id: marginalia-005-artifact-skill
title: "Artifact：academic-voices 五风格润色技能"
date: 2026-08-16
published: 2026-08-16
kind: artifact（制品）
sources:
  - "C:/Users/yunqi/.zcode/skills/academic-voices/ —— 原样快照（SKILL.md + references/ + scripts/）"
initial-prompt: "把 paul style 升级成 paul + 这几类期刊 style 的文笔润色和修改 skill。"
agent: ZCode CLI
model: GLM（智谱）
issue: 无（artifact 直接走 PR，按发布者要求）
---

# Artifact：`academic-voices` 技能

> 工作中 ZCode 代理技能的原样快照。[002 的 dourish-style 技能](../002-writing-like-dourish/artifact.zh.md)在此升级为五 voice 版本：Dourish 之外新增 BDS / HCI / Sociology / SE 四种学科语域，全部带实测基线。

## 它是什么

一个"学术声音"润色与诊断技能，五种 voice 各自配：

- **voice guide**（`references/voices/{bds,hci,soc,se}.md`）：画像、目标密度表（每千词）、词汇场、结构仪式、改写配方（B1–B6 / H1–H6 / S1–S6 / E1–E7，before→after）、反模式清单、标题公式；Dourish 保留原 style-guide/patterns/motifs 三件套（P1–P12、M1–M8）。
- **`scripts/voice_check.py`**：多基线诊断。`auto` 模式是"学科伪装检测器"——把稿件对五个基线（370 万词语料实测，密度存于 `scripts/baselines.json`）算平均对数比距离并排名；留出语料实测 top-1 62% / top-2 92%。`--voice X` 模式输出全密度表 + 最缺的签名模式（opportunities）。

## 红线（与 002 相同）

不得把语料原句抄进用户稿件；不改主张/证据/引用；不编造轶事与参与者；一次只用一种 voice。
