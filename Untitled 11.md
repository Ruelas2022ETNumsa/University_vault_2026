```tikz
\begin{document}

\begin{tikzpicture}[>=stealth, scale=1.2]

% Ejes
\draw[->, thick, teal] (-0.3,0) -- (6.8,0)
    node[right] {$x$};

\draw[->, thick, teal] (0,-0.2) -- (0,4.2)
    node[above] {$y$};

% Origen
\node[below left] at (0,0) {$O$};

% Semicircunferencia
\draw[thick, teal]
    (0,0) arc (180:0:3);

% Barra inclinada
\draw[thick, orange]
    (0,0) -- (5.25,2);

% Resorte
\draw[thick, orange]
    (1.8,0.68)
    -- (1.95,1.15)
    -- (2.10,0.85)
    -- (2.25,1.32)
    -- (2.40,1.02)
    -- (2.55,1.48)
    -- (2.70,1.18)
    -- (2.85,1.65);

% Etiqueta k
\node[teal] at (2.3,1.8) {$k$};

% Masa
\draw[thick, orange]
    (5.00,2.05)
    -- (5.25,2.35)
    -- (5.60,2.10)
    -- (5.35,1.80)
    -- cycle;

% Rayas de la masa
\draw[orange] (5.05,2.00) -- (5.20,2.30);
\draw[orange] (5.15,1.92) -- (5.35,2.25);
\draw[orange] (5.28,1.86) -- (5.48,2.16);

% Etiqueta m
\node[teal] at (5.85,2.30) {$m$};

% Centro
\fill (3,0) circle (2pt);

% Radio R
\draw[thick, red]
    (3,0) -- (5.25,2);

% Etiqueta R
\node[red] at (4.45,0.75) {$R$};

% Ángulo theta
\draw[orange]
    (1,0) arc (0:21:1);

\node[orange] at (1.15,0.35) {$\theta$};

\end{tikzpicture}

\end{document}
```
