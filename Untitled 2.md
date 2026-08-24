##### Ej. Una masa $m$ se mueve sobre la curva $y = 4x^2$ bajo la acción de la gravedad. La única coordenada generalizada es $x$. Fuerzas: $F_x = 0$, $F_y = -mg$, $F_z = 0$. Obtener la GDE para $q_r = x$ mediante la ecuación de Lagrange.

```tikz
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[>=latex, scale=1.2]

  % Ejes
  \draw[->, thick, teal] (-2,0) -- (2,0)
    node[right] {$x$};

  \draw[->, thick, teal] (0,-0.5) -- (0,3.5)
    node[above] {$y$};

  % Trayectoria parabólica
  \draw[
    domain=-0.8:0.8,
    smooth,
    variable=\x,
    thick,
    teal
  ]
  plot ({\x},{4*\x*\x});

  % Masa
  \filldraw[orange] (0.5,1.0) circle (3pt)
    node[above right, teal] {$m$};

  % Fuerza gravitacional
  \draw[->, thick, orange]
    (0.5,1.0) -- (0.5,0.2)
    node[below] {$-mg\hat{j}$};

\end{tikzpicture}

\end{document}
```

**Resolución**
Se determinan las derivadas temporales y parciales de la energía cinética para el lado izquierdo de la ecuación de Lagrange, y se calculan las proyecciones de las fuerzas aplicadas en el lado derecho.


$$
\begin{array}{rcl}
\dfrac{\partial T}{\partial \dot x} & = & m(1+64x^2)\dot x \\
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot x}\right) & = & m(1+64x^2)\ddot x + 128mx\dot x^2 \\
\dfrac{\partial T}{\partial x} & = & 64mx\dot x^2 \\
\text{LHS} = \dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot x}\right) - \dfrac{\partial T}{\partial x} & = & m(1+64x^2)\ddot x + 64mx\dot x^2 \\
\text{RHS} = F_x\dfrac{\partial x}{\partial x} + F_y\dfrac{\partial y}{\partial x} + F_z\dfrac{\partial z}{\partial x} & = & 0 \cdot (1) - mg \cdot (8x) + 0 \cdot (0) \\
\text{RHS} & = & -8mgx \\
m(1+64x^2)\ddot x + 64mx\dot x^2 & = & -8mgx \\
(1+64x^2)\ddot x + 64x\dot x^2 & = & -8gx \\
\therefore\quad \color{orange}{(1+64x^2)\ddot x + 64x\dot x^2 + 8gx = 0}
\end{array}
$$


