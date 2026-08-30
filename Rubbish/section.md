
### N_CAP2_PALANI. CAP. 2 — DFT Y CONVOLUCIÓN CIRCULAR (PALANI)

---

#### Convolución circular — pasos del método gráfico (círculos concéntricos)

> Contexto para NotebookLM: usar para ilustrar cada paso $m = 0, 1, \ldots, N-1$ del método gráfico de Palani (Fig. 2.11).
>
> **Reglas generales — válidas para cualquier N:**
> - Los N valores se distribuyen uniformemente sobre cada círculo — distancia angular igual entre puntos consecutivos: $\Delta\theta = 360°/N$
> - Siempre se inicia en 0° (derecha)
> - Círculo exterior x₁(n): sentido antihorario desde 0° — nunca rota
> - Círculo interior x₂(n): sentido horario desde 0° — en cada paso m rota hasta coincidir con el siguiente punto en sentido antihorario (es decir, avanza $\Delta\theta$ CCW por paso)
>
> **Ejemplo N=4 — $\Delta\theta = 90°$:**
>
> Disposición fija — círculo exterior x₁(n), antihorario desde 0°:
> - n=0 → 0°   (derecha)    x₁(0)=2
> - n=1 → 90°  (arriba)     x₁(1)=1
> - n=2 → 180° (izquierda)  x₁(2)=2
> - n=3 → 270° (abajo)      x₁(3)=1
>
> Círculo interior x₂, horario desde 0°, m=0 sin rotar:
> - n=0 → 0°   (derecha)    x₂(0)=1
> - n=1 → 270° (abajo)      x₂(1)=2
> - n=2 → 180° (izquierda)  x₂(2)=3
> - n=3 → 90°  (arriba)     x₂(3)=4
>
> **Ejemplo N=5 — $\Delta\theta = 72°$:**
>
> Disposición fija — círculo exterior x₁(n), antihorario desde 0°:
> - n=0 → 0°   x₁(0)
> - n=1 → 72°  x₁(1)
> - n=2 → 144° x₁(2)
> - n=3 → 216° x₁(3)
> - n=4 → 288° x₁(4)
>
> Círculo interior x₂, horario desde 0°, m=0 sin rotar:
> - n=0 → 0°   x₂(0)
> - n=1 → 288° x₂(1)
> - n=2 → 216° x₂(2)
> - n=3 → 144° x₂(3)
> - n=4 → 72°  x₂(4)
>
> **Cada paso m: el interior rota $\Delta\theta$ CCW hasta alinear el siguiente punto con 0°. El exterior nunca cambia.**
>
> Patrón por paso (N=4):
> - $m=0$: interior sin rotar → $x_3(0) = 2\times1 + 1\times4 + 2\times3 + 1\times2 = 14$
> - $m=1$: interior rota 90° CCW → der=x₂(1)=2, arriba=x₂(2)=3, izq=x₂(3)=4, abajo=x₂(0)=1 → $x_3(1) = 2\times2 + 1\times1 + 2\times4 + 1\times3 = 16$
> - $m=2$: interior rota 90° CCW → der=x₂(2)=3, arriba=x₂(3)=4, izq=x₂(0)=1, abajo=x₂(1)=2 → $x_3(2) = 2\times3 + 1\times2 + 2\times1 + 1\times4 = 14$
> - $m=3$: interior rota 90° CCW → der=x₂(3)=4, arriba=x₂(0)=1, izq=x₂(1)=2, abajo=x₂(2)=3 → $x_3(3) = 2\times4 + 1\times3 + 2\times2 + 1\times1 = 16$

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.9]

% Círculo exterior — x1(n) fijo, antihorario desde 0°
% n=0 → der (0°), n=1 → arriba (90°), n=2 → izq (180°), n=3 → abajo (270°)
\draw[thick, teal] (0,0) circle (1.4);
\fill[orange] ( 1.4,  0)   circle (0.08);  % n=0
\fill[orange] ( 0,    1.4) circle (0.08);  % n=1
\fill[orange] (-1.4,  0)   circle (0.08);  % n=2
\fill[orange] ( 0,   -1.4) circle (0.08);  % n=3
\node[teal] at ( 1.85, 0)   {$x_1(0)=2$};   % 0°
\node[teal] at ( 0,    1.7) {$x_1(1)=1$};   % 90°
\node[teal] at (-1.85, 0)   {$x_1(2)=2$};   % 180°
\node[teal] at ( 0,   -1.7) {$x_1(3)=1$};   % 270°

% Círculo interior — x2(n) horario desde 0°, m=0 sin rotar
% x2(0) → der (0°), x2(1) → abajo (270°), x2(2) → izq (180°), x2(3) → arriba (90°)
\draw[thick, orange] (0,0) circle (0.85);
\fill[teal] ( 0.85,  0)   circle (0.08);  % x2(0)
\fill[teal] ( 0,    -0.85) circle (0.08);  % x2(1)
\fill[teal] (-0.85,  0)   circle (0.08);  % x2(2)
\fill[teal] ( 0,     0.85) circle (0.08);  % x2(3)
\node[orange] at ( 1.1,  0)    {$x_2(0)=1$};   % 0°
\node[orange] at ( 0,   -1.05) {$x_2(1)=2$};   % 270°
\node[orange] at (-1.1,  0)    {$x_2(2)=3$};   % 180°
\node[orange] at ( 0,    1.05) {$x_2(3)=4$};   % 90°

% Flecha rotación interior (sentido horario — CW — para graficar x2)
\draw[->, thick, orange, dashed] (0.2, 0.6) arc (70:-70:0.65);
\node[orange, font=\tiny] at (1.0, 0.55) {CW};

% Flecha rotación paso (CCW — cada m rota interior 1 pos CCW)
\draw[->, thick, gray] (-0.2, 0.6) arc (110:250:0.65);
\node[gray, font=\tiny] at (-1.0, 0.55) {CCW};

% Etiqueta m y resultado
\node[font=\small, teal] at (0, 2.2) {$m=0$};
\node[font=\small, gray] at (0,-2.3) {$x_3(0)=2{\times}1+1{\times}4+2{\times}3+1{\times}2=14$};

\end{tikzpicture}
\end{document}
```

> **Nota para NotebookLM:** generar un bloque TikZ por cada valor de $m$. En cada bloque rotar los valores del interior 1 posición CCW respecto al paso anterior — el exterior nunca cambia. Las etiquetas de los nodos del interior cambian de posición angular según la tabla de patrón arriba.

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
