---


---
1.



```tikz
\begin{document}
\begin{tikzpicture}

% Conjuntos
\draw (-4,0) ellipse (1 and 1.5);
\draw (0,0) ellipse (1 and 1.5);
\draw (4,0) ellipse (1 and 1.5);

% Nombres de conjuntos
\node at (-4,2) {$A$};
\node at (0,2) {$B$};
\node at (4,2) {$C$};

% Elementos
\node (x) at (-4,0) {$x$};
\node (gx) at (0,0) {$g(x)$};
\node (fgx) at (4,0) {$f(g(x))$};

% Flechas
\draw[->, thick] (x) -- (gx);
\node at (-2,0.4) {$g$};

\draw[->, thick] (gx) -- (fgx);
\node at (2,0.4) {$f$};

% Composición
\draw[->, thick]
(-4,0.8) .. controls (0,2.5) .. (4,0.8);

\node at (0,2.9) {$f\circ g$};

\end{tikzpicture}
\end{document}
```

---
2.

```tikz
\begin{tikzpicture}[scale=2]
\draw[->] (-1.3,0) -- (1.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,1.3) node[above] {$y$};
\draw[thick] (0,0) circle(1);

\coordinate (P) at (50:1);
\draw[thick, red] (0,0) -- (P);
\fill (P) circle(1pt) node[above right] {$P$};

\coordinate (Q) at ($(1,0)!(P)!(1,-2)$);
\fill (Q) circle(1pt) node[right] {$Q$};
\draw[dashed] (P) -- (Q);

\node[below right] at (1,0) {$T$};
\draw[thick, blue] (1,0) -- (1, {tan(50)}) node[right] {$R$};

\node[below] at (0,0) {$O$};
\node[below right] at (1,0) {$1$};

\draw (0.2,0) arc(0:50:0.2) node[midway, right] {\tiny$x$};
\end{tikzpicture}
```

---

3.

```tikz
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};

\draw[dashed, gray] (-0.3,-0.3) -- (2.8,2.8) node[right] {$y=x$};

\draw[thick, blue, domain=0.1:2.7, samples=100]
  plot (\x, {ln(\x)+1.5}) node[right] {$y=f(x)$};

\draw[thick, red, domain=0.1:2.7, samples=100]
  plot ({ln(\x)+1.5}, \x) node[below] {$y=f^{-1}(x)$};
\end{tikzpicture}
```



---

4.

```tikz
\begin{tikzpicture}[scale=1]
\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-2) -- (0,3) node[above] {$y$};

\draw[thick, blue, domain=-2.5:0, samples=50]
  plot (\x, {-\x});
\draw[thick, blue, domain=0:2.5, samples=50]
  plot (\x, {\x});

\fill (0,0) circle(2pt);
\node[below left] at (0,0) {$0$};
\node[above right] at (1.5,1.5) {$y=|x|$};
\end{tikzpicture}
```



