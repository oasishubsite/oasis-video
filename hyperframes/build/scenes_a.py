from common import *

def words(text, cls="w", base_id=None):
    out=[]
    for i,wd in enumerate(text.split(" ")):
        idattr=f' id="{base_id}-{i}"' if base_id else ""
        out.append(f'<span class="{cls}"{idattr}>{wd}</span>')
    return " ".join(out)

# ---------- S01 HOOK (3.0 s) ----------
S01 = scene("s01", 1080, 1920, """
#s01-q{position:absolute;left:60px;top:300px;width:960px;font-family:'Syne';font-weight:700;font-size:100px;line-height:1.0;letter-spacing:-0.035em;}
#s01-bar{position:absolute;left:60px;top:760px;width:960px;height:132px;border-radius:66px;background:rgba(255,255,255,.07);
  border:2px solid rgba(255,255,255,.16);display:flex;align-items:center;padding:0 44px;gap:28px;}
#s01-bar svg{width:52px;height:52px;color:#94A3B8;flex:none;}
#s01-typed{font-size:52px;font-weight:500;color:#F8FAFB;white-space:pre;}
#s01-caret{width:4px;height:58px;background:#3B82F6;margin-left:-22px;}
#s01-res{position:absolute;left:60px;top:930px;width:960px;height:300px;border-radius:36px;background:rgba(255,255,255,.04);border:2px solid rgba(255,255,255,.08);padding:44px;}
.sk{height:22px;border-radius:11px;background:rgba(148,163,184,.18);margin-bottom:22px;}
#s01-none{position:absolute;left:44px;top:150px;display:flex;align-items:center;gap:18px;font-size:46px;font-weight:600;color:rgba(239,68,68,.85);}
#s01-none svg{width:46px;height:46px;}
""", """
    <h1 id="s01-q">¿Tu negocio <span class="blue">no aparece</span> cuando te buscan?</h1>
    <div id="s01-push" class="abs" style="inset:0">
      <div id="s01-bar">""" + SEARCH + """<span id="s01-typed"></span><span id="s01-caret"></span></div>
      <div id="s01-res">
        <div class="sk" style="width:62%"></div><div class="sk" style="width:38%"></div>
        <div id="s01-none">""" + CROSS + """<span id="s01-none-t">Sin resultados relevantes</span></div>
      </div>
    </div>
""", """
    const typed = document.getElementById("s01-typed");
    const txt = "tu negocio";
    for (let i = 0; i <= txt.length; i++) tl.set(typed, { textContent: txt.slice(0, i) }, 0.15 + i * 0.07);
    [0, .45, .9, 1.35, 1.8, 2.25, 2.7].forEach((t, i) => tl.set("#s01-caret", { opacity: i % 2 ? 0 : 1 }, t));
    tl.fromTo("#s01-res", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: .5, ease: EASE }, 0.95);
    tl.fromTo("#s01-none", { opacity: 0 }, { opacity: 1, duration: .12 }, 1.25);
    // glitch determinístico
    const g = [[8,-4],[-10,3],[5,6],[-6,-2],[0,0]];
    g.forEach(([x, y], i) => tl.set("#s01-none-t", { x, y, textShadow: x ? `${-x/2}px 0 rgba(59,130,246,.9), ${x/2}px 0 rgba(239,68,68,.9)` : "none" }, 1.3 + i * 0.06));
    [[-6,0],[7,0],[0,0]].forEach(([x], i) => tl.set("#s01-none-t", { x, textShadow: x ? `${-x}px 0 rgba(59,130,246,.9)` : "none" }, 2.0 + i * 0.05));
    // salida: push hacia el resultado vacío
    tl.fromTo("#s01-push", { scale: 1, filter: "blur(0px)" }, { scale: 1.12, filter: "blur(6px)", duration: .35, ease: "power3.in", transformOrigin: "50% 60%" }, 2.65);
    tl.fromTo("#s01-q", { opacity: 1 }, { opacity: 0, duration: .25, ease: "power2.in" }, 2.75);
""")

# ---------- S02 PROBLEMA (5.75 s) ----------
S02 = scene("s02", 1080, 1920, """
.s02-line{position:absolute;left:60px;top:300px;width:960px;font-family:'Syne';font-weight:700;font-size:88px;line-height:1.02;letter-spacing:-0.03em;}
#s02-phonewrap{position:absolute;left:300px;top:640px;width:480px;height:980px;}
#s02-phone{left:0;top:0;width:480px;height:980px;}
#s02-phone .screen{width:458px;height:958px;background:#0F172A;}
.s02-ui{position:absolute;left:28px;right:28px;}
.s02-field{top:90px;height:84px;border-radius:42px;background:#1E293B;display:flex;align-items:center;gap:16px;padding:0 28px;font-size:34px;color:#CBD5E1;}
.s02-field svg{width:34px;height:34px;color:#64748B;}
.s02-card{height:150px;border-radius:24px;background:#1E293B;padding:26px;}
.s02-card .sk{height:18px;border-radius:9px;background:#334155;margin-bottom:16px;}
.s02-card .sk.b{background:#475569;width:55%;}
.s02-p{position:absolute;width:92px;height:92px;border-radius:50%;background:rgba(148,163,184,.14);border:2px solid rgba(148,163,184,.35);color:#94A3B8;padding:18px;}
""", """
    <h2 class="s02-line" id="s02-a">""" + words("Hoy los clientes investigan", base_id="s02a") + """ <span class="blue">""" + words("antes de comprar.", base_id="s02b") + """</span></h2>
    <h2 class="s02-line" id="s02-c" style="opacity:0">""" + words("Si no te encuentran…", base_id="s02c") + """ <span class="blue">""" + words("compran en otro lado.", base_id="s02d") + """</span></h2>
    <div id="s02-phonewrap">
      <div class="iphone" id="s02-phone"><div class="island"></div><div class="screen">
        <div class="s02-ui s02-field">""" + SEARCH + """tu negocio</div>
        <div class="s02-ui s02-card" style="top:210px"><div class="sk b"></div><div class="sk" style="width:85%"></div><div class="sk" style="width:60%"></div></div>
        <div class="s02-ui s02-card" style="top:380px"><div class="sk b"></div><div class="sk" style="width:80%"></div><div class="sk" style="width:50%"></div></div>
        <div class="s02-ui s02-card" style="top:550px"><div class="sk b"></div><div class="sk" style="width:75%"></div><div class="sk" style="width:65%"></div></div>
      </div></div>
    </div>
""" + "".join(f'    <div class="s02-p" id="s02-p{i}" style="left:{x}px;top:{y}px">{PERSON}</div>\n' for i,(x,y) in enumerate([(80,700),(150,880),(60,1060),(170,1180),(860,720),(930,900),(840,1070),(920,1200)])), """
    const W = (id, n, times) => times.forEach((t, i) => tl.fromTo(`#${id}-${i}`, { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .14, ease: "power2.out" }, t));
    W("s02a", 4, [0.0, 0.16, 0.36, 0.78]); W("s02b", 3, [1.34, 1.6, 1.72]);
    tl.fromTo("#s02-phonewrap", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .8, ease: EASE }, 0.05);
    for (let i = 0; i < 8; i++) tl.fromTo(`#s02-p${i}`, { opacity: 0, scale: .6 }, { opacity: 1, scale: 1, duration: .5, ease: EASE }, 0.3 + i * 0.06);
    tl.to("#s02-a", { opacity: 0, filter: "blur(8px)", duration: .18, ease: "power2.in" }, 2.55);
    tl.set("#s02-c", { opacity: 1 }, 2.72);
    W("s02c", 4, [2.74, 2.86, 3.02, 3.1]); W("s02d", 4, [4.58, 4.94, 5.06, 5.3]);
    // los clientes se van (hacia la derecha, fuera de cuadro)
    for (let i = 0; i < 8; i++) tl.to(`#s02-p${i}`, { x: 1100 - (i < 4 ? 0 : 0), opacity: 0, duration: .9, ease: "power3.in" }, 3.3 + i * 0.12);
    // zoom-through a la pantalla del teléfono
    tl.to("#s02-c", { opacity: 0, filter: "blur(8px)", duration: .2, ease: "power2.in" }, 5.72);
    tl.to("#s02-phonewrap", { scale: 3.2, duration: .5, ease: "power3.in", transformOrigin: "50% 45%" }, 5.5);
""")

# ---------- S03 REVEAL (6.45 s) ----------
S03 = scene("s03", 1080, 1920, """
#s03-flood{position:absolute;inset:0;background:#0F172A;}
#s03-mark{position:absolute;left:340px;top:520px;width:400px;}
#s03-word{position:absolute;left:0;top:810px;width:1080px;text-align:center;font-family:'Syne';font-weight:700;font-size:96px;letter-spacing:-0.035em;line-height:1;}
#s03-sub{position:absolute;left:60px;top:960px;width:960px;text-align:center;font-size:50px;font-weight:500;line-height:1.25;color:#CBD5E1;}
#s03-sweep{position:absolute;left:-600px;top:380px;width:420px;height:760px;background:linear-gradient(90deg,transparent,rgba(96,165,250,.35),rgba(255,255,255,.55),rgba(96,165,250,.35),transparent);filter:blur(30px);mix-blend-mode:screen;transform:rotate(18deg);}
#s03-halo{position:absolute;left:190px;top:420px;width:700px;height:520px;border-radius:50%;background:radial-gradient(closest-side,rgba(23,84,207,.45),transparent);}
""", """
    <div id="s03-flood"></div>
    <div id="s03-halo"></div>
    <img id="s03-mark" src="assets/brand/logo_mark.png" alt="Oasis Hub Studio">
    <div id="s03-word">""" + "".join(f'<span class="w grad" id="s03-l{i}">{c if c!=" " else "&nbsp;"}</span>' for i,c in enumerate("Oasis Hub")) + """<span class="w">&nbsp;</span>""" + "".join(f'<span class="w" id="s03-m{i}">{c}</span>' for i,c in enumerate("Studio")) + """</div>
    <p id="s03-sub"><span class="blue" style="font-weight:700">""" + words("+10 años", base_id="s03a") + """</span> """ + words("creando websites que venden", base_id="s03b") + """</p>
    <div id="s03-sweep"></div>
""", """
    tl.fromTo("#s03-flood", { opacity: 1 }, { opacity: 0, duration: .6, ease: "power2.inOut" }, 0.0);
    tl.fromTo("#s03-halo", { opacity: 0, scale: .7 }, { opacity: 1, scale: 1, duration: 1.2, ease: "power2.out" }, 0.1);
    tl.fromTo("#s03-mark", { opacity: 0, scale: .82, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: .8, ease: EASE }, 0.15);
    for (let i = 0; i < 9; i++) tl.fromTo(`#s03-l${i}`, { opacity: 0.0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 0.26 + i * 0.045);
    for (let i = 0; i < 6; i++) tl.fromTo(`#s03-m${i}`, { opacity: 0.0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 0.94 + i * 0.045);
    [1.66, 2.22].forEach((t, i) => tl.fromTo(`#s03a-${i}`, { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .14 }, t));
    [2.5, 2.94, 3.44, 3.56].forEach((t, i) => tl.fromTo(`#s03b-${i}`, { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .14 }, t));
    tl.fromTo("#s03-sweep", { x: 0 }, { x: 2000, duration: 1.1, ease: "power2.inOut" }, 0.2);
    tl.fromTo("#s03-sweep", { x: 0 }, { x: 2000, duration: 1.0, ease: "power2.inOut", immediateRender: false }, 4.3);
    // corte a negro justo antes del drop (silencio de la música)
    tl.to(["#s03-mark", "#s03-word", "#s03-sub", "#s03-halo"], { opacity: 0, scale: .94, filter: "blur(10px)", duration: .22, ease: "power3.in" }, 5.72);
    tl.shiftChildren(-0.25, true, 0.3);   // la escena empieza en 9.0 s (tiempos escritos para 8.75 s)
""")

# ---------- S04 OFERTA (5.8 s) ----------
S04 = scene("s04", 1080, 1920, """
#s04-kicker{position:absolute;left:0;top:300px;width:1080px;text-align:center;font-family:'Syne';font-weight:700;font-size:68px;letter-spacing:-0.02em;}
#s04-price{position:absolute;left:0;top:440px;width:1080px;text-align:center;font-family:'Syne';font-weight:800;font-size:250px;line-height:1;letter-spacing:-0.05em;}
#s04-price .cur{font-size:140px;vertical-align:top;position:relative;top:30px;margin-right:6px;}
#s04-once{position:absolute;left:0;top:780px;width:1080px;text-align:center;font-size:44px;font-weight:600;color:#94A3B8;letter-spacing:.02em;}
#s04-days{position:absolute;left:110px;top:930px;width:860px;height:150px;border-radius:75px;background:rgba(23,84,207,.18);border:2px solid rgba(59,130,246,.6);
  display:flex;align-items:center;justify-content:center;gap:22px;font-family:'Syne';font-weight:700;font-size:64px;letter-spacing:-0.02em;}
#s04-ticks{position:absolute;left:390px;top:1110px;width:300px;display:flex;gap:18px;}
#s04-ticks div{flex:1;height:14px;border-radius:7px;background:rgba(148,163,184,.25);}
#s04-ticks div i{display:block;height:100%;width:100%;border-radius:7px;background:#3B82F6;transform-origin:0 50%;}
#s04-maint{position:absolute;left:0;top:1160px;width:1080px;text-align:center;font-size:36px;font-weight:500;color:#94A3B8;}
#s04-glow{position:absolute;left:90px;top:380px;width:900px;height:460px;border-radius:50%;background:radial-gradient(closest-side,rgba(59,130,246,.55),transparent);}
""", """
    <div id="s04-glow"></div>
    <div id="s04-kicker">Landing page <span class="blue">profesional</span></div>
    <div id="s04-price" class="grad-wrap"><span class="cur">$</span><span id="s04-num">249</span></div>
    <div id="s04-once">pago único</div>
    <div id="s04-days"><span>Lista en</span><span class="blue">2–3 días</span></div>
    <div id="s04-ticks"><div><i id="s04-t0"></i></div><div><i id="s04-t1"></i></div><div><i id="s04-t2"></i></div></div>
    <div id="s04-maint">1er año de mantenimiento incluido</div>
""", """
    tl.fromTo("#s04-kicker", { opacity: 0, filter: "blur(10px)", scale: 1.06 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: .35, ease: EASE }, 0.02);
    // conteo rápido 0 → 249 y slam en "$249" de la voz
    const num = document.getElementById("s04-num");
    tl.fromTo("#s04-price", { opacity: 0, y: 40 }, { opacity: .35, y: 0, duration: .4, ease: EASE }, 0.3);
    for (let i = 0; i <= 24; i++) { const t = i / 24, v = Math.round(249 * (1 - Math.pow(1 - t, 3))); tl.set(num, { textContent: String(v) }, 0.3 + t * 1.3); }
    tl.set("#s04-price", { opacity: 1, scale: 1.28 }, 1.66);
    tl.to("#s04-price", { scale: 1, duration: .22, ease: "expo.out" }, 1.66);
    tl.fromTo("#s04-glow", { opacity: 0 }, { opacity: 1, duration: .05 }, 1.66);
    tl.to("#s04-glow", { opacity: .35, duration: .9, ease: "power2.out" }, 1.75);
    tl.fromTo("#s04-once", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 2.1);
    tl.fromTo("#s04-days", { opacity: 0, scale: .9 }, { opacity: 1, scale: 1, duration: .45, ease: "back.out(1.6)" }, 3.6);
    ["#s04-t0", "#s04-t1", "#s04-t2"].forEach((s, i) => tl.fromTo(s, { scaleX: 0 }, { scaleX: 1, duration: .28, ease: "power2.out" }, 4.1 + i * 0.22));
    tl.fromTo("#s04-maint", { opacity: 0 }, { opacity: 1, duration: .3 }, 4.75);
    // whip hacia arriba
    tl.to(["#s04-kicker", "#s04-price", "#s04-once", "#s04-days", "#s04-ticks", "#s04-maint", "#s04-glow"], { y: -260, opacity: 0, filter: "blur(10px)", duration: .3, ease: "power3.in" }, 5.5);
""")
