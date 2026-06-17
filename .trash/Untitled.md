

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
\node[draw,circle,thick,color=orange]  (A) at (2,6) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,6) {$B$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (1,7) and (3,7) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.5,above] {$0.4$} (B);

% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (9,7) and (11,7) ..node[above] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.5,below] {$0.4$} (A);

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
\node[draw,circle,thick,color=orange]  (A) at (6,10) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,4) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (2,4) {$C$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,11) and (7,11) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,5) and (11,3) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (1,3) and (1,5) ..node[left] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

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
\node[draw,circle,thick,color=orange]  (A) at (6,10) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,6) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (6,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (2,6) {$D$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,11) and (7,11) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);

% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,7) and (11,5) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (7,1) and (5,1) ..node[below] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (1,5) and (1,7) ..node[left] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
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
\node[draw,circle,thick,color=pink]    (B) at (10,7) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (9,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (3,2) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (2,7) {$E$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,12) and (7,12) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.3,right] {$0.2$} (E);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,8) and (11,6) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (10,3) and (10,1) ..node[right] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (4,1) and (2,1) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.3,right] {$0.4$} (E);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (1,6) and (1,8) ..node[left] {$0.8$}(E);
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
\node[draw,circle,thick,color=lime]    (C) at (10,4) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (6,1) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (2,4) {$E$};
\node[draw,circle,thick,color=magenta]    (F) at (2,8) {$F$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,12) and (7,12) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (E);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.4,right] {$0.2$} (F);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,9) and (11,7) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (F);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.4,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (11,5) and (11,3) ..node[right] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (F);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);
% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (7,0) and (5,0) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.3,right] {$0.4$} (F);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (1,3) and (1,5) ..node[left] {$0.8$}(E);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.3,right] {$0.4$} (F);
% =====================================================
% F
% =====================================================
\draw[->,ultra thick,magenta] (F) .. controls (1,7) and (1,9) ..node[left] {$0.8$}(F);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.3,right] {$0.4$} (E);

\end{tikzpicture}
\end{document}
```






