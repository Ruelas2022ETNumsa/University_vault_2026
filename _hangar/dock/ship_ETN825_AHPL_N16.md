---
galaxy_body: ship
project: "ETN825 AHPL — N16: ejemplos pregunta→respuesta para NotebookLM"
date: 2026-08-29
status: in-orbit
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-29
**Retomar desde:** Fase 3 — re-subir `ETN825_AHPL.md` a NotebookLM y re-probar snippets H y G con puntero
**Completado esta sesión:** N16 escrita en la guía con edit_file (Par 1–Par 4 + tabla de tamaños); N16 duplicado eliminado; N11 paso 7 corregido `(3,1)` → `(3,8)`
**Próximo paso:** re-subir guía a NotebookLM → re-probar H y G capturando con puntero (no botón)
**Preguntas de cierre:** —

---

## Resumen y objetivo

La guía `ETN825_AHPL.md` tiene reglas de notación AHPL bien definidas (N1–N15) pero le faltaba una sección de ejemplos de pares pregunta→respuesta (N16). Sin esos ejemplos, NotebookLM genera tamaños incorrectos en declaraciones y otros errores de contenido. N16 está redactada y lista en `Rubbish\section.md` — falta pegarla en la guía y verificar.

---

## Contexto para sesión nueva

> Leer esto si se retoma en una sesión distinta — suficiente para arrancar sin re-explicar.

**Archivos clave:**
- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal — N16 va al final del BLOQUE D, después de N15, antes del bloque `%%`
- `E:\University_vault_2026\Rubbish\section.md` — N16 lista para copiar/pegar o escribir con edit_file
- `E:\University_vault_2026\notebooklm_question.md` — snippets H y G para re-probar después de subir la guía actualizada
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt activo — ya tiene la línea de tamaños agregada (`MEMORY/OUTPUTS/COMBUS: vectores SIEMPRE con tamaño. DR[18] no DR. CHAR[8] no CHAR.`) — NO tocar

**Estado al cierre de esta sesión:**
- Guía `ETN825_AHPL.md` — N1–N15 corregidas (v3). N16 NO escrita todavía en la guía — está en `Rubbish\section.md`.
- Prompt `BCv1i` — línea de tamaños agregada. Tamaño actual: ~9900 chars (bajo el límite de 10000).
- N16 en `section.md` — versión final con: tabla de tamaños estándar + Par 1 (módulo TEST) + Par 2 (PRINTER INTERFACE) + Par 3 (bucle de espera) + Par 4 (operador `*`).

**Convenciones definidas (no renegociar):**
- Bloques de código AHPL: `~` como prefijo para negados
- Tablas KaTeX: `\overline{X}` para negados, `\( \)` inline
- Transferencia: `←` / Conexión bus: `=` / Row concatenate: `!`
- Delimitadores: `\( \)` inline — NO `$$`, NO `\[ \]` para bloques AHPL
- NUNCA `\begin{aligned}`, NUNCA `\begin{array}`, NUNCA `$$`
- `COMBUS:` (sin S) — canónico del libro
- Tamaños: DR[18], CR[8], IOBUS[18], CHAR[8], AC[18], PC[12], IR[18], MD[18], MA[12]

---

## Hallazgos de esta sesión

| # | Hallazgo | Impacto |
|---|---|---|
| 1 | El botón de copiar de NotebookLM stripea corchetes `[]` y su contenido | Los tamaños `DR[18]` se pierden al copiar con el botón — usar arrastre con puntero |
| 2 | NotebookLM SÍ genera tamaños cuando tiene referencia — pero infiere `[1]` o `[2]` sin ella | N16 con tabla de tamaños estándar resuelve esto |
| 3 | El error era del botón, no de la guía ni del prompt | Workaround permanente: capturar output con puntero, no con botón |
| 4 | Prompt con línea de tamaños agregada no resolvió el problema solo | La guía (N16) es la pieza que falta — el prompt solo no alcanza para AHPL como lenguaje de nicho |
| 5 | Gemini tiene acceso a las mismas fuentes del notebook (incluyendo el prompt si está cargado) | Comportamiento equivalente a NotebookLM — se puede usar indistintamente para tests |

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-28 | Formato final: bloque de código AHPL + tabla KaTeX inline | KaTeX puro no renderizó de forma confiable; bloque de código sí funcionó |
| 2026-08-28 | Delimitadores: `\( \)` inline — NO `$$` | `$$` rompió renderizado en versiones anteriores de NotebookLM |
| 2026-08-29 | Tests con todo cargado — no quitar guía ni prompt | El comportamiento con todo presente es el que importa para el usuario final |
| 2026-08-29 | Workaround botón: capturar output con puntero, no con botón de copiar | El botón stripea `[]` — bug confirmado empíricamente, sin fix disponible |
| 2026-08-29 | Notación `()` para declaraciones — postergada | Requiere cambiar N1/N2 y el libro usa `[]`; evaluar después de verificar si N16 resuelve el problema |
| 2026-08-29 | Tabla de tamaños estándar incluida en N16 | Modelo infería `[1]`/`[2]` sin referencia — tabla explícita lo corrige |

> [!note]- Descartadas
> - Generar N16 sin verificar contra NotebookLM — descartado; los pares deben reflejar outputs reales corregidos
> - Notación `()` para tamaños en declaraciones — postergada, no descartada
> - Cambio inmediato de delimitadores `\[ \]` → `$$` — postergado; plugin disponible si hace falta

---

## Planificación

N16 está lista. El único paso pendiente es escribirla en la guía y verificar que el output de NotebookLM mejora. Si los tamaños siguen incorrectos después de subir la guía actualizada → evaluar notación `()` para declaraciones como siguiente línea de ataque.

---

## Flujo de pasos

### ✅ Fase 1 — obtener y analizar outputs (completada)
- Snippets H y G ejecutados x2
- Errores documentados: sin tamaños, tamaños incorrectos (`[1]`/`[2]`), bug del botón
- N16 redactada con pares corregidos

### ⬜ Fase 2 — escribir N16 en la guía
1. Leer el final de `ETN825_AHPL.md` para confirmar posición de inserción (después de N15, antes de `%%`)
2. Escribir N16 con `edit_file` — contenido en `Rubbish\section.md`
3. Verificar que el archivo quedó bien con `read_text_file` (últimas 20 líneas)

### ⬜ Fase 3 — verificar
4. Re-subir `ETN825_AHPL.md` actualizada a NotebookLM (reemplazar fuente anterior)
5. Probar snippets H y G de `notebooklm_question.md` — capturar con puntero
6. Verificar: ¿`DR[18]`, `CR[8]`, `IOBUS[18]` aparecen correctos?
7. Si sí → ship delivered. Si no → evaluar notación `()` o agregar par adicional

---

## Tareas

- [x] Leer todos los archivos del proyecto
- [x] Diagnóstico del estado actual
- [x] Crear ship
- [x] Crear snippets de prueba en `notebooklm_question.md`
- [x] Ejecutar snippet H — capturar output (x2)
- [x] Ejecutar snippet G — capturar output (x2)
- [x] Analizar outputs — documentar errores
- [x] Identificar bug del botón de copiar
- [x] Redactar N16 en `Rubbish\section.md`
- [x] Agregar tabla de tamaños estándar a N16
- [x] Revisar y corregir formato de N16
- [x] Escribir N16 en `ETN825_AHPL.md` con `edit_file`
- [x] Eliminar N16 duplicado
- [x] Corregir N11 paso 7: `(3,1)` → `(3,8)`
- [ ] Re-subir guía a NotebookLM
- [ ] Re-prueba final — snippets H y G con puntero
- [ ] Cerrar ship (status: delivered)

---

## Preguntas abiertas

- ¿Notación `()` para tamaños en declaraciones? — evaluar solo si N16 no resuelve el problema de tamaños
- ¿Agregar Par 5 con imagen de ejercicio real de la cátedra? — opcional, si el usuario trae material

---

## Recursos

- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal
- `E:\University_vault_2026\Rubbish\section.md` — N16 lista para insertar
- `E:\University_vault_2026\notebooklm_question.md` — snippets de prueba H y G
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt activo
- `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_ejemplos 1.md` — historia completa de correcciones v1/v2/v3
- Hill & Peterson — Digital Systems 2ª ed. — p. 105 (operador `*`) y p. 349-350 (PRINTER INTERFACE)
