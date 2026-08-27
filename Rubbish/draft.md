```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% ---- CONSTANTES ----
% Cada celda: 0.65 de ancho, 0.7 de alto
% Bit i comienza en x = i*0.65

% ---- FILA DE BITS ----
% Bits 0-5: OP con valores 1,1,1,1,0,1
\foreach \i/\v in {0/1, 1/1, 2/1, 3/1, 4/0, 5/1} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
    \node[font=\small] at (\i*0.65+0.325, 0.35) {\v};
}

% Bits 6, 7, 8 — individuales vacíos
\foreach \i in {6,7,8} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
}

% Bit 9 — Input/Output (individual)
\draw[thick] (9*0.65, 0) rectangle (9*0.65+0.65, 0.7);

% Bits 10-11-12 — Device code (bloque de 3)
\draw[thick] (10*0.65, 0) rectangle (10*0.65+1.95, 0.7);

% Bits 12... espera, en la imagen bits 10,11 = device code, 12-17 = control code
% Corregido: bits 10-11 son device code (2 celdas), bits 12-17 son control code (bloque)
% Rehago: device code = bits 10 y 11 (2 celdas individuales)
% Cancelamos el bloque anterior y hacemos 2 individuales + bloque grande

\end{tikzpicture}
\end{document}
```
