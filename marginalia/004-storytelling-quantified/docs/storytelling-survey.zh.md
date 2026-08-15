# "CHI/ACL 是故事会"的量化研究:先导调研

日期:2026-08-15
核心问题(用户原始表述拆解):
1. 什么叫"故事会"?如何把"讲故事"(storytelling / narrativity)操作化为可测量概念?
2. 论文有多"故事"?用哪些指标衡量一篇论文讲故事的水平?
3. 会讲故事真的更容易发表 / 获得更高影响力吗?
4. 能否与"语言膨胀"(hype 词通胀 + LLM 用词膨胀)结合,直接用 ACL + CHI 发表文章做语料分析?

---

## 一、一句话结论

"故事性 → 学术回报"这条线**有人做过、但从未在 CS 顶会语料上做过**:
- 在生物医学/气候学/综合期刊上,promotional language 与叙事风格确实与引用、资助、关注度正相关(Hillier 2016;Peng 2024;Qiu 2024;Stavrova 2025);
- 但在 AI 会议语料上出现了**反例**:Vincent-Lamarre & Larivière (2021) 发现被录用的 AI 投稿**可读性更低、技术词汇更多**——"故事溢价"可能是场域依赖的;
- **没有人定义并测量过 CHI/ACL 论文的"故事性指数",没有人做过 CHI vs ACL 的跨场域对比,更没有人把故事性 × hype 通胀 × LLM 用词膨胀放在一个时间序列里**。这是一个干净的可做空白。

---

## 二、用户提到的 Sophie Qiu:已定位

Sophie Qiu = **Huilian Sophie Qiu**(邱惠莲,音译),CMU 软件与社会计算方向博士(2022,导师 Christian Kästner / Bogdan Vasilescu,早期研究 code review 中的冲突与毒性),现于 Northwestern University 与 **Brian Uzzi** 合作做计算社会科学。她的 promotional language 研究线:

| 论文 | 场所 | 数据 | 核心发现 |
|---|---|---|---|
| Use of Promotional Language in Grant Applications and Grant Success | **JAMA Network Open 2024**(Qiu HS et al., Uzzi lab) | 11,535 份医学基金申请书 | promotional language 占比与获资助显著正相关,OR = 1.47 (95% CI 1.25–1.71) |
| Effect of Promotional Language in Academic Papers | **IC2S2 2025** poster(Qiu, Yu, Uzzi) | 学术论文 | 论文层面 promotional 语言的影响(她最接近本 topic 的工作) |
| Who Uses Promotional Language in Grants and Grant Success | **Metascience 2025** | 基金 | 谁在用 promotional 语言(分层分析) |

同一条 Uzzi-lab 线上还有:
- **Peng H. et al. 2024, PNAS** "Promotional language and the adoption of innovative ideas in science"(121(25): e2320066121):申请书里 promotional language 占比高,获资助概率最高翻倍,且与创新思想的采纳率相关。
- **Stavrova O., Kleinberg B., Evans A. M., Ivanovic M. 2025**, Nature Humanities & Social Sciences Communications "Scientific publications that use promotional language in the abstract receive more citations and public attention"(预印本 PsyArXiv 2024):Science/Nature/PNAS 1991–2023 共 13 万+ 摘要,promotional language 预测更高引用、全文阅读量、社交媒体提及与 Altmetric;并且**男性使用 promotional language 获得的回报更高,性别差距反而扩大**。

> 注意区分:promotional language(hype 词,如 novel/robust/unprecedented)只是"讲故事"的一个维度(夸张度),不是叙事结构本身。这是文献里已经做烂的维度;**叙事结构维度在 CS 会议语料上基本没人做**——这是机会。

---

## 三、相关文献地图(六条线)

### 线 A:hype / promotional language 的通胀与回报(最成熟的一条线)

| 研究 | 数据 | 发现 |
|---|---|---|
| **Vinkers, Tijdink & Otte 2015**(PLOS ONE;Nature 新闻报道) | PubMed 摘要 1974–2014 | 25 个正面词(novel, robust, unprecedented, innovative…)相对频率增长约 9 倍;"novel" 通胀的经典起点 |
| NIH 基金 hype 研究(2022, PMC9412227) | NIH 申请书摘要 | 中标申请书里 hype 语言同样随时间上涨 |
| Mishra & Diesner(ISSI 2023 → QSS)"A probabilistic model of hype" | 生物医学摘要 | 用生成式概率模型检测 hype 引发的修辞偏移(rhetorical shift),方法可移植 |
| Scientometrics 2023 "Presence and consequences of positive words" | 科学摘要 | 正面词与引用、资助正相关——通胀被制度奖励强化 |
| Peng 2024 PNAS;Qiu 2024 JAMA Netw Open;Stavrova 2025 | 见上节 | 回报证据 + 性别异质性 |

### 线 B:叙事性(narrativity)→ 学术影响(方法上最值得直接复用的一条线)

- **Hillier, Kelly & Klinger 2016, PLOS ONE** "Narrative Style Influences Citation Frequency in Climate Change Literature"——**本 topic 最重要的方法模板**。732 篇气候变化论文摘要,众包 7 人/篇打分,六个叙事元素合成 narrativity 指数:
  1. **Setting**(具体时间/地点)
  2. **Narrative perspective**(第一人称叙述者)
  3. **Sensory language**(感官/情绪语言,按长度归一)
  4. **Conjunctions**(因果/转折/时间连词密度)
  5. **Connectivity**(相邻句之间的显式词汇衔接)
  6. **Appeal**(对读者的显式呼吁/行动建议)
  PCA 第一主成分解释 76.5% 方差;6 元素中 4 个(sensory、conjunctions、connectivity、appeal)与引用量正相关;回归(年份+narrativity+作者数+IF)解释 41% 引用方差。**关键教训**:narrativity 与期刊影响因子 R²=0.62——叙事风格与场域强混淆,做 CS 语料时必须做 venue/topic 固定效应。
- **Green & Brock 2000** narrative transportation(叙事传输理论):心理学理论基础,量表可借用。
- **JCOM 2026** "What makes a good story?"(science communication 期刊):narrative depth → transportation/参与度,最新延续。

### 线 C:写作风格 → 会议"录用"(证据最少、也最有意思的一条线)

- **Vincent-Lamarre & Larivière 2021, QSS** "Textual analysis of artificial intelligence manuscripts reveals features associated with peer review outcome"(arXiv 1911.02648):OpenReview 有录用标签的 AI 会议投稿——**被录用稿件在两个可读性指标上得分更低、技术/科学词汇更多**。与"故事会"直觉相反:至少在 AI 会议,"讲人话"不加分。⚠️ 但注意:可读性 ≠ 叙事性,这是两个维度,该文没测叙事结构。
- CHI 官方数据:CHI 2024/2025/2026 录用率 26.4% / 24.9% / 25.3%,revise-resubmit 二次录用约 64–65%(chi2024–2026.acm.org 官方 Post-PC 报告)。
- Wobbrock 短文 "Reject me: peer review and SIGCHI":CHI 拒稿文化与大基数拒稿的批评。
- 录用预测的 ML 练手项目不少(Stanford CS229 等),学术价值低,略。

### 线 D:"故事会"作为社区话语(norm 侧证据)

- 知乎问题 "**ACL 为什么叫故事汇?**"(zhihu.com/question/646340702,2023):中文 NLP 社区对该 meme 的原始讨论(含对 Lamport《How to write a 21st century abstract》式"讲好故事"的反思)。可作为 RQ0 话语分析素材。
- **CHI EA 2025** "How do design stories work? Exploring narrative forms of knowledge in HCI"(DOI 10.1145/3706599.3706717):HCI 已把 narrative 当作**认识论资源**(scenarios、design fiction、personas)正面研究——CHI 的"故事"不完全是贬义,这本身构成 CHI/ACL 对比的张力。
- Lennart Nacke 的 "How to write a CHI paper" 课程/Substack 及其与 Regan Mandryk、Jofish Kaye 的访谈:CHI 写作文化公开传授"叙事弧"——**CHI 社区明文把 storytelling 当技能训练**,这是"场域规范"的直接证据。
- arXiv 2401.05818 "How to write a CHI paper (asking for a friend)":自嘲式复刻 CHI 文体的元论文,可作 CHI 文体规约的语料。
- Cliff Lampe(Medium)"What makes research a contribution to CHI?":贡献标准与社区叙事的关系。

### 线 E:计量工具箱(现成可组装)

| 工具/框架 | 用途 |
|---|---|
| **Swales CARS 模型**(1990,Genre Analysis)| 引言"三步走":establishing a territory → establishing a niche → occupying the niche。学术"故事"的经典修辞学操作化 |
| CODI Workshop 2024(ACL Anthology 2024.codi-1.7)| 对 CARS 三 move 的量化指标 |
| MDPI Electronics 2025 "Automatic Detection of the CaRS Framework" | CARS move 的自动检测(NLP) |
| **Coh-Metrix**(Graesser, McNamara et al.)| 自带 narrativity 指数(主成分),经典文本计量工具 |
| **Reagan et al. 2016, EPJ Data Science** | 情感弧六基本形状(rags-to-riches、man in a hole、Cinderella 等),hedonometer 词表 + SVD;有开源实现 |
| EmotionArcs(ACL 2024 LaTeCHCLfL, 2024.latechclfl-1.7)| 9000 文学文本情感弧工具,可迁移 |
| Brysbaert concreteness norms(40k 词)| 感官/具体性维度 |
| Hyland hedging/boosting 词表;Vinkers 25 正面词;Peng/Qiu promotional 词典 | 膨胀与模糊/强化语 |
| **Beese, Altunbaş, Güzeler & Eger 2023, Royal Society Open Science** "Did AI get more negative recently?"(arXiv 2202.13610)| 4.1 万篇 NLP/ML 论文 35 年,SciBERT 分类 positive/negative stance:**整体越来越正面**("提出新方法打败 SOTA"型),但负面型论文(critique 型)引用更高。直接可在 ACL 语料上扩展 |

### 线 F:语言膨胀 × LLM 时代(时间轴的新变量)

- **Kobak, González-Márquez, Horvát & Lause 2025, Science Advances** "Delving into LLM-assisted writing in biomedical publications through excess vocabulary"(arXiv 2406.07016):1500 万 PubMed 摘要的 excess vocabulary 分析,2024 年生物医学摘要**至少 13.5% 经 LLM 处理**,部分子领域/国家 30–40%;delve、intricate、pivotal 等词超额出现。
- "Why Does ChatGPT 'Delve' So Much?"(arXiv 2412.11385):LLM 词偏好来源分析。
- Liang et al. 2024(arXiv 2403.07183)对 ICLR 2024 审稿的同类分析:≥16.9% 审稿意见含 LLM 修改痕迹(注明:此条为本 session 未逐一核验的记忆引用,使用前请核对原文数字)。
- CHI 2025 论文 "LLM or Human? Perceptions of Trust and Quality in Research Summaries":读者把 "delve" 类词识别为 LLM 风格线索并影响信任判断。
- 与本 topic 的接口:**如果 2023 年后"叙事模板 + 膨胀词"同时上升,则"故事会"可能正在变成"AI 模板故事会"**——语言膨胀给 storytelling 趋势研究提供了天然的时间断点(regression discontinuity at ChatGPT release)。

---

## 四、差距分析(可发表的空白)

- **G1 场域空白**:narrativity 从未被测量于 CS 顶会语料。Hillier 是气候学期刊、Stavrova 是三大综合期刊、Qiu/Peng 是生物医学。CHI(阐释型、贡献驱动)与 ACL(实证型、SOTA 表驱动)的对比是现成的自然实验。
- **G2 结果变量空白**:"录用"几乎不可直接观察(CHI 的 PCS、ACL 的 ARR 评审都不公开)。但有三条替代路:(a) **OpenReview 公开场域**(ICLR/NeurIPS 等)有 accept/reject 标签;(b) 录用论文内部分层:CHI Best Paper / Honorable Mention / oral-poster、ACL main vs Findings vs workshop、outstanding paper 奖;(c) **arXiv 预印本 vs camera-ready 的 diff**——投稿被"改故事"的量本身就是一个新测量(rebuttal 期叙事重构)。
- **G3 维度混淆空白**:可读性(Vincent-Lamarre 测的)≠ 叙事结构 ≠ hype 通胀,三个维度从未在同一语料上分解。"ACL 故事会"直觉可能是"低技术密度 + 高叙事结构 + 高 hype"的混合体,值得做因子分解。
- **G4 时间 × LLM 空白**:narrativity 时间序列 + hype 通胀 + Kobak 式 excess vocabulary 三线从未合并;ChatGPT 发布(2022-11)是天然断点。

---

## 五、测量方案草案(可直接开工)

### 5.1 论文"故事性指数"(Paper Narrativity Index)——五维

| 维度 | 具体指标 | 复用来源 |
|---|---|---|
| D1 宏观结构 | CARS 三 move 完整度与顺序;开头 hook 类型(场景/悬念问题/轶事/数据冲击);情感弧形状分类(Reagan 六弧)对引言段 | Swales;CODI 2024;Reagan 2016 |
| D2 词汇 | concreteness 均值;感官词密度;情感词;hype 词密度(Vinkers 25 + Peng/Qiu 词典);boosters/hedges 比 | Brysbaert;Hyland;线 A 词典 |
| D3 叙述者与角色 | 第一人称 we 密度;"角色"名词(participants/users/system/model)作主语的比例;agency 动词 | Hillier 元素 2 改造 |
| D4 连贯与因果 | 因果/转折/时间连词密度;相邻句语义衔接(sentence-embedding 相邻相似度 = Hillier connectivity 的自动化) | Hillier 元素 4、5 |
| D5 呼吁与承诺 | Appeal 句(we call for / our work opens);贡献句数量与强度;结果预告句("we show that …") | Hillier 元素 6 |

评分方式:**LLM-as-annotator + 人工校准**——先按 Hillier 的众包流程(每篇 5–7 人)标注 300–500 篇建立金标,验证 LLM 与人类一致性(Cohen's κ / Krippendorff α),再放量。这一步本身可发表(测量论文)。

### 5.2 数据源

| 语料 | 获取 | 结果变量 |
|---|---|---|
| **ACL Anthology** 全量(1979–2026) | 官方 data + PDF;含 main/Findings/workshop、award 标记 | 引用(OpenAlex/S2)、award、main vs Findings |
| **CHI proceedings**(ACM DL) | 元数据 + 开放 PDF(SIGCHI openTOC);OpenAlex 引用 | Best Paper/Honorable Mention 分层 |
| OpenReview(ICLR/NeurIPS 等) | API,含录用标签与评分 | 唯一能测"录用"的场域 |
| arXiv 对照 | 预印本 v1 vs camera-ready diff | "叙事重构量"新测量 |
| 知乎/Reddit/Mastodon 话语 | "故事会/故事汇"meme 语料 | RQ0 定性部分 |

### 5.3 识别与稳健性

- 主题控制:SPECTER2 embedding + topic FE(学 Hillier 的教训:narrativity–IF R²=0.62,必须去混淆)。
- venue × year 固定效应;比较"同一作者跨场域论文"。
- 相关≠因果:主分析做关联;因果留给 vignette 实验(见 5.4)。
- 循环性风险:用 LLM 标注 LLM 时代的文本,需人类金标锚定 + 报告 LLM 风格词(delve 等)的敏感度分析。

### 5.4 研究问题草案

- **RQ0(话语)**:"故事会"批评在中英文社区(知乎/Reddit/X)如何言说?针对 CHI 与 ACL 的指控是否不同?(定性,贡献 framing)
- **RQ1(测量)**:五维 narrativity 指数能否跨场域可靠测量?(测量论文)
- **RQ2(分布与趋势)**:CHI vs ACL vs NeurIPS/ICSE 的故事性分布与 30 年趋势?故事性与 hype 通胀、excess vocabulary 的联合时间序列;ChatGPT 断点前后是否跳变?
- **RQ3(回报)**:故事性 → award / main-vs-Findings / 引用的关联,**场域是否调节故事溢价(CHI > ACL?)**;与 Vincent-Lamarre 的低可读性效应对照,分解叙事性 vs 技术密度两个因子。
- **RQ4(AI 时代)**:2023 后高 LLM 痕迹论文的叙事是否模板化(弧型多样性下降)?即"AI 平庸故事"假说。
- **RQ5(实验,选做)**:招募 CHI/ACL 评审员做 within-subject vignette 实验——同一研究内容的 intro 改写为高叙事 vs 中性版本,测评分差(参考 Stavrova/Kleinberg 的实验风格)。

### 5.5 可投场所

CHI(论文本身是 HCI 元科学)/ CSCW / IC2S2 / Metascience 2026 / QSS / Scientometrics;ACL 侧:NLP+CSS 类 workshop。与既有议程的接口:可并入 CSS 方向作为 NS 系列之外的新提案;与 [[research-agenda-proposals]] 的"AI 改变知识生产"主线同构。

---

## 六、关键文献清单(带链接)

1. Hillier, Kelly & Klinger 2016, PLOS ONE — Narrative Style Influences Citation Frequency in Climate Change Literature. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0167983
2. Qiu HS et al. 2024, JAMA Network Open — Use of Promotional Language in Grant Applications and Grant Success. https://pubmed.ncbi.nlm.nih.gov/39661389/ (PMC11635532)
3. Peng H. et al. 2024, PNAS — Promotional language and the adoption of innovative ideas in science. https://www.pnas.org/doi/10.1073/pnas.2320066121
4. Stavrova, Kleinberg, Evans & Ivanovic 2025, Nat. HSSC — …receive more citations and public attention. https://www.nature.com/articles/s44271-025-00293-8 (预印本 https://europepmc.org/article/ppr/ppr882316)
5. Qiu, Yu & Uzzi 2025 — Effect of Promotional Language in Academic Papers. IC2S2 2025(https://ic2s2-2025.org/program/);Metascience 2025 版 https://nomadit.co.uk/conference/metascience2025/paper/90996
6. Vincent-Lamarre & Larivière 2021, QSS — Textual analysis of AI manuscripts… https://direct.mit.edu/qss/article/2/2/662/97556 (arXiv 1911.02648)
7. Vinkers, Tijdink & Otte 2015, PLOS ONE — positive words in PubMed abstracts(Nature 报道 https://www.nature.com/articles/nature.2015.19024)
8. Mishra & Diesner — A probabilistic model of hype. ISSI 2023 / QSS https://direct.mit.edu/qss/article-pdf/doi/10.1162/QSS.a.482/
9. Beese et al. 2023, RSOS — Did AI get more negative recently? https://arxiv.org/abs/2202.13610 (10.1098/rsos.221159)
10. Reagan et al. 2016, EPJ Data Science — The emotional arcs of stories. https://link.springer.com/article/10.1140/epjds/s13688-016-0093-1
11. Kobak et al. 2025, Science Advances — Delving into LLM-assisted writing… https://arxiv.org/abs/2406.07016
12. Why Does ChatGPT "Delve" So Much? https://arxiv.org/html/2412.11385v1
13. CHI EA 2025 — How do design stories work? https://dl.acm.org/doi/10.1145/3706599.3706717
14. CODI 2024 — Quantitative Metrics to the CARS Model. https://aclanthology.org/2024.codi-1.7.pdf ;MDPI Electronics 2025 自动 CARS 检测 https://www.mdpi.com/2079-9292/14/14/2799
15. CHI 官方录用统计:CHI 2026 https://chi2026.acm.org/2026/02/06/insights-into-the-papers-track-post-pc-meeting-outcomes/ ;CHI 2025 https://chi2025.acm.org/chi-2025-papers-track-post-pc-outcomes-report/ ;CHI 2024 https://chi2024.acm.org/2024/01/29/chi-2024-papers-track-post-pc-outcomes-report/
16. 知乎 — ACL 为什么叫故事汇? https://www.zhihu.com/question/646340702
17. Wobbrock — Reject me: peer review and SIGCHI. https://faculty.washington.edu/wobbrock/pubs/chi-12.07.pdf
18. Nacke — How to write a CHI paper. https://lennartnacke.substack.com/p/how-to-write-a-chi-paper ;元论文 arXiv 2401.05818 https://arxiv.org/html/2401.05818v1
19. JCOM 2026 — What makes a good story? https://jcom.sissa.it/article/pubid/JCOM_2503_2026_A06/
20. LLM or Human? CHI'25 https://dl.acm.org/doi/10.1145/3772318.3793386
