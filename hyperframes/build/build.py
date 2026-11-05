# Genera compositions/*.html e index.html del master 9:16.  Uso: cd hyperframes && python3 build/build.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import FONTS
from scenes_a import S01, S02, S03, S04
from scenes_b import S05, S06, S07
from scenes_c import S08, S09, S10, S11, S12
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCENES = [("s01",0.0,3.0,S01),("s02",3.0,6.0,S02),("s03",9.0,6.2,S03),("s04",15.2,5.8,S04),("s05",21.0,7.0,S05),("s06",28.0,8.0,S06),
          ("s07",36.0,8.0,S07),("s08",44.0,4.4,S08),("s09",48.4,13.8,S09),("s10",62.2,11.0,S10),("s11",73.2,6.7,S11),("s12",79.9,8.6,S12)]
TOTAL = 88.5
for cid,_,_,html in SCENES:
    open(f"{HERE}/compositions/{cid}.html","w").write(html)
lines = json.load(open(f"{HERE}/../assets/audio/vo/lines.json"))
hosts = "\n".join(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{st}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:2"></div>' for cid,st,d,_ in SCENES)
import subprocess
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
vo = "\n".join(f'      <audio id="vo-{n[:2]}" class="clip" src="assets/audio/{n}.mp3" data-start="{t}" data-duration="{dur(f"{HERE}/assets/audio/{n}.mp3"):.2f}" data-track-index="{3 + i % 2}" data-volume="1"></audio>' for i,(n,t,_) in enumerate(lines))
index = f"""<!doctype html>
<html lang="es" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      {FONTS}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #05070D; }}
      #root {{ width: 100%; height: 100%; position: relative; font-family: 'DM Sans', sans-serif; }}
      #ground {{ position: absolute; inset: 0; z-index: 0;
        background: radial-gradient(90% 55% at 50% 38%, #0F1A2E 0%, #0B1220 45%, #05070D 100%); }}
      #grain {{ position: absolute; inset: 0; z-index: 50; pointer-events: none; opacity: .07; mix-blend-mode: overlay;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="ground" data-layout-ignore></div>
{hosts}
      <div id="grain" data-layout-ignore></div>
      <audio id="music" class="clip" src="assets/audio/music.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-volume="0.5" data-fade-out="2"></audio>
{vo}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
open(f"{HERE}/index.html","w").write(index)
print("ok", len(SCENES), "scenes")
