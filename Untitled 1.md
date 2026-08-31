```tikz
\begin{tikzpicture}[scale=0.8, >=stealth, every node/.style={font=\small}]
    \draw[thick, teal]   (0,0) circle (2.2cm);
    \draw[thick, orange] (0,0) circle (1.2cm);
    \foreach \angle in {0, 72, 144, 216, 288} {
        \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
    }
    \foreach \angle in {0, 72, 144, 216, 288} {
        \fill[teal] (\angle:2.2cm) circle (3pt);
    }
    \foreach \angle in {0, 72, 144, 216, 288} {
        \fill[orange] (\angle:1.2cm) circle (3pt);
    }
    \node[teal, anchor=west]       at (0:2.35cm)   {$2$};
    \node[teal, anchor=south west] at (72:2.35cm)  {$1$};
    \node[teal, anchor=south east] at (144:2.35cm) {$2$};
    \node[teal, anchor=north east] at (216:2.35cm) {$1$};
    \node[teal, anchor=north west] at (288:2.35cm) {$0$};
    \node[orange, anchor=west]       at (0:1.35cm)   {$1$};
    \node[orange, anchor=north west] at (288:1.35cm) {$2$};
    \node[orange, anchor=north east] at (216:1.35cm) {$3$};
    \node[orange, anchor=south east] at (144:1.35cm) {$4$};
    \node[orange, anchor=south west] at (72:1.35cm)  {$5$};
    % Flecha CW interna
    \draw[->, orange, thick] (0.55cm,0) arc (0:-270:0.55cm);
\end{tikzpicture}
\captionof{figure}{$m=0$: sin rotación. $x_2(0-n)$.}
```


