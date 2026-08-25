
```tikz
\begin{tikzpicture}[
    >=stealth,
    line cap=round,
    line join=round,
    scale=1.15
]

% -------------------------------------------------
% Parámetros geométricos
% -------------------------------------------------
\def\R{2.0}
\def\ang{35}

% Centro de la circunferencia
\coordinate (O) at (0,0);

% Punto de tangencia
\coordinate (P) at ({\R*cos(\ang)},{\R*sin(\ang)});

% Dirección tangente (hacia abajo-derecha)
\coordinate (T) at ({\R*cos(\ang)+2.7*sin(\ang)},
                     {\R*sin(\ang)-2.7*cos(\ang)});

% Punto de la masa
\coordinate (M) at ({\R*cos(\ang)+3.5*sin(\ang)},
                     {\R*sin(\ang)-3.5*cos(\ang)});

% -------------------------------------------------
% Circunferencia
% -------------------------------------------------
\draw[thick] (O) circle (\R);

% -------------------------------------------------
% Ejes coordenados
% -------------------------------------------------
\draw[->,thick,red] (O) -- (4.0,0)
    node[right] {$x$};

\draw[->,thick,red] (O) -- (0,-3.2)
    node[below] {$y$};

% Origen
\node[red,left] at (O) {$O$};

% -------------------------------------------------
% Radio
% -------------------------------------------------
\draw[thick,teal] (O) -- (P)
    node[midway,above left] {$R$};

% -------------------------------------------------
% Línea vertical auxiliar
% -------------------------------------------------
\draw[dashed,orange,thick]
    (P) -- ({\R*cos(\ang)},-2.8);

% Longitud l
\draw[<->,orange,thick]
    ({\R*cos(\ang)+0.18},0)
    -- ({\R*cos(\ang)+0.18},-2.35)
    node[midway,right] {$\ell$};

% -------------------------------------------------
% Ángulo theta en el centro
% -------------------------------------------------
\draw[->,teal,thick]
    (0.65,0) arc[start angle=0,end angle=\ang,radius=0.65];

\node[teal] at (0.72,0.25) {$\theta$};

% -------------------------------------------------
% Tangente / cuerda
% -------------------------------------------------
\draw[very thick,black]
    (P) -- (M);

% -------------------------------------------------
% Longitud desarrollada theta R
% -------------------------------------------------
\draw[<->,blue,thick]
    ({\R*cos(\ang)+0.12},{\R*sin(\ang)+0.12})
    -- ({\R*cos(\ang)+1.75*sin(\ang)+0.12},
        {\R*sin(\ang)-1.75*cos(\ang)+0.12})
    node[midway,right] {$\theta R$};

% -------------------------------------------------
% Distancia total d = l + theta R
% -------------------------------------------------
\node[orange] at (2.9,-0.25)
    {$d=\ell+\theta R$};

% -------------------------------------------------
% Ángulo theta respecto a la vertical
% -------------------------------------------------
\draw[->,teal,thick]
    ({\R*cos(\ang)},{\R*sin(\ang)-0.65})
    arc[start angle=90,end angle={90-\ang},radius=0.65];

\node[teal] at ({\R*cos(\ang)+0.15},
                {\R*sin(\ang)-0.95})
    {$\theta$};

% -------------------------------------------------
% Masa
% -------------------------------------------------
\fill[orange] (M) circle (0.22);

% -------------------------------------------------
% Fuerza de tensión T
% -------------------------------------------------
\draw[->,red,very thick]
    ({M}-0.05,-0.05)
    -- ({M}-0.55,0.85)
    node[left] {$T$};

% -------------------------------------------------
% Peso mg
% -------------------------------------------------
\draw[->,red,very thick]
    (M) -- ++(0,-1.0)
    node[below] {$mg$};

% -------------------------------------------------
% Pequeños puntos de referencia
% -------------------------------------------------
\fill[orange] (-1.85,0) circle (0.10);
\fill[orange] ({\R*cos(\ang)},-2.8) circle (0.10);

% -------------------------------------------------
% Etiqueta del ejercicio
% -------------------------------------------------
\node[orange,font=\large] at (-1.8,3.0) {Ejercicio};

\end{tikzpicture}
```

$$
T = \frac{m}{2}(l+\theta R)^2\dot{\theta}^{\,2}
$$

$$
T = \frac{m}{2}(\dot{x}^{\,2}+\dot{y}^{\,2})
$$

$$
T = \frac{m}{2}\left(\dot{x}^{\,2}+64x^2\dot{x}^{\,2}\right)
$$

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot{\theta}}\right)
-\frac{\partial T}{\partial\theta}
=
F_x\frac{\partial x}{\partial\theta}
+
F_y\frac{\partial y}{\partial\theta}
$$

$$
F_y=-\left(l+\theta R\right)mg\sin\theta
$$

$$
m\left[
2(l+\theta R)R\dot{\theta}^{\,2}
+(l+\theta R)^2\ddot{\theta}
\right]
-\frac{m}{2}\dot{\theta}^{\,2}(l+\theta R)R
$$

$$
\begin{cases}
x=R\cos\theta+(l+\theta R)\sin\theta\\
y=-R\sin\theta+(l+\theta R)\cos\theta
\end{cases}
$$

$$
\begin{cases}
\dot{x}=-R\sin\theta\,\dot{\theta}
+R\sin\theta\,\dot{\theta}
+(l+\theta R)\cos\theta\,\dot{\theta}\\
\dot{y}=-R\cos\theta\,\dot{\theta}
+R\cos\theta\,\dot{\theta}
-(l+\theta R)\sin\theta\,\dot{\theta}
\end{cases}
$$

$$
m\left[
(l+\theta R)R\dot{\theta}^{\,2}
+(l+\theta R)^2\ddot{\theta}
\right]
=
-mg(l+\theta R)\sin\theta
$$

$$
R\dot{\theta}^{\,2}+(l+\theta R)\ddot{\theta}
=
g\sin\theta
$$
