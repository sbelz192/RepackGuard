# Firefox Add-ons — Formular-Eingaben (zum Kopieren)

Firefox-AMO ist englischsprachig. **Empfehlung: Englisch** für die Felder nutzen
(Reviewer lesen es, größere Reichweite). Deutsche Varianten liegen als
Alternative dabei.

---

## 1 · Zusammenfassung (Summary, max. 255 Zeichen)

**Englisch (empfohlen):**
```
Warns before fraudulent pages load: fake MrBeast giveaways, fake casinos, repack sites.
```

**Deutsch:**
```
Warnt, bevor betrügerische Seiten laden: falsche Mr-Beast-Giveaways, Fake-Casinos, Repack-Seiten.
```

## 2 · Beschreibung (Description)

**Englisch (empfohlen):**
```markdown
RepackGuard Link Guard warns before a fraudulent page loads.

Behind the MrBeast scam is a simple chain: a message with a link — a click — a
fake casino or giveaway — a download or phishing. The extension recognises known
scam domains and redirects to a warning page before the site is loaded.

Features
- Checks every clicked address against a local scam database
- Shows a warning page instead of the fraudulent site
- Counts blocked attempts locally

Privacy
- No data collection, no telemetry, no tracking
- Page contents are not read or transmitted
- The check runs entirely locally in the browser

Honest limits
- Works in the browser only, not in the Discord desktop client
- Does not protect against files you download and run anyway
- Checks domains, not page contents

RepackGuard does not replace an antivirus — it adds one more warning layer.
```

**Deutsch:**
```markdown
RepackGuard Link Guard warnt, bevor eine betrügerische Seite geladen wird.

Hinter dem Mr-Beast-Scam steckt eine einfache Kette: eine Nachricht mit einem
Link — ein Klick — ein Fake-Casino oder Giveaway — ein Download oder Phishing.
Die Erweiterung erkennt bekannte Scam-Domains und leitet vor dem Laden auf eine
Warnseite um.

Funktionen
- Prüft angeklickte Adressen gegen eine lokale Scam-Datenbank
- Zeigt eine Warnseite statt der betrügerischen Seite
- Zählt blockierte Versuche lokal

Datenschutz
- Keine Datensammlung, keine Telemetrie, kein Tracking
- Seiteninhalte werden nicht gelesen oder übertragen
- Die Prüfung läuft vollständig lokal im Browser

Ehrliche Grenzen
- Nur im Browser, nicht im Discord-Desktop-Client
- Kein Schutz vor Dateien, die trotzdem geladen und ausgeführt werden
- Prüft Domains, keine Seiteninhalte

RepackGuard ersetzt keinen Virenschutz — es ist eine zusätzliche Warnschicht.
```

## 3 · Kategorie (eine auswählen)

`Security & Privacy` (bzw. `Privacy & Security`)

## 4 · Tags (max. 5)

```
scam
phishing
warning
security
link
```

## 5 · Datenschutzerklärung (Privacy Policy URL)

```
https://sbelz192.github.io/RepackGuard/privacy.html
```

## 6 · Support-Website / Homepage (optional)

```
https://github.com/sbelz192/RepackGuard
```

## 7 · Support-E-Mail (optional)

E-Mail-Adresse des Repository-Inhabers.

## 8 · Anmerkungen für die Prüfer (Notes to reviewer)

```
Link Guard blocks navigation to known scam domains. Permissions:
- webNavigation: detect page loads so the warning can be shown before loading
- tabs: open the warning page in the same tab
- storage: store the local block counter
- <all_urls>: the URL check must work for every site
No data leaves the browser. The domain database ships inside the add-on.
```

## 9 · Datenschutz-Fragen des Formulars

| Frage | Antwort |
|---|---|
| Does your add-on collect or transmit data? | **No** |
| Does it require a privacy policy? | Ja — Link oben |
| Single purpose? | Ja: warn before fraudulent pages load |

---

## Wichtig

- Der **Beschreibungstext darf nicht** behaupten, die Erweiterung schütze vor
  allen Betrug — nur vor bekannten Domains.
- **Keine** Versprechungen zu Discord-Desktop schützen.
