# Voz en off: guion y clips

- **Voz:** ElevenLabs `AwmgI32PB22lsT7wnBFH` · modelo `eleven_multilingual_v2` · español · seed 249 · velocidad 1.1 (línea 10: 1.15)
- **Clips:** `assets/audio/vo/` (un MP3 por escena). Los tiempos de inicio están en `assets/audio/vo/lines.json`.
- **Regenerar:** `python3 scripts/gen_vo.py AwmgI32PB22lsT7wnBFH` (genera los clips, recalcula tiempos y mezcla). Con `--mix-only` rehace solo la mezcla.
- **Mezcla de prueba:** `assets/audio/preview_mix.mp3` (88.5 s, música con ducking bajo la voz, -13.6 LUFS, pico -1.0 dBFS). Es solo una referencia: la mezcla final se hace en la Fase 6.
- Pronunciación verificada con speech-to-text (ElevenLabs Scribe): todas las líneas se transcriben correctamente.
- Los montos van escritos en palabras para la voz. En pantalla se muestran como $249, 2–3 días, etc.

| Clip | Inicio | Duración | Texto |
|---|---|---|---|
| `01_hook.mp3` | 0:00.00 | 2.3 s | ¿Tu negocio no aparece cuando te buscan? |
| `02_problema.mp3` | 0:03.00 | 6.3 s | Hoy los clientes investigan antes de comprar. Si no te encuentran… compran en otro lado. |
| `03_reveal.mp3` | 0:08.91 | 4.6 s | Oasis Hub Studio. Más de diez años creando websites que venden. |
| `04_oferta.mp3` | 0:15.20 | 5.6 s | Landing page profesional. Doscientos cuarenta y nueve dólares. Lista en dos a tres días. |
| `05_melo.mp3` | 0:21.22 | 4.1 s | Melo Kombucha. Un proyecto real, en línea hoy. |
| `06_barahona.mp3` | 0:28.00 | 4.2 s | Barahona Caribbean Stay. Reservas directo a WhatsApp. |
| `07_ecogreen.mp3` | 0:36.00 | 3.5 s | Proyecto Ecogreen. Paisajismo con propósito. |
| `08_grid.mp3` | 0:44.00 | 4.8 s | Tres industrias. Tres diseños únicos. Cero plantillas. |
| `09_comparacion.mp3` | 0:48.51 | 13.4 s | Una agencia tradicional suele cobrar más y tardar semanas. Con nosotros: doscientos cuarenta y nueve dólares, en dos a tres días, cien por ciento a la medida y con atención directa por WhatsApp. La elección es obvia. |
| `10_incluido.mp3` | 1:02.28 | 10.6 s | Todo incluido: diseño a la medida, WhatsApp y formularios, SEO inicial, hosting con SSL, el primer año de mantenimiento… y Google Business, gratis. |
| `11_proceso.mp3` | 1:13.31 | 5.0 s | Nos escribes por WhatsApp. Diseñamos tu sitio. Y en dos a tres días, estás en línea. |
| `12_cta.mp3` | 1:20.00 | 5.5 s | Tu website, listo esta semana. Doscientos cuarenta y nueve dólares. Escríbenos por WhatsApp. |

**Timing:** cada línea entra en el ancla de su escena o 0.4 s después de que termina la anterior. "$249" cae justo en el drop de la música (0:15.2). El master queda en **~88.5 s**. La música termina hacia ~1:24 y el CTA habla hasta 1:25.5, así que en la Fase 6 hay que extender la cola musical (eco/fade o loop del último compás).
