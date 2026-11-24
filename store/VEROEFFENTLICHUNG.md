# Veröffentlichung — Stand und Pläne

## Aktueller Stand

| Kanal | Status |
|---|---|
| **Firefox (AMO)** | **live** — [RepackGuard Link Guard](https://addons.mozilla.org/de/firefox/addon/repackguard-link-guard/) |
| **GitHub Releases** | live (v0.1.1 mit Installer + Browser-ZIPs) |
| **Chrome Web Store** | **vorbereitet** — Einreichung gegen Ende Dezember (5 $) |
| Edge Add-ons | nicht geplant |
| Opera Add-ons | optional, nach Chrome (deckt Chromium ohnehin mit ab) |

## Dateien je Kanal

| Zweck | Datei |
|---|---|
| Chrome / Edge | `dist/link-guard-v0.1.1-store.zip` |
| Firefox | `dist/link-guard-firefox-v0.1.1.zip` |
| Chrome-Texte & Formular | `store/CHROME.md` |
| Firefox-Formular | `store/FIREFOX_FORMULAR.md` |
| Datenschutz | `docs/privacy.html` (live unter `sbelz192.github.io/RepackGuard/privacy.html`) |
| Screenshots / Icon | `dist/screenshots/` |

## Reihenfolge

1. **Chrome** (5 $) — deckt Chrome, Edge, Brave, **Opera GX**, Vivaldi ab.
2. Opera-Eigenliste nur, wenn danach noch Bedarf besteht.

## Wichtige Hinweise

- Die Domain-Liste liegt **im ZIP** → jede Änderung braucht ein Store-Update.
- Version im Manifest vor dem Upload prüfen (höher als die live).
- Texte enthalten keine „100 % Schutz"-Versprechungen; Grenzen werden benannt.
- AMO-Prüfer-Notiz für Updates steht in `store/FIREFOX_FORMULAR.md`.
