; RepackGuard — Windows-Installer (Inno Setup 6)
; Bau:  ISCC installer/RepackGuard.iss
; Ergebnis: dist/RepackGuard-0.1.1-Setup.exe

#define MyAppName "RepackGuard"
#define MyAppVersion "0.1.1"
#define MyAppPublisher "RepackGuard"
#define MyAppExeName "RepackGuard.exe"

[Setup]
AppId={{8F3C2A11-5D4E-4B6A-9C77-1E2F3A4B5C6D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={localappdata}\Programs\RepackGuard
DefaultGroupName=RepackGuard
PrivilegesRequired=lowest
OutputDir=..\dist
OutputBaseFilename=RepackGuard-{#MyAppVersion}-Setup
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
SetupIconFile=..\assets\icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
WizardSizePercent=110
DisableWelcomePage=no

[Languages]
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\bridge\RepackGuard.Tray\publish\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Eine Verknuepfung auf dem Desktop erstellen"; GroupDescription: "Zusaetzliche Symbole:"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall

[Registry]
; Autostart fuer den angemeldeten Benutzer (HKCU — kein Administrator noetig)
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "RepackGuard"; ValueData: """{app}\{#MyAppExeName}"""; Flags: preservestringtype

[Code]
// Hinweis, falls .NET-Runtime fehlen sollte (self-contained ist normalerweise inklusive)
function InitializeSetup(): Boolean;
begin
  Result := true;
end;
