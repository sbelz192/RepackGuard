#!/usr/bin/env python3
"""
RepackGuard — konservative Kuratierung der Kandidaten.

Niemals alles uebernehmen: die Erweiterung blockt Domains HART. Dieses Skript
wendet ein dokumentiertes Regelwerk an und gibt eine begruendete Liste aus.
Ein Mensch prueft sie vor der Uebernahme (domains.json) und vor dem Store-Update.

Regeln:
  A) Legitime Marken (Buchmaecher, Vergleichs-/Hilfe-Seiten) -> IMMER raus.
  B) Uebernahme, wenn Scam-Muster UND (risikoreische TLD ODER Marken-Missbrauch).
  C) Alles andere bleibt Kandidat.
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "browser-extension", "data"))

# Buchmacher- und Branchenmarken: ihre eigenen/Affiliate-Seiten sind legitim.
LEGIT_BRANDS = [
    "bet365", "888casino", "888holdings", "888poker", "leonbets", "leon",
    "ladbrokes", "williamhill", "betsson", "pinnacle", "marathonbet",
    "unibet", "betfair", "pokerstars", "partypoker", "pokerstrategy",
    "askgamblers", "casinomeister", "casinoguru", "gambleaware",
    "begambleaware", "gamstop", "gamcare", "casinogrounds",
    "latestcasinobonuses", "latest-casino", "onlinecasino", "casinoreviews",
    "review", "reviews", "news", "blog",
]

# Tech-/Payment-Marken: ihr Name in einer Fremddomain ist hoechstwahrscheinlich
# Markenmissbrauch (Phishing/Scam) -> Kandidat fuer Uebernahme.
ABUSED_BRANDS = [
    "paypal", "apple", "microsoft", "netflix", "amazon", "steam", "roblox",
    "fortnite", "discord", "metamask", "coinbase", "binance", "trustwallet",
    "ledger", "exodus", "near", "pancakeswap", "uniswap", "aave", "lido",
    "opensea", "kraken", "revolut", "payoneer", "cashapp", "venmo", "irs",
    "chatgpt", "openai", "gemini", "anthropic", "aliexpress", "temu",
    "shein", "alibaba", "spotify", "hulu", "disney", "primevideo",
]

RISK_TLDS = [".xyz", ".top", ".cc", ".site", ".shop", ".live", ".fun",
             ".gq", ".icu", ".tk", ".ml", ".ga", ".cf", ".su", ".link", ".click"]


def _has(low, word):
    return re.search(r"(?<![a-z0-9])" + re.escape(word) + r"(?![a-z0-9])", low) is not None


def main():
    cand = json.load(io.open(os.path.join(DATA, "candidates.json"), encoding="utf-8"))
    take, drop = [], []
    for c in cand["candidates"]:
        d = c["domain"].lower()
        tld = "." + d.rsplit(".", 1)[-1]
        scam = any(_has(d, w) for w in (
            "casino", "cheat", "crack", "keygen", "repack", "robux", "nitro",
            "giftcard", "wallet", "claim", "airdrop", "crypto", "reward",
            "prize", "giveaway", "bet", "slot", "poker", "lotto", "loan",
            "freecoin", "freebit", "hack"))
        if any(b in d for b in LEGIT_BRANDS):
            drop.append((d, "legitime Marke"))
            continue
        if scam and (tld in RISK_TLDS or any(b in d for b in ABUSED_BRANDS)):
            take.append({"domain": d, "reason": c["reason"], "source": c["source"]})
        else:
            drop.append((d, "kein klares Signal (TLD/Marke fehlt)"))
    print("Kandidaten:", cand["count"])
    print("Zur Uebernahme:", len(take))
    print("Abgelehnt:", len(drop))
    print("\n--- ZUR UEBERNAHME (Spot-Check!) ---")
    for x in take:
        print("  ", x["domain"], "|", x["reason"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
