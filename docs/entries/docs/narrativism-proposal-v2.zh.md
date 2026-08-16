# 显性与隐性叙事主义:AI 论文中潜藏的叙事性
## Explicit and Implicit Narrationism in Scientific Publication: A Case Study on AI Venue Papers — 提案 v2

日期:2026-08-15
前置文档:`CHI_ACL_故事会量化_调研.md`(v1:六条文献线 + 五维 narrativity 指数 + RQ0–RQ5)

---

## 1. v1 → v2 的增量

| | v1"故事会量化" | v2"显/隐叙事主义" |
|---|---|---|
| 核心概念 | narrativity(文本属性) | **narrationism(场域意识形态)** 与 narrativity 分离;显性/隐性两层 |
| 语料角色 | 论文文本是测量对象 | 文本 + **图表**(多模态);"看似最技术"的 AI 论文是最强案例——因为它自我宣称"让数据说话" |
| 方法 | 计算文本分析 | 计算双轨:**大规模多模态分析 + 批判算法研究/民族志接线** |
| 论文自身 | 常规论文 | **自反性(reflexive)**:本文自身的图表按叙事可视化设计,并把自己放进自己的语料打分 |

一句话研究纲领:**在最宣称反叙事的文体(带公式与基准表的 AI 论文)里,把叙事性从语言层追到图表层与制度层,并测量哪一层的叙事在为录用与引用付酬——其中最强的叙事,是对叙事本身的否认("数据不言自明")。**

---

## 1.5 与 v1 的整合架构(2026-08-15 补:统一为"叙事深度梯度")

**统一构念:narrative depth gradient(叙事深度梯度)——故事越藏越深,而回报可能越深越高。**

| 层 | 内容 | 来源 | 现成工具 |
|---|---|---|---|
| L1 显性语言 | v1 五维指数(hook、第一人称、连词衔接、appeal、hype 词) | v1 | NarraDetect(13k 段落叙事分类数据集,2025)、RAAMove(摘要 move 语料,2024)、Coh-Metrix |
| L2 图表 | teaser 指数、hero chart、caption 叙事度、视觉修辞代码 | v2 §4 | ArXivCap/SciCap、本地 VLM 三级标注 |
| L3 artifact 配置 | 基准选角、指标情节、基线人物表、消融道德剧、规模史诗 | v2 2f | §4.4 纯文本抽取 |
| 贯穿姿态 | 叙事否认与否认差("数据不言自明") | v2 2e | 显证词/无施事被动/发现式动词 |

**整合后才能问的问题(优雅性的检验标准,单独哪一半都问不出)**:
1. **故事溢价的分层分解(premium decomposition)**:控制主题/venue/年份后,L1/L2/L3 各自的叙事指数哪个对录用/引用/award 有独立贡献?——v1 只有 L1 和回报模型,v2 有三层概念但没有回报模型,合起来才有这个问题:"哪一层的故事在领工资?"
2. **调和表面打架的文献**:Vincent-Lamarre 2021("录用 AI 论文可读性更低")与 Hillier 2016("高叙事高引用")看似矛盾——在分层框架里变成互补:如果起作用的是 L2/L3 而非 L1,两个结果同时成立。这本身就是论文 motivation 的第三段。
3. **场域×深度交互**:场域越"技术"(NeurIPS > ACL > CHI),回报是否越向深层(L2/L3)转移?——"故事会"批评与"否认溢价"在同一个模型里检验。

**统一经验设计**:一个语料(ACL + OpenReview 场域 + CHI 对照),四层预测变量,一套结果变量(OpenReview 录用/award/main-Findings/引用/arXiv v1↔camera-ready diff),两个调节(场域、时间含 ChatGPT 断点),一个批判轨(访谈+自反性)。

**出口:三篇系列,共享语料与指数**
- **P1 测量论文**(最快、低风险):跨三层叙事指数 + 金标 + 与 NarraDetect/RAAMove 对齐验证 → IC2S2 / QSS / Metascience;
- **P2 主论文**:premium decomposition + 场域对比 + LLM 断点 + 混合方法 → CHI / CSCW(自反性设计在此);
- **P3 批判版**:否认意识形态 + 故事劳动访谈 + autoethnography → Big Data & Society / CHI alt 格式。

---

## 2. 理论接线

### 2.0 理论锚点:数据即叙事(2026-08-15 补,引文已核实)

> "Data makes sense only to the extent that we have frames for making sense of it, and the difference between a productive data analysis and a random-number generator is a narrative account of the meaningfulness of their outputs. Moreover, one of the most powerful narratives about data is precisely that it demands no interpretation or narration because of its **self-evidentiary character**."
> —— **Dourish & Gómez Cruz 2018**, "Datafication and data fiction: Narrating data and narrating with data", *Big Data & Society* 5(2), DOI 10.1177/2053951718784083

这段话把本提案的中心命题推到底:**叙事主义的最高形态不是讲故事,而是否认叙事**。"数据不言自明"(self-evidentiary)的自我宣称,是数据文化中最强的 master narrative——它让整台说服装置(基准表、hero chart、消融实验)以"中性测量"的名义免于修辞审查。AI venue 是这一命题的完美试验场:该场域的写作规范公开贬低"故事",同时把叙事劳动全部转移到图表与实验编排里。由此得到一个可测量的新构念——**叙事否认(narrative disavowal)**及其复合指标**否认差(disavowal gap)**:文本层"零解释"姿态的强度,与同一论文视觉/词汇修辞强度(hero chart、hype 词、强调装置)之间的落差。落差越大,"让数据说话"的伪装越彻底(见 §3 Layer 2e、§6 RQ7)。

操作便利:Dourish 20 篇论文的本地语料与风格分析已就绪(2026-08-15 另一会话),可作叙事否认编码的金标示例与构念效度材料。

### 2.1 数据叙事主义 / 批判数据研究(用户点名的线)
- **Georgakopoulou, Iversen & Stage 2020**, *Quantified Storytelling: A Narrative Analysis of Metrics on Social Media*(Palgrave)。量化指标(likes/views)如何进入并组织叙事——本研究把它倒过来:学术叙事如何被 citation/benchmark 指标组织。
- **Drucker 2014**, *Graphesis*(Harvard UP):图形不是数据的再现而是解释(captA not data)——图表分析的正当性根基。
- **Gitelman ed. 2013**, *Raw Data Is an Oxymoron*:数据从来是"被给予"的。
- **d'Ignazio & Klein 2020**, *Data Feminism*(MIT Press):量化实践的权力分析;为"故事溢价分配不公"子问题提供框架。
- **Espeland & Stevens 1998**(commensuration as a social process):基准=benchmark 把异质能力通约成单一数字——这本身就是叙事的"情节装置"(antagonist)。

### 2.2 叙事可视化(图表分析的方法论母学科)
- **Segel & Heer 2010**, "Narrative Visualization: Telling Stories with Data"(IEEE TVCG/InfoVis,引用 2300+):58 个新闻/研究可视化归纳出 7 种叙事可视化体裁(genre)与视觉叙事策略(ordering、highlighting 等)——直接改编为"论文图表叙事代码表"。
- **Hullman & Diakopoulos 2011**, "Visualization Rhetoric: Framing Effects in Narrative Visualization"(TVCG):可视化修辞框架(information access、provenance、mapping、composition、stylization、perspective 等修辞维度)——**本研究的图表编码方案直接从它改编**。

### 2.3 批判算法研究 / 民族志
- **Seaver 2017** "Algorithms as Culture"(算法作为文化,民族志战术);**Burrell 2016**(ML 算法的三种不透明)。
- AI 实验室民族志已成型:"Crafting computer vision through human eyes: An AI laboratory ethnography"(Big Data & Society)、*Handbook of Critical Studies of Artificial Intelligence*(Edward Elgar)的 AI Ethnography 章节——证明该领域有发表场地。
- **Pardo-Guerra 2022**, *The Quantified Scholar: How Research Evaluations Transformed the British Social Sciences*(Columbia UP):量化评审的民族志——评审端叙事主义制度的最佳先例。
- 反身性方法根基:**Clifford & Marcus 1986**, *Writing Culture*——"论文自身成为叙事主义论文"的写法有谱系(performance writing / 反身民族志)。

### 2.4 AI 场域自身的叙事批判(AI 场域内的内应)
- **Raji, Bender, Paullada, Denton & Hanna 2021**(NeurIPS D&B)"AI and the Everything in the Whole Wide World Benchmark":基准被当作"通用智能"的证据——通约化叙事失控的经典批判。
- **Beese et al. 2023**(RSOS):AI 论文 stance 分类——越来越"positive stance"(提出新方法打败 SOTA 型叙事),但负面 stance 论文引用更高。
- 可作分析对象的 master narratives:**The Bitter Lesson**、scaling hypothesis、"打榜"文化、stochastic parrots 作为反叙事。

### 2.5 技术与数据作为隐性叙事(artifact 层,2026-08-15 补)
- 谱系:**Winner 1980** "Do Artifacts Have Politics?"(人工物有政治)→ **Akrich 1992** "The De-Scription of Technical Objects"(技术物内嵌 *script*,设计者把世界观"铭写"进人工物)→ **Latour 的 blackboxing**(技术把叙事劳动封进黑箱)。命题:技术物有政治,因此也有叙事。
- 直接方法先例:**Birhane, Kalluri, Card, Agnew, Dotan & Singhal 2022**(FAccT)"The Values Encoded in Machine Learning Research":对 100 篇高被引 ML 论文逐行注释,提炼 59 种被 promoting 的价值——性能压倒社会影响。本文把"价值编码"推进为"叙事编码":不只问论文 promote 什么价值,还问它的技术配置讲了个什么故事。
- 榜单的反应性:**Espeland & Sauder 2007**,"Rankings and Reactivity: How Public Measures Recreate Social Worlds"(*AJS* 113(1):1–40;书版 *Engines of Anxiety* 2016):排名不只是描述,而是重塑被排名者的行为——leaderboard 是会自我实现的叙事装置。
- 反体裁(counter-genre):**Gebru et al. 2018** Datasheets for Datasets、**Mitchell et al. 2019** Model Cards、**Bender & Friedman 2018** Data Statements(TACL)——文档化体裁本质上是"强迫隐性叙事显性化"的制度尝试;它们在 AI venue 的渗透率低、常被当附录,本身就是叙事否认的证据。

### 2.6 图表抽取与多模态基础设施(全部现成)
- **PDFFigures 2.0**(AllenAI):从学术 PDF 抽 figure + caption + 类型。
- **SciCap**(Findings of EMNLP 2021):41.6 万张 CS arXiv 图-caption(2010–2020);SciCap Challenge 2023 扩到全部 8 个 arXiv 域。
- **ArXivCap / Multimodal ArXiv**(arXiv 2403.00231):**640 万图 + 390 万 caption**,57.2 万篇 arXiv 论文,含 ArXivQA——开发图表编码方案的现成操场。
- 邻接先研究(需精读):**DiagramBank**(arXiv 2604.20857,大尺度 diagram 设计范例库,明确讨论 ML/DML venue 的 teaser figure 惯例——最接近的竞品);"Identifying the Central Figure of a Scientific Paper"(NSF PAR 10188257)。

---

## 3. 概念操作化:三层

**Layer 1 — Explicit narrativity(显性,语言表层)**
即 v1 的五维指数(hook 开头、第一人称 quest、感官/appeal 语言、连词与句间衔接、hype 词汇)。位于 abstract/intro/discussion,人人可见,最容易被审稿人识别为"故事"。

**Layer 2 — Implicit narrativity(隐性,结构与视觉层)**——v2 的核心增量
- 2a. **无人称的修辞结构**:被动语态下 CARS move 仍完整("It has long been known that…" = establishing territory)。技术文体没有消灭叙事,只是把施事者藏起来。
- 2b. **Master narratives**:progress myth(表格里永远向上的数字)、scaling epic(参数量 x 轴 = 史诗的时间轴)、benchmark-as-antagonist(基线=反派,消融=决战)。
- 2c. **图表叙事装置**(多模态,见 §4 代码表):Figure 1 teaser(整篇论文的电梯陈述图,ML 场域的成文惯例)、hero chart(胜差放大的主结果图)、架构图=英雄之旅地图、caption 微叙事(完整叙事句 vs 名词片段)。
- 2d. **"让数据说话"的伪装机制**:显性叙事性最低的段落(结果、公式)恰恰是隐性叙事密度最高的地方——叙事被转移到图表设计、实验排序与表格加粗里。可检验假设:**narrativity gradient**(显性叙事 intro>results,隐性叙事 results>intro)。
- 2e. **叙事否认(narrative disavowal)**——Dourish & Gómez Cruz 2018 命题的操作化:对"无需解释"姿态的语言标记,包括:显证词(clearly / obviously / evidently / simply / merely / as expected)、无施事被动+现在时("It is shown that…"、"Table 2 demonstrates…")、"发现"式而非"论证"式动词(report/observe/measure vs argue/suggest)、结果段解释从句的缺失、以及"客观/中性/直接"的自我描述。与 2c/2d 的修辞强度合成**否认差(disavowal gap)= 视觉词汇修辞强度 − 显性解释性标记**。核心可检验命题:否认差在技术性强的场域(ACL/NeurIPS)更高,且**否认差本身可能有录用溢价**——最成功的"纯技术"论文恰恰是叙事转移做得最彻底的论文。
- 2f. **技术与数据配置层(artifact grammar)**——"技术与数据作为一种隐性叙事"的操作化:论文的技术选择本身构成无声的情节。六个可测装置:
  ① **基准选角(benchmark casting)**:选哪些数据集=选哪些配角与战场;用 MMLU 还是人类专家评估,叙事的是"能力"的本体论(接 Raji et al. 2021);
  ② **指标即情节(metric as plot)**:accuracy → BLEU → win-rate,指标定义了"胜利"是什么;换指标=改写故事结局;
  ③ **基线名单=人物表(dramatis personae)**:纳入/排除哪些基线、把谁设为"最强对手"、胜差多大——冲突的搭建;
  ④ **消融实验=道德剧(ablation as morality tale)**:每个组件必须"挣得"自己的位置——必然性叙事(just-so story of necessity);
  ⑤ **规模=史诗(scale epic)**:参数量/数据量/FLOPs 作为情节时间轴,"更大"自带进步叙事(scaling laws 作为 master narrative);
  ⑥ **资源合法性**:"8×H100 / 70B" 的装备清单作为英雄的武力值展示。
  反向指标:文档体裁(datasheets/model cards/data statements)的使用率与位置——隐性叙事被制度性显性化的程度。

**Layer 3 — Narrationism(场域意识形态,制度层)**
讲故事作为信仰体系:写作课程(Nacke 类"How to write a CHI paper" 是显性训练制度)、how-to 博文、rebuttal 话术("please highlight your contribution story")、录用统计(25% 录用率下的选择压力)。用话语语料 + 访谈测量,不用 LLM 猜。

### 叙事的规范带:storytelling(褒)vs 故事会(贬)——污名边界(2026-08-15 补,用户命题)

前提修正(2026-08-15,用户按 Latour 提示):**不存在"真科学 vs 卖故事"的本体分界**。按 **Latour & Woolgar 1979(Laboratory Life)与 Latour 1987(Science in Action)的 science in the making**:事实是被构造、再被**去模态化(de-modalized)**的陈述——论文把"我们似乎发现 X"逐步写成"X(不言自明)";所谓纯技术内核不是叙事的对立面,而是叙事的终产品(blackboxed、看起来"从来就在那里"的 ready-made science)。因此本框架**不做叙事/实质二分,改做模态(modality)分析**:同一构造过程,不同文体处于模态连续体的不同位置。语言直觉的区分(夸"storytelling 好"、骂"故事会")依然是真实的规范现象,但它划的不是科学与故事的边界,而是**"挣得的 facticity"与"未挣得的 facticity"的边界**。三根判据轴据此重构:

- **facticity 轴(挣得度)**:指控的真实内容不是"故事多",而是**去模态化超出铭写劳动(inscription work)**——把 claims 写成事实所需的构造工作(实验、证明、消融、误差条、被动员的盟友=引用与基线)没做够,却提前领走了事实地位。心理学先例"准确的自我推销惩罚更轻"在此重读为:挣得的 facticity 豁免惩罚。原 RQ9b 的操作化不变(claim strength/hedging × 实质密度),但理论语义改变:实质密度 = 铭写劳动量的代理,**不是"非叙事的实质"**。
- **制作可见度轴(making visible)**:ready-made 规范要求论文抹去 construction 的痕迹;显性叙事(hook、研究历程、第一人称 quest)是**让 making 可见**的文体。可见度过高被骂"故事会"(把科研写成见闻录),过低则干瘪无人读。规范带 = 允许露出多少 making 的双边界。
- **工艺轴(craft vs template)**:《故事会》作为杂志名自带"大众量产故事"的阶层意涵——贬义不只指向"故事多",更指向"模板化的量产叙事"。这一轴直接连接 LLM 时代:AI 生成的叙事恰是"故事会式"的模板叙事,而人写的 bespoke 叙事仍可称为 craft。**污名边界可能在 LLM 时代沿这条轴重新划定。**

**机制闭环(拉图尔版,本项目最大的理论收益)**:L1 显性叙事是"**展示 making**"的文体;L2(图表修辞)与 L3(基准/指标/消融编排)是**以 ready-made 面目出现的 inscription 文体**——表格与数字看起来"从来就在那里"(facts have no history),其 facticity 在评审现场几乎无法被当场挑战。于是场域奖励 ready-made 文体、惩罚 making 可见文体——**叙事不是从"实质"逃向更深处,而是从"可见的构造"逃向"不可见的构造"**。深度梯度因此是模态政治的产物:最深层的叙事之所以领工资,恰因为它已把叙事痕迹洗成了测量(去模态化的完成态)。文献劈叉的和解随之更干净:心理学测到叙事惩罚、科学计量测到叙事回报(Hillier/Stavrova)——**罚的是 making 可见,奖的是 blackboxing 完成,两个文献各测了模态连续体的一端**。附带红利:arXiv v1 → camera-ready 的 diff 恰是 making→ready-made 的压缩过程,可直接测"去构造化"幅度;自反性设计(autoethnography 附录)也不再是姿态,而是把我们的 making 留在明处的方法论承诺。Gieryn 的 boundary-work 保留但降级:标签在经验上确是划界实践,但被划的边界不是科学/故事,而是 facticity 的合法性——**标签争的是模态,不是本体**。

---

## 4. 图表多模态分析:本地管线(用户要的落地思路)

### 4.1 语料与抽取
- 语料:ACL Anthology(main+Findings,~5 万篇)+ NeurIPS/ICLR(OpenReview,带录用标签)+ CHI(对照场域);窗口 2012–2026(覆盖 teaser 惯例兴起与 ChatGPT 断点)。
- 抽取:**Docling**(IBM 开源,本地,图/表/caption/阅读顺序,arXiv 2501.17887)+ **GROBID**(元数据/引用,TEI XML)互补;pdffigures2 做备选(自带 figure-type)。
- 热身捷径:先在 **ArXivCap(640 万图)** 上开发并验证编码方案,再定向抽目标 venue 全文。

### 4.2 三级本地标注(由便宜到贵)
| 级 | 任务 | 本地模型 | 说明 |
|---|---|---|---|
| L1 便宜 | 图类型(teaser/架构/结果图/定性示例/表格)、位置、页码、尺寸 | CLIP/SigLIP embedding + 浅层分类器;Florence-2 | 全量跑 |
| L2 结构化 | 轴范围与截断、基线选择、强调色/加粗、箭头与光晕 | **Qwen2.5-VL-7B**(Ollama/vLLM,server 可跑;显存够则 72B) | chart-to-table 也可用 DePlot/MatCha 类 |
| L3 语义 | caption 叙事性、图表修辞代码(改编 Hullman&Diakopoulos)、功能角色 | Qwen2.5-VL 本地放量;GLM 视觉 API 只用于打样 | 500 图人工金标锚定 |

### 4.3 图表叙事指标(编码表草案)
| 指标 | 操作化 | 假说方向 |
|---|---|---|
| Teaser 指数 | Figure 1 是否为"整篇概览"型图 | 随年份上升;award 论文更高 |
| Caption 叙事度 | caption 句长、完整句比例、动词密度、"我们"主语 | 与文本显性叙事性解耦(独立因子?) |
| Hero chart 强度 | 胜差放大:轴截断、对数轴、基线剔除、我方高亮色 | 越强 → 引用越高?(hype 的视觉形态) |
| 架构图叙事化 | 箭头表因果、拟人图标、模块命名(the Encoder "reads"…) | 场域差异:CV/NLP vs HCI |
| 图表-正文整合 | 图被正文叙事句引用("as Figure 2 shows, our method…") | 整合度高 → 可读性与引用 ↑ |
| 模板收敛度 | SigLIP embedding 聚类后的类集中度(按年) | LLM 时代收敛加速 = "视觉 slop" |

### 4.4 artifact 层抽取(2f 的落地,全是便宜任务)
基准实体抽取(benchmark NER:GLUE/MMLU/HumanEval…)+ 指标识别(regex/词典:accuracy/BLEU/win-rate)+ 基线表解析(Docling/GROBID 的 table 结构)+ 消融章节检测与组件命名 + 架构图模块命名(VLM L3 顺带标注)+ 文档体裁探测(datasheet/model card/data statements 段落存在与位置)。全部纯文本任务,与 4.2 管线共用 GROBID 输出。

### 4.6 跨平台污名话语:online community 语料(RQ0 扩容,2026-08-15 补)

"故事会"指控不只存在于评审文本,更活在社区公共话语里(知乎/小红书/X/Reddit/B站)。跨平台矩阵(按可行性排序):

| 平台 | 场域性质 | 获取方案 | 难度 |
|---|---|---|---|
| Discord(已有) | 深度 insider | **复用 discord_workflow 配置驱动管线**(4 社区 37.8k 消息架构),增配 ML 学术服务器 | 最低 |
| Reddit r/MachineLearning, r/hci | 英文 insider 辩论 | 免费 API(研究档) | 低 |
| Mastodon(fediscience 等) | 英文/欧陆学术圈 | 免费 API | 低 |
| B站/YouTube 评论 | 论文讲解视频下的讨论 | API 可用 | 低中 |
| 知乎 | 中文 insider,职业策略框架 | 自写爬虫(复用 discord_workflow 架构;问题 646340702 + "ACL 故事会/CHI 讲故事/画饼"关键词族) | 中 |
| X/Twitter | 英文公开 callout,论文级指控 | API 收费;**先用现成数据集**:de Marcellis-Warin et al. 2025(89.3 万条 AI 推文,2017–2023)+ Mongeon et al. 2022(学者 6000 万推文事件,arXiv 2208.11065);2024 后缺口走合作/小额购买补 | 中高 |
| 小红书 | 中文年轻研究生,情绪/体验框架 | 反爬最强、无 API;**降级方案**:关键词搜索抽样 + 截图存证,只做定性补位不做全量 | 高 |

研究问题(RQ0 从单一话语分析扩容为四问):
- **RQ0a 靶子结构**:指控对象的分布(venue / 论文 / 实验室 / 个人 / 国家群体)及其平台差异——X 上是指向具体论文的 callout,知乎上可能是对会议的总体判断?
- **RQ0b 平台体裁**:同一指控的体裁差——知乎=职业策略文、小红书=情绪体验帖、X=公开 callout 带证据链、Reddit=技术辩论。平台可供性(affordances)如何塑造污名话语的形态。
- **RQ0c 生命周期**:指控量 × 事件日历(录用通知 / award 公布 / 撤稿丑闻 / ChatGPT 断点)的时间序列;与论文语料的叙事通胀曲线叠加——RQ9d 的实证版。
- **RQ0d folk theories(民间理论)**:社区成员如何解释"讲故事溢价"?他们的民间理论与我们测得的 premium decomposition 对不对得上?**测量的分层回报 vs 社区信仰的分层回报——三角验证,论文最出彩的一节。**

理论锚:**Latour 的 science in the making**——污名话语是模态之争(挣得/未挣得的 facticity),不是科学/故事的本体分界;Gieryn 1983 boundary-work 降级为经验层描述(标签是划界实践,但被划的边界是 facticity 合法性);folk theories 接 HCI 的 folk theory 文献线。

方法:关键词族(会议名 × 叙事词族:故事会/故事汇/画饼/讲故事/overselling/style over substance/just a story/vibes paper)→ LLM 辅助编码(指控对象/框架/立场/体裁)+ 人工金标(复用 §4.2 校准流程)。**跨文化污名词汇学**(中文"故事会/画饼" vs 英文贬义词表的对照)本身是一个子研究。伦理:公开帖子、匿名转述、不点名个人;小红书 ToS 风险单独评估;按 CHI 公共话语研究规范走伦理审查路径。

### 4.5 存储与规模
- 存储进 **DuckDB**(直接复用现有 OpenAlex+DuckDB 栈);图表原图 + embedding + 标注 JSON 三表。
- 规模估算:5 万篇 × ~5 图 ≈ 25 万图;7B VLM 本地 ~1s/图 ≈ 3 GPU·天,完全可全量。

---

## 5. 自反性设计:让论文本身成为叙事主义论文

1. **Self-inclusion**:论文定稿版跑自己的显/隐指标,附录公布打分——"我们论文的 teaser 图与 hero chart 长这样,我们的 caption 叙事度是 X"。
2. **图表按 Segel & Heer 体裁设计**:主结果图做成 annotated chart / 流程型叙事可视化,并在 caption 里标注我们使用的修辞装置(自曝 visual rhetoric)。
3. **Autoethnography 附录**:记录我们自己写作、rebuttal、改图过程中的"讲故事劳动"(接 Writing Culture 谱系)。
4. **批判子题:故事溢价的分配**——讲故事是需要资源的(画图技能、英语修辞、模板库);接 Stavrova 2025 的性别异质性发现 → 非母语者/junior/无设计资源的组是否被故事溢价惩罚。这是 CHI/CSCW 的强卖点,也回应 Data Feminism 的 "unmasking power" 原则。

---

## 6. 研究问题(v2,继承并扩展 v1 的 RQ0–RQ5)

- **RQ0(跨平台污名话语,2026-08-15 扩容)**:RQ0a 靶子结构 / RQ0b 平台体裁 / RQ0c 生命周期×事件日历 / RQ0d folk theories 与测量回报的三角验证(方案见 §4.6)。
- **RQ1(显隐分离)**:显性语言叙事与图表隐性叙事是同一构念还是独立因子?narrativity gradient 假设(显性 intro>results,隐性 results>intro)是否成立?
- **RQ2(视觉修辞普查)**:AI venue 图表叙事装置 15 年演化史——teaser 惯例何时制度化?hero chart 强度是否随录用率下降而上升(竞争→修辞军备竞赛)?
- **RQ3(回报分解)**:控制主题/venue/年份后,显性 vs 隐性叙事分别对 award、main-vs-Findings、引用的边际贡献——**故事溢价到底买的是语言还是图表?**
- **RQ4(场域对比)**:NeurIPS/ICLR vs ACL vs CHI 的三层叙事结构差异(接 v1 的"故事会"场域对比)。
- **RQ5(LLM 时代)**:2022-11 后:caption 模板化、图表模板收敛(视觉 slop)、"叙事外包"给 LLM 的痕迹(excess vocabulary 在 caption 层的对应物)。
- **RQ6(批判轨/民族志)**:15–20 个深度访谈(作者/AC/评审):"讲故事"如何被教授、被内化、被外包?故事劳动的隐形成本与分配。
- **RQ7(叙事否认溢价,核心新命题)**:"数据不言自明"姿态的强度(2e)与否认差,是否(a)随场域技术性递增(ACL/NeurIPS > CHI),(b)对录用/引用有独立于实际修辞强度的正回报——即**隐式叙事力量 > 显式叙事力量**(Dourish & Gómez Cruz 命题的量化版)?
- **RQ8(artifact 层叙事)**:技术配置的叙事装置(2f:基准选角、指标选择、基线人物表、消融结构、规模叙事)能否被可靠编码?控制语言层叙事后,artifact 层叙事对录用/引用是否有独立贡献——**"论文的技术选择讲的那个故事"本身是否有价**?子问题(反应性):leaderboard 叙事是否自我实现(Espeland & Sauder 式 reactivity——被基准定义的能力反过来组织研究议程)?
- **RQ9(污名边界:从 storytelling 到故事会)**:叙事在何时从褒义词翻转为贬义词?
  - **RQ9a(评审话语)**:OpenReview 公开评审中"叙事褒扬"(well-motivated / compelling / clear)与"叙事贬抑"(just a story / overselling / style over substance)的分布;**同一评审人内**(within-reviewer)对比:什么论文特征让同一个人从夸"故事讲得好"变成骂"这只是故事"?
  - **RQ9b(模态落差,原"规范带断点")**:modality gap = claim 的模态高度(去模态化程度:显证词、无施事被动、发现式动词)− 铭写劳动密度(定理/证明/数据集/误差条/统计检验/开源工件;claim-evidence 对齐用 claim strength / hedging 检测)。假设:gap 越过阈值,"故事会"类评语概率跳升——把看不见的 facticity 规范变成可估断点。注意理论语义:**操作化沿用的"实质密度"只是铭写劳动的代理,不预设叙事/实质二分**。
  - **RQ9c(标签的公平性)**:同样叙事强度 × 同样实质,精英机构 vs 边缘机构、母语 vs 非母语,被贴贬义标签的概率差(接 Stavrova 性别异质性与 self-promotion penalty 文献)。
  - **RQ9d(通胀动态)**:叙事通胀(平均 L1 上升)是否引发污名话语上升(知乎/Reddit/X 的"故事会/故事汇"指控时间线)?信号贬值模型:人人讲故事时,指控本身成为新的区分手段。
  - **RQ9e(vignette 实验,因果版)**:同一研究内容 × 叙事强度(高/低)× 实质存在(有/无)的 2×2,请评审员/社区成员评判——褒贬翻转点落在哪一格。

## 7. 风险与对策
- **两张皮风险**(计算轨与批判轨各说各话):编码方案由两轨共同开发,访谈材料用于校准计算标签的解释(混合方法序列设计)。
- **VLM 标注可靠性**:500 图双人独立标注金标,报告 Krippendorff α 与 VLM-人类一致性;报告对 LLM 风格图的敏感度。
- **自反性沦为姿态**:self-inclusion 必须定量化(打分进附录),否则删。
- **版权**:ACL Anthology 允许研究性抽取(注明);ACM CHI 图表需逐张检查 open access 状态,必要时只发统计不附原图。
- **DiagramBank 撞车风险**:其关注 diagram 设计范例(工程向),本研究关注叙事/修辞(社会科学向),但必须精读并明确切割。

## 8. 节奏
- M1:图表编码方案 + 500 图金标(ArXivCap 热身)→ 可先发 workshop / alt 格式;
- M2:全量普查(25 万图)+ 15 年演化史;
- M3:回报分解模型(接 v1 的结果变量方案:OpenReview 录用标签、award、main-Findings、arXiv v1 vs camera-ready diff);
- M4:访谈 + 批判轨;
- M5:成文。投稿定位:**CHI / CSCW**(主打,混合方法+自反性正对口)、**IC2S2 / QSS / Metascience**(计算版)、Big Data & Society(批判版)。

---

## 9. 本轮新增文献清单
1. Segel & Heer 2010, TVCG — Narrative Visualization. https://ieeexplore.ieee.org/document/5613452/
2. Hullman & Diakopoulos 2011, TVCG — Visualization Rhetoric. https://dl.acm.org/doi/10.1109/TVCG.2011.255
3. Georgakopoulou, Iversen & Stage 2020 — Quantified Storytelling. https://link.springer.com/book/10.1007/978-3-030-48074-5
4. Pardo-Guerra 2022 — The Quantified Scholar. Columbia UP(LSE)
5. Raji, Bender, Paullada, Denton & Hanna 2021 — Everything in the Whole Wide World Benchmark. https://arxiv.org/abs/2111.15366
6. SciCap — Findings EMNLP 2021. https://aclanthology.org/2021.findings-emnlp.277/ ;https://scicap.ai/
7. ArXivCap / Multimodal ArXiv — arXiv 2403.00231. https://mm-arxiv.github.io/ ;HF: MMInstruction/ArxivCap
8. PDFFigures 2.0. http://pdffigures2.allenai.org/
9. DiagramBank — arXiv 2604.20857(邻接竞品,必读)
10. Identifying the Central Figure of a Scientific Paper. https://par.nsf.gov/servlets/purl/10188257
11. Docling — arXiv 2501.17887. https://github.com/docling-project/docling ;GROBID https://grobid.readthedocs.io/
12. Crafting computer vision through human eyes — Big Data & Society. https://journals.sagepub.com/doi/10.1177/20539517261438637
13. Handbook of Critical Studies of Artificial Intelligence(Edward Elgar)AI Ethnography 章
14. 经典(凭已有知识列出,写作时核对版本):Drucker *Graphesis* 2014;Gitelman ed. *Raw Data Is an Oxymoron* 2013;d'Ignazio & Klein *Data Feminism* 2020;Espeland & Stevens 1998;Clifford & Marcus *Writing Culture* 1986;Seaver 2017;Burrell 2016
15. **Dourish & Gómez Cruz 2018** — Datafication and data fiction. *Big Data & Society* 5(2), 10.1177/2053951718784083(**本提案理论锚点**)
16. Gray — Data Worlds(KCL 仓储版)https://kclpure.kcl.ac.uk/portal/files/127612348/Data_Worlds_GRAY_Published6Mar2020_AAM.pdf
17. "Numbers will not save us: Agonistic data practices" — *The Information Society* 2021 https://www.tandfonline.com/doi/full/10.1080/01972243.2021.1920081 ;"Data, anecdotes, anecdotal data: Feminist data activism" — *BD&S* 2024 https://journals.sagepub.com/doi/abs/10.1177/20539517241306347(两篇均为 Dourish&Cruz 的后续对话)
18. **Birhane, Kalluri, Card, Agnew, Dotan & Singhal 2022**(FAccT)— The Values Encoded in Machine Learning Research. https://dl.acm.org/doi/10.1145/3531146.3533083 ;arXiv 2106.15590(**artifact 层方法先例,100 篇高被引 ML 论文 59 种价值**)
19. **Espeland & Sauder 2007** — Rankings and Reactivity. *AJS* 113(1):1–40. https://www.jstor.org/stable/10.1086/517897 ;书版 *Engines of Anxiety*(Russell Sage, 2016)
20. artifact 层谱系(经典,写作时核对版本):Winner 1980 "Do Artifacts Have Politics?"(*Daedalus*);Akrich 1992 "The De-Scription of Technical Objects"(in Bijker & Law eds., *Shaping Technology/Building Society*);Latour blackboxing(*Pandora's Hope*);Gebru et al. 2018 Datasheets(arXiv 1803.09010);Mitchell et al. 2019 Model Cards(FAT*);Bender & Friedman 2018 Data Statements(*TACL*)

## 10. Seed Papers 清单(2026-08-15 补)

**如果只种一棵树:Hillier, Kelly & Klinger 2016**——本项目 = 把它从气候学期刊搬到 AI 会议,从单层语言指数扩成三层深度梯度,补上它没做的场域对比、回报分解与 LLM 断点。故事讲法:"2016 年有人证明气候论文的叙事风格预测引用;十年后,在最反叙事的 AI 论文里,我们证明故事藏得更深、领工资的层次更深。"

| # | Seed | 角色 | 用法 |
|---|---|---|---|
| S1 | **Hillier, Kelly & Klinger 2016**(PLOS ONE) | 测量种子(全项目的母体) | 复制其指数构造逻辑(金标+PCA)并升维到三层 |
| S2 | **Dourish & Gómez Cruz 2018**(BD&S) | 理论种子(题眼) | "self-evidentiary"=否认构念的出处,引言第一段 |
| S3 | **Birhane et al. 2022**(FAccT) | 最近邻/对话种子 | 100 篇人工价值编码 → 我们全语料三层叙事编码;必须正面切割:价值编码 vs 叙事编码 |
| S4 | **Stavrova et al. 2025**(+Peng 2024 PNAS;Qiu 2024 JAMA) | 回报种子 | hype→引用/关注的回归框架 + 调节分析模板(gender equity 迁移到语言资源 equity) |
| S5 | **Vincent-Lamarre & Larivière 2021**(QSS) | 反例种子(motivation) | "低可读性高录用"与 S1 矛盾 → 分解设计的存在理由 |
| S6 | **Hullman & Diakopoulos 2011**(TVCG) | L2 编码种子 | 图表修辞代码表直接改编 |
| 工具 | **NarraDetect 2025**(wnu-1.1;13k 段落叙事分类)、**RAAMove 2024**(arXiv 2403.15872;摘要 move 语料)、**Kobak et al. 2025**(excess vocabulary) | L1 分类器训练 / move 自动化 / 断点设计 | https://aclanthology.org/2025.wnu-1.1.pdf ;https://arxiv.org/html/2403.15872v1 |
| 备选 | Espeland & Sauder 2007(榜单反应性);Beese et al. 2023(AI 论文 stance) | RQ8 动态子问题 / 立场分类先例 | 见前文 |

21. RQ9 支撑(2026-08-15 补):PeerJudge(开放评审褒/贬自动检测,NLP 工具)https://www.researchgate.net/publication/342618173_Automatically_detecting_open_academic_review_praise_and_criticism ;self-promotion 惩罚及其准确性调节(Scopelliti et al. 线;"Is self-promotion evaluated more positively if it is accurate?" https://www.researchgate.net/publication/324755568 );Sumner et al. 2016(PLOS ONE,新闻稿夸张源于机构通稿——污名话语的相邻案例)
22. RQ0 支撑(2026-08-15 补):de Marcellis-Warin et al. 2025(89.3 万条 AI 推文数据集,2017–2023)https://pmc.ncbi.nlm.nih.gov/articles/PMC12361611/ ;Mongeon et al. 2022(学者推特 6000 万事件)https://arxiv.org/pdf/2208.11065 ;Gieryn 1983 boundary-work(*AJS*,降级为经验层描述);r/MachineLearning 审稿文化帖(toxicity thread、NeurIPS 公开宣传帖——英文污名话语存在性证据)
23. 模态框架经典(2026-08-15 补,用户提示;写作时核对版本):Latour, B. & Woolgar, S. 1979/1986 *Laboratory Life: The [Social] Construction of Scientific Facts*(事实构造、模态连续体、TRF(H) 案例);Latour, B. 1987 *Science in Action*(ready-made science vs science in the making);Latour, B. 1999 *Pandora's Hope*(blackboxing 与 circulating reference)——**全项目反二元论的理论根基:叙事不是科学的包装,而是科学的构造方式;被指控的从来不是讲故事,而是"没做够铭写劳动就领走事实地位"**
