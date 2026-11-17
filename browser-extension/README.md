# RepackGuard Link Guard

Link Guard ist eine Browser-Erweiterung (Chrome, Edge, Firefox), die **warnt,
bevor** eine betrügerische Seite lädt.

Geschützt wird vor der Kette hinter dem Mr-Beast-Scam und ähnlichen
Repack-Infektionen: ein Link in einer Nachricht — Klick —
Fake-Casino/Giveaway — Download oder Phishing.

## Was die Erweiterung tut

- Sie prüft jede angeklickte Adresse gegen `data/domains.json` (bekannte
  Scam-Domains und Domain-Muster) und leitet auf eine Warnseite um.
- Eine Heuristik (riskante Domain-Endung plus Schlüsselwort) markiert
  auffällige Links in **Discord Web** direkt im Chat.
- Blockierte Versuche werden gezählt und im Popup angezeigt.
- „Trotzdem öffnen“ ist möglich, aber bewusst eingeschränkt: einmal pro
  Minute freigebbar.

## Was sie nicht tut

- Sie greift **nicht** im Discord-**Desktop-Client**, nur im Browser.
- Sie schützt nicht vor Dateien, die trotzdem heruntergeladen und ausgeführt
  werden.
- Sie prüft keine Seiteninhalte, nur Domains und Muster.

## Installieren

**Chrome/Edge**

1. `chrome://extensions` öffnen, „Entwicklermodus“ aktivieren.
2. „Entpackte Erweiterung laden“ → Ordner `browser-extension` wählen.
3. Test: `https://runicwin.com/claim` aufrufen — die Warnseite erscheint.

**Firefox**

1. `about:debugging` → „Dieser Firefox“ → „Temporäre Erweiterung laden“.
2. Die Datei `browser-extension/manifest.json` wählen.

## Testen

```sh
node test-rules.js
```

Erwartet: `ALLE OK`.

## Dateien

| Datei | Zweck |
|---|---|
| `manifest.json` | Erweiterungs-Konfiguration (MV3) |
| `background.js` | Prüft Navigationen, leitet bei Alarm um |
| `content.js` | Markiert auffällige Links in Discord Web |
| `shared/rules.js` | Gemeinsame Regel-Engine (auch für zukünftige Bausteine) |
| `data/domains.json` | Blockliste (bekannte Scam-Domains) |
| `data/candidates.json` | Ungeprüfte Kandidaten aus dem URLhaus-Export |
| `warn.html` | Warnseite |

## Mitmachen

Ergänze Domains oder Muster in `data/domains.json` (Issue oder Pull Request).
Die Datenbank wird ggf. später mit der Desktop-Anwendung geteilt.
