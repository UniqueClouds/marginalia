# Marginalia（书页边注）

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
| — | *（条目发布后会出现在这里）* | | |

## 语言

每份文档都存在两份——`*.en.md` 与 `*.zh.md`，内容相同，互不将就：切换到 [English README](README.md)。

---

个人科研笔记——暂未授权任何许可，转载/引用前请先询问。
