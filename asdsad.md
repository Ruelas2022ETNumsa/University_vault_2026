


```tikz
\begin{document}
\begin{tikzpicture}[node distance=2cm, auto]
    % Estilo de los nodos
    \tikzstyle{state} = [circle, draw, minimum size=1.2cm, very thick]

    % 1. DIBUJO DE NODOS (Ubicación circular centro 6,6)
    \node[state, draw=cyan, fill=cyan!10] (S0) at (6,10) {$S_0$};
    \node[state, draw=blue, fill=blue!10] (S1) at (10,6) {$S_1$};
    \node[state, draw=green!60!black, fill=green!10] (S2) at (6,2) {$S_2$};
    \node[state, draw=orange, fill=orange!10] (S3) at (2,6) {$S_3$};

    % 2. BUCLES (Probabilidad de quedarse p_ii = 0.7)
    \path (S0) edge [loop above, ultra thick, cyan] node {0.7} (S0);
    \path (S1) edge [loop right, ultra thick, blue] node {0.7} (S1);
    \path (S2) edge [loop below, ultra thick, green!60!black] node {0.7} (S2);
    \path (S3) edge [loop left, ultra thick, orange] node {0.7} (S3);

    % 3. TRANSICIONES (Probabilidades p_ij = 0.1)
    % Salidas de S0 (Cyan)
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S2);
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S1 (Blue)
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S2);
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S2 (Green)
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S3 (Orange)
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S2);

\end{tikzpicture}
\end{document}
```



```tikz
\begin{tikzpicture}
    % Estilo de los nodos
% 1. DIBUJO DE NODOS (Ubicación circular centro 6,6)
    \node[state, draw=cyan, fill=cyan!10] (S0) at (6,10) {$S_0$};
    \node[state, draw=blue, fill=blue!10] (S1) at (10,6) {$S_1$};
    \node[state, draw=green!60!black, fill=green!10] (S2) at (6,2) {$S_2$};
    \node[state, draw=orange, fill=orange!10] (S3) at (2,6) {$S_3$};
    



\end{tikzpicture}
```

    
    % 2. BUCLES (Probabilidad de quedarse p_ii = 0.7)
    \path (S0) edge [loop above, ultra thick, cyan] node {0.7} (S0);
    \path (S1) edge [loop right, ultra thick, blue] node {0.7} (S1);
    \path (S2) edge [loop below, ultra thick, green!60!black] node {0.7} (S2);
    \path (S3) edge [loop left, ultra thick, orange] node {0.7} (S3);

    % 3. TRANSICIONES (Probabilidades p_ij = 0.1)
    % Salidas de S0 (Cyan)
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S2);
    \path[->, cyan, very thick] (S0) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S1 (Blue)
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S2);
    \path[->, blue, very thick] (S1) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S2 (Green)
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, green!60!black, very thick] (S2) edge [bend left=20] node[pos=0.3] {0.1} (S3);

    % Salidas de S3 (Orange)
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S0);
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S1);
    \path[->, orange, very thick] (S3) edge [bend left=20] node[pos=0.3] {0.1} (S2);