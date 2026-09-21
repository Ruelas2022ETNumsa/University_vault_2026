Un bloque-cuña de masa $m_1$ desliza sin fricción sobre una superficie horizontal, conectado a una pared fija mediante un resorte de constante $K$ y longitud natural $\ell_0$. Una segunda cuña de masa $m_2$ apoya sobre la cara inclinada a $60°$ de $m_1$ y está guiada verticalmente por una pared fija, de modo que solo puede desplazarse en dirección vertical. La restricción geométrica del contacto impone $\dot{y}_2 = -\dot{x}_1/\sqrt{3}$.

Hallar la ecuación de movimiento de Lagrange del sistema (1 GDL: $x_1$).

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

    % m1 — trapecio: base ancha abajo, cara inclinada 60° a la izquierda, lado derecho vertical con resorte
    % esquinas: (2.5,0) vértice inf-izq, (5.5,0) inf-der, (5.5,1.5) sup-der, (3.433,1.5) sup-izq
    % la cara izq inclinada va de (2.5,0) a (3.433,1.5): tan60=1.5/(3.433-2.5)=1.5/0.933≈1.608 ≈ correcto con sqrt3
    \draw[fill=teal!10, draw=maincolor, thick] (2.5,0) -- (5.5,0) -- (5.5,1.5) -- (3.366,1.5) -- cycle;
    \node[maincolor] at (4.5,0.7) {$m_1$};

    % Resorte K de lado derecho de m1 a pared derecha
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (5.5,0.75) -- (7,0.75);
    \node[above, maincolor] at (6.25,0.95) {$K$};

    % Ángulo 60° en vértice inf-izq de m1
    \draw[thick, maincolor] (2.5,0) ++(0.5,0) arc (0:60:0.5);
    \node[maincolor] at (3.25,0.28) {$60^\circ$};

    % m2 — mismo trapecio girado 180°, pegado a pared izquierda
    % m1 girado 180°: cara inclinada queda a la derecha, lado izq vertical en x=0
    % esquinas: (0,1.5) inf-izq, (2.134,1.5) inf-der (=ancho de m1 sup), (0,3.0) sup-izq, (0+B,3.0) sup-der
    % ancho sup de m1 = 5.5-3.366=2.134, ancho inf de m1 = 5.5-2.5=3.0
    % m2 girado: base ancha ARRIBA (ancho 3.0), base angosta ABAJO (ancho 2.134), cara inclinada a la derecha
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

> figura v4 — $m_1$ trapecio con cara inclinada 60° a la izquierda y resorte a la derecha; $m_2$ mismo trapecio girado 180° pegado a pared izquierda, cara inclinada a la derecha. Contacto en interfaz inclinada.

---

## Coordenadas y restricciones

Coordenadas posibles: $x_1,\ y_2$

Restricción geométrica — contacto en interfaz a $60°$:

$$\tan 60° = \sqrt{3} = \frac{y_2}{B_2 - x_1} \implies B_2 - x_1 = \frac{y_2}{\sqrt{3}} \cdot \sqrt{3} \implies y_2 = \frac{B_2 - x_1}{\sqrt{3}}$$

Derivando:

$$\dot{y}_2 = -\frac{1}{\sqrt{3}}\,\dot{x}_1$$

**GDL = 1** — coordenada independiente: $x_1$

---

## Energía cinética

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2$$

Sustituyendo $\dot{y}_2 = -\dfrac{\dot{x}_1}{\sqrt{3}}$:

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \frac{\dot{x}_1^2}{3} = \frac{1}{2}\!\left(m_1 + \frac{m_2}{3}\right)\dot{x}_1^2$$

$$\boxed{T = \frac{1}{2}\!\left(m_1 + \frac{m_2}{3}\right)\dot{x}_1^2}$$

---

## Energía potencial

$$V = \frac{1}{2}K(B - B_1 - x_1 - \ell_0)^2 + m_2 g\, y_2$$

Sustituyendo $y_2 = \dfrac{B_2 - x_1}{\sqrt{3}}$:

$$\boxed{V = \frac{1}{2}K(B - B_1 - x_1 - \ell_0)^2 + \frac{m_2 g}{\sqrt{3}}(B_2 - x_1)}$$

---

## Ecuación de Lagrange

### Para $x_1$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) = \left(m_1 + \frac{m_2}{3}\right)\ddot{x}_1, \qquad \frac{\partial T}{\partial x_1} = 0$$

$$-\frac{\partial V}{\partial x_1} = +K(B - B_1 - x_1 - \ell_0) + \frac{m_2 g}{\sqrt{3}}$$

---

## EDO final

$$\boxed{\left(m_1 + \frac{m_2}{3}\right)\ddot{x}_1 = +K(B - B_1 - x_1 - \ell_0) + \frac{m_2 g}{\sqrt{3}}}$$
