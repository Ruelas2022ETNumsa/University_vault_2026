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
$$R_{f={5}}= \text{imagen o rango}$$
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

## Álgebra de funciones

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
> No es impar porque no cumple $f(-x)=-f(x)$. El 4 añadido impide la condición

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

- para $a$

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





--



---










También se observa:

- Parábola con (a>0) (abre hacia arriba).
    
- Parábola con (a<0) (abre hacia abajo).
    
- Vértice (V=(h,k)).
    
- Eje de simetría:
    

$$  
x=h  
$$

- Transformación:
    

$$  
y=ax^2+bx+c  
$$

en

$$  
y-k=a(x-h)^2  
$$

(con el proceso de completar cuadrados).

Y el ejemplo parece ser:

```markdown
**Ej. Gráfica**

$$
f(x)=1+6x-2x^2
$$
```

pero para el desarrollo completo y los recorridos que aparecen en las gráficas prefiero no inventar nada.

¿Podrías subir un recorte más cercano de la mitad izquierda de la página (solo la sección de la parábola)? Con un zoom de aproximadamente el doble podré transcribirla completa, incluyendo:

- el ejemplo de completar cuadrados,
    
- el vértice,
    
- el recorrido,
    
- y reproducir las dos parábolas con código Desmos/TikZ según corresponda.

