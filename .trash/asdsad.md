


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




Para diseñar una cadena de Markov de 7 estados en TikZ, seguiremos estrictamente el patrón técnico, los cálculos geométricos y las reglas de estilo definidas en la fuente **"Tikz_markov_guide.md"**.

### 1. Identificación de Datos y Requisitos

Según los estándares de diseño proporcionados:

- **Número de estados ($N$):** 7.
- **Nombres de los estados:** $S_0, S_1, S_2, S_3, S_4, S_5, S_6$.
- **Radio sugerido ($R$):** 5.5 unidades (para $N \ge 7$).
- **Centro del diagrama:** Coordenada $(6,6)$.
- **Paleta de colores (en orden):** Cyan, Blue, Green, Orange, Purple, Yellow, Magenta.
- **Matriz de Transición ($P$):** Para este ejemplo, utilizaremos una estructura de ciclo donde cada estado tiene un $70%$ de probabilidad de permanecer en sí mismo y un $30%$ de pasar al siguiente estado ($S_i \to S_{i+1 \pmod 7}$). Esto garantiza que la suma de cada fila sea exactamente 1.

### 2. Cálculo de Posiciones (Geometría Circular)

Utilizamos la fórmula angular para distribuir los estados en un círculo horario empezando por la parte superior: $$\text{Ángulo}_i = 90^\circ - i \cdot \left(\frac{360^\circ}{N}\right)$$

**Desarrollo de las coordenadas $(x, y) = (6 + 5.5\cos\theta, 6 + 5.5\sin\theta)$:**

- **Estado 0 ($i=0$):** $90^\circ - 0 \cdot (360/7) = 90^\circ$.
    - $x_0 = 6 + 5.5\cos(90^\circ) = 6 + 0 = 6$.
    - $y_0 = 6 + 5.5\sin(90^\circ) = 6 + 5.5 = 11.5$.
    - **Coordenada:** $(6, 11.5)$.
- **Estado 1 ($i=1$):** $90^\circ - 51.43^\circ \approx 38.57^\circ$.
    - $x_1 = 6 + 5.5\cos(38.57^\circ) \approx 6 + 4.3 = 10.3$.
    - $y_1 = 6 + 5.5\sin(38.57^\circ) \approx 6 + 3.4 = 9.4$.
    - **Coordenada:** $(10.3, 9.4)$.
- **Estado 2 ($i=2$):** $90^\circ - 102.86^\circ = -12.86^\circ$.
    - $x_2 = 6 + 5.5\cos(-12.86^\circ) \approx 6 + 5.4 = 11.4$.
    - $y_2 = 6 + 5.5\sin(-12.86^\circ) \approx 6 - 1.2 = 4.8$.
    - **Coordenada:** $(11.4, 4.8)$.
- **Estado 3 ($i=3$):** $90^\circ - 154.29^\circ = -64.29^\circ$.
    - $x_3 = 6 + 5.5\cos(-64.29^\circ) \approx 6 + 2.4 = 8.4$.
    - $y_3 = 6 + 5.5\sin(-64.29^\circ) \approx 6 - 5.0 = 1.0$.
    - **Coordenada:** $(8.4, 1)$.
- **Estado 4 ($i=4$):** $90^\circ - 205.71^\circ = -115.71^\circ$.
    - $x_4 = 6 + 5.5\cos(-115.71^\circ) \approx 6 - 2.4 = 3.6$.
    - $y_4 = 6 + 5.5\sin(-115.71^\circ) \approx 6 - 5.0 = 1.0$.
    - **Coordenada:** $(3.6, 1)$.
- **Estado 5 ($i=5$):** $90^\circ - 257.14^\circ = -167.14^\circ$.
    - $x_5 = 6 + 5.5\cos(-167.14^\circ) \approx 6 - 5.4 = 0.6$.
    - $y_5 = 6 + 5.5\sin(-167.14^\circ) \approx 6 - 1.2 = 4.8$.
    - **Coordenada:** $(0.6, 4.8)$.
- **Estado 6 ($i=6$):** $90^\circ - 308.57^\circ = -218.57^\circ \equiv 141.43^\circ$.
    - $x_6 = 6 + 5.5\cos(141.43^\circ) \approx 6 - 4.3 = 1.7$.
    - $y_6 = 6 + 5.5\sin(141.43^\circ) \approx 6 + 3.4 = 9.4$.
    - **Coordenada:** $(1.7, 9.4)$.

### 3. Razonamiento Detallado del Diagrama

- **Bucles (Self-loops):** Se dibujan utilizando curvas de control que apuntan hacia afuera del centro para evitar colisiones. Por ejemplo, para $S_0$ (arriba), el bucle usa `controls (5,12.5) and (7,12.5)` para elevarse sobre el nodo.
- **Transiciones:** Se utiliza `bend left=20` para las flechas de un estado a otro. El color de la flecha coincide con el color del nodo de origen.
- **Formato de Código:** El bloque de código se envuelve en un entorno LaTeX completo (document) para asegurar su compatibilidad.

### 4. Código TikZ Final

```tikz
%\documentclass%[tikz,border=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=stealth, auto, node distance=2.5cm]

    % ESTILOS DE NODOS (Sin relleno 'fill' para legibilidad)
    \tikzstyle{state} = [circle, draw, thick, minimum size=1cm]

    % 1. DIBUJO DE NODOS (Ubicación circular radio 5.5)
    \node[state, color=cyan] (S0) at (6,11.5) {$S_0$};
    \node[state, color=blue] (S1) at (10.3,9.4) {$S_1$};
    \node[state, color=green!60!black] (S2) at (11.4,4.8) {$S_2$};
    \node[state, color=orange] (S3) at (8.4,1) {$S_3$};
    \node[state, color=purple] (S4) at (3.6,1) {$S_4$};
    \node[state, color=yellow!80!black] (S5) at (0.6,4.8) {$S_5$};
    \node[state, color=magenta] (S6) at (1.7,9.4) {$S_6$};

    % 2. BUCLES (Probabilidad p_ii = 0.7) - Curvas de control externas
    \path[ultra thick, cyan] (S0) .. controls (5,12.5) and (7,12.5) .. (S0) node[pos=0.5, above] {0.7};
    \path[ultra thick, blue] (S1) .. controls (11.3,10.4) and (11.8,8.4) .. (S1) node[pos=0.5, right] {0.7};
    \path[ultra thick, green!60!black] (S2) .. controls (12.4,5.8) and (12.4,3.8) .. (S2) node[pos=0.5, right] {0.7};
    \path[ultra thick, orange] (S3) .. controls (9.4,0) and (7.4,0) .. (S3) node[pos=0.5, below] {0.7};
    \path[ultra thick, purple] (S4) .. controls (4.6,0) and (2.6,0) .. (S4) node[pos=0.5, below] {0.7};
    \path[ultra thick, yellow!80!black] (S5) .. controls (-0.4,3.8) and (-0.4,5.8) .. (S5) node[pos=0.5, left] {0.7};
    \path[ultra thick, magenta] (S6) .. controls (0.7,8.4) and (1.2,10.4) .. (S6) node[pos=0.5, left] {0.7};

    % 3. TRANSICIONES (Probabilidad p_ij = 0.3) - Flechas curvas
    \draw[->, very thick, cyan] (S0) to [bend left=20] node {0.3} (S1);
    \draw[->, very thick, blue] (S1) to [bend left=20] node {0.3} (S2);
    \draw[->, very thick, green!60!black] (S2) to [bend left=20] node {0.3} (S3);
    \draw[->, very thick, orange] (S3) to [bend left=20] node {0.3} (S4);
    \draw[->, very thick, purple] (S4) to [bend left=20] node {0.3} (S5);
    \draw[->, very thick, yellow!80!black] (S5) to [bend left=20] node {0.3} (S6);
    \draw[->, very thick, magenta] (S6) to [bend left=20] node {0.3} (S0);

\end{tikzpicture}
\end{document}
```

### 5. Verificación de Resultados

- **Normalización:** Para cada estado, la probabilidad de salida es $0.7$ (bucle) + $0.3$ (transición al siguiente) = $1.0$. Esto cumple con la condición fundamental de las cadenas de Markov.
- **Estética:** Los nodos no tienen relleno, lo que permite que el texto "$S_i$" sea perfectamente legible en el color del estado correspondiente.
- **Geometría:** El radio de $5.5$ asegura que el diagrama ocupe un espacio cómodo en una grilla de $12 \times 12$ sin tocar los bordes.


