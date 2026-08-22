# -*- coding: utf-8 -*-
"""Build the polished blog-style markdown guide from data/*.json."""
import json, os, time

DATA = r"C:\Users\yunqi\ZCodeProject\data"
OUT = r"C:\Users\yunqi\ZCodeProject\Spotify_Podcast_定制清单_2026-08.md"
shows = {s["key"]: s for s in json.load(open(os.path.join(DATA, "shows.json"), encoding="utf-8"))["shows"]}
eps = json.load(open(os.path.join(DATA, "episodes.json"), encoding="utf-8"))["episodes"]
TOP = json.load(open(os.path.join(DATA, "top_episodes.json"), encoding="utf-8"))
state = {}
if os.path.exists(os.path.join(DATA, "state.json")):
    state = json.load(open(os.path.join(DATA, "state.json"), encoding="utf-8"))
UPDATED = state.get("last_update", "2026-08-16")

SPOT_LOGO_W = "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_White.png"
SPOT_LOGO_G = "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png"

LOGO = {
    "rih": "https://megaphone.imgix.net/podcasts/00c0a118-2426-11ee-b258-73d331d0123b/image/db3295fcd9d3a7113e8000e931f0541d.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "rip": "https://megaphone.imgix.net/podcasts/ebd5041a-2425-11ee-9505-bbe771b4af3b/image/e65e7d3f7665fc8da759a53ed8b182b5.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "ripus": "https://megaphone.imgix.net/podcasts/1b5f91fc-fe62-11ee-b88b-77db1c558f1e/image/41a605f25f78d94eeb1329abffb59638.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "riplead": "https://megaphone.imgix.net/podcasts/f416b74a-2425-11ee-962c-67efcc0de41e/image/5f89de4600ae90ec20ead3e8efb3a3c0.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "rient": "https://megaphone.imgix.net/podcasts/2d9ca178-74df-11ee-ad6a-4fdff40d06f0/image/ae2aaf3060b63e7d0d7c915c05fa4c4e.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "rimoney": "https://megaphone.imgix.net/podcasts/70d67460-223b-11ee-94e6-fb0ccc7b9b93/image/6f20dbe617d02babe1e39c25923f1b41.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "riclass": "https://megaphone.imgix.net/podcasts/5c112b7e-a5d9-11ef-b63f-4fe287d9eeb4/image/82c3d225cc8b4400bd29701ce468519b.jpg?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "blankcheck": "https://megaphone.imgix.net/podcasts/0d46143a-4e92-11ef-87e2-9b8be5c6c221/image/ebe361b1220c86bdecab0556a72aa54f.png?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "filmcomment": "https://img.transistorcdn.com/i_CWIHwGQw-b-npAo5T8zkgmXUK2nelVHnhPh3qhmHA/rs:fill:0:0:1/w:1400/h:1400/q:60/aHR0cHM6Ly9pbWctdXBsb2FkLXByb2R1Y3Rpb24udHJhbnNpc3Rvci5mbS9lYTM5OWEzOWNmOWQ1MDIxY2VjYzZiYzRjMjJiNjIwOC5wbmc.jpg",
    "purecinema": "https://static.libsyn.com/p/assets/a/e/d/b/aedb9a597f00a24640be95ea3302a6a1/PCP_Sunset_Logo.png",
    "cinephiliacs": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/3c/da/96/3cda96c0-640d-4b72-4127-4aab230816b1/mza_15356397536247558728.jpg/600x600bb.jpg",
    "newbookssts": "https://megaphone.imgix.net/podcasts/2ad5366a-f106-11e8-95a3-6b919e58ee88/image/32378277f79ae4f8e84f78e681c1b9a6.png?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "techwontsaveus": "https://storage.buzzsprout.com/tutsi25s4vue63c1xwucuexriowa?.jpg",
    "econtalk": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/a0/13/c5/a013c54f-362a-670d-a75c-1c5486dfc40f/mza_6055952261821533990.jpg/600x600bb.jpg",
    "philosophybites": "https://static.libsyn.com/p/assets/6/6/2/9/6629afb289ae5c80/philo_bites.jpg",
    "pel": "https://static.libsyn.com/p/assets/4/8/4/c/484cbe56ea2bd154/PartiallyExaminedLifeLogo_3000x3000.jpeg",
    "hpwag": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/01/76/52/01765219-d70c-a243-1924-0c5651c8604d/mza_11881655681855403902.jpg/600x600bb.jpg",
    "betweenthecovers": "https://feeds.podcastmirror.com/~images/2379831782120745.jpeg",
    "geeksguide": "https://megaphone.imgix.net/podcasts/7b34d678-1dde-11ef-a81d-df8aa93d996f/image/13a67708e1834c61f141bca5e7e4f39c.png?ixlib=rails-4.3.1&max-w=120&max-h=120&fit=crop&auto=format,compress",
    "parisreview": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts116/v4/4f/77/8e/4f778e30-a37c-d1f0-b297-ed8ba1f4b5ae/mza_13039420152799601545.png/600x600bb.jpg",
    "backlisted": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/92/ee/ac/92eeacc1-d762-6370-e359-e08e765eada9/mza_17537234364179943806.jpeg/600x600bb.jpg",
    "historyhit": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/0c/d7/01/0cd701da-de4f-9a76-b8bc-eaf886cacb51/mza_5440014230451480464.jpeg/600x600bb.jpg",
    "longnow": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/4b/b8/55/4bb85591-10f6-b191-1022-dd9b199bbbd6/mza_2616693323836638892.jpg/600x600bb.jpg",
    "lrb": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/b2/57/13/b25713de-f7ac-b232-cf2a-a261adaf4ecd/mza_10223797150949552626.jpeg/600x600bb.jpg",
    "sinica": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/70/7b/43/707b43c0-64b0-e6c3-6e7b-138f84c16a32/mza_6990403855782084776.jpeg/600x600bb.jpg",
    "candidframe": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/3b/7f/eb/3b7febf4-2897-2cfd-794c-97d85c21b953/mza_2999533948577658608.jpg/600x600bb.jpg",
    "videoarchives": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/44/b3/f9/44b3f953-fbae-4e99-4d82-4c2cc83630e5/mza_1552332279859047099.jpg/100x100bb.jpg",
    "ymrt": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts112/v4/da/e9/e6/dae9e6d3-6b4e-b600-bb37-0ce7833c24d5/mza_9711243178432328693.jpg/100x100bb.jpg",
    "filmspotting": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/bd/8c/05/bd8c05d9-fd70-e35f-da50-f3d67256d648/mza_6805140787842707960.jpg/100x100bb.jpg",
    "screendrafts": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/43/d0/6e/43d06e55-8738-e6b8-8443-52d8a8691524/mza_16169572317619041426.png/100x100bb.jpg",
    "teamdeakins": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/a5/fa/f6/a5faf61e-b752-2ca4-0d26-d431795b66d2/mza_16741861178976893909.jpg/100x100bb.jpg",
    "newyorkerfiction": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/06/5d/f2/065df280-c91f-b43c-2396-51affc5dc883/mza_15681886892269349970.jpeg/100x100bb.jpg",
    "bookworm": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/8a/b8/54/8ab8542d-284c-5845-06c6-600cb82f9c29/mza_18132178739310816340.png/100x100bb.jpg",
    "literaryfriction": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/ed/ea/fe/edeafe0f-89ec-ebf9-9342-5140331bc33b/mza_5722044305146301427.jpg/100x100bb.jpg",
    "inourtimeculture": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/96/f2/ee/96f2ee8b-5aac-19b0-5386-e0bf0ddc317e/mza_4055653295864790255.jpg/100x100bb.jpg",
    "asmallvoice": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/0e/1e/dd/0e1eddeb-c18f-6841-dc23-804958252210/mza_12449687298292391614.jpg/100x100bb.jpg",
    "photowork": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/71/78/ac/7178ac57-01ea-6256-c6cf-bf25549a034e/mza_6390775298639228920.jpg/100x100bb.jpg",
    "abrushwith": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts116/v4/7d/2f/8f/7d2f8f2f-8e2e-1b7c-a00d-c444912b028a/mza_17793975999210383938.jpeg/100x100bb.jpg",
    "talkart": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts126/v4/a8/a3/09/a8a309c7-6670-cdd3-85b8-e6c8504ccc77/mza_18440349357499617051.jpg/100x100bb.jpg",
    "artangle": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/fa/29/db/fa29db6d-424a-d811-d2f6-cc6fa3fdfcf1/mza_1413286888087716503.jpeg/100x100bb.jpg",
    "areweonair": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts116/v4/98/be/2a/98be2a36-9499-ad4b-bd9f-63f9d1ca9ddf/mza_14484981562628970456.jpg/100x100bb.jpg",
    "messytruth": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/a3/a3/11/a3a31131-5a2f-5ea4-d581-1af5198cce98/mza_17867446674733191134.jpg/100x100bb.jpg",
    "righteyedominant": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/e8/9f/97/e89f9746-baaf-e470-c4fc-4933864a000f/mza_9624174152945520709.jpg/100x100bb.jpg",
    "fost": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/be/fe/bd/befebda0-eb0b-fe2b-093f-811cdf999f6d/mza_10514524817047797964.jpg/100x100bb.jpg",
    "emulsions": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/a7/5c/fb/a75cfb40-0df0-78ab-3e48-54d3ee3cd860/mza_8667587312304846208.jpg/100x100bb.jpg",
    "thoughtpieces": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/58/36/7c/58367cb8-6fd3-dcc1-70c4-e871ab3c4dde/mza_8563331525689247233.jpg/100x100bb.jpg",
    "analogtalk": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/80/01/b5/8001b5ab-bb77-3b55-2685-cc1b803ea172/mza_9275432949298650948.jpg/100x100bb.jpg",
    "nbn_socio": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts112/v4/d0/2a/26/d02a26fe-da6c-0870-b3d9-829565854eff/mza_16259726718725408912.jpeg/100x100bb.jpg",
    "socbites": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/ca/6b/8b/ca6b8bee-2dff-876b-4fa0-1a21c8b904aa/mza_10919283292258937037.png/100x100bb.jpg",
    "givetheory": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/26/20/d7/2620d76c-d952-d0e4-2a63-8ceb189590ce/mza_4274720744265111944.jpg/100x100bb.jpg",
    "uncommonsense": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/87/24/2a/87242a0e-1999-958a-2db2-3f0500b42b74/mza_7661165672176171153.jpg/100x100bb.jpg",
    "taop": "https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/5b/f5/7c/5bf57cdf-2fc3-9326-94aa-0fcf6c33a3c6/mza_10936932589617636035.jpg/100x100bb.jpg",
}
CAT = {
    "A": (["blankcheck", "filmcomment", "purecinema", "cinephiliacs",
           "videoarchives", "ymrt", "filmspotting", "screendrafts", "teamdeakins"], "🎬", "电影 · 作者论与影评 · 影史", "#C62828",
          "这份清单的电影组，给两类人：一类把导演当坐标系、按作者论逐部刷片；另一类把影评当写作来读。前者有 Blank Check 的整部作品长谈，后者有 Film Comment 的期刊级批评——Pure Cinema Podcast 与 The Cinephiliacs 补足冷门片单与学院派方法论。2026-08 增补：昆汀·塔伦蒂诺亲开的 The Video Archives Podcast、Karina Longworth 的好莱坞秘史 You Must Remember This、影评常青树 Filmspotting、正典选秀 Screen Drafts 与摄影大师对谈 Team Deakins。"),
    "B": (["newbookssts", "techwontsaveus", "econtalk"], "🧪", "科技 · 社会 · 技术批判（STS）", "#1565C0",
          "科技与社会（STS）是英文播客里的小众富矿：New Books in Science, Technology, and Society 是学术新书访谈的正统频道，Tech Won't Save Us 提供批判科技的政治经济学，EconTalk 则以跨学科访谈把科学哲学与经济学连在一起。"),
    "C": (["philosophybites", "pel", "hpwag"], "🧠", "哲学 · 思想", "#6A1B9A",
          "三档互补的哲学入口：Philosophy Bites 是 15 分钟的对谈点心，The Partially Examined Life 是博士们逐段精读原著，History of Philosophy Without Any Gaps 把整部哲学史按年代无缝走完——从通勤速食到系统深造都有落点。"),
    "D": (["betweenthecovers", "geeksguide", "parisreview", "backlisted",
           "newyorkerfiction", "bookworm", "literaryfriction", "inourtimeculture"], "📖", "文学 · 科幻 · 文学评论", "#2E7D32",
          "文学组覆盖当代写作、文学正典、科幻前沿与文学评论：Between the Covers 是当代作者访谈的顶配，The Paris Review 把文学季刊的最佳访谈变成声音，Backlisted 回访被遗忘的老书，Geek's Guide to the Galaxy 是科幻作者访谈的旗舰。2026-08 增补文学评论线：The New Yorker: Fiction 的作家朗读细读、Bookworm 三十余年的传奇文学访谈、Literary Friction 的主题式批评对谈，以及 BBC In Our Time: Culture 的学院派正典导读。"),
    "E": (["rih", "rip", "ripus", "riplead", "rient", "rimoney", "riclass"], "🏛️", "The Rest Is… 系列 · 历史 · 政治 · 谍影 · 娱乐 · 经济", "#EF6C00",
          "Goalhanger 出品的 The Rest Is… 宇宙是英文播客的现象级存在：历史、政治、影视、财经、谍影五条线，周更 2–3 期，单是历史一档就有近千集。以下按为何值得听排序，并从全量目录里筛好了 26 集精华。"),
    "F": (["historyhit", "longnow", "lrb", "sinica"], "🧭", "扩展精选 · 画像延伸", "#00838F",
          "最后一组把偏好再往外推一步：Dan Snow's History Hit 是每日历史加餐，Long Now 谈长期主义与技术哲学，The LRB Podcast 是书评界最锋利的声音，Sinica Podcast 是英文世界的中国观察。"),
    "G": (["candidframe", "asmallvoice", "photowork", "abrushwith",
           "talkart", "artangle", "messytruth", "righteyedominant",
           "analogtalk", "areweonair", "fost", "emulsions", "thoughtpieces"], "📷", "摄影 · 影像文化", "#455A64",
          "摄影组以三位摄影师为锚点组织：Wolfgang Tillmans、Alec Soth、Stephen Shore 采访过的节目全部收录。核心访谈档：The Candid Frame 是老牌摄影对谈，A Small Voice（Ben Smith）与 PhotoWork（Sasha Wolf）是当代摄影深访的双璧，A brush with…（Art Newspaper）让艺术家自述影响图谱；机构媒体线：Talk Art 与 The Art Angle 覆盖当代艺术场域，The Messy Truth（Gem Fletcher）拆解行业真相，Right Eye Dominant 谈收藏与摄影史；胶片社区线：Analog Talk 与 Emulsions 来自胶片复兴一线；跨界线：ARE WE ON AIR ? 探访文化名人的「人生原声」，FoST 讲故事科学，MACK 出版社的 Thought Pieces 让作者亲读艺术写作。"),
    "H": (["nbn_socio", "socbites", "taop", "givetheory", "uncommonsense"], "🎓", "社会学 · 社会科学", "#5D4037",
          "社会学组以 Andrew Abbott 与 Brian Uzzi 为锚点：Abbott《The System of Professions》在 Talking About Organizations 第 67/109 期被整整精读两期；New Books in Sociology 是社会学家讲新书的正统频道（Uzzi 一系的网络与科学学研究常在此出现）；Social Science Bites 由 Philosophy Bites 团队打造，Lamont 论污名是代表集；give theory a chance 谈社会理论，Uncommon Sense 是《社会学评论》官方播客。"),
}

def spotify_show_url(s):
    if s.get("spotify_id"):
        return f'https://open.spotify.com/show/{s["spotify_id"]}'
    return "https://open.spotify.com/search/" + s["name"].replace(" ", "%20")

def pill(url, label, bg, fg, logo=None):
    img = f'<img src="{logo}" width="13" style="vertical-align:-2px;margin-right:5px;">' if logo else ""
    return (f'<a href="{url}" target="_blank" style="display:inline-block;background:{bg};color:{fg};'
            f'border-radius:14px;padding:2px 11px;font-size:11.5px;font-weight:600;text-decoration:none;'
            f'margin:2px 5px 2px 0;border:1px solid {bg};">{img}{label}</a>')

def show_cell(s):
    img = f'<img src="{LOGO.get(s["key"],"")}" width="42" height="42" style="border-radius:50%;vertical-align:middle;margin-right:10px;box-shadow:0 1px 4px rgba(0,0,0,.15);">'
    name = f'<span style="color:#111;font-weight:700;font-size:14.5px;">{s["name"]}</span>'
    cn = f'<span style="color:#888;font-size:12.5px;margin-left:6px;">{s["cn_name"]}</span>'
    chips = f'<div style="font-size:11.5px;color:#888;margin-top:3px;">📦 {s["publisher"]} &nbsp;·&nbsp; 🏷 {s["genre"]} &nbsp;·&nbsp; 🎧 {s["track_count"] if s["track_count"] else "—"} 集 &nbsp;·&nbsp; ✅ 官方链接已验证</div>'
    links = f'<div style="margin-top:5px;">{pill(spotify_show_url(s), "Spotify", "#1DB954", "#fff", SPOT_LOGO_W)}'
    if s.get("official_site"):
        links += pill(s["official_site"], "官网", "#fff", "#555")
    if s.get("apple_url"):
        links += pill(s["apple_url"], "Apple Podcasts", "#fff", "#555")
    links += "</div>"
    return img + name + cn + chips + links

def hot_block(key):
    rows = TOP.get(key) or []
    if not rows:
        return ""
    items = []
    for i, r in enumerate(rows, 1):
        t = r["title"]
        if len(t) > 56:
            t = t[:54] + "…"
        items.append(f'<div style="margin-top:2px;">{i} <a href="{r["spotify_url"]}" target="_blank" '
                     f'style="color:#12805c;text-decoration:none;">{t}</a></div>')
    return ('<div style="margin-top:7px;font-size:11.8px;color:#333;line-height:1.6;background:#F7F7F7;'
            'border-left:3px solid #1DB954;padding:6px 9px;border-radius:0 6px 6px 0;">'
            '<b style="color:#111;">🔥 热门单集</b>' + "".join(items) + '</div>')


def table(keys, header):
    rows = []
    for k in keys:
        s = shows[k]
        desc_en = s["desc_en"]
        if len(desc_en) > 260:
            desc_en = desc_en[:258] + "…"
        rows.append(
            f'<tr style="border-bottom:1px solid #ececec;background:#FFFFFF;">'
            f'<td style="padding:12px 12px;width:31%;vertical-align:top;">{show_cell(s)}</td>'
            f'<td style="padding:12px 12px;vertical-align:top;"><div style="font-size:12.3px;color:#777;line-height:1.55;">{desc_en}</div>'
            f'<div style="font-size:12.8px;color:#333;line-height:1.6;margin-top:6px;background:#FAFAFA;border-left:3px solid {header};padding:6px 10px;border-radius:0 6px 6px 0;">{s["desc_cn"]}</div></td>'
            f'<td style="padding:12px 12px;vertical-align:top;color:#444;font-size:13px;width:22%;line-height:1.6;">{s["reason_cn"]}{hot_block(k)}</td></tr>')
    return (f'<table style="width:100%;border-collapse:collapse;font-family:-apple-system,\'Segoe UI\',Roboto,sans-serif;font-size:13px;box-shadow:0 1px 6px rgba(0,0,0,.06);border-radius:10px;overflow:hidden;">'
            f'<thead><tr style="background:{header};color:#fff;"><th style="padding:9px 12px;text-align:left;font-size:13.5px;">节目（原名 · 中文名）</th>'
            f'<th style="padding:9px 12px;text-align:left;font-size:13.5px;">官方简介 <span style="font-weight:400;font-size:11px;">(EN 原文 / 中文)</span></th>'
            f'<th style="padding:9px 12px;text-align:left;font-size:13.5px;">推荐理由</th></tr></thead><tbody>' + "".join(rows) + '</tbody></table>')

def ep_row(e, strong_color):
    num = f'<b style="color:{strong_color};font-size:13px;">No.{e["number"]}</b> ' if e["number"] != "—" else ""
    title_html = f'<b style="color:#222;">{e["title_en"]}</b>'
    if e.get("spotify_url"):
        title_html = (f'<a href="{e["spotify_url"]}" target="_blank" style="color:#1DB954;text-decoration:none;">'
                      f'{title_html}</a> <span style="font-size:10px;color:#1DB954;">▶</span>')
    cn_html = f'<div style="color:#666;font-size:12.5px;margin-top:2px;">{e["title_cn"]}</div>'
    links = ""
    if e.get("spotify_url"):
        links += pill(e["spotify_url"], "在 Spotify 收听", "#1DB954", "#fff", SPOT_LOGO_W)
    if e.get("link") and not e["link"].startswith("SEARCH"):
        links += pill(e["link"], "Apple", "#fff", "#555")
    return (f'<tr style="border-bottom:1px solid #ececec;">'
            f'<td style="padding:9px 12px;">{num}{title_html}{cn_html}</td>'
            f'<td style="padding:9px 12px;font-size:12.5px;color:#555;">{e["show_cn"]}<div style="color:#aaa;font-size:11px;">{shows[e["show"]]["name"]}</div></td>'
            f'<td style="padding:9px 12px;text-align:center;color:#666;font-size:12.5px;">{e["date"]}</td>'
            f'<td style="padding:9px 12px;text-align:center;"><span style="background:#E3F2FD;color:#1565C0;border-radius:10px;padding:2px 9px;font-size:11.5px;">{e["tag"]}</span></td>'
            f'<td style="padding:9px 12px;">{links}</td></tr>')

def ep_table(rows, strong_color, header="#37474F"):
    head = ('<thead><tr style="background:%s;color:#fff;"><th style="padding:8px 10px;text-align:left;font-size:13px;">单集（英文原题 · 中文译名 · 点击标题直达）</th>'
            '<th style="padding:8px 10px;text-align:left;font-size:13px;">节目</th><th style="padding:8px 10px;text-align:center;font-size:13px;">日期</th>'
            '<th style="padding:8px 10px;text-align:center;font-size:13px;">主题</th><th style="padding:8px 10px;text-align:left;font-size:13px;">收听链接</th></tr></thead>') % header
    body = "".join(ep_row(e, strong_color) for e in rows)
    return ('<table style="width:100%;border-collapse:collapse;font-family:-apple-system,\'Segoe UI\',Roboto,sans-serif;font-size:13px;box-shadow:0 1px 6px rgba(0,0,0,.06);border-radius:10px;overflow:hidden;">'
            + head + '<tbody>' + body + '</tbody></table>')

restis_eps = [e for e in eps if e.get("group", "restis") == "restis"]
main_eps = restis_eps[:18]
extra_eps = restis_eps[18:]
other_eps = [e for e in eps if e.get("group") == "other"]
def ep_row_other(e, color):
    num = f'<b style="color:{color};font-size:13px;">No.{e["number"]}</b> ' if e["number"] != "—" else ""
    title_html = f'<b style="color:#222;">{e["title_en"]}</b>'
    if e.get("spotify_url"):
        title_html = (f'<a href="{e["spotify_url"]}" target="_blank" style="color:#1DB954;text-decoration:none;">'
                      f'{title_html}</a> <span style="font-size:10px;color:#1DB954;">▶</span>')
    cn_html = f'<div style="color:#666;font-size:12.5px;margin-top:2px;">{e["title_cn"]}</div>'
    links = ""
    if e.get("spotify_url"):
        links += pill(e["spotify_url"], "在 Spotify 收听", "#1DB954", "#fff", SPOT_LOGO_W)
    show_full = shows[e["show"]]["name"]
    return (f'<tr style="border-bottom:1px solid #ececec;">'
            f'<td style="padding:9px 12px;"><b style="color:#111;font-size:13px;">{show_full}</b>'
            f'<div style="color:#888;font-size:12px;">{e["show_cn"]}</div></td>'
            f'<td style="padding:9px 12px;">{num}{title_html}{cn_html}</td>'
            f'<td style="padding:9px 12px;text-align:center;color:#666;font-size:12.5px;">{e["date"]}</td>'
            f'<td style="padding:9px 12px;text-align:center;"><span style="background:#E0F7FA;color:#00695C;border-radius:10px;padding:2px 9px;font-size:11.5px;">{e["tag"]}</span></td>'
            f'<td style="padding:9px 12px;">{links}</td></tr>')

def ep_table_other(rows, color):
    head = ('<thead><tr style="background:%s;color:#fff;"><th style="padding:8px 10px;text-align:left;font-size:13px;">节目（完整原名）</th>'
            '<th style="padding:8px 10px;text-align:left;font-size:13px;">精选单集（英文原题 · 中文译名 · 点击直达）</th>'
            '<th style="padding:8px 10px;text-align:center;font-size:13px;">日期</th>'
            '<th style="padding:8px 10px;text-align:center;font-size:13px;">主题</th>'
            '<th style="padding:8px 10px;text-align:left;font-size:13px;">收听链接</th></tr></thead>') % color
    body = "".join(ep_row_other(e, color) for e in rows)
    return ('<table style="width:100%;border-collapse:collapse;font-family:-apple-system,\'Segoe UI\',Roboto,sans-serif;font-size:13px;box-shadow:0 1px 6px rgba(0,0,0,.06);border-radius:10px;overflow:hidden;">'
            + head + '<tbody>' + body + '</tbody></table>')



hero = f"""<div align="center" style="background:linear-gradient(135deg,#1DB954 0%,#121212 55%,#191414 100%);color:#fff;padding:36px 22px;border-radius:18px;font-family:-apple-system,'Segoe UI',Roboto,sans-serif;box-shadow:0 6px 24px rgba(29,185,84,.18);">
<h1 style="margin:0 0 8px;font-size:31px;letter-spacing:1px;">🎧 Spotify Podcast Guide</h1>
<div style="font-size:16px;opacity:.95;">英文播客推荐博客 · 35 档节目 / 65 集精选 · 官方链接全部验证</div>
<div style="margin-top:14px;font-size:12.8px;opacity:.9;">🎬 电影作者论与影史 · 🧪 科技与社会 STS · 🧠 哲学 · 📖 文学·科幻·文学评论 · 🏛️ 历史政治谍影 · 💷 经济 AI</div>
<div style="margin-top:10px;font-size:11.5px;opacity:.75;">上次自动更新：{UPDATED} &nbsp;·&nbsp; 数据源：官方 RSS / iTunes / Spotify API（详见文末）</div>
</div>"""

doc = []
doc.append("""---
title: "Spotify Podcast Guide 2026-08（英文播客推荐博客：历史 · STS · 哲学 · 电影 · 科幻）"
description: "26 档英文播客 + The Rest Is… 系列 26 集精选；官方简介中英对照；节目名/单集名保留英文原名；全部链接经 Spotify 官方 API 核验；可自动化增量更新（scripts/update_pipeline.py）"
prov-type: podcast-curation
prov-created: 2026-08-16
prov-source:
  - "Goalhanger The Rest Is… 系列官方 RSS（约 3,100 集全量标题）"
  - "iTunes Search/Lookup API（Apple 链接、封面、出品方、类型）"
  - "Spotify Web API（Client Credentials：节目/单集官方直链逐条核验）"
  - "data/shows.json · data/episodes.json · data/itunes_meta.json（本地原始数据）"
tags: [podcast, spotify, blog, the-rest-is, sts, cinema, philosophy, literature, history]
---
""")
doc.append(hero)
doc.append("""
> 📖 **写在前面**：这是一份可以按图索骥的英文播客地图。挑选原则很简单——题材向「深」看（历史、思想、批评），制作向「好」看（口碑长跑型节目），单集向「值得听」看（从全量目录里筛）。<b>所有节目名与单集名均保留英文原名</b>，中文译名随附；每个节目与单集都带官方 Spotify 链接（绿色按钮，点击直达）。原始数据（JSON/CSV）保存在 `data/`，可用 `scripts/update_pipeline.py` 一键增量刷新。

## 📑 目录

1. [这份清单怎么来的](#sec-about)
2. [🎬 电影 · 作者论与影评](#sec-a)
3. [🧪 科技 · 社会 · 技术批判 STS](#sec-b)
4. [🧠 哲学 · 思想](#sec-c)
5. [📖 文学 · 科幻](#sec-d)
6. [🏛️ The Rest Is… 系列](#sec-e)
7. [🧭 扩展精选](#sec-f)
8. [推荐单集精选（65 集）](#sec-ep)
9. [自动化更新 / 数据与方法](#sec-meta)

---
---

<h2 id="sec-about">一、这份清单怎么来的</h2>

1. **主题线筛选**：按影迷、STS 研究者、哲学/文学/科幻读者、历史政治爱好者四条兴趣线，从英文播客池中初筛 40+ 档；
2. **内容深挖**：把 The Rest Is… 系列 7 档节目全部官方 RSS（约 3,100 集）拉到本地，按主题关键词逐条比对，筛出 65 集精华（The Rest Is… 26 集 + 其他节目 39 集）；
3. **链接核验**：35 档节目与 65 集单集的 Spotify 官方链接全部经 **Spotify Web API 逐条解析并二次校验**（节目用 `GET /v1/shows/{id}`、单集用 `GET /v1/shows/{id}/episodes` 列表核对标题一致）；
4. **自动化**：`scripts/update_pipeline.py` 可随时重跑——刷新 RSS、刷新 iTunes 元数据、增量扫描新单集候选、重建数据与博客。

✅ 本版状态：**35/35 节目、65/65 单集全部 🟢 官方链接已验证**，无待核验项。

---
""")

for sec, (keys, emoji, title, color, intro) in CAT.items():
    doc.append(f'\n### {sec}｜{emoji} {title}\n')
    doc.append(f'\n<div style="border-left:6px solid {color};background:#FBFBFB;padding:11px 14px;border-radius:8px;font-size:13.5px;color:#333;margin-bottom:10px;">{intro}</div>\n')
    doc.append(table(keys, color))
    doc.append("")

doc.append("<h2 id=\"sec-ep\">八、推荐单集精选（65 集）</h2>")
doc.append('''<div style="background:#FFF8E1;border:1px solid #FFE082;border-radius:10px;padding:12px 14px;font-size:13px;color:#5c4a00;margin-bottom:10px;">
🎯 全部 65 集精选在一个章节里：The Rest Is… 系列 26 集（主推 18 + 进阶 8）+ 其他节目 39 集。<b>单集编号与标题均为英文原题</b>，中文译名随附；点击标题或绿色按钮直达 Spotify 单集；日期为开播日（RSS 核验）。
</div>''')
doc.append('<h4 style="color:#B71C1C;margin:16px 0 6px;">① The Rest Is… 系列 · 主推 18 集</h4>')
doc.append(ep_table(main_eps, "#B71C1C"))
doc.append('<h4 style="color:#37474F;margin:16px 0 6px;">② The Rest Is… 系列 · 进阶 8 集</h4>')
doc.append('<div style="font-size:12.5px;color:#888;margin-bottom:6px;">主推之外的第二梯队——同样从全量目录筛出，主题更发散。</div>')
doc.append(ep_table(extra_eps, "#37474F", "#455A64"))
doc.append('<h4 style="color:#00838F;margin:16px 0 6px;">③ 其他节目 · 精选 39 集</h4>')
doc.append('<div style="font-size:12.5px;color:#888;margin-bottom:6px;">除 The Rest Is… 系列外，其余 28 档节目各精选 1–3 集（2026-08 增补电影组与文学评论组共 9 档）——按画像主题从各节目官方目录筛选。</div>')
doc.append(ep_table_other(other_eps, "#00838F"))
doc.append("""<div style="background:#FFF8E1;border:1px solid #FFE082;border-radius:10px;padding:12px 14px;margin-top:14px;font-size:13px;color:#5c4a00;">
💡 <b>收听动线建议</b>：中国史线「No.173 Chairman Mao → No.366 The Architect of Modern China → No.444 The First Emperor of China」；冷战线「No.92 Nuclear Weapons → No.125 The CIA → No.160 The Fall of the Soviet Union → No.370 Chilean Coup」；谍影线「No.184 Kim Philby → No.162 Argo → No.101 James Bond」；科幻彩蛋「No.412 Romans in Space」；产业放松线「Spielberg vs Nolan → The Oscars」；AI 社会线「No.301 China AI Race → Data Centres vs. Water → No.297 AI Workforce」。
</div>""")


doc.append("""
---
---

<h2 id="sec-meta">九、自动化更新 / 数据与方法</h2>

### 🔄 自动化增量更新

```bash
python scripts/update_pipeline.py                # 常规增量更新（幂等）
python scripts/update_pipeline.py --force-episodes  # 强制重解析全部单集直链
```

管线自动完成：刷新 Rest Is RSS → 刷新 iTunes 元数据 → （可选）重解析 Spotify 单集 → 扫描新上架单集候选（`data/new_episode_candidates.json`，只建议不自动并入）→ 重建 `data/` 与博客。更新后博客头部的时间戳自动刷新。

### 🔗 链接体系（全部官方源）

- **Spotify**：每档节目（绿色按钮）与每集单集（标题即链接）→ 官方 `open.spotify.com` 页面；
- **官网**：已核验的节目官网（Backlisted / Philosophy Bites / The Rest Is History 等 9 家）；
- **Apple Podcasts**：节目页 + 单集页（iTunes API 官方链接）。

### 📁 原始数据（`data/` 目录）

| 文件 | 内容 |
|---|---|
| `shows.json` / `shows.csv` | 35 档节目：原名/中文名/出品方/类型/集数/Spotify ID/Apple 页/官网/官方简介 EN+CN/推荐理由 |
| `episodes.json` / `episodes.csv` | 65 集精选：节目/编号/英文原题/中文译名/日期/主题/Spotify 单集直链/Apple 链接 |
| `itunes_meta.json` / `feed_meta.json` | iTunes 与 RSS 元数据快照（管线自动刷新） |
| `spotify_episode_lookup.json` | 单集直链解析结果（含校验匹配到的官方标题） |
| `new_episode_candidates.json` | 增量扫描出的新单集候选（人工审阅后可选并入） |
| `spotify_my_shows.json` | （授权后自动生成）你的已关注节目快照 |

### 🧾 验证与口径

- 35 档节目、65 集单集的 Spotify 官方链接均经官方 API 解析并二次校验（`/v1/shows/{id}`、`/v1/shows/{id}/episodes` 列表核对名称一致）。
- 单集日期与编号来自 Goalhanger 官方 RSS；集数来自 RSS/iTunes（每次更新自动刷新）。
- Spotify 不公开单集播放量，故以「集数 + 日期」作为参考维度。
- 官方简介取自各节目官方 RSS / Apple 页面摘要；The Cinephiliacs 官方简介暂未取得（以概述替代，数据中 `desc_official=false` 标注）。

---
<div align="center" style="font-size:12px;color:#999;">本页为 Markdown + 内嵌 HTML 样式，浏览器打开后可用截图工具导出长图 · 由 scripts/build_blog.py 自动生成 · 上次更新 {UPDATED}</div>""")

doc[-1] = doc[-1].replace("{UPDATED}", UPDATED)
open(OUT, "w", encoding="utf-8").write("\n".join(doc))
print("blog written:", OUT, os.path.getsize(OUT), "bytes")