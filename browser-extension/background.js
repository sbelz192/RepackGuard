// RepackGuard Link Guard — Background Service Worker (MV3, ES-Modul).
import { check } from './shared/rules.js';

const DB_URL = chrome.runtime.getURL('data/domains.json');
let DB = { domains: [], patterns: [], risky_tlds: [], risky_keywords: [] };

// URLs, die der Nutzer auf der Warnseite bewusst freigegeben hat (60 s).
const bypass = new Map();
chrome.runtime.onMessage.addListener((msg) => {
  if (msg && msg.type === 'bypass' && msg.url) bypass.set(msg.url, Date.now());
});

fetch(DB_URL)
  .then((r) => r.json())
  .then((d) => { DB = d; })
  .catch((e) => console.error('Link Guard: DB nicht ladbar', e));

chrome.webNavigation.onBeforeNavigate.addListener((details) => {
  if (details.frameId !== 0) return; // nur Top-Frame
  const v = check(details.url, DB);
  if (!v.block) return;
  const b = bypass.get(details.url);
  if (b && (Date.now() - b) < 60000) return; // bewusst freigegeben

  chrome.storage.local.get({ blocked: 0 }, (s) => {
    chrome.storage.local.set({ blocked: (s.blocked || 0) + 1 });
  });
  const target = chrome.runtime.getURL('warn.html')
    + '?to=' + encodeURIComponent(details.url)
    + '&why=' + encodeURIComponent(v.why);
  chrome.tabs.update(details.tabId, { url: target });
});
