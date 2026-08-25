

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.35, >=latex]

% ============================================
% CAJA
% ============================================

\draw[thick, black!60]
    (0,0) rectangle (4,4);

% ============================================
% BARRA DIAGONAL
% ============================================

\draw[
    very thick,
    black!70
]
    (0,0) -- (4,4);

% Segunda línea para dar grosor a la barra
\draw[
    thick,
    black!30
]
    (0.08,0) -- (4,3.92);

% ============================================
% EJES DE REFERENCIA
% ============================================

% Eje x
\draw[
    ->,
    dashed,
    thick,
    black!50
]
    (-0.3,4.25) -- (1.8,4.25)
    node[right] {$x$};

% Eje y
\draw[
    ->,
    dashed,
    thick,
    black!50
]
    (-0.3,4.25) -- (-0.3,2.1)
    node[below] {$y$};

% ============================================
% PUNTO DE FIJACIÓN DEL RESORTE
% ============================================

\coordinate (A) at (0,4);

% ============================================
% MASA SOBRE LA BARRA
% ============================================

\coordinate (M) at (2.25,2.25);

% ============================================
% RESORTE
% ============================================

% Pequeño tramo inicial
\draw[
    thick,
    teal
]
    (A) -- (0.35,3.65);

% Resorte helicoidal
\draw[
    thick,
    teal,
    decoration={
        coil,
        aspect=0.35,
        segment length=5pt,
        amplitude=4pt
    },
    decorate
]
    (0.35,3.65) -- (2.05,2.45);

% Tramo final
\draw[
    thick,
    teal
]
    (2.05,2.45) -- (M);

% ============================================
% LONGITUD r
% ============================================

\node[
    teal,
    font=\large
]
    at (1.15,3.15) {$r$};

% ============================================
% ÁNGULO THETA
% ============================================

\draw[
    ->,
    blue,
    thick
]
    (0,2.9)
    arc[
        start angle=270,
        end angle=315,
        radius=1.1
    ];

\node[
    blue,
    font=\large
]
    at (0.35,3.05) {$\theta$};

% ============================================
% MASA
% ============================================

\filldraw[
    fill=orange!85,
    draw=orange!50!black,
    thick
]
    (M) circle (0.18);

\node[
    orange!80!black,
    right
]
    at (2.42,2.25) {$m$};

% ============================================
% FUERZA DEL RESORTE F_R
% ============================================

\draw[
    ->,
    red,
    very thick
]
    (M) -- (1.35,3.15)
    node[
        above left,
        red
    ] {$F_R$};

% ============================================
% PESO mg
% ============================================

\draw[
    ->,
    red,
    very thick
]
    (M) -- ++(0,-0.95)
    node[
        below,
        red
    ] {$mg$};

% ============================================
% ALTURA h
% ============================================

\draw[
    thick,
    orange
]
    (4.55,0) -- (4.55,4);

% Extremos de la cota
\draw[
    thick,
    orange
]
    (4.38,0) -- (4.72,0);

\draw[
    thick,
    orange
]
    (4.38,4) -- (4.72,4);

% Flechas de altura
\draw[
    <->,
    thick,
    orange
]
    (4.55,0.15) -- (4.55,3.85);

\node[
    orange,
    right,
    font=\large
]
    at (4.7,2) {$h$};

\end{tikzpicture}

\end{document}
```


$$
z=0
$$

$$
\nu=1
$$

$$
\begin{cases}
x\\
y\\
z\\
\theta
\end{cases}
$$

$$
y=H-x
\qquad
x=0
\qquad
y=H
$$

$$
y=-x
\qquad
y=0
\qquad
x=H
$$

$$
T=\frac{m}{2}\left(\dot{x}^{\,2}+\dot{y}^{\,2}+\dot{z}^{\,2}\right)
$$

$$
T=\frac{m}{2}\left(\dot{x}^{\,2}+\dot{x}^{\,2}\right)
=\frac{m}{2}\left(2\dot{x}^{\,2}\right)
$$

$$
T=m\dot{x}^{\,2}
$$

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot{x}}\right)
-\frac{\partial T}{\partial x}
=
F_x\frac{\partial x}{\partial x}
+
F_y\frac{\partial y}{\partial x}
+
F_z\frac{\partial z}{\partial x}
$$

$$
2m\ddot{x}
$$

$$
-k(r-\ell_0)\sin\theta
\qquad
-k(r-\ell_0)\cos\theta+mg
$$

$$
2m\ddot{x}
=
-k(r-\ell_0)\sin\theta
-k(r-\ell_0)\cos\theta
+mg
$$

$$
\sin\theta
=
\frac{x}{\sqrt{x^2+(H-x)^2}}
$$

$$
\cos\theta
=
\frac{H-x}{\sqrt{x^2+(H-x)^2}}
$$