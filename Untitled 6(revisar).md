Dos poleas sin inercia rotacional $m_1$ y $m_2$ forman un sistema vertical en cadena con dos resortes y una fuerza aplicada. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$ conectado a su centro; su ramal izquierdo sostiene a la polea $m_2$ por el centro mediante un cable, y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La polea $m_2$ cuelga del ramal izquierdo de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene un punto de aplicación de fuerza $F$ mediante un cable. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, el centro de $m_2$ y el punto de aplicación de $F$ respectivamente. La distancia $a$ se mide desde el centro de $m_2$ hacia abajo hasta el punto de aplicación de $F$.

Hallar las ecuaciones de movimiento de Lagrange del sistema usando las coordenadas generalizadas $(y_1, a)$.

> **Nota:** Las coordenadas $(y_3, a)$ no son resolubles directamente porque $y_3$ no puede expresarse de forma independiente. Se eligen $(y_1, a)$ como coordenadas generalizadas ($N = 3 - 1 = 2$ GDL, dado que el cable inextensible impone una ligadura). Las ligaduras cinemáticas del sistema de poleas dan:
> $$y_2 = y_1 - \tfrac{1}{2}a \implies \dot{y}_2 = \dot{y}_1 - \tfrac{1}{2}\dot{a}$$
> $$y_3 = y_2 + a = y_1 + \tfrac{1}{2}a \implies \dot{y}_3 = \dot{y}_1 + \tfrac{1}{2}\dot{a}$$

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
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.2,7.3) -- (1.2,6.0);
    \node[left, maincolor] at (0.95,6.65) {$K$};

    % Polea m1 (teal)
    \draw[thick, fill=teal!10, draw=maincolor] (1.2,5.7) circle (0.3);
    \fill[maincolor] (1.2,5.7) circle (0.05);
    \node[left, maincolor] at (0.7,5.7) {$m_1$};

    % Ramal izquierdo de m1 — cable baja a m2
    \draw[thick, maincolor] (0.9,5.7) -- (0.9,3.4);

    % Ramal derecho de m1 — cable baja a resorte K'
    \draw[thick, maincolor] (1.5,5.7) -- (1.5,2.0);

    % Resorte K' — cable de m1 al piso
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, maincolor, thick] (1.5,2.0) -- (1.5,0);
    \node[right, maincolor] at (1.7,1.0) {$K'$};

    % Polea m2 (accentcolor)
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (0.9,3.4) circle (0.3);
    \fill[accentcolor] (0.9,3.4) circle (0.05);
    \node[left, accentcolor] at (0.4,3.4) {$m_2$};

    % Ramal izquierdo de m2 — cable fijo al piso
    \draw[thick, accentcolor] (0.6,3.4) -- (0.6,0);

    % Ramal derecho de m2 — cable desciende a la fuerza F
    \draw[thick, accentcolor] (1.2,3.4) -- (1.2,1.2);
    \draw[->, accentcolor, ultra thick] (1.2,1.2) -- (1.2,0.4) node[right, accentcolor] {$F$};
    \fill[accentcolor] (1.2,1.2) circle (0.06);

    % Cota H — altura total
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,7.3) node[midway, left] {$H$};

    % Coordenada y1 — techo a m1
    \draw[->, maincolor, thick] (2.8,7.3) -- (2.8,5.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.2,7.3) -- (2.9,7.3);
    \draw[dotted] (1.2,5.7) -- (2.9,5.7);

    % Coordenada y2 — techo a m2
    \draw[->, accentcolor, thick] (3.5,7.3) -- (3.5,3.4) node[midway, right] {$y_2$};
    \draw[dotted] (0.9,3.4) -- (3.6,3.4);

    % Coordenada y3 — techo al punto F
    \draw[->, accentcolor, thick] (4.2,7.3) -- (4.2,1.2) node[midway, right] {$y_3$};
    \draw[dotted] (1.2,1.2) -- (4.3,1.2);

    % Cota a — m2 al punto F
    \draw[<->, accentcolor, thick] (2.1,3.4) -- (2.1,1.2) node[midway, right] {$a$};
    \draw[dotted] (0.9,3.4) -- (2.2,3.4);
    \draw[dotted] (1.2,1.2) -- (2.2,1.2);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** El resorte $K$ (teal) conecta el techo con el centro de la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable hasta el centro de la polea $m_2$ (naranja). Del ramal derecho de $m_1$ desciende un cable que conecta con el resorte $K'$ (teal) anclado al piso. Del ramal izquierdo de $m_2$ desciende un cable fijo al piso. Del ramal derecho de $m_2$ desciende un cable hasta el punto de aplicación de la fuerza $F$ (naranja, flecha hacia abajo). Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, el centro de $m_2$ y el punto de $F$ respectivamente. La cota $a$ va desde el centro de $m_2$ hasta el punto de $F$. La cota $H$ es la altura total techo–piso (rojo).

---

**Paso 1 — Energía cinética**

Cada masa contribuye con su energía cinética traslacional. Se sustituye $\dot{y}_2$ usando la ligadura:

$$T = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\!\left(\dot{y}_1 - \frac{1}{2}\dot{a}\right)^{\!2}$$

Expandiendo:

$$\boxed{T = \frac{1}{2}(m_1 + m_2)\dot{y}_1^2 - \frac{1}{2}m_2\dot{y}_1\dot{a} + \frac{1}{8}m_2\dot{a}^2}$$

**Paso 2 — Energía potencial**

Se define $\ell_K = y_1 - \ell_0$ como la deformación del resorte $K$. Para $K'$, su extremo superior está en el ramal derecho de $m_1$, cuya posición se obtiene de la ligadura de la polea $m_1$: si el ramal izquierdo baja $y_2$ y el ramal derecho sube simétricamente, la longitud del resorte $K'$ es $H - y_1 - \frac{1}{2}a + C$ donde $C$ agrupa las longitudes fijas de cable. Definiendo la deformación natural de $K'$ en términos de posición:

$$V_K = \frac{1}{2}K(y_1 - \ell_0)^2$$

$$V_{K'} = \frac{1}{2}K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right)^{\!2}$$

La energía potencial gravitatoria (positiva hacia abajo, coordenadas desde el techo):

$$V_g = -m_1 g y_1 - m_2 g y_2 = -m_1 g y_1 - m_2 g\!\left(y_1 - \frac{1}{2}a\right) = -(m_1+m_2)g y_1 + \frac{1}{2}m_2 g a$$

$$\boxed{V = \frac{1}{2}K(y_1-\ell_0)^2 + \frac{1}{2}K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right)^{\!2} - (m_1+m_2)g y_1 + \frac{1}{2}m_2 g a}$$

**Paso 3 — Fuerzas generalizadas**

La fuerza $F$ actúa sobre el punto $y_3 = y_1 + \frac{1}{2}a$. El trabajo virtual:

$$\delta W = F\,\delta y_3 = F\,\delta y_1 + \frac{1}{2}F\,\delta a$$

$$Q_{y_1} = F \qquad Q_a = \frac{1}{2}F$$

**Paso 4 — Ecuación de Lagrange para $y_1$**

$$\frac{\partial T}{\partial \dot{y}_1} = (m_1+m_2)\dot{y}_1 - \frac{1}{2}m_2\dot{a} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_1}\right) = (m_1+m_2)\ddot{y}_1 - \frac{1}{2}m_2\ddot{a}$$

$$\frac{\partial V}{\partial y_1} = K(y_1-\ell_0) - K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right) - (m_1+m_2)g$$

$$\boxed{(m_1+m_2)\ddot{y}_1 - \frac{1}{2}m_2\ddot{a} + K(y_1-\ell_0) - K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right) - (m_1+m_2)g = F}$$

**Paso 5 — Ecuación de Lagrange para $a$**

$$\frac{\partial T}{\partial \dot{a}} = -\frac{1}{2}m_2\dot{y}_1 + \frac{1}{4}m_2\dot{a} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{a}}\right) = -\frac{1}{2}m_2\ddot{y}_1 + \frac{1}{4}m_2\ddot{a}$$

$$\frac{\partial V}{\partial a} = K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right) + \frac{1}{2}m_2 g$$

$$\boxed{-\frac{1}{2}m_2\ddot{y}_1 + \frac{1}{4}m_2\ddot{a} - K'\!\left(H - \ell + \pi R_2 + a - y_1 - \ell_0'\right) - \frac{1}{2}m_2 g = \frac{1}{2}F}$$
