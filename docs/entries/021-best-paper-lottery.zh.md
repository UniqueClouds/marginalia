# 重跑一遍，一半论文会换人——Best Paper 的随机性与「不丑」的底线

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](021-best-paper-lottery.en.md)
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-021</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>重跑一遍，一半论文会换人——Best Paper 的随机性与「不丑」的底线</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-09-06</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-09-06</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>research memo（研究备忘）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>50</td></tr></table></details>


# 重跑一遍，一半论文会换人——Best Paper 的随机性与「不丑」的底线

> 研究备忘：核心问题是**「优秀/Best Paper 的定义能否形成共识」**。注意两个 construct 必须分开——NeurIPS 重复评审实验测的是「录用/拒稿边界」的随机性，不能直接当「奖项层随机」的证据；奖项层要用奖项层的数据（Wainer 0.72、MISQ 5/22、各会政策原文等，见想法 3）。旧版论证文见 git 历史；引用已于 2026-09-07 全量搜索核验，记录见文末。

## 核心想法

1. **构造 A（基线）：录用边界的随机性**——NeurIPS 2014/2021 重复评审：决策不一致 23–26%，accept precision ≈50%；回访：被接收论文评分与引用零相关。这是「及格线附近是噪声」，不是「奖项随机」。
2. **构造 B（真问题）：奖项层「好」的定义与共识**——best paper 有信号但远非共识（P(best>随机)=0.72）；事后评奖显著更准（追认效应）；各会对 "Best" 的定义互相不可通约（ACL 明文争议条款 / CHI 自认无标准 / ACM MM 配额制）。
3. **「不丑」是真实存在的一致带**——贝叶斯重分析：基本质量判据满足率 ≈56%（CI 0.34–0.83）；判据之下的论文被稳定拒绝——可辩护下限集合成立（NOTUGLY-P 的落点）。
4. **争议作为常态**：获奖即争议（BERT、Bender & Koller、ICLR 2017 Dietterich 公开反对）；中英社区话语可按晒分偏差模板做。
5. **ToT = 事后追认的制度**：经典论文当初被拒的一手案例（WFQ、GraphLab）+ 被拒经典系统研究（Gans & Shepherd、Campanario）；「ToT 名单 × 当初评分」对账仍无人做过 = gap。

## 想法 × 材料

### 想法 1 · 构造 A：录用边界的随机性（基线数据）

- **[NeurIPS 官方博客: The NeurIPS 2021 Consistency Experiment](https://blog.neurips.cc/2021/12/08/the-neurips-2021-consistency-experiment/)**（2021-12-08，程序主席 Beygelzimer (Yahoo Research)、Dauphin (Google Brain)、Liang (Stanford)、Wortman Vaughan (Microsoft Research)）——8,820 篇中 10% 双委员会独立评审：不一致 23.0%（203/882）；accept 翻转 50.6%（2014 为 49.5%）；oral+spotlight 阈值下两委员会分别录 29 与 25 篇、**共识仅 3 篇**（Results 节原文）。
- **[arXiv:2306.03262](https://arxiv.org/abs/2306.03262)**（同四人，2023）——正式论文 "Has the Machine Learning Review Process Become More Arbitrary as the Field Has Grown? The NeurIPS 2021 Consistency Experiment"；Table 1 = 882 篇推荐矩阵；§4.3 有 oral/spotlight 共识数据与伦理 flag 平行数据（23 vs 22，交集仅 3）。
- **[arXiv:2109.09774](https://arxiv.org/abs/2109.09774)**（Cortes (Google Research) & Lawrence (University of Cambridge)，2021）——"Inconsistency in Conference Peer Review: Revisiting the 2014 NeurIPS Experiment"：评分方差约 50% 是主观成分；被接收论文评分与引用量零相关；结论原话 "good for identifying poor papers, but poor for identifying good papers"。
- **[arXiv:1507.06411](https://arxiv.org/abs/1507.06411)**（**Olivier François，单作者**，Université Grenoble-Alpes / CNRS, TIMC-IMAG，2015）——"Arbitrariness of peer review: A Bayesian analysis of the NIPS experiment"：隐藏参数（满足基本质量判据的概率）估计 **56%**，95% CI (0.34, 0.83)。**注意：**「reject-or-flip-a-coin / 拒绝或掷币」是本词条自拟的简称，原文没有这个词——原文只描述「质量关之后掷偏币，成功概率 π/x」。
- **[Shah et al., JMLR 2018](https://jmlr.org/papers/v19/17-511.html)**——Nihar B. Shah (UC Berkeley，时任)、Behzad Tabibian (MPI Tübingen)、Krikamol Muandet (MPI)、Isabelle Guyon (ChaLearn)、Ulrike von Luxburg (Tübingen & MPI)。"Design and Analysis of the NIPS 2016 Review Process." *Journal of Machine Learning Research* 19(49): 1–34（preprint arXiv:1708.09794）。

### 想法 2 · 构造 B：奖项层的信号与追认（本词条的主战场）

- **[Wainer, Eckmann & Rocha 2015, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118446)**——"Peer-Selected 'Best Papers'—Are They Really That 'Good'?"（Wainer & Rocha: Unicamp；Eckmann: UFRGS）。**迄今最直接的奖项 vs 随机检验**：P(best paper 引用数 > 同会随机论文) = 0.72（Scopus）/ 0.78（Google Scholar）；51% 的 best paper 落在本会前 10% 高引——奖项层有信号，但 0.72 ≠ 1，远非共识。
- **[Wang 2024, Scientometrics](https://doi.org/10.1007/s11192-023-04881-5)**——"Comparison of citation impact between pre- and post-publication peer-selected best papers"（CS 会议 299 对配对）：看得到实际影响后选出的 best paper 显著更常胜出（P 最高 0.79）——**追认效应**的直接证据。
- **[Dutchak, Tseng & Grover, CAIS](https://aisel.aisnet.org/cgi/viewcontent.cgi?article=4055&context=cais)**——"Winning Awards or Winning Citations"（MIS Quarterly 数据）：1993–2014 年 MISQ 年度最佳论文只有 **5/22** 同时是当年前五高引；获奖文偏「 revelatory（新）」、高引文偏「incremental（稳）」——奖项与共识系统性错位。
- **Lemus（Northwestern，working paper）**：[Best paper awards and uncertainty of innovation](http://gradstudents.wcas.northwestern.edu/~jal941/BestPaperAward.pdf)——ex-ante best paper 平均位于引用分布 75 分位，ex-post classic paper 位于 95 分位。
- **[mako hill 2018 博客综述](https://mako.cc/copyrighteous/awards-and-citations-at-computing-conferences)**（Univ. of Washington）——「best paper 与引用无关」这一社区流传说法的来源（Bartneck & Hu, CHI 2009 null result）及其后被 Wainer 2015 等推翻的过程——社区对奖项的直觉互相矛盾的现成梳理。

### 想法 3 · 各会对「Best」的定义不可通约（政策原文）

- **[ACL Awards Policy](https://www.aclweb.org/adminwiki/index.php/ACL_Conference_Awards_Policy)**（现行版；页面未标"2025 年"）——原句：'We define "Best" as work that is particularly **fascinating, controversial, surprising**, impressive, and/or potentially field-changing.' 另有量化条款：Best ≤ 录用数的 0.25%（录用 <2000 篇时上限 6 篇）。
- **[CHI 2020 Awards 页](https://chi2020.acm.org/for-attendees/awards/)**——官方自认：'Given the diverse ways in which submissions can contribute to the field of HCI, **there is no formal selection criteria for Best Papers at CHI**.'（流程：AC 提名前 5% → Best Paper Committee 选前 1%。）
- **[NeurIPS 2021 Award Recipients 公告](https://blog.neurips.cc/2021/11/30/announcing-the-neurips-2021-award-recipients/)**——标准 "excellent clarity, insight, creativity, and potential for lasting impact"；流程 62 篇初选池 → 三轮筛到 6 篇；原话 'While there is of course **no perfect process** for choosing award papers'。
- **[ACM MM Award Policy](https://acmmm.org/files/ACMMMAwardPolicy_2025.pdf)**——配额制：5% Outstanding + 1% Best，按 topic 配额，Best 只能从 Outstanding 顶格中选。

### 想法 4 · 争议作为常态（可核查的获奖争议案例）

- **BERT × NAACL 2019**：抱怨原话见 **[Forbes: The PhD Metagame](https://www.maxwellforbes.com/phd-metagame)**（Maxwell Forbes，2025-03-15；"the postdocs I talked to universally grumbled about it... 'It just scaled some stuff up.'"）；HN [id 43398816](https://news.ycombinator.com/item?id=43398816) 是引述该文的一条评论（在 "The PhD Metagame" 讨论串内，2025-03-18），非独立争议帖。
- **Bender & Koller 2020**：[ACL 2020 论文页](https://aclanthology.org/2020.acl-main.463/)——精确奖项名是 **Best Thematic Paper Award**（非「最佳论文」）；获奖争论综述：[Julian Michael, "To Dissect an Octopus"](https://julianmichael.org/blog/2020/07/23/to-dissect-an-octopus.html)（2020-07-23）与 [TeachingNLP 2024 "Occam's Razor and Bender and Koller's Octopus"](https://aclanthology.org/2024.teachingnlp-1.18/)。
- **ICLR 2017**：[Understanding deep learning requires rethinking generalization](https://openreview.net/forum?id=Sy8gdB9xx) 获 Best Paper，Thomas Dietterich 在 OpenReview 公开评论："the results in this paper are completely unsurprising... I'm shocked that at least one reviewer thought this was ground breaking"（可经 [UBC MLRG 讲义](https://www.cs.ubc.ca/labs/lci/mlrg/slides/understanding_deep_learning.pdf)转引）。
- 中文圈：[量子位 IJCAI 2019「审稿宇宙最烂」](https://www.qbitai.com/2019/05/2282.html)；[腾讯云社区 CVPR 2019「金酸莓奖」](https://cloud.tencent.com/developer/article/1460113)；[TrueSight IJCAI 2025「学术抽奖」](https://tsight.io/articles/16396475)（5,404 投稿、1,042 录取、19.3%）。
- **晒分偏差的原始论文已找到**：[arXiv:2509.16831](https://arxiv.org/abs/2509.16831)——Zhu（Texas A&M）、Yin（Cornell）、Zhang（Texas A&M），"Survivors, Complainers, and Borderliners: Upward Bias in Online Discussions of Academic Conference Reviews"（五届会议、知乎+Reddit；ARR 均分样本比总体高 0.489，+18.6%，p<0.001）。「1,261 帖」数字出自 [yanfajia 报道](https://www.yanfajia.com/news/6470.html)（论文正文未直接定位到该数，引用时数字挂报道、结论挂论文）。

### 想法 5 · ToT = 事后追认的制度

- **[SIGIR Forum 51(2) 2017 专刊](https://sigir.org/forum/issues/july-special-issue-2017/)**（Harman & Kelly 编；Overview PDF）——专刊 Awardees 栏为 **26 篇**回访（1978–2001 共评出 30 篇，59 提名池三人组评分取前 30；方法说明见 [SIGIR ToT 页](http://sigir.org/awards/test-of-time-awards/pre-2002-recipients/)）。**旧版写「21 篇」有误。**
- **[Paxson, McKeown & Rexford 2009](https://doi.org/10.1145/1517480.1517488)**——"Selecting the 2008 SIGCOMM Test-of-Time Award Winner(s)." **ACM SIGCOMM Computer Communication Review 39(2): 40–41**（Paxson: ICSI；McKeown: Stanford；Rexford: Princeton）——两个 landmark 候选无法分出高下，三篇共享。**旧版误记为 SIGIR Forum。**
- **[Keshav, CCR ToT 回顾](https://ccronline.sigcomm.org/wp-content/uploads/2019/10/acmdl19-331.pdf)**（Waterloo）——一手案例：WFQ 论文被 SIGMETRICS 1989 拒稿（评审原话逐字保留："I recommend that the paper be rejected"），转投 SIGCOMM 1989 后成经典并获 ToT。
- **[Gonzalez 2023: How our Test-of-Time Paper Almost Wasn't](https://frontierai.substack.com/p/how-our-test-of-time-paper-almost-wasnt)**（UC Berkeley）——GraphLab（VLDB'12 ToT）此前被 NeurIPS、SOSP 拒稿的自述，含评审意见摘录。
- **[Gans & Shepherd 1994, JEP](https://www.aeaweb.org/articles?id=10.1257%2Fjep.8.1.165)**——"How Are the Mighty Fallen: Rejected Classic Articles by Leading Economists." *Journal of Economic Perspectives* 8(1): 165–179——60+ 篇被拒经典（含 15 位诺奖得主）的系统自述集，「对账」式研究的最近邻模板。
- **[Campanario 2009, Scientometrics](https://www.miketaylor.org.uk/tmp/PDF/art%3A10.1007%2Fs11192-008-2141-5.pdf)**——"Rejecting and resisting Nobel class discoveries"——诺奖级发现被拒/抵制的系统整理。**未发现任何把会议 ToT 名单与当初评分系统对账的研究 = gap 成立。**

## 理论源卡片（品味不可通约的哲学底座）

### Kant · 判断力批判（审美判断四契机）

**引用**：Immanuel Kant. 1790/1987. *Critique of Judgment*（Kritik der Urteilskraft）. Trans. Werner S. Pluhar, foreword Mary J. Gregor. Indianapolis: Hackett Publishing. 686 页. ISBN 0872200256.（[出版社页](https://hackettpublishing.com/critique-of-judgment)）

**落点**：「无概念的普遍判断」= 美的分析论第二契机（§6–9，§9 "美是无概念地普遍令人愉悦"）；四契机 = 质（无利害 §§1–5）/ 量（无概念的普遍性 §§6–9）/ 关系（无目的的合目的性 §§10–17）/ 模态（必然性 §§18–22）。

### 配套书目

- Bourdieu, Pierre. 1984. *Distinction: A Social Critique of the Judgement of Taste*. Trans. Richard Nice. Cambridge, MA: Harvard University Press. 613 页. ISBN 0674212770.
- Lamont, Michèle（Harvard University）. 2009. *How Professors Think: Inside the Curious World of Academic Judgment*. **Cambridge, MA: Harvard University Press**. ISBN 0674032667.（**旧版误记为 Princeton UP**）

## 参考资料

（本条引用已全部内联在「想法 × 材料」中并附链接；上述条目均经 2026-09-07 搜索核验。内部来源：NOTUGLY-S 提案见 [003 · NOTUGLY-S](003-notugly-s.zh.md)；本站相关：[023 · 顶刊的媒体化](023-journal-mediatization.zh.md)（taste 重定向的需求侧延伸）。）

## 核验记录（2026-09-07）

- 18/18 条现有引用全部实存，0 死链；aclweb 对脚本返回 418（反爬，内容可读，"fascinating, controversial, surprising" 原句确认在页）；dl.acm.org 对 curl 403（DOI 经 dblp+Exa 确认）。
- 已修正 6 处：arXiv:1507.06411 作者为 Olivier François 单人（56% 与 CI 0.34–0.83 为真），「reject-or-flip-a-coin」系本词条自拟名；SIGCOMM ToT 出处为 CCR 39(2):40–41（2009），非 SIGIR Forum；SIGIR Forum 2017 专刊回访 26 篇（非 21）；HN id 是评论（转引 Forbes "The PhD Metagame"）；Lamont 出版社为 Harvard UP。
- 新增 award 级材料 12 条（想法 2/3/5），其中 Wainer 2015（P=0.72）、CHI「无正式标准」自认、MISQ 5/22、Keshav WFQ 被拒案为最有力四件。


---

> 🌐 [Read this note in English](021-best-paper-lottery.en.md)

