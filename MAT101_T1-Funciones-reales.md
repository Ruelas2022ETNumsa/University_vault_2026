# Funciones reales

## Definición de función

$f$ es función si para cada $x$ de un conjunto $D$ (dominio) existe una ley, regla de correspondencia que le asigna un único $y$ de otro conjunto $R$ (imágenes) según:

$$
y=f(x)
$$

$\therefore$ " $y$ es función de $x$ según $f$ "

- En lenguaje matemático

$$
f \text{ es función}
\iff
(\forall x\in D)(\exists !\, y\in R)
/\; y=f(x)
$$

- De otro modo

$$f:D\to R$$
$$x\mapsto y$$
$$y=f(x)$$

- Notación conjuntista

$$
f=\{(x,y)\mid y=f(x),\;x\in D,\;y\in R\}
$$

Ej. de funciones
$$
f(x)=\frac{x^3-4x}{x^2+1}
$$
$$
f(x)=\ln(4x)+\arctan \!\left(
\frac{\sqrt{x-1}}{x}
\right)
$$
$$
y=\sqrt{x^3-x-1}+\cos(x^2)
$$
$$
y=e^{-2x}+\tanh (6x)+\operatorname{sech}(x)
$$
$$etc.$$

---

## Notación

En $y=f(x)$ se reemplaza en cualquier "$x$" en $f$.

### Ejemplo 1
$$
f(x)=2x^2-3x+1
$$

$$
\begin{array}{rcl}
f(3) & = & 2(3)^2-3(3)+1 \\
     & = & 2(9)-9+1 \\
     & = & 18-9+1 \\
     & = & 10
\end{array}
$$

$$
\begin{array}{rcl}
f(a) & = & 2a^2-3a+1
\end{array}
$$

$$
\begin{array}{rcl}
f(4x-5)
& = &
2(4x-5)^2-3(4x-5)+1
\\[4pt]
& = &
2(16x^2-40x+25)-12x+15+1
\\[4pt]
& = &
32x^2-80x+50-12x+16
\\[4pt]
& = &
32x^2-92x+66
\end{array}
$$

$$
\begin{array}{rcl}
f\!\left(\frac{2}{x^3}\right)
& = &
2\left(\frac{2}{x^3}\right)^2
-3\left(\frac{2}{x^3}\right)+1
\\[6pt]
& = &
2\left(\frac{4}{x^6}\right)
-\frac{6}{x^3}+1
\\[6pt]
& = &
\frac{8}{x^6}
-\frac{6}{x^3}
+1
\end{array}
$$

---

### Ejercicio 2

Analizar si $f$ es o no función.
#### a)

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, orange]
(a1) .. controls (-1,1.5) and (1,-1.5) .. (b6);

\draw[->, thick, blue!70!green]%teal]
(a2) -- (b5);

\draw[->, thick, color=olive]%green]
(a3) .. controls (-1,-1.5) and (1,1.5) .. (b4);

\end{tikzpicture}
\end{document}
```


$f$ sí es función.

$$  D_f=\{1,2,3\}  $$
$$R_f=\{4,5,6\}=rango,\ recorrido,\ codominio ,\text{ conjunto de imágenes}$$
  $$f={(1,6),(2,5),(3,4)}$$

- $\forall x$ del $D$ debe tener imagen.
- El $D$ debe ser único y no debe repetirse.
    
---

#### b)

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, purple]
(a1) .. controls (-1,1.2) and (1,0.6) .. (b5);

\draw[->, thick, teal]
(a2) -- (b5);

\draw[->, thick, orange]
(a3) .. controls (-1,-1.2) and (1,-0.6) .. (b5);

\end{tikzpicture}
\end{document}
```

La relación **sí** es función porque:
$$D_f=\{1,2,3\}$$  $$R=\{4,5,6\} = codominio$$
$$R_{f}=\{5\}= \text{imagen o rango}$$
Todas las flechas llegan a 5.

---

#### c)

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

% 1 -> 4
\draw[->, thick, violet]
(a1) .. controls (-1,2) and (1,2) .. (b4);

% 3 -> 5
\draw[->, thick, teal]
(a3) .. controls (-1,-0.4) and (1,-0.2) .. (b5);

% 3 -> 6
\draw[->, thick, orange]
(a3) .. controls (-1,-2) and (1,-2) .. (b6);

\end{tikzpicture}
\end{document}
```

$f$ no es función.

- $2\in D$ no tiene imagen $\nexists, y\in R$.
- $3\in D$ tiene doble imagen $\nexists !, y\in R$.

---

## Álgebra de funciones

El dominio $D_f$ de la función
$$
y=f(x)
$$

se reconoce como el subconjunto de la recta real $\mathbb{R}$ que cumple las restricciones:

1. Si $f(x)=\frac{P(x)}{Q(x)}$ entonces : $$Q(x)\neq 0$$

2. Si $f(x)=\sqrt[n]{P(x)}$ con $n$ par, entonces : $$P(x)\ge 0$$
3. Si $f(x)=\log_a(P(x))$ con $a>0$, entonces : $$P(x)>0$$
4. Si $f(x)=a^{P(x)}$ entonces : $$a>0\quad y\quad a\neq 1$$
5. Si $f(x)=\arcsin (P(x))\quad$ o $\quad f(x)=\arccos(P(x))$ entonces : $$-1\le P(x)\le 1$$

---

### **Ej.** Hallar el dominio de

$$
f(x)=\sqrt{\frac{x^3-4x}{1-x^2}}
+\log\left(\frac{x^3-x^2-2x}{x+4}\right)
$$
Analizamos por separado.

1. Sea $\sqrt{\frac{x^3-4x}{1-x^2}}$ entonces :
$$
\frac{x^3-4x}{1-x^2}\ge 0
$$
Factorizando:

$$
\frac{x(x^2-4)}{(1+x)(1-x)}\ge 0
$$
$$
\frac{x(x-2)(x+2)}{(1+x)(1-x)}\ge 0
$$

Puntos críticos:

$$
x=-2,\,-1,\,0,\,1,\,2
$$


Tabla

Para $\frac{x(x-2)(x+2)}{(1+x)(1-x)}\ge 0$

| Intervalo      | Prueba x | Signo i                        | $R_i$ |
| -------------- | -------- | ------------------------------ | ----- |
| $]-\infty,-2[$ | $-10$    | $\frac{(-)(-)(-)}{(-)(+)}=(+)$ | V     |
| $-2$           | $-2$     | $0$                            | V     |
| $]-2,-1[$      | $-1.5$   | $\frac{(-)(-)(+)}{(-)(+)}=(-)$ | F     |
| $-1$           | $-1$     | No existe                      | F     |
| $]-1,0[$       | $-0.5$   | $\frac{(-)(-)(+)}{(+)(+)}=(+)$ | V     |
| $0$            | $0$      | $0$                            | V     |
| $]0,1[$        | $0.5$    | $\frac{(+)(-)(+)}{(+)(+)}=(-)$ | F     |
| $1$            | $1$      | No existe                      | F     |
| $]1,2[$        | $1.5$    | $\frac{(+)(-)(+)}{(+)(-)}=(+)$ | V     |
| $2$            | $2$      | $0$                            | V     |
| $]2,+\infty[$  | $10$     | $\frac{(+)(+)(+)}{(+)(-)}=(-)$ | F     |

Gráfico de intervalos (Cs₁)

```desmos-graph
left=-5.5; right=5.5; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{x<-5\}|#7e57c2|DOTTED
y=0 \{-5<x<=-2\}|#7e57c2

(-2,0)|label:-2|#7e57c2

y=0 \{-1<x<=0\}|#7e57c2
(-1,0)|OPEN|label:-1|#7e57c2
(0,0)|label:0|#7e57c2

y=0 \{1<=x<=2\}|#7e57c2
(1,0)|OPEN|label:1|#7e57c2
(2,0)|label:2|#7e57c2
```


son **verdaderos** los intervalos donde el signo es positivo o cero:

$$Cs_{1}=]−∞,−2]∪]−1,0]∪]1,2]$$


---

2. Sea $\log\left(\frac{x^3-x^2-2x}{x+4}\right)$ entonces :
$$
\frac{x^3-x^2-2x}{x+4}>0
$$
Factorizando:
$$
\frac{x(x-2)(x+1)}{x+4}>0
$$
Puntos críticos:
$$
x=-4,\,-1,\,0,\,2
$$


Para

$$
\frac{x(x-2)(x+1)}{x+4}>0
$$

los puntos críticos son

$$
x=-4,\,-1,\,0,\,2
$$

| Intervalo      | Prueba x | Signo i                     | $R_i$ |
| -------------- | -------- | --------------------------- | ----- |
| $]-\infty,-4[$ | $-10$    | $\frac{(-)(-)(-)}{(-)}=(+)$ | V     |
| $-4$           | $-4$     | No existe                   | F     |
| $]-4,-1[$      | $-2$     | $\frac{(-)(-)(-)}{(+)}=(-)$ | F     |
| $-1$           | $-1$     | $0$                         | F     |
| $]-1,0[$       | $-0.5$   | $\frac{(-)(-)(+)}{(+)}=(+)$ | V     |
| $0$            | $0$      | $0$                         | F     |
| $]0,2[$        | $1$      | $\frac{(+)(-)(+)}{(+)}=(-)$ | F     |
| $2$            | $2$      | $0$                         | F     |
| $]2,+\infty[$  | $10$     | $\frac{(+)(+)(+)}{(+)}=(+)$ | V     |

Gráfico de intervalos (Cs₂)

```desmos-graph
left=-6.5; right=5.5; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{x<-6\}|#26a69a|DOTTED
y=0 \{-6<x<-4\}|#26a69a
(-4,0)|OPEN|label:-4|#26a69a

y=0 \{-1<x<0\}|#26a69a
(-1,0)|OPEN|label:-1|#26a69a
(0,0)|OPEN|label:0|#26a69a

y=0 \{2<x<5\}|#26a69a
y=0 \{x>5\}|#26a69a|DOTTED
(2,0)|OPEN|label:2|#26a69a
```

Por tanto,

$$  
Cs_2=  
]-\infty,-4[  
\cup  
]-1,0[  
\cup  
]2,+\infty[  
$$

---

Finalmente:

$$  
D_f=Cs_1\cap Cs_2  
$$

```desmos-graph
left=-5.5; right=5.5; bottom=-1; top=3;
width=500; height=120;
---
y=2 \{x<-5\}|#7e57c2|DOTTED
y=2 \{-5<x<=-2\}|#7e57c2

(-2,2)|label:-2|#7e57c2

y=2 \{-1<x<=0\}|#7e57c2
(-1,2)|OPEN|label:-1|#7e57c2
(0,2)|label:0|#7e57c2

y=2 \{1<=x<=2\}|#7e57c2
(1,2)|OPEN|label:1|#7e57c2
(2,2)|label:2|#7e57c2

y=1 \{x<-6\}|#26a69a|DOTTED
y=1 \{-6<x<-4\}|#26a69a
(-4,1)|OPEN|label:-4|#26a69a

y=1 \{-1<x<0\}|#26a69a
(-1,1)|OPEN|label:-1|#26a69a
(0,1)|OPEN|label:0|#26a69a

y=1 \{2<x<5\}|#26a69a
y=1 \{x>5\}|#26a69a|DOTTED
(2,1)|OPEN|label:2|#26a69a


y=0 \{x<-5\}|#8d6e63|DOTTED
y=0 \{-5<x<-4\}|#8d6e63
(-4,0)|OPEN|label:-4|#8d6e63

y=0 \{-1<x<0\}|#8d6e63
(-1,0)|OPEN|label:-1|#8d6e63
(0,0)|OPEN|label:0|#8d6e63

```

$$
D_f=
]-\infty,-4[
\cup
]-1,0[
$$

---

## Aritmética de funciones

Sean $y=f(x) \quad,\quad y=g(x)$ funciones reales con dominios $D_f$ y $D_g$ respectivamente.

1. **Suma**
$$
(f\pm g)(x)=f(x)\pm g(x)
$$
$$
D_{f\pm g}=D_f\cap D_g
$$

2. **Producto**
$$
(f\cdot g)(x)=f(x)\,g(x)
$$
$$
D_{f\cdot g}=D_f\cap D_g
$$

3. **Cociente**
$$
\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}
$$
$$
D_{f}{g}=D_{f}\cap D_{g}\quad y
\quad
g(x)\neq 0
$$

---

## 4. Función par

$y=f(x)$ es par si verifica

$$
f(-x)=f(x)
$$

La gráfica de $y=f(x)$ es simétrica respecto al eje $y$.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.5]

% Ejes
\draw[->] (-2.2,0) -- (2.2,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.8) node[above] {$y$};

% Curva
\draw[thick, teal, domain=-1.35:1.35, samples=120]
  plot (\x,{(\x)^4-(\x)^2+0.5});

% Segmento de simetría
\draw[dashed] (-1,0.5) -- (1,0.5);

% Puntos
\fill (-1,0.5) circle (0.05);
\fill (1,0.5) circle (0.05);

% Etiquetas de puntos
\node[above] at (-1,0.5) {$(-1, 0.5)$};
\node[above] at (1,0.5) {$(1, 0.5)$};

% Marcas en eje x
\node[below] at (-1,0) {$-1$};
\node[below] at (1,0) {$1$};

% Etiqueta de función
\node[right] at (1.1,1.55) {$y=x^4-x^2+0.5$};

% Eje de simetría
\node at (0,-0.35) {Eje de sim\'etria};

\end{tikzpicture}
\end{document}
```
> [!note]
> Gráfica: espejo.

**Ej.**

$$
f(x)=\frac{x^8-4x^6}{x^2+1}
$$
es par, ya que
$$
f(-x)=\frac{x^8-4x^6}{x^2+1}
$$

por tanto
$$
f(-x)=f(x)
$$


**Otro**
$$
f(x)=\cos x
$$
es par porque
$$
f(-x)=\cos(-x)=\cos(x)
$$
$$
f(-x)=f(x)
$$

---

## 5. Función impar

$y=f(x)$ es impar si cumple:

$$
f(-x)=-f(x)
$$

La gráfica de $y=f(x)$ impar es simétrica respecto al origen $(0,0)$.



```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-1.8,0) -- (1.8,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

% Curva
\draw[thick, teal, domain=-1.5:1.5, samples=200]
  plot (\x,{(\x)^3-(\x)});

% Segmento que muestra la simetría respecto al origen
\draw[dashed] (-1,0) -- (1,0);

% Puntos simétricos
\fill (-0.5,0.375) circle (0.05);
\fill (0.5,-0.375) circle (0.05);

% Etiquetas de puntos
\node[above left] at (-0.5,0.375) {$(-0.5,\;0.375)$};
\node[below right] at (0.5,-0.375) {$(0.5,\;-0.375)$};



% Etiqueta de función
\node[right] at (0.8,0.9) {$y=x^3-x$};

% Centro de simetría
\fill (0,0) circle (0.05);
\node[below left] at (0,0) {$O(0,0)$};

\end{tikzpicture}
\end{document}
```


> [!note]
> Gráfica: doble espejo.

**Ej.**

$$
f(x)=2x^5+6x^3-8x
$$

es impar porque:

$$
\begin{array}{rcl}
f(-x) & = & 2(-x)^5+6(-x)^3-8(-x) \\
      & = & -2x^5-6x^3+8x \\
      & = & -(2x^5+6x^3-8x) \\
      & = & -f(x)
\end{array}
$$

Por tanto,

$$
f(-x)=-f(x)
$$

**Otro**

$\text{sen}\,x$ es impar porque

$$
f(-x)=\text{sen}(-x)=-(\text{sen}(x))=-f(x)
$$

> [!note]
> Ejemplo que no es función impar:
> $$f(x)=2x^5+6x^3-8x+4$$
> No es impar ni par, porque no cumple $f(-x)=-f(x)$. El 4 añadido impide la condición

---

## 6. Función periódica

$y=f(x)$ es periódica con período $p$ si cumple

$$
f(x+p)=f(x)
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5]

% Ejes
\draw[->] (-0.5,0) -- (7.2,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.4) node[above] {$y$};

% Curva y = sen²(x)
\draw[thick, teal, domain=0:6.283, samples=200]
  plot (\x,{sin(\x r)*sin(\x r)});

% Marcas
\node[below] at (0,0) {$0$};
\node[below] at (1.57,0) {$\frac{\pi}{2}$};
\node[below] at (3.14,0) {$\pi$};
\node[below] at (4.71,0) {$\frac{3\pi}{2}$};
\node[below] at (6.28,0) {$2\pi$};

% Máximos
\fill (1.57,1) circle (0.04);
\fill (4.71,1) circle (0.04);

% Etiqueta
\node[right] at (6.3,0.5) {$y=\sin^2 x$};

% Periodo
\draw[dashed] (0,1) -- (6.28,1);
\node[above] at (1.57,1.2) {$p=\pi$};

\end{tikzpicture}
\end{document}
```

- La gráfica en $p$ unidades se repite indefinidamente.

- **Ej.**

$f(x)=\text{sen}\,x$ es periódica con $p=2\pi$

$$
\begin{array}{rcl}
f(x+2\pi) & = & \text{sen}(x+2\pi) \\
          & = & \text{sen}\,x \\
          & = & f(x)
\end{array}
$$

Por tanto,

$$
f(x+2\pi)=f(x)
$$

> [!note]
> Gráfica: función periódica ($y=\text{sen}\,x$).

- otros

$$f(x)=\cos (x) \quad,\quad p=2\pi$$
$$f(x)=\tan (x) \quad,\quad p=\pi$$


---

## 7. Función inversa

- Sea la función biyectiva $f : X \to Y$
$$
f=\{(x,y)\mid y=f(x)\}
$$
- Se define
$$
f^{-1}=\text{función inversa de }f
$$
$$
f^{-1}=\{(x^{*},y^{*})\mid y^{*}=f^{-1}(x^{*})\}
$$

Si se usan las variables originales:
$$
x=f^{-1}(y)
$$

> [!note]
> $$f^{-1}(x)\neq \dfrac{1}{f(x)}$$

> [!important]
> Ojo:
>
> $$a^{-1}=\dfrac{1}{a}$, si $a\neq 0 \quad y \quad\in\mathbb{R}.$$

- Operativamente, para calcular

$$
y=f^{-1}(x)
$$

a partir de

$$
y=f(x)
$$

- Se recomienda:

	- Intercambiar variables
	$$x \text{ por } y \;;\; y \text{ por } x$$$$x=f(y)$$
	- Por álgebra despejar la nueva $y$
	$$
	y=g(x)
	$$
- El resultado es lo pedido
$$
y=f^{-1}(x)
$$
**Ej.** Hallar $f^{-1}(x)$ para

$$
f(x)=\frac{2x^3-7}{3x^3+4}
$$
$$
y=\frac{2x^3-7}{3x^3+4}
\;\Rightarrow\;
x=\frac{2y^3-7}{3y^3+4}
$$
$$
\begin{array}{rcl}
(3y^3+4)x &=& 2y^3-7\\
4x+7 &=& y^3(2-3x)
\end{array}
$$
$$
\sqrt[3]{\frac{4x+7}{2-3x}}=y
$$
Por tanto,
$$
f^{-1}(x)=\sqrt[3]{\frac{4x+7}{2-3x}}
$$

## 8. Composición de funciones

**Def.** Sean las funciones
$$f:B\to C$$
$$g:A\to B$$
donde
$$y=f(x)$$

- Se define
$$(f \circ g)(x) = f(g(x))$$

("f compuesta con g en x")
$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$
$$D_{f\circ g}=
\{\,x\in D_g \;:\; g(x)\in D_f\,\}
$$



```tikz
\begin{document}
\begin{tikzpicture}

% Conjuntos
\draw (-3.5,0) ellipse (1 and 1.5);
\draw (0,0) ellipse (1 and 1.5);
\draw (3.5,0) ellipse (1 and 1.5);

% Nombres de conjuntos (debajo)
\node at (-3.5,-2.1) {$A$};
\node at (0,-2.1) {$B$};
\node at (3.5,-2.1) {$C$};

% Elementos
\node (x) at (-3.5,0) {$x$};
\node (gx) at (0,0) {$g(x)$};
\node (fgx) at (3.5,0) {$f(g(x))$};

% Flecha g
\draw[->, thick, teal]
(x) .. controls (-2.0,0.8) and (-1.2,0.8) .. (gx);

\node at (-1.75,1.05) {$g$};

% Flecha f
\draw[->, thick, orange]
(gx) .. controls (1.2,0.8) and (2.0,0.8) .. (fgx);

\node at (1.75,1.05) {$f$};

\end{tikzpicture}
\end{document}
```

> donde el dominio de $f \circ g$ es el conjunto de todos los $x$ en el dominio de $g$ tales que $g(x)$ esté en el dominio de $f$.






### Propiedades
1. Propiedad 1 — No conmutatividad
$$f \circ g \neq g \circ f \quad \text{(en general)}$$

La composición **no es conmutativa**. El orden importa: aplicar primero $g$ y luego $f$ es distinto de aplicar primero $f$ y luego $g$.


2. Propiedad 2 — Distributividad de la composición por la derecha
$$(f + g) \circ h = f \circ h + g \circ h$$

La composición **es distributiva respecto a la suma por la derecha**: componer una suma de funciones con $h$ es equivalente a componer cada función con $h$ y luego sumar.

> **Condición:** $h$ debe estar en el dominio de $f$ y de $g$.


3. Propiedad 3 — No distributividad de la composición por la izquierda
$$f \circ (g + h) \neq f \circ g + f \circ h \quad \text{(en general)}$$

La composición **no es distributiva respecto a la suma por la izquierda**, salvo que $f$ sea una función lineal de la forma $f(x) = ax + b$ con $b = 0$ (es decir, $f(x) = ax$).


4. Propiedad 4 — Asociatividad
$$f \circ (g \circ h) = (f \circ g) \circ h$$

La composición **es asociativa**, siempre que las composiciones involucradas estén definidas (es decir, que los dominios e imágenes sean compatibles).

> **Condición:** Se requiere que $\text{Im}(h) \subseteq \text{Dom}(g)$ y $\text{Im}(g) \subseteq \text{Dom}(f)$.

5. Propiedad 5 — Composición con la función inversa

Si $f$ es biyectiva (inyectiva y sobreyectiva), entonces existe $f^{-1}$ y se cumple:

$$(f \circ f^{-1})(x) = (f^{-1} \circ f)(x) = x = \text{Id}(x)$$

donde $\text{Id}$ es la **función identidad**. Es decir, componer una función con su inversa (en cualquier orden) produce la identidad.

> **Condición:** $f$ debe ser biyectiva para que $f^{-1}$ exista.


6. Propiedad 6 — Dominio e imagen de la composición ⚠️ _Corrección_
Si $f: A \to B$ y $g: B \to C$, entonces:
$$g \circ f : A \to C$$

> **Condición:** El codominio de $f$ debe coincidir con el dominio de $g$ (es decir, $\text{Im}(f) \subseteq \text{Dom}(g) = B$).

7. Propiedad 7 — Composición con la función identidad
Sea $\text{Id}$ la función identidad, definida como $\text{Id}(x) = x$. Entonces:
$$f \circ \text{Id} = \text{Id} \circ f = f$$

La identidad actúa como **elemento neutro** de la composición.

---

#### **Ejercicio a.**
Para
$$f(x)=\sqrt{\frac{x}{x-1}}$$
$$g(x)=e^{-4x^2}$$

Hallar $(f\circ g)(x)$ y $(g\circ f)(x)$.

**Sol.**

a) Composición $f\circ g$
$$(f\circ g)(x)=f(g(x))$$

Sustituyendo $g(x)$ en $f$:
$$(f\circ g)(x)=
\sqrt{
\frac{e^{-4x^2}}
     {e^{-4x^2}-1}
}$$

simplificando
$$(f\circ g)(x)=
\sqrt{
\frac{1}
     {1-e^{4x^2}}
}$$


b) Composición $g\circ f$
$$(g\circ f)(x)=g(f(x))$$

Sustituyendo $f(x)$ en $g$:
$$(g\circ f)(x)=
e^{-4\left(\sqrt{\frac{x}{x-1}}\right)^2}$$

$$(g\circ f)(x)=
e^{-\frac{4x}{x-1}}$$

$$(g\circ f)(x)=
\sqrt[1-x]{e^{4x}}$$

---

#### **Ejercicio b**
Si
$$f(x)=\frac{3x}{2}-1$$

hallar
$$(f\circ f\circ f)\left(\frac{3x}{2}+1\right)$$

**Sol.**

Sea
$$u=\frac{3x}{2}+1$$

Primera composición:
$$f(u)=
\frac{3}{2}\left(\frac{3x}{2}+1\right)-1
$$

$$f(u)=
\frac{9x}{4}+\frac{1}{2}
$$

Segunda composición:
$$f(f(u))=
\frac{3}{2}\left(\frac{9x}{4}+\frac{1}{2}\right)-1
$$

$$f(f(u))=
\frac{27x}{8}-\frac{1}{4}
$$

Tercera composición:
$$f(f(f(u)))=
\frac{3}{2}\left(\frac{27x}{8}-\frac{1}{4}\right)-1
$$

$$f(f(f(u)))=\frac{81x}{16}-\frac{11}{8}
$$

Por tanto,
$$(f\circ f\circ f)\left(\frac{3x}{2}+1\right)=
\frac{81x}{16}-\frac{11}{8}
$$


---


#### **Ejercicio c**
Se conocen
$$f(x)=\frac{2x^{3}-7}{3x^3+4}$$
y
$$f^{-1}(x)=\sqrt[3]{\frac{7+4x}{2-3x}}$$
Hallar
$$(f\circ f^{-1})(x)$$

**Sol.**

Por definición de composición,
$$(f\circ f^{-1})(x)=
f\!\left(f^{-1}(x)\right)
$$

Sustituyendo:
$$(f\circ f^{-1})(x)=
\frac{
2\left(\sqrt[3]{\frac{7+4x}{2-3x}}\right)^3-7
}{
3\left(\sqrt[3]{\frac{7+4x}{2-3x}}\right)^3+4
}
$$

Como
$$\left(\sqrt[3]{\frac{7+4x}{2-3x}}\right)^3=
\frac{7+4x}{2-3x}
$$

resulta
$$(f\circ f^{-1})(x)=
\frac{
2\left(\frac{7+4x}{2-3x}\right)-7
}{
3\left(\frac{7+4x}{2-3x}\right)+4
}$$

$$=\frac{
\frac{14+8x-14+21x}{2-3x}
}{
\frac{21+12x+8-12x}{2-3x}
}$$

$$=
\frac{
\frac{29x}{2-3x}
}{
\frac{29}{2-3x}
}$$

$$=x$$

Por tanto,
$$(f\circ f^{-1})(x)=x$$


> [!note]  
> Se verifica la propiedad de la función inversa:
> 
> $$  
> f\circ f^{-1}=I  
> $$
> 
> donde $I(x)=x$ es la función identidad.


---

#### **Ejercicio d**
Si
$$f(x)=\frac{2x+1}{x}$$
y
$$(f\circ g)(x)=\frac{x}{x-1}$$

hallar $g(x)$.

**Sol.**

Por definición de composición,

$$(f\circ g)(x)=f(g(x))$$

Sustituyendo $g(x)$ en la función $f$:
$$\frac{2g(x)+1}{g(x)}=
\frac{x}{x-1}
$$

Multiplicando en cruz:
$$(2g(x)+1)(x-1)=x\,g(x)$$

$$2xg(x)-2g(x)+x-1=xg(x)$$

Agrupando términos con $g(x)$:
$$xg(x)-2g(x)=1-x$$

$$g(x)(x-2)=1-x$$

Despejando:
$$g(x)=\frac{1-x}{x-2}$$

o equivalentemente,
$$g(x)=\frac{x-1}{2-x}$$

Por tanto,
$$g(x)=\frac{1-x}{x-2}$$

>[!note]  
>También puede resolverse utilizando
>$$g=f^{−1}∘(f∘g)$$
>pero el despeje directo suele ser el procedimiento más corto.

---
#### **Ejercicio e**
Si
$$f(x)=\frac{x-1}{x}$$

hallar
$$\underbrace{(f\circ f\circ f\circ\cdots\circ f)}_{50\text{ veces}}(x)$$

**Sol.**

Calculamos las primeras composiciones:
$$f(x)=\frac{x-1}{x}$$

$$f(f(x))=
\frac{\frac{x-1}{x}-1}{\frac{x-1}{x}}
$$

$$=\frac{-1/x}{(x-1)/x}$$

$$=-\frac{1}{x-1}$$

Entonces,
$$f^2(x)=-\frac{1}{x-1}$$

Ahora,
$$f^3(x)=
f\!\left(-\frac{1}{x-1}\right)
$$

$$=\frac{-\frac{1}{x-1}-1}{-\frac{1}{x-1}}$$

$$=x$$

Por tanto,
$$f^3(x)=x$$

Luego la composición es periódica de período $3$:
$$f^1(x)=f(x)$$

$$f^2(x)=-\frac{1}{x-1}$$

$$f^3(x)=x$$

$$f^4(x)=f(x)$$

$$f^5(x)=f^2(x)$$

$$f^6(x)=x$$

y así sucesivamente.

Como
$$50=3\cdot16+2$$

se tiene
$$f^{50}(x)=f^2(x)$$

Por consiguiente,
$$\underbrace{(f\circ f\circ f\circ\cdots\circ f)}_{50\text{ veces}}(x)=
-\frac{1}{x-1}
$$

> [!note]  
> Se utilizó que la función cumple
> 
> $$  
> f^3(x)=x  
> $$
> 
> por lo que las composiciones se repiten cada tres aplicaciones.

---

#### **Ejercicio f**
Para
$$f\!\left(\frac{x-2}{x}\right)=\frac{x-1}{x+1}$$

y
$$g^{-1}\!\left(\frac{2}{x}\right)=\frac{x}{x+2}$$

hallar
$$(f^{-1}\circ g\circ f)\left(\frac{1}{x^3}\right)$$

**Sol.**

Primero determinamos $f$.
Sea
$$t=\frac{x-2}{x}$$

entonces
$$tx=x-2$$

$$x(t-1)=-2$$

$$x=\frac{2}{1-t}$$

Sustituyendo en
$$f(t)=\frac{x-1}{x+1}$$

obtenemos
$$f(t)=
\frac{\frac{2}{1-t}-1}
     {\frac{2}{1-t}+1}
$$

$$=\frac{1+t}{3-t}$$

Por tanto,
$$f(x)=\frac{x+1}{3-x}$$

Ahora hallamos $f^{-1}$:

$$y=\frac{x+1}{3-x}$$

$$y(3-x)=x+1$$

$$3y-1=x(1+y)$$

$$x=\frac{3y-1}{y+1}$$

Luego,
$$f^{-1}(x)=\frac{3x-1}{x+1}$$

---

Determinamos ahora $g$.

Sea
$$t=\frac{2}{x}$$

entonces
$$x=\frac{2}{t}$$

y
$$g^{-1}(t)=
\frac{\frac{2}{t}}
     {\frac{2}{t}+2}
=
\frac{1}{t+1}
$$

Así,
$$g^{-1}(x)=\frac{1}{x+1}$$

Hallando la inversa:
$$y=\frac{1}{x+1}$$

$$x+1=\frac{1}{y}$$

$$x=\frac{1-y}{y}$$

Por tanto,
$$g(x)=\frac{1-x}{x}$$

---

Ahora calculamos
$$(f^{-1}\circ g\circ f)\left(\frac{1}{x^3}\right)$$

Sea
$$u=\frac{1}{x^3}$$

Entonces
$$f(u)=
\frac{u+1}{3-u}
$$

$$=\frac{\frac1{x^3}+1}
     {3-\frac1{x^3}}
$$

$$=\frac{x^3+1}{3x^3-1}$$

Aplicando $g$:
$$g(f(u))=
\frac{1-\frac{x^3+1}{3x^3-1}}
     {\frac{x^3+1}{3x^3-1}}
$$

$$=\frac{2x^3-2}{x^3+1}$$

$$=\frac{2(x^3-1)}{x^3+1}$$

Aplicando $f^{-1}$:
$$f^{-1}(g(f(u)))=
\frac{3\left(\frac{2(x^3-1)}{x^3+1}\right)-1}
     {\left(\frac{2(x^3-1)}{x^3+1}\right)+1}
$$

$$=\frac{\frac{6(x^3-1)-(x^3+1)}{x^3+1}}
     {\frac{2(x^3-1)+(x^3+1)}{x^3+1}}
$$

$$=\frac{5x^3-7}{3x^3-1}$$

Por consiguiente,
$$(f^{-1}\circ g\circ f)\left(\frac{1}{x^3}\right)=
\frac{5x^3-7}{3x^3-1}
$$

---

## Características generales de las principales funciones reales

### Función de 1er grado (recta)

La función de primer grado tiene la forma:

$$f(x)=ax+b$$

donde:
- $D_{f}=\mathbb{R} \, , \, R_{f}=\mathbb{R}$

ademas:

- $a=\text{tg}(\alpha)$ es la pendiente de la recta.
- $b$ es la ordenada en el origen.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Ejes
\draw[->] (-0.5,0) -- (4.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

% Recta f(x)=ax+b con b=1
\draw[very thick,color=teal] (0,1) -- (4,4);

% Marca de b
\draw (-0.08,1) -- (0.08,1);
\node[left] at (0,1) {$b$};

% Triángulo para la pendiente
\draw[dashed] (1,1.75) -- (2,1.75);
\draw[dashed] (2,1.75) -- (2,2.5);

\node[below] at (1.5,1.75) {$1$};
\node[right] at (2,2.1) {$a$};

% Ángulo alfa
\draw (1.7,1.8) arc[start angle=0,end angle=37,radius=0.5];
\node at (1.4,1.9) {$\alpha$};

% Etiquetas
\node[color=teal] at (3.2,2.5) {$f(x)=ax+b$};
\node at (3.2,1.5) {$\mathrm{tg}(\alpha)=a$};

\end{tikzpicture}
\end{document}
```

#### Función constante

Cuando:
$$a=0$$

la función queda:
$$f(x)=b$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

\draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};

\draw[very thick,color=teal] (-0.2,2) -- (3.5,2);

\node[left] at (0,2) {$b$};
\node[above right] at (2.5,2) {$f(x)=b$};

\end{tikzpicture}
\end{document}
```

#### Recta vertical

La ecuación:

$$x=c$$

representa una recta vertical.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Ejes
\draw[->] (-1,0) -- (3.5,0);
\draw[->] (0,-1) -- (0,3.5);

% Recta vertical x=c
\draw[very thick,color=orange] (2,-0.8) -- (2,3);

% Etiquetas
\node at (2,-0.3) {$c$};
\node at (2.7,2.5) {$x=c$};

\end{tikzpicture}
\end{document}
```

La recta vertical no representa una función.


#### Función lineal 

$$y=f(x)=ax \, ; \, a\in \mathbb{R}$$
$$D_{f}=\mathbb{R} \, ; \, R_{f}=\mathbb{R}$$


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

% Ejes
\draw[->] (-0.5,0) -- (4.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};

% Recta
\draw[very thick,color=teal] (0,0) -- (4,3);



% Etiquetas
\node[right] at (2,1.15) {$a$};

% Ángulo alfa
\draw (0.6,0) arc[start angle=0,end angle=37,radius=0.6];
\node at (0.95,0.25) {$\alpha$};

% Fórmula
\node[below right] at (2.6,1.9) {recta en el origen};

\end{tikzpicture}
\end{document}
```

- además, ideas graficas

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-0.5, xmax=13,
    ymin=-1.5, ymax=1.5,
    width=12cm,
    height=6cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Curva senoidal
\addplot[
    very thick,
    teal,
    domain=0:12.56,
    samples=200
]
{sin(deg(x))};

% Rectas verticales
\draw[dashed,gray] (axis cs:1, -1.3) -- (axis cs:1, 1.3);
\draw[dashed,gray] (axis cs:4, -1.3) -- (axis cs:4, 1.3);
\draw[dashed,gray] (axis cs:7, -1.3) -- (axis cs:7, 1.3);
\draw[dashed,gray] (axis cs:10, -1.3) -- (axis cs:10, 1.3);

% Puntos de intersección
\fill[orange] (axis cs:1,{sin(deg(1))}) circle (2pt);
\fill[orange] (axis cs:4,{sin(deg(4))}) circle (2pt);
\fill[orange] (axis cs:7,{sin(deg(7))}) circle (2pt);
\fill[orange] (axis cs:10,{sin(deg(10))}) circle (2pt);

\end{axis}
\end{tikzpicture}
\end{document}
```

>Si toda vertical corta en un punto la grafica es **funcion**

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% Ejes
\draw[->] (-2,0) -- (6,0) node[right] {$x$};
\draw[->] (0,-3) -- (0,3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-1,1,2,3,4,5}
    \draw (\x,0.05) -- (\x,-0.05) node[below, font=\small] {\x};

% Ticks eje y
\foreach \y in {-2,-1,1,2}
    \draw (0.05,\y) -- (-0.05,\y) node[left, font=\small] {\y};

% Parábola y²=x+1 → x=y²-1, graficada con y como parámetro
\draw[very thick, teal, smooth, samples=100, domain=-2.7:2.7]
    plot ({(\x)^2 - 1}, {\x});

% Recta vertical x=2
\draw[dashed, gray, thick] (2,-2.7) -- (2,2.7);

% Puntos de intersección
\fill[orange] (2, 1.732) circle (0.07);
\fill[orange] (2,-1.732) circle (0.07);

% Etiquetas curva y recta
\node[teal] at (4.8, 2) {$y^2=x+1$};
\node[gray]  at (2.6, 2.4) {$x=2$};



% Vértice
\fill[teal!70] (-1,0) circle (0.07);
\node[teal, above left, font=\small] at (-1,0) {$(-1,0)$};

\end{tikzpicture}
\end{document}
```

>Si una vertical corta en mas de un punto es una grafica **no es función**, es solo relacion.


```tikz
\usepackage{pgfplots}
\begin{document}

\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-5, xmax=5,
    ymin=-5, ymax=5,
    width=12cm,
    height=9cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-5,-4,...,5},
    ytick={-5,-4,...,5},
    clip=true
]

% Recta y=x
\addplot[
    domain=-5:5,
    dashed,
    gray,
    thick
]
{x};

% y=f^{-1}(x)=x^3+1
\addplot[
    domain=-1.8:1.6,
    samples=200,
    very thick,
    teal
]
{x^3+1};

% y=f(x)=\sqrt[3]{x-1}
\addplot[
    domain=-1.8:1.6,
    samples=200,
    very thick,
    orange
]
({x^3+1},{x});

\node[teal] at (axis cs:-2.2,1.2)
{$y=f^{-1}(x)$};

\node[orange] at (axis cs:2,-1.8)
{$y=f(x)$};

\node[gray] at (axis cs:4,3.2)
{$y=x$};

\end{axis}
\end{tikzpicture}

\end{document}
```

>Función identidad

---

### Función de 2do grado (parabólica)

$$y=f(x)=ax^{2}+bx+c \quad ; \quad a,b,c\in\mathbb{R}$$

$$D_f=\mathbb{R}$$

$$R_f=\text{según coeficientes } a,b,c$$



- para $a>0$


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};

% Parábola: y = a(x-h)² + k  con h=2, k=1, a=0.5
\draw[very thick, teal, smooth, samples=100, domain=-0.2:4.2]
    plot ({\x}, {0.5*(\x-2)^2 + 1});

% Vértice
\fill[teal] (2,1) circle (0.06);
\node[below right, font=\small] at (2,1) {$V(2,1)$};

% Líneas guía punteadas
\draw[dashed, gray] (2,0) -- (2,1);
\draw[dashed, gray] (0,1) -- (2,1);

% Etiquetas ejes
\node[below] at (2,0) {$2$};
\node[left]  at (0,1) {$1$};

% Etiquetas
\node[teal, right, font=\small] at (3.2,2.6) {$y=a(x-2)^2+1$};
\node[right, font=\small] at (0.3,0.3) {$a>0$};

\end{tikzpicture}
\end{document}
```

- para $a<0$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

% Parábola: y = a(x-h)² + k  con h=2, k=2.5, a=-0.5
\draw[very thick, teal, smooth, samples=100, domain=-0.5:4.5]
    plot ({\x}, {-0.5*(\x-2)^2 + 2.5});

% Vértice
\fill[teal] (2,2.5) circle (0.06);
\node[above right, font=\small] at (2,2.5) {$V(2,\,2.5)$};

% Líneas guía punteadas
\draw[dashed, gray] (2,0) -- (2,2.5);
\draw[dashed, gray] (0,2.5) -- (2,2.5);

% Etiquetas ejes
\node[below] at (2,0) {$2$};
\node[left]  at (0,2.5) {$2.5$};

% Etiquetas
\node[teal, right, font=\small] at (3.0,0.5) {$y=a(x-2)^2+2.5$};
\node[right, font=\small] at (0.3,3.5) {$a<0$};

\end{tikzpicture}
\end{document}
```

Se reconoce las graficas identificando

- Vértice $$V=(h,k)$$.
    
- Eje de simetría: $$x=h$$

También se observa:

- Parábola con (a>0) (abre hacia arriba).
- Parábola con (a<0) (abre hacia abajo).
- Transformación:
	$$y=ax^2+bx+c$$
	en
	$$y-k=a(x-h)^2$$
	(con el proceso de completar cuadrados).

---

#### Ejemplo
$$f(x)=1+6x-2x^2$$

Reordenando:
$$y=-2x^2+6x+1$$

Factorizando:
$$y=-2(x^2-3x)+1$$

Completando cuadrados:
$$y=-2\left(x^2-3x+\left(\frac32\right)^2\right)+1+2\left(\frac32\right)^2  
$$

$$y-\frac{11}{2}=-2\left(x-\frac32\right)^{2}$$

Forma de vértice:
$$y-k=a(x-h)^{2}$$

Por comparación:
$$a=-2,\qquad h=\frac32,\qquad k=\frac{11}{2}$$

Vértice:
$$V(h,k)=\left(\frac32,\frac{11}{2}\right)$$

Eje de simetría:
$$x=\frac32$$

Como (a<0), la parábola abre hacia abajo.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.6]

% Ejes
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,7) node[above] {$y$};

% Ticks eje x
\foreach \x in {-1,1,2,3}
    \draw (\x,0.05) -- (\x,-0.05) node[below, font=\small] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5,6}
    \draw (0.05,\y) -- (-0.05,\y) node[left, font=\small] {\y};

% Parábola: y = -2(x - 3/2)² + 11/2
\draw[very thick, teal, smooth, samples=150, domain=-0.45:3.45]
    plot ({\x}, {-2*(\x - 1.5)^2 + 5.5});

% Vértice V(3/2, 11/2)
\fill[teal] (1.5, 5.5) circle (0.07);
\node[above right, font=\small] at (1.5, 5.5) {$V\!\left(\frac{3}{2},\frac{11}{2}\right)$};

% Líneas guía punteadas al vértice
\draw[dashed, gray] (1.5, 0) -- (1.5, 5.5);
\draw[dashed, gray] (0, 5.5) -- (1.5, 5.5);

% Tick vértice eje x y y
\node[below, font=\small] at (1.5,-0.05) {$\frac{3}{2}$};
\node[left,  font=\small] at (-0.3, 5.5) {$\frac{11}{2}$};

% Raíces: x = 3/2 ± √(11/4) = 3/2 ± √11/2
% x₁ ≈ -0.158   x₂ ≈ 3.158
\fill[orange] (-0.158, 0) circle (0.07);
\fill[orange] ( 3.158, 0) circle (0.07);
\node[below right, orange, font=\small] at (-2, 1) {$\frac{3-\sqrt{11}}{2}$};
\node[below left,  orange, font=\small] at ( 5.158, 0) {$\frac{3+\sqrt{11}}{2}$};

% Intersección eje y: x=0 → y = -2(9/4)+11/2 = 7/2
\fill[purple] (0, 3.5) circle (0.07);
\node[right, purple, font=\small] at (-0.1, 3.5) {$\frac{7}{2}$};

% Etiqueta ecuación
\node[teal, font=\small] at (3.3, 1.5) {$y-\frac{11}{2}=-2\!\left(x-\frac{3}{2}\right)^{\!2}$};

\end{tikzpicture}
\end{document}
```


$$D_{f}=\mathbb{R}\quad ; \quad  R_{f}=\left]-\infty,\frac{11}{2}\right]$$

---

### Función potencial generalizada

$$y=f(x)=x^{n} \quad ; \quad n=2,3,4,5,\ldots$$

donde 
$$D_f=\mathbb{R}$$

$$
R_f=
\begin{cases}
\mathbb{R}^{+}\cup\{0\}, & \text{si } n \text{ es par} \\
\mathbb{R}, & \text{si } n \text{ es impar}
\end{cases}
$$

Ejemplo

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.8]

% Cuadrícula
%\draw[gray!25, thin, step=1] (-5,-5) grid (5,5);

% Ejes
\draw[->] (-5.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-5.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1,1,2,3,4,5}
   \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
%\foreach \y in {-5,-4,-3,-2,-1,1,2,3,4,5}
%   \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% n=2  y=x^2   dominio recortado para no salir de y=5 → |x|≤√5≈2.236
\draw[very thick, teal, smooth, samples=120, domain=-2.236:2.236]
    plot ({\x}, {\x*\x});

% n=3  y=x^3   |x|≤∛5≈1.71
\draw[very thick, orange, smooth, samples=120, domain=-1.71:1.71]
    plot ({\x}, {\x*\x*\x});

% n=4  y=x^4   |x|≤5^(1/4)≈1.495
\draw[very thick, violet, smooth, samples=120, domain=-1.495:1.495]
    plot ({\x}, {\x*\x*\x*\x});

% n=5  y=x^5   |x|≤5^(1/5)≈1.38
\draw[very thick, red!70!black, smooth, samples=120, domain=-1.38:1.38]
    plot ({\x}, {\x*\x*\x*\x*\x});

% Leyenda
\draw[very thick, teal]          (1.8, 4.8) -- (2.8, 4.8) node[right, font=\small] {$f(x)=x^2$};
\draw[very thick, orange]        (1.8, 4.1) -- (2.8, 4.1) node[right, font=\small] {$f(x)=x^3$};
\draw[very thick, violet]        (1.8, 3.4) -- (2.8, 3.4) node[right, font=\small] {$f(x)=x^4$};
\draw[very thick, red!70!black]  (1.8, 2.7) -- (2.8, 2.7) node[right, font=\small] {$f(x)=x^5$};

% Origen
\fill[black] (0,0) circle (0.07);

\end{tikzpicture}
\end{document}
```

---

### Función exponencial

$$
y=f(x)=a^x
$$

con:

$$
a>0,\qquad a\neq 1
$$

$$
D_f=\mathbb{R}
$$

$$
R_f=\mathbb{R}^{+}
$$

- a>0

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Cuadrícula
%\draw[gray!25, thin, step=1] (-5,-1) grid (5,5);

% Ejes
\draw[->] (-5.3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% Asíntota horizontal y=0
\draw[dashed, gray!60, thin] (-5.3,0) -- (5.3,0);

% a=2  y=2^x
% y=5 → x=log2(5)≈2.322   y=-1 → x=log2(-1) no existe, x→-∞ asíntota
\draw[very thick, teal, smooth, samples=150, domain=-5:2.322]
    plot ({\x}, {2^\x});

% a=3  y=3^x
% y=5 → x=log3(5)≈1.465
\draw[very thick, orange, smooth, samples=150, domain=-5:1.465]
    plot ({\x}, {3^\x});

% a=5  y=5^x
% y=5 → x=1
\draw[very thick, violet, smooth, samples=150, domain=-5:1]
    plot ({\x}, {5^\x});

% a=10  y=10^x
% y=5 → x=log10(5)≈0.699
\draw[very thick, red!70!black, smooth, samples=150, domain=-5:0.699]
    plot ({\x}, {10^\x});

% Punto común (0,1) para todas
\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (0,1) {$(0,1)$};




% Leyenda
\draw[very thick, teal]         (-4.8, 4.8) -- (-3.8, 4.8) node[right, font=\small] {$y=2^x$};
\draw[very thick, orange]       (-4.8, 4.1) -- (-3.8, 4.1) node[right, font=\small] {$y=3^x$};
\draw[very thick, violet]       (-4.8, 3.4) -- (-3.8, 3.4) node[right, font=\small] {$y=5^x$};
\draw[very thick, red!70!black] (-4.8, 2.7) -- (-3.8, 2.7) node[right, font=\small] {$y=10^x$};

% Etiqueta asíntota
\node[gray, font=\small] at (3.5,-0.6) {asíntota $y=0$};

\end{tikzpicture}
\end{document}
```


- 0<a<1

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};

% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% Asíntota horizontal y=0
\draw[dashed, gray!60, thin] (-3,0) -- (5.3,0);

% a=1/2  y=(1/2)^x
% y=5 → x=log_{1/2}(5)=-log2(5)≈-2.322
\draw[very thick, teal, smooth, samples=150, domain=-2.322:5]
    plot ({\x}, {(0.5)^\x});

% a=1/3  y=(1/3)^x
% y=5 → x=-log3(5)≈-1.465
\draw[very thick, orange, smooth, samples=150, domain=-1.465:5]
    plot ({\x}, {(0.333)^\x});

% a=1/5  y=(1/5)^x
% y=5 → x=-1
\draw[very thick, violet, smooth, samples=150, domain=-1:5]
    plot ({\x}, {(0.2)^\x});

% a=1/10  y=(1/10)^x
% y=5 → x=-log10(5)≈-0.699
\draw[very thick, red!70!black, smooth, samples=150, domain=-0.699:5]
    plot ({\x}, {(0.1)^\x});

% Punto común (0,1)
\fill[black] (0,1) circle (0.07);
\node[below left, font=\small] at (0,1) {$(0,1)$};

% Leyenda
\draw[very thick, teal]         (2.5, 4.8) -- (3.5, 4.8) node[right, font=\small] {$y=\left(\frac{1}{2}\right)^x$};
\draw[very thick, orange]       (2.5, 4.1) -- (3.5, 4.1) node[right, font=\small] {$y=\left(\frac{1}{3}\right)^x$};
\draw[very thick, violet]       (2.5, 3.4) -- (3.5, 3.4) node[right, font=\small] {$y=\left(\frac{1}{5}\right)^x$};
\draw[very thick, red!70!black] (2.5, 2.7) -- (3.5, 2.7) node[right, font=\small] {$y=\left(\frac{1}{10}\right)^x$};

% Etiqueta asíntota
\node[gray, font=\small] at (-1.5,-0.6) {asíntota $y=0$};

\end{tikzpicture}
\end{document}
```

en general  $$a=\dfrac{1}{b}$$


$$f(x)=a^{x} = \left( \frac{1}{b}\right)^{x}= b^{-x} \quad ;\quad b>1$$

- Caso particular
$$a= e = 2,718281\dots \quad = \text{número de nepper}$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9]
% Ejes
\draw[->] (-5.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,5.3) node[above] {$y$};
% Ticks eje x
\foreach \x in {-5,-4,-3,-2,-1,1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};
% Ticks eje y
\foreach \y in {1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};
% f(x)=e^x
\draw[very thick, teal, smooth, samples=150, domain=-5:1.609]
    plot ({\x}, {exp(\x)});
% Tangente en (0,1): y = x + 1  →  pasa por (0,1) con pendiente 1
\draw[dashed, gray, thick] (-2.3,-1.3) -- (4,5);
\node[gray, font=\small] at (4.2,5.0) {$\frac{\pi}{4}$};
% Punto (0,1)
\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (-1,1.7) {$(0,1)$};
% Leyenda
\draw[very thick, teal] (-4.8,4.8) -- (-3.8,4.8)
    node[right, font=\small] {$f(x)=e^x$};


\fill[black] (0,1) circle (0.07);
\node[below right, font=\small] at (-0.5,0.7) {$\alpha = 45^{\circ}$};

% Ángulo alfa
\draw (-0.5,0) arc[start angle=0,end angle=37,radius=0.6];
    
\end{tikzpicture}
\end{document}
```

----

#### Propiedades de las potencias
1. **Producto de potencias de igual base**
	- $a^m \cdot a^n = a^{m+n}$
2. **Cociente de potencias de igual base**
	- $\dfrac{a^m}{a^n}=a^{m-n}$
3. **Igualdad de potencias de igual base**
	- Si $a^b=a^c$, entonces $b=c$
4. **Potencia de una potencia**
	- $(a^b)^c=a^{bc}$
5. **Potencia de una potencia**
	- $a^{(b^c)}=a^{b^c}$
6. **Potencia de un producto**
	- $(ab)^n=a^n b^n$
7. **Potencia de un cociente**
	- $\left(\dfrac{a}{b}\right)^n=\dfrac{a^n}{b^n}$
8. **Exponente cero**
	- $a^0=1\quad, \quad a\neq0$
9. **Exponente negativo**
	- $a^{-n}=\dfrac{1}{a^n}$
10. **Exponente uno**
	- $a^1=a$

---

### Funciones logarítmicas 

- Se define "$\log$" segun:
$$\log_{b}{a} = c\quad \Rightarrow \quad b^{c}=a$$

- Como fúncion
$$y=f(x)=\log_{a}{x} \quad ; \quad a>0 , \quad y\neq 0$$

$$D_{f}=\mathbb{R}^{+} \quad ; \quad R_{f}=\mathbb{R}$$

- $a>1$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-1.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-3.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x
\foreach \x in {1,2,3,4,5}
    \draw (\x,0.07) -- (\x,-0.07) node[below, font=\tiny] {\x};
\draw (-1,0.07) -- (-1,-0.07) node[below, font=\tiny] {$-1$};

% Ticks eje y
\foreach \y in {-3,-2,-1,1,2,3,4,5}
    \draw (0.07,\y) -- (-0.07,\y) node[left, font=\tiny] {\y};

% f(x) = log_2(x)
\draw[very thick, teal, smooth, samples=200, domain=0.03:5]
    plot ({\x}, {ln(\x)/ln(2)});

% Asíntota vertical x=0 (referencia punteada)
\draw[dotted, gray!60] (0,-3.2) -- (0,5.2);

% Tangente en (1,0): derivada de log_2(x) es 1/(x*ln2), en x=1 es 1/ln(2)≈1.4427
% y - 0 = (1/ln2)(x - 1)  →  y = (x-1)/ln(2)
\draw[dashed, gray, thick, domain=-0.5:3.6]
    plot ({\x}, {(\x - 1)/ln(2)});

% Punto (1,0)
\fill[black] (1,0) circle (0.07);
\node[above right, font=\small] at (1,0) {$(1,0)$};

% Ángulo alfa en el origen de la tangente
\draw (1.55,0) arc[start angle=0,end angle=55,radius=0.55];
\node[font=\scriptsize] at (1.8,0.3) {$\alpha$};

% Etiqueta ángulo en grados aproximado
\node[below right, font=\small] at (2.5,0.4) {$\approx 55.3^\circ$};

% Leyenda
\draw[very thick, teal] (-0.8,4.8) -- (0.2,4.8)
    node[right, font=\small] {$f(x)=\log_2 x$};

% Asíntota label
\node[gray, font=\tiny] at (-0.45,-2.5) {$x=0$};

\end{tikzpicture}
\end{document}
```

- $0>a>1$


```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9]

% Ejes
\draw[->] (-1.3,0) -- (5.3,0) node[right] {$x$};
\draw[->] (0,-3.3) -- (0,5.3) node[above] {$y$};

% Ticks eje x manualmente
\draw (1,0.07) -- (1,-0.07) node[below, font=\tiny] {$1$};
\draw (2,0.07) -- (2,-0.07) node[below, font=\tiny] {$2$};
\draw (3,0.07) -- (3,-0.07) node[below, font=\tiny] {$3$};
\draw (4,0.07) -- (4,-0.07) node[below, font=\tiny] {$4$};
\draw (5,0.07) -- (5,-0.07) node[below, font=\tiny] {$5$};

% Ticks eje y manualmente
\draw (0.07,1) -- (-0.07,1) node[left, font=\tiny] {$1$};
\draw (0.07,2) -- (-0.07,2) node[left, font=\tiny] {$2$};
\draw (0.07,3) -- (-0.07,3) node[left, font=\tiny] {$3$};
\draw (0.07,-1) -- (-0.07,-1) node[left, font=\tiny] {$-1$};
\draw (0.07,-2) -- (-0.07,-2) node[left, font=\tiny] {$-2$};
\draw (0.07,-3) -- (-0.07,-3) node[left, font=\tiny] {$-3$};

% f(x) = log_{1/2}(x) aproximada con puntos clave unidos
% log_{1/2}(x) = -log_2(x)
% Valores: (0.125, 3), (0.25, 2), (0.5, 1), (1, 0), (2,-1), (4,-2)
\draw[very thick, teal, smooth]
    (0.06,4.06) ..controls (0.1,3.5) and (0.2,2.5)..
    (0.25,2) ..controls (0.35,1.4) and (0.45,0.8)..
    (0.5,1) ..controls (0.7,0.4) and (0.85,0.1)..
    (1,0) ..controls (1.5,-0.6) and (1.8,-0.9)..
    (2,-1) ..controls (2.8,-1.4) and (3.5,-1.8)..
    (4,-2) ..controls (4.5,-2.2) and (4.9,-2.4)..
    (5,-2.32);

% Asintota vertical punteada
\draw[dotted, gray] (0,-3.2) -- (0,5.2);

% Tangente en (1,0): pendiente = -1/ln(2) ≈ -1.4427
% y = -1.4427*(x-1)
% en x=0: y=1.4427, en x=3: y=-2.885 (fuera), usamos x in [0, 2.8]
\draw[dashed, gray, thick] (0, 1.44) -- (2.8, -2.6);

% Punto (1,0)
\fill[black] (1,0) circle (0.07);
\node[above right, font=\small] at (1,0) {$(1,0)$};

% Puntos de referencia
\fill[black] (2,-1) circle (0.05);
\node[right, font=\tiny] at (2.05,-1) {$(2,-1)$};
\fill[black] (4,-2) circle (0.05);
\node[right, font=\tiny] at (4.05,-2) {$(4,-2)$};
\fill[black] (0.5,1) circle (0.05);
\node[right, font=\tiny] at (0.55,1) {$(1/2,1)$};

% Angulo en (1,0)
\draw (1.45,0) arc[start angle=0, end angle=125, radius=0.45];
\node[font=\scriptsize] at (0.75,0.38) {$\alpha$};

% Leyenda
\draw[very thick, teal] (0.2,4.8) -- (1.0,4.8);
\node[right, font=\small] at (1.05,4.8) {$f(x)=\log_{1/2} x$};

\end{tikzpicture}
\end{document}
```

- Casos especiales

$$a=10 \Rightarrow f(x)=\log_{10}{x}= \log x = \text{logatirmo decimal}$$

$$a=e \Rightarrow f(x)=\log_{e}{x}= \ln x = \text{logaritmo  natural , neperiano}$$

#### Propiedades de los logaritmos

1. **Logaritmo de un producto**
   * $\log_a(mn) = \log_a m + \log_a n$

2. **Logaritmo de un cociente**
   * $\log_a\left(\dfrac{m}{n}\right) = \log_a m - \log_a n$

3. **Logaritmo de una potencia**
   * $\log_a(m^n) = n\log_a m$

4. **Logaritmo de una raíz**
   * $\log_a\left(\sqrt[n]{m}\right) = \dfrac{\log_a m}{n}$

5. **Logaritmo de la base**
   * $\log_a a = 1$

6. **Logaritmo de la unidad**
   * $\log_a 1 = 0 \quad,\quad a \neq 1,\ a > 0$

7. **Igualdad de logaritmos**
   * Si $\log_a m = \log_a n$, entonces $m = n$

8. **Cambio de base**
   * $\log_a m = \dfrac{\log_b m}{\log_b a}$

9. **Logaritmo recíproco**
   * $\log_a b = \dfrac{1}{\log_b a}$

10. **Potenciación logarítmica**
    * $a^{\log_a m} = m$

11. **Logaritmo natural y decimal**
    * $\ln m = \log_e m \qquad \log m = \log_{10} m$

---

#### Ejercicio 1
Evaluación de $f(x) = \ln(x)$

**$x = 1$**
$$f(1) = \ln(1) = 0$$

**$x = e$**
$$f(e) = \ln(e) = 1$$

**$x \to +\infty$**
$$\lim_{x \to +\infty} \ln(x) = +\infty$$

>A medida que $x$ crece, necesitamos exponentes $n$ cada vez más grandes

**$x \to 0^+$**
$$\lim_{x \to 0^+} \ln(x) = -\infty$$

> $x = 0$ no pertenece al dominio de $\ln(x)$, ya que el logaritmo solo está definido para $x > 0$.  
> Por eso se analiza el límite cuando $x$ se acerca a $0$ por la derecha.



#### Ejercicio 2
Inversa de $f(x) = \ln x$

$$y = \ln x$$
$$x = \ln y^{-1} \implies e^x = y$$

$$\boxed{f^{-1}(x) = e^x}$$

---

#### Ejercicio 3

Composición $f(x) = \ln x$ y $f^{-1}(x) = e^x$

$$(f \circ f^{-1})(x) = f(f^{-1}(x)) = \ln(e^x) = x$$

$$\boxed{(f \circ f^{-1})(x) = x}$$

---

## Funciones trigonométricas

Se definen en la circunferencia trigonométrica.








```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2]

% Ejes
\draw[->] (-1.2,0) -- (2.1,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,1.4) node[above] {$y$};

% Semicircunferencia superior punteada
\draw[thick, dashed,teal] (1,0) arc (0:180:1);

% Recta L desde el origen (angulo 30 grados)
% pasa por P=(cos30,sin30), R=(1, tan30), M=(cot30, 1)
% tan(30)=1/sqrt(3) ~ 0.5774, cot(30)=sqrt(3) ~ 1.7321
\draw[thick, orange ] (0,0) -- (1.85,1.069);

% Recta tangente horizontal en N=(0,1)
\draw[thick,dashed] (-1.1,1) -- (1.85,1);

% Recta tangente vertical en T=(1,0)
\draw[thick,dashed] (1,-0.5) -- (1,1.3);

% Punto P = (cos30, sin30) = (0.866, 0.5)
\fill (0.866,0.5) circle (0.03);
\node[above left, font=\small] at (0.866,0.5) {$P$};

% Punto N = (0,1)
\fill (0,1) circle (0.03);
\node[left, font=\small] at (0.3,1.1) {$N$};

% Punto M = (sqrt(3), 1) ~ (1.7321, 1)
\fill (1.7321,1) circle (0.03);
\node[above, font=\small] at (1.7321,1) {$M$};

% Punto T = (1,0)
\fill (1,0) circle (0.03);
\node[below, font=\small] at (0.85,0) {$T$};

% Punto R = (1, tan30) = (1, 0.5774)
\fill (1,0.5774) circle (0.03);
\node[right, font=\small] at (1,0.5774) {$R$};

% Origen
\node[below left, font=\small] at (0,0) {$O$};

% Angulo 30 grados en el origen
\draw (0.25,0) arc (0:30:0.25);
\node[font=\small] at (0.36,0.08) {$x$};

% Labels de tangentes
\node[above, font=\small] at (-0.9,1) {Tangente en $N$};
\node[right, font=\small] at (1.1,-0.4) {Tangente en $T$};

% Labels lado derecho (+) 0 y (-) 360
\node[right, font=\small] at (1.05,0.05) {$(+)\ 0^\circ$};
\node[right, font=\small] at (1.05,-0.12) {$(-)\ 360^\circ$};

% Segmentos de referencia punteados
\draw[dotted] (0.866,0) -- (0.866,0.5);
\draw[dotted] (0,0.5) -- (0.866,0.5);

% Tick en x=1
\draw (1,0.04) -- (1,-0.04) node[below, font=\tiny] {$1$};

% Tick en y=1
\draw (0.04,1) -- (-0.04,1);

\end{tikzpicture}
\end{document}
```



Donde:

| $\sin{x}=\overline{PQ}$ | $\tan{x}=\overline{RT}$ | $\sec{x}=\overline{OR}$ |
| ----------------------- | ----------------------- | ----------------------- |
| $\cos{x}=\overline{OQ}$ | $\cot{x}=\overline{MN}$ | $\csc{x}=\overline{OM}$ |

>Solo se miden ángulos redianes
>$$1^{\circ}=\frac{\pi}{180^{\circ}}[rad]$$

Por ejemplo

$$30^{\circ}=\frac{\pi}{180^{\circ}}\times 30^{\circ}=\frac{\pi}{6}$$

$$45^{\circ}=\frac{\pi}{180^{\circ}}\times 45^{\circ}=\frac{\pi}{4}$$

$$90^{\circ}=\frac{\pi}{180^{\circ}}\times 90^{\circ}=\frac{\pi}{2}$$

$$120^{\circ}=\frac{\pi}{180^{\circ}}\times 120^{\circ}=\frac{2\pi}{3}$$

$$\vdots$$

Además

$$\sin\frac{\pi}{6} = \frac{1}{2}\quad ; \quad \cos \frac{\pi}{6}=\frac{\sqrt{3}}{2} \quad ; \quad \sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}=\frac{1}{\sqrt{2}}$$
$$\vdots$$

---

### Función seno

$$y=f(x)=\sin{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}=[-1,1]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-1.2, ymax=1.2,
    width=12cm,
    height=6cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Funcion
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{sin(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=1pt] (axis cs:-3, 1) -- (axis cs:13, 1);
\draw[dashed, gray, line width=1pt] (axis cs:-3, -1) -- (axis cs:13, -1);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:0, 0) circle (2pt)node[above right] {$0$};
\fill[orange] (axis cs:3.14, 0) circle (2pt)node[above right] {$\pi$};
\fill[orange] (axis cs:6.28, 0) circle (2pt)node[above right] {$2\pi$};
\fill[orange] (axis cs:9.42, 0) circle (2pt)node[above right] {$3\pi$};


\end{axis}
\end{tikzpicture}
\end{document}
```

>$f(x)=\sin x$ es periódico con $p=2\pi$ y es impar $\sin{-x}=-\sin{x}$

---

### Función coseno

$$y=f(x)=\cos{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}=[-1,1]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-1.2, ymax=1.2,
    width=12cm,
    height=6cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Funcion
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{cos(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=1pt] (axis cs:-3, 1) -- (axis cs:13, 1);
\draw[dashed, gray, line width=1pt] (axis cs:-3, -1) -- (axis cs:13, -1);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:1.57, 0) circle (2pt)node[above right] {$\frac{\pi}{2}$};
\fill[orange] (axis cs:4.71, 0) circle (2pt)node[above right] {$\frac{3\pi}{2}$};
\fill[orange] (axis cs:7.85, 0) circle (2pt)node[above right] {$\frac{5\pi}{2}$};
\fill[orange] (axis cs:10.99, 0) circle (2pt)node[above right] {$\frac{7\pi}{2}$};


\end{axis}
\end{tikzpicture}
\end{document}
```

>$f(x)=\cos x$ es periódico con $p=2\pi$ y es par $\cos{-x}=\cos{x}$

---

### Función tangente

$$y=f(x)=\tan{x}=\dfrac{\sin x}{\cos x}$$

$$D_{f}=\mathbb{R} \quad \rightarrow \{ \; x / x = (2k+1)\frac{\pi}{2}\quad,\quad k\in \mathbb{Z} \; \}$$

$$R_{f}=\mathbb{R}$$

>$f(x)=\tan x$ es periódico con $p=2\pi$ y es impar $\tan{-x}=-\tan{x}$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-3, xmax=13,
    ymin=-4, ymax=4,
    width=12cm,
    height=6cm,
    xlabel={$x$},
    ylabel={$y$},
    xtick=\empty,
    ytick={-1,0,1}
]

% Curva tangente
\addplot[
    very thick,
    teal,
    domain=-4:12.56,
    samples=200
]
{tan(deg(x))};

% Asintotas verticales - gruesas para tapar la linea falsa
\draw[dashed, gray, line width=3pt] (axis cs:-1.57, -4) -- (axis cs:-1.57, 4);

\draw[dashed, gray, line width=3pt] (axis cs:1.57, -4) -- (axis cs:1.57, 4);
\draw[dashed, gray, line width=3pt] (axis cs:4.71, -4) -- (axis cs:4.71, 4);
\draw[dashed, gray, line width=3pt] (axis cs:7.85, -4) -- (axis cs:7.85, 4);
\draw[dashed, gray, line width=3pt] (axis cs:10.99, -4) -- (axis cs:10.99, 4);

% Puntos donde tan(x)=0
\fill[orange] (axis cs:0, 0) circle (2pt)node[above right] {$0$};
\fill[orange] (axis cs:3.14, 0) circle (2pt)node[above right] {$\pi$};
\fill[orange] (axis cs:6.28, 0) circle (2pt)node[above right] {$2\pi$};
\fill[orange] (axis cs:9.42, 0) circle (2pt)node[above right] {$3\pi$};


\end{axis}
\end{tikzpicture}
\end{document}
```



- además

$$f(x)=\cot{x}=\frac{1}{\tan x} = \frac{\cos x}{\sin x}$$

$$f(x)=\sec{x}=\frac{1}{\cos x} $$

$$f(x)=\csc{x}=\frac{1}{\sin x} $$

>- también  $$\sin^{2}{x}+\cos^{2}{x}=1\quad ; \quad \forall x\in \mathbb{R}$$
>Identidad fundamental

---

### Funciones trigonométricas inversas 


Se definen los elementos inversos según:
$$\arcsin{u}=v \quad \Rightarrow \quad u=\sin{v}$$
$$\arccos{u}=v \quad \Rightarrow \quad u=\cos{v}$$
$$\arctan{u}=v \quad \Rightarrow \quad u=\tan{v}$$
$$\text{arcotg }{u}=v \quad \Rightarrow \quad u=\cot v$$
$$\text{arcsec }{u}=v \quad \Rightarrow \quad u=\sec{v}$$
$$\text{arcosec }{u}=v \quad \Rightarrow \quad u=\csc v$$

- por ejemplo:

$$\arcsin{1}=\frac{\pi}{2}$$
$$\arctan{1}=\frac{\pi}{4}$$
$$\arccos{0}=\frac{\pi}{2}$$
$$\arcsin{\frac{\sqrt{3}}{2}}=\frac{\pi}{3}$$
$$\arctan \infty =\frac{\pi}{2}$$
$$\vdots$$


#### Funcion $\arcsin$

$$y=f(x)=\arcsin{x}$$

$$D_{f}=[-1,1] \quad ; \quad R_{f}=\Big [-\frac{\pi}{2},\frac{\pi}{2}\Big ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-2, xmax=2,
    ymin=-2, ymax=2,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={-1,0,1}
]

% Funcion seno
\addplot[
    dashed,
    very thick,
    teal,
    domain=-4:4,
    samples=200
]{sin(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-4, -4) -- (axis cs:4, 4);

% Funcion arcoseno
\addplot[
    very thick,
    orange,
    domain=-1:1,
    samples=200
]{asin(x)/180*pi};

% Puntos clave arcoseno
\fill[orange] (axis cs:-1, -1.5708) circle (2pt) node[left] {$(-1,-\frac{\pi}{2})$};
\fill[orange] (axis cs:0, 0)        circle (2pt) node[above right] {$(0,0)$};
\fill[orange] (axis cs:1,  1.5708)  circle (2pt) node[right] {$(1,\frac{\pi}{2})$};
%asintotas
%||
\draw[dashed, gray, line width=1pt] (axis cs:1, -2) -- (axis cs:1, 2);
\draw[dashed, gray, line width=1pt] (axis cs:-1, -2) -- (axis cs:-1, 2);
%--
\draw[dashed, gray, line width=1pt] (axis cs:-2, -1.57) -- (axis cs:2, -1.57);
\draw[dashed, gray, line width=1pt] (axis cs:-2, 1.57) -- (axis cs:2, 1.57);

\end{axis}
\end{tikzpicture}
\end{document}
```


---


#### Funcion $\arccos$

$$y=f(x)=\arccos{x}$$

$$D_{f}=[-1,1] \quad ; \quad R_{f}= [0 ,\pi ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-2.5, xmax=3,
    ymin=-2, ymax=4,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={0,1,2,3}
]

% Funcion coseno rama principal [0,pi]
\addplot[
    dashed,
    very thick,
    teal,
    domain=0:3.14,
    samples=100
]{cos(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-2, -2) -- (axis cs:4, 4);

% Funcion arcocoseno
\addplot[
    very thick,
    orange,
    domain=-1:1,
    samples=200
]{acos(x)/180*pi};

% Puntos clave arcocoseno
\fill[orange] (axis cs:-1, 3.1416) circle (2pt) node[left] {$(-1,\pi)$};
\fill[orange] (axis cs:0, 1.5708)  circle (2pt) node[above right] {$(0,\frac{\pi}{2})$};
\fill[orange] (axis cs:1, 0)       circle (2pt) node[below right] {$(1,0)$};

% Lineas de referencia ||
\draw[dashed, gray, line width=1pt] (axis cs:1, -2) -- (axis cs:1, 4);
\draw[dashed, gray, line width=1pt] (axis cs:-1, -2) -- (axis cs:-1, 4);
% Lineas de referencia --
\draw[dashed, gray, line width=1pt] (axis cs:-2, 3.14) -- (axis cs:4, 3.14);
\draw[dashed, gray, line width=1pt] (axis cs:-2, 0) -- (axis cs:4, 0);

\end{axis}
\end{tikzpicture}
\end{document}
```



---


#### Funcion $\arctan$

$$y=f(x)=\arctan{x}$$

$$D_{f}=\mathbb{R} \quad ; \quad R_{f}= \Big [ -\frac{\pi}{2},\frac{\pi}{2} \Big ]$$

Grafica :

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4, xmax=4,
    ymin=-4, ymax=4,
    xlabel={$x$},
    ylabel={$y$},
    xtick={-1,0,1},
    ytick={-1,0,1}
]

% Tangente rama principal (-pi/2, pi/2)
\addplot[
    dashed,
    very thick,
    teal,
    domain=-1.47:1.47,
    samples=100
]{tan(deg(x))};

% Linea espejo y=x
\draw[dashed, gray, line width=1pt] (axis cs:-4, -4) -- (axis cs:4, 4);

% Arcotangente domain todos los reales
\addplot[
    very thick,
    orange,
    domain=-4:4,
    samples=200
]{atan(x)/180*pi};

% Puntos clave arctan
\fill[orange] (axis cs:-1, -0.7854) circle (2pt) node[below left] {$(-1,-\frac{\pi}{4})$};
\fill[orange] (axis cs:0, 0)        circle (2pt) node[above right] {$(0,0)$};
\fill[orange] (axis cs:1, 0.7854)   circle (2pt) node[above left] {$(1,\frac{\pi}{4})$};

% Asintotas horizontales de arctan en y=+-pi/2
\draw[dashed, gray, line width=1pt] (axis cs:-4,  1.5708) -- (axis cs:4,  1.5708);
\draw[dashed, gray, line width=1pt] (axis cs:-4, -1.5708) -- (axis cs:4, -1.5708);

% Asintotas verticales de tan en x=+-pi/2
\draw[dashed, gray, line width=1pt] (axis cs: 1.5708, -4) -- (axis cs: 1.5708, 4);
\draw[dashed, gray, line width=1pt] (axis cs:-1.5708, -4) -- (axis cs:-1.5708, 4);

\end{axis}
\end{tikzpicture}
\end{document}
```

--

### Funciones Hiperbólicas

Se definen en términos de $e^{x}$ según:





