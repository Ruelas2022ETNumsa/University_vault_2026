




```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (13,0) node[right] {Tiempo};
\foreach \x/\lbl in {0/T0, 2/T1, 4/T2, 6/T3, 8/T4, 10/T5} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.5);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.5) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.4) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
% Activo T0 → mitad T2 (x=5)
\draw[ultra thick, blue] (0, 4.2) -- (5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (2.4, 4.2) {Activo};
\draw[ultra thick, blue] (5, 4.2) -- (5, 3.7);
\draw[ultra thick, blue] (5, 3.7) -- (8.6, 3.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (6.8, 3.7) {Cede el bus};
\draw[ultra thick, blue] (8.6, 3.7) -- (8.6, 4.2);
\draw[ultra thick, blue] (8.6, 4.2) -- (12.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (10.5, 4.2) {Activo};

% === Fila 2: DMA HRQ ===
% Bajo T0 → T1 (x=2), sube
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2, 2.6);
\draw[ultra thick, orange!80!black] (2, 2.6) -- (2, 3.1);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (4.5, 3.1) {HRQ activo};
\draw[ultra thick, orange!80!black] (2, 3.1) -- (8.0, 3.1);
\draw[ultra thick, orange!80!black] (8.0, 3.1) -- (8.0, 2.6);
\draw[ultra thick, orange!80!black] (8.0, 2.6) -- (12.5, 2.6);

% === Fila 3: Bus Master ===
% CPU T0 → x=5.4
\draw[ultra thick, green!50!black] (0, 1.2) -- (5.4, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (2.4, 1.2) {CPU};
\draw[ultra thick, green!50!black] (5.4, 1.2) -- (5.4, 1.7);
% DMA x=5.4 → x=8.0
\draw[ultra thick, red!70!black] (5.4, 1.7) -- (8.0, 1.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (6.7, 1.7) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (8.0, 1.7) -- (8.0, 1.2);
\draw[ultra thick, green!50!black] (8.0, 1.2) -- (12.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (10.5, 1.2) {CPU};

% --- Guías de pasos (escaladas x2 respecto a versión anterior) ---
\draw[densely dashed, red!50, line width=0.6pt]         (0,   0) -- (0,   -4.4);
\draw[densely dashed, violet!60, line width=0.6pt]      (2,   0) -- (2,   -4.4);
\draw[densely dashed, gray!50, line width=0.6pt]        (5,   0) -- (5,   -4.4);
\draw[densely dashed, green!50!black, line width=0.6pt] (5.4, 0) -- (5.4, -4.4);
\draw[densely dashed, green!40!black, line width=0.6pt] (6.0, 0) -- (6.0, -4.4);
\draw[densely dashed, blue!50, line width=0.6pt]        (7.0, 0) -- (7.0, -4.4);
\draw[densely dashed, orange!70, line width=0.6pt]      (8.0, 0) -- (8.0, -4.4);

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!60!black]    at (0,   -0.6) {P1: DREQ activo (periférico listo)};
\node[right, font=\sffamily\scriptsize, violet]          at (2,   -1.2) {P2: HRQ activo — DMA solicita bus};
\node[right, font=\sffamily\scriptsize, gray!70!black]   at (5,   -1.8) {P3: CPU termina ciclo actual};
\node[right, font=\sffamily\scriptsize, green!60!black]  at (5.4, -2.4) {P4: HLDA — CPU cede, bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (6.0, -3.0) {P5: DACK — DMA toma el bus};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (7.0, -3.6) {P6: Transferencia directa E/S $\to$ RAM};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (8.0, -4.2) {P7: HRQ baja — bus devuelto a CPU};

\end{tikzpicture}
\end{document}
```





---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (8,0) node[right] {Tiempo};
\foreach \x/\lbl in {0/T0, 1/T1, 2/T2, 3/T3, 4/T4, 5/T5} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.5);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.5) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.4) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.2) -- (2.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (1.2, 4.2) {Activo};
\draw[ultra thick, blue] (2.5, 4.2) -- (2.5, 3.7);
\draw[ultra thick, blue] (2.5, 3.7) -- (4.3, 3.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.4, 3.7) {Cede el bus};
\draw[ultra thick, blue] (4.3, 3.7) -- (4.3, 4.2);
\draw[ultra thick, blue] (4.3, 4.2) -- (7.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (5.8, 4.2) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (1, 2.6);
\draw[ultra thick, orange!80!black] (1, 2.6) -- (1, 3.1);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (2.3, 3.1) {HRQ activo};
\draw[ultra thick, orange!80!black] (1, 3.1) -- (4.0, 3.1);
\draw[ultra thick, orange!80!black] (4.0, 3.1) -- (4.0, 2.6);
\draw[ultra thick, orange!80!black] (4.0, 2.6) -- (7.5, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (2.7, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.2, 1.2) {CPU};
\draw[ultra thick, green!50!black] (2.7, 1.2) -- (2.7, 1.7);
\draw[ultra thick, red!70!black] (2.7, 1.7) -- (4.0, 1.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.35, 1.7) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (4.0, 1.7) -- (4.0, 1.2);
\draw[ultra thick, green!50!black] (4.0, 1.2) -- (7.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (5.8, 1.2) {CPU};

% --- Guías de pasos ---
\draw[densely dashed, red!50, line width=0.6pt]         (0,   0) -- (0,   -4.4);
\draw[densely dashed, violet!60, line width=0.6pt]      (1,   0) -- (1,   -4.4);
\draw[densely dashed, gray!50, line width=0.6pt]        (2.5, 0) -- (2.5, -4.4);
\draw[densely dashed, green!50!black, line width=0.6pt] (2.7, 0) -- (2.7, -4.4);
\draw[densely dashed, green!40!black, line width=0.6pt] (3.0, 0) -- (3.0, -4.4);
\draw[densely dashed, blue!50, line width=0.6pt]        (3.5, 0) -- (3.5, -4.4);
\draw[densely dashed, orange!70, line width=0.6pt]      (4.0, 0) -- (4.0, -4.4);

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!60!black]    at (0,   -0.6) {P1: DREQ activo (periférico listo)};
\node[right, font=\sffamily\scriptsize, violet]          at (1,   -1.2) {P2: HRQ activo — DMA solicita bus};
\node[right, font=\sffamily\scriptsize, gray!70!black]   at (2.5, -1.8) {P3: CPU termina ciclo actual};
\node[right, font=\sffamily\scriptsize, green!60!black]  at (2.7, -2.4) {P4: HLDA — CPU cede, bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (3.0, -3.0) {P5: DACK — DMA toma el bus};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (3.5, -3.6) {P6: Transferencia directa E/S $\to$ RAM};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (4.0, -4.2) {P7: HRQ baja — bus devuelto a CPU};

\end{tikzpicture}
\end{document}
```


---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (11,0) node[right] {Tiempo};
\foreach \x/\lbl in {0/T0, 1/T1, 2/T2, 3/T3, 4/T4, 5/T5, 6/T6, 7/T7, 8/T8} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.5);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.5) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.4) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.2) -- (2.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (1.2, 4.2) {Activo};
\draw[ultra thick, blue] (2.5, 4.2) -- (2.5, 3.7);
\draw[ultra thick, blue] (2.5, 3.7) -- (4.3, 3.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.4, 3.7) {Cede el bus};
\draw[ultra thick, blue] (4.3, 3.7) -- (4.3, 4.2);
\draw[ultra thick, blue] (4.3, 4.2) -- (10.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (7.0, 4.2) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (1, 2.6);
\draw[ultra thick, orange!80!black] (1, 2.6) -- (1, 3.1);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (2.3, 3.1) {HRQ activo};
\draw[ultra thick, orange!80!black] (1, 3.1) -- (4.0, 3.1);
\draw[ultra thick, orange!80!black] (4.0, 3.1) -- (4.0, 2.6);
\draw[ultra thick, orange!80!black] (4.0, 2.6) -- (10.5, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (2.7, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.2, 1.2) {CPU};
\draw[ultra thick, green!50!black] (2.7, 1.2) -- (2.7, 1.7);
\draw[ultra thick, red!70!black] (2.7, 1.7) -- (4.0, 1.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.35, 1.7) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (4.0, 1.7) -- (4.0, 1.2);
\draw[ultra thick, green!50!black] (4.0, 1.2) -- (10.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (7.0, 1.2) {CPU};

% --- Guías de pasos ---
\draw[densely dashed, red!50, line width=0.6pt]         (0,   0) -- (0,   -4.4);
\draw[densely dashed, violet!60, line width=0.6pt]      (1,   0) -- (1,   -4.4);
\draw[densely dashed, gray!50, line width=0.6pt]        (2.5, 0) -- (2.5, -4.4);
\draw[densely dashed, green!50!black, line width=0.6pt] (2.7, 0) -- (2.7, -4.4);
\draw[densely dashed, green!40!black, line width=0.6pt] (3.0, 0) -- (3.0, -4.4);
\draw[densely dashed, blue!50, line width=0.6pt]        (3.5, 0) -- (3.5, -4.4);
\draw[densely dashed, orange!70, line width=0.6pt]      (4.0, 0) -- (4.0, -4.4);

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!60!black]    at (0,   -0.6) {P1: DREQ activo (periférico listo)};
\node[right, font=\sffamily\scriptsize, violet]          at (1,   -1.2) {P2: HRQ activo — DMA solicita bus};
\node[right, font=\sffamily\scriptsize, gray!70!black]   at (2.5, -1.8) {P3: CPU termina ciclo actual};
\node[right, font=\sffamily\scriptsize, green!60!black]  at (2.7, -2.4) {P4: HLDA — CPU cede, bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (3.0, -3.0) {P5: DACK — DMA toma el bus};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (3.5, -3.6) {P6: Transferencia directa E/S $\to$ RAM};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (4.0, -4.2) {P7: HRQ baja — bus devuelto a CPU};

\end{tikzpicture}
\end{document}
```


---
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (11,0) node[right] {Tiempo};
\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.5);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.5) {T\x};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.4) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
% Activo T0 → T3.5 (CPU termina su ciclo actual antes de ceder)
\draw[ultra thick, blue] (0, 4.2) -- (3.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (1.7, 4.2) {Activo};
% Baja en T3.5 (después de HLDA)
\draw[ultra thick, blue] (3.5, 4.2) -- (3.5, 3.7);
\draw[ultra thick, blue] (3.5, 3.7) -- (5.3, 3.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.4, 3.7) {Cede el bus};
% Sube en T5.3 (después de que HRQ baja + retraso)
\draw[ultra thick, blue] (5.3, 3.7) -- (5.3, 4.2);
\draw[ultra thick, blue] (5.3, 4.2) -- (10.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (7.5, 4.2) {Activo};

% === Fila 2: DMA HRQ ===
% Bajo T0 → T2 (retraso: DMA reacciona al DREQ en T1)
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2, 2.6);
% Sube en T2 (P2: HRQ activo, un ciclo después de DREQ)
\draw[ultra thick, orange!80!black] (2, 2.6) -- (2, 3.1);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.3, 3.1) {HRQ activo};
\draw[ultra thick, orange!80!black] (2, 3.1) -- (5.0, 3.1);
% Baja en T5.0 (P7: DMA libera bus tras transferencia)
\draw[ultra thick, orange!80!black] (5.0, 3.1) -- (5.0, 2.6);
\draw[ultra thick, orange!80!black] (5.0, 2.6) -- (10.5, 2.6);

% === Fila 3: Bus Master ===
% CPU T0 → T3.7 (retraso: DMA toma bus DESPUÉS del HLDA)
\draw[ultra thick, green!50!black] (0, 1.2) -- (3.7, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.7, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3.7, 1.2) -- (3.7, 1.7);
% DMA T3.7 → T5.0
\draw[ultra thick, red!70!black] (3.7, 1.7) -- (5.0, 1.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.35, 1.7) {DMA (ciclo robado)};
% Baja y CPU retoma en T5.3 (retraso post-HRQ)
\draw[ultra thick, green!50!black] (5.0, 1.7) -- (5.0, 1.2);
\draw[ultra thick, green!50!black] (5.0, 1.2) -- (10.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (7.5, 1.2) {CPU};

% --- Guías de pasos ---
\draw[densely dashed, red!50, line width=0.6pt]        (1,   0) -- (1,   -4.4);
\draw[densely dashed, violet!60, line width=0.6pt]     (2,   0) -- (2,   -4.4);
\draw[densely dashed, gray!50, line width=0.6pt]       (3.5, 0) -- (3.5, -4.4);
\draw[densely dashed, green!50!black, line width=0.6pt](3.7, 0) -- (3.7, -4.4);
\draw[densely dashed, green!40!black, line width=0.6pt](4.0, 0) -- (4.0, -4.4);
\draw[densely dashed, blue!50, line width=0.6pt]       (4.5, 0) -- (4.5, -4.4);
\draw[densely dashed, orange!70, line width=0.6pt]     (5.0, 0) -- (5.0, -4.4);

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!60!black]    at (1,   -0.6) {P1: DREQ activo (periférico listo)};
\node[right, font=\sffamily\scriptsize, violet]          at (2,   -1.2) {P2: HRQ activo — DMA solicita bus};
\node[right, font=\sffamily\scriptsize, gray!70!black]   at (3.5, -1.8) {P3: CPU termina ciclo actual};
\node[right, font=\sffamily\scriptsize, green!60!black]  at (3.7, -2.4) {P4: HLDA — CPU cede, bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (4.0, -3.0) {P5: DACK — DMA toma el bus};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (4.5, -3.6) {P6: Transferencia directa E/S $\to$ RAM};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (5.0, -4.2) {P7: HRQ baja — bus devuelto a CPU};

\end{tikzpicture}
\end{document}
```


---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Ciclos encima ---
\node[above, font=\sffamily\scriptsize, gray!70!black] at (0.75, 6.0) {C1};
\node[above, font=\sffamily\scriptsize, gray!70!black] at (2.25, 6.0) {C2};
\node[above, font=\sffamily\scriptsize, red!70!black]  at (3.75, 6.0) {C3};
\draw[red!70!black, thick] (3.0, 5.8) -- (3.0, 6.4) -- (4.5, 6.4) -- (4.5, 5.8);
\node[above, font=\sffamily\scriptsize, gray!70!black] at (5.25, 6.0) {C4};
\node[above, font=\sffamily\scriptsize, gray!70!black] at (6.75, 6.0) {C5};

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (13.5,0) node[right] {Tiempo};
\foreach \x/\lbl in {1.5/T1, 3/T2, 4.5/T3, 6/T4, 7.5/T5, 9/T6} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.2);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.2) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
% Activo hasta T2 (x=3.0), baja, cede hasta T3 (x=4.5), sube, activo
\draw[ultra thick, blue] (0, 4.0) -- (3.0, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.5, 4.0) {Activo};
\draw[ultra thick, blue] (3.0, 4.0) -- (3.0, 3.6);
\draw[ultra thick, blue] (3.0, 3.6) -- (4.5, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.75, 3.6) {Cede el bus};
\draw[ultra thick, blue] (4.5, 3.6) -- (4.5, 4.0);
\draw[ultra thick, blue] (4.5, 4.0) -- (13.0, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (9.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
% Sube en T1 (x=1.5), baja en T3 (x=4.5)
\draw[ultra thick, orange!80!black] (0, 2.6) -- (1.5, 2.6);
\draw[ultra thick, orange!80!black] (1.5, 2.6) -- (1.5, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.0, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (1.5, 3.0) -- (4.5, 3.0);
\draw[ultra thick, orange!80!black] (4.5, 3.0) -- (4.5, 2.6);
\draw[ultra thick, orange!80!black] (4.5, 2.6) -- (13.0, 2.6);

% === Fila 3: Bus Master ===
% CPU hasta T2 (x=3.0), DMA T2→T3 (3.0→4.5), CPU desde T3
\draw[ultra thick, green!50!black] (0, 1.2) -- (3.0, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.5, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3.0, 1.2) -- (3.0, 1.6);
\draw[ultra thick, red!70!black] (3.0, 1.6) -- (4.5, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.75, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (4.5, 1.6) -- (4.5, 1.2);
\draw[ultra thick, green!50!black] (4.5, 1.2) -- (13.0, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (9.0, 1.2) {CPU};

% --- Guías verticales punteadas ---
\foreach \x in {1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0} {
    \draw[densely dashed, blue!40!black, line width=0.6pt] (\x, 0) -- (\x, -4.6);
}

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!70!black]    at (1.5,  -0.6) {P1: DREQ activo};
\node[right, font=\sffamily\scriptsize, violet]          at (2.25, -1.2) {P2: HRQ $\rightarrow$ CPU};
\node[right, font=\sffamily\scriptsize, gray!50!black]   at (3.0,  -1.8) {P3: CPU termina ciclo};
\node[right, font=\sffamily\scriptsize, green!50!black]  at (3.75, -2.4) {P4: HLDA — bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (4.5,  -3.0) {P5: DACK — transf. inicia};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (5.25, -3.6) {P6: transf. directa};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (6.0,  -4.2) {P7: HRQ baja — bus devuelto};

\end{tikzpicture}
\end{document}
```



---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Ciclos encima (entre ticks) ---
\foreach \x/\lbl in {0.75/C1, 2.25/C2, 3.4/C3, 5.15/C4, 6.4/C5} {
    \node[above, font=\sffamily\scriptsize, gray!70!black] at (\x, 6.0) {\lbl};
}
% C3 resaltado (ciclo robado)
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.4, 6.0) {C3};
\draw[red!70!black, thick] (3.0, 5.8) -- (3.0, 6.4) -- (3.8, 6.4) -- (3.8, 5.8);

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (13.5,0) node[right] {Tiempo};
\foreach \x/\lbl in {1.5/T1, 3/T2, 4.5/T3, 6/T4, 7.5/T5, 9/T6} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.2);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.2) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.0) -- (3.8, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.8, 4.0) {Activo};
\draw[ultra thick, blue] (3.8, 4.0) -- (3.8, 3.6);
\draw[ultra thick, blue] (3.8, 3.6) -- (6.8, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (5.3, 3.6) {Cede el bus};
\draw[ultra thick, blue] (6.8, 3.6) -- (6.8, 4.0);
\draw[ultra thick, blue] (6.8, 4.0) -- (13.0, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (10.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (3.0, 2.6);
\draw[ultra thick, orange!80!black] (3.0, 2.6) -- (3.0, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (5.0, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (3.0, 3.0) -- (6.8, 3.0);
\draw[ultra thick, orange!80!black] (6.8, 3.0) -- (6.8, 2.6);
\draw[ultra thick, orange!80!black] (6.8, 2.6) -- (13.0, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (3.8, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.8, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3.8, 1.2) -- (3.8, 1.6);
\draw[ultra thick, red!70!black] (3.8, 1.6) -- (6.8, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (5.3, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (6.8, 1.6) -- (6.8, 1.2);
\draw[ultra thick, green!50!black] (6.8, 1.2) -- (13.0, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (10.0, 1.2) {CPU};

% --- Guías verticales punteadas ---
\foreach \x in {1.5, 3.0, 3.8, 4.5, 5.3, 6.0, 6.8} {
    \draw[densely dashed, blue!40!black, line width=0.6pt] (\x, 0) -- (\x, -4.6);
}

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!70!black]    at (1.5, -0.6) {P1: DREQ activo};
\node[right, font=\sffamily\scriptsize, violet]          at (3.0, -1.2) {P2: HRQ $\rightarrow$ CPU};
\node[right, font=\sffamily\scriptsize, gray!50!black]   at (3.8, -1.8) {P3: CPU termina ciclo};
\node[right, font=\sffamily\scriptsize, green!50!black]  at (4.5, -2.4) {P4: HLDA — bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (5.3, -3.0) {P5: DACK — transf. inicia};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (6.0, -3.6) {P6: transf. directa};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (6.8, -4.2) {P7: HRQ baja — bus devuelto};

\end{tikzpicture}
\end{document}
```


---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (13.5,0) node[right] {Tiempo};
\foreach \x/\lbl in {1.5/T1, 3/T2, 4.5/T3, 6/T4, 7.5/T5, 9/T6} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.2);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.2) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.0) -- (3.8, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.8, 4.0) {Activo};
\draw[ultra thick, blue] (3.8, 4.0) -- (3.8, 3.6);
\draw[ultra thick, blue] (3.8, 3.6) -- (6.8, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (5.3, 3.6) {Cede el bus};
\draw[ultra thick, blue] (6.8, 3.6) -- (6.8, 4.0);
\draw[ultra thick, blue] (6.8, 4.0) -- (13.0, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (10.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (3.0, 2.6);
\draw[ultra thick, orange!80!black] (3.0, 2.6) -- (3.0, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (5.0, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (3.0, 3.0) -- (6.8, 3.0);
\draw[ultra thick, orange!80!black] (6.8, 3.0) -- (6.8, 2.6);
\draw[ultra thick, orange!80!black] (6.8, 2.6) -- (13.0, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (3.8, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.8, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3.8, 1.2) -- (3.8, 1.6);
\draw[ultra thick, red!70!black] (3.8, 1.6) -- (6.8, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (5.3, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (6.8, 1.6) -- (6.8, 1.2);
\draw[ultra thick, green!50!black] (6.8, 1.2) -- (13.0, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (10.0, 1.2) {CPU};

% --- Guías verticales punteadas — color oscuro visible ---
\foreach \x in {1.5, 3.0, 3.8, 4.5, 5.3, 6.0, 6.8} {
    \draw[densely dashed, blue!40!black, line width=0.6pt] (\x, 0) -- (\x, -4.6);
}

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!70!black]    at (1.5, -0.6) {P1: DREQ activo};
\node[right, font=\sffamily\scriptsize, violet]          at (3.0, -1.2) {P2: HRQ $\rightarrow$ CPU};
\node[right, font=\sffamily\scriptsize, gray!50!black]   at (3.8, -1.8) {P3: CPU termina ciclo};
\node[right, font=\sffamily\scriptsize, green!50!black]  at (4.5, -2.4) {P4: HLDA — bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black]  at (5.3, -3.0) {P5: DACK — transf. inicia};
\node[right, font=\sffamily\scriptsize, blue!70!black]   at (6.0, -3.6) {P6: transf. directa};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (6.8, -4.2) {P7: HRQ baja — bus devuelto};

\end{tikzpicture}
\end{document}
```


---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (7.5,0) node[right] {Tiempo};
\foreach \x in {1,2,3,4,5,6} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.2);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.2) {T\x};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.0) -- (2.5, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.2, 4.0) {Activo};
\draw[ultra thick, blue] (2.5, 4.0) -- (2.5, 3.6);
\draw[ultra thick, blue] (2.5, 3.6) -- (4.5, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.5, 3.6) {Cede el bus};
\draw[ultra thick, blue] (4.5, 3.6) -- (4.5, 4.0);
\draw[ultra thick, blue] (4.5, 4.0) -- (7.0, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (6.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2, 2.6);
\draw[ultra thick, orange!80!black] (2, 2.6) -- (2, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.2, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (2, 3.0) -- (4.5, 3.0);
\draw[ultra thick, orange!80!black] (4.5, 3.0) -- (4.5, 2.6);
\draw[ultra thick, orange!80!black] (4.5, 2.6) -- (7.0, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (2.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.2, 1.2) {CPU};
\draw[ultra thick, green!50!black] (2.5, 1.2) -- (2.5, 1.6);
\draw[ultra thick, red!70!black] (2.5, 1.6) -- (4.5, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (3.5, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (4.5, 1.6) -- (4.5, 1.2);
\draw[ultra thick, green!50!black] (4.5, 1.2) -- (7.0, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (6.0, 1.2) {CPU};

% --- Guías verticales punteadas ---
\draw[dotted, gray!60] (1,   0) -- (1,   -3.8);
\draw[dotted, gray!60] (2,   0) -- (2,   -3.8);
\draw[dotted, gray!60] (2.5, 0) -- (2.5, -3.8);
\draw[dotted, gray!60] (3,   0) -- (3,   -3.8);
\draw[dotted, gray!60] (3.5, 0) -- (3.5, -3.8);
\draw[dotted, gray!60] (4,   0) -- (4,   -3.8);
\draw[dotted, gray!60] (4.5, 0) -- (4.5, -3.8);

% --- Pasos escalonados ---
\node[right, font=\sffamily\scriptsize, red!60!black]   at (1,   -0.6) {P1: DREQ activo};
\node[right, font=\sffamily\scriptsize, violet]         at (2,   -1.2) {P2: HRQ $\rightarrow$ CPU};
\node[right, font=\sffamily\scriptsize, gray!70!black]  at (2.5, -1.8) {P3: CPU termina ciclo};
\node[right, font=\sffamily\scriptsize, green!50!black] at (3,   -2.4) {P4: HLDA — bus libre};
\node[right, font=\sffamily\scriptsize, green!40!black] at (3.5, -3.0) {P5: DACK — transf. inicia};
\node[right, font=\sffamily\scriptsize, blue!70!black]  at (4,   -3.6) {P6: transf. directa};
\node[right, font=\sffamily\scriptsize, orange!80!black] at (4.5, -4.2) {P7: HRQ baja — bus devuelto};

\end{tikzpicture}
\end{document}
```



---

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

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.0) -- (3, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.5, 4.0) {Activo};
\draw[ultra thick, blue] (3, 4.0) -- (3, 3.6);
\draw[ultra thick, blue] (3, 3.6) -- (5, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 3.6) {Cede el bus};
\draw[ultra thick, blue] (5, 3.6) -- (5, 4.0);
\draw[ultra thick, blue] (5, 4.0) -- (9.5, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (7.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2.5, 2.6);
\draw[ultra thick, orange!80!black] (2.5, 2.6) -- (2.5, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.8, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (2.5, 3.0) -- (5, 3.0);
\draw[ultra thick, orange!80!black] (5, 3.0) -- (5, 2.6);
\draw[ultra thick, orange!80!black] (5, 2.6) -- (9.5, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (3, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.5, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3, 1.2) -- (3, 1.6);
\draw[ultra thick, red!70!black] (3, 1.6) -- (5, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (5, 1.6) -- (5, 1.2);
\draw[ultra thick, green!50!black] (5, 1.2) -- (9.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (7.0, 1.2) {CPU};

% --- Pasos escalonados debajo del eje ---
% Línea guía vertical punteada por paso
\draw[dotted, gray!60] (1,   0) -- (1,   -3.8);
\draw[dotted, gray!60] (2.5, 0) -- (2.5, -3.8);
\draw[dotted, gray!60] (3,   0) -- (3,   -3.8);
\draw[dotted, gray!60] (3.5, 0) -- (3.5, -3.8);
\draw[dotted, gray!60] (4,   0) -- (4,   -3.8);
\draw[dotted, gray!60] (4.5, 0) -- (4.5, -3.8);
\draw[dotted, gray!60] (5,   0) -- (5,   -3.8);

% P1 — columna 1 (x=1), fila -0.6
\node[right, font=\sffamily\scriptsize, red!60!black]        at (1,   -0.6) {P1: DREQ activo};

% P2 — columna 2.5, fila -1.2
\node[right, font=\sffamily\scriptsize, violet]              at (2.5, -1.2) {P2: HRQ $\rightarrow$ CPU};

% P3 — columna 3, fila -1.8
\node[right, font=\sffamily\scriptsize, gray!70!black]       at (3,   -1.8) {P3: CPU termina ciclo};

% P4 — columna 3.5, fila -2.4
\node[right, font=\sffamily\scriptsize, green!50!black]      at (3.5, -2.4) {P4: HLDA — bus libre};

% P5 — columna 4, fila -3.0
\node[right, font=\sffamily\scriptsize, green!40!black]      at (4,   -3.0) {P5: DACK — transf. inicia};

% P6 — columna 4.5, fila -3.6 (solo marca, descripción en tabla)
\node[right, font=\sffamily\scriptsize, blue!70!black]       at (4.5, -3.6) {P6: transf. directa};

% P7 — columna 5, fila -4.2
\node[right, font=\sffamily\scriptsize, orange!80!black]     at (5,   -4.2) {P7: HRQ baja — bus devuelto};

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


---

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

% --- Pasos P1-P7 sobre ticks ---
\node[above, font=\sffamily\scriptsize, red!60!black] at (1, 5.6) {P1};
\node[above, font=\sffamily\scriptsize, violet] at (2.5, 5.6) {P2};
\node[above, font=\sffamily\scriptsize, gray] at (3, 5.6) {P3};
\node[above, font=\sffamily\scriptsize, green!50!black] at (3.5, 5.6) {P4};
\node[above, font=\sffamily\scriptsize, green!40!black] at (4, 5.6) {P5};
\node[above, font=\sffamily\scriptsize, blue!70!black] at (4.5, 5.6) {P6};
\node[above, font=\sffamily\scriptsize, orange!80!black] at (5, 5.6) {P7};

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.2) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.0) -- (3, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (1.5, 4.0) {Activo};
\draw[ultra thick, blue] (3, 4.0) -- (3, 3.6);
\draw[ultra thick, blue] (3, 3.6) -- (5, 3.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 3.6) {Cede el bus};
\draw[ultra thick, blue] (5, 3.6) -- (5, 4.0);
\draw[ultra thick, blue] (5, 4.0) -- (9.5, 4.0);
\node[above, font=\sffamily\scriptsize, blue] at (7.0, 4.0) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2.5, 2.6);
\draw[ultra thick, orange!80!black] (2.5, 2.6) -- (2.5, 3.0);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (3.8, 3.0) {HRQ activo};
\draw[ultra thick, orange!80!black] (2.5, 3.0) -- (5, 3.0);
\draw[ultra thick, orange!80!black] (5, 3.0) -- (5, 2.6);
\node[below, font=\sffamily\scriptsize, orange!80!black] at (5.0, 2.6) {P7};
\draw[ultra thick, orange!80!black] (5, 2.6) -- (9.5, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (3, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (1.5, 1.2) {CPU};
\draw[ultra thick, green!50!black] (3, 1.2) -- (3, 1.6);
\draw[ultra thick, red!70!black] (3, 1.6) -- (5, 1.6);
\node[above, font=\sffamily\scriptsize, red!70!black] at (4.0, 1.6) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (5, 1.6) -- (5, 1.2);
\draw[ultra thick, green!50!black] (5, 1.2) -- (9.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (7.0, 1.2) {CPU};

% --- Anotaciones eje inferior ---
\node[below, font=\sffamily\scriptsize, gray] at (2.5, 0.2) {P2};
\node[below, font=\sffamily\scriptsize, gray] at (3.0, 0.2) {P3/P4};
\node[below, font=\sffamily\scriptsize, gray] at (4.0, 0.2) {P5};
\node[below, font=\sffamily\scriptsize, gray] at (5.0, 0.2) {P7};

\end{tikzpicture}
\end{document}
```



