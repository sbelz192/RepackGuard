// RepackGuard Link Guard — Firefox (klassisches background script, MV3).
const DB_URL = browser.runtime.getURL('data/domains.json');
let DB = { domains: [], patterns: [], risky_tlds: [], risky_keywords: [] };
const bypass = new Map();
browser.runtime.onMessage.addListener((msg) => {
  if (msg && msg.type === 'bypass' && msg.url) bypass.set(msg.url, Date.now());
});
fetch(DB_URL).then((r) => r.json()).then((d) => { DB = d; }).catch((e) => console.error(e));

browser.webNavigation.onBeforeNavigate.addListener((details) => {
  if (details.frameId !== 0) return;
  const v = RGRules.check(details.url, DB);
  if (!v.block) return;
  const b = bypass.get(details.url);
  if (b && (Date.now() - b) < 60000) return;
  browser.storage.local.get({ blocked: 0 }).then((s) =>
    browser.storage.local.set({ blocked: (s.blocked || 0) + 1 }));
  const target = browser.runtime.getURL('warn.html')
    + '?to=' + encodeURIComponent(details.url)
    + '&why=' + encodeURIComponent(v.why);
  browser.tabs.update(details.tabId, { url: target });
});
