# RepackGuard

RepackGuard erkennt den Moment, in dem ein Installer den Microsoft Defender
aushebelt — und warnt, **bevor** der Schaden weitergeht. Daneben warnt die
Browser-Erweiterung **Link Guard** vor bekannten Scam-Seiten, bevor sie laden.

## Was es konkret kann

| Schutz | Wie | Wo |
|---|---|---|
| **Aushebel-Erkennung** | Erkennt das Muster *Quarantäne-Restore + Defender-Ausnahme* in Echtzeit und zeigt Sofortmaßnahmen | Desktop-Tray (Windows) |
| **Scam-Warnung** | Prüft angeklickte Links gegen eine kuratierte Datenbank (aktuell **92 Domains**) und eine Heuristik | Link Guard (Browser) |
| **Laufende Aktualisierung** | Täglicher Abruf neuer Kandidaten aus URLhaus und Phishing.Database | Cron / Updater |

## Am einfachsten nutzen

**1 · Link Guard (Browser)** — die einfachste Variante:

- **Firefox:** im Add-ons-Store verfügbar:
  [addons.mozilla.org/…/repackguard-link-guard](https://addons.mozilla.org/de/firefox/addon/repackguard-link-guard/)
- **Chrome / Edge:** Store-Einreichung läuft.
- **Manuell:** `chrome://extensions` → Entwicklermodus → „Entpackte Erweiterung
  laden“ → Ordner `browser-extension`.

**2 · Desktop-Tray (Windows):**

- **Installer:** im [Release-Bereich](https://github.com/sbelz192/RepackGuard/releases)
  — doppelklicken, fertig. Legt Autostart an, kein Administrator nötig.
- **Aus dem Quelltext:** siehe [Bauen](#bauen).

## Der Vorfall hinter dem Projekt

Am 14.11.2026 enthielt eine Repack-Installation (Dark Souls II, DODI-Repacks)
`steam_api64.dll` mit dem Trojaner `Trojan:Win32/Occamy!rfn`:

```
17:43:55  1116  Trojan:Win32/Occamy!rfn erkannt      (steam_api64.dll)
17:44:15  1117  Aktion: Quarantäne
17:48:44  1009  aus der Quarantäne wiederhergestellt   <-- der Installer
17:48:45  5007  Defender-Ausnahme für genau diese Datei <-- Scanner blindgeschaltet
```

Schritt 2 und 3 zusammen: Die Infektion wurde wieder aktiviert **und** der
Virenschutz für genau diese Datei ausgeschaltet. Genau das Muster erkennt
RepackGuard.

## Bausteine

| Baustein | Aufgabe | Status |
|---|---|---|
| `src/rg_core` | Erkennungslogik in C (portabel, ohne Windows-Zwang) | fertig, getestet |
| `src/rg_cli` | Kommandozeile zum Prüfen von Ereignis-Exporten | fertig, getestet |
| `bridge/RepackGuard.Tray` | Desktop-App mit Tray, Defender-Eventlog, P/Invoke | fertig, getestet |
| `browser-extension` | Link Guard: warnt vor Scam-Seiten im Browser | fertig, im Store |
| `tools/update-db.py` | Kandidaten aus URLhaus + Phishing.Database | fertig |
| `tools/kuratieren.py` | Regelwerk zur konservativen Kuratierung | fertig |
| `docs` | Webseite | online |

## Bauen

Der C-Kern und die Windows-DLL:

```sh
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build
```

Die Desktop-App (benötigt .NET 10):

```sh
cd bridge/RepackGuard.Tray
dotnet publish -c Release -r win-x64 --self-contained true -o publish
```

Der Installer (benötigt Inno Setup 6):

```sh
iscc installer/RepackGuard.iss
```

## Testen

```sh
ctest --test-dir build --output-on-failure
```

Erwartetes Ergebnis: **100 % bestanden, 0 Warnungen, 0 Fehler.**

Der Interop-Test verbindet die C#-Seite mit der C-DLL und prüft den realen
Vorfall:

```sh
cd bridge/RepackGuard.Tests
dotnet run -c Release
```

Erwartet: `INTEROP OK` (Vorfall → `alarm=1`, Kontrollfall → `alarm=0`).

## Scam-Datenbank

`browser-extension/data/domains.json` enthält die **kuratierte** Liste
(92 Domains). `candidates.json` enthält den unkuratierten Rohbestand.

Quellen (nur klar lizenzierte):

- **URLhaus** (abuse.ch) — alle 5 Minuten aktualisiert, fair-use.
- **Phishing.Database** (MIT) — stündlich aktualisiert.

Bewusst **nicht** verwendet: Quellen unter **GPL-3.0** (Copyleft, würde das
MIT-Projekt unter GPL zwingen) und solche mit **non-commercial**-Klauseln.

```sh
python tools/update-db.py     # Kandidaten neu laden
python tools/kuratieren.py    # Kuratierungsvorschlag anzeigen
```

Details zu Quellen und Lizenzen: `browser-extension/data/SOURCES.md`.
Der tägliche Abruf ist als Cron-Job eingerichtet (schreibt nur Kandidaten,
kuratiert nichts).

## Webseite

**https://sbelz192.github.io/RepackGuard/**

## Grenzen, ehrlich formuliert

- RepackGuard ersetzt **keinen** Virenschutz. Er erweitert Defender und
  Malwarebytes um eine Schicht, die das spezielle Aushebel-Muster erkennt.
- Der Discord-**Desktop-Client** wird nicht überwacht. Das ist technisch nicht
  sauber abbildbar und würde gegen die Discord-Nutzungsbedingungen verstoßen.
  Link Guard greift nur im Browser.
- Der Tray-Benutzer braucht ggf. Administratorrechte, um das
  Defender-Ereignisprotokoll zu lesen. Ohne Rechte bleibt die App im
  Informationsmodus.
- Erkannt wird ein **Muster**, nicht „alle Trojaner". Die Domain-Datenbank
  erfasst bekannte Scam-Domains, nicht jede betrügerische Seite.
- Der Windows-Installer ist **nicht signiert** — Windows SmartScreen warnt beim
  ersten Start einmal.

## Mitmachen

- Scam-Domains in `browser-extension/data/domains.json` ergänzen
  (Issue oder Pull Request).
- Den Link Guard in der eigenen Community verbreiten.
- Fälle melden, die vom Muster erfasst werden.

## Lizenz

MIT — siehe [LICENSE](LICENSE). Die Domain-Daten stammen aus den oben
genannten Quellen; deren Lizenzen sind in `browser-extension/data/SOURCES.md`
festgehalten.
