---


---
1.


```tikz
\begin{tikzpicture}
\draw[thick] (-4,0) ellipse (1 and 1.5);
\draw[thick] (0,0) ellipse (1 and 1.5);
\draw[thick] (4,0) ellipse (1 and 1.5);

\node at (-4, 2) {$A$};
\node at (0, 2) {$B$};
\node at (4, 2) {$C$};

\node (x) at (-4, 0) {$x$};
\node (gx) at (0, 0) {$g(x)$};
\node (fgx) at (4, 0) {$\cdot$};

\draw[->, thick] (x) -- (gx) node[midway, above] {$g$};
\draw[->, thick] (gx) -- (fgx) node[midway, above] {$f$};
\draw[->, thick, bend left=40] (x) to node[above] {$f \circ g$} (fgx);
\end{tikzpicture}
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

