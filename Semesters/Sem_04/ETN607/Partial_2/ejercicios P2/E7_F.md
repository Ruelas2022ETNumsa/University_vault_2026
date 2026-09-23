##### Ej. Sistema mecánico horizontal de tres masas acopladas por resortes, amortiguadores y fuerza externa aplicada en $m_2$

**Enunciado:**
Tres masas $m_1$, $m_2$ y $m_3$ se deslizan horizontalmente sin fricción sobre una superficie plana. La masa $m_1$ está conectada a la pared izquierda mediante el resorte $K_1$ y el amortiguador $C_1$ en paralelo. La masa $m_1$ y la masa $m_3$ están acopladas entre sí por el resorte $K_{13}$. La masa $m_1$ y la masa $m_2$ están acopladas por el amortiguador $C_{12}$. La masa $m_2$ está conectada a la pared izquierda mediante el resorte $K_2$, y está acoplada a la masa $m_3$ mediante el resorte $K_{23}$ y el amortiguador $C_{23}$ en paralelo; sobre $m_2$ actúa además una fuerza externa $F_2$ dirigida hacia la derecha. La masa $m_3$ está conectada a la pared derecha mediante el resorte $K_3$. Obtenga las ecuaciones de movimiento del sistema usando las ecuaciones de Lagrange y expréselas en forma matricial $M\ddot{x} + C\dot{x} + Kx = F$.

**Descripción de la figura:**
El diagrama muestra tres masas dispuestas horizontalmente entre dos paredes rígidas. La masa $m_1$ (bloque izquierdo) está suspendida entre la pared izquierda y los elementos que la acoplan al resto del sistema: hacia su izquierda se conectan en paralelo el resorte $K_1$ y el amortiguador $C_1$, ambos anclados a la pared izquierda; hacia su derecha, el resorte $K_{13}$ la comunica con $m_3$ y el amortiguador $C_{12}$ la comunica con $m_2$. La masa $m_2$ (bloque central-inferior) recibe por su izquierda el amortiguador $C_{12}$ proveniente de $m_1$ y el resorte $K_2$ anclado a la pared izquierda; por su derecha se conectan en paralelo el resorte $K_{23}$ y el amortiguador $C_{23}$, ambos hacia $m_3$, y sobre ella actúa la fuerza externa $F_2$ apuntando hacia la derecha. La masa $m_3$ (bloque derecho) recibe por su izquierda el resorte $K_{13}$ desde $m_1$, y el par $K_{23}$–$C_{23}$ desde $m_2$; por su derecha el resorte $K_3$ la conecta a la pared derecha.


```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.0, >=latex]

% Definición de colores
\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% Pared izquierda
\fill[pattern=north east lines] (-0.3,-0.5) rectangle (0,5.2);
\draw[thick] (0,-0.5) -- (0,5.2);

% Pared derecha
\fill[pattern=north east lines] (8.0,-0.5) rectangle (8.3,5.2);
\draw[thick] (8.0,-0.5) -- (8.0,5.2);

% Masa 1
\draw[fill=teal!10, draw=maincolor, thick]
    (2.0,2.8) rectangle (3.0,5.0);
\node[maincolor, font=\Large] at (2.5,3.9) {$1$};

% Masa 2 (elevada)
\draw[fill=teal!10, draw=maincolor, thick]
    (3.8,1.2) rectangle (4.8,3.6);
\node[maincolor, font=\Large] at (4.3,2.4) {$2$};

% Masa 3
\draw[fill=orange!10, draw=accentcolor, thick]
    (5.8,2.4) rectangle (6.8,5.0);
\node[accentcolor, font=\Large] at (6.3,3.7) {$3$};

% Resorte K1 (Pared a Masa 1)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (0,4.4) -- (2.0,4.4);
\node[above, maincolor] at (1.0,4.55) {$K_1$};

% Amortiguador C1 (Pared a Masa 1)
\draw[thick, maincolor] (0,3.3) -- (0.6,3.3);
\draw[thick, maincolor] (0.6,3.0) -- (0.6,3.6);
\draw[thick, maincolor] (0.5,3.6) -- (1.2,3.6);
\draw[thick, maincolor] (0.5,3.0) -- (1.2,3.0);
\draw[thick, maincolor] (1.0,3.15) -- (1.0,3.45);
\draw[thick, maincolor] (1.0,3.3) -- (2.0,3.3);
\node[above, maincolor] at (1.0,3.6) {$C_1$};

% Resorte K2 (Pared a Masa 2)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (0,1.8) -- (3.8,1.8);
\node[above, maincolor] at (1.9,1.95) {$K_2$};

% Resorte K13 (Masa 1 a Masa 3)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (3.0,4.4) -- (5.8,4.4);
\node[above, maincolor] at (4.4,4.55) {$K_{13}$};

% Amortiguador C12 (Masa 1 a Masa 2)
\draw[thick, maincolor]
    (3.0,3.1) -- (3.3,3.1) -- (3.3,2.6) -- (3.5,2.6);
\draw[thick, maincolor] (3.5,2.3) -- (3.5,2.9);
\draw[thick, maincolor] (3.4,2.9) -- (3.7,2.9);
\draw[thick, maincolor] (3.4,2.3) -- (3.7,2.3);
\draw[thick, maincolor] (3.65,2.45) -- (3.65,2.75);
\draw[thick, maincolor] (3.65,2.6) -- (3.8,2.6);
\node[above, maincolor] at (3.4,2.95) {$C_{12}$};

% Resorte K23 (Masa 2 a Masa 3)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2mm, coil}, decorate, maincolor, thick]
    (4.8,3.2) -- (5.8,3.2);
\node[above, maincolor] at (5.3,3.35) {$K_{23}$};

% Amortiguador C23 (Masa 2 a Masa 3)
\draw[thick, maincolor] (4.8,2.5) -- (5.1,2.5);
\draw[thick, maincolor] (5.1,2.2) -- (5.1,2.8);
\draw[thick, maincolor] (5.1,2.8) -- (5.6,2.8);
\draw[thick, maincolor] (5.1,2.2) -- (5.6,2.2);
\draw[thick, maincolor] (5.6,2.35) -- (5.6,2.65);
\draw[thick, maincolor] (5.6,2.5) -- (5.8,2.5);
\node[below, maincolor] at (5.3,2.15) {$C_{23}$};

% Resorte K3 (Masa 3 a Pared derecha)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, accentcolor, thick]
    (6.8,3.7) -- (8.0,3.7);
\node[above, accentcolor] at (7.4,3.85) {$K_3$};

% Fuerza F2
\draw[->, red, ultra thick] (4.8,1.8) -- (5.6,1.8)
    node[right] {$F_2$};

\end{tikzpicture}

\end{document}
```

---

**Paso 0 — Identificación**
Sistema mecánico translacional acoplado de 3 grados de libertad (3 GDL) con disipación viscosa, acoplamiento elástico y fuerza de excitación externa aplicada a la masa $m_2$.

**Paso 1 — Coordenadas y GDL**
Coordenadas independientes de desplazamiento horizontal: $x_1, x_2, x_3$ medidas a partir de las posiciones de equilibrio de cada cuerpo.
Grados de libertad: $\text{GDL} = 3$.

**Paso 2 — Energía cinética**
Energía cinética total del sistema $T$:


$$
T = \frac{1}{2}m_1\dot{x}_1^2 + \frac{1}{2}m_2\dot{x}_2^2 + \frac{1}{2}m_3\dot{x}_3^2
$$


Matriz de masa $M$:


$$
M = \begin{bmatrix} m_1 & 0 & 0 \\ 0 & m_2 & 0 \\ 0 & 0 & m_3 \end{bmatrix}
$$


**Paso 3 — Energía potencial**
Energía potencial elástica total acumulada en los resortes $K_1, K_2, K_3, K_{13}, K_{23}$:


$$
V = \frac{1}{2}K_1 x_1^2 + \frac{1}{2}K_2 x_2^2 + \frac{1}{2}K_3 x_3^2 + \frac{1}{2}K_{13}(x_3 - x_1)^2 + \frac{1}{2}K_{23}(x_3 - x_2)^2
$$


Función de disipación de Rayleigh para los amortiguadores $C_1, C_{12}, C_{23}$:


$$
\mathcal{F} = \frac{1}{2}C_1 \dot{x}_1^2 + \frac{1}{2}C_{12}(\dot{x}_2 - \dot{x}_1)^2 + \frac{1}{2}C_{23}(\dot{x}_3 - \dot{x}_2)^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicación de las ecuaciones de Lagrange extendidas para sistemas disipativos:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_i}\right) - \frac{\partial T}{\partial x_i} + \frac{\partial \mathcal{F}}{\partial \dot{x}_i} + \frac{\partial V}{\partial x_i} = F_i \qquad (i = 1, 2, 3)
$$


- Para $x_1$:


$$
m_1 \ddot{x}_1 + (C_1 + C_{12})\dot{x}_1 - C_{12}\dot{x}_2 + (K_1 + K_{13})x_1 - K_{13}x_3 = 0
$$


- Para $x_2$:


$$
m_2 \ddot{x}_2 - C_{12}\dot{x}_1 + (C_{12} + C_{23})\dot{x}_2 - C_{23}\dot{x}_3 + (K_2 + K_{23})x_2 - K_{23}x_3 = F_2
$$


- Para $x_3$:


$$
m_3 \ddot{x}_3 - C_{23}\dot{x}_2 + C_{23}\dot{x}_3 - K_{13}x_1 - K_{23}x_2 + (K_3 + K_{13} + K_{23})x_3 = 0
$$


**Paso 5 — EDOs finales**
Formulación en espacio matricial de la ecuación diferencial de movimiento $M\ddot{x} + C\dot{x} + Kx = F$:


$$
\boxed{\begin{bmatrix} m_1 & 0 & 0 \\ 0 & m_2 & 0 \\ 0 & 0 & m_3 \end{bmatrix} \begin{bmatrix} \ddot{x}_1 \\ \ddot{x}_2 \\ \ddot{x}_3 \end{bmatrix} + \begin{bmatrix} C_1 + C_{12} & -C_{12} & 0 \\ -C_{12} & C_{12} + C_{23} & -C_{23} \\ 0 & -C_{23} & C_{23} \end{bmatrix} \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} + \begin{bmatrix} K_1 + K_{13} & 0 & -K_{13} \\ 0 & K_2 + K_{23} & -K_{23} \\ -K_{13} & -K_{23} & K_3 + K_{13} + K_{23} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ F_2 \\ 0 \end{bmatrix}}
$$

