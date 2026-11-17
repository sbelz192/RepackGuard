// RepackGuard — Regeln, klassische Variante fuer Firefox (kein ES-Modul).
(function (root) {
  function hostOf(raw) {
    try { return new URL(raw).hostname.toLowerCase(); } catch (e) { return ''; }
  }
  function isLocalOrSafe(host) {
    if (!host) return true;
    if (host === 'localhost' || host.endsWith('.localhost')) return true;
    if (/^(\d{1,3}\.){3}\d{1,3}$/.test(host)) return true;
    return false;
  }
  function check(rawUrl, DB) {
    DB = DB || { domains: [], patterns: [], risky_tlds: [], risky_keywords: [] };
    const host = hostOf(rawUrl);
    if (isLocalOrSafe(host)) return { block: false, level: 'ok', why: '' };
    if (DB.domains.some((d) => host === d || host.endsWith('.' + d)))
      return { block: true, level: 'block', why: 'Bekannte Scam-Domain: ' + host };
    const path = (rawUrl || '').toLowerCase();
    if (DB.patterns.some((p) => path.includes(p.toLowerCase())))
      return { block: true, level: 'block', why: 'Domain-Muster: ' + host };
    const labels = host.split('.');
    const tld = labels.length ? '.' + labels[labels.length - 1] : '';
    const kw = (DB.risky_keywords || []).filter((k) => host.includes(k));
    if ((DB.risky_tlds || []).includes(tld) && kw.length > 0)
      return { block: false, level: 'warn', why: 'Auffaellig: ' + tld + ' + ' + kw.join(', ') };
    return { block: false, level: 'ok', why: '' };
  }
  root.RGRules = { hostOf: hostOf, isLocalOrSafe: isLocalOrSafe, check: check };
})(typeof self !== 'undefined' ? self : this);
