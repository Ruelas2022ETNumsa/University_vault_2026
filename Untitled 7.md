##### Ej. Sistema de dos cuñas con pared inclinada, resorte y fuerza externa — 1 GDL, coordenada $x_1$

**Enunciado:**
Un bloque-cuña $m_1$ descansa sobre el piso horizontal y apoya su cara izquierda sobre una pared inclinada a $60°$ respecto a la horizontal (rampa fija). Su cara derecha forma un ángulo de $45°$ con la horizontal, sobre la cual apoya el bloque-cuña $m_2$. El bloque $m_2$ tiene su cara izquierda inclinada a $45°$ (en contacto con $m_1$) y su cara derecha es vertical ($90°$), conectada a la pared derecha vertical mediante un resorte de constante $K$ y longitud natural $\ell_0$. Sobre $m_1$ actúa una fuerza externa $F$ dirigida hacia abajo. El sistema desliza sin fricción. Se define $x_1$ como el desplazamiento horizontal de $m_1$ e $y_1$ como la altura vertical de $m_2$. Hallar la ecuación de movimiento de Lagrange del sistema.

> **Nota:** GDL $= 1$, coordenada generalizada $x_1$. La ligadura geométrica por contacto en la interfaz inclinada a $60°$ entre $m_1$ y la rampa da:
> $$\tan 60° = \frac{y_1}{x_1} \implies y_1 = x_1\sqrt{3}, \qquad \dot{y}_1 = \dot{x}_1\sqrt{3}$$
> La ligadura de la interfaz a $45°$ entre $m_1$ y $m_2$ relaciona el desplazamiento horizontal de $m_2$ con $x_1$:
> $$\tan 45° = 1 \implies \dot{x}_2 = -\dot{x}_1$$
> ($m_2$ se desplaza horizontalmente en sentido opuesto a $m_1$.)

**Descripción de la figura:**
La pared izquierda está inclinada a $60°$ respecto a la horizontal (rampa fija, rayada). El bloque $m_1$ (azul oscuro, trapecio asimétrico) reposa sobre el piso horizontal con su cara izquierda apoyada contra la rampa inclinada y su cara derecha inclinada a $45°$ formando la interfaz con $m_2$. La fuerza $F$ (flecha roja) actúa hacia abajo sobre la parte superior de $m_1$. El bloque $m_2$ (azul claro, trapecio) tiene su cara izquierda inclinada a $45°$ apoyada sobre $m_1$ y su cara derecha vertical conectada mediante el resorte $K$ a la pared derecha vertical. La pared derecha es vertical ($90°$). El resorte $K$ actúa horizontalmente entre $m_2$ y la pared derecha.

---


---

**Paso 1 — Ligadura geométrica y GDL**

La pared izquierda inclinada a $60°$ impone que el desplazamiento vertical de $m_1$ queda ligado a su desplazamiento horizontal $x_1$. La interfaz a $45°$ entre $m_1$ y $m_2$ impone que $m_2$ se desplaza horizontalmente cuando $m_1$ se mueve. Con estas dos ligaduras el sistema tiene $\text{GDL} = 1$, coordenada generalizada $x_1$.

Ligadura de la rampa (60°):

$$\tan 60° = \sqrt{3} = \frac{y_1}{x_1} \implies y_1 = x_1\sqrt{3}, \qquad \dot{y}_1 = \dot{x}_1\sqrt{3}$$

Ligadura de la interfaz (45°) — cuando $m_1$ avanza $\Delta x_1$, la altura de la interfaz sube $\Delta x_1 \cdot \tan 45° = \Delta x_1$, empujando a $m_2$ horizontalmente:

$$\dot{x}_2 = -\dot{x}_1 \qquad (m_2 \text{ se aleja de } m_1)$$

**Paso 2 — Energía cinética**

$m_1$ tiene velocidades $\dot{x}_1$ (horizontal) e $\dot{y}_1$ (vertical, impuesta por la rampa). $m_2$ solo tiene velocidad horizontal $\dot{x}_2$:

$$T = \frac{1}{2}m_1(\dot{x}_1^2 + \dot{y}_1^2) + \frac{1}{2}m_2\dot{x}_2^2$$

Sustituyendo las ligaduras:

$$T = \frac{1}{2}m_1(\dot{x}_1^2 + 3\dot{x}_1^2) + \frac{1}{2}m_2\dot{x}_1^2 = \frac{1}{2}(4m_1 + m_2)\dot{x}_1^2$$

$$\boxed{T = \frac{1}{2}(4m_1 + m_2)\dot{x}_1^2}$$

**Paso 3 — Energía potencial**

$m_1$ sube verticalmente con $y_1 = x_1\sqrt{3}$. $m_2$ solo se desplaza horizontalmente, sin cambio de altura, por lo que no contribuye a $V_g$. El resorte $K$ se deforma con el desplazamiento horizontal de $m_2$:

$$V_g = m_1 g y_1 = m_1 g x_1\sqrt{3}$$

$$V_K = \frac{1}{2}K(x_2 - \ell_0)^2 = \frac{1}{2}K(x_1 - \ell_0)^2 \qquad (\text{usando } x_2 = x_1 + C)$$

$$\boxed{V = m_1 g x_1\sqrt{3} + \frac{1}{2}K(x_1 - \ell_0)^2}$$

**Paso 4 — Fuerza generalizada de $F$**

$F$ actúa verticalmente sobre $m_1$, que tiene desplazamiento vertical $y_1 = x_1\sqrt{3}$:

$$Q_{x_1}^F = F\frac{\partial y_1}{\partial x_1} = F\sqrt{3}$$

**Paso 5 — Ecuación de Lagrange para $x_1$**

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) = (4m_1 + m_2)\ddot{x}_1$$

$$\frac{\partial V}{\partial x_1} = m_1 g\sqrt{3} + K(x_1 - \ell_0)$$

$$\boxed{(4m_1 + m_2)\ddot{x}_1 + K(x_1 - \ell_0) + m_1 g\sqrt{3} = F\sqrt{3}}$$

---

noteboolm:

##### Ej. Un bloque-cuña $m_1$ descansa sobre el piso horizontal y apoya su cara izquierda sobre una pared inclinada a $60^\circ$ respecto a la horizontal (rampa fija). Su cara derecha forma un ángulo de $45^\circ$ con la horizontal, sobre la cual apoya el bloque-cuña $m_2$. El bloque $m_2$ tiene su cara izquierda inclinada a $45^\circ$ (en contacto con $m_1$) y su cara derecha es vertical ($90^\circ$), conectada a la pared derecha vertical mediante un resorte de constante $K$ y longitud natural $\ell_0$. Sobre $m_1$ actúa una fuerza externa $F$ dirigida hacia abajo. El sistema desliza sin fricción. Se define $x_1$ como el desplazamiento horizontal de $m_1$ e $y_1$ como la altura vertical de $m_2$. Hallar la ecuación de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Rampa fija a 60°
    \fill[pattern=north east lines] (-0.5,0) -- (1.5,2.598) -- (1.0,2.598) -- (-0.5,0) -- cycle;
    \draw[thick] (-0.5,0) -- (1.5,2.598);

    % Piso horizontal
    \fill[pattern=north east lines] (-0.5,-0.3) rectangle (7.0,0);
    \draw[thick] (-0.5,0) -- (7.0,0);

    % Pared derecha vertical
    \fill[pattern=north east lines] (7.0,0) rectangle (7.3,3.0);
    \draw[thick] (7.0,0) -- (7.0,3.0);

    % Bloque m1 (trapecio: cara izq a 60°, cara der a 45°)
    \draw[fill=teal!10, draw=maincolor, thick] (1.0,1.732) -- (2.0,0) -- (4.5,0) -- (3.0,1.732) -- cycle;
    \node[maincolor] at (2.6,0.6) {$m_1$};

    % Bloque m2 (cara izq a 45°, cara der vertical)
    \draw[fill=orange!10, draw=accentcolor, thick] (3.0,1.732) -- (4.5,0.232) -- (5.5,0.232) -- (5.5,1.732) -- cycle;
    \node[accentcolor] at (4.6,1.1) {$m_2$};

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (5.5,0.982) -- (7.0,0.982);
    \node[above, accentcolor] at (6.25,1.15) {$K$};

    % Fuerza F externa sobre m1 (flecha roja)
    \draw[->, red, ultra thick] (2.5,2.3) -- (2.5,1.732) node[midway, right] {$F$};

    % Coordenada x1
    \draw[->, maincolor, thick] (0,-0.6) -- (2.0,-0.6) node[midway, below] {$x_1$};
    \draw[dotted] (2.0,0) -- (2.0,-0.8);

    % Coordenada y1
    \draw[->, accentcolor, thick] (-0.8,0) -- (-0.8,1.732) node[midway, left] {$y_1$};
    \draw[dotted] (3.0,1.732) -- (-1.0,1.732);
    \draw[dotted] (-0.5,0) -- (-1.0,0);

    % Ángulos 60° y 45°
    \draw[thick, maincolor] (0,0) ++(0.5,0) arc (0:60:0.5);
    \node[maincolor] at (0.7,0.3) {$60^\circ$};

    \draw[thick, accentcolor] (4.5,0) ++(-0.4,0) arc (180:135:0.4);
    \node[accentcolor] at (3.9,0.25) {$45^\circ$};

\end{tikzpicture}
\end{document}
```

**Resolución**
Se formulan las ligaduras cinemáticas, se construyen las energías cinética y potencial del sistema en función de $x_1$ y se obtiene la ecuación diferencial mediante Euler-Lagrange.

**Paso 1 — Velocidades del sistema en función de $\dot{x}_1$**


$$
y_1 = x_1\sqrt{3} \implies \dot{y}_1 = \dot{x}_1\sqrt{3}
$$



$$
\dot{x}_2 = -\dot{x}_1
$$



$$
v_1^2 = \dot{x}_1^2 + \dot{y}_1^2 = \dot{x}_1^2 + 3\dot{x}_1^2 = 4\dot{x}_1^2
$$



$$
v_2^2 = \dot{x}_2^2 + \dot{y}_1^2 = (-\dot{x}_1)^2 + 3\dot{x}_1^2 = 4\dot{x}_1^2
$$


**Paso 2 — Energía cinética del sistema**


$$
T = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2
$$



$$
T = \frac{1}{2}m_1 (4\dot{x}_1^2) + \frac{1}{2}m_2 (4\dot{x}_1^2)
$$



$$
T = 2(m_1 + m_2)\dot{x}_1^2
$$


**Paso 3 — Energía potencial del sistema**


$$
V = m_1 g y_1 + m_2 g y_1 + F y_1 + \frac{1}{2}K(x_1 - \ell_0)^2
$$



$$
V = (m_1 + m_2)g \sqrt{3} x_1 + F \sqrt{3} x_1 + \frac{1}{2}K(x_1 - \ell_0)^2
$$


**Paso 4 — Función Lagrangiana**


$$
L = T - V
$$



$$
L = 2(m_1 + m_2)\dot{x}_1^2 - [(m_1 + m_2)g + F]\sqrt{3} x_1 - \frac{1}{2}K(x_1 - \ell_0)^2
$$


**Paso 5 — Ecuación de Euler-Lagrange para $x_1$**


$$
\frac{\partial L}{\partial \dot{x}_1} = 4(m_1 + m_2)\dot{x}_1 \implies \frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}_1}\right) = 4(m_1 + m_2)\ddot{x}_1
$$



$$
\frac{\partial L}{\partial x_1} = -[(m_1 + m_2)g + F]\sqrt{3} - K(x_1 - \ell_0)
$$



$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}_1}\right) - \frac{\partial L}{\partial x_1} = 0
$$



$$
\boxed{4(m_1 + m_2)\ddot{x}_1 + K(x_1 - \ell_0) + [(m_1 + m_2)g + F]\sqrt{3} = 0}
$$

