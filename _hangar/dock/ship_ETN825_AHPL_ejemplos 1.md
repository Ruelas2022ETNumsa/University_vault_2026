---
galaxy_body: ship
project: "ETN825 AHPL — Ejemplos para forzar output LaTeX en NotebookLM"
date: 2026-08-28
status: delivered
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-29
**Retomar desde:** —
**Completado esta sesión:** re-prueba NotebookLM (formato bloque de código correcto, contenido con errores); análisis de notación con 2 ejemplos del libro; correcciones N1/N2/N4/N11/N12/N15 aplicadas en guía; investigación RETURN() x5 (Gemini x3 + Perplexity + ChatGPT + web) — conclusión: no es primitiva AHPL, es combinational logic unit definida en el ejemplo; guía y prompt revisados — todo consistente
**Próximo paso:** —
**Preguntas de cierre:** —

---

## Resumen y objetivo

Agregar una sección de ejemplos de pares pregunta→respuesta a la guía `ETN825_AHPL.md` para que NotebookLM genere código AHPL en KaTeX y no en texto plano. El problema es que NotebookLM entiende la notación pero no la produce en el formato correcto sin ejemplos concretos de imitación.

## Problema pendiente — inicio próxima sesión

**Síntoma:** NotebookLM sigue generando `$$\begin{aligned}...\end{aligned}$$` por su cuenta aunque la guía y el prompt no lo usan. El modelo lo hace por preentrenamiento — ignora las instrucciones de formato.

**Lo descartado:** el problema no es la guía ni los delimitadores — ambos ya están corregidos. El modelo genera ese formato por defecto cuando produce AHPL.

**Líneas de ataque para la próxima sesión:**
1. Agregar prohibición explícita en el prompt: `NUNCA \begin{aligned}, NUNCA \begin{array}, NUNCA ningún entorno \begin{...}`
2. Agregar en la sección `🤖 NOTEBOOKLM` de la guía la misma prohibición con ejemplo negativo explícito
3. Evaluar si agregar un par pregunta→respuesta en la guía donde se muestre el output correcto (líneas \[ \] independientes) vs el incorrecto ($$\begin{aligned}$$)

**Nota sobre delimitadores:** mantener `\[ \]` y `\( \)` — NO usar `$$`. La web no tiene documentación oficial de Google sobre este punto, pero la experiencia directa del usuario confirma que `$$` rompió el renderizado en versiones anteriores de NotebookLM. Hasta que haya evidencia contraria, `\[ \]` es el delimitador correcto.

**Archivos a revisar:**
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md`
- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — sección 🤖 NOTEBOOKLM

---

## Diagnóstico técnico — problema de renderizado

**Causa raíz identificada:** `\begin{aligned}` genera un bloque multilinea que NotebookLM divide en múltiples nodos del DOM y no renderiza completo. El problema no son los delimitadores `\[ \]` sino el entorno `aligned`.

**Solución:** reemplazar cada bloque `\[ \begin{aligned} ... \end{aligned} \]` por líneas `\[ \]` independientes — una por paso. Así cada línea es un nodo DOM separado que renderiza solo.

**Delimitadores a mantener:** `\[ \]` para display, `\( \)` para inline — NO usar `$$` (falló en versiones anteriores de NotebookLM).

**Ejemplo de conversión:**
```
❌ ANTES:
\[ \begin{aligned}
&\textbf{MODULE: PRINTER INTERFACE} \\
&1.\; ready = 1 \\
\end{aligned} \]

✅ DESPUÉS:
\[\textbf{MODULE: PRINTER INTERFACE}\]
\[1.\; ready = 1\]
```

**Alcance del cambio:**
- Guía `ETN825_AHPL.md` — todas las secciones N1–N16 que usen `\begin{aligned}`
- Prompt `ETN825-comp_indice_BCv1i.md` — FORMATO EJERCICIO RESUELTO
- Prompt: también bajar de 10231 a <10000 chars (faltan ~231 chars menos)

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-28 | No cambiar delimitadores `\[ \]` / `\( \)` por `$$` aún | El usuario tiene plugin que hace la conversión; primero se prueba con ejemplos |
| 2026-08-28 | Agregar sección de pares pregunta→respuesta (N16 o similar) | NotebookLM aprende por imitación — ejemplos de output exacto son más efectivos que reglas abstractas |
| 2026-08-28 | Si los ejemplos no dan resultado → conversión de delimitadores con plugin + corrección | Plan B documentado |

> [!note]- Descartadas
> Cambio inmediato de delimitadores — descartado por ahora, el usuario tiene plugin para hacerlo si los ejemplos no funcionan.

---

## Planificación

NotebookLM es un sistema RAG sobre Gemini — lee los fuentes y genera respuestas condicionadas a ellos. El problema detectado: la guía tiene reglas de notación bien definidas pero no ejemplos del *output exacto* que NotebookLM debe producir. Desmos y TikZ funcionaron porque probablemente el modelo ya tiene patrones de esos lenguajes en preentrenamiento; AHPL es un lenguaje de nicho sin representación en corpus públicos, entonces la guía tiene que hacer todo el trabajo.

**Enfoque:** agregar pares pregunta→respuesta donde la respuesta es exactamente el KaTeX que NotebookLM debería emitir. Los pares vienen de imágenes que el usuario provee (ejercicios resueltos de la materia).

**Restricciones:**
- No cambiar delimitadores existentes en la guía
- Los ejemplos deben cubrir los patrones más frecuentes: módulo completo, bucle de espera, bifurcación, operación condicional con `*`
- Formato de la sección: consistente con N11–N15 ya existentes

---

## Sugerencias

- NotebookLM tiene soporte nativo de LaTeX desde octubre 2025 (Chat, Flashcards, Quizzes)
- El motor nativo reconoce `$$...$$` y `$...$` — el plugin del usuario hace esa conversión si es necesario
- Patrón de prompt engineering efectivo en RAG: incluir ejemplos de pares input/output en el documento fuente es más efectivo que instrucciones abstractas de formato

---

## Flujo de pasos

1. Usuario muestra imágenes de ejercicios resueltos de ETN825
2. krajo extrae los pares pregunta→respuesta en KaTeX
3. Se redacta sección nueva (N16 o subsección de BLOQUE D) con los pares
4. Se escribe en `ETN825_AHPL.md` con `edit_file`
5. Usuario prueba en NotebookLM
6. Si no da → usuario corre el plugin de conversión `\[ \]` → `$$` y muestra resultado a krajo para corrección

---

## Tareas

- [x] Diagnóstico del problema
- [x] Investigación web sobre soporte LaTeX en NotebookLM
- [x] Crear ship
- [x] Recibir imágenes del usuario (3 imágenes revisadas)
- [x] Redactar N16 — CONTROLADOR DE MÁQUINAS-HERRAMIENTA
- [x] Escribir N16 en `ETN825_AHPL.md`
- [ ] Recibir más imágenes del usuario (si las hay)
- [x] Prueba en NotebookLM — falló (entregó bloque de código)
- [x] Diagnóstico: conflicto entre prompt y guía — prompt prohibía KaTeX explícitamente
- [x] Corregir prompt `ETN825-comp_indice_BCv1i.md` — 3 secciones actualizadas a KaTeX
- [x] Comprimir prompt — bajó a 10231 chars (límite 10000, faltan ~231 chars menos)
- [x] Diagnóstico renderizado — causa: \begin{aligned} rompe DOM en NotebookLM
- [x] Reemplazar \begin{aligned} por líneas \[ \] independientes en guía (N1–N16) — 9 bloques
- [x] Reemplazar \begin{aligned} en prompt (FORMATO EJERCICIO RESUELTO)
- [x] Terminar compresión del prompt — 9852 chars (✓ bajo 10000)
- [x] Eliminar \begin{array} del prompt
- [x] Re-prueba en NotebookLM — sigue fallando: modelo genera $$\begin{aligned}$$ por preentrenamiento
- [x] Revisión completa del enfoque — descartado KaTeX para bloques AHPL ($$ / \( \) / \[ \] no renderizaron de forma confiable)
- [x] Formato final definido: bloque de código para AHPL + tabla con KaTeX inline para operadores
- [x] Prompt `BCv1i` actualizado al formato final
- [x] Guía `ETN825_AHPL.md` actualizada — tabla N11 con KaTeX inline
- [x] Investigación operadores AHPL — P1/P2/P3 consultados a ChatGPT + Gemini/NotebookLM
- [x] Corregir guía `ETN825_AHPL.md` — 6 inconsistencias adicionales identificadas en revisión (ver ## Correcciones pendientes v2) — todas aplicadas
- [x] Corregir guía `ETN825_AHPL.md` — `COMBUSES` → `COMBUS` en 6 ocurrencias (🤖 NOTEBOOKLM, N1, N2, N3, N10) — confirmado por Gemini P8 — aplicado
- [x] Re-prueba en NotebookLM con formato final — parcialmente exitoso (formato bloque de código correcto, sin \begin{aligned}; contenido con errores)
- [x] Corrección guía N1/N2 — reforzar que vectores SIEMPRE llevan tamaño entre corchetes (NotebookLM omitió tamaños: `DR` en lugar de `DR[18]`, etc.) — aplicado en buffer
- [x] Corrección guía N2/N3 — agregar nota: declaraciones con dos dimensiones son válidas, ej. `ROM[1024, 18]` — aplicado en buffer
- [x] Corrección guía N12 — aclarar sentido del bucle: espera mientras señal=0, sale cuando señal=1; ejemplo con `~señal` explícito — aplicado en buffer
- [x] Corrección guía N15 — agregar patrón con `*` fuera de secuencia: `ss * (start ∨ stop) ← (1!0) * (start, stop)` — aplicado en buffer
- [x] Verificar y eliminar cualquier mención de `busy` en N11 (módulo PRINTER INTERFACE) — no había `busy`, N11 limpio
- [x] Corregir N11 — paso 7: destino incorrecto `(3, 8)` → debe ser `(3, 1)` en bloque de código y tabla — aplicado en buffer
- [x] Corrección guía N4 — clarificar `RETURN()`: investigación x4 (Gemini x3 + Perplexity + ChatGPT + web) — conclusión: no es operador estándar AHPL, es combinational logic unit definida en el ejemplo (detector booleano). `BUSFN` agregado como operador formal. Aplicado en guía.

---

## Correcciones pendientes — ETN825_AHPL.md

Basadas en investigación P1/P2 (ChatGPT + Gemini, 2026-08-28). Fuente: Hill & Peterson 2ª ed. p. 112, 128-129.

**Sobre el operador `!` (row concatenate):**
- `!` NO es complemento de bits — es ROW CONCATENATE (encadenamiento de filas/vectores)
- La concatenación de vectores simples usa coma: `X, Y`
- El `!` construye una matriz/vector compuesto: `(A ! B)` = filas de A sobre filas de B

**Sobre el NOT en texto plano:**
- La notación canónica del libro es barra superior: `overline{X}`
- En texto plano / bloques de código AHPL: `~` es sustitución tipográfica aceptada, no notación original
- En tablas KaTeX: `\overline{X}` es la forma correcta

**Sobre el paso 3A del módulo PRINTER INTERFACE (P3):**
- Fuente: ChatGPT con foto del libro, p. 349, Example 9.3 (cap. 9)
- Fuente: Gemini/NotebookLM, p. 350
- El paso 3A real del libro es:
  `CR ← (DR₁₀:₁₇ ∧ first) ∨ (DR₁:₈ ∧ ~first)`
- NO usa operador `*` ni `!` — usa AND/OR lógico directamente
- Lo que tenía la guía (`CR ← (D₁₀:₁₇!) * (first, ~first)`) es incorrecto en estructura y operadores

**Sobre el operador `*` (transferencia condicional) — P4:**
- Fuente: Gemini (todas las fuentes cargadas), p. 105 cap. 4 sec. 4.7 + ChatGPT
- El `*` SÍ existe en AHPL pero es distinto de `∧` — son operadores diferentes
- Formas válidas según el libro:
  - `DV ← OCLV * F` — transferencia condicionada por F
  - `DM * F ← OCLV` — destino condicionado por F
  - `D ← (A ! B ! C) * (f, g, h)` — selección condicional del origen con row concatenate
  - `A * ~a ← B ; D * a ← C` — dos transferencias condicionales simultáneas (p. 105)
- El paso 3A del PRINTER INTERFACE usa `∧`/`∨`, NO `*` — son mecanismos distintos
- N14 debe mostrar un ejemplo real con `*` tomado de p. 105, no del paso 3A

**Decisión de convención de notación — 2026-08-28:**
- **Bloques de código AHPL:** `~` como prefijo para negados (sustitución tipográfica aceptada — Opción A)
- **Tablas KaTeX:** `\overline{X}` para negados, notación matemática completa (Opción C)
- **Concatenación de vectores simples:** coma — `X, Y`
- **Row concatenate:** `!` — `A ! B`
- **NOT canónico del libro:** barra superior tipográfica — se mantiene en tablas KaTeX, se sustituye por `~` en bloques de código
- Esta convención aplica a toda la guía y al prompt

**Módulo PRINTER INTERFACE completo — P5 (fuente: ChatGPT, Example 9.3 p. 349-350):**
```
MODULE: PRINTER INTERFACE
MEMORY: DR[18]; CR[8]; first(JK)
OUTPUTS: CHAR[8]; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS[18]
1. ready = 1
   → (~datavalid)/(1)
2. DR ← IOBUS; accept = 1; first ← 1
3. CR ← (DR₁₀:₁₇ ∧ first) ∨ (DR₁:₈ ∧ ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. → (wait)/(6)
7. first ← 0
   → (first, ~first)/(3, 8)
8. DEAD END
END SEQUENCE
CHAR = CR
END
```

**Paso 1 del PRINTER INTERFACE — P6:**
- `1. → (csrdy ∧ ~CSBUS₀ ∧ CSBUS₁ ∧ ~CSBUS₂)/(1)`
- El libro usa barra superior tipográfica para negados, NO `~`
- El AND se representa con `∧`

**Notación de negado en bloques de código — P7:**
- El libro usa EXCLUSIVAMENTE barra superior en las secuencias numeradas
- NUNCA usa `~` ni `NOT()` en el código AHPL
- Ejemplos confirmados:
  - p. 98: `→ ((Ā₀ ∨ ...), (Ā₀ ∨ ...))/(5,1)` — barra sobre cada término
  - p. 177: `MD ← (AC ! (5T0, INC(PC))) * (IR₂, ~IR₂)` — barra sobre IR₂

**Puntos a corregir en la guía:**
1. **N4 — tabla "Selección de bits"** — fila `REG_{i:j}!` dice "complementados" → incorrecto, es row concatenate
2. **N4 — tabla "Transferencia y conexión"** — ejemplo `(D_{10:17}!) * (first, overline{first})` — estructura incorrecta, no es así en el libro
3. **N7 — bloque código paso 3A** — `CR ← (D₁₀:₁₇!) * (first, ~first)` → debe ser `CR ← (DR₁₀:₁₇ ∧ first) ∨ (DR₁:₈ ∧ ~first)`
4. **N11 — bloque código paso 3A** — ídem N7
5. **N14 — bloque código y nota al pie** — reescribir con ejemplos reales de p. 105: `A * ~a ← B` y `D ← (A ! B ! C) * (f, g, h)`. Eliminar descripción "complemento lógico bit a bit"

---

## Correcciones pendientes v2 — ETN825_AHPL.md

Identificadas en revisión post-corrección (sesión 2026-08-28). Fuente: análisis de consistencia interna de la guía.

| # | Sección | Problema | Acción | Estado |
|---|---|---|---|---|
| 1 | N3 — ejemplo declaraciones | Usa módulo viejo (`csrdy`, `CSBUS[12]`, `ready`, `datavalid`, `accept` en COMBUSES) — desincronizado con módulo P5 | Actualizar ejemplo al módulo P5 | ✅ aplicado |
| 2 | N6 — ejemplo operaciones simultáneas | Usa `2A. DR ← IOBUS; busy ← 1; accept = 1; first ← 1` — subpaso y `busy` ya no existen en P5 | Actualizar a `2. DR ← IOBUS; accept = 1; first ← 1` | ✅ aplicado |
| 3 | N7 — ejemplo etiquetas | Muestra módulo viejo con subpasos (`1A`, `2A`, `3A`) y `CSBUS` — P5 no tiene subpasos | Reemplazar ejemplo por uno representativo del P5 o patrón genérico | ✅ aplicado |
| 4 | N9 — nota al pie convención `~` | Dice "en texto plano se indica con subíndice negado o `NOT(...)`" — contradice convención `~` establecida | Corregir nota según convención definida | ✅ aplicado |
| 5 | N1 — estructura genérica | Dice `COMBUSES:` pero P5 usa `COMBUS:` (sin S) — confirmar forma canónica del libro | Preguntar a Gemini antes de editar | ✅ confirmado — `COMBUSES` es correcto, no requiere cambio |
| 6 | N12 — ejemplos bucle | Usa `readȳ` y `6A. → (wait)/(6A)` con subpaso — P5 tiene `6. → (wait)/(6)` sin subpaso | Actualizar ejemplos al módulo P5 | ✅ aplicado |

---

## Correcciones pendientes v3 — ETN825_AHPL.md

Identificadas en revisión final (sesión 2026-08-28). Fuente: confirmación Gemini P8 — `COMBUS:` es la forma canónica del libro (Hill & Peterson 2ª ed., p. 350). `COMBUSES:` es variante de apuntes/resúmenes.

| # | Sección | Cambio |
|---|---|---|
| 1 | 🤖 NOTEBOOKLM — Defaults | `COMBUSES` → `COMBUS` |
| 2 | N1 — bloque estructura + explicación | `COMBUSES:` → `COMBUS:` |
| 3 | N2 — encabezado tabla Buses + nota al pie | `(COMBUSES)` → `(COMBUS)` |
| 4 | N3 — tabla, fila COMBUSES | `COMBUSES` → `COMBUS` |
| 5 | N10 — checklist | `COMBUSES:` → `COMBUS:` |

---

## Preguntas abiertas

- ¿Cuántos pares de ejemplos son suficientes? (estimado: 3–5 cubriendo los patrones principales)
- ¿Los ejemplos deben mostrar también el output renderizado visualmente o solo el código KaTeX crudo?

---

## Recursos

- Guía principal: `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md`
- Referencia: Hill & Peterson — Digital Systems 2ª ed.
- NotebookLM LaTeX nativo: octubre 2025 (Chat, Flashcards, Quizzes)
- Plugin de conversión de delimitadores: disponible en el entorno del usuario
- Consultas a Gemini+NotebookLM (P1–P7 + sesión actual): `E:\University_vault_2026\Untitled.md`
