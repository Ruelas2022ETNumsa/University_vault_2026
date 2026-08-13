---
galaxy_body: dropship
carrier: "[[_hangar/NBLM_update/tsk_NBLM_update.md]]"
scope: opcion-A
status: activo
date: 2026-08-13
---

## Proposito

Sesión dedicada a actualizar el script `notebooklm_fix/src/main.py` a la nueva notación matemática de NotebookLM (`\(...\)` / `\[...\]`). Analizar qué correcciones siguen siendo válidas y cuáles deben modificarse o eliminarse.

---

## Contenido

### Contexto

NotebookLM dejó de usar `$...$` y `$$...$$`. Ahora entrega:
- Inline: `\(expresión\)`
- Display: `\[expresión\]`

El plugin de corrección LaTeX en Obsidian convierte automáticamente al importar. El script `notebooklm_fix` tiene 5 correcciones — algunas pueden seguir siendo válidas, otras no.

### Preguntas a responder en la sesión

- ¿La corrección `\frac → \dfrac` (regex 1) sigue siendo necesaria con la nueva notación, o el plugin ya lo maneja?
- ¿La corrección de arrays (regex 3) aplica igual con `\[...\]` en lugar de `$$...$$`?
- ¿Las correcciones de Cornell (regex 0) y marginalia (regex 4) siguen siendo válidas? — probablemente sí, son independientes de la notación matemática
- ¿La corrección de desmos (regex 2) sigue siendo relevante?
- ¿El plugin LaTeX cubre alguna de estas correcciones y las hace redundantes?

### Estado

Pendiente — sesión dedicada. Leer `shellcmd_NBLM_fix.md` y el `main.py` actual como punto de partida.
