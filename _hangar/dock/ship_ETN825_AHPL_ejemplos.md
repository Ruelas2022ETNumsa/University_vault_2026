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
**Retomar desde:** `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — después de N16 (si hay más imágenes) o prueba en NotebookLM
**Completado esta sesión:** diagnóstico, investigación web, ship, revisión de 3 imágenes (2 variantes de PRINTER INTERFACE descartadas), N16 CONTROLADOR DE MÁQUINAS-HERRAMIENTA agregado
**Próximo paso:** re-prueba en NotebookLM con prompt corregido
**Preguntas de cierre:** —

---

## Resumen y objetivo

Agregar una sección de ejemplos de pares pregunta→respuesta a la guía `ETN825_AHPL.md` para que NotebookLM genere código AHPL en KaTeX y no en texto plano. El problema es que NotebookLM entiende la notación pero no la produce en el formato correcto sin ejemplos concretos de imitación.

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
- [ ] Re-prueba en NotebookLM
- [ ] (Si falla) conversión de delimitadores + corrección

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
