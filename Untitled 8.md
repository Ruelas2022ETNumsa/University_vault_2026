### Ejercicio 1 — Resorte péndulo (Fig. 2.8)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.8]
  % Techo
  \draw[line width=1.5pt, black!60] (-1.5,0) -- (1.5,0);
  \foreach \x in {-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0,1.25,1.5}
    \draw[black!40] (\x,0) -- (\x+0.15,0.15);

  % Ejes de referencia
  \draw[dashed, black!30] (0,0) -- (0,-4) node[below] {$y\downarrow$};
  \draw[dashed, black!30] (0,0) -- (3.5,0) node[right] {$x$};

  % Puntos
  \coordinate (O) at (0,0);
  \coordinate (M) at (-60:3.2);

  % Angulo theta
  \draw[->, orange, thick] (0,-1.2) arc (-90:-60:1.2);
  \node[orange] at (-75:1.5) {$\theta$};

  % Resorte
  \draw[thick, teal] (O) -- (-60:0.4);
  \draw[thick, teal, decoration={coil, aspect=0.3, segment length=4pt, amplitude=3pt}, decorate] (-60:0.4) -- (-60:2.5);
  \draw[thick, teal] (-60:2.5) -- (M);
  \node[black] at (-53:1.8) {$r$};

  % Masa
  \filldraw[fill=orange!80, draw=orange!40!black, thick] (M) circle (0.18) node[below right, black] {$m$};

  % Fuerzas
  \draw[->, orange, very thick] (M) -- ++(0,-1.0) node[below] {$mg$};
  \draw[->, teal, very thick] (M) -- ++(120:1.2) node[above left] {$k(r-l_0)$};

\end{tikzpicture}
\end{document}
```

**Sistema:** masa $m$ unida a un resorte ($k$, longitud natural $l_0$) colgando de un punto fijo. Coordenadas generalizadas: longitud $r$ y ángulo $\theta$ desde la vertical. Eje $y$ hacia abajo — dos grados de libertad.

---

#### Ecuación de movimiento general (ecuación alfa)

$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot q_r}\right)
-
\frac{\partial T}{\partial q_r}
=
F_x\frac{\partial x}{\partial q_r}
+
F_y\frac{\partial y}{\partial q_r}
+
F_z\frac{\partial z}{\partial q_r}
$$
Se aplica una vez por cada coordenada generalizada.

---

#### Datos del sistema

**Coordenadas cartesianas:**
$$
x = r\sin\theta \qquad y = r\cos\theta
$$

**Energía cinética** (polares planas, $\dot z = 0$):
$$
T = \frac{1}{2}m\!\left(\dot r^2 + r^2\dot\theta^2\right)
$$

**Fuerzas** — el resorte actúa radialmente hacia el origen con magnitud $k(r-l_0)$; la gravedad actúa en $+y$:

> **¿Por qué $k(r-l_0)$ y no $\frac{1}{2}k(r-l_0)^2$?**
> $\frac{1}{2}k(r-l_0)^2$ es la **energía potencial elástica** $V$ del resorte.
> La **fuerza** es su derivada respecto a $r$:
> $$\frac{dV}{dr} = \frac{d}{dr}\!\left[\frac{1}{2}k(r-l_0)^2\right] = k(r-l_0)$$
> En la ecuación alfa las fuerzas van en el lado derecho — por eso se usa $k(r-l_0)$, no $V$.
$$
F_x = -k(r-l_0)\sin\theta \qquad F_y = -k(r-l_0)\cos\theta + mg
$$

---

#### GDE para $q_r = r$

**Lado izquierdo** — derivadas de $T$:

$$
\frac{\partial T}{\partial \dot r} = m\dot r
\qquad\Rightarrow\qquad
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot r}\right) = m\ddot r
$$

$$
\frac{\partial T}{\partial r} = mr\dot\theta^2
$$

$$
\therefore\quad \text{lado izq} = m\ddot r - mr\dot\theta^2
$$

**Lado derecho** — proyección de fuerzas sobre $r$:

$$
\frac{\partial x}{\partial r} = \sin\theta \qquad \frac{\partial y}{\partial r} = \cos\theta
$$

$$
\begin{array}{rcl}
Q_r & = & -k(r-l_0)\sin\theta\cdot\sin\theta + \left[-k(r-l_0)\cos\theta + mg\right]\cos\theta \\[6pt]
    & = & -k(r-l_0)\sin^2\theta - k(r-l_0)\cos^2\theta + mg\cos\theta \\[6pt]
    & = & -k(r-l_0)\underbrace{(\sin^2\theta+\cos^2\theta)}_{=\,1} + mg\cos\theta \\[6pt]
    & = & -k(r-l_0) + mg\cos\theta
\end{array}
$$

> Los términos del resorte se combinan usando la identidad pitagórica — la dirección de la fuerza queda solo en magnitud radial.

**Igualando lado izquierdo = lado derecho:**

> [!important]
> $$
> \boxed{m(\ddot r - r\dot\theta^2) = -k(r-l_0) + mg\cos\theta}
> $$

---

#### GDE para $q_r = \theta$

**Lado izquierdo** — derivadas de $T$:

$$
\frac{\partial T}{\partial \dot\theta} = mr^2\dot\theta
\qquad\Rightarrow\qquad
\frac{d}{dt}\!\left(mr^2\dot\theta\right) = mr^2\ddot\theta + 2mr\dot r\dot\theta
$$

> La regla del producto sobre $r^2\dot\theta$ genera los dos términos: $2r\dot r\dot\theta + r^2\ddot\theta$.

$$
\frac{\partial T}{\partial \theta} = 0
$$

$$
\therefore\quad \text{lado izq} = mr^2\ddot\theta + 2mr\dot r\dot\theta
$$

**Lado derecho** — proyección de fuerzas sobre $\theta$:

$$
\frac{\partial x}{\partial \theta} = r\cos\theta \qquad \frac{\partial y}{\partial \theta} = -r\sin\theta
$$

$$
\begin{array}{rcl}
Q_\theta & = & -k(r-l_0)\sin\theta\cdot r\cos\theta + \left[-k(r-l_0)\cos\theta + mg\right](-r\sin\theta) \\[6pt]
         & = & -kr(r-l_0)\sin\theta\cos\theta + kr(r-l_0)\cos\theta\sin\theta - mgr\sin\theta \\[6pt]
         & = & -mgr\sin\theta
\end{array}
$$

> Los dos términos del resorte se cancelan entre sí — la fuerza radial no tiene componente en la dirección angular.

**Igualando:**

> [!important]
> $$
> \boxed{m(2r\dot r\dot\theta + r^2\ddot\theta) = -mgr\sin\theta}
> $$

---

#### Caso particular — péndulo simple ($r = l = \text{cte}$, $\dot r = 0$)

Con $r$ constante, $\dot r = 0$, la GDE de $\theta$ se reduce a:

$$
ml^2\ddot\theta + mgl\sin\theta = 0
$$

Dividiendo por $ml$:

> [!important]
> $$
> \boxed{l\ddot\theta = -g\sin\theta}
> $$

> Resultado clásico del péndulo simple. El resorte no aparece porque $r$ es constante — la dinámica queda gobernada solo por la gravedad y la longitud $l$.
