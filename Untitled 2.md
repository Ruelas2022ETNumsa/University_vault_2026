##### Ej. Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene a la polea $m_3$. La polea $m_3$ cuelga del ramal derecho de $m_2$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente. La distancia $a$ se mide desde el centro de $m_1$ hasta el centro de $m_3$. Hallar las ecuaciones de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-0.5,6.0) rectangle (5.0,6.3);
    \draw[thick] (-0.5,6.0) -- (5.0,6.0);

    % Piso
    \fill[pattern=north east lines] (-0.5,-0.3) rectangle (5.0,0);
    \draw[thick] (-0.5,0) -- (5.0,0);

    % Resorte K — techo a polea 1
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,6.0) -- (1.0,4.8);
    \node[left, maincolor] at (0.75,5.4) {$K$};

    % Polea 1 (m1)
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,4.5) circle (0.3);
    \fill[maincolor] (1.0,4.5) circle (0.05);
    \node[left, maincolor] at (0.55,4.5) {$m_1$};

    % Cable 1 — ramal izquierdo al piso
    \draw[thick, maincolor] (0.7,4.5) -- (0.7,0);

    % Cable 1 — ramal derecho a polea 2
    \draw[thick, maincolor] (1.3,4.5) -- (1.3,3.0);

    % Polea 2 (m2)
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,2.7) circle (0.3);
    \fill[accentcolor] (1.3,2.7) circle (0.05);
    \node[left, accentcolor] at (0.85,2.7) {$m_2$};

    % Cable 2 — ramal izquierdo al piso
    \draw[thick, accentcolor] (1.0,2.7) -- (1.0,0);

    % Cable 2 — ramal derecho a polea 3
    \draw[thick, accentcolor] (1.6,2.7) -- (1.6,1.5);

    % Polea 3 (m3)
    \draw[thick, fill=teal!10, draw=maincolor] (1.6,1.2) circle (0.3);
    \fill[maincolor] (1.6,1.2) circle (0.05);
    \node[left, maincolor] at (1.15,1.2) {$m_3$};

    % Cable 3 — ramal izquierdo al piso
    \draw[thick, maincolor] (1.3,1.2) -- (1.3,0);

    % Cable 3 — ramal derecho al resorte K'
    \draw[thick, maincolor] (1.9,1.2) -- (1.9,0.8);

    % Resorte K' — al piso
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,0.8) -- (1.9,0);
    \node[right, accentcolor] at (2.0,0.4) {$K'$};

    % Cota H — altura total
    \draw[<->, red, thick] (-0.3,0) -- (-0.3,6.0) node[midway, left] {$H$};

    % Coordenada y1 — techo a m1
    \draw[->, maincolor, thick] (2.5,6.0) -- (2.5,4.5) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,4.5) -- (2.6,4.5);
    \draw[dotted] (1.0,6.0) -- (2.6,6.0);

    % Coordenada y2 — techo a m2
    \draw[->, accentcolor, thick] (3.2,6.0) -- (3.2,2.7) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,2.7) -- (3.3,2.7);

    % Coordenada y3 — techo a m3
    \draw[->, maincolor, thick] (3.9,6.0) -- (3.9,1.2) node[midway, right] {$y_3$};
    \draw[dotted] (1.6,1.2) -- (4.0,1.2);

    % Cota a — distancia de m1 a m3
    \draw[<->, maincolor, thick] (2.1,4.5) -- (2.1,1.2) node[midway, left] {$a$};

\end{tikzpicture}
\end{document}
```

**Resolución**
Se determinan las relaciones de restricción cinemática asociadas a los cables inextensibles, se formulan las energías cinética y potencial en función de la coordenada independiente seleccionada y se aplica la ecuación de Euler-Lagrange.

**Paso 1 — Coordenadas, ecuaciones de restricción y grados de libertad**

Vector de coordenadas posibles del sistema:

$$
N = (y_1,\ y_2,\ y_3)
$$


Restricción cinemática del primer cable (asociado a $m_1$):

$$
(H - y_1) + \pi R_1 + (y_2 - y_1) = L_1 \implies y_2 - 2 y_1 = C_1
$$


$$
y_2 = 2 y_1 + C_1 \implies \dot{y}_2 = 2 \dot{y}_1
$$


Restricción cinemática del segundo cable (asociado a $m_2$):

$$
(H - y_2) + \pi R_2 + (y_3 - y_2) = L_2 \implies y_3 - 2 y_2 = C_2
$$


$$
y_3 = 2(2 y_1 + C_1) + C_2 = 4 y_1 + 2 C_1 + C_2 \implies \dot{y}_3 = 4 \dot{y}_1
$$


Relación cinemática para la cota de separación $a$:

$$
a = y_3 - y_1 = 3 y_1 + 2 C_1 + C_2 \implies \dot{a} = 3 \dot{y}_1
$$


Número de grados de libertad del sistema:

$$
\text{GDL} = N - \text{restricciones} = 3 - 2 = 1
$$


Coordenada generalizada independiente seleccionada: $y_1$.

**Paso 2 — Energía cinética del sistema**

Expresión de la energía cinética traslacional del sistema (poleas sin inercia rotacional):

$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$


Sustituyendo las relaciones de velocidad $\dot{y}_2 = 2 \dot{y}_1$ y $\dot{y}_3 = 4 \dot{y}_1$:

$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (2 \dot{y}_1)^2 + \frac{1}{2} m_3 (4 \dot{y}_1)^2
$$


$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (4 \dot{y}_1^2) + \frac{1}{2} m_3 (16 \dot{y}_1^2)
$$


$$
T = \frac{1}{2} (m_1 + 4 m_2 + 16 m_3) \dot{y}_1^2
$$


**Paso 3 — Energía potencial del sistema**

Energía potencial gravitatoria (tomando el techo como origen de referencia y el sentido hacia abajo como positivo):

$$
V_g = - m_1 g y_1 - m_2 g y_2 - m_3 g y_3
$$


$$
V_g = - m_1 g y_1 - m_2 g (2 y_1 + C_1) - m_3 g (4 y_1 + 2 C_1 + C_2)
$$


$$
V_g = - (m_1 + 2 m_2 + 4 m_3) g y_1 - \text{cte}
$$


Deformación y energía elástica del resorte $K$ (suspendido del techo):

$$
\Delta \ell_K = y_1 - R_1 - \ell_0 = y_1 - C_0
$$


$$
V_K = \frac{1}{2} K (y_1 - C_0)^2
$$


Deformación y energía elástica del resorte $K'$ (conectado al piso mediante el tercer cable):

$$
L_3 = (H - y_3) + \pi R_3 + \ell_{\text{ramal}}
$$


$$
y_{s} = y_3 + \ell_{\text{ramal}} = 2 y_3 + L_3 - H - \pi R_3
$$


$$
\ell_{K'} = H - y_{s} = 2 H - L_3 + \pi R_3 - 2 y_3
$$


$$
\Delta \ell_{K'} = \ell_{K'} - \ell_0' = C_0' - 2 y_3 \quad \text{con } C_0' = 2 H - L_3 + \pi R_3 - \ell_0'
$$

Sustituyendo $y_3 = 4 y_1 + 2 C_1 + C_2$:

$$
\Delta \ell_{K'} = C_0'' - 8 y_1 \quad \text{con } C_0'' = C_0' - 4 C_1 - 2 C_2
$$


$$
V_{K'} = \frac{1}{2} K' (C_0'' - 8 y_1)^2
$$


Energía potencial total del sistema:

$$
V = \frac{1}{2} K (y_1 - C_0)^2 + \frac{1}{2} K' (C_0'' - 8 y_1)^2 - (m_1 + 2 m_2 + 4 m_3) g y_1
$$


**Paso 4 — Ecuación de movimiento de Lagrange**

Ecuación de Euler-Lagrange para la coordenada generalizada $y_1$:

$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_1}\right) - \frac{\partial T}{\partial y_1} = -\frac{\partial V}{\partial y_1}
$$


Evaluación de las derivadas de la energía cinética:

$$
\frac{\partial T}{\partial \dot{y}_1} = (m_1 + 4 m_2 + 16 m_3) \dot{y}_1
$$


$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_1}\right) = (m_1 + 4 m_2 + 16 m_3) \ddot{y}_1
$$


$$
\frac{\partial T}{\partial y_1} = 0
$$


Evaluación de la derivada de la energía potencial:

$$
-\frac{\partial V}{\partial y_1} = - K (y_1 - C_0) - K' (C_0'' - 8 y_1)(-8) + (m_1 + 2 m_2 + 4 m_3) g
$$


$$
-\frac{\partial V}{\partial y_1} = - K (y_1 - C_0) + 8 K' (C_0'' - 8 y_1) + (m_1 + 2 m_2 + 4 m_3) g
$$


Sustituyendo los términos en la ecuación de Lagrange:

$$
(m_1 + 4 m_2 + 16 m_3) \ddot{y}_1 + K (y_1 - C_0) - 8 K' (C_0'' - 8 y_1) = (m_1 + 2 m_2 + 4 m_3) g
$$


Expresando en términos de las deformaciones instantáneas de los resortes $\Delta \ell_K = y_1 - C_0$ y $\Delta \ell_{K'} = C_0' - 2 y_3$:

$$
\boxed{(m_1 + 4 m_2 + 16 m_3) \ddot{y}_1 + K \Delta \ell_K - 8 K' \Delta \ell_{K'} = (m_1 + 2 m_2 + 4 m_3) g}
$$


Alternativamente, en términos de la aceleración de la cota $a$ ($\ddot{y}_1 = \frac{1}{3}\ddot{a}$):

$$
\boxed{\frac{1}{3}(m_1 + 4 m_2 + 16 m_3) \ddot{a} + K \Delta \ell_K - 8 K' \Delta \ell_{K'} = (m_1 + 2 m_2 + 4 m_3) g}
$$



