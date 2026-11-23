#!/usr/bin/env python3
"""
RepackGuard — Domain-DB-Updater.

Holt Kandidaten aus oeffentlichen Quellen und schreibt sie als
'candidates.json'. Kuratierung ist noetig — das ist KEIN Autopilot fuer die
Blockliste.

Quellen (bewusst nur klar lizenzierte):
  urlhaus             abuse.ch URLhaus, recent.csv — braucht Auth-Key
  phishing-database   Phishing.Database (MIT), phishing-domains-ACTIVE.txt

Nicht verwendet (Lizenz blockiert Einbettung):
  jarelllama/Scam-Blocklist, hagezi/dns-blocklists  -> GPL-3.0 (Copyleft)
  Phishing Army, OpenPhish                            -> non-commercial-/
                                                   Upstream-Bedingungen
"""
import csv
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

UA = "RepackGuard-DB-Updater/0.2 (OpenSource)"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "browser-extension", "data", "candidates.json"))

URLHAUS_EXPORT = "https://urlhaus-api.abuse.ch/v2/files/exports/{key}/recent.csv"
PHISHDB = ("https://raw.githubusercontent.com/Phishing-Database/"
           "Phishing.Database/master/phishing-domains-ACTIVE.txt")

SOURCES = {
    "urlhaus": {
        "url": URLHAUS_EXPORT, "key": True, "kind": "url",
        "license": "abuse.ch fair-use (free key, non-commercial)",
    },
    "phishing-database": {
        "url": PHISHDB, "key": False, "kind": "domains",
        "license": "MIT (Phishing.Database, Mitchell Krog)",
    },
}

# Scam-Muster — bewusst konservativ. Nur klare Betrugs-Vokabular, keine
# generischen Woerter (sonst blocken wir legitime Seiten).
PATTERNS = [
    "repack", "fitgirl", "dodi", "giveaway", "give-away", "casino", "crypto",
    "robux", "nitro", "mrbeast", "cheat", "crack", "keygen", "freecoin",
    "airdrop", "freeskins", "free-skins", "claim", "prize", "reward",
    "wallet", "giftcard", "gift-card",
]
# Kurze Muster wie "eth"/"btc" fallen bewusst raus: sie treffen Woerter wie
# "methods" oder "object" (False Positives).
RISKY_TLDS = [".cc", ".xyz", ".to", ".top", ".site", ".shop", ".live", ".fun", ".icu", ".gq"]

# Zwei-Teilige TLDs, fuer die eTLD+1 drei Labels braucht.
TWO_PART_TLDS = [
    "co.uk", "org.uk", "ac.uk", "gov.uk", "co.jp", "or.jp", "ne.jp",
    "com.au", "net.au", "org.au", "co.nz", "com.br", "com.mx", "co.za",
    "co.in", "com.tr", "com.cn", "com.tw", "com.sg", "com.hk", "co.kr",
]

# Plattformen/Hosting: hier duerfen Scam-Payloads hausen. Die Plattform selbst
# zu blocken waere eine Katastrophe (False Positives) — also Subdomains filter.
PLATFORMS = [
    "github.com", "githubusercontent.com", "gitlab.com", "gitlab.io", "bitbucket.org",
    "drive.google.com", "googleusercontent.com", "sites.google.com", "dropbox.com",
    "onedrive.live.com", "mediafire.com", "mega.nz", "discord.com", "discordapp.com",
    "discord.gg", "cdn.discordapp.com", "pastebin.com", "tinyurl.com", "bit.ly",
    "t.co", "youtube.com", "youtu.be", "tiktok.com", "facebook.com", "instagram.com",
    "telegram.org", "t.me", "wetransfer.com", "sendspace.com", "4shared.com",
    # Hosting-Baukasten (Phishing.Database ist voller Subdomains dieser Anbieter)
    "weebly.com", "weeblysite.com", "webflow.io", "wixsite.com", "wix.com",
    "squarespace.com", "blogspot.com", "wordpress.com", "wordpress.org",
    "000webhostapp.com", "webnode.at", "jimdo.com", "strikingly.com",
    "cargo.site", "notion.site", "netlify.app", "vercel.app", "pages.dev",
    "firebaseapp.com", "web.app", "azurewebsites.net", "herokuapp.com",
    "repl.co", "neocities.org", "tripod.com", "angelfire.com", "glitch.me",
]

FIELDS = ["id", "dateadded", "url", "url_status", "last_online",
          "threat", "tags", "urlhaus_link", "reporter"]


def load_key(argv):
    if "--key" in argv:
        return argv[argv.index("--key") + 1]
    if os.environ.get("URLHAUS_AUTH_KEY"):
        return os.environ["URLHAUS_AUTH_KEY"]
    p = os.path.join(HERE, ".urlhaus-key")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    return ""


def fetch(url, timeout=180):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        # MinGW-Python hat oft kein CA-Bundle; curl nutzt den System-Store.
        print("  urllib fehlgeschlagen (" + type(e).__name__ + "), nutze curl ...")
        out = subprocess.run(
            ["curl", "-sS", "--fail", "--max-time", str(timeout), "-A", UA, url],
            capture_output=True, text=True, timeout=timeout + 10)
        if out.returncode != 0:
            raise RuntimeError("curl-Fehler: " + (out.stderr or "").strip())
        return out.stdout


def domain_of(url):
    m = re.match(r"(?i)https?://([^/:?#]+)", url or "")
    return m.group(1).lower() if m else ""


def normalize_domain(raw):
    """Bereinigt eine Zeile und liefert die registrierte Domain (eTLD+1)."""
    d = (raw or "").strip().lower()
    # hosts-Format-Reste: "0.0.0.0 domain", "127.0.0.1 domain"
    d = re.sub(r"^(0\.0\.0\.0|127\.0\.0\.1|::|255\.255\.255\.255)\s+", "", d)
    d = d.split()[0] if d.split() else ""
    d = d.strip(".:")
    if not d or "." not in d or d.startswith(".") or d.endswith("."):
        return ""
    labels = d.split(".")
    if len(labels) < 2:
        return ""
    if ".".join(labels[-2:]) in TWO_PART_TLDS:
        take = 3
    else:
        take = 2
    return ".".join(labels[-take:])


def is_platform(dom):
    return any(dom == p or dom.endswith("." + p) for p in PLATFORMS)


def _has(low, pat):
    """Muster mit Wortgrenzen: 'dodi' matcht NICHT 'ofertasdodia'."""
    return re.search(r"(?<![a-z0-9])" + re.escape(pat) + r"(?![a-z0-9])", low) is not None


def reason_for(dom):
    low = dom.lower()
    pat = [p for p in PATTERNS if _has(low, p)]
    tld = "." + low.rsplit(".", 1)[-1]
    risky = tld in RISKY_TLDS and any(_has(low, k) for k in ("claim", "win", "free", "gift"))
    if pat:
        return "Muster: " + ",".join(pat)
    if risky:
        return "riskante TLD " + tld
    return ""


def collect(name, spec, key):
    print("Lade", name, "...")
    raw = fetch(spec["url"].format(key=key) if spec["key"] else spec["url"])
    rows = []
    if spec["kind"] == "url":
        clean = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
        rows = list(csv.DictReader(io.StringIO(clean), fieldnames=FIELDS))
        print("  Eintraege gesamt:", len(rows))
        return rows

    # reine Domainliste (eine Domain pro Zeile, # = Kommentar)
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        rows.append({"url": "", "domain": line, "threat": "phishing",
                     "tags": "", "reporter": "", "dateadded": "",
                     "url_status": "online"})
    print("  Domains gesamt:", len(rows))
    return rows


def main(argv):
    key = load_key(argv)
    wanted = [a for a in argv if not a.startswith("--") and a != key]
    names = wanted or ["urlhaus", "phishing-database"]

    candidates = []
    seen = set()
    stats = {}

    for name in names:
        spec = SOURCES.get(name)
        if not spec:
            print("Unbekannte Quelle:", name, "| verfuegbar:", ", ".join(SOURCES))
            return 2
        if spec["key"] and not key:
            print("Quelle", name, "braucht einen URLhaus-Auth-Key — uebersprungen.")
            print("Kostenlos: https://urlhaus.abuse.ch/api/  (Auth-Key)")
            continue
        try:
            rows = collect(name, spec, key)
        except Exception as e:
            print("  FEHLER bei", name, ":", e)
            continue

        hits = 0
        for r in rows:
            dom = normalize_domain(r.get("domain") or domain_of(r.get("url")))
            if not dom or dom in seen:
                continue
            if is_platform(dom):
                continue
            status = (r.get("url_status") or "online").lower()
            if status not in ("online", "alive", ""):
                continue
            reason = reason_for(dom)
            if not reason:
                continue
            seen.add(dom)
            hits += 1
            candidates.append({
                "domain": dom, "url": r.get("url") or "",
                "source": name, "threat": r.get("threat") or "",
                "tags": r.get("tags") or "", "reporter": r.get("reporter") or "",
                "date": r.get("dateadded") or "", "reason": reason,
            })
        stats[name] = hits

    candidates.sort(key=lambda c: c["domain"])
    out = {
        "generated": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "sources": {n: SOURCES[n]["license"] for n in names},
        "counts": stats,
        "count": len(candidates), "kuratiert": False,
        "candidates": candidates,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Kandidaten gesamt:", len(candidates), "->", OUT)
    print("Pro Quelle:", stats)
    for c in candidates[:20]:
        print("  ", c["domain"], "|", c["reason"], "|", c["source"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
