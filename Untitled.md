```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% ---- FILA DE BITS ----
% Bits 0-5: OP con valores 1,1,1,1,0,1
\foreach \i/\v in {0/1, 1/1, 2/1, 3/1, 4/0, 5/1} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
    \node[font=\small] at (\i*0.65+0.325, 0.35) {\v};
}

% Bits 6-11 — celdas individuales vacías
\foreach \i in {6,7,8,9,10,11} {
    \draw[thick] (\i*0.65, 0) rectangle (\i*0.65+0.65, 0.7);
}

% Bits 12-17 — Control code: bloque grande
\draw[thick] (12*0.65, 0) rectangle (18*0.65, 0.7);

% ---- ETIQUETA IZQUIERDA ----
\node[font=\small, left] at (0, 0.35) {IOT};

% ---- ETIQUETA "OP" ARRIBA (centrada sobre bits 0-5) ----
\draw[thin] (0, 0.85) -- (0, 1.0) -- (1.95, 1.0) -- (1.95, 1.1);
\draw[thin] (3.9, 0.85) -- (3.9, 1.0) -- (1.95, 1.0);
\node[font=\small] at (1.95, 1.3) {OP};

% ---- ÍNDICES DE BIT ----
\foreach \i/\lbl in {0/0, 5/5, 6/6, 7/7, 8/8, 9/9, 10/10, 11/11, 12/12, 17/17} {
    \node[font=\scriptsize] at (\i*0.65+0.325, -0.2) {\lbl};
}

% ---- ETIQUETA "Device code (n)" — sobre bits 6-7-8 ----
\node[font=\scriptsize, align=center] at (7*0.65+0.325, 2.0) {Device\\code (\textbf{n})};
\draw[gray, thin] (6*0.65, 0.85) -- (6*0.65, 1.5) -- (7*0.65+0.325, 1.5);
\draw[gray, thin] (8*0.65+0.65, 0.85) -- (8*0.65+0.65, 1.5) -- (7*0.65+0.325, 1.5);
\draw[gray, thin, ->] (7*0.65+0.325, 1.5) -- (7*0.65+0.325, 1.7);

% ---- ETIQUETA "Control code" — sobre bits 12-17 ----
\node[font=\scriptsize] at (15*0.65, 2.0) {Control code};
\draw[gray, thin] (12*0.65, 0.85) -- (12*0.65, 1.5) -- (15*0.65, 1.5);
\draw[gray, thin] (18*0.65, 0.85) -- (18*0.65, 1.5) -- (15*0.65, 1.5);

% ---- ANOTACIONES IZQUIERDA ----
% Texto alineado a la derecha, llaves, flechas hacia bits 6, 7, 8

% Bit 9 → 1=Command / 0=Transfer
\node[font=\scriptsize, anchor=east] at (3.5, -1.5) {$1 =$ Command};
\node[font=\scriptsize, anchor=east] at (3.5, -1.9) {$0 =$ Transfer};
\draw[thick] (3.55, -1.3) -- (3.8, -1.3) -- (3.8, -2.1) -- (3.55, -2.1);
\draw[->, gray, thin] (3.8, -1.7) -- (9*0.65+0.325, -1.7) -- (9*0.65+0.325, 0);

% Bit 10 → 1=Status / 0=Data
\node[font=\scriptsize, anchor=east] at (3.5, -2.7) {$1 =$ Status};
\node[font=\scriptsize, anchor=east] at (3.5, -3.1) {$0 =$ Data};
\draw[thick] (3.55, -2.5) -- (3.8, -2.5) -- (3.8, -3.3) -- (3.55, -3.3);
\draw[->, gray, thin] (3.8, -2.9) -- (10*0.65+0.325, -2.9) -- (10*0.65+0.325, 0);

% Bit 10 → 1=Command / 0=Buffer
\node[font=\scriptsize, anchor=east] at (3.5, -3.9) {$1 =$ Command};
\node[font=\scriptsize, anchor=east] at (3.5, -4.3) {$0 =$ Buffer};
\draw[thick] (3.55, -3.7) -- (3.8, -3.7) -- (3.8, -4.5) -- (3.55, -4.5);
\draw[->, gray, thin] (3.8, -4.1) -- (10*0.65+0.325, -4.1) -- (10*0.65+0.325, 0);

% ---- CONEXIONES ENTRE GRUPOS ----
% De a-Command (y=-1.5) → c (Command/Buffer, centro y=-4.1): llave [ a la izquierda
\draw[thick,->] (1.5, -1.5) -- (0.5, -1.5) -- (0.5, -4.1) -- (1.4, -4.1);

\draw[thick] (1.9, -2.5) -- (1.65, -2.5) -- (1.65, -3.3) -- (1.9, -3.3);

% De a-Transfer (y=-1.9) → b (Status/Data, centro y=-2.9): llave [ a la izquierda
\draw[thick,->] (1.5, -1.9) -- (1, -1.9) -- (1, -2.9) -- (1.4, -2.9);


\draw[thick] (2.5, -3.7) -- (2.25, -3.7) -- (2.25, -4.5) -- (2.4, -4.5);

% ---- ANOTACIÓN ABAJO: bit 11 → 1=Input / 0=Output ----
\draw[->, gray, thin] (11*0.65+0.325, -1.5) -- (11*0.65+0.325, 0);
\node[font=\scriptsize, align=left] at (11*0.65+0.325+0.5, -1.75) {$1 =$ Input};
\node[font=\scriptsize, align=left] at (11*0.65+0.325+0.5, -2.1)  {$0 =$ Output};

\end{tikzpicture}
\end{document}
```
