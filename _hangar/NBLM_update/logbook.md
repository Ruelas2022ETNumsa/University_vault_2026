---
galaxy_body: logbook
scope: NBLM_update
status: on-track
date_updated: 2026-08-13
---

## Visión general

NotebookLM migró a Gemini 3 (diciembre 2025) y dejó de usar `$...$` / `$$...$$` para notación matemática. Ahora entrega las fórmulas con delimitadores `\(...\)` para inline y `\[...\]` para display. El script `notebooklm_fix` y los prompts de materia fueron escritos para la notación anterior y necesitan actualizarse. Este carrier agrupa todas las tareas de adaptación del sistema vault a la nueva versión de NBLM — script, plugin, y prompts.

---

## Estado actual

**Salud:** on-track
**Resumen:** Carrier recién creado. Scope acotado a actualización — no cubre el flujo Gemini (P2, P2b, P3) que vive en `IMA_NBLM`.
**Último avance:** `ETN607-transcription-v2.md` creado con nueva notación. `shellcmd_NBLM_fix.md` documentado.
**Próximo hito:** Actualización del script `notebooklm_fix` en sesión dedicada.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_NBLM_update.md` | tsk | — | archivo de trabajo activo |
| `NBLM_update-opc_script.md` | dropship | activo | Actualización script notebooklm_fix — sesión dedicada |

---

## Hitos

- 2026-08-13 — Carrier creado — scope definido y primeros archivos externos producidos

---

## Riesgos y dependencias

- El script `notebooklm_fix` tiene correcciones que pueden seguir siendo válidas con la nueva notación (Cornell, desmos, arrays, marginalia) — evaluar antes de reescribir
- El plugin de corrección LaTeX no está documentado — riesgo de perder contexto si cambia

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-13 | Scope acotado a actualización — P2, P2b, P3 quedan en `IMA_NBLM` | Carriers con foco distinto — imágenes vs. sistema NBLM |
| 2026-08-13 | Actualización del script en sesión dedicada (dropship separado) | Requiere análisis completo de qué correcciones siguen siendo válidas |
| 2026-08-13 | Nombre: `NBLM_update` | Refleja el scope real — es una actualización, no una integración nueva |

> [!note]- Descartadas
> - Nombre `NBLM_gemini` — descartado porque el carrier no cubre el flujo Gemini
