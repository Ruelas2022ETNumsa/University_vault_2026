

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
\begin{document}
\begin{tikzpicture}
\begin{axis}[axis lines=middle]
\end{axis}
\end{tikzpicture}
\end{document}
```



```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[axis lines=middle]
\addplot[domain=0:4, samples=50] {x^2};
\addplot[domain=0:4, samples=50] {x/2};
\end{axis}
\end{tikzpicture}
\end{document}
```


```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xlabel={$x$},
    ylabel={$y$},
    xmin=0, xmax=5.5,
    ymin=0, ymax=24
]

\addplot[teal!30, fill=teal!30, domain=2:4, samples=100]
    {x^2} \closedcycle;
\addplot[white, fill=white, domain=2:4, samples=100]
    {x} \closedcycle;

\addplot[domain=0:4.5, samples=100, -latex] {x^2}
    node[very near end, right] {$y=x^2$};
\addplot[domain=0:4.5, -latex] {x}
    node[pos=1, above] {$y=x$};

\draw[dashed, teal] (axis cs:2,2) -- (axis cs:2,4);
\draw[dashed, teal] (axis cs:4,4) -- (axis cs:4,16);
\draw[dashed] (axis cs:2,0) -- (axis cs:2,2);
\draw[dashed] (axis cs:4,0) -- (axis cs:4,4);

\end{axis}
\end{tikzpicture}
\end{document}
```