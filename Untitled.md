


```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.82,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=3.0cm,
                      minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entradas
\node[jump] (n72) at (-2, 0)  {72};
\node[jump] (n73) at ( 2, 0)  {73};
\node[jump] (n85) at ( 2, 1.2) {85};

% Rombo COMMAND (72)
\node[font=\scriptsize, gray, above] at (-2,0.5) {COMMAND};

% Rombo BUFFER
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (buf) at (0,-1.2) {BUFFER?};
\draw[->, thick] (n72) -- (buf);
\draw[->, thick] (n73) -- (buf);
\draw[->, thick] (n85) -- (n73);

% Salto BUFFER=Yes → (85) (vuelve arriba)
\draw[->, thick] (buf.east) -- ++(1.8,0) -- ++(0,2.4) -- (n85);
\node[font=\scriptsize, gray, above] at (1.5,-1.8) {Yes};

% Op 78: ready=1 (Input, BUFFER=No)
\node[operation] (op78) at (0,-2.8) {$ready \leftarrow 1$};
\node[font=\scriptsize, gray, left] at (-2.0,-2.5) {78};
\draw[->, thick] (buf) -- node[left, font=\scriptsize]{No (Input)} (op78);

% Rombo datavalid (bucle espera)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dvw) at (0,-4.2) {datavalid?};
\draw[->, thick] (op78) -- (dvw);

% Rombo DATA (79 rama)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dat1) at (0,-5.8) {DATA?};
\draw[->, thick] (dvw) -- node[right, font=\scriptsize]{Yes} (dat1);

% Bucle No de datavalid → vuelve
\draw[thick,->] (dvw.west) -- ++(-2.0,0) -- ++(0,1.45) -- (-1.8,-2.75);
\node[font=\scriptsize, gray, above] at (-1.4,-4.2) {No};

% Op 79 Yes: MD←IOBUS y CSR←CSBUS (simultáneo)
\node[operation] (op79) at (-2.2,-7.4)
    {$MD \leftarrow IOBUS$\\$CSR \leftarrow CSBUS$};
\node[font=\scriptsize, gray, left] at (-4,-7.1) {79};
\draw[->, thick] (dat1) -- node[left, font=\scriptsize]{Yes} (op79);

% accept=1
\node[operation] (accop) at (-2.2,-8.8) {$accept \leftarrow 1$};
\draw[->, thick] (op79) -- (accop);

% Rombo datavalid (80)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dv80) at (-2.2,-10.2) {datavalid?};
\draw[->, thick] (accop) -- (dv80);
\node[font=\scriptsize, gray, left] at (-3.4,-10.4) {80};

% Rombo DATA (81)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (dat81) at (-2.2,-11.6) {DATA?};
\draw[->, thick] (dv80) -- node[right, font=\scriptsize]{No} (dat81);
\node[font=\scriptsize, gray, left] at (-3.4,-11.6) {81};

% Bucle Yes de dv80 → vuelve a op79
\draw[thick,->] (dv80.west) -- ++(-2.0,0) -- ++(0,2.9) -- (-4.0,-7.35);
\node[font=\scriptsize, gray, above] at (-3.6,-10.2) {Yes};

% AC←MD (82)
\node[operation] (op82) at (3.0,-11.6) {$AC \leftarrow MD$};
\node[font=\scriptsize, gray, right] at (4.8,-11.6) {82};
\draw[->, thick] (dat1)  -- node[above left, font=\scriptsize]{No}  (op82);
\draw[->, thick] (dat81) -- node[above, font=\scriptsize]{Yes} (op82);

% AC←MD → (24)
\node[jump] (n24c) at (3.0,-13.0) {24};
\draw[->, thick] (op82) -- (n24c);

% Rombo SKIP (83)
\node[font=\small, draw=gray, thick,
      diamond, aspect=2.2, inner sep=1pt] (sk) at (-2.2,-13.0) {SKIP?};
\draw[->, thick] (dat81) -- node[right, font=\scriptsize]{No} (sk);
\node[font=\scriptsize, gray, left] at (-3.4,-13.0) {83};

% Op 84: PC←INC(PC)
\node[operation] (op84) at (-2.2,-14.4) {$PC \leftarrow INC(PC)$};
\draw[->, thick] (sk) -- node[right, font=\scriptsize]{Yes} (op84);
\node[font=\scriptsize, gray, left] at (-4.2,-14.4) {84};

% Salida (24) desde 84
\node[jump] (n24a) at (-2.2,-15.6) {24};
\draw[->, thick] (op84) -- (n24a);

% SKIP No → mismo (24) que AC←MD
\draw[->, thick] (sk) -- node[above, font=\scriptsize]{No} (n24c);


\end{tikzpicture}
\end{document}
```
