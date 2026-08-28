```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    scale=0.88,
    decision/.style={diamond, draw=gray, thick, aspect=2.4,
                     inner sep=0pt, font=\small},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small},
    subseq/.style={draw=gray, thick, rounded corners=4pt,
                   minimum width=1.5cm, minimum height=0.6cm, font=\small}
]

% Entrada
\node[jump] (n4) at (0,0) {4};

% Rombo MRI
\node[decision] (mri) at (2.2,0) {MRI?};
\node[jump] (n6)  at (2.2,-1.5) {6};
\node[font=\scriptsize, gray] at (2.55,-0.75) {Yes};

% Número de paso 5
\node[font=\scriptsize, gray] at (1.8, 0.35) {5};

% Rombo OPR
\node[decision] (opr) at (4.8,0) {OPR?};
\node[jump] (n26) at (4.8,-1.5) {26};
\node[font=\scriptsize, gray] at (5.15,-0.75) {Yes};
\node[font=\scriptsize, gray] at (4.1, 0.35) {25};

% Rombo INT
\node[decision] (intd) at (7.4,0) {INT?};
\node[subseq]   (intseq) at (7.4,-1.5) {INT\\seq};
\node[font=\scriptsize, gray] at (7.75,-0.75) {Yes};
\node[font=\scriptsize, gray] at (6.7, 0.35) {50};

% Rombo TST
\node[decision] (tst) at (10.0,0) {TST?};
\node[subseq]   (tstseq) at (11.6,0) {TST\\seq};
\node[font=\scriptsize, gray] at (10.8, 0.25) {Yes};
\node[font=\scriptsize, gray] at (9.3, 0.35) {51};

% Salida No de TST → paso 70
\node[font=\scriptsize, gray] at (10.35,-0.75) {No};
\node[jump] (n70) at (10.0,-1.5) {70};

% Conexiones horizontales
\draw[->, thick] (n4) -- (mri);
\draw[->, thick] (mri) -- node[above, font=\scriptsize]{No} (opr);
\draw[->, thick] (opr) -- node[above, font=\scriptsize]{No} (intd);
\draw[->, thick] (intd) -- node[above, font=\scriptsize]{No} (tst);
\draw[->, thick] (tst) -- (tstseq);

% Salidas Yes (hacia abajo)
\draw[->, thick] (mri)  -- (n6);
\draw[->, thick] (opr)  -- (n26);
\draw[->, thick] (intd) -- (intseq);
\draw[->, thick] (tst)  -- (n70);

\end{tikzpicture}
\end{document}
```
