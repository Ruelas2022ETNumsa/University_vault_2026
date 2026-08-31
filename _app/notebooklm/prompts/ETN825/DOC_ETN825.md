# Resumen de sesión — ETN825 AHPL (guía + prompt)
> Leer esto al inicio de una sesión nueva para retomar sin re-explicar.
> Última actualización: 2026-08-31

---

## Archivos clave

| Archivo | Rol |
|---|---|
| `E:\University_vault_2026\_app\notebooklm\guides\ETN825\ETN825_AHPL.md` | Guía principal — subir a NotebookLM |
| `E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-comp_indice_BCv1i.md` | Prompt activo de configuración (también en `Rubbish\promtpx.md` como borrador editable) |
| `E:\University_vault_2026\Rubbish\section.md` | Scratchpad para borradores de correcciones |
| `E:\University_vault_2026\notebooklm_question.md` | Snippets de prueba A–H |
| `E:\University_vault_2026\_hangar\dock\ship_ETN825_AHPL_N16.md` | Ship del proyecto (status: delivered) |

---

## Estado actual

- Guía `ETN825_AHPL.md` — **completa y verificada** — N1–N16 corregidas, subida a NotebookLM.
- Prompt — **activo y consistente** con la guía.
- Snippets A–H probados — outputs correctos en formato, notación y tamaños.
- Ship cerrado — `status: delivered`.

**Pendiente para próxima sesión:**
- Par 5 en N16 — ejercicio real de la cátedra (el usuario debe traerlo).

---

## Convenciones — no renegociar

| Regla | Valor |
|---|---|
| Tamaños de vectores | `(N)` siempre — nunca `[N]` |
| Negados en bloques de código | `~` como prefijo — nunca barra superior ni `NOT()` |
| Negados en tablas KaTeX | `\overline{X}` |
| AND en bloques de código | `/\` — nunca `&` |
| OR en bloques de código | `\/` — nunca `\|` ni `+` |
| Delimitadores KaTeX | `\( \)` inline — nunca `$$`, nunca `\[ \]` para AHPL |
| Bloques AHPL | bloque de código estándar — nunca `\begin{...}` |
| Transferencia | `←` o `<-` |
| Conexión bus | `=` |
| Row concatenate | `!` |
| Rangos de bits | `DR(10:17)` — nunca `DR[10:17]` ni `DR₁₀:₁₇` |
| Bifurcación | `→` y `->` equivalentes — ambos aceptados |
| Declaración buses | `COMBUS:` (sin S) |

**Tamaños estándar del SIC:**
`DR(18)` · `IR(18)` · `MD(18)` · `AC(18)` · `IOBUS(18)` · `PC(12)` · `MA(12)` · `CR(8)` · `CHAR(8)`

---

## Estructura de la guía ETN825_AHPL.md

| Sección | Contenido |
|---|---|
| **SECCIÓN NOTEBOOKLM** | Defaults y reglas base para el modelo |
| **N1** | Estructura obligatoria de un módulo AHPL |
| **N2** | Declaración de registros y buses |
| **N3** | Entradas y salidas |
| **N4** | Operadores — transferencia, lógicos, selección de bits, aritméticos |
| **N5** | Tipos de paso — operación, bifurcación, nulo, fin de secuencia |
| **N6** | Operaciones simultáneas en un paso |
| **N7** | Etiquetas de paso y subpaso |
| **N8** | Expresiones combinacionales fuera de secuencia |
| **N9** | Condición compuesta y señales negadas |
| **N10** | Checklist antes de entregar un módulo |
| **N11** | Módulo completo — PRINTER INTERFACE (Example 9.3, p. 349-350) |
| **N12** | Patrón — bucle de espera con señal |
| **N13** | Patrón — bifurcación múltiple (incluye bifurcación paralela) |
| **N14** | Patrón — transferencia condicional con operador `*` |
| **N15** | Patrón — salida combinacional permanente |
| **N16** | Pares pregunta→respuesta para imitación (4 pares + tabla de tamaños) |

---

## Estructura del prompt

El prompt (`promtpx.md`) tiene dos bloques:

**Bloque 1 — FORMATO AHPL (va al inicio del prompt):**
- Reglas de notación para bloques de código
- Tabla de registros MEMORY con ejemplos
- Tabla de tamaños estándar del SIC

**Bloque 2 — TAREA Y COMPORTAMIENTO:**
- 4 tipos de mensaje con su flujo
- Formato de ejercicio resuelto (tabla declaraciones → bloque código → tabla pasos)
- Selección de fuentes y jerarquía
- Niveles de complemento B y C
- Formato de respuesta con figura (CASO A libro / CASO B TikZJax)
- Reglas generales y de citado
- Lista de libros y complementos disponibles
- Teoría por tema (T1, T2, T3)

---

## Workarounds conocidos

| Problema | Solución |
|---|---|
| Botón copiar de NotebookLM stripea `[]` y su contenido | Capturar output con puntero — nunca con el botón |
| KaTeX serializa con `$` al copiar con puntero | No es error — es comportamiento interno de NotebookLM, no corregir |
| Gemini puede fabricar citas con páginas inventadas | Verificar contra el libro antes de incorporar cualquier cita específica |
| `first(JK)` — modelo suele omitir `(JK)` | Menor — no afecta el comportamiento del módulo; corregir si se transcribe para examen |
