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
**Resumen:** Carrier cerrado. Script, plugin y prompts actualizados. Pendientes de ETN607 (`ETN607-study.md`, `contexto_ETN607.md`) trasladados a `tsk_ini_ETN607.md`.
**Último avance:** `ETN607-transcription-v3.md` creado. `ETN607_latex.md` creado. `DOC-ETN607-transcription.md` creado. `tsk_ini_ETN607.md` actualizado.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_NBLM_update.md` | tsk | — | archivo de trabajo activo |
| `NBLM_update-opc_script.md` | dropship | evaluado | Actualización script notebooklm_fix — completado |

---

## Hitos

- 2026-08-13 — Carrier creado — scope definido y primeros archivos externos producidos
- 2026-08-13 — Plugin `Fix Math for Obsidian` modificado (mod alx-rul) y documentado en `_legacy`
- 2026-08-13 — Script `notebooklm_fix/main.py` actualizado a nueva notación — dropship entregado
- 2026-08-13 — `shellcmd_NBLM_fix.md` documentado completamente
- 2026-08-13 — `ETN607-transcription-v3.md` creado — prompt limpio sin instrucciones de delimitadores
- 2026-08-13 — `ETN607_latex.md` creado — guía de notación KaTeX para ETN607
- 2026-08-13 — `DOC-ETN607-transcription.md` creado — documentación del prompt
- 2026-08-13 — Carrier cerrado — todas las tareas completadas

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-13 | Scope acotado a actualización — P2, P2b, P3 quedan en `IMA_NBLM` | Carriers con foco distinto — imágenes vs. sistema NBLM |
| 2026-08-13 | Actualización del script en sesión dedicada (dropship separado) | Requiere análisis completo de qué correcciones siguen siendo válidas |
| 2026-08-13 | Nombre: `NBLM_update` | Refleja el scope real — es una actualización, no una integración nueva |
| 2026-08-13 | Instrucciones de delimitadores eliminadas del prompt | Plugin + script resuelven la conversión — no es responsabilidad del prompt |
| 2026-08-13 | `ETN607_latex.md` como nombre de la guía KaTeX | Consistente con MAT101 — el renderizador es KaTeX pero la nomenclatura del archivo es latex |

> [!note]- Descartadas
> - Nombre `NBLM_gemini` — descartado porque el carrier no cubre el flujo Gemini
