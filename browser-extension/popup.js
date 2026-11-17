// RepackGuard Link Guard — Popup-Zaehler.
chrome.storage.local.get({ blocked: 0 }, (s) => {
  document.getElementById('n').textContent = String(s.blocked || 0);
});
