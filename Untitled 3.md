### 3. EDO $x$, $N=1$

$$
z=0
$$

$$
y=H-x
$$

$$
\dot{y}=-\dot{x}
$$

$$
x^2+y^2=r^2
$$

$$
x^2+(H-x)^2=r^2
$$

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[>=latex, scale=1.35]
  % Caja
  \draw[thick, black!50] (0,0) rectangle (4,4);
  % Barra diagonal
  \draw[very thick, black!70] (0,0) -- (4,4);
  % Ejes
  \draw[->, dashed, thick, black!40] (-0.3,4.25) -- (1.8,4.25) node[right] {$x$};
  \draw[->, dashed, thick, black!40] (-0.3,4.25) -- (-0.3,2.1) node[below] {$y$};
  % Punto fijo del resorte
  \coordinate (A) at (0,4);
  % Masa
  \coordinate (M) at (2.25,2.25);
  % Resorte
  \draw[thick, teal] (A) -- (0.35,3.65);
  \draw[thick, teal,
    decoration={coil, aspect=0.35, segment length=5pt, amplitude=4pt},
    decorate] (0.35,3.65) -- (2.05,2.45);
  \draw[thick, teal] (2.05,2.45) -- (M);
  \node[teal, font=\large] at (1.05,3.25) {$r$};
  % Angulo theta
  \draw[->, blue, thick] (0,2.9) arc[start angle=270, end angle=315, radius=1.1];
  \node[blue, font=\large] at (0.38,3.08) {$\theta$};
  % Masa
  \filldraw[fill=orange!85, draw=orange!50!black, thick] (M) circle (0.18);
  \node[orange!80!black, right] at (2.42,2.25) {$m$};
  % Fuerza resorte
  \draw[->, red, very thick] (M) -- (1.35,3.15) node[above left, red] {$F_R$};
  % Peso
  \draw[->, red, very thick] (M) -- ++(0,-0.95) node[below, red] {$mg$};
  % Cota h
  \draw[thick, orange] (4.55,0) -- (4.55,4);
  \draw[thick, orange] (4.38,0) -- (4.72,0);
  \draw[thick, orange] (4.38,4) -- (4.72,4);
  \draw[<->, thick, orange] (4.55,0.15) -- (4.55,3.85);
  \node[orange, right, font=\large] at (4.7,2) {$h$};
\end{tikzpicture}
\end{document}
```

### Sol.

$$
T=\frac{m}{2}
\left(
\dot{x}^{\,2}+\dot{y}^{\,2}
\right)
=m\dot{x}^{\,2}
$$

Entonces:

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot{x}}
\right)
-
\frac{\partial T}{\partial x}
=
F_x\frac{\partial x}{\partial x}
+
F_y\frac{\partial y}{\partial x}
+
F_z\frac{\partial z}{\partial x}
$$

$$
2m\ddot{x}
=
-k(r-\ell_0)\sin\theta
+
\left[
mg-k(r-\ell_0)\cos\theta
\right](-1)
$$

$$
2m\ddot{x}
=
-k(r-\ell_0)
\left(
\sin\theta-\cos\theta
\right)
-mg
$$

Además:

$$
r=
\sqrt{(H-x)^2+x^2}
$$

$$
\sin\theta=\frac{x}{r}
$$

$$
\cos\theta=\frac{H-x}{r}
$$

Por tanto:

$$
2m\ddot{x}
=
-k
\left(
\sqrt{(H-x)^2+x^2}-\ell_0
\right)
\left(
\frac{x}{r}
-
\frac{H-x}{r}
\right)
-mg
$$