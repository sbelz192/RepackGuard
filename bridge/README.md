# RepackGuard Desktop (Tray)

Laeuft im Hintergrund, abonniert das Defender-Ereignisprotokoll und ruft den
C-Kern (`rg_core.dll`) per P/Invoke auf.

## Bauen

```sh
# 1) C-Kern + DLL
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build

# 2) Tray-App
cd bridge/RepackGuard.Tray
dotnet build -c Release
```

## Starten

`bridge/RepackGuard.Tray/bin/Release/net10.0-windows/RepackGuard.exe`
(die `rg_core.dll` muss neben der exe liegen — das Build kopieren sie hin).

Der Defender-Log `Microsoft-Windows-Windows Defender/Operational` ist ohne
Administrator ggf. nicht lesbar; dann meldet die App das und bleibt im
Sicherheitsmodus (kein Alarm).

## Test

```sh
cd bridge/RepackGuard.Tests
dotnet run -c Release
```
Erwartet: `INTEROP OK` (Vorfall -> alarm=1, Kontrolle -> alarm=0).
