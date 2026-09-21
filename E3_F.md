Una polea de masa $m_1$ (sin inercia rotacional) está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$. Del ramal izquierdo de $m_1$ cuelga un resorte de constante $K'$ y longitud natural $\ell_0'$ fijo al piso. Del ramal derecho cuelga una segunda polea de masa $m_2$ (sin inercia rotacional) a una distancia $a$ de $m_1$. Un cable inextensible de longitud $\ell$ pasa por $m_2$ y del extremo inferior cuelga una masa puntual $m_3$. La altura total del sistema es $H$.

Hallar las ecuaciones de movimiento de Lagrange del sistema (2 GDL: $y_3$, $a$).

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,5.0) rectangle (4.5,5.3);
    \draw[thick] (-1,5.0) -- (4.5,5.0);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (4.5,0);
    \draw[thick] (-1,0) -- (4.5,0);

    % Resorte K — techo a polea 1
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,5.0) -- (1.0,3.7);
    \node[left, maincolor] at (0.75,4.35) {$K$};

    % Polea 1 (m1)
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,3.4) circle (0.3);
    \fill[maincolor] (1.0,3.4) circle (0.05);
    \node[left, maincolor] at (0.55,3.4) {$m_1$};

    % Ramal izquierdo de m1 — cable + resorte K' al piso
    \draw[thick, maincolor] (0.7,3.4) -- (0.7,1.8);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, maincolor, thick] (0.7,1.8) -- (0.7,0);
    \node[left, maincolor] at (0.45,0.9) {$K'$};

    % Ramal derecho de m1 — cable a polea 2
    \draw[thick, maincolor] (1.3,3.4) -- (1.3,2.0);

    % Polea 2 (m2)
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,1.7) circle (0.3);
    \fill[accentcolor] (1.3,1.7) circle (0.05);
    \node[right, accentcolor] at (1.65,1.7) {$m_2$};

    % Cable por polea 2 — ramal derecho baja a m3
    \draw[thick, accentcolor] (1.6,1.7) -- (1.6,0.6);

    % m3 — masa puntual (círculo pequeño)
    \draw[thick, fill=accentcolor!30, draw=accentcolor] (1.6,0.45) circle (0.15);
    \node[right, accentcolor] at (1.8,0.45) {$m_3$};

    % Ramal izquierdo de m2 — baja directo al piso
    \draw[thick, accentcolor] (1.0,1.7) -- (1.0,0);

    % Cota H — altura total
    \draw[<->, red, thick] (-0.6,0) -- (-0.6,5.0) node[midway, left] {$H$};

    % Coordenada y1 — techo a m1
    \draw[->, maincolor, thick] (2.2,5.0) -- (2.2,3.4) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,3.4) -- (2.3,3.4);
    \draw[dotted] (1.0,5.0) -- (2.3,5.0);

    % Coordenada y2 — techo a m2
    \draw[->, accentcolor, thick] (2.9,5.0) -- (2.9,1.7) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,1.7) -- (3.0,1.7);

    % Coordenada y3 — techo a m3
    \draw[->, accentcolor, thick] (3.6,5.0) -- (3.6,0.45) node[midway, right] {$y_3$};
    \draw[dotted] (1.75,0.45) -- (3.7,0.45);

    % Cota a — distancia entre poleas
    \draw[<->, maincolor, thick] (1.85,3.4) -- (1.85,1.7) node[midway, right] {$a$};
    \draw[dotted] (1.3,3.4) -- (2.0,3.4);

\end{tikzpicture}
\end{document}
```

---

## Coordenadas y restricciones

Coordenadas posibles: $y_1,\ y_2,\ y_3$

Restricción — cable inextensible por polea 2:

$$H - y_2 + \pi R_2 + y_3 - y_2 = \ell \implies y_2 = \frac{1}{2}(H + \pi R_2 + y_3 - \ell)$$

$$\dot{y}_2 = \frac{\dot{y}_3}{2}$$

**GDL = 3 - 1 = 2** — coordenadas independientes: $y_3$ y $a$

Relación entre poleas:

$$y_2 = y_1 + a \implies y_1 = y_2 - a = \frac{1}{2}(H + \pi R_2 + y_3 - \ell) - a$$

$$\dot{y}_1 = \frac{\dot{y}_3}{2} - \dot{a}$$

> **Aux:** $y_1$ es cambio de variable — el docente lo expande directamente en las EDOs:
> $y_1 - \ell_0 = \tfrac{H + \pi R_2 + y_3 - \ell}{2} - a - \ell_0$ · · · $H - y_1 + \pi R_1 + a - \ell_0' = \tfrac{H - \pi R_2 - y_3 + \ell}{2} + 2a + \pi R_1 - \ell_0'$

---

## Energía cinética

$$T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{y}_2^2 + \frac{m_3}{2}\dot{y}_3^2$$

Sustituyendo $\dot{y}_1 = \dfrac{\dot{y}_3}{2} - \dot{a}$ y $\dot{y}_2 = \dfrac{\dot{y}_3}{2}$:

$$\boxed{T = \frac{m_1}{2}\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right)^{\!2} + \frac{m_2}{2}\!\left(\frac{\dot{y}_3}{2}\right)^{\!2} + \frac{m_3}{2}\dot{y}_3^2}$$

---

## Energía potencial

$$V = \frac{K}{2}(y_1 - \ell_0)^2 - m_1 g\, y_1 - m_2 g\, y_2 - m_3 g\, y_3 + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')^2$$

Sustituyendo $y_1$ e $y_2$ en función de $y_3$ y $a$:

$$\boxed{V = \frac{K}{2}\!\left[\frac{H + \pi R_2 + y_3 - \ell}{2} - a - \ell_0\right]^{\!2} - m_1 g\!\left(\frac{H + \pi R_2 + y_3 - \ell}{2} - a\right) - m_2 g\!\left(\frac{H + \pi R_2 + y_3 - \ell}{2}\right) - m_3 g\, y_3 + \frac{K'}{2}\!\left[\frac{H - \pi R_2 - y_3 + \ell}{2} + 2a + \pi R_1 - \ell_0'\right]^{\!2}}$$

---

## Ecuaciones de Lagrange

### Para $y_3$

$$\frac{\partial T}{\partial \dot{y}_3} = \frac{m_1}{2}\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right) + \frac{m_2}{4}\dot{y}_3 + m_3\dot{y}_3 \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_3}\right) = \left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a}$$

$$-\frac{\partial V}{\partial y_3} = -\frac{K}{2}(y_1 - \ell_0) + \frac{m_1 g}{2} + \frac{m_2 g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')$$

$$\boxed{\left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a} = -\frac{K}{2}(y_1 - \ell_0) + \frac{(m_1 + m_2)g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')}$$

### Para $a$

$$\frac{\partial T}{\partial \dot{a}} = -m_1\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right) \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{a}}\right) = m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3$$

$$-\frac{\partial V}{\partial a} = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')$$

$$\boxed{m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3 = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')}$$

---

## EDOs finales

$$\boxed{\left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a} = -\frac{K}{2}(y_1 - \ell_0) + \frac{(m_1 + m_2)g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')}$$

$$\boxed{m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3 = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')}$$
