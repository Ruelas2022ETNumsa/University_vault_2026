

##### Ej. La Tierra de masa $m$ orbita alrededor del Sol (estático) bajo la acción de la fuerza gravitacional $F = \frac{GMm}{r^2}$. Las coordenadas generalizadas son $x$ e $y$ (cartesianas en el plano orbital). El Sol está fijo en el origen. Fuerzas: $F_x = -\frac{GMm}{r^2} \cos \theta = -\frac{GMm \cdot x}{r^3}$, $F_y = -\frac{GMm}{r^2} \text{sen } \theta = -\frac{GMm \cdot y}{r^3}$, donde $r = \sqrt{x^2 + y^2}$ y $\theta$ es el ángulo desde el eje $x$. Obtener las ecuaciones de movimiento para $q_r = x$ e $q_r = y$ usando la ecuación alfa de Lagrange.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
% Ejes
\draw[->, thick, gray] (-0.5,0) -- (2.5,0) node[right, black] {$x$};
\draw[->, thick, gray] (0,-0.5) -- (0,2) node[above, black] {$y$};
% Sol en el origen
\filldraw[orange!80!yellow, draw=orange, thick] (0,0) circle (0.15) node[below left, black] {Sol ($M$)};
% Órbita elíptica
\draw[dashed, gray] (0,0) ellipse (1.8cm and 1.3cm);
% Tierra
\coordinate (E) at (36:1.8cm);
\filldraw[teal, draw=black] (E) circle (0.08) node[above right, black] {Tierra ($m$)};
% Vector de posición
\draw[->, thick, teal] (0,0) -- (E) node[midway, above left] {$\vec{r}$};
% Ángulo theta
\draw[->, thick, orange] (0.5,0) arc (0:36:0.5) node[midway, right] {$\theta$};
% Vector de fuerza atractiva hacia el origen
\draw[->, ultra thick, orange] (E) -- (36:0.8cm) node[midway, below right] {$\vec{F}$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Determinar la energía cinética en coordenadas cartesianas y aplicar las ecuaciones de Lagrange para cada coordenada con las fuerzas dadas.

Para la coordenada generalizada $q_1 = x$:


$$
\begin{array}{rcl}
T & = & \displaystyle \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) \[10pt]
\displaystyle \frac{\partial T}{\partial \dot{x}} & = & m\dot{x} \[10pt]
\displaystyle \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) & = & m\ddot{x} \[10pt]
\displaystyle \frac{\partial T}{\partial x} & = & 0 \[10pt]
F_x & = & \displaystyle -\frac{GMm \cdot x}{(x^2 + y^2)^{3/2}} \[10pt]
\displaystyle \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} & = & F_x \[10pt]
m\ddot{x} - 0 & = & \displaystyle -\frac{GMm \cdot x}{(x^2 + y^2)^{3/2}} \[10pt]
\ddot{x} & = & \displaystyle -\frac{GM \cdot x}{(x^2 + y^2)^{3/2}} \[10pt]
\therefore\quad \ddot{x} + \displaystyle \frac{GM \cdot x}{(x^2 + y^2)^{3/2}} & = & \color{orange}{0}
\end{array}
$$


Para la coordenada generalizada $q_2 = y$:


$$
\begin{array}{rcl}
T & = & \displaystyle \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) \[10pt]
\displaystyle \frac{\partial T}{\partial \dot{y}} & = & m\dot{y} \[10pt]
\displaystyle \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}}\right) & = & m\ddot{y} \[10pt]
\displaystyle \frac{\partial T}{\partial y} & = & 0 \[10pt]
F_y & = & \displaystyle -\frac{GMm \cdot y}{(x^2 + y^2)^{3/2}} \[10pt]
\displaystyle \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}}\right) - \frac{\partial T}{\partial y} & = & F_y \[10pt]
m\ddot{y} - 0 & = & \displaystyle -\frac{GMm \cdot y}{(x^2 + y^2)^{3/2}} \[10pt]
\ddot{y} & = & \displaystyle -\frac{GM \cdot y}{(x^2 + y^2)^{3/2}} \[10pt]
\therefore\quad \ddot{y} + \displaystyle \frac{GM \cdot y}{(x^2 + y^2)^{3/2}} & = & \color{orange}{0}
\end{array}
$$

