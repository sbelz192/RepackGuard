# Datenschutzerklärung — RepackGuard Link Guard

**Stand:** 17.11.2026

## Kurzfassung

Die Erweiterung **RepackGuard Link Guard** überprüft die Adressen der Seiten,
die Sie aufrufen, und warnt Sie, bevor eine bekannte Betrugsmasche geladen
wird. Sie sammelt **keine personenbezogenen Daten**, sendet **keine** Daten an
Dritte und speichert lediglich eine Zählung blockierter Versuche **lokal auf
Ihrem Gerät**.

## Verantwortliche Stelle

RepackGuard (Open-Source-Projekt)

## Welche Daten werden verarbeitet?

1. **Aufruf-Adressen (URLs) und Domainnamen.**
   Die Erweiterung prüft die Adresse jeder Seite, die Sie öffnen, gegen eine
   lokale Liste betrügerischer Domains. Dieser Abgleich erfolgt **lokal** im
   Browser. Die Adresse wird **nicht** an einen Server gesendet.

2. **Zählung blockierter Versuche.**
   Die Anzahl der Warnungen wird lokal im Browserspeicher
   (`chrome.storage.local`) abgelegt und nur in Ihrem Browser angezeigt.

## Was nicht passiert

- Es werden **keine** Namen, E-Mail-Adressen, Passwörter oder
  Kontodaten erhoben.
- Es werden **keine** Inhalte von Nachrichten, Chats oder Seiteninhalten
  gelesen oder übertragen.
- Es finden **keine** Analysen, Telemetrie oder Tracking statt.
- Es werden **keine** Daten an Dritte weitergegeben.

## Berechtigungen und deren Zweck

| Berechtigung | Zweck |
|---|---|
| `webNavigation` | Erkennt den Aufruf einer Seite, um die Adresse zu prüfen und gegebenenfalls eine Warnseite anzuzeigen. |
| `tabs` | Öffnet die Warnseite im selben Tab. |
| `storage` | Speichert die Zählung blockierter Versuche lokal. |
| `<all_urls>` | Der Abgleich der Adresse muss für alle Seiten möglich sein, damit die Warnung **vor** dem Laden erscheint. |

## Datenübertragung in die USA

Der Chrome Web Store bzw. der Firefox Add-ons Store stellen die Erweiterung
bereit. Soweit der Store technisch eingreift (Installation, Updates), finden
die Datenschutzbedingungen des jeweiligen Anbieters Anwendung. Die Erweiterung
selbst überträgt keine Daten.

## Ihre Rechte

Da keine personenbezogenen Daten verarbeitet werden, entfallen
Auskunfts- und Löschansprüche gegen das Projekt. Bei Fragen wenden Sie sich
über das GitHub-Repository an den Verantwortlichen.

## Änderungen

Diese Erklärung kann bei Änderungen der Erweiterung angepasst werden. Die
jeweils aktuelle Fassung liegt im Repository.
