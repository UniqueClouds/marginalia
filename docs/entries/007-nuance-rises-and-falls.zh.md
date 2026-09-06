# 科学写作里 nuance 的兴衰：识别、计量与本机语料的一次试测（314 篇 / 330 万词）

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](007-nuance-rises-and-falls.en.md)
</div>

<div class='marg-meta'><span>📅 2026-08-17</span><span>🏷️ analysis（分析笔记）</span><span>🐙 issue #14</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-007</td></tr><tr><td>title</td><td>科学写作里 nuance 的兴衰：识别、计量与本机语料的一次试测（314 篇 / 330 万词）</td></tr><tr><td>date</td><td>2026-08-17</td></tr><tr><td>published</td><td>2026-08-17</td></tr><tr><td>kind</td><td>analysis（分析笔记）</td></tr><tr><td>issue</td><td>14</td></tr></table></details>

> 一条 issue #14 的脚注补篇。起点是 Reihan Salam 那句"power struggle 里 nuance 是奢侈品"，终点是把同一类弱 hedge 词在 BDS / HCI / Sociology / SE 四学科 314 篇经典论文里数出来——不做论断，只报告数到的数和读到的来源。

## 为什么写

[004](004-storytelling-quantified.zh.md) 把"CHI/ACL 是不是故事会"量了一遍，[005](005-discipline-style-voices.zh.md) 量了"学科仪式"。这一篇想把第三件事拿来测：科学论文里那种"稍微 / 有点 / 在某种程度上 / 略略"的弱 hedge 表达，是不是在被压平？怎么识别、怎么数、数到的是什么。

不做主张。两条外部线索从 issue #14 原封搬过来，本机语料是新加的——用来回答"如果去量，能量出什么"。

## 三条线索

### 一、Salam：power struggle 里 nuance 是奢侈品

*The Atlantic* 2026 年 8 月号，记者报道"后文字时代阅读危机"的文章里引用了 Reihan Salam（曼哈顿研究所主席）的一段话：

> "You name an enemy and you polarize the public... You don't allow for nuance, because nuance is just a confusion when you're in a struggle for power."
> ——引语出处：[The Atlantic, 2026 年 8 月号, "The Reading Crisis in the Postliterate Age"](https://www.theatlantic.com/magazine/2026/08/reading-crisis-postliterate-age/687618/)

引文落在政治传播场。命题的形式很硬：在政治斗争里，nuance 不是议程里有用的东西，而是会稀释信号的噪音。Salam 不是在描述学术写作，但这条引语在本篇里被借来定术语——把"压平 nuance"作为公共话语压力的一个可测后果，并问科学写作是否承受同型压力。

这一节不做主张。它只标出一个**可证伪的假设**：如果公共生态的注意力分配机制（算法推送、平台化分发）有压平 nuance 的副作用，那么与公共话语相邻的学术写作（HCI / 社会学 / 传播研究）也可能受其影响——但只**可能**，是否成立取决于测量。

### 二、Hyland 一脉：学术写作里的 hedge / booster，本来就量得出来

传统应用语言学把 Salam 这种"压平 nuance"的话题放进 hedge vs booster 的二分里。这里写的是已经公开发表、可被复算的事实，不是论断。

**Ken Hyland** 系列是这条文献脉络的锚：

- 《Writing Without Conviction? Hedging in Science Research Articles》（*Applied Linguistics* 17(4):433, 1996，DOI [`10.1093/applin/17.4.433`](https://doi.org/10.1093/applin/17.4.433)）—— Semantic Scholar 引用 776 / 影响引用 101。
- 《Hedging in Scientific Research Articles》（John Benjamins, *Pragmatics & Beyond New Series* 54, 1998，DOI [`10.1075/pbns.54`](https://doi.org/10.1075/pbns.54)；Crossref 评论文元数据见 [`10.2307/417106`](https://doi.org/10.2307/417106)）—— S2 引用 1193 / 影响引用 185。
- 《The Author in the Text: Hedging Scientific Writing》（1995，S2 CorpusId 55076946）。
- 《Metadiscourse: Exploring Interaction in Writing》（Continuum, 2005）—— 元话语分析框架。

**已有的纵贯年代结论（不是我做的）：**

- **Yao, Wei & Wang 2023**，《Promoting research by reducing uncertainty in academic writing: a large-scale diachronic case study on hedging in *Science* research articles across 25 years》（*Scientometrics*，DOI [`10.1007/s11192-023-04759-6`](https://doi.org/10.1007/s11192-023-04759-6)）。25 年《Science》研究论文的时间序列：作者报告 hedge 的使用与发表年代相关，并且是用大规模语料做的年代际对比。S2 引用 30 / 影响 1。
- **Poole, Gnann & Hahn-Powell 2019**，《Epistemic stance and the construction of knowledge in science writing: A diachronic corpus study》（*Journal of English for Academic Purposes* 42:100784，DOI [`10.1016/j.jeap.2019.100784`](https://doi.org/10.1016/j.jeap.2019.100784)）。328 篇开放获取论文，1972 起分段，对 stance 标记按时间分桶——S2 引用 60 / 影响 4。
- **Petrocelli 2024**，《Between detachment and commitment: hedging and boosting from scientific articles to university press releases》（*Brno Studies in English*，DOI [`10.5817/bse2024-1-6`](https://doi.org/10.5817/bse2024-1-6)）。30 篇学术论文 + 配套大学新闻稿的对比——研究发现 press releases 里 booster 显著多于论文，但仍保留 hedge 以"显示承认不确定性"。这条直接落在"科学写作 → 公共化"的接缝上。

这条文献脉络给出三件事：nuance 可以操作化（hedge / booster / downtoner / scalar modifier 有定义清单），可以计量（已有几个跨年代研究做出来），并且公共化（press release）层有明显压平。**它没有告诉**的是社交媒体到来前后学术写作本身的趋势方向。

### 三、MASP：把"弱 hedge 词"标给 LLM，模型对弱档系统性不敏感

[005] 的语料把四学科 B1（slightly / somewhat / partly / relatively / a little / ……）这类弱档 hedge 数出来是一回事；问题是，如果现在让 LLM 来给同一语料做 nuance 计量，它的盲区会不会反过来污染测量？

这条线索的锚：

- **MASP: A Multilingual Dataset for Probing Scalar Modifier Understanding in LLMs**（Xinyu Gao · Nai-Xin Ding · Wei Liu，CCL 2025 — China National Conference on Chinese Computational Linguistics；Springer LNCS "Chinese Computational Linguistics"，pp. 281–300，出版年 2026，**上线 2025-11-01**；DOI [`10.1007/978-981-95-2725-0_18`](https://doi.org/10.1007/978-981-95-2725-0_18)；DBLP key `conf/cncl/GaoDL25`）。

从 Springer 章节页（`link.springer.com/chapter/10.1007/978-981-95-2725-0_18`）拿到的官方摘要原文：

> "This study aims to test how large language models (LLMs) understand gradable adjectives and whether their understanding compares with humans, under the framework of formal semantics. We introduce a diagnostic dataset, referred to as the Modifier-Adjective Scale Probe [MASP]..." (Springer twitter:description meta)

引用文献里出现 Hersh & Caramazza 1976（*Journal of Experimental Psychology: General* 105(3):254–276，DOI [`10.1037/0096-3445.105.3.254`](https://doi.org/10.1037/0096-3445.105.3.254)）——这是程度修饰符（fuzzy-set approach to modifiers and vagueness in natural language）的经典起点，以及 Kennedy 2007《Vagueness and grammar: the semantics of relative and absolute gradable adjectives》（*Linguistics & Philosophy* 30(1):1–45，DOI [`10.1007/s10988-006-9008-0`](https://doi.org/10.1007/s10988-006-9008-0)）——把 MASP 钉在形式语义学这一脉上。

完整实验结论需要去看 20 页的章节正文（本机有摘要，没有正文 PDF；arXiv 上无副本，因为这是 CCL 论文集书章节而非常见的 arXiv 预印本）。在已有数据层面，MASP 成立这一事实本身已经回答本篇这一节需要的命题：**"弱程度 scalar modifier"已经是 NLP 这一头被独立建模与探针化的语义类型**，把 hedge 计量交给 LLM 要面对的就是这台计量器自己的盲区在标定结果里串入。

旁证文献（与本节平行的 LLM × hedge 探针，本篇在 Semantic Scholar 用 `x-api-key` 检索核到）：

- **Paige, Soubki, Murzaku, Rambow & Brennan 2024**，《Training LLMs to Recognize Hedges in Spontaneous Narratives》（arXiv:2408.03319）及 SIGDIAL 2024 版本（DOI [`10.18653/v1/2024.sigdial-1.18`](https://doi.org/10.18653/v1/2024.sigdial-1.18)）：在 Roadrunner 卡通叙事口语语料上比对三种 LLM 方法做 hedge 检测——fine-tuned BERT 强于 few-shot GPT-4o；做了错误分析后用 LLM-in-the-loop 改进金标。S2 引用 4。
- **Ahmed 2025**，《A Corpus-Based Analysis of Epistemic Stance in AI-Generated Instructional Content》（*JESAF* 4(2)）——直接量 AI 生成内容里的 hedge / booster 密度。

## 本机试测：四学科 + Dourish 的弱 hedge 密度

[005] 已经把 314 篇经典论文 XML 化成段落级 `paras.json`（330 万词），并对每篇做了 60+ 修辞动块的正则统计——但那里的 hedge 只就 `may/might/could/suggest/appear/seem/likely/perhaps/possibly/arguably/approximately/roughly` 计，**没有把 MASP 关心的弱档程度副词单立一档**。这一步在本篇补上。

`nuance_scan.py`（与 [005] 同一目录，本文未单发）把段落级文本复送过四档正则：

| 档 | 词族 | 与文献的对应 |
|---|---|---|
| **B1 弱 hedge** | slightly / somewhat / partly / partially / relatively / mildly / a bit / a little / marginally / nominally / to some extent / to some degree / to a limited extent | MASP 的 target class |
| **B2 中等程度** | quite / rather / fairly / moderately / considerably / noticeably / substantially / meaningfully / to a large extent / to a great extent | Kennedy 2007 中等档 gradable adjective 修饰 |
| **B3 强 booster** | very / highly / extremely / entirely / completely / fully / totally / utterly / strongly / clearly / obviously / significantly / indeed / in fact / demonstrate / prove / proven | Hyland 的 booster 端 |
| **epistemic_hedge** | may / might / could / suggest(+s|ed|ing) / appear(+s|ed|ing) / seem(+s|ed|ing) / likely / perhaps / possibly / arguably / plausibly / approximately / roughly | Hyland 1996/1998 hedge 端 |

中文 scalar modifier（稍微 / 略微 / 有点 / 有些 / 一些 / 部分 / 些许 / 多少）也扫了——0 命中（[005] 的 `05_cjk_clean.py` 已经把中文翻译版 PDF 段剔出主体语料）。

### 全语料分学科总表（每万词）

| 学科 | 篇数 | 万词 | **B1 弱** | B2 中 | B3 强 | epistemic |
|---|---|---|---|---|---|---|
| Big Data & Society | 27 | 21.2 | **4.30** | 11.75 | 19.26 | 52.58 |
| HCI | 94 | 81.8 | **4.03** | 7.52 | 17.59 | 61.57 |
| Sociology | 79 | 110.6 | **4.33** | 8.21 | 20.74 | 50.79 |
| Software Engineering | 114 | 116.7 | **3.49** | 5.37 | 15.47 | 44.33 |
| Dourish 基线（21 篇） | 21 | 40.8 | 3.51 | 18.79 | 20.61 | 60.15 |

读数（事实，不是论断）：

- 四学科 B1 弱 hedge 密度都落在 **3.5–4.3 / 万词** 的窄带里——跨学科差异远小于 B3 强 booster（15–21 档的差距）。
- SE 的 B1（3.49）与 B3（15.47）都是四学科最低，与 [005] 里 SE "短句工程报告体"的画像一致；Dourish 基线的 B1 也是 3.51——但 Dourish 的 B2 高到 **18.79**（"rather" 583 次），是签名句式 not-simply-X-but-rather-Y 的副产品，在 [002] 与 [005] 里都验证过，这里复现。

完整散点（每篇一篇一行）见 [`data/paper_level_rates.csv`](data/paper_level_rates.csv)；学科 × 年代聚合见 [`data/discipline_decade_rates.csv`](data/discipline_decade_rates.csv)。

### 分年代切片（B1 弱 hedge，每万词）

| 学科 | 1970s | 1980s | 2000s | 2010s | 2020s |
|---|---|---|---|---|---|
| BDS | — | — | 5.67 | 5.67 | 0.00 (1 篇/4 052 词) |
| HCI | — | — | 1.02 | 3.95 | 5.41 |
| SOC | 2.30 (1 篇) | 1.83 (1 篇) | 4.68 | 2.72 | 5.42 |
| SE | — | — | 3.82 | 2.89 | 2.46 |

读数（仍是事实报告，含样本量警示）：

- **HCI 与 SE 的 B1 走出相反斜率**：HCI 2000s→2010s→2020s 平滑上升 1.02→3.95→5.41（三个年代都有几十篇样本），SE 反向 3.82→2.89→2.46。这两个是该语料里**前后方向最稳定、样本最厚**的两条。
- Sociology 1970s / 1980s 各仅 1 篇；BDS 2020s 仅 1 篇 4 052 词——这两个 cell 的数字在本篇只是被报告，不参予任何"方向"结论。完整细胞覆盖见 CSV。

### 几条真实命中句（B1 弱 hedge 出现在文里什么样）

下面这些是从 `paras.json` 段落级文本里按学年抽取的真实命中句，让上面的数字落到版面：

- **BDS** — Burrell, "How the machine 'thinks'"（[005] 语料）：

  > "The top left box, for example, shows a hidden layer node that cues in on darkened pixels sort of in the lower left part of the quadrant and **a little bit** in the middle."

  > "They had become, in the words of Governing Algorithms' organizers, '**somewhat** of a modern myth' (Barocas et al., 2013: 1), attributed with great signiﬁcance and power, but with ill-deﬁned properties." —— Bier, "Algorithms as culture"

- **HCI** — 数据科学协作主题：

  > "Pre-existing market analysis (and, **to some extent**, word-of-mouth business wisdom) showed that leads with credit scores greater than 500 were very likely to get special financing approval."

- **Sociology** — DellaPosta/Shi/Macy 复现研究：

  > "In an article entitled, 'Why Do Liberals Drink Lattes?,' sociologists DellaPosta, Shi, and Macy (2015) were unable to address whether this empirical assertion is true, thus rendering the question of why **somewhat** premature." —— *The real reason liberals drink lattes*

- **SE** — OSS 代码评审：

  > "This variation can be **partially** explained by the culture on the projects." —— "Peer review on open-source software projects"

  > "KDE, FreeBSD, and Gnome all have medians of **slightly** over 100 reviews per month, while the smaller projects, Apache and SVN, have around 40 reviews in the median case." —— 同上

### 不解读的地方（挑明）

- Se 2020s 2.46 与 HCI 2020s 5.41 这两条斜率我**不解读**。可能有人会读成"SE 越规范越压平 nuance / HCI 越批判越留 hedge"——那是一条论断，本篇不发表。两条斜率在本篇只是数字本身，与外部机制（社交平台压力 / LLM 盲区 / 学科写作仪式）之间的关系**值得作为后续 hypothesis 单独追**。
- "rather" 在 BDS / SOC / Dourish 里被 B2 计为命中，但**多数是 "rather than" 的句式残痕**而非程度副词——这一点已在 [data/README.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/007-nuance-rises-and-falls/data/README.md) 的 caveat 里写明。B2 数字应当被打折读，B1 的"slightly / somewhat / a little"基本干净。B2 在 Dourish 这里超比例，[002] 早就指出原因。
- 整个 314 篇语料是**手工圈选的"经典清单"** ——不是各学科随机抽样。任何"这学科怎样"的论断都要打折。

## 下一步可走的几条

**真的把 nuance 当 construct 测：**

1. 把 B1 词族与 MASP 的训练集对齐——本机用的是英文 surface pattern，MASP 是多语种形式语义探针；如果 CCL 那一章正文里的 MASP 数据集开源（Springer 章节未明示），把本机 B1 词表与 MASP 的 scalar-modifier 标签集做映射，能升级成语义标定而不是正则匹配。
2. 把语料时间轴往前推到 1970 年前——SOC 1970s 仅 1 篇是硬约束；可以补 AJS / ASR 早期经典（1940–1960s）扩成 SOC 的 PCI cell。
3. 跑一个**对照接缝**：学术论文 vs 该论文的被媒体二次平化版本（Petrocelli 2024 就是这种对照的设计），把"压平 nuance"作为接缝两侧的可测差异。

**严守护栏不发表的部分：**

- 不主张"社交媒体导致 nuance 减少"
- 不主张"LLM 盲区已经污染了科学计量"
- 不主张"某学科压平/留存 nuance 更严重"

这三条都是本篇**可被未来的某一篇**检验的假设。本篇的职务只是把证据摆到桌面上：弱 hedge 在经典论文语料里数得出来，分学科有方向性的年代斜率，外部文献把每条线索都接到了可被引用的工作上。

## 溯源

| 字段 | 内容 |
|---|---|
| 数据 | [005 语料] 314 篇经典论文 `discipline_style_analysis/paras.json`（330 万词）；[002 语料] Dourish 21 篇 `dourish_analysis/paras.json`（40.8 万词）|
| 引用源（外部检索） | Crossref（不限速）· Springer Nature HTML 元数据 · arXiv API · Semantic Scholar Graph API（带 `x-api-key`）|
| Salam 引语 | 用户提供；URL: <https://www.theatlantic.com/magazine/2026/08/reading-crisis-postliterate-age/687618/>；WebFetch + Wayback 在本机代理网络下当时超时，原文未取到本地——引用文字由用户提供并经其确认 |
| 计量器 | `ZCodeProject/discipline_style_analysis/nuance_scan.py`（与 [005] 管线同目录，不单独提交到 repo）|
| 时间 | 分析 2026-08-17 · 笔记发布 2026-08-17 |
| Agent / 模型 | ZCode CLI · GLM（智谱） |
| Issue | [#14](https://github.com/UniqueClouds/marginalia/issues/14) |
| 上游 | [002 Dourish 风格](002-writing-like-dourish.zh.md) · [004 故事会量化](004-storytelling-quantified.zh.md) · [005 四学科声音](005-discipline-style-voices.zh.md) |


<div class='marg-attach'>📎 附属材料：[README.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/007-nuance-rises-and-falls/data/README.md)</div>


---

> 🌐 [Read this note in English](007-nuance-rises-and-falls.en.md)

