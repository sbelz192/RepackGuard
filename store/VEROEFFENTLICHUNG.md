# Veröffentlichung — Schritt für Schritt

Drei Stores. **Edge und Firefox sind kostenlos**, Chrome kostet einmalig 5 $.
Empfohlene Reihenfolge: Edge → Firefox → Chrome (wenn Geld da).

## Dateien, die du brauchst

| Zweck | Datei |
|---|---|
| Chrome-Paket | `dist/link-guard-v0.1.0-store.zip` |
| Edge-Paket (identisch) | `dist/link-guard-edge-v0.1.0.zip` |
| Firefox-Paket | `dist/link-guard-firefox-v0.1.0.zip` |
| Texte | `store/CHROME.md`, `store/EDGE.md`, `store/FIREFOX.md` |
| Datenschutz | `store/PRIVACY.md` |
| Listing-Icon 128×128 | `dist/screenshots/icon-128.png` |
| Screenshots | `dist/screenshots/link-guard-warn-1280x800.png`, `link-guard-popup-1280x800.png` |
| Promo-Tile (optional) | `dist/screenshots/promo-tile-1400x560.png` |

---

## 1 · Microsoft Edge Add-ons (kostenlos)

1. **Partner Center** öffnen: `partner.microsoft.com` → mit einem
   **persönlichen Microsoft-Konto** (Outlook/Live/Hotmail) anmelden —
   **kein** Firmen-/Schulkonto.
2. Land und Kontotyp (Privat/Unternehmen) wählen — **danach unveränderlich**.
3. **Neue Erweiterung** anlegen → `dist/link-guard-edge-v0.1.0.zip` hochladen.
4. Verfügbarkeit, Eigenschaften und Datenschutz ausfüllen.
5. Listing je Sprache (Deutsch/Englisch) aus `store/EDGE.md` übernehmen.
6. Icon 128×128 und Screenshots hochladen.
7. **Zertifizierungs-Hinweise** aus `store/EDGE.md` einfügen → Veröffentlichen.

Review: bis zu 7 Werktage.

## 2 · Firefox Add-ons (kostenlos)

1. **AMO-Konto**: `addons.mozilla.org` → Entwickler → anmelden.
2. „Eigenes Add-on einreichen“ → `dist/link-guard-firefox-v0.1.0.zip` hochladen.
3. Liste aus `store/FIREFOX.md` übernehmen, Icon und Screenshots ergänzen.
4. Datenschutzangaben ausfüllen (aus `store/PRIVACY.md`).
5. Einreichen.

Review: meist innerhalb von 24 Stunden, bei manueller Prüfung länger.

## 3 · Chrome Web Store (5 $ einmalig)

1. **Chrome Web Store Developer Dashboard**: `chrome.google.com/webstore/devconsole`
   → einmalig 5 $ Registriergebühr.
2. „Neue Erweiterung“ → `dist/link-guard-v0.1.0-store.zip` hochladen.
3. Texte aus `store/CHROME.md`, Datenschutz („Privacy practices") ausfüllen.
4. Icon, Screenshots, optional Promo-Tile hochladen.
5. „Single purpose“-Begründung und Berechtigungs-Erklärungen stehen in
   `store/CHROME.md` unter „Berechtigungen".

Review: einige Tage bis Wochen.

---

## Hinweise

- **„Chrome"-Branding** im Listing vermeiden (Edge-Prüfung).
- Screenshots müssen die **tatsächliche** Funktion zeigen; die Vorlagen in
  `dist/screenshots` sind teils gestellt (Popup). Echte Screenshots sind
  stärker.
- Nach der Genehmigung: Link in README/Webseite ergänzen (ich kann das).
