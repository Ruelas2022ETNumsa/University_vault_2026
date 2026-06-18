Este ejercicio se identifica como una **Cadena de Markov en tiempo discreto** porque el sistema evoluciona a través de un número finito de estados (las posibles composiciones de las bolas en la urna) y la probabilidad de transición al siguiente estado depende únicamente de la composición actual y de las reglas fijas establecidas (propiedad de Markov).

### 1. Identificación de Estados y Datos

Existen dos bolas en la urna. Denotaremos los posibles colores como:

- **U:** Sin pintar (Unpainted).
- **R:** Roja (Red).
- **N:** Negra (Black/Negra).

Los estados del sistema se definen por la combinación de colores de las dos bolas (el orden no importa):

- **Estado 0 ($S_0$):** ${U, U}$ — Dos bolas sin pintar.
- **Estado 1 ($S_1$):** ${R, U}$ — Una bola roja y una sin pintar.
- **Estado 2 ($S_2$):** ${N, U}$ — Una bola negra y una sin pintar.
- **Estado 3 ($S_3$):** ${R, R}$ — Dos bolas rojas.
- **Estado 4 ($S_4$):** ${N, N}$ — Dos bolas negras.
- **Estado 5 ($S_5$):** ${R, N}$ — Una bola roja y una negra.

---

### Diagrama de la Cadena de Markov

```tikz
\begin{document}
\begin{tikzpicture}
% Definición de estados (N=6, posicionamiento circular)
\node[draw,circle,thick,color=orange] (S0) at (90:4) {$S_0$};
\node[draw,circle,thick,color=pink] (S1) at (30:4) {$S_1$};
\node[draw,circle,thick,color=lime] (S2) at (330:4) {$S_2$};
\node[draw,circle,thick,color=purple] (S3) at (270:4) {$S_3$};
\node[draw,circle,thick,color=teal] (S4) at (210:4) {$S_4$};
\node[draw,circle,thick,color=magenta] (S5) at (150:4) {$S_5$};

% Transiciones desde S0 (0.5 a S1, 0.5 a S2)
\draw[->,very thick,orange] (S0) to[bend left=15] node[pos=0.3, right] {$0.5$} (S1);
\draw[->,very thick,orange] (S0) to[bend right=15] node[pos=0.3, left] {$0.5$} (S2);

% Transiciones desde S1 (0.5 a S2, 0.25 a S3, 0.25 a S5)
\draw[->,very thick,pink] (S1) to[bend left=15] node[pos=0.2, right] {$0.5$} (S2);
\draw[->,very thick,pink] (S1) to[bend left=15] node[pos=0.2, right] {$0.25$} (S3);
\draw[->,very thick,pink] (S1) to[bend right=15] node[pos=0.2, above] {$0.25$} (S5);

% Transiciones desde S2 (0.5 a S1, 0.25 a S4, 0.25 a S5)
\draw[->,very thick,lime] (S2) to[bend left=15] node[pos=0.2, left] {$0.5$} (S1);
\draw[->,very thick,lime] (S2) to[bend left=15] node[pos=0.2, left] {$0.25$} (S4);
\draw[->,very thick,lime] (S2) to[bend left=15] node[pos=0.2, below] {$0.25$} (S5);

% Transiciones desde S3 (1.0 a S5)
\draw[->,very thick,purple] (S3) to[bend right=15] node[pos=0.2, left] {$1.0$} (S5);

% Transiciones desde S4 (1.0 a S5)
\draw[->,very thick,teal] (S4) to[bend left=15] node[pos=0.2, left] {$1.0$} (S5);

% Transiciones desde S5 (0.5 a S3, 0.5 a S4)
\draw[->,very thick,magenta] (S5) to[bend right=15] node[pos=0.2, left] {$0.5$} (S3);
\draw[->,very thick,magenta] (S5) to[bend left=15] node[pos=0.2, left] {$0.5$} (S4);

\end{tikzpicture}
\end{document}
```

---

### 2. Análisis de Probabilidades de Transición ($P_{ij}$)

Para cada estado, analizamos qué sucede al seleccionar una bola y lanzar la moneda ($H$: cara, $T$: cruz):

- **Desde $S_0$ ${U, U}$:**
    
    - Se elige una bola $U$ (probabilidad $1.0$).
    - Si moneda es $H$ (prob $0.5$): la bola se pinta de Rojo $\rightarrow {R, U}$ ($S_1$).
    - Si moneda es $T$ (prob $0.5$): la bola se pinta de Negro $\rightarrow {N, U}$ ($S_2$).
    - $P_{01} = 0.5$, $P_{02} = 0.5$.
- **Desde $S_1$ ${R, U}$:**
    
    - Elegir bola $U$ (prob $0.5$): Si moneda es $H$ ($0.5$), pasa a ${R, R}$ ($S_3$); si es $T$ ($0.5$), pasa a ${R, N}$ ($S_5$).
    - Elegir bola $R$ (prob $0.5$): Cambia a Negro independientemente de la moneda $\rightarrow {N, U}$ ($S_2$).
    - $P_{13} = 0.5 \times 0.5 = 0.25$; $P_{15} = 0.5 \times 0.5 = 0.25$; $P_{12} = 0.5$.
- **Desde $S_2$ ${N, U}$:**
    
    - Elegir bola $U$ (prob $0.5$): Si moneda es $H$ ($0.5$), pasa a ${N, R}$ ($S_5$); si es $T$ ($0.5$), pasa a ${N, N}$ ($S_4$).
    - Elegir bola $N$ (prob $0.5$): Cambia a Rojo independientemente de la moneda $\rightarrow {R, U}$ ($S_1$).
    - $P_{25} = 0.5 \times 0.5 = 0.25$; $P_{24} = 0.5 \times 0.5 = 0.25$; $P_{21} = 0.5$.
- **Desde $S_3$ ${R, R}$:**
    
    - Cualquier bola elegida es $R$ (prob $1.0$). Cambia a Negro $\rightarrow {R, N}$ ($S_5$).
    - $P_{35} = 1.0$.
- **Desde $S_4$ ${N, N}$:**
    
    - Cualquier bola elegida es $N$ (prob $1.0$). Cambia a Rojo $\rightarrow {N, R}$ ($S_5$).
    - $P_{45} = 1.0$.
- **Desde $S_5$ ${R, N}$:**
    
    - Elegir bola $R$ (prob $0.5$): Cambia a Negro $\rightarrow {N, N}$ ($S_4$).
    - Elegir bola $N$ (prob $0.5$): Cambia a Rojo $\rightarrow {R, R}$ ($S_3$).
    - $P_{54} = 0.5$, $P_{53} = 0.5$.

---

### 3. Matriz de Probabilidades de Transición ($P$)

La matriz se construye colocando las probabilidades $P_{ij}$ donde la fila representa el estado actual y la columna el estado futuro.

$$P = \begin{bmatrix} 0 & 0.5 & 0.5 & 0 & 0 & 0 \ 0 & 0 & 0.5 & 0.25 & 0 & 0.25 \ 0 & 0.5 & 0 & 0 & 0.25 & 0.25 \ 0 & 0 & 0 & 0 & 0 & 1 \ 0 & 0 & 0 & 0 & 0 & 1 \ 0 & 0 & 0 & 0.5 & 0.5 & 0 \end{bmatrix}$$

### 4. Verificación

Comprobamos que la suma de cada renglón sea igual a 1 para asegurar que es una matriz estocástica válida:

- Fila 0: $0.5 + 0.5 = 1.0$ (Correcto)
- Fila 1: $0.5 + 0.25 + 0.25 = 1.0$ (Correcto)
- Fila 2: $0.5 + 0.25 + 0.25 = 1.0$ (Correcto)
- Fila 3: $1.0 = 1.0$ (Correcto)
- Fila 4: $1.0 = 1.0$ (Correcto)
- Fila 5: $0.5 + 0.5 = 1.0$ (Correcto)