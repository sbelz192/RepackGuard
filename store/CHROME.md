# Chrome Web Store — Einreichungstexte für Link Guard

## Kurzbeschreibung (max. 132 Zeichen)

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
• Zählt blockierte Versuche lokal

Datenschutz:
• Keine Datensammlung, keine Telemetrie, kein Tracking
• Keine Seiteninhalte werden gelesen oder übertragen
• Die Prüfung erfolgt vollständig lokal im Browser

Bewusste Grenzen:
• Greift nur im Browser, nicht im Discord-Desktop-Client
• Schützt nicht vor Dateien, die Sie trotzdem herunterladen und ausführen
• Prüft Domains, keine Seiteninhalte

Ersetzt RepackGuard keinen Virenschutz — es ist eine zusätzliche Warnschicht.
```

## Kategorie

`Produktivität` (oder `Sicherheit`/`Tools`)

## Sprache

Deutsch (Primärsprache) + Englisch

## Berechtigungen — Begründung (wird abgefragt)

- **browserlesender Zugriff auf alle Websites (`<all_urls>`):** Die Erweiterung
  muss die Adresse prüfen können, **bevor** eine Seite lädt. Das ist nur mit
  Zugriff auf die aufgerufene Adresse möglich.
- **`webNavigation`:** Erkennt den Seitenaufruf, um die Warnseite rechtzeitig
  anzuzueigen.
- **`tabs`:** Zeigt die Warnseite im selben Tab.
- **`storage`:** Speichert die lokale Zählung.

## Datenschutz

Link zu `store/PRIVACY.md` (als Seite hosten, z. B. GitHub Pages).

## Screenshots (vom Nutzer erstellen)

Chrome verlangt mindestens ein Screenshot (1280×800 oder 640×400). Sinnvoll:
1. Warnseite bei `https://runicwin.com/claim`
2. Erweiterung im Chrome-Menü / Popup mit Zähler

## Veröffentlichung

Erstmalig veröffentlichen, nicht als „unveröffentlicht".
