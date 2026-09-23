```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.0, >=latex]

% Colores
\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% =================================================
% PARED IZQUIERDA
% =================================================

\fill[pattern=north east lines]
    (-0.5,0) rectangle (0,2);

\draw[thick]
    (0,0) -- (0,2);


% =================================================
% PISO HORIZONTAL
% =================================================

\fill[pattern=north east lines]
    (0,-0.2) rectangle (5.5,0);

\draw[thick]
    (0,0) -- (5.5,0);


% =================================================
% RESORTE K
% =================================================

\draw[
    decorate,
    decoration={
        coil,
        aspect=0.3,
        segment length=2mm,
        amplitude=3mm
    },
    maincolor,
    thick
]
    (0,0.7) -- (1.5,0.7);

\node[above, maincolor]
    at (0.75,0.9) {$K$};


% =================================================
% BLOQUE m1
% =================================================

\draw[
    fill=teal!10,
    draw=maincolor,
    thick
]
    (1.5,0) rectangle (2.8,1.4);

\node[maincolor]
    at (2.15,0.7) {$m_1$};


% =================================================
% CUERDA HORIZONTAL
% =================================================

\draw[thick]
    (2.8,1.0) -- (5.2,1.0);


% =================================================
% POLEA
% Centro de la polea = (5.5,0.7)
% =================================================

\draw[
    thick,
    fill=gray!20
]
    (5.5,0.7) circle (0.3);

\fill
    (5.5,0.7) circle (0.05);


% Soporte de la polea
\draw[thick]
    (5.5,0) -- (5.5,0.4);


% =================================================
% CUERDA VERTICAL
% Tangente al lado derecho de la polea
% =================================================

\draw[thick]
    (5.8,0.7) -- (5.8,-1.0);


% =================================================
% PARED VERTICAL
% =================================================

\fill[pattern=north east lines]
    (4.5,-4) rectangle (5,0);

\draw[thick]
    (5,-4) -- (5,0);


% =================================================
% BLOQUE m2
% =================================================

\draw[
    fill=teal!10,
    draw=maincolor,
    thick
]
    (5,-1.7) rectangle (6,-1.0);

\node[maincolor]
    at (5.5,-1.35) {$m_2$};


% =================================================
% RESORTE K'
% =================================================

\draw[
    decorate,
    decoration={
        coil,
        aspect=0.3,
        segment length=2mm,
        amplitude=2.5mm
    },
    accentcolor,
    thick
]
    (5.5,-1.7) -- (5.5,-2.8);

\node[right, accentcolor]
    at (5.7,-2.25) {$K'$};


% =================================================
% BLOQUE m3
% =================================================

\draw[
    fill=orange!10,
    draw=accentcolor,
    thick
]
    (5,-3.5) rectangle (6,-2.8);

\node[accentcolor]
    at (5.5,-3.15) {$m_3$};


% =================================================
% COORDENADA x1
% Pared -> centro de m1
% =================================================

\draw[<->, maincolor, thick]
    (0,2.1) -- (2.15,2.1)
    node[midway, above] {$x_1$};

% Referencia de la pared
\draw[dotted]
    (0,1.8) -- (0,2.3);

% Referencia del centro de m1
\draw[dotted]
    (2.15,0.7) -- (2.15,2.3);


% =================================================
% COORDENADA y2
% Centro de m1 -> centro de m2
% =================================================

\draw[<->, maincolor, thick]
    (6.7,0.7) -- (6.7,-1.35)
    node[midway, right] {$y_2$};

% Línea desde centro de m1
\draw[dotted]
    (2.15,0.7) -- (6.7,0.7);

% Línea hasta centro de m2
\draw[dotted]
    (5.5,-1.35) -- (6.7,-1.35);


% =================================================
% COORDENADA y3
% Centro de m1 -> centro de m3
% =================================================

\draw[<->, accentcolor, thick]
    (7.5,0.7) -- (7.5,-3.15)
    node[midway, right] {$y_3$};

% Línea desde centro de m1
\draw[dotted]
    (2.15,0.7) -- (7.5,0.7);

% Línea hasta centro de m3
\draw[dotted]
    (5.5,-3.15) -- (7.5,-3.15);


\end{tikzpicture}

\end{document}
```
