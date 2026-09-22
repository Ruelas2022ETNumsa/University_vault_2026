##### Ej. Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal, conectado a una pared fija a su izquierda mediante un resorte de constante $K$ y longitud natural $\ell_0$. Un cable inextensible sale del lado derecho de $m_1$, pasa por una polea fija en el borde de la superficie y desciende verticalmente a lo largo de una pared vertical. La masa $m_2$ desciende rozando la pared vertical con coeficiente de amortiguamiento viscoso $c_2$; de su parte inferior cuelga, mediante un resorte de constante $K'$ y longitud natural $\ell_0'$, la masa $m_3$ que también roza la misma pared con coeficiente $c_3$. La altura total del sistema vertical es $H$. Las coordenadas $x_1$ (desde la pared izquierda hasta el centro de $m_1$), $y_2$ e $y_3$ (desde la polea hacia abajo hasta el centro de $m_2$ y $m_3$ respectivamente) describen la configuración del sistema. Hallar las ecuaciones de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.5,0) rectangle (0,2.2);
    \draw[thick] (0,0) -- (0,2.2);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.2) rectangle (5.0,0);
    \draw[thick] (0,0) -- (5.0,0);

    % Pared vertical derecha
    \fill[pattern=north east lines] (5.3,-4.2) rectangle (5.6,0);
    \draw[thick] (5.0,0) -- (5.0,-4.2);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (0,1.0) -- (1.5,1.0);
    \node[above, maincolor] at (0.75,1.15) {$K$};

    % Bloque m1
    \draw[fill=teal!10, draw=maincolor, thick] (1.5,0.3) rectangle (2.7,1.7);
    \node[maincolor] at (2.1,1.0) {$m_1$};

    % Polea fija
    \draw[thick, fill=gray!20] (5.0,1.0) circle (0.25);
    \fill (5.0,1.0) circle (0.04);
    \draw[thick] (5.0,0) -- (5.0,0.75);

    % Cable
    \draw[thick] (2.7,1.25) -- (5.0,1.25);
    \draw[thick] (5.25,1.0) -- (5.25,-1.0);

    % Bloque m2
    \draw[fill=teal!10, draw=maincolor, thick] (5.0,-1.7) rectangle (5.8,-1.0);
    \node[maincolor] at (5.4,-1.35) {$m_2$};

    % Resorte K'
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (5.4,-1.7) -- (5.4,-2.7);
    \node[right, accentcolor] at (5.55,-2.2) {$K'$};

    % Bloque m3
    \draw[fill=orange!10, draw=accentcolor, thick] (5.0,-3.4) rectangle (5.8,-2.7);
    \node[accentcolor] at (5.4,-3.05) {$m_3$};

    % Coordenadas
    \draw[->, maincolor, thick] (0,2.1) -- (2.1,2.1) node[midway, above] {$x_1$};
    \draw[dotted] (2.1,1.7) -- (2.1,2.3);
    \draw[dotted] (0,2.0) -- (0,2.3);

    \draw[->, maincolor, thick] (6.5,1.0) -- (6.5,-1.35) node[midway, right] {$y_2$};
    \draw[dotted] (5.8,-1.35) -- (6.7,-1.35);
    \draw[dotted] (5.0,1.0) -- (6.7,1.0);

    \draw[->, accentcolor, thick] (7.3,1.0) -- (7.3,-3.05) node[midway, right] {$y_3$};
    \draw[dotted] (5.8,-3.05) -- (7.5,-3.05);

\end{tikzpicture}
\end{document}
```

**Resolución**
Se establece la relación cinematica del cable inextensible para reducir los grados de libertad, se formulan la energía cinética, la energía potencial y la función de disipación de Rayleigh, y se aplican las ecuaciones de Euler-Lagrange.

**Paso 1 — Relación de ligadura entre las coordenadas del cable**


$$
L_c = \left(d_p - x_1 - \dfrac{b_1}{2}\right) + \pi R + \left(y_2 - \dfrac{b_2}{2}\right) = \text{cte}
$$



$$
y_2 - x_1 = C_0 \implies x_1 = y_2 - C_0
$$



$$
\dot{x}_1 = \dot{y}_2
$$


**Paso 2 — Energía cinética del sistema**


$$
T = \dfrac{1}{2}m_1 \dot{x}_1^2 + \dfrac{1}{2}m_2 \dot{y}_2^2 + \dfrac{1}{2}m_3 \dot{y}_3^2
$$



$$
T = \dfrac{1}{2}(m_1 + m_2)\dot{y}_2^2 + \dfrac{1}{2}m_3 \dot{y}_3^2
$$


**Paso 3 — Energía potencial total del sistema**


$$
V_g = -m_2 g y_2 - m_3 g y_3
$$



$$
\Delta \ell_K = x_1 - \dfrac{b_1}{2} - \ell_0
$$



$$
\Delta \ell_{K'} = y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'
$$



$$
V = -m_2 g y_2 - m_3 g y_3 + \dfrac{1}{2}K\left(x_1 - \dfrac{b_1}{2} - \ell_0\right)^{\!2} + \dfrac{1}{2}K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right)^{\!2}
$$


**Paso 4 — Función de disipación de Rayleigh**


$$
F_D = \dfrac{1}{2}c_2 \dot{y}_2^2 + \dfrac{1}{2}c_3 \dot{y}_3^2
$$


**Paso 5 — Función Lagrangiana del sistema**


$$
L = T - V
$$



$$
L = \dfrac{1}{2}(m_1 + m_2)\dot{y}_2^2 + \dfrac{1}{2}m_3 \dot{y}_3^2 + m_2 g y_2 + m_3 g y_3 - \dfrac{1}{2}K\left(x_1 - \dfrac{b_1}{2} - \ell_0\right)^{\!2} - \dfrac{1}{2}K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right)^{\!2}
$$


**Paso 6 — Ecuación de movimiento para la coordenada $y_2$**


$$
\dfrac{\partial L}{\partial \dot{y}_2} = (m_1 + m_2)\dot{y}_2 \implies \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) = (m_1 + m_2)\ddot{y}_2
$$



$$
\dfrac{\partial L}{\partial y_2} = m_2 g - K\left(x_1 - \dfrac{b_1}{2} - \ell_0\right) + K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right)
$$



$$
\dfrac{\partial F_D}{\partial \dot{y}_2} = c_2 \dot{y}_2
$$



$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) - \dfrac{\partial L}{\partial y_2} + \dfrac{\partial F_D}{\partial \dot{y}_2} = 0
$$



$$
\boxed{(m_1 + m_2)\ddot{y}_2 + c_2 \dot{y}_2 + K\left(x_1 - \dfrac{b_1}{2} - \ell_0\right) - K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right) = m_2 g}
$$


**Paso 7 — Ecuación de movimiento para la coordenada $y_3$**


$$
\dfrac{\partial L}{\partial \dot{y}_3} = m_3 \dot{y}_3 \implies \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_3}\right) = m_3 \ddot{y}_3
$$



$$
\dfrac{\partial L}{\partial y_3} = m_3 g - K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right)
$$



$$
\dfrac{\partial F_D}{\partial \dot{y}_3} = c_3 \dot{y}_3
$$



$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_3}\right) - \dfrac{\partial L}{\partial y_3} + \dfrac{\partial F_D}{\partial \dot{y}_3} = 0
$$



$$
\boxed{m_3 \ddot{y}_3 + c_3 \dot{y}_3 + K'\!\left(y_3 - y_2 - \dfrac{b_2 + b_3}{2} - \ell_0'\right) = m_3 g}
$$

