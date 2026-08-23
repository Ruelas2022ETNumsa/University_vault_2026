---
galaxy_body: ship
project: "latex-overleaf-estructura-profesional"
date: 2026-08-23
status: in-orbit
fleet: Latex
blocked_by:
---
%%
galaxy_body: ship → carrier si el proyecto escala (necesita carpeta propia y archivos extra)

status:
- docked: en dock/, esperando operator
- in-orbit: fue trabajado, pausado sin dependencia externa
- delayed: bloqueado por dependencia externa — ver blocked_by
- delivered: terminado y documentado, listo para archivar
- aborted: proyecto no viable, descartado
%%

## Handoff
%%
Sobreescribir con edit_file al cerrar cada sesión.
%%

**Última sesión:** 2026-08-23 — sesión alx-rul
**Retomar desde:** definir `\lstinputlisting` en `Anexos/` o cerrar task
**Completado esta sesión:** arquitectura completa definida y documentada — `subfiles`, numeración, draft, `\graphicspath`, estructura vault vs Overleaf, dos READMEs (general y ETN1015)
**Próximo paso:** `Anexos/` — convención `\lstinputlisting` (pendiente menor)
**Preguntas de cierre:** —

---

## Resumen y objetivo

Mejorar la estructura profesional del proyecto LaTeX en Overleaf (pdfLaTeX).
Meta: compilación eficiente, organización escalable por laboratorio, y flujo limpio Obsidian → Overleaf.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-23 | Mantener `\input` para preámbulo y carátula | `\include` forzaría salto de página no deseado en carátula |
| 2026-08-23 | Migrar capítulos a paquete `subfiles` en lugar de `\include` | `subfiles` permite compilar cada laboratorio independientemente en Overleaf; `\include` solo permite compilación parcial desde el main |
| 2026-08-23 | No convertir a `.sty` todavía | El proyecto aún no tiene la madurez suficiente para justificarlo |

> [!note]- Descartadas
> `\include` + `\includeonly` para capítulos — descartado porque no permite compilar un capítulo solo sin pasar por `Main_Include.tex`. Reemplazado por `subfiles`.

---

## Planificación

El proyecto LaTeX ya tiene una base sólida y modular. Las mejoras son incrementales, no una refactorización.
Restricciones: debe compilar en Overleaf con pdfLaTeX sin cambios de clase o motor.

Enfoque elegido: **paquete `subfiles`** para capítulos. Cada archivo de `Capitulos/` agrega una línea de encabezado (`\documentclass[../Main_Include.tex]{subfiles}`) que le permite compilarse solo en Overleaf, reutilizando el preámbulo del main automáticamente. Ideal para escalar a muchos laboratorios.

El preámbulo y la carátula siguen con `\input` — no se tocan.

---

## Sugerencias

—

---

## Flujo de pasos

1. Agregar `\usepackage{subfiles}` en `Preambulo/Preambulo.tex`
2. Editar `Main_Include.tex`: cambiar `\input{Capitulos/...}` → `\subfile{Capitulos/...}` para capítulos (carátula se queda con `\input`)
3. Editar `Capitulos/Laboratorio1_903.tex`: agregar encabezado `subfiles` al inicio y `\end{document}` al final
4. Verificar compilación del main y del laboratorio solo en Overleaf
5. Leer `Preambulo/Preambulo.tex` y actualizar `\graphicspath` con multi-ruta
6. Crear subcarpetas `Lab1/`, `Lab2/` en `Graficos/`
7. Definir convención `\lstinputlisting` para `Anexos/` y documentar en README
8. Actualizar README con los cambios aplicados y la nueva convención `subfiles`

---

## Tareas

**Migración a subfiles:**
- [x] `Preambulo/Preambulo.tex` — agregar `\usepackage{subfiles}`
- [x] `Main_Include.tex` — cambiar `\input{Capitulos/...}` → `\subfile{Capitulos/...}` para capítulos
- [x] `Capitulos/Laboratorio1_903.tex` — agregar encabezado `subfiles` y `\end{document}` final
- [x] `Main_Include.tex` — `\setcounter{page}{1}` tras carátula para numeración correcta
- [x] `Capitulos/Laboratorio1_903.tex` — `\backgroundsetup{contents={}}` para suprimir draft standalone
- [x] Verificar compilación completa desde `Main_Include.tex` en Overleaf
- [x] Verificar compilación standalone de `Laboratorio1_903.tex` en Overleaf

**Estructura y organización:**
- [x] `Preambulo/Preambulo.tex` — actualizar `\graphicspath` a multi-ruta (Lab1–Lab5, Legacy)
- [x] `Graficos/` — subcarpetas Lab1–Lab5 creadas, Cap3legacy renombrada a Legacy
- [ ] `Anexos/` — definir estructura y convención con `\lstinputlisting`
- [ ] Reestructurar vault: mover contenido actual a `ETN903/` dentro de `Latex/`

**Documentación:**
- [x] `Latex/README.md` — readme general del vault (estructura, flujo, convenciones)
- [x] `ETN1015/README.md` — readme de materia (solo archivos de esa carpeta)
- [x] `README_vault.md` — vaciado, borrar desde Obsidian

---

## Preguntas abiertas

- ¿`Anexos/` se organiza por laboratorio (`Lab1/`, `Lab2/`) o por tipo de archivo (`.m`, `.py`)?
- ¿`Cap3legacy/` se integra eventualmente o se deja como referencia estática?

---

## Recursos

**Archivos clave:**
- `E:\University_vault_2026\Latex\Main_Include.tex`
- `E:\University_vault_2026\Latex\Preambulo\Preambulo.tex`
- `E:\University_vault_2026\Latex\Preambulo\Colores.tex`
- `E:\University_vault_2026\Latex\Preambulo\TikzEstilos.tex`
- `E:\University_vault_2026\Latex\Preambulo\Entornos.tex`
- `E:\University_vault_2026\Latex\Capitulos\Laboratorio1_903.tex`
- `E:\University_vault_2026\Latex\Graficos\`
- `E:\University_vault_2026\Latex\Anexos\`
- `E:\University_vault_2026\Latex\README.md`

**Referencia:**
- Overleaf — multi-file projects: https://www.overleaf.com/learn/latex/Multi-file_LaTeX_projects
- Overleaf — management large project: https://www.overleaf.com/learn/latex/Management_in_a_large_project
- subfiles CTAN docs: https://ctan.csail.mit.edu/macros/latex2e/contrib/subfiles/subfiles.pdf
