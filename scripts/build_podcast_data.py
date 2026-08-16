# -*- coding: utf-8 -*-
"""Build data/ raw files (json+csv) and the blog-style markdown for the Spotify podcast guide."""
import json, os, csv, re, time, html

T = r"C:\Users\yunqi\AppData\Local\Temp"
DATA = r"C:\Users\yunqi\ZCodeProject\data"
os.makedirs(DATA, exist_ok=True)

rss_meta = json.load(open(os.path.join(T, "rss_meta.json"), encoding="utf-8"))

# ---------- shows ----------
S = {}
def reg(k, name, cn, publisher, genre, count, first, sid, status, reason, desc_cn):
    d = rss_meta.get(k, {}).get("desc", "") or ""
    d = html.unescape(html.unescape(d))      # 双重解码（&amp;lt;p&amp;gt; 之类）
    d = re.sub(r'<[^>]+>', ' ', d)           # 去残留标签
    d = re.sub(r'\*+', '', d)                # 去字面 ** 强调符
    d = re.sub(r'\s+', ' ', d).strip()
    S[k] = {"key": k, "name": name, "cn_name": cn, "publisher": publisher, "genre": genre,
            "track_count": count, "first_date": first, "spotify_id": sid, "status": status,
            "reason_cn": reason, "desc_en": d[:700], "desc_cn": desc_cn,
            "desc_official": k not in ("cinephiliacs", "lrb", "sinica", "candidframe")}

reg("rih", "The Rest Is History", "其余皆为历史", "Goalhanger", "History", 973, "2020-10-28", "7Cvsbcjhtur7nplC148TWy", "G",
    "历史顶流对谈；从中国史、冷战到科幻史都做，作者叙事强、信息密度高。",
    "与汤姆·霍兰德、多米尼克·桑德布鲁克一起潜入历史最重要的瞬间：最残暴的统治者、最惨烈的战役与改变世界的事件——从罗马帝国的兴衰、纳粹的征服到冷战，还原权力、阴谋与灾难未被切碎的故事。")
reg("rip", "The Rest Is Politics", "其余皆为政治", "Goalhanger", "Politics", 646, "2022-05-26", "1Ysx8g1Iw42gESAtegrFaH", "G",
    "前工党幕僚长 × 前外交大臣的双视角时政拆解，全球议题与权力内幕。",
    "阿拉斯泰尔·坎贝尔与罗里·斯图尔特拆解英国及全球时政：分析最新国际新闻、辩论全球议题、揭示威斯敏斯特内幕，并复兴一度失传的辩论艺术。")
reg("ripus", "The Rest Is Politics: US", "其余皆为政治：美国版", "Goalhanger", "Politics", 346, "2024-04-23", "1OY3nyGYqjIO4aWMW2feLy", "G",
    "白宫视角的美国政治镜像版，与主节目互补。",
    "（本节目 Spotify 官方简介）揭露白宫核心圈内幕，并俯瞰美国社会肌理与世界最重要经济体的运转。主持：安东尼·斯卡拉穆奇与凯蒂·凯。")
reg("riplead", "The Rest Is Politics: Leading", "其余皆为政治：领导者", "Goalhanger", "Politics", 207, "2023-01-13", "0Z0KhuivFm1Ry4WIpWspPv", "G",
    "领导人主题长访谈：权力、人生与领导力哲学。",
    "《其余皆为政治》的延伸系列：坎贝尔与斯图尔特对话政治内外的领导人、知识分子等——从政治内部与外部，谈论人生、领导力，以及引领他们走到今日的那些哲学。")
reg("rient", "The Rest Is Entertainment", "其余皆为娱乐", "Goalhanger", "TV & Film", 391, "2023-11-24", "1mDl2B7a016YRXR2wSBy4T", "G",
    "影视/流媒体/奥斯卡产业内幕，聚会闲聊感十足的行业情报。",
    "理查德·奥斯曼与玛丽娜·海德分享电视、电影与流行文化的内幕知识：什么正热、什么过气，来自两位圈内消息最灵通声音的幕后洞察。")
reg("rimoney", "The Rest Is Money", "其余皆为金钱", "Goalhanger", "Politics/Finance", 307, "2023-08-22", "69DL3DIVIJZHpbSEzXs0Kc", "G",
    "宏观经济/AI 就业/住房/债务——财经硬话题的通俗拆解。",
    "罗伯特·佩斯顿与斯蒂芬·麦戈文带来精到的商业与金融故事：从科技投资到当下的关键挑战与机遇，拆解今天商业世界的复杂性。")
reg("riclass", "The Rest Is Classified", "其余皆为机密", "Goalhanger", "History", 271, "2024-11-27", "1Jn1HIW6I1AQnKVpsJHdEf", "G",
    "前 CIA 分析师 × 资深安全记者的真实谍报故事。",
    "走进间谍、谍报与秘密行动的隐秘世界。曾任中情局分析师、现为间谍小说家的大卫·麦克洛斯基与资深安全记者戈登·科雷拉共同还原真实谍报故事与情报战。")
reg("blankcheck", "Blank Check with Griffin & David", "空白支票（Blank Check）", "Blank Check Productions", "Film Reviews", 467, "2015-10-01", "4zmVd1CGeUCxAAMwGAwsFD", "G",
    "逐位导演全片单位长谈；作者论影迷的福音。",
    "不止是又一个烂片播客：Blank Check 一集集回顾导演的完整作品目录——尤其是那些早期成功换来好莱坞'空白支票'、得以拍摄心血之作的作者导演。每一档系列都深入一位影史最张扬创作者的全部作品。")
reg("filmcomment", "The Film Comment Podcast", "电影评论播客", "Film Comment Magazine", "TV & Film", 597, "2016-06-03", "0Y9HVocBb0mYmuVLO8NahP", "G",
    "美国影评重刊官方播客，影评级深度。",
    "1962 年创刊的《电影评论》五十余年来一直是独立电影写作的家园：深度访谈、批评分析与对全球主流、艺术电影及先锋电影的长篇报道；播客延续这份批判传统。")
reg("purecinema", "Pure Cinema Podcast", "纯粹电影播客", "Elric Kane & Brian Saur", "TV & Film", 272, "2018-02-10", "4xbAl28Rnh9la3khRm09lv", "G",
    "每周新片/老片/邪典/联映片单，补冷门利器。",
    "每周电影播客，由（Shock Waves 的）埃里克·凯恩与（Rupert Pupkin Speaks 影评博客的）布莱恩·绍尔主持：新片、老片、双片连映、邪典电影、影人与片单一应俱全。")
reg("cinephiliacs", "The Cinephiliacs", "影迷学", "Peter Labuza", "Film Interviews", 39, "2017-03-15", "3XRuUQLY8mBIw0zqTsx5JN", "G",
    "学院派影评访谈；'ReWatch'重看经典环节极具价值。（官方简介未取到，此条为概述）",
    "影评人彼得·拉布扎主持的学院派电影对谈：'ReWatch' 环节逐场重看经典作品，并专访影史学者与批评家，硬核电影研究的播客版。")
reg("newbookssts", "New Books in Science, Technology, and Society", "新书：科学·技术·社会", "New Books Network", "Social Sciences", 809, "2016-01-16", "7HXF18K7if2pUE59yGPDX0", "G",
    "STS 学者新书访谈频道，拉图尔/科学知识社会学的英文重镇。",
    "新书网（New Books Network）旗下频道。新书网是一座致力于公共教育的学术音频图书馆；每期由学者与同行专家对谈他们新近发表的研究。")
reg("techwontsaveus", "Tech Won't Save Us", "科技救不了我们", "Paris Marx", "Technology", 357, "2020-01-11", "3UhsI7s4bkH1FcMZI5u9iD", "G",
    "批判科技的政治经济学：数据中心、AI 与平台权力。",
    "硅谷想塑造我们的未来，但我们凭什么让它这么做？每周四，巴黎·马克思与嘉宾一道批判性地审视科技产业、它的大承诺，以及背后的那些人。")
reg("econtalk", "EconTalk", "EconTalk 经济漫谈", "Russ Roberts", "Economics/Ideas", 1062, "2006-03-16", "4M5Gb71lskQ0Rg6e08uQhi", "G",
    "跨学科思想者访谈，科学哲学与 STS 味道浓。",
    "EconTalk：好奇者的对话（Conversations for the Curious），获奖周播节目，主持人是耶路撒冷沙勒姆学院与斯坦福胡佛研究所的罗斯·罗伯茨。嘉宾名单横跨作家、医生、心理学家、历史学家与哲学家。")
reg("philosophybites", "Philosophy Bites", "哲学小咬", "Edmonds & Warburton", "Philosophy", 408, "2007-06-02", "6UmBytzR58EY4hN1jzQG2o", "G",
    "15 分钟哲学访谈，通勤友好；与哲学大家直接对话。",
    "牛津大学（上广中心）大卫·埃德蒙兹与自由哲学家奈杰尔·沃伯顿访谈顶级哲学家，话题覆盖广泛；以此系列为基础已出版两本牛津大学出版社著作。")
reg("pel", "The Partially Examined Life", "半途而废的哲学人生", "Mark Linsenmayer et al.", "Philosophy", 802, "2010-03-11", "1APpUKebKOXJZjoCaCfoVk", "G",
    "几位'想开了'的哲学博士逐段精读原著。",
    "一档由几位曾经立志以哲学为业、后来'想开'了的人制作的播客。每期挑一小段文本，在洞见与插科打诨之间围绕它深聊；不需要哲学背景也能跟上。")
reg("hpwag", "History of Philosophy Without Any Gaps", "无缝哲学史", "Peter Adamson", "Philosophy", 506, "2010-10-25", "5NkIduNOSgSELCYIa4RaNq", "G",
    "按年代'无缝'走完整个哲学史，治史系哲学家的选择。",
    "慕尼黑 LMU 与伦敦国王学院哲学教授彼得·亚当森带你'没有一丝缝隙'地走完哲学史：考察各大哲学家的思想、生平与时代语境。")
reg("betweenthecovers", "Between the Covers", "书页之间", "David Naimon / Milkweed Editions", "Books", 331, "2019-12-14", "0P9Mwj5XvNZxEpkvJrjAU6", "G",
    "当代文学深度访谈；作家常客是村上、石黑、韩江级。",
    "作家大卫·奈蒙主持的著名文学播客：与今日最富活力的思想家进行慷慨而深入的文学对话，照亮当代写作的复杂性。")
reg("geeksguide", "Geek's Guide to the Galaxy", "极客银河指南", "David Barr Kirtley / Wired", "Sci-Fi", 623, "2013-01-04", "56AQKnEAl8pkpMeo2KZWyF", "G",
    "科幻作家访谈殿堂：特德·姜、尼尔·盖曼级嘉宾。",
    "主持人、作家大卫·巴尔·柯特利与尼尔·盖曼、乔治·R·R·马丁、玛格丽特·阿特伍德等嘉宾畅谈极客文化——科幻与流行文化访谈的旗舰节目。")
reg("parisreview", "The Paris Review", "巴黎评论", "The Paris Review", "Books", 51, "2018-10-24", "6TydwAwFbh9V9ua1XNsO12", "G",
    "文学季刊最佳访谈/小说/诗歌的有声化。",
    "《巴黎评论》播客带来美国最传奇文学季刊的最佳访谈、小说、随笔与诗歌，以声音重现；与莎伦·欧茨、奥尔加·托卡尔丘克等人的亲密交谈。")
reg("backlisted", "Backlisted", "绝版好书榜", "Backlisted", "Books", 272, "2015-11-30", "1avsCeXhwQOXcNO52VsmZ2", "G",
    "每一集介绍一本被时代遗忘的好书（英式扎实书话）。",
    "自 2015 年起让老书重获新生的文学播客。节目笔记见 backlisted.fm，并可通过 Patreon 支持获取每月额外两期节目。")
reg("historyhit", "Dan Snow's History Hit", "丹·斯诺历史直击", "History Hit", "History", 1640, "2013-01-01", "19ywAHxXEhulGqF9jS32Kg", "G",
    "每日历史档，二战/中世纪/冷战选题密集。",
    "历史学家丹·斯诺走遍全球讲述历史的决定性时刻：从罗马斗兽场到中国长城，从滑铁卢战场到图坦卡蒙墓。")
reg("longnow", "Long Now", "漫长的当下", "The Long Now Foundation", "Society & Culture", 400, "2014-11-14", "7n1yR56sQ4LRXyEWNZSpN4", "G",
    "长期主义思想演讲：技术哲学、文明尺度。",
    "长期现在基金会是一家致力于培育长期思考与责任的非营利机构：数百场科学家、历史学家、艺术家与企业家的讲座与对话。")
reg("lrb", "The LRB Podcast", "伦敦书评播客", "London Review of Books", "Books", 475, None, "5qp7xVVpV5lavnMcm0zMN1", "G",
    "深度书评与观念批评的英音权威。",
    "（Spotify 页面未能机器核验，采用站内搜索直达）《伦敦书评》杂志的播客：评书、评观念，英国书评界最锋利的声音之一。")
reg("sinica", "Sinica Podcast", "中国纵横", "SupChina / Kaiser Kuo", "China", 557, None, "1QlGMoMsAncoBdH9Uz5u4N", "G",
    "英文世界看中国的深度访谈节目。",
    "（官方简介概要）SupChina 旗下深度中国政治与社会访谈节目，由资深媒体人郭恺（Kaiser Kuo）主持/出品。")
reg("candidframe", "The Candid Frame", "坦率的取景框", "Ibarionex Perello", "Photography", 669, None, "2WiuIilqvFukFTpV86c8ds", "G",
    "摄影访谈：每位摄影师谈自己的创作与观看。",
    "（官方简介概要）摄影师访谈节目：与来自不同领域的摄影师对话，探讨他们的创作实践、想法与观看方式。")

SITES = {"rih": "https://www.therestishistory.com/", "rip": "https://www.therestispolitics.com/", "philosophybites": "https://philosophybites.com/", "pel": "https://partiallyexaminedlife.com/", "backlisted": "https://www.backlisted.fm/", "geeksguide": "https://www.geeksguideshow.com/", "betweenthecovers": "https://milkweed.org/between-the-covers", "candidframe": "https://www.ibarionex.net/thecandidframe", "sinica": "https://www.sinicapodcast.com/"}

# --- merge iTunes meta (apple page / counts / genre) ---
im = {}
if os.path.exists(os.path.join(DATA, "itunes_meta.json")):
    im = json.load(open(os.path.join(DATA, "itunes_meta.json"), encoding="utf-8"))
for k, v in im.items():
    if k in S:
        if v.get("trackCount"): S[k]["track_count"] = v["trackCount"]
        if v.get("genre"): S[k]["genre"] = v["genre"]
        if v.get("publisher"): S[k]["publisher"] = v["publisher"]
        if v.get("apple_url"): S[k]["apple_url"] = v["apple_url"]
for k in S:
    S[k].setdefault("apple_url", "")
    S[k]["official_site"] = SITES.get(k, "")

# ---------- episodes ----------
EP = [
 ("rih", "173", "Chairman Mao & the Cultural Revolution", "毛泽东与文化大革命 ★首推", "2022-04-07", "中国史·革命", "https://podcasts.apple.com/us/podcast/chairman-mao-the-cultural-revolution/id1537788786?i=1000556477944"),
 ("rih", "366", "The Architect of Modern China", "现代中国的建筑师（邓小平时代）", "2023-09-06", "中国史·改革", "https://podcasts.apple.com/us/podcast/the-architect-of-modern-china/id1537788786?i=1000626979385"),
 ("rih", "444", "The First Emperor of China", "中国的第一位皇帝（秦始皇）", "2024-04-28", "中国史·秦", "https://podcasts.apple.com/us/podcast/the-first-emperor-of-china/id1537788786?i=1000652959468"),
 ("rih", "20", "China", "中国（中华文明通史总纲）", "2021-02-04", "中国史·通史", "SEARCH:20 China"),
 ("rih", "412", "Romans in Space: Star Wars, Dune and Beyond...", "太空中的罗马人：星球大战、沙丘与更远", "2024-01-25", "历史×科幻", "https://podcasts.apple.com/us/podcast/romans-in-space-star-wars-dune-and-beyond/id1537788786?i=1000642778501"),
 ("rih", "125", "The CIA", "中央情报局", "2021-11-25", "谍影·冷战", "https://podcasts.apple.com/us/podcast/the-cia/id1537788786?i=1000543009453"),
 ("rih", "92", "Nuclear Weapons", "核武器", "2021-09-01", "冷战·技术", "https://podcasts.apple.com/us/podcast/nuclear-weapons/id1537788786?i=1000534042480"),
 ("rih", "160", "The Fall of the Soviet Union", "苏联解体（普京系列之一）", "2022-03-08", "冷战·俄国", "https://podcasts.apple.com/us/podcast/the-fall-of-the-soviet-union/id1537788786?i=1000553246963"),
 ("rih", "560", "The Golden Age of Japan: Lady Murasaki and the Shining Prince", "日本黄金时代：紫式部与光源氏", "2025-04-27", "日本·文学", "https://podcasts.apple.com/us/podcast/the-golden-age-of-japan-lady-murasaki-and/id1537788786?i=1000704461473"),
 ("rih", "—", "The Beatles: The Band that Changed the World, with Conan O'Brien (Part 1)", "披头士：改变世界的乐队 × 柯南·奥布莱恩（上）", "2025-12-03", "音乐·文化", "https://podcasts.apple.com/us/podcast/the-beatles-the-band-that-changed-the-world-with/id1537788786?i=1000739409015"),
 ("riclass", "184", "The Secret Spy Network: Kim Philby Threatens the Alliance (Ep 2)", "秘密间谍网：金·菲尔比威胁同盟（第 2 集）", "2026-08-12", "谍影·剑桥五杰", "https://podcasts.apple.com/us/podcast/the-secret-spy-network-kim-philby-threatens-the/id1780384916?i=1000781231735"),
 ("riclass", "162", "Argo: How the CIA Made a Movie That Never Existed (Ep 3)", "Argo：中情局如何拍了一部不存在的电影（第 3 集）", "2026-05-31", "谍影×电影", "https://podcasts.apple.com/us/podcast/argo-how-the-cia-made-a-movie-that-never-existed-ep-3/id1780384916?i=1000769066301"),
 ("rip", "556", "The US-China AI Arms Race and Badenoch vs. Rory's Centrism", "中美 AI 军备竞赛 · Badenoch 对 Rory 的中间路线", "2026-07-22", "科技·地缘", "https://podcasts.apple.com/us/podcast/the-us-china-ai-arms-race-and-badenoch-vs-rorys-centrism/id1611374685?i=1000777740303"),
 ("rip", "561", "How Trump's Chaos Keeps Splintering the World Order", "特朗普的混乱如何持续撕裂世界秩序", "2026-08-11", "全球政治", "https://podcasts.apple.com/us/podcast/how-trumps-chaos-keeps-splintering-the-world-order/id1611374685?i=1000782760060"),
 ("rient", "—", "Box Office Battle: Spielberg vs Nolan", "票房大战：斯皮尔伯格 vs 诺兰", "2026-01-13", "电影产业", "https://podcasts.apple.com/us/podcast/box-office-battle-spielberg-vs-nolan/id1718287198?i=1000744872161"),
 ("rient", "—", "The Oscars: Drama, Fallout and Chalamet's Shocker", "奥斯卡：戏剧、余波与查拉梅的震撼", "2026-03-16", "电影产业", "https://podcasts.apple.com/us/podcast/the-oscars-drama-fallout-and-chalamets-shocker/id1718287198?i=1000755574421"),
 ("rimoney", "301", "Why the US won't stop China in the AI race", "为什么美国阻止不了中国在 AI 竞赛中的脚步", "2026-08-02", "科技×经济", "SEARCH:China AI race"),
 ("rimoney", "302", "Can the West bridge the gap with China, India and the BRICs+ nations?", "西方能否弥合与中国、印度及金砖+国家的鸿沟？", "2026-08-05", "全球经济", "https://podcasts.apple.com/us/podcast/can-the-west-bridge-the-gap-with-china/id1703785141?i=1000780145448"),
 # 进阶
 ("rih", "166", "Genghis Khan: Lord of the Mongols", "成吉思汗：蒙元之主", "2022-03-22", "中亚史", "SEARCH:Genghis Khan"),
 ("rih", "277", "Japan: Samurai and Shoguns", "日本：武士与幕府将军", "2022-12-09", "日本·武士", "SEARCH:Samurai and Shoguns"),
 ("rih", "101", "James Bond", "詹姆斯·邦德（007）", "2021-09-27", "谍影×流行", "SEARCH:James Bond"),
 ("rih", "370", "The 1973 Chilean Coup: Allende, Nixon and the CIA (Part 1)", "1973 智利政变：阿连德、尼克松与中情局（上）", "2023-09-20", "冷战·拉美", "SEARCH:Chilean Coup"),
 ("riclass", "174", "The Murder of Litvinenko: Did the British State Hide the Truth? (Ep 6)", "利特维年科之死：英国政府是否掩盖了真相？（第 6 集）", "2026-07-08", "俄谍·投毒", "SEARCH:Litvinenko"),
 ("riclass", "175", "How China Downed a US Spy Plane (Ep 1)", "中国如何击落美国侦察机（第 1 集）", "2026-07-12", "中美·军事", "SEARCH:US Spy Plane"),
 ("rimoney", "297", "How do we reshape our workforce in the AI era?", "我们如何在 AI 时代重塑劳动力？", "2026-07-19", "AI×就业", "SEARCH:AI era workforce"),
 ("rip", "—", "Data Centres vs. Drinking Water: What Matters To Us Most?", "数据中心 vs 饮用水：什么对我们更重要？", "2026-07-30", "STS·基建", "SEARCH:Data Centres Water"),
]
SHOW_CN = {k: v["cn_name"] for k, v in S.items()}
EPISODES = [{"show": k, "show_cn": SHOW_CN[k], "number": n, "title_en": t, "title_cn": c,
             "date": d, "tag": tag, "link": l} for (k, n, t, c, d, tag, l) in EP]


# --- merge per-show picks (non Rest Is) ---
OP = []
if os.path.exists(os.path.join(DATA, "picks_other_resolved.json")):
    OP = json.load(open(os.path.join(DATA, "picks_other_resolved.json"), encoding="utf-8"))
for x in OP:
    EPISODES.append({
        "show": x["show"], "show_cn": SHOW_CN.get(x["show"], x["show"]),
        "number": "—", "title_en": x["title_en"], "title_cn": x["title_cn"],
        "date": x["date"], "tag": x["tag"], "link": "",
        "spotify_episode_id": x.get("spotify_episode_id"),
        "spotify_url": x.get("spotify_url"),
        "spotify_matched_title": x.get("matched_title"),
        "group": "other"})
for e in EPISODES:
    e.setdefault("group", "restis")
    e["show_name"] = S[e["show"]]["name"]

# ---------- write data ----------

# --- merge official API lookups ---
lookup_e = json.load(open(os.path.join(DATA, "spotify_episode_lookup.json"), encoding="utf-8"))
by_title = {x["title"]: x for x in lookup_e}
for e in EPISODES:
    if e.get("group", "restis") != "restis":
        continue
    hit = by_title.get(e["title_en"])
    if hit and hit.get("spotify_episode_id"):
        e["spotify_episode_id"] = hit["spotify_episode_id"]
        e["spotify_url"] = hit["spotify_url"]
        e["spotify_matched_title"] = hit.get("matched_title")
    else:
        e["spotify_episode_id"] = None; e["spotify_url"] = None

json.dump({"generated": time.strftime("%Y-%m-%d"), "shows": list(S.values())},
          open(os.path.join(DATA, "shows.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
json.dump({"generated": time.strftime("%Y-%m-%d"), "episodes": EPISODES},
          open(os.path.join(DATA, "episodes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
with open(os.path.join(DATA, "shows.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["key","name","cn_name","publisher","genre","track_count","first_date","spotify_id","status","reason_cn","desc_en","desc_cn","desc_official","apple_url","official_site"])
    w.writeheader(); [w.writerow({k: (str(v) if v is not None else "") for k, v in row.items()}) for row in S.values()]
with open(os.path.join(DATA, "episodes.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["show","show_name","show_cn","number","title_en","title_cn","date","tag","link","spotify_episode_id","spotify_url","spotify_matched_title","group"])
    w.writeheader(); [w.writerow(row) for row in EPISODES]
print("data files written:", os.listdir(DATA))
print("shows:", len(S), "| episodes:", len(EPISODES))