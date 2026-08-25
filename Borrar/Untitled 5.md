```tikz
\begin{tikzpicture}[scale=1.2, >=stealth]

\begin{tikzpicture}[scale=1.2, >=stealth]

% Rueda
\draw[thick] (0,0) circle (2);

% Centro
\fill (0,0) circle (2pt);
\node[below left] at (0,0) {$O$};

% Radio
\draw[thick] (0,0) -- (1.55,1.27);
\node[above] at (0.8,0.7) {$R$};

% Angulo theta
\draw[->] (0.7,0) arc (0:39:0.7);
\node at (0.75,0.25) {$\theta$};

% Eje x
\draw[->] (-0.5,0) -- (4.5,0);
\node[right] at (4.5,0) {$x$};

% Punto donde sale la cuerda
\fill (1.55,1.27) circle (2pt);

% Cuerda alrededor de la rueda
\draw[thick] (1.55,1.27)
    arc (39:-65:2);

% Cuerda que sostiene la masa
\draw[thick] (2.82,-1.81) -- (3.65,-4.2);

% Linea auxiliar vertical
\draw[dashed] (2.82,1.27) -- (2.82,-4.2);

% Distancia d
\draw[<->] (3.05,-1.7) -- (3.85,-4.05);
\node[right] at (3.5,-2.8) {$d$};

% Angulo phi
\draw[->] (2.82,-1.1) arc (-90:-70:0.6);
\node[right] at (3.1,-1.0) {$\varphi$};

% Masa
\draw[thick] (3.65,-4.2) circle (0.28);
\node[below] at (3.65,-4.5) {$m$};

% Peso
\draw[->,thick] (3.65,-4.5) -- (3.65,-5.3);
\node[right] at (3.65,-4.9) {$mg$};

% Relacion
\node at (0,-3) {$d=\ell+\theta R$};

\end{tikzpicture}

\end{tikzpicture}
```