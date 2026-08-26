---
title: "tsk_ini_ETN607"
galaxy_body: workshop
subject: ETN607
semester: 4
tags: [ETN607, workshop, inicio]
date_created: 2026-08-08
date_updated: 2026-08-16
status: activo
---

# tsk — Inicio de materia · ETN607

## Libros

- [x] Temario completo entregado a Claude
- [x] Bibliografía sugerida por el docente evaluada
- [x] Stack aprobado → ver `[[_app/_config/_library-system]]` + `[[Semesters/template/tpl-w-library]]`
- [x] `_library_ETN607.md` creado en `Semesters/Sem_04/ETN607/`

---

## NotebookLM — fuentes

- [x] PDFs del stack subidos al notebook
- [~] Índices extraídos — no aplica para ETN607 (mapeo por tema ya definido en prompt)
- [x] Fuentes cargadas en NotebookLM

---

## NotebookLM — prompts

- [x] `ETN607-transcription.md` creado en `_app/notebooklm/prompts/ETN607/`
- [x] `ETN607-transcription-divisions.md` creado en `_app/notebooklm/prompts/ETN607/`
- [x] `ETN607-transcription-v2.md` creado en `_app/notebooklm/prompts/ETN607/` — incluye IMA-SRC y nueva notación NBLM
- [x] `ETN607-transcription-v3.md` creado en `_app/notebooklm/prompts/ETN607/` — instrucciones de delimitadores eliminadas (resueltas por plugin + script)
- [x] `ETN607-transcription-v3.md` revisado y optimizado 2026-08-16 — correcciones: `CUANDO NO SE ENTIENDE` indica número de página, desempate B/C en complemento, `valor[unidad]` aclarado como notación del apunte
- [x] `DOC-ETN607-transcription.md` creado en `_app/notebooklm/prompts/ETN607/` — documentación del prompt
- [ ] `ETN607-study.md` creado en `_app/notebooklm/prompts/ETN607/`
- [ ] Notebook configurado — fuentes + Instructions cargado

---

## NotebookLM — guías

- [x] `ETN607_TikzJax.md` creado en `_app/notebooklm/guides/ETN607/`
- [x] `ETN607_latex.md` creado en `_app/notebooklm/guides/ETN607/` — notación KaTeX de la materia
- [ ] ETN607_TikzJax.md — completar biblioteca de ejemplos N12-N19 (por tema a medida que avance la materia)
- [ ] ETN607_TikzJax.md — N16 T7 circuitos: probar soporte circuitikz en TikZJax, sesión dedicada

---

## Claude

- [ ] `contexto_ETN607.md` generado vía `[[_app/_config/_claude-matter-boot]]`

---

## Decisiones de infraestructura del prompt

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| 2026-08-16 | IMA-SRC solo referencia imágenes (fuente + página + id + posición) — no lleva a otras IAs | Más rápido; pruebas de redibujo con Gemini descartadas por el momento |
| 2026-08-16 | Script `notebooklm_fix/src/main.py` resuelve Cornell mal formado, arrays en línea, tikz sin etiqueta, marginalia, `\frac→\dfrac` | Estas correcciones no están en el prompt para no consumir caracteres |
| 2026-08-16 | TikZJax se mantiene en el prompt para sistemas sin figura equivalente en fuente y curvas de potencial/espacio de fases | La guía `ETN607_TikzJax.md` con N10 define el criterio de decisión |
| 2026-08-16 | Prompt v3 al límite de 10000 chars — toda corrección futura debe compensar espacio | Límite de NotebookLM para Instructions |

> [!note]- Descartadas
> - Llevar IMA-SRC a Gemini para redibujo automático — descartado por complejidad y tiempo; pruebas en `_hangar/IMA_NBLM/`
> - Incluir correcciones del script en el prompt — descartado, el script las resuelve y ahorran caracteres

---

## Handoff

**Última sesión:** 2026-08-16
**Retomar desde:** `ETN607-transcription-v3.md` listo para cargar en NotebookLM
**Completado esta sesión:** revisión y optimización del prompt v3, documentación de decisiones
**Próximo paso:** crear `ETN607-study.md` + configurar notebook (fuentes + Instructions)
**Script activo:** `notebooklm_fix/src/main.py` — correr desde Obsidian con `NBLM — fix formato` después de cada exportación de NotebookLM

---

## Notas y pendientes

%%
galaxy-links
[[_library_ETN607]]
[[ETN607-transcription]]
[[_app/notebooklm/prompts/ETN607/ETN607-transcription-divisions]]
[[_app/notebooklm/guides/ETN607/ETN607_TikzJax]]
[[ETN607-transcription-v3]]
[[_app/notebooklm/prompts/ETN607/DOC-ETN607-transcription]]
[[_app/notebooklm/guides/ETN607/ETN607_latex]]
%%
