---
id: marginalia-029
title: "AGENTS.md 之前：ICSE 1976–1999 里关于文档、过程与“机器读的文档”的论文清单"
date: 2026-11-13
published: 2026-11-13
kind: survey (literature survey)
sources:
  - "dblp ICSE 年度目录 icse76–icse99（https://dblp.org/db/conf/icse/），逐年逐条浏览约 1,190 条记录；2026-11-09/10"
  - "ACM Digital Library 论文页（经 dblp 电子版链接定位）；OpenAlex 与 Crossref API（DOI、页码、摘要）"
  - "筛选依据：agent-doc-evolution 项目（AI 编码时代开源文档的演化、文档债务、工具与社区的共演）"
initial-prompt: '你能不能派个haiku subagent去用acm(用浏览器？）搜索一下ICSE conference在2000年前的论文或者talk里面哪些和我这个项目里面讨论相关的内容。'
agent: Claude Code
issue: 84
model: Claude Opus 5.5（Haiku 5.5 子代理执行检索）
---

# AGENTS.md 之前：ICSE 1976–1999 里关于文档、过程与“机器读的文档”的论文

> 今天的 AGENTS.md、CLAUDE.md、规则文件，是写给机器读、由机器执行的项目文档。这件事在软件工程里并不全新：1987 年 Osterweil 就主张“软件过程也是软件”，1988 年 Potts 与 Bruns 讨论如何把设计理由记下来，1994 年 Parnas 讲软件老化。这份清单从 ICSE 前 21 届（1976–1999）里挑出 89 篇与文档、过程、工具辅助和社区协作相关的论文与演讲，作为 agent-doc-evolution 项目的“前史”。

## 这份清单是怎么来的

- **范围**：ICSE 2（1976）至 ICSE 21（1999）。dblp 上没有 ICSE 1（1975）的目录，故未覆盖；1977、1980、1983、1986 年没有举办 ICSE。
- **筛选**：逐年浏览 dblp 目录（约 1,190 条），按标题挑出与文档、设计理由、过程、演化、配置管理、工具与助手、程序理解、需求、复用、协作相关的条目。测试、形式化方法和纯算法论文不收。
- **核实**：前 20 篇读过摘要后逐一给出“核心 / 背景”判断（无一剔除）。其余条目的入选理由来自标题，摘要供自行判断。
- **链接**：84 篇有 ACM DL 页面，来自 dblp 的电子版链接，并与 OpenAlex / Crossref 的 DOI 交叉核对。30 篇有可在 doi.org 解析的 DOI。
- **摘要**：67 篇找到摘要（OpenAlex 或 ACM DL 原文，未改写）。很多 1970–80 年代的 ICSE 论文在 ACM 上本来就没有摘要。
- **导入 Zotero**：带 `doi:` 链接的条目可以把 DOI 粘贴到 Zotero 的“通过标识符添加”。只有 `10.5555/...` 编号的条目是 ACM 内部编号，doi.org 无法解析，请打开 ACM DL 页面用 Zotero 浏览器插件保存。
- **摘要版权**：摘要原文版权归各出版方（ACM / IEEE）所有，此处仅为研究参考而引用，不在本站 CC BY-NC 许可范围内。

## 先读这十篇 {#top10}

| # | 年份 | 论文 | 一句话 |
|---|---|---|---|
| 1 | 1987 | [Software Processes Are Software Too](#p-t01) | 把过程描述当作机器能够运行的软件来处理。这对应于智能体指令文件和规则文件，它们正是智能体所执行的过程描述。 |
| 2 | 1987 | [On Building Software Process Models Under the Lamppost](#p-t02) | 主张形式化的过程模型只描述阶段结束时的制品，遗漏了产生这些制品的实际工作，这正是已记录过程与实际执行过程之间的差距。其实地研究方法，以及对沟通与决策的关注，都与研究文档与实践之间关系的工作相契合。 |
| 3 | 1988 | [Recording the Reasons for Design Decisions](#p-t03) | 把设计历史建模为制品（文档）与审议节点构成的网络，这与将文档与决策相连的行动者网络视角相吻合。与制品并列记录的理由，也关系到之后的智能体和维护者需要哪些内容被记录下来。 |
| 4 | 1991 | [Designing Software for Use by Humans, not Machines](#p-t04) | 标题暗示了软件制品面向机器还是面向人类读者的区分，但摘要讨论的是电信系统中将用户界面与处理逻辑分离。它与面向智能体的文档之间的联系是间接的，因此仅作背景保留。 |
| 5 | 1985 | [SODOS - A Software Documentation Support Environment: Its Use](#p-t05) | 把文档视为受管理的对象，并通过跨生命周期阶段的可追溯性相互链接，这是多层文档的一种早期形式。它是前代智能体的工具，因此可作为工具主题的背景材料。 |
| 6 | 1992 | [Process Programming by Hindsight](#p-t06) | 从已记录的历史中恢复过程描述，而不是事先撰写，这与从代码仓库历史中重建已记录的约定相呼应。其中的版本控制示例与本研究的数据非常接近。 |
| 7 | 1994 | [Software Aging](#p-t07) | 刻画软件产品的长期衰退与健康状况，是文档漂移与文档债务的概念基础。其关于关注长期健康的呼吁，支持对文档在时间中的维护进行研究。 |
| 8 | 1995 | [The World and the Machine](#p-t08) | 将现实世界（目的、实践）与机器区分开来，这类似于把人、工具与文档视为同一系统的行动者网络框架。其焦点在于开发实践中的扭曲，而非文档本身。 |
| 9 | 1999 | [Splitting the Organization and Integrating the Code: Conway's Law Revisited](#p-t09) | 表明稳定的计划和规格有助于协调，而不可预测的工作则需要自发的沟通渠道。这正是分布式开源工作中共享文档背后的社会技术张力。 |
| 10 | 1999 | [Software Evolution and 'light' Semantics](#p-t10) | 无法读取摘要，因此相关性判断只依据标题和清单中的描述（即软件变更下的含义）。在引用它支持任何论断之前，需要对照全文核实。 |

## 按年份索引 {#by-year}

| 年份 | ICSE | 篇数 | 论文 |
|---|---|---|---|
| 1976 | 2 | 5 | [Documentation Tools and Techniques](#p-r01) · [PSL/PSA: A Computer-Aided Technique for Structur…](#p-r02) · [Program Evolution and Its Impact on Software Eng…](#p-t18) · [Software Requirements: Are They Really a Problem](#p-r49) · [The Dimensions of Maintenance](#p-r23) |
| 1978 | 3 | 2 | [Software Engineering: A Keynote Address](#p-r65) · [Using a Behavioral Theory of Program Comprehensi…](#p-r43) |
| 1979 | 4 | 1 | [Software Engineering: As it is](#p-r68) |
| 1981 | 5 | 4 | [A Database Model for Effective Configuration Man…](#p-r32) · [Evaluation of a Software Requirements Document b…](#p-t16) · [Executable Requirements for Embedded Systems](#p-r50) · [The Effect of Modularization and Comments on Pro…](#p-t13) |
| 1982 | 6 | 7 | [An Editor for Documentation in pi-System to Supp…](#p-r03) · [An Examination of Evolution Dynamics](#p-r25) · [Configuration Control for Evolutional Software P…](#p-r30) · [DUAL: An Interactive Tool for Developing Documen…](#p-r04) · [Design, Implementation, and Evaluation of a Revi…](#p-r29) · [MAP: A Tool for Understanding Software](#p-r42) · [The Dimensions of Healthy Maintenance](#p-r24) |
| 1984 | 7 | 4 | [Fifteen Years of Psychology in Software Engineer…](#p-r46) · [Knowledge-Based Communication Processes in Softw…](#p-r37) · [PROUST: Knowledge-Based Program Understanding](#p-r36) · [The Modular Structure of Complex Systems](#p-r06) |
| 1985 | 8 | 4 | [Active Design Reviews: Principles and Practices](#p-r05) · [SODOS - A Software Documentation Support Environ…](#p-t05) · [Software Technology Maturation](#p-t20) · [The Software Knowledge Base](#p-r38) |
| 1987 | 9 | 8 | [An Architecture for Intelligent Assistance in So…](#p-t12) · [From Design to Redesign](#p-r35) · [Knowledge-Based Software Design Using Design Sch…](#p-r34) · [On Building Software Process Models Under the La…](#p-t02) · [Process Models, Process Programs, Programming Su…](#p-r12) · [Software Processes Are Software Too](#p-t01) · [Tailoring the Software Process to Project Goals …](#p-r21) · [Version Control in the Inscape Environment](#p-r31) |
| 1988 | 10 | 5 | [Enhancing Program Readability and Comprehensibil…](#p-r47) · [Evolution of Tools (Abstract)](#p-r40) · [Models of Software Development Environments](#p-r41) · [Recording the Reasons for Design Decisions](#p-t03) · [Theory-W Software Project Management: A Case Stu…](#p-r69) |
| 1989 | 11 | 2 | [A Model for the Reuse of Software Design Informa…](#p-r07) · [Software Process Modeling: Principles of Entity …](#p-r13) |
| 1990 | 12 | 5 | [A Decision-Based Configuration Process Model](#p-r33) · [LaSSIE: a Knowledge-based Software Information S…](#p-t19) · [Technology Transfer as Collaboration: The Recept…](#p-r58) · [The Evolution of Technology Transfer at MCC's So…](#p-r59) · [Use of Video for Program Documentation (Experien…](#p-r09) |
| 1991 | 13 | 6 | [Augmenting SADT to Develop Computer Support for …](#p-r57) · [Designing Software for Use by Humans, not Machin…](#p-t04) · [Extending the Potts and Bruns Model for Recordin…](#p-r08) · [Non-Technological Issues in Software Engineering](#p-r61) · [Software Reuse: is it delivering?](#p-r51) · [Tolerating Inconsistency](#p-t17) |
| 1992 | 14 | 3 | [High-Pressure Steam Engines and Computer Softwar](#p-r67) · [Process Programming by Hindsight](#p-t06) · [The Software Engineering Laboratory: An Operatio…](#p-r14) |
| 1993 | 15 | 4 | [A Process for Consolidating and Reusing Design K…](#p-r52) · [Documentation for Safety Critical Software](#p-t11) · [Expressing the Relationships Between Multiple Vi…](#p-r48) · [The Concept Assignment Problem in Program Unders…](#p-r44) |
| 1994 | 16 | 4 | [Comprehension Processes During Large Scale Maint…](#p-r45) · [Software Aging](#p-t07) · [Understanding 'Why' in Software Process Modellin…](#p-r15) · [What Small Business and Small Organizations Say …](#p-r60) |
| 1995 | 17 | 4 | [Architectural Mismatch or Why It's Hard to Build…](#p-r54) · [Automating Process Discovery Through Event-Data …](#p-r16) · [How to Deal With Deviations During Process Model…](#p-t15) · [The World and the Machine](#p-t08) |
| 1996 | 18 | 5 | [A Systematic Survey of CMM Experience and Result](#p-r17) · [Prototypes as Assets, not Toys: Why and How to E…](#p-r39) · [Supporting the Construction and Evolution of Com…](#p-r53) · [The Role of Experimentation in Software Engineer…](#p-r66) · [The Role of Software Development Methodologies: …](#p-r64) |
| 1997 | 19 | 5 | [An Empirical Study of Communication in Code Insp…](#p-r55) · [Anywhere, Anytime Code Inspections: Using the We…](#p-r56) · [Comprehension and Evolution of Legacy Software](#p-r28) · [Process Modelling - Where Next](#p-r63) · [Software Processes Are Software Too, Revisited: …](#p-r62) |
| 1998 | 20 | 8 | [A Conceptual Model of Software Maintenance](#p-r27) · [Conceptual Simplicity Meets Organizational Compl…](#p-r20) · [Extracting Concepts from File Names: A New File …](#p-r11) · [Overcoming the NAH Syndrome for Inspection Deplo…](#p-r18) · [The Ramp-Up Problem in Software Projects: A Case…](#p-t14) · [The Use of Goals to Surface Requirements for Evo…](#p-r26) · [Toward Computational Support for Software Proces…](#p-r19) · [Towards Better Software Projects and Contracts: …](#p-r22) |
| 1999 | 21 | 3 | [CHIME: Customizable Hyperlink Insertion and Main…](#p-r10) · [Software Evolution and 'light' Semantics](#p-t10) · [Splitting the Organization and Integrating the C…](#p-t09) |

## 1. 文档与设计理由 {#t1}

<a id="p-r01"></a>
**Documentation Tools and Techniques** (1976)  
John R. Mashey; D. W. Smith · ICSE 2 (1976), pp. 177–181 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807671) · `10.5555/800253.807671`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** Programmer's Workbench 环境中面向文档的早期工具，是清单中 2000 年以前最早的文档工具条目之一。

??? quote "摘要（原文，来源 OpenAlex）"
    In a software development project of any appreciable size, the production of usable, accurate documentation may well consume more effort than the production of the software itself. Several years of experience on many Programmer's Workbench projects have shown that document preparation should not be separated from software development and that the combination of a flexible operating system, a powerful command language, and good text processing facilities permits quick and convenient production of many kinds of documentation which might be otherwise unobtainable, impractical, or very expensive. Our basic approach has been to develop techniques for effective combination of existing UNIX facilities. A number of case histories are given to illustrate the flexibility, convenience, and general usefulness of these techniques.

<a id="p-r02"></a>
**PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis** (1976)  
Daniel Teichroew; Ernest A. Hershey III · ICSE 2 (1976), p. 2 · 仅摘要 · [ACM DL](https://dl.acm.org/citation.cfm?id=807641)  
**为什么相关：** 信息系统的机器可读结构化文档，接近于让工具能够解析文档的想法。

??? quote "摘要（原文，来源 ACM DL）"
    PSL/PSA is a Computer-Aided Structured Documentation and Analysis technique that was developed for, and is being used for, analysis and documentation of requirements and preparation of functional specifications for information processing systems. The present status of requirements definition is described as the basis for describing the problem which PSL/PSA is intended to solve. The basic concepts of the Problem Statement Language are introduced and the content and use of a number of standard reports that can be produced by the Problem Statement Analyzer are briefly described. The experience to date indicates that computer aided methods can be used to aid system development during the requirements definition stage and that the main factors holding back such use are not so much related to the particular characteristics and capabilities of PSL/PSA as they are to organizational considerations involved in any change in methodology and procedure.

<a id="p-t13"></a>
**The Effect of Modularization and Comments on Program Comprehension** (1981)  
Scott N. Woodfield; Hubert E. Dunsmore; Vincent Y. Shen · ICSE 5 (1981), pp. 215–223 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802534) · `10.5555/800078.802534`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 关于注释能提升理解力的实验证据，是文档对读者产生影响的先例。这里的读者是人类程序员，因此与智能体读者的联系只是类比性的。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 OpenAlex）"
    An experiment was conducted to investigate how different types of modularization and comments are related to programmers' ability to understand programs. Forty-eight experienced programmers were given eight different versions of the same program and asked to answer a twenty question quiz used to measure comprehension. These eight different versions were the result of the program being constructed with four types of modularization (monolithic, functional, super, and abstract data type), each with and without comments. Those subjects whose programs contained comments were able to answer more questions than those without comments. Also, those subjects who were given the abstract data type version of the program were able to do significantly better than those with any other type of modularization.

<a id="p-r03"></a>
**An Editor for Documentation in pi-System to Support Software Development and Maintenance** (1982)  
Yukikazu Nakamoto; T. Iwamoto; M. Hori; Kenichi Hagihara; Nobuki Tokura · ICSE 6 (1982), pp. 330–339 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=807775)  
**为什么相关：** 面向维护的文档编辑，与随代码一同保存的文档相关。

??? quote "摘要（原文，来源 ACM DL）"
    A lot of information necessary to maintain a software tends to be lost in conventional documentation. One of the leading causes is considered that the ideas of developers which maintainers will want to know later are not fixed in any documents while the ideas are fresh. To remove the cause, we propose a new description form, called a frame, and construct a system called π, to support a software through its lifetime. This system gathers all the information with the frames, stores it in a database and provides the various services with respect to programming and documentation. This paper describes the frames and a subsystem, called π-editor, which provides a user friendly interface to make it easy to gather essential information. By using frames, (1) the associated information around one programming concept can be gathered at one time and (2) lack of necessary information hardly arises. The editor has the distinguished features such as (1) a structure-oriented display editor, (2) facilities to display selective information, provide helpful user guides, and check input errors immediately.

<a id="p-r04"></a>
**DUAL: An Interactive Tool for Developing Documented Programs by Step-Wise Refinements** (1982)  
Luigi Petrone; Antonio Di Leva; Franco Sirovich · ICSE 6 (1982), pp. 350–359 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=807777)  
**为什么相关：** 程序与其文档一同开发，是文学式编程和自文档化开发的前身。

??? quote "摘要（原文，来源 ACM DL）"
    Programs are integrated hierarchical structures of formal texts - instructions - and informal texts - documentation. Only if there is a mechanical connection between program design and program development there can be higher chances that the program documentation, originated at design time, will not, sooner or later, become obsolete with respect to the current state of the system. DUAL is an interactive, incremental, intelligent editor of program and documentation texts to be used for software implementations whose anticipated life cycle is significantly long to deserve much attention. The screen interface plays a unique role in DUAL since it allows a visitor ( designer or maintenance engineer) “to replay” as many times as desired the evolution of the system from design to implementation. The access to the hierarchically organized Design Information is made easy and natural by the DUAL video oriented user interface.

<a id="p-r06"></a>
**The Modular Structure of Complex Systems** (1984)  
David Lorge Parnas; Paul C. Clements; David M. Weiss · ICSE 7 (1984), pp. 408–419 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801999) · `10.5555/800054.801999`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 为不同读者而组织的模块结构文档，与系统的分层文档相关。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper discusses the organization of software that is inherently complex because there are very many arbitrary details that must be precisely right for the software to be correct. We show how the software design technique known as information hiding or abstraction can be supplemented by a hierarchically-structured document, which we call a module guide. The guide is intended to allow both designers and maintainers to identify easily the parts of the software that they must understand without reading irrelevant details about other parts of the software. The paper includes an extract from a software module guide to illustrate our proposals.

<a id="p-r05"></a>
**Active Design Reviews: Principles and Practices** (1985)  
David Lorge Parnas; David M. Weiss · ICSE 8 (1985), pp. 132–136 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=319599)  
**为什么相关：** 把设计文档评审作为一个持续进行的活动，与文档如何被检查并保持更新相关。

??? quote "摘要（原文，来源 ACM DL）"
    Although many new software design techniques have emerged in the past 15 years, there have been few changes to the procedures for reviewing the designs produced using these techniques. This paper describes an improved technique, based on the following ideas, for reviewing designs. The efforts of each reviewer should be focussed on those aspects of the design that suit his experience and expertise. The characteristics of the reviewers needed should be explicitly specified before reviewers are selected. Reviewers should be asked to make positive assertions about the design rather than simply allowed to point out defects. The designers pose questions to the reviewers, rather than vice versa. These questions are posed on a set of questionnaires that requires careful study of some aspect of the design. Interaction between designers and reviewers occurs in small meetings involving 2 - 4 people rather than meetings of large groups. Illustrations of these ideas drawn from the application of active design reviews to the Naval Research Laboratory's Software Cost Reduction Project are included.

<a id="p-t05"></a>
**SODOS - A Software Documentation Support Environment: Its Use** (1985) ⭐  
Ellis Horowitz; Ronald Williamson · ICSE 8 (1985), pp. 8–14 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319571) · `10.5555/319568.319571`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 把文档视为受管理的对象，并通过跨生命周期阶段的可追溯性相互链接，这是多层文档的一种早期形式。它是前代智能体的工具，因此可作为工具主题的背景材料。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 OpenAlex）"
    This paper describes a computerized environment, SODOS (Software Documentation Support), which supports the definition and manipulation of documents used in developing software. An object oriented environment is used as a basis for the SODOS interface. SODOS is built around a Software Life Cycle (SLC) Model that structures all access to the documents stored in the environment. One advantage of this model is that it supports software documentation independent of any fixed methodology that the developers may be using. The main advantage of the system is that it permits traceability through each phase of the Life Cycle, thus facilitating the testing and maintenance phases. Finally the effort involved in learning and using SODOS is simplified due to a sophisticated "user-friendly" interface.

<a id="p-t03"></a>
**Recording the Reasons for Design Decisions** (1988) ⭐  
Colin Potts; Glenn Bruns · ICSE 10 (1988), pp. 418–427 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=55863) · [doi:10.1109/icse.1988.93722](https://doi.org/10.1109/icse.1988.93722)  
**为什么相关：** 把设计历史建模为制品（文档）与审议节点构成的网络，这与将文档与决策相连的行动者网络视角相吻合。与制品并列记录的理由，也关系到之后的智能体和维护者需要哪些内容被记录下来。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    The authors outline a generic model for representing design deliberation and the relation between deliberation and the generation of method-specific artifacts. A design history is regarded as a network consisting of artifacts and deliberation nodes. Artifacts represent specifications or design documents. Deliberation nodes represent issues, alternatives or justifications. Existing artifacts give rise to issue about the evolving design, an alternative is one of several positions that respond to the issue (perhaps calling for the creation or modification of an artifact), and a justification is a statement giving the reasons for and against the related alternative. The model is applied to the development of a text formatter. The example development is represented in hypertext and as a Prolog database, the two representations being shown to complement each other. The authors conclude with a discussion of the relation between this model and other work and of the implications for tool support and methods.

<a id="p-r07"></a>
**A Model for the Reuse of Software Design Information** (1989)  
Kevin W. Jameson · ICSE 11 (1989), pp. 205–216 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74615) · [doi:10.1145/74587.74615](https://doi.org/10.1145/74587.74615)  
**为什么相关：** 把设计信息当作可复用的制品，与文档作为持久知识相关。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper presents a general model for the representation and manipulation of module level software design information, leading to the effective reuse of software design information across different programming languages.Language independent design documents are represented as ASCII files containing tagged design information sufficient for the construction of a compilable program architecture.The resulting architecture is composed of documented module stubs which describe calling relationships, parameters, functional descriptions, and algorithms characteristic of the architecture.No executable code is included in the compilable modules.Frameworks of tagged locations in Zanguage dependent standard module templates are matched against corresponding tags in the ASCII design files, effectively blending language dependent and independent information into a compilable stub architecture.The process is reversible in that a language independent design file can be generated from an architecture in the standard tagged format, thus supporting the movement of design information across different programming languages.

<a id="p-r09"></a>
**Use of Video for Program Documentation (Experience Report)** (1990)  
Tom DeMarco; Curt Geertgens · ICSE 12 (1990), pp. 126–128 · 经验报告 · [ACM DL](https://dl.acm.org/citation.cfm?id=100314)  
**为什么相关：** 以非文本形式呈现的程序文档，涉及什么算作文档的问题。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r08"></a>
**Extending the Potts and Bruns Model for Recording Design Rationale** (1991)  
Lee · ICSE 13 (1991), pp. 114–125 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=256705)  
**为什么相关：** 扩展了设计理由的捕获，与 Potts & Bruns 条目直接相连。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-t11"></a>
**Documentation for Safety Critical Software** (1993)  
Courtois & Parnas · ICSE 15 (1993), pp. 315–323 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=257650) · [doi:10.1109/icse.1993.346033](https://doi.org/10.1109/icse.1993.346033)  
**为什么相关：** 把文档当作验证软件所需的、经过审慎规划的正式制品，是 2000 年以前对文档作为制品类型最接近的处理。该方法面向人工评估者，因此只是间接地与被工具和智能体读取的文档相关。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    The authors review some of the fundamental difficulties presented by the design and the validation of software for safety critical applications. They suggest that software formal documentation techniques ameliorate the problems described. The principles behind a method of documenting both requirements and software design are presented. The methods have been used by the Atomic Energy Control Board of Canada in its safety assessment of the shutdown software of the Darlington generating station (D.L. Parnas et al., 1991). The method is illustrated by applying it to a small portion of the safety feature actuation system of a PWR nuclear reactor.

<a id="p-r11"></a>
**Extracting Concepts from File Names: A New File Clustering Criterion** (1998)  
Nicolas Anquetil; Timothy Lethbridge · ICSE 20 (1998), pp. 84–93 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302172) · [doi:10.1109/ICSE.1998.671105](https://doi.org/10.1109/ICSE.1998.671105)  
**为什么相关：** 把文件名作为概念结构的来源，接近代码仓库中的命名惯例。

??? quote "摘要（原文，来源 OpenAlex）"
    Decomposing complex software systems into conceptually independent subsystems is a significant software engineering activity which received considerable research attention. Most of the research in this domain considers the body of the source code; trying to cluster together files which are conceptually related. We discuss techniques for extracting concepts (abbreviations) from a more informal source of information: file names. The task is difficult because nothing indicates where to split the file names into substrings. In general, finding abbreviations would require domain knowledge to identify the concepts that are referred to in a name and intuition to recognize such concepts in abbreviated forms. We show by experiment that the techniques we propose allow about 90% of the abbreviations to be found automatically.

<a id="p-r10"></a>
**CHIME: Customizable Hyperlink Insertion and Maintenance Engine for Software Engineering Environments** (1999)  
Premkumar T. Devanbu; Yih-Farn Chen; Emden R. Gansner; Hausi A. Müller; Johannes Martin · ICSE 21 (1999), pp. 473–482 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302679) · [doi:10.1145/302405.302679](https://doi.org/10.1145/302405.302679)  
**为什么相关：** 在软件制品之间插入并维护的超链接，与链接失效和跨文档一致性相关。

*ACM DL / OpenAlex 均无摘要。*

## 2. 过程、组织与社会层面 {#t2}

<a id="p-t02"></a>
**On Building Software Process Models Under the Lamppost** (1987) ⭐  
Bill Curtis; Herb Krasner; Vincent Y. Shen; Neil Iscoe · ICSE 9 (1987), pp. 96–105 · 专题讨论论文 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41776) · `10.5555/41765.41776`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 主张形式化的过程模型只描述阶段结束时的制品，遗漏了产生这些制品的实际工作，这正是已记录过程与实际执行过程之间的差距。其实地研究方法，以及对沟通与决策的关注，都与研究文档与实践之间关系的工作相契合。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 ACM DL）"
    Most software process models are based on the management tracking and control of a project. The popular alternatives to these models such as rapid prototyping and program transformation are built around specific technologies, many of which are still in their adolescence. Neither of these approaches describe the actual processes that occur during the development of a software system. That is, these models focus on the series of artifacts that exist at the end of phases of the process, rather than on the actual processes that are conducted to create the artifacts. We conducted a field study of large system development projects to gather empirical information about the communication and technical decision-making processes that underlie the design of such systems. The findings of this study are reviewed for their implications on modeling the process of designing large software systems. The thesis of the paper is that while there are many foci for process models, the most valuable are those which capture the processes that control the most variance in software productivity and quality.

<a id="p-r12"></a>
**Process Models, Process Programs, Programming Support** (1987)  
M. M. Lehman · ICSE 9 (1987), pp. 14–16 · 大会报告 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41767) · `10.5555/41765.41767`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** Lehman 把过程模型视为程序的观点，与 Osterweil 的观点相互补充。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-t01"></a>
**Software Processes Are Software Too** (1987) ⭐  
Leon J. Osterweil · ICSE 9 (1987), pp. 2–13 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41766) · `10.5555/41765.41766`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 把过程描述当作机器能够运行的软件来处理。这对应于智能体指令文件和规则文件，它们正是智能体所执行的过程描述。（读过摘要后的判断：核心）

??? quote "摘要（原文，实为正文首段，来源 OpenAlex）"
    The major theme of this meeting is the exploration of the importance of.ul process as a vehicle for improving both the quality of software products and the the way in which we develop and evolve them. In beginning this exploration it seems important to spend at least a short time examining the nature of process and convincing ourselves that this is indeed a promising vehicle. We shall take as our elementary notion of a process that it is a systematic approach to the creation of a product or the accomplishment of some task. We observe that this characterization describes the notion of process commonly used in operating systems-- namely that a process is a computational task executing on a single computing device. Our characterization is much broader, however, describing any mechanism used to carry out work or achieve a goal in an orderly way.

<a id="p-r21"></a>
**Tailoring the Software Process to Project Goals and Environments** (1987)  
Victor R. Basili; H. Dieter Rombach · ICSE 9 (1987), pp. 345–359 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=41804)  
**为什么相关：** 依据情境裁剪过程，是 2000 年以前对项目专属规则文件的对应思路。

??? quote "摘要（原文，来源 ACM DL）"
    This paper presents a methodology for improving the software process by tailoring it to the specific project goals and environment. This improvement process is aimed at the global software process model as well as methods and tools supporting that model. The basic idea is to use defect profiles to help characterize the environment and evaluate the project goals and the effectiveness of methods and tools in a quantitative way. The improvement process is implemented iteratively by setting project improvement goals, characterizing those goals and the environment, in part, via defect profiles in a quantitative way, choosing methods and tools fitting those characteristics, evaluating the actual behavior of the chosen set of methods and tools, and refining the project goals based on the evaluation results. All these activities require analysis of large amounts of data and, therefore, support by an automated tool. Such a tool — TAME (Tailoring A Measurement Environment) — is currently being developed.

<a id="p-r13"></a>
**Software Process Modeling: Principles of Entity Process Models** (1989)  
Watts S. Humphrey; Marc I. Kellner · ICSE 11 (1989), pp. 331–342 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74631) · [doi:10.1145/74587.74631](https://doi.org/10.1145/74587.74631)  
**为什么相关：** 与其所作用实体相绑定的过程模型，与把文档视为过程实体相关。

??? quote "摘要（原文，来源 OpenAlex）"
    A defined software process is needed to provide organizations with a consistent framework for performing their work and im- proving the way they do it. An overall framework for modeling simplifies the task of producing process models, permits them to be tailored to individual needs, and facilitates process evolution. This paper outlines the principles of entity process, models and suggests ways in which they can help to address some of the problems with more conventional approaches to modeling software processes.

<a id="p-t06"></a>
**Process Programming by Hindsight** (1992) ⭐  
Pankaj K. Garg; Sanjay Bhansali · ICSE 14 (1992), pp. 280–293 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143128) · [doi:10.1145/143062.143128](https://doi.org/10.1145/143062.143128)  
**为什么相关：** 从已记录的历史中恢复过程描述，而不是事先撰写，这与从代码仓库历史中重建已记录的约定相呼应。其中的版本控制示例与本研究的数据非常接近。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 OpenAlex）"
    Process programming refers to the activity of algorithmicly describing models of programming activities (processes). A serious limitation of process programming has been that . it is often hard to describe a programming process a priori. In this paper we present an approach to process programming which addresses this limitation. Our approach is based on the premise that process programs are easier to describe in hindsight rather than by foresight, and hence can be synthe- sized by observing and analyzing a recorded process history. In this paper we describe an adaptation of the well-known explanation-based learning algorithm to synthesize a process fragment from a process history. We demonstrate the usefulness of the approach on a realistic example of coordinating file changes through a version control system.

<a id="p-r14"></a>
**The Software Engineering Laboratory: An Operational Software Experience Factory** (1992)  
Victor R. Basili; Gianluigi Caldiera; Frank E. McGarry; Rose Pajerski; Gerald T. Page; Sharon Waligora · ICSE 14 (1992), pp. 370–381 · Invited state-of-the-art paper · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143154) · [doi:10.1145/143062.143154](https://doi.org/10.1145/143062.143154)  
**为什么相关：** 通过可复用的经验库实现组织学习，是思考社区如何积累知识的基础。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r15"></a>
**Understanding 'Why' in Software Process Modelling, Analysis, and Design** (1994)  
Yu & Mylopoulos · ICSE 16 (1994), pp. 159–168 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=257757)  
**为什么相关：** 过程设计层面的设计理由，把设计理由这一主题与过程联系起来。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r16"></a>
**Automating Process Discovery Through Event-Data Analysis** (1995)  
Jonathan E. Cook; Alexander L. Wolf · ICSE 17 (1995), pp. 73–82 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225021) · [doi:10.1145/225014.225021](https://doi.org/10.1145/225014.225021)  
**为什么相关：** 从事件日志中恢复过程，这一方法可迁移到对开源软件仓库历史的挖掘中。

??? quote "摘要（原文，来源 OpenAlex）"
    Many software process methods and tools presuppose the existence of a formal model of a process.Unfortunately, developing a formal model for an on-going, complex process can be dificult, costly, and err-or prone.This presents a practical barrier to the adoption of process technologies.The barrier would be lowered by automatmg the creation of formal models.We are currently exploring techniques that can use basic event data captured from an on-going process to generate a formal model of process behavior.We term this kind of data analysis process discovery.Thts paper descr~bes and illustrates three methods with whzch we have been experimenting: algorithmic grammar inference, Markov models, and neural networks.

<a id="p-t15"></a>
**How to Deal With Deviations During Process Model Enactment** (1995)  
Gianpaolo Cugola; Elisabetta Di Nitto; Carlo Ghezzi; M. Mantione · ICSE 17 (1995), pp. 265–273 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225039) · [doi:10.1145/225014.225039](https://doi.org/10.1145/225014.225039)  
**为什么相关：** 指出书面的过程描述与其实际执行必然会出现偏离，这正是本研究所考察的已记录与已执行之间的差距。该论文提出容忍偏离的主张，也是为逐渐脱节的文档提供的一种设计选项。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    A fundamental problem in software processes is how the mintrinsic rigidity of a predejined (formal) model can be reconciled with the need for flexibility, change, and evolution.We therefore distinguish between software processes, as specified in a process description, and their actual performance by humans.Further, we claim that the two inevitably diverge, and thus it is necessary to provide means to reconcile them.We present a preliminary exploration into the problem.In particular, we illustrate how a temporal logic-based approach can be used to capture and tolerate some deviations from the process description during execution.We present a simple process language (LATIN), and its prototype environment (SENTINEL), in which these ideas are currently experimented.1

<a id="p-r17"></a>
**A Systematic Survey of CMM Experience and Results** (1996)  
Herbsleb & Goldenson · ICSE 18 (1996), pp. 323–330 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/227726.227791) · `10.5555/227726.227791`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 关于采用过程标准的实证证据，与社区如何采纳正式约定相关。

??? quote "摘要（原文，来源 OpenAlex）"
    The capability maturity model * (CMM) for sojlware has become very influential as a basis for software process improvement (SPI). Most of the evidence to date showing the results of these efforts has consisted of case studies. We present a systematic survey of organizations that have undertaken CMM-based SPI to get more representative results. Wefound evidence that process maturity is in fact associated with better organizational pe~ormance, and that software process appraisals are viewed, in retrospect, as extremely valuable and accurate guides for the improvement effort. The path was not always smooth, however, and e~orts generally took longer and cost more than expected. A number of factors that distinguished highly successful from unsuccessful efforts are identified. Most of these factors are under management control, suggesting that a number of specijic management decisions are likely to have a major impact on the success of the effort.

<a id="p-r20"></a>
**Conceptual Simplicity Meets Organizational Complexity: Case Study of a Corporate Metrics Program** (1998)  
James D. Herbsleb; Rebecca E. Grinter · ICSE 20 (1998), pp. 271–280 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302190) · [doi:10.1109/ICSE.1998.671136](https://doi.org/10.1109/ICSE.1998.671136)  
**为什么相关：** 决定工具项目成败的组织因素，与工具采纳相关。

??? quote "摘要（原文，来源 OpenAlex）"
    A corporate-wide metrics program faces enormous and poorly understood challenges as its implementation spreads out from the centralized planning body across many organizational boundaries into the sites where the data collection actually occurs. This paper presents a case study of the implementation of one corporate-wide program, focusing particularly on the unexpected difficulties of collecting a small number of straightforward metrics. Several mechanisms causing these difficulties are identified, including attenuated communication across organizational boundaries, inertia created by existing data collection systems, and the perceptions, expectations, and fears about how the data will be used. We describe how these factors influence the interpretation of the definitions of the measurements and influence the degree of conformance that is actually achieved. We conclude with lessons learned about both content and mechanisms to help in navigating the tricky waters of organizational dynamics in implementing a company-wide program.

<a id="p-r18"></a>
**Overcoming the NAH Syndrome for Inspection Deployment** (1998)  
Pankaj Jalote; M. Haragopal · ICSE 20 (1998), pp. 371–378 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302200) · [doi:10.1109/ICSE.1998.671390](https://doi.org/10.1109/ICSE.1998.671390)  
**为什么相关：** 抵制采用既有实践，是对新工具和规则进行被动采纳的先例。

??? quote "摘要（原文，来源 OpenAlex）"
    Despite considerable evidence to show that inspections can help reduce costs and improve quality, inspections are not widely deployed in the software industry. One of the likely reasons for this is the "not applicable here (NAH)" syndrome-developers and managers believe that in their environment, inspections will not provide the benefits seen by other organizations. One of the big challenges for deploying inspections is to overcome this syndrome. We describe two experiments that can be conducted, with little effort, in an organization to obtain data from the organization to build a case for inspections. By conducting one of these experiments, we were able to effectively overcome the NAH syndrome in our organization-many developers and managers are now ready to try inspections in their projects. Though the purpose of the experiment was to overcome the syndrome, the data from the experiment also shows how code inspections compare with unit testing in terms of defect detection capability, and the effect of inspections on the overall cost of development.

<a id="p-t14"></a>
**The Ramp-Up Problem in Software Projects: A Case Study of How Software Immigrants Naturalize** (1998)  
Susan Elliott Sim; Richard C. Holt · ICSE 20 (1998), pp. 361–370 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302199) · [doi:10.1109/ICSE.1998.671389](https://doi.org/10.1109/ICSE.1998.671389)  
**为什么相关：** 描述新加入者如何学习项目的规范，这与智能体和新贡献者如何从文档中学习相似。它是针对人的定性研究，因此两者之间的联系是概念性的。（读过摘要后的判断：背景）

??? quote "摘要（原文，实为正文首段，来源 OpenAlex）"
    Joining a software development team is like moving to a new country to start employment; the immigrant has a lot to learn about the job, the local customs, and sometimes a new language. In an exploratory case study, we interviewed four software immigrants, in order to characterize their naturalization process. Seven patterns in four major categories were found. In this paper, these patterns are substantiated, and their implications discussed. The lessons learned from this study can be applied equally to improving the naturalization process, and to the formulation of further research questions.

<a id="p-r19"></a>
**Toward Computational Support for Software Process Improvement Activities** (1998)  
Keishi Sakamoto; Kumiyo Nakakoji; Yasunari Takagi; Naoki Niihara · ICSE 20 (1998), pp. 22–31 · 论文 · [doi:10.1109/ICSE.1998.671099](https://doi.org/10.1109/ICSE.1998.671099)  
**为什么相关：** 面向过程改进工作的工具支持，与实践和工具的共同演化相关。

??? quote "摘要（原文，来源 OpenAlex）"
    Software organizations and projects need guidance on how to improve software process, not just guidelines on what to improve. Several surveys demonstrate that the Capability Maturity Model (CMM) and ISO-9000 only provide the latter. We report our in-depth analysis on a seventeen-month effort in software process improvement (SPI) at OMRON Corporation. The goal of the analysis was to identify issues and challenges of SPI and to design a step-wise practical method to avoid such problems. Major problems we have found include the lack of shared goal among stakeholders, insufficient understanding of the current progress of SPI efforts, and underutilization of a large amount of complex information generated during SPI. We present the method for software organizations and projects for dealing with the problems, and argue for a knowledge-based SPI support system based on the method.

<a id="p-r22"></a>
**Towards Better Software Projects and Contracts: Commitment Specifications in Software Development Projects** (1998)  
Jyrki Kontio; Olli Pitkänen; Reijo Sulonen · ICSE 20 (1998), pp. 486–489 · 论文 · [doi:10.1109/ICSE.1998.671612](https://doi.org/10.1109/ICSE.1998.671612)  
**为什么相关：** 以规格形式写下的当事方之间的承诺，与文档作为协调工具相关。

??? quote "摘要（原文，来源 OpenAlex）"
    Any software development project requires commitments from its participants. These commitments can include money, resources, deadlines, and specified functionality for the end product. The authors have developed a framework and a set of guidelines to support the specification of such commitments. They have evaluated the framework empirically in a series of case studies. The studies indicated that the framework addresses commitment specification issues that are normally not covered in project contracts and that the specification framework was considered beneficial by project representatives.

<a id="p-t09"></a>
**Splitting the Organization and Integrating the Code: Conway's Law Revisited** (1999) ⭐  
James D. Herbsleb; Rebecca E. Grinter · ICSE 21 (1999), pp. 85–95 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302455) · [doi:10.1145/302405.302455](https://doi.org/10.1145/302405.302455)  
**为什么相关：** 表明稳定的计划和规格有助于协调，而不可预测的工作则需要自发的沟通渠道。这正是分布式开源工作中共享文档背后的社会技术张力。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    It is widely acknowledged that coordination of large scale software development is an extremely difficult and persistent problem. Since the structure of the code mirrors the structure of the organization, one might expect that splitting the organization across time zones, cultures, and (natural) languages would make it difficult to assemble the components. This paper presents a case study of what indeed turned out to be the most difficult part of a geographically distributed software project, i.e., integration. Coordination problems were greatly exaggerated across sites, largely because of the breakdown of informal communication channels. The results imply that multi-site development can benefit to some extent from stable plans, processes, and specifications. The inherently unpredictable aspects of projects, however, require communication channels that can be invoked spontaneously, by developers, as needed. These results shed light on the problems and mechanisms underlying the coordination needs of development projects generally, be they co-located or distributed.

## 3. 演化、维护与衰退 {#t3}

<a id="p-t18"></a>
**Program Evolution and Its Impact on Software Engineering** (1976)  
M. M. Lehman; F. N. Parr · ICSE 2 (1976), pp. 350–357 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807698) · `10.5555/800253.807698`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 提供了大型系统通过维护与重构而持续演化的定量证据。它是本研究所依托的基础性演化成果，但它针对的是程序而非文档。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    Large scale, widely used programs such as operating systems are never complete. They undergo a continuing evolutionary cycle of maintenance, augmentation and restructuring to keep pace with evolving usage and implementation technologies. The paper provides quantitative evidence, from widely different environments, of the existence and nature of this evolutionary process. Interpretations and possible significance of some of the observed phenomena are discussed. Some implications for software engineering and for project planners and managers are noted.

<a id="p-r23"></a>
**The Dimensions of Maintenance** (1976)  
E. Burton Swanson · ICSE 2 (1976), pp. 492–497 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807723) · `10.5555/800253.807723`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 经典的维护分类学，可用于对文档维护活动进行归类。

??? quote "摘要（原文，来源 OpenAlex）"
    The area of software maintenance has been described by one author as an “iceberg.” (EDP Analyzer, 1972) Much goes on here that does not currently meet the eye. In part, this is the consequence of measurement difficulties. Practitioners and researchers can benefit from an understanding of the “dimensionality” of the maintenance problem. Some measures are suggested for coming to grips with this dimensionality, and problems of utilization associated with these measures are explored.

<a id="p-r25"></a>
**An Examination of Evolution Dynamics** (1982)  
M. J. Lawrence · ICSE 6 (1982), pp. 188–196 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807761) · `10.5555/800254.807761`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 对系统如何演化的实证考察，与随时间度量漂移相关。

??? quote "摘要（原文，来源 OpenAlex）"
    Data on the history of seven systems was analysed to statistically test the 5 laws of software evolution proposed first by Belady and Lehman in 1976.While there was some evidence supporting laws 1 and 2, laws 3-5 were not supported by the data. In the light of the result a new discontinuous model of software evolution is proposed to replace the smoothly changing continuous model proposed by Lehman.

<a id="p-r24"></a>
**The Dimensions of Healthy Maintenance** (1982)  
Robert S. Arnold; D. A. Parker · ICSE 6 (1982), pp. 10–27 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807744) · `10.5555/800254.807744`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 健康的维护是什么样子，与文档健康相关。

??? quote "摘要（原文，来源 OpenAlex）"
    What characterizes “healthy” or “satisfactory” software maintenance? How can we know it when we see it? This paper gives initial answers to these questions. We first argue the need for objectively measurable maintenance performance criteria in judging the “adequacy” of maintenance and present a set of criteria for judging maintenance performance in a particular software environment. We then subject the criteria to a practical test by applying them in this environment. We show how applying the criteria enables an informed overall maintenance performance appraisal, locates general maintenance problems, stimulates suggestions for improving maintenance on individual projects, allows these projects' maintenance to be compared and the projects ordered for improvement, and assesses the potential effectiveness of the suggestions in new project maintenance. We also sketch how criteria application can be generalized to software development monitoring and design methodology evaluation.

<a id="p-t07"></a>
**Software Aging** (1994) ⭐  
Parnas · ICSE 16 (1994), pp. 279–287 · Invited talk · [ACM DL](https://dl.acm.org/citation.cfm?id=257788) · [doi:10.1109/icse.1994.296790](https://doi.org/10.1109/icse.1994.296790)  
**为什么相关：** 刻画软件产品的长期衰退与健康状况，是文档漂移与文档债务的概念基础。其关于关注长期健康的呼吁，支持对文档在时间中的维护进行研究。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    Programs, like people, get old. We can't prevent aging, but we can understand its causes, take steps to limits its effects, temporarily reverse some of the damage it has caused, and prepare for the day when the software is no longer viable. A sign that the software engineering profession has matured will be that we lose our preoccupation with the first release and focus on the long-term health of our products. Researchers and practitioners must change their perception of the problems of software development. Only then will software engineering deserve to be called "engineering".

<a id="p-r28"></a>
**Comprehension and Evolution of Legacy Software** (1997)  
Václav Rajlich · ICSE 19 (1997), pp. 669–670 · 教程摘要 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253820) · [doi:10.1145/253228.253820](https://doi.org/10.1145/253228.253820)  
**为什么相关：** 遗留系统随其变化而被理解的问题。

??? quote "摘要（原文，来源 OpenAlex）"
    This tutorial presents an overview of legacy systems comprehension and evolution.Software comprehension typically consumes more than one-half of the programming effort with the legacy systems.Software evolution is a change in requirements and it is the most common type of change in legacy systems.

<a id="p-r27"></a>
**A Conceptual Model of Software Maintenance** (1998)  
Mira Kajko-Mattsson · ICSE 20 (1998), pp. 422–425 · 短文 · [doi:10.1109/ICSE.1998.671597](https://doi.org/10.1109/ICSE.1998.671597)  
**为什么相关：** 维护的概念模型，是文档维护的一个候选分析框架。

??? quote "摘要（原文，来源 OpenAlex）"
    Four distinct maintenance systems are studied and synthesised: the SEI quality framework and three industrial systems belonging to ABB, Ellemtel, and Ericsson. The goal is to validate the SEI framework, and to build a "state of the practice" conceptual model of the most fundamental software maintenance concepts. This model can help understand the underlying conditions for managing software maintenance. It can provide guidance to organisations in the process of building or improving their maintenance systems. It also constitutes a common basis for communication, for reasoning about software quality, and for building quality and maintenance models.

<a id="p-r26"></a>
**The Use of Goals to Surface Requirements for Evolving Systems** (1998)  
Annie I. Antón; Colin Potts · ICSE 20 (1998), pp. 157–166 · 论文 · [doi:10.1109/ICSE.1998.671112](https://doi.org/10.1109/ICSE.1998.671112)  
**为什么相关：** 以目标作为追踪需求在演化中变化的方式。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper addresses the use of goals to surface requirements for the redesign of existing or legacy systems. Goals are widely recognized as important precursors to system requirements, but the process of identifying and abstracting them has not been researched thoroughly. We present a summary of a goal-based method (GBRAM) for uncovering hidden issues, goals, and requirements and illustrate its application to a commercial system, an Intranet-based electronic commerce application, evaluating the method in the process. The core techniques comprising GBRAM are the systematic application of heuristics and inquiry questions for the analysis of goals, scenarios and obstacles. We conclude by discussing the lessons learned through applying goal refinement in the field and the implications for future research.

<a id="p-t10"></a>
**Software Evolution and 'light' Semantics** (1999) ⭐  
Dewayne E. Perry · ICSE 21 (1999), pp. 587–590 · Best paper, extended abstract · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302706) · [doi:10.1145/302405.302706](https://doi.org/10.1145/302405.302706)  
**为什么相关：** 无法读取摘要，因此相关性判断只依据标题和清单中的描述（即软件变更下的含义）。在引用它支持任何论断之前，需要对照全文核实。（读过摘要后的判断：背景）

*ACM DL / OpenAlex 均无摘要。*

## 4. 配置管理与版本控制 {#t4}

<a id="p-r32"></a>
**A Database Model for Effective Configuration Management in the Programming Environment** (1981)  
Karen E. Huff · ICSE 5 (1981), pp. 54–62 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802516) · `10.5555/800078.802516`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 保存在数据库中的配置数据。

??? quote "摘要（原文，来源 OpenAlex）"
    The effective management of configurations by programmers requires automatic techniques which are operative in the program development environment. In this paper, an abstract model is developed to cover the significant aspects of a typical programming environment pertinent to configuration management, using a database to capture configuration knowledge. The two aspects of the model deal with configuration identification and configuration control. In considering configuration identification, it is shown that the tools in the programming environment determine which configuration items need to be identified and also determine what the interesting and useful relations are among those items. In considering configuration control, the notion of a workspace, consisting of certain modification rights and certain visibility into the database, is developed to prevent conflict and to promote cooperation among programmers. The entire model can be used to evaluate the effectiveness of configuration management within a particular programming environment or as the basis of a programming environment design.

<a id="p-r30"></a>
**Configuration Control for Evolutional Software Products** (1982)  
Osamu Shigo; Yoshio Wada; Yuichi Terashima; Kanji Iwamoto; Takashi Nishimura · ICSE 6 (1982), pp. 68–83 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807749) · `10.5555/800254.807749`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 贯穿产品演化的配置控制。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper describes the concept of and a system for configuration control for evolutional software products, in which a wide spectrum of varied software products are being continuously evolved, along with rapid advancements in hardware technologies. The system contains a database for dealing with the overall configuration structure, including hierarchical product structure with change status, master file directories, difficulty occurrences and user information. The data representing the configuration can be in more abstract or macroscopic level than the traditional software configuration control, since the configuration manager should control the overall outlines for all software products. The concept and system described in the paper have been used for intelligent terminal software product management in NEC's Data Terminals Division.

<a id="p-r29"></a>
**Design, Implementation, and Evaluation of a Revision Control System** (1982)  
Walter F. Tichy · ICSE 6 (1982), pp. 58–67 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=807748)  
**为什么相关：** 修订控制，是本研究用于考察文档演化的代码仓库历史数据的前身。

??? quote "摘要（原文，来源 ACM DL）"
    The Revision Control System (RCS) is a software tool that helps in managing multiple revisions of text. RCS automates the storing, retrieval, logging, identification, and merging of revisions, and provides access control. It is useful for text that is revised frequently, for example programs and documentation. This paper presents the design and implementation of RCS. Both design and implementation are evaluated by contrasting RCS with SCCS, a similar system. SCCS is implemented with forward, merged deltas, while RCS uses reverse, separate deltas. (Deltas are the differences between successive revisions.) It is shown that the latter technique improves run-time efficiency, while requiring almost no extra space.

<a id="p-r31"></a>
**Version Control in the Inscape Environment** (1987)  
Dewayne E. Perry · ICSE 9 (1987), pp. 142–149 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41780) · `10.5555/41765.41780`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 某一环境中的版本控制。

??? quote "摘要（原文，来源 OpenAlex）"
    We present the important issues to be considered in version control mechanisms and characterize and compare the kinds of version control systems extant in current programming environments. We then characterize Inscape's version control mechanism. Invariant, and show that it makes several significant advances in the state of the art. Using Instress (Inscape's module interface specification language) specifications, Invariant provides a better understanding of the notion of parallel versions, a more comprehensive notion of version consistency, and a more flexible method of system composition than current mechanisms. In particular, Invariant provides a formalization of the notions of version equivalence and compatibility that correspond closely with our intuitive (and practical) notions of version equivalence and compatibility. These various forms of version compatibility provide the system builder with the concept of plug-compatibility — an extremely useful facility in composing systems from component parts.

<a id="p-r33"></a>
**A Decision-Based Configuration Process Model** (1990)  
Thomas Rose; Matthias Jarke · ICSE 12 (1990), pp. 316–325 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=100341)  
**为什么相关：** 把配置视为一个决策过程，将配置与设计理由联系起来。

*ACM DL / OpenAlex 均无摘要。*

## 5. 工具、助手与基于知识的支持 {#t5}

<a id="p-r42"></a>
**MAP: A Tool for Understanding Software** (1982)  
S. Warren · ICSE 6 (1982), pp. 28–39 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807745) · `10.5555/800254.807745`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 对既有软件进行理解的工具支持。

??? quote "摘要（原文，来源 OpenAlex）"
    Maintenance of software is a major problem that the data processing industry faces today. This paper describes MAP, a tool, that addresses the problems of software maintenance by helping programmers to understand their programs.

<a id="p-r37"></a>
**Knowledge-Based Communication Processes in Software Engineering** (1984)  
Gerhard Fischer; Matthias Schneider · ICSE 7 (1984), pp. 358–368 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801993) · `10.5555/800054.801993`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 通过知识库中介的开发者之间的沟通。

??? quote "摘要（原文，来源 OpenAlex）"
    A large number of problems to be solved with the help of computer systems are ill-structured. Their solution requires incremental design processes, because complete and stable specifications are net available.For tasks of this sort, life cycle models are inadequate. Our design methodology is based on a rapid prototyping approach which supports the coevolution of specification and implementation. Communication between customers, designers and implementors and communication between the humans and the knowledge base in which the emerging product is embedded are of crucial importance. Our work is centered around knowledge-based systems which enhance and support the communication needs in connection with software systems.Program documentation systems are used as an example to illustrate the relevance of knowledge-based human-computer communication in software engineering.

<a id="p-r36"></a>
**PROUST: Knowledge-Based Program Understanding** (1984)  
W. Lewis Johnson; Elliot Soloway · ICSE 7 (1984), pp. 369–380 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801994) · `10.5555/800054.801994`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 利用知识对程序进行的自动理解。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper1 describes a program called PROUST which does on- line analysis and understanding of Pascal programs written by novice programmers. PROUST takes as input a program and a non-algorithmic description of the program requirements, and finds the most likely mapping-between the requirements and the code. This mapping is in essence a reconstruction of the design and implementation steps that the programmer went through in writing the program. A knowledge base of programming plans and strategies, together with common bugs associated with them, is used in constructing this mapping. Bugs are discovered in the process of relating plans to the code; PROUST can therefore give deep explanations of program bugs by relating the buggy code to its underlying intentions.

<a id="p-r38"></a>
**The Software Knowledge Base** (1985)  
Bertrand Meyer · ICSE 8 (1985), pp. 158–165 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319611) · `10.5555/319568.319611`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 作为显式知识库的软件知识。

??? quote "摘要（原文，来源 OpenAlex）"
    We describe a system for maintaining useful information about a software project. The “software knowledge base” keeps track of software components and their properties; these properties are described through binary relations and the constraints that these relations must satisfy. The relations and constraints are entirely user-definable, although a set of predefined libraries of relations with associated constraints is provided for some of the most important aspects of software development (specification, design, implementation, testing, project management).The use of the binary relational model for describing the properties of software is backed by a theoretical study of the relations and constraints which play an important role in software development.

<a id="p-t12"></a>
**An Architecture for Intelligent Assistance in Software Development** (1987)  
Gail E. Kaiser; Peter H. Feiler · ICSE 9 (1987), pp. 180–188 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41783) · `10.5555/41765.41783`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 由规则驱动、作用于开发活动的智能助手，是直接读取规则文件并在代码仓库上行动的智能体的前身。规则即机器可读指令的模式，与本研究关注 AGENTS.md 和规则文件的焦点相吻合。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    We define an architecture for a software engineering environment that behaves as an intelligent assistant. Our architecture consists of three key aspects: an objectbase, a model of the software development activities, and controlled automation. Our objectbase is adapted from other research, but our model is unique in that is consists primarily of rules that define the preconditions and multiple postconditions of software development activities. Our most significant contribution is opportunistic processing, whereby the environment performs software development activities through controlled automation. This is accomplished by a forward and backward chaining interpretation of the rule set. Activities are automatically carried out at some time between when their preconditions are satisfied and when their postconditions are required. Automation is controlled through strategies that guide the assistant in choosing an appropriate point for carrying out each activity.

<a id="p-r35"></a>
**From Design to Redesign** (1987)  
Gerhard Fischer; Andreas C. Lemke; Christian Rathke · ICSE 9 (1987), pp. 369–376 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=41806)  
**为什么相关：** 借助设计知识支持的重新设计，与设计知识如何持续存在相关。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r34"></a>
**Knowledge-Based Software Design Using Design Schemas** (1987)  
Mitchell D. Lubars; Mehdi T. Harandi · ICSE 9 (1987), pp. 253–262 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41790) · `10.5555/41765.41790`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 编码在模式中的设计知识，是机器可读约定的前身。

??? quote "摘要（原文，来源 OpenAlex）"
    Design schemas provide a means for abstracting software designs into broadly reusable components that can be assembled and refined into new software designs. This paper describes a knowledge-based software development paradigm that is based on the design schema representation. It combines design schemas, domain knowledge, and various types of rules to assist in the quick generation of software designs from user specifications. A prototypical environment, IDeA (Intelligent Design Aid), is described that supports the knowledge-based paradigm. The schema-based techniques used in IDeA are presented along with some examples of their use.

<a id="p-r40"></a>
**Evolution of Tools (Abstract)** (1988)  
Kishida · ICSE 10 (1988), p. 2 · Technical keynote, abstract only · 无在线链接  
**为什么相关：** 工具的演化，与工具和实践共同变化相关。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r41"></a>
**Models of Software Development Environments** (1988)  
Dewayne E. Perry; Gail E. Kaiser · ICSE 10 (1988), pp. 60–68 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/55823.55830) · `10.5555/55823.55830`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 环境模型，为比较工具生态提供框架。

??? quote "摘要（原文，来源 OpenAlex）"
    We present a general model of software development environments that consists of three components: structures, mechanisms and policies. The advantage of this model is that it distinguishes intuitively those aspects of an environment that are useful in comparing and contrasting software development environments. Our initial application of the model is to characterize four classes of environments by means of a sociological metaphor based on scale: the individual, the family, the city and the state models. The utility of the IFCS taxonomy is that it delineates the important classes of interactions among software developers and exposes the ways in which current software development environments inadequately support the development of large systems. We demonstrate the generality of our model by also applying it to a previously published taxonomy that categorizes environments according to how they relate to four historical trends: language-centered, structure-oriented, toolkit and method-based environments.

<a id="p-t19"></a>
**LaSSIE: a Knowledge-based Software Information System** (1990)  
Premkumar T. Devanbu; Ronald J. Brachman; Peter G. Selfridge; Bruce W. Ballard · ICSE 12 (1990), pp. 249–261 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=100333) · [doi:10.1109/icse.1990.63631](https://doi.org/10.1109/icse.1990.63631)  
**为什么相关：** 关注难以察觉的项目知识，提供多视图与可被机器查询的索引。这与本研究的问题相近：项目知识如何在多层文档中变得机器可读。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    The authors discuss the important problem of invisibility that is inherent in the task of developing large software systems. It is pointed out that there are no direct solutions to this problem; however, there are several categories of systems-relational code analyzers, reuse librarians, and project management databases-that can be seen as addressing aspects of the invisibility problem. It is argued that these systems do not adequately deal with certain important aspects of the problem of invisibility-semantic proliferation, multiple views, and the need for intelligent indexing. A system called LaSSIE, which uses knowledge representation and reasoning technology to address each of these three issues directly and thereby help with the invisibility problem, has been built. The authors conclude with an evaluation of the system and a discussion of open problems and ongoing work.

<a id="p-r39"></a>
**Prototypes as Assets, not Toys: Why and How to Extract Knowledge from Prototypes** (1996)  
Schneider · ICSE 18 (1996), pp. 522–531 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=227840)  
**为什么相关：** 从原型中捕获知识，与知识离开开发者的头脑、进入文档相关。

*ACM DL / OpenAlex 均无摘要。*

## 6. 程序理解与人的因素 {#t6}

<a id="p-r43"></a>
**Using a Behavioral Theory of Program Comprehension in Software Engineering** (1978)  
Ruven E. Brooks · ICSE 3 (1978), pp. 196–201 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800099.803210) · `10.5555/800099.803210`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 应用于工程实践的理解理论，是推理读者（无论是人还是智能体）需要什么的基础。

??? quote "摘要（原文，来源 OpenAlex）"
    A theory is presented of how a programmer goes about understanding a program. The theory is based on a representation of knowledge about programs as a succession of knowledge domains which bridge between the problem domain and the executing program. A hypothesis and verify process is used by programmers to reconstruct these domains when they seek to understand a program.The theory is useful in several ways in software engineering: It makes accurate predictions about the effectiveness of documentation; it can be used to systematically evaluate and critique other claims about documentation, and it may even be a useful guideline to a programmer in actually constructing documentation.

<a id="p-r46"></a>
**Fifteen Years of Psychology in Software Engineering: Individual Differences and Cognitive Science** (1984)  
Bill Curtis · ICSE 7 (1984), pp. 97–107 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801956) · `10.5555/800054.801956`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 对软件工程中认知与个体因素的综述。

??? quote "摘要（原文，来源 OpenAlex）"
    Since the 1950's, psychologists have studied the behavioral aspects of software engineering. However, the results of their research have never been organized into a subfield of either software engineering or psychology. This failure results from the difficulty of integrating theory and data from the mixture of paradigms borrowed from psychology. This paper will review some of the psychological research on software engineering performed since the Garmisch Conference in 1968. This review will be organized under two of the psychological paradigms used in exploring programming problems: individual differences and cognitive science. The major theoretical and practical contributions of each area to the theory and practice of software engineering will be discussed. The review will end with a call for more research guided by the paradigm of cognitive science, since such results are the easiest to integrate with new developments in artificial intelligence and computer science theory.

<a id="p-r47"></a>
**Enhancing Program Readability and Comprehensibility with Tools for Program Visualization** (1988)  
Ronald Baecker · ICSE 10 (1988), pp. 356–366 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=55858)  
**为什么相关：** 可读性辅助手段，与制品是否可供人和工具阅读相关。

??? quote "摘要（原文，来源 ACM DL）"
    In order to make computer programs more comprehensible, the presentation of program source text, program documentation, and program execution needs to be enhanced over its conventional treatment. The paper describes a number of new techniques and tools developed to achieve these ends. One of these is a novel design for the effective presentation of source text in the C programming language using high quality digital typography, and a processor which implements the design. Some experimental evidence is summarized to demonstrate that the resulting source text presentation is significantly more readable and comprehensible than the presentation conventionally used today. Brief descriptions are also given of two other techniques, the development of a novel system of structured program documentation incorporating both text and graphics, and the portrayal of program execution with coloured computer animation.

<a id="p-t04"></a>
**Designing Software for Use by Humans, not Machines** (1991) ⭐  
Ruston, Muller, Cebulka · ICSE 13 (1991), pp. 104–113 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=256701) · [doi:10.1109/icse.1991.130628](https://doi.org/10.1109/icse.1991.130628)  
**为什么相关：** 标题暗示了软件制品面向机器还是面向人类读者的区分，但摘要讨论的是电信系统中将用户界面与处理逻辑分离。它与面向智能体的文档之间的联系是间接的，因此仅作背景保留。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 OpenAlex）"
    The authors describe an architecture that supports a more user-centered way to design software applications architectures, and by using a specific example, they also describe benefits gained by the software applications that result. The architecture aims to resolve some management and maintenance problems which have arisen in the telecommunications support systems network specifically, but which the authors also envision arising in any large-scale, multivendor, database environment. This examination includes consideration of technological advances in user-centered design, recent discoveries about the ability to separate processing functionalityfrom user interface functionality, and the rapidly expanding wealth of available user interface software tools.

<a id="p-r44"></a>
**The Concept Assignment Problem in Program Understanding** (1993)  
Biggerstaff, Mitbander, Webster · ICSE 15 (1993), pp. 482–498 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=257679)  
**为什么相关：** 将人的概念映射到代码，这正是智能体在阅读文档时所面临的问题。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r45"></a>
**Comprehension Processes During Large Scale Maintenance** (1994)  
von Mayrhauser & Vans · ICSE 16 (1994), pp. 39–48 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/257734.257741) · `10.5555/257734.257741`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 关于维护人员如何理解大型系统的实地研究。

??? quote "摘要（原文，实为正文首段，来源 OpenAlex）"
    We present results of observing professional maintenance engineers working with industrial code at actual maintenance tasks. Protocol analysis is used to explore how code understanding might differ for small versus large scale code. The experiment confirms that cognition processes work at all levels of abstraction simultaneously as programmers build a mental model of the code. Cognition processes emerged at three levels of aggregation representing lower and higher level strategies of understanding. They show differences in what triggers them and how they achieve their goals. Results are useful for defining core competencies which maintenance engineers need for their work and for documentation and development standards.

## 7. 由工具读取的需求与规格 {#t7}

<a id="p-r49"></a>
**Software Requirements: Are They Really a Problem?** (1976)  
Thomas E. Bell; T. A. Thayer · ICSE 2 (1976), pp. 61–68 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807650) · `10.5555/800253.807650`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 对需求文档问题的早期表述。

??? quote "摘要（原文，来源 OpenAlex）"
    Do requirements arise naturally from an obvious need, or do they come about only through diligent effort—and even then contain problems? Data on two very different types of software requirements were analyzed to determine what kinds of problems occur and whether these problems are important. The results are dramatic: software requirements are important, and their problems are surprisingly similar across projects. New software engineering techniques are clearly needed to improve both the development and statement of requirements.

<a id="p-t16"></a>
**Evaluation of a Software Requirements Document by Analysis of Change Data** (1981)  
Victor R. Basili; David M. Weiss · ICSE 5 (1981), pp. 314–324 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802544) · `10.5555/800078.802544`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 利用配置控制中的变更数据来评估需求文档，这接近于通过文档的演化来评估文档。它是为数不多的、直接测量文档变更历史的 2000 年以前论文之一。（读过摘要后的判断：核心）

??? quote "摘要（原文，来源 OpenAlex）"
    We describe in this paper an effective data collection method for evaluating software development methodologies, from definition of the objectives of the data collection to analysis of the results. We show how the data analysis can answer questions with respect to how successfully the goals of the development methodology are met. The A-7 requirements document is used as an example. We provide the results of data analyses conducted partway through the A-7 flight software development cycle, and discuss the utility of information obtained by such partial analyses. Results from the study show that data collection is feasible and useful when performed as part of configuration control, that data distributions based on partial data provide useful feedback to the developers, and that the A-7 Requirements Document is easily maintained and changed.

<a id="p-r50"></a>
**Executable Requirements for Embedded Systems** (1981)  
Pamela Zave; Raymond T. Yeh · ICSE 5 (1981), pp. 295–304 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802542) · `10.5555/800078.802542`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 工具可以执行的需求，与由机器阅读的文档相关。

??? quote "摘要（原文，来源 OpenAlex）"
    An approach to requirements specification for embedded systems, based on constructing an executable model of the proposed system interacting with its environment, is proposed. The approach is explained, motivated, and related to data-oriented specification techniques. Portions of a specification language embodying it are introduced, and illustrated with an extended example in which the requirements for a process-control system are developed incrementally.

<a id="p-t17"></a>
**Tolerating Inconsistency** (1991)  
Balzer · ICSE 13 (1991), pp. 158–165 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256748) · `10.5555/256664.256748`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 把不一致的数据标记出来并保持其可用，而不是禁止其存在，这是与文档漂移共存的一种机制。合作式设计的框架适合多方维护，但原文为非正式的正文，因此只作背景材料。（读过摘要后的判断：背景）

??? quote "摘要（原文，实为正文首段，来源 OpenAlex）"
    This is a short paper about a simple technique for making applications robust by marking data that violates specially identified invariants and using those marks as guards around code which is sensitive to that invariant.Such a capability is needed when dealing with the exceptions that arise in practical applications and distinguish them from idealized specifications. Previous techniques either required the removal of the constraint so that the exception would be allowed, or its modification to exclude the particular exception from the restriction.Our technique softens the entire constraint without introducing special cases, and is intended primarily for temporary exceptions. Rather than synchronizing all updates required by some constraint, it allows them instead to occur distributed in time in any arbitrary order. Thus, it is particularly useful in multiclient applications with shared responsibilities and authority, such as cooperative design (including software development).

<a id="p-r48"></a>
**Expressing the Relationships Between Multiple Views in Requirements Specification** (1993)  
Nuseibeh, Kramer, Finkelstein · ICSE 15 (1993), pp. 187–196 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=257610)  
**为什么相关：** 同一规格的多个视图保持一致，是多层文档的一个模型。

*ACM DL / OpenAlex 均无摘要。*

## 8. 复用、构件与体系结构 {#t8}

<a id="p-r51"></a>
**Software Reuse: is it delivering?** (1991)  
Frakes, Biggerstaff, Prieto-Díaz, Matsumura, Schäfer · ICSE 13 (1991), pp. 52–59 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256681) · `10.5555/256664.256681`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 实践中的复用，是复用采纳问题的最早形式。

??? quote "摘要（原文，来源 OpenAlex）"
    A panel discussion is presented to examine the evidence, pro and con, that software reuse is delivering. Verifiable and repeatable increases in software quality and productivity in field settings are used as criteria for the success of reuse. Reusability is defined as a technology that can be of significant value to software development and maintenance. A scale to evaluate whether reuse is delivering is outlined. The scale is ordinal, with five being the best possible rating. The three respondents, from Germany, Japan, and the US, discuss how reuse, as defined, is delivering in their parts of the world. >

<a id="p-r52"></a>
**A Process for Consolidating and Reusing Design Knowledge** (1993)  
Arango, Schoen, Pettengill · ICSE 15 (1993), pp. 231–242 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=257626)  
**为什么相关：** 为复用而整理的设计知识，与跨项目的约定复用相关。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r54"></a>
**Architectural Mismatch or Why It's Hard to Build Systems Out Of Existing Parts** (1995)  
David Garlan; Robert Allen; John Ockerbloom · ICSE 17 (1995), pp. 179–185 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225031) · [doi:10.1145/225014.225031](https://doi.org/10.1145/225014.225031)  
**为什么相关：** 各部分假设之间的不匹配，是工具与约定之间不匹配的先例。

??? quote "摘要（原文，来源 OpenAlex）"
    Many would argue that future breakthroughs in software productivity will depend on our ability to combine existing pieces of software to produce new applications.An important step towards this goal is the development of new techniques to detect and cope with mismatches in the assembled parts.Some problems of composition are due to low-level issues of interoperability, such as mismatches in programming languages or database schemas.However, in this paper we highlight a different, and in many ways more pervasive, class of problem: architectural mismatch.Specifically, we use our experience in building a family of software design environments from existing parts to illustrate a variety of types of mismatch that center around the assumptions a reusable part makes about the structure of the application in which is to appear.Based on this experience we show how an architectural view of the mismatch problem exposes some fundamental, thorny problems for software composition and suggests possible research avenues needed to solve them.

<a id="p-r53"></a>
**Supporting the Construction and Evolution of Component Repositories** (1996)  
Henninger · ICSE 18 (1996), pp. 279–288 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=227776)  
**为什么相关：** 不断演化的代码仓库，接近规则与约定仓库。

??? quote "摘要（原文，来源 ACM DL）"
    Repositories must be designed to meet the evolving and dynamic needs of software development organizations. Current software repository methods rely heavily on classification, which exacerbates acquisition and evolution problems by requiring costly classification and domain analysis efforts before a repository can be used effectively. This paper outlines an approach in which minimal initial structure is used to effectively find relevant software components while methods are employed to incrementally improve repository structures. The approach is demonstrated through PEEL, a tool to semi-automatically identify reusable components, and CodeFinder, a retrieval system that compensates for the lack of explicit knowledge structures through spreading activation retrieval and allows component representations to be incrementally improved while users are searching for information. The combination of these techniques yields a flexible software repository that minimizes up-front costs and improves its retrieval effectiveness as developers use it to find reusable software artifacts.

## 9. 协作、分布式工作与技术转移 {#t9}

<a id="p-t20"></a>
**Software Technology Maturation** (1985)  
Samuel T. Redwine Jr.; William E. Riddle · ICSE 8 (1985), pp. 189–200 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319624) · `10.5555/319568.319624`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 描述技术如何从概念走向广泛的专业应用，以及什么能加速这一过程。这与本研究中文档工具的被动采纳与主动采纳之别相对应，但该论文并未直接涉及文档或智能体。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 ACM DL）"
    We have reviewed the growth and propagation of a variety of software technologies in an attempt to discover natural characteristics of the process as well as principles and techniques useful in transitioning modern software technology into widespread use. What we have looked at is the technology maturation process, the process by which a piece of technology is first conceived, then shaped into something usable, and finally "marketed" to the point that it is found in the repertoire of a majority of professionals. A major interest is the time required for technology maturation — and our conclusion is that technology maturation generally takes much longer than popularly thought, especially for major technology areas. But our prime interest is in determining what actions, if any, can accelerate the maturation of technology, in particular that part of maturation that has to do with transitioning the technology into widespread use. Our observations concerning maturation facilitators and inhibitors are the major subject of this paper.

<a id="p-r58"></a>
**Technology Transfer as Collaboration: The Receptor Group** (1990)  
Priscilla J. Fowler · ICSE 12 (1990), pp. 332–333 · Position paper within the technology-transfer panel · [ACM DL](https://dl.acm.org/citation.cfm?id=100345)  
**为什么相关：** 把采纳视为接收方与提供方之间的协作，与被动采纳和共同塑造式采纳的区别相关。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r59"></a>
**The Evolution of Technology Transfer at MCC's Software Technology Program: From Didactic to Dialectic** (1990)  
James D. Babcock; Laszlo A. Belady; Nancy C. Gore · ICSE 12 (1990), pp. 290–299 · 论文 · [ACM DL](https://dl.acm.org/doi/10.5555/100296.100337) · `10.5555/100296.100337`（ACM 内部编号，doi.org 无法解析）  
**为什么相关：** 一个技术转移项目如何随时间变化，与工具和社区的共同演化相关。

??? quote "摘要（原文，来源 OpenAlex）"
    MCC's software technology program (STP) has a dual mission: to create tools and methodologies to assist development teams in the design of large, complex, distributed software systems, and to ensure the widespread diffusion of these technologies within STP shareholder organizations. STP has developed a comprehensive set of traditional technology transfer methods; although these methods make it possible to communicate research results successfully to shareholder receptors, they have spurred little actual use of released technology. STP has recently reevaluated its approach to technology transfer and discovered how it can be better accomplished-by fostering collaboration as its chief agent, rather than by depending on traditional transfer-and-feedback mechanisms. The authors describe the evolution of this new approach and present some of the results of collaborative experiences to date. It is found that collaborations revitalize research and that they empower STP's shareholders to affect the directions of that research. >

<a id="p-r57"></a>
**Augmenting SADT to Develop Computer Support for Cooperative Work** (1991)  
Marca · ICSE 13 (1991), pp. 94–103 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=256693)  
**为什么相关：** 计算机支持的协作工作，即 CSCW 的联系所在。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r61"></a>
**Non-Technological Issues in Software Engineering** (1991)  
Kellner, Curtis, DeMarco, Kishida, Schlumberger, Tully · ICSE 13 (1991), pp. 144–146 · 专题讨论 · [ACM DL](https://dl.acm.org/citation.cfm?id=256728)  
**为什么相关：** 社会与管理因素，与简短的立场论文归为一组。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r60"></a>
**What Small Business and Small Organizations Say About the CMM: Experience Report** (1994)  
Brodman & Johnson · ICSE 16 (1994), pp. 331–340 · 经验报告 · [ACM DL](https://dl.acm.org/citation.cfm?id=257795)  
**为什么相关：** 小型组织对过程标准的采纳，与社区采纳相关。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r55"></a>
**An Empirical Study of Communication in Code Inspections** (1997)  
Carolyn B. Seaman; Victor R. Basili · ICSE 19 (1997), pp. 96–106 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253248) · [doi:10.1145/253228.253248](https://doi.org/10.1145/253228.253248)  
**为什么相关：** 评审过程中的沟通，与问题讨论、评审、合并的流程相关。

??? quote "摘要（原文，来源 OpenAlex）"
    This paper describes an empirical study which addresses the issue of communication among members of a software development organization.In particular, data was collected concerning code inspections in one software development project.The question of interest is whether or not organizational structure (the network of relationships between developers) has an effect on the amount of effort expended on communication between developers.Both quantitative and qualitative methods were used, including participant observation, structured interviews, generation of hypotheses from field notes, some simple statistical tests of relationships, and interpretation of results with qualitative anecdotes.The study results show that past and present working relationships between inspection participants affect the amount of meeting time spent in different types of discussion, thus affecting the overall meeting length.Reporting relationships and physical proximity also have an effect, as well as the point in the project that an inspection occurs.All but the last of these factors are organizational structure relationships.The contribution of the study is a set of well-supported hypotheses for further investigation.

<a id="p-r56"></a>
**Anywhere, Anytime Code Inspections: Using the Web to Remove Inspection Bottlenecks in Large-Scale Software Development** (1997)  
James Perpich; Dewayne E. Perry; Adam A. Porter; Lawrence G. Votta; Michael W. Wade · ICSE 19 (1997), pp. 14–21 · 论文 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253234) · [doi:10.1145/253228.253234](https://doi.org/10.1145/253228.253234)  
**为什么相关：** 以网络为媒介的评审，是在线协作的早期前身。

*ACM DL / OpenAlex 均无摘要。*

## 10. 主旨报告、特邀报告与展望 {#t10}

<a id="p-r65"></a>
**Software Engineering: A Keynote Address** (1978)  
C. A. R. Hoare · ICSE 3 (1978), pp. 1–4 · 主题演讲 · [ACM DL](https://dl.acm.org/citation.cfm?id=803183)  
**为什么相关：** 关于 1978 年软件工程现状的主旨报告；仅作一般背景。

??? quote "摘要（原文，来源 ACM DL）"
    This paper argues that our recent progress in the development of a sound programming methodology should not lead us to ignore the more difficult aspects of engineering; and that in future we should pay more attention to the quality of our designs, and not just the accuracy of their implementation.

<a id="p-r68"></a>
**Software Engineering: As it is** (1979)  
Barry W. Boehm · ICSE 4 (1979), pp. 11–21 · Invited paper · [ACM DL](https://dl.acm.org/citation.cfm?id=802916)  
**为什么相关：** 关于软件工程实际如何被实践的早期记述，与已记录过程和实际过程之间的差距相关。

??? quote "摘要（原文，来源 ACM DL）"
    This paper presents a view of software engineering as it is in 1979. It discusses current software engineering practice with respect to lessons learned in the past few years, and concludes that the lessons are currently not heeded roughly half of the time. The paper discusses some of the factors which may account for this lag, including rapid technological change, education shortfalls, technology transfer inhibitions, resistance to disciplined methods, inappropriate role models, and a restricted view of software engineering. The paper also updates a 1976 state of the art survey of software engineering technology, including such topics as requirements and specifications, design, programming, verification and validation, maintenance, software psychology, and software economics. It concludes that the field is making solid progress, but that it is growing more complex at a faster rate than we can put it in order.

<a id="p-r69"></a>
**Theory-W Software Project Management: A Case Study** (1988)  
Barry W. Boehm; Rony Ross · ICSE 10 (1988), pp. 30–40 · 论文 · [ACM DL](https://dl.acm.org/citation.cfm?id=55827)  
**为什么相关：** 利益相关者双赢管理，与协商式约定相关。

??? quote "摘要（原文，来源 ACM DL）"
    The search for a single unifying principle to guide software project management has been relatively unrewarding to date. Most candidate principles are either insufficiently general to apply in many situations, or so general that they provide no useful specific guidance. This paper presents a candidate unifying principle which appears to do somewhat better. Reflecting various alphabetical management theories (X, Y, Z), it is called the Theory W approach to software project management. Theory W: Make Everyone a Winner The paper explains the Theory W principle and its two subsidiary principles: Plan the flight and fly the plan; and, Identify and manage your risks. To test the practicability of Theory W, a case study is presented and analyzed: the attempt to introduce new information systems to a large industrial corporation in an emerging nation. The case may seem unique, yet it is typical. The analysis shows that Theory W and its subsidiary principles do an effective job both in explaining why the project encountered problems, and in prescribing ways in which the problems could have been avoided.

<a id="p-r67"></a>
**High-Pressure Steam Engines and Computer Software** (1992)  
Nancy G. Leveson · ICSE 14 (1992), pp. 2–14 · 主题演讲 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143076) · [doi:10.1145/143062.143076](https://doi.org/10.1145/143062.143076)  
**为什么相关：** 来自另一工程领域的经验教训。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-t08"></a>
**The World and the Machine** (1995) ⭐  
Michael Jackson · ICSE 17 (1995), pp. 283–292 · 主题演讲 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225041) · [doi:10.1145/225014.225041](https://doi.org/10.1145/225014.225041)  
**为什么相关：** 将现实世界（目的、实践）与机器区分开来，这类似于把人、工具与文档视为同一系统的行动者网络框架。其焦点在于开发实践中的扭曲，而非文档本身。（读过摘要后的判断：背景）

??? quote "摘要（原文，来源 OpenAlex）"
    As software developers we are engineers because we make useful machines.We are concerned both with the world, in which the machine serves a useful purpose, and with the machine itself.The competing demands and attractions of these two concerns must be appropriately balanced.Failure to balance them harms our work.Certainly it must take some of the blame for the gulf between researchers and practitioners in software development.To achieve proper balance we must sometimes fight against tendencies and inclinations that are deeply ingrained in our customary practices and attitudes in software development.In this paper some aspects of the relationship between the world and the machine are explored; some sources of distortion are identified; and some suggestions are put forward for maintaining a proper balance.

<a id="p-r66"></a>
**The Role of Experimentation in Software Engineering: Past, Current, and Future** (1996)  
Basili · ICSE 18 (1996), pp. 442–449 · 主题演讲 · [ACM DL](https://dl.acm.org/citation.cfm?id=227818)  
**为什么相关：** 软件工程中的实证方法。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r64"></a>
**The Role of Software Development Methodologies: Past, Present, and Future** (1996)  
DeMarco · ICSE 18 (1996), pp. 2–4 · 主题演讲 · [ACM DL](https://dl.acm.org/citation.cfm?id=227730)  
**为什么相关：** 方法论的历史与展望。

*ACM DL / OpenAlex 均无摘要。*

<a id="p-r63"></a>
**Process Modelling - Where Next** (1997)  
M. M. Lehman · ICSE 19 (1997), pp. 549–552 · 大会报告 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253441) · [doi:10.1145/253228.253441](https://doi.org/10.1145/253228.253441)  
**为什么相关：** Lehman 关于过程建模的观点。

??? quote "摘要（原文，来源 OpenAlex）"
    After limited interest prior to the 1980s, the software process attracted the attention of a small group of researchers and practitioners as evidenced by a series of International Process Workshops commencing with the first in 1984.General interest had, however, to wait until Osterweil's now classic paper being honoured today and the present author's response were delivered at ICSE 87.This brief paper seeks to move forward from the positions presented then to introduce three process related issues, software process improvement, feedback in the software process and business process improvement.The first is, currently the principal focus of the software process community.The second, it is believed, should be.The third is equally relevant.Individually and collectively these issues appear, to this author at least, to make the majority view of the current focus of process modelling in general and process programming in particular largely irrelevant.

<a id="p-r62"></a>
**Software Processes Are Software Too, Revisited: An Invited Talk on the Most Influential Paper of ICSE 9** (1997)  
Leon J. Osterweil · ICSE 19 (1997), pp. 540–548 · Invited talk · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253440) · [doi:10.1145/253228.253440](https://doi.org/10.1145/253228.253440)  
**为什么相关：** 对 1987 年那篇论文的回顾。

??? quote "摘要（原文，来源 OpenAlex）"
    The ICSE 9 paper, "Software Processes are Software Too," suggests that software processes are themselves a form of software and that there are considerable benefits that will derive from basing a discipline of software process development on the more traditional discipline of application software development.This paper attempts to clarify some misconceptions about this original ICSE 9 suggestion and summarizes some research carried out over the past ten years that seems to confirm the original suggestion.The paper then goes on to map out some future research directions that seem indicated.The paper closes with some ruminations about the significance of the controversy that has continued to surround this work.
