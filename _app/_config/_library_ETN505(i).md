---
title: "Biblioteca ETN505 — Guía de libros"
galaxy_body: beacon
scope: vault
audience: usuario
related_notes:
  - "[[_config/_library-system]]"
  - "[[guides/ETN505/ETN505_library]]"
tags: [beacon, library, ETN505, infraestructura]
date_created: 2026-07-09
date_updated: 2026-07-09
status: desarollo
---

# 📚 Biblioteca ETN505 — Guía de libros

## Propósito

Este archivo es tu referencia personal para saber qué libro usar en cada tema de ETN505. Para el detalle completo de capítulos y páginas, consultá `[[guides/ETN505/ETN505_library]]`.

---

## Temario oficial

### T1 — INTRODUCCIÓN
- Métodos analíticos métodos numéricos 
- Algoritmos y estabilidad 
- Teoría de errores 
- Aplicaciones de los métodos numéricos en ingeniería electrónica 
- Ejercicios 

### T2 — SOLUCIÓN DE ECUACIONES NO LINEALES
- Búsqueda de valores iniciales teorema de Bolzano 
- Método de punto fijo 
	- Algoritmo Método de punto fijo 
- Método de Newton-Raphson 
	- Algoritmo Método de Newton-Raphson 
- Método de la secante 
	- Algoritmo Método de la secante 
- Método de posición falsa 
	- Algoritmo Método de posición falsa 
- Método de la bisección 
- Ejercicios 

### T3 — SISTEMAS DE ECUACIONES LINEALES
- Métodos iterativos 
	- Algoritmo Métodos de Jacobi y Gauss-Seidel 
- Ejercicios 

### T4 — APROXIMACIÓN, AJUSTE FUNCIONAL E INTERPOLACIÓN
- Aproximación polinomial simple e interpolación 
	- Algoritmo Aproximación polinomial simple 
- Polinomios de Lagrange 
	- Algoritmo Interpolación con polinomios de Lagrange 
- Diferencias divididas 
	- Algoritmo Tabla de diferencias divididas 
- Aproximación polinomial de Newton 
	- Algoritmo Interpolación polinomial de Newton 
- Polinomio de Newton en diferencias finitas 
- Estimación de errores en la aproximación 
- Aproximación polinomial segmentaria 
- Aproximación polinomial con mínimos cuadrados 
	- Algoritmo Aproximación con mínimos cuadrados 
- Aproximación multilineal con mínimos cuadrados 
- Ejercicios 

### T5 — INTEGRACIÓN Y DIFERENCIACIÓN NUMÉRICA
- Métodos de Newton-Cotes 
	- Algoritmo Método trapezoidal compuesto 
	- Algoritmo Método de Simpson compuesto 
- Cuadratura de Gauss 
	- Algoritmo Cuadratura de Gauss-Legendre 
- Integrales múltiples 
	- Algoritmo Integración doble por Simpson $1/3$ 
- Diferenciación numérica 
	- Algoritmo Derivación de polinomios de Lagrange 
- Ejercicios 

### T6 — SOLUCIÓN DE ECUACIONES DIFERENCIALES ORDINARIAS
- Formulación del problema de valor inicial 
- Método de Euler 
	- Algoritmo Método de Euler 
- Métodos de Taylor 
- Método de Euler modificado 
	- Algoritmo Método de Euler modificado 
- Métodos de Runge-Kutta 
	- Algoritmo Método de Runge-Kutta de cuarto orden 
- Métodos de predicción-corrección 
	- Algoritmo Método predictor-corrector 
- Ecuaciones diferenciales ordinarias de orden superior y sistemas de ecuaciones diferenciales ordinarias 
	- Algoritmo Método de Runge-Kutta de cuarto orden para un sistema de dos ecuaciones diferenciales ordinarias 
- Ejercicios 

### T7 — SOLUCIÓN DE ECUACIONES DIFERENCIALES PARCIALES
- Obtención de algunas ecuaciones diferenciales parciales a partir de la modelación de fenómenos físicos (ecuación de calor y ecuación de onda) 
- Aproximación de derivadas por diferencias finitas 
- Solución de la ecuación de calor unidimensional 
	- Algoritmo Método explícito 
	- Algoritmo Método implícito 
- Convergencia (método explícito), estabilidad y consistencia 
- Método de Crank-Nicholson 
	- Algoritmo Método de Crank-Nicholson 
- Otros métodos para resolver el problem de conducción de calor unidimensional 
- Solución de la ecuación de onda unidimensional 
- Tipos de condiciones frontera en procesos físicos y tratamientos de condiciones frontera irregulares 
- Ejercicios

---

## Bibliográfica (docente)

1. Antonio Nieves Hurtado, F. C. (2017). Métodos numéricos aplicados a la ingeniería. Mexico: GRUPO EDITORIAL PATRIA, S.A. DE C.V.
2. Steven C. Chapra, R. P. (2007). Métodos numéricos para ingenieros. Mexico: MCGRAW- HILL/INTERAMERICANA EDITORES, S.A. DE C.V.


---

## Stack completo

| Libro | Rol | Idioma |
|---|---|---|
| Chapra, Steven C. & Canale, Raymond P. — Numerical Methods for Engineers 7ma ed. | Teoría principal — columna vertebral del curso | Inglés |
| Burden, Richard L.; Faires, J. Douglas & Burden, Annette M. — Análisis Numérico 10ma ed. | Teoría rigurosa — demostraciones y análisis de error | Español |
| Kharab, Abdelwahab & Guenther, Ronald B. — An Introduction to Numerical Methods: A MATLAB Approach 4ta ed. | Problemas resueltos con implementación | Inglés |
| LeVeque, Randall J. — Finite Difference Methods for Ordinary and Partial Differential Equations 1ra ed. | Complemento EDPs — profundidad en diferencias finitas (T7) | Inglés |

---

## Flujo de uso

```
Tema nuevo                → Chapra & Canale
No entiendo el fondo      → Burden, Faires & Burden
A practicar / implementar → Kharab & Guenther
Profundidad en EDPs (T7)  → LeVeque
```

---

## Libros descartados

| Libro | Razón |
|---|---|
| Nieves Hurtado, Antonio — Métodos numéricos aplicados a la ingeniería (2017) | Redundante con Chapra y de menor profundidad |

---

%%
galaxy-links
[[_config/_library-system]]
[[guides/ETN505/ETN505_library]]
%%
