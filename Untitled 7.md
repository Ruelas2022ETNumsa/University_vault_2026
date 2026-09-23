##### Ej. Sistema de dos cuñas con pared inclinada, resorte y fuerza externa — 1 GDL, coordenada $x_2$

**Enunciado:**
Dos bloques-cuña $m_1$ y $m_2$ se encuentran sobre un piso horizontal liso. La pared izquierda es una rampa fija inclinada a $60°$ respecto a la horizontal. El bloque $m_1$ (trapecio) queda suspendido entre la rampa izquierda y el bloque $m_2$: su cara izquierda apoya contra la rampa a $60°$ y su cara inferior-derecha forma la interfaz inclinada a $45°$ con la cara izquierda de $m_2$. El bloque $m_2$ tiene su cara izquierda inclinada a $45°$ (en contacto con $m_1$), cara superior horizontal y cara derecha vertical, conectada mediante un resorte de constante $K$ a la pared derecha fija. Sobre $m_1$ actúa una fuerza externa $F$ dirigida hacia abajo. El sistema desliza sin fricción. Se definen: $x_1$ como el desplazamiento horizontal de $m_1$ desde la rampa, $x_2$ como el desplazamiento horizontal de $m_2$, $y_1$ como la altura de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto sobre el piso, $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = x_2 - x_1$ la separación horizontal entre ambos bloques. Hallar la ecuación de movimiento de Lagrange del sistema.

**Descripción de la figura:**
La pared izquierda es una rampa fija inclinada a $60°$ respecto a la horizontal (rayada). El bloque $m_1$ (trapecio) flota apoyado entre la rampa y $m_2$: su cara izquierda toca la rampa a $60°$ y su cara derecha forma la interfaz a $45°$ con $m_2$. La fuerza $F$ actúa verticalmente hacia abajo sobre $m_1$. El bloque $m_2$ (trapecio) tiene cara izquierda a $45°$ en contacto con $m_1$, cara superior horizontal y cara derecha vertical conectada al resorte $K$, que actúa horizontalmente hasta la pared derecha fija (rayada). Las cotas indican: $y_1$ (altura de $m_1$ sobre el piso), $y_2$ (altura del punto de contacto), $x_1$ (desplazamiento horizontal de $m_1$), $x_2$ (desplazamiento horizontal de $m_2$), $B_1$ (ancho de $m_1$), $B_2$ (ancho de $m_2$) y $d$ (diferencia $x_2 - x_1$).

---

##### Ej. Dos bloques-cuña $m_1$ y $m_2$ se encuentran sobre un piso horizontal liso. La pared izquierda es una rampa fija inclinada a $60°$ respecto a la horizontal. El bloque $m_1$ (trapecio) queda suspendido entre la rampa izquierda y el bloque $m_2$: su cara izquierda apoya contra la rampa a $60°$ y su cara inferior-derecha forma la interfaz inclinada a $45°$ con la cara izquierda de $m_2$. El bloque $m_2$ tiene su cara izquierda inclinada a $45°$ (en contacto con $m_1$), cara superior horizontal y cara derecha vertical, conectada mediante un resorte de constante $K$ a la pared derecha fija. Sobre $m_1$ actúa una fuerza externa $F$ dirigida hacia abajo. El sistema desliza sin fricción. Se definen: $x_1$ como el desplazamiento horizontal de $m_1$ desde la rampa, $x_2$ como el desplazamiento horizontal de $m_2$, $y_1$ como la altura de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto sobre el piso, $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = x_2 - x_1$ la separación horizontal entre ambos bloques. Hallar la ecuación de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Rampa izquierda a 60°
    \draw[thick] (0,4.5) -- (2.02,1.0);
    \fill[pattern=north east lines] (0,4.5) -- (2.02,1.0) -- (1.6,1.0) -- (-0.4,4.5) -- cycle;

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (7.5,0);
    \draw[thick] (0,0) -- (7.5,0);

    % Pared derecha fija
    \fill[pattern=north east lines] (7.5,0) rectangle (7.8,3.5);
    \draw[thick] (7.5,0) -- (7.5,3.5);

    % Bloque m1 (trapecio)
    \draw[fill=teal!10, draw=maincolor, thick] (1.155,2.5) -- (2.5,2.5) -- (3.5,1.155) -- (1.732,1.155) -- cycle;
    \node[maincolor] at (2.2,1.85) {$m_1$};

    % Fuerza F actuando hacia abajo sobre m1
    \draw[->, red, ultra thick] (2.2,3.1) -- (2.2,2.5) node[above=6pt, red] {$F$};

    % Bloque m2 (trapecio)
    \draw[fill=orange!10, draw=accentcolor, thick] (2.345,0) -- (5.5,0) -- (5.5,1.5) -- (3.845,1.5) -- cycle;
    \node[accentcolor] at (4.3,0.75) {$m_2$};

    % Resorte K conectado a m2
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (5.5,0.75) -- (7.5,0.75);
    \node[above, accentcolor] at (6.5,0.95) {$K$};

    % Ángulos
    \draw[thick, gray] (2.02,1.0) ++(-0.5,0) arc (180:120:0.5);
    \node[gray] at (1.3,1.3) {$60^\circ$};

    \draw[thick, accentcolor] (2.345,0) ++(0.6,0) arc (0:45:0.6);
    \node[accentcolor] at (3.2,0.25) {$45^\circ$};

    % Coordenada x1
    \draw[->, maincolor, thick] (0,-0.6) -- (1.732,-0.6) node[midway, below] {$x_1$};
    \draw[dotted] (0,0) -- (0,-0.8);
    \draw[dotted] (1.732,1.155) -- (1.732,-0.8);

    % Coordenada x2
    \draw[->, accentcolor, thick] (0,-1.2) -- (2.345,-1.2) node[midway, below] {$x_2$};
    \draw[dotted] (2.345,0) -- (2.345,-1.4);

    % Cota d = x2 - x1
    \draw[<->, black, thick] (1.732,-0.6) -- (2.345,-0.6) node[midway, above] {$d$};

    % Coordenada y1 (altura de m1)
    \draw[->, maincolor, thick] (-0.6,0) -- (-0.6,1.85) node[midway, left] {$y_1$};
    \draw[dotted] (0,0) -- (-0.8,0);
    \draw[dotted] (2.2,1.85) -- (-0.8,1.85);

    % Coordenada y2 (altura de punto de contacto)
    \draw[->, accentcolor, thick] (-1.2,0) -- (-1.2,1.155) node[midway, left] {$y_2$};
    \draw[dotted] (1.732,1.155) -- (-1.4,1.155);

\end{tikzpicture}
\end{document}
```

**Resolución**
Se identifican las ligaduras cinemáticas del sistema de $1\text{ GDL}$, se formulan las expresiones de energía cinética y potencial en función de la coordenada generalizada $x_1$, y se aplica la ecuación de Euler-Lagrange.

**Paso 1 — Relación de ligaduras cinemáticas entre coordenadas**

$$
y_1 = x_1 \tan 60^\circ = \sqrt{3} x_1 \implies \dot{y}_1 = \sqrt{3} \dot{x}_1
$$


$$
y_1 = d \tan 45^\circ = x_2 - x_1 \implies x_2 = (1 + \sqrt{3}) x_1 \implies \dot{x}_2 = (1 + \sqrt{3}) \dot{x}_1
$$


$$
y_2 = \sqrt{3} x_1
$$


**Paso 2 — Energía cinética del sistema**

$$
T_1 = \frac{1}{2} m_1 (\dot{x}_1^2 + \dot{y}_1^2) = \frac{1}{2} m_1 (\dot{x}_1^2 + 3 \dot{x}_1^2) = 2 m_1 \dot{x}_1^2
$$


$$
T_2 = \frac{1}{2} m_2 \dot{x}_2^2 = \frac{1}{2} m_2 (1 + \sqrt{3})^2 \dot{x}_1^2 = (2 + \sqrt{3}) m_2 \dot{x}_1^2
$$


$$
\boxed{T = \frac{1}{2} \left[ 4 m_1 + 2(2 + \sqrt{3}) m_2 \right] \dot{x}_1^2}
$$


**Paso 3 — Energía potencial del sistema**

$$
V_g = m_1 g y_1 = \sqrt{3} m_1 g x_1
$$


$$
V_F = F y_1 = \sqrt{3} F x_1
$$


$$
V_K = \frac{1}{2} K (x_2 - \ell_0)^2 = \frac{1}{2} K \left( (1 + \sqrt{3}) x_1 - \ell_0 \right)^2
$$


$$
\boxed{V = \sqrt{3}(m_1 g + F) x_1 + \frac{1}{2} K \left( (1 + \sqrt{3}) x_1 - \ell_0 \right)^2}
$$


**Paso 4 — Función Lagrangiana**

$$
L = T - V
$$


$$
\boxed{L = \frac{1}{2} \left[ 4 m_1 + 2(2 + \sqrt{3}) m_2 \right] \dot{x}_1^2 - \sqrt{3}(m_1 g + F) x_1 - \frac{1}{2} K \left( (1 + \sqrt{3}) x_1 - \ell_0 \right)^2}
$$


**Paso 5 — Ecuación de Euler-Lagrange → EDO de movimiento**

$$
\frac{\partial L}{\partial \dot{x}_1} = \left[ 4 m_1 + 2(2 + \sqrt{3}) m_2 \right] \dot{x}_1 \implies \frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}_1}\right) = \left[ 4 m_1 + (4 + 2\sqrt{3}) m_2 \right] \ddot{x}_1
$$


$$
\frac{\partial L}{\partial x_1} = -\sqrt{3}(m_1 g + F) - K (1 + \sqrt{3}) \left( (1 + \sqrt{3}) x_1 - \ell_0 \right)
$$


$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}_1}\right) - \frac{\partial L}{\partial x_1} = 0
$$


$$
\boxed{\left[ 4 m_1 + (4 + 2\sqrt{3}) m_2 \right] \ddot{x}_1 + (4 + 2\sqrt{3}) K x_1 = (1 + \sqrt{3}) K \ell_0 - \sqrt{3}(m_1 g + F)}
$$

