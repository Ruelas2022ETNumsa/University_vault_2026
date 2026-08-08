---
galaxy_body: logbook
scope: TABnote
status: blocked
date_updated: 2026-08-08
---

---

## Visión general

Sistema unificado de apuntes en tablet (Samsung Notes, S Pen) y transcripción automática vía NotebookLM. El carrier abarca el diseño del template TABnote (plantilla visual A4, jerarquía, marginalia, símbolos) y los prompts NLM de transcripción adaptados al flujo tablet. Es carrier porque combina diseño físico, convenciones de escritura, flujo de exportación y prompts de IA en un sistema interdependiente que debe cerrarse como unidad antes de ser adoptado en otras materias.

Criterio de éxito: template probado en clase real, ajustado si es necesario, y prompt NLM funcional con el PDF exportado desde Samsung Notes.

---

## Estado actual

**Salud:** blocked
**Resumen:** Template v1 diseñado y cargado en Samsung Notes. Documentación completa. Bloqueado esperando prueba real en clase para validar y cerrar.
**Último avance:** Carrier constituido — tsk, logbook y dropship de prompt consolidados en `_hangar/TPL_TAB/`.
**Próximo hito:** Prueba del template en clase real → ajustes post-prueba → redacción del prompt NLM.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_tabnote.md` | tsk | delayed | archivo de trabajo activo — plantilla y sistema TABnote |
| `tsk_tabnote-prompt-nlm.md` | dropship | docked | prompt de transcripción NLM para tablet |
| `_TABnote-ref.md` | ref | — | referencia definitiva del sistema TABnote v1 |

---

## Hitos

- 2026-08-03 — Inicio del proyecto TABnote, relevamiento del sistema actual
- 2026-08-04 — Template v1 diseñado en Excalidraw, exportado a Samsung Notes en 3 variantes
- 2026-08-04 — Sistema de marginalia tablet definido (notación + flujo transcripción)
- 2026-08-05 — Catálogo de símbolos cerrado (9 símbolos), borrador de especificaciones completo
- 2026-08-05 — `_TABnote-ref.md` creado como referencia definitiva del sistema
- 2026-08-05 — Prompt NLM separado a dropship independiente
- 2026-08-08 — Carrier constituido en `_hangar/TPL_TAB/`

---

## Riesgos y dependencias

- **Prueba en clase pendiente** — el template puede necesitar ajustes de grosor, espaciado o convenciones al usarse en condiciones reales. Sin esta prueba no se puede cerrar el carrier ni escribir el prompt NLM.
- **Prompt NLM bloqueado** — depende directamente del resultado de la prueba. No se puede escribir sin saber cómo responde NLM al PDF de Samsung Notes.

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-03 | Un solo color para apuntes: #005F73 | Consistencia y legibilidad OCR |
| 2026-08-03 | Callout = caja cerrada 4 lados, `> Título` como primera línea | NLM reconoce el bloque sin depender del color |
| 2026-08-03 | Imagen = subtítulo gris + sigla IMA + área vacía | Señal explícita para NLM de omitir el bloque |
| 2026-08-04 | Cuadrícula 44×56 recuadros de 4mm, márgenes 15mm | Balance entre espacio de escritura y márgenes para marginalia |
| 2026-08-04 | Herramienta Cinta (Tape) descartada | Causa pérdida de sincronización tablet → PC |
| 2026-08-04 | Catálogo de símbolos: 9 símbolos de 1 carácter, cualquier color | Simplicidad de escritura con S Pen en clase |
| 2026-08-05 | Prompt NLM separado a dropship independiente | Proyectos con distinto bloqueo y distinto ciclo de vida |
