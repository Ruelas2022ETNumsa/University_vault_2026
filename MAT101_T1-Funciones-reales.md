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
### Gráfico de intervalos (Cs₁)

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

### Gráfico de intervalos (Cs₂)

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

## Función par

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
$$(f\circ g)(x)$$

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
\draw[->, thick]
(x) .. controls (-2.0,0.8) and (-1.2,0.8) .. (gx);

\node at (-1.75,1.05) {$g$};

% Flecha f
\draw[->, thick]
(gx) .. controls (1.2,0.8) and (2.0,0.8) .. (fgx);

\node at (1.75,1.05) {$f$};

\end{tikzpicture}
\end{document}
```




---




Siguiendo tu indicación, el **Cap. I – Funciones reales** comienza en la mitad derecha de la página 1. Revisando las primeras páginas del capítulo, los títulos y subtítulos que se distinguen son:

- Cap. I
    
    - Funciones reales
        
        - Definición de función
            
        - Notación
            
        - Álgebra de funciones
            
        - Función par
            
        - Función impar
            
        - Función periódica
            
        - Función inversa
            

Además, dentro de **Álgebra de funciones** aparecen los subtemas:

- Álgebra de funciones
    
    - Suma de funciones
        
    - Producto de funciones
        
    - Cociente de funciones
        
    - Dominio de una función
        
        - Funciones racionales
            
        - Funciones radicales
            
        - Funciones logarítmicas
            
        - Funciones exponenciales
            
        - Funciones trigonométricas inversas
            

Si quieres, puedo continuar revisando las páginas restantes del PDF y extraer la **estructura completa del capítulo** en formato jerárquico antes de hacer cualquier transcripción.
