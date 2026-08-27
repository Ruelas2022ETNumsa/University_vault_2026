```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    scale=0.9,
    decision/.style={diamond, draw=gray, thick, aspect=2.2,
                     inner sep=1pt, font=\small},
    operation/.style={draw=teal, thick, minimum width=2.8cm,
                      minimum height=0.6cm, font=\small},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Nodo de entrada (salto desde paso anterior)
\node[jump] (n24) at (0,0) {24};

% Rombo 1
\node[decision] (mri) at (0,-1.4) {MRI?};
\node[font=\small, gray] at (-1.2,-1.4) {Nox};
\node[font=\small, gray] at (0.2,-2.1) {Yes};

% Salto Yes hacia (6)
\node[jump] (n6) at (0,-2.8) {6};

% Rombo 2 (rama No del primero)
\node[decision] (opr) at (2.8,-1.4) {OPR?};
\node[font=\small, gray] at (4.1,-1.4) {No};
\node[font=\small, gray] at (2.8,-2.1) {Yes};

% Salto Yes hacia (26)
\node[jump] (n26) at (2.8,-2.8) {26};

% Operación (rama No de OPR)
\node[operation] (op1) at (5.8,-1.4) {$CSR \leftarrow IR_{8:17}$};

% Conexiones
\draw[->, thick] (n24) -- (mri);
\draw[->, thick] (mri) -- node[left, font=\small]{Yes} (n6);
\draw[->, thick] (mri) -- node[above, font=\small]{No} (opr);
\draw[->, thick] (opr) -- node[left, font=\small]{Yes} (n26);
\draw[->, thick] (opr) -- node[above, font=\small]{No} (op1);

\end{tikzpicture}
\end{document}
```

