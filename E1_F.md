# E1_F (grados de libertad deben ser mejorados)

Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal, conectado a una pared fija mediante un resorte de constante $K$, longitud natural $\ell_0$ y semiancho $b_1/2$. Un cable inextensible pasa por una polea fija en el borde y conecta $m_1$ con una masa $m_2$ que cuelga verticalmente, imponiendo $\dot{x}_1 = \dot{y}_2$. Debajo de $m_2$ cuelga una masa $m_3$ unida por un resorte de constante $K'$ y longitud natural $\ell_0'$. Los semianchos de $m_2$ y $m_3$ son $b_2/2$ y $b_3/2$ respectivamente.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.5,0) rectangle (0,2);
    \draw[thick] (0,0) -- (0,2);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.2) rectangle (5,0);
    \draw[thick] (0,0) -- (5,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (0,1) -- (1.5,1);
    \node[above, maincolor] at (0.75,1.2) {$K$};

    % Bloque m1
    \draw[fill=teal!10, draw=maincolor, thick] (1.5,0.3) rectangle (2.8,1.7);
    \node[maincolor] at (2.15,1.0) {$m_1$};

    % Polea
    \draw[thick, fill=gray!20] (5,1) circle (0.3);
    \fill (5,1) circle (0.05);
    \draw[thick] (5,0) -- (5,1);

    % Cable
    \draw[thick] (2.8,1.3) -- (5,1.3);
    \draw[thick] (5.3,1) -- (5.3,-1);

    % Bloque m2
    \draw[fill=teal!10, draw=maincolor, thick] (4.8,-1.7) rectangle (5.8,-1);
    \node[maincolor] at (5.3,-1.35) {$m_2$};

    % Resorte K'
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (5.3,-1.7) -- (5.3,-2.8);
    \node[right, accentcolor] at (5.5,-2.25) {$K'$};

    % Bloque m3
    \draw[fill=orange!10, draw=accentcolor, thick] (4.8,-3.5) rectangle (5.8,-2.8);
    \node[accentcolor] at (5.3,-3.15) {$m_3$};

    % Coordenadas
    \draw[->, maincolor, thick] (0,2.1) -- (2.15,2.1) node[midway, above] {$x_1$};
    \draw[dotted] (2.15,1.7) -- (2.15,2.3);
    \draw[dotted] (0,2) -- (0,2.3);

    \draw[->, maincolor, thick] (6.5,1) -- (6.5,-1.35) node[midway, right] {$y_2$};
    \draw[dotted] (5.8,-1.35) -- (6.7,-1.35);
    \draw[dotted] (5,1) -- (6.7,1);

    \draw[->, accentcolor, thick] (7.3,1) -- (7.3,-3.15) node[midway, right] {$y_3$};
    \draw[dotted] (5.8,-3.15) -- (7.5,-3.15);
\end{tikzpicture}
\end{document}
```

---

## Coordenadas y restricciones

Coordenadas posibles: $x_1,\ y_2,\ y_3$

Restricción — cable inextensible:

$$\dot{x}_1 = \dot{y}_2 \implies x_1 = y_2 + C_0$$

**GDL = 2** — coordenadas independientes: $x_1$ e $y_3$

---

## Energía cinética

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

Aplicando $\dot{y}_2 = \dot{x}_1$:

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{x}_1^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

---

## Energía potencial

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_1 g\, 0- m_2 g\, y_2 - m_3 g\, y_3 + \frac{K'}{2}\!\left(y_3 - y_2 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

Sustituyendo $y_2 = x_1 - C_0$:

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,(x_1 - C_0) - m_3 g\, y_3 + \frac{K'}{2}\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

---

## Ecuaciones de Lagrange

### Para $x_1$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) = (m_1 + m_2)\ddot{x}_1, \qquad \frac{\partial T}{\partial x_1} = 0$$

$$-\frac{\partial V}{\partial x_1} = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)$$

$$\boxed{(m_1 + m_2)\ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

### Para $y_3$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_3}\right) = m_3 \ddot{y}_3, \qquad \frac{\partial T}{\partial y_3} = 0$$

$$-\frac{\partial V}{\partial y_3} = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)$$

$$\boxed{m_3 \ddot{y}_3 = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

---

## EDOs finales

$$\boxed{(m_1 + m_2)\ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

$$\boxed{m_3 \ddot{y}_3 = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$
