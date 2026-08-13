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
**Retomar desde:** — stack completo entregado
**Completado esta sesión:**
- Guía TikZ `ETN1015_tikz.md` creada (Bloques A, B y C completos)
- Referencias a guías agregadas al prompt `ETN1015-study.md`
- `obsidian_notation.md` actualizada con nota de notación para ETN1015
- Ejemplo N19 (plano z) depurado y corregido — reescrito en `tikzpicture` puro sin `pgfplots` por incompatibilidad con el plugin
- Decisión documentada: bloques TikZ con `axis` de pgfplots no renderizan en obsidian-tikzjax cuando incluyen etiquetas con modo math en nodos
**Próximo paso:** Resolver bug de bloques de código con triple backtick + salto de línea + etiqueta (desmos / tikz) — NBLM no los anota; requiere reconfigurar el prompt.
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
| 2026-08-12 | Referencias a guías agregadas al inicio del prompt | NBLM debe consultar `ETN1015_desmos.md` y `ETN1015_tikz.md` antes de generar cualquier bloque de código |
| 2026-08-12 | `obsidian_notation.md` actualizada con bloque ETN1015 | La guía es general — se agregó sin eliminar contenido existente |
| 2026-08-12 | Ejemplo N19 reescrito sin `pgfplots` | `axis` con etiquetas en modo math falla en obsidian-tikzjax — plano z dibujado en `tikzpicture` puro con coordenadas manuales |

> [!note]- Descartadas
> - **Fix en `fix-math` plugin (main.js):** el plugin de Obsidian protege intencionalmente los bloques de código — `splitByCodeFences` los marca como `type: code` y los pasa sin tocar. Agregar el fix de etiqueta ahí requeriría operar justo sobre lo que el plugin excluye a propósito. Descartado. Además el `main.js` es compilado desde `main.ts` — editarlo directo es frágil.
> - **Fix vía prompt en NBLM:** se intentó indicar en el prompt la sintaxis correcta (triple backtick + etiqueta en la misma línea). NBLM sigue generando el salto de línea intermedio de forma inconsistente. No es suficiente como solución única.

---

## Planificación

Replicar la arquitectura de MAT101 para ETN1015, adaptando cada archivo al dominio de señales y sistemas. El stack tiene tres capas:

1. **Prompt** (`ETN1015-study.md`) — instrucciones de comportamiento para NBLM: modos de respuesta, libro base, flujo de uso, reglas de visualización sin paleta de colores.
2. **Guía Desmos** (`ETN1015_desmos.md`) — sintaxis, reglas, checklist y biblioteca de ejemplos por capítulo de Rao.
3. **Guía TikZ** (`ETN1015_tikz.md`) — cubre diagramas de bloques, plano de polos/ceros, diagramas de flujo de señal — todo lo que Desmos no puede hacer bien.

Restricciones clave:
- NBLM tiene bug con identificador de bloque — corregido en el prompt, no en las guías.
- Desmos es continuo — señales discretas se aproximan; para diagramas de tallo exactos usar TikZ.

---

## Sugerencias

### Enfoque para resolver el bug de etiqueta de bloque

El bug: NBLM genera ` ``` ` + salto de línea + `desmos-graph` (o `tikz`) en lugar de ` ```desmos-graph ` pegado. Obsidian no reconoce la etiqueta y el bloque no renderiza.

**Tres enfoques evaluados:**

**A) Ampliar `main.py` (recomendado)** 
El parche natural es agregar una regex en `main.py` antes del bloque 2 (desmos sin etiqueta), que detecte el patrón ` ``` ` + newline + etiqueta conocida y lo colapse en una sola línea. Ya existe el patrón para `desmos-graph` (bloque 2) — es extenderlo para `tikz` y para el caso con salto de línea intermedio. Ventaja: mismo archivo, mismo flujo, misma responsabilidad. El script ya corre sobre el archivo activo desde Obsidian.

```python
# Patrón a agregar en main.py
# Colapsa: ```\n<etiqueta>\n  →  ```<etiqueta>\n
content = re.sub(r'```\n(desmos-graph|tikz)\n', r'```\1\n', content)
```

**B) Script de clipboard (idea tuya — copiar desde NBLM → fix → pegar ya corregido)** 
Un script Python con `pyperclip` que lee el portapapeles, aplica las mismas regex de `main.py`, y devuelve el contenido corregido al portapapeles. El flujo sería: copiar en NBLM → ejecutar script (hotkey global) → pegar en Obsidian ya limpio. Ventaja: el fix ocurre antes de tocar el vault. Desventaja: requiere `pyperclip` instalado y un hotkey de sistema (AutoHotkey en Windows o similar) para ejecutarlo sin abrir terminal.

**C) Script separado solo para este bug** 
Un `fix_codeblocks.py` independiente de `main.py`, invocado desde Obsidian igual que el actual. Mantiene separación de responsabilidades pero agrega fricción (otro comando, otro archivo). Solo vale si el scope crece mucho.

**Recomendación:** opción A para el vault (ampliar `main.py`) + opción B como mejora futura si el flujo clipboard se vuelve frecuente. Son complementarias, no excluyentes.

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
9. [x] Referenciar guías desde el prompt (`ETN1015-study.md`) si corresponde
10. [x] Actualizar `obsidian_notation.md` con nota para ETN1015
11. [x] Depurar y corregir ejemplo N19 — plano z reescrito en `tikzpicture` puro

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
- [x] Verificar que el prompt referencia correctamente las guías como fuentes del notebook
- [x] Actualizar `obsidian_notation.md` con bloque de notación para ETN1015
- [x] Depurar ejemplo N19 (plano z) — reescrito en `tikzpicture` puro
- [ ] **BUG:** NBLM no anota bloques de código con sintaxis ` ``` ` + salto de línea + etiqueta (`desmos-graph`, `tikz`). Reconfigurar el prompt para parchear este comportamiento.

---

## Preguntas abiertas

- ¿Cómo debe indicarse en el prompt que NBLM anote bloques con triple backtick + salto de línea + etiqueta? ¿Instrucción explícita de copia literal, ejemplo incluido en el prompt, o ambos?

---

## Recursos

**Archivos creados / modificados esta sesión:**
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN1015\ETN1015-study.md`
- `E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_desmos.md`
- `E:\University_vault_2026\_app\notebooklm\guides\ETN1015\ETN1015_tikz.md`
- `E:\University_vault_2026\_app\notebooklm\general\obsidian_notation.md`

**Archivos de referencia:**
- `E:\University_vault_2026\_app\notebooklm\prompts\MAT101\MAT101-study.md` — estructura base del prompt
- `E:\University_vault_2026\_app\notebooklm\guides\MAT101\MAT101_desmos.md` — estructura base de la guía
- `E:\University_vault_2026\_app\notebooklm\guides\MAT101\MAT101_TikzJax.md` — base estructural de la guía TikZ
- `E:\University_vault_2026\Semesters\Sem_08\ETN1015\_library_ETN1015.md` — stack de libros y temario oficial
