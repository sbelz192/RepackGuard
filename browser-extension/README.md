# RepackGuard Link Guard (Browser-Erweiterung)

Warnt, **bevor** eine betruegerische Seite laedt. Gegen die Kette des
Mr-Beast-Scams: Ein Link in einer Nachricht (Discord, Mail, Forum) — Klick —
Fake-Casino/Giveaway — Download oder Phishing.

## Was sie tut

- Prueft jede angeklickte URL gegen `data/domains.json` (bekannte Scam-Domains
  und Domain-Muster) und leitet auf eine Warnseite um.
- Heuristik (riskante TLD + Schluesselwort) markiert auffaellige Links in
  **Discord Web** direkt im Chat.
- Zaehlt blockierte Versuche (Popup).
- „Trotzdem oeffnen" ist moeglich, aber bewusst: einmal pro Minute freigeben.

## Was sie nicht tut

- Nichts im Discord-**Desktop-Client** (nur Browser/Web).
- Kein Schutz vor Dateien, die trotzdem geladen und ausgefuehrt werden.
- Keine Pruefung von Inhalten, nur von Domains/Mustern.

## Installieren (Chrome/Edge)

1. `chrome://extensions` oeffnen, „Entwicklermodus" aktivieren.
2. „Entpackte Erweiterung laden“ -> Ordner `browser-extension` waehlen.
3. Test: `https://runicwin.com/claim` aufrufen -> Warnseite erscheint.

## Testen

```sh
node test-rules.js
```

## Mitmachen

Ergaenze Domains/Muster in `data/domains.json` (GitHub-Issue oder PR).
Die Datenbank liegt ggf. spaeter geteilt mit der Desktop-Anwendung neben.
