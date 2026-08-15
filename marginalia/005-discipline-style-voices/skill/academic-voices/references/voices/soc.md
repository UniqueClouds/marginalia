# Voice: Sociology（AJS / ASR / BJS 理论统计学家体）

基线：79 篇（AJS 34 / ASR 12 / BJS 11），110.6 万词，1975–2026。报告：`ZCodeProject/学科风格分析_3_Sociology.md`。
画像：**与韦伯和 GSS 同时对话的理论统计学家**——论文最长（1.4 万词/篇），散文肌理四学科最松弛（敢用破折号、缩写词、scare quotes），证据句式是 "consistent with / net of / Model 1→3 阶梯"。

## 目标密度（每千词；voice_check.py --voice soc）

| 指标 | 基线 | 说明 |
|---|---|---|
| 平均句长 | 23.6 词（P50=18） | 中位短、尾部长——方差最大 |
| 破折号 | **3.5** | 四学科第一（插入语随时打断句子） |
| 缩写词 | **0.74** | 四学科唯一普遍使用（theory prose 允许 don't/can't） |
| 弯引号 | 5.6 | scare quotes 之冠（"illegals"、"latte liberals"） |
| in other words | 0.043 | 四学科第一（理论→白话复述对） |
| consistent with | 0.15（45/79 篇） | 证据句式 |
| net of | 0.028（13/79 篇，他科为零） | 净效应咒语 |
| we / our / I | 5.2 / 1.8 / 1.6 | we use > we observe > we argue |
| 被动 be+V-ed | 6.5 | 四学科最低——研究者主动操作数据 |
| this article | 0.23 | 期刊自称（正文 we，AJS 摘要 the authors） |
| 分号 | 4.4 | 与 BDS 同档 |

## 词汇场
关系术语：homophily, brokerage, dyads, ties, diffusion, contagion, small world, network, cohesion, niche, field。方法论：net of, fixed effects, robustness, odds ratio, Model 1–3, GSS/ANES。经典对话：Durkheim/Weber/Merton/Granovetter 与当代方法家（Snijders/Breiger）同页出现——开头引 Durkheim 定调，方法节引 Snijders 落地。引用：author-date（16/万词）。

## 结构仪式
- **AJS 摘要第三人称**：正文满篇 we，摘要强制 "The authors examine... They find..."（投稿 AJS 必改；ASR/BJS 不用）。
- **开篇**：epigraph 对置（一条经典引语 + 一条俗世文本，不解释）或三连问（把领域问题重述一遍）。
- **理论节**："Drawing on X, we argue that..."；与在世学者正面对话（"contra their interpretation..."）。
- **结果节**：模型阶梯叙事——"Model 1 shows... Adding network measures (Model 2)... consistent with H2"。
- **收尾**：limitations + 未来研究方向（理论抱负收口）。

## 改写配方（S1–S6）

**S1 AJS 摘要第三人称化**
- before: "We analyze 22,572 correlations from the GSS. We find that lifestyle politics..."
- after: "The authors analyze 22,572 pairwise correlations from the General Social Survey (1972–2010). They find that lifestyle politics..."

**S2 epigraph 对置**（intro 前无标题引块；只用用户已有的真实材料）
- 模板：`[经典理论引语]\n[竞选广告/新闻/访谈原话]` ——两段引语气质相斥，不解释，正文首段再接。

**S3 in-other-words 复述对**（理论断言后）
- before: "Homophily amplifies initial preference."
- after: "Homophily amplifies initial preference. In other words, a small elective affinity — once compounded over generations of network formation — can harden into the appearance of deep cultural division."

**S4 证据句式**
- before: "Our regression proves the effect."
- after: "The association persists net of demographic covariates (Model 3, Table 2), consistent with H2."

**S5 模型阶梯叙事**
- 模板：`Model 1 establishes the baseline... Model 2 adds [关键变量]... Model 3 reports the full specification, robust to alternative measures of X.`

**S6 标题**
- 模板：`[隐喻主标题]: [机制]副标题`（副标题可含年代范围——*...Lynching in the Deep South, 1882–1930*）
- 隐喻库：The Hidden Abode / Bending with the Wind / The Emperor's Dilemma / Leviathan

## 反模式（改稿时删除）
- 数字引用 [12]（改 author-date 括注）
- "We present..." / "In this paper, we present"（会议腔）
- design implications / RQ 编号 / threats to validity（换 limitations）
- 破折号恐惧症：插入语用破折号而非括号；缩写词保留（理论散文肌理）
- 把 hedge 当装饰：判断交給 "consistent with"，事实直说
- "A Study of..." 标题
