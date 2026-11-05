"""Genera la voz en off con ElevenLabs y la mezcla de prueba.
Uso: python3 scripts/gen_vo.py VOICE_ID [--mix-only]   (la key la inyecta el proxy del entorno)"""
import json, subprocess, sys
VOICE = sys.argv[1]
L = json.load(open('assets/audio/vo/lines.json'))
SPEED = {"10_incluido": 1.15}
DEFAULT_SPEED = 1.1
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
MIX_ONLY = "--mix-only" in sys.argv
for i,(n,t,txt) in enumerate([] if MIX_ONLY else L):
    vs={"stability":0.5,"similarity_boost":0.8,"style":0.25,"use_speaker_boost":True,"speed":SPEED.get(n,DEFAULT_SPEED)}
    body={"text":txt,"model_id":"eleven_multilingual_v2","language_code":"es","seed":249,"voice_settings":vs}
    if i>0: body["previous_text"]=L[i-1][2]
    if i<len(L)-1: body["next_text"]=L[i+1][2]
    out=f"assets/audio/vo/{n}.mp3"
    code=subprocess.run(["curl","-sS","-m","120","-X","POST",f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_192",
        "-H","xi-api-key: dummy","-H","Content-Type: application/json","-d",json.dumps(body),"-o",out,"-w","%{http_code}"],capture_output=True,text=True).stdout
    nxt=L[i+1][1] if i<len(L)-1 else 86.0
    print(f"{n} {code} {dur(out):.2f}s / ventana {nxt-t:.1f}s")

# ---- Layout: cada línea entra en su ancla de escena o 0.4 s después de que termina la anterior ----
import re as _re
ANCHOR = {"01_hook":0.0,"02_problema":3.0,"03_reveal":8.0,"04_oferta":15.2,"05_melo":20.5,"06_barahona":28.0,
          "07_ecogreen":36.0,"08_grid":44.0,"09_comparacion":48.0,"10_incluido":62.0,"11_proceso":72.0,"12_cta":80.0}
def speech_end(p):
    o=subprocess.run(["ffmpeg","-hide_banner","-i",p,"-af","silencedetect=n=-45dB:d=0.1","-f","null","-"],capture_output=True,text=True).stderr
    st=[float(x) for x in _re.findall(r"silence_start: ([0-9.]+)",o)]; en=[float(x) for x in _re.findall(r"silence_end: ([0-9.]+)",o)]
    d=dur(p); return st[-1] if st and (len(en)<len(st) or en[-1]>=d-0.05) else d
end=0.0
for row in L:
    n=row[0]; p=f"assets/audio/vo/{n}.mp3"
    row[1]=round(max(ANCHOR[n], end+0.4 if end else 0),2)
    end=row[1]+speech_end(p)
    print(f"{n}: {row[1]:6.2f} -> {end:6.2f}  (ancla {ANCHOR[n]})")
json.dump(L,open('assets/audio/vo/lines.json','w'),ensure_ascii=False,indent=1)
TOTAL=round(end+3.0,1); print("Duración sugerida del master:",TOTAL)
# ---- Mezcla de prueba ----
inputs=[];f=[]
for i,(n,t,_) in enumerate(L):
    inputs+=["-i",f"assets/audio/vo/{n}.mp3"]; ms=int(t*1000); f.append(f"[{i}:a]aresample=48000,adelay={ms}|{ms}[v{i}]")
k=len(L); f.append("".join(f"[v{i}]" for i in range(k))+f"amix=inputs={k}:normalize=0,apad=whole_dur={TOTAL}[vo]")
subprocess.run(["ffmpeg","-y","-v","error",*inputs,"-filter_complex",";".join(f),"-map","[vo]","-ac","2","/tmp/vo_stem.wav"],check=True)
fc=(f"[0:a]aresample=48000,volume=-4dB,apad=whole_dur={TOTAL}[m];[1:a]asplit=2[vo1][vo2];"
    "[m][vo1]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[md];"
    "[md][vo2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.83:level=false[out]")
subprocess.run(["ffmpeg","-y","-v","error","-i","assets/audio/music.mp3","-i","/tmp/vo_stem.wav","-filter_complex",fc,"-map","[out]","-ar","48000","-b:a","192k","assets/audio/preview_mix.mp3"],check=True)
