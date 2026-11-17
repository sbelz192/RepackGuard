// RepackGuard Link Guard — markiert auffaellige Links in Discord-Web.
// Content scripts sind in MV3 keine Module; deshalb bewusst eine eigene,
// schlanke Heuristik statt Import. Aendert nichts an der Funktionalitaet.

const RISKY_TLDS = ['.cc', '.xyz', '.to', '.top', '.site', '.shop', '.live', '.fun'];
const RISKY_KW = ['giveaway', 'claim', 'casino', 'crypto', 'robux', 'free-nitro', 'mrbeast'];

function isRisky(href) {
  let host;
  try { host = new URL(href).hostname.toLowerCase(); } catch (e) { return false; }
  if (!host || host.endsWith('discord.com') || host.endsWith('discordapp.com') ||
      host.endsWith('discord.gg') || host.endsWith('discord.media')) return false;
  const labels = host.split('.');
  const tld = labels.length ? '.' + labels[labels.length - 1] : '';
  const kw = RISKY_KW.filter((k) => host.includes(k));
  return RISKY_TLDS.includes(tld) && kw.length > 0;
}

function markLinks(root) {
  const nodes = (root || document).querySelectorAll('a[href]');
  nodes.forEach((a) => {
    if (a.dataset.rgMarked) return;
    if (isRisky(a.href)) {
      a.dataset.rgMarked = '1';
      a.style.outline = '1px solid #f87171';
      a.style.outlineOffset = '1px';
      a.title = 'RepackGuard: Domain sieht nach Scam aus (' + a.hostname + ')';
    }
  });
}

markLinks(document);
// Discord rendert spaeter nach; Beobachtung ist bewusst sparsam.
let scheduled = false;
const mo = new MutationObserver(() => {
  if (scheduled) return;
  scheduled = true;
  setTimeout(() => { scheduled = false; markLinks(document); }, 800);
});
mo.observe(document.body || document.documentElement, { childList: true, subtree: true });
