---
id: marginalia-029
title: "ICSE 1976–1999 老论文与摘要"
date: 2026-11-13
published: 2026-11-13
kind: survey (reading list)
sources:
  - "dblp ICSE year tables icse76–icse99 (https://dblp.org/db/conf/icse/)"
  - "ACM Digital Library paper pages; OpenAlex and Crossref APIs (abstracts, DOIs)"
initial-prompt: '你能不能派个haiku subagent去用acm(用浏览器？）搜索一下ICSE conference在2000年前的论文或者talk里面哪些和我这个项目里面讨论相关的内容。'
agent: Claude Code
issue: 84
model: Claude Opus 5.5 (searches by Haiku 5.5 subagents)
---

# ICSE 1976–1999 老论文与摘要

ICSE 前 21 届（1976–1999）中挑出的 89 篇论文与演讲，按年份排列，附原文摘要及中文翻译（67 篇有摘要；其余在 ACM DL / OpenAlex 上没有）。摘要版权归 ACM / IEEE 所有，仅供阅读参考，不在本站 CC BY-NC 许可范围内。

## 1976 · ICSE 2 {#y1976}

### Documentation Tools and Techniques

John R. Mashey; D. W. Smith · pp. 177–181 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807671)

> In a software development project of any appreciable size, the production of usable, accurate documentation may well consume more effort than the production of the software itself. Several years of experience on many Programmer's Workbench projects have shown that document preparation should not be separated from software development and that the combination of a flexible operating system, a powerful command language, and good text processing facilities permits quick and convenient production of many kinds of documentation which might be otherwise unobtainable, impractical, or very expensive. Our basic approach has been to develop techniques for effective combination of existing UNIX facilities. A number of case histories are given to illustrate the flexibility, convenience, and general usefulness of these techniques.

**中文翻译**：在任何规模可观的软件开发项目中，编写可用且准确的文档所耗费的工作量，很可能超过软件本身的开发工作量。在 Programmer's Workbench 的多个项目上积累的数年经验表明，文档编制不应与软件开发相分离；灵活的操作系统、强大的命令语言以及良好的文本处理设施相结合，能够快速、方便地生成多种类型的文档，而这些文档在其他情况下可能难以获得、不切实际或成本极高。我们的基本思路是开发有效组合现有 UNIX 设施的技术。文中给出了若干案例，以说明这些技术的灵活性、便利性和普遍实用性。

### PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems (Abstract)

Daniel Teichroew; Ernest A. Hershey III · p. 2 · [ACM DL](https://dl.acm.org/citation.cfm?id=807641)

> PSL/PSA is a Computer-Aided Structured Documentation and Analysis technique that was developed for, and is being used for, analysis and documentation of requirements and preparation of functional specifications for information processing systems. The present status of requirements definition is described as the basis for describing the problem which PSL/PSA is intended to solve. The basic concepts of the Problem Statement Language are introduced and the content and use of a number of standard reports that can be produced by the Problem Statement Analyzer are briefly described. The experience to date indicates that computer aided methods can be used to aid system development during the requirements definition stage and that the main factors holding back such use are not so much related to the particular characteristics and capabilities of PSL/PSA as they are to organizational considerations involved in any change in methodology and procedure.

**中文翻译**：PSL/PSA 是一种计算机辅助的结构化文档编制与分析技术，最初是为信息处理系统的需求分析与文档编制以及功能规格说明的编写而开发并投入使用的。文章首先阐述了需求定义的现状，以此作为描述 PSL/PSA 所要解决问题的基础。文中介绍了问题陈述语言（Problem Statement Language）的基本概念，并简要说明了问题陈述分析器（Problem Statement Analyzer）可生成的若干标准报告的内容与用法。迄今的经验表明，计算机辅助方法可以在需求定义阶段辅助系统开发；阻碍此类方法应用的主要因素，与 PSL/PSA 的具体特性和能力关系不大，而更多地与任何方法论和流程变革所涉及的组织因素有关。

### Program Evolution and Its Impact on Software Engineering

Meir M. Lehman; Francis N. Parr · pp. 350–357 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807698)

> Large scale, widely used programs such as operating systems are never complete. They undergo a continuing evolutionary cycle of maintenance, augmentation and restructuring to keep pace with evolving usage and implementation technologies. The paper provides quantitative evidence, from widely different environments, of the existence and nature of this evolutionary process. Interpretations and possible significance of some of the observed phenomena are discussed. Some implications for software engineering and for project planners and managers are noted.

**中文翻译**：大规模、广泛使用的程序（如操作系统）从来都不是完整的。它们会经历持续的演化周期，包括维护、扩充和重构，以跟上不断变化的使用方式和实现技术。本文从差异很大的多种环境中提供了这一演化过程之存在及其性质的定量证据。文中讨论了对部分观察现象的解释及其可能意义，并指出了其对软件工程以及项目规划者和管理者的若干启示。

### Software Requirements: Are They Really a Problem

Thomas E. Bell; T. A. Thayer · pp. 61–68 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807650)

> Do requirements arise naturally from an obvious need, or do they come about only through diligent effort—and even then contain problems? Data on two very different types of software requirements were analyzed to determine what kinds of problems occur and whether these problems are important. The results are dramatic: software requirements are important, and their problems are surprisingly similar across projects. New software engineering techniques are clearly needed to improve both the development and statement of requirements.

**中文翻译**：需求是自然地源于某种显而易见的需要，还是只能通过艰苦努力才得以产生，而即便如此，其中仍然包含各种问题？我们分析了两类差异很大的软件需求数据，以确定会出现哪些问题，以及这些问题是否重要。结果颇为显著：软件需求十分重要，而其存在的问题在不同项目之间惊人地相似。显然，需要新的软件工程技术来改进需求的开发与陈述。

### The Dimensions of Maintenance

E. Burton Swanson · pp. 492–497 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807723)

> The area of software maintenance has been described by one author as an “iceberg.” (EDP Analyzer, 1972) Much goes on here that does not currently meet the eye. In part, this is the consequence of measurement difficulties. Practitioners and researchers can benefit from an understanding of the “dimensionality” of the maintenance problem. Some measures are suggested for coming to grips with this dimensionality, and problems of utilization associated with these measures are explored.

**中文翻译**：软件维护领域曾被一位作者比作一座“冰山”（EDP Analyzer，1972）。其中大量工作并不易被察觉。部分原因在于度量上的困难。从业人员和研究人员都可以从理解维护问题的“维度性”中获益。本文提出了一些用于把握这种维度性的度量，并探讨了这些度量在应用中存在的问题。

## 1978 · ICSE 3 {#y1978}

### Software Engineering: A Keynote Address

Charles Antony Richard Hoare · pp. 1–4 · [ACM DL](https://dl.acm.org/citation.cfm?id=803183)

> This paper argues that our recent progress in the development of a sound programming methodology should not lead us to ignore the more difficult aspects of engineering; and that in future we should pay more attention to the quality of our designs, and not just the accuracy of their implementation.

**中文翻译**：本文认为，我们在开发合理的程序设计方法论方面取得的近期进展，不应使我们忽视工程中更为艰难的方面；并且，今后我们应当更加关注设计的质量，而不仅仅是其实现的准确性。

### Using a Behavioral Theory of Program Comprehension in Software Engineering

Ruven E. Brooks · pp. 196–201 · [ACM DL](https://dl.acm.org/doi/10.5555/800099.803210)

> A theory is presented of how a programmer goes about understanding a program. The theory is based on a representation of knowledge about programs as a succession of knowledge domains which bridge between the problem domain and the executing program. A hypothesis and verify process is used by programmers to reconstruct these domains when they seek to understand a program.The theory is useful in several ways in software engineering: It makes accurate predictions about the effectiveness of documentation; it can be used to systematically evaluate and critique other claims about documentation, and it may even be a useful guideline to a programmer in actually constructing documentation.

**中文翻译**：本文提出了一种关于程序员如何理解程序的理论。该理论基于这样一种表示：关于程序的知识是由一系列知识域构成的，这些知识域在问题域与执行中的程序之间起桥梁作用。程序员在试图理解程序时，会运用一种假设—验证过程来重建这些知识域。该理论在软件工程中有多方面的用途：它能够对文档的有效性作出准确预测；可用于系统地评估和批判关于文档的其他论断；它甚至可能成为程序员实际编写文档时的有用指南。

## 1979 · ICSE 4 {#y1979}

### Software Engineering: As it is

Barry W. Boehm · pp. 11–21 · [ACM DL](https://dl.acm.org/citation.cfm?id=802916)

> This paper presents a view of software engineering as it is in 1979. It discusses current software engineering practice with respect to lessons learned in the past few years, and concludes that the lessons are currently not heeded roughly half of the time. The paper discusses some of the factors which may account for this lag, including rapid technological change, education shortfalls, technology transfer inhibitions, resistance to disciplined methods, inappropriate role models, and a restricted view of software engineering. The paper also updates a 1976 state of the art survey of software engineering technology, including such topics as requirements and specifications, design, programming, verification and validation, maintenance, software psychology, and software economics. It concludes that the field is making solid progress, but that it is growing more complex at a faster rate than we can put it in order.

**中文翻译**：本文提出了 1979 年时软件工程的现状视角。文章结合过去几年的经验教训，讨论了当前的软件工程实践，并得出结论：这些教训目前大约有一半时间未被重视。文中讨论了造成这种滞后的若干因素，包括技术的快速变化、教育的不足、技术转移的障碍、对有纪律方法的抵制、不恰当的角色典范，以及对软件工程的狭隘理解。本文还更新了 1976 年的软件工程技术现状综述，涵盖需求与规格说明、设计、编程、验证与确认、维护、软件心理学和软件经济学等主题。文章的结论是，该领域正在取得坚实进展，但其复杂性的增长速度快于我们将其理清头绪的速度。

## 1981 · ICSE 5 {#y1981}

### A Database Model for Effective Configuration Management in the Programming Environment

Karen E. Huff · pp. 54–62 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802516)

> The effective management of configurations by programmers requires automatic techniques which are operative in the program development environment. In this paper, an abstract model is developed to cover the significant aspects of a typical programming environment pertinent to configuration management, using a database to capture configuration knowledge. The two aspects of the model deal with configuration identification and configuration control. In considering configuration identification, it is shown that the tools in the programming environment determine which configuration items need to be identified and also determine what the interesting and useful relations are among those items. In considering configuration control, the notion of a workspace, consisting of certain modification rights and certain visibility into the database, is developed to prevent conflict and to promote cooperation among programmers. The entire model can be used to evaluate the effectiveness of configuration management within a particular programming environment or as the basis of a programming environment design.

**中文翻译**：程序员有效管理配置，需要在程序开发环境中运行的自动化技术。本文建立了一个抽象模型，涵盖与配置管理相关的典型程序设计环境的重要方面，并使用数据库来捕获配置知识。该模型的两个方面分别处理配置标识与配置控制。在考虑配置标识时，本文表明，程序设计环境中的工具决定了哪些配置项需要被标识，也决定了这些项之间哪些关系是有趣且有用的。在考虑配置控制时，本文提出了工作空间（workspace）的概念，它由一定的修改权限以及对数据库的一定可见性构成，用以防止冲突并促进程序员之间的合作。整个模型既可用于评估某一程序设计环境中配置管理的有效性，也可作为程序设计环境设计的基础。

### Evaluation of a Software Requirements Document by Analysis of Change Data

Victor R. Basili; David M. Weiss · pp. 314–324 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802544)

> We describe in this paper an effective data collection method for evaluating software development methodologies, from definition of the objectives of the data collection to analysis of the results. We show how the data analysis can answer questions with respect to how successfully the goals of the development methodology are met. The A-7 requirements document is used as an example. We provide the results of data analyses conducted partway through the A-7 flight software development cycle, and discuss the utility of information obtained by such partial analyses. Results from the study show that data collection is feasible and useful when performed as part of configuration control, that data distributions based on partial data provide useful feedback to the developers, and that the A-7 Requirements Document is easily maintained and changed.

**中文翻译**：本文描述了一种有效的数据收集方法，用于评估软件开发方法论，涵盖从确定数据收集目标到分析结果的全过程。我们说明了数据分析如何回答开发方法论的目标在多大程度上得以实现这一问题。文中以 A-7 需求文档为示例。我们提供了在 A-7 飞行软件开发周期中途进行的数据分析结果，并讨论了此类阶段性分析所获信息的效用。研究结果表明：当数据收集作为配置控制的一部分进行时，它是可行且有用的；基于部分数据的数据分布能够为开发人员提供有益反馈；并且 A-7 需求文档易于维护和修改。

### Executable Requirements for Embedded Systems

Pamela Zave; Raymond T. Yeh · pp. 295–304 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802542)

> An approach to requirements specification for embedded systems, based on constructing an executable model of the proposed system interacting with its environment, is proposed. The approach is explained, motivated, and related to data-oriented specification techniques. Portions of a specification language embodying it are introduced, and illustrated with an extended example in which the requirements for a process-control system are developed incrementally.

**中文翻译**：本文提出一种嵌入式系统的需求规格说明方法，其基础是构建一个可执行模型，该模型描述所提议系统与其环境的交互。文中解释并阐明了该方法的动机，并将其与面向数据的规格说明技术相联系。文中介绍了体现该方法的规格说明语言的部分内容，并通过一个扩展示例加以说明：在该示例中，一个过程控制系统的需求被逐步开发出来。

### The Effect of Modularization and Comments on Program Comprehension

Scott N. Woodfield; Hubert E. Dunsmore; Vincent Y. Shen · pp. 215–223 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802534)

> An experiment was conducted to investigate how different types of modularization and comments are related to programmers' ability to understand programs. Forty-eight experienced programmers were given eight different versions of the same program and asked to answer a twenty question quiz used to measure comprehension. These eight different versions were the result of the program being constructed with four types of modularization (monolithic, functional, super, and abstract data type), each with and without comments. Those subjects whose programs contained comments were able to answer more questions than those without comments. Also, those subjects who were given the abstract data type version of the program were able to do significantly better than those with any other type of modularization.

**中文翻译**：本实验考察了不同类型的模块化与注释同程序员理解程序的能力之间的关系。四十八名经验丰富的程序员拿到了同一程序的八个不同版本，并被要求回答一份用于测量理解能力的二十题测验。这八个版本是由四种模块化类型（单体式、功能式、超级式和抽象数据类型）构造而成的，每种类型分别带注释和不带注释。程序中含有注释的被试能够回答的问题多于没有注释的被试。此外，拿到抽象数据类型版本程序的被试，其表现显著优于拿到其他任何模块化类型版本的被试。

## 1982 · ICSE 6 {#y1982}

### An Editor for Documentation in pi-System to Support Software Development and Maintenance

Yukikazu Nakamoto; T. Iwamoto; M. Hori; Kenichi Hagihara; Nobuki Tokura · pp. 330–339 · [ACM DL](https://dl.acm.org/citation.cfm?id=807775)

> A lot of information necessary to maintain a software tends to be lost in conventional documentation. One of the leading causes is considered that the ideas of developers which maintainers will want to know later are not fixed in any documents while the ideas are fresh. To remove the cause, we propose a new description form, called a frame, and construct a system called π, to support a software through its lifetime. This system gathers all the information with the frames, stores it in a database and provides the various services with respect to programming and documentation. This paper describes the frames and a subsystem, called π-editor, which provides a user friendly interface to make it easy to gather essential information. By using frames, (1) the associated information around one programming concept can be gathered at one time and (2) lack of necessary information hardly arises. The editor has the distinguished features such as (1) a structure-oriented display editor, (2) facilities to display selective information, provide helpful user guides, and check input errors immediately.

**中文翻译**：许多维护软件所必需的信息在传统文档中往往会丢失。其主要原因之一被认为是：开发者的想法（维护人员日后希望了解的内容）在构思之初并未被固定在任何文档中。为消除这一原因，我们提出了一种称为“框架”（frame）的新型描述形式，并构建了一个名为 π 的系统，以支持软件的全生命周期。该系统借助框架收集全部信息，将其存入数据库，并提供与编程和文档编制相关的各类服务。本文介绍了框架以及一个子系统 π-editor，该子系统提供了用户友好的界面，便于收集关键信息。借助框架，(1) 围绕某一编程概念的相关信息可以一次性集中收集；(2) 必要信息缺失的情况很少出现。该编辑器具有以下突出特点：(1) 结构导向的显示编辑器；(2) 能够选择性地显示信息、提供有用的用户指南，并即时检查输入错误的设施。

### An Examination of Evolution Dynamics

Michael J. Lawrence · pp. 188–196 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807761)

> Data on the history of seven systems was analysed to statistically test the 5 laws of software evolution proposed first by Belady and Lehman in 1976.While there was some evidence supporting laws 1 and 2, laws 3-5 were not supported by the data. In the light of the result a new discontinuous model of software evolution is proposed to replace the smoothly changing continuous model proposed by Lehman.

**中文翻译**：我们分析了七个系统的历史数据，以统计检验 Belady 和 Lehman 于 1976 年首次提出的软件演化五条定律。数据为第一条和第二条定律提供了一些支持，而第三至第五条定律未得到数据支持。基于这一结果，本文提出一种非连续的软件演化新模型，以取代 Lehman 提出的平滑连续变化模型。

### Configuration Control for Evolutional Software Products

Osamu Shigo; Yoshio Wada; Yuichi Terashima; Kanji Iwamoto; Takashi Nishimura · pp. 68–83 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807749)

> This paper describes the concept of and a system for configuration control for evolutional software products, in which a wide spectrum of varied software products are being continuously evolved, along with rapid advancements in hardware technologies. The system contains a database for dealing with the overall configuration structure, including hierarchical product structure with change status, master file directories, difficulty occurrences and user information. The data representing the configuration can be in more abstract or macroscopic level than the traditional software configuration control, since the configuration manager should control the overall outlines for all software products. The concept and system described in the paper have been used for intelligent terminal software product management in NEC's Data Terminals Division.

**中文翻译**：本文描述了一种针对演化型软件产品的配置控制概念及相应系统。在该类软件产品中，随着硬件技术的飞速进步，各种各样的软件产品不断被演化。该系统包含一个数据库，用于处理整体配置结构，包括带有变更状态的层次化产品结构、主文件目录、故障发生情况以及用户信息。由于配置管理者应当控制所有软件产品的总体轮廓，因此所表示的配置可以比传统软件配置控制更为抽象或宏观。本文所述的概念与系统已用于 NEC 数据终端部门的智能终端软件产品管理。

### DUAL: An Interactive Tool for Developing Documented Programs by Step-Wise Refinements

Luigi Petrone; Antonio Di Leva; Franco Sirovich · pp. 350–359 · [ACM DL](https://dl.acm.org/citation.cfm?id=807777)

> Programs are integrated hierarchical structures of formal texts - instructions - and informal texts - documentation. Only if there is a mechanical connection between program design and program development there can be higher chances that the program documentation, originated at design time, will not, sooner or later, become obsolete with respect to the current state of the system. DUAL is an interactive, incremental, intelligent editor of program and documentation texts to be used for software implementations whose anticipated life cycle is significantly long to deserve much attention. The screen interface plays a unique role in DUAL since it allows a visitor ( designer or maintenance engineer) “to replay” as many times as desired the evolution of the system from design to implementation. The access to the hierarchically organized Design Information is made easy and natural by the DUAL video oriented user interface.

**中文翻译**：程序是由形式化文本（指令）与非形式化文本（文档）构成的分层集成结构。只有当程序设计与程序开发之间存在机械化的联系时，在设计阶段产生的程序文档才更有可能不会随着系统现状的演变而迟早过时。DUAL 是一个交互式、增量式、智能化的程序与文档文本编辑器，适用于生命周期预期相当长、因而值得投入大量关注的软件实现。屏幕界面在 DUAL 中发挥着独特作用：它允许访问者（设计人员或维护工程师）任意多次地“回放”系统从设计到实现的演变过程。借助 DUAL 的视频导向用户界面，对按层次组织的设计信息的访问变得简便而自然。

### Design, Implementation, and Evaluation of a Revision Control System

Walter F. Tichy · pp. 58–67 · [ACM DL](https://dl.acm.org/citation.cfm?id=807748)

> The Revision Control System (RCS) is a software tool that helps in managing multiple revisions of text. RCS automates the storing, retrieval, logging, identification, and merging of revisions, and provides access control. It is useful for text that is revised frequently, for example programs and documentation. This paper presents the design and implementation of RCS. Both design and implementation are evaluated by contrasting RCS with SCCS, a similar system. SCCS is implemented with forward, merged deltas, while RCS uses reverse, separate deltas. (Deltas are the differences between successive revisions.) It is shown that the latter technique improves run-time efficiency, while requiring almost no extra space.

**中文翻译**：修订控制系统（RCS）是一种帮助管理文本多个修订版本的软件工具。RCS 自动完成修订的存储、检索、记录、标识和合并，并提供访问控制。它适用于频繁修订的文本，例如程序和文档。本文介绍了 RCS 的设计与实现。通过将 RCS 与类似系统 SCCS 进行对比，对其设计和实现进行了评估。SCCS 采用前向合并增量（forward, merged deltas）实现，而 RCS 采用反向、独立增量（reverse, separate deltas）实现。（增量即相继修订版本之间的差异。）结果表明，后一种技术提高了运行时效率，同时几乎不需要额外的空间。

### MAP: A Tool for Understanding Software

Sally Warren · pp. 28–39 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807745)

> Maintenance of software is a major problem that the data processing industry faces today. This paper describes MAP, a tool, that addresses the problems of software maintenance by helping programmers to understand their programs.

**中文翻译**：软件维护是当今数据处理行业面临的一个主要问题。本文介绍了一个名为 MAP 的工具，它通过帮助程序员理解自己的程序来应对软件维护问题。

### The Dimensions of Healthy Maintenance

Robert S. Arnold; Donald A. Parker · pp. 10–27 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807744)

> What characterizes “healthy” or “satisfactory” software maintenance? How can we know it when we see it? This paper gives initial answers to these questions. We first argue the need for objectively measurable maintenance performance criteria in judging the “adequacy” of maintenance and present a set of criteria for judging maintenance performance in a particular software environment. We then subject the criteria to a practical test by applying them in this environment. We show how applying the criteria enables an informed overall maintenance performance appraisal, locates general maintenance problems, stimulates suggestions for improving maintenance on individual projects, allows these projects' maintenance to be compared and the projects ordered for improvement, and assesses the potential effectiveness of the suggestions in new project maintenance. We also sketch how criteria application can be generalized to software development monitoring and design methodology evaluation.

**中文翻译**：什么样的软件维护才是“健康”或“令人满意”的？我们如何在看到它时识别出来？本文对这些问题给出了初步回答。我们首先论证了需要客观可测的维护绩效标准，以判断维护是否“充分”；随后提出了一套在特定软件环境中判断维护绩效的标准。接着，我们在该环境中对这些标准进行了实际检验。我们表明，应用这些标准能够实现有依据的整体维护绩效评估，定位普遍性的维护问题，激发针对个别项目维护改进的建议，使各项目的维护可以相互比较并据此排定改进顺序，并评估这些建议在新项目维护中可能的有效性。我们还勾勒了如何将标准的应用推广到软件开发监控和设计方法评估之中。

## 1984 · ICSE 7 {#y1984}

### Fifteen Years of Psychology in Software Engineering: Individual Differences and Cognitive Science

Bill Curtis · pp. 97–107 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801956)

> Since the 1950's, psychologists have studied the behavioral aspects of software engineering. However, the results of their research have never been organized into a subfield of either software engineering or psychology. This failure results from the difficulty of integrating theory and data from the mixture of paradigms borrowed from psychology. This paper will review some of the psychological research on software engineering performed since the Garmisch Conference in 1968. This review will be organized under two of the psychological paradigms used in exploring programming problems: individual differences and cognitive science. The major theoretical and practical contributions of each area to the theory and practice of software engineering will be discussed. The review will end with a call for more research guided by the paradigm of cognitive science, since such results are the easiest to integrate with new developments in artificial intelligence and computer science theory.

**中文翻译**：自 1950 年代以来，心理学家就一直在研究软件工程中的行为层面。然而，他们的研究成果从未被组织成软件工程或心理学的一个子领域。造成这一失败的原因在于，要整合那些从心理学借来的、范式各异的理论与数据十分困难。本文将回顾自 1968 年加尔米施会议（Garmisch Conference）以来，在软件工程方面所开展的部分心理学研究。该综述将依据心理学在探索编程问题时所采用的两种范式进行组织：个体差异与认知科学。文中将讨论每个领域对软件工程理论与实践的主要理论和实践贡献。综述结尾呼吁开展更多以认知科学范式为指导的研究，因为此类成果最易于与人工智能和计算机科学理论的新进展相整合。

### Knowledge-Based Communication Processes in Software Engineering

Gerhard Fischer; Matthias Schneider · pp. 358–368 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801993)

> A large number of problems to be solved with the help of computer systems are ill-structured. Their solution requires incremental design processes, because complete and stable specifications are net available.For tasks of this sort, life cycle models are inadequate. Our design methodology is based on a rapid prototyping approach which supports the coevolution of specification and implementation. Communication between customers, designers and implementors and communication between the humans and the knowledge base in which the emerging product is embedded are of crucial importance. Our work is centered around knowledge-based systems which enhance and support the communication needs in connection with software systems.Program documentation systems are used as an example to illustrate the relevance of knowledge-based human-computer communication in software engineering.

**中文翻译**：大量需要借助计算机系统解决的问题都是结构不良（ill-structured）的。由于完整且稳定的规格说明尚不可得，解决这类问题需要增量式设计过程。对于此类任务，生命周期模型是不充分的。我们的设计方法基于快速原型方法，该方法支持规格说明与实现的协同演化。客户、设计人员和实现人员之间的沟通，以及人与知识库之间的沟通（新生成的产品即嵌入其中）至关重要。我们的工作以基于知识的系统为中心，这类系统增强并支持软件系统相关的沟通需求。程序文档编制系统被用作示例，以说明基于知识的人机沟通在软件工程中的相关性。

### PROUST: Knowledge-Based Program Understanding

W. Lewis Johnson; Elliot Soloway · pp. 369–380 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801994)

> This paper1 describes a program called PROUST which does on- line analysis and understanding of Pascal programs written by novice programmers. PROUST takes as input a program and a non-algorithmic description of the program requirements, and finds the most likely mapping-between the requirements and the code. This mapping is in essence a reconstruction of the design and implementation steps that the programmer went through in writing the program. A knowledge base of programming plans and strategies, together with common bugs associated with them, is used in constructing this mapping. Bugs are discovered in the process of relating plans to the code; PROUST can therefore give deep explanations of program bugs by relating the buggy code to its underlying intentions.

**中文翻译**：本文介绍了一个名为 PROUST 的程序，它能够对新手程序员编写的 Pascal 程序进行在线分析与理解。PROUST 以一个程序及其非算法式的程序需求描述作为输入，并找出需求与代码之间最可能的映射。该映射本质上是对程序员编写程序时所经历的设计与实现步骤的重构。程序设计计划与策略的知识库，连同与之相关的常见错误，被用于构建该映射。在将计划与代码相关联的过程中会发现错误；因此，PROUST 能够通过将错误代码与其底层意图相关联，对程序错误给出深入的解释。

### The Modular Structure of Complex Systems

David Lorge Parnas; Paul C. Clements; David M. Weiss · pp. 408–419 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801999)

> This paper discusses the organization of software that is inherently complex because there are very many arbitrary details that must be precisely right for the software to be correct. We show how the software design technique known as information hiding or abstraction can be supplemented by a hierarchically-structured document, which we call a module guide. The guide is intended to allow both designers and maintainers to identify easily the parts of the software that they must understand without reading irrelevant details about other parts of the software. The paper includes an extract from a software module guide to illustrate our proposals.

**中文翻译**：本文讨论了这样一类软件的组织问题：这类软件本身十分复杂，因为存在大量任意细节，每一项都必须精确无误，软件才能正确。我们说明了如何用一种层次化结构的文档（我们称之为“模块指南”，module guide）来补充信息隐藏（information hiding）或抽象这一软件设计技术。该指南旨在使设计人员和维护人员能够轻松识别他们必须理解的软件部分，而无需阅读软件其他部分的无关细节。本文附有一份软件模块指南的摘录，以说明我们的建议。

## 1985 · ICSE 8 {#y1985}

### Active Design Reviews: Principles and Practices

David Lorge Parnas; David M. Weiss · pp. 132–136 · [ACM DL](https://dl.acm.org/citation.cfm?id=319599)

> Although many new software design techniques have emerged in the past 15 years, there have been few changes to the procedures for reviewing the designs produced using these techniques. This paper describes an improved technique, based on the following ideas, for reviewing designs. The efforts of each reviewer should be focussed on those aspects of the design that suit his experience and expertise. The characteristics of the reviewers needed should be explicitly specified before reviewers are selected. Reviewers should be asked to make positive assertions about the design rather than simply allowed to point out defects. The designers pose questions to the reviewers, rather than vice versa. These questions are posed on a set of questionnaires that requires careful study of some aspect of the design. Interaction between designers and reviewers occurs in small meetings involving 2 - 4 people rather than meetings of large groups. Illustrations of these ideas drawn from the application of active design reviews to the Naval Research Laboratory's Software Cost Reduction Project are included.

**中文翻译**：尽管过去 15 年间涌现了许多新的软件设计技术，但设计评审的程序却很少改变。本文提出了一种改进的设计评审技术，其基于以下思想：每位评审人员的精力应集中于设计中与其经验和专长相适应的方面；在选定评审人员之前，应明确规定所需评审人员的特征；应要求评审人员对设计作出肯定性断言，而不仅仅是指出缺陷；由设计人员向评审人员提问，而非相反；这些问题以问卷的形式提出，要求评审人员仔细研究设计的某一方面；设计人员与评审人员之间的交流在 2 至 4 人的小型会议中进行，而非大型小组会议。文中包含了将这些思想应用于美国海军研究实验室软件成本削减项目（Software Cost Reduction Project）的示例。

### SODOS - A Software Documentation Support Environment: Its Use

Ellis Horowitz; Ronald Williamson · pp. 8–14 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319571)

> This paper describes a computerized environment, SODOS (Software Documentation Support), which supports the definition and manipulation of documents used in developing software. An object oriented environment is used as a basis for the SODOS interface. SODOS is built around a Software Life Cycle (SLC) Model that structures all access to the documents stored in the environment. One advantage of this model is that it supports software documentation independent of any fixed methodology that the developers may be using. The main advantage of the system is that it permits traceability through each phase of the Life Cycle, thus facilitating the testing and maintenance phases. Finally the effort involved in learning and using SODOS is simplified due to a sophisticated "user-friendly" interface.

**中文翻译**：本文介绍了一个计算机化环境 SODOS（Software Documentation Support，软件文档支持），用于支持软件开发过程中所用文档的定义与操作。SODOS 接口以面向对象环境为基础。SODOS 围绕软件生命周期（SLC）模型构建，该模型统一约束对环境中所存文档的全部访问。该模型的一个优点是，它能够独立于开发者可能采用的任何固定方法论来支持软件文档编制。该系统的主要优点在于，它允许在生命周期的每个阶段进行可追溯性管理，从而便于测试和维护阶段的工作。最后，由于采用了“用户友好”的界面，学习和使用 SODOS 所需的工作量得以简化。

### Software Technology Maturation

Samuel T. Redwine Jr.; William E. Riddle · pp. 189–200 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319624)

> We have reviewed the growth and propagation of a variety of software technologies in an attempt to discover natural characteristics of the process as well as principles and techniques useful in transitioning modern software technology into widespread use. What we have looked at is the technology maturation process, the process by which a piece of technology is first conceived, then shaped into something usable, and finally "marketed" to the point that it is found in the repertoire of a majority of professionals. A major interest is the time required for technology maturation — and our conclusion is that technology maturation generally takes much longer than popularly thought, especially for major technology areas. But our prime interest is in determining what actions, if any, can accelerate the maturation of technology, in particular that part of maturation that has to do with transitioning the technology into widespread use. Our observations concerning maturation facilitators and inhibitors are the major subject of this paper.

**中文翻译**：我们回顾了多种软件技术的成长与传播情况，试图发现该过程的自然特征，以及有助于将现代软件技术转化为广泛应用的原则和技术。我们考察的是技术成熟化过程（technology maturation process），即一项技术先被构思，再被塑造成可用之物，最后被“推向市场”，直至成为大多数专业人员工具箱中的一部分。我们特别关注技术成熟所需的时间，结论是技术成熟通常比人们普遍认为的要花费更长的时间，对于重大技术领域尤其如此。但我们的首要兴趣在于确定哪些行动（如果有的话）能够加速技术的成熟，尤其是成熟过程中与将技术转化为广泛应用相关的那部分。本文的主要内容即是我们关于成熟促进因素与抑制因素的观察。

### The Software Knowledge Base

Bertrand Meyer · pp. 158–165 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319611)

> We describe a system for maintaining useful information about a software project. The “software knowledge base” keeps track of software components and their properties; these properties are described through binary relations and the constraints that these relations must satisfy. The relations and constraints are entirely user-definable, although a set of predefined libraries of relations with associated constraints is provided for some of the most important aspects of software development (specification, design, implementation, testing, project management).The use of the binary relational model for describing the properties of software is backed by a theoretical study of the relations and constraints which play an important role in software development.

**中文翻译**：我们描述了一个用于维护软件项目有用信息的系统。“软件知识库”记录软件组件及其属性；这些属性通过二元关系以及这些关系必须满足的约束来描述。关系与约束完全可由用户定义，同时系统为软件开发中一些最重要的方面（规格说明、设计、实现、测试、项目管理）提供了一组预定义的关系库及相应约束。使用二元关系模型来描述软件属性，有一项关于在软件开发中起重要作用的关系与约束的理论研究作为支撑。

## 1987 · ICSE 9 {#y1987}

### An Architecture for Intelligent Assistance in Software Development

Gail E. Kaiser; Peter H. Feiler · pp. 180–188 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41783)

> We define an architecture for a software engineering environment that behaves as an intelligent assistant. Our architecture consists of three key aspects: an objectbase, a model of the software development activities, and controlled automation. Our objectbase is adapted from other research, but our model is unique in that is consists primarily of rules that define the preconditions and multiple postconditions of software development activities. Our most significant contribution is opportunistic processing, whereby the environment performs software development activities through controlled automation. This is accomplished by a forward and backward chaining interpretation of the rule set. Activities are automatically carried out at some time between when their preconditions are satisfied and when their postconditions are required. Automation is controlled through strategies that guide the assistant in choosing an appropriate point for carrying out each activity.

**中文翻译**：我们定义了一种软件工程环境的体系结构，使其表现为一个智能助手。该体系结构包含三个关键方面：对象库（objectbase）、软件开发活动模型以及受控自动化。我们的对象库借鉴了其他研究的成果，但我们的模型是独特的，因为它主要由定义软件开发活动前置条件与多重后置条件的规则构成。我们最重要的贡献是机会式处理（opportunistic processing），即环境通过受控自动化来执行软件开发活动。这是通过对规则集进行前向与后向链式解释来实现的。活动会在其前置条件得到满足之后、其后置条件被需要之前的某个时刻被自动执行。自动化通过策略加以控制，这些策略指导助手为每项活动选择合适的执行时机。

### From Design to Redesign

Gerhard Fischer; Andreas C. Lemke; Christian Rathke · pp. 369–376 · [ACM DL](https://dl.acm.org/citation.cfm?id=41806)

*无摘要。*

### Knowledge-Based Software Design Using Design Schemas

Mitchell D. Lubars; Mehdi T. Harandi · pp. 253–262 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41790)

> Design schemas provide a means for abstracting software designs into broadly reusable components that can be assembled and refined into new software designs. This paper describes a knowledge-based software development paradigm that is based on the design schema representation. It combines design schemas, domain knowledge, and various types of rules to assist in the quick generation of software designs from user specifications. A prototypical environment, IDeA (Intelligent Design Aid), is described that supports the knowledge-based paradigm. The schema-based techniques used in IDeA are presented along with some examples of their use.

**中文翻译**：设计图式（design schema）为将软件设计抽象为广泛可复用的组件提供了手段，这些组件可以被组装和精化为新的软件设计。本文描述了一种基于设计图式表示的知识型软件开发范式。它结合了设计图式、领域知识以及各类规则，以协助从用户规格说明快速生成软件设计。文中描述了支持该知识型范式的原型环境 IDeA（Intelligent Design Aid，智能设计辅助），并介绍了 IDeA 所采用的基于图式的技术及其应用示例。

### On Building Software Process Models Under the Lamppost

Bill Curtis; Herb Krasner; Vincent Y. Shen; Neil Iscoe · pp. 96–105 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41776)

> Most software process models are based on the management tracking and control of a project. The popular alternatives to these models such as rapid prototyping and program transformation are built around specific technologies, many of which are still in their adolescence. Neither of these approaches describe the actual processes that occur during the development of a software system. That is, these models focus on the series of artifacts that exist at the end of phases of the process, rather than on the actual processes that are conducted to create the artifacts. We conducted a field study of large system development projects to gather empirical information about the communication and technical decision-making processes that underlie the design of such systems. The findings of this study are reviewed for their implications on modeling the process of designing large software systems. The thesis of the paper is that while there are many foci for process models, the most valuable are those which capture the processes that control the most variance in software productivity and quality.

**中文翻译**：大多数软件过程模型都以项目的管理跟踪与控制为基础。与之相对的流行替代方案，如快速原型法和程序变换，则围绕特定技术构建，而其中许多技术仍处于早期阶段。这两类方法都没有描述软件系统开发过程中实际发生的过程。也就是说，这些模型关注的是各阶段结束时存在的一系列制品，而不是为创造这些制品而实际开展的过程。我们对大型系统开发项目进行了一项实地研究，以收集有关支撑此类系统设计的沟通与技术决策过程的经验信息。文中回顾了该研究的结果，并探讨了其对大型软件系统设计过程建模的启示。本文的论点是：过程模型的关注焦点有很多，但最有价值的，是那些能够捕捉对软件生产率与质量方差影响最大之控制过程的模型。

### Process Models, Process Programs, Programming Support

Meir M. Lehman · pp. 14–16 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41767)

*无摘要。*

### Software Processes Are Software Too

Leon J. Osterweil · pp. 2–13 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41766)

*无单独摘要，以下为正文首段。*

> The major theme of this meeting is the exploration of the importance of.ul process as a vehicle for improving both the quality of software products and the the way in which we develop and evolve them. In beginning this exploration it seems important to spend at least a short time examining the nature of process and convincing ourselves that this is indeed a promising vehicle. We shall take as our elementary notion of a process that it is a systematic approach to the creation of a product or the accomplishment of some task. We observe that this characterization describes the notion of process commonly used in operating systems-- namely that a process is a computational task executing on a single computing device. Our characterization is much broader, however, describing any mechanism used to carry out work or achieve a goal in an orderly way.

**中文翻译**：本次会议的主要主题是探讨过程（process）作为一种手段的重要性，它既可用于提升软件产品的质量，也可用于改进我们开发和演化软件的方式。在开始这一探讨时，有必要花至少一小段时间考察过程的本质，并使我们自己确信它确实是一种有前景的手段。我们将过程的基本概念定义为：为创造某种产品或完成某项任务而采取的系统性方法。我们注意到，这一刻画描述的是操作系统中通常使用的过程概念，即在单一计算设备上执行的计算任务。然而，我们的刻画要宽泛得多，它描述的是任何以有序方式用于开展工作或实现目标的机制。

### Tailoring the Software Process to Project Goals and Environments

Victor R. Basili; Hans Dieter Rombach · pp. 345–359 · [ACM DL](https://dl.acm.org/citation.cfm?id=41804)

> This paper presents a methodology for improving the software process by tailoring it to the specific project goals and environment. This improvement process is aimed at the global software process model as well as methods and tools supporting that model. The basic idea is to use defect profiles to help characterize the environment and evaluate the project goals and the effectiveness of methods and tools in a quantitative way. The improvement process is implemented iteratively by setting project improvement goals, characterizing those goals and the environment, in part, via defect profiles in a quantitative way, choosing methods and tools fitting those characteristics, evaluating the actual behavior of the chosen set of methods and tools, and refining the project goals based on the evaluation results. All these activities require analysis of large amounts of data and, therefore, support by an automated tool. Such a tool — TAME (Tailoring A Measurement Environment) — is currently being developed.

**中文翻译**：本文提出了一种通过使软件过程适应具体项目目标与环境来改进软件过程的方法论。该改进过程既针对全局软件过程模型，也针对支持该模型的方法与工具。其基本思想是利用缺陷剖面（defect profiles）来刻画环境，并以定量方式评估项目目标以及方法与工具的有效性。改进过程以迭代方式实施：设定项目改进目标；部分地通过定量的缺陷剖面来刻画这些目标与环境；选择与这些特征相契合的方法与工具；评估所选方法与工具集的实际表现；并根据评估结果精化项目目标。所有这些活动都需要分析大量数据，因此需要自动化工具的支持。这一工具——TAME（Tailoring A Measurement Environment，裁剪度量环境）——目前正在开发之中。

### Version Control in the Inscape Environment

Dewayne E. Perry · pp. 142–149 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41780)

> We present the important issues to be considered in version control mechanisms and characterize and compare the kinds of version control systems extant in current programming environments. We then characterize Inscape's version control mechanism. Invariant, and show that it makes several significant advances in the state of the art. Using Instress (Inscape's module interface specification language) specifications, Invariant provides a better understanding of the notion of parallel versions, a more comprehensive notion of version consistency, and a more flexible method of system composition than current mechanisms. In particular, Invariant provides a formalization of the notions of version equivalence and compatibility that correspond closely with our intuitive (and practical) notions of version equivalence and compatibility. These various forms of version compatibility provide the system builder with the concept of plug-compatibility — an extremely useful facility in composing systems from component parts.

**中文翻译**：我们提出了版本控制机制中需要考虑的重要问题，并对当前程序设计环境中存在的各类版本控制系统进行了刻画与比较。随后，我们刻画了 Inscape 的版本控制机制 Invariant，并表明它在技术水平上取得了若干重要进展。Invariant 使用 Instress（Inscape 的模块接口规格说明语言）规格说明，相比当前机制，能够更好地理解并行版本的概念，获得更全面的版本一致性概念，并提供更灵活的系统组合方法。特别地，Invariant 对版本等价性与兼容性的概念进行了形式化，使之与我们直观的（同时也是实践中的）版本等价性与兼容性概念密切对应。这些不同形式的版本兼容性为系统构建者提供了即插即用兼容性（plug-compatibility）的概念，这是由组件部件组合系统时极为有用的一项功能。

## 1988 · ICSE 10 {#y1988}

### Enhancing Program Readability and Comprehensibility with Tools for Program Visualization

Ronald Baecker · pp. 356–366 · [ACM DL](https://dl.acm.org/citation.cfm?id=55858)

> In order to make computer programs more comprehensible, the presentation of program source text, program documentation, and program execution needs to be enhanced over its conventional treatment. The paper describes a number of new techniques and tools developed to achieve these ends. One of these is a novel design for the effective presentation of source text in the C programming language using high quality digital typography, and a processor which implements the design. Some experimental evidence is summarized to demonstrate that the resulting source text presentation is significantly more readable and comprehensible than the presentation conventionally used today. Brief descriptions are also given of two other techniques, the development of a novel system of structured program documentation incorporating both text and graphics, and the portrayal of program execution with coloured computer animation.

**中文翻译**：为使计算机程序更易于理解，有必要在传统处理方式的基础上，改进程序源文本、程序文档以及程序执行的呈现方式。本文描述了为实现这些目标而开发的若干新技术与工具。其中之一是一种新颖的设计方案，即利用高质量的数字排版来有效呈现 C 语言程序源文本，并附带实现该设计的处理器。部分实验证据表明，由此得到的源文本呈现方式，比当今常规使用的呈现方式显著更易阅读、更易理解。文中还简要介绍了另外两种技术：一种是融合文本与图形的结构化程序文档新系统，另一种是利用彩色计算机动画展现程序执行过程。

### Evolution of Tools (Abstract)

Kishida · p. 2 · 无在线链接

*无摘要。*

### Models of Software Development Environments

Dewayne E. Perry; Gail E. Kaiser · pp. 60–68 · [ACM DL](https://dl.acm.org/doi/10.5555/55823.55830)

> We present a general model of software development environments that consists of three components: structures, mechanisms and policies. The advantage of this model is that it distinguishes intuitively those aspects of an environment that are useful in comparing and contrasting software development environments. Our initial application of the model is to characterize four classes of environments by means of a sociological metaphor based on scale: the individual, the family, the city and the state models. The utility of the IFCS taxonomy is that it delineates the important classes of interactions among software developers and exposes the ways in which current software development environments inadequately support the development of large systems. We demonstrate the generality of our model by also applying it to a previously published taxonomy that categorizes environments according to how they relate to four historical trends: language-centered, structure-oriented, toolkit and method-based environments.

**中文翻译**：我们提出了一个软件开发环境的通用模型，该模型由三个组成部分构成：结构（structures）、机制（mechanisms）和策略（policies）。该模型的优点在于，它能够直观地区分环境中那些有助于比较和对照不同软件开发环境的方面。我们对该模型的初步应用，是借助一种基于规模的社会学隐喻来刻画四类环境：个体模型、家庭模型、城市模型和国家模型。IFCS 分类法的效用在于，它界定了软件开发者之间互动的重要类别，并揭示了当前软件开发环境在支持大型系统开发方面存在的不足之处。我们还将该模型应用于一种已发表的分类法，该分类法依据环境与四种历史趋势的关系对环境进行分类：以语言为中心、结构导向、工具包以及基于方法的环境，从而展示了该模型的通用性。

### Recording the Reasons for Design Decisions

Colin Potts; Glenn Bruns · pp. 418–427 · [ACM DL](https://dl.acm.org/citation.cfm?id=55863)

> The authors outline a generic model for representing design deliberation and the relation between deliberation and the generation of method-specific artifacts. A design history is regarded as a network consisting of artifacts and deliberation nodes. Artifacts represent specifications or design documents. Deliberation nodes represent issues, alternatives or justifications. Existing artifacts give rise to issue about the evolving design, an alternative is one of several positions that respond to the issue (perhaps calling for the creation or modification of an artifact), and a justification is a statement giving the reasons for and against the related alternative. The model is applied to the development of a text formatter. The example development is represented in hypertext and as a Prolog database, the two representations being shown to complement each other. The authors conclude with a discussion of the relation between this model and other work and of the implications for tool support and methods.

**中文翻译**：作者概述了一个通用模型，用于表示设计审议（design deliberation），以及审议与特定方法所产生的制品（artifact）之间的关系。设计历史被视为由制品节点和审议节点构成的网络。制品代表规格说明或设计文档；审议节点代表问题（issue）、备选方案（alternative）或论证（justification）。既有制品会引发关于演化中设计的问题；备选方案是回应某一问题的若干立场之一（可能要求创建或修改某个制品）；论证则是陈述支持或反对相关备选方案之理由的声明。该模型被应用于一个文本格式化程序的开发。该开发示例同时以超文本和 Prolog 数据库两种形式表示，二者被证明可以互为补充。作者最后讨论了该模型与其他工作之间的关系，以及其对工具支持和方法的启示。

### Theory-W Software Project Management: A Case Study

Barry W. Boehm; Rony Ross · pp. 30–40 · [ACM DL](https://dl.acm.org/citation.cfm?id=55827)

> The search for a single unifying principle to guide software project management has been relatively unrewarding to date. Most candidate principles are either insufficiently general to apply in many situations, or so general that they provide no useful specific guidance. This paper presents a candidate unifying principle which appears to do somewhat better. Reflecting various alphabetical management theories (X, Y, Z), it is called the Theory W approach to software project management. Theory W: Make Everyone a Winner The paper explains the Theory W principle and its two subsidiary principles: Plan the flight and fly the plan; and, Identify and manage your risks. To test the practicability of Theory W, a case study is presented and analyzed: the attempt to introduce new information systems to a large industrial corporation in an emerging nation. The case may seem unique, yet it is typical. The analysis shows that Theory W and its subsidiary principles do an effective job both in explaining why the project encountered problems, and in prescribing ways in which the problems could have been avoided.

**中文翻译**：迄今为止，寻找一个统一原则来指导软件项目管理的努力收效甚微。大多数候选原则要么过于狭窄，难以适用于许多情形，要么过于宽泛，以至于无法提供有用的具体指导。本文提出了一个似乎比这些原则做得稍好的候选统一原则。它借鉴了各种以字母命名的管理理论（X、Y、Z），被称为软件项目管理的 Theory W 方法。Theory W：让每个人都成为赢家。本文阐述了 Theory W 原则及其两条从属原则：规划飞行并按计划飞行；识别并管理你的风险。为检验 Theory W 的可行性，文中提出并分析了一个案例研究：在一个新兴国家的大型工业企业引入新信息系统的尝试。这一案例可能看似独特，但实际上是典型的。分析表明，Theory W 及其从属原则既能有效地解释项目为何遇到问题，也能有效地规定问题本可以如何避免。

## 1989 · ICSE 11 {#y1989}

### A Model for the Reuse of Software Design Information

Kevin W. Jameson · pp. 205–216 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74615)

> This paper presents a general model for the representation and manipulation of module level software design information, leading to the effective reuse of software design information across different programming languages.Language independent design documents are represented as ASCII files containing tagged design information sufficient for the construction of a compilable program architecture.The resulting architecture is composed of documented module stubs which describe calling relationships, parameters, functional descriptions, and algorithms characteristic of the architecture.No executable code is included in the compilable modules.Frameworks of tagged locations in Zanguage dependent standard module templates are matched against corresponding tags in the ASCII design files, effectively blending language dependent and independent information into a compilable stub architecture.The process is reversible in that a language independent design file can be generated from an architecture in the standard tagged format, thus supporting the movement of design information across different programming languages.

**中文翻译**：本文提出了一个用于表示和操作模块级软件设计信息的通用模型，从而使软件设计信息能够在不同编程语言之间得到有效复用。与语言无关的设计文档以 ASCII 文件表示，其中包含带标记的设计信息，这些信息足以构造出可编译的程序体系结构。所得体系结构由带文档说明的模块桩（stub）组成，这些桩描述了调用关系、参数、功能说明及算法特征。这些可编译模块中不包含任何可执行代码。与语言相关的标准模块模板中带标记位置的框架，与 ASCII 设计文件中相应的标记相匹配，从而将语言相关与语言无关的信息融合为一个可编译的桩体系结构。该过程是可逆的：可以从标准标记格式的体系结构生成与语言无关的设计文件，从而支持设计信息在不同编程语言之间的迁移。

### Software Process Modeling: Principles of Entity Process Models

Watts S. Humphrey; Marc I. Kellner · pp. 331–342 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74631)

> A defined software process is needed to provide organizations with a consistent framework for performing their work and im- proving the way they do it. An overall framework for modeling simplifies the task of producing process models, permits them to be tailored to individual needs, and facilitates process evolution. This paper outlines the principles of entity process, models and suggests ways in which they can help to address some of the problems with more conventional approaches to modeling software processes.

**中文翻译**：组织需要明确定义的软件过程，以便为其工作开展及改进工作方式提供一致的框架。一个总体建模框架可以简化生成过程模型的任务，使模型能够根据个体需要进行裁剪，并促进过程的演化。本文概述了实体过程模型（entity process models）的原则，并提出了它们有助于解决传统软件过程建模方法中若干问题的途径。

## 1990 · ICSE 12 {#y1990}

### A Decision-Based Configuration Process Model

Thomas Rose; Matthias Jarke · pp. 316–325 · [ACM DL](https://dl.acm.org/citation.cfm?id=100341)

*无摘要。*

### LaSSIE: a Knowledge-based Software Information System

Premkumar T. Devanbu; Ronald J. Brachman; Peter G. Selfridge; Bruce W. Ballard · pp. 249–261 · [ACM DL](https://dl.acm.org/citation.cfm?id=100333)

> The authors discuss the important problem of invisibility that is inherent in the task of developing large software systems. It is pointed out that there are no direct solutions to this problem; however, there are several categories of systems-relational code analyzers, reuse librarians, and project management databases-that can be seen as addressing aspects of the invisibility problem. It is argued that these systems do not adequately deal with certain important aspects of the problem of invisibility-semantic proliferation, multiple views, and the need for intelligent indexing. A system called LaSSIE, which uses knowledge representation and reasoning technology to address each of these three issues directly and thereby help with the invisibility problem, has been built. The authors conclude with an evaluation of the system and a discussion of open problems and ongoing work.

**中文翻译**：作者讨论了开发大型软件系统这一任务中固有的重要问题——不可见性（invisibility）。文中指出，该问题并不存在直接的解决方案；然而，有若干类系统——关系式代码分析器、复用库管理工具以及项目管理数据库——可被视为在处理不可见性问题的某些方面。文中认为，这些系统并未充分处理该问题的某些重要方面，即语义膨胀（semantic proliferation）、多重视图以及对智能索引的需求。已经构建了一个名为 LaSSIE 的系统，它利用知识表示与推理技术直接处理这三个问题，从而有助于应对不可见性问题。作者最后对该系统进行了评估，并讨论了尚未解决的问题及正在进行的工作。

### Technology Transfer as Collaboration: The Receptor Group

Priscilla J. Fowler · pp. 332–333 · [ACM DL](https://dl.acm.org/citation.cfm?id=100345)

*无摘要。*

### The Evolution of Technology Transfer at MCC's Software Technology Program: From Didactic to Dialectic

James D. Babcock; Laszlo A. Belady; Nancy C. Gore · pp. 290–299 · [ACM DL](https://dl.acm.org/doi/10.5555/100296.100337)

> MCC's software technology program (STP) has a dual mission: to create tools and methodologies to assist development teams in the design of large, complex, distributed software systems, and to ensure the widespread diffusion of these technologies within STP shareholder organizations. STP has developed a comprehensive set of traditional technology transfer methods; although these methods make it possible to communicate research results successfully to shareholder receptors, they have spurred little actual use of released technology. STP has recently reevaluated its approach to technology transfer and discovered how it can be better accomplished-by fostering collaboration as its chief agent, rather than by depending on traditional transfer-and-feedback mechanisms. The authors describe the evolution of this new approach and present some of the results of collaborative experiences to date. It is found that collaborations revitalize research and that they empower STP's shareholders to affect the directions of that research. >

**中文翻译**：MCC 的软件技术计划（STP）肩负双重使命：一是创造工具和方法论，协助开发团队设计大型、复杂的分布式软件系统；二是确保这些技术在 STP 股东组织中得到广泛扩散。STP 已发展出一整套完备的传统技术转移方法；尽管这些方法能够成功地将研究成果传达给股东接收方，但它们几乎没有促成已发布技术的实际使用。STP 近来重新评估了其技术转移方法，并发现了更好实现这一目标的途径：以合作作为主要手段，而不是依赖传统的转移—反馈机制。作者描述了这一新方法的演变过程，并展示了迄今合作经验的部分结果。研究发现，合作能够重振研究，并使 STP 的股东能够影响研究的方向。

### Use of Video for Program Documentation (Experience Report)

Tom DeMarco; Curt Geertgens · pp. 126–128 · [ACM DL](https://dl.acm.org/citation.cfm?id=100314)

*无摘要。*

## 1991 · ICSE 13 {#y1991}

### Augmenting SADT to Develop Computer Support for Cooperative Work

Marca · pp. 94–103 · [ACM DL](https://dl.acm.org/citation.cfm?id=256693)

*无摘要。*

### Designing Software for Use by Humans, not Machines

Ruston, Muller, Cebulka · pp. 104–113 · [ACM DL](https://dl.acm.org/citation.cfm?id=256701)

> The authors describe an architecture that supports a more user-centered way to design software applications architectures, and by using a specific example, they also describe benefits gained by the software applications that result. The architecture aims to resolve some management and maintenance problems which have arisen in the telecommunications support systems network specifically, but which the authors also envision arising in any large-scale, multivendor, database environment. This examination includes consideration of technological advances in user-centered design, recent discoveries about the ability to separate processing functionalityfrom user interface functionality, and the rapidly expanding wealth of available user interface software tools.

**中文翻译**：作者描述了一种架构，它支持以用户为中心的方式来设计软件应用体系结构；通过一个具体示例，他们还描述了由此产生的软件应用所获得的益处。该架构旨在解决电信支持系统网络中出现的一些管理和维护问题，但作者也设想此类问题会出现在任何大规模、多供应商的数据库环境中。这一考察包括：用户中心设计的技术进展、关于将处理功能与用户界面功能相分离的能力的最新发现，以及迅速增多的可用用户界面软件工具。

### Extending the Potts and Bruns Model for Recording Design Rationale

Lee · pp. 114–125 · [ACM DL](https://dl.acm.org/citation.cfm?id=256705)

*无摘要。*

### Non-Technological Issues in Software Engineering

Kellner, Curtis, DeMarco, Kishida, Schlumberger, Tully · pp. 144–146 · [ACM DL](https://dl.acm.org/citation.cfm?id=256728)

*无摘要。*

### Software reuse: is it delivering?

Frakes, Biggerstaff, Prieto-Díaz, Matsumura, Schäfer · pp. 52–59 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256681)

> A panel discussion is presented to examine the evidence, pro and con, that software reuse is delivering. Verifiable and repeatable increases in software quality and productivity in field settings are used as criteria for the success of reuse. Reusability is defined as a technology that can be of significant value to software development and maintenance. A scale to evaluate whether reuse is delivering is outlined. The scale is ordinal, with five being the best possible rating. The three respondents, from Germany, Japan, and the US, discuss how reuse, as defined, is delivering in their parts of the world. >

**中文翻译**：本文呈现了一场小组讨论，旨在考察软件复用是否真正产生效益的正反两方面证据。以实际应用场景中可验证且可重复的软件质量与生产率提升，作为复用成功的标准。复用性被定义为一种能够为软件开发与维护带来重大价值的技术。文中概述了评估复用是否产生效益的一种量表。该量表为序数量表，五分为最佳评级。三位受访者分别来自德国、日本和美国，讨论了按照所定义的标准，复用在各自地区是如何产生效益的。

### Tolerating Inconsistency

Balzer · pp. 158–165 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256748)

*无单独摘要，以下为正文首段。*

> This is a short paper about a simple technique for making applications robust by marking data that violates specially identified invariants and using those marks as guards around code which is sensitive to that invariant.Such a capability is needed when dealing with the exceptions that arise in practical applications and distinguish them from idealized specifications. Previous techniques either required the removal of the constraint so that the exception would be allowed, or its modification to exclude the particular exception from the restriction.Our technique softens the entire constraint without introducing special cases, and is intended primarily for temporary exceptions. Rather than synchronizing all updates required by some constraint, it allows them instead to occur distributed in time in any arbitrary order. Thus, it is particularly useful in multiclient applications with shared responsibilities and authority, such as cooperative design (including software development).

**中文翻译**：这是一篇简短的论文，介绍一种简单技术：通过标记违反特定标识不变式（invariants）的数据，并以这些标记作为保护，围绕对该不变式敏感的代码，从而使应用程序更加健壮。在处理实际应用中出现的异常、并将其与理想化的规格说明区分开来时，需要这种能力。以往的技术要么要求去除约束以允许异常存在，要么要求修改约束以将该特定异常排除在限制之外。我们的技术则软化整个约束，而无需引入特殊情况，主要用于临时性异常。它不要求同步约束所要求的所有更新，而是允许这些更新以任意顺序、分布在不同时间发生。因此，该技术对于具有共享职责与权限的多客户端应用（如协作设计，包括软件开发）尤为有用。

## 1992 · ICSE 14 {#y1992}

### High-Pressure Steam Engines and Computer Software

Nancy G. Leveson · pp. 2–14 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143076)

*无摘要。*

### Process Programming by Hindsight

Pankaj K. Garg; Sanjay Bhansali · pp. 280–293 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143128)

> Process programming refers to the activity of algorithmicly describing models of programming activities (processes). A serious limitation of process programming has been that . it is often hard to describe a programming process a priori. In this paper we present an approach to process programming which addresses this limitation. Our approach is based on the premise that process programs are easier to describe in hindsight rather than by foresight, and hence can be synthe- sized by observing and analyzing a recorded process history. In this paper we describe an adaptation of the well-known explanation-based learning algorithm to synthesize a process fragment from a process history. We demonstrate the usefulness of the approach on a realistic example of coordinating file changes through a version control system.

**中文翻译**：过程编程（process programming）指以算法方式描述编程活动（过程）模型的活动。过程编程的一个严重局限在于，往往难以事先（a priori）描述编程过程。本文提出了一种解决这一局限的过程编程方法。我们的方法基于这样一个前提：过程程序事后描述比事先预见更容易，因此可以通过观察和分析记录下来的过程历史来综合得出。本文描述了对著名的基于解释的学习算法（explanation-based learning algorithm）的一种改编，用于从过程历史中综合出过程片段。我们通过一个现实示例展示了该方法的实用性，该示例涉及通过版本控制系统协调文件修改。

### The Software Engineering Laboratory: An Operational Software Experience Factory

Victor R. Basili; Gianluigi Caldiera; Frank E. McGarry; Rose Pajerski; Gerald T. Page; Sharon Waligora · pp. 370–381 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143154)

*无摘要。*

## 1993 · ICSE 15 {#y1993}

### A Process for Consolidating and Reusing Design Knowledge

Arango, Schoen, Pettengill · pp. 231–242 · [ACM DL](https://dl.acm.org/citation.cfm?id=257626)

*无摘要。*

### Documentation for Safety Critical Software

Courtois & Parnas · pp. 315–323 · [ACM DL](https://dl.acm.org/citation.cfm?id=257650)

> The authors review some of the fundamental difficulties presented by the design and the validation of software for safety critical applications. They suggest that software formal documentation techniques ameliorate the problems described. The principles behind a method of documenting both requirements and software design are presented. The methods have been used by the Atomic Energy Control Board of Canada in its safety assessment of the shutdown software of the Darlington generating station (D.L. Parnas et al., 1991). The method is illustrated by applying it to a small portion of the safety feature actuation system of a PWR nuclear reactor.

**中文翻译**：作者回顾了安全关键应用软件的设计与验证所面临的一些根本性困难，并提出软件形式化文档编制技术可以缓解上述问题。文中介绍了同时记录需求与软件设计的一种方法所依据的原则。该方法曾被加拿大原子能控制委员会用于其对达灵顿发电站停堆软件的安全评估（D.L. Parnas 等，1991）。文中将该方法应用于一座压水堆核反应堆安全特征驱动系统的一小部分，以说明其用法。

### Expressing the Relationships Between Multiple Views in Requirements Specification

Nuseibeh, Kramer, Finkelstein · pp. 187–196 · [ACM DL](https://dl.acm.org/citation.cfm?id=257610)

*无摘要。*

### The Concept Assignment Problem in Program Understanding

Biggerstaff, Mitbander, Webster · pp. 482–498 · [ACM DL](https://dl.acm.org/citation.cfm?id=257679)

*无摘要。*

## 1994 · ICSE 16 {#y1994}

### Comprehension processes during large scale maintenance

von Mayrhauser & Vans · pp. 39–48 · [ACM DL](https://dl.acm.org/doi/10.5555/257734.257741)

> We present results of observing professional maintenance engineers working with industrial code at actual maintenance tasks. Protocol analysis is used to explore how code understanding might differ for small versus large scale code. The experiment confirms that cognition processes work at all levels of abstraction simultaneously as programmers build a mental model of the code. Cognition processes emerged at three levels of aggregation representing lower and higher level strategies of understanding. They show differences in what triggers them and how they achieve their goals. Results are useful for defining core competencies which maintenance engineers need for their work and for documentation and development standards.

**中文翻译**：我们报告了对专业维护工程师在处理工业代码的实际维护任务时的观察结果。我们采用协议分析（protocol analysis）来探讨大规模代码与小规模代码的理解方式有何不同。实验证实，在程序员构建代码心理模型的过程中，认知过程会同时在各个抽象层次上发挥作用。认知过程在三个聚合层次上出现，分别代表理解的低层与高层策略。它们在触发因素以及实现目标的方式上存在差异。研究结果有助于界定维护工程师开展工作所需的核心能力，并可为文档编制与开发标准提供参考。

### Software Aging

Parnas · pp. 279–287 · [ACM DL](https://dl.acm.org/citation.cfm?id=257788)

> Programs, like people, get old. We can't prevent aging, but we can understand its causes, take steps to limits its effects, temporarily reverse some of the damage it has caused, and prepare for the day when the software is no longer viable. A sign that the software engineering profession has matured will be that we lose our preoccupation with the first release and focus on the long-term health of our products. Researchers and practitioners must change their perception of the problems of software development. Only then will software engineering deserve to be called "engineering".

**中文翻译**：程序和人一样会变老。我们无法阻止老化，但可以理解其成因，采取措施限制其影响，暂时逆转它已造成的部分损害，并为软件不再可用的那一天做好准备。软件工程专业走向成熟的一个标志，将是我们不再执着于第一版的发布，而转而关注产品的长期健康。研究人员和从业者必须改变他们对软件开发问题的认知。只有这样，软件工程才配得上“工程”之名。

### Understanding 'Why' in Software Process Modelling, Analysis, and Design

Yu & Mylopoulos · pp. 159–168 · [ACM DL](https://dl.acm.org/citation.cfm?id=257757)

*无摘要。*

### What Small Business and Small Organizations Say About the CMM: Experience Report

Brodman & Johnson · pp. 331–340 · [ACM DL](https://dl.acm.org/citation.cfm?id=257795)

*无摘要。*

## 1995 · ICSE 17 {#y1995}

### Architectural Mismatch or Why It's Hard to Build Systems Out Of Existing Parts

David Garlan; Robert Allen; John Ockerbloom · pp. 179–185 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225031)

> Many would argue that future breakthroughs in software productivity will depend on our ability to combine existing pieces of software to produce new applications.An important step towards this goal is the development of new techniques to detect and cope with mismatches in the assembled parts.Some problems of composition are due to low-level issues of interoperability, such as mismatches in programming languages or database schemas.However, in this paper we highlight a different, and in many ways more pervasive, class of problem: architectural mismatch.Specifically, we use our experience in building a family of software design environments from existing parts to illustrate a variety of types of mismatch that center around the assumptions a reusable part makes about the structure of the application in which is to appear.Based on this experience we show how an architectural view of the mismatch problem exposes some fundamental, thorny problems for software composition and suggests possible research avenues needed to solve them.

**中文翻译**：许多人认为，软件生产率未来的突破将取决于我们能否将现有软件片段组合起来，以产生新的应用。实现这一目标的一个重要步骤，是开发新技术来检测并应对组装部件中的失配（mismatch）。组合中的一些问题源于底层的互操作性问题，例如编程语言或数据库模式之间的失配。然而，本文强调的是另一类在许多方面更为普遍的问题：体系结构失配（architectural mismatch）。具体而言，我们基于由现有部件构建一系列软件设计环境的经验，说明了一系列围绕可复用部件所作假设的失配类型，这些假设涉及该部件将要出现于其中的应用的结构。基于这一经验，我们表明，从体系结构视角看待失配问题，能够揭示软件组合中一些根本性的、棘手的问题，并提出解决这些问题所需的可能研究方向。

### Automating Process Discovery Through Event-Data Analysis

Jonathan E. Cook; Alexander L. Wolf · pp. 73–82 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225021)

> Many software process methods and tools presuppose the existence of a formal model of a process.Unfortunately, developing a formal model for an on-going, complex process can be dificult, costly, and err-or prone.This presents a practical barrier to the adoption of process technologies.The barrier would be lowered by automatmg the creation of formal models.We are currently exploring techniques that can use basic event data captured from an on-going process to generate a formal model of process behavior.We term this kind of data analysis process discovery.Thts paper descr~bes and illustrates three methods with whzch we have been experimenting: algorithmic grammar inference, Markov models, and neural networks.

**中文翻译**：许多软件过程方法与工具都以存在某种过程的形式化模型为前提。遗憾的是，为一个持续进行的复杂过程开发形式化模型，可能既困难、代价高昂，又容易出错。这构成了过程技术被采用的实际障碍。若能将形式化模型的创建自动化，这一障碍便可降低。我们目前正在探索一些技术，能够利用从持续进行的过程中采集的基本事件数据，生成过程行为的形式化模型。我们将这类数据分析称为过程发现（process discovery）。本文描述并说明了我们一直在试验的三种方法：算法语法推断（algorithmic grammar inference）、马尔可夫模型（Markov models）和神经网络。

### How to Deal With Deviations During Process Model Enactment

Gianpaolo Cugola; Elisabetta Di Nitto; Carlo Ghezzi; M. Mantione · pp. 265–273 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225039)

> A fundamental problem in software processes is how the mintrinsic rigidity of a predejined (formal) model can be reconciled with the need for flexibility, change, and evolution.We therefore distinguish between software processes, as specified in a process description, and their actual performance by humans.Further, we claim that the two inevitably diverge, and thus it is necessary to provide means to reconcile them.We present a preliminary exploration into the problem.In particular, we illustrate how a temporal logic-based approach can be used to capture and tolerate some deviations from the process description during execution.We present a simple process language (LATIN), and its prototype environment (SENTINEL), in which these ideas are currently experimented.1

**中文翻译**：软件过程中的一个根本问题在于：预定义（形式化）模型固有的刚性，如何与对灵活性、变化和演化的需求相协调。因此，我们区分了两者：一方面是过程描述中所规定的软件过程，另一方面是人们对它的实际执行。我们进一步认为，二者不可避免地会产生偏离，因此有必要提供手段来调和两者。本文对这一问题进行了初步探索。具体而言，我们说明了如何运用基于时序逻辑的方法，在执行过程中捕捉并容忍对过程描述的某些偏离。我们提出了一种简单的过程语言 LATIN 及其原型环境 SENTINEL，目前正在该环境中对这些思想进行实验。

### The World and the Machine

Michael Jackson · pp. 283–292 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225041)

> As software developers we are engineers because we make useful machines.We are concerned both with the world, in which the machine serves a useful purpose, and with the machine itself.The competing demands and attractions of these two concerns must be appropriately balanced.Failure to balance them harms our work.Certainly it must take some of the blame for the gulf between researchers and practitioners in software development.To achieve proper balance we must sometimes fight against tendencies and inclinations that are deeply ingrained in our customary practices and attitudes in software development.In this paper some aspects of the relationship between the world and the machine are explored; some sources of distortion are identified; and some suggestions are put forward for maintaining a proper balance.

**中文翻译**：作为软件开发者，我们是工程师，因为我们制造有用的机器。我们既关注机器所服务的有用目的所在的世界，也关注机器本身。这两种关注之间相互竞争的需求与吸引力，必须得到适当平衡。未能保持平衡会损害我们的工作。它无疑应为软件开发中研究者与实践者之间的鸿沟承担部分责任。要实现适当的平衡，我们有时必须对抗那些深植于软件开发中既有惯例与态度的倾向和偏好。本文探讨了世界与机器之间关系的某些方面，识别了若干扭曲的来源，并提出了保持适当平衡的一些建议。

## 1996 · ICSE 18 {#y1996}

### A systematic survey of CMM experience and results

Herbsleb & Goldenson · pp. 323–330 · [ACM DL](https://dl.acm.org/doi/10.5555/227726.227791)

> The capability maturity model * (CMM) for sojlware has become very influential as a basis for software process improvement (SPI). Most of the evidence to date showing the results of these efforts has consisted of case studies. We present a systematic survey of organizations that have undertaken CMM-based SPI to get more representative results. Wefound evidence that process maturity is in fact associated with better organizational pe~ormance, and that software process appraisals are viewed, in retrospect, as extremely valuable and accurate guides for the improvement effort. The path was not always smooth, however, and e~orts generally took longer and cost more than expected. A number of factors that distinguished highly successful from unsuccessful efforts are identified. Most of these factors are under management control, suggesting that a number of specijic management decisions are likely to have a major impact on the success of the effort.

**中文翻译**：能力成熟度模型（CMM）作为软件过程改进（SPI）的基础，已产生了极大影响。迄今为止，显示这些努力成效的证据大多来自案例研究。我们对已开展基于 CMM 的 SPI 的组织进行了系统性调查，以获得更具代表性的结果。我们发现，过程成熟度确实与更好的组织绩效相关；回顾来看，软件过程评估被认为是改进工作极为宝贵且准确的指南。然而，这一道路并非总是平坦的，改进工作通常比预期耗时更长、花费更多。文中还指出了若干区分高度成功与不成功改进工作的因素。其中大多数因素处于管理层的控制之下，这表明一些具体的管理决策很可能对改进工作的成败产生重大影响。

### Prototypes as Assets, not Toys: Why and How to Extract Knowledge from Prototypes

Schneider · pp. 522–531 · [ACM DL](https://dl.acm.org/citation.cfm?id=227840)

*无摘要。*

### Supporting the Construction and Evolution of Component Repositories

Henninger · pp. 279–288 · [ACM DL](https://dl.acm.org/citation.cfm?id=227776)

> Repositories must be designed to meet the evolving and dynamic needs of software development organizations. Current software repository methods rely heavily on classification, which exacerbates acquisition and evolution problems by requiring costly classification and domain analysis efforts before a repository can be used effectively. This paper outlines an approach in which minimal initial structure is used to effectively find relevant software components while methods are employed to incrementally improve repository structures. The approach is demonstrated through PEEL, a tool to semi-automatically identify reusable components, and CodeFinder, a retrieval system that compensates for the lack of explicit knowledge structures through spreading activation retrieval and allows component representations to be incrementally improved while users are searching for information. The combination of these techniques yields a flexible software repository that minimizes up-front costs and improves its retrieval effectiveness as developers use it to find reusable software artifacts.

**中文翻译**：软件资料库必须针对软件开发组织不断演变和动态变化的需求进行设计。当前的软件资料库方法严重依赖分类，这使得获取和演化问题更加突出：在资料库能够有效使用之前，需要付出高昂的分类与领域分析代价。本文提出了一种方法，利用最少的初始结构来有效查找相关软件组件，同时采用一些方法逐步改进资料库结构。该方法通过两个工具加以演示：PEEL，一个半自动识别可复用组件的工具；以及 CodeFinder，一个检索系统，它通过扩散激活检索（spreading activation retrieval）弥补缺乏显式知识结构的不足，并允许在用户搜索信息的同时逐步改进组件表示。这些技术的结合产生了一种灵活的软件资料库，它将前期成本降至最低，并随着开发人员用它查找可复用软件制品而不断提高其检索效果。

### The Role of Experimentation in Software Engineering: Past, Current, and Future

Basili · pp. 442–449 · [ACM DL](https://dl.acm.org/citation.cfm?id=227818)

*无摘要。*

### The Role of Software Development Methodologies: Past, Present, and Future

DeMarco · pp. 2–4 · [ACM DL](https://dl.acm.org/citation.cfm?id=227730)

*无摘要。*

## 1997 · ICSE 19 {#y1997}

### An Empirical Study of Communication in Code Inspections

Carolyn B. Seaman; Victor R. Basili · pp. 96–106 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253248)

> This paper describes an empirical study which addresses the issue of communication among members of a software development organization.In particular, data was collected concerning code inspections in one software development project.The question of interest is whether or not organizational structure (the network of relationships between developers) has an effect on the amount of effort expended on communication between developers.Both quantitative and qualitative methods were used, including participant observation, structured interviews, generation of hypotheses from field notes, some simple statistical tests of relationships, and interpretation of results with qualitative anecdotes.The study results show that past and present working relationships between inspection participants affect the amount of meeting time spent in different types of discussion, thus affecting the overall meeting length.Reporting relationships and physical proximity also have an effect, as well as the point in the project that an inspection occurs.All but the last of these factors are organizational structure relationships.The contribution of the study is a set of well-supported hypotheses for further investigation.

**中文翻译**：本文描述了一项实证研究，探讨软件开发组织成员之间的沟通问题。具体而言，研究收集了一个软件开发项目中审查（inspections）的相关数据。所关注的问题是：组织结构（即开发人员之间的关系网络）是否会影响开发人员之间沟通所耗费的精力。研究同时采用了定量与定性方法，包括参与式观察、结构化访谈、从田野笔记中生成假设、若干简单的关系统计检验，以及结合质性轶事对结果进行的解释。研究结果表明：审查参与者过去与现在的工作关系，会影响会议中不同类型讨论所花费的时间，从而影响会议的总时长。汇报关系与物理距离同样有影响，审查发生在项目的哪个阶段也有影响。除最后一项外，所有这些因素都属于组织结构关系。本研究的贡献在于提出了一组有充分支持的假设，以供进一步研究。

### Anywhere, Anytime Code Inspections: Using the Web to Remove Inspection Bottlenecks in Large-Scale Software Development

James Perpich; Dewayne E. Perry; Adam A. Porter; Lawrence G. Votta; Michael W. Wade · pp. 14–21 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253234)

*无摘要。*

### Comprehension and Evolution of Legacy Software (Tutorial)

Václav Rajlich · pp. 669–670 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253820)

> This tutorial presents an overview of legacy systems comprehension and evolution.Software comprehension typically consumes more than one-half of the programming effort with the legacy systems.Software evolution is a change in requirements and it is the most common type of change in legacy systems.

**中文翻译**：本教程概述了遗留系统的理解与演化。对于遗留系统而言，软件理解通常要消耗一半以上的编程工作量。软件演化是需求的变化，也是遗留系统中最常见的变更类型。

### Process Modelling - Where Next

Meir M. Lehman · pp. 549–552 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253441)

> After limited interest prior to the 1980s, the software process attracted the attention of a small group of researchers and practitioners as evidenced by a series of International Process Workshops commencing with the first in 1984.General interest had, however, to wait until Osterweil's now classic paper being honoured today and the present author's response were delivered at ICSE 87.This brief paper seeks to move forward from the positions presented then to introduce three process related issues, software process improvement, feedback in the software process and business process improvement.The first is, currently the principal focus of the software process community.The second, it is believed, should be.The third is equally relevant.Individually and collectively these issues appear, to this author at least, to make the majority view of the current focus of process modelling in general and process programming in particular largely irrelevant.

**中文翻译**：在 1980 年代之前，软件过程仅受到有限的关注；此后，它吸引了一小群研究者和从业者的注意，这可以从 1984 年首次召开的一系列国际过程研讨会（International Process Workshops）中看出。然而，普遍的兴趣直到 Osterweil 的那篇经典论文（今日受到表彰）与本文作者的回应在 ICSE 87 上发表之后才真正到来。这篇简短的论文试图在当时所提出立场的基础上继续推进，引入三个与过程相关的问题：软件过程改进、软件过程中的反馈，以及业务过程改进。第一个问题目前是软件过程界的主要关注点。第二个问题，作者认为，本应成为主要关注点。第三个问题同样重要。在作者看来，这些问题单独或合起来看，似乎使得当前过程建模总体上、以及过程编程（process programming）尤其所关注的焦点，在很大程度上变得无关紧要。

### Software Processes Are Software Too, Revisited: An Invited Talk on the Most Influential Paper of ICSE 9

Leon J. Osterweil · pp. 540–548 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253440)

> The ICSE 9 paper, "Software Processes are Software Too," suggests that software processes are themselves a form of software and that there are considerable benefits that will derive from basing a discipline of software process development on the more traditional discipline of application software development.This paper attempts to clarify some misconceptions about this original ICSE 9 suggestion and summarizes some research carried out over the past ten years that seems to confirm the original suggestion.The paper then goes on to map out some future research directions that seem indicated.The paper closes with some ruminations about the significance of the controversy that has continued to surround this work.

**中文翻译**：ICSE 9 论文《软件过程也是软件》提出，软件过程本身就是一种软件，并且将软件过程开发建立在更为传统的应用软件开发学科之上，将带来相当大的益处。本文试图澄清人们对这一 ICSE 9 原始建议的一些误解，并总结过去十年间开展的、似乎证实了该原始建议的部分研究。随后，本文勾勒了一些似乎有必要的未来研究方向。文章最后对围绕这一工作持续存在的争议之意义作了一些思考。

## 1998 · ICSE 20 {#y1998}

### A Conceptual Model of Software Maintenance

Mira Kajko-Mattsson · pp. 422–425 · [doi:10.1109/ICSE.1998.671597](https://doi.org/10.1109/ICSE.1998.671597)

> Four distinct maintenance systems are studied and synthesised: the SEI quality framework and three industrial systems belonging to ABB, Ellemtel, and Ericsson. The goal is to validate the SEI framework, and to build a "state of the practice" conceptual model of the most fundamental software maintenance concepts. This model can help understand the underlying conditions for managing software maintenance. It can provide guidance to organisations in the process of building or improving their maintenance systems. It also constitutes a common basis for communication, for reasoning about software quality, and for building quality and maintenance models.

**中文翻译**：本文研究并综合了四个不同的维护系统：SEI 质量框架，以及分别属于 ABB、Ellemtel 和 Ericsson 的三个工业系统。其目标是验证 SEI 框架，并构建一个关于最基本软件维护概念的“实践现状”概念模型。该模型有助于理解管理软件维护的基本条件，可为正在建立或改进其维护系统的组织提供指导。它也构成了沟通的共同基础，可用于推理软件质量，以及构建质量与维护模型。

### Conceptual Simplicity Meets Organizational Complexity: Case Study of a Corporate Metrics Program

James D. Herbsleb; Rebecca E. Grinter · pp. 271–280 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302190)

> A corporate-wide metrics program faces enormous and poorly understood challenges as its implementation spreads out from the centralized planning body across many organizational boundaries into the sites where the data collection actually occurs. This paper presents a case study of the implementation of one corporate-wide program, focusing particularly on the unexpected difficulties of collecting a small number of straightforward metrics. Several mechanisms causing these difficulties are identified, including attenuated communication across organizational boundaries, inertia created by existing data collection systems, and the perceptions, expectations, and fears about how the data will be used. We describe how these factors influence the interpretation of the definitions of the measurements and influence the degree of conformance that is actually achieved. We conclude with lessons learned about both content and mechanisms to help in navigating the tricky waters of organizational dynamics in implementing a company-wide program.

**中文翻译**：企业范围的度量计划面临着巨大且尚未被充分理解的挑战：随着其实施从集中规划机构扩散到众多组织边界，进入实际收集数据的各个站点时，困难层出不穷。本文介绍了一个企业范围计划实施的案例研究，尤其关注收集少量简单度量时遇到的意外困难。文中识别出了导致这些困难的若干机制，包括跨组织边界的沟通弱化、既有数据收集系统的惯性，以及对数据将如何被使用的认知、期望与担忧。我们描述了这些因素如何影响对度量定义的解释，以及如何影响实际达到的一致性程度。最后，我们总结了关于内容与机制两方面的经验教训，以帮助在实施全公司范围的计划时应对组织动力学中的复杂局面。

### Extracting Concepts from File Names: A New File Clustering Criterion

Nicolas Anquetil; Timothy Lethbridge · pp. 84–93 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302172)

> Decomposing complex software systems into conceptually independent subsystems is a significant software engineering activity which received considerable research attention. Most of the research in this domain considers the body of the source code; trying to cluster together files which are conceptually related. We discuss techniques for extracting concepts (abbreviations) from a more informal source of information: file names. The task is difficult because nothing indicates where to split the file names into substrings. In general, finding abbreviations would require domain knowledge to identify the concepts that are referred to in a name and intuition to recognize such concepts in abbreviated forms. We show by experiment that the techniques we propose allow about 90% of the abbreviations to be found automatically.

**中文翻译**：将复杂软件系统分解为概念上相互独立的子系统，是一项重要的软件工程活动，并已受到大量研究关注。该领域的大部分研究着眼于源代码主体，试图将概念相关的文件聚类在一起。本文讨论了从信息性更弱但更为直接的来源——文件名——中提取概念（缩写）的技术。这一任务十分困难，因为没有任何标记指示应在何处将文件名切分为子串。一般而言，要找出这些缩写，需要领域知识来识别名称中所指的概念，并凭直觉辨认这些概念的缩写形式。我们通过实验表明，所提出的技术能够自动找到约 90% 的缩写。

### Overcoming the NAH Syndrome for Inspection Deployment

Pankaj Jalote; M. Haragopal · pp. 371–378 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302200)

> Despite considerable evidence to show that inspections can help reduce costs and improve quality, inspections are not widely deployed in the software industry. One of the likely reasons for this is the "not applicable here (NAH)" syndrome-developers and managers believe that in their environment, inspections will not provide the benefits seen by other organizations. One of the big challenges for deploying inspections is to overcome this syndrome. We describe two experiments that can be conducted, with little effort, in an organization to obtain data from the organization to build a case for inspections. By conducting one of these experiments, we were able to effectively overcome the NAH syndrome in our organization-many developers and managers are now ready to try inspections in their projects. Though the purpose of the experiment was to overcome the syndrome, the data from the experiment also shows how code inspections compare with unit testing in terms of defect detection capability, and the effect of inspections on the overall cost of development.

**中文翻译**：尽管有大量证据表明，审查（inspections）有助于降低成本、提高质量，但审查在软件业中并未得到广泛部署。其可能原因之一是“此处不适用（NAH）”综合征：开发人员和管理者认为，在他们的环境中，审查不会带来其他组织所见到的益处。克服这一综合征是推广审查面临的重大挑战之一。本文描述了两项可以在组织内以很少投入开展的实验，用以获取组织自身的数据，从而为审查构建论证。通过开展其中一项实验，我们有效克服了本组织中的 NAH 综合征：许多开发人员和管理者现已准备好在各自项目中尝试审查。虽然该实验的目的是克服这一综合征，但其数据还表明，在缺陷检测能力方面审查与单元测试相比如何，以及审查对开发总成本的影响。

### The Ramp-Up Problem in Software Projects: A Case Study of How Software Immigrants Naturalize

Susan Elliott Sim; Richard C. Holt · pp. 361–370 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302199)

> Joining a software development team is like moving to a new country to start employment; the immigrant has a lot to learn about the job, the local customs, and sometimes a new language. In an exploratory case study, we interviewed four software immigrants, in order to characterize their naturalization process. Seven patterns in four major categories were found. In this paper, these patterns are substantiated, and their implications discussed. The lessons learned from this study can be applied equally to improving the naturalization process, and to the formulation of further research questions.

**中文翻译**：加入一个软件开发团队，就像移居新国家开始工作：新来者需要学习大量关于工作、当地习俗，有时还有新语言的内容。在一项探索性案例研究中，我们访谈了四位“软件移民”，以刻画他们的融入过程（naturalization process）。研究发现了四大类别中的七种模式。本文对这些模式进行了论证，并讨论了其含义。从本研究中获得的经验教训，既可用于改进融入过程，也可用于提出进一步的研究问题。

### The Use of Goals to Surface Requirements for Evolving Systems

Annie I. Antón; Colin Potts · pp. 157–166 · [doi:10.1109/ICSE.1998.671112](https://doi.org/10.1109/ICSE.1998.671112)

> This paper addresses the use of goals to surface requirements for the redesign of existing or legacy systems. Goals are widely recognized as important precursors to system requirements, but the process of identifying and abstracting them has not been researched thoroughly. We present a summary of a goal-based method (GBRAM) for uncovering hidden issues, goals, and requirements and illustrate its application to a commercial system, an Intranet-based electronic commerce application, evaluating the method in the process. The core techniques comprising GBRAM are the systematic application of heuristics and inquiry questions for the analysis of goals, scenarios and obstacles. We conclude by discussing the lessons learned through applying goal refinement in the field and the implications for future research.

**中文翻译**：本文探讨了如何利用目标来揭示既有或遗留系统重新设计所需的需求。目标被广泛认为是系统需求的重要前身，但识别和抽象目标的过程尚未得到充分研究。我们提出了一种基于目标的方法（GBRAM）概要，用于发现隐藏的问题、目标和需求，并将其应用于一个商用系统（一个基于 Intranet 的电子商务应用），同时在此过程中对该方法进行了评估。GBRAM 的核心技术在于系统性地应用启发式规则和询问问题，以分析目标、场景和障碍。最后，我们讨论了在实地应用目标精化过程中获得的经验教训，以及对未来研究的启示。

### Toward Computational Support for Software Process Improvement Activities

Keishi Sakamoto; Kumiyo Nakakoji; Yasunari Takagi; Naoki Niihara · pp. 22–31 · [doi:10.1109/ICSE.1998.671099](https://doi.org/10.1109/ICSE.1998.671099)

> Software organizations and projects need guidance on how to improve software process, not just guidelines on what to improve. Several surveys demonstrate that the Capability Maturity Model (CMM) and ISO-9000 only provide the latter. We report our in-depth analysis on a seventeen-month effort in software process improvement (SPI) at OMRON Corporation. The goal of the analysis was to identify issues and challenges of SPI and to design a step-wise practical method to avoid such problems. Major problems we have found include the lack of shared goal among stakeholders, insufficient understanding of the current progress of SPI efforts, and underutilization of a large amount of complex information generated during SPI. We present the method for software organizations and projects for dealing with the problems, and argue for a knowledge-based SPI support system based on the method.

**中文翻译**：软件组织和项目需要的是关于如何改进软件过程的指导，而不仅仅是应当改进什么的指南。若干调查表明，能力成熟度模型（CMM）和 ISO-9000 只提供了后者。我们报告了在 OMRON 公司开展的为期十七个月的软件过程改进（SPI）工作的深入分析。该分析的目标是识别 SPI 的问题与挑战，并设计一种逐步实施的实用方法以避免此类问题。我们发现的主要问题包括：利益相关者之间缺乏共同目标、对 SPI 工作当前进展的理解不足，以及对 SPI 过程中产生的大量复杂信息利用不足。我们提出了软件组织和项目应对这些问题的方法，并主张基于该方法构建一个基于知识的 SPI 支持系统。

### Towards Better Software Projects and Contracts: Commitment Specifications in Software Development Projects

Jyrki Kontio; Olli Pitkänen; Reijo Sulonen · pp. 486–489 · [doi:10.1109/ICSE.1998.671612](https://doi.org/10.1109/ICSE.1998.671612)

> Any software development project requires commitments from its participants. These commitments can include money, resources, deadlines, and specified functionality for the end product. The authors have developed a framework and a set of guidelines to support the specification of such commitments. They have evaluated the framework empirically in a series of case studies. The studies indicated that the framework addresses commitment specification issues that are normally not covered in project contracts and that the specification framework was considered beneficial by project representatives.

**中文翻译**：任何软件开发项目都需要其参与者作出承诺。这些承诺可能包括资金、资源、期限以及最终产品的规定功能。作者开发了一个框架和一套指南，以支持此类承诺的规格说明。他们通过一系列案例研究对该框架进行了实证评估。研究表明，该框架涵盖了通常不在项目合同中涉及的承诺规格说明问题，并且项目代表认为该规格说明框架是有益的。

## 1999 · ICSE 21 {#y1999}

### CHIME: Customizable Hyperlink Insertion and Maintenance Engine for Software Engineering Environments

Premkumar T. Devanbu; Yih-Farn Chen; Emden R. Gansner; Hausi A. Müller; Johannes Martin · pp. 473–482 · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302679)

*无摘要。*

### Software Evolution and "light" Semantics (Extended Abstract)

Dewayne E. Perry · pp. 587–590 · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302706)

*无摘要。*

### Splitting the Organization and Integrating the Code: Conway's Law Revisited

James D. Herbsleb; Rebecca E. Grinter · pp. 85–95 · [ACM DL](https://dl.acm.org/doi/10.1145/302405.302455)

> It is widely acknowledged that coordination of large scale software development is an extremely difficult and persistent problem. Since the structure of the code mirrors the structure of the organization, one might expect that splitting the organization across time zones, cultures, and (natural) languages would make it difficult to assemble the components. This paper presents a case study of what indeed turned out to be the most difficult part of a geographically distributed software project, i.e., integration. Coordination problems were greatly exaggerated across sites, largely because of the breakdown of informal communication channels. The results imply that multi-site development can benefit to some extent from stable plans, processes, and specifications. The inherently unpredictable aspects of projects, however, require communication channels that can be invoked spontaneously, by developers, as needed. These results shed light on the problems and mechanisms underlying the coordination needs of development projects generally, be they co-located or distributed.

**中文翻译**：人们普遍认为，大规模软件开发的协调是一个极其困难且持久的问题。由于代码结构反映组织结构，人们可能预计，将组织分散在不同时区、文化和（自然）语言之间，会使组件的装配变得困难。本文介绍了一项案例研究，考察了地理上分布的软件项目中确实最为困难的部分，即集成。跨站点的协调问题因非正式沟通渠道的瓦解而被大大加剧。研究结果表明，多站点开发在一定程度上可以从稳定的计划、过程和规格说明中获益。然而，项目中固有的不可预测性要求开发者能够根据需要随时启用沟通渠道。这些结果有助于阐明开发项目（无论是同地还是分布式）协调需求背后的问题与机制。
