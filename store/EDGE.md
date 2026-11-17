# Microsoft Edge Add-ons — Einreichungstexte für Link Guard

## Kurzbeschreibung

```
Warnt vor Scam-Seiten (Mr-Beast-Giveaways, Fake-Casinos, Repack-Repos), bevor sie laden.
```

## Ausführliche Beschreibung (250–10.000 Zeichen, pro Sprache)

```
RepackGuard Link Guard warnt, bevor eine betrügerische Seite geladen wird.

Die Kette hinter dem Mr-Beast-Scam: eine Nachricht mit einem Link — Klick —
Fake-Casino oder Giveaway — Download oder Phishing. Die Erweiterung erkennt
betrügerische Domains und leitet vor dem Laden auf eine Warnseite um.

Funktionen:
• Prüft angeklickte Adressen gegen eine lokale Scam-Datenbank
• Zeigt eine Warnseite statt der betrügerischen Seite
• Markiert auffällige Links in Discord Web direkt im Chat
• Zählt blockierte Versuche lokal

Datenschutz: keine Datensammlung, keine Telemetrie, keine Übertragung.
Die Prüfung erfolgt vollständig lokal im Browser.

Bewusste Grenzen: nur im Browser (nicht im Discord-Desktop-Client),
kein Schutz vor Dateien, die trotzdem geladen und ausgeführt werden,
Prüfung von Domains, nicht von Seiteninhalten.
```

## Konto

Partner Center, **kostenlos**. Persönliches Microsoft-Konto (Outlook/Live/Hotmail)
oder Anmeldung über GitHub. Wichtig: Land und Kontotyp (Privat/Unternehmen)
sind nach der Anmeldung **unveränderlich**.

## Paket

Gleich wie Chrome: `dist/link-guard-v0.1.0-store.zip` (eine Kopie liegt als
`link-guard-edge-v0.1.0.zip` bereit).

## Suchbegriffe (max. 7, je 30 Zeichen)

`scam`, `phishing`, `betrug`, `warnung`, `link`, `sicherheit`, `discord`

## Screenshots

1280×800 oder 640×480, bis zu 6 Stück. Gleiche Motive wie bei Chrome.

## Zertifizierung

Review bis zu 7 Werktage. Die Berechtigungen (`webNavigation`, `tabs`,
`storage`, `<all_urls>`) müssen begründet werden — Text liegt in
`store/CHROME.md` unter „Berechtigungen".

## Hinweis

Edge ist Chromium. Manifest V3 funktioniert unverändert. Ein reines
„Chrome"-Branding sollte im Listing vermieden werden.
