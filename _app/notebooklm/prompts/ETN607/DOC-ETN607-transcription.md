---
title: "DOC — ETN607 Transcription Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts]
date_created: 2026-08-13
date_updated: 2026-08-13
status: activo
---

# DOC — ETN607 Transcription Prompt

Documentación del prompt de transcripción para ETN607 (Mecánica Clásica / Lagrange) en NotebookLM.

---

## Archivo activo

`ETN607-transcription-v3.md` — versión actual del prompt.

---

## Historial de versiones

| Versión | Fecha | Cambios |
|---|---|---|
| v1 | anterior | Versión original — notación `$...$` / `$$...$$` |
| v2 | 2026-08-13 | Adaptación a nueva notación NBLM (`\(...\)` / `\[...\]`) tras migración a Gemini 3 |
| v3 | 2026-08-13 | Eliminadas instrucciones de delimitadores del prompt — resueltas por plugin + script. Referencia al Cornell clarificada. |

---

## Fuentes guía que carga el prompt

| Archivo | Ubicación | Rol |
|---|---|---|
| `obsidian_notation.md` | `_app/notebooklm/guides/` | Sintaxis Obsidian, Cornell, callouts, wikilinks |
| `_library_ETN607.md` | `Semesters/Sem_04/ETN607/` | Criterio de selección de libros y capítulos por tema |
| `ETN607_latex.md` | `_app/notebooklm/guides/ETN607/` | Notación KaTeX de la materia |
| `ETN607_TikzJax.md` | `_app/notebooklm/guides/ETN607/` | Reglas y ejemplos TikZJax para ETN607 |

---

## Sistema de corrección de notación

La migración de NBLM a Gemini 3 (dic 2025) cambió los delimitadores matemáticos de `$...$` / `$$...$$` a `\(...\)` / `\[...\]`. El prompt ya no gestiona esta conversión — la resuelven dos herramientas del vault:

| Herramienta | Rol |
|---|---|
| Plugin `Fix Math for Obsidian` (mod alx-rul) | Convierte `\(...\)` / `\[...\]` al importar en Obsidian |
| Script `notebooklm_fix/src/main.py` | Correcciones adicionales (tikz, Cornell, arrays, marginalia) |

Documentación del script: `_app/shellcommands/shellcmd_NBLM_fix.md`

---

## Estructura del prompt

El prompt define tres mensajes de trabajo:

- **Mensaje 1** — Transcripción + complemento de un subtítulo
- **Mensaje 2** — Ejercicios de libros fuente
- **Mensaje 3** — Ejercicios del cuaderno

Cada subtítulo de teoría se estructura en bloque Cornell. Los ejemplos resueltos y bloques IMA van fuera del Cornell.

---

## Notas

- `ETN607-transcription-divisions.md` — archivo auxiliar de divisiones de temas, no es un prompt independiente.
- `ETN607-transcription.md` — versión v1, conservada como referencia histórica.

---

%%
# galaxy-links
[[_app/notebooklm/prompts/ETN607/ETN607-transcription-v3.md]]
[[_app/notebooklm/prompts/ETN607/ETN607-transcription.md]]
[[_app/notebooklm/guides/ETN607/ETN607_latex.md]]
[[_app/notebooklm/guides/ETN607/ETN607_TikzJax.md]]
[[_app/shellcommands/shellcmd_NBLM_fix.md]]
[[Semesters/Sem_04/ETN607/_library_ETN607.md]]
%%
