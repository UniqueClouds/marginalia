# 像 Dourish 那样写作：一位批判 HCI 学者 21 篇文本的语料分析（2004–2026）

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](002-writing-like-dourish.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis（分析笔记）</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #3</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-002</td></tr><tr><td>title</td><td>像 Dourish 那样写作：一位批判 HCI 学者 21 篇文本的语料分析（2004–2026）</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>analysis（分析笔记）</td></tr><tr><td>issue</td><td>3</td></tr></table></details>

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
3. **`dourish-style` 技能** —— 修稿工作流：Register A/B、食谱 P1–P10；红线：*绝不照抄原句*，只复现机制。已作为 artifact 发布：[artifact.zh.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/002-writing-like-dourish/artifact.zh.md)。
4. **第一个实验** —— 用该语域改写我自己的 OSS 立场论文（附变更表）。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | Zotero（`zotero.sqlite`，API :23119）→ `zotero_copy.sqlite`（201MB）；`dourish_analysis/`；技能位于 `~/.zcode/skills/dourish-style/` |
| 初始 prompt | "在我的 Zotero 里检索 Paul Dourish 的论文，定量且可核验地分析他的语言/风格特征。" |
| 时间 | 分析 2026-08-15 20:56 → 21:35 · 笔记发布 2026-08-15 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| Issue | [#3](https://github.com/UniqueClouds/marginalia/issues/3) |


<div class='marg-attach'><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> 附属材料：[SKILL.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/002-writing-like-dourish/skill/SKILL.md)</div>


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](002-writing-like-dourish.en.md)

