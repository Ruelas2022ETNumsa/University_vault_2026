

### Ejemplos resueltos

#### a) $x^4 \ge 9x^2$

$$
\begin{array}{rcl}
x^4 & \ge & 9x^2 \\[4pt]
x^4-9x^2 & \ge & 0 \\[4pt]
x^2(x^2-9) & \ge & 0 \\[4pt]
x^2(x-3)(x+3) & \ge & 0
\end{array}
$$

Puntos críticos:

$$
x=-3,\quad x=0,\quad x=3
$$

Tabla de signos:

| Intervalo        | Signo de \(x^2(x-3)(x+3)\) |
| ---------------- | -------------------------- |
| \(]-\infty,-3[\) | \(+\)                      |
| \(]-3,0[\)       | \(-\)                      |
| \(]0,3[\)        | \(-\)                      |
| \(]3,+\infty[\)  | \(+\)                      |

Como la inecuación es \(\ge 0\), se incluyen además los ceros.

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{-6<x<=-3\}|#ff7b7b
y=0 \{3<=x<6\}|#ff7b7b

(-3,0)|label:-3|#ff7b7b
(0,0)|label:0|#ff7b7b
(3,0)|label:3|#ff7b7b
````

$$  
C_s=  
]-\infty,-3]  
\cup  
{0}  
\cup  
[3,+\infty[  
$$

















---

#### b)

$$  
\frac{2x}{x^2+2x-3}  
+  
\frac{2x+1}{3x^2+8x-3}  
\le  
-\frac{1}{3x^2-4x+1}  
$$

Factorizando denominadores:

$$  
\begin{array}{rcl}  
x^2+2x-3 &=& (x+3)(x-1) \[4pt]  
3x^2+8x-3 &=& (3x-1)(x+3) \[4pt]  
3x^2-4x+1 &=& (3x-1)(x-1)  
\end{array}  
$$

Llevando todo al primer miembro:

$$  
\frac{2x}{(x+3)(x-1)}  
+  
\frac{2x+1}{(3x-1)(x+3)}  
+  
\frac{1}{(3x-1)(x-1)}  
\le 0  
$$

Reduciendo a un solo cociente:

$$  
\frac{  
2(x-1)(x+3)(3x-1)(4x^2-x+1)  
}{  
(x-1)^2(x+3)^2(3x-1)^2  
}  
\le 0  
$$

Como

$$  
4x^2-x+1>0  
\qquad \forall x\in\mathbb{R}  
$$

y los factores cuadrados del denominador son positivos en su dominio, el signo depende de

$$  
(x-1)(x+3)(3x-1)  
$$

Puntos críticos:

$$  
x=-3,\qquad x=\frac13,\qquad x=1  
$$

Además:

$$  
x\ne -3,\quad x\ne \frac13,\quad x\ne 1  
$$

Tabla de signos:

|Intervalo|Signo|
|---|---|
|(]-\infty,-3[)|(-)|
|(]-3,\frac13[)|(+)|
|(]\frac13,1[)|(-)|
|(]1,+\infty[)|(+)|

Por tanto:

```desmos-graph
left=-6; right=4; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{-6<x<-3\}|#ff7b7b
y=0 \{0.333333<x<1\}|#ff7b7b

(-3,0)|OPEN|label:-3|#ff7b7b
(0.333333,0)|OPEN|label:\frac{1}{3}|#ff7b7b
(1,0)|OPEN|label:1|#ff7b7b
```

$$  
C_s=  
]-\infty,-3[  
\cup  
]\tfrac13,1[  
$$

```

Para este inciso b) la simplificación algebraica intermedia es extensa; si en tu apunte aparece desarrollada paso a paso, puedo reproducirla con el mismo formato `array rcl` que has estado usando.
```