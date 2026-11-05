# remotion/

Reservado para las escenas de "data motion" (comparación, $249, contador de días, checklist).

Propuesta en revisión (ver `storyboard.md` → "Decisión técnica"): hacer esas escenas directamente en HyperFrames,
en el mismo timeline, para tener un solo motor, el mismo render de fuentes y colores, y poder re-maquetarlas para
4:5 y 1:1 sin re-renderizar clips con alpha. Las skills de Remotion están instaladas (`.agents/skills/remotion-*`)
por si se decide volver a la arquitectura original.
