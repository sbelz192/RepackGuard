# SignPath — Bewerbung für kostenlose Code-Signatur

SignPath Foundation stellt Open-Source-Projekten kostenlose Code-Signaturen
aus. Ziel: Der Windows-Installer von RepackGuard wird signiert, SmartScreen
warnt nicht mehr.

## Voraussetzungen — aktueller Stand des Projekts

| Bedingung | Stand |
|---|---|
| Öffentliches Repository | ✓ `github.com/sbelz192/RepackGuard` |
| OSI-Lizenz, keine Dual-Lizenzierung | ✓ MIT |
| Kein proprietärer Code | ✓ |
| Releases per CI aus dem öffentlichen Repo | ✓ GitHub Actions baut den Installer |
| Projekt aktiv gepflegt und dokumentiert | ✓ Webseite, README, Tests |
| Signatur-Schritt in der Pipeline vorbereitet | ✓ auskommentiert in `.github/workflows/build.yml` |

## Ablauf der Bewerbung

1. Auf <https://signpath.io> eine Bewerbung für das Projekt stellen
   (Open-Source-Programm).
2. SignPath prüft Repository und Build-Pipeline.
3. Nach Annahme erhältst du:
   - **Organization ID**
   - **Project** (Slug)
   - **Signing Policy** (Slug)
   - **API-Token**
4. Die vier Werte als **GitHub-Repository-Secrets** hinterlegen:
   `SIGNPATH_ORGANIZATION_ID`, `SIGNPATH_PROJECT`, `SIGNPATH_SIGNING_POLICY`,
   `SIGNPATH_API_TOKEN`.
5. Den auskommentierten Signatur-Schritt in der Pipeline aktivieren
   (eine Zeile, ich kann das einsetzen).

## Nach der Aktivierung

Der Signatur-Schritt muss gemäß SignPath-Bedingungen einen Hinweis im
Projekt platzieren:

> „Free code signing provided by SignPath.io, certificate by SignPath
> Foundation."

Diesen Hinweis ergänze ich in README und Webseite, sobald die Bewerbung
angenommen ist.

## Wichtige Einschränkung

Das Zertifikat steht auf den Namen der **SignPath Foundation**, nicht auf
deinen. SmartScreen akzeptiert es trotzdem; in den Dateieigenschaften steht
als Herausgeber „SignPath Foundation".

## Ehrlich

- Die Bewerbung ist ein **Review** und dauert. Nicht garantiert.
- Bis dahin bleibt der Installer **unsigniert** — SmartScreen warnt einmal.
  Das ist keine Defekt, sondern der normale Zustand ohne Zertifikat.
- Alternativen (kostenpflichtig): OV-Zertifikat bei einer Zertifizierungsstelle
  (ca. 100–400 $/Jahr) — für den Privatzweck über SignPath kostenlos vorzuziehen.
