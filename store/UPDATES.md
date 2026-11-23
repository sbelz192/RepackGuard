# Updates — Ablauf und Synchronisation

## Kurzantwort

Das Repository und AMO (Firefox) sind **zwei getrennte Speicher**. Eine Änderung
im Repo wird **nicht** nach AMO übertragen. Firefox-Hosting ist eine Kopie des
ZIPs, das du eingereicht hast.

## Manueller Ablauf (der normale Weg)

1. **Version erhöhen** — in `browser-extension/manifest.json` (`version`) und in
   `store/firefox/manifest.json`. Ohne neue Version lehnt AMO ab.
2. **ZIP bauen** — siehe `store/VEROEFFENTLICHUNG.md` (Firefox-ZIP liegt in
   `dist/link-guard-firefox-<version>.zip`).
3. **AMO öffnen** — `addons.mozilla.org` → Developer Hub → deine Erweiterung →
   **Neue Version** → ZIP hochladen.
4. **Formular erneut** — Texte ändern sich selten; bei Bedarf anpassen.
5. **Einreichen** — Review. Bei kleinen Aktualisierungen meist schnell, bei
   großen Änderungen (neue Berechtigungen) gründlicher.

## Was die CI bereits übernimmt

- Build + Tests + ZIP + Release bei Tags (`v*`).
- Der Release enthält den Installer; die Store-ZIPs musst du manuell
  herunterladen oder aus `dist/` kopieren.

## Was NICHT automatisch geht (und warum)

| Kanal | Automatisch? | Grund |
|---|---|---|
| GitHub Releases | ja (bei Tag) | CI mit `contents: write` |
| AMO/Firefox | **nein** | Hosting ist separat; Einreichung über Formular |
| Chrome Web Store | **nein** | Entweder Formular oder Publisher-API mit OAuth |

## Optional: AMO-API-Automatisierung

Möglich über `web-ext sign` mit AMO-API-Credentials:

```
web-ext sign --api-key <JWT-Issuer> --api-secret <JWT-Secret> \
             --channel listed --source-dir dist/firefox-pkg
```

Voraussetzungen:
- API-Schlüssel im **AMO Developer Hub** erzeugen (der Nutzer muss das selbst
  tun — Credentials niemals in Chats/Repos).
- Schlüssel als GitHub-Secrets hinterlegen.
- Ein Workflow-Schritt, der bei Tags einreicht.

**Ehrlich:** Bei einem Solo-Projekt mit wenigen Updates pro Jahr ist der
manuelle Weg überschaubarer und weniger fehleranfällig als eine API-
Automatisierung mit rotierenden Credentials. Die Automatisierung lohnt erst
bei häufigen Versionen.

## Versionsregeln

- Jede AMO-Einreichung braucht eine **höhere** Version als die bisherige.
- Semantisch: `0.1.0` → `0.1.1` (Bugfix), `0.2.0` (neue Funktion).
- Die Version sollte im Repo und im Manifest identisch sein.
