

##### Ejercicio 2

Una masa $m$ se mueve libremente en el plano $z=0$ bajo la acción de la gravedad. Las coordenadas generalizadas son $x$ e $y$ directamente. Fuerzas: $F_x=0$, $F_y=-mg$, $F_z=0$. Obtener las GDE para $q_r=x$ y $q_r=y$.

$$
T = \frac{m}{2}\left(\dot x^2+\dot y^2\right)
$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]
  % Ejes
  \draw[->, thick, teal] (-0.3,0) -- (3.5,0) node[right] {$x$};
  \draw[->, thick, teal] (0,-0.3) -- (0,2.5) node[above] {$y$};
  % Semicircunferencia
  \draw[thick, teal] (3,0) arc (0:180:1.5);
  % Masa
  \filldraw[orange] (0.9,1.35) circle (3.5pt) node[above right, black] {$m$};
  % Fuerza gravedad
  \draw[->, ultra thick, orange] (0.9,1.35) -- (0.9,0.45) node[right, black] {$-mg\,\hat{\mathbf{e}}_y$};
  % z=0
  \node[teal] at (2.8,0.25) {$z=0$};
\end{tikzpicture}
\end{document}
```

```ad-info
collapse: open

La curva (semicircunferencia) ilustra una posible trayectoria pero no es una restricción del sistema — el método es idéntico para cualquier trayectoria libre en el plano: parábola, recta, arco. Lo que define el problema son las fuerzas y las coordenadas generalizadas, no la forma de la curva.
```

**Resolución**
Se aplican las derivadas parciales de la energía cinética y de las relaciones de posición cartesianas directamente en la ecuación alfa para cada coordenada generalizada independiente.

Para $q_r = x$:

$$
\begin{array}{rcl}
\dfrac{\partial x}{\partial x} = 1, \quad \dfrac{\partial y}{\partial x} = 0, \quad \dfrac{\partial z}{\partial x} & = & 0 \\
\dfrac{\partial T}{\partial \dot{x}} = \dfrac{\partial}{\partial \dot{x}} \left[ \dfrac{m}{2} (\dot{x}^2 + \dot{y}^2) \right] & = & m\dot{x} \\
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{x}}\right) & = & m\ddot{x} \\
\dfrac{\partial T}{\partial x} & = & 0 \\
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{x}}\right) - \dfrac{\partial T}{\partial x} & = & F_x \dfrac{\partial x}{\partial x} + F_y \dfrac{\partial y}{\partial x} + F_z \dfrac{\partial z}{\partial x} \\
m\ddot{x} - 0 & = & (0)(1) + (-mg)(0) + (0)(0) \\
m\ddot{x} & = & 0 \\
\therefore\quad \color{orange}{\ddot{x}} & = & \color{orange}{0}
\end{array}
$$


Para $q_r = y$:

$$
\begin{array}{rcl}
\dfrac{\partial x}{\partial y} = 0, \quad \dfrac{\partial y}{\partial y} = 1, \quad \dfrac{\partial z}{\partial y} & = & 0 \\
\dfrac{\partial T}{\partial \dot{y}} = \dfrac{\partial}{\partial \dot{y}} \left[ \dfrac{m}{2} (\dot{x}^2 + \dot{y}^2) \right] & = & m\dot{y} \\
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{y}}\right) & = & m\ddot{y} \\
\dfrac{\partial T}{\partial y} & = & 0 \\
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{y}}\right) - \dfrac{\partial T}{\partial y} & = & F_x \dfrac{\partial x}{\partial y} + F_y \dfrac{\partial y}{\partial y} + F_z \dfrac{\partial z}{\partial y} \\
m\ddot{y} - 0 & = & (0)(0) + (-mg)(1) + (0)(0) \\
m\ddot{y} & = & -mg \\
\therefore\quad \color{orange}{\ddot{y}} & = & \color{orange}{-g}
\end{array}
$$

