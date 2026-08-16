# -*- coding: utf-8 -*-
"""Resolve Spotify episode IDs: search candidates, then verify via GET /v1/episodes/{id} (returns show+title)."""
import json, os, re, time, subprocess, urllib.parse
from spotify_creds import get as _creds

CLIENT_ID, CLIENT_SECRET = _creds()
DATA = r"C:\Users\yunqi\ZCodeProject\data"

def token():
    r = subprocess.run(["curl", "-sS", "-m", "15", "-X", "POST", "https://accounts.spotify.com/api/token",
                        "-H", "Content-Type: application/x-www-form-urlencoded",
                        "-d", f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"],
                       capture_output=True, text=True, encoding="utf-8").stdout
    return json.loads(r)["access_token"]

def api(url):
    for attempt in range(4):
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

TOK = token()
print("token ok", flush=True)

SHOW_EXPECT = {
    "rih": "Rest Is History", "riclass": "Rest Is Classified", "rip": "Rest Is Politics",
    "rient": "Rest Is Entertainment", "rimoney": "Rest Is Money",
}

def resolve(title_en, show_key, date_hint=None):
    kw = re.sub(r"\bEp \d\b|\(Part \d\)|…|\.\.\.", "", title_en)
    kw = re.sub(r"[^\w\s']", " ", kw)
    kw = re.sub(r"\s+", " ", kw).strip()
    q = urllib.parse.quote(kw[:60])
    j = api(f"https://api.spotify.com/v1/search?q={q}&type=episode&limit=10&market=US")
    cands = [(e.get("id"), e.get("name") or "") for e in (j.get("episodes", {}).get("items", []) or []) if e.get("id")][:5]
    best = None
    for eid, name in cands:
        d = api(f"https://api.spotify.com/v1/episodes/{eid}?market=US")
        sn = (d.get("show") or {}).get("name") or ""
        dn = d.get("name") or ""
        rd = (d.get("release_date") or "")[:4]
        if SHOW_EXPECT[show_key] not in sn:
            continue
        score = sum(1 for w in kw.split()[:5] if w.lower() in dn.lower())
        if date_hint and rd and abs(int(rd) - int(date_hint[:4])) > 2:
            continue
        if score >= 1 and (best is None or score > best[0]):
            best = (score, eid, dn, rd, sn)
        time.sleep(0.25)
    return best

eps = json.load(open(os.path.join(DATA, "episodes.json"), encoding="utf-8"))["episodes"]
DATE_HINT = {"rih_20": "2021"}  # special-case old generic titles
results = []
for e in eps:
    key = e["show"] + "_" + e["number"]
    hint = DATE_HINT.get(key)
    r = resolve(e["title_en"], e["show"], hint)
    if r:
        score, eid, dn, rd, sn = r
        results.append({"title": e["title_en"], "spotify_episode_id": eid,
                        "spotify_url": f"https://open.spotify.com/episode/{eid}",
                        "matched_title": dn, "matched_show": sn, "released": rd})
        print("OK ", e["title_en"][:44], "->", eid, "|", dn[:40], flush=True)
    else:
        results.append({"title": e["title_en"], "spotify_episode_id": None, "spotify_url": None,
                        "matched_title": None, "matched_show": None})
        print("MISS", e["title_en"][:44], flush=True)
    time.sleep(0.3)

json.dump(results, open(os.path.join(DATA, "spotify_episode_lookup.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("DONE")