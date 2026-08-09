---
galaxy_body: logbook
scope: anki
status: blocked
date_updated: 2026-08-09
---

%%
# Al actualizar este archivo
  1. Actualizar date_updated y status en el YAML
  2. Revisar ## Estado actual si cambió la salud del proyecto
  3. Agregar entradas a ## Hitos cuando se completa algo significativo
  4. Agregar a ## Archivos del carrier cuando se crea un dropship nuevo
  5. Actualizar ## Riesgos y dependencias si aparece algo nuevo
%%

---

## Visión general

Sistema completo de exportación Obsidian → Anki para el vault Galaxy. El proyecto es un carrier porque involucra tres opciones de exportación independientes (A, B, C) que deben coexistir sin conflictos y cubrir distintos tipos de notas galaxy. El criterio de éxito es tener las tres opciones operativas, documentadas e integradas al vault.

---

## Estado actual

**Salud:** blocked
**Resumen:** el carrier está bloqueado por los 3 dropships — ninguno ha sido entregado aún. Las opciones están definidas y los scripts principales implementados, pero faltan pruebas reales y documentación final.
**Último avance:** Script 2 (latex_to_mathjax) y Script 3 (occlusion_actions) implementados y documentados. Decisiones A vs B tomadas y registradas.
**Próximo hito:** entregar los 3 dropships (A, B, C) para desbloquear el carrier.

---

## Archivos del carrier

%%
Tabla de todos los archivos de la carpeta del carrier.
Actualizar cuando se crea o elimina un archivo — permite a Claude saber
qué existe sin listar el directorio.

Tipos posibles: tsk | logbook | chronicle | dropship | beacon | void
Estado para dropships: activo | evaluado | descartado
%%

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `tsk_anki.md` | tsk | — | archivo de trabajo activo |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_marginalia_anki.md` | dropship | activo | Opcion A — validacion con Script 2 |
| `tsk_flashcards.md` | dropship | activo | Opcion B — activacion y pruebas |
| `tsk_obsidian_to_anki.md` | dropship | activo | Opcion C — Image Occlusion completo |
| `anki_galaxy_guide.md` | beacon | activo | Guia maestra del sistema Anki |
| `anki-opcionA-marginalia.md` | beacon | activo | Documentacion Opcion A |
| `anki-opcionB-flashcards.md` | beacon | activo | Documentacion Opcion B |
| `anki-opcionC-obsidian-to-anki.md` | beacon | activo | Documentacion Opcion C |
| `Obsidian_to_anki.md` | beacon | activo | Flujo Image Occlusion — pendiente integracion |
| `opA_vs_opB.md` | beacon | activo | Comparativa y veredicto A vs B |

---

## Hitos

- 2026-07-28 — Evaluacion inicial de opciones: AnkiSync+ y Opcion D descartadas
- 2026-08-02 — Carrier creado. 3 dropships individuales definidos (A, B, C)
- 2026-08-02 — Decision A vs B tomada: A principal para planet/moon/comet, B complemento para dwarf/formularios T00
- 2026-08-02 — Script 2 (latex_to_mathjax) implementado y documentado
- 2026-08-02 — Script 3 (occlusion_actions) implementado y documentado

---

## Riesgos y dependencias

- Plugin Flashcards (Opcion B): riesgo de conflicto con Image Occlusion (Opcion C) al activarse — pendiente de verificacion
- Carrier bloqueado hasta que los 3 dropships esten en status entregado

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-02 | Opcion A principal para planet/moon/comet | Marginalia invisible, Script 2 resuelve LaTeX, mantenimiento activo |
| 2026-08-02 | Opcion B complemento para dwarf/formularios T00 | Cloze y reversed utiles en notas de repaso puro, carpeta = deck automatico |
| 2026-08-02 | Opcion C exclusiva para Image Occlusion | Unico plugin que soporta Image Occlusion Enhanced desde Excalidraw |

> [!note]- Descartadas
> - AnkiSync+ (RochaG07): creaba mazos pero no tarjetas. Sin fix, sin mantenimiento.
> - Opcion D (Obsidian-Anki-Sync debanjandhar12): sintaxis de cloze en LaTeX muy compleja.
> - TrillStones Image Occlusion: genera 2 PNG separados, no compatible con Image Occlusion Enhanced.
