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
**Retomar desde:** Crear Par 5 en N16 — ejercicio real de la cátedra como ejemplo de imitación.
**Completado esta sesión:** notación `(N)` aplicada globalmente en guía y prompt — bloques de código incluidos. Verificado con output real de NotebookLM: tamaños correctos, formato correcto. `->` y `→` confirmados como equivalentes — ambos aceptados sin corrección.
**Próximo paso:** agregar Par 5 a N16 con ejercicio real de la cátedra.
**Preguntas de cierre:** —

---

## Resumen y objetivo

La guía `ETN825_AHPL.md` tiene reglas de notación AHPL bien definidas (N1–N15) y una sección de ejemplos de pares pregunta→respuesta (N16). El objetivo era que NotebookLM generara tamaños correctos en declaraciones y siguiera el formato de la guía. Verificado y confirmado con output real.

---

## Contexto para sesión nueva

> Leer esto si se retoma en una sesión distinta — suficiente para arrancar sin re-explicar.

**Archivos clave:**
- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal — Par 5 va al final de N16, antes del bloque `%%`
- `E:\University_vault_2026\Rubbish\section.md` — scratchpad para borradores
- `E:\University_vault_2026\notebooklm_question.md` — snippets H y G para re-probar
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt activo

**Estado al cierre de esta sesión:**
- Guía `ETN825_AHPL.md` — N1–N16 completas y corregidas. Notación `(N)` global aplicada.
- Prompt `promtpx.md` — tabla Notación unificada a `REG(N)`. Todo en `(N)`.
- Output NotebookLM verificado — tamaños correctos, formato correcto.

**Convenciones definidas (no renegociar):**
- Bloques de código AHPL: `~` como prefijo para negados
- Tablas KaTeX: `\overline{X}` para negados, `\( \)` inline
- Transferencia: `←` / Conexión bus: `=` / Row concatenate: `!`
- Delimitadores: `\( \)` inline — NO `$$`, NO `\[ \]` para bloques AHPL
- NUNCA `\begin{aligned}`, NUNCA `\begin{array}`, NUNCA `$$`
- `COMBUS:` (sin S) — canónico del libro
- Tamaños: `(N)` siempre — en bloques de código, tablas y prosa. Nunca `[N]` para tamaños.
- Valores: DR(18), CR(8), IOBUS(18), CHAR(8), AC(18), PC(12), IR(18), MD(18), MA(12)
- Bifurcación: `→` y `->` son equivalentes — ambos aceptados en bloques de código, no corregir

---

## Hallazgos de esta sesión

| # | Hallazgo | Impacto |
|---|---|---|
| 1 | El botón de copiar de NotebookLM stripea corchetes `[]` y su contenido | Workaround permanente: capturar output con puntero, no con botón |
| 2 | NotebookLM SÍ genera tamaños cuando tiene referencia — pero infiere `[1]` o `[2]` sin ella | N16 con tabla de tamaños estándar resuelve esto |
| 3 | El error era del botón, no de la guía ni del prompt | Workaround permanente: capturar output con puntero, no con botón |
| 4 | Prompt con línea de tamaños agregada no resolvió el problema solo | La guía (N16) es la pieza que faltaba |
| 5 | Gemini tiene acceso a las mismas fuentes del notebook | Comportamiento equivalente a NotebookLM — se puede usar indistintamente para tests |
| 6 | `->` es equivalente a `→` en bloques de código | Sin impacto — NotebookLM entiende ambas formas sin error |
| 7 | Notación `(N)` global resuelve el conflicto con NotebookLM | Output verificado: AC(8), DR(18), IOBUS(18) correctos en tabla y en código |

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-28 | Formato final: bloque de código AHPL + tabla KaTeX inline | KaTeX puro no renderizó de forma confiable; bloque de código sí funcionó |
| 2026-08-28 | Delimitadores: `\( \)` inline — NO `$$` | `$$` rompió renderizado en versiones anteriores de NotebookLM |
| 2026-08-29 | Tests con todo cargado — no quitar guía ni prompt | El comportamiento con todo presente es el que importa para el usuario final |
| 2026-08-29 | Workaround botón: capturar output con puntero, no con botón de copiar | El botón stripea `[]` — bug confirmado empíricamente, sin fix disponible |
| 2026-08-29 | Notación `(N)` global — en bloques de código, tablas y prosa | NotebookLM stripea `[]` — `(N)` evita el conflicto en todos los contextos |
| 2026-08-29 | `->` y `→` son equivalentes — ambos aceptados | NotebookLM entiende ambas formas sin error — no corregir |
| 2026-08-29 | Siguiente mejora: Par 5 en N16 con ejercicio real de la cátedra | Refuerza imitación con material concreto del curso |

> [!note]- Descartadas
> - Generar N16 sin verificar contra NotebookLM — descartado; los pares deben reflejar outputs reales corregidos
> - Mantener `[N]` en bloques de código — descartado; NotebookLM stripea `[]` en todos los contextos
> - Cambio inmediato de delimitadores `\[ \]` → `$$` — postergado; plugin disponible si hace falta

---

## Planificación

N1–N16 completas y verificadas. El próximo paso es agregar Par 5 a N16 con un ejercicio real de la cátedra para reforzar la imitación del modelo.

---

## Flujo de pasos

### ✅ Fase 1 — obtener y analizar outputs (completada)
- Snippets H y G ejecutados x2
- Errores documentados: sin tamaños, tamaños incorrectos, bug del botón
- N16 redactada con pares corregidos

### ✅ Fase 2 — escribir N16 en la guía (completada)
- Posición de inserción confirmada
- N16 escrita con `edit_file`
- Verificación OK

### ✅ Fase 3 — corregir notación (completada)
- Notación `(N)` global aplicada en guía y prompt
- Output verificado — tamaños correctos

### ⬜ Fase 4 — reforzar N16 con Par 5
1. Obtener ejercicio real de la cátedra
2. Redactar Par 5 en `Rubbish\section.md`
3. Insertar en N16 después de Par 4, antes de `%%`
4. Re-subir guía y verificar

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
- [x] Re-subir guía a NotebookLM
- [x] Agregar tabla de notación de registros al prompt
- [x] Agregar tabla de tamaños estándar SIC al prompt
- [x] OCR a `2-4-5-6.pdf` y cargar en NotebookLM
- [x] OCR a `7.pdf` → cargar en NotebookLM
- [x] OCR a `9-10-11-13.pdf` → cargar en NotebookLM
- [x] Verificar si tamaños en tabla de declaraciones se corrigen (no — bug del botón confirmado)
- [x] Documentar bug `[N]` en `notebooklm_solve.md`
- [x] Cambiar notación `[N]` → `(N)` en tablas de declaraciones del prompt (`promtpx.md`)
- [x] Cambiar notación `[N]` → `(N)` en tablas de N16 de la guía (`ETN825_AHPL.md`)
- [x] Cargar prompt actualizado en NotebookLM — resultado mejorado confirmado
- [x] Corregir guía: N1, N2, N3 — `(N)` global en prosa y bloques de código
- [x] Corregir guía: N10 — checklist actualizado a `(N)`
- [x] Corregir guía: N16 tablas de pasos — `(N)` en KaTeX inline
- [x] Aplicar `(N)` global en bloques de código de N11, N16 Par 1 y Par 2
- [x] Actualizar regla en N1: `(N)` siempre, en todos los contextos
- [x] Actualizar prompt `promtpx.md`: tabla Notación unificada a `REG(N)`
- [x] Verificar output NotebookLM — tamaños correctos confirmados
- [ ] Crear Par 5 en N16 — ejercicio real de la cátedra como ejemplo de imitación
- [ ] Re-subir guía actualizada a NotebookLM
- [ ] Re-prueba final — snippets H y G con puntero
- [ ] Cerrar ship (status: delivered)

---

## Preguntas abiertas

- ¿Ejercicio real de la cátedra disponible para Par 5? — traer en la próxima sesión

---

## Recursos

- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal
- `E:\University_vault_2026\Rubbish\section.md` — scratchpad
- `E:\University_vault_2026\notebooklm_question.md` — snippets de prueba H y G
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt activo
- `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_ejemplos 1.md` — historia completa de correcciones v1/v2/v3
- Hill & Peterson — Digital Systems 2ª ed. — p. 105 (operador `*`) y p. 349-350 (PRINTER INTERFACE)
