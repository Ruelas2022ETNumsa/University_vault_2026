---
title: "Inecuación: valor absoluto de fracción ≥ 3"
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

$$\left| \dfrac{4x+1}{x-2} \right| \geq 3$$

## Desarrollo

> [!note] Se aplica la propiedad $|a| \geq b \iff a \geq b \lor a \leq -b$. La solución final se obtiene mediante la unión de ambos casos.

**Caso 1:** $$\dfrac{4x+1}{x-2} \geq 3$$

$$\begin{array}{rcll}
\dfrac{4x+1}{x-2} - 3 & \geq & 0 & (\text{transposición})\\
\dfrac{4x+1-3(x-2)}{x-2} & \geq & 0 & (\text{común denominador})\\
\dfrac{x+7}{x-2} & \geq & 0 & (\text{simplificación})
\end{array}$$

Puntos críticos: $x = -7$, $x = 2$.

```desmos-graph
left=-12; right=5; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-7, 0) | label: -7
(2, 0) | open | label: 2
x <= -7 | #94D2BD
x > 2 | #94D2BD
```

$C_{s_1} = ]-\infty, -7] \cup ]2, \infty[$

**Caso 2:** $$\dfrac{4x+1}{x-2} \leq -3$$

$$\begin{array}{rcll}
\dfrac{4x+1}{x-2} + 3 & \leq & 0 & (\text{transposición})\\
\dfrac{4x+1+3(x-2)}{x-2} & \leq & 0 & (\text{común denominador})\\
\dfrac{7x-5}{x-2} & \leq & 0 & (\text{simplificación})
\end{array}$$

Puntos críticos: $x = \dfrac{5}{7}$, $x = 2$.

```desmos-graph
left=-2; right=5; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(0.714, 0) | label: 5/7
(2, 0) | open | label: 2
0.714 <= x < 2 | #94D2BD
```

$C_{s_2} = \left[ \dfrac{5}{7}, 2 \right[$

## Solución

$C_s = C_{s_1} \cup C_{s_2}$

```desmos-graph
left=-12; right=5; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-7, 0) | label: -7
(0.714, 0) | label: 5/7
(2, 0) | open | label: 2
(2, 0) | open | #005F73
x <= -7 | #EE9B00
2 > x >= 0.714 | #EE9B00
2 < x | #EE9B00
```

$C_s = ]-\infty, -7] \cup \left[ \dfrac{5}{7}, \infty \right[ - {2}$

%%
galaxy-links
[[MAT101-T00-metodo_signos]]
%%
