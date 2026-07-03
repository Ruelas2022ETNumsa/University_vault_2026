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
date_updated: 2026-06-25
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

**Prompt de NotebookLM — tabla de fuentes por tema:**
```
── PROGRAMA Y LIBROS POR TEMA ──
Priorizá estos libros según el tema consultado. Para ejercicios,
siempre Schaum's, Maron y Demidovich son válidos en cualquier tema.
El Stewart 7ma en español actúa como puente lingüístico — usarlo
para confirmar terminología en español o cuando se prefiera
explicación en ese idioma.

── MAPA DE ARCHIVOS ──
Apostol Vol.1 2ed     → 1to7 | 8to16
Thomas 14th ed        → 1to6 | 7to12 | 13to17
Stewart 7ma español   → 1to4 | 5to8  | 9to11
Stewart 9na ET        → archivo único
Piskunov Vol.1        → archivo único
Schaum's 3000         → archivo único
Maron                 → archivo único
Demidovich            → archivo único

── LIBROS POR TEMA ──
| Tema                        | Parcial | Primera fuente          | Segunda fuente       | Respaldo español      |
|-----------------------------|---------|-------------------------|----------------------|-----------------------|
| Funciones reales            | 1P      | Stewart 9na             | Thomas (1to6)        | Stewart 7ma (1to4)    |
| Límites y continuidad       | 1P      | Stewart 9na             | Apostol (1to7)       | Stewart 7ma (1to4)    |
| Derivación                  | 2P      | Stewart 9na             | Piskunov             | Stewart 7ma (1to4)    |
| Aplicaciones de derivación  | 2P      | Thomas (1to6)           | Stewart 9na          | Stewart 7ma (5to8)    |
| Integración                 | 3P      | Stewart 9na             | Piskunov             | Stewart 7ma (5to8)    |
| Aplicaciones de integración | 3P      | Thomas (7to12)          | Stewart 9na          | Stewart 7ma (5to8)    |
| Series reales               | extra   | Apostol (8to16)         | Piskunov             | Stewart 7ma (9to11)   |

Apostol como primera fuente solo cuando el usuario pida rigor
formal o demostración. Para series, Apostol es siempre primera
opción.

── NOTA SOBRE ARCHIVOS DIVIDIDOS ──
Cuando un libro está dividido en partes, consultá el rango
correspondiente al tema. Si el tema cae entre dos rangos,
consultá ambos archivos.
```

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
galaxy-links
[[_claude-boot]]
[[_notebooklm-system]]
[[_ToDo-system]]
%%
