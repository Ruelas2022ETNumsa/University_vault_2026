---
galaxy_body: ship
project: "tsk_prompt_guides_1015"
date: 2026-08-12
status: in-orbit
fleet: ETN1015
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

**Última sesión:** 2026-08-12 — 19:27
**Retomar desde:** Verificar referencias al prompt si corresponde (paso 9)
**Completado esta sesión:**
- Guía TikZ `ETN1015_tikz.md` creada (Bloques A, B y C completos)
**Próximo paso:** Verificar que el prompt `ETN1015-study.md` referencia correctamente las guías como fuentes del notebook
**Preguntas de cierre:** —

---

## Resumen y objetivo

Crear el stack completo de prompts y guías para NotebookLM de la materia ETN1015 — Procesamiento Digital de Señales, siguiendo la arquitectura ya establecida en MAT101. El objetivo es que NBLM actúe como tutor de la materia con libro base Rao, notación correcta y bloques de visualización listos para copiar en Obsidian.

---

## Decisiones

| Fecha      | Decisión | Motivo |
| ---------- | -------- | ------ |
| 2026-08-12 | Libro base es Rao — los demás son soporte | El docente dicta siguiendo Rao cap. a cap. |
| 2026-08-12 | Eliminar sección Cornell del prompt | ETN1015 no usa notas Cornell — no aplica |
| 2026-08-12 | Nombre exacto del PDF de Rao incluido en el prompt | NBLM necesita el nombre para localizar la fuente: `K. Deergha Rao — Signals and Systems.pdf` |
| 2026-08-12 | Corrección de identificador de bloque en el prompt | NBLM tiene bug con `desmos-graph` inline — el prompt indica tres backticks + salto de línea + identificador |
| 2026-08-12 | En la guía los bloques llevan ` ```desmos-graph ` completo | La guía es para que NBLM copie la sintaxis correcta — debe mostrarla tal cual |
| 2026-08-12 | Paleta de colores se queda en la guía, no en el prompt | El prompt no necesita la paleta — la guía es la referencia de colores |

> [!note]- Descartadas
> — Sin descartadas por ahora.

---

## Planificación

Replicar la arquitectura de MAT101 para ETN1015, adaptando cada archivo al dominio de señales y sistemas. El stack tiene tres capas:

1. **Prompt** (`ETN1015-study.md`) — instrucciones de comportamiento para NBLM: modos de respuesta, libro base, flujo de uso, reglas de visualización sin paleta de colores.
2. **Guía Desmos** (`ETN1015_desmos.md`) — sintaxis, reglas, checklist y biblioteca de ejemplos por capítulo de Rao.
3. **Guía TikZ** (`ETN1015_tikz.md`) — pendiente. Cubre diagramas de bloques, plano de polos/ceros, diagramas de flujo de señal — todo lo que Desmos no puede hacer bien.

Restricciones clave:
- NBLM tiene bug con identificador de bloque — corregido en el prompt, no en las guías.
- Desmos es continuo — señales discretas se aproximan; para diagramas de tallo exactos usar TikZ.

---

## Sugerencias

—

---

## Flujo de pasos

1. [x] Leer `MAT101-study.md` como base estructural
2. [x] Leer `_library_ETN1015.md` para stack de libros y temario
3. [x] Crear `ETN1015-study.md` — prompt principal
4. [x] Refinar prompt: eliminar Cornell, fijar Rao como base, nombre exacto del PDF, corrección bug identificador, quitar paleta
5. [x] Leer `MAT101_desmos.md` como base de la guía
6. [x] Crear `ETN1015_desmos.md` — guía Desmos con Bloques A, B y C
7. [x] Corregir identificadores en Bloque C — todos con ` ```desmos-graph `
8. [x] Crear `ETN1015_tikz.md` — guía TikZ
9. [ ] Referenciar guías desde el prompt (`ETN1015-study.md`) si corresponde

---

## Tareas

- [x] Crear prompt `ETN1015-study.md`
- [x] Eliminar sección Cornell del prompt
- [x] Fijar Rao como libro base con nombre exacto del PDF
- [x] Corregir bug de identificador de bloque en el prompt
- [x] Quitar paleta de colores del prompt
- [x] Crear guía `ETN1015_desmos.md` (Bloques A, B, C)
- [x] Corregir identificadores ` ```desmos-graph ` en todos los bloques del Bloque C
- [x] Crear guía `ETN1015_tikz.md`
- [ ] Verificar que el prompt referencia correctamente las guías como fuentes del notebook

---

## Preguntas abiertas

— Sin preguntas abiertas al cierre de sesión.

---

## Recursos

**Archivos creados / modificados esta sesión:**
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN1015\ETN1015-study.md`
- `E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_desmos.md`
- `E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_tikz.md`

**Archivos de referencia:**
- `E:\University_vault_2026\_app\notebooklm\prompts\MAT101\MAT101-study.md` — estructura base del prompt
- `E:\University_vault_2026\_app\notebooklm\guides\MAT101\MAT101_desmos.md` — estructura base de la guía
- `E:\University_vault_2026\_app\notebooklm\guides\MAT101\MAT101_TikzJax.md` — referencia para la guía TikZ pendiente
- `E:\University_vault_2026\Semesters\Sem_08\ETN1015\_library_ETN1015.md` — stack de libros y temario oficial
