Dos poleas sin inercia rotacional $m_1$ y $m_2$ forman un sistema vertical en cadena con dos resortes y una fuerza aplicada. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$ conectado a su centro; su ramal izquierdo sostiene a la polea $m_2$ por el centro mediante un cable, y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La polea $m_2$ cuelga del ramal izquierdo de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene un punto de aplicación de fuerza $F$ mediante un cable. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, el centro de $m_2$ y el punto de aplicación de $F$ respectivamente. La distancia $a$ se mide desde el centro de $m_2$ hacia abajo hasta el punto de aplicación de $F$.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

> **Nota del docente:** Usar coordenadas generalizadas $(y_2, a)$. Las ligaduras cinemáticas dan:
> $$\dot{y}_3 = \dot{y}_2 + \dot{a}$$
> $$\dot{y}_1 = \dot{y}_2 + \tfrac{1}{2}\dot{a}$$

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
**Resolución**
Se emplean las coordenadas generalizadas $(y_2, a)$ indicadas para expresar las relaciones de ligadura cinemática, formular la energía cinética, la energía potencial y el trabajo virtual, y derivar las ecuaciones de Lagrange del sistema.

---

**Paso 1 — Relaciones cinemáticas y coordenadas generalizadas**

$$
\text{A partir de la cota } a = y_3 - y_2 \implies y_3 = y_2 + a \implies \dot{y}_3 = \dot{y}_2 + \dot{a}
$$
$$
\text{Según la ligadura del cable de la polea } m_1: \quad y_1 = y_2 + \frac{1}{2}a + C_1 \implies \dot{y}_1 = \dot{y}_2 + \frac{1}{2}\dot{a}
$$

$$
\text{La posición del extremo superior del resorte } K' \text{ resulta } y_{s'} = y_2 + a + C_1'
$$

$$
\text{Las coordenadas generalizadas seleccionadas son } (q_1, q_2) = (y_2, a)
$$

> **Nota:** $C_1$ y $C_1'$ son constantes que agrupan las longitudes fijas de cable y los términos $\pi R$ de cada polea (longitud de arco de contacto). No dependen del tiempo y se absorben en las condiciones iniciales.


**Paso 2 — Energía cinética del sistema**

$$
T = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\dot{y}_2^2
$$

$$
T = \frac{1}{2}m_1\left(\dot{y}_2 + \frac{1}{2}\dot{a}\right)^{\!2} + \frac{1}{2}m_2\dot{y}_2^2
$$

$$
\boxed{T = \frac{1}{2}(m_1 + m_2)\dot{y}_2^2 + \frac{1}{2}m_1\dot{y}_2\dot{a} + \frac{1}{8}m_1\dot{a}^2}
$$

**Paso 3 — Energía potencial total y fuerzas generalizadas**
$$
V_g = -m_1 g y_1 - m_2 g y_2 = -(m_1 + m_2)g y_2 - \frac{1}{2}m_1 g a - m_1 g C_1
$$

$$
V_K = \frac{1}{2}K\left(y_2 + \frac{1}{2}a + C_1 - \ell_0\right)^{\!2}
$$
$$
V_{K'} = \frac{1}{2}K'\left(H - y_2 - a - C_1' - \ell_0'\right)^{\!2}
$$

$$
\boxed{V = -(m_1 + m_2)g y_2 - \frac{1}{2}m_1 g a + \frac{1}{2}K\left(y_2 + \frac{1}{2}a + C_1 - \ell_0\right)^{\!2} + \frac{1}{2}K'\left(H - y_2 - a - C_1' - \ell_0'\right)^{\!2}}
$$

$$
\delta W = F \, \delta y_3 = F \, \delta y_2 + F \, \delta a \implies Q_{y_2} = F, \quad Q_a = F
$$

**Paso 4 — Función Lagrangiana del sistema**

$$
L = T - V
$$

$$
\boxed{L = \frac{1}{2}(m_1 + m_2)\dot{y}_2^2 + \frac{1}{2}m_1\dot{y}_2\dot{a} + \frac{1}{8}m_1\dot{a}^2 + (m_1 + m_2)g y_2 + \frac{1}{2}m_1 g a - \frac{1}{2}K\left(y_2 + \frac{1}{2}a + C_1 - \ell_0\right)^{\!2} - \frac{1}{2}K'\left(H - y_2 - a - C_1' - \ell_0'\right)^{\!2}}
$$

**Paso 5 — Ecuación diferencial para la coordenada $y_2$**

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_2}\right) - \frac{\partial L}{\partial y_2} = Q_{y_2}
$$

$$
\frac{\partial L}{\partial \dot{y}_2} = (m_1 + m_2)\dot{y}_2 + \frac{1}{2}m_1\dot{a} \implies \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_2}\right) = (m_1 + m_2)\ddot{y}_2 + \frac{1}{2}m_1\ddot{a}
$$

$$
\frac{\partial L}{\partial y_2} = (m_1 + m_2)g - K\left(y_2 + \frac{1}{2}a + C_1 - \ell_0\right) + K'\left(H - y_2 - a - C_1' - \ell_0'\right)
$$

$$
\boxed{(m_1 + m_2)\ddot{y}_2 + \frac{1}{2}m_1\ddot{a} + (K + K')y_2 + \left(\frac{1}{2}K + K'\right)a = (m_1 + m_2)g + F + K(\ell_0 - C_1) + K'(H - C_1' - \ell_0')}
$$

**Paso 6 — Ecuación diferencial para la coordenada $a$**

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{a}}\right) - \frac{\partial L}{\partial a} = Q_a
$$

$$
\frac{\partial L}{\partial \dot{a}} = \frac{1}{2}m_1\dot{y}_2 + \frac{1}{4}m_1\dot{a} \implies \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{a}}\right) = \frac{1}{2}m_1\ddot{y}_2 + \frac{1}{4}m_1\ddot{a}
$$

$$
\frac{\partial L}{\partial a} = \frac{1}{2}m_1 g - \frac{1}{2}K\left(y_2 + \frac{1}{2}a + C_1 - \ell_0\right) + K'\left(H - y_2 - a - C_1' - \ell_0'\right)
$$

$$
\boxed{\frac{1}{2}m_1\ddot{y}_2 + \frac{1}{4}m_1\ddot{a} + \left(\frac{1}{2}K + K'\right)y_2 + \left(\frac{1}{4}K + K'\right)a = \frac{1}{2}m_1 g + F + \frac{1}{2}K(\ell_0 - C_1) + K'(H - C_1' - \ell_0')}
$$
