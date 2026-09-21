##### Ej. Sistema compuesto por un bloque $m_1$ en superficie horizontal con resorte $K$ y dos masas colgantes $m_2$ y $m_3$ conectadas por un resorte $K'$

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    % Definición de colores
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.5,0) rectangle (0,2);
    \draw[thick] (0,0) -- (0,2);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.2) rectangle (5,0);
    \draw[thick] (0,0) -- (5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (0,1) -- (1.5,1);
    \node[above, maincolor] at (0.75,1.2) {$K$};

    % Bloque m1
    \draw[fill=teal!10, draw=maincolor, thick] (1.5,0.3) rectangle (2.8,1.7);
    \node[maincolor] at (2.15,1.0) {$m_1$};

    % Polea
    \draw[thick, fill=gray!20] (5,1) circle (0.3);
    \fill (5,1) circle (0.05);
    \draw[thick] (5,0) -- (5,1);

    % Cable
    \draw[thick] (2.8,1.3) -- (5,1.3);
    \draw[thick] (5.3,1) -- (5.3,-1);

    % Bloque m2
    \draw[fill=teal!10, draw=maincolor, thick] (4.8,-1.7) rectangle (5.8,-1);
    \node[maincolor] at (5.3,-1.35) {$m_2$};

    % Resorte K'
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (5.3,-1.7) -- (5.3,-2.8);
    \node[right, accentcolor] at (5.5,-2.25) {$K'$};

    % Bloque m3
    \draw[fill=orange!10, draw=accentcolor, thick] (4.8,-3.5) rectangle (5.8,-2.8);
    \node[accentcolor] at (5.3,-3.15) {$m_3$};

    % Coordenadas
    \draw[->, maincolor, thick] (0,2.1) -- (2.15,2.1) node[midway, above] {$x_1$};
    \draw[dotted] (2.15,1.7) -- (2.15,2.3);
    \draw[dotted] (0,2) -- (0,2.3);

    \draw[->, maincolor, thick] (6.5,1) -- (6.5,-1.35) node[midway, right] {$y_2$};
    \draw[dotted] (5.8,-1.35) -- (6.7,-1.35);
    \draw[dotted] (5,1) -- (6.7,1);

    \draw[->, accentcolor, thick] (7.3,1) -- (7.3,-3.15) node[midway, right] {$y_3$};
    \draw[dotted] (5.8,-3.15) -- (7.5,-3.15);
\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación**
Sistema mecánico translacional conservativo formado por tres masas ($m_1, m_2, m_3$) y dos resortes ($K, K'$). La masa $m_1$ se mueve horizontalmente en una superficie lisa acoplada a un resorte $K$, unida mediante un cable inextendible a la masa $m_2$. De la masa $m_2$ cuelga la masa $m_3$ mediante un resorte $K'$. Tema: Ecuaciones de Lagrange.

**Paso 1 — Coordenadas y GDL**
Coordenadas posibles del sistema:


$$
N = (x_1, y_2, y_3)
$$


Restricción por cable inextendible:


$$
\text{Vel}_1 = \text{Vel}_2 \implies \dot{x}_1 = \dot{y}_2 \implies x_1 = y_2 + C_0
$$


Número de grados de libertad:


$$
\text{GDL} = N - \text{restricciones} = 3 - 1 = 2
$$


Coordenadas independientes seleccionadas: $x_1$ e $y_3$.

**Paso 2 — Energía cinética**
Energía cinética total del sistema expresada con las coordenadas iniciales:


$$
T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$


Aplicando la restricción $\dot{y}_2 = \dot{x}_1$:


$$
T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{x}_1^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$


**Paso 3 — Energía potencial**
Energía potencial gravitatoria y elástica total del sistema:


$$
V = \frac{K}{2} \left(x_1 - \frac{b_1}{2} - l_0\right)^2 + m_1 g (0) - m_2 g y_2 - m_3 g y_3 + \frac{K'}{2} \left(y_3 - y_2 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)^2
$$


Sustituyendo la relación de restricción $y_2 = x_1 - C_0$:


$$
V = \frac{K}{2} \left(x_1 - \frac{b_1}{2} - l_0\right)^2 - m_2 g (x_1 - C_0) - m_3 g y_3 + \frac{K'}{2} \left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicando la ecuación de Lagrange para cada coordenada generalizada independiente:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}_r}\right) - \frac{\partial T}{\partial q_r} = -\frac{\partial V}{\partial q_r}
$$


1. Para la coordenada $x_1$:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_1}\right) = (m_1 + m_2) \ddot{x}_1, \quad \frac{\partial T}{\partial x_1} = 0
$$



$$
-\frac{\partial V}{\partial x_1} = -K\left(x_1 - \frac{b_1}{2} - l_0\right) + m_2 g + K'\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)
$$


Ecuación diferencial para $x_1$:


$$
m_1 \ddot{x}_1 + m_2 \ddot{x}_1 = -K\left(x_1 - \frac{b_1}{2} - l_0\right) + m_2 g + K'\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)
$$


2. Para la coordenada $y_3$:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) = m_3 \ddot{y}_3, \quad \frac{\partial T}{\partial y_3} = 0
$$



$$
-\frac{\partial V}{\partial y_3} = m_3 g - K'\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)
$$


Ecuación diferencial para $y_3$:


$$
m_3 \ddot{y}_3 = -K'(y_3 - x_1) + m_3 g - K'\left(C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)
$$


**Paso 5 — EDOs finales**


$$
\boxed{m_1 \ddot{x}_1 + m_2 \ddot{x}_1 = -K\left(x_1 - \frac{b_1}{2} - l_0\right) + m_2 g + K'\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)}
$$



$$
\boxed{m_3 \ddot{y}_3 = -K'(y_3 - x_1) + m_3 g - K'\left(C_0 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)}
$$

