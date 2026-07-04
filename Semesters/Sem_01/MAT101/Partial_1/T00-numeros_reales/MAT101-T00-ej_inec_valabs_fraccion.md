---
title: "Inecuación: valor absoluto de fracción < 2"
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
Resolver la inecuación

$$\left| \dfrac{2x-1}{3x+2} \right| < 2$$

## Desarrollo

> [!note] Se aplica la propiedad del valor absoluto para inecuaciones: $|x| < a \iff -a < x < a$. 

El desarrollo se divide en dos condiciones que deben cumplirse simultáneamente (intersección).

**Condición 1:** $$\dfrac{2x-1}{3x+2} < 2$$

$$\begin{array}{rcll}
\dfrac{2x-1}{3x+2} - 2 & < & 0 & (\text{transposición})\\
\dfrac{2x-1-2(3x+2)}{3x+2} & < & 0 & (\text{común denominador})\\
\dfrac{-4x-5}{3x+2} & < & 0 & (\text{simplificación})
\end{array}$$

Puntos críticos: $x = -\dfrac{5}{4}$, $x = -\dfrac{2}{3}$. 

Prueba con $x=0$: $\dfrac{(-)}{(+)} = (-) < 0$ (Verdad).

```desmos-graph
left=-3; right=1; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-1.25, 0) | open | label: -5/4
(-0.666, 0) | open | label: -2/3
x < -1.25 | #94D2BD
x > -0.666 | #94D2BD
```

$C_{s_1} = ]-\infty, -\dfrac{5}{4}[ \cup ]-\dfrac{2}{3}, \infty[$

**Condición 2:** $$\dfrac{2x-1}{3x+2} > -2$$ 

$$\begin{array}{rcll}
\dfrac{2x-1}{3x+2} + 2 & > & 0 & (\text{transposición})\\
\dfrac{2x-1+6x+4}{3x+2} & > & 0 & (\text{común denominador})\\
\dfrac{8x+3}{3x+2} & > & 0 & (\text{simplificación})
\end{array}$$

Puntos críticos: $x = -\dfrac{3}{8}$, $x = -\dfrac{2}{3}$.
Prueba con $x=0$: $\dfrac{(+)}{(+)} = (+) > 0$ (Verdad).

```desmos-graph
left=-2; right=1; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-0.666, 0) | open | label: -2/3
(-0.375, 0) | open | label: -3/8
x < -0.666 | #94D2BD
x > -0.375 | #94D2BD
```

$C_{s_2} = ]-\infty, -\dfrac{2}{3}[ \cup ]-\dfrac{3}{8}, \infty[$

## Solución

$C_s = C_{s_1} \cap C_{s_2}$

```desmos-graph
left=-3; right=1; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-1.25, 0) | open | label: -5/4
(-0.375, 0) | open | label: -3/8
x < -1.25 | #EE9B00
x > -0.375 | #EE9B00
```

$C_s = ]-\infty, -\dfrac{5}{4}[ \cup ]-\dfrac{3}{8}, \infty[$ $C_s = {x / x < -\dfrac{5}{4} \lor x > -\dfrac{3}{8}}$

%%
galaxy-links
[[MAT101-T00-metodo_signos]]
%%
