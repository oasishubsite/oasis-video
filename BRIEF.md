# BRIEF — Video Ad "Landing Page $249" · Oasis Hub Studio
### Versión para Claude Code en la nube (claude.ai/code)

> Este archivo vive en la raíz del repo `oasis-video`. En una sesión de Claude Code en la nube escribe:
> **"Lee BRIEF.md y ejecútalo fase por fase. Empieza por la sección 3B (entorno cloud)."**

---

## 0. ROL Y OBJETIVO

Eres un director creativo de performance ads + motion designer senior + ingeniero de video programático.
Tu trabajo: producir un **video publicitario para Meta Ads (Instagram Reels, Stories, Facebook Feed)** que venda la **Landing Page profesional de $249 de Oasis Hub Studio** y deje claro que hacer el website con nosotros es la decisión obvia.

**Una sola idea que el espectador debe llevarse:**
> "Un website profesional, a la medida, en 2–3 días, por $249. Ya lo hicieron para negocios reales. Escribo por WhatsApp."

**Objetivo de negocio:** mensajes de WhatsApp (campaña de mensajes / leads). Todo el video empuja a una acción: **escribir por WhatsApp**.

---

## 1. HECHOS DE LA MARCA (fuente de verdad — NO inventes nada fuera de esto)

**Marca:** Oasis Hub Studio — agencia de websites y apps, Costa Rica, clientes en toda Latinoamérica.
**Web:** https://oasishub.studio · **Precios:** https://oasishub.studio/precios
**WhatsApp:** +506 6469 2948 → `https://wa.me/50664692948`
**Instagram:** @oasishub.studio

**Oferta principal — Landing Page:**
- **$249** desarrollo, pago único
- **Entrega en 2–3 días**
- Mantenimiento $50/año — **primer año incluido**
- Website premium de una página, diseñado a la medida (no plantilla)
- Diseño para celular, tablet y computadora
- WhatsApp, formularios y captación de clientes
- SEO inicial y configuración de indexación en Google
- Hosting seguro, SSL y soporte técnico
- **Optimización de Google Business GRATIS** (en todos los planes)

**Credenciales:** +10 años de experiencia.

**Otros planes (solo mencionar como "también hacemos", nunca protagonistas):** Website a la medida desde $379 · Apps a la medida desde $750.

**Taglines reales del sitio (puedes usarlos):**
- "Hoy los clientes investigan antes de comprar."
- "¿Qué encuentran cuando buscan tu negocio?"
- "Tu próxima venta puede empezar con un mejor website."
- "Más presencia · Más confianza · Más ventas"

**⚠️ Restricciones legales/honestidad (obligatorias):**
- **NO** decir que el dominio o el correo empresarial están incluidos (se cotizan aparte).
- **NO** inventar testimonios, reseñas, estrellas, cantidades de clientes ni métricas de resultados.
- **NO** nombrar ni mostrar logos de agencias competidoras. La comparación es contra "Agencia tradicional" genérica.
- **NO** usar logos de Meta, Google, Apple, etc. como si fueran partners. (Íconos genéricos de "Google search" estilizados sí, sin el logo oficial.)

---

## 2. PORTAFOLIO — SITIOS REALES APROBADOS PARA MOSTRAR

Estos son proyectos reales entregados y aprobados por los clientes. **Son la prueba social del video.** Captúralos en vivo (ver Fase 2).

| Proyecto | URL | Industria | Qué destacar visualmente |
|---|---|---|---|
| **Melo Kombucha** | https://melokombucha.com | Bebidas / e-commerce | Hero "¡Eleva tu experiencia de bienestar!", sabores, mapa de puntos de venta, quiz interactivo. Paleta cálida, fresca. |
| **Barahona Caribbean Stay** | https://barahonastay.site | Hospedaje / turismo (Limón, CR) | "Tu estadía VIP", galería, amenidades (self check-in, Alexa), **formulario de reserva → WhatsApp**, bilingüe ES/EN. |
| **Proyecto Ecogreen** | https://proyectoecogreen.com | Paisajismo / vivero | "Diseñamos jardines con propósito", servicios, **tabla comparativa "Ecogreen vs Otros"**, mapa/Waze, reseñas Google reales del cliente. |
| *(bonus)* Oasis Hub | https://oasishub.studio | La propia agencia | Usar para el cierre y la sección de precios. |

Mensaje clave del portafolio: **tres industrias completamente distintas → cada sitio se ve único, nada de plantillas.**
Etiqueta para cada uno: `Proyecto real · En línea hoy` + nombre + industria.

---

## 3. STACK Y SKILLS — INSTALA Y VERIFICA ANTES DE EMPEZAR

Requisitos: **Node.js 22+**, **FFmpeg**, Chromium (Playwright).

```bash
# HyperFrames (HeyGen) — motor principal, HTML → MP4 determinístico
npx skills add heygen-com/hyperframes --full-depth --yes
npx hyperframes skills update

# Remotion — escenas de datos/comparación en React
npx skills add remotion-dev/skills
#   (alternativa vía plugin: claude plugin marketplace add remotion-dev/claude-code-plugin
#                              claude plugin install remotion@remotion)

# Capturas de los sitios
npm i -D playwright && npx playwright install chromium
```

**Skills a usar (léelas antes de escribir código):**
- `/hyperframes` (router) → luego `/product-launch-video`, `/hyperframes-core`, `/hyperframes-cli`, `/hyperframes-media` (TTS, transcripción, captions)
- `/remotion-best-practices` → `/remotion-create`, `/remotion-markup`, `/remotion-captions`, `/remotion-render`
- `frontend-design` (si está disponible) para la dirección visual
- Cualquier otra skill instalada que aplique (captions, audio, transiciones del catálogo `npx hyperframes add …`)

**Arquitectura (decisión tomada, no la cambies sin razón):**
- **HyperFrames = timeline maestro** y montaje final: hook, portafolio con capturas reales, cierre, audio, captions, export de todos los formatos.
- **Remotion = escenas de "data motion"**: tabla comparativa animada, contador de precio $249, contador "2–3 días", checklist de lo incluido. Se renderizan como clips (MP4/ProRes 4444 con alpha si hace falta) y se importan al timeline de HyperFrames.
- Si una de las dos herramientas falla en tu entorno, haz TODO en la otra y explícame por qué. No te bloquees.

Al terminar esta fase, imprime: versiones instaladas + lista de skills detectadas.

---

## 3B. ENTORNO CLOUD — REGLAS ESPECÍFICAS (léelo antes de la Fase 1)

Estás corriendo en una VM de Claude Code en la nube (Ubuntu 24.04, ~4 vCPU, 16 GB RAM, 30 GB disco). Nadie puede ver un servidor local ni abrir una pestaña de preview. Adáptate así:

1. **Verifica el entorno primero:** `check-tools`, `node -v` (debe ser 22+; si no: `source ~/.nvm/nvm.sh && nvm use 22`), `ffmpeg -version`. Si falta FFmpeg: `apt-get update && apt-get install -y ffmpeg`.
2. **Red:** prueba con `curl -sI https://melokombucha.com https://barahonastay.site https://proyectoecogreen.com https://oasishub.studio`. Si alguno devuelve error de proxy/403, **detente y avísame** que hay que ajustar el acceso de red del entorno (no intentes saltarte el proxy).
3. **Skills:** instálalas con los comandos de la sección 3. Si después de instalarlas no aparecen como slash commands en esta sesión, **léelas directamente** (`.agents/skills/*/SKILL.md` o `.claude/skills/*/SKILL.md`) con Read y sigue sus instrucciones igual. Haz commit de las carpetas de skills al repo para que la próxima sesión las cargue solas.
4. **Navegador para render/capturas:** HyperFrames usa Puppeteer y Remotion usa su propio Chrome headless. Si la descarga de Chrome de Playwright falla por red, usa Puppeteer (o el Chrome que ya descargó Remotion/HyperFrames) para las capturas; no pierdas tiempo peleando con Playwright.
5. **Nada de preview en vivo.** En lugar de `hyperframes preview` / Remotion Studio, valida con **stills** (`render` de frames sueltos) y extracción de frames con FFmpeg. Mira tú mismo los PNG con Read antes de seguir.
6. **Música:** busca primero `assets/audio/` en el repo (JP puede haber subido una pista con licencia). Si no hay pista, NO descargues música de sitios externos: arma el video con un placeholder silencioso + guía de beats en `assets/audio/BEATS.md`, y avísame.
7. **Voz en off (TTS):** solo si `/hyperframes-media` puede hacerlo sin API keys externas. Si pide una key que no existe, deja el video 100% texto + música y entrega `VO_SCRIPT.md`.
8. **Fuentes:** descarga Syne y DM Sans de Google Fonts (`fonts.googleapis.com` / `fonts.gstatic.com` están permitidos) y guárdalas en `assets/brand/fonts/` para que el render sea determinístico.
9. **Rendimiento:** renderiza **un export a la vez** (no en paralelo), para no quedarte sin RAM. Primero un render de prueba en baja resolución (540×960) del master completo, luego los finales.
10. **Entrega por Git (límite de GitHub: 100 MB por archivo):**
    - Cada MP4 final debe pesar **< 90 MB**. Ajusta bitrate según duración (master 90 s ≈ 7 Mbps; cortes de 15–30 s pueden ir a 12–15 Mbps). Verifica el tamaño con `ls -lh` antes de hacer commit.
    - Haz commit en la rama de trabajo de la sesión: `out/` (videos finales), `out/stills/` (frames clave del storyboard), `storyboard.md`, `QA_REPORT.md`, `meta_ad_copy.md`.
    - **Haz commit y push al final de cada fase** (no solo al final), para no perder trabajo si la sesión se corta.
    - Abre un Pull Request al terminar con la lista de archivos entregados y sus pesos.
11. **Checkpoint de aprobación:** en la Fase 3, haz commit + push de `storyboard.md` y `out/stills/*.png`, dime la rama, y **espera mi respuesta en esta conversación** antes de renderizar en alta.

---

## 4. DIRECCIÓN VISUAL

**Look:** cinematográfico premium, nivel Apple / Stripe / Linear. Limpio, con aire, movimientos suaves pero con energía de ad.

- **Fondo:** oscuro profundo (`#05070D` → `#0B1220` con gradientes sutiles y grain ligero)
- **Acento principal:** azul de marca **`#1754CF`** (muestreado de oasishub.studio) + versión eléctrica para glows (`#3B82F6` / `#60A5FA`)
- **Texto:** blanco `#F8FAFB`, secundario `#94A3B8`
- **Positivo (checks):** verde `#22C55E` · **Negativo (agencia tradicional):** gris apagado / rojo muy sutil `#EF4444` al 70%
- **Tipografía:** **Syne** (titulares, bold/extrabold, tracking ajustado) + **DM Sans** (cuerpo, captions, datos). Nada de Inter/Arial/system-ui en el video.
- **Mockups:** iPhone, MacBook e iMac genéricos (marcos dibujados en CSS/SVG, sin logos Apple), con reflejos suaves, sombras realistas, leve perspectiva 3D y parallax.
- **Movimiento:** easing `cubic-bezier(0.22, 1, 0.36, 1)`, springs suaves; transiciones con match-cuts, zoom-through a la pantalla, light sweeps azules. Cada corte con intención, ritmo sincronizado a la música.
- **Precio $249:** momento "héroe" — número gigante en Syne, conteo rápido o slam con glow azul.
- Respeta **safe zones de Reels/Stories**: deja libre ~14% superior y ~35% inferior para la UI de Instagram (en 9:16). Todo texto crítico en la franja central.

---

## 5. GUION Y STORYBOARD — MASTER 9:16 (~75–90 s)

Captions grandes quemados en pantalla durante TODO el video (la mayoría ve sin sonido). Voz en off opcional en **español latino neutro**, cálida y segura (usa TTS de `/hyperframes-media`; si no hay TTS de calidad, deja el video 100% texto + música y entrégame el guion de VO aparte).

| # | Tiempo | Escena | Texto en pantalla / VO |
|---|---|---|---|
| 1 | 0:00–0:03 | **HOOK.** Barra de búsqueda estilizada escribe "tu negocio" → resultado vacío con glitch: "Sin resultados relevantes". | **"¿Tu negocio no aparece cuando te buscan?"** |
| 2 | 0:03–0:08 | Pulso rápido: celular con búsqueda, clientes que se van (íconos que se desvanecen). | "Hoy los clientes investigan **antes de comprar**." / "Si no te encuentran… compran en otro lado." |
| 3 | 0:08–0:14 | **REVEAL.** Zoom-through desde la pantalla vacía → logo Oasis Hub Studio con light sweep azul. | "Oasis Hub Studio" · "+10 años creando websites que venden" |
| 4 | 0:14–0:20 | **OFERTA HÉROE** (Remotion): "$249" slam + "Lista en 2–3 días". | **"Landing page profesional. $249. Lista en 2–3 días."** |
| 5 | 0:20–0:28 | **PORTAFOLIO 1 — Melo Kombucha.** iMac + iPhone con scroll real del sitio. Tag de industria. | "Melo Kombucha · Bebidas" · "Proyecto real · En línea hoy" |
| 6 | 0:28–0:36 | **PORTAFOLIO 2 — Barahona Stay.** MacBook + iPhone, scroll por galería y formulario de reserva → WhatsApp. | "Barahona Caribbean Stay · Hospedaje" · "Reservas directo a WhatsApp" |
| 7 | 0:36–0:44 | **PORTAFOLIO 3 — Proyecto Ecogreen.** Scroll por servicios y su tabla comparativa. | "Proyecto Ecogreen · Paisajismo" |
| 8 | 0:44–0:48 | Grid de los 3 sitios lado a lado, se juntan. | **"3 industrias. 3 diseños únicos. Cero plantillas."** |
| 9 | 0:48–1:02 | **COMPARACIÓN** (Remotion): split-screen "Agencia tradicional" (gris, apagado) vs "Oasis Hub Studio" (azul, brillante). Filas entran una por una con ✗ / ✓. | Ver tabla abajo. Remate: **"La elección es obvia."** |
| 10 | 1:02–1:12 | **TODO INCLUIDO** (Remotion): checklist animado con íconos. | Ver lista abajo. |
| 11 | 1:12–1:20 | **PROCESO** en 3 pasos con timeline horizontal y contador de días. | "1. Nos escribes por WhatsApp → 2. Diseñamos tu sitio → 3. **En línea en 2–3 días**" |
| 12 | 1:20–1:30 | **CTA FINAL.** Botón WhatsApp verde pulsando, precio, URL. Mantener 3+ s estático legible. | **"Tu website listo esta semana. $249."** · "Escríbenos por WhatsApp" · "oasishub.studio" · "+506 6469 2948" |

**Tabla comparativa (escena 9):**

| | Agencia tradicional | **Oasis Hub Studio** |
|---|---|---|
| Precio landing page | $500 – $1,500+ | **$249 pago único** |
| Tiempo de entrega | 2 – 6 semanas | **2 – 3 días** |
| Diseño | Plantilla adaptada | **100% a la medida** |
| Mantenimiento 1er año | Se cobra aparte | **Incluido** |
| Google Business | Servicio extra | **Gratis** |
| WhatsApp integrado | A veces | **Siempre** |
| Hosting + SSL | Se cobra aparte | **Incluido** |
| Atención | Tickets y correos | **Directo por WhatsApp** |

(Los valores de "Agencia tradicional" son rangos típicos de mercado. Mantén la etiqueta genérica y en tono de "promedio del mercado", nunca un competidor específico.)

**Checklist "Todo incluido" (escena 10):**
✓ Diseño a la medida para tu marca · ✓ Celular, tablet y computadora · ✓ Botón de WhatsApp y formularios · ✓ SEO inicial para Google · ✓ Hosting seguro + SSL · ✓ 1er año de mantenimiento · ✓ Google Business optimizado **gratis**

---

## 6. FASES DE EJECUCIÓN

**Fase 1 — Setup.** Verifica el entorno (sección 3B, puntos 1–2), instala todo (sección 3) y crea la estructura dentro del repo:
```
(raíz del repo)
  BRIEF.md
  assets/captures/   assets/audio/   assets/brand/
  remotion/          (escenas de datos)
  hyperframes/       (timeline maestro)
  out/
  storyboard.md
```

**Fase 2 — Captura de sitios reales (Playwright o Puppeteer, ver 3B punto 4).** Para cada URL del portafolio + oasishub.studio:
- Desktop 1440×900 y móvil 390×844 (DPR 2–3 para nitidez).
- Screenshot full-page (PNG) **y** video de scroll suave (graba ~8–10 s, scroll con easing, no saltos). Espera a que carguen fuentes, imágenes y animaciones; cierra banners de cookies si aparecen.
- Guarda también los colores/hero de cada sitio para matizar el fondo de su escena (sutil, siempre dentro de la marca Oasis).
- Si un sitio no carga, avísame y continúa con los demás.

**Fase 3 — Storyboard + guion.** Escribe `storyboard.md` con: escenas, tiempos, texto exacto, transición, asset usado y descripción del movimiento. Renderiza **stills** (1 frame clave por escena) en baja resolución.
**⏸ PARA AQUÍ:** commit + push de `storyboard.md` y `out/stills/`, dime la rama y espera mi aprobación en esta conversación antes de renderizar en alta.

**Fase 4 — Escenas Remotion.** Comparación, precio héroe, contador de días, checklist. Render como clips independientes a 1080×1920, 30 fps.

**Fase 5 — Timeline maestro HyperFrames.** Monta todo: capturas en mockups, clips Remotion, captions kinetic, transiciones, música y VO. Usa `npx hyperframes lint` antes de cada render y valida con stills (no hay preview en la nube).

**Fase 6 — Audio.**
- Música: usa la pista que JP haya subido a `assets/audio/` (ver 3B punto 6); si no hay, placeholder silencioso + `BEATS.md` y avísame. Estilo: electrónica moderna, confiada, beat limpio ~110–124 BPM, con drop en el reveal del precio.
- Cortes sincronizados al beat. Ducking de música bajo la VO.
- Loudness final ≈ **-14 LUFS**, picos ≤ -1 dBTP.

**Fase 7 — Exports.**

| Archivo | Formato | Duración | Uso |
|---|---|---|---|
| `oasis_249_master_9x16.mp4` | 1080×1920 | 75–90 s | Reels / Stories (principal) |
| `oasis_249_30s_9x16.mp4` | 1080×1920 | 30 s | Reels ad corto: hook → $249 → 3 sitios rápidos → comparación resumida → CTA |
| `oasis_249_15s_9x16.mp4` | 1080×1920 | 15 s | Stories: hook → $249 + 2–3 días → montage portafolio → CTA |
| `oasis_249_master_4x5.mp4` | 1080×1350 | 75–90 s | Feed Facebook/Instagram (re-layout, no solo recorte) |
| `oasis_249_30s_1x1.mp4` | 1080×1080 | 30 s | Feed / placements cuadrados |
| `thumb_*.jpg` | por formato | — | Portada: "$249 · Website en 2–3 días" |

Specs: H.264 High, 30 fps, AAC 48 kHz, yuv420p, `+faststart`. Bitrate ajustado para que cada archivo pese **< 90 MB** (ver 3B punto 10); usa 2-pass o CRF ~18–20 con tope `-maxrate`. Cada versión debe funcionar **sin sonido**.

**Fase 8 — QA (obligatoria antes de entregarme).**
- Extrae frames cada ~2 s de cada export y **revísalos tú mismo**: texto legible en celular, nada cortado, safe zones respetadas, sin texto encima de caras/UI crítica, sin frames negros ni flashes.
- Verifica ortografía y acentos en español en TODO el texto.
- Verifica que precio, días, WhatsApp y URL sean exactamente los de la sección 1.
- Verifica que no hay claims prohibidos (sección 1).
- Mide loudness con FFmpeg (`ebur128`).
- Confirma que ningún archivo supera 90 MB.
- Entrégame un `QA_REPORT.md` con lo que revisaste y lo que corregiste, haz commit + push y abre el Pull Request.

---

## 7. BONUS — COPY PARA META ADS

Genera `meta_ad_copy.md` con:
- **3 textos principales** (uno corto, uno medio, uno con bullets/emojis moderados), en español latino, que repitan la promesa: $249 · 2–3 días · a la medida · WhatsApp.
- **5 titulares** (≤ 40 caracteres), ej. "Tu website en 2–3 días por $249".
- **3 descripciones** cortas.
- CTA recomendado: **"Enviar mensaje" (WhatsApp)**.
- 3 ideas de **hooks alternativos** (primeros 3 s) para hacer test A/B, cada uno con su variante de escena 1 lista para renderizar.

---

## 8. REGLAS DE ORO

1. **Los primeros 3 segundos deciden todo.** Movimiento + pregunta fuerte desde el frame 1. Sin logos ni intros lentas al inicio.
2. **Cada escena vende.** Si una escena no acerca al espectador al WhatsApp, recórtala.
3. **Prueba real > promesas.** El portafolio se ve con capturas reales y nítidas, nunca mockups inventados.
4. **$249 y "2–3 días" aparecen al menos 3 veces** en el master (hook/oferta, comparación, CTA).
5. **Premium, no barato.** El precio es bajo; el video NO debe verse barato. Nada de clip-art, stock genérico ni efectos cheesy.
6. **No inventes datos.** Si te falta algo, pregúntame o déjalo marcado como `TODO`.
7. Trabaja por fases, muéstrame avances, y **no avances a render final sin mi OK al storyboard.**
