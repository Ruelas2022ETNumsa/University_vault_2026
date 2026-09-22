Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal, conectado a una pared fija a su izquierda mediante un resorte de constante $K$ y longitud natural $\ell_0$. Un cable inextensible sale del lado derecho de $m_1$, pasa por una polea fija en el borde de la superficie y desciende verticalmente a lo largo de una pared vertical. La masa $m_2$ desciende rozando la pared vertical con coeficiente de amortiguamiento viscoso $c_2$; de su parte inferior cuelga, mediante un resorte de constante $K'$ y longitud natural $\ell_0'$, la masa $m_3$ que también roza la misma pared con coeficiente $c_3$. La altura total del sistema vertical es $H$. Las coordenadas $x_1$ (desde la pared izquierda hasta el centro de $m_1$), $y_2$ e $y_3$ (desde la polea hacia abajo hasta el centro de $m_2$ y $m_3$ respectivamente) describen la configuración del sistema.

> **Nota de notación:** El docente emplea $b_i$ con doble significado en este problema: como **dimensión geométrica** (altura) del bloque $i$ al calcular la energía potencial (deformaciones de resortes), y como **coeficiente de amortiguamiento viscoso** al plantear las fuerzas disipativas. En la resolución se sigue la notación del docente — $b_1$, $b_2$, $b_3$ dentro de $V$ son alturas de los bloques; los coeficientes de amortiguamiento se indican aquí como $c_2$ y $c_3$ para distinguirlos, aunque en la pizarra ambos usan $b$.

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
    \fill[pattern=north east lines] (0,-0.2) rectangle (5.8,0);
    \draw[thick] (0,0) -- (5.8,0);

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (0,0.7) -- (1.5,0.7);
    \node[above, maincolor] at (0.75,0.9) {$K$};

    % Bloque m1
    \draw[fill=teal!10, draw=maincolor, thick] (1.5,0) rectangle (2.8,1.4);
    \node[maincolor] at (2.15,0.7) {$m_1$};

    % Polea
    \draw[thick, fill=gray!20] (5.5,0.7) circle (0.3);
    \fill (5.5,0.7) circle (0.05);
    \draw[thick] (5.5,0) -- (5.5,0.4);

    % Cable
    \draw[thick] (2.8,1.0) -- (5.5,1.0);
    \draw[thick] (5.5,0.4) -- (5.5,-1);

    % Pared vertical izquierda del canal (m2 y m3 rozan aqui)
    \fill[pattern=north east lines] (4.5,-4) rectangle (5,-0.5);
    \draw[thick] (5,-4) -- (5,-0.5);

    % Bloque m2
    \draw[fill=teal!10, draw=maincolor, thick] (5,-1.7) rectangle (6,-1);
    \node[maincolor] at (5.5,-1.35) {$m_2$};

    % Resorte K'
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, accentcolor, thick] (5.5,-1.7) -- (5.5,-2.8);
    \node[right, accentcolor] at (5.7,-2.25) {$K'$};

    % Bloque m3
    \draw[fill=orange!10, draw=accentcolor, thick] (5,-3.5) rectangle (6,-2.8);
    \node[accentcolor] at (5.5,-3.15) {$m_3$};

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

> **Descripción de la figura:** $m_1$ (teal) reposa sobre el piso y está conectada a la pared izquierda por el resorte $K$. Un cable horizontal parte del lado derecho de $m_1$, rodea la polea fija en el borde derecho del piso y desciende verticalmente. $m_2$ (teal) y $m_3$ (naranja) deslizan rozando la pared vertical con coeficientes viscosos $c_2$ y $c_3$ respectivamente. El resorte $K'$ conecta la base de $m_2$ con la parte superior de $m_3$. Las coordenadas $x_1$ (horizontal, desde la pared hasta el centro de $m_1$), $y_2$ e $y_3$ (verticales, desde la polea hasta el centro de $m_2$ y $m_3$) se indican con flechas.

---

## Caso 1 — Resolución del docente

Coordenadas generalizadas independientes: $x_1$ e $y_3$ (se elimina $y_2$ con la ligadura del cable).

### Coordenadas y GDL

$$N = (x_1,\ y_2,\ y_3)$$

Restricción por cable inextensible:

$$\dot{x}_1 = \dot{y}_2 \implies x_1 = y_2 + C_0$$

$$\text{GDL} = 3 - 1 = 2 \qquad \text{coord. independientes: } x_1,\ y_3$$

---

### Energía cinética

$$T = \frac{1}{2}m_1\dot{x}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 + \frac{1}{2}m_3\dot{y}_3^2$$

Aplicando $\dot{y}_2 = \dot{x}_1$:

$$T = \frac{1}{2}(m_1 + m_2)\dot{x}_1^2 + \frac{1}{2}m_3\dot{y}_3^2$$

---

### Energía potencial

Las elongaciones de los resortes dependen de la posición del centro de cada bloque, descontando la mitad de su altura $b_i$ y la longitud natural:

$$\Delta\ell_K = x_1 - \tfrac{b_1}{2} - \ell_0 \qquad \Delta\ell_{K'} = y_3 - y_2 - \tfrac{b_2}{2} - \tfrac{b_3}{2} - \ell_0'$$

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,y_2 - m_3 g\,y_3 + \frac{K'}{2}\!\left(y_3 - y_2 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

Sustituyendo $y_2 = x_1 - C_0$:

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,(x_1 - C_0) - m_3 g\,y_3 + \frac{K'}{2}\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

---

### Ecuaciones de Lagrange

#### Para $x_1$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) = (m_1+m_2)\ddot{x}_1$$

$$-\frac{\partial V}{\partial x_1} = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)$$

$$\boxed{(m_1+m_2)\ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

#### Para $y_3$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_3}\right) = m_3\ddot{y}_3$$

$$-\frac{\partial V}{\partial y_3} = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)$$

$$\boxed{m_3\ddot{y}_3 = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

> **Nota:** El docente omite la disipación en pizarra. Las EDOs completas con amortiguamiento viscoso se presentan en el Caso 2.

---

## Caso 2 — Resolución con disipación (NotebookLM / Rayleigh)

Misma ligadura y mismo sistema, pero usando $y_2$ como coordenada libre (equivalente por simetría) e incorporando la función de disipación de Rayleigh.

### Coordenadas independientes: $y_2$ e $y_3$

La ligadura $\dot{x}_1 = \dot{y}_2$ permite expresar todo en $y_2$:

$$T = \frac{1}{2}(m_1+m_2)\dot{y}_2^2 + \frac{1}{2}m_3\dot{y}_3^2$$

### Energía potencial

Mismas elongaciones, expresadas en $y_2$:

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,y_2 - m_3 g\,y_3 + \frac{K'}{2}\!\left(y_3 - y_2 - \frac{b_2+b_3}{2} - \ell_0'\right)^{\!2}$$

> $x_1$ en el término de $K$ se mantiene por la ligadura $x_1 = y_2 + C_0$.

### Función de disipación de Rayleigh

$$\mathcal{F} = \frac{1}{2}c_2\dot{y}_2^2 + \frac{1}{2}c_3\dot{y}_3^2$$

### EDOs con disipación

Aplicando $\dfrac{d}{dt}\dfrac{\partial T}{\partial \dot{q}_i} - \dfrac{\partial T}{\partial q_i} + \dfrac{\partial \mathcal{F}}{\partial \dot{q}_i} = -\dfrac{\partial V}{\partial q_i}$:

$$\boxed{(m_1+m_2)\ddot{y}_2 + c_2\dot{y}_2 + K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) - K'\!\left(y_3 - y_2 - \frac{b_2+b_3}{2} - \ell_0'\right) = m_2 g}$$

$$\boxed{m_3\ddot{y}_3 + c_3\dot{y}_3 + K'\!\left(y_3 - y_2 - \frac{b_2+b_3}{2} - \ell_0'\right) = m_3 g}$$

> **Relación con Caso 1:** sustituyendo $y_2 = x_1 - C_0$ y $c_2 = c_3 = 0$ se recuperan exactamente las EDOs del docente.
