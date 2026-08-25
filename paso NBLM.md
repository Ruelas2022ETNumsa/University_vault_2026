##### Ej. Una masa $m$ se mueve libremente en el plano $z=0$ bajo la acción exclusiva de la gravedad. Las coordenadas generalizadas son $r$ y $\theta$ (polares planas), con origen en el punto de lanzamiento. Las coordenadas cartesianas se relacionan como $x = r \cos\theta$, $y = r\sin\theta$. Fuerzas: $F_x = 0$, $F_y = -mg$, $F_z = 0$. Obtener las GDE para $q_r = r$ y $q_r = \theta$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex, scale=1.2]
  % Axes
  \draw[->, gray, thick] (0,0) -- (3,0) node[right, black] {$x$};
  \draw[->, gray, thick] (0,0) -- (0,3) node[above, black] {$y$};
  \draw[->, gray, dashed] (0,0) -- (0,-1);
  % Vector r
  \draw[->, teal, ultra thick] (0,0) -- (35:2.5) node[midway, above left] {$r$};
  % Point m
  \filldraw[orange] (35:2.5) circle (2.5pt) node[above right, black] {$m$};
  % Angle theta
  \draw[->, thick, orange] (0.8,0) arc (0:35:0.8) node[midway, right=2pt] {$\theta$};
  % Gravity vector
  \draw[->, red, thick] (35:2.5) -- ++(0,-1) node[below] {$\vec{F}_g = -mg\hat{j}$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Aplicar la ecuación general de Lagrange (ecuación alfa) proyectando las fuerzas cartesianas sobre las direcciones de las coordenadas polares $r$ y $\theta$.

**Para $q_r = r$:**


$$
\begin{array}{rcl}
T & = & \dfrac{1}{2}m\left(\dot{r}^2 + r^2\dot{\theta}^2\right) \[10pt]
\dfrac{\partial T}{\partial \dot{r}} & = & m\dot{r} \[10pt]
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{r}}\right) & = & m\ddot{r} \[10pt]
\dfrac{\partial T}{\partial r} & = & mr\dot{\theta}^2 \[10pt]
Q_r & = & F_x\dfrac{\partial x}{\partial r} + F_y\dfrac{\partial y}{\partial r} + F_z\dfrac{\partial z}{\partial r} \[10pt]
& = & (0)\cos\theta + (-mg)\sin\theta + (0)(0) \[10pt]
& = & -mg\sin\theta \[10pt]
\therefore\quad & & \color{orange}{m(\ddot{r} - r\dot{\theta}^2) = -mg\sin\theta}
\end{array}
$$


**Para $q_r = \theta$:**


$$
\begin{array}{rcl}
\dfrac{\partial T}{\partial \dot{\theta}} & = & mr^2\dot{\theta} \[10pt]
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{\theta}}\right) & = & mr^2\ddot{\theta} + 2mr\dot{r}\dot{\theta} \[10pt]
\dfrac{\partial T}{\partial \theta} & = & 0 \[10pt]
Q_\theta & = & F_x\dfrac{\partial x}{\partial \theta} + F_y\dfrac{\partial y}{\partial \theta} + F_z\dfrac{\partial z}{\partial \theta} \[10pt]
& = & (0)(-r\sin\theta) + (-mg)(r\cos\theta) + (0)(0) \[10pt]
& = & -mgr\cos\theta \[10pt]
\therefore\quad & & \color{orange}{m(r^2\ddot{\theta} + 2r\dot{r}\dot{\theta}) = -mgr\cos\theta}
\end{array}
$$

