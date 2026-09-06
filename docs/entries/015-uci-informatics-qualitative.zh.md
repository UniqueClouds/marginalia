# UCI Informatics 系的质性 HCI 版图——调研:谁在做质性、STS 与健康信息

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](015-uci-informatics-qualitative.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-09-05</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> survey(院系调研)</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #39</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-015</td></tr><tr><td>title</td><td>UCI Informatics 系的质性 HCI 版图——调研:谁在做质性、STS 与健康信息</td></tr><tr><td>date</td><td>2026-09-05</td></tr><tr><td>published</td><td>2026-09-05</td></tr><tr><td>kind</td><td>survey(院系调研)</td></tr><tr><td>issue</td><td>39</td></tr></table></details>

> 院系调研。问题:一个 informatics 系里,"非软件工程"的那半边到底由哪些学术共同体构成,其中做**质性研究、偏 STS、偏人类学**的学者都在做什么?本文用四条途径交叉验证——系官网名单结构化、系自维护的 CHI/CSCW 逐年论文列表、OpenAlex 逐作者作品拉取(2022–2026)、实验室与个人主页的自述原文。**结论先行:这个系的"质性半边"呈三块一线——批判/STS–人类学、质性健康+可及性、游戏/学习/青年文化;健康信息方向质性浓度很高,"健康 = 做系统 + user study"的刻板印象只对一半;2025–26 最大的新簇是 GenAI × 残障/健康。**

## 一、动机与方法

想系统回答"某个系里谁在做质性"这类问题,单靠记忆或搜索都不够:人事变动快、同名学者多、emeriti 与在任混在一起。本次用四条途径交叉:

1. **名单表**:抓系官网 People 页并结构化(职称/轨制/分组),先分清 Core Faculty、Affiliated、Emeriti、教学轨;
2. **实验室与学生**:抓各实验室/中心主页的自述原文(EVOKE、ARC、CREATE、CLL、PIE Lab 等),从论文作者名单反推学生研究方向;
3. **OpenAlex 逐人拉取**:2022–2026 作品清单(注意同名消歧——"Yunan Chen"会匹配到一位材料学者,"Kai Zheng"会匹配到中医文献,要用姓名+机构双重过滤);
4. **场馆扫描**:系里自己维护 CHI/CSCW 逐年论文列表页(这个比 OpenAlex 更全,还带获奖信息),期刊侧补 BD&S/STHV/ToCHI 的机构过滤查询。

一个实操发现:OpenAlex 里 UC Irvine 的 institution id 是 `I204250578`,用 `raw_author_name.search` + `institutions.id` 组合过滤可以绕开大部分同名坑。

## 二、格局速览与近期变动

**三块一线**的构成(排除 SE 阵营:van der Hoek、Malek、Ahmed、Garcia、Moshirpour、James A. Jones、Thomas Zimmermann、Daye Nam 等):

- **批判 / STS–人类学**:Paul Dourish、Melissa Mazmanian、Roderic Crooks、Mimi Ito;
- **质性健康 + 可及性**:Yunan Chen、Madhu Reddy、Daniel Epstein、Elena Agapie、Stacy Branham、Anne Marie Piper、Gillian Hayes;
- **游戏 / 学习 / 青年文化集群**(Connected Learning Lab 旗下):Kurt Squire、Constance Steinkuehler、Katie Salen Tekinbas、Kylie Peppler、Aaron Trammell;
- **量化/实现一翼**(健康信息另一面):Kai Zheng、Sean Young;外加可持续据点 Bill Tomlinson。

近期结构性变动(对"印象里的系"更新很有必要):

- **Emeriti 化**:Gloria Mark(注意力研究)、Bonnie Nardi(科技人类学)、Geoffrey Bowker(STS)、Gary & Judy Olson(CSCW 奠基者)、David Redmiles 均已转荣休;Nardi 仍有论文问世(ToCHI 2023 *Post-growth Human–Computer Interaction*)。
- **离职**:Yubo Kou、Bryan Semaan 已不在系 People 页。
- **新进**:Elena Agapie(前 Microsoft Research)、Anne Marie Piper、Madhu Reddy(前 Penn State)——三位都是质性 HCI 的强手,构成实质性的新鲜血液。
- **行政与荣誉**:Yunan Chen 任系主任;Dourish 获 **2025 ACM SIGCHI 终身研究成就奖**、任 Steckler Center(CREATE)主任;Hayes 升任 Vice Provost for Academic Personnel(仍带 STAR 组);Mazmanian 与 Merage 商学院 joint appointment;Piper 任 CHI 2026 Accessibility Subcommittee Chair;Dourish 组博士生 Eunkyung Jo 获 CHI 2026 Outstanding Dissertation Award。

## 三、核心学者总表

方法/理论列是综合自述与论文版图的判读;自述关键词尽量取原文。

| 学者 | 位置 | 自述方向(关键词) | 方法/理论 | 近两年代表 topic |
|---|---|---|---|---|
| **Paul Dourish** | Chancellor's Professor;CREATE 主任 | 把人类学、STS、文化研究用于数字实践;**data imaginaries**;理论资源:实用主义、符号互动论、实践理论、英国文化研究、女性主义认识论、去殖民批判、常人方法学 | 民族志;批判理论 | 地方政府数据关系(CSCW'24 *Reconfiguring Data Relations*);编程美学(STHV'24,与 Mazmanian) |
| **Melissa Mazmanian** | 教授;Merage 商学院 joint | "trained as a sociologist of work";技术在使用实践中(creative work、predictive systems、quantification、busy professionals 的日常) | 组织民族志;meso-organization theory | 数据完整性的生态观(MISQ'25 *The Myth of Good Data*);政府数据叙事(BD&S'25);照护危机;一线服务者 data work(CHI'26) |
| **Roderic Crooks** | 副教授;EVOKE Lab PI | 接续 **social informatics** 传统:"racial, cultural, ethical, and political dimensions of computing";借 HCI、STS、media studies、**Black studies** | 社会信息学;数据正义;质性与设计 | 社区组织者的数据实践;监禁国家与信息技术;监视与种族(Surveillance & Society);政府作为设计语境 |
| **Mimi Ito** | Professor in Residence;CLL 主任 | 数字青年文化的人类学家 + learning scientist;connected learning | 文化人类学;参与式/设计研究 | 主编 *Youth Well-Being by Design*(MIT Press 2026);Youth Connections for Wellbeing;neurodiversity × AI;儿童算法权利 |
| **Stacy Branham** | 副教授;ARC | 可及计算;"informed by **disability studies, critical theory, participatory design, action research**" | 质性;共同设计;autoethnography | 盲/低视力者用 GenAI;成人盲文学习者;BLV 软件从业者职业流动;生命转折期与技术(TACCESS'26) |
| **Anne Marie Piper** | 副教授;CREATE 副主任 | 可及性、老年、照护、human-AI interaction | 质性/混合;参与式设计 | 盲低视力雇员的 *Accessibility Paradox*(CSCW'25 Best Paper);GenAI 信息获取不确定性;老年×对话 AI 综述;中国聋人创作者手语翻译工作(CHI'26 HM) |
| **Yunan Chen** | 教授兼**系主任** | HCI × CSCW × Health Informatics 交点;"how health information is generated, managed, shared, and utilized" | 强质性 CSCW;sociotechnical 信息实践 | 保姆零工 risk work(CSCW'25 HM + CHI'26);car dwellers(CHI'26);心理健康对话中的 ChatGPT(CSCW'25 Best Paper);青少年与 health AI 设计虚构 |
| **Madhu Reddy** | 教授;Grad Programs Associate Dean | CSCW × 心理健康/健康 IT;患者安全 | 质性 + co-design | 抑郁自管理工具包;亚裔美国人数字心理健康 co-design(CHI'25);台湾 emerging adults 心理福祉;Black 成人抑郁工具;Reddit 压力支持(CSCW'25) |
| **Daniel Epstein** | 副教授;PIE Lab | personal informatics;HCI × health | 质性+混合;部署+访谈 | 育儿追踪的时间性;家庭健康追踪生态;女性健康与遗传;弃用实践;公共机构 AI 健康聊天机器人 |
| **Elena Agapie** | 助理教授(前 MSR) | HCI × health 的**目标**与行为改变;数字心理健康参与 | 质性+混合;临床合作 | therapist–client 目标协作(CSCW'24);行为改变目标元分析(CHI'25);日常目标中断(CHI'26) |
| **Gillian Hayes** | Chancellor's Professor;Vice Provost | "design, develop, deploy, and evaluate technologies…in sensitive and ethically responsible ways";assistive + educational tech + health informatics | 混合方法;参与式设计 | 自闭症×LLM 偏见(CHI'25);噪声敏感可穿戴(CHI'26);ADHD 学生协作;南非幼儿社会情感评估 co-design |
| **Kurt Squire / Constance Steinkuehler / Katie Salen / Kylie Peppler** | CLL 群 | 游戏×学习;毒性/极端主义(话语分析);play 理论;learning sciences/making | 设计研究;混合;话语分析 | 社区取向 GenAI 设计(再入社会青少年);游戏毒性;博物馆游戏化(CHI'25 HM);craft×计算思维;Child–AI co-creation |
| **Aaron Trammell** | 教授 | 游戏研究、亚文化、race/whiteness 与游戏文化;Analog Game Studies 主编 | 批判媒体研究;文化研究 | D&D 与种族/欲望;极客与白人性;后女性主义控制(GLaDOS 章) |
| **Kai Zheng / Sean Young** | 教授 | 健康 IT、ambient AI;社交媒体 × 公共卫生行为 | 偏定量/实现科学 + 质性穿插 | ambient AI 临床文档的医生编辑行为(JAMIA'26 系列);数字心理健康系统落地;HIV 检测的社交媒体干预 |

Affiliated 但常被算进这个圈子的:Bonnie Ruberg(现为 Film & Media Studies,**queer game studies**,质性+批判媒体理论)、June Ahn(Education 系,Informatics by courtesy,participatory design/RPP)、Stephen Schueller、Candice Odgers(心理科学,数字心理健康/青少年)、Mark Warschauer(Education)。

## 四、健康信息的两面(最容易被误读的一块)

健康信息(Health Informatics)在这个系里是**双层的**:

- **质性 CSCW 一翼**:Chen 的信息实践传统(现场考察照护者/病人的 work)、Reddy 的心理健康 co-design、Epstein 的个人信息学、Agapie 的目标与临床协作。他们的产出主体是 PACMHCI 论文,方法以访谈、田野、co-design 为主;
- **量化/实现一翼**:Zheng 的临床 NLP 与 ambient AI 文档研究(JAMIA 高产)、Young 的社交媒体行为干预(公共卫生试验)、Future Health 研究所的可穿戴与 agentic AI(工程导向,由 Ramesh Jain / Amir Rahmani 主理)。

两翼共享 Future Health 等机构,但学术品味几乎不同。想跟做质性健康研究的人,看错门会很痛苦。

## 五、场馆扫描

系官网自维护逐年列表(比数据库更全、更快,还记获奖与 committee 角色):

- **CSCW 2025:14 篇**。两篇 Best Paper(Piper 的 accessibility paradox;Chen 组的 ChatGPT 心理健康对话)+ 一篇 Honorable Mention(Chen 组的保姆零工 risk work)。主题簇:心理健康×LLM/平台、无障碍、照护与零工经济、政府数据与公共记录、住房不稳定的 infrastructural work。
- **CHI 2025:28 篇**(含 LBW/SIG/Workshop)。数字心理健康×少数族裔、BLV×GenAI、个人信息学、Aging×对话 AI、 clinically useful AI 的全球视野、游戏与学习。
- **CHI 2026:23 篇 full paper**。最大新簇是 **GenAI × 残障/健康**(自闭症 LLM 偏见、盲人用 GenAI、口吃者标注 co-design、AI 无障碍的 rhetoric vs responsibility、青少年眼中的 health AI)。
- **期刊侧(OpenAlex 2023–26)**:PACMHCI 36 篇;Big Data & Society 1 篇(Mazmanian 组政府数据叙事);STHV 1 篇(Dourish/Mazmanian 编程美学);ToCHI 5 篇。4S 会议不被 OpenAlex 有效索引,只能靠各自主页追踪。

## 六、方法论注记与局限

- **同名消歧是逐人拉取的最大坑**:同名不同人会导致"某教授近两年研究突变成完全不相关的领域"的假象,务必姓名+机构双过滤后人工抽查标题;
- **系官网的逐年论文列表是被低估的数据源**:比 OpenAlex 及时(2026 届的都上线了)、含获奖与 committee 角色、且已按系归属过滤;
- 快照时效:人事数据为 2026-09-05 状态;Emeriti 是否仍带学生、各 Lab 是否招生,以各自页面为准(EVOKE 页面明示只走 Graduate Division 通道且要求相关经验);
- 本文是公开信息的版图调研,不构成任何招生/申请判断。

---

*Read this note in [English](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/015-uci-informatics-qualitative/note.en.md).*


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](015-uci-informatics-qualitative.en.md)

