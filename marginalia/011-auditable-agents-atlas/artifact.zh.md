---
id: marginalia-011-artifact
title: "Artifact：auditable-agents-atlas 速查版"
date: 2026-08-17
published: 2026-08-17
kind: artifact（制品 / 速查卡）
sources:
  - "本目录 note.zh.md —— 完整系统汇编（约 10k 字，含分节扫描、八条 open gap、与用户研究议程的接点）"
  - "https://github.com/yzhao062/awesome-auditable-ai —— Yue Zhao (USC-FORTIS, PyOD/ADBench 作者) 维护的 curated list，2026-08-17 克隆快照"
initial-prompt: "新的随想笔记，对这个 link 进行一些总结，提炼，已有研究的进展，待研究的内容，等等，系统性汇总。"
agent: ZCode CLI
model: GLM（智谱）
issue: 26
---

# Artifact：10 分钟读懂 `awesome-auditable-ai`

> 配套长篇：[note.zh.md](note.zh.md)。本卡只给"是什么 / 几条数字 / 怎么读 / 留几个洞"。

## 它是什么

Yue Zhao（USC-FORTIS，PyOD 之父）维护的 curated list，标题 **Awesome Auditable AI**。把"AI 智能体的可审计性"重新定义成"可靠性工程 + 决策问责"的合题。一句话命题：**光记日志没用，能从记录里事后重建发生了什么、谁负责、能否撤销，才算可审计；不可靠的 agent 即便记日志也审不了。**

2026-08-17 快照：**188 entries / 9 节 / 132 arXiv 论文 / 87 GitHub repo / 16 standards / 1 framework / 5 篇跨节重列**。README 565 行；自带 `tools/check_links.py` 在每个 PR 跑数据-标题核对，threshold = 1.0（"Part I" 与 "Part II" 相似度 0.995 仍计分歧）；2026-08-17 run 跨 262 destination 零分歧，且把"3 天前还活着、3 天后 404"的 dataset repo 也抓住过。

## 几个不能忽略的数字（来自 README 引言）

- *Towards a Science of AI Agent Reliability* (ICML 2026)：**Agent capability is rising much faster than agent reliability** —— 12 项指标 × 15 个模型证实剪刀差。
- *Who&When* (ICML 2025)：3 种归因方法里最强一种，在 184 个标注失败任务上识别责负 agent **53.5%**、决定性错误步 **14.2%**（取自 127 个多智能体系统日志）。
- *TraceElephant* (ACL 2026)：完整执行轨迹把步级归因从 17% 抬到 30%（相对增益 **76%**）。
- *MITRE ATLAS* v2026.07：新增 AI Agent Tool Poisoning 子技术 AML.T0110.000/.001/.002 与 AML.T0115，共 16 tactics / 101 techniques / 77 sub-techniques。
- *Cloak and Detonate*：自解包打包规避全部 8 个扫描器 >90%，新沙箱审计器捕获 97%。
- *Classifier Context Rot*：Opus 4.6 / GPT 5.4 / Gemini 3.1 在 800K token 后漏检危险动作 **2–30×**。

## 9 节速查（条目量已按 README 表行复核）

| # | 节 | 量 | 主要主张 |
|---|---|---|---|
| 1 | Surveys & Foundations | 8 | 给"可审计"做术语奠基：agent identifier / monitoring / activity logging |
| 2 | Failure Attribution & Diagnosis | ~25 | 自动归因从 100–200 标注轨迹走到 12,326 构造式轨迹（Who&When Pro） |
| 3 | Reliability & Robustness | 11 | pass^k 一致性 + 工具事务化 + 防语义回滚；恢复评测无协议 |
| 4 | Runtime Monitoring & Guardrails | ~28 | 监控器自身成为被攻击面：Adaptive Attacks + Classifier Context Rot + SLEIGHT |
| 5 | Audit Trails & Decision Records | ~19 | framework 5 维（recoverability/coverage/checkability/responsibility/integrity）；**跨供应商 schema 仍缺** |
| 6 | Security Auditing & Scanners | ~23 | MCP/skill supply chain 独立成节：MCPZoo 64,611 servers、9.93% 不一致、40.55% 无鉴权 |
| 7 | Datasets & Benchmarks | ~29 | 含 Evaluation Integrity 子节：BenchJack 219 reward-hacking flaws |
| 8 | Tools & Platforms | ~21 | observability + sandbox + auditing engine；LangSmith `[Managed]` 透明标注闭源 |
| 9 | Standards & Governance | 6 论文 + 16 standards + 1 framework + 1 tool = 24 | 治理工具大体就位（NIST/ISO/EU AI Act/MITRE ATLAS/OWASP/MCP/A2A/C2PA） |

## 8 条 "open gaps"（研究机会，依动手优先级与用户议程接合排开）

1. **跨供应商 decision-record schema** —— OpenTelemetry 只管 trace；Agent-BOM/ActiveGraph/GRADE 各做各的，无人统一 decisions+dependencies+rationale+integrity+responsibility。命中 RT-13 AI slop governance。
2. **MCP / skill supply chain 安全** —— SkillTrace 已到 AUROC 0.938，但 marketplace 上架前无 in-toto attestation / SLSA 类 provenance。命中 RT-12 agent skills。
3. **监控器自身的对抗鲁棒性** —— Adaptive Attacks + Context Rot + SLEIGHT 三路打监控，无独立基准与 monitor-side decision record。
4. **多根因失败归因** —— MP-Bench 已论证单根因基准低估模型能力；Conformal Agent 刚起，给 finite-sample coverage 的归因 step set 值得养。
5. **评测完整性 / benchmark gaming** —— BenchJack 在 8 个基准里近完美得分但没解任何任务；与 AB-slop / 批判数据研究的 puzzle 接口。
6. **成本 × 可靠性 Pareto** —— *AI Agents That Matter* (TMLR 2025) 呼吁 cost-aware；现有 12 指标 + 4 长程指标都不含成本维度。
7. **检测—定位半步问题** —— TelemetrySuffBench 证实 OpenTelemetry 视图检测 F1 99.5–100% 但 step 准确率 ≤0.5%；HINTBench 强模型检测风险但 Strict-F1 <35 定位。检测够、定位不够，是面向审计的下一个瓶颈。
8. **calibrated abstention 升格为新维度** —— AgentAbstain 17 model 最好 59.5% paired、HiL-Bench Ask-F1。这条建议把"何时停止/何时求助"作为可靠性第九维独立评。

## 一处元观察

list 自身是可审计性的自我示范：188 条、9 节、5 篇跨节重列透明化；audit run 名列每个拒绝自动化访问的目标（而非默会算通过）；4 个不审计的目标（自家 badge）也明示。把 curated list 当作"agent 时代的 audit artifact" 范式做，本身就是个研究方法。匹配你 [[corpus-first-research-approach]] 的做法：先获取原样内容（克隆仓库），再做综合。

## 怎么用这份 list

- 找某主题的代表性论文 / 工具：按节查表，每条都标了 venue + links。
- 复跑链接审计：`python tools/check_links.py` → 写到 `LINK-AUDIT.md`。
- 重新点数：`python tools/inventory.py`。
- 贡献新项：`CONTRIBUTING.md` 列收录准则，每项须有 working link，通过同样的 audit。

详细分析、每节内分支、与用户研究议程的更精细接点见 [note.zh.md](note.zh.md)。
