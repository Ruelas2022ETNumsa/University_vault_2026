---
title: "Biblioteca ETN1015 — Guía de libros"
galaxy_body: beacon
scope: vault
audience: usuario
related_notes:
  - "[[_config/_library-system]]"
tags: [beacon, library, ETN1015, infraestructura]
date_created: 2026-08-11
date_updated: 2026-08-11
date_last_edit: 2026-08-17 — libro base cambiado a Palani & Kalaiyarasi 2da ed.
status: activo
---

# 📚 Biblioteca ETN1015 — Guía de libros

## Propósito

Este archivo es tu referencia personal para saber qué libro usar en cada tema de ETN1015 — Procesamiento Digital de Señales. El libro base del docente es ahora **Palani & Kalaiyarasi (2da ed.)**, que dicta el orden del curso.

---

> [!info] Libro base actualizado — 2026-08-17
> El docente **cambió el libro base a Palani & Kalaiyarasi**. Palani arranca directo en tiempo discreto y DSP puro (sin señales continuas, Laplace ni filtros analógicos). Rao pasa a rol de referencia de fondo para la parte continua (caps. 1–5 del curso anterior).

---

## Temario oficial

> **Sin temario oficial disponible.** El docente avanza siguiendo el libro base (Rao) capítulo a capítulo. Los temas están inferidos del índice del libro.

### Cap. 1 — Introducción a señales y sistemas
- Definición de señal y sistema
- Operaciones elementales: desplazamiento, escalado, inversión temporal
- Clasificación de señales
- Señales básicas en tiempo continuo
- Ejemplos de señales y sistemas reales

### Cap. 2 — Señales y sistemas en tiempo continuo
- Representación de señales en términos de impulsos
- Sistemas en tiempo continuo y sus propiedades (linealidad, invarianza, causalidad, estabilidad)
- Integral de convolución
- Sistemas descritos por ecuaciones diferenciales
- Funciones singulares
- Representación en espacio de estados de sistemas LTI en tiempo continuo

### Cap. 3 — Análisis en frecuencia de señales y sistemas en tiempo continuo
- Series de Fourier exponencial compleja
- Series de Fourier trigonométrica
- Transformada de Fourier en tiempo continuo
- Respuesta en frecuencia de sistemas en tiempo continuo
- Aplicaciones: modulación AM, SSB, FDM

### Cap. 4 — Transformada de Laplace
- Definición bilateral y unilateral
- Región de convergencia (ROC)
- Transformada inversa de Laplace
- Propiedades de la transformada de Laplace
- Análisis de sistemas LTI en tiempo continuo con Laplace
- Solución de ecuaciones de estado con Laplace

### Cap. 5 — Filtros analógicos
- Filtros ideales
- Diseño de filtros analógicos de paso bajo: Butterworth, Chebyshev, Elíptico, Bessel
- Transformaciones a paso alto, paso banda y rechazo de banda
- Efecto de polos y ceros en la respuesta en frecuencia
- Filtros especializados por ubicación de polos y ceros

### Cap. 6 — Señales y sistemas en tiempo discreto
- Proceso de muestreo de señales analógicas
- Clasificación de señales en tiempo discreto
- Sistemas en tiempo discreto y propiedades
- Sistemas LTI en tiempo discreto: suma de convolución
- Ecuaciones en diferencias
- Representación en espacio de estados de sistemas LTI discretos

### Cap. 7 — Análisis en frecuencia de señales y sistemas en tiempo discreto
- Series de Fourier en tiempo discreto (DTFS)
- Transformada de Fourier en tiempo discreto (DTFT)
- Respuesta en frecuencia de sistemas discretos
- Representación del muestreo en frecuencia
- Reconstrucción de señal banda limitada desde sus muestras

### Cap. 8 — Transformada Z y análisis de sistemas LTI discretos
- Definición de la transformada Z
- Región de convergencia
- Propiedades de la transformada Z
- Transformada Z inversa
- Análisis de sistemas LTI discretos en el dominio Z
- Sistemas de fase mínima, máxima y mixta
- Transformada Z unilateral
- Solución de ecuaciones de estado con Z
- Transformaciones entre sistemas continuos y discretos

---

## Stack completo

| Libro                                                                | Rol                                            | Idioma  |
| -------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| Palani & Kalaiyarasi — Principles of DSP — Springer 2022 (2da ed.)   | Teoría principal — libro base del docente      | Inglés  |
| K. Deergha Rao — Signals and Systems — Birkhäuser 2018               | Referencia de fondo — parte continua (caps. 1–5) | Inglés  |
| Oppenheim, Willsky, Nawab — Signals and Systems — 2da ed. (1to5)     | Teoría rigurosa — caps. 1–5                    | Inglés  |
| Oppenheim, Willsky, Nawab — Signals and Systems — 2da ed. (6to11)    | Teoría rigurosa — caps. 6–11                   | Inglés  |
| Oppenheim & Willsky — Señales y Sistemas — 2da ed. (1to5)            | Puente lingüístico — caps. 1–5                 | Español |
| Oppenheim & Willsky — Señales y Sistemas — 2da ed. (6to11)           | Puente lingüístico — caps. 6–11                | Español |
| Mani, Oppenheim, Willsky, Nawab — Solutions Manual                   | Soluciones oficiales del Oppenheim             | Inglés  |
| Hsu — Schaum's Signals and Systems — 1995                            | Problemas estándar resueltos                    | Inglés  |
| Hayes — Schaum's Digital Signal Processing — 1999                    | Ejercicios DSP — complemento directo de Palani  | Inglés  |
| Phillips, Parr & Riskin — Signals, Systems, and Transforms — 4ta ed. | Transformadas y análisis avanzado              | Inglés  |

---

## Archivos divididos

Algunos libros están divididos en partes. Usá el archivo que corresponde al capítulo:

```
Oppenheim EN (Signals and Systems 2da ed.)  → 1to5  (Caps. 1–5)  | 6to11 (Caps. 6–11)
Oppenheim ES (Señales y Sistemas 2da ed.)   → 1to5  (Caps. 1–5)  | 6to11 (Caps. 6–11)
```

---

## Qué usar por tema

> Sin temario parcializado — organizado por capítulo de **Palani** (nuevo libro base).

| Capítulo Palani | Teoría principal | Teoría rigurosa | Ejercicios | Español |
|---|---|---|---|---|
| Cap. 1 — Discrete Signals and Systems | Palani — Cap. 1 | Oppenheim EN (1to5) — Cap. 5 + (6to11) — Cap. 6 | Hsu Schaum — Cap. 3–4 | Oppenheim ES (1to5) — Cap. 5 + (6to11) — Cap. 6 |
| Cap. 2 — DFT y FFT | Palani — Cap. 2 | Oppenheim EN (6to11) — Cap. 8 | Hayes Schaum DSP — Cap. 5–6 | Oppenheim ES (6to11) — Cap. 8 |
| Cap. 3 — Diseño de filtros IIR | Palani — Cap. 3 | Oppenheim EN (6to11) — Cap. 7 + Phillips — Cap. 8–9 | Hayes Schaum DSP — Cap. 8–9 | Oppenheim ES (6to11) — Cap. 7 |
| Cap. 4 — Diseño de filtros FIR | Palani — Cap. 4 | Oppenheim EN (6to11) — Cap. 7 | Hayes Schaum DSP — Cap. 10–11 | Oppenheim ES (6to11) — Cap. 7 |
| Cap. 5 — Finite Word Length Effects | Palani — Cap. 5 | Oppenheim EN (6to11) — Cap. 6 | Hayes Schaum DSP — Cap. 12 | — |
| Cap. 6 — Multi-rate DSP | Palani — Cap. 6 | — | Hayes Schaum DSP — Cap. 13 | — |

---

## Flujo de uso

```
Tema nuevo del docente              → Palani (seguís el libro base)
No entiendo el fondo / parte continua → Rao (referencia de fondo)
Teoría rigurosa discreta            → Oppenheim 2da ed. (6to11)
Teoría rigurosa continua            → Oppenheim 2da ed. (1to5)
Terminología en español             → Oppenheim versión Pearson Educación
Verificar ejercicios del Oppenheim  → Solutions Manual de Mani
Practicar ejercicios estándar       → Hsu Schaum
Ejercicios DSP (DFT, filtros, FWL)  → Hayes Schaum DSP
Transformadas profundas             → Phillips, Parr & Riskin
```

---

## Libros descartados

| Libro | Razón |
|---|---|
| — | Stack construido desde cero — no hubo descartados |

---

%%
# galaxy-links
[[_app/_config/_library-system.md]]
%%
