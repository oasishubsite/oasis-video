// Busca la posición vertical (px CSS) de secciones clave en cada sitio, desktop y móvil.
const { chromium } = require('playwright');
const Q = {
  melo: ['Sabores','sabor','Puntos de Venta','Encuentra','quiz','Quiz','Descubre tu'],
  barahona: ['Galería','Amenidades','Reserva','WhatsApp','Self','Alexa','Check-in'],
  ecogreen: ['Servicios','vs','Otros','Reseñas','Waze','Proyectos'],
};
(async () => {
  const b = await chromium.launch(); const out = {};
  for (const [slug, words] of Object.entries(Q)) {
    const url = require('../assets/captures/meta.json')[slug].url;
    for (const [dev, vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]) {
      const p = await b.newPage({ viewport: vp });
      await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(()=>{});
      const h = await p.evaluate(() => document.documentElement.scrollHeight);
      for (let y=0;y<h;y+=400){ await p.evaluate(y=>scrollTo(0,y),y); await p.waitForTimeout(60);} await p.evaluate(()=>scrollTo(0,0));
      out[`${slug}/${dev}`] = await p.evaluate(words => {
        const res = {};
        for (const el of document.querySelectorAll('h1,h2,h3,h4,form,table,button,label,iframe')) {
          const t = (el.innerText || el.tagName).trim().split('\n')[0].slice(0, 60);
          const y = Math.round(el.getBoundingClientRect().top + scrollY);
          if (['H2','FORM','TABLE','IFRAME'].includes(el.tagName) || words.some(w => t.includes(w))) res[`${el.tagName}:${t}`] = y;
        }
        return res;
      }, words);
      await p.close();
    }
  }
  console.log(JSON.stringify(out, null, 1)); await b.close();
})();
