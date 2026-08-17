---
title: "DOC — ETN607 Transcription Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts]
date_created: 2026-08-13
date_updated: 2026-08-17
reviewed: 2026-08-17
status: activo
---

# DOC — ETN607 Transcription Prompt

Documentación del prompt de transcripción para ETN607 (Mecánica Clásica / Lagrange) en NotebookLM.

---

## Archivos activos

| Archivo | Rol | Estado |
|---|---|---|
| `ETN607-transcription_Av4.md` | Transcripción pura — bloques Cornell, figuras del apunte, IMA | en pruebas |
| `ETN607-transcription_BCv4.md` | Complemento B/C — ad-note 6 backticks, embed PDF++, IMA-SRC, TikZJax fallback | probado ✅ |

> Los demás archivos (`v2`, `v3`, `v4`) son **legacy** — conservados como referencia. No usar.

---

## Historial de versiones

| Versión | Fecha | Cambios |
|---|---|---|
| v1 | anterior | Versión original — notación `$...$` / `$$...$$` |
| v2 | 2026-08-13 | Adaptación a nueva notación NBLM (`\(...\)` / `\[...\]`) tras migración a Gemini 3 |
| v3 | 2026-08-13 | Eliminadas instrucciones de delimitadores del prompt — resueltas por plugin + script. Referencia al Cornell clarificada. |
| A-v4 | 2026-08-17 | Separación en dos prompts. A: solo transcripción — sin complemento ni referencias a libros fuente. Detección de figuras del apunte con bloque IMA. |
| BC-v4 | 2026-08-17 | BC: complemento nivel B/C con embed PDF++ + IMA-SRC en `%% %%` + TikZJax fallback. Reemplazo de callout nativo por `ad-note` (ebullient/obsidian-admonition). Bloque abre y cierra con **6 backticks** para permitir bloques de código internos (tikz) sin colisión. Workaround de script: ver nota abajo. **Probado y comprobado.** |

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

## Estructura de los prompts

**ETN607-transcription_Av4** — dos mensajes:
- **Mensaje 1** — Transcripción de subtítulo(s) del apunte manuscrito
- **Mensaje 2** — Ejercicios del cuaderno

Cada subtítulo de teoría se estructura en bloque Cornell. Ejemplos resueltos e IMA van fuera del Cornell.

**ETN607-transcription_BCv4** — dos mensajes:
- **Mensaje 1** — Complemento nivel B/C de un rango de subtítulos
- **Mensaje 2** — Complemento nivel B/C de un concepto individual (prueba puntual)

Cada subtítulo se estructura en bloque `ad-note` (6 backticks apertura/cierre). Figuras con embed `[[]]` + IMA-SRC en `%% %%`. TikZJax como fallback si no hay figura.

> [!warning] Workaround — script `notebooklm_fix`
> El script de corrección de ecuaciones (`main.py`) no procesa el contenido del bloque si los 6 backticks de apertura están intactos — los interpreta como fence cerrado.
> **Solución:** anteponer `\` a los 6 backticks de apertura (`\``````ad-note`) antes de correr el script. Esto rompe el fence para el parser del script sin afectar el render en Obsidian. Restaurar luego si es necesario.

---

## Notas

- `ETN607-transcription-divisions.md` — archivo auxiliar de divisiones de temas, no es un prompt independiente.
- `ETN607-transcription.md` — versión v1, conservada como referencia histórica.
- `ETN607-transcription-v2.md`, `v3.md`, `v4.md` — versiones legacy, no usar.

---

%%
# galaxy-links
[[_app/notebooklm/prompts/ETN607/ETN607-transcription_Av4.md]]
[[_app/notebooklm/prompts/ETN607/ETN607-transcription_BCv4.md]]
[[_app/notebooklm/prompts/ETN607/ETN607-transcription-v3.md]]
[[_app/notebooklm/prompts/ETN607/ETN607-transcription.md]]
[[_app/notebooklm/guides/ETN607/ETN607_latex.md]]
[[_app/notebooklm/guides/ETN607/ETN607_TikzJax.md]]
[[_app/shellcommands/shellcmd_NBLM_fix.md]]
[[Semesters/Sem_04/ETN607/_library_ETN607.md]]
%%
