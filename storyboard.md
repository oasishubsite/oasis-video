# Storyboard — "Landing Page $249" · Oasis Hub Studio · Master 9:16

**Formato:** 1080×1920 · 30 fps · **88.5 s** · voz en off (ElevenLabs, voz `AwmgI32PB22lsT7wnBFH`) + música (ElevenLabs, 118 BPM) + texto en pantalla durante todo el video.
**Stills:** `out/stills/` (un frame por escena, 540×960). Hoja de contacto: `out/stills/_contact_sheet.jpg`.
**Fuente del video:** `hyperframes/` (las escenas se generan con `python3 hyperframes/build/build.py`).

**Safe zones (Reels/Stories):** todo el texto y el producto van en la franja **y = 270–1250 px** (libre el 14 % superior y el 35 % inferior). Debajo de 1250 px solo hay decoración (pie del iMac, base de la laptop, borde de teléfonos).

**Look:** fondo `#05070D → #0B1220` con viñeta radial y grano al 7 %. Acento `#1754CF` / `#3B82F6` / `#60A5FA`, texto `#F8FAFB` / `#94A3B8`, checks `#22C55E`, ✗ `#EF4444` al 70 %. Titulares en **Syne 700** (el precio en **Syne 800**) y cuerpo en **DM Sans**. Easing de llegada `expo.out`; salidas `power3.in`. Mockups de iMac, MacBook e iPhone dibujados en CSS, sin logos.

---

## Escenas

| # | Tiempo | Escena | Texto en pantalla (exacto) | Voz en off | Movimiento / transición | Assets |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:03.0 | **Hook** | **¿Tu negocio no aparece cuando te buscan?** ("no aparece" en azul) · barra de búsqueda: "tu negocio" · "✕ Sin resultados relevantes" | ¿Tu negocio no aparece cuando te buscan? | El titular está visible desde el frame 0 (sirve de miniatura). La barra escribe "tu negocio" letra por letra con cursor. Entra la tarjeta de resultados y "Sin resultados relevantes" hace **glitch** (RGB split). **Salida:** push hacia el resultado vacío con blur. | Íconos dibujados (lupa genérica, sin logo de Google) |
| 2 | 0:03.0–0:09.0 | **Problema** | Hoy los clientes investigan **antes de comprar.** → Si no te encuentran… **compran en otro lado.** | Hoy los clientes investigan antes de comprar. Si no te encuentran… compran en otro lado. | Las palabras aparecen con blur, sincronizadas con la voz. Teléfono con una búsqueda genérica y 8 íconos de clientes alrededor. Con "Si no te encuentran" los clientes **se van** de cuadro uno por uno. **Salida:** zoom-through a la pantalla del teléfono. | Mockup de iPhone (CSS) |
| 3 | 0:09.0–0:15.2 | **Reveal** | Logo + **Oasis Hub Studio** · **+10 años** creando websites que venden | Oasis Hub Studio. Más de diez años creando websites que venden. | La pantalla oscura se abre. El logo entra con desenfoque → nítido y halo azul, el wordmark aparece letra por letra y dos barridos de luz azul cruzan el cuadro. **Salida:** todo se apaga a los 14.7 s, justo en el silencio de la música antes del drop. | `assets/brand/logo.png` (logo real del sitio) |
| 4 | 0:15.2–0:21.0 | **Oferta héroe** | Landing page **profesional** · **$249** · pago único · **Lista en 2–3 días** · 1er año de mantenimiento incluido | Landing page profesional. $249. Lista en dos a tres días. | **Drop de la música** con "Landing page profesional". Conteo rápido 0 → 249 que termina en un **slam** con destello azul justo cuando la voz dice "$249". La pastilla "Lista en 2–3 días" entra con rebote y se llenan 3 barras (días). **Salida:** whip hacia arriba. | — |
| 5 | 0:21.0–0:28.0 | **Portafolio 1** | ● Proyecto real · En línea hoy · **Melo Kombucha** · Bebidas · Costa Rica | Melo Kombucha. Un proyecto real, en línea hoy. | Entran un iMac y un iPhone desde la derecha. **Scroll real** del sitio: hero → "Encuentra tu favorito" (sabores) → mapa con 85 puntos de venta. **Salida:** whip a la izquierda. | `melokombucha.com`: capturas desktop y móvil |
| 6 | 0:28.0–0:36.0 | **Portafolio 2** | ● Proyecto real · En línea hoy · **Barahona Caribbean Stay** · Hospedaje · Limón, CR · chip verde: **Reservas directo a WhatsApp** | Barahona Caribbean Stay. Reservas directo a WhatsApp. | MacBook + iPhone. Scroll: hero → galería "Explora el espacio" → formulario **"Reserva tu estadía"** ("Completa el formulario y escríbenos por WhatsApp"). El chip entra con la voz. **Salida:** whip a la izquierda. | `barahonastay.site` |
| 7 | 0:36.0–0:44.0 | **Portafolio 3** | ● Proyecto real · En línea hoy · **Proyecto Ecogreen** · Paisajismo · Vivero · chip: Diseñamos jardines **con propósito** | Proyecto Ecogreen: paisajismo con propósito. | MacBook + iPhone. Scroll: hero → servicios → **tabla real "Ecogreen vs Otros"**, con punch-in a la tabla (×1.36). **Salida:** se encoge con blur. | `proyectoecogreen.com` |
| 8 | 0:44.0–0:48.4 | **Grid** | 3 industrias. · 3 diseños únicos. · **Cero plantillas.** · Bebidas / Hospedaje / Paisajismo | Tres industrias. Tres diseños únicos. Cero plantillas. | Los 3 teléfonos (heroes móviles reales) se juntan en fila. Cada línea entra con la voz. **Salida:** los teléfonos caen fuera de cuadro. | Capturas móviles de los 3 sitios |
| 9 | 0:48.4–1:02.2 | **Comparación** | Tabla de 8 filas: *Agencia tradicional* (gris, ✗) vs **Oasis Hub Studio** (columna azul, ✓). Valores exactos de la tabla del brief. Nota: "Agencia tradicional: rangos típicos del mercado." Remate: **La elección es obvia.** | Una agencia tradicional suele cobrar más y tardar semanas. Con nosotros: $249, en dos a tres días, cien por ciento a la medida y con atención directa por WhatsApp. La elección es obvia. | Primero entran las celdas de la agencia (precio y tiempo) con "cobrar más / tardar semanas". Con "Con nosotros" se enciende la columna Oasis y cada ✓ entra cuando la voz lo menciona; las filas 4–7 entran en cascada. Al final la tabla se atenúa y aparece la tarjeta "La elección es obvia." | — |
| 10 | 1:02.2–1:13.2 | **Todo incluido** | **Todo incluido** · ✓ Diseño a la medida para tu marca · ✓ Celular, tablet y computadora · ✓ Botón de WhatsApp y formularios · ✓ SEO inicial para Google · ✓ Hosting seguro + SSL · ✓ 1er año de mantenimiento · ✓ Google Business optimizado **GRATIS** | Todo incluido: diseño a la medida, WhatsApp y formularios, SEO inicial, hosting con SSL, el primer año de mantenimiento… y Google Business, gratis. | Cada ítem entra cuando la voz lo nombra y su ✓ se dibuja. El sello "GRATIS" aparece con la palabra "gratis". **Salida:** la lista sale hacia la derecha con blur. | — |
| 11 | 1:13.2–1:19.9 | **Proceso** | Así de **simple** · 1 Nos escribes por WhatsApp · 2 Diseñamos tu sitio · 3 **En línea en 2–3 días** · Día 1 / Día 2 / Día 3 · ✓ En línea | Nos escribes por WhatsApp. Diseñamos tu sitio. Y en dos a tres días, estás en línea. | Timeline horizontal: cada nodo se enciende con su paso y la línea azul avanza. Luego se iluminan los bloques Día 1 → 2 → 3 y entra el sello verde "✓ En línea" con "estás en línea". | — |
| 12 | 1:19.9–1:28.5 | **CTA final** | Logo + Oasis Hub Studio · **Tu website listo esta semana.** · **$249** · botón verde **Escríbenos por WhatsApp** · oasishub.studio · +506 6469 2948 | Tu website, listo esta semana. $249. Escríbenos por WhatsApp. | El titular entra palabra por palabra, "$249" hace slam con destello y el botón entra con rebote y pulsa 2 veces. **Últimos 3 s: todo quieto y legible.** | Logo real |

**$249** aparece en las escenas 4, 9 y 12 (y en la voz 3 veces). **2–3 días** aparece en las escenas 4, 9 y 11.

---

## Audio
- **Música:** `assets/audio/music.mp3`. El drop cae a los 15.2 s, justo en la escena 4. La pista termina hacia 1:24, así que en la Fase 6 se extiende la cola bajo el CTA.
- **Voz:** 12 clips en `assets/audio/vo/`. Cada texto en pantalla se sincroniza con los tiempos por palabra de `words.json` (ElevenLabs Scribe).
- **Mezcla final (Fase 6):** ducking de la música bajo la voz, -14 LUFS, picos ≤ -1 dBTP.

## Decisión técnica: todo en HyperFrames (propuesta)
El brief pide hacer en Remotion las escenas de datos (4, 9, 10, 11). Propongo hacerlas en **HyperFrames**, dentro del mismo timeline, porque:
1. Hay **un solo motor y un solo render**: mismas fuentes, colores y antialiasing en todo el video, sin clips ProRes con alpha que importar.
2. Los cortes **4:5, 1:1, 30 s y 15 s** se arman re-maquetando las mismas escenas. Con Remotion habría que re-renderizar cada clip para cada formato.
3. Ya están construidas y sincronizadas con la voz (ver stills 04, 09a, 09b, 10 y 11).

Las skills de Remotion quedan instaladas. Si prefieres la arquitectura original, la cambio.

## Cumplimiento (sección 1 del brief)
- No se menciona dominio ni correo incluidos.
- No hay testimonios, estrellas, cantidades de clientes ni métricas. La tabla de Ecogreen y el mapa de Melo son contenido real de esos sitios; no se presentan como resultados de Oasis.
- La comparación es contra una "Agencia tradicional" genérica, con la nota "rangos típicos del mercado".
- No hay logos de Google, Meta ni Apple. La lupa, los mockups y el ícono de chat son genéricos (no se usa el logo oficial de WhatsApp).

## Preguntas para tu aprobación
1. ¿Apruebas el guion y los stills tal como están?
2. ¿Te parece bien hacer todo en HyperFrames en vez de usar Remotion para las escenas de datos?
3. El master dura **88.5 s** (el brief pide 75–90 s). ¿Está bien así?
