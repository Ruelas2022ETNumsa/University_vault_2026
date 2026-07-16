---
title: "Inecuación racional: fracciones con factores cuadráticos"
galaxy_body: comet
subject: MAT101
semester: 1
partial: 1
topic: T00
source: "apunte"
concepts_used:
tags: [MAT101, galaxy-comet, P1, T00]
date_created: 2026-07-04
status: resuelto
---
## Enunciado
Resolver la inecuación
$$\dfrac{2x}{x^2+2x-3} + \dfrac{2x+1}{3x^2+8x-3} \leq \dfrac{-1}{3x^2-4x+1}$$

## Desarrollo

$$\begin{array}{rcll}
\dfrac{2x}{(x+3)(x-1)} + \dfrac{2x+1}{(3x-1)(x+3)} + \dfrac{1}{(3x-1)(x-1)} & \leq & 0 & (\text{factorización y transposición})\\
\dfrac{2x(3x-1) + (2x+1)(x-1) + (x+3)}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{común denominador})\\
\dfrac{6x^2-2x + 2x^2-x-1 + x+3}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{desarrollo})\\
\dfrac{8x^2-2x+2}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{simplificación})\\
\dfrac{4x^2-x+1}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{división entre 2}) 
\end{array}$$

Análisis del numerador $4x^2-x+1$: $D = (-1)^2 - 4(4)(1) = -15 < 0$.

> [!note] Como el discriminante es negativo y el coeficiente principal es positivo, la expresión es siempre positiva ($\in \mathbb{C}$ para raíces, siempre $(+)$ en $\mathbb{R}$).

Puntos críticos (denominador): $x=-3, 1/3, 1$. Prueba de signos en $x=0$: $\dfrac{(+)}{(+)(-)(-)} = \dfrac{(+)}{(+)} = (+) \leq 0$ (Falsedad).

```desmos-graph
left=-5; right=3; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-3, 0) | open | label: -3
(0.333, 0) | open | label: 1/3
(1, 0) | open | label: 1
x < -3 | #94D2BD
0.333 < x < 1 | #94D2BD
```

## Solución

$C_s = ]-\infty, -3[ \cup ]1/3, 1[$

 $C_s = {x / x < -3 \lor 1/3 < x < 1}$

---

%%
# galaxy-links
[[MAT101-T00-metodo_signos]]
%%
