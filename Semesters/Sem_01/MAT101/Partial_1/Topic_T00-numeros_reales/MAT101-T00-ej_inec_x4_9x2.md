---
title: "Inecuación: x⁴ ≥ 9x²"
galaxy_body: comet
subject: MAT101
semester: 1
partial: 1
topic: T00
source: "apunte"
concepts_used:
  - "[[MAT101-T00-metodo_signos]]"
tags: [MAT101, galaxy-comet, P1, T00]
date_created: 2026-07-04
status: resuelto
---

## Enunciado

$x^4 \geq 9x^2$

## Desarrollo

$\begin{array}{rcll}
x^2(x^2-9) & \geq & 0 & (\text{transposición y factorización})\\
x^2(x-3)(x+3) & \geq & 0 & (\text{diferencia de cuadrados})\\
(x-0)^2(x-3)(x+3) & \geq & 0 & (\text{forma de puntos críticos})
\end{array}$

Puntos críticos: $x=-3, 0, 3$.

Prueba de signos en $I_1$: $x=-10 \rightarrow (+)(-)(-) \Rightarrow (+) \geq 0$ ✓

> [!note] El exponente par en $(x-0)^2$ hace que el signo **no se alterne** al pasar por $x=0$.

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-3, 0) | label: -3
(0, 0) | label: 0
(3, 0) | label: 3
x <= -3 | #94D2BD
x = 0 | #94D2BD
x >= 3 | #94D2BD
```

## Solución

$C_s = ]-\infty, -3] \cup \{0\} \cup [3, +\infty[$

$C_s = \{x \in \mathbb{R} \mid x \leq -3 \lor x=0 \lor x \geq 3\}$

%%
galaxy-links
[[MAT101-T00-metodo_signos]]
%%
