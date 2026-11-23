# Datenquellen der Domain-Liste

RepackGuard nutzt ausschließlich **oeffentlich lizenzierte** Quellen. Bei
jeder Übernahme wird die Quelle und Lizenz hier festgehalten.

| Quelle | URL | Lizenz | Aktualisierung |
|---|---|---|---|
| **URLhaus** (abuse.ch) | <https://urlhaus.abuse.ch/api/> | free, fair-use (Free-Key, non-commercial) | alle 5 Minuten |
| **Phishing.Database** (Mitchell Krog) | <https://github.com/Phishing-Database/Phishing.Database> | **MIT** | stündlich |

## Bewusst nicht verwendet

| Quelle | Grund |
|---|---|
| jarelllama/Scam-Blocklist | **GPL-3.0** (Copyleft — würde das MIT-Projekt unter GPL zwingen) |
| hagezi/dns-blocklists | **GPL-3.0** (s. o.) |
| Phishing Army | aggregiert OpenPhish u. a. (non-commercial-Bedingungen der Upstreams) |
| OpenPhish Community-Feed | ausdrücklich **non-commercial** |
| PhishTank | Registrierung derzeit ausgeschaltet (API-Key nötig) |

## Aufbereitung

- Es werden **Domains** (eTLD+1) übernommen, keine vollständigen URLs.
- Hosting-Plattformen (Weebly, Webflow, Netlify, GitHub Pages usw.) werden
  **ausgefiltert** — die Plattform selbst darf nie blockiert werden.
- Muster brauchen **Wortgrenzen** („dodi" darf „ofertasdodia" nicht treffen).
- `candidates.json` ist die **unkuratierte** Rohliste. Die Übernahme in
  `domains.json` erfolgt nur nach Prüfung.

## Aktualisieren

```sh
python3 tools/update-db.py            # URLhaus + Phishing.Database
python3 tools/update-db.py urlhaus    # nur eine Quelle
```

Danach: `candidates.json` prüfen → `domains.json` ergänzen → Version
hochsetzen → Store-Paket neu bauen.
