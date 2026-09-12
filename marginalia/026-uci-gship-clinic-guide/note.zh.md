---
id: marginalia-026
title: 'UCI 校医院使用指南——把 7700 刀的 GSHIP 花在校内'
date: 2026-09-12
published: 2026-09-12
kind: practical-guide(校园医保与校医院实用调研)
sources:
  - '官方一手核验:studenthealth.uci.edu(GSHIP 费用与日期/How to Use/转诊指南 PDF/疫苗/药房/牙科诊所/眼科/专科/价目表 PDF)'
  - '计划文件:Wellfleet Benefits at a Glance 2025-26(29p)、Certificate of Coverage(107p)、Summary of Benefits & Coverage、Wellfleet 过渡信(2025-07)、MetLife Dental 与 Superior Vision Plan Summary、Hinge Health 传单——PDF 已存档'
initial-prompt: '研究生医保 GSHIP 一年 7771 刀,到底包含什么?把小红书上流传的免费/低价服务(开药/定制鞋垫/免费洗牙疫苗/眼镜额度/$10 推拿/康复训练)逐条对照官方文档核实;以"尽量用校内校医院"为前提整理就医路线;每个服务条目附英文专业术语和挂号话术;运动康复各项目(PT/整脊/运动医学/虚拟PT/针灸/骨科)的保险算法逐一拆开。'
agent: ZCode CLI
model: GLM-5.3-Flash (智谱)
issue: 59
---

# UCI 校医院使用指南——把 7700 刀的 GSHIP 花在校内

> 研究生强制参保 GSHIP,2026-27 学年保费 **$7,771.86**,但这笔钱的大部分价值都藏在**校内 Student Health Center(SHC)**里:校内就诊免免赔额、门诊 copay 只有 **$5**、疫苗 100% 免费、牙科洗牙一年两次 $0、整脊(含"推拿"式软组织手法)**$10/次**、还能在校内直接配定制鞋垫。这篇的用法:**先看图 1 弄懂动线(§四),再按自己的诉求查"传说核实"(§三)和"康复专项"(§五),到时候要挂号了翻"术语与话术"(§六)照着说**。全部结论来自官方一手文档(来源清单在文末),英文原文可点链接复核。

## 一、GSHIP 基本盘:钱交给了谁,换了什么

UCI 官方对这套保险的定性:"UC IRVINE SHIP is a **fully-insured, comprehensive** health insurance program … The plan includes **medical, behavioral health, pharmacy, dental and vision benefits**."([GSHIP 主页](https://studenthealth.uci.edu/graduate-insurance/))——注册即自动投保,保费按学季打进 [ZOT 账户](https://studenthealth.uci.edu/graduate-uc-irvine-ship-costs-and-dates-of-coverage/),有等同保险可在截止前 waive。

**保费**:2025-26 年 Graduate 年缴 $6,847.26;**2026-27 涨到 $7,771.86**($2,590.62 × 3 学季),Med 1st Year $8,693.60、Law $8,561.93——"一年 7000 多"就是这么来的。

**2025-26 起承保结构大换血**(2025 年 7 月[官方过渡信](https://studenthealth.uci.edu/files/2025/07/Irvine-Intro-to-Wellfleet-Letter-Student-communication-6.12.25-No-UCIrvine-SHIP-logo.pdf)原文):"UCI has selected **Wellfleet Insurance Company** … **Blue Shield of CA is your PPO Network for services/care in California, and Cigna is your PPO network for services/care outside of California.**"

| 组件 | 管理方 | 网络/入口 |
|---|---|---|
| 医疗 + 行为健康 | Wellfleet(客服 1-877-657-5029) | 加州内 [Blue Shield of CA PPO] · 州外 [Cigna PPO](https://www.mycigna.com/) |
| 药房 | Wellfleet Rx(=ESI 体系,[formulary](http://wellfleetrx.com/students/formularies/)) | 校内药房 + 全美网内药房 |
| 牙科 | [MetLife Dental](https://studenthealth.uci.edu/files/2025/08/UC-Irvine-Dental-Plan-Summary.pdf)(PDP Plus 网,客服 1-800-438-6388) | SHC 牙科诊所在网内 |
| 眼科 | [MetLife / Superior Vision](https://studenthealth.uci.edu/files/2025/08/UC-Irvine-Superior-Vision-Plan-Summary-exp0426.pdf)(客服 1-833-EYE-LIFE) | Costco/LensCrafters/Walmart 等都在网 |

⚠️ 网上还流传的 "Anthem Prudent Buyer / Delta Dental / Blue View Vision" 是换约前的旧信息;现役信息一律以 [studenthealth.uci.edu](https://studenthealth.uci.edu/) 和 2025-26 计划文件为准。

## 二、校医院本体:一栋楼能解决多少事

**地点与时间**:[SHC 主楼](https://www.google.com/maps/search/?api=1&query=Student+Health+Center+501+Student+Health+Irvine+CA+92697)(501 Student Health)周一/二/四/五 8am–5pm、周三 9am–5pm、周六 9am–1pm(季节性);[牙科诊所](https://www.google.com/maps/search/?api=1&query=500+East+Peltason+Drive+Irvine+CA+92697)在斜对面的 Student Health II(500 East Peltason Dr),周一至五 8am–5pm。开车停 [Lot 19A](https://www.google.com/maps/search/?api=1&query=UCI+Lot+19A+Irvine+CA)。官方自述([About Us](https://studenthealth.uci.edu/about-us/)):"staffed with licensed primary care physicians, psychiatrists, licensed clinical social workers, **dentists** … Medical specialists … including **orthopedics/sports medicine** … SHC also offers basic radiology and clinical laboratory services … and an **on-site pharmacy**."

**总入口是 [My Student Chart](https://mystudentchart.uci.edu/)**(UCINetID 登录):约号、续方、传消息给保险部、看账单明细都在这里;电话总机 (949) 824-5301。科室与标准做法:

| 科室/服务 | 能干什么 | SHIP 学生实付 | 怎么约 |
|---|---|---|---|
| [Primary Care](https://studenthealth.uci.edu/primary-care/) | 全科门诊、开化验开药、转诊枢纽 | **$5/次** | Chart 在线约 |
| [Specialty Care·Sports Medicine](https://studenthealth.uci.edu/specialty-care/) | 运动损伤/肌骨痛诊断治疗,"Two board-certified specialists","no referral needed for most visits" | **$5/次** | 直接约 |
| [Specialty Care·Chiropractic](https://studenthealth.uci.edu/specialty-care/) | 整脊、deep tissue/软组织手法、肌贴、**配 custom orthotics** | **$10/次**(30 次/年) | 直接约 |
| [Immunizations](https://studenthealth.uci.edu/immunizations/) | 全套疫苗 + TB 检测 | **$0**(100%) | Chart 约 Vaccine 门诊 |
| [Dental Clinic](https://studenthealth.uci.edu/dental-clinic/) | 洗牙/检查/补牙/拔智齿/夜磨牙垫 | 预防类 **$0**;补牙 20% | (949) 824-5307 |
| [Pharmacy](https://studenthealth.uci.edu/pharmacy/) | 取药、续方、寄到家、白菜价 OTC | 仿制药 **$5**,40+ 种 **$0** | Chart 在线续方 |
| [Clinical Laboratory](https://studenthealth.uci.edu/lab/) / [Radiology](https://studenthealth.uci.edu/radiology/) | 抽血化验、X 光 | SHC 内 100% 覆盖(免赔额豁免) | 医生开单 |
| [Psychiatry & Mental Health](https://studenthealth.uci.edu/psychiatry-mental-health/) | 精神科评估、药物管理 | 门诊 $5 起(按 SBC) | Chart 约;另设免费 [Counseling Center](https://counseling.uci.edu/) |
| [Nutrition](https://studenthealth.uci.edu/nutrition/) | 注册营养师咨询 | 按门诊 | 直接约 |

SHC 没有的:线下 PT、验光配镜、MRI 等复杂影像(转诊出去,见 §五、§六)。**价目表**([Fees for Common Services PDF](https://studenthealth.uci.edu/files/2025/10/AY-2025-2026-UC-Irvine-SHC-Fees-for-Common-Services-v4.pdf))列出每项服务的标准计费价——那是 SHC 向保险收的钱,SHIP 学生只付对应 copay;**就诊当天一律不收钱**,保险结算后(约 2–3 周)自付部分进 [ZOT 账户](https://zotaccount.uci.edu/)。爽约费 Medical $50 / 心理 $60。

## 三、小红书"校园传说"逐条核实

| 传说 | 核实结果 | 关键数字 |
|---|---|---|
| 免费打疫苗 | ✅ 官方原话 | "Vaccines and TB testing are **covered 100%**. There is no office visit copay or coinsurance required, and **referrals are not required**."([疫苗页](https://studenthealth.uci.edu/immunizations/)) |
| 免费洗牙 | ✅ 网内预防类全免 | 洗牙/检查/涂氟各 **2 次/年,100%**;补牙 80%、大件 70%、年度上限 $1,000([MetLife 牙科摘要](https://studenthealth.uci.edu/files/2025/08/UC-Irvine-Dental-Plan-Summary.pdf)) |
| 眼镜有免费额度 | ✅ 但额度是 $120 | 验光 **$10 copay 全包**/年;镜框 **$120 额度 + $25 copay**(指定店 +$25);标准镜片 $25 后全包;隐形 $120 额度([Superior Vision 摘要](https://studenthealth.uci.edu/files/2025/08/UC-Irvine-Superior-Vision-Plan-Summary-exp0426.pdf)) |
| $5/$10 的"推拿" | ⚠️ 真实对应物不同 | **$10 = 整脊 chiropractic copay/次**(30 次/年),其诊疗含 "deep tissue work, soft-tissue therapy";**$5 = 门诊 copay**;独立 massage 不在福利内——Certificate 把 "Manipulation or massage" 定义为 **Physical Therapy 的一种**,只有作为医嘱 PT 的一部分才保 |
| 配定制鞋垫 | ✅ 校内就能配 | SHC 整脊诊所官方服务含 "**custom orthotics**";保险按 Prosthetic & Orthotic Devices 走(处方 + 医疗必需 + pre-cert),网内 **95%**;纯运动防护型不保 |
| 开药便宜 | ✅ 且流程全线上 | 仿制药 **$5/30 天**、[Wellfleet Rx 名单](http://wellfleetrx.com/students/formularies/) 40+ 种 **$0**、ACA 预防药 $0;处方**不需要转诊**;SHC 药房可寄到家(FedEx 2–3 天) |

![SHC 热门服务实付价](../assets/entries/026-uci-gship-clinic-guide/fig2-copay-cards.svg)
*图 1 · SHC 热门服务实付价速查——六张卡片是学生最常用的六项,底部是其他常用价格。数据源:Wellfleet Benefits at a Glance 2025-26 与各官方页面,自绘。*

## 四、钱怎么走:动线、转诊与报销

官方模型([How to Use UC IRVINE SHIP](https://studenthealth.uci.edu/how-to-use-uc-irvine-ship/)):"your health care **starts at Student Health Center (SHC) as we are your primary care provider**"——SHC 就是全体 SHIP 学生的 PCP(家庭医生),这是理解一切规则的钥匙。

![GSHIP 就诊动线](../assets/entries/026-uci-gship-clinic-guide/fig1-journey.svg)
*图 2 · GSHIP 就诊动线——从 SHC 出发的三条路:校内直接解决 / 校外专科(必须转诊)/ 转诊豁免清单,底部是账单流向。自绘,规则依据 Referral Guidelines PDF 与 Certificate。*

三条硬规则:

1. **50 英里规则**:校园 50 英里内原则上一切先去 SHC;50 英里外(实习/开会/放假在家)仍需转诊但**不必先跑 SHC**——在 Chart 里给 "SHC - Insurance: Referral Request and Other General Inquiries" 发消息办线上授权即可。
2. **豁免清单**:急诊、Urgent Care、药房、牙科、验光配镜、OB-GYN、Winter Break 期间就医,**不需要转诊**;心理健康校外就医需转诊但不受 50 英里约束。
3. **罚则**:Certificate 原文 "if an Insured Student does not obtain a Referral … **We will not pay** for Covered Medical Expenses"——无转诊=整单拒赔;事后补救走 [Retroactive Referral Request Form](https://studenthealth.uci.edu/files/2025/09/Retroactive-Referral-Appeal-Request-Form-2025.pdf)。

**结算流**:SHC 就诊 → SHC 自动向保险理赔 → 保险付款(约 2–3 周)→ 你的 copay/coinsurance 进 ZOT 账户,当天不掏钱。校外网内就医由 provider 直接向保险收账;垫付了才需要自己报销:向 Wellfleet 报账(claims 处理地址 Cigna, PO Box 188061, Chattanooga, TN;[Incurred/Notice/Proof 三条期限都是 90 天](https://studenthealth.uci.edu/files/2025/10/FINAL-2526-UC-Irvine-Grad-Undergrads-SHIP-Cert-combined-w-notices-rev-10.15.25-JR.pdf)),收据与 itemized statement 从 Chart 打印。

主要自付价目(2025-26 计划,详见 [Benefits at a Glance](https://studenthealth.uci.edu/files/2025/10/WEB-2526-UC-Irvine-BGlance-rev-9.17.25-JR.pdf)):SHC/网内门诊 **$5**;Urgent Care $25;急诊 $200(收住院免);住院 $500/次;网内免赔额 $300(**SHC 内一律豁免**);年度自付上限网内 $4,500;境外非急诊 50% 报销(上限 $10,000,另含 medevac $50,000/repatriation $25,000 与 Travel Guard 24 小时援助)。

## 五、运动康复专项:有哪些项目,保险分别怎么算

以"腰突/侧弯/肌肉紧张/拉伤"这类肌骨问题为入口,保险实际给你铺了**七条路**,算法各不相同:

| # | 项目 | 在哪 | 保险怎么算 | 需要转诊? |
|---|---|---|---|---|
| 1 | **Sports Medicine 运动医学门诊** | 校内 SHC | **$5 copay/次**,按门诊计,无次数上限 | **不用**,直接约 |
| 2 | **Chiropractic 整脊**(含软组织手法/肌贴/运动处方) | 校内 SHC | **$10 copay/次,30 次/政策年**(preferred 档;网外社区整脊同价) | 不用 |
| 3 | **定制鞋垫 custom orthotics** | 校内整脊诊所评估取模 | 按 **Prosthetic & Orthotic Devices**:网内 **95%** 报销,单件需 **pre-cert**(预授权),且须"医疗必需 + 医生处方" | 鞋垫处方向接诊医生要 |
| 4 | **社区 PT 物理治疗**(线下康复训练主力) | 校外网内诊所 | preferred 档 **95% 报销**(自付约 5%),**PT/OT/ST 合计 30 次/政策年**;in-network 档 90%(免赔后) | **要**,SHC 开转诊 + Insurance Services 授权 |
| 5 | **Hinge Health 虚拟 PT** | 手机 App | **$0**(计划增值服务),专属 PT 指导训练方案,**不占 30 次额度** | 不用,[hinge.health/wellfleet](https://hinge.health/wellfleet) 自助注册 |
| 6 | **Acupuncture 针灸** | 网内(校内外均可) | **$20 copay/次,30 次/年**,限"医疗必需" | 针灸在校外做需要转诊 |
| 7 | **骨科/外科专科**(含 MRI、手术) | UCI Health 等网内 | 门诊 $5;复杂影像与手术 **pre-cert** 必须提前办 | 要,SHC 转诊 |

两个容易踩的坑:① **massage 本身不是独立福利**——Certificate 定义 "Physical Therapy means … **5. Manipulation or massage**",即手法按摩只有包在医嘱 PT 里才按 PT 算,想"松解肌肉"该约的是整脊($10)而不是找按摩店;② 网外 PT 的 95% 是"preferred(蓝盾 PPO 首选)"档,若你的免赔额($300)还没满足,先自付的部分要不要计入,以 Certificate 对应行与 Wellfleet 客服确认为准——SHC 内的处置则完全无此顾虑。

**常见症状的推荐路线**(按"校内优先"原则):

- **肌肉太紧/久坐肩颈腰背僵**:直接约 **SHC Chiropractic**($10)——评估 + deep tissue/软组织手法 + 拉伸处方;让整脊医生判断是否需要 PT;长期方案叠加 **Hinge Health**($0)。
- **急性拉伤/扭伤(肌肉拉伤 muscle strain、脚踝扭伤 sprain)**:**SHC Sports Medicine**($5,直接约)——诊断、必要時 SHC 拍 X 光(校内 100% 覆盖)、开药、需要康复时由其转诊社区 PT。
- **腰椎间盘突出(腿麻/放射痛)**:先 **Primary Care 或 Sports Medicine**($5)评估红旗征(见 §六疼痛词汇),SHC 拍片 → 转诊社区 PT(95%,30 次/年)做系统康复;保守治疗无效再转骨科(MRI 走 pre-cert)。
- **脊柱侧弯(成人)**:**Sports Medicine/Primary Care**($5)→ SHC X 光量化角度 → 视情况转专科;日常姿势与肌肉失衡管理交给 Chiropractic + Hinge Health。
- **足底筋膜炎/扁平足(顺带鞋垫)**:**Sports Medicine 或 Chiropractic** 诊断 → 整脊诊所直接取模配 **custom orthotics**(鞋垫费 95%,记得让医生开处方 + 走 pre-cert)。

## 六、挂号与术语速查:到了怎么讲

### 6.1 三种挂号渠道

- **[My Student Chart](https://mystudentchart.uci.edu/)**(首选):Appointments → 选类型(Primary Care / Sports Medicine / Chiropractic / Immunization / Gynecology…);转诊请求走 Messages → New message → **"SHC - Insurance: Referral Request and Other General Inquiries"**。
- **电话**:总机 (949) 824-5301;牙科 (949) 824-5307;保险部 (949) 824-2388。
- **紧急**:真急诊直接 911 或 ER($200 copay);不算急诊但当晚很疼 → Urgent Care($25、免转诊)。

### 6.2 全服务术语 + 挂号话术对照表

| 你要做的事 | 专业术语(英文) | 挂号入口 | 电话/Chart 里可以这么说 |
|---|---|---|---|
| 看普通门诊/首次评估 | primary care appointment / PCP visit | Chart → Primary Care | "Hi, I'm a UCI graduate student enrolled in GSHIP. I'd like to schedule a primary care appointment." |
| 看运动损伤/肌骨问题 | sports medicine appointment | Chart → Specialty Care → Sports Medicine | "I sprained my ankle / pulled a muscle working out — can I get a sports medicine appointment?" |
| 松解肌肉/整脊/推拿 | chiropractic appointment;spinal adjustment;soft-tissue / deep-tissue work | Chart → Chiropractic | "I'd like to book a chiropractic visit — I have chronic muscle tightness in my shoulders and lower back." |
| 配定制鞋垫 | custom orthotics (evaluation & fitting) | 同上,整脊诊所 | "I'm interested in custom orthotics — can my visit include an evaluation and casting?" |
| 开 PT 康复转诊 | referral to (community) physical therapy | Chart → Messages → Insurance | "Could you refer me to an in-network physical therapist for lumbar disc herniation rehab?" |
| 打疫苗 | immunization / vaccine appointment | Chart → Immunization | "I need a flu shot and a Tdap booster."(TB 检测 = TB test / QuantiFERON) |
| 洗牙/看牙 | dental cleaning (prophylaxis);dental checkup;filling 补牙;extraction 拔牙 | (949) 824-5307 | "I'd like to schedule a dental cleaning and exam." |
| 配眼镜/验光 | eye exam;prescription glasses;contact lens fitting | [metlife.com/vision](https://www.metlife.com/vision/) 查网后直接约店 | "I'd like to book an eye exam — I have Superior Vision through MetLife."(无需 SHC 转诊) |
| 看眼睛疾病(非验光) | ophthalmologist(眼科医生,处理眼病) | Chart → Insurance 要转诊 | "I have an eye problem (not just a vision check) — I need a referral to an ophthalmologist." |
| 拿药/续药 | prescription (Rx);refill 续方 | Chart → Pharmacy Request | "I'd like to request a refill of my prescription." / "Please send my prescription to the SHC pharmacy." |
| 妇科 | gynecology / OB-GYN visit | Chart → Gynecology | "I'd like to schedule a gynecology appointment."(免转诊) |
| 心理咨询 | counseling;CAPS(Campus 免费咨询中心) vs psychiatry(精神科,开药) | [counseling.uci.edu](https://counseling.uci.edu/) / Chart | "I'd like to schedule a counseling intake appointment." |
| 化验/拍片 | lab work / blood test;X-ray;MRI/CT(需转诊+pre-cert) | 医生开单后校内做 | "Do I need to fast for this blood test?" |
| 急症(不致命) | urgent care | 网内 urgent care 诊所 | "I need to be seen today — I'm going to an in-network urgent care."(留好单据) |
| 真急诊 | emergency room (ER) / call 911 | 最近 ER | "This is an emergency."(回去后按规则回 SHC 随访) |

### 6.3 描述症状的关键词(医生一定会问)

- **疼痛性质**:sharp(刺痛)/ dull or aching(钝痛/酸痛)/ burning(灼痛)/ throbbing(搏动痛)/ stiffness(僵硬)/ **muscle tightness**(肌肉紧绷)/ **muscle strain / pulled muscle**(拉伤)/ **sprain**(韧带扭伤)。
- **放射与麻木**:"The pain **radiates** down my leg"(放射性疼痛)、"I feel **numbness / tingling** in my foot"(麻木/针刺感)——**腰突伴腿麻要说这句**,医生会按神经受压处理。
- **时间规律**:"It's **worse with sitting**"(久坐加重)、"I have **morning stiffness**"(晨僵)、"It comes and goes"(间歇性)/ constant(持续性)、"It's a **flare-up** of an old injury"(旧伤发作)。
- **量化**:"On a scale of 1 to 10, it's about a **5**";**脊柱侧弯 = scoliosis**,**腰椎间盘突出 = lumbar disc herniation(herniated disc)**,**坐骨神经痛 = sciatica**——这三个词直接说,挂号台和医生都秒懂。
- **红旗词(说出来会被优先处理,出现以下情况直接去 ER)**:loss of bowel/bladder control(大小便失禁)、progressive weakness in the legs(下肢进行性无力)、fever with back pain(发热伴腰痛)。

### 6.4 保险词汇(看账单/查福利要用)

copay(每次固定自付)/ deductible(免赔额)/ coinsurance(比例自付)/ out-of-pocket maximum(年度自付上限)/ in-network(网内)/ out-of-network(网外)/ referral(转诊)/ prior authorization 或 pre-cert(预授权)/ claim(理赔)/ EOB(理赔说明单)/ formulary(药品目录)/ Zot account(校园结算账户)。

## 七、链接速查

| 用途 | 入口 |
|---|---|
| 约号/续方/转诊/查账单 | [My Student Chart](https://mystudentchart.uci.edu/) |
| GSHIP 总览/费用/规则 | [GSHIP 主页](https://studenthealth.uci.edu/graduate-insurance/) · [费用](https://studenthealth.uci.edu/graduate-uc-irvine-ship-costs-and-dates-of-coverage/) · [How to Use](https://studenthealth.uci.edu/how-to-use-uc-irvine-ship/) |
| 计划文件 | [Benefits at a Glance](https://studenthealth.uci.edu/files/2025/10/WEB-2526-UC-Irvine-BGlance-rev-9.17.25-JR.pdf) · [Certificate](https://studenthealth.uci.edu/files/2025/10/FINAL-2526-UC-Irvine-Grad-Undergrads-SHIP-Cert-combined-w-notices-rev-10.15.25-JR.pdf) · [SBC](https://studenthealth.uci.edu/files/2025/09/2526-UC-Irvine-Grad-Undergrad-SBC-9.19.25-JR.pdf) · [价目表](https://studenthealth.uci.edu/files/2025/10/AY-2025-2026-UC-Irvine-SHC-Fees-for-Common-Services-v4.pdf) |
| 找网内医生/诊所 | 加州内 Blue Shield PPO 目录(过渡信链接)/ 州外 [mycigna.com](https://www.mycigna.com/) / 牙科 [metlife.com/mybenefits](https://www.metlife.com/mybenefits/) / 眼科 [metlife.com/vision](https://www.metlife.com/vision/) |
| 增值服务 | [Hinge Health 虚拟 PT](https://hinge.health/wellfleet) · [Teladoc 心理](https://www.teladoc.com/wellfleetstudent/) · Nurseline (866) 440-2752 · Wellfleet 客服 (877) 657-5029 · [Wellfleet Rx 药品目录](http://wellfleetrx.com/students/formularies/) |
| 校内电话 | SHC 总机 (949) 824-5301 · 牙科 (949) 824-5307 · 保险部 (949) 824-2388 · 爽约申诉 billing (949) 824-7084 |

## 来源与说明

全部结论核对自官方一手来源:[studenthealth.uci.edu](https://studenthealth.uci.edu/) 各服务页(GSHIP/费用/How to Use/疫苗/药房/牙科/眼科/专科/价目表)与 Wellfleet 2025-26 计划文件(Benefits at a Glance、Certificate of Coverage、SBC、过渡信、MetLife 牙科与 Superior Vision 摘要、Hinge Health 传单)。**注意**:shc.uci.edu 旧站的 Anthem/Delta Dental/Blue View Vision 描述是换约前信息,勿再引用。文中价格均为 2025-26 计划年(eff. 2025-09-22 至 2026-09-20),2026 年秋季注册后应在 [wellfleetstudent.com](https://www.wellfleetstudent.com/) 复核当年文件;校内实际入账 copay 档位(如整脊 $10)以 Zot 账单为准。
