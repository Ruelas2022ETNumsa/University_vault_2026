Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$ a una distancia $a$ por debajo de ella; está conectada al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$ unido a su centro, y su ramal derecho sostiene a la masa puntual $m_3$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

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

    % Resorte K' — centro de m2 al piso
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.3,3.1) -- (1.3,0);
    \node[left, accentcolor] at (1.1,1.5) {$K'$};

    % Ramal izquierdo de m2 — libre
    \draw[thick, accentcolor] (1.0,3.4) -- (1.0,0);

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

> **Descripción de la figura:** El resorte $K$ (teal) conecta el techo con la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable fijo al piso. Del ramal derecho de $m_1$ desciende un cable hasta la polea $m_2$ (naranja), separada de $m_1$ por la distancia $a$. Del centro de $m_2$ desciende el resorte $K'$ (naranja) conectado al piso. Del ramal derecho de $m_2$ cuelga la masa puntual $m_3$ (naranja). Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo. La cota $H$ es la altura total techo–piso (rojo).

---

##### Ej. Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$ a una distancia $a$ por debajo de ella; está conectada al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$ unido a su centro, y su ramal derecho sostiene a la masa puntual $m_3$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente. Hallar las ecuaciones de movimiento de Lagrange del sistema.

**Resolución**
Se identifican las ligaduras cinemáticas, se formula el Lagrangiano en función de la coordenada generalizada $y_2$, y se aplica la ecuación de Euler-Lagrange.

**Paso 1 — Ligaduras cinemáticas y coordenada generalizada** *(conservación de longitud de cable en cada polea)*

$$
L_1 = (H - y_1) + \pi R_1 + (y_2 - y_1) = \text{cte} \implies \dot{y}_1 = \dfrac{\dot{y}_2}{2}
$$

$$
L_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = \text{cte} \implies \dot{y}_3 = 2\dot{y}_2
$$

> Coordenada generalizada: $q = y_2$ \quad (1 GDL)

**Paso 2 — Energía cinética efectiva** *(sustitución de ligaduras en $T$)*

$$
T = \dfrac{1}{2}m_1\!\left(\dfrac{\dot{y}_2}{2}\right)^{\!2} + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\left(2\dot{y}_2\right)^{\!2}
$$

$$
\boxed{T = \dfrac{1}{2}\!\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2^2}
$$

**Paso 3 — Energía potencial** *(gravedad + resorte $K$ en $m_1$ + resorte $K'$ al centro de $m_2$)*

La deformación de $K$ es $y_1 - \ell_0 = y_2/2 - \ell_0$. La deformación de $K'$ es $y_2 - \ell_0'$ (distancia del techo al centro de $m_2$ menos longitud natural). Sustituyendo $y_1 = y_2/2$ e $y_3 = 2y_2$:

$$
\boxed{V = \dfrac{1}{2}K\!\left(\dfrac{y_2}{2} - \ell_0\right)^{\!2} + \dfrac{1}{2}K'(y_2 - \ell_0')^2 - \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g\,y_2}
$$

**Paso 4 — Euler-Lagrange → EDO de movimiento** *($\partial y_1/\partial y_2 = 1/2$, $\partial y_3/\partial y_2 = 2$, de las ligaduras del Paso 1)*

$$
\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) = \left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2
$$

$$
\dfrac{\partial L}{\partial y_2} = -\dfrac{K}{2}\!\left(\dfrac{y_2}{2} - \ell_0\right) - K'(y_2 - \ell_0') + \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g
$$

$$
\boxed{\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2 + \left(\dfrac{K}{4} + K'\right)y_2 = \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g + \dfrac{K\,\ell_0}{2} + K'\ell_0'}
$$
