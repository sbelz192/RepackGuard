#!/usr/bin/env python3
"""
RepackGuard — Domain-DB-Updater.

Holt Kandidaten aus dem URLhaus-Export (abuse.ch) und schreibt sie als
'candidates.json'. Kuratierung ist noetig — das ist KEIN Autopilot fuer die
Blockliste.

URLhaus braucht seit 2026 einen kostenlosen Auth-Key:
    https://urlhaus.abuse.ch/api/  -> "Auth-Key"
Key uebergeben via:
    --key <key>   oder   Umgebungsvariable URLHAUS_AUTH_KEY
    oder Datei     tools/.urlhaus-key
"""
import csv
import io
import json
import os
import re
import sys
import time
import urllib.request

EXPORT = "https://urlhaus-api.abuse.ch/v2/files/exports/{key}/recent.csv"
UA = "RepackGuard-DB-Updater/0.1 (OpenSource)"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "browser-extension", "data", "candidates.json"))

PATTERNS = [
    "repack", "fitgirl", "dodi", "giveaway", "casino", "crypto", "robux",
    "nitro", "mrbeast", "cheat", "crack", "keygen", "freecoin", "airdrop",
]
RISKY_TLDS = [".cc", ".xyz", ".to", ".top", ".site", ".shop", ".live", ".fun"]


def load_key(argv):
    if "--key" in argv:
        return argv[argv.index("--key") + 1]
    if os.environ.get("URLHAUS_AUTH_KEY"):
        return os.environ["URLHAUS_AUTH_KEY"]
    p = os.path.join(HERE, ".urlhaus-key")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    return ""


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def domain_of(url):
    m = re.match(r"(?i)https?://([^/:?#]+)", url or "")
    return m.group(1).lower() if m else ""


def main(argv):
    key = load_key(argv)
    if not key:
        print("Kein URLhaus-Auth-Key vorhanden.")
        print("Kostenlos beantragen: https://urlhaus.abuse.ch/api/  (Auth-Key)")
        print("Dann: python tools/update-db.py --key <key>")
        return 2

    print("Lade URLhaus-Export ...")
    raw = fetch(EXPORT.format(key=key))
    rows = list(csv.DictReader(io.StringIO(raw)))
    print("Eintraege gesamt:", len(rows))

    seen = set()
    candidates = []
    for r in rows:
        url = (r.get("url") or "").strip()
        status = (r.get("url_status") or "").lower()
        tags = (r.get("tags") or "").lower()
        if status and status != "alive":
            continue
        dom = domain_of(url)
        if not dom or dom in seen:
            continue
        if "phishing" not in tags and "malware" not in tags:
            continue
        low = dom.lower()
        pat = [p for p in PATTERNS if p in low]
        tld = "." + low.rsplit(".", 1)[-1]
        risky = tld in RISKY_TLDS
        if not (pat or (risky and any(k in low for k in ("claim", "win", "free")))):
            continue
        seen.add(dom)
        candidates.append({
            "domain": dom, "url": url,
            "threat": r.get("threat") or "", "tags": r.get("tags") or "",
            "reporter": r.get("reporter") or "", "date": r.get("dateadded") or "",
            "reason": ("Muster: " + ",".join(pat)) if pat else ("riskante TLD " + tld),
        })

    candidates.sort(key=lambda c: c["domain"])
    out = {
        "generated": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "source": "urlhaus.abuse.ch v2 export (keyed recent.csv)",
        "count": len(candidates), "kuratiert": False,
        "candidates": candidates,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Kandidaten:", len(candidates), "->", OUT)
    for c in candidates[:15]:
        print("  ", c["domain"], "|", c["reason"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
