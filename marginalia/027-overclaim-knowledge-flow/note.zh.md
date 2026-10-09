---
id: marginalia-027
title: "Overclaim 与名义上的知识流动——研究想法与基础文献"
date: 2026-10-08
published: 2026-10-08
kind: proposal
sources:
  - "Peng, Qiu, Fosse & Uzzi (2024), doi:10.1073/pnas.2320066121；PMC 全文"
  - "Qiu, Chen & Li (2026), Counterfactual LLM-based Framework for Measuring Rhetorical Style；ICLR 正式论文"
  - "Fang et al. (2022), doi:10.1145/3510003.3510121；作者实验室全文"
  - "Stavrova et al. (2025), doi:10.1038/s44271-025-00293-8；出版者全文"
  - "Chen, Teplitskiy & Jurgens (2025), doi:10.18653/v1/2025.acl-long.1534；ACL Anthology"
  - "Gilbert (1977), doi:10.1177/030631277700700112；出版者记录"
  - "Small (1978), doi:10.1177/030631277800800305；出版者摘要与原文扫描"
  - "Latour (1987), Science in Action；作者书目与原书第一部分扫描"
  - "Cozzens (1989), doi:10.1007/BF02017064；出版者摘要"
  - "Mizruchi & Fein (1999), doi:10.2307/2667051；出版者摘要"
  - "Greenberg (2009), doi:10.1136/bmj.b2680；原研究摘要"
  - "Teplitskiy et al. (2022), doi:10.1016/j.respol.2022.104484；出版者全文"
  - "Boutron et al. (2010), doi:10.1001/jama.2010.651；PubMed/出版者摘要与元数据"
  - "Meyer & Rowan (1977), doi:10.1086/226550；出版者摘要与元数据"
  - "Bromley & Powell (2012), doi:10.1080/19416520.2012.684462；作者网站原文"
  - "Weiss (1979), doi:10.2307/3109916；JSTOR 元数据与大学托管原文"
  - "Carlile (2004), doi:10.1287/orsc.1040.0094；INFORMS 摘要与元数据"
  - "Szulanski (1996), doi:10.1002/smj.4250171105；Wiley 摘要与元数据"
initial-prompt: "overclaim in academic research paper；overclaim and 形式上 或者 名义上的 知识流动 而非实质上的流动。搜索相关的一些基础文献放进去即可，然后更新我的网页。"
agent: Codex
follow-up-prompt: "知识社会学和科学学没有这个相关内容的探究的文献么；联系 Sophie Qiu 的 promotional language、陈鸿的 Counterfactual LLM-based Framework for Measuring Rhetorical Style，以及 Hongbo 的 This Is Damn Slick，研究修辞性论文（包括 overclaim）是否更容易被引用。"
model: GPT-6
issue: 75
---

# Overclaim 与名义上的知识流动——研究想法与基础文献

> 研究种子：论文的修辞是否提高可见度与被引用的机会？这些引用又有多少转化为实质知识使用，overclaim 是否改变这种转化？本条整理问题和基础文献，尚无本研究的实证结果。

## 核心想法

将入口从 overclaim 扩展到**论文的修辞及其后续接受**：promotional language 强调重要性或新颖性；rhetorical style 还包括愿景、确定性与贡献的组织方式。**Overclaim（过度宣称）** 则要求判断宣称是否超出设计与证据。它可以借助修辞实现，却不是所有强修辞或积极用词的同义词。

拟议的传播链是：**修辞呈现 → 被注意／阅读 → 被引用 → 实质使用**。已有研究支持其中修辞与引用、关注的关联；每一步的转化仍需分别观察。强修辞可能帮助有价值的发现被采用，也可能主要增加背景引用或合法化用途，还可能引发实质性的检验、批评和修正。

原来的问题因此保留为更具体的一支：当宣称超出证据时，下游接收到的是有条件的研究发现，还是被包装成确定事实的贡献叙事？应同时观察**使用的深度**与**传递的准确性**，因为失真的论断也可能被实质采用。

## 与 promotional language、修辞测量和 OSS 宣传研究的连接

1. **Peng, H., Qiu, H. S., Fosse, H. B., & Uzzi, B. (2024). _Promotional language and the adoption of innovative ideas in science._ PNAS, 121(25), e2320066121.** [全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11194578/) · [DOI](https://doi.org/10.1073/pnas.2320066121)。Sophie Qiu 的这项共同一作研究分析**基金申请书**中的宣传性语言，关联资助、创新性及受资助项目后续论文的产出和引用。它提示修辞参与科学资源配置；没有直接测量论文摘要修辞，也没有把宣传性语言等同于无依据的夸大。文中的词语替换检验针对模型预测，不能当作真实引用的随机实验。

2. **Qiu, J., Chen, H., & Li, Z. (2026). _Counterfactual LLM-based Framework for Measuring Rhetorical Style._ ICLR 2026.** [正式记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/085b4b5d1f81ad9e057ad2b3de922ad4-Abstract-Conference.html) · [正式全文](https://proceedings.iclr.cc/paper_files/paper/2026/file/085b4b5d1f81ad9e057ad2b3de922ad4-Paper-Conference.pdf)。对相同实质内容生成不同 persona 的摘要，结合成对比较与 Bradley–Terry 模型测量修辞。在 8,485 篇 ICLR 投稿中，控制评审均分、子领域和年份后，修辞强度仍正向预测引用与媒体关注。这已经直接覆盖“修辞性论文是否更容易被引用”的关联问题。**反事实用于测量风格，未随机改变真实论文的曝光**；评审分数也只是质量代理，因此不能直接解释为修辞的因果效应。

3. **Fang, H., Lamba, H., Herbsleb, J., & Vasilescu, B. (2022). _“This Is Damn Slick!” Estimating the Impact of Tweets on Open Source Project Popularity and New Contributors._ ICSE 2022, 2116–2129.** [作者全文](https://cmustrudel.github.io/papers/fang2022twitter.pdf) · [DOI](https://doi.org/10.1145/3510003.3510121)。Hongbo 的研究使用匹配与双重差分，估计推文集中提及对 OSS 项目的影响：平均新增 stars 约增加 7%，新增 commit authors 约增加 2%。可借鉴的是**把受欢迎程度与实际参与分开测量**。处理变量是推文曝光，不是标题中那句话的修辞强度；“宣传性”分类也主要依据链接对象。Stars、贡献者与论文引用、知识使用只能作机制类比，不能直接互换。

4. **Stavrova, O., Kleinberg, B., Evans, A. M., & Ivanović, M. (2025). _Scientific publications that use promotional language in the abstract receive more citations and public attention._ Communications Psychology, 3, 118.** [全文](https://www.nature.com/articles/s44271-025-00293-8)。直接分析 Nature、Science 和 PNAS 的 136,615 篇摘要：宣传词占比每增加 **1 个百分点**，模型预测年均引用多约 9–14%；有控制变量的模型约为 9%。这是论文语言与引用关联的另一项直接证据，尚不是因果识别。详见已有 [023 · 顶刊媒体化](../023-journal-mediatization/note.zh.md)。

5. **Chen, H., Teplitskiy, M., & Jurgens, D. (2025). _The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research._ ACL 2025, 31786–31802.** [正式记录与全文](https://aclanthology.org/2025.acl-long.1534/)。陈鸿的另一篇论文匹配被引原文论断与引用句，测量 **citation fidelity（引用忠实度）**，并研究引用链中的失真。它为连接“源论文修辞—下游论断变化”提供工具。忠实度与实质使用仍须分别编码：准确复述未必改变研究，经过改造的方法也可能被实质使用。

**研究定位**：既然修辞与被引用的关联已有直接研究，更值得推进的是把这类测量接到知识流动上：**修辞带来的引用优势，主要表现为名义承认、准确而深入的使用，还是失真论断的传播？Overclaim 是否改变这些结果的组合？** 这是拟议的整合方向，尚不能宣称首次发现。

## 先区分三个概念

| 概念 | 本研究的工作定义 | 可以寻找的证据 |
|---|---|---|
| Overclaim | 宣称的强度或范围超出证据所能支持的程度 | 对照摘要／讨论中的宣称与方法、结果和局限；例如把相关性写成因果、把有限样本推广到全部场景 |
| 形式上／名义上的知识流动 | 论文、术语或贡献叙事进入下游文本，但在所观察材料中只能确认承认、复述或合法化用途 | 背景性引用、套用贡献标签、复述结论；未观察到具体使用时，先标为“实质使用未确认” |
| 实质上的知识流动 | 知识进入下游推理或工作，改变问题界定、方法、解释或实践 | 方法适配、理论推导、对边界条件的处理、复现或反驳、可追溯的设计／决策改变 |

这不是把引用分成“有用／没用”。引文数量只能说明可见关联；概念影响可能长期、间接发生。批评性引用也可能有实质贡献，名义使用也可能产生声望、资源或合法性上的真实后果。两个维度应分别判断，不预设 overclaim 与名义流动必然相伴。

## 更直接的基础：知识社会学、科学社会学与科学学

这个问题已有明确的文献前史，不应仅用组织脱耦或一般知识转移来定位。相关研究分别考察**引用的修辞功能、论文作为概念符号、知识的选择性解释、论断的事实化，以及引用与实际影响的差异**。这些概念彼此相关，却不都等于 overclaim，也没有共同证明“引用越多，知识越空洞”。

1. **Gilbert, G. N. (1977). _Referencing as Persuasion._ Social Studies of Science, 7(1), 113–122.** [DOI](https://doi.org/10.1177/030631277700700112)。引用可以参与说服读者、支持论证，不只是记录知识债务。这是“引用流动与知识使用不能直接画等号”的经典起点；修辞功能本身不等于欺骗或没有知识贡献。

2. **Small, H. G. (1978). _Cited Documents as Concept Symbols._ Social Studies of Science, 8(3), 327–340.** [DOI](https://doi.org/10.1177/030631277800800305) · [原文扫描](https://garfield.library.upenn.edu/small/hsmallsocstudsciv8y1978.pdf)。通过化学论文的引用语境，研究被引文献如何成为某个概念、方法或数据的标准符号。这最接近“论文名字／标签在流动”的问题；但符号也可能有效压缩并传递知识，不能直接认定为名义使用。

3. **Latour, B. (1987). _Science in Action: How to Follow Scientists and Engineers Through Society._ Harvard University Press.** [作者书目](https://www.bruno-latour.fr/node/130.html) · [原书第一部分](https://classes.matthewjbrown.net/teaching-files/hps/latour-SiA-pt1.pdf)。第一章（尤其原书 pp. 22–23、42–43）追踪下游文本如何通过 **modalities（对论断的限定与修饰）**，把一句话推向公认事实，或带回其生产条件与争议。适合研究限定条件如何消失、论断如何被事实化。事实稳定化并不自动是 overclaim；必须另行判断证据是否足以支持这种确定性。

4. **Cozzens, S. E. (1989). _What Do Citations Count? The Rhetoric-First Model._ Scientometrics, 15, 437–447.** [DOI](https://doi.org/10.1007/BF02017064)。主张先从修辞、再从奖励与承认理解引用。它提醒我们：相同的引用数可能包含不同的论证用途与影响强度，不能未经检验就当作“实质知识流量”。

5. **Mizruchi, M. S., & Fein, L. C. (1999). _The Social Construction of Organizational Knowledge: A Study of the Uses of Coercive, Mimetic, and Normative Isomorphism._ Administrative Science Quarterly, 44(4), 653–683.** [DOI](https://doi.org/10.2307/2667051)。追踪 DiMaggio 与 Powell 的经典同构论文如何被选择性挪用：模仿性同构获得不成比例的关注，不同概念的操作化也出现混淆。这是社会科学内部“理论被引用，但其内容与区分在流动中被重构”的直接个案，不只是抽象的知识社会学背景。

6. **Greenberg, S. A. (2009). _How Citation Distortions Create Unfounded Authority: Analysis of a Citation Network._ BMJ, 339, b2680.** [DOI](https://doi.org/10.1136/bmj.b2680)。研究一个特定生物医学论断的引用网络，识别忽略反证的引用偏差、无新增相关数据的放大，以及仅通过引用把假说变成事实的情况。这是 **overclaim × 传播中的认识论失真** 最直接的经验锚点；它展示一种可能机制，不能据此判断所有引用网络都如此。

7. **Teplitskiy, M., Duede, E., Menietti, M., & Lakhani, K. R. (2022). _How Status of Research Papers Affects the Way They Are Read and Cited._ Research Policy, 51(4), 104484.** [DOI](https://doi.org/10.1016/j.respol.2022.104484) · [作者机构全文](https://knowledge.uchicago.edu/record/5150/files/How-status-of-research-papers-affects-the-way-they-are-read-and-cited.pdf)。对 15 个领域、9,380 位通讯作者提供的 17,154 条随机抽样引用进行调查，54% 被报告为对引用者影响很小或没有影响；但最常被引的论文，其引用反而更可能对应实质影响。它直接研究“修辞性／实质性引用”，也反对简单的“高引用 = 空洞声望”假设。这是作者自报影响，且没有直接检验 overclaim 的作用。

**与新切口的连接**：这些研究解释为什么引用可以增加承认与权威，却不一定同等增加知识影响。可以把**修辞强度、宣称是否超出证据、下游是否实质使用及是否忠实传递**放在同一条传播链里观察，并区分过度宣称发生在源论文还是后续引用中。

## 补充文献：组织机制、研究利用与转移阻力

1. **Boutron, I., Dutton, S., Ravaud, P., & Altman, D. G. (2010). _Reporting and Interpretation of Randomized Controlled Trials With Statistically Nonsignificant Results for Primary Outcomes._ JAMA, 303(20), 2058–2064.** [DOI](https://doi.org/10.1001/jama.2010.651) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/20501928/)。研究临床试验报告中的 **spin**：在主要结果不显著时，如何突出有利解释或转移注意力。可作为“宣称—证据不匹配”的操作化起点；临床试验的类别和发生率不能直接外推到 HCI／SE 或所有学科。

2. **Meyer, J. W., & Rowan, B. (1977). _Institutionalized Organizations: Formal Structure as Myth and Ceremony._ American Journal of Sociology, 83(2), 340–363.** [DOI](https://doi.org/10.1086/226550)。形式结构可以获得合法性，同时与实际活动脱耦。可借来追问：引用、理论标签或“知识转移”叙事，是否在承担合法化功能？这是从组织层面理论向论文及知识使用过程的延伸，尚不是本文机制的直接证据。

3. **Bromley, P., & Powell, W. W. (2012). _From Smoke and Mirrors to Walking the Talk: Decoupling in the Contemporary World._ Academy of Management Annals, 6(1), 483–530.** [DOI](https://doi.org/10.1080/19416520.2012.684462) · [作者原文](https://patriciabromley.com/wp-content/uploads/2018/06/BromleyPowellDecoupling.pdf)。区分 **policy–practice** 与 **means–ends decoupling**：既可能是宣称采用而没有落实，也可能是程序确实执行了，却与预期目标关联薄弱。这提示我们分别观察“有没有使用”与“使用是否实现了所宣称的知识贡献”。

4. **Weiss, C. H. (1979). _The Many Meanings of Research Utilization._ Public Administration Review, 39(5), 426–431.** [DOI](https://doi.org/10.2307/3109916) · [原文扫描](https://sites.ualberta.ca/~dcl3/KT/Public%20Administration%20Review_Weiss_The%20many%20meanings%20of%20research_1979.pdf)。研究利用包括解决问题、政治／策略用途和长期的概念启蒙等不同路径。它为“名义使用”提供更细的分类，也提醒：没有立即改变实践，不等于没有知识影响；准确使用研究来支持既有立场，也不自动构成 overclaim。

5. **Carlile, P. R. (2004). _Transferring, Translating, and Transforming: An Integrative Framework for Managing Knowledge Across Boundaries._ Organization Science, 15(5), 555–568.** [DOI](https://doi.org/10.1287/orsc.1040.0094)。区分句法、语义与实践／利益边界，以及 transfer、translation、transformation。可用来追踪：下游只是接收信息，还是处理了意义差异、利益冲突并改变了工作方式？“实质”不应只认 transformation；有效的 transfer 或 translation 也可能构成实质使用。

6. **Szulanski, G. (1996). _Exploring Internal Stickiness: Impediments to the Transfer of Best Practice Within the Firm._ Strategic Management Journal, 17(S2), 27–43.** [DOI](https://doi.org/10.1002/smj.4250171105)。知识转移受吸收能力、因果模糊和来源—接收方关系等因素制约。它提供一个替代解释：实质转移不足可能源于接收方条件或转移阻力，而不是源论文的 overclaim。

## 更新后的问题与一个小规模起点

1. **引用优势**：在考虑研究内容、证据质量、作者地位、领域和论文年龄后，修辞强度是否仍与被引用的概率、数量及首次被引时间相关？复核已有发现，同时单独考察 overclaim，而不把宣传词计数当作 overclaim 指标。
2. **知识转化**：更强修辞所伴随的引用增长，是背景／合法化引用增加，还是方法、理论、结果的具体使用增加？同时报告各类引用的数量与占比；实质使用占比下降，不意味着实质使用总量下降。
3. **失真传播**：overclaim 是否更容易让下游保留贡献叙事、遗漏适用条件，或将假说写成事实？也考察谨慎的源论断在后续引用中被强化，以及批评／复现是否反而增加。

先在一个领域选择少量源论文及其后续引用，使用固定长度的观察窗口。修辞测量可借鉴陈鸿的内容条件化比较，并人工核查反事实摘要是否确实保留技术内容；另用全文对照“源宣称—证据—局限”标注 overclaim。逐条配对引用句与源论断，分别编码引用功能、具体使用、忠实度和边界条件。未观察到使用时保留“实质使用未确认”，不能凭摘要用词、引用位置或数量直接认定空洞流动。

应使用引用发生前的文本版本，考虑新颖性、开放获取、代码可用性和作者声望等替代解释。媒体曝光可能是修辞影响引用的**中介**，估计总关联与考察传播路径时应分别处理。内容条件化测量和质量控制不能自动消除混杂；若要检验因果机制，可随机展示内容一致、修辞不同的摘要，测量阅读选择或引用意愿，但这些结果不等同于真实长期引用。

与已有随想的连接：[004 · 故事会量化](../004-storytelling-quantified/note.zh.md)关注叙事如何被衡量；[007 · Nuance 兴衰](../007-nuance-rises-and-falls/note.zh.md)关注边界与限定如何表达；[023 · 顶刊媒体化](../023-journal-mediatization/note.zh.md)关注宣称如何被放大。本想法进一步问：这些叙事进入后续工作时，究竟带走了哪些知识？
