# NOTUGLY-S：学\"不丑\"而非\"美\"——NLP 与程序分析融合训练提案

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](003-notugly-s.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> proposal（提案笔记）</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #2</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-003</td></tr><tr><td>title</td><td>NOTUGLY-S：学\"不丑\"而非\"美\"——NLP 与程序分析融合训练提案</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>proposal（提案笔记）</td></tr><tr><td>issue</td><td>2</td></tr></table></details>

> 如果民族志说"美"多元且被悬置、"丑"具体且被制裁，为什么还坚持训练模型去给"美"打分？这个提案把目标倒过来——而它的架构本身就是对该理论的检验。

## 倒转

随想 [001](001-code-taste-discord.zh.md) 停在 Fedorova 的结论上："美"是组织性的、被有意悬置；"丑"可指认，并通过评审*制裁*执行——负面评论之后跟着修订、revert 或 request-changes。NOTUGLY-S（v1.1）把这句话直接当作监督信号。

## 打分器

一个以仓库为条件、跨语言的**"不丑"打分器**：

```
s(x) = g_θ(d) + h_φ(d, c_r) + α·reviewer + ε
```

`g_θ` 全局（跨仓库可迁移），`h_φ` 局部（以仓库档案 `c_r` 为条件），`α·reviewer` 人在回路项——按轴输出"不丑"概率，永不出单一"美"分。监督来自评审制裁，而非静态标签。

## 问题与假设

- **RQ1** 可学性 · **RQ2** 信号价值 · **RQ3** 模态贡献 · **RQ4** 理论检验。
- **H1** 仓库内 AUROC 高全局模型 ≥0.05 · **H2** 修订对优于静态标签 · **H3** 全局+局部分解有效 · **H4** 双模态>单模态 · **H5** 生态效度（标记与 revert/30 天 churn 相关）· **H6** 作者身份置换不变性（KL 低于阈值）· **H7** 跨语言迁移：`g` 可迁移、`h` 锚定在仓库层。

## 三轨并行

1. **层次可解释模型** —— 全局 GBM + 逐仓库贝叶斯收缩。
2. **图-文融合 Transformer** —— 7–14B 开源代码 LLM + LoRA；diff + repo card + 线性化程序图；DPO。
3. **偏好专线** —— Bradley–Terry / DPO。

程序分析侧：tree-sitter 统一 **8 语言** AST + 惯用表；复杂度/命名/克隆/图特征，按 `(语言, 是否测试)` 百分位归一。NLP 侧：评审评论、commit/issue 文本、Snorkel 式弱监督、PU 学习。

## 评估

仓库内时间外推 AUROC/AUPRC · 30 天 churn 生存分析（C-index、Cox HR）· 修订对排序 · 行级归因 IoU · 标注一致性 α≥0.7。基线：SonarQube、LLM zero-shot、LLM+repo-card、CodeReviewer DQE。跨语言主张用留一语言检验；偏差用作者置换探针。

## 玩具原型已就位

`notugly.py`——规则版，Python AST，L1–L3 三层。`notugly2.py`——tree-sitter 跨语言版，百分位分层回退。express/flask/gin 三份仓库档案（文件、命名风格、分布、commit 大小、热点、revert 记录）充当"仓库自身分布"——一切偏离都对着它判。

## 伴随调研

从 McCabe 到 ISO 5055 到 LLM-as-judge，六层定量"好代码"度量在结构上都是*丑探测器*，受四重约束：Goodhart 定律、共线性、阈值任意性、层次错位。跨源规范语料（Google eng-practices、PEP 8、Rust API 指南、Swift、Linux 内核、CISQ；数千条条文）配八字段 schema（极性、可自动化性、冲突、执行机制……），导出三个可检验假说：禁令主导；共识内核+仓库局部残差可干净分解；阈值数字的跨源分布本身有信息量。

## 现状

提案 v1.1（跨语言设计 + notugly2 验证）、玩具原型、调研——全部完成于 2026-08-15。下一步：在真实评审语料上挖制裁信号，然后上 Track A。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | `code_beauty_simplification/`（提案 v1.1 + 调研 + notugly/ 原型）；随想 001 的上游语料 |
| 初始 prompt | "把 Fedorova 的'制裁/模仿/不丑'解读变成一个可检验的 ML 目标——NLP 遇上程序分析。" |
| 时间 | 提案 v1.1 2026-08-15 · 笔记发布 2026-08-15 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| Issue | [#2](https://github.com/UniqueClouds/marginalia/issues/2) |


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](003-notugly-s.en.md)

