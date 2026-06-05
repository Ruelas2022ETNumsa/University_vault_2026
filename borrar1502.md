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
\begin{document}
\begin{tikzpicture}[scale=2]

% Ejes
\draw[->] (-1.3,0) -- (1.3,0) node[right] {$x$};
\draw[->] (0,-1.3) -- (0,1.3) node[above] {$y$};

% Circunferencia unidad
\draw[thick] (0,0) circle (1);

% Punto P
\coordinate (P) at (50:1);
\draw[thick] (0,0) -- (P);
\fill (P) circle (0.03);
\node[above right] at (P) {$P$};

% Proyección Q sobre x=1
\coordinate (Q) at (1,{tan(50)});
\fill (Q) circle (0.03);
\node[right] at (Q) {$Q$};

% Segmento PQ
\draw[dashed] (P) -- (Q);

% Tangente
\draw[thick] (1,0) -- (Q);

\node[below] at (0,0) {$O$};
\node[below right] at (1,0) {$T$};
\node[below] at (0.95,0) {$1$};

% Ángulo x
\draw (0.2,0) arc (0:50:0.2);
\node at (0.32,0.12) {\tiny $x$};

\end{tikzpicture}
\end{document}
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


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Ejes
\draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};

% Recta y=x
\draw[dashed] (-0.3,-0.3) -- (2.8,2.8);
\node[right] at (2.8,2.8) {$y=x$};

% f(x)=ln(x)+1.5
\draw[thick, domain=0.1:2.7]
plot (\x,{ln(\x)+1.5});

\node[right] at (2.7,2.5) {$y=f(x)$};

% f^{-1}(x)=e^{x-1.5}
\draw[thick, domain=0.1:2.5]
plot ({exp(\x-1.5)},\x);

\node[below] at (2.4,2.4) {$y=f^{-1}(x)$};

\end{tikzpicture}
\end{document}
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




```tikz
\begin{document}
\begin{tikzpicture}[scale=1]

% Ejes
\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-2) -- (0,3) node[above] {$y$};

% y = |x|
\draw[thick, domain=-2.5:0]
plot (\x,{-\x});

\draw[thick, domain=0:2.5]
plot (\x,{\x});

% Origen
\fill (0,0) circle (0.05);
\node[below left] at (0,0) {$0$};

% Etiqueta
\node[above right] at (1.5,1.5) {$y=|x|$};

\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}[scale=1]

\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-2) -- (0,3) node[above] {$y$};

\draw[thick] (-2.5,2.5) -- (0,0);
\draw[thick] (0,0) -- (2.5,2.5);

\fill (0,0) circle (0.05);
\node[below left] at (0,0) {$0$};
\node[above right] at (1.5,1.5) {$y=|x|$};

\end{tikzpicture}
\end{document}
```


