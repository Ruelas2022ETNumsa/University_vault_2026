### 6. EDO $\theta$, $N=1$

$$
x = \ell\sin\theta
$$

$$
y = \ell\cos\theta
$$

```tikz
\usepackage{tikz}

\usetikzlibrary{decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.5]

%------------------------------------------------
% TECHO
%------------------------------------------------

\draw[line width=1.5pt, black!60] (-1.5,0) -- (1.5,0);

\foreach \x in {-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0,1.25,1.5}
\draw[black!40] (\x,0) -- (\x+0.18,0.18);

%------------------------------------------------
% PISO
%------------------------------------------------

\draw[line width=1.5pt, black!60] (-1.5,-4) -- (1.5,-4);

\foreach \x in {-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0,1.25,1.5}
\draw[black!40] (\x,-4) -- (\x-0.18,-3.82);

%------------------------------------------------
% EJE VERTICAL DE REFERENCIA
%------------------------------------------------

\draw[dashed, black!40] (0,0) -- (0,-4);

%------------------------------------------------
% EJE x EN EL TECHO
%------------------------------------------------

\draw[->, red, dashed, thick] (0.0,0.15) -- (0.9,0.15)
    node[right] {$x$};

%------------------------------------------------
% PUNTOS DE REFERENCIA
%------------------------------------------------

\coordinate (O) at (0,0);
\coordinate (A) at (0,-4);

%------------------------------------------------
% ALTURA H
%------------------------------------------------

\draw[<->, red, thick] (-1.75,0) -- (-1.75,-4);

\draw[red, thick] (-1.85,0) -- (-1.65,0);
\draw[red, thick] (-1.85,-4) -- (-1.65,-4);

\node[red] at (-1.95,-2) {$H$};

%------------------------------------------------
% BARRA / PÉNDULO
%------------------------------------------------

\coordinate (M) at (2.0,-2.75);

\draw[very thick, black!60] (O) -- (M);

% Longitud l
\node[black!70] at (1.65,-1.35) {$l$};

%------------------------------------------------
% ÁNGULO THETA
%------------------------------------------------

\draw[->, cyan, thick]
    (0,-1.15) arc (-90:-54:1.15);

\node[cyan] at (0.45,-1.25) {$\theta$};

%------------------------------------------------
% RESORTE
%------------------------------------------------

\draw[thick, teal] (A) -- (0.45,-3.55);

\draw[
    thick,
    teal,
    decoration={
        coil,
        aspect=0.3,
        segment length=4pt,
        amplitude=3pt
    },
    decorate
] (0.45,-3.55) -- (1.55,-3.0);

\draw[thick, teal] (1.55,-3.0) -- (M);

% Etiqueta r
\node[teal] at (1,-3) {$r$};

%------------------------------------------------
% MASA
%------------------------------------------------

\filldraw[
    fill=orange!80,
    draw=orange!40!black,
    thick
] (M) circle (0.18);

\node[black] at (2.35,-2.65) {$m$};

%------------------------------------------------
% FUERZA DE GRAVEDAD
%------------------------------------------------

\draw[->, red, very thick]
    (M) -- (2.0,-3.55);

\node[red] at (2.25,-3.35) {$mg$};

%------------------------------------------------
% FUERZA DEL RESORTE
%------------------------------------------------

\draw[->, teal, very thick]
    (M) -- (1.25,-1.7);

\node[teal] at (0.8,-2) {$k(r-l_0)$};

%------------------------------------------------
% INDICACIÓN DEL EJE VERTICAL
%------------------------------------------------

\node[red] at (-0.25,-0.65) {$y$};

\end{tikzpicture}

\end{document}
```


---
### Sol.

_Verificación de $T$: $\dot{x} = \ell\dot{\theta}\cos\theta$, $\dot{y} = -\ell\dot{\theta}\sin\theta$ $\Rightarrow$ $\dot{x}^2+\dot{y}^2 = \ell^2\dot{\theta}^2(\cos^2\theta+\sin^2\theta) = \ell^2\dot{\theta}^2$, por tanto $T = \frac{m}{2}\ell^2\dot{\theta}^2$._

$$
T = \frac{m}{2}
\left(
\dot{r}^{\,2}
+
r^2\dot{\theta}^{\,2}
+
\dot{z}^{\,2}
\right)
$$

$$
r = \ell
\quad\Rightarrow\quad
\dot{r}=0
$$

$$
z=0
\quad\Rightarrow\quad
\dot{z}=0
$$

Por tanto:

$$
T = \frac{m}{2}\ell^2\dot{\theta}^{\,2}
$$

Aplicando la ecuación de Lagrange:

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot{\theta}}
\right)
-
\frac{\partial T}{\partial\theta}
=
F_x\frac{\partial x}{\partial\theta}
+
F_y\frac{\partial y}{\partial\theta}
+
F_z\frac{\partial z}{\partial\theta}
$$

$$
\frac{m\ell^2\ddot{\theta}}{2}
-
0
=
\left[-k(r-\ell_0)\sin\alpha\right]
\left[\ell\cos\theta\right]
+
\left[k(r-\ell_0)\cos\alpha+mg\right]
\left[-\ell\sin\theta\right]
$$

$$
m\ell^2\ddot{\theta}
=
-k(r-\ell_0)\ell
\left(
\sin\alpha\cos\theta
+
\cos\alpha\sin\theta
\right)
-
mg\ell\sin\theta
$$

### Operación auxiliar

_$r$ se obtiene por ley de cosenos en el triángulo formado por $H$, $\ell$ y $r$. $\sin\alpha$ se obtiene por ley de senos en ese mismo triángulo. Ambos se usan para expandir $\sin\alpha\cos\theta + \cos\alpha\sin\theta = \sin(\alpha+\theta)$ y simplificar el lado derecho de la GDE._

$$
r^2=H^2+\ell^2-2H\ell\cos\theta
$$

$$
\frac{\ell}{\sin\alpha}
=
\frac{r}{\sin\theta}
$$

$$
\sin\alpha
=
\frac{\ell\sin\theta}{r}
$$

Además:

$$
r=
\sqrt{H^2+\ell^2-2H\ell\cos\theta}
$$

Por tanto:

$$
m\ell^2\ddot{\theta}
=
-k
\left(
\sqrt{H^2+\ell^2-2H\ell\cos\theta}
-\ell_0
\right)
\ell
\left(
\frac{\ell}{r}\sin\theta\cos\theta
+
\sqrt{
1-\frac{\ell^2\sin^2\theta}{r^2}
}
\sin\theta
\right)
-
mg\ell\sin\theta
$$