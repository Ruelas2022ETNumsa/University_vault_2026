---
galaxy_body: ship
project: "ETN1015 — NotebookLM: guía LaTeX + actualización prompt"
date: 2026-08-17
status: delivered
fleet: ETN1015
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-17
**Retomar desde:** —
**Completado esta sesión:** guía LaTeX creada, secciones de parte continua agregadas, prompt actualizado
**Próximo paso:** agregar ETN1015_latex.md como fuente en NotebookLM
**Preguntas de cierre:** —

---

## Resumen y objetivo

NotebookLM actualizó su motor y dejó de soportar `$$...$$` y `$...$` como delimitadores de ecuaciones. El objetivo fue crear una guía KaTeX específica para ETN1015 y actualizar el prompt de estudio para reflejar la nueva notación.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-17 | Crear ETN1015_latex.md desde cero (no adaptar ETN607_latex.md directamente) | ETN607 es Mecánica Clásica — la notación de DSP es estructuralmente distinta |
| 2026-08-17 | Agregar secciones de señales continuas, Laplace, Series de Fourier y espacio de estados | La library_ETN1015.md cubre caps. 1–5 de Rao/Oppenheim (parte continua) — la guía debía cubrirlos |
| 2026-08-17 | Unificar NOTACIÓN OBSIDIAN + GUÍAS DE VISUALIZACIÓN en bloque FUENTES GUÍA | Consistencia con el formato de ETN607 y jerarquía de prioridad explícita |

> [!note]- Descartadas
> Adaptar ETN607_latex.md directamente — descartado porque la notación de Lagrange (punto, vectores, coordenadas generalizadas) no aplica a DSP.

---

## Planificación

Flujo ejecutado en una sola sesión:
1. Leer el prompt existente y la guía de ETN607 como referencia de estructura
2. Verificar la library para identificar gaps de notación
3. Crear la guía ETN1015_latex.md cubriendo DSP puro
4. Ampliar con parte continua (Laplace, CTFT, Series de Fourier, espacio de estados) según la library
5. Editar el prompt en dos puntos quirúrgicos: regla de delimitadores en REGLAS GENERALES y bloque FUENTES GUÍA

---

## Flujo de pasos

1. Leer `ETN1015-study.md` y `ETN607_latex.md`
2. Leer `_library_ETN1015.md` para verificar cobertura temática
3. Crear `ETN1015_latex.md` — secciones §1–§13 (DSP discreto)
4. Agregar §14–§18 (parte continua: señales, CTFT, Laplace, Series de Fourier, espacio de estados)
5. Editar `ETN1015-study.md` — agregar regla LaTeX en REGLAS GENERALES
6. Editar `ETN1015-study.md` — reemplazar bloque de guías por FUENTES GUÍA unificado

---

## Tareas

- [x] Leer prompt ETN1015-study.md
- [x] Leer ETN607_latex.md como referencia de estructura
- [x] Leer _library_ETN1015.md para verificar gaps
- [x] Crear E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_latex.md
- [x] Agregar secciones §14–§18 (parte continua)
- [x] Editar ETN1015-study.md — regla de delimitadores en REGLAS GENERALES
- [x] Editar ETN1015-study.md — bloque FUENTES GUÍA unificado
- [x] Agregar ETN1015_latex.md como fuente en NotebookLM

---

## Preguntas abiertas

—

---

## Recursos

**Archivos creados / editados:**
- `E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_latex.md` — guía KaTeX nueva
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN1015\ETN1015-study.md` — prompt editado

**Archivos de referencia:**
- `E:\University_vault_2026\_app\notebooklm\guides\ETN607\ETN607_latex.md` — estructura base
- `E:\University_vault_2026\Semesters\Sem_08\ETN1015\_library_ETN1015.md` — cobertura temática

**Fuentes del notebook ETN1015 (4 guías):**
- `obsidian_notation.md`
- `ETN1015_latex.md`
- `ETN1015_desmos.md`
- `ETN1015_tikz.md`
