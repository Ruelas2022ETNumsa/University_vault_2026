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
**Resumen:** Script y plugin actualizados. Pendiente: documentar y registrar `ETN607-transcription-v2.md`, y revisar el prompt de transcripción/estudio para mejorarlo.
**Último avance:** Plugin `Fix Math for Obsidian` modificado y documentado. Script `notebooklm_fix/main.py` actualizado (tikz, bloque LaTeX comentado). `shellcmd_NBLM_fix.md` documentado completamente. Dropship de actualización del script entregado.
**Próximo hito:** Revisión y mejora del prompt de transcripción `ETN607-transcription-v2.md`.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_NBLM_update.md` | tsk | — | archivo de trabajo activo |
| `NBLM_update-opc_script.md` | dropship | entregado | Actualización script notebooklm_fix — completado |

---

## Hitos

- 2026-08-13 — Carrier creado — scope definido y primeros archivos externos producidos
- 2026-08-13 — Plugin `Fix Math for Obsidian` modificado (mod alx-rul) y documentado en `_legacy`
- 2026-08-13 — Script `notebooklm_fix/main.py` actualizado a nueva notación — dropship entregado
- 2026-08-13 — `shellcmd_NBLM_fix.md` documentado completamente

---

## Riesgos y dependencias

- `ETN607-transcription-v2.md` aún no registrado en `tsk_ini_ETN607.md` — pendiente
- Evaluar si `ETN607_library.md` va en este carrier o en `tsk_ini_ETN607`

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-13 | Scope acotado a actualización — P2, P2b, P3 quedan en `IMA_NBLM` | Carriers con foco distinto — imágenes vs. sistema NBLM |
| 2026-08-13 | Actualización del script en sesión dedicada (dropship separado) | Requiere análisis completo de qué correcciones siguen siendo válidas |
| 2026-08-13 | Nombre: `NBLM_update` | Refleja el scope real — es una actualización, no una integración nueva |

> [!note]- Descartadas
> - Nombre `NBLM_gemini` — descartado porque el carrier no cubre el flujo Gemini
