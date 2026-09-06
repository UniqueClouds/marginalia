# -*- coding: utf-8 -*-
"""2026-09-07 播客增补：The Book Club + The Rest Is Science → data/ 与 artifact.zh.md（幂等）。"""
import json, re, csv, io

BASE = "marginalia/006-podcast-guide"
ART = f"{BASE}/artifact.zh.md"

TBC = dict(key="tbc", name="The Book Club", cn_name="读书会", publisher="Goalhanger",
           genre="Books", track_count=32, first_date="2026-02-17",
           spotify_id="1yQX55n13t1G8CcOhjfy61",
           apple_url="https://podcasts.apple.com/us/podcast/the-book-club/id1876049295?uo=4",
           official_site="https://www.thebookclubhq.com/",
           artwork="https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/13/f3/08/13f30879-5501-0137-b51a-bc75c052a890/mza_17225192423393937631.jpg/100x100bb.jpg",
           reason_cn="《The Rest Is History》的文学支线：一周一书、史家讲书，作者论与历史语境并重——D 组口味的天然延伸。",
           desc_en="The Book Club, hosted by Dominic Sandbrook and Tabitha Syrett, brings the historical context behind famous books to life. Each week, the hosts explore a classic or contemporary title, unpacking the world in which it was written and the story behind its author. This is not your typical literature podcast: The Book Club educates AND entertains, leaving you knowing some of the greatest stories ever told.",
           desc_cn="Dominic Sandbrook 与制作人 Tabitha Syrett 把名著背后的历史语境讲活：每周精读一本经典或当代之作，拆解它诞生的世界与作者的故事。",
           hot=[("7. Frankenstein: Horror, Humanity, and Hubris", "2026-03-30", "玛丽·雪莱《弗兰肯斯坦》",
                 "https://open.spotify.com/episode/7JvbhkZuyNBnWDozeIv7H3"),
                ("10. East Of Eden: Steinbeck, Sin, and Redemption", "2026-04-20", "斯坦贝克《伊甸之东》",
                 "https://open.spotify.com/episode/1WZJ9arxdwvLkgFXsnBcvi"),
                ("14. Beloved: Memory, Morrison, and Modern American Fiction", "2026-05-18", "莫里森《宠儿》",
                 "https://open.spotify.com/episode/7F5jlv1UZhVllPCYORuNQR"),
                ("29. Rebecca: Daphne du Maurier’s Gothic Epic", "2026-08-24", "杜穆里埃《蝴蝶梦》",
                 "https://open.spotify.com/episode/0awJvXMa5QR9uSW2nxY34L")])

TRIS = dict(key="trisci", name="The Rest Is Science", cn_name="其余皆为科学", publisher="Goalhanger",
            genre="Science", track_count=86, first_date="2025-11-25",
            spotify_id="5oLIbjbUqQmSMVSm0qNLge",
            apple_url="https://podcasts.apple.com/us/podcast/the-rest-is-science/id1853007888?uo=4",
            official_site="https://therestis.com/science",
            artwork="https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/b5/7d/0c/b57d0c08-17e6-0ec9-484a-491f759d48b7/mza_3391787018699283273.jpeg/100x100bb.jpg",
            reason_cn="The Rest Is… 家族 2025 年新支线：Hannah Fry × Vsauce 的顶配科普双主持，周二深挖一个大问题、周四 Field Notes 由小物件出发——补足 E 组的科学维度。",
            desc_en="Launching in November 2025, The Rest Is Science explores the forces, patterns, and questions that define the world around us. Hosted by mathematician and broadcaster Professor Hannah Fry and educator Michael Stevens (Vsauce), it invites us to think deeper - to notice what we've overlooked, and to see the familiar through fresh eyes.",
            desc_cn="数学家 Hannah Fry × Vsauce 主理人 Michael Stevens：每周两集，从「湖泊为何不结冰」到「你的大脑如何发明疼痛」，把世界的古怪与美妙一层层拆给你看。",
            hot=[("The Scale of the Universe", "2026-09-02", "宇宙的尺度",
                  "https://open.spotify.com/episode/43Ok2F5FLKWUbkIxrDkolU"),
                 ("Why Lithium Batteries SUCK", "2026-08-02", "锂电池为何糟糕",
                  "https://open.spotify.com/episode/1egyqQz8RuXEXmpqAaElt4"),
                 ("The Audio Illusion That Proves We Don't Experience Reality", "2026-06-28", "证明「知觉≠现实」的听错觉",
                  "https://open.spotify.com/episode/5PcWD2pVOjnR4EFD3Jxgxz"),
                 ("A Paleontology Of The Future: What We Will Leave Behind", "2026-06-21", "未来古生物学：我们会留下什么",
                  "https://open.spotify.com/episode/1K3EN9henEQquXjZagpZiu")])

NEW = [TBC, TRIS]

# ---------- 1. shows.csv（幂等） ----------
csv_text = open(f"{BASE}/data/shows.csv", encoding="utf-8-sig").read()
cols = ["key", "name", "cn_name", "publisher", "genre", "track_count", "first_date",
        "spotify_id", "status", "reason_cn", "desc_en", "desc_cn", "desc_official",
        "apple_url", "official_site"]
if "tbc," not in csv_text:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols)
    for r in NEW:
        w.writerow({**{c: r.get(c, "") for c in cols}, "status": "G", "desc_official": "True"})
    csv_text = csv_text.rstrip("\n") + "\n" + buf.getvalue().rstrip("\n") + "\n"
    open(f"{BASE}/data/shows.csv", "w", encoding="utf-8", newline="").write(csv_text)
    print("shows.csv: +2")

# ---------- 2. shows.json（幂等） ----------
J = f"{BASE}/data/shows.json"
doc = json.load(open(J, encoding="utf-8"))
keys = [x["key"] for x in doc["shows"]]
added = [r for r in NEW if r["key"] not in keys]
if added:
    for r in added:
        doc["shows"].append({**{c: r.get(c, "") for c in cols}, "status": "G", "desc_official": True})
    json.dump(doc, open(J, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("shows.json: +%d" % len(added))

# ---------- 3. top_episodes.json（幂等） ----------
T = f"{BASE}/data/top_episodes.json"
top = json.load(open(T, encoding="utf-8"))
for r in NEW:
    top.setdefault(r["key"], [{"title": t, "date": d, "note": n, "spotify_url": u}
                              for t, d, n, u in r["hot"]])
json.dump(top, open(T, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("top_episodes: synced")

# ---------- 4. artifact.zh.md ----------
s = open(ART, encoding="utf-8").read()

if "52 档节目 / 81 集精选" in s:
    def sub1(old, new):
        global s
        assert old in s, f"锚点缺失: {old[:60]}"
        assert s.count(old) == 1, f"锚点不唯一: {old[:60]}"
        s = s.replace(old, new)

    sub1("英文播客推荐博客 · 52 档节目 / 81 集精选 · 另附每档节目 🔥 热门单集 161 集",
         "英文播客推荐博客 · 54 档节目 / 81 集精选 · 另附每档节目 🔥 热门单集 169 集")
    sub1("上次自动更新：2026-08-22（再增 🎓 社会学组 5 档：Abbott / Uzzi / Lamont 一系 · 全部 52 档节目附 🔥 热门单集）",
         "上次自动更新：2026-09-07（增补 📖 文学组 The Book Club + 🏛️ The Rest Is… 新支线 The Rest Is Science · 全部 54 档节目附 🔥 热门单集）")
    sub1("共 128 集，全部经官方 API 核验", "共 169 集，全部经官方 API 核验")
    sub1("✅ 本版状态：**52/52 节目、81/81 精选单集、161/161 热门单集全部 🟢 官方链接已验证**，无待核验项。",
         "✅ 本版状态：**54/54 节目、81/81 精选单集、169/169 热门单集全部 🟢 官方链接已验证**，无待核验项。")
    sub1('  - "ZCodeProject/data/ —— shows/episodes JSON+CSV、itunes_meta、feed_meta"',
         '  - "2026-09-07 增补批次：文学组 The Book Club（Goalhanger，2026-02 开播）+ The Rest Is… 新支线 The Rest Is Science（2025-11 开播），8 集热门单集经 /v1/shows/{id}/episodes 解析核验"\n  - "ZCodeProject/data/ —— shows/episodes JSON+CSV、itunes_meta、feed_meta"')

    def row(r, group_color):
        def esc(t):
            return t.replace("&", "&amp;")
        hot = "".join(
            f'<div style="margin-top:2px;">{i+1} <a href="{u}" target="_blank" style="color:#12805c;text-decoration:none;">'
            f'{(t[:44] + "…") if len(t) > 46 else t}</a></div>'
            for i, (t, d, n, u) in enumerate(r["hot"]))
        return (
            f'<tr style="border-bottom:1px solid #ececec;background:#FFFFFF;">'
            f'<td style="padding:12px 12px;width:31%;vertical-align:top;">'
            f'<img src="{r["artwork"]}" width="42" height="42" style="border-radius:50%;vertical-align:middle;margin-right:10px;box-shadow:0 1px 4px rgba(0,0,0,.15);">'
            f'<span style="color:#111;font-weight:700;font-size:14.5px;">{esc(r["name"])}</span>'
            f'<span style="color:#888;font-size:12.5px;margin-left:6px;">{r["cn_name"]}</span>'
            f'<div style="font-size:11.5px;color:#888;margin-top:3px;">📦 {esc(r["publisher"])} &nbsp;·&nbsp; 🏷 {r["genre"]} &nbsp;·&nbsp; 🎧 {r["track_count"]} 集 &nbsp;·&nbsp; ✅ 官方链接已验证</div>'
            f'<div style="margin-top:5px;">'
            f'<a href="https://open.spotify.com/show/{r["spotify_id"]}" target="_blank" style="display:inline-block;background:#1DB954;color:#fff;border-radius:14px;padding:2px 11px;font-size:11.5px;font-weight:600;text-decoration:none;margin:2px 5px 2px 0;border:1px solid #1DB954;">'
            f'<img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_White.png" width="13" style="vertical-align:-2px;margin-right:5px;">Spotify</a>'
            f'<a href="{r["apple_url"]}" target="_blank" style="display:inline-block;background:#fff;color:#555;border-radius:14px;padding:2px 11px;font-size:11.5px;font-weight:600;text-decoration:none;margin:2px 5px 2px 0;border:1px solid #fff;">Apple Podcasts</a>'
            f'</div></td>'
            f'<td style="padding:12px 12px;vertical-align:top;">'
            f'<div style="font-size:12.3px;color:#777;line-height:1.55;">{esc(r["desc_en"])}</div>'
            f'<div style="font-size:12.8px;color:#333;line-height:1.6;margin-top:6px;background:#FAFAFA;border-left:3px solid {group_color};padding:6px 10px;border-radius:0 6px 6px 0;">{esc(r["desc_cn"])}</div>'
            f'</td>'
            f'<td style="padding:12px 12px;vertical-align:top;color:#444;font-size:13px;width:22%;line-height:1.6;">{esc(r["reason_cn"])}'
            f'<div style="margin-top:7px;font-size:11.8px;color:#333;line-height:1.6;background:#F7F7F7;border-left:3px solid #1DB954;padding:6px 9px;border-radius:0 6px 6px 0;">'
            f'<b style="color:#111;">🔥 热门单集</b>{hot}</div></td></tr>')

    def add_row(anchor, r):
        i = s.find(f"{{#{anchor}}}")
        assert i > 0, anchor
        seg = s[i:i + 9000]
        th = re.search(r'<thead><tr style="background:(#[0-9A-Fa-f]{6})', seg)
        color = th.group(1) if th else "#5D4037"
        tb = s.find("</tbody>", i)
        assert tb > 0, f"{anchor}: tbody 未找到"
        return tb, row(r, color), color

    tb, tbc_row, c1 = add_row("sec-d", TBC)
    s = s[:tb] + tbc_row + s[tb:]
    print("sec-d row, thead:", c1)
    tb, tris_row, c2 = add_row("sec-e", TRIS)
    s = s[:tb] + tris_row + s[tb:]
    print("sec-e row, thead:", c2)

    # 组简介增补句
    d_i = s.find("{#sec-d}")
    d_seg = s[d_i:s.find("</table>", d_i)]
    m = re.search(r"</div>", d_seg)
    new = ("…<b>2026-09 增补</b>：Goalhanger 文学支线 The Book Club 入驻——Dominic Sandbrook 一周讲透一本书，"
           "从《弗兰肯斯坦》到《蝴蝶梦》。</div>")
    s = s[:d_i] + d_seg[:m.start()] + new + d_seg[m.end():] + s[s.find("</table>", d_i):]

    e_i = s.find("{#sec-e}")
    e_seg = s[e_i:s.find("</table>", e_i)]
    m = re.search(r"</div>", e_seg)
    new = ("…<b>2026-09 增补</b>：家族新支线 The Rest Is Science（Hannah Fry × Vsauce）入列，E 组补上科学维度。</div>")
    s = s[:e_i] + e_seg[:m.start()] + new + e_seg[m.end():] + s[s.find("</table>", e_i):]

    sub1("「TAOP 第 67 期 Abbott 上 → 下 → SSB Lamont 论污名 → NBN 科技工人的社会密码」。",
         "「TAOP 第 67 期 Abbott 上 → 下 → SSB Lamont 论污名 → NBN 科技工人的社会密码」；"
         "<b>书友会线</b>「Frankenstein → East of Eden → Beloved → Rebecca」；"
         "<b>科学支线</b>「The Scale of the Universe → Why Lithium Batteries SUCK → The Audio Illusion」。")
    sub1("| `shows.json` / `shows.csv` | 52 档节目：", "| `shows.json` / `shows.csv` | 54 档节目：")
    sub1("- 52 档节目、81 集单集的 Spotify 官方链接均经官方 API 解析并二次校验",
         "- 54 档节目、81 集单集的 Spotify 官方链接均经官方 API 解析并二次校验"
         "（2026-09-07 增补批次：The Book Club / The Rest Is Science 及其 8 集热门单集经 `/v1/shows/{id}` 与 `/v1/shows/{id}/episodes` 解析）")
    open(ART, "w", encoding="utf-8").write(s)
    print("artifact.zh.md: 计数/增补块/动线/口径 已更新")
else:
    open(ART, "w", encoding="utf-8").write(s)
    print("artifact.zh.md 已是更新后状态")
