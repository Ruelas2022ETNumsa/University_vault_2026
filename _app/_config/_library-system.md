---
title: "Library System — Protocolo de búsqueda y selección de libros"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_claude-boot]]"
  - "[[_notebooklm-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, library, infraestructura]
date_created: 2026-06-25
date_updated: 2026-08-08
status: activo
---

# 📚 LIBRARY SYSTEM — Book Search Protocol

## Propósito
Este archivo define el protocolo de búsqueda y selección de libros para cualquier materia universitaria. Al leer este archivo, el asistente debe seguir exactamente este sistema para ayudar al usuario a construir un stack de libros óptimo.

---

## ⚙️ Protocolo de trabajo

### Paso 1 — Input requerido del usuario
Antes de recomendar cualquier libro, el asistente debe tener:

1. **Temario completo** — dividido por parciales o unidades, con todos los temas listados
2. **Nivel de la materia** — ingeniería / ciencias / licenciatura / posgrado
3. **Lista previa** — si el usuario ya tiene libros en mente, listarlos para evaluarlos

Si alguno de estos tres puntos falta, pedirlo antes de continuar.

---

### Paso 2 — Construcción del stack

El stack final debe cubrir exactamente estos tres roles. No más, no menos:

| Rol | Cantidad ideal | Descripción |
|---|---|---|
| **Teoría + Ejemplos** | 1 libro principal + 1 riguroso | Cubre todo el temario con explicaciones y ejemplos resueltos |
| **Problemas resueltos** | 1-2 libros | Solo ejercicios con soluciones paso a paso, sin teoría necesariamente |
| **Puente lingüístico** | 1 libro (opcional) | Versión en español del libro principal — mismo contenido, terminología en español para NLM. Puede ser traducción oficial o libro de autor hispanohablante de nivel equivalente |
| **Complemento opcional** | 1 libro máximo | Solo si existe un hueco real que los anteriores no cubren |

---

### Paso 3 — Formato de presentación de cada libro

Cada libro recomendado debe presentarse así:

```
**Título completo oficial** — Autor(es) completos — Editorial — Edición recomendada
Idioma original: [idioma]
Rol en el stack: [Teoría principal / Teoría rigurosa / Problemas / Puente lingüístico / Complemento]
Por qué este libro: [2-3 líneas justificando su lugar en el stack]
Edición alternativa aceptable: [si aplica]
Libro alternativo (opción 1) si no se consigue: [título — autor — editorial — edición]
Libro alternativo (opción 2) si tampoco se consigue: [título — autor — editorial — edición]
Puente lingüístico sugerido: [título en español — autor — editorial — edición] (si aplica)
```

---

### Paso 4 — Evaluación de libros existentes

Cuando el usuario presente libros que ya consiguió, evaluarlos con este criterio:

- ✅ **Visto bueno** — el libro cumple su rol, quédatelo
- ⚠️ **Condicionado** — sirve pero con limitaciones, explicar cuáles
- ❌ **Descartado** — redundante o inferior, explicar por qué y qué lo reemplaza

Siempre explicar la razón. Nunca descartar sin justificación.

---

### Paso 5 — Reglas del stack

1. **Sin redundancia** — si dos libros cubren lo mismo, quedarse con el mejor y descartar el otro
2. **Sin acumulación innecesaria** — más libros no es mejor aprendizaje
3. **El idioma no importa** — el usuario trabaja con NotebookLM, que procesa cualquier idioma
4. **Siempre dar edición exacta** — título completo, autor(es) completos, editorial, número de edición
5. **Siempre dar dos alternativas** — por cada libro recomendado, indicar opción 1 y opción 2 si no se consigue
5b. **Siempre sugerir puente lingüístico** — buscar versión en español del libro principal (traducción oficial, editorial Reverté, Pearson Educación, etc.) o libro equivalente de autor hispanohablante
6. **Priorizar libros con teoría Y ejemplos** — el libro principal nunca debe ser solo teoría o solo problemas
7. **Los libros soviéticos son válidos** — editorial Mir, Piskunov, Demidovich, Maron, etc. son de alta calidad para ingeniería

---

### Paso 6 — Stack final

Presentar siempre una tabla resumen al final:

```
STACK FINAL — [Nombre de la materia]

Teoría principal   → [Libro]
Teoría rigurosa    → [Libro]
Problemas estándar → [Libro]
Problemas difíciles→ [Libro] (si aplica)
Complemento        → [Libro] (solo si hay hueco real)
```

Y un flujo de uso:

```
Tema nuevo           → [libro de teoría principal]
No entiendo el fondo → [libro riguroso]
A practicar          → [libro de problemas estándar]
Quiero más reto      → [libro de problemas difíciles]
```

---

## 📋 Template de conversación

Cuando el usuario inicie una búsqueda de libros, usar este orden:

1. Confirmar que se tiene temario + nivel + lista previa
2. Evaluar lista previa si existe (✅ / ⚠️ / ❌)
3. Identificar huecos en la lista previa
4. Recomendar libros para llenar huecos
5. Presentar stack final consolidado
6. Evaluar libros adicionales que el usuario consiga posteriormente

---

## 🗂️ Historial de stacks construidos

### Cálculo 1 — Ingeniería (2026)

**Stack NotebookLM:**

| Archivo en disco | Rol |
|---|---|
| Stewart, James - Calculus Early Transcendentals 9th Ed Metric (único archivo) | Teoría principal (inglés) |
| Stewart, James 7ed-Cálculo en una variable. Trascendentes tempranas-1to4 | Puente lingüístico español (temas 1-4) |
| Stewart, James 7ed-Cálculo en una variable. Trascendentes tempranas-5to8 | Puente lingüístico español (temas 5-8) |
| Stewart, James 7ed-Cálculo en una variable. Trascendentes tempranas-9to11 | Puente lingüístico español (temas 9-11) |
| Apostol-Calculus Vol.1 2ed-1to7 | Teoría rigurosa (temas 1-7) |
| Apostol-Calculus Vol.1 2ed-8to16 | Teoría rigurosa (temas 8-16) |
| Thomas 14th ed-Calculus-1to6 | Segunda opinión (temas 1-6) |
| Thomas 14th ed-Calculus-7to12 | Segunda opinión (temas 7-12) |
| Thomas 14th ed-Calculus-13to17 | Reservado para Cálculo 2/3 |
| Piskunov-Differential and Integral Calculus Vol.1 2ed | Teoría rigurosa soviética |
| Mendelson-Schaum's 3000 Solved Problems in Calculus 1ed | Problemas estándar |
| Maron-Problems in Calculus of One Variable | Problemas difíciles |
| Demidovich-Problems in Mathematical Analysis | Problemas desafiantes / series |

**Referencia rápida (fuera de NotebookLM):**
- Larson Calculus Cheat Sheet

**Mapa de archivos divididos:**
```
Apostol Vol.1 2ed   → 1to7  | 8to16
Thomas 14th ed      → 1to6  | 7to12 | 13to17
Stewart 7ma español → 1to4  | 5to8  | 9to11
```

**Prompts de NotebookLM:**
- Transcripción de apuntes → `[[prompts/MAT101/MAT101-transcription]]`
- Estudio y consulta → `[[prompts/MAT101/MAT101-study]]`

**Libros por tema (actualizado):** ver `[[_config/_library_MAT101]]`

**Guía de fuentes del notebook:** ver `[[guides/MAT101/MAT101_library]]`

**Descartados y razón:**
- Larson 11va ed. → redundante con Stewart
- Larson Early Transcendental Functions 7va ed. → redundante con Stewart ET
- Larson Hostetler Edwards "Essential Calculus ETF" → versión reducida, inferior a Stewart
- Edwards & Penney 4ta ed. → redundante con Stewart
- Briggs & Cochran 3ra ed. → redundante con Stewart
- Spivak 4ta ed. → reemplazado por Apostol para ingeniería
- Granville → desactualizado
- Thomas, Finney 9na ed. → reemplazado por Thomas 14va
- Bitsadze → física matemática, fuera del scope de Cálculo 1
- Thomas 14va (13to17) → temas de Cálculo 2/3, reservado para esas materias

---

%%
# galaxy-links
[[_claude-boot]]
[[_app/_config/_notebooklm-system.md]]
[[_app/_config/_ToDo-system.md]]
[[Semesters/template/tpl-w-library.md]]
%%
