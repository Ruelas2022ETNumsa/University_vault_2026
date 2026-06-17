


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
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,9) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (9,6) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (8,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (4,2) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (3,6) {$E$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,10) and (7,10) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.3,right] {$0.2$} (E);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (10,7) and (10,5) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (8.5,1.0) and (7.5,1.0) ..node[below] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);
% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (4.5,1.0) and (3.5,1.0) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.3,right] {$0.4$} (E);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (2,5) and (2,7) ..node[left] {$0.8$}(E);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.3,right] {$0.4$} (D);


\end{tikzpicture}
\end{document}
```





```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,11) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,8) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (8,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (4,2) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (3,6) {$E$};
\node[draw,circle,thick,color=teal]    (F) at (3,6) {$E$};


\end{tikzpicture}
\end{document}
```



% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,10) and (7,10) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.3,right] {$0.2$} (E);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (10,7) and (10,5) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (8.5,1.0) and (7.5,1.0) ..node[below] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);
% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (4.5,1.0) and (3.5,1.0) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.3,right] {$0.4$} (E);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (2,5) and (2,7) ..node[left] {$0.8$}(E);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.3,right] {$0.4$} (D);
