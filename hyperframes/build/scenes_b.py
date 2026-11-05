from common import *

def portfolio(cid, dur, name, industry, slug, device, tint, stops_d, stops_m, extra_css="", extra_body="", extra_js="", exit_js=""):
    """Escena de portafolio: pill 'Proyecto real', nombre, industria, desktop + iPhone con scroll real."""
    SW, SH = 900, 562          # pantalla desktop (16:10)
    PW, PH = 236, 511          # pantalla iPhone (390x844)
    rd, rm = SW / 1440, PW / 390
    if device == "imac":
        dev = f"""<div class="imac" id="{cid}-dev" style="left:70px;top:560px;width:940px">
        <div class="bezel"><div class="screen" style="width:{SW}px;height:{SH}px"><img id="{cid}-dimg" src="assets/sites/{slug}_desktop.jpg"></div></div>
        <div class="chin"></div><div class="neck"></div><div class="foot"></div></div>"""
    else:
        dev = f"""<div class="mbp" id="{cid}-dev" style="left:72px;top:600px;width:936px">
        <div class="lid"><div class="screen" style="width:{SW}px;height:{SH}px;border-radius:6px"><img id="{cid}-dimg" src="assets/sites/{slug}_desktop.jpg"></div></div>
        <div class="base"></div></div>"""
    phone = f"""<div class="iphone" id="{cid}-ph" style="left:772px;top:830px;width:{PW+22}px;height:{PH+22}px"><div class="island" style="width:64px;height:20px;margin-left:-32px;top:20px"></div>
        <div class="screen" style="width:{PW}px;height:{PH}px;border-radius:40px"><img id="{cid}-mimg" src="assets/sites/{slug}_mobile.jpg"></div></div>"""
    css = f"""
#{cid}-tint{{position:absolute;left:-100px;top:420px;width:1280px;height:1000px;border-radius:50%;background:radial-gradient(closest-side,{tint},transparent);}}
#{cid}-name{{position:absolute;left:60px;top:378px;width:960px;font-family:'Syne';font-weight:700;font-size:88px;line-height:1;letter-spacing:-0.035em;white-space:nowrap;}}
#{cid}-ind{{position:absolute;left:62px;top:480px;font-size:42px;font-weight:500;color:#94A3B8;}}
#{cid}-cam{{position:absolute;inset:0;}}
""" + extra_css
    body = f"""
    <div id="{cid}-tint"></div>
    <div class="pill-real" id="{cid}-pill"><span class="dot"></span>Proyecto real · En línea hoy</div>
    <h2 id="{cid}-name">{name}</h2>
    <div id="{cid}-ind">{industry}</div>
    <div id="{cid}-cam">
      {dev}
      {phone}
    </div>
""" + extra_body
    js = f"""
    tl.fromTo("#{cid}-tint", {{ opacity: 0 }}, {{ opacity: 1, duration: .8, ease: "power2.out" }}, 0);
    tl.fromTo("#{cid}-dev", {{ opacity: 0, x: 220, filter: "blur(14px)" }}, {{ opacity: 1, x: 0, filter: "blur(0px)", duration: .55, ease: EASE }}, 0.0);
    tl.fromTo("#{cid}-ph", {{ opacity: 0, x: 260, filter: "blur(14px)" }}, {{ opacity: 1, x: 0, filter: "blur(0px)", duration: .6, ease: EASE }}, 0.14);
    tl.fromTo("#{cid}-name", {{ opacity: 0, filter: "blur(8px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: .2, ease: "power2.out" }}, 0.25);
    tl.fromTo("#{cid}-ind", {{ opacity: 0 }}, {{ opacity: 1, duration: .25 }}, 0.55);
    tl.fromTo("#{cid}-pill", {{ opacity: 0, scale: .9 }}, {{ opacity: 1, scale: 1, duration: .35, ease: "back.out(1.7)" }}, 1.9);
    const sd = {stops_d}, sm = {stops_m};   // [tiempo, y CSS] del scroll real
    for (let i = 1; i < sd.length; i++) tl.fromTo("#{cid}-dimg", {{ y: -sd[i-1][1] * {rd:.5f} }}, {{ y: -sd[i][1] * {rd:.5f}, duration: sd[i][0] - sd[i-1][2], ease: "power2.inOut", immediateRender: false }}, sd[i-1][2]);
    for (let i = 1; i < sm.length; i++) tl.fromTo("#{cid}-mimg", {{ y: -sm[i-1][1] * {rm:.5f} }}, {{ y: -sm[i][1] * {rm:.5f}, duration: sm[i][0] - sm[i-1][2], ease: "power2.inOut", immediateRender: false }}, sm[i-1][2]);
""" + extra_js + exit_js
    return scene(cid, 1080, 1920, css, body, js)

WHIP_OUT = lambda cid, t: f"""
    tl.to(["#{cid}-cam", "#{cid}-name", "#{cid}-ind", "#{cid}-pill", "#{cid}-tint"], {{ x: -900, opacity: 0, filter: "blur(16px)", duration: .3, ease: "power3.in" }}, {t});
"""

# stops: [fin_del_tramo, y_destino, inicio_del_tramo]; el primero es [0, y0, t_inicio]
S05 = portfolio("s05", 7.0, "Melo Kombucha", "Bebidas · Costa Rica", "melo", "imac", "rgba(232,200,119,.22)",
    "[[0,0,0.9],[3.0,2560,4.4],[5.6,4020,0]]", "[[0,0,1.0],[3.1,4129,4.5],[5.7,5132,0]]",
    exit_js=WHIP_OUT("s05", 6.7))

S06 = portfolio("s06", 8.0, "Barahona Caribbean Stay", "Hospedaje · Limón, CR", "barahona", "mbp", "rgba(45,110,90,.28)",
    "[[0,0,0.7],[2.2,1530,3.0],[4.6,4870,0]]", "[[0,0,0.8],[2.3,1668,3.1],[4.7,4909,0]]",
    extra_css="""
#s06-name{font-size:68px !important;top:388px !important;}
#s06-chip{position:absolute;left:60px;top:1110px;display:flex;align-items:center;gap:18px;padding:22px 34px 22px 26px;border-radius:999px;background:#22C55E;color:#052E16;
  font-size:40px;font-weight:700;box-shadow:0 20px 50px rgba(34,197,94,.35);}
#s06-chip svg{width:46px;height:46px;}
""", extra_body="""    <div id="s06-chip">""" + CHAT_ICON + """Reservas directo a WhatsApp</div>
""", extra_js="""
    tl.fromTo("#s06-chip", { opacity: 0, y: 40, scale: .9 }, { opacity: 1, y: 0, scale: 1, duration: .45, ease: "back.out(1.6)" }, 2.1);
""", exit_js="""
    tl.to("#s06-chip", { x: -900, opacity: 0, filter: "blur(16px)", duration: .3, ease: "power3.in" }, 7.7);
""" + WHIP_OUT("s06", 7.7))

S07 = portfolio("s07", 8.0, "Proyecto Ecogreen", "Paisajismo · Vivero", "ecogreen", "mbp", "rgba(76,140,60,.26)",
    "[[0,0,0.7],[2.0,1000,2.6],[4.0,2600,0]]", "[[0,0,0.8],[2.1,2168,2.7],[4.1,4017,0]]",
    extra_css="""
#s07-chip{position:absolute;left:60px;top:1110px;padding:20px 32px;border-radius:999px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);font-size:38px;font-weight:600;}
""", extra_body="""    <div id="s07-chip">Diseñamos jardines <span style="color:#86EFAC">con propósito</span></div>
""", extra_js="""
    tl.fromTo("#s07-chip", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: .4, ease: EASE }, 1.7);
    // punch-in a la tabla comparativa real del sitio
    tl.to(["#s07-ph", "#s07-chip", "#s07-ind"], { opacity: 0, filter: "blur(8px)", duration: .3, ease: "power2.in" }, 4.3);
    tl.to("#s07-cam", { scale: 1.36, duration: .6, ease: "power2.inOut", transformOrigin: "50% 64%" }, 4.4);
""", exit_js="""
    tl.to(["#s07-cam", "#s07-name", "#s07-ind", "#s07-pill", "#s07-chip", "#s07-tint"], { opacity: 0, scale: .9, filter: "blur(12px)", duration: .3, ease: "power3.in" }, 7.7);
""")
