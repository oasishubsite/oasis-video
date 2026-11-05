// Capturas de los sitios del portafolio: full-page desktop/móvil + video de scroll + colores/hero.
// Uso: node scripts/capture.mjs [slug...]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';

const SITES = {
  melo:     'https://melokombucha.com',
  barahona: 'https://barahonastay.site',
  ecogreen: 'https://proyectoecogreen.com',
  oasis:    'https://oasishub.studio',
  oasis_precios: 'https://oasishub.studio/precios',
};
const DEVICES = {
  desktop: { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 },
  mobile:  { viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true,
             userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' },
};
const OUT = 'assets/captures';
const only = process.argv.slice(2);
const ease = t => 1 - Math.pow(1 - t, 3) * (t < 1 ? 1 : 0);

async function settle(page) {
  // cerrar banners de cookies comunes
  for (const sel of ['button:has-text("Aceptar")','button:has-text("Accept")','button:has-text("Acepto")','button:has-text("Entendido")','[aria-label="Close"]']) {
    const b = page.locator(sel).first();
    if (await b.isVisible().catch(() => false)) await b.click({ timeout: 1500 }).catch(() => {});
  }
  // recorrer la página para disparar lazy-load y animaciones on-scroll
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 400) { await page.evaluate(y => window.scrollTo(0, y), y); await page.waitForTimeout(120); }
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.evaluate(async () => { await document.fonts.ready;
    await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); }))); });
  await page.waitForTimeout(1500);
}

const browser = await chromium.launch();
const meta = {};
for (const [slug, url] of Object.entries(SITES)) {
  if (only.length && !only.includes(slug)) continue;
  const dir = path.join(OUT, slug); fs.mkdirSync(dir, { recursive: true });
  meta[slug] = { url };
  for (const [dev, opts] of Object.entries(DEVICES)) {
    const ctx = await browser.newContext({ ...opts, locale: 'es-CR',
      recordVideo: { dir: path.join(dir, '_rec'), size: opts.viewport } });
    const page = await ctx.newPage();
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => page.goto(url, { waitUntil: 'load', timeout: 60000 }));
      await settle(page);
      await page.screenshot({ path: path.join(dir, `${dev}-hero.png`) });
      await page.screenshot({ path: path.join(dir, `${dev}-full.png`), fullPage: true });
      const info = await page.evaluate(() => {
        const cs = el => el && getComputedStyle(el);
        const h1 = document.querySelector('h1');
        return { title: document.title, h1: h1?.innerText?.trim(), h1Color: cs(h1)?.color, h1Font: cs(h1)?.fontFamily,
                 bodyBg: cs(document.body).backgroundColor, height: document.documentElement.scrollHeight,
                 theme: document.querySelector('meta[name="theme-color"]')?.content || null };
      });
      meta[slug][dev] = info;
      // video de scroll suave ~9 s: 1 s quieto, 7 s de scroll con easing, 1 s quieto
      const maxY = Math.min(info.height - opts.viewport.height, opts.viewport.height * 6);
      await page.waitForTimeout(1000);
      const steps = 7 * 30;
      for (let i = 1; i <= steps; i++) {
        const t = i / steps, e = t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3) / 2;
        await page.evaluate(y => window.scrollTo(0, y), Math.round(maxY * e));
        await page.waitForTimeout(33);
      }
      await page.waitForTimeout(1000);
      console.log('ok', slug, dev, info.height, info.h1);
    } catch (e) { console.log('FAIL', slug, dev, e.message); meta[slug][dev] = { error: e.message }; }
    const vid = page.video();
    await ctx.close();
    if (vid) { const p = await vid.path(); fs.renameSync(p, path.join(dir, `${dev}-scroll.webm`)); }
    fs.rmSync(path.join(dir, '_rec'), { recursive: true, force: true });
  }
}
await browser.close();
const mf = path.join(OUT, 'meta.json');
const prev = fs.existsSync(mf) ? JSON.parse(fs.readFileSync(mf)) : {};
fs.writeFileSync(mf, JSON.stringify({ ...prev, ...meta }, null, 2));
