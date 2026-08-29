---
galaxy_body: ship
project: "ETN825 AHPL — N16: ejemplos pregunta→respuesta para NotebookLM"
date: 2026-08-29
status: docked
fleet: ETN825
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-29
**Retomar desde:** paso 1 del Flujo — leer el estado de `ETN825_AHPL.md` y verificar que N15 sea el último bloque antes de agregar N16
**Completado esta sesión:** diagnóstico completo del estado anterior; planificación de N16; creación de este ship
**Próximo paso:** ejecutar el Flujo de pasos — sección "Fase 1: obtener ejemplos"
**Preguntas de cierre:** —

---

## Resumen y objetivo

La guía `ETN825_AHPL.md` tiene reglas de notación AHPL bien definidas (N1–N15) pero le falta una sección de ejemplos de pares pregunta→respuesta (N16). Sin esos ejemplos, NotebookLM genera `$$\begin{aligned}...\end{aligned}$$` por preentrenamiento aunque la guía lo prohíba. El objetivo es agregar N16 con 3–5 pares concretos que cubran los patrones principales, verificados contra las fuentes reales cargadas en NotebookLM.

---

## Contexto para sesión nueva

> Leer esto si se retoma en una sesión distinta — es suficiente para arrancar sin re-explicar.

**Archivos clave:**
- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal, agregar N16 al final del BLOQUE D (después de N15)
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt de NotebookLM — NO tocar en esta sesión
- `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_ejemplos 1.md` — ship anterior con toda la historia de correcciones (v1/v2/v3) — leer si hay dudas sobre decisiones pasadas

**Estado de la guía al inicio:**
- Guía `ETN825_AHPL.md` — revisada y corregida (v3). N1–N15 consistentes con Hill & Peterson 2ª ed. N16 no existe todavía.
- Prompt `BCv1i` — 9852 chars, bajo el límite de 10000. Formato final: bloque de código AHPL + tabla KaTeX inline.

**Convenciones ya definidas (no renegociar):**
- Bloques de código AHPL: `~` como prefijo para negados
- Tablas KaTeX: `\overline{X}` para negados
- Transferencia: `←` / Conexión bus: `=`
- Row concatenate: `!` / NOT canónico del libro: barra superior
- Delimitadores: `\[ \]` display, `\( \)` inline — NO `$$`
- Bloques AHPL: NUNCA `\begin{aligned}`, NUNCA `\begin{array}`, NUNCA `$$`
- `COMBUS:` (sin S) — canónico del libro
- Formato final de output NotebookLM: bloque de código + tabla con KaTeX inline

**Por qué se necesita N16:**
NotebookLM es RAG sobre Gemini. Para lenguajes de nicho sin representación en corpus públicos (como AHPL), las reglas abstractas no alcanzan — el modelo necesita ejemplos concretos de input/output para imitar el formato correcto. Los pares pregunta→respuesta en el documento fuente son la forma más efectiva de forzar el output deseado.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-28 | Formato final: bloque de código AHPL + tabla KaTeX inline | KaTeX puro (`\[ \]`) no renderizó de forma confiable en NotebookLM; bloque de código sí funcionó |
| 2026-08-28 | Delimitadores: `\[ \]` / `\( \)` — NO `$$` | `$$` rompió renderizado en versiones anteriores de NotebookLM; mantener hasta evidencia contraria |
| 2026-08-29 | Obtener ejemplos para N16 preguntando a NotebookLM/Gemini CON fuentes cargadas | Permite verificar cómo el modelo interpreta las fuentes reales y qué output produce — luego se corrige y ese output corregido se convierte en el ejemplo N16 |
| 2026-08-29 | NO quitar la guía AHPL ni el prompt al consultar | Las fuentes ya están cargadas; quitar guía y prompt haría que el modelo pierda contexto. Se consulta con todo cargado y se evalúa el output tal como lo verá el usuario final |

> [!note]- Descartadas
> - Generar N16 directamente desde krajo sin verificar contra NotebookLM — descartado porque el valor de N16 es mostrar exactamente el output que NotebookLM produce correctamente, no un output ideal inventado
> - Quitar guía AHPL y prompt al consultar — descartado; las fuentes ya están cargadas y el comportamiento con todo presente es el que importa

---

## Planificación

**Enfoque:** obtener los pares pregunta→respuesta interrogando directamente a NotebookLM (con todas las fuentes cargadas, incluyendo guía y prompt), capturar el output, corregirlo si tiene errores, y volcar esos pares corregidos como N16 en la guía.

**Por qué este enfoque:**
- Se verifica cómo el modelo interpreta las fuentes reales — no solo cómo debería interpretarlas
- El output capturado (corregido) sirve como ejemplo de imitación exacta para futuras consultas
- Si el modelo ya produce el formato correcto en algún patrón → ese par entra directo a N16 sin corrección
- Si el modelo falla → se documenta la corrección y el par corregido entra a N16 como ejemplo explícito del formato esperado

**Restricciones:**
- No cambiar convenciones ya definidas (ver Contexto)
- N16 debe ser consistente en estructura con N11–N15
- Los pares deben cubrir los 4 patrones principales (ver Flujo)
- No tocar el prompt `BCv1i` en esta sesión

**Patrones a cubrir en N16:**
1. Módulo completo con declaraciones + secuencia (patrón N11)
2. Bucle de espera con señal (patrón N12)
3. Bifurcación múltiple por bits (patrón N13)
4. Transferencia condicional con `*` y row concatenate `!` (patrón N14)

Opcionalmente, si el usuario trae imágenes de ejercicios del libro → agregar un 5º par basado en ese material real de la cátedra.

---

## Flujo de pasos

### Fase 1: obtener ejemplos desde NotebookLM

1. Abrir NotebookLM con todas las fuentes cargadas (incluyendo `ETN825_AHPL.md` y prompt `BCv1i`)
2. Hacer las siguientes preguntas en orden — una por vez, capturar el output exacto:

**Pregunta A — módulo completo:**
> "Escribí un módulo AHPL completo para una interfaz que espera una señal `start`, carga un registro `DR[8]` desde `IOBUS[8]`, y termina en DEAD END."

**Pregunta B — bucle de espera:**
> "Mostrá el patrón AHPL de un paso que espera mientras `ready = 0` y sale cuando `ready = 1`."

**Pregunta C — bifurcación múltiple:**
> "Escribí una bifurcación AHPL que evalúa `IR[0]` e `IR[1]` y salta a tres destinos distintos según la combinación."

**Pregunta D — transferencia condicional con `*`:**
> "Mostrá la transferencia condicional AHPL donde `A` recibe `B` solo si `a = 0`, y `D` recibe `C` solo si `a = 1`, en el mismo paso."

3. Para cada output recibido: verificar formato (bloque de código + tabla KaTeX) y contenido (operadores, declaraciones, convenciones)
4. Anotar errores detectados — qué generó mal el modelo

### Fase 2: armar N16

5. Para cada par: escribir la pregunta tal como fue hecha + el output correcto (con correcciones aplicadas si las hubo)
6. Redactar la sección N16 con el encabezado consistente con N11–N15:

```
### N16. EJEMPLOS DE PARES PREGUNTA→RESPUESTA

> Contexto para NotebookLM: pares input/output exactos para calibrar el formato de respuesta.
> Para cada par: la pregunta es como la haría un estudiante; la respuesta es exactamente
> el formato esperado — bloque de código AHPL + tabla de lectura con KaTeX inline.
```

7. Escribir N16 en `ETN825_AHPL.md` con `edit_file` — agregar después de N15, antes del bloque `%%`

### Fase 3: verificar

8. Re-subir `ETN825_AHPL.md` actualizada a NotebookLM (reemplazar fuente anterior)
9. Repetir las preguntas A–D y verificar que el output mejoró
10. Si algún patrón sigue fallando → agregar par corregido adicional o reforzar la prohibición en la sección 🤖 NOTEBOOKLM de la guía

---

## Tareas

- [x] Leer todos los archivos del proyecto
- [x] Diagnóstico del estado actual
- [x] Crear este ship
- [ ] Hacer Pregunta A en NotebookLM — capturar output
- [ ] Hacer Pregunta B en NotebookLM — capturar output
- [ ] Hacer Pregunta C en NotebookLM — capturar output
- [ ] Hacer Pregunta D en NotebookLM — capturar output
- [ ] Verificar outputs — anotar errores
- [ ] Redactar N16 con pares corregidos
- [ ] Escribir N16 en `ETN825_AHPL.md` con `edit_file`
- [ ] Re-subir guía a NotebookLM
- [ ] Re-prueba final — verificar mejora de formato
- [ ] Actualizar Handoff y cerrar ship (status: delivered)

---

## Preguntas abiertas

- ¿El usuario trae imágenes de ejercicios del libro para agregar un 5º par basado en material real de la cátedra?
- Si el output de NotebookLM ya es correcto en algún patrón → ¿ese par entra igual a N16 o se omite?

---

## Recursos

- `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` — guía principal (agregar N16 al final de BLOQUE D)
- `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` — prompt activo (no tocar)
- `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_ejemplos 1.md` — ship anterior con historia completa de correcciones
- `E:\University_vault_2026\Untitled.md` — historial de consultas a Gemini (P1–P9) con outputs reales
- Hill & Peterson — Digital Systems 2ª ed. — fuente primaria AHPL (p. 105 cap. 4 sec. 4.7 para operador `*`; p. 349-350 para PRINTER INTERFACE)
- NotebookLM — todas las fuentes de `_library_ETN825.md` cargadas
