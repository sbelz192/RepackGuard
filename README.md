# RepackGuard

RepackGuard erkennt den Moment, in dem ein Installer den Microsoft Defender
aushebelt — und warnt, **bevor** der Schaden weitergeht.

Hintergrund ist eine reale Infektion vom 14.11.2026: Eine Repack-Installation
(Dark Souls II, DODI-Repacks) enthielt `steam_api64.dll` mit dem Trojaner
`Trojan:Win32/Occamy!rfn`. Der Defender erkannte die Datei, aber der User fügte eine Ausnahme hinzu.:

```
17:43:55  1116  Trojan:Win32/Occamy!rfn erkannt   (steam_api64.dll)
17:44:15  1117  Aktion: Quarantäne
17:48:44  1009  aus der Quarantäne wiederhergestellt   <-- der Installer
17:48:45  5007  Defender-Ausnahme für genau diese Datei <-- Scanner blindgeschaltet
```

Schritt 2 und 3 zusammen bedeuten: Die Infektion wurde wieder aktiviert, und
der Virenschutz wurde für genau diese Datei ausgeschaltet. Genau das Muster
erkennt RepackGuard.

## Bausteine

| Baustein | Aufgabe | Status |
|---|---|---|
| `src/rg_core` | Erkennungslogik in C (portabel, ohne Windows-Zwang) | fertig, getestet |
| `src/rg_cli` | Kommandozeile zum Prüfen von Ereignis-Exporten | fertig, getestet |
| `bridge/RepackGuard.Tray` | Desktop-App mit Tray, Defender-Eventlog, P/Invoke | fertig, getestet |
| `browser-extension` | Link Guard: warnt vor Scam-Seiten im Browser | fertig, getestet |
| `tools/update-db.py` | Sammelt Kandidaten für die Scam-Datenbank (URLhaus) | fertig, getestet |
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
dotnet build -c Release
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

## Architektur

```
rg_core (C, portabel)
   ├── rg_cli ............ Test- und Diagnose-Werkzeug
   ├── rg_core.dll ....... P/Invoke-Schnittstelle
   │      └── RepackGuard.exe (C#-Tray: Eventlog, Alarm, Sofortmaßnahmen)
   └── shared/rules.js ... Link-Bewertung (Browser-Erweiterung)
```

Der Kern kennt nichts von Windows: Er bekommt eine Liste von Ereignissen und
liefert einen Report. Dadurch ist die Erkennung logbar, testbar und portierbar.

## Link Guard

Die Browser-Erweiterung (Chrome, Edge, Firefox) prüft angeklickte Links gegen
die Scam-Datenbank und die Heuristik und leitet vor dem Laden auf eine
Warnseite um. In Discord Web werden auffällige Links zusätzlich markiert.

Installieren: `chrome://extensions` → Entwicklermodus → „Entpackte Erweiterung
laden“ → Ordner `browser-extension`.

## Scam-Datenbank

`browser-extension/data/domains.json` enthält bekannte Scam-Domains und
Domain-Muster. `browser-extension/data/candidates.json` enthält Kandidaten aus
dem URLhaus-Export. **Kandidaten sind nicht kuratiert** und werden nicht
automatisch blockiert — eine Übernahme ohne Prüfung würde echte Seiten
blockieren.

Datenbank aktualisieren (benötigt einen kostenlosen URLhaus-Schlüssel):

```sh
python tools/update-db.py --key <schluessel>
```

Der Schlüssel liegt in `tools/.urlhaus-key` und wird bewusst nicht
mitcommittet.

## Webseite

Die Projektseite liegt in `docs/` und ist erreichbar unter:

**https://sbelz192.github.io/RepackGuard/**

## Grenzen, ehrlich formuliert

- RepackGuard ersetzt **keinen** Virenschutz. Er erweitert Defender und
  Malwarebytes um eine Schicht, die das spezielle Aushebel-Muster erkennt.
- Der Discord-**Desktop-Client** wird nicht überwacht. Das ist technisch nicht
  sauber abbildbar und würde gegen die Discord-Nutzungsbedingungen verstoßen.
  Link Guard greift nur im Browser.
- Der Tray-Benutzer muss ggf. Administratorrechte haben, um das
  Defender-Ereignisprotokoll zu lesen. Ohne Rechte bleibt die App im
  Informationsmodus.
- Erkannt wird ein **Muster**, nicht „alle Trojaner“.

## Mitmachen

- Scam-Domains in `browser-extension/data/domains.json` ergänzen
  (Issue oder Pull Request).
- Den Link Guard in der eigenen Community verbreiten.
- Fälle melden, die vom Muster erfasst werden.

## Lizenz

MIT — siehe [LICENSE](LICENSE).
