



```tikz
\begin{document}

\begin{tikzpicture}

% Estados
\node[draw,circle] (A) at (0,0) {$A$};
\node[draw,circle] (B) at (4,0) {$B$};

% Transiciones entre estados
\draw[->] (A) to[bend left=25] node[above] {$0.2$} (B);
\draw[->] (B) to[bend left=25] node[below] {$0.1$} (A);

% Bucles
\draw[->]
(A) .. controls (-1,1.2) and (1,1.2) ..
node[above] {$0.8$}
(A);

\draw[->]
(B) .. controls (3,1.2) and (5,1.2) ..
node[above] {$0.9$}
(B);

\end{tikzpicture}

\end{document}
```





```tikz
\begin{document}

\begin{tikzpicture}
% Grilla
\draw[gray!90] (0,0) grid (15,10);
% Marcas en los ejes
\foreach \x in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
    \node[below, color=red] at (\x,0) {\x};
\foreach \y in {1,2,3,4,5,6,7,8,9,10}
    \node[left, color=red] at (0,\y) {\y};
% Aquí van tus nodos...
% =====================================================
% CADENA DE MARKOV DE 5 ESTADOS
% Estado destacado: A
% Las transiciones que salen de A tienen el mismo color.
% =====================================================
% Estados
\node[draw,circle ,color=orange ] (A) at (6,9) {$A$};
\node[draw,circle ,color=pink   ] (B) at (9,6) {$B$};
\node[draw,circle, color=lime   ] (C) at (8,2) {$C$};
\node[draw,circle, color=magenta] (D) at (4,2) {$D$};
\node[draw,circle, color=teal   ] (E) at (3,6) {$E$};

% -----------------------------------------------------
% Transiciones desde A (azules)
% -----------------------------------------------------

%\draw[->,blue,thick]
%(A) to[bend left=15]
%node[above] {$0.4$}
%(B);

%\draw[->,blue,thick]
%(A) to[bend right=15]
%node[below] {$0.3$}
%(C);

%\draw[->,blue,thick]
%(A) .. controls (-1,1.2) and (1,1.2) ..
%node[above] {$0.3$}
%(A);

% -----------------------------------------------------
% Transiciones desde B
% -----------------------------------------------------

%\draw[->]
%(B) to[bend left=15]
%node[above] {$0.5$}
%(D);

%\draw[->]
%(B) to[bend left=15]
%node[left] {$0.2$}
%(C);

%\draw[->]
%(B) .. controls (3.2,3.2) and (4.8,3.2) ..
%node[above] {$0.3$}
%(B);

% -----------------------------------------------------
% Transiciones desde C
% -----------------------------------------------------

%\draw[->]
%(C) to[bend right=15]
%node[below] {$0.4$}
%(E);

%\draw[->]
%(C) to[bend left=15]
%node[right] {$0.2$}
%(B);

%\draw[->]
%(C) .. controls (3.2,-3.2) and (4.8,-3.2) ..
%node[below] {$0.4$}
%(C);

% -----------------------------------------------------
% Transiciones desde D
% -----------------------------------------------------

%\draw[->]
%(D) to[bend left=20]
%node[right] {$0.3$}
%(E);

%\draw[->]
%(D) to[bend left=20]
%node[above] {$0.2$}
%(B);

%\draw[->]
%(D) .. controls (7.2,3.2) and (8.8,3.2) ..
%node[above] {$0.5$}
%(D);

% -----------------------------------------------------
% Transiciones desde E
% -----------------------------------------------------

%\draw[->]
%(E) to[bend left=20]
%node[left] {$0.4$}
%(D);

%\draw[->]
%(E) to[bend left=20]
%node[below] {$0.2$}
%(C);

%\draw[->]
%(E) .. controls (7.2,-3.2) and (8.8,-3.2) ..
%node[below] {$0.4$}
%(E);

\end{tikzpicture}

\end{document}
```



| Color           | Nombre      |
| --------------- | ----------- |
| `red`           | rojo        |
| `green`         | verde       |
| `blue`          | azul        |
| `cyan`          | cian        |
| `magenta`       | magenta     |
| `yellow`        | amarillo    |
| `black`         | negro       |
| `white`         | blanco      |
| `gray` / `grey` | gris        |
| `darkgray`      | gris oscuro |
| `lightgray`     | gris claro  |
| `brown`         | marrón      |
| `lime`          | lima        |
| `olive`         | oliva       |
| `orange`        | naranja     |
| `pink`          | rosa        |
| `purple`        | púrpura     |
| `teal`          | turquesa    |
| `violet`        | violeta     |
