# -*- coding: utf-8 -*-
"""Resolve Spotify episode IDs for the per-show picks (data/picks_other.json)."""
import json, os, re, time, subprocess, urllib.parse
from spotify_creds import get as _creds

CLIENT_ID, CLIENT_SECRET = _creds()
DATA = r"C:\Users\yunqi\ZCodeProject\data"

SHOW_MATCH = {
    "blankcheck": "blank check", "filmcomment": "film comment", "purecinema": "pure cinema",
    "cinephiliacs": "cinephiliac", "newbookssts": "science, technology, and society",
    "techwontsaveus": "tech won't save us", "econtalk": "econtalk",
    "philosophybites": "philosophy bites", "pel": "partially examined",
    "hpwag": "philosophy without any gaps", "betweenthecovers": "between the covers",
    "geeksguide": "geek's guide", "parisreview": "paris review", "backlisted": "backlisted",
    "historyhit": "history hit", "longnow": "long now", "lrb": "lrb", "sinica": "sinica",
    "candidframe": "candid frame",
}

def token():
    r = subprocess.run(["curl", "-sS", "-m", "15", "-X", "POST", "https://accounts.spotify.com/api/token",
                        "-H", "Content-Type: application/x-www-form-urlencoded",
                        "-d", f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"],
                       capture_output=True, text=True, encoding="utf-8").stdout
    return json.loads(r)["access_token"]

def api(url):
    for _ in range(5):
        r = subprocess.run(["curl", "-sS", "-m", "20", "-H", f"Authorization: Bearer {TOK}", url],
                           capture_output=True, text=True, encoding="utf-8").stdout
        try:
            j = json.loads(r)
        except Exception:
            time.sleep(2); continue
        if j.get("error", {}).get("status") in (429, 503):
            time.sleep(6); continue
        return j
    return {}

def resolve(pick):
    show_expect = SHOW_MATCH[pick["show"]]
    kw = re.sub(r"[^\w\s']", " ", pick["title_en"])
    kw = re.sub(r"\s+", " ", kw).strip()
    # 关键词：取标题里较有区分度的词（去掉编号/通用词）
    words = [w for w in kw.split() if w.lower() not in
             ("the", "a", "an", "and", "with", "on", "of", "for", "ep", "tc", "tcf", "ho",
              "part", "one", "w/", "issue", "inside", "review", "special")]
    j = api("https://api.spotify.com/v1/search?q=" + urllib.parse.quote(kw[:60]) +
            "&type=episode&limit=10&market=US")
    cands = [(e.get("id"), e.get("name") or "") for e in (j.get("episodes", {}).get("items", []) or []) if e.get("id")][:6]
    best = None
    for eid, _ in cands:
        d = api(f"https://api.spotify.com/v1/episodes/{eid}?market=US")
        sn = (d.get("show") or {}).get("name") or ""
        dn = d.get("name") or ""
        if show_expect not in sn.lower():
            continue
        score = sum(1 for w in words[:6] if w.lower() in dn.lower())
        if score >= 1 and (best is None or score > best[0]):
            best = (score, eid, dn, sn)
        time.sleep(0.25)
    return best

TOK = token()
picks = json.load(open(os.path.join(DATA, "picks_other.json"), encoding="utf-8"))["picks"]
out = []
for p in picks:
    r = resolve(p)
    if r:
        score, eid, dn, sn = r
        p["spotify_episode_id"] = eid
        p["spotify_url"] = f"https://open.spotify.com/episode/{eid}"
        p["matched_title"] = dn
        p["matched_show"] = sn
        print("OK ", p["show"], "|", p["title_en"][:44], "->", eid, "|", dn[:40], flush=True)
    else:
        p["spotify_episode_id"] = None
        p["spotify_url"] = None
        p["matched_title"] = None
        p["matched_show"] = None
        print("MISS", p["show"], "|", p["title_en"][:44], flush=True)
    out.append(p)
    time.sleep(0.35)
json.dump(out, open(os.path.join(DATA, "picks_other_resolved.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("DONE resolved:", sum(1 for x in out if x.get("spotify_episode_id")), "/", len(out))