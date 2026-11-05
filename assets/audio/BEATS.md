# Música — `music.mp3`

Pista instrumental generada con **ElevenLabs Music** (`music_v1`). El plan de composición está en `music_plan.json`; para regenerarla, haz POST de ese archivo a `https://api.elevenlabs.io/v1/music`.

- Duración del archivo: 90.0 s (la música suena hasta ~83.3 s y termina en silencio desde ~84.8 s)
- Tempo objetivo: 118 BPM (1 compás ≈ 2.03 s)
- Loudness original: -12.4 LUFS integrado, pico real +0.3 dBFS. **Normalizar a -14 LUFS / -1 dBTP en la mezcla final (Fase 6).**

## Mapa de secciones (medido sobre la forma de onda)

| Tiempo | Sección | Escenas del brief |
|---|---|---|
| 0:00–0:08 | Tensión: pulso filtrado, hi-hat, acentos glitch | 1–2 (hook) |
| 0:08–0:14.7 | Subida con sweep y redoble | 3 (reveal) |
| 0:14.7–0:15.2 | Corte de silencio antes del drop | — |
| **0:15.2** | **DROP**: bajo y batería completos | **4 — slam del $249 (alinear aquí)** |
| 0:15–1:05 | Groove continuo con energía alta | 5–9 (portafolio + comparación) |
| ~1:05–1:23 | Baja la densidad y vuelve a construir con acordes | 10–12 (checklist, proceso, CTA) |
| ~1:23 | Final resuelto / fade | fin del CTA |

**Nota de montaje:** el master puede durar ~84 s para terminar con la música, o hay que extender la cola con un fade/eco si el CTA necesita llegar a 90 s.
