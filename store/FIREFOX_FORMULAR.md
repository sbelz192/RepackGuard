# Firefox Add-ons — Formular-Eingaben (zum Kopieren)

Die Felder sind **auf Deutsch** geführt (Zielgruppe DACH). Eine englische
Variante liegt am Ende als Alternative.

---

## 1 · Zusammenfassung (Summary, max. 255 Zeichen)

```
Warnt, bevor betrügerische Seiten laden: falsche Mr-Beast-Giveaways, Fake-Casinos, Repack-Seiten.
```

## 2 · Beschreibung (Description)

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

`Sicherheit und Datenschutz` (Security & Privacy)

## 4 · Tags (max. 5)

```
scam
betrug
warnung
sicherheit
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
Link Guard blockiert die Navigation zu bekannten Scam-Domains. Berechtigungen:
- webNavigation: erkennt Seitenaufrufe, damit die Warnung vor dem Laden erscheint
- tabs: öffnet die Warnseite im selben Tab
- storage: speichert die lokale Blockier-Zählung
- <all_urls>: der Adressabgleich muss für alle Seiten möglich sein
Es verlassen keine Daten den Browser. Die Domain-Datenbank liegt in der Erweiterung.
```

## 9 · Datenschutz-Fragen des Formulars

| Frage | Antwort |
|---|---|
| Sammelt oder überträgt die Erweiterung Daten? | **Nein** |
| Benötigt sie eine Datenschutzerklärung? | Ja — Link oben |
| Ein einziger Zweck? | Ja: Warnung vor dem Laden betrügerischer Seiten |

---

## Englische Alternative (falls gewünscht)

**Summary:**
```
Warns before fraudulent pages load: fake MrBeast giveaways, fake casinos, repack sites.
```

**Description:**
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

---

## Wichtig

- Der Beschreibungstext behauptet **nicht**, die Erweiterung schütze vor jedem
  Betrug — nur vor bekannten Domains.
- **Keine** Versprechungen zum Schutz im Discord-Desktop-Client.
