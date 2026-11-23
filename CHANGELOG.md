# Changelog

Alle nennenswerten Änderungen an RepackGuard werden hier dokumentiert.
Format nach [Keep a Changelog](https://keepachangelog.com/de/1.1.0/).

## [Unreleased]

Noch nicht veröffentlicht.

## [0.1.0] — 2026-11-18

### Hinzugefügt

- **C-Kern** (`rg_core`): Mustererkennung für Quarantäne-Restore und
  Defender-Ausnahme; Tests gegen den dokumentierten Real-Vorfall
  (`testdata/ds2_incident.tsv`) und einen Negativfall.
- **CLI** (`rg_cli`) mit Exit-Code-Vertrag: Alarm = 1, unauffällig = 0,
  Nutzungsfehler = 2.
- **Link Guard** (Browser-Erweiterung, Manifest V3): prüft angeklickte Adressen
  gegen eine lokale Scam-Datenbank und zeigt eine Warnseite statt der Seite.
  Enthält Popup, Warnseite und Domain-Daten.
- **Desktop-Tray** (C#, Windows): überwacht das Defender-Ereignisprotokoll,
  zeigt Status und Sofortmaßnahmen, Autostart über HKCU.
- **Installer** (Inno Setup 6, self-contained, kein Admin nötig).
- **CI** (GitHub Actions): Build, C-Tests, Link-Guard-Tests, Interop-Test,
  Publish, Installer, Release bei Tags.
- **Datenschutzerklärung** und Store-Texte.
- **Domain-DB-Updater** (`tools/update-db.py`): URLhaus-Export → unkuratierte
  Kandidaten (`candidates.json`).

### Bekannte Grenzen

- Der Installer ist **nicht signiert** (SmartScreen-Warnung beim ersten Start).
- Die Erweiterung schützt nur im Browser, nicht im Discord-Desktop-Client.
- Die Domain-Datenbank im ZIP erfordert ein Erweiterungs-Update bei Änderungen.
- `candidates.json` ist **nicht kuratiert** — keine Übernahme in `domains.json`
  ohne Prüfung.

[Unreleased]: https://github.com/sbelz192/RepackGuard/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/sbelz192/RepackGuard/releases/tag/v0.1.0
