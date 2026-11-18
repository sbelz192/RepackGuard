// RepackGuard Link Guard — Warnseite (externes Skript, CSP-konform).
const q = new URLSearchParams(location.search);
const to = q.get('to') || '';
const why = q.get('why') || 'Unbekannter Grund';

document.getElementById('why').textContent = why;
document.getElementById('to').textContent = to;
document.getElementById('back').onclick =
  () => (history.length > 1 ? history.back() : chrome.tabs.remove(null));
document.getElementById('go').onclick = () => {
  if (!to) return;
  if (chrome.runtime && chrome.runtime.sendMessage) {
    chrome.runtime.sendMessage({ type: 'bypass', url: to }, () => { location.href = to; });
  } else {
    location.href = to;
  }
};
