
### N13. CAP. 2 — SISTEMAS EN TIEMPO CONTINUO

> Integral de convolución, sistemas LTI, respuesta al impulso, ecuaciones diferenciales.

#### Sistema en cascada

> Contexto para NotebookLM: usar cuando el usuario pida representar la composición de dos sistemas LTI en serie. La función de transferencia equivalente $H = H_1 \cdot H_2$ se puede agregar como etiqueta debajo.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Entrada
\draw[->, thick, orange] (-2.5,0) -- (-1.1,0);
\node[left, orange] at (-2.5,0) {$x(t)$};

% Bloque H1
\draw[thick, teal] (-1.1,-0.4) rectangle (0.1,0.4);
\node[teal] at (-0.5,0) {$H_1$};

% Señal intermedia
\draw[->, thick] (0.1,0) -- (0.9,0);
\node[above, font=\small] at (0.5,0) {$w(t)$};

% Bloque H2
\draw[thick, teal] (0.9,-0.4) rectangle (2.1,0.4);
\node[teal] at (1.5,0) {$H_2$};

% Salida
\draw[->, thick, orange] (2.1,0) -- (3,0);
\node[right, orange] at (3,0) {$y(t)$};

% Equivalente
\node[gray, font=\small] at (0.5,-0.9) {Equivalente: $H = H_1 \cdot H_2$};

\end{tikzpicture}
\end{document}
```

---

### N_CAP2_PALANI. CAP. 2 — DFT Y CONVOLUCIÓN CIRCULAR (PALANI)

---

#### Convolución circular — método de la matriz circulante

> Contexto para NotebookLM: usar cuando el usuario pida representar la matriz de convolución circular para calcular $x_3(m) = x_1(n) \circledast x_2(n)$. La primera fila de la matriz contiene $x_1(n)$; cada fila siguiente es un desplazamiento circular a la derecha. El resultado es el producto matriz-vector $[M] \cdot x_2$.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]

% Título
\node[font=\small] at (3, 1.2) {Matriz circulante de $x_1(n) = \{2,1,2,1\}$, $N=4$};

% Matriz — cada fila es un desplazamiento circular de x1
% Fila 0: [2 1 2 1]
% Fila 1: [1 2 1 2]
% Fila 2: [2 1 2 1]
% Fila 3: [1 2 1 2]

% Corchete izquierdo
\draw[thick] (0.3, 0.7) -- (0.1, 0.7) -- (0.1, -1.5) -- (0.3, -1.5);
% Corchete derecho
\draw[thick] (5.7, 0.7) -- (5.9, 0.7) -- (5.9, -1.5) -- (5.7, -1.5);

% Fila 0
\node at (1.2, 0.4) {$2$};
\node at (2.4, 0.4) {$1$};
\node at (3.6, 0.4) {$2$};
\node at (4.8, 0.4) {$1$};

% Fila 1
\node at (1.2,-0.1) {$1$};
\node at (2.4,-0.1) {$2$};
\node at (3.6,-0.1) {$1$};
\node at (4.8,-0.1) {$2$};

% Fila 2
\node at (1.2,-0.6) {$2$};
\node at (2.4,-0.6) {$1$};
\node at (3.6,-0.6) {$2$};
\node at (4.8,-0.6) {$1$};

% Fila 3
\node at (1.2,-1.1) {$1$};
\node at (2.4,-1.1) {$2$};
\node at (3.6,-1.1) {$1$};
\node at (4.8,-1.1) {$2$};

% Símbolo multiplicación
\node[font=\large] at (6.4,-0.4) {$\cdot$};

% Vector x2
\draw[thick] (6.7, 0.7) -- (6.5, 0.7) -- (6.5,-1.5) -- (6.7,-1.5);
\draw[thick] (7.3, 0.7) -- (7.5, 0.7) -- (7.5,-1.5) -- (7.3,-1.5);
\node at (7.0, 0.4) {$1$};
\node at (7.0,-0.1) {$2$};
\node at (7.0,-0.6) {$3$};
\node at (7.0,-1.1) {$4$};

% Símbolo igual
\node[font=\large] at (8.0,-0.4) {$=$};

% Vector resultado x3
\draw[thick] (8.4, 0.7) -- (8.2, 0.7) -- (8.2,-1.5) -- (8.4,-1.5);
\draw[thick] (9.6, 0.7) -- (9.8, 0.7) -- (9.8,-1.5) -- (9.6,-1.5);
\node at (9.0, 0.4) {$14$};
\node at (9.0,-0.1) {$16$};
\node at (9.0,-0.6) {$14$};
\node at (9.0,-1.1) {$16$};

\end{tikzpicture}
\end{document}
```

---

#### Convolución circular — pasos del método gráfico (círculos concéntricos)

> Contexto para NotebookLM: usar para ilustrar cada paso $m = 0, 1, 2, 3$ del método gráfico de Palani (Fig. 2.11). Para cada valor de $m$: el círculo exterior tiene $x_1(n)$ fijo en sentido antihorario; el círculo interior tiene $x_2(m-n)$ rotado $m$ posiciones en sentido antihorario. Se multiplican los valores alineados y se suman.

> **Patrón por paso — indicar a NotebookLM:**
> - $m=0$: $x_2(0-n)$ → círculo interior sin rotar → $x_3(0) = 2\times1 + 1\times4 + 2\times3 + 1\times2 = 14$
> - $m=1$: $x_2(1-n)$ → rotación 1 posición antihoraria → $x_3(1) = 2\times2 + 1\times1 + 2\times4 + 1\times3 = 16$
> - $m=2$: $x_2(2-n)$ → rotación 2 posiciones → $x_3(2) = 2\times3 + 1\times2 + 2\times1 + 1\times4 = 14$
> - $m=3$: $x_2(3-n)$ → rotación 3 posiciones → $x_3(3) = 2\times4 + 1\times3 + 2\times2 + 1\times1 = 16$

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0]

% --- m=0 ---
% Círculo exterior (x1 fijo, antihorario desde arriba: 2,1,2,1)
\draw[thick, teal] (0,0) circle (1.4);
\node[teal] at (0, 1.6)  {$2$};   % n=0, arriba
\node[teal] at (-1.6, 0) {$1$};   % n=1, izq
\node[teal] at (0,-1.6)  {$2$};   % n=2, abajo
\node[teal] at (1.6, 0)  {$1$};   % n=3, der

% Círculo interior (x2 sin rotar, horario desde arriba: 1,4,3,2)
\draw[thick, orange] (0,0) circle (0.8);
\node[orange] at (0, 1.0)  {$1$};  % x2(0)
\node[orange] at (-1.0, 0) {$4$};  % x2(3) — horario
\node[orange] at (0,-1.0)  {$3$};  % x2(2)
\node[orange] at (1.0, 0)  {$2$};  % x2(1)

% Flecha de rotación
\draw[->, thick, gray] (0.3,0.55) arc (60:300:0.6);

% Etiqueta m y resultado
\node[font=\small] at (0, 2.2)  {$m=0$};
\node[font=\small, gray] at (0,-2.2) {$x_3(0)=2{\times}1+1{\times}4+2{\times}3+1{\times}2=14$};

\end{tikzpicture}
\end{document}
```

> **Nota para NotebookLM:** el bloque anterior muestra $m=0$ como plantilla. Para $m=1,2,3$ rotar los valores del círculo interior una posición más en cada paso, manteniendo el exterior fijo. Generar un bloque TikZ separado por cada valor de $m$ si el usuario pide el diagrama completo.

---

#### Sistema en paralelo

> Contexto para NotebookLM: usar para representar dos sistemas LTI en paralelo con sumador. La función equivalente $H = H_1 + H_2$ se puede agregar como etiqueta.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]

% Entrada
\draw[->, thick, orange] (-3,0) -- (-2,0);
\node[left, orange] at (-3,0) {$x(t)$};

% Punto de bifurcación
\fill (-2,0) circle (0.06);

% Rama superior
\draw[->, thick] (-2,0) -- (-2,1) -- (-1,1);
\draw[thick, teal] (-1,0.6) rectangle (0,1.4);
\node[teal] at (-0.5,1) {$H_1$};
\draw[->, thick] (0,1) -- (1,1) -- (1,0.3);

% Rama inferior
\draw[->, thick] (-2,0) -- (-2,-1) -- (-1,-1);
\draw[thick, teal] (-1,-1.4) rectangle (0,-0.6);
\node[teal] at (-0.5,-1) {$H_2$};
\draw[->, thick] (0,-1) -- (1,-1) -- (1,-0.3);

% Sumador
\draw[thick] (1,0) circle (0.3);
\draw (0.7,0) -- (1.3,0);
\draw (1,-0.3) -- (1,0.3);
\node[above right, font=\tiny] at (1.1,0.1) {$+$};
\node[below right, font=\tiny] at (1.1,-0.1) {$+$};

% Salida
\draw[->, thick, orange] (1.3,0) -- (2.5,0);
\node[right, orange] at (2.5,0) {$y(t)$};

% Equivalente
\node[gray, font=\small] at (0,-2.2) {Equivalente: $H = H_1 + H_2$};

\end{tikzpicture}
\end{document}
```

---

#### Sistema con retroalimentación (feedback)

> Contexto para NotebookLM: usar para representar un sistema con lazo cerrado. Bloque directo $H_1$ en la rama hacia adelante, bloque $H_2$ en la rama de retroalimentación, sumador con signo negativo.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]

% Sumador
\draw[thick] (-1,0) circle (0.3);
\draw (-1.3,0) -- (-0.7,0);
\draw (-1,-0.3) -- (-1,0.3);
\node[above right, font=\small] at (-0.85,0.1) {$+$};
\node[below right, font=\small] at (-0.85,-0.15) {$-$};

% Entrada
\draw[->, thick, orange] (-2.8,0) -- (-1.3,0);
\node[left, orange] at (-2.8,0) {$x(t)$};

% Señal de error e(t)
\draw[->, thick] (-0.7,0) -- (0.4,0);
\node[above, font=\small] at (-0.1,0) {$e(t)$};

% Bloque H1 (hacia adelante)
\draw[thick, teal] (0.4,-0.4) rectangle (1.8,0.4);
\node[teal] at (1.1,0) {$H_1(s)$};

% Salida
\draw[->, thick, orange] (1.8,0) -- (3.2,0);
\node[right, orange] at (3.2,0) {$y(t)$};

% Punto de bifurcación en la salida
\fill (2.5,0) circle (0.06);

% Rama de retroalimentación
\draw[->, thick] (2.5,0) -- (2.5,-1.2) -- (0.4,-1.2);
\draw[thick, teal] (0.4,-1.6) rectangle (1.8,-0.8);
\node[teal] at (1.1,-1.2) {$H_2(s)$};
\draw[->, thick] (-0.3,-1.2) -- (-1,-1.2) -- (-1,-0.3);

\end{tikzpicture}
\end{document}
```

---

### N14. CAP. 3 — FOURIER EN TIEMPO CONTINUO

> Series de Fourier, transformada de Fourier continua, respuesta en frecuencia.

#### Espectro de magnitud — serie de Fourier

> Contexto para NotebookLM: usar para mostrar el espectro bilateral de magnitud de una señal periódica. Tallos en frecuencias discretas $k\omega_0$, magnitudes simétricas respecto al origen. Usar `ycomb` en `pgfplots`.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
    axis lines=middle,
    xmin=-4.5, xmax=4.5,
    ymin=-0.1, ymax=1.2,
    xlabel={$k\omega_0$},
    ylabel={$|c_k|$},
    width=11cm, height=5cm,
    xtick={-4,-3,-2,-1,0,1,2,3,4},
    xticklabels={$-4\omega_0$,$-3\omega_0$,$-2\omega_0$,$-\omega_0$,$0$,$\omega_0$,$2\omega_0$,$3\omega_0$,$4\omega_0$},
    ytick={0,0.5,1},
    tick style={thin, black}
]

\addplot[ycomb, very thick, teal, mark=*, mark size=3pt]
    coordinates {(-4,0.1)(-3,0.2)(-2,0.35)(-1,0.6)(0,1)(1,0.6)(2,0.35)(3,0.2)(4,0.1)};

\end{axis}
\end{tikzpicture}
\end{document}
```

---
