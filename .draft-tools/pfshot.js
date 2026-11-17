const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = '/home/user/My-Portfolio';
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.webp': 'image/webp' };
const srv = http.createServer((q, r) => {
  if (q.method === 'POST') { r.writeHead(200); return r.end('ok'); }
  const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
}).listen(4174);
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost' } });
  const files = fs.readdirSync(root + '/v2/drafts/pf').filter(f => /^\d{2,3}-.*\.html$/.test(f)).filter(f => !process.argv[2] || process.argv[2].split(',').includes(f.split('-')[0]));
  for (const f of files) {
    for (const [name, w, h] of [['d', 1440, 900], ['m', 390, 844]]) {
      const c = await b.newContext({ viewport: { width: w, height: h }, reducedMotion: process.env.RM ? 'reduce' : 'no-preference' });
      const p = await c.newPage();
      const errs = []; p.on('console', m => m.type() === 'error' && errs.push(m.text())); p.on('pageerror', e => errs.push(String(e)));
      await p.goto('http://localhost:4174/v2/drafts/pf/' + f, { waitUntil: 'networkidle' });
      await p.evaluate(() => document.fonts.ready); if (!process.env.RM) { await p.waitForTimeout(2600); const H = await p.evaluate(() => document.documentElement.scrollHeight); for (let y = 0; y < H; y += 500) { await p.evaluate((y) => scrollTo(0, y), y); await p.waitForTimeout(120); } await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(1400); }
      await p.screenshot({ path: `pfout/${f.split('-')[0]}-${name}.png`, fullPage: true });
      const ov = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth, document.documentElement.scrollHeight].join('/'));
      let st = '';
      if (name === 'd') { try { await p.fill('#email', 'a@b.co', { timeout: 4000 }); await p.click('.btn', { timeout: 4000 }); await p.waitForTimeout(700); st = await p.evaluate(() => document.querySelector('form').className); } catch (e) { st = 'FORM-NOT-REACHABLE'; } }
      console.log(f, name, ov, st, errs.join('|'));
      await c.close();
    }
  }
  await b.close(); srv.close();
})();
