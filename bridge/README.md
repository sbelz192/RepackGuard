# RepackGuard Desktop (Tray)

Die Desktop-Anwendung läuft im Hintergrund, abonniert das
Defender-Ereignisprotokoll und ruft den C-Kern (`rg_core.dll`) per P/Invoke
auf.

Bei einer verdächtigen Manipulation erscheint ein Alarm-Popup mit
Sofortmaßnahmen:

1. Discord: Einstellungen → alle Geräte abmelden
2. Passwörter ändern (von einem sauberen Gerät aus)
3. Vollständigen Virenscan starten

## Bauen

```sh
# 1. C-Kern und DLL bauen
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build

# 2. Tray-Anwendung bauen
cd bridge/RepackGuard.Tray
dotnet build -c Release
```

## Starten

```
bridge/RepackGuard.Tray/bin/Release/net10.0-windows/RepackGuard.exe
```

Die Datei `rg_core.dll` muss neben der ausführbaren Datei liegen — der
Build kopiert sie dorthin.

## Administratorrechte

Das Defender-Ereignisprotokoll
(`Microsoft-Windows-Windows Defender/Operational`) ist ohne Administrator
gegebenenfalls nicht lesbar. In diesem Fall meldet die Anwendung das und
bleibt im Informationsmodus; es wird kein Alarm ausgelöst.

## Testen

```sh
cd bridge/RepackGuard.Tests
dotnet run -c Release
```

Erwartet: `INTEROP OK` (Vorfall → `alarm=1`, Kontrollfall → `alarm=0`).

## Dateien

| Datei | Zweck |
|---|---|
| `Program.cs` | Tray, Eventlog-Beobachter, Alarm, Popup |
| `Native.cs` | P/Invoke-Schnittstelle zum C-Kern |
| `RepackGuard.Tray.csproj` | Projektdatei (.NET 10, Windows Forms) |
