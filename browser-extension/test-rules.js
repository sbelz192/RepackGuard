// Test der gemeinsamen Regeln (Node): node test-rules.js
import { check } from './shared/rules.js';
import { readFileSync } from 'node:fs';

const DB = JSON.parse(readFileSync(new URL('./data/domains.json', import.meta.url), 'utf8'));

let fails = 0;
function t(name, url, wantBlock, wantLevel) {
  const r = check(url, DB);
  const ok = r.block === wantBlock && (wantLevel ? r.level === wantLevel : true);
  if (!ok) { fails++; console.log('  FEHL', name, '->', JSON.stringify(r)); }
  else console.log('  ok  ', name, '->', r.level);
}

console.log('Link Guard — Regel-Tests');
t('bekannte Scam-Domain', 'https://runicwin.com/claim', true);
t('Subdomain der Scam-Domain', 'https://www.runicwin.com/x', true);
t('FitGirl-Fake', 'https://fitgirl-repacks.xyz/download', true);
t('normales Video', 'https://www.youtube.com/watch?v=abc', false);
t('Wikipedia', 'https://de.wikipedia.org/wiki/Test', false);
t('localhost', 'http://localhost:8080/x', false);
t('Private IP', 'http://192.168.0.5/admin', false);
t('Heuristik (warn, kein Block)', 'https://crypto-casino.xyz/claim', false, 'warn');
t('Block-Muster MrBeast', 'https://mrbeast-giveaway.cc/claim', true);
t('Heuristik-TLD ohne Keyword', 'https://beispiel-website.cc/', false, 'ok');

console.log(fails ? 'FEHLER: ' + fails : 'ALLE OK');
process.exit(fails ? 1 : 0);
