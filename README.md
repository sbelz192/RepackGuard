# RepackGuard — Repack-Reaktions-Watchdog (Kern)

Erkennt das Muster, mit dem infizierte Repack-Installer den Microsoft Defender
aushebeln:

1. Schadsoftware wird erkannt (Defender-Ereignis 1116/1117)
2. die Datei wird **aus der Quarantäne wiederhergestellt** (Ereignis 1009)
3. für genau diese Datei wird eine **Defender-Ausnahme gesetzt** (Ereignis 5007)

Schritt 2 + 3 zusammen bedeuten: Die Infektion wurde wieder aktiviert und der
Scanner dafür blindgeschaltet. Genau so lief der Vorfall am 14.11.2026.

## Status

- [x] C-Kern (`rg_core`) mit Mustererkennung
- [x] CLI (`rg_cli`) zum Testen gegen Event-Exporte
- [x] Unit-Tests mit dem realen Vorfall
- [x] Icon (Vektor + KI-Variante)
- [ ] C#-Bridge (Windows-Eventlog + Tray)
- [ ] Installer / Release

## Icon

`assets/icon.svg` ist die Vektor-Vorlage, `assets/icon.png` das gerenderte
App-Icon. `assets/icon-ai.png` ist eine generierte Alternativvariante.

## Echter Fund, den das Tool abbildet

Ereignisse aus dem Vorfall am 14.11.2026 (Auszug):

```
17:43:55  1116  Trojan:Win32/Occamy!rfn erkannt   (steam_api64.dll)
17:44:15  1117  Aktion: Quarantäne
17:48:44  1009  aus Quarantäne wiederhergestellt  <-- Installer
17:48:45  5007  Defender-Ausnahme für dieselbe Datei  <-- Scanner blindgeschaltet
```

## Bauen (Windows, MinGW-W64)

```sh
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build
```

## Testen

```sh
ctest --test-dir build --output-on-failure
```

## Architektur

```
rg_core (C, portabel)  ->  rg_cli (Test/CLI)
                        ->  rg_bridge (C#, Windows-Eventlog, Tray)
```

Der Kern kennt nichts von Windows. Er bekommt eine Liste von Ereignissen und
gibt einen Report. So ist die Erkennung logbar, testbar und portierbar.
