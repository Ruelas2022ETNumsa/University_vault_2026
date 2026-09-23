##### Ej. Sistema cuña doble — construcción gráfica

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.1, >=latex]

% Pared izquierda inclinada 120°
\fill[pattern=north east lines]
(0,0)
-- (-1.73,3)
-- (-1.30,3)
-- (0,0)
-- cycle;

\draw[thick]
(0,0) -- (-1.73,3);

% Piso horizontal
\fill[pattern=north east lines]
(0,-0.3) rectangle (7.0,0);

\draw[thick]
(0,0) -- (7.0,0);

% Pared derecha vertical
\fill[pattern=north east lines]
(7.0,0) rectangle (7.3,3.0);

\draw[thick]
(7.0,0) -- (7.0,3.0);

\end{tikzpicture}

\end{document}
```

---



```tikz

```

