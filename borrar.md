






$$
\begin{array}{rcl}
2x(3x-1)+(2x+1)(x-1)+(x+3)
&=&
6x^2-2x+2x^2-x-1+x+3 \\[4pt]
&=&
8x^2-2x+2
\end{array}
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
x^2+2x-3 &=& (x+3)(x-1) \\[4pt]
3x^2+8x-3 &=& (3x-1)(x+3) \\[4pt]
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




---
---
---


Sí. Hay varios errores de sintaxis LaTeX y además el resultado final parece algebraicamente sospechoso.


---

### Problema con la reducción al mismo denominador

Voy a verificar el numerador.

Con denominador común

[  
(x+3)(x-1)(3x-1)  
]

el numerador es

[  
2x(3x-1)+(2x+1)(x-1)+(x+3).  
]

Desarrollando:

[  
6x^2-2x+2x^2-x-1+x+3  
]

[  
8x^2-2x+2.  
]

Por tanto,

```latex
$$
\frac{8x^2-2x+2}
{(x+3)(x-1)(3x-1)}
\le 0
$$
```

o factorizando un 2:

```latex
$$
\frac{2(4x^2-x+1)}
{(x+3)(x-1)(3x-1)}
\le 0
$$
```

---

### El paso final que escribiste

```latex
$$
\frac{
2(x-1)(x+3)(3x-1)(4x^2-x+1)
}{
(x-1)^2(x+3)^2(3x-1)^2
}
\le 0
$$
```

no es equivalente al paso anterior. Parece que alguien multiplicó numerador y denominador por el denominador común para obtener un denominador cuadrado, pero no lo indicó.

Si deseas usar el método de "denominador positivo", debe escribirse explícitamente:

```latex
$$
\frac{2(4x^2-x+1)}
{(x+3)(x-1)(3x-1)}
\cdot
\frac{(x+3)(x-1)(3x-1)}
{(x+3)(x-1)(3x-1)}
\le 0
$$
```

y entonces

```latex
$$
\frac{
2(x+3)(x-1)(3x-1)(4x^2-x+1)
}{
(x+3)^2(x-1)^2(3x-1)^2
}
\le 0
$$
```

Este último sí es algebraicamente correcto. Además,

[  
4x^2-x+1  
]

tiene discriminante

[  
\Delta=(-1)^2-4(4)(1)=-15<0,  
]

por lo que es siempre positivo y puede ignorarse en la tabla de signos. La inecuación se reduce a estudiar el signo de

[  
(x+3)(x-1)(3x-1).  
]