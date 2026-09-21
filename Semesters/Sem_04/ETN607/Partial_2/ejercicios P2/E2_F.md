Un bloque-cuña de masa $m_1$ y ancho $B_1$ desliza sin fricción sobre una superficie horizontal, conectado a la pared derecha mediante un resorte de constante $K$ y longitud natural $\ell_0$. La cara izquierda de $m_1$ está inclinada a $60°$ respecto a la horizontal. Una segunda cuña de masa $m_2$ apoya su cara inclinada sobre la de $m_1$ y está guiada verticalmente por la pared izquierda, de modo que solo puede desplazarse en dirección vertical. La distancia entre paredes es $B$ y la posición horizontal de $m_1$ medida desde la pared izquierda es $x_1$.

Hallar la ecuación de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda (guía vertical para m2)
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,4);
    \draw[thick] (0,0) -- (0,4);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (7,0);
    \draw[thick] (0,0) -- (7,0);

    % Pared derecha (apoyo del resorte)
    \fill[pattern=north east lines] (7,0) rectangle (7.3,3);
    \draw[thick] (7,0) -- (7,3);

    \draw[fill=teal!10, draw=maincolor, thick] (2.5,0) -- (5.5,0) -- (5.5,1.5) -- (3.366,1.5) -- cycle;
    \node[maincolor] at (4.5,0.7) {$m_1$};

    % Resorte K de lado derecho de m1 a pared derecha
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (5.5,0.75) -- (7,0.75);
    \node[above, maincolor] at (6.25,0.95) {$K$};

    % Ángulo 60° en vértice inf-izq de m1
    \draw[thick, maincolor] (2.5,0) ++(0.5,0) arc (0:60:0.5);
    \node[maincolor] at (3.25,0.28) {$60^\circ$};

    \draw[fill=orange!10, draw=accentcolor, thick] (0,1.5) -- (2.134,1.5) -- (3.0,3.0) -- (0,3.0) -- cycle;
    \node[accentcolor] at (1.0,2.3) {$m_2$};

    % Coordenada x1 — de pared izq al vértice inf-izq de m1
    \draw[->, maincolor, thick] (0,-0.7) -- (2.5,-0.7) node[midway, below] {$x_1$};
    \draw[dotted] (0,0) -- (0,-0.9);
    \draw[dotted] (2.5,0) -- (2.5,-0.9);

    % Cota B1 — ancho total de m1
    \draw[<->, maincolor] (2.5,-1.2) -- (5.5,-1.2) node[midway, below] {$B_1$};
    \draw[dotted] (5.5,0) -- (5.5,-1.4);

    % Cota B — de pared a pared
    \draw[<->, accentcolor] (0,-1.7) -- (7,-1.7) node[midway, below] {$B$};

    % Coordenada y2 — vertical desde piso hasta base inferior de m2
    \draw[->, accentcolor, thick] (-0.7,0) -- (-0.7,1.5) node[midway, left] {$y_2$};
    \draw[dotted] (0,0) -- (-0.9,0);
    \draw[dotted] (0,1.5) -- (-0.9,1.5);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** $m_1$ (teal, trapecio) reposa sobre el piso con su cara derecha vertical conectada al resorte $K$ y su cara izquierda inclinada a $60°$. $m_2$ (naranja, trapecio invertido) está pegada a la pared izquierda y apoya su cara inclinada derecha sobre la de $m_1$; solo puede moverse verticalmente. La coordenada $x_1$ mide la posición horizontal del vértice inferior izquierdo de $m_1$ desde la pared izquierda. La coordenada $y_2$ mide la altura de la base inferior de $m_2$ desde el piso. Se indican las cotas $B_1$ (ancho de $m_1$) y $B$ (distancia entre paredes).

---

## Resolución

### Coordenadas y GDL

Coordenadas posibles del sistema:

$$N = (x_1,\ y_2)$$

Donde $x_1$ es la posición horizontal de $m_1$ e $y_2$ es la posición vertical de $m_2$.

Restricción geométrica por contacto en la interfaz inclinada a $60°$:

$$\tan 60° = \sqrt{3} = \frac{y_2}{B_2 - x_1} \implies y_2 = \frac{B_2 - x_1}{\sqrt{3}}$$

Derivando con respecto al tiempo:

$$\dot{y}_2 = -\frac{1}{\sqrt{3}}\,\dot{x}_1$$

Número de grados de libertad:

$$\text{GDL} = N - \text{restricciones} = 2 - 1 = 1$$

Coordenada independiente seleccionada: $x_1$.

---

### Energía cinética

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2$$

Sustituyendo $\dot{y}_2 = -\dfrac{\dot{x}_1}{\sqrt{3}}$:

$$\boxed{T = \frac{1}{2}\!\left(m_1 + \frac{m_2}{3}\right)\dot{x}_1^2}$$

---

### Energía potencial

$$V = \frac{1}{2}K(B - B_1 - x_1 - \ell_0)^2 + m_2 g\, y_2$$

Sustituyendo $y_2 = \dfrac{B_2 - x_1}{\sqrt{3}}$:

$$\boxed{V = \frac{1}{2}K(B - B_1 - x_1 - \ell_0)^2 + \frac{m_2 g}{\sqrt{3}}(B_2 - x_1)}$$

---

### Ecuación de Lagrange

#### Para $x_1$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) = \left(m_1 + \frac{m_2}{3}\right)\ddot{x}_1, \qquad \frac{\partial T}{\partial x_1} = 0$$

$$-\frac{\partial V}{\partial x_1} = +K(B - B_1 - x_1 - \ell_0) + \frac{m_2 g}{\sqrt{3}}$$

---

### EDO final

$$\boxed{\left(m_1 + \frac{m_2}{3}\right)\ddot{x}_1 = +K(B - B_1 - x_1 - \ell_0) + \frac{m_2 g}{\sqrt{3}}}$$
