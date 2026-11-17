# Firefox Add-ons — Einreichungstexte für Link Guard

## Kurzbeschreibung

```
Warnt vor Scam-Seiten (Mr-Beast-Giveaways, Fake-Casinos, Repack-Repos), bevor sie laden.
```

## Ausführliche Beschreibung

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

## Kategorie

`Sicherheit & Datenschutz` / `Produktivität`

## Unterstützte Sprachen

Deutsch, Englisch

## Datenschutz

Die Erweiterung erhebt keine personenbezogenen Daten. Eine
Datenschutzerklärung liegt unter `store/PRIVACY.md`.

## Unterschied zum Chrome-Paket

Firefox verträgt das ES-Modul im Hintergrundskript nicht zuverlässig.
Das Firefox-Paket liegt unter `store/firefox` und nutzt ein klassisches
Hintergrundskript. Beide Varianten halten dieselbe Regellogik.

## Hinweis zur Verifizierung

Die Erweiterung blockiert nicht alle Links, nur Adressen aus der lokalen
Scam-Datenbank. Eine Überprüfung findet im Browser statt, keine Daten werden
übertragen.
