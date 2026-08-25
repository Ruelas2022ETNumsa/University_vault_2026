
```tikz
\usepackage{tikz}

\begin{document}

\begin{tikzpicture}[>=latex, scale=0.55]

% Ejes
\draw[->, thick, teal] (-1,0) -- (7.5,0) node[right] {$x$};
\draw[->, thick, teal] (0,0) -- (0,19) node[above] {$y$};

% Trayectoria parabólica
\draw[
    domain=0.5:6.5,
    smooth,
    variable=\x,
    thick,
    teal
]
plot ({\x},{1+(\x-2)^2});

% Masa en el punto (6,17)
\filldraw[orange] (6,17) circle (5pt)
    node[above right, teal] {$m$};

% Fuerza gravitacional
\draw[->, thick, orange]
    (6,17) -- (6,14)
    node[right] {$-mg\,\hat{j}$};

% Vértice
\filldraw[teal] (2,1) circle (2pt)
    node[below right] {$(2,1)$};

% Punto de referencia
\draw[dashed, teal] (6,0) -- (6,17);
\draw[dashed, teal] (0,17) -- (6,17);

% Etiqueta de la curva
\node[teal] at (4.8,8.5) {$y-1=(x-2)^2$};

% Etiquetas de coordenadas
\node[below, teal] at (6,0) {$6$};
\node[left, teal] at (0,17) {$17$};

\end{tikzpicture}

\end{document}
```


$$
y-1=(x-2)^2
$$

$$
z=0
$$

$$
(y-1)=k(x-2)^2
$$

$$
17-1=k(6-2)^2
$$

$$
\frac{16}{16}=k
$$

$$
k=1
$$

$$
\dot{y}=2(x-2)\dot{x}
$$

$$
T=\frac{1}{2}m\left[\dot{x}^{\,2}+\left(2(x-2)\dot{x}\right)^2\right]
=\frac{m}{2}\dot{x}^{\,2}\left[1+4(x-2)^2\right]
$$

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot{x}}\right)-\frac{\partial T}{\partial x}
=F_x\frac{\partial x}{\partial x}
+F_y\frac{\partial y}{\partial x}
+F_z\frac{\partial z}{\partial x}
$$

$$
m\left\{\ddot{x}\left[1+4(x-2)^2\right]
+\left[8(x-2)\dot{x}^{\,2}\right]\right\}
-\frac{m}{2}\dot{x}^{\,2}\left[8(x-2)\right]
=-mg\,2(x-2)
$$