# Piezas compartidas para generar las escenas (fuentes, paleta, mockups, íconos).
FONTS = """
@font-face{font-family:'Syne';src:url('assets/fonts/Syne-normal-latin-variable.woff2') format('woff2');font-weight:400 800;}
@font-face{font-family:'DM Sans';src:url('assets/fonts/DMSans-normal-latin-variable.woff2') format('woff2');font-weight:100 1000;}
"""
BASE = FONTS + """
#root{position:absolute;inset:0;overflow:hidden;font-family:'DM Sans',sans-serif;color:#F8FAFB;}
#root *{box-sizing:border-box;margin:0;padding:0;}
.syne{font-family:'Syne',sans-serif;}
.blue{color:#3B82F6;}
.grad{background:linear-gradient(90deg,#1754CF,#3B82F6 55%,#60A5FA);-webkit-background-clip:text;background-clip:text;color:transparent;}
.muted{color:#94A3B8;}
.abs{position:absolute;}
.w{display:inline-block;}
.pill-real{position:absolute;left:60px;top:292px;display:flex;align-items:center;gap:14px;padding:12px 26px 12px 20px;border-radius:999px;
  background:rgba(34,197,94,.10);border:1.5px solid rgba(34,197,94,.45);font-size:30px;font-weight:600;color:#BBF7D0;}
.pill-real .dot{width:14px;height:14px;border-radius:50%;background:#22C55E;box-shadow:0 0 14px #22C55E;}
/* Mockups genéricos (sin logos) */
.imac{position:absolute;}
.imac .bezel{background:#0A0A0C;border-radius:24px 24px 0 0;padding:20px;box-shadow:0 0 0 2px #2a2d33 inset;}
.imac .chin{height:62px;border-radius:0 0 24px 24px;background:linear-gradient(180deg,#e3e6eb,#b9bfc8);}
.imac .neck{width:190px;height:96px;margin:0 auto;background:linear-gradient(180deg,#9aa1ab,#cfd4db 40%,#a9b0b9);clip-path:polygon(12% 0,88% 0,100% 100%,0 100%);}
.imac .foot{width:330px;height:14px;margin:0 auto;border-radius:7px;background:linear-gradient(180deg,#d7dbe1,#9aa1ab);}
.mbp{position:absolute;}
.mbp .lid{background:#0B0B0D;border-radius:26px 26px 6px 6px;padding:20px 18px 26px;box-shadow:0 0 0 2px #2c2f35 inset;}
.mbp .base{position:relative;left:-56px;width:calc(100% + 112px);height:30px;border-radius:2px 2px 22px 22px;
  background:linear-gradient(180deg,#d9dde3 0%,#aab0ba 60%,#7d838d 100%);}
.mbp .base:after{content:'';position:absolute;left:50%;top:0;width:150px;height:9px;margin-left:-75px;border-radius:0 0 10px 10px;background:#8e949e;}
.screen{position:relative;overflow:hidden;background:#fff;}
.screen img{position:absolute;left:0;top:0;width:100%;display:block;}
.iphone{position:absolute;border-radius:54px;background:#0d0d10;padding:11px;box-shadow:0 0 0 2px #3a3d44, 0 40px 80px rgba(0,0,0,.6);}
.iphone .screen{border-radius:44px;}
.iphone .island{position:absolute;left:50%;top:22px;width:84px;height:24px;margin-left:-42px;border-radius:14px;background:#000;z-index:3;}
.shadow{box-shadow:0 50px 90px rgba(0,0,0,.6);}
"""
# Ícono de chat con teléfono (genérico, estilo WhatsApp sin usar el logo oficial)
CHAT_ICON = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M9.2 8.4c.3-.5.9-.5 1.1 0l.6 1.3c.1.3 0 .6-.2.8l-.5.5a5 5 0 0 0 2.8 2.8l.5-.5c.2-.2.5-.3.8-.2l1.3.6c.5.2.5.8 0 1.1-.6.5-1.4.8-2.2.6a7 7 0 0 1-4.8-4.8c-.2-.8.1-1.6.6-2.2Z" fill="currentColor" stroke="none"/></svg>"""
CHECK = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path pathLength="100" d="M5 12.5l4.5 4.5L19 7.5"/></svg>"""
CROSS = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>"""
SEARCH = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>"""
PERSON = """<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7z"/></svg>"""

def scene(cid, w, h, css, body, js):
    return f"""<template>
  <style>{BASE}
{css}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{w}" data-height="{h}">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const EASE = "expo.out";
{js}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
