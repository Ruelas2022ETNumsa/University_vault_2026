##### Ej. Una masa m se mueve sobre la curva y − 1 = (x − 2)² bajo la acción de la gravedad. La única coordenada generalizada es x. Fuerzas: Fx = 0, Fy = −mg, Fz = 0. Obtener la GDE para qr = x.

```tikz
\usepackage{tikz}
\begin{document}
\draw[->, thick, gray] (-0.5,0) -- (4.5,0) node[right] {$x$};
\draw[->, thick, gray] (0,-0.5) -- (0,5) node[above] {$y$};
\draw[domain=0.3:3.7, smooth, variable=\x, teal, ultra thick] plot ({\x}, {1 + (\x-2)*(\x-2)});
\filldraw[orange] (1,2) circle (2.5pt) node[above left, black] {$m$};
\draw[->, orange, ultra thick] (1,2) -- (1,0.8) node[below, black] {$m\vec{g}$};
\end{document}
```

**Resolución**
Se aplica el formalismo lagrangiano $L = T - V$ con el vínculo holónomo de la trayectoria en el plano.


$$
\begin{array}{rcl}
y & = & 1 + (x - 2)^2 \[4pt]
\dot{y} & = & 2(x - 2)\dot{x} \[4pt]
T & = & \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) \[4pt]
T & = & \frac{1}{2}m\left[\dot{x}^2 + 4(x-2)^2\dot{x}^2\right] \[4pt]
T & = & \frac{1}{2}m\dot{x}^2\left[1 + 4(x-2)^2\right] \[4pt]
V & = & mgy \[4pt]
V & = & mg\left[1 + (x - 2)^2\right] \[4pt]
L & = & T - V \[4pt]
L & = & \frac{1}{2}m\dot{x}^2\left[1 + 4(x-2)^2\right] - mg\left[1 + (x - 2)^2\right] \[4pt]
\frac{\partial L}{\partial \dot{x}} & = & m\dot{x}\left[1 + 4(x-2)^2\right] \[4pt]
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) & = & m\ddot{x}\left[1 + 4(x-2)^2\right] + 8m(x-2)\dot{x}^2 \[4pt]
\frac{\partial L}{\partial x} & = & 4m(x-2)\dot{x}^2 - 2mg(x-2) \[4pt]
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) - \frac{\partial L}{\partial x} & = & 0 \[4pt]
m\ddot{x}\left[1 + 4(x-2)^2\right] + 8m(x-2)\dot{x}^2 - 4m(x-2)\dot{x}^2 + 2mg(x-2) & = & 0 \[4pt]
m\ddot{x}\left[1 + 4(x-2)^2\right] + 4m(x-2)\dot{x}^2 + 2mg(x-2) & = & 0 \[4pt]
\therefore\quad \color{orange}{\ddot{x}\left[1 + 4(x-2)^2\right] + 4(x-2)\dot{x}^2 + 2g(x-2) = 0}
\end{array}
$$


