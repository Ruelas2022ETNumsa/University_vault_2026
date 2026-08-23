---
galaxy_body: ship
project: "latex-overleaf-estructura-profesional"
date: 2026-08-23
status: docked
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
**Retomar desde:** `Main_Include.tex` — listo para aplicar cambios, no se tocó nada aún
**Completado esta sesión:** lectura de README, Main_Include.tex y análisis del estado actual
**Próximo paso:** aplicar `\include` + `\includeonly` en `Main_Include.tex` (tarea 1)
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
| 2026-08-23 | Migrar capítulos a `\include` | Permite `\includeonly` para compilación parcial en Overleaf |
| 2026-08-23 | No convertir a `.sty` todavía | El proyecto aún no tiene la madurez suficiente para justificarlo |

> [!note]- Descartadas
> — ninguna por ahora

---

## Planificación

El proyecto LaTeX ya tiene una base sólida y modular. Las mejoras son incrementales, no una refactorización.
Restricciones: debe compilar en Overleaf con pdfLaTeX sin cambios de clase o motor.
Enfoque: aplicar mejoras en orden de prioridad (alta → baja) sin romper la compilación actual.

---

## Sugerencias

—

---

## Flujo de pasos

1. Leer `Main_Include.tex` y aplicar `\include` + bloque `\includeonly` comentado
2. Leer `Preambulo/Preambulo.tex` y actualizar `\graphicspath` con multi-ruta
3. Crear subcarpetas `Lab1/`, `Lab2/` en `Graficos/`
4. Definir convención `\lstinputlisting` para `Anexos/` y documentar en README
5. Actualizar README con los cambios aplicados

---

## Tareas

- [ ] `Main_Include.tex` — cambiar `\input{Capitulos/...}` → `\include{Capitulos/...}` para capítulos
- [ ] `Main_Include.tex` — agregar bloque `\includeonly` comentado con instrucciones de uso
- [ ] `Preambulo/Preambulo.tex` — verificar y actualizar `\graphicspath` a multi-ruta
- [ ] `Graficos/` — crear subcarpetas `Lab1/` y `Lab2/`
- [ ] `Anexos/` — definir estructura y convención con `\lstinputlisting`
- [ ] `README.md` — actualizar con cambios aplicados y convenciones nuevas
- [ ] Verificar compilación en Overleaf después de los cambios

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
- Overleaf docs: `\include` vs `\input` — https://www.overleaf.com/learn/latex/Management_in_a_large_project
