# Números reales y desigualdades
## Axiomas de cuerpo de la de los números reales
Si a, b, c ∈ $\mathbb{R}$

1. Clausura
	- $a+b \in \mathbb{R}$
	- $a \cdot b \in \mathbb{R}$
2. Conmutatividad 
	- $a+b=b+a$
	- $a\cdot b=b\cdot a$
3. Asociatividad
	- $(a+b)+c=a+(b+c)$
	- $(a\cdot b)\cdot c=a\cdot(b\cdot c)$
4. ∃ de neutros
	- ∃ 0∈ $\mathbb{R}$  $\rightsquigarrow$ a+0 = a
		→ 0 neutro para "+"
	* ∃ 1 ∈ $\mathbb{R}$ $\rightsquigarrow$ a·1 = a
		→ I neutro para "×"
5. ∃ de negativos
∀a ∈ $\mathbb{R}$ ∃-a ∈ $\mathbb{R}$  $\rightsquigarrow$ a+(-a)=0
 -a = negativo de a
A6) ∃ de inversos
∀a ∈ $\mathbb{R}$ - {0} ∃ $a^{-1}$ ∈ $\mathbb{R}$ $a \cdot a^{-1}=1$
a^{-1} = $\frac{1}{a}$ immero de a
A7) Distribución
a (b+c) = ab+ac
Ocio mas de igualdad.
- ci a, b, c ∈ IR
A1) Reflexión a = a
A2) simetría a = b => b = a


A3) Transmisión
$(a = b \wedge b = c) \Rightarrow a = c$

Mód. Resta y división con sólo casos
especiados de "x" y "y"

- Recala $a - b = a + (-b)$
- División $\frac{a}{b} = a - \frac{1}{b} = a - b^{-1}, b \neq 0$
- Mo configuración
$2^8 = 8$ siguidad → verdad evidente
$x^4 - 4 = 0 \Rightarrow$ equación → verdad para
algunos $x$
$x^2 - 4 = (x - 2)(x + 2)$ identidad →
verdad para todo $x \in \mathbb{R}$

Theorem sobre $n \div x$ scale
$x: a, b, c, d, x \in \mathbb{R}$
1) $a + b = a + c \Rightarrow b - c$
2) $(a + b = a \cdot c) \wedge a \neq 0 \Rightarrow b = c$
3) $a + x = b \rightarrow x = b - a$
4) $(a \cdot x = b \wedge a \neq 0) \Rightarrow x = b/a$
5) $a \cdot 0 = 0$
6) $a \cdot b = 0 \Rightarrow (a = 0 \vee b = 0)$
7) $a = b \Rightarrow -a > -b$
8) $a (-b) = -a b$
9) $(-a)(-b) = ab$
10) $\frac{a}{b} + \frac{c}{b} = \frac{a + c}{b}$


1.lkhj
1) 

$$
\begin{aligned}
\|\mathbf{x}\times\mathbf{y}\|^2
&=
(x_2y_3-x_3y_2)^2
+(x_3y_1-x_1y_3)^2
+(x_1y_2-x_2y_1)^2 \\
&=
x_2^2y_3^2
-2x_2x_3y_2y_3
+x_3^2y_2^2
+x_3^2y_1^2
-2x_1x_3y_1y_3 \\
&\qquad
+x_1^2y_3^2
+x_1^2y_2^2
-2x_1x_2y_1y_2
+x_2^2y_1^2 \\
&=
(x_1^2+x_2^2+x_3^2)
(y_1^2+y_2^2+y_3^2)
-(x_1y_1+x_2y_2+x_3y_3)^2 \\
&=
\|\mathbf{x}\|^2\|\mathbf{y}\|^2
-(\mathbf{x}\cdot\mathbf{y})^2 \\
&=
\|\mathbf{x}\|^2\|\mathbf{y}\|^2
-\|\mathbf{x}\|^2\|\mathbf{y}\|^2\cos^2\theta \\
&=
\|\mathbf{x}\|^2\|\mathbf{y}\|^2\sin^2\theta.
\end{aligned}$$


```tikz
\begin{document}
\begin{tikzpicture}

% Ejes
\draw[->] (-2,0) -- (2.5,0) node[right] {$y$};
\draw[->] (0,-2) -- (0,2.5) node[above] {$z$};

% Cilindro
\draw (-1,1) arc(180:360:1 and 0.4);
\draw (-1,-1) arc(180:360:1 and 0.4);

\draw (-1,1) -- (-1,-1);
\draw (1,1) -- (1,-1);

\draw[dashed] (-1,-1) arc(180:360:1 and 0.4);
\draw (1,1) arc(0:180:1 and 0.4);

\node at (0.5,1.3) {$r_0$};

\end{tikzpicture}
\end{document}
```



```tikz
\usepackage{tikz-3dplot}

\begin{document}

\tdplotsetmaincoords{70}{120}

\begin{tikzpicture}[tdplot_main_coords,scale=0.7]

\filldraw[fill=red!20]
(-4,-4,4) --
(4,-4,4) --
(4,5,4) --
(-4,5,4) -- cycle;

\filldraw[fill=blue!20]
(0,0,4) --
(5.2,6,4) --
(5.2,6,0) --
(0,0,0) -- cycle;

\draw[->] (0,0,0) -- (6,0,0) node[right] {$x$};
\draw[->] (0,0,0) -- (0,6,0) node[left] {$y$};
\draw[->] (0,0,0) -- (0,0,6) node[above] {$z$};

\draw (0,0,0) circle (3);
\draw (0,0,4) circle (3);

\draw (1.9,-2.35,0) -- (1.9,-2.35,4);
\draw (-1.9,2.35,0) -- (-1.9,2.35,4);

\fill (2,2.25,4) circle (2pt);

\node at (2.5,1,4.3)
{$P_1(r_1,\phi_1,z_1)$};

\draw[->] (2,2.25,4) -- (3,3.45,4)
node[right] {$\hat r$};

\draw[->] (2,2.25,4) -- (1,2.5,4)
node[left] {$\hat\phi$};

\draw[->] (2,2.25,4) -- (2,2.25,4.75)
node[right] {$\hat k$};

\draw[->] (4,0,0) arc (0:45:4);

\node at (3.6,2,0) {$\phi_1$};

\draw[->] (0,0,0) -- (2,2.35,0);
\node at (1,1,0) {$r_1$};

\draw (2,2.25,4) -- (2,2.25,0);

\node at (-3.5,5.5,4) {$z=z_1$};

\node at (5.5,6,0) {$\phi=\phi_1$};

\end{tikzpicture}

\end{document}
```


```tikz
\usepackage{tikz-3dplot}

\begin{document}

\tdplotsetmaincoords{70}{120}

\begin{tikzpicture}[tdplot_main_coords]

\draw[->] (0,0,0) -- (3,0,0) node[right] {$x$};
\draw[->] (0,0,0) -- (0,3,0) node[left] {$y$};
\draw[->] (0,0,0) -- (0,0,3) node[above] {$z$};

\end{tikzpicture}

\end{document}
```
```tikz
\usepackage{tikz-3dplot}

\begin{document}

\tdplotsetmaincoords{70}{120}

\begin{tikzpicture}[tdplot_main_coords]

\shade[ball color=cyan!40] (0,0) circle (1.5);

\draw[->] (0,0,0) -- (2,0,0);
\draw[->] (0,0,0) -- (0,2,0);
\draw[->] (0,0,0) -- (0,0,4);

\node[right] at (2,0,0) {$y$};
\node[left] at (0,2,0) {$z$};
\node[above] at (0,0,4) {$x$};

\draw (-1.5,0) arc (180:360:1.5 and 0.4);
\draw[dashed] (1.5,0) arc (0:180:1.5 and 0.4);

\draw[dashed,->] (0,0) -- (1.06,1.06);

\node at (0.6,0.8) {$\rho_0$};

\end{tikzpicture}

\end{document}
```

```tikz
\begin{document}

\begin{tikzpicture}

\fill[red!30]
(0,-0.5) --
(1,-1.5) --
(1,0.5) --
(0,1.5) -- cycle;

\draw[->] (0,0) -- (2,0) node[right] {$y$};
\draw[->] (0,-0.5) -- (0,2) node[above] {$z$};
\draw[->] (0,0) -- (-1,-1) node[left] {$x$};

\draw[dashed] (0,0) -- (1,-1);

\draw[->]
(-0.7,-0.7)
arc(225:315:1 and 0.7);

\node at (-0.4,-0.9) {$\theta_0$};

\end{tikzpicture}

\end{document}
```

```tikz
\begin{document}

\begin{tikzpicture}

\fill[blue!20]
(-1,2.2)
arc(180:360:1 and 0.3)
-- (0,0)
-- cycle;

\draw
(-1,2.2)
arc(180:360:1 and 0.3);

\draw
(-1,2.2)
arc(180:360:1 and 0.3)
-- (0,0)
-- cycle;

\draw[->] (0,0) -- (2,0) node[right] {$y$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$z$};
\draw[->] (0,0) -- (-1,-1) node[left] {$x$};

\draw[dashed] (-1,2.2) -- (1,2.2);

\draw[->]
(0,1.4)
arc(100:65:1 and 1.2);

\node at (0.4,1) {$\phi_0$};

\end{tikzpicture}

\end{document}
```


```tikz
\begin{document}

\begin{tikzpicture}[
    scale=1.2,
    every node/.style={
        black,
        text height=1.5ex,
        text depth=0.25ex
    }
]

\footnotesize

% Ejes
\draw[-stealth] (-0.4,0) -- (5.2,0) node[right] {$x$};
\draw[-stealth] (0,-0.4) -- (0,3) node[above] {$y$};

% Curva izquierda
\draw[Blue,thick,densely dashed]
(0.4,1.5)
node[above right,yshift=3.5mm] {$f$}
parabola[bend at end] (2,2.7);

\draw[Blue,semithick,densely dashed]
(0.4,1.5) -- (0.4,0)
node[below] {$a$};

\draw[Blue,semithick,densely dashed]
(1,2.23) --
node[right=-0.5mm] {$f(x-c)$}
(1,0)
node[below] {$x-c$};

\draw[Blue,semithick,densely dashed]
(2,2.7) -- (2,0)
node[below] {$b$};

% Curva derecha trasladada
\begin{scope}[xshift=2.3cm]

\draw[Blue,thick]
(0.4,1.5)
node[above right,yshift=3.5mm] {$g$}
parabola[bend at end] (2,2.7);

\draw[Blue,semithick]
(0.4,1.5) -- (0.4,0)
node[below] {$a+c$};

\draw[Blue,semithick]
(1,2.23) --
node[right=-0.5mm] {$g(x)$}
(1,0)
node[below] {$x$};

\draw[Blue,semithick]
(2,2.7) -- (2,0)
node[below] {$b+c$};

\end{scope}

% Flecha de traslación
\draw[-latex]
(1.4,-0.4)
to[bend right=20]
(3,-0.4);

\node[below left] at (0,0) {$O$};

\end{tikzpicture}

\end{document}
```
