# Voice: HCI（CHI / CSCW / PACMHCI 工坊体）

基线：94 篇，81.9 万词，2003–2025。报告：`ZCodeProject/学科风格分析_2_HCI.md`。
画像：**兴奋的工坊主持人**——"We present..." 报菜名开场，we 的动词库最丰富，小样本永远 hedge，参与者登记细到报酬，发现折算成 design implications。注意：CHI 内部有批判支线（Bardzell/Irani/Keyes/Dourish 系），其风格偏 bds/dourish——用户点名批判 HCI 时建议改用那两个 voice。

## 目标密度（每千词；voice_check.py --voice hci）

| 指标 | 基线 | 说明 |
|---|---|---|
| 平均句长 | 23.7 词 | 居中；节奏感来自段落切换而非长句 |
| we / our | **9.1 / 3.4** | 工坊集体在说话 |
| we 动词库 | found > conducted > present > describe > argue > observe > report | 实证与论证双轮 |
| hedge: may / might / suggest | **1.66 / 0.76 / 0.88** | 三项四学科第一 |
| In this paper, we | 0.17 | 全库最高频开场公式 |
| this paper | 0.38（this article 仅 0.01） | 会议自称 |
| 弯引号 | 5.1 | 概念+参与者引语都加引号 |
| 问句 | 0.73 | 开场设问与标题问句合法 |
| 缩写词 | 0.27 | 少量（多在引语内） |
| p 值报告 | 5.4/万词（39/94 篇） | 统计为体验主张服务 |

## 词汇场
user(s), participants, design, system, study, findings, implications, affordances, sensemaking, trust, reliance, transparency, human-centered, high-stakes, AI/LLM/XAI（2018 后）。引用：ACM 数字 [n] 高密度内嵌（90/万词），一句话挂 1–3 个方括号是视觉签名。

## 结构仪式
- **摘要公式**：`We present [X/a study of X]... We conducted [N interviews/survey/study]... We found that...`（一句话完成方法+规模+发现）。
- **"revisit" 姿态**：把新数据放进老问题——"This paper revisits the present understanding of X, which originates mostly from..."
- **方法节**：参与者小节逐项登记 N、招募渠道、报酬金额、伦理审查（IRB/informed consent）；引语保真不清洗，编号 P1/P2 引用。
- **三角验证叙事**："First... Second, we conducted a survey to triangulate... Third..."
- **收尾**：Design Implications 小节，把发现翻译给设计者（3–5 条，动词开头）。
- **开场钩子**：新闻语、参与者语录、反问均可；参与者原话可直接做标题。

## 改写配方（H1–H6）

**H1 摘要公式**
- before: "This research studies how people use emoji on WeChat."
- after: "We present a qualitative study of mobile communication via WeChat in Southern China, based on interviews and observations with 30 participants. We find that emoji use..."

**H2 hedge 注入**（一切小样本主张）
- before: "This shows that users prefer AI explanations."
- after: "Our findings suggest that participants may prefer AI explanations when stakes are high (P2, P7)."

**H3 参与者登记句**（方法节首句）
- 模板：`We recruited N participants (F/M, age range) through [渠道], compensated at [金额]; the study was approved by [IRB#].`

**H4 三角验证句**
- 模板：`To triangulate our interview findings, we then conducted a survey with a broader population of X (N=...).`

**H5 design implication 条目**
- 模板：`Designers should [动作] for [人群], so that [体验结果] — echoing our finding that [F#].`

**H6 标题钩子**（冒号前放钩子）
- 问句 / 参与者原话加引号 / 俗语戏仿（"Why Johnny Can't Prompt" 型）/ 交错配列（"Goodbye X, hello Y"）

## 标题公式
55% 含冒号、19% 带引号、24% How/Why 开头；允许第一人称（"Am I wasting my time organizing email?"）。冒号后必须出现研究内容词。

## 反模式（改稿时删除）
- 无 hedge 的强因果主张（"proves""demonstrates that"配小样本）
- 宣言式开场（"X is a form of power."——这是 BDS 的）
- 参与者属性缺失（N、报酬、招募渠道必补）
- 数字统计而无引语、或引语而无编号（双轨证据缺一不可）
- epistemology/assemblage 级抽象词堆叠（批判支线除外）
- "A Study of..." 标题
