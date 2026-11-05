from common import *
from scenes_a import words

# ---------- S08 GRID (4.4 s) ----------
PH = [("melo","Bebidas"),("barahona","Hospedaje"),("ecogreen","Paisajismo")]
S08 = scene("s08", 1080, 1920, """
.s08-l{position:absolute;left:60px;width:960px;font-family:'Syne';font-weight:700;font-size:84px;line-height:1;letter-spacing:-0.035em;}
.s08-ph{position:absolute;top:640px;width:300px;height:620px;border-radius:44px;background:#0d0d10;padding:9px;box-shadow:0 0 0 2px #3a3d44,0 40px 80px rgba(0,0,0,.6);}
.s08-ph .screen{width:282px;height:602px;border-radius:36px;}
.s08-lab{position:absolute;top:1290px;width:300px;text-align:center;font-size:32px;font-weight:600;color:#94A3B8;}
""", """
    <div class="s08-l" id="s08-a" style="top:300px">3 industrias.</div>
    <div class="s08-l" id="s08-b" style="top:396px">3 diseños únicos.</div>
    <div class="s08-l blue" id="s08-c" style="top:492px">Cero plantillas.</div>
""" + "".join(f"""    <div class="s08-ph" id="s08-p{i}" style="left:{60+i*330}px"><div class="screen"><img src="assets/sites/{s}_mobile.jpg"></div></div>
    <div class="s08-lab" id="s08-t{i}" style="left:{60+i*330}px">{lab}</div>
""" for i,(s,lab) in enumerate(PH)), """
    [["#s08-a", 0.1], ["#s08-b", 1.58], ["#s08-c", 3.3]].forEach(([s, t]) => tl.fromTo(s, { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: .18, ease: "power2.out" }, t));
    [-1, 0, 1].forEach((d, i) => tl.fromTo(`#s08-p${i}`, { opacity: 0, x: d * 160, y: 80, scale: .9 }, { opacity: 1, x: 0, y: 0, scale: 1, duration: .7, ease: EASE }, 0.0 + i * 0.08));
    [0, 1, 2].forEach(i => tl.fromTo(`#s08-t${i}`, { opacity: 0 }, { opacity: 1, duration: .3 }, 0.6 + i * 0.1));
    tl.to(["#s08-p0", "#s08-p1", "#s08-p2", "#s08-t0", "#s08-t1", "#s08-t2"], { y: 700, opacity: 0, duration: .32, ease: "power3.in", stagger: .03 }, 4.05);
    tl.to(["#s08-a", "#s08-b", "#s08-c"], { opacity: 0, filter: "blur(8px)", duration: .2, ease: "power2.in" }, 4.15);
""")

# ---------- S09 COMPARACIÓN (13.8 s) ----------
ROWS = [("Precio landing page","$500 – $1,500+","$249 pago único"),
        ("Tiempo de entrega","2 – 6 semanas","2 – 3 días"),
        ("Diseño","Plantilla adaptada","100% a la medida"),
        ("Mantenimiento 1er año","Se cobra aparte","Incluido"),
        ("Google Business","Servicio extra","Gratis"),
        ("WhatsApp integrado","A veces","Siempre"),
        ("Hosting + SSL","Se cobra aparte","Incluido"),
        ("Atención","Tickets y correos","Directo por WhatsApp")]
# tiempos locales: [celda tradicional, celda Oasis]
RT = [(1.75,5.15),(2.57,7.05),(8.2,8.25),(8.7,8.75),(8.95,9.0),(9.2,9.25),(9.45,9.5),(10.0,10.0)]
rows_html = ""
for i,(lab,a,b) in enumerate(ROWS):
    y = 420 + i*100
    rows_html += f"""    <div class="s09-row" id="s09-r{i}" style="top:{y}px">
      <div class="s09-lab">{lab}</div>
      <div class="s09-a" id="s09-a{i}"><span class="ic x">{CROSS}</span>{a}</div>
      <div class="s09-b" id="s09-b{i}"><span class="ic v">{CHECK}</span>{b}</div>
    </div>
"""
S09 = scene("s09", 1080, 1920, """
#s09-colb{position:absolute;left:640px;top:300px;width:390px;height:930px;border-radius:32px;background:linear-gradient(180deg,rgba(23,84,207,.32),rgba(23,84,207,.14));border:2px solid rgba(59,130,246,.55);}
.s09-h{position:absolute;top:322px;font-size:32px;font-weight:700;line-height:1.1;}
#s09-ha{left:340px;width:280px;color:#94A3B8;}
#s09-hb{left:664px;width:350px;font-family:'Syne';font-weight:700;font-size:36px;}
.s09-row{position:absolute;left:40px;width:1000px;height:100px;border-top:1.5px solid rgba(148,163,184,.14);}
.s09-lab{position:absolute;left:10px;top:22px;width:280px;font-size:28px;font-weight:600;line-height:1.1;color:#CBD5E1;}
.s09-a{position:absolute;left:300px;top:20px;width:290px;font-size:28px;font-weight:500;line-height:1.15;color:#94A3B8;display:flex;gap:10px;align-items:flex-start;}
.s09-b{position:absolute;left:624px;top:18px;width:370px;font-size:31px;font-weight:700;line-height:1.12;color:#F8FAFB;display:flex;gap:12px;align-items:flex-start;}
.ic{flex:none;width:30px;height:30px;margin-top:2px;}
.ic.x{color:rgba(239,68,68,.7);} .ic.v{color:#22C55E;}
.ic svg{width:100%;height:100%;}
#s09-note{position:absolute;left:50px;top:1236px;font-size:28px;color:#64748B;}
#s09-final{position:absolute;left:60px;top:640px;width:960px;padding:56px 40px;border-radius:40px;background:rgba(5,7,13,.86);border:2px solid rgba(59,130,246,.6);
  text-align:center;font-family:'Syne';font-weight:700;font-size:100px;line-height:1;letter-spacing:-0.035em;box-shadow:0 0 120px rgba(23,84,207,.45);}
""", """
    <div id="s09-table">
    <div id="s09-colb"></div>
    <div class="s09-h" id="s09-ha">Agencia tradicional</div>
    <div class="s09-h" id="s09-hb"><span class="grad">Oasis Hub</span> Studio</div>
""" + rows_html + """    <div id="s09-note">Agencia tradicional: rangos típicos del mercado.</div>
    </div>
    <div id="s09-final">La elección<br>es <span class="blue">obvia.</span></div>
""", """
    tl.fromTo("#s09-ha", { opacity: 0 }, { opacity: 1, duration: .3 }, 0.2);
    tl.fromTo("#s09-colb", { opacity: 0, scaleY: .96 }, { opacity: 1, scaleY: 1, duration: .5, ease: EASE, transformOrigin: "50% 0%" }, 4.0);
    tl.fromTo("#s09-hb", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 4.1);
    const RT = """ + str([list(x) for x in RT]) + """;
    RT.forEach(([ta, tb], i) => {
      tl.fromTo(`#s09-r${i}`, { opacity: 0 }, { opacity: 1, duration: .25 }, Math.min(ta, tb) - 0.05);
      tl.fromTo(`#s09-a${i}`, { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: .3, ease: EASE }, ta);
      tl.fromTo(`#s09-b${i}`, { opacity: 0, x: 24, filter: "blur(6px)" }, { opacity: 1, x: 0, filter: "blur(0px)", duration: .32, ease: EASE }, tb);
    });
    tl.fromTo("#s09-note", { opacity: 0 }, { opacity: 1, duration: .3 }, 2.9);
    tl.to("#s09-table", { opacity: .28, filter: "blur(3px)", duration: .3, ease: "power2.inOut" }, 11.85);
    tl.fromTo("#s09-final", { opacity: 0, scale: 1.08, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: .35, ease: EASE }, 11.95);
    tl.to(["#s09-final", "#s09-table"], { opacity: 0, y: -120, filter: "blur(10px)", duration: .28, ease: "power3.in" }, 13.5);
""")

# ---------- S10 TODO INCLUIDO (11 s) ----------
ITEMS = [("Diseño a la medida para tu marca",1.2),("Celular, tablet y computadora",1.75),("Botón de WhatsApp y formularios",2.36),
         ("SEO inicial para Google",3.94),("Hosting seguro + SSL",5.1),("1er año de mantenimiento",6.86),("Google Business optimizado",8.74)]
S10 = scene("s10", 1080, 1920, """
#s10-t{position:absolute;left:60px;top:296px;font-family:'Syne';font-weight:700;font-size:104px;line-height:1;letter-spacing:-0.035em;}
.s10-i{position:absolute;left:60px;width:960px;height:96px;display:flex;align-items:center;gap:26px;font-size:42px;font-weight:600;}
.s10-c{flex:none;width:64px;height:64px;border-radius:50%;background:rgba(34,197,94,.16);border:2px solid rgba(34,197,94,.6);color:#22C55E;padding:12px;}
.s10-c svg{width:100%;height:100%;}
.s10-c path{stroke-dasharray:100 120;}
#s10-free{margin-left:6px;padding:6px 20px;border-radius:14px;background:#22C55E;color:#052E16;font-size:34px;font-weight:700;letter-spacing:.04em;}
""", """
    <h2 id="s10-t">Todo <span class="blue">incluido</span></h2>
""" + "".join(f"""    <div class="s10-i" id="s10-i{i}" style="top:{450+i*110}px"><span class="s10-c">{CHECK}</span><span>{t}</span>{'<span id="s10-free">GRATIS</span>' if i==6 else ''}</div>
""" for i,(t,_) in enumerate(ITEMS)), """
    tl.fromTo("#s10-t", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 0.15);
    const IT = """ + str([t for _,t in ITEMS]) + """;
    IT.forEach((t, i) => {
      tl.fromTo(`#s10-i${i}`, { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: .4, ease: EASE }, t - 0.1);
      tl.fromTo(`#s10-i${i} path`, { strokeDashoffset: 100 }, { strokeDashoffset: 0, duration: .3, ease: "power2.out" }, t + 0.05);
    });
    tl.fromTo("#s10-free", { opacity: 0, scale: .4 }, { opacity: 1, scale: 1, duration: .35, ease: "back.out(2.2)" }, 9.8);
    tl.to(["#s10-t", ...IT.map((_, i) => `#s10-i${i}`)], { opacity: 0, x: 60, filter: "blur(8px)", duration: .25, ease: "power3.in", stagger: .02 }, 10.6);
""")

# ---------- S11 PROCESO (6.7 s) ----------
STEPS = [("Nos escribes<br>por WhatsApp",0.19),("Diseñamos<br>tu sitio",1.53),("<span class='blue'>En línea en<br>2–3 días</span>",2.93)]
S11 = scene("s11", 1080, 1920, """
#s11-t{position:absolute;left:60px;top:300px;font-family:'Syne';font-weight:700;font-size:84px;line-height:1;letter-spacing:-0.035em;}
#s11-track{position:absolute;left:200px;top:596px;width:680px;height:8px;border-radius:4px;background:rgba(148,163,184,.22);}
#s11-fill{position:absolute;left:0;top:0;width:100%;height:100%;border-radius:4px;background:#3B82F6;transform-origin:0 50%;}
.s11-n{position:absolute;top:540px;width:120px;height:120px;border-radius:50%;background:#0B1220;border:3px solid rgba(148,163,184,.35);display:flex;align-items:center;justify-content:center;
  font-family:'Syne';font-weight:700;font-size:56px;color:#94A3B8;}
.s11-l{position:absolute;top:700px;width:330px;text-align:center;font-size:40px;font-weight:600;line-height:1.15;}
#s11-days{position:absolute;left:120px;top:930px;width:840px;display:flex;gap:24px;}
.s11-d{flex:1;height:170px;border-radius:28px;background:rgba(255,255,255,.05);border:2px solid rgba(148,163,184,.2);display:flex;flex-direction:column;align-items:center;justify-content:center;}
.s11-d b{font-family:'Syne';font-size:72px;line-height:1;}
.s11-d span{font-size:30px;color:#94A3B8;margin-top:6px;}
#s11-live{position:absolute;left:310px;top:1130px;width:460px;height:96px;border-radius:48px;background:#22C55E;color:#052E16;display:flex;align-items:center;justify-content:center;gap:14px;font-size:40px;font-weight:700;}
#s11-live svg{width:40px;height:40px;}
""", """
    <h2 id="s11-t">Así de <span class="blue">simple</span></h2>
    <div id="s11-track"><div id="s11-fill"></div></div>
""" + "".join(f"""    <div class="s11-n" id="s11-n{i}" style="left:{140+i*340}px">{i+1}</div>
    <div class="s11-l" id="s11-l{i}" style="left:{35+i*340}px">{t}</div>
""" for i,(t,_) in enumerate(STEPS)) + """    <div id="s11-days">""" + "".join(f'<div class="s11-d" id="s11-d{i}"><span>Día</span><b>{i+1}</b></div>' for i in range(3)) + """</div>
    <div id="s11-live">""" + CHECK + """En línea</div>
""", """
    tl.fromTo("#s11-t", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: .2 }, 0.0);
    const ST = """ + str([t for _,t in STEPS]) + """;
    tl.fromTo("#s11-fill", { scaleX: 0 }, { scaleX: 0, duration: .01 }, 0);
    ST.forEach((t, i) => {
      tl.fromTo(`#s11-n${i}`, { scale: .7, opacity: .4 }, { scale: 1, opacity: 1, borderColor: "#3B82F6", color: "#F8FAFB", backgroundColor: "#1754CF", duration: .4, ease: "back.out(2)" }, t);
      tl.fromTo(`#s11-l${i}`, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: .35, ease: EASE }, t + 0.05);
      if (i < 2) tl.to("#s11-fill", { scaleX: (i + 1) / 2, duration: 1.0, ease: "power2.inOut" }, t + 0.3);
    });
    [3.1, 3.45, 3.8].forEach((t, i) => tl.fromTo(`#s11-d${i}`, { opacity: .25 }, { opacity: 1, borderColor: "#3B82F6", backgroundColor: "rgba(23,84,207,.25)", duration: .25 }, t));
    tl.fromTo("#s11-days", { opacity: 0 }, { opacity: 1, duration: .3 }, 2.9);
    tl.fromTo("#s11-live", { opacity: 0, scale: .6 }, { opacity: 1, scale: 1, duration: .4, ease: "back.out(2)" }, 4.15);
    tl.to(["#s11-t","#s11-track","#s11-n0","#s11-n1","#s11-n2","#s11-l0","#s11-l1","#s11-l2","#s11-days","#s11-live"], { opacity: 0, filter: "blur(8px)", duration: .25, ease: "power2.in" }, 6.4);
""")

# ---------- S12 CTA (8.6 s) ----------
S12 = scene("s12", 1080, 1920, """
#s12-lock{position:absolute;left:0;top:290px;width:1080px;display:flex;align-items:center;justify-content:center;gap:18px;}
#s12-lock img{width:150px;}
#s12-lock span{font-family:'Syne';font-weight:700;font-size:54px;letter-spacing:-0.03em;}
#s12-h{position:absolute;left:60px;top:430px;width:960px;text-align:center;font-family:'Syne';font-weight:700;font-size:96px;line-height:1;letter-spacing:-0.035em;}
#s12-price{position:absolute;left:0;top:670px;width:1080px;text-align:center;font-family:'Syne';font-weight:800;font-size:190px;line-height:1;letter-spacing:-0.05em;}
#s12-glow{position:absolute;left:140px;top:620px;width:800px;height:320px;border-radius:50%;background:radial-gradient(closest-side,rgba(59,130,246,.45),transparent);}
#s12-btn{position:absolute;left:110px;top:910px;width:860px;height:140px;border-radius:70px;background:#22C55E;color:#052E16;display:flex;align-items:center;justify-content:center;gap:20px;
  font-size:50px;font-weight:700;box-shadow:0 24px 60px rgba(34,197,94,.4);}
#s12-btn svg{width:60px;height:60px;}
#s12-url{position:absolute;left:0;top:1086px;width:1080px;text-align:center;font-size:46px;font-weight:700;}
#s12-tel{position:absolute;left:0;top:1150px;width:1080px;text-align:center;font-size:42px;font-weight:500;color:#94A3B8;}
""", """
    <div id="s12-glow"></div>
    <div id="s12-lock"><img src="assets/brand/logo_mark.png" alt=""><span><span class="grad">Oasis Hub</span> Studio</span></div>
    <h2 id="s12-h">""" + words("Tu website listo", base_id="s12a") + """ <span class="blue">""" + words("esta semana.", base_id="s12b") + """</span></h2>
    <div id="s12-price">$249</div>
    <div id="s12-btn">""" + CHAT_ICON + """Escríbenos por WhatsApp</div>
    <div id="s12-url">oasishub.studio</div>
    <div id="s12-tel">+506 6469 2948</div>
""", """
    tl.fromTo("#s12-lock", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: .4, ease: EASE }, 0.0);
    [0.16, 0.32, 1.06].forEach((t, i) => tl.fromTo(`#s12a-${i}`, { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .14 }, t));
    [1.32, 1.58].forEach((t, i) => tl.fromTo(`#s12b-${i}`, { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: .14 }, t));
    tl.set("#s12-price", { opacity: 1, scale: 1.25 }, 2.22);
    tl.fromTo("#s12-price", { opacity: 0 }, { opacity: 0, duration: .01 }, 0);
    tl.to("#s12-price", { scale: 1, duration: .22, ease: "expo.out" }, 2.22);
    tl.fromTo("#s12-glow", { opacity: 0 }, { opacity: 1, duration: .05 }, 2.22);
    tl.to("#s12-glow", { opacity: .5, duration: .8 }, 2.3);
    tl.fromTo("#s12-btn", { opacity: 0, scale: .7 }, { opacity: 1, scale: 1, duration: .5, ease: "back.out(1.8)" }, 4.1);
    tl.fromTo("#s12-url", { opacity: 0 }, { opacity: 1, duration: .3 }, 4.5);
    tl.fromTo("#s12-tel", { opacity: 0 }, { opacity: 1, duration: .3 }, 4.65);
    [5.3, 6.4].forEach(t => { tl.to("#s12-btn", { scale: 1.045, duration: .18, ease: "power2.out" }, t); tl.to("#s12-btn", { scale: 1, duration: .35, ease: "power2.inOut" }, t + .18); });
""")
