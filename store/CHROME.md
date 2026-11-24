# Chrome Web Store — Vorbereitung (Einreichung erst gegen Ende Dezember)

> **Zustand: vorbereitet.** ZIP, Texte, Icon, Screenshots und Datenschutzseite
> liegen bereit. Die einzige offene Handlung ist die **Registrierung (5 $)**.

## 1 · Was du brauchst

| Voraussetzung | Zustand |
|---|---|
| Google-Konto | vorhanden |
| Registrierungsgebühr **5 $** (einmalig) | noch offen |
| Entwickler-Verifizierung | Google kann eine Identitätsprüfung anfordern — bei Erstanmeldung beachten |
| Paket | `dist/link-guard-v0.1.1-store.zip` (Manifest V3) |
| Icon 128×128 | `dist/screenshots/icon-128.png` |
| Screenshots 1280×800 | `dist/screenshots/link-guard-warn-1280x800.png`, `link-guard-popup-1280x800.png` |
| Promo-Tile (optional) | `dist/screenshots/promo-tile-1400x560.png` |
| Datenschutz-Seite | https://sbelz192.github.io/RepackGuard/privacy.html |

## 2 · Schritt für Schritt

1. `chrome.google.com/webstore/devconsole` → mit Google-Konto anmelden.
2. Einmalig **5 $** Registrierungsgebühr zahlen.
3. Ggf. **Identitätsverifizierung** abschließen (Google fordert das manchmal erst nach der ersten Einreichung).
4. **„Neue Erweiterung"** → `dist/link-guard-v0.1.1-store.zip` hochladen.
5. Listing-Felder ausfüllen (unten).
6. **Datenschutz / Privacy practices** ausfüllen (Pflicht).
7. **Single purpose** bestätigen.
8. Veröffentlichen → Review (dauert einige Tage bis Wochen).

## 3 · Formularfelder

### Name
```
RepackGuard Link Guard
```

### Kurzbeschreibung (max. 132 Zeichen)
```
Warnt vor Scam-Seiten (Giveaways, Fake-Casinos, Wallet-Maschen), bevor sie laden.
```

### Ausführliche Beschreibung
```markdown
RepackGuard Link Guard warnt, bevor eine betrügerische Seite geladen wird.

Die Kette hinter dem Mr-Beast-Scam: eine Nachricht mit einem Link — ein Klick —
ein Fake-Casino oder Giveaway — ein Download oder Phishing. Die Erweiterung
erkennt bekannte Scam-Domains und leitet vor dem Laden auf eine Warnseite um.

Funktionen
• Prüft angeklickte Adressen gegen eine kuratierte Scam-Datenbank
  (aktuell 92 Domains)
• Zeigt eine Warnseite statt der betrügerischen Seite
• Heuristik für auffällige TLDs und Wörter
• Zählt blockierte Versuche lokal

Datenschutz
• Keine Datensammlung, keine Telemetrie, kein Tracking
• Seiteninhalte werden nicht gelesen oder übertragen
• Die Prüfung läuft vollständig lokal im Browser
• Datenquellen der Domain-Liste: URLhaus und Phishing.Database (MIT)

Bewusste Grenzen
• Nur im Browser, nicht im Discord-Desktop-Client
• Kein Schutz vor Dateien, die trotzdem geladen und ausgeführt werden
• Prüft Domains, keine Seiteninhalte

RepackGuard ersetzt keinen Virenschutz — es ist eine zusätzliche Warnschicht.
```

### Kategorie
`Sicherheit` (Security) oder `Tools`

### Sprache
Deutsch (Primär) — bei Bedarf zusätzlich Englisch als Übersetzung.

### Homepage / Support
```
https://github.com/sbelz192/RepackGuard
```

## 4 · Privacy Practices (Chrome fragt explizit)

| Frage | Antwort |
|---|---|
| Sammelt oder überträgt die Erweiterung Nutzerdaten? | **Nein** |
| Datenkategorien | keine |
| Zweck der Datenerfassung | Nicht zutreffend |
| Datenschutzerklärung | `https://sbelz192.github.io/RepackGuard/privacy.html` |

## 5 · Single Purpose (Pflichtfeld)

> „Warnt Nutzer davor, auf betrügerische Websites zu klicken, indem es die
> aufgerufene Domain gegen eine lokale Sperrliste prüft und vor dem Laden eine
> Warnseite anzeigt."

## 6 · Berechtigungen — Begründung

- **Zugriff auf alle Websites (`<all_urls>`):** Die Adresse muss **vor dem
  Laden** geprüft werden; das ist nur so möglich.
- **`webNavigation`:** erkennt den Seitenaufruf rechtzeitig.
- **`tabs`:** öffnet die Warnseite im selben Tab.
- **`storage`:** speichert die lokale Zählung.

## 7 · Assets

- `icon-128.png` (Listing-Icon)
- Screenshots: **echte** Aufnahmen wirken stärker als gestellte. Wenn du
  einen echten Screenshot der Warnseite hast (Popup-Klick → Warnung), nimm den.
- Promo-Tile optional.

## 8 · Nach der Einreichung

- Review: einige Tage bis Wochen. Bei Rückfrage: die Begründungen aus Abschnitt 6 nutzen.
- Nach Genehmigung: Link in README/Webseite ergänzen (ich kann das).

## 9 · Wichtig zu wissen

- Chrome hat Manifest V2 eingestellt — wir sind **MV3**, passt also.
- Sobald der Chrome-Eintrag live ist, können auch **Opera GX, Brave, Vivaldi und Edge**
  die Erweiterung installieren (Chromium-Basis). Der Opera-Eigen Eintrag wird dadurch
  überflüssig.
- Der Store verlangt keine separates Chrome-Paket — dasselbe ZIP wie Edge.
