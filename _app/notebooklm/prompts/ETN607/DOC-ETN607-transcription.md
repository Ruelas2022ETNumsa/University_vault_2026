---
title: "DOC — ETN607 Transcription Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts]
date_created: 2026-08-13
date_updated: 2026-08-21
reviewed: 2026-08-21
status: activo
---

# DOC — ETN607 Transcription Prompt

Documentación del prompt de transcripción para ETN607 (Mecánica Clásica / Lagrange) en NotebookLM.

---

## Archivos activos

| Archivo | Rol | Estado |
|---|---|---|
| `ETN607-transcription_Av6.md` | Transcripción pura + corrección contra libros fuente | activo ✅ |
| `ETN607-comp_apuntes_BCv4i.md` | Complemento B/C guiado por el apunte | probado ✅ |
| `ETN607-comp_indice_BCv4ii.md` | Complemento B/C guiado por el índice del docente + ejercicios | en pruebas |
| `ETN607-transcription_Av5.md` | Transcripción pura (sin corrección) | legacy |

> Los demás archivos (`Av5`, `Av4`, `BCv4`, versiones anteriores) son **legacy** — conservados como referencia. No usar.

---

## Para qué sirve cada prompt

### `ETN607-transcription_Av6` — Transcripción + corrección
**Cuándo usarlo:** cuando se tiene el PDF del apunte manuscrito y se quiere transcribir a Markdown, con opción de corrección posterior contra los libros fuente.

**Mensajes disponibles:**
- **M1** — transcribir un subtítulo (o rango) del apunte
- **M2** — transcribir ejercicios del cuaderno por enunciado o ecuación inicial
- **M3** — corregir un subtítulo ya transcripto contra los libros fuente (T1–T2)

**Flujo típico:** M1 o M2 → revisar → M3 para corregir → revisar resultado y decidir qué incorporar.

**Qué produce:**
- M1/M2: bloques Cornell con transcripción fiel, detección de figuras (IMA dentro de `::note`), marginalia inline, mapas mentales en LaTeX, callouts con admonitions.
- M3: bloque completo corregido (Cornell o `##### Ej.`) con `%%< correcciones hechas %%` al inicio si hubo cambios. Sin correcciones → responde `"Subtítulo [Y]: sin correcciones."`

**Libros fuente para M3:**
- T1: Taylor Cap.1 · Goldstein Cap.1
- T2: Taylor Cap.1-2 · Alonso & Finn Vol.1 Cap.1-2

**Límite de caracteres:** 9966 / 10000 — margen mínimo, no agregar contenido sin revisar el conteo.

---

### `ETN607-transcription_Av5` — Transcripción (legacy)
**Reemplazado por Av6.** Conservado como referencia. No usar.

---

### `ETN607-comp_apuntes_BCv4i` — Complemento por apunte
**Cuándo usarlo:** cuando ya se tiene el apunte transcripto y se quiere complementar secciones específicas con los libros fuente. El apunte debe estar cargado como fuente en el notebook.

**Mensajes disponibles:**
- **M1** — complemento nivel B/C para un rango de subtítulos del apunte
- **M2** — complemento nivel B/C para un concepto puntual

**Qué produce:** bloques `ad-note` con definición formal, figura del libro (IMA-SRC o TikZJax), y ejercicios resueltos (nivel C).

---

### `ETN607-comp_indice_BCv4ii` — Complemento por índice + ejercicios
**Cuándo usarlo:** cuando se quiere complementar o practicar a partir del índice del docente, sin necesidad de tener el apunte cargado. Ideal para repasar antes de parcial o cubrir temas no transcriptos aún.

**Mensajes disponibles:**
- **M1** — complemento nivel B/C de un subtítulo del índice con límite de alcance
- **M2** — complemento nivel B/C de un concepto puntual
- **M3** — 1 ejercicio tipo examen resuelto paso a paso para un subtítulo
- **M4** — resolución de un enunciado propio ingresado por el usuario

**Qué produce:** bloques `ad-note` con definición formal + figura + ejercicios; o resolución completa con array LaTeX sin saltear pasos algebraicos.

---

## Fuentes guía que cargan los prompts

| Archivo | Ubicación | Rol | Av6 | comp_apuntes | comp_indice |
|---|---|---|---|---|---|
| `obsidian_notation.md` | `_app/notebooklm/guides/` | Sintaxis Obsidian, Cornell, callouts | ✅ | — | — |
| `_library_ETN607.md` | `Semesters/Sem_04/ETN607/` | Criterio de selección de libros por tema | — | ✅ | ✅ |
| `ETN607_latex.md` | `_app/notebooklm/guides/ETN607/` | Notación LaTeX de la materia | ✅ | — | — |
| `ETN607_TikzJax.md` | `_app/notebooklm/guides/ETN607/` | Reglas TikZJax para ETN607 | ✅ | ✅ | ✅ |

---

## Sistema de corrección de notación

La migración de NBLM a Gemini 3 (dic 2025) cambió los delimitadores matemáticos de `$...$` / `$$...$$` a `\(...\)` / `\[...\]`. El prompt ya no gestiona esta conversión — la resuelven dos herramientas del vault:

| Herramienta | Rol |
|---|---|
| Plugin `Fix Math for Obsidian` (mod alx-rul) | Convierte `\(...\)` / `\[...\]` al importar en Obsidian |
| Script `notebooklm_fix/src/main.py` | Correcciones adicionales (tikz, Cornell, arrays, marginalia) |

Documentación del script: `_app/shellcommands/shellcmd_NBLM_fix.md`

> [!warning] Workaround — script `notebooklm_fix`
> El script no procesa el contenido del bloque si los 6 backticks de apertura están intactos.
> **Solución:** anteponer `\` a los 6 backticks de apertura antes de correr el script. Restaurar luego si es necesario.

---

## Historial de versiones

| Versión | Fecha | Cambios clave |
|---|---|---|
| v1 | anterior | Versión original |
| v2 | 2026-08-13 | Adaptación a delimitadores Gemini 3 |
| v3 | 2026-08-13 | Eliminadas instrucciones de delimitadores — resueltas por plugin + script |
| Av4 | 2026-08-17 | Separación en dos prompts. A: solo transcripción |
| BCv4 | 2026-08-17 | Complemento B/C con embed PDF++ + IMA-SRC + TikZJax + ad-note |
| Av5 | 2026-08-20 | Marginalia lista completa + prohibición de generación · IMA dentro de ::note · callouts → admonitions · número de página · descripción automática de figura · mapas mentales LaTeX |
| BCv4i | 2026-08-20 | Número de página · descripción automática de figura · sistema IMA confirmado |
| BCv4ii | 2026-08-20 | Número de página · descripción automática de figura · sistema IMA confirmado · M3 ejercicio tipo examen · M4 resolución de enunciado propio |
| Av6 | 2026-08-21 | Fork de Av5 · M3 corrección contra libros fuente (T1–T2) · marginalia `%%<` unificada · límite 9966/10000 chars |

---

%%
# galaxy-links
[[ETN607-transcription_Av6]]
[[ETN607-transcription_Av5]]
[[ETN607-comp_apuntes_BCv4i]]
[[ETN607-comp_indice_BCv4ii]]
[[ETN607-transcription_Av4]]
[[ETN607-transcription]]
[[_app/notebooklm/guides/ETN607/ETN607_latex.md]]
[[_app/notebooklm/guides/ETN607/ETN607_TikzJax.md]]
[[_app/shellcommands/shellcmd_NBLM_fix.md]]
[[_library_ETN607]]
%%
