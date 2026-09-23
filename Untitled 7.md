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

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{blue!70!black}
    \colorlet{accentcolor}{cyan!70!black}

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (8.0,0);
    \draw[thick] (0,0) -- (8.0,0);

    % Pared izquierda inclinada 60 grados (rampa)
    \fill[pattern=north east lines] (-0.25,0) -- (0,0) -- (1.732,3.0) -- (1.482,3.0) -- cycle;
    \draw[thick] (0,0) -- (1.732,3.0);

    % Pared derecha vertical
    \fill[pattern=north east lines] (7.8,0) rectangle (8.1,3.5);
    \draw[thick] (7.8,0) -- (7.8,3.5);

    % Angulo 60 en la rampa
    \draw[thick, red] (0.6,0) arc (0:60:0.6);
    \node[red] at (0.85,0.28) {\small $60°$};
    \node[red] at (-0.2,-0.35) {\small $d=60$};

    % Bloque m1 (azul oscuro, trapecio)
    % cara izq apoyada en rampa (60°), cara der a 45°
    % base inferior sobre el piso: de x=1.732 a x=4.5
    % cara izquierda sube 60° desde (1.732,0) -> (1.732+1.0, 1.732) ~ sigue la rampa
    % cara superior horizontal
    % cara derecha baja 45° desde esquina superior derecha
    \draw[fill=blue!10, draw=maincolor, thick]
        (1.732,0) -- (4.5,0) -- (4.5,1.5) -- (3.0,3.0) -- (1.732,3.0) -- cycle;
    \node[maincolor, font=\large] at (3.0,1.4) {$1$};

    % Angulo 45 en cara derecha de m1
    \draw[thick, maincolor] (4.5,1.5) ++(-0.4,0) arc (180:135:0.4);
    \node[maincolor] at (4.0,1.75) {\small $45°$};

    % Fuerza F sobre m1
    \draw[->, red, ultra thick] (2.8,3.8) -- (2.8,3.0) node[midway, right] {$F$};

    % Bloque m2 (cyan, cara izq a 45°, cara der vertical)
    % cara izq inclinada 45° contacto con m1
    % cara der vertical pegada al resorte
    \draw[fill=cyan!10, draw=accentcolor, thick]
        (4.5,1.5) -- (4.5,3.0) -- (7.0,3.0) -- (7.0,1.5) -- cycle;
    \node[accentcolor, font=\large] at (5.9,2.25) {$2$};

    % Resorte K entre m2 y pared derecha
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (7.0,2.25) -- (7.8,2.25);
    \node[above, accentcolor] at (7.4,2.45) {$K$};

    % Coordenada x1 (horizontal de m1)
    \draw[->, maincolor, thick] (1.732,-0.6) -- (4.5,-0.6) node[midway, below] {$x_1$};
    \draw[dotted] (1.732,0) -- (1.732,-0.8);
    \draw[dotted] (4.5,0) -- (4.5,-0.8);

    % Coordenada y1 (vertical de m2 / altura de interfaz)
    \draw[->, accentcolor, thick] (8.4,0) -- (8.4,1.5) node[midway, right] {$y_1$};
    \draw[dotted] (7.8,0) -- (8.6,0);
    \draw[dotted] (7.8,1.5) -- (8.6,1.5);

\end{tikzpicture}
\end{document}
```

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
