# -*- coding: utf-8 -*-
"""2026-09 增补:解析 The Book Club / The Rest Is Science 的节目与热门单集官方直链。"""
import sys, json, urllib.request, urllib.parse, base64
sys.path.insert(0, "scripts")
from spotify_creds import get

cid, sec = get()
body = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
req = urllib.request.Request("https://accounts.spotify.com/api/token", data=body, headers={
    "Authorization": "Basic " + base64.b64encode(f"{cid}:{sec}".encode()).decode(),
    "Content-Type": "application/x-www-form-urlencoded"})
TOK = json.loads(urllib.request.urlopen(req, timeout=30).read())["access_token"]
H = {"Authorization": f"Bearer {TOK}"}

PICKS = {
    "1yQX55n13t1G8CcOhjfy61": ([
        "Frankenstein: Horror, Humanity, and Hubris",
        "East Of Eden: Steinbeck, Sin, and Redemption",
        "Beloved: Memory, Morrison",
        "Rebecca: Daphne",
    ], "The Book Club"),
    "5oLIbjbUqQmSMVSm0qNLge": ([
        "The Scale of the Universe",
        "Why Lithium Batteries SUCK",
        "The Audio Illusion That Proves",
        "A Paleontology Of The Future",
    ], "The Rest Is Science"),
}

out = {}
for sid, (picks, expect) in PICKS.items():
    show = json.loads(urllib.request.urlopen(urllib.request.Request(
        f"https://api.spotify.com/v1/shows/{sid}?market=GB", headers=H), timeout=30).read())
    assert show["name"] == expect, (show["name"], expect)
    eps, found = [], {p: None for p in picks}
    url = f"https://api.spotify.com/v1/shows/{sid}/episodes?market=GB&limit=50"
    while url and any(v is None for v in found.values()):
        batch = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=30).read())
        for it in batch.get("items", []):
            if not isinstance(it, dict):
                continue
            e = it.get("item") or it  # 新版 API 单集对象在顶层；受限度播 item 为 None
            if not e.get("name"):
                continue
            name = e["name"].strip()
            for p in picks:
                if found[p] is None and p.lower() in name.lower():
                    found[p] = {"name": name, "date": (e.get("release_date") or "")[:10],
                                "url": e.get("external_urls", {}).get("spotify")}
        url = batch.get("next")
    eps = [v for v in found.values() if v]
    missing = [p for p, v in found.items() if v is None]
    out[expect] = {"spotify_id": sid, "show_name": show["name"], "publisher": (show.get("publisher") or (show.get("show") or {}).get("publisher")),
                   "total_episodes": show["total_episodes"], "hot_episodes": eps, "missing": missing}
    print(expect, "| eps:", show["total_episodes"], "| hot:", len(eps), "| missing:", missing)
    for e in eps:
        print("   -", e["date"], "|", e["name"][:80], "|", e["url"])

json.dump(out, open("podcast_update_2026_09.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved podcast_update_2026_09.json")
