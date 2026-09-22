##### Ej. Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$ a una distancia $a$ por debajo de ella; su ramal izquierdo está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$, y su ramal derecho sostiene a la masa puntual $m_3$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente. Hallar las ecuaciones de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,7.3) rectangle (5.5,7.6);
    \draw[thick] (-1,7.3) -- (5.5,7.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (5.5,0);
    \draw[thick] (-1,0) -- (5.5,0);

    % Resorte K — techo a m1
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,7.3) -- (1.0,6.0);
    \node[left, maincolor] at (0.75,6.65) {$K$};

    % Polea m1 (teal)
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,5.7) circle (0.3);
    \fill[maincolor] (1.0,5.7) circle (0.05);
    \node[left, maincolor] at (0.5,5.7) {$m_1$};

    % Ramal izquierdo de m1 — cable fijo al piso
    \draw[thick, maincolor] (0.7,5.7) -- (0.7,0);

    % Ramal derecho de m1 — cable baja a m2
    \draw[thick, maincolor] (1.3,5.7) -- (1.3,3.7);

    % Polea m2 (accentcolor)
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (1.3,3.4) circle (0.3);
    \fill[accentcolor] (1.3,3.4) circle (0.05);
    \node[left, accentcolor] at (0.8,3.4) {$m_2$};

    % Ramal izquierdo de m2 — resorte K' al piso
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.0,3.4) -- (1.0,0);
    \node[left, accentcolor] at (0.8,1.5) {$K'$};

    % Ramal derecho de m2 — cuelga m3
    \draw[thick, accentcolor] (1.6,3.4) -- (1.6,1.4);
    \draw[thick, fill=accentcolor!30, draw=accentcolor] (1.6,1.4) circle (0.15);
    \node[right, accentcolor] at (1.8,1.4) {$m_3$};

    % Cota H
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,7.3) node[midway, left] {$H$};

    % Coordenada y1 — techo a m1
    \draw[->, maincolor, thick] (2.8,7.3) -- (2.8,5.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,7.3) -- (2.9,7.3);
    \draw[dotted] (1.0,5.7) -- (2.9,5.7);

    % Coordenada y2 — techo a m2
    \draw[->, accentcolor, thick] (3.5,7.3) -- (3.5,3.4) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,3.4) -- (3.6,3.4);

    % Coordenada y3 — techo a m3
    \draw[->, maincolor, thick] (4.2,7.3) -- (4.2,1.4) node[midway, right] {$y_3$};
    \draw[dotted] (1.6,1.4) -- (4.3,1.4);

    % Cota a — m1 a m2
    \draw[<->, maincolor, thick] (2.1,5.7) -- (2.1,3.4) node[midway, right] {$a$};
    \draw[dotted] (1.3,5.7) -- (2.2,5.7);
    \draw[dotted] (1.3,3.4) -- (2.2,3.4);

\end{tikzpicture}
\end{document}
```

**Resolución**
Se establecen las relaciones de ligadura cinemática para los cables del sistema, se construyen la energía cinética y potencial para determinar la función Lagrangiana, y se aplican las ecuaciones de Euler-Lagrange.

---

### Caso 1 — Sistema con ligaduras de cables anclados al piso (1 GDL)

**Paso 1 — Ligaduras cinemáticas y coordenadas generalizadas**


$$
L_1 = (H - y_1) + \pi R_1 + (y_2 - y_1) = H + \pi R_1 + y_2 - 2y_1 = \text{cte}
$$



$$
\dot{y}_1 = \dfrac{\dot{y}_2}{2}
$$



$$
y_1 = \dfrac{y_2 - C_1}{2} \qquad \text{donde } C_1 = L_1 - H - \pi R_1
$$



$$
L_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = H + \pi R_2 + y_3 - 2y_2 = \text{cte}
$$



$$
\dot{y}_3 = 2\dot{y}_2
$$



$$
y_3 = 2y_2 + C_2 \qquad \text{donde } C_2 = L_2 - H - \pi R_2
$$



$$
\text{GDL} = 3 - 2 = 1 \implies q = y_2
$$


**Paso 2 — Energía cinética del sistema**


$$
T = \dfrac{1}{2}m_1\dot{y}_1^2 + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2
$$



$$
T = \dfrac{1}{2}m_1\left(\dfrac{\dot{y}_2}{2}\right)^{\!2} + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\left(2\dot{y}_2\right)^{\!2}
$$



$$
\boxed{T = \dfrac{1}{2}\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2^2}
$$


**Paso 3 — Energía potencial total**


$$
V = V_g + V_K + V_{K'}
$$



$$
V_g = -m_1 g y_1 - m_2 g y_2 - m_3 g y_3
$$



$$
V_g = -\left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g y_2 + \text{cte}
$$



$$
V_K = \dfrac{1}{2}K\left(y_1 - \ell_0\right)^2 = \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^2
$$



$$
V_{K'} = \dfrac{1}{2}K'\left(H - y_2 - \ell_0'\right)^2
$$



$$
\boxed{V = -\left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g y_2 + \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^2 + \dfrac{1}{2}K'\left(H - y_2 - \ell_0'\right)^2}
$$


**Paso 4 — Función Lagrangiana**


$$
L = T - V
$$



$$
L = \dfrac{1}{2}\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2^2 + \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g y_2 - \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^2 - \dfrac{1}{2}K'\left(H - y_2 - \ell_0'\right)^2
$$


**Paso 5 — Ecuación diferencial de movimiento**


$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) - \dfrac{\partial L}{\partial y_2} = 0
$$



$$
\dfrac{\partial L}{\partial \dot{y}_2} = \left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2
$$



$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) = \left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2
$$



$$
\dfrac{\partial L}{\partial y_2} = \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g - \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right) + K'\left(H - y_2 - \ell_0'\right)
$$



$$
\boxed{\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2 + \left(\dfrac{K}{8} + K'\right)y_2 = \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g + \dfrac{K}{4}\left(\dfrac{C_1}{2} + \ell_0\right) + K'(H - \ell_0')}
$$


---

### Caso 2 — Sistema con coordenada $y_3$ independiente acoplada al resorte $K'$ (2 GDL)

**Paso 1 — Coordenadas generalizadas y posición del extremo del resorte $K'$**


$$
q_1 = y_2, \qquad q_2 = y_3
$$



$$
y_1 = \dfrac{y_2 - C_1}{2} \implies \dot{y}_1 = \dfrac{\dot{y}_2}{2}
$$



$$
L_2 = (y_s - y_2) + \pi R_2 + (y_3 - y_2) = y_s + y_3 - 2y_2 + \pi R_2 = \text{cte} \implies y_s = 2y_2 - y_3 + C_2
$$



$$
\text{GDL} = 2
$$


**Paso 2 — Energía cinética y potencial del sistema**


$$
T = \dfrac{1}{2}m_1\dot{y}_1^2 + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2 = \dfrac{1}{2}\left(\dfrac{m_1}{4} + m_2\right)\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2
$$



$$
V = -m_1 g y_1 - m_2 g y_2 - m_3 g y_3 + \dfrac{1}{2}K\left(y_1 - \ell_0\right)^2 + \dfrac{1}{2}K'\left(H - y_s - \ell_0'\right)^2
$$



$$
V = -\left(\dfrac{m_1}{2} + m_2\right)g y_2 - m_3 g y_3 + \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^2 + \dfrac{1}{2}K'\left(H - 2y_2 + y_3 - C_2 - \ell_0'\right)^2
$$


**Paso 3 — Función Lagrangiana**


$$
L = \dfrac{1}{2}\left(\dfrac{m_1}{4} + m_2\right)\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2 + \left(\dfrac{m_1}{2} + m_2\right)g y_2 + m_3 g y_3 - \dfrac{1}{2}K\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^2 - \dfrac{1}{2}K'\left(H - 2y_2 + y_3 - C_2 - \ell_0'\right)^2
$$


**Paso 4 — Ecuaciones diferenciales de movimiento acopladas**


$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) - \dfrac{\partial L}{\partial y_2} = 0
$$



$$
\boxed{\left(\dfrac{m_1}{4} + m_2\right)\ddot{y}_2 + \left(\dfrac{K}{8} + 2K'\right)y_2 - K' y_3 = \left(\dfrac{m_1}{2} + m_2\right)g + \dfrac{K}{4}\left(\dfrac{C_1}{2} + \ell_0\right) + K'(H - C_2 - \ell_0')}
$$



$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{y}_3}\right) - \dfrac{\partial L}{\partial y_3} = 0
$$



$$
\boxed{m_3 \ddot{y}_3 + K' y_3 - 2K' y_2 = m_3 g - K'(H - C_2 - \ell_0')}
$$

