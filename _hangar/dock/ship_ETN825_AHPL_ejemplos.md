---
galaxy_body: ship
project: "ETN825 AHPL — Ejemplos para forzar output LaTeX en NotebookLM"
date: 2026-08-28
status: docked
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-28
**Retomar desde:** resultado estable — probar con negados `~` y evaluar output
**Completado esta sesión:** diagnóstico x2, investigación web x2, ship, imágenes revisadas, N16 agregado, prompt corregido (KaTeX + sin bloques), prompt comprimido (9852 chars), \begin{aligned} eliminado de guía y prompt, \begin{array} eliminado del prompt, revisión completa de prompt y guía — formato final: bloque de código AHPL + tabla con KaTeX inline
**Próximo paso:** cambiar `!` por `~` para negados en prompt y guía, luego re-prueba en NotebookLM
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
- [ ] Cambiar `!` por `~` para negados en prompt y guía
- [ ] Re-prueba en NotebookLM con formato final

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
