---
title: "Library System — Book Search Protocol"
galaxy_body: beacon
scope: vault
audience: [claude]
related_notes:
  - "[[_pdf-system]]"
  - "[[_galaxy-system]]"
tags: [beacon, libros, notebooklm, bibliografía]
date_created: 2026-01-01
date_updated: 2026-05-30
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
| **Complemento opcional** | 1 libro máximo | Solo si existe un hueco real que los anteriores no cubren |

---

### Paso 3 — Formato de presentación de cada libro

Cada libro recomendado debe presentarse así:

```
**Título completo oficial** — Autor(es) completos — Edición recomendada
Idioma original: [idioma]
Rol en el stack: [Teoría principal / Teoría rigurosa / Problemas / Complemento]
Por qué este libro: [2-3 líneas justificando su lugar en el stack]
Edición alternativa aceptable: [si aplica]
Libro alternativo si no se consigue: [título — autor — edición]
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
4. **Siempre dar edición exacta** — título completo, autor(es) completos, número de edición
5. **Siempre dar alternativa** — por cada libro recomendado, indicar qué usar si no se consigue
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
Tema nuevo        → [libro de teoría principal]
No entiendo el fondo → [libro riguroso]
A practicar       → [libro de problemas estándar]
Quiero más reto   → [libro de problemas difíciles]
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
- Calculus: Early Transcendentals, 9th Edition, Metric Version — James Stewart — 9na ed.
- Cálculo — Tom M. Apostol — Vol. 1, 2da ed.
- Differential and Integral Calculus — N. Piskunov — Vol. 1, 2da ed.
- Schaum's 3,000 Solved Problems in Calculus — Elliott Mendelson — 1ra ed.
- Problems in Calculus of One Variable — I.A. Maron — cualquier edición
- A Course of Mathematical Analysis (Problems) — B.P. Demidovich — cualquier edición
- Thomas' Calculus — George B. Thomas, Joel Hass, Christopher Heil, Maurice Weir — 14va ed.

**Referencia rápida (fuera de NotebookLM):**
- Larson Calculus Cheat Sheet

**Descartados y razón:**
- Larson 11va ed. → redundante con Stewart
- Larson Early Transcendental Functions 7va ed. → redundante con Stewart ET
- Edwards & Penney 4ta ed. → redundante con Stewart
- Briggs & Cochran 3ra ed. → redundante con Stewart
- Spivak 4ta ed. → reemplazado por Apostol para ingeniería
- Granville → desactualizado
- Thomas, Finney 9na ed. → reemplazado por Thomas 14va
- Larson Hostetler Edwards "Essential Calculus ETF" → versión reducida, inferior a Stewart
- Bitsadze → física matemática, fuera del scope de Cálculo 1

---

%%
galaxy-links
[[_pdf-system]]
[[_galaxy-system]]
%%
