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

ICSE 前 21 届（1976–1999）中挑出的 89 篇论文与演讲，按年份排列，附原文摘要（67 篇有摘要；其余在 ACM DL / OpenAlex 上没有）。摘要版权归 ACM / IEEE 所有，仅供阅读参考，不在本站 CC BY-NC 许可范围内。

## 1976 · ICSE 2 {#y1976}

### Documentation Tools and Techniques

John R. Mashey; D. W. Smith · pp. 177–181 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807671)

> In a software development project of any appreciable size, the production of usable, accurate documentation may well consume more effort than the production of the software itself. Several years of experience on many Programmer's Workbench projects have shown that document preparation should not be separated from software development and that the combination of a flexible operating system, a powerful command language, and good text processing facilities permits quick and convenient production of many kinds of documentation which might be otherwise unobtainable, impractical, or very expensive. Our basic approach has been to develop techniques for effective combination of existing UNIX facilities. A number of case histories are given to illustrate the flexibility, convenience, and general usefulness of these techniques.

### PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems (Abstract)

Daniel Teichroew; Ernest A. Hershey III · p. 2 · [ACM DL](https://dl.acm.org/citation.cfm?id=807641)

> PSL/PSA is a Computer-Aided Structured Documentation and Analysis technique that was developed for, and is being used for, analysis and documentation of requirements and preparation of functional specifications for information processing systems. The present status of requirements definition is described as the basis for describing the problem which PSL/PSA is intended to solve. The basic concepts of the Problem Statement Language are introduced and the content and use of a number of standard reports that can be produced by the Problem Statement Analyzer are briefly described. The experience to date indicates that computer aided methods can be used to aid system development during the requirements definition stage and that the main factors holding back such use are not so much related to the particular characteristics and capabilities of PSL/PSA as they are to organizational considerations involved in any change in methodology and procedure.

### Program Evolution and Its Impact on Software Engineering

M. M. Lehman; F. N. Parr · pp. 350–357 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807698)

> Large scale, widely used programs such as operating systems are never complete. They undergo a continuing evolutionary cycle of maintenance, augmentation and restructuring to keep pace with evolving usage and implementation technologies. The paper provides quantitative evidence, from widely different environments, of the existence and nature of this evolutionary process. Interpretations and possible significance of some of the observed phenomena are discussed. Some implications for software engineering and for project planners and managers are noted.

### Software Requirements: Are They Really a Problem

Thomas E. Bell; T. A. Thayer · pp. 61–68 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807650)

> Do requirements arise naturally from an obvious need, or do they come about only through diligent effort—and even then contain problems? Data on two very different types of software requirements were analyzed to determine what kinds of problems occur and whether these problems are important. The results are dramatic: software requirements are important, and their problems are surprisingly similar across projects. New software engineering techniques are clearly needed to improve both the development and statement of requirements.

### The Dimensions of Maintenance

E. Burton Swanson · pp. 492–497 · [ACM DL](https://dl.acm.org/doi/10.5555/800253.807723)

> The area of software maintenance has been described by one author as an “iceberg.” (EDP Analyzer, 1972) Much goes on here that does not currently meet the eye. In part, this is the consequence of measurement difficulties. Practitioners and researchers can benefit from an understanding of the “dimensionality” of the maintenance problem. Some measures are suggested for coming to grips with this dimensionality, and problems of utilization associated with these measures are explored.

## 1978 · ICSE 3 {#y1978}

### Software Engineering: A Keynote Address

C. A. R. Hoare · pp. 1–4 · [ACM DL](https://dl.acm.org/citation.cfm?id=803183)

> This paper argues that our recent progress in the development of a sound programming methodology should not lead us to ignore the more difficult aspects of engineering; and that in future we should pay more attention to the quality of our designs, and not just the accuracy of their implementation.

### Using a Behavioral Theory of Program Comprehension in Software Engineering

Ruven E. Brooks · pp. 196–201 · [ACM DL](https://dl.acm.org/doi/10.5555/800099.803210)

> A theory is presented of how a programmer goes about understanding a program. The theory is based on a representation of knowledge about programs as a succession of knowledge domains which bridge between the problem domain and the executing program. A hypothesis and verify process is used by programmers to reconstruct these domains when they seek to understand a program.The theory is useful in several ways in software engineering: It makes accurate predictions about the effectiveness of documentation; it can be used to systematically evaluate and critique other claims about documentation, and it may even be a useful guideline to a programmer in actually constructing documentation.

## 1979 · ICSE 4 {#y1979}

### Software Engineering: As it is

Barry W. Boehm · pp. 11–21 · [ACM DL](https://dl.acm.org/citation.cfm?id=802916)

> This paper presents a view of software engineering as it is in 1979. It discusses current software engineering practice with respect to lessons learned in the past few years, and concludes that the lessons are currently not heeded roughly half of the time. The paper discusses some of the factors which may account for this lag, including rapid technological change, education shortfalls, technology transfer inhibitions, resistance to disciplined methods, inappropriate role models, and a restricted view of software engineering. The paper also updates a 1976 state of the art survey of software engineering technology, including such topics as requirements and specifications, design, programming, verification and validation, maintenance, software psychology, and software economics. It concludes that the field is making solid progress, but that it is growing more complex at a faster rate than we can put it in order.

## 1981 · ICSE 5 {#y1981}

### A Database Model for Effective Configuration Management in the Programming Environment

Karen E. Huff · pp. 54–62 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802516)

> The effective management of configurations by programmers requires automatic techniques which are operative in the program development environment. In this paper, an abstract model is developed to cover the significant aspects of a typical programming environment pertinent to configuration management, using a database to capture configuration knowledge. The two aspects of the model deal with configuration identification and configuration control. In considering configuration identification, it is shown that the tools in the programming environment determine which configuration items need to be identified and also determine what the interesting and useful relations are among those items. In considering configuration control, the notion of a workspace, consisting of certain modification rights and certain visibility into the database, is developed to prevent conflict and to promote cooperation among programmers. The entire model can be used to evaluate the effectiveness of configuration management within a particular programming environment or as the basis of a programming environment design.

### Evaluation of a Software Requirements Document by Analysis of Change Data

Victor R. Basili; David M. Weiss · pp. 314–324 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802544)

> We describe in this paper an effective data collection method for evaluating software development methodologies, from definition of the objectives of the data collection to analysis of the results. We show how the data analysis can answer questions with respect to how successfully the goals of the development methodology are met. The A-7 requirements document is used as an example. We provide the results of data analyses conducted partway through the A-7 flight software development cycle, and discuss the utility of information obtained by such partial analyses. Results from the study show that data collection is feasible and useful when performed as part of configuration control, that data distributions based on partial data provide useful feedback to the developers, and that the A-7 Requirements Document is easily maintained and changed.

### Executable Requirements for Embedded Systems

Pamela Zave; Raymond T. Yeh · pp. 295–304 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802542)

> An approach to requirements specification for embedded systems, based on constructing an executable model of the proposed system interacting with its environment, is proposed. The approach is explained, motivated, and related to data-oriented specification techniques. Portions of a specification language embodying it are introduced, and illustrated with an extended example in which the requirements for a process-control system are developed incrementally.

### The Effect of Modularization and Comments on Program Comprehension

Scott N. Woodfield; Hubert E. Dunsmore; Vincent Y. Shen · pp. 215–223 · [ACM DL](https://dl.acm.org/doi/10.5555/800078.802534)

> An experiment was conducted to investigate how different types of modularization and comments are related to programmers' ability to understand programs. Forty-eight experienced programmers were given eight different versions of the same program and asked to answer a twenty question quiz used to measure comprehension. These eight different versions were the result of the program being constructed with four types of modularization (monolithic, functional, super, and abstract data type), each with and without comments. Those subjects whose programs contained comments were able to answer more questions than those without comments. Also, those subjects who were given the abstract data type version of the program were able to do significantly better than those with any other type of modularization.

## 1982 · ICSE 6 {#y1982}

### An Editor for Documentation in pi-System to Support Software Development and Maintenance

Yukikazu Nakamoto; T. Iwamoto; M. Hori; Kenichi Hagihara; Nobuki Tokura · pp. 330–339 · [ACM DL](https://dl.acm.org/citation.cfm?id=807775)

> A lot of information necessary to maintain a software tends to be lost in conventional documentation. One of the leading causes is considered that the ideas of developers which maintainers will want to know later are not fixed in any documents while the ideas are fresh. To remove the cause, we propose a new description form, called a frame, and construct a system called π, to support a software through its lifetime. This system gathers all the information with the frames, stores it in a database and provides the various services with respect to programming and documentation. This paper describes the frames and a subsystem, called π-editor, which provides a user friendly interface to make it easy to gather essential information. By using frames, (1) the associated information around one programming concept can be gathered at one time and (2) lack of necessary information hardly arises. The editor has the distinguished features such as (1) a structure-oriented display editor, (2) facilities to display selective information, provide helpful user guides, and check input errors immediately.

### An Examination of Evolution Dynamics

M. J. Lawrence · pp. 188–196 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807761)

> Data on the history of seven systems was analysed to statistically test the 5 laws of software evolution proposed first by Belady and Lehman in 1976.While there was some evidence supporting laws 1 and 2, laws 3-5 were not supported by the data. In the light of the result a new discontinuous model of software evolution is proposed to replace the smoothly changing continuous model proposed by Lehman.

### Configuration Control for Evolutional Software Products

Osamu Shigo; Yoshio Wada; Yuichi Terashima; Kanji Iwamoto; Takashi Nishimura · pp. 68–83 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807749)

> This paper describes the concept of and a system for configuration control for evolutional software products, in which a wide spectrum of varied software products are being continuously evolved, along with rapid advancements in hardware technologies. The system contains a database for dealing with the overall configuration structure, including hierarchical product structure with change status, master file directories, difficulty occurrences and user information. The data representing the configuration can be in more abstract or macroscopic level than the traditional software configuration control, since the configuration manager should control the overall outlines for all software products. The concept and system described in the paper have been used for intelligent terminal software product management in NEC's Data Terminals Division.

### DUAL: An Interactive Tool for Developing Documented Programs by Step-Wise Refinements

Luigi Petrone; Antonio Di Leva; Franco Sirovich · pp. 350–359 · [ACM DL](https://dl.acm.org/citation.cfm?id=807777)

> Programs are integrated hierarchical structures of formal texts - instructions - and informal texts - documentation. Only if there is a mechanical connection between program design and program development there can be higher chances that the program documentation, originated at design time, will not, sooner or later, become obsolete with respect to the current state of the system. DUAL is an interactive, incremental, intelligent editor of program and documentation texts to be used for software implementations whose anticipated life cycle is significantly long to deserve much attention. The screen interface plays a unique role in DUAL since it allows a visitor ( designer or maintenance engineer) “to replay” as many times as desired the evolution of the system from design to implementation. The access to the hierarchically organized Design Information is made easy and natural by the DUAL video oriented user interface.

### Design, Implementation, and Evaluation of a Revision Control System

Walter F. Tichy · pp. 58–67 · [ACM DL](https://dl.acm.org/citation.cfm?id=807748)

> The Revision Control System (RCS) is a software tool that helps in managing multiple revisions of text. RCS automates the storing, retrieval, logging, identification, and merging of revisions, and provides access control. It is useful for text that is revised frequently, for example programs and documentation. This paper presents the design and implementation of RCS. Both design and implementation are evaluated by contrasting RCS with SCCS, a similar system. SCCS is implemented with forward, merged deltas, while RCS uses reverse, separate deltas. (Deltas are the differences between successive revisions.) It is shown that the latter technique improves run-time efficiency, while requiring almost no extra space.

### MAP: A Tool for Understanding Software

S. Warren · pp. 28–39 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807745)

> Maintenance of software is a major problem that the data processing industry faces today. This paper describes MAP, a tool, that addresses the problems of software maintenance by helping programmers to understand their programs.

### The Dimensions of Healthy Maintenance

Robert S. Arnold; D. A. Parker · pp. 10–27 · [ACM DL](https://dl.acm.org/doi/10.5555/800254.807744)

> What characterizes “healthy” or “satisfactory” software maintenance? How can we know it when we see it? This paper gives initial answers to these questions. We first argue the need for objectively measurable maintenance performance criteria in judging the “adequacy” of maintenance and present a set of criteria for judging maintenance performance in a particular software environment. We then subject the criteria to a practical test by applying them in this environment. We show how applying the criteria enables an informed overall maintenance performance appraisal, locates general maintenance problems, stimulates suggestions for improving maintenance on individual projects, allows these projects' maintenance to be compared and the projects ordered for improvement, and assesses the potential effectiveness of the suggestions in new project maintenance. We also sketch how criteria application can be generalized to software development monitoring and design methodology evaluation.

## 1984 · ICSE 7 {#y1984}

### Fifteen Years of Psychology in Software Engineering: Individual Differences and Cognitive Science

Bill Curtis · pp. 97–107 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801956)

> Since the 1950's, psychologists have studied the behavioral aspects of software engineering. However, the results of their research have never been organized into a subfield of either software engineering or psychology. This failure results from the difficulty of integrating theory and data from the mixture of paradigms borrowed from psychology. This paper will review some of the psychological research on software engineering performed since the Garmisch Conference in 1968. This review will be organized under two of the psychological paradigms used in exploring programming problems: individual differences and cognitive science. The major theoretical and practical contributions of each area to the theory and practice of software engineering will be discussed. The review will end with a call for more research guided by the paradigm of cognitive science, since such results are the easiest to integrate with new developments in artificial intelligence and computer science theory.

### Knowledge-Based Communication Processes in Software Engineering

Gerhard Fischer; Matthias Schneider · pp. 358–368 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801993)

> A large number of problems to be solved with the help of computer systems are ill-structured. Their solution requires incremental design processes, because complete and stable specifications are net available.For tasks of this sort, life cycle models are inadequate. Our design methodology is based on a rapid prototyping approach which supports the coevolution of specification and implementation. Communication between customers, designers and implementors and communication between the humans and the knowledge base in which the emerging product is embedded are of crucial importance. Our work is centered around knowledge-based systems which enhance and support the communication needs in connection with software systems.Program documentation systems are used as an example to illustrate the relevance of knowledge-based human-computer communication in software engineering.

### PROUST: Knowledge-Based Program Understanding

W. Lewis Johnson; Elliot Soloway · pp. 369–380 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801994)

> This paper1 describes a program called PROUST which does on- line analysis and understanding of Pascal programs written by novice programmers. PROUST takes as input a program and a non-algorithmic description of the program requirements, and finds the most likely mapping-between the requirements and the code. This mapping is in essence a reconstruction of the design and implementation steps that the programmer went through in writing the program. A knowledge base of programming plans and strategies, together with common bugs associated with them, is used in constructing this mapping. Bugs are discovered in the process of relating plans to the code; PROUST can therefore give deep explanations of program bugs by relating the buggy code to its underlying intentions.

### The Modular Structure of Complex Systems

David Lorge Parnas; Paul C. Clements; David M. Weiss · pp. 408–419 · [ACM DL](https://dl.acm.org/doi/10.5555/800054.801999)

> This paper discusses the organization of software that is inherently complex because there are very many arbitrary details that must be precisely right for the software to be correct. We show how the software design technique known as information hiding or abstraction can be supplemented by a hierarchically-structured document, which we call a module guide. The guide is intended to allow both designers and maintainers to identify easily the parts of the software that they must understand without reading irrelevant details about other parts of the software. The paper includes an extract from a software module guide to illustrate our proposals.

## 1985 · ICSE 8 {#y1985}

### Active Design Reviews: Principles and Practices

David Lorge Parnas; David M. Weiss · pp. 132–136 · [ACM DL](https://dl.acm.org/citation.cfm?id=319599)

> Although many new software design techniques have emerged in the past 15 years, there have been few changes to the procedures for reviewing the designs produced using these techniques. This paper describes an improved technique, based on the following ideas, for reviewing designs. The efforts of each reviewer should be focussed on those aspects of the design that suit his experience and expertise. The characteristics of the reviewers needed should be explicitly specified before reviewers are selected. Reviewers should be asked to make positive assertions about the design rather than simply allowed to point out defects. The designers pose questions to the reviewers, rather than vice versa. These questions are posed on a set of questionnaires that requires careful study of some aspect of the design. Interaction between designers and reviewers occurs in small meetings involving 2 - 4 people rather than meetings of large groups. Illustrations of these ideas drawn from the application of active design reviews to the Naval Research Laboratory's Software Cost Reduction Project are included.

### SODOS - A Software Documentation Support Environment: Its Use

Ellis Horowitz; Ronald Williamson · pp. 8–14 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319571)

> This paper describes a computerized environment, SODOS (Software Documentation Support), which supports the definition and manipulation of documents used in developing software. An object oriented environment is used as a basis for the SODOS interface. SODOS is built around a Software Life Cycle (SLC) Model that structures all access to the documents stored in the environment. One advantage of this model is that it supports software documentation independent of any fixed methodology that the developers may be using. The main advantage of the system is that it permits traceability through each phase of the Life Cycle, thus facilitating the testing and maintenance phases. Finally the effort involved in learning and using SODOS is simplified due to a sophisticated "user-friendly" interface.

### Software Technology Maturation

Samuel T. Redwine Jr.; William E. Riddle · pp. 189–200 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319624)

> We have reviewed the growth and propagation of a variety of software technologies in an attempt to discover natural characteristics of the process as well as principles and techniques useful in transitioning modern software technology into widespread use. What we have looked at is the technology maturation process, the process by which a piece of technology is first conceived, then shaped into something usable, and finally "marketed" to the point that it is found in the repertoire of a majority of professionals. A major interest is the time required for technology maturation — and our conclusion is that technology maturation generally takes much longer than popularly thought, especially for major technology areas. But our prime interest is in determining what actions, if any, can accelerate the maturation of technology, in particular that part of maturation that has to do with transitioning the technology into widespread use. Our observations concerning maturation facilitators and inhibitors are the major subject of this paper.

### The Software Knowledge Base

Bertrand Meyer · pp. 158–165 · [ACM DL](https://dl.acm.org/doi/10.5555/319568.319611)

> We describe a system for maintaining useful information about a software project. The “software knowledge base” keeps track of software components and their properties; these properties are described through binary relations and the constraints that these relations must satisfy. The relations and constraints are entirely user-definable, although a set of predefined libraries of relations with associated constraints is provided for some of the most important aspects of software development (specification, design, implementation, testing, project management).The use of the binary relational model for describing the properties of software is backed by a theoretical study of the relations and constraints which play an important role in software development.

## 1987 · ICSE 9 {#y1987}

### An Architecture for Intelligent Assistance in Software Development

Gail E. Kaiser; Peter H. Feiler · pp. 180–188 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41783)

> We define an architecture for a software engineering environment that behaves as an intelligent assistant. Our architecture consists of three key aspects: an objectbase, a model of the software development activities, and controlled automation. Our objectbase is adapted from other research, but our model is unique in that is consists primarily of rules that define the preconditions and multiple postconditions of software development activities. Our most significant contribution is opportunistic processing, whereby the environment performs software development activities through controlled automation. This is accomplished by a forward and backward chaining interpretation of the rule set. Activities are automatically carried out at some time between when their preconditions are satisfied and when their postconditions are required. Automation is controlled through strategies that guide the assistant in choosing an appropriate point for carrying out each activity.

### From Design to Redesign

Gerhard Fischer; Andreas C. Lemke; Christian Rathke · pp. 369–376 · [ACM DL](https://dl.acm.org/citation.cfm?id=41806)

*无摘要。*

### Knowledge-Based Software Design Using Design Schemas

Mitchell D. Lubars; Mehdi T. Harandi · pp. 253–262 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41790)

> Design schemas provide a means for abstracting software designs into broadly reusable components that can be assembled and refined into new software designs. This paper describes a knowledge-based software development paradigm that is based on the design schema representation. It combines design schemas, domain knowledge, and various types of rules to assist in the quick generation of software designs from user specifications. A prototypical environment, IDeA (Intelligent Design Aid), is described that supports the knowledge-based paradigm. The schema-based techniques used in IDeA are presented along with some examples of their use.

### On Building Software Process Models Under the Lamppost

Bill Curtis; Herb Krasner; Vincent Y. Shen; Neil Iscoe · pp. 96–105 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41776)

> Most software process models are based on the management tracking and control of a project. The popular alternatives to these models such as rapid prototyping and program transformation are built around specific technologies, many of which are still in their adolescence. Neither of these approaches describe the actual processes that occur during the development of a software system. That is, these models focus on the series of artifacts that exist at the end of phases of the process, rather than on the actual processes that are conducted to create the artifacts. We conducted a field study of large system development projects to gather empirical information about the communication and technical decision-making processes that underlie the design of such systems. The findings of this study are reviewed for their implications on modeling the process of designing large software systems. The thesis of the paper is that while there are many foci for process models, the most valuable are those which capture the processes that control the most variance in software productivity and quality.

### Process Models, Process Programs, Programming Support

M. M. Lehman · pp. 14–16 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41767)

*无摘要。*

### Software Processes Are Software Too

Leon J. Osterweil · pp. 2–13 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41766)

*无单独摘要，以下为正文首段。*

> The major theme of this meeting is the exploration of the importance of.ul process as a vehicle for improving both the quality of software products and the the way in which we develop and evolve them. In beginning this exploration it seems important to spend at least a short time examining the nature of process and convincing ourselves that this is indeed a promising vehicle. We shall take as our elementary notion of a process that it is a systematic approach to the creation of a product or the accomplishment of some task. We observe that this characterization describes the notion of process commonly used in operating systems-- namely that a process is a computational task executing on a single computing device. Our characterization is much broader, however, describing any mechanism used to carry out work or achieve a goal in an orderly way.

### Tailoring the Software Process to Project Goals and Environments

Victor R. Basili; H. Dieter Rombach · pp. 345–359 · [ACM DL](https://dl.acm.org/citation.cfm?id=41804)

> This paper presents a methodology for improving the software process by tailoring it to the specific project goals and environment. This improvement process is aimed at the global software process model as well as methods and tools supporting that model. The basic idea is to use defect profiles to help characterize the environment and evaluate the project goals and the effectiveness of methods and tools in a quantitative way. The improvement process is implemented iteratively by setting project improvement goals, characterizing those goals and the environment, in part, via defect profiles in a quantitative way, choosing methods and tools fitting those characteristics, evaluating the actual behavior of the chosen set of methods and tools, and refining the project goals based on the evaluation results. All these activities require analysis of large amounts of data and, therefore, support by an automated tool. Such a tool — TAME (Tailoring A Measurement Environment) — is currently being developed.

### Version Control in the Inscape Environment

Dewayne E. Perry · pp. 142–149 · [ACM DL](https://dl.acm.org/doi/10.5555/41765.41780)

> We present the important issues to be considered in version control mechanisms and characterize and compare the kinds of version control systems extant in current programming environments. We then characterize Inscape's version control mechanism. Invariant, and show that it makes several significant advances in the state of the art. Using Instress (Inscape's module interface specification language) specifications, Invariant provides a better understanding of the notion of parallel versions, a more comprehensive notion of version consistency, and a more flexible method of system composition than current mechanisms. In particular, Invariant provides a formalization of the notions of version equivalence and compatibility that correspond closely with our intuitive (and practical) notions of version equivalence and compatibility. These various forms of version compatibility provide the system builder with the concept of plug-compatibility — an extremely useful facility in composing systems from component parts.

## 1988 · ICSE 10 {#y1988}

### Enhancing Program Readability and Comprehensibility with Tools for Program Visualization

Ronald Baecker · pp. 356–366 · [ACM DL](https://dl.acm.org/citation.cfm?id=55858)

> In order to make computer programs more comprehensible, the presentation of program source text, program documentation, and program execution needs to be enhanced over its conventional treatment. The paper describes a number of new techniques and tools developed to achieve these ends. One of these is a novel design for the effective presentation of source text in the C programming language using high quality digital typography, and a processor which implements the design. Some experimental evidence is summarized to demonstrate that the resulting source text presentation is significantly more readable and comprehensible than the presentation conventionally used today. Brief descriptions are also given of two other techniques, the development of a novel system of structured program documentation incorporating both text and graphics, and the portrayal of program execution with coloured computer animation.

### Evolution of Tools (Abstract)

Kishida · p. 2 · 无在线链接

*无摘要。*

### Models of Software Development Environments

Dewayne E. Perry; Gail E. Kaiser · pp. 60–68 · [ACM DL](https://dl.acm.org/doi/10.5555/55823.55830)

> We present a general model of software development environments that consists of three components: structures, mechanisms and policies. The advantage of this model is that it distinguishes intuitively those aspects of an environment that are useful in comparing and contrasting software development environments. Our initial application of the model is to characterize four classes of environments by means of a sociological metaphor based on scale: the individual, the family, the city and the state models. The utility of the IFCS taxonomy is that it delineates the important classes of interactions among software developers and exposes the ways in which current software development environments inadequately support the development of large systems. We demonstrate the generality of our model by also applying it to a previously published taxonomy that categorizes environments according to how they relate to four historical trends: language-centered, structure-oriented, toolkit and method-based environments.

### Recording the Reasons for Design Decisions

Colin Potts; Glenn Bruns · pp. 418–427 · [ACM DL](https://dl.acm.org/citation.cfm?id=55863)

> The authors outline a generic model for representing design deliberation and the relation between deliberation and the generation of method-specific artifacts. A design history is regarded as a network consisting of artifacts and deliberation nodes. Artifacts represent specifications or design documents. Deliberation nodes represent issues, alternatives or justifications. Existing artifacts give rise to issue about the evolving design, an alternative is one of several positions that respond to the issue (perhaps calling for the creation or modification of an artifact), and a justification is a statement giving the reasons for and against the related alternative. The model is applied to the development of a text formatter. The example development is represented in hypertext and as a Prolog database, the two representations being shown to complement each other. The authors conclude with a discussion of the relation between this model and other work and of the implications for tool support and methods.

### Theory-W Software Project Management: A Case Study

Barry W. Boehm; Rony Ross · pp. 30–40 · [ACM DL](https://dl.acm.org/citation.cfm?id=55827)

> The search for a single unifying principle to guide software project management has been relatively unrewarding to date. Most candidate principles are either insufficiently general to apply in many situations, or so general that they provide no useful specific guidance. This paper presents a candidate unifying principle which appears to do somewhat better. Reflecting various alphabetical management theories (X, Y, Z), it is called the Theory W approach to software project management. Theory W: Make Everyone a Winner The paper explains the Theory W principle and its two subsidiary principles: Plan the flight and fly the plan; and, Identify and manage your risks. To test the practicability of Theory W, a case study is presented and analyzed: the attempt to introduce new information systems to a large industrial corporation in an emerging nation. The case may seem unique, yet it is typical. The analysis shows that Theory W and its subsidiary principles do an effective job both in explaining why the project encountered problems, and in prescribing ways in which the problems could have been avoided.

## 1989 · ICSE 11 {#y1989}

### A Model for the Reuse of Software Design Information

Kevin W. Jameson · pp. 205–216 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74615)

> This paper presents a general model for the representation and manipulation of module level software design information, leading to the effective reuse of software design information across different programming languages.Language independent design documents are represented as ASCII files containing tagged design information sufficient for the construction of a compilable program architecture.The resulting architecture is composed of documented module stubs which describe calling relationships, parameters, functional descriptions, and algorithms characteristic of the architecture.No executable code is included in the compilable modules.Frameworks of tagged locations in Zanguage dependent standard module templates are matched against corresponding tags in the ASCII design files, effectively blending language dependent and independent information into a compilable stub architecture.The process is reversible in that a language independent design file can be generated from an architecture in the standard tagged format, thus supporting the movement of design information across different programming languages.

### Software Process Modeling: Principles of Entity Process Models

Watts S. Humphrey; Marc I. Kellner · pp. 331–342 · [ACM DL](https://dl.acm.org/doi/10.1145/74587.74631)

> A defined software process is needed to provide organizations with a consistent framework for performing their work and im- proving the way they do it. An overall framework for modeling simplifies the task of producing process models, permits them to be tailored to individual needs, and facilitates process evolution. This paper outlines the principles of entity process, models and suggests ways in which they can help to address some of the problems with more conventional approaches to modeling software processes.

## 1990 · ICSE 12 {#y1990}

### A Decision-Based Configuration Process Model

Thomas Rose; Matthias Jarke · pp. 316–325 · [ACM DL](https://dl.acm.org/citation.cfm?id=100341)

*无摘要。*

### LaSSIE: a Knowledge-based Software Information System

Premkumar T. Devanbu; Ronald J. Brachman; Peter G. Selfridge; Bruce W. Ballard · pp. 249–261 · [ACM DL](https://dl.acm.org/citation.cfm?id=100333)

> The authors discuss the important problem of invisibility that is inherent in the task of developing large software systems. It is pointed out that there are no direct solutions to this problem; however, there are several categories of systems-relational code analyzers, reuse librarians, and project management databases-that can be seen as addressing aspects of the invisibility problem. It is argued that these systems do not adequately deal with certain important aspects of the problem of invisibility-semantic proliferation, multiple views, and the need for intelligent indexing. A system called LaSSIE, which uses knowledge representation and reasoning technology to address each of these three issues directly and thereby help with the invisibility problem, has been built. The authors conclude with an evaluation of the system and a discussion of open problems and ongoing work.

### Technology Transfer as Collaboration: The Receptor Group

Priscilla J. Fowler · pp. 332–333 · [ACM DL](https://dl.acm.org/citation.cfm?id=100345)

*无摘要。*

### The Evolution of Technology Transfer at MCC's Software Technology Program: From Didactic to Dialectic

James D. Babcock; Laszlo A. Belady; Nancy C. Gore · pp. 290–299 · [ACM DL](https://dl.acm.org/doi/10.5555/100296.100337)

> MCC's software technology program (STP) has a dual mission: to create tools and methodologies to assist development teams in the design of large, complex, distributed software systems, and to ensure the widespread diffusion of these technologies within STP shareholder organizations. STP has developed a comprehensive set of traditional technology transfer methods; although these methods make it possible to communicate research results successfully to shareholder receptors, they have spurred little actual use of released technology. STP has recently reevaluated its approach to technology transfer and discovered how it can be better accomplished-by fostering collaboration as its chief agent, rather than by depending on traditional transfer-and-feedback mechanisms. The authors describe the evolution of this new approach and present some of the results of collaborative experiences to date. It is found that collaborations revitalize research and that they empower STP's shareholders to affect the directions of that research. >

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

### Extending the Potts and Bruns Model for Recording Design Rationale

Lee · pp. 114–125 · [ACM DL](https://dl.acm.org/citation.cfm?id=256705)

*无摘要。*

### Non-Technological Issues in Software Engineering

Kellner, Curtis, DeMarco, Kishida, Schlumberger, Tully · pp. 144–146 · [ACM DL](https://dl.acm.org/citation.cfm?id=256728)

*无摘要。*

### Software reuse: is it delivering?

Frakes, Biggerstaff, Prieto-Díaz, Matsumura, Schäfer · pp. 52–59 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256681)

> A panel discussion is presented to examine the evidence, pro and con, that software reuse is delivering. Verifiable and repeatable increases in software quality and productivity in field settings are used as criteria for the success of reuse. Reusability is defined as a technology that can be of significant value to software development and maintenance. A scale to evaluate whether reuse is delivering is outlined. The scale is ordinal, with five being the best possible rating. The three respondents, from Germany, Japan, and the US, discuss how reuse, as defined, is delivering in their parts of the world. >

### Tolerating Inconsistency

Balzer · pp. 158–165 · [ACM DL](https://dl.acm.org/doi/10.5555/256664.256748)

*无单独摘要，以下为正文首段。*

> This is a short paper about a simple technique for making applications robust by marking data that violates specially identified invariants and using those marks as guards around code which is sensitive to that invariant.Such a capability is needed when dealing with the exceptions that arise in practical applications and distinguish them from idealized specifications. Previous techniques either required the removal of the constraint so that the exception would be allowed, or its modification to exclude the particular exception from the restriction.Our technique softens the entire constraint without introducing special cases, and is intended primarily for temporary exceptions. Rather than synchronizing all updates required by some constraint, it allows them instead to occur distributed in time in any arbitrary order. Thus, it is particularly useful in multiclient applications with shared responsibilities and authority, such as cooperative design (including software development).

## 1992 · ICSE 14 {#y1992}

### High-Pressure Steam Engines and Computer Software

Nancy G. Leveson · pp. 2–14 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143076)

*无摘要。*

### Process Programming by Hindsight

Pankaj K. Garg; Sanjay Bhansali · pp. 280–293 · [ACM DL](https://dl.acm.org/doi/10.1145/143062.143128)

> Process programming refers to the activity of algorithmicly describing models of programming activities (processes). A serious limitation of process programming has been that . it is often hard to describe a programming process a priori. In this paper we present an approach to process programming which addresses this limitation. Our approach is based on the premise that process programs are easier to describe in hindsight rather than by foresight, and hence can be synthe- sized by observing and analyzing a recorded process history. In this paper we describe an adaptation of the well-known explanation-based learning algorithm to synthesize a process fragment from a process history. We demonstrate the usefulness of the approach on a realistic example of coordinating file changes through a version control system.

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

### Software Aging

Parnas · pp. 279–287 · [ACM DL](https://dl.acm.org/citation.cfm?id=257788)

> Programs, like people, get old. We can't prevent aging, but we can understand its causes, take steps to limits its effects, temporarily reverse some of the damage it has caused, and prepare for the day when the software is no longer viable. A sign that the software engineering profession has matured will be that we lose our preoccupation with the first release and focus on the long-term health of our products. Researchers and practitioners must change their perception of the problems of software development. Only then will software engineering deserve to be called "engineering".

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

### Automating Process Discovery Through Event-Data Analysis

Jonathan E. Cook; Alexander L. Wolf · pp. 73–82 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225021)

> Many software process methods and tools presuppose the existence of a formal model of a process.Unfortunately, developing a formal model for an on-going, complex process can be dificult, costly, and err-or prone.This presents a practical barrier to the adoption of process technologies.The barrier would be lowered by automatmg the creation of formal models.We are currently exploring techniques that can use basic event data captured from an on-going process to generate a formal model of process behavior.We term this kind of data analysis process discovery.Thts paper descr~bes and illustrates three methods with whzch we have been experimenting: algorithmic grammar inference, Markov models, and neural networks.

### How to Deal With Deviations During Process Model Enactment

Gianpaolo Cugola; Elisabetta Di Nitto; Carlo Ghezzi; M. Mantione · pp. 265–273 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225039)

> A fundamental problem in software processes is how the mintrinsic rigidity of a predejined (formal) model can be reconciled with the need for flexibility, change, and evolution.We therefore distinguish between software processes, as specified in a process description, and their actual performance by humans.Further, we claim that the two inevitably diverge, and thus it is necessary to provide means to reconcile them.We present a preliminary exploration into the problem.In particular, we illustrate how a temporal logic-based approach can be used to capture and tolerate some deviations from the process description during execution.We present a simple process language (LATIN), and its prototype environment (SENTINEL), in which these ideas are currently experimented.1

### The World and the Machine

Michael Jackson · pp. 283–292 · [ACM DL](https://dl.acm.org/doi/10.1145/225014.225041)

> As software developers we are engineers because we make useful machines.We are concerned both with the world, in which the machine serves a useful purpose, and with the machine itself.The competing demands and attractions of these two concerns must be appropriately balanced.Failure to balance them harms our work.Certainly it must take some of the blame for the gulf between researchers and practitioners in software development.To achieve proper balance we must sometimes fight against tendencies and inclinations that are deeply ingrained in our customary practices and attitudes in software development.In this paper some aspects of the relationship between the world and the machine are explored; some sources of distortion are identified; and some suggestions are put forward for maintaining a proper balance.

## 1996 · ICSE 18 {#y1996}

### A systematic survey of CMM experience and results

Herbsleb & Goldenson · pp. 323–330 · [ACM DL](https://dl.acm.org/doi/10.5555/227726.227791)

> The capability maturity model * (CMM) for sojlware has become very influential as a basis for software process improvement (SPI). Most of the evidence to date showing the results of these efforts has consisted of case studies. We present a systematic survey of organizations that have undertaken CMM-based SPI to get more representative results. Wefound evidence that process maturity is in fact associated with better organizational pe~ormance, and that software process appraisals are viewed, in retrospect, as extremely valuable and accurate guides for the improvement effort. The path was not always smooth, however, and e~orts generally took longer and cost more than expected. A number of factors that distinguished highly successful from unsuccessful efforts are identified. Most of these factors are under management control, suggesting that a number of specijic management decisions are likely to have a major impact on the success of the effort.

### Prototypes as Assets, not Toys: Why and How to Extract Knowledge from Prototypes

Schneider · pp. 522–531 · [ACM DL](https://dl.acm.org/citation.cfm?id=227840)

*无摘要。*

### Supporting the Construction and Evolution of Component Repositories

Henninger · pp. 279–288 · [ACM DL](https://dl.acm.org/citation.cfm?id=227776)

> Repositories must be designed to meet the evolving and dynamic needs of software development organizations. Current software repository methods rely heavily on classification, which exacerbates acquisition and evolution problems by requiring costly classification and domain analysis efforts before a repository can be used effectively. This paper outlines an approach in which minimal initial structure is used to effectively find relevant software components while methods are employed to incrementally improve repository structures. The approach is demonstrated through PEEL, a tool to semi-automatically identify reusable components, and CodeFinder, a retrieval system that compensates for the lack of explicit knowledge structures through spreading activation retrieval and allows component representations to be incrementally improved while users are searching for information. The combination of these techniques yields a flexible software repository that minimizes up-front costs and improves its retrieval effectiveness as developers use it to find reusable software artifacts.

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

### Anywhere, Anytime Code Inspections: Using the Web to Remove Inspection Bottlenecks in Large-Scale Software Development

James Perpich; Dewayne E. Perry; Adam A. Porter; Lawrence G. Votta; Michael W. Wade · pp. 14–21 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253234)

*无摘要。*

### Comprehension and Evolution of Legacy Software (Tutorial)

Václav Rajlich · pp. 669–670 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253820)

> This tutorial presents an overview of legacy systems comprehension and evolution.Software comprehension typically consumes more than one-half of the programming effort with the legacy systems.Software evolution is a change in requirements and it is the most common type of change in legacy systems.

### Process Modelling - Where Next

M. M. Lehman · pp. 549–552 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253441)

> After limited interest prior to the 1980s, the software process attracted the attention of a small group of researchers and practitioners as evidenced by a series of International Process Workshops commencing with the first in 1984.General interest had, however, to wait until Osterweil's now classic paper being honoured today and the present author's response were delivered at ICSE 87.This brief paper seeks to move forward from the positions presented then to introduce three process related issues, software process improvement, feedback in the software process and business process improvement.The first is, currently the principal focus of the software process community.The second, it is believed, should be.The third is equally relevant.Individually and collectively these issues appear, to this author at least, to make the majority view of the current focus of process modelling in general and process programming in particular largely irrelevant.

### Software Processes Are Software Too, Revisited: An Invited Talk on the Most Influential Paper of ICSE 9

Leon J. Osterweil · pp. 540–548 · [ACM DL](https://dl.acm.org/doi/10.1145/253228.253440)

> The ICSE 9 paper, "Software Processes are Software Too," suggests that software processes are themselves a form of software and that there are considerable benefits that will derive from basing a discipline of software process development on the more traditional discipline of application software development.This paper attempts to clarify some misconceptions about this original ICSE 9 suggestion and summarizes some research carried out over the past ten years that seems to confirm the original suggestion.The paper then goes on to map out some future research directions that seem indicated.The paper closes with some ruminations about the significance of the controversy that has continued to surround this work.

## 1998 · ICSE 20 {#y1998}

### A Conceptual Model of Software Maintenance

Mira Kajko-Mattsson · pp. 422–425 · [doi:10.1109/ICSE.1998.671597](https://doi.org/10.1109/ICSE.1998.671597)

> Four distinct maintenance systems are studied and synthesised: the SEI quality framework and three industrial systems belonging to ABB, Ellemtel, and Ericsson. The goal is to validate the SEI framework, and to build a "state of the practice" conceptual model of the most fundamental software maintenance concepts. This model can help understand the underlying conditions for managing software maintenance. It can provide guidance to organisations in the process of building or improving their maintenance systems. It also constitutes a common basis for communication, for reasoning about software quality, and for building quality and maintenance models.

### Conceptual Simplicity Meets Organizational Complexity: Case Study of a Corporate Metrics Program

James D. Herbsleb; Rebecca E. Grinter · pp. 271–280 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302190)

> A corporate-wide metrics program faces enormous and poorly understood challenges as its implementation spreads out from the centralized planning body across many organizational boundaries into the sites where the data collection actually occurs. This paper presents a case study of the implementation of one corporate-wide program, focusing particularly on the unexpected difficulties of collecting a small number of straightforward metrics. Several mechanisms causing these difficulties are identified, including attenuated communication across organizational boundaries, inertia created by existing data collection systems, and the perceptions, expectations, and fears about how the data will be used. We describe how these factors influence the interpretation of the definitions of the measurements and influence the degree of conformance that is actually achieved. We conclude with lessons learned about both content and mechanisms to help in navigating the tricky waters of organizational dynamics in implementing a company-wide program.

### Extracting Concepts from File Names: A New File Clustering Criterion

Nicolas Anquetil; Timothy Lethbridge · pp. 84–93 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302172)

> Decomposing complex software systems into conceptually independent subsystems is a significant software engineering activity which received considerable research attention. Most of the research in this domain considers the body of the source code; trying to cluster together files which are conceptually related. We discuss techniques for extracting concepts (abbreviations) from a more informal source of information: file names. The task is difficult because nothing indicates where to split the file names into substrings. In general, finding abbreviations would require domain knowledge to identify the concepts that are referred to in a name and intuition to recognize such concepts in abbreviated forms. We show by experiment that the techniques we propose allow about 90% of the abbreviations to be found automatically.

### Overcoming the NAH Syndrome for Inspection Deployment

Pankaj Jalote; M. Haragopal · pp. 371–378 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302200)

> Despite considerable evidence to show that inspections can help reduce costs and improve quality, inspections are not widely deployed in the software industry. One of the likely reasons for this is the "not applicable here (NAH)" syndrome-developers and managers believe that in their environment, inspections will not provide the benefits seen by other organizations. One of the big challenges for deploying inspections is to overcome this syndrome. We describe two experiments that can be conducted, with little effort, in an organization to obtain data from the organization to build a case for inspections. By conducting one of these experiments, we were able to effectively overcome the NAH syndrome in our organization-many developers and managers are now ready to try inspections in their projects. Though the purpose of the experiment was to overcome the syndrome, the data from the experiment also shows how code inspections compare with unit testing in terms of defect detection capability, and the effect of inspections on the overall cost of development.

### The Ramp-Up Problem in Software Projects: A Case Study of How Software Immigrants Naturalize

Susan Elliott Sim; Richard C. Holt · pp. 361–370 · [ACM DL](https://dl.acm.org/doi/10.5555/302163.302199)

> Joining a software development team is like moving to a new country to start employment; the immigrant has a lot to learn about the job, the local customs, and sometimes a new language. In an exploratory case study, we interviewed four software immigrants, in order to characterize their naturalization process. Seven patterns in four major categories were found. In this paper, these patterns are substantiated, and their implications discussed. The lessons learned from this study can be applied equally to improving the naturalization process, and to the formulation of further research questions.

### The Use of Goals to Surface Requirements for Evolving Systems

Annie I. Antón; Colin Potts · pp. 157–166 · [doi:10.1109/ICSE.1998.671112](https://doi.org/10.1109/ICSE.1998.671112)

> This paper addresses the use of goals to surface requirements for the redesign of existing or legacy systems. Goals are widely recognized as important precursors to system requirements, but the process of identifying and abstracting them has not been researched thoroughly. We present a summary of a goal-based method (GBRAM) for uncovering hidden issues, goals, and requirements and illustrate its application to a commercial system, an Intranet-based electronic commerce application, evaluating the method in the process. The core techniques comprising GBRAM are the systematic application of heuristics and inquiry questions for the analysis of goals, scenarios and obstacles. We conclude by discussing the lessons learned through applying goal refinement in the field and the implications for future research.

### Toward Computational Support for Software Process Improvement Activities

Keishi Sakamoto; Kumiyo Nakakoji; Yasunari Takagi; Naoki Niihara · pp. 22–31 · [doi:10.1109/ICSE.1998.671099](https://doi.org/10.1109/ICSE.1998.671099)

> Software organizations and projects need guidance on how to improve software process, not just guidelines on what to improve. Several surveys demonstrate that the Capability Maturity Model (CMM) and ISO-9000 only provide the latter. We report our in-depth analysis on a seventeen-month effort in software process improvement (SPI) at OMRON Corporation. The goal of the analysis was to identify issues and challenges of SPI and to design a step-wise practical method to avoid such problems. Major problems we have found include the lack of shared goal among stakeholders, insufficient understanding of the current progress of SPI efforts, and underutilization of a large amount of complex information generated during SPI. We present the method for software organizations and projects for dealing with the problems, and argue for a knowledge-based SPI support system based on the method.

### Towards Better Software Projects and Contracts: Commitment Specifications in Software Development Projects

Jyrki Kontio; Olli Pitkänen; Reijo Sulonen · pp. 486–489 · [doi:10.1109/ICSE.1998.671612](https://doi.org/10.1109/ICSE.1998.671612)

> Any software development project requires commitments from its participants. These commitments can include money, resources, deadlines, and specified functionality for the end product. The authors have developed a framework and a set of guidelines to support the specification of such commitments. They have evaluated the framework empirically in a series of case studies. The studies indicated that the framework addresses commitment specification issues that are normally not covered in project contracts and that the specification framework was considered beneficial by project representatives.

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
