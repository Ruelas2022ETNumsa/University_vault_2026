

```tikz
\begin{document}
  \begin{tikzpicture}[domain=0:4]
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};
    \draw[color=red]    plot (\x,\x)             node[right] {$f(x) =x$};
    \draw[color=blue]   plot (\x,{sin(\x r)})    node[right] {$f(x) = \sin x$};
    \draw[color=orange] plot (\x,{0.05*exp(\x)}) node[right] {$f(x) = \frac{1}{20} \mathrm e^x$};
  \end{tikzpicture}
\end{document}
```



```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\usepgfplotslibrary{fillbetween}

\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines = middle,
    xlabel = {$x$},
    ylabel = {$y$},
    xmin=0, xmax=5.5,
    ymin=0, ymax=24
]

\addplot[name path=A, domain=0:4.5, samples=100, -latex] {x^2}
    node[very near end, right] {$y=x^2$};

\addplot[name path=B, domain=0:4.5, -latex] {x}
    node[pos=1, above] {$y=x$};

\addplot[teal!30] fill between[of=A and B, soft clip={domain=2:4}];

\draw[dashed, teal] (axis cs:2,2) -- (axis cs:2,4);
\draw[dashed, teal] (axis cs:4,4) -- (axis cs:4,16);
\draw[dashed] (axis cs:2,0) -- (axis cs:2,2);
\draw[dashed] (axis cs:4,0) -- (axis cs:4,4);

\end{axis}
\end{tikzpicture}
\end{document}
```
