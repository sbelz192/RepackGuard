# Installer (Windows)

Erzeugt einen echten Windows-Installer für die Desktop-Anwendung mit
Inno Setup. Der Installer ist **self-contained**: Die .NET-Runtime ist
enthalten, es muss nichts installiert werden.

## Voraussetzungen

- Inno Setup 6 (`winget install --id JRSoftware.InnoSetup`)
- .NET 10 SDK
- CMake + MinGW-W64

## Bauen

```sh
# 1) C-Kern und DLL
cmake -S . -B build -G "MinGW Makefiles"
cmake --build build

# 2) Tray-Anwendung self-contained publishen
cd bridge/RepackGuard.Tray
dotnet publish -c Release -r win-x64 --self-contained true -o publish --no-restore

# 3) Installer erzeugen
cd ../../
"C:\Users\Admin\AppData\Local\Programs\Inno Setup 6\ISCC.exe" installer/RepackGuard.iss
```

Ergebnis: `dist/RepackGuard-0.1.0-Setup.exe`.

## Eigenschaften des Installers

- Installation unter `%LOCALAPPDATA%\Programs\RepackGuard` (kein Administrator
  nötig)
- Autostart über `HKCU\...\Run` (kein Administrator nötig)
- Desktop-Verknüpfung als wählbare Aufgabe
- Vollständige Deinstallation über Systemsteuerung bzw. Programm und Features

## Signierung (ehrlich)

Der Installer ist **nicht signiert**. Windows SmartScreen warnt beim ersten
Start. Für eine vertrauenswürdige Verteilung braucht es ein
Code-Signing-Zertifikat (OV/EV, kostenpflichtig beim Zertifikatsstelle).
Ohne Zertifikat ist die Warnung zu erwarten und keine Anzeige für einen
Defekt.
