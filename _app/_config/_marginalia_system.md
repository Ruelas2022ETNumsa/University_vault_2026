---
title: "Cornell Marginalia — Integración Galaxy"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[Marginalia_guide]]"
  - "[[_note-system]]"
  - "[[_template-system]]"
tags: [beacon, obsidian, plugins, infraestructura, marginalia, galaxy]
date_created: 2026-07-22
date_updated: 2026-07-22
status: activo
---

# Cornell Marginalia — Integración Galaxy

> Referencia de integración del plugin Cornell Marginalia en el Sistema Galaxy.
> Para el funcionamiento técnico del plugin ver [[Marginalia_guide]].
> Cada sección documenta: qué se probó, qué se notó, y dónde se usa en Galaxy.

> **Convención de este archivo:** los ejemplos de sintaxis se muestran
> en bloques de código fenced (\`\`\`) para evitar que el plugin los procese.
> El escape \%% se usa solo cuando la sintaxis aparece en línea dentro del texto.

---

## Índice

- [[#A1. Sintaxis core]]
- [[#A2. Semantic Highlighting]]
- [[#A3. Grouping Method A]]
- [[#A4. Grouping Method B]]
- [[#A5. Imágenes en el margen]]
- [[#A6. Marginalia Explorer]]
- [[#A7. Active Recall — Blur]]
- [[#A8. Flashcard Generator]]
- [[#A9. Margin Threads]]
- [[#A10. Doodle Engine]]
- [[#A11. Omni-Capture]]
- [[#A12. PDF Export]]
- [[#B. Configuración]]

---

## A1. Sintaxis core

> Sintaxis:
> ```
> %%> texto %%   → margen izquierdo
> %%< texto %%   → margen derecho
> ```
### Probado

- Inline izquierdo (\%%>) y derecho (\%%<) en medio de párrafo → renderiza correctamente en Live Preview y Reading View.
- Con fórmulas LaTeX dentro del margen → renderiza sin conflicto.
- Con escape `\%%`: usar `\%%>` y `\%%` en línea evita que el plugin procese la sintaxis — el texto permanece visible en el cuerpo. Para bloques de ejemplo usar fenced code (` ``` `). Convención estándar de este archivo para documentación.

### Notado

- Con escape `\%%` o bloque fenced, la sintaxis queda visible en Reading View sin ser procesada por el plugin — útil para documentación técnica (este archivo).
- Sin escape, la marginalia desaparece del cuerpo y aparece al margen — comportamiento normal de integración.
- Backticks solos (`` ` ``) no son suficientes: el contenido dentro de `%%...%%` igualmente desaparece del cuerpo en Reading View.

### Dónde se usa en Galaxy

| `galaxy_body` | Uso |
|---|---|
| `planet` / `moon` | Anotar dudas (`?`), referencias a otros planets, aclaraciones de fórmulas sin interrumpir el flujo del texto principal |
| `comet` | Marcar pasos clave de un ejercicio, errores detectados durante la resolución, observaciones del proceso |
| `supernova` | Anotaciones rápidas durante transcripción de clase — agregar contexto sin cortar el flujo bruto |
| `dwarf` | Claves de repaso al margen del resumen, referencias a planets relacionados |
| `beacon` (documentación) | Usar escape `\%%` o bloque fenced para mostrar la sintaxis como ejemplo sin que el plugin la procese |

---

## A2. Semantic Highlighting

> Pendiente de prueba.

---

## A3. Grouping Method A

> Pendiente de prueba.

---

## A4. Grouping Method B

> Pendiente de prueba.

---

## A5. Imágenes en el margen

> Pendiente de prueba.

---

## A6. Marginalia Explorer

> Pendiente de prueba.

---

## A7. Active Recall — Blur

> Pendiente de prueba.

---

## A8. Flashcard Generator

> Pendiente de prueba.

---

## A9. Margin Threads

> Pendiente de prueba.

---

## A10. Doodle Engine

> Pendiente de prueba.

---

## A11. Omni-Capture

> Pendiente de prueba.

---

## A12. PDF Export

> Pendiente de prueba.

---

## B. Configuración

> Pendiente de revisión.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_config/_note-system.md]]
[[_app/_config/_template-system.md]]
%%
