---
title: Sistema de Prompts — NotebookLM
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_notebooklm-system]]"
  - "[[notebooklm-prompt-guide]]"
tags:
  - beacon
  - notebooklm
  - prompts
  - infraestructura
date_created: 2026-07-31
date_updated: 2026-07-31
status: activo
---

# Sistema de Prompts — NotebookLM

> Sistema NotebookLM completo: [[_notebooklm-system]]
> Guía para crear prompts nuevos: [[notebooklm-prompt-guide]]

Los prompts le dicen a NotebookLM cómo comportarse: modos de respuesta,
reglas de graficación, programa de la materia, prioridad de fuentes.
Se cargan en el campo **Instructions** del notebook antes de trabajar.

Viven en `_app/notebooklm/prompts/` organizados por subcarpeta de materia.
Un prompt por materia/parcial. Para crear uno nuevo, seguir la guía de plantillas.

---

## Inventario de prompts

### MAT101 — Cálculo 1

| Archivo | Tipo | Parcial | Estado |
|---|---|---|---|
| `prompts/MAT101/MAT101-study.md` | estudio activo | todos | ✅ activo |
| `prompts/MAT101/MAT101-transcription.md` | transcripción cuaderno físico | todos | ✅ activo |
| `prompts/MAT101/MAT101-transcription-legacy.md` | transcripción cuaderno físico | todos | 🗄️ legacy |
| `prompts/MAT101/MAT101-transcription (multi columns pluggin)-legacy.md` | transcripción cuaderno físico (Multi-Column) | todos | 🗄️ legacy |

### ETN806 — Procesos Estocásticos

> Todos los prompts de ETN806 son **legacy** — cumplieron su rol y no se actualizan.

| Archivo | Tipo | Parcial | Estado |
|---|---|---|---|
| `prompts/ETN806/ETN806-P1.md` | estudio activo | P1 — Discretas | 🗄️ legacy |
| `prompts/ETN806/ETN806-P2.md` | estudio activo | P2 — Continuas | 🗄️ legacy |
| `prompts/ETN806/ETN806-P3.md` | estudio activo | P3 — Markov/Colas | 🗄️ legacy |
| `prompts/ETN806/ETN806-P1-legacy.md` | estudio activo | P1 | 🗄️ legacy |

---

## Convención de nombres

```
ETNXXX-PN-description.md    → prompt por parcial        (ej: ETN806-P1-study.md)
ETNXXX-description.md       → todos los parciales       (ej: MAT101-study.md)
```

Sufijo `-legacy` para prompts fuera de uso que se conservan como histórico.

---

## Para crear un prompt nuevo

Seguir la guía de plantillas: [[notebooklm-prompt-guide]]
Ruta: `_app/notebooklm/general/notebooklm-prompt-guide.md`

Una vez creado, agregar al inventario de este archivo y al de [[_notebooklm-system]].

---

%%
# galaxy-links
[[_app/_config/_notebooklm-system.md]]
[[_app/notebooklm/general/notebooklm-prompt-guide.md]]
[[_app/notebooklm/prompts/MAT101/MAT101-study.md]]
[[_app/notebooklm/prompts/MAT101/MAT101-transcription.md]]
[[_app/notebooklm/prompts/MAT101/MAT101-transcription-legacy.md]]
[[_app/notebooklm/prompts/ETN806/ETN806-P1.md]]
[[_app/notebooklm/prompts/ETN806/ETN806-P2.md]]
[[_app/notebooklm/prompts/ETN806/ETN806-P3.md]]
[[_app/notebooklm/prompts/ETN806/ETN806-P1-legacy.md]]
%%
