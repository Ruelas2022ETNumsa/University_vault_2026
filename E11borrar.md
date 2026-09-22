
---
---
---
##### Ej. Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene a la polea $m_3$. La polea $m_3$ cuelga del ramal derecho de $m_2$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente. La distancia $a$ se mide desde el centro de $m_1$ hasta el centro de $m_3$. Hallar las ecuaciones de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-0.5,5.5) rectangle (4.5,5.8);
    \draw[thick] (-0.5,5.5) -- (4.5,5.5);

    % Piso
    \fill[pattern=north east lines] (-0.5,-0.3) rectangle (4.5,0);
    \draw[thick] (-0.5,0) -- (4.5,0);

    % Resorte K (techo a m1)
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,5.5) -- (1.0,4.2);
    \node[left, maincolor] at (0.75,4.85) {$K$};

    % Polea m1
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,3.9) circle (0.3);
    \fill[maincolor] (1.0,3.9) circle (0.05);
    \node[left, maincolor] at (0.55,3.9) {$m_1$};

    % Cable 1
    \draw[thick, maincolor] (0.7,3.9) -- (0.7,0);
    \draw[thick, maincolor] (1.3,3.9) -- (1.3,2.6);

    % Polea m2
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,2.3) circle (0.3);
    \fill[accentcolor] (1.3,2.3) circle (0.05);
    \node[right, accentcolor] at (1.65,2.3) {$m_2$};

    % Cable 2
    \draw[thick, accentcolor] (1.0,2.3) -- (1.0,0);
    \draw[thick, accentcolor] (1.6,2.3) -- (1.6,1.2);

    % Polea m3
    \draw[thick, fill=teal!10, draw=maincolor] (1.6,0.9) circle (0.3);
    \fill[maincolor] (1.6,0.9) circle (0.05);
    \node[left, maincolor] at (1.15,0.9) {$m_3$};

    % Cable 3
    \draw[thick, maincolor] (1.3,0.9) -- (1.3,0);
    \draw[thick, maincolor] (1.9,0.9) -- (1.9,0.6);

    % Resorte K'
    \draw[decoration={aspect=0.3, segment length=1.5mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,0.6) -- (1.9,0);
    \node[right, accentcolor] at (2.0,0.3) {$K'$};

    % Cota H
    \draw[<->, red, thick] (-0.3,0) -- (-0.3,5.5) node[midway, left] {$H$};

    % Coordenadas y1, y2, y3
    \draw[->, maincolor, thick] (2.5,5.5) -- (2.5,3.9) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,3.9) -- (2.6,3.9);

    \draw[->, accentcolor, thick] (3.1,5.5) -- (3.1,2.3) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,2.3) -- (3.2,2.3);

    \draw[->, maincolor, thick] (3.7,5.5) -- (3.7,0.9) node[midway, right] {$y_3$};
    \draw[dotted] (1.6,0.9) -- (3.8,0.9);

    % Cota a
    \draw[<->, accentcolor, thick] (2.1,3.9) -- (2.1,0.9) node[midway, right] {$a$};
    \draw[dotted] (1.0,3.9) -- (2.2,3.9);
    \draw[dotted] (1.6,0.9) -- (2.2,0.9);
\end{tikzpicture}
\end{document}
```

**Resolución**
Se determinan las ligaduras geométricas cinemáticas entre los tres cables inextensibles para reducir el sistema a un solo grado de libertad y aplicar las ecuaciones de Euler-Lagrange.

**Paso 1 — Análisis cinemático de ligaduras y grados de libertad**

$$
L_1 = (H - y_1) + (y_2 - y_1) + \pi R_1 = H + y_2 - 2y_1 + \pi R_1
$$

$$
y_2 = 2y_1 + L_1 - H - \pi R_1 \implies \dot{y}_2 = 2\dot{y}_1
$$



$$
L_2 = (H - y_2) + (y_3 - y_2) + \pi R_2 = H + y_3 - 2y_2 + \pi R_2
$$



$$
y_3 = 2y_2 + L_2 - H - \pi R_2 \implies \dot{y}_3 = 2\dot{y}_2 = 4\dot{y}_1
$$



$$
a = y_3 - y_1 = 3y_1 + C_a \implies \dot{a} = 3\dot{y}_1
$$



$$
\text{GDL} = 3 - 2 = 1
$$


Se selecciona como coordenada generalizada independiente $q = y_1$.

**Paso 2 — Posición y deformación de los resortes**


$$
\delta_K = y_1 - \ell_0
$$



$$
L_3 = (H - y_3) + (y_s - y_3) + \pi R_3 = H + y_s - 2y_3 + \pi R_3
$$



$$
y_s = 2y_3 + L_3 - H - \pi R_3
$$



$$
\ell_{K'} = H - y_s = 2H - L_3 + \pi R_3 - 2y_3
$$



$$
\ell_{K'} = 2H - L_3 + \pi R_3 - 2(4y_1 + C_3) = C_0 - 8y_1
$$



$$
\delta_{K'} = \ell_{K'} - \ell_0' = C_0 - \ell_0' - 8y_1 = C_0' - 8y_1
$$


**Paso 3 — Formulación de la energía cinética**


$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$



$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (2\dot{y}_1)^2 + \frac{1}{2} m_3 (4\dot{y}_1)^2
$$



$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (4\dot{y}_1^2) + \frac{1}{2} m_3 (16\dot{y}_1^2)
$$



$$
T = \frac{1}{2} (m_1 + 4m_2 + 16m_3) \dot{y}_1^2
$$


**Paso 4 — Formulación de la energía potencial**


$$
V_g = -m_1 g y_1 - m_2 g y_2 - m_3 g y_3
$$



$$
V_g = -m_1 g y_1 - m_2 g (2y_1 + C_1) - m_3 g (4y_1 + C_3)
$$



$$
V_g = -(m_1 + 2m_2 + 4m_3) g y_1 + \text{const}
$$



$$
V_e = \frac{1}{2} K (y_1 - \ell_0)^2 + \frac{1}{2} K' (C_0' - 8y_1)^2
$$



$$
V = -(m_1 + 2m_2 + 4m_3) g y_1 + \frac{1}{2} K (y_1 - \ell_0)^2 + \frac{1}{2} K' (C_0' - 8y_1)^2
$$


**Paso 5 — Formulación de la función Lagrangiana**


$$
L = T - V
$$



$$
L = \frac{1}{2} (m_1 + 4m_2 + 16m_3) \dot{y}_1^2 + (m_1 + 2m_2 + 4m_3) g y_1 - \frac{1}{2} K (y_1 - \ell_0)^2 - \frac{1}{2} K' (C_0' - 8y_1)^2
$$


**Paso 6 — Derivadas parciales de la Lagrangiana**


$$
\frac{\partial L}{\partial \dot{y}_1} = (m_1 + 4m_2 + 16m_3) \dot{y}_1
$$



$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_1}\right) = (m_1 + 4m_2 + 16m_3) \ddot{y}_1
$$



$$
\frac{\partial L}{\partial y_1} = (m_1 + 2m_2 + 4m_3) g - K(y_1 - \ell_0) + 8K'(C_0' - 8y_1)
$$


**Paso 7 — Obtención de la ecuación diferencial del movimiento**


$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_1}\right) - \frac{\partial L}{\partial y_1} = 0
$$



$$
(m_1 + 4m_2 + 16m_3) \ddot{y}_1 - (m_1 + 2m_2 + 4m_3) g + K(y_1 - \ell_0) - 8K'(C_0' - 8y_1) = 0
$$



$$
\therefore (m_1 + 4m_2 + 16m_3) \ddot{y}_1 + K(y_1 - \ell_0) - 8K'\delta_{K'} = (m_1 + 2m_2 + 4m_3) g
$$



$$
\boxed{(m_1 + 4m_2 + 16m_3) \ddot{y}_1 + (K + 64 K') y_1 = (m_1 + 2m_2 + 4m_3) g + K \ell_0 + 8 K' C_0'}
$$

