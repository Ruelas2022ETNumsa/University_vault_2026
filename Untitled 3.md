```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[node distance=2cm, font=\sffamily\small]

\draw [thick, ->] (0,0) -- (10,0) node [right] {Tiempo};
\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw [dashed, gray!50] (\x, -1) -- (\x, 4);
    \node [above] at (\x, 4) {T\x};
}
\node [left] at (0, 3) {CPU Bus Access};
\draw [ultra thick, blue] (0, 3) -- (3, 3) node [midway, above] {Activo}
                         -- (3, 2.2) -- (5, 2.2) node [midway, above, red] {Cede el bus}
                         -- (5, 3) -- (9, 3) node [midway, above] {Activo};
\node [left] at (0, 1.5) {DMA HRQ};
\draw [ultra thick, orange] (0, 1.2) -- (2.5, 1.2) -- (2.5, 1.8) node [above right] {HRQ}
                           -- (5, 1.8) -- (5, 1.2) -- (9, 1.2);
\node [left] at (0, 0.5) {Bus Master};
\draw [ultra thick, green!60!black] (0, 0.5) -- (3, 0.5) node [midway, below] {CPU}
                                   -- (5, 0.5) node [midway, below, red] {DMA (ciclo robado)}
                                   -- (9, 0.5) node [midway, below] {CPU};
\end{tikzpicture}
\end{document}
```

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (10.5,0) node[right] {Tiempo};
\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.2);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.2) {T\x};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus (y base = 4.0, alto = 4.4) ===
% Activo T0-T3
\draw[ultra thick, blue] (0, 4.0) -- (3, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.5, 4.0) {Activo};
% Bajada T3
\draw[ultra thick, blue] (3, 4.0) -- (3, 3.6);
% Cede el bus T3-T5
\draw[ultra thick, blue] (3, 3.6) -- (5, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 3.6) {Cede el bus};
% Subida T5
\draw[ultra thick, blue] (5, 3.6) -- (5, 4.0);
% Activo T5-T9
\draw[ultra thick, blue] (5, 4.0) -- (9.5, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (7.0, 4.0) {Activo};

% === Fila 2: DMA HRQ (y base = 2.6, alto = 3.0) ===
% Bajo T0-T2.5
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2.5, 2.6);
% Subida T2.5 (HRQ activo)
\draw[ultra thick, orange!80!black] (2.5, 2.6) -- (2.5, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.8, 3.0) {HRQ activo};
% Alto T2.5-T5
\draw[ultra thick, orange!80!black] (2.5, 3.0) -- (5, 3.0);
% Bajada T5 (HRQ desactiva — P7)
\draw[ultra thick, orange!80!black] (5, 3.0) -- (5, 2.6);
\node[below, font=\sffamily\scriptsize, orange!80!black] at (5.0, 2.6) {P7};
% Bajo T5-T9
\draw[ultra thick, orange!80!black] (5, 2.6) -- (9.5, 2.6);

% === Fila 3: Bus Master (y base = 1.2, alto = 1.6) ===
% CPU T0-T3
\draw[ultra thick, green!50!black] (0, 1.2) -- (3, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.5, 1.2) {CPU};
% Bajada
\draw[ultra thick, green!50!black] (3, 1.2) -- (3, 1.6);
% DMA T3-T5
\draw[ultra thick, red!70!black] (3, 1.6) -- (5, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 1.6) {DMA (ciclo robado)};
% Bajada
\draw[ultra thick, green!50!black] (5, 1.6) -- (5, 1.2);
% CPU T5-T9
\draw[ultra thick, green!50!black] (5, 1.2) -- (9.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (7.0, 1.2) {CPU};

% --- Anotación P2 (HRQ sube) ---
\draw[dashed, gray!60] (2.5, 0.2) -- (2.5, 2.6);
\node[below, font=\sffamily\scriptsize, gray] at (2.5, 0.2) {P2};

% --- Anotación P4 (HLDA / bus libre) ---
\node[below, font=\sffamily\scriptsize, gray] at (3.0, 0.2) {P4};

% --- Anotación P5 (DACK) ---
\node[below, font=\sffamily\scriptsize, gray] at (3.5, 0.2) {P5};

\end{tikzpicture}
\end{document}
```




