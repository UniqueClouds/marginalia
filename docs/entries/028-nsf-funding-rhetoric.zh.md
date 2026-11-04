# 摘要是一份微型提案：NSF 资助摘要的修辞拆解——软件工程、AI 与社会、科学学与组织研究

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](028-nsf-funding-rhetoric.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-11-04</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #81</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-028</td></tr><tr><td>title</td><td>摘要是一份微型提案：NSF 资助摘要的修辞拆解——软件工程、AI 与社会、科学学与组织研究</td></tr><tr><td>date</td><td>2026-11-04</td></tr><tr><td>published</td><td>2026-11-04</td></tr><tr><td>kind</td><td>analysis</td></tr><tr><td>issue</td><td>81</td></tr></table></details>

> 读这些文本不是为了抄一套“获奖公式”，而是观察作者怎样把一个重要问题压缩成可评审的研究计划：为什么现在要做、现有理解哪里不够、项目具体怎样推进、团队凭什么做得到，以及成果会到达谁手里。

## 先说明材料边界

截至 2026-11-03，本地筛选集包含 **19,630 项** NSF 奖项记录。筛选沿用此前的范围：主要关注软件工程、计算机、人工智能（含 AI 与社会）、计算社会科学、科学学、创新和组织研究；一般排除总金额低于 $200,000 的项目，学生专门资助例外；排除 fellowship、会议以及此前逐轮排除的学科。这里的条目只做修辞近读，不替代本地全量数据库，也没有把全部摘要搬进公开仓库。

主题标签彼此重叠，不能相加：计算机与计算 18,687 项、人工智能 12,493 项、软件工程 7,738 项、创新研究 1,443 项、AI 与社会 / 人本 AI 730 项、计算社会科学 504 项、科学学 / 科学政策 424 项、组织研究 270 项。按奖项记录显示金额计算，中位数约 **$461,435**，均值约 **$722,141**；均值受少数大型计算基础设施奖项影响。CAREER 标签有 2,950 项，占筛选集约 15%，其中位金额约 $522,748；项目期限中位数约四年。金额是奖项记录中的项目总额，不是年度预算、实际支出或 PI 个人所得；全部项目总额也不能解释为某一年的 NSF 支出。

**这里读到的是 NSF 公开 award abstract，不是完整申请书。** NSF 说明，Award Search 提供资助摘要，提交的 proposal 属于提交机构的保密知识产权；因此我没有找到这些获资助申请书的完整正文。每个案例都链接回 NSF 原页面，供你查看完整公开摘要。项目摘要与论文成果能帮助观察项目如何被公开呈现，但不能还原完整的研究计划、预算论证、评审意见或评审者真实判断。

**查看完整摘要原文：**[打开 19,630 条项目浏览页](docs/028-nsf-award-browser.zh.md)。每条记录可展开查看英文摘要、PI/学校/金额/学科元数据、NSF 页面列出的论文成果，以及原数据中已有的中文译文；也可按标题、PI、学校、领域和金额筛选。

## 可以标注的论证链

一个常见、但不是每篇摘要都照此排列的结构是：

**重要性 / 谁受影响 → 具体缺口或反常之处 → 项目主张与研究对象 → 方法如何逐步回答问题 → 团队、场景与资源如何支撑 → 可交付成果由谁使用、怎样产生影响。**

| 写作动作 | 读者需要看见什么 | 自查问题 |
|---|---|---|
| 建立 stakes | 问题影响哪些人、系统或决策；“重要”最好有范围或证据 | 删除“transformative”之后，问题仍然清楚吗？ |
| 把 gap 写成张力 | 现有方法为什么不够，或一个现象为什么与主流预期不符 | 你指出的是可验证的缺口，还是只说“研究很少”？ |
| 给出可辨认的研究对象 | 一个机制、能力、系统或理论对象，而不是一串宏大名词 | 能否用一句话说清项目要理解或改变什么？ |
| 让方法形成链条 | 每项方法回答哪个问题、产生什么证据、怎样送到下一步 | 访谈、模型、实验各自承担的工作是否不同？ |
| 建立可行性 | 数据、研究场景、合作方、跨学科能力、前期基础 | 这些资源是项目实际依赖的条件，还是只在名单里出现？ |
| 具体化影响 | 产出 → 使用者 → 使用渠道 → 可观察的变化 | broader impacts 是否具体到课程、工具、政策流程或社区合作？ |
| 校准承诺 | 能检验的目标、边界、风险和备选方案 | “因果”“可信”“普适”“突破”分别靠什么证据成立？ |

## 六个近读案例：按奖项总额从高到低

下表是为了覆盖用户关心的研究方向而做的**示范性近读**，不代表对 19,630 条摘要的完整修辞编码，也不表示这些措辞导致了获资助。金额和 PI 按 NSF 记录列出。

| 金额 | 项目、PI 与机构 | NSF / 学科定位 | 可以观察的修辞动作 |
|---:|---|---|---|
| $20,000,000 | [Global Observatory and Virtual Laboratory for Science and Technology Advance](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2404109) · James A. Evans · University of Chicago | APTO；科学学、技术创新与政策 | 把全球技术竞争变成“观测站 + 虚拟实验室”的研究基础设施 |
| $20,000,000 | [Institute for Trustworthy AI in Law and Society (TRAILS)](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2229885) · Hal Daumé · University of Maryland, College Park | CISE / AI Research Institutes；AI 与社会 | 从透明度与公众信任问题，铺到跨技术、社会、感知和治理的研究架构 |
| $1,299,701 | [Qualitative Data Repository 2021–2024](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2116935) · Sebastian Karcher · Syracuse University | SBE / Social and Economic Sciences；科学基础设施与研究方法 | 把“仓库”写成促成透明、累积与伦理分享的公共基础设施 |
| $1,195,189 | [Understanding the Algorithmic Workplace](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1928608) · H. C. Robinson · Northeastern University | SBE / Social and Economic Sciences；计算社会科学、组织与工作研究 | 把多方法设计写成从劳动者经验到模型、再到实地检验的证据链 |
| $1,085,570 | [Formal and Informal Boundary Spanning in Multiteam Systems](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1231154) · John R. Hollenbeck · Michigan State University | Science of Organizations / Virtual Organizations；创新与组织研究 | 用“正式 / 非正式”关系的张力，聚焦跨团队知识与创新问题 |
| $846,731 | [CAREER: Scientist-in-the-loop-software testing](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2339830) · Joshua S. Sunshine · Carnegie Mellon University | CISE / Software & Systems Foundations；软件工程、CAREER | 从科学软件缺陷的实际后果，连接测试工具、基础研究与教育活动 |

### 1. 把宏观竞争压成一个可想象的研究装置：APTO

项目摘要用“**global observatory and virtual laboratory**”（“全球观测站与虚拟实验室”）把科学与技术竞争从抽象议题转成研究装置。公开摘要的论证顺序是：全球领导力变化 → 美国需要理解技术能力、生产与使用 → 汇集跨技术与跨组织数据 → 建立大型语言模型作为“数字双胞胎” → 用模拟实验分析政策杠杆 → 为资助方、政策制定者和研究者提供 dashboard。

它的修辞优势是**把一组复杂技术变成可复述的基础设施愿景**，并且把模型、模拟和最终用户放在同一条路线图上。值得追问的是，“digital double”和“causal estimation”都承担很重的承诺：需要说明模型如何验证、模拟结果如何与真实政策效应区分。摘要提出要做，不等于已经证明能做到。

NSF 记录列出的相关论文之一是 Wu、Esposito 与 Evans 的 [“Shifting power asymmetries in scientific teams reveal China’s rising leadership in global science”](https://doi.org/10.1073/pnas.2414893122)，发表于 *PNAS*。奖项页面将论文列为项目成果；这类列表说明官方记录有关联，不意味着该奖项是论文的唯一资金来源。

### 2. 把技术性能问题拓展为社会信任与治理问题：TRAILS

摘要先承认 AI 的能力承诺，再提出反向张力：“**Current AI systems are not created in a way that is transparent**”（“当前 AI 系统的构建方式并不透明”）。随后将透明度不足连接到公众信任、潜在伤害和技术采用，并以多机构研究所回应。研究计划把 Society、Technical Design、Socio-Technical Perceptions、Governance 组织成四个互相连接的 thrusts。

这里可学的是**先指出技术系统之外的社会条件，再说明为何需要多学科、跨机构架构**。注意它并未把信任简化成单一技术指标：写自己的申请时，可以分别定义“人们是否信任”“系统是否值得信任”以及参与者是谁。否则“促进信任”会变成难以核验的总目标。

相关成果包括 TRAILS 团队成员的 [“The epistemologies of trust: conflicting worldviews in the ‘Trustworthy AI’ discourse”](https://doi.org/10.1007/s43681-026-01087-2)，*AI and Ethics*。NSF 项目记录列出该论文；在引用时仍应区分“记录关联”与“唯一资助”。可对照 [NSF AI Research Institutes solicitation](https://www.nsf.gov/funding/opportunities/national-artificial-intelligence-research-institutes/nsf22-502/solicitation)：申请摘要的架构既回应研究问题，也回应项目公告对 institute 规模、跨学科和合作网络的要求。

### 3. 把研究支持设施写成科学能力：QDR

QDR 摘要将自己称为“**an open repository dedicated to the curation, preservation, and publication of data**”（“一个专门用于数据整理、保存和发布的开放仓库”），但论证没有停在“我们要建一个仓库”。它接着把数据分享与复用连接到研究透明度、伦理和法律保障、累积性、严谨性与效率。

这是一种适合基础设施型项目的写法：**先交代服务，再解释它改变科研流程的机制**。相比只承诺一个平台，QDR 把可访问、可复用、合规分享写成多个受益环节。自己的申请可以继续追问：谁会使用？哪些数据能分享？伦理审查和参与者保护怎样落实？成功用什么指标衡量？

NSF 记录列出的相关出版物包括 [“Actually Accessible Data: An Update and a Call to Action”](https://doi.org/10.31274/jlsc.15449) 和 [“Teaching with shared data for learning qualitative data analysis”](https://doi.org/10.1080/1743727X.2024.2443935)。前者尤其能帮助读者思考“开放”与“可访问”之间的差别。

### 4. 让多方法设计像一条证据生产线：Algorithmic Workplace

这个项目把研究对象明确成“**workers, business organizations, and government institutions**”（“劳动者、企业组织与政府机构”）。然后依次提出平台劳动者经验资料、企业数据、劳动者行为模型、实地实验，并把结果分别送往企业留任与激励、政策制定者以及美国劳动力影响研究。

修辞上的关键不只是列出访谈、调查、模型和 field experiments，而是说明**前一步的证据怎样成为后一步的输入**。这种写法让多个方法看起来是同一问题的不同证据，而不是一串并列工具。风险是“综合优化”之类的大标题可能超过实际可识别的因果范围，所以摘要应交代模型预测如何被检验、实地实验能回答哪些问题。

有论文在正文中明确致谢 NSF award 1928608，例如 Vallas 与 Schor 的 [“Labour platforms as mechanisms of class reproduction”](https://doi.org/10.1332/27324176Y2024D000000023)，以及 Schor、Tirrell 与 Vallas 的 [“Consent and Contestation: How Platform Workers Reckon with the Risks of Gig Labor”](https://doi.org/10.1177/09500170231199404)。前者的核心修辞也值得读：从“算法控制”与劳动者对平台工作的支持之间的悖论，导出阶级位置和不同工作经验的解释。

### 5. 用一个可观察的理论张力组织组织研究：Boundary Spanning

项目标题本身就设置了“formal and informal”的分析对照。摘要先解释多团队系统为什么需要跨边界协作，再提出正式联络结构之外的非正式关系可能补强、也可能削弱正式结构。它随后把问题落在 Michigan State 的 FRIB 场景，并列出深入访谈、调查和网络分析。

值得借鉴的是：**理论张力—可观察场景—相应方法**三者互相对齐。场景不是装饰性的“亮点”；只有当它确实让研究者观察到所提机制时，才构成可行性论据。相关论文 Guo 等人的 [“When Discretionary Boundary Spanning Relationships Cease Becoming Discretionary”](https://doi.org/10.1037/apl0000911) 明确列出 NSF 1231154，同时也列出另一项 NSF 奖项；因此不能把它说成单一奖项独家资助的产出。

### 6. CAREER 如何把研究议程和教育议程扣在一起：Scientist-in-the-loop testing

摘要从一个具体后果切入：科学家日常写代码，程序缺陷可能让科学结论失效。它再指出训练缺口：“**scientists do not follow common testing practices**”（“科学家往往没有采用常见的软件测试实践”），然后收窄到可执行的研究目标：帮助科学程序员更有效地生成测试套件。

这个 CAREER 案例把**问题后果 → 技术研究 → 面向非计算机专业学生的课程与训练**连在一起。NSF CAREER 本身强调早期职业教师的研究与教育整合，因此教育并非事后添加的一段宣传，而是此项目的计划组成部分。可以对照 [CAREER 项目说明](https://www.nsf.gov/funding/opportunities/career-faculty-early-career-development-program)。

NSF 记录列出的成果包括 [“TestLoop: A Process Model Describing Human-in-the-Loop Software Test Suite Generation”](https://doi.org/10.1145/3765754) 与 [“TerzoN: Human-in-the-Loop Software Testing with a Composite Oracle”](https://doi.org/10.1145/3729359)。从申请修辞学习时，重点看摘要怎样把工具研究与教育活动合并成同一研究议程；读论文时则检查项目是否真的形成了对应的模型和工具。

## 从这些案例提炼出的写作练习

用一段话填完下面的骨架，再检查每个箭头是否有证据：

> 因为 **[有证据的问题]** 影响 **[明确的人群 / 系统 / 决策]**，现有 **[主流方法或解释]** 仍无法 **[指出具体限制]**。本项目研究 **[一个机制、能力或问题]**。我们将先用 **[方法 A]** 识别 **[证据]**，再用 **[方法 B]** 发展 **[模型 / 理论 / 工具]**，最后通过 **[方法 C]** 检验 **[什么结果]**。团队已有 **[数据、场景、合作关系或前期工作]**，支持这一路线。我们将向 **[明确受众]** 提供 **[可交付成果]**，通过 **[具体渠道]** 使用，并以 **[指标]** 评估进展。

改稿时逐项问：

1. 把“重要、创新、变革性、前所未有”删掉，问题和方法是否仍然成立？如果不成立，用对照数据或清楚的研究缺口替代形容词。
2. 每个方法是否对应一个研究问题？方法数量是否真的构成互补证据？
3. 影响链是否写出实际使用者与使用场景，而不只是“将产生广泛影响”？
4. 项目能证明到哪一步？将来可望实现的价值是否被写成已知事实？
5. CAREER 项目是否把教育设计与研究发现相连，说明具体课程、对象和评估方式？
6. 至少写明一个风险、边界或备选路径，让雄心看起来可管理，而不是无边界承诺。

## 不要从获奖摘要中推出的结论

- 这六个项目是用于覆盖目标主题的例子，不是随机抽样；它们不能代表 19,630 个项目的平均修辞风格。
- 我们读到的是获奖后的公开摘要，没有失败申请作为对照。因此不能说某个修辞动作“带来了”资助。
- Peng、Qiu、Fosse 与 Uzzi 的研究 [“Promotional language and the adoption of innovative ideas in science”](https://doi.org/10.1073/pnas.2320066121) 使用了资助与未资助申请文本，发现 promotional language 与资助、创新性及后续影响存在关联；其中的词语替换实验测量的是文本带来的正面印象，不是真实评审中的随机处理。它提示修辞值得研究，不意味着应堆砌夸张词或过度宣称。
- NSF Award Search 的成果列表以及论文致谢可以帮助追踪关联，但“页面列为成果”不等于“该奖项是唯一资金来源”。
- 完整申请书、详细预算论证和评审材料不在公开摘要里。本笔记因此分析的是**资助项目如何公开讲述自己的计划**，而不是完整 proposal 的全部写作策略。


<div class='marg-attach'><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> 附属材料：[028-nsf-award-browser.en.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/028-nsf-funding-rhetoric/docs/028-nsf-award-browser.en.md) · [028-nsf-award-browser.zh.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/028-nsf-funding-rhetoric/docs/028-nsf-award-browser.zh.md)</div>


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](028-nsf-funding-rhetoric.en.md)

