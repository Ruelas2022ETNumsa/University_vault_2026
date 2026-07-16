---
title: "Inecuación irracional: raíz con condición de existencia"
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

$$\sqrt{x^2+x} < \sqrt{6}$$

## Desarrollo

> [!note] Esta inecuación irracional requiere que el radicando sea no negativo para existir en el campo real.

**1. Elevando al cuadrado:** 

$$\begin{array}{rcll}
x^2 + x & < & 6 & (\text{siendo ambos miembros } \geq 0)\\
x^2 + x - 6 & < & 0 & (\text{transposición})\\
(x+3)(x-2) & < & 0 & (\text{factorización})
\end{array}$$

Solución preliminar: $]-3, 2[$.

**2. Condición de existencia:** $x^2 + x \geq 0$ 

$$\begin{array}{rcll}
x(x+1) & \geq & 0 & (\text{factor común})
\end{array}$$ Puntos críticos: $x = 0$, $x = -1$.

```desmos-graph
left=-5; right=4; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(0, 0) | label: 0
(-1, 0) | label: -1
x <= -1 | #BB3E03
x >= 0 | #BB3E03
```

## Solución

**3. Intersección final:**

```desmos-graph
left=-5; right=4; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-3, 0) | open | label: -3
(-1, 0) | label: -1
(0, 0) | label: 0
(2, 0) | open | label: 2
-3 < x <= -1 | #EE9B00
0 <= x < 2 | #EE9B00
```

$C_s = ]-3, -1] \cup [0, 2[$

---

%%
# galaxy-links
[[MAT101-T00-metodo_signos]]
%%
