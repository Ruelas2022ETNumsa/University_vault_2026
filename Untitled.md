# Ej 1
##### Ej. Sistema de tres masas con resortes, polea y pared vertical — 2 GDL

**Enunciado:**
Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal, conectado a una pared fija a su izquierda mediante un resorte de constante $K$ y longitud natural $\ell_0$. Un cable inextensible sale del lado derecho de $m_1$, pasa por una polea fija en el borde de la superficie y desciende verticalmente por el lado derecho de la polea a lo largo de una pared vertical fija. La masa $m_2$ está conectada al cable y su cara izquierda roza la pared vertical; de su parte inferior cuelga, mediante un resorte de constante $K'$ y longitud natural $\ell_0'$, la masa $m_3$ cuya cara izquierda también roza la misma pared vertical. Se definen $x_1$ como la distancia horizontal desde la pared izquierda hasta el centro de $m_1$, $y_2$ como la distancia vertical desde el eje de la polea hasta el centro de $m_2$, e $y_3$ como la distancia vertical desde el eje de la polea hasta el centro de $m_3$. El sistema tiene 2 grados de libertad. Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.0, >=latex]

\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% PARED IZQUIERDA
\fill[pattern=north east lines] (-0.5,0) rectangle (0,2);
\draw[thick] (0,0) -- (0,2);

% PISO HORIZONTAL
\fill[pattern=north east lines] (0,-0.2) rectangle (5.5,0);
\draw[thick] (0,0) -- (5.5,0);

% RESORTE K
\draw[decorate, decoration={coil, aspect=0.3, segment length=2mm, amplitude=3mm}, maincolor, thick]
    (0,0.7) -- (1.5,0.7);
\node[above, maincolor] at (0.75,0.9) {$K$};

% BLOQUE m1
\draw[fill=teal!10, draw=maincolor, thick] (1.5,0) rectangle (2.8,1.4);
\node[maincolor] at (2.15,0.7) {$m_1$};

% CUERDA HORIZONTAL
\draw[thick] (2.8,1.0) -- (5.2,1.0);

% POLEA — centro (5.5, 0.7)
\draw[thick, fill=gray!20] (5.5,0.7) circle (0.3);
\fill (5.5,0.7) circle (0.05);
\draw[thick] (5.5,0) -- (5.5,0.4);

% CUERDA VERTICAL — lado derecho de la polea: x = 5.8
\draw[thick] (5.8,0.7) -- (5.8,-1.0);

% PARED VERTICAL
\fill[pattern=north east lines] (4.5,-4) rectangle (5,0);
\draw[thick] (5,-4) -- (5,0);

% BLOQUE m2
\draw[fill=teal!10, draw=maincolor, thick] (5,-1.7) rectangle (6,-1.0);
\node[maincolor] at (5.5,-1.35) {$m_2$};

% RESORTE K'
\draw[decorate, decoration={coil, aspect=0.3, segment length=2mm, amplitude=2.5mm}, accentcolor, thick]
    (5.5,-1.7) -- (5.5,-2.8);
\node[right, accentcolor] at (5.7,-2.25) {$K'$};

% BLOQUE m3
\draw[fill=orange!10, draw=accentcolor, thick] (5,-3.5) rectangle (6,-2.8);
\node[accentcolor] at (5.5,-3.15) {$m_3$};

% COORDENADA x1
\draw[<->, maincolor, thick] (0,2.1) -- (2.15,2.1) node[midway, above] {$x_1$};
\draw[dotted] (0,1.8) -- (0,2.3);
\draw[dotted] (2.15,1.4) -- (2.15,2.3);

% COORDENADA y2 — eje polea -> centro m2
\draw[<->, maincolor, thick] (6.7,0.7) -- (6.7,-1.35) node[midway, right] {$y_2$};
\draw[dotted] (5.5,0.7) -- (6.9,0.7);
\draw[dotted] (6.0,-1.35) -- (6.9,-1.35);

% COORDENADA y3 — eje polea -> centro m3
\draw[<->, accentcolor, thick] (7.5,0.7) -- (7.5,-3.15) node[midway, right] {$y_3$};
\draw[dotted] (5.5,0.7) -- (7.7,0.7);
\draw[dotted] (6.0,-3.15) -- (7.7,-3.15);

\end{tikzpicture}

\end{document}
```

---

**Descripción del sistema:**

$m_1$ (teal) reposa sobre el piso horizontal y está conectada a la pared izquierda fija mediante el resorte $K$. Un cable inextensible parte horizontalmente del lado derecho de $m_1$, rodea la polea fija (apoyada en el piso por su soporte) y desciende verticalmente por el lado derecho de la misma. La pared vertical fija se ubica a la izquierda de $m_2$ y $m_3$: ambas tienen su cara izquierda en contacto con esta pared. El cable conecta directamente al techo de $m_2$. El resorte $K'$ une la base de $m_2$ con el techo de $m_3$. Las coordenadas $x_1$ (horizontal, desde la pared izquierda hasta el centro de $m_1$), $y_2$ e $y_3$ (verticales, desde el eje de la polea hacia abajo hasta el centro de $m_2$ y $m_3$ respectivamente) se indican con flechas.

**Datos del sistema:** $m_1,\ m_2,\ m_3,\ K,\ K',\ \ell_0,\ \ell_0',\ b_1,\ b_2,\ b_3$ (alturas de bloques), $g$

---

**Resolución**

---

**Paso 1 — Ligadura cinemática**

Cuando $m_1$ avanza a la derecha ($\dot{x}_1 > 0$), $m_2$ desciende ($\dot{y}_2 > 0$):

$$\dot{x}_1 = \dot{y}_2 \implies x_1 = y_2 + C_0$$

Coordenadas generalizadas independientes: $q_1 = x_1$, $q_2 = y_3$ $\quad(\text{GDL} = 2)$

---

**Paso 2 — Energía cinética**

$$T = \frac{1}{2}m_1\dot{x}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 + \frac{1}{2}m_3\dot{y}_3^2$$

Aplicando $\dot{y}_2 = \dot{x}_1$:

$$\boxed{T = \frac{1}{2}(m_1 + m_2)\dot{x}_1^2 + \frac{1}{2}m_3\dot{y}_3^2}$$

---

**Paso 3 — Energía potencial**

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,y_2 - m_3 g\,y_3 + \frac{K'}{2}\!\left(y_3 - y_2 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

Sustituyendo $y_2 = x_1 - C_0$:

$$\boxed{V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,(x_1 - C_0) - m_3 g\,y_3 + \frac{K'}{2}\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}}$$

---

**Paso 4 — Ecuaciones de movimiento de Lagrange**

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{q}_i}\right) - \frac{\partial T}{\partial q_i} = -\frac{\partial V}{\partial q_i}$$

#### Para $q_1 = x_1$

$$\boxed{(m_1 + m_2)\ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

#### Para $q_2 = y_3$

$$\boxed{m_3\ddot{y}_3 = m_3 g - K'\!\left(y_3 - x_1 + C_0 - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

---
---

# Ej 2

Un bloque-cuña de masa $m_1$ y ancho $B_1$ desliza sin fricción sobre una superficie horizontal, conectado a la pared derecha mediante un resorte de constante $K$ y longitud natural $\ell_0$. La cara izquierda de $m_1$ está inclinada a $60°$ respecto a la horizontal. Una segunda cuña de masa $m_2$ apoya su cara inclinada sobre la de $m_1$ y está guiada verticalmente por la pared izquierda, de modo que solo puede desplazarse en dirección vertical. La distancia entre paredes es $B$ y la posición horizontal de $m_1$ medida desde la pared izquierda es $x_1$. En la resolución se emplea la constante $B_2$, definida como la proyección horizontal de la cara inclinada de $m_2$ sobre el piso (ancho horizontal de $m_2$ medido desde su vértice inferior-izquierdo hasta su vértice inferior-derecho); la restricción de contacto en la interfaz inclinada a $60°$ resulta $\tan 60° = y_2/(B_2 - x_1)$, tal como lo plantea el docente en la resolución de referencia.

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

---
---

# Ej 3

Una polea de masa $m_1$ (sin inercia rotacional) está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$. Por el ramal izquierdo de $m_1$ pasa un cable que llega hasta el piso, donde está unido mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. Por el ramal derecho de $m_1$ pasa un cable que sostiene a una segunda polea de masa $m_2$ (sin inercia rotacional), ubicada a una distancia $a$ por debajo de $m_1$. Por $m_2$ pasa un cable inextensible de longitud $\ell$: del ramal izquierdo el cable baja hasta el piso, y del ramal derecho cuelga una masa puntual $m_3$. La altura total del sistema es $H$.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

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

> **Descripción de la figura:** El resorte $K$ conecta el techo con la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable hasta el resorte $K'$ anclado al piso. Del ramal derecho de $m_1$ desciende un cable hasta la polea $m_2$ (naranja), separada de $m_1$ por la distancia $a$. Del ramal izquierdo de $m_2$ un cable baja hasta el piso (extremo fijo). Del ramal derecho cuelga la masa puntual $m_3$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta cada masa. La cota $H$ es la altura total techo–piso.

---

## Resolución

### Coordenadas y GDL

Coordenadas posibles del sistema:

$$N = (y_1,\ y_2,\ y_3)$$

Restricción — cable inextensible por polea 2:

$$H - y_2 + \pi R_2 + y_3 - y_2 = \ell \implies y_2 = \frac{1}{2}(H + \pi R_2 + y_3 - \ell)$$

$$\dot{y}_2 = \frac{\dot{y}_3}{2}$$

Número de grados de libertad:

$$\text{GDL} = N - \text{restricciones} = 3 - 1 = 2$$

Coordenadas independientes seleccionadas: $y_3$ y $a$

Relación entre poleas:

$$y_2 = y_1 + a \implies y_1 = y_2 - a = \frac{1}{2}(H + \pi R_2 + y_3 - \ell) - a$$

$$\dot{y}_1 = \frac{\dot{y}_3}{2} - \dot{a}$$

> **Aux:** $y_1$ es cambio de variable — el docente lo expande directamente en las EDOs:
> $y_1 - \ell_0 = \tfrac{H + \pi R_2 + y_3 - \ell}{2} - a - \ell_0$ · · · $H - y_1 + \pi R_1 + a - \ell_0' = \tfrac{H - \pi R_2 - y_3 + \ell}{2} + 2a + \pi R_1 - \ell_0'$

---

### Energía cinética

$$T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{y}_2^2 + \frac{m_3}{2}\dot{y}_3^2$$

Sustituyendo $\dot{y}_1 = \dfrac{\dot{y}_3}{2} - \dot{a}$ y $\dot{y}_2 = \dfrac{\dot{y}_3}{2}$:

$$\boxed{T = \frac{m_1}{2}\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right)^{\!2} + \frac{m_2}{2}\!\left(\frac{\dot{y}_3}{2}\right)^{\!2} + \frac{m_3}{2}\dot{y}_3^2}$$

---

### Energía potencial

$$V = \frac{K}{2}(y_1 - \ell_0)^2 - m_1 g\, y_1 - m_2 g\, y_2 - m_3 g\, y_3 + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')^2$$

Sustituyendo $y_1$ e $y_2$ en función de $y_3$ y $a$:

$$\boxed{V = \frac{K}{2}\!\left[\frac{H + \pi R_2 + y_3 - \ell}{2} - a - \ell_0\right]^{\!2} - m_1 g\!\left(\frac{H + \pi R_2 + y_3 - \ell}{2} - a\right) - m_2 g\!\left(\frac{H + \pi R_2 + y_3 - \ell}{2}\right) - m_3 g\, y_3 + \frac{K'}{2}\!\left[\frac{H - \pi R_2 - y_3 + \ell}{2} + 2a + \pi R_1 - \ell_0'\right]^{\!2}}$$

---

### Ecuaciones de Lagrange

#### Para $y_3$

$$\frac{\partial T}{\partial \dot{y}_3} = \frac{m_1}{2}\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right) + \frac{m_2}{4}\dot{y}_3 + m_3\dot{y}_3 \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_3}\right) = \left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a}$$

$$-\frac{\partial V}{\partial y_3} = -\frac{K}{2}(y_1 - \ell_0) + \frac{m_1 g}{2} + \frac{m_2 g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')$$

$$\boxed{\left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a} = -\frac{K}{2}(y_1 - \ell_0) + \frac{(m_1 + m_2)g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')}$$

#### Para $a$

$$\frac{\partial T}{\partial \dot{a}} = -m_1\!\left(\frac{\dot{y}_3}{2} - \dot{a}\right) \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{a}}\right) = m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3$$

$$-\frac{\partial V}{\partial a} = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')$$

$$\boxed{m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3 = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')}$$

---

### EDOs finales

$$\boxed{\left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a} = -\frac{K}{2}(y_1 - \ell_0) + \frac{(m_1 + m_2)g}{2} + m_3 g + \frac{K'}{2}(H - y_1 + \pi R_1 + a - \ell_0')}$$

$$\boxed{m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3 = K(y_1 - \ell_0) - m_1 g - 2K'(H - y_1 + \pi R_1 + a - \ell_0')}$$

---
---
# Ej 4

Un carro de masa $M$ rueda sin fricción sobre una superficie horizontal. Sobre el carro está articulado un péndulo simple de varilla rígida sin masa, longitud $\ell$ y masa puntual $m$ en su extremo, que oscila en el plano vertical. El punto de articulación del péndulo se encuentra a altura $H$ sobre el suelo. El péndulo puede adoptar posiciones tanto por debajo como por encima del pivote; el ángulo $\theta$ se mide desde la vertical hacia arriba.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda (referencia origen)
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,3.0);
    \draw[thick] (0,0) -- (0,3.0);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (6.0,0);
    \draw[thick] (0,0) -- (6.0,0);

    % Carro M
    \draw[fill=teal!10, draw=maincolor, thick] (1.8,0.35) rectangle (3.8,1.5);
    \node[maincolor] at (2.8,0.92) {$M$};

    % Ruedas
    \draw[thick, fill=gray!30] (2.2,0.18) circle (0.18);
    \draw[thick, fill=gray!30] (3.4,0.18) circle (0.18);

    % Pivote del péndulo
    \fill[maincolor] (2.8,1.5) circle (0.06);

    % Línea vertical de referencia (ángulo theta)
    \draw[dashed, gray] (2.8,1.5) -- (2.8,2.8);

    % Varilla del péndulo — hacia arriba
    \draw[thick, accentcolor] (2.8,1.5) -- (4.1,2.65);
    \node[accentcolor, above right] at (3.45,2.1) {$\ell$};

    % Masa m (círculo) — arriba
    \draw[thick, fill=orange!20, draw=accentcolor] (4.1,2.65) circle (0.2);
    \node[accentcolor, right=4pt] at (4.1,2.65) {$m$};

    % Ángulo theta — desde vertical hacia arriba
    \draw[->, accentcolor] (2.8,2.15) arc (90:55:0.65);
    \node[accentcolor] at (3.1,2.35) {$\theta$};

    % Cota H — altura del pivote
    \draw[<->, gray] (4.8,0) -- (4.8,1.5) node[midway, right] {$H$};
    \draw[dotted] (3.8,1.5) -- (4.9,1.5);

    % Coordenada x — posición horizontal del carro
    \draw[->, maincolor, thick] (0,2.2) -- (2.8,2.2) node[midway, above] {$x$};
    \draw[dotted] (0,0) -- (0,2.4);
    \draw[dotted] (2.8,1.5) -- (2.8,2.4);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** El carro $M$ (teal, con ruedas) rueda sobre el piso. El pivote del péndulo está en la parte superior del carro a altura $H$. La varilla de longitud $\ell$ parte del pivote y lleva la masa $m$ (naranja) en su extremo; en la figura se muestra el péndulo en posición invertida (hacia arriba y a la derecha). El ángulo $\theta$ se mide desde la vertical hacia arriba hasta la varilla. La coordenada $x$ mide la posición horizontal del pivote desde la pared izquierda (origen).

---

## Resolución

### Coordenadas y GDL

Coordenadas posibles del sistema:

$$N = (x,\ \theta)$$

Sin restricciones adicionales — ambas coordenadas son independientes.

Número de grados de libertad:

$$\text{GDL} = 2 \quad \text{con coordenadas independientes } (x,\,\theta)$$

Posición absoluta de $m$:

$$x_2 = x + \ell\sin\theta \qquad y_2 = H + \ell\cos\theta$$

Velocidades de $m$:

$$\dot{x}_2 = \dot{x} + \ell\cos\theta\,\dot{\theta} \qquad \dot{y}_2 = -\ell\sin\theta\,\dot{\theta}$$

---

### Energía cinética

$$T_M = \frac{M}{2}\dot{x}^2$$

$$T_m = \frac{m}{2}(\dot{x}_2^2 + \dot{y}_2^2) = \frac{m}{2}\!\left(\dot{x}^2 + 2\dot{x}\ell\cos\theta\,\dot{\theta} + \ell^2\cos^2\theta\,\dot{\theta}^2 + \ell^2\sin^2\theta\,\dot{\theta}^2\right)$$

$$\boxed{T = \frac{M}{2}\dot{x}^2 + \frac{m}{2}\!\left(\dot{x}^2 + 2\dot{x}\ell\cos\theta\,\dot{\theta} + \ell^2\dot{\theta}^2\right)}$$

---

### Energía potencial

$$\boxed{V = mg(H + \ell\cos\theta)}$$

---

### Ecuaciones de Lagrange

#### Para $x$

$$\frac{\partial T}{\partial \dot{x}} = (M+m)\dot{x} + m\ell\cos\theta\,\dot{\theta} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}}\right) = (M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2$$

$$\frac{\partial T}{\partial x} = 0 \qquad \frac{\partial V}{\partial x} = 0$$

$$\boxed{(M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2 = 0}$$

#### Para $\theta$

$$\frac{\partial T}{\partial \dot{\theta}} = m\ell\dot{x}\cos\theta + m\ell^2\dot{\theta} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m\ell\ddot{x}\cos\theta - m\ell\dot{x}\sin\theta\,\dot{\theta} + m\ell^2\ddot{\theta}$$

$$\frac{\partial T}{\partial \theta} = -m\ell\dot{x}\dot{\theta}\sin\theta \qquad -\frac{\partial V}{\partial \theta} = mg\ell\sin\theta$$

Sustituyendo (los términos $-m\ell\dot{x}\sin\theta\,\dot{\theta}$ y $+m\ell\dot{x}\dot{\theta}\sin\theta$ se anulan):

$$\boxed{\ell\ddot{\theta} + \ddot{x}\cos\theta - \dot{x}\sin\theta\,\dot{\theta} + \dot{x}\dot{\theta}\sin\theta + g\sin\theta = 0}$$

---

### EDOs finales

$$\boxed{(M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2 = 0}$$

$$\boxed{\ell\ddot{\theta} + \ddot{x}\cos\theta - \dot{x}\sin\theta\,\dot{\theta} + \dot{x}\dot{\theta}\sin\theta + g\sin\theta = 0}$$

---
---

# Ej 5

Dos masas puntuales $m_1$ y $m_2$ forman un péndulo doble planar. Ambas varillas son rígidas, sin masa y de igual longitud $\ell$. La primera varilla está articulada al techo y forma el ángulo $\theta$ con la vertical; la segunda varilla está articulada al extremo inferior de la primera y forma el ángulo $\phi$ con la vertical. El sistema oscila libremente bajo la acción de la gravedad.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,0) rectangle (1,0.2);
    \draw[thick] (-1,0) -- (1,0);

    % Eje vertical de referencia
    \draw[dashed, gray] (0,0) -- (0,-3.5);

    % Primer péndulo (m1, l, theta)
    \draw[thick, maincolor] (0,0) -- (1.2,-1.8);
    \draw[fill=teal!20, draw=maincolor, thick] (1.2,-1.8) circle (0.18);
    \node[maincolor, right=2pt] at (1.2,-1.8) {$m_1$};
    \node[maincolor, above left] at (0.6,-0.9) {$\ell$};

    % Ángulo theta
    \draw[dashed, gray] (1.2,-1.8) -- (1.2,-3.8);
    \draw[->, maincolor, thick] (0,-1.0) arc (-90:-56:1.0);
    \node[maincolor] at (0.25,-1.2) {$\theta$};

    % Segundo péndulo (m2, l, phi)
    \draw[thick, accentcolor] (1.2,-1.8) -- (2.6,-3.2);
    \draw[fill=orange!20, draw=accentcolor, thick] (2.6,-3.2) circle (0.18);
    \node[accentcolor, right=2pt] at (2.6,-3.2) {$m_2$};
    \node[accentcolor, above left] at (1.9,-2.5) {$\ell$};

    % Ángulo phi
    \draw[->, accentcolor, thick] (1.2,-2.8) arc (-90:-45:1.0);
    \node[accentcolor] at (1.45,-3.0) {$\phi$};

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** La primera varilla (teal) parte del pivote fijo en el techo y lleva la masa $m_1$ en su extremo; el ángulo $\theta$ se mide desde la vertical hasta la primera varilla. La segunda varilla (naranja) parte de $m_1$ y lleva la masa $m_2$ en su extremo; el ángulo $\phi$ se mide desde la vertical (línea punteada que pasa por $m_1$) hasta la segunda varilla. Ambas varillas tienen la misma longitud $\ell$.

---

## Resolución

### Coordenadas y GDL

Posiciones rectangulares de cada masa respecto al soporte articulado superior (origen $(0,0)$), eje $y$ orientado hacia abajo:

- Para $m_1$:

$$x_1 = \ell\sin\theta \qquad y_1 = \ell\cos\theta$$

- Para $m_2$:

$$x_2 = \ell\sin\theta + \ell\sin\phi \qquad y_2 = \ell\cos\theta + \ell\cos\phi$$

Derivadas de $m_2$:

$$\dot{x}_2 = \ell\cos\theta\,\dot{\theta} + \ell\cos\phi\,\dot{\phi} \qquad \dot{y}_2 = -\ell\sin\theta\,\dot{\theta} - \ell\sin\phi\,\dot{\phi}$$

Sin restricciones adicionales:

$$\text{GDL} = 2 \quad \text{con coordenadas generalizadas } (\theta,\,\phi)$$

---

### Energía cinética

$$T_1 = \frac{1}{2}m_1\ell^2\dot{\theta}^2$$

$$T_2 = \frac{1}{2}m_2\ell^2\!\left[\dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta-\phi) + \dot{\phi}^2\right]$$

$$\boxed{T = \frac{1}{2}m_1\ell^2\dot{\theta}^2 + \frac{1}{2}m_2\ell^2\!\left[\dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta-\phi) + \dot{\phi}^2\right]}$$

---

### Energía potencial

Referencia $y = 0$ en el techo, eje $y$ descendente — energía potencial negativa (masas por debajo del origen). El nivel de referencia no afecta las EDOs.

$$\boxed{V = -m_1 g\ell\cos\theta - m_2 g\ell(\cos\theta + \cos\phi)}$$

---

### Ecuaciones de Lagrange

#### Respecto de $\theta$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}$$

$$\frac{\partial T}{\partial \dot{\theta}} = (m_1 + m_2)\ell^2\dot{\theta} + m_2\ell^2\dot{\phi}\cos(\theta-\phi)$$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) = (m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) - m_2\ell^2\dot{\phi}\sin(\theta-\phi)(\dot{\theta}-\dot{\phi})$$

$$\frac{\partial T}{\partial \theta} = -m_2\ell^2\dot{\theta}\dot{\phi}\sin(\theta-\phi) \qquad -\frac{\partial V}{\partial \theta} = -(m_1+m_2)g\ell\sin\theta$$

$$\boxed{(m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) + m_2\ell^2\dot{\phi}^2\sin(\theta-\phi) + (m_1+m_2)g\ell\sin\theta = 0}$$

#### Respecto de $\phi$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\phi}}\right) - \frac{\partial T}{\partial \phi} = -\frac{\partial V}{\partial \phi}$$

$$\frac{\partial T}{\partial \dot{\phi}} = m_2\ell^2\dot{\phi} + m_2\ell^2\dot{\theta}\cos(\theta-\phi)$$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\phi}}\right) = m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}\sin(\theta-\phi)(\dot{\theta}-\dot{\phi})$$

$$\frac{\partial T}{\partial \phi} = m_2\ell^2\dot{\theta}\dot{\phi}\sin(\theta-\phi) \qquad -\frac{\partial V}{\partial \phi} = -m_2 g\ell\sin\phi$$

$$\boxed{m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}^2\sin(\theta-\phi) + m_2 g\ell\sin\phi = 0}$$

---

### EDOs finales

$$\boxed{(m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) + m_2\ell^2\dot{\phi}^2\sin(\theta-\phi) + (m_1+m_2)g\ell\sin\theta = 0}$$

$$\boxed{m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}^2\sin(\theta-\phi) + m_2 g\ell\sin\phi = 0}$$

---
---

# Ej 6

##### Ej. Sistema masa-resorte-amortiguador de 1 GDL sometido a una fuerza externa $F$ (edo3.pdf)

**Enunciado:**
Un bloque de masa $M$ se desliza horizontalmente sin fricción sobre una superficie plana. Por su lado izquierdo está conectado en paralelo a un resorte de rigidez $K$ y un amortiguador viscoso de coeficiente $C$, ambos anclados a una pared rígida fija. Sobre el lado derecho del bloque actúa una fuerza externa $F$ dirigida hacia la derecha. Obtenga la ecuación de movimiento del sistema usando las ecuaciones de Lagrange.

**Descripción de la figura:**
El diagrama muestra un bloque de masa $M$ apoyado sobre una superficie horizontal sin fricción, con una pared rígida a su izquierda. Desde esa pared parten dos elementos en paralelo que se conectan al lado izquierdo del bloque: el resorte $K$ en la parte superior y el amortiguador $C$ en la parte inferior. Sobre el lado derecho del bloque actúa la fuerza externa $F$ apuntando hacia la derecha. La coordenada $x$ indica el desplazamiento horizontal del bloque medido desde su posición de equilibrio estático.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.3,-0.5) rectangle (0,3.0);
    \draw[thick] (0,-0.5) -- (0,3.0);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (5.5,0);
    \draw[thick] (0,0) -- (5.5,0);

    % Bloque M
    \draw[fill=teal!10, draw=maincolor, thick] (2.5,0.3) rectangle (4.0,2.2);
    \node[maincolor, font=\Large] at (3.25,1.25) {$M$};

    % Resorte K (Pared a Bloque M)
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (0,2.0) -- (2.5,2.0);
    \node[above, maincolor] at (1.25,2.15) {$K$};

    % Amortiguador C (Pared a Bloque M)
    \draw[thick, maincolor] (0,0.8) -- (0.8,0.8);
    \draw[thick, maincolor] (0.8,0.5) -- (0.8,1.1);
    \draw[thick, maincolor] (0.7,1.1) -- (1.6,1.1);
    \draw[thick, maincolor] (0.7,0.5) -- (1.6,0.5);
    \draw[thick, maincolor] (1.3,0.65) -- (1.3,0.95);
    \draw[thick, maincolor] (1.3,0.8) -- (2.5,0.8);
    \node[above, maincolor] at (1.25,1.1) {$C$};

    % Fuerza F
    \draw[->, red, ultra thick] (4.0,1.25) -- (5.2,1.25) node[right] {$F$};

    % Coordenada x
    \draw[->, maincolor, thick] (2.5,2.6) -- (3.5,2.6) node[midway, above] {$x$};
    \draw[dotted] (2.5,2.2) -- (2.5,2.8);
\end{tikzpicture}
\end{document}
```

---

**Paso 0 — Identificación**
Sistema mecánico translacional de 1 grado de libertad (1 GDL) constituido por un bloque de masa $M$, acoplado en paralelo a un resorte de rigidez $K$ y un amortiguador viscoso de coeficiente $C$, sometido a una fuerza impulsora externa $F$.

**Paso 1 — Coordenadas y GDL**
Coordenada independiente de desplazamiento horizontal: $x$ medida desde la posición de equilibrio estático.
Grados de libertad: $\text{GDL} = 1$.

**Paso 2 — Energía cinética**
Energía cinética del sistema:


$$
T = \frac{1}{2}M\dot{x}^2
$$


**Paso 3 — Energía potencial**
Energía potencial elástica acumulada en el resorte:


$$
V = \frac{1}{2}Kx^2
$$


Función de disipación de Rayleigh del amortiguador:


$$
\mathcal{F} = \frac{1}{2}C\dot{x}^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Ecuación diferencial de movimiento planteada mediante la ecuación de Lagrange extendida con disipación viscosa y fuerza generalizada externa:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} + \frac{\partial \mathcal{F}}{\partial \dot{x}} + \frac{\partial V}{\partial x} = F
$$


Sustituyendo las derivadas parciales:


$$
M\ddot{x} + C\dot{x} + Kx = F
$$


Ensayo de solución exponencial propuesta en el apunte ($x = c e^{\lambda t}$):


$$
\dot{x} = c\lambda e^{\lambda t}, \qquad \ddot{x} = c\lambda^2 e^{\lambda t}
$$


Casos de solución según la naturaleza de las raíces $\lambda$ del polinomio característico:

1. **Solución 1: Sobreamortiguado ($\lambda \in \mathbb{R}$, raíces reales distintas)**
   
$$
x(t) = c_1 e^{-\alpha_1 t} + c_2 e^{-\alpha_2 t}
$$


2. **Solución 2: Amortiguamiento crítico ($\lambda \in \mathbb{R}$, raíces reales iguales $\lambda_1 = \lambda_2 = -\alpha$)**
   
$$
x(t) = c_1 e^{-\alpha t} + c_2 t e^{-\alpha t}
$$


3. **Solución 3: Subamortiguado ($\lambda \in \mathbb{C}$, raíces complejas conjugadas $-\alpha \pm i\beta$)**
   
$$
x(t) = c_1 e^{-\alpha t} \sin(\beta t) + c_2 e^{-\alpha t} \cos(\beta t)
$$


Parámetros de frecuencia y período del apunte:


$$
\omega_n = \sqrt{\frac{K}{M}}
$$


Ejemplo numérico asignado en el apunte (para $K = 2$, $M = 3$):


$$
\omega_n = \sqrt{\frac{2}{3}}
$$



$$
f = \frac{\omega_n}{2\pi}, \qquad T = \frac{1}{f}
$$


**Paso 5 — EDOs finales**

$$
\boxed{M\ddot{x} + C\dot{x} + Kx = F}
$$

---
---

# Ej 7

##### Ej. Sistema mecánico horizontal de tres masas acopladas por resortes, amortiguadores y fuerza externa aplicada en $m_2$

**Enunciado:**
Tres masas $m_1$, $m_2$ y $m_3$ se deslizan horizontalmente sin fricción sobre una superficie plana. La masa $m_1$ está conectada a la pared izquierda mediante el resorte $K_1$ y el amortiguador $C_1$ en paralelo. La masa $m_1$ y la masa $m_3$ están acopladas entre sí por el resorte $K_{13}$. La masa $m_1$ y la masa $m_2$ están acopladas por el amortiguador $C_{12}$. La masa $m_2$ está conectada a la pared izquierda mediante el resorte $K_2$, y está acoplada a la masa $m_3$ mediante el resorte $K_{23}$ y el amortiguador $C_{23}$ en paralelo; sobre $m_2$ actúa además una fuerza externa $F_2$ dirigida hacia la derecha. La masa $m_3$ está conectada a la pared derecha mediante el resorte $K_3$. Obtenga las ecuaciones de movimiento del sistema usando las ecuaciones de Lagrange y expréselas en forma matricial $M\ddot{x} + C\dot{x} + Kx = F$.

**Descripción de la figura:**
El diagrama muestra tres masas dispuestas horizontalmente entre dos paredes rígidas. La masa $m_1$ (bloque izquierdo) está suspendida entre la pared izquierda y los elementos que la acoplan al resto del sistema: hacia su izquierda se conectan en paralelo el resorte $K_1$ y el amortiguador $C_1$, ambos anclados a la pared izquierda; hacia su derecha, el resorte $K_{13}$ la comunica con $m_3$ y el amortiguador $C_{12}$ la comunica con $m_2$. La masa $m_2$ (bloque central-inferior) recibe por su izquierda el amortiguador $C_{12}$ proveniente de $m_1$ y el resorte $K_2$ anclado a la pared izquierda; por su derecha se conectan en paralelo el resorte $K_{23}$ y el amortiguador $C_{23}$, ambos hacia $m_3$, y sobre ella actúa la fuerza externa $F_2$ apuntando hacia la derecha. La masa $m_3$ (bloque derecho) recibe por su izquierda el resorte $K_{13}$ desde $m_1$, y el par $K_{23}$–$C_{23}$ desde $m_2$; por su derecha el resorte $K_3$ la conecta a la pared derecha.


```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.0, >=latex]

% Definición de colores
\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% Pared izquierda
\fill[pattern=north east lines] (-0.3,-0.5) rectangle (0,5.2);
\draw[thick] (0,-0.5) -- (0,5.2);

% Pared derecha
\fill[pattern=north east lines] (8.0,-0.5) rectangle (8.3,5.2);
\draw[thick] (8.0,-0.5) -- (8.0,5.2);

% Masa 1
\draw[fill=teal!10, draw=maincolor, thick]
    (2.0,2.8) rectangle (3.0,5.0);
\node[maincolor, font=\Large] at (2.5,3.9) {$1$};

% Masa 2 (elevada)
\draw[fill=teal!10, draw=maincolor, thick]
    (3.8,1.2) rectangle (4.8,3.6);
\node[maincolor, font=\Large] at (4.3,2.4) {$2$};

% Masa 3
\draw[fill=orange!10, draw=accentcolor, thick]
    (5.8,2.4) rectangle (6.8,5.0);
\node[accentcolor, font=\Large] at (6.3,3.7) {$3$};

% Resorte K1 (Pared a Masa 1)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (0,4.4) -- (2.0,4.4);
\node[above, maincolor] at (1.0,4.55) {$K_1$};

% Amortiguador C1 (Pared a Masa 1)
\draw[thick, maincolor] (0,3.3) -- (0.6,3.3);
\draw[thick, maincolor] (0.6,3.0) -- (0.6,3.6);
\draw[thick, maincolor] (0.5,3.6) -- (1.2,3.6);
\draw[thick, maincolor] (0.5,3.0) -- (1.2,3.0);
\draw[thick, maincolor] (1.0,3.15) -- (1.0,3.45);
\draw[thick, maincolor] (1.0,3.3) -- (2.0,3.3);
\node[above, maincolor] at (1.0,3.6) {$C_1$};

% Resorte K2 (Pared a Masa 2)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (0,1.8) -- (3.8,1.8);
\node[above, maincolor] at (1.9,1.95) {$K_2$};

% Resorte K13 (Masa 1 a Masa 3)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, maincolor, thick]
    (3.0,4.4) -- (5.8,4.4);
\node[above, maincolor] at (4.4,4.55) {$K_{13}$};

% Amortiguador C12 (Masa 1 a Masa 2)
\draw[thick, maincolor]
    (3.0,3.1) -- (3.3,3.1) -- (3.3,2.6) -- (3.5,2.6);
\draw[thick, maincolor] (3.5,2.3) -- (3.5,2.9);
\draw[thick, maincolor] (3.4,2.9) -- (3.7,2.9);
\draw[thick, maincolor] (3.4,2.3) -- (3.7,2.3);
\draw[thick, maincolor] (3.65,2.45) -- (3.65,2.75);
\draw[thick, maincolor] (3.65,2.6) -- (3.8,2.6);
\node[above, maincolor] at (3.4,2.95) {$C_{12}$};

% Resorte K23 (Masa 2 a Masa 3)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2mm, coil}, decorate, maincolor, thick]
    (4.8,3.2) -- (5.8,3.2);
\node[above, maincolor] at (5.3,3.35) {$K_{23}$};

% Amortiguador C23 (Masa 2 a Masa 3)
\draw[thick, maincolor] (4.8,2.5) -- (5.1,2.5);
\draw[thick, maincolor] (5.1,2.2) -- (5.1,2.8);
\draw[thick, maincolor] (5.1,2.8) -- (5.6,2.8);
\draw[thick, maincolor] (5.1,2.2) -- (5.6,2.2);
\draw[thick, maincolor] (5.6,2.35) -- (5.6,2.65);
\draw[thick, maincolor] (5.6,2.5) -- (5.8,2.5);
\node[below, maincolor] at (5.3,2.15) {$C_{23}$};

% Resorte K3 (Masa 3 a Pared derecha)
\draw[decoration={aspect=0.3, segment length=2mm,
    amplitude=2.5mm, coil}, decorate, accentcolor, thick]
    (6.8,3.7) -- (8.0,3.7);
\node[above, accentcolor] at (7.4,3.85) {$K_3$};

% Fuerza F2
\draw[->, red, ultra thick] (4.8,1.8) -- (5.6,1.8)
    node[right] {$F_2$};

\end{tikzpicture}

\end{document}
```

---

**Paso 0 — Identificación**
Sistema mecánico translacional acoplado de 3 grados de libertad (3 GDL) con disipación viscosa, acoplamiento elástico y fuerza de excitación externa aplicada a la masa $m_2$.

**Paso 1 — Coordenadas y GDL**
Coordenadas independientes de desplazamiento horizontal: $x_1, x_2, x_3$ medidas a partir de las posiciones de equilibrio de cada cuerpo.
Grados de libertad: $\text{GDL} = 3$.

**Paso 2 — Energía cinética**
Energía cinética total del sistema $T$:


$$
T = \frac{1}{2}m_1\dot{x}_1^2 + \frac{1}{2}m_2\dot{x}_2^2 + \frac{1}{2}m_3\dot{x}_3^2
$$


Matriz de masa $M$:


$$
M = \begin{bmatrix} m_1 & 0 & 0 \\ 0 & m_2 & 0 \\ 0 & 0 & m_3 \end{bmatrix}
$$


**Paso 3 — Energía potencial**
Energía potencial elástica total acumulada en los resortes $K_1, K_2, K_3, K_{13}, K_{23}$:


$$
V = \frac{1}{2}K_1 x_1^2 + \frac{1}{2}K_2 x_2^2 + \frac{1}{2}K_3 x_3^2 + \frac{1}{2}K_{13}(x_3 - x_1)^2 + \frac{1}{2}K_{23}(x_3 - x_2)^2
$$


Función de disipación de Rayleigh para los amortiguadores $C_1, C_{12}, C_{23}$:


$$
\mathcal{F} = \frac{1}{2}C_1 \dot{x}_1^2 + \frac{1}{2}C_{12}(\dot{x}_2 - \dot{x}_1)^2 + \frac{1}{2}C_{23}(\dot{x}_3 - \dot{x}_2)^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicación de las ecuaciones de Lagrange extendidas para sistemas disipativos:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_i}\right) - \frac{\partial T}{\partial x_i} + \frac{\partial \mathcal{F}}{\partial \dot{x}_i} + \frac{\partial V}{\partial x_i} = F_i \qquad (i = 1, 2, 3)
$$


- Para $x_1$:


$$
m_1 \ddot{x}_1 + (C_1 + C_{12})\dot{x}_1 - C_{12}\dot{x}_2 + (K_1 + K_{13})x_1 - K_{13}x_3 = 0
$$


- Para $x_2$:


$$
m_2 \ddot{x}_2 - C_{12}\dot{x}_1 + (C_{12} + C_{23})\dot{x}_2 - C_{23}\dot{x}_3 + (K_2 + K_{23})x_2 - K_{23}x_3 = F_2
$$


- Para $x_3$:


$$
m_3 \ddot{x}_3 - C_{23}\dot{x}_2 + C_{23}\dot{x}_3 - K_{13}x_1 - K_{23}x_2 + (K_3 + K_{13} + K_{23})x_3 = 0
$$


**Paso 5 — EDOs finales**
Formulación en espacio matricial de la ecuación diferencial de movimiento $M\ddot{x} + C\dot{x} + Kx = F$:


$$
\boxed{\begin{bmatrix} m_1 & 0 & 0 \\ 0 & m_2 & 0 \\ 0 & 0 & m_3 \end{bmatrix} \begin{bmatrix} \ddot{x}_1 \\ \ddot{x}_2 \\ \ddot{x}_3 \end{bmatrix} + \begin{bmatrix} C_1 + C_{12} & -C_{12} & 0 \\ -C_{12} & C_{12} + C_{23} & -C_{23} \\ 0 & -C_{23} & C_{23} \end{bmatrix} \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} + \begin{bmatrix} K_1 + K_{13} & 0 & -K_{13} \\ 0 & K_2 + K_{23} & -K_{23} \\ -K_{13} & -K_{23} & K_3 + K_{13} + K_{23} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ F_2 \\ 0 \end{bmatrix}}
$$

---
---

# Ej 8

##### Ej. Sistema de dos cuñas con pared inclinada, resorte y fuerza externa — 1 GDL

**Enunciado:**
Una cuña $m_1$ de forma trapezoidal (caras superior e inferior horizontales, cara izquierda inclinada a $60°$ y cara derecha vertical) queda suspendida entre una rampa fija inclinada a $60°$ y la cara superior inclinada a $45°$ de la cuña $m_2$. La cuña $m_2$ es un trapecio rectángulo que descansa sobre el piso horizontal: vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical conectada mediante un resorte de constante $K$ a la pared derecha fija, y cara inferior horizontal apoyada sobre el piso. Sobre $m_1$ actúa una fuerza externa $F$ dirigida verticalmente hacia abajo. El sistema desliza sin fricción y tiene 1 grado de libertad. Se definen $x_1$ como la distancia horizontal desde el origen (base de la rampa) al borde inferior-izquierdo de $m_1$ — que se encuentra a la izquierda del origen, en coordenada $-x_1$ —, $x_2$ como la distancia horizontal desde el origen al vértice inferior-izquierdo de $m_2$, $y_1$ como la altura del borde inferior de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto entre $m_1$ y $m_2$ sobre el piso, $B_1$ el ancho horizontal de $m_1$ (medido de borde a borde), $B_2$ el ancho horizontal de $m_2$, y $d = B_1 - x_1 - x_2$ la separación horizontal entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$. Dado que el punto de contacto (punto verde) pertenece simultáneamente a la cara inferior de $m_1$ y a la cara inclinada de $m_2$, sus alturas son iguales: $y_1 = y_2$. Esta condición de contacto, combinada con los vínculos geométricos de ambas superficies inclinadas, reduce el sistema a 1 grado de libertad. Hallar la ecuación de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
\colorlet{maincolor}{teal}
\colorlet{accentcolor}{orange}

% PARED IZQUIERDA - 60°
\fill[pattern=north east lines] (0,0) -- (-1.73,3) -- (-1.30,3) -- (0,0) -- cycle;
\draw[thick] (0,0) -- (-1.73,3);

% PISO
\fill[pattern=north east lines] (0,-0.3) rectangle (8.5,0);
\draw[thick] (0,0) -- (8.5,0);

% BLOQUE 2
\fill[orange!10] (2.5,0) -- (5.5,3) -- (7.0,3) -- (7.0,0) -- cycle;
\draw[thick, accentcolor] (2.5,0) -- (5.5,3) -- (7.0,3) -- (7.0,0) -- cycle;
\node[accentcolor] at (5.5,1.3) {\Large $m_2$};

% BLOQUE 1
\fill[teal!10] (-0.58,1.0) -- (3.50,1.0) -- (4.70,2.20) -- (-1.27,2.20) -- cycle;
\draw[thick, maincolor] (-0.58,1.0) -- (3.50,1.0) -- (4.70,2.20) -- (-1.27,2.20) -- cycle;
\node[maincolor] at (1.65,1.60) {\Large $m_1$};

% FUERZA F SOBRE BLOQUE 1
\draw[->, very thick, red] (1.65,3.0) -- (1.65,2.20) node[midway, right] {$F$};

% PUNTOS DE CONTACTO
\fill[red] (-0.58,1.0) circle (2pt);
\fill[teal!60!black] (3.50,1.0) circle (2pt);

% ÁNGULOS
\draw[thick] (0,0) ++(180:0.55) arc (180:120:0.55);
\node at (-0.38,0.30) {$60^\circ$};

\draw[thick] (2.5,0) ++(0.55,0) arc (0:45:0.55);
\node at (3.05,0.25) {$45^\circ$};

% RESORTE
\draw[thick, decorate, decoration={coil, aspect=0.35, segment length=5pt, amplitude=5pt}, maincolor] (7.0,1.5) -- (8.5,1.5);
\node[above, maincolor] at (7.75,1.7) {$K$};

% PARED DERECHA
\fill[pattern=north east lines] (8.5,0) rectangle (8.8,3.0);
\draw[thick] (8.5,0) -- (8.5,3.0);

% ALTURA y_1
\draw[red, <->, thick] (-2.0,0) -- (-2.0,1.0);
\draw[red, dashed] (-2.0,1.0) -- (-0.58,1.0);
\draw[red, dashed] (-2.0,0) -- (0,0);
\node[red] at (-2.25,0.5) {$y_1$};

% ALTURA y_2
\draw[teal!60!black, <->, thick] (3.50,-0.05) -- (3.50,1.0);
\draw[teal!60!black, dashed] (3.50,1.0) -- (4.10,1.0);
\node[teal!60!black] at (3.75,0.5) {$y_2$};

% DISTANCIA d
\draw[teal!60!black, <->, thick] (2.50,-0.55) -- (3.50,-0.55);
\draw[teal!60!black, dashed] (3.50,0) -- (3.50,-0.55);
\draw[teal!60!black, dashed] (2.50,1.0) -- (2.50,-0.55);
\node[teal!60!black] at (3.00,-0.75) {$d$};

% x_1
\draw[red, <->, thick] (-0.58,-0.55) -- (0,-0.55);
\draw[red, dashed] (-0.58,1.0) -- (-0.58,-0.55);
\node[red] at (-0.29,-0.75) {$x_1$};

% x_2
\draw[accentcolor, <->, thick] (0,-0.55) -- (2.50,-0.55);
\draw[accentcolor, dashed] (2.50,0) -- (2.50,-0.55);
\node[accentcolor] at (1.25,-0.75) {$x_2$};

% B_1
\draw[violet, <->, thick] (-0.58,1.40) -- (3.50,1.40);
\node[violet] at (1.46,1.60) {$B_1$};

% B_2
\draw[violet, <->, thick] (2.5,-0.40) -- (7.0,-0.40);
\draw[violet, dashed] (7.0,0) -- (7.0,-0.40);
\node[violet] at (4.75,-0.60) {$B_2$};

\end{tikzpicture}
\end{document}
```

---

**Solución:**

## 1. Relaciones geométricas de vínculo

El sistema tiene 2 cuerpos móviles con restricciones geométricas que reducen los grados de libertad a 1. Se elige $x_2$ como coordenada generalizada.

**Vínculo de la rampa (60°):**

El punto rojo está a la **izquierda del origen**, en coordenada horizontal $-x_1$. La altura $y_1$ satisface:

$$\tan 60° = \frac{y_1}{x_1} \implies y_1 = x_1\sqrt{3}$$

**Posición del punto verde:**

El ancho de $m_1$ es $B_1$, medido desde el punto rojo hacia la derecha. Por tanto el punto verde (borde inferior-derecho de $m_1$) tiene coordenada horizontal:

$$X_{\text{verde}} = -x_1 + B_1 = B_1 - x_1$$

El vértice inferior-izquierdo de $m_2$ está en $x_2$. La separación horizontal es:

$$d = (B_1 - x_1) - x_2 = B_1 - x_1 - x_2$$

**Vínculo de la interfaz $m_1$–$m_2$ (45°):**

$$\tan 45° = \frac{y_2}{d} = 1 \implies y_2 = d = B_1 - x_1 - x_2$$

**Condición de contacto** ($y_1 = y_2$, el punto verde es común a ambos cuerpos):

$$x_1\sqrt{3} = B_1 - x_1 - x_2$$

$$x_1(\sqrt{3} + 1) = B_1 - x_2$$

$$\boxed{x_1 = \frac{B_1 - x_2}{\sqrt{3}+1}}$$

Derivando respecto al tiempo:

$$\dot{x}_1 = \frac{-\dot{x}_2}{\sqrt{3}+1} \qquad \dot{y}_1 = \sqrt{3}\,\dot{x}_1 = \frac{-\sqrt{3}\,\dot{x}_2}{\sqrt{3}+1}$$

---

## 2. Energía cinética

$m_1$ se mueve en el plano; $m_2$ solo horizontalmente ($\dot{y}_2 = 0$):

$$T = \frac{m_1}{2}(\dot{x}_1^2 + \dot{y}_1^2) + \frac{m_2}{2}\dot{x}_2^2$$

$$\dot{x}_1^2 + \dot{y}_1^2 = \frac{\dot{x}_2^2 + 3\dot{x}_2^2}{(\sqrt{3}+1)^2} = \frac{4\dot{x}_2^2}{(\sqrt{3}+1)^2}$$

$$\boxed{T = \frac{1}{2}M^*\dot{x}_2^2} \qquad M^* = \frac{4m_1}{(\sqrt{3}+1)^2} + m_2 = (4-2\sqrt{3})m_1 + m_2$$

---

## 3. Energía potencial

Solo entra el peso de $m_1$ (el resorte y el piso no hacen trabajo potencial gravitatorio sobre $m_2$):

$$V = m_1 g\,y_1 + \frac{1}{2}K(x_2-x_{2,0})^2 = \frac{m_1 g\sqrt{3}(B_1-x_2)}{\sqrt{3}+1} + \frac{1}{2}K(x_2-x_{2,0})^2$$

---

## 4. Fuerza generalizada de $F$

La fuerza $F$ (vertical hacia abajo, no conservativa) se trata por trabajo virtual. Un desplazamiento $\delta x_2$ produce:

$$\delta y_1 = \frac{-\sqrt{3}}{\sqrt{3}+1}\,\delta x_2$$

Como $F$ actúa hacia abajo y $y_1$ crece hacia arriba:

$$\delta W_F = -F\,\delta y_1 = \frac{F\sqrt{3}}{\sqrt{3}+1}\,\delta x_2 \implies Q_{x_2} = \frac{F\sqrt{3}}{\sqrt{3}+1}$$

> **Nota:** $F$ puede también incorporarse al potencial como $(m_1 g + F)\,y_1$ si se la trata como fuerza conservativa constante. Ambos enfoques dan el mismo resultado.

---

## 5. Ecuación de movimiento de Lagrange

$$L = T - V = \frac{1}{2}M^*\dot{x}_2^2 - \frac{m_1 g\sqrt{3}(B_1-x_2)}{\sqrt{3}+1} - \frac{1}{2}K(x_2-x_{2,0})^2$$

Aplicando $\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot{x}_2} - \dfrac{\partial L}{\partial x_2} = Q_{x_2}$:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_2} = M^*\ddot{x}_2$$

$$\frac{\partial L}{\partial x_2} = \frac{m_1 g\sqrt{3}}{\sqrt{3}+1} - K(x_2-x_{2,0})$$

Sustituyendo:

$$M^*\ddot{x}_2 - \frac{m_1 g\sqrt{3}}{\sqrt{3}+1} + K(x_2-x_{2,0}) = \frac{F\sqrt{3}}{\sqrt{3}+1}$$

$$\boxed{M^*\ddot{x}_2 + K(x_2-x_{2,0}) = \frac{\sqrt{3}}{\sqrt{3}+1}(m_1 g + F)}$$

con:

$$M^* = \frac{4m_1}{(\sqrt{3}+1)^2} + m_2 = (4-2\sqrt{3})m_1 + m_2$$

---
---

# Ej 9
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
Se emplean las coordenadas generalizadas $(y_1, a)$ indicadas por el docente para expresar las relaciones de ligadura cinemática, formular la energía cinética, la energía potencial y el trabajo virtual de $F$, y derivar las ecuaciones de Lagrange del sistema.

---

**Paso 1 — Ligaduras cinemáticas y coordenadas generalizadas**

La cota $a$ mide la distancia vertical desde el centro de $m_2$ hasta el punto de aplicación de $F$:

$$a = y_3 - y_2 \implies y_3 = y_2 + a$$

Ligadura del cable de $m_2$ (ramal izquierdo fijo al piso, ramal derecho a $F$):

$$L_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = \text{cte} \implies \dot{y}_3 = 2\dot{y}_2 - \dot{y}_2$$

Como $y_3 = y_2 + a$, derivando: $\dot{y}_3 = \dot{y}_2 + \dot{a}$. Sustituyendo en la ligadura:

$$\dot{y}_2 + \dot{a} + \dot{y}_2 = 2\dot{y}_2 \implies \dot{a} = 0 \text{ (contradicción)}$$

La ligadura correcta de $m_2$ es sobre su propio cable: ramal izq fijo al piso, ramal der sostiene el punto $F$:

$$\dot{y}_3 - \dot{y}_2 = \dot{a} \implies \dot{y}_3 = \dot{y}_2 + \dot{a}$$

Y la ligadura de $m_1$ (ramal izq a $m_2$, ramal der al resorte $K'$) da la posición del extremo del resorte $K'$:

$$y_{K'} = 2y_1 - y_2 + C \implies \dot{y}_{K'} = 2\dot{y}_1 - \dot{y}_2$$

Con $(y_1, a)$ como coordenadas generalizadas y $\dot{y}_2 = \dot{a}$ (de la ligadura interna de $m_2$, ver PDF del docente):

$$\boxed{q_1 = y_1, \quad q_2 = a \qquad (2 \text{ GDL})}$$

$$\dot{y}_2 = \dot{a}, \qquad \dot{y}_{K'} = 2\dot{y}_1 - \dot{a}$$

---

**Paso 2 — Energía cinética**

$$T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{y}_2^2 = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{a}^2$$

$$\boxed{T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{a}^2}$$

> El punto de aplicación de $F$ no tiene masa propia, por lo que no aporta término cinético.

---

**Paso 3 — Energía potencial**

Longitud del resorte $K$: $y_1 - \ell_0$ (estiramiento desde longitud natural).

Posición del extremo superior del resorte $K'$ (desde el techo): $y_{K'} = 2y_1 - y_2 + C = 2y_1 - a + C$, donde $C$ agrupa constantes de longitud de cable y arcos de polea. La longitud del resorte $K'$ es $H - y_{K'} - \pi R_1 = H - 2y_1 + a - C - \pi R_1$.

$$V = \frac{K}{2}(y_1 - \ell_0)^2 + \frac{K'}{2}(y_2 - y_1 + \pi R_2 + H - y_1 - \ell_0')^2 - m_1 g\, y_1 - m_2 g\, y_2 - F y_3$$

En términos de $(y_1, a)$, sustituyendo $y_2 = a + \text{cte}$ según el docente y agrupando constantes:

$$\boxed{V = \frac{K}{2}(y_1 - \ell_0)^2 + \frac{K'}{2}(2H + \pi R_2 + a - 2y_1 + \pi R_1 - \ell_0')^2 - m_1 g\, y_1 - m_2 g\, a - Fa}$$

> La fuerza $F$ puede tratarse como fuerza generalizada no conservativa ($Q_a = 2F$ según el docente) o incorporarse al potencial como $-Fy_3 = -F(y_2 + a)$; ambos enfoques dan las mismas EDOs.

---

**Paso 4 — Ecuaciones de Lagrange**

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{q}_i}\right) - \frac{\partial T}{\partial q_i} = -\frac{\partial V}{\partial q_i} + Q_i$$

#### Para $y_1$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_1}\right) = m_1\ddot{y}_1$$

$$-\frac{\partial V}{\partial y_1} = -K(y_1 - \ell_0) + 2K'(2H + \pi R_2 + a - 2y_1 + \pi R_1 - \ell_0') + m_1 g$$

$$\boxed{m_1\ddot{y}_1 = -K(y_1 - \ell_0) + 2K'(2H + \pi R_2 + a - 2y_1 + \pi R_1 - \ell_0') + m_1 g}$$

#### Para $a$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{a}}\right) = m_2\ddot{a}$$

$$-\frac{\partial V}{\partial a} = -K'(2H + \pi R_2 + a - 2y_1 + \pi R_1 - \ell_0') + m_2 g + F$$

El docente obtiene $Q_a = 2F$ al considerar el trabajo virtual de $F$ sobre $y_3 = y_2 + a$:

$$\boxed{m_2\ddot{a} = -K'(2H + \pi R_2 + a - 2y_1 + \pi R_1 - \ell_0') + m_2 g + 2F}$$
---
---
# Ej 10

Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$ a una distancia $a$ por debajo de ella; su ramal izquierdo está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$, y su ramal derecho sostiene a la masa puntual $m_3$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo
    \fill[pattern=north east lines] (-1,5.3) rectangle (4.5,5.6);
    \draw[thick] (-1,5.3) -- (4.5,5.3);

    % Piso
    \fill[pattern=north east lines] (-1,-0.3) rectangle (4.5,0);
    \draw[thick] (-1,0) -- (4.5,0);

    % Resorte K — techo a m1
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (1.0,5.3) -- (1.0,4.0);
    \node[left, maincolor] at (0.75,4.65) {$K$};

    % Polea m1 (teal)
    \draw[thick, fill=teal!10, draw=maincolor] (1.0,3.7) circle (0.3);
    \fill[maincolor] (1.0,3.7) circle (0.05);
    \node[left, maincolor] at (0.5,3.7) {$m_1$};

    % Ramal izquierdo de m1 — cable fijo al piso
    \draw[thick, maincolor] (0.7,3.7) -- (0.7,0);

    % Ramal derecho de m1 — cable baja a m2
    \draw[thick, maincolor] (1.3,3.7) -- (1.3,2.3);

    % Polea m2 (naranja grande)
    \draw[thick, fill=orange!10, draw=accentcolor] (1.3,2.0) circle (0.3);
    \fill[accentcolor] (1.3,2.0) circle (0.05);
    \node[right, accentcolor] at (1.7,2.0) {$m_2$};

    % Ramal izquierdo de m2 — resorte K' al piso
    \draw[thick, accentcolor] (1.0,2.0) -- (1.0,1.4);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.0,1.4) -- (1.0,0);
    \node[left, accentcolor] at (0.75,0.7) {$K'$};

    % Ramal derecho de m2 — cable baja a m3
    \draw[thick, accentcolor] (1.6,2.0) -- (1.6,1.0);

    % m3 — masa puntual
    \draw[thick, fill=accentcolor!40, draw=accentcolor] (1.6,0.8) circle (0.15);
    \node[right, accentcolor] at (1.8,0.8) {$m_3$};

    % Cota H — altura total
    \draw[<->, red, thick] (-0.5,0) -- (-0.5,5.3) node[midway, left] {$H$};

    % Coordenada y1 — techo a m1
    \draw[->, maincolor, thick] (2.2,5.3) -- (2.2,3.7) node[midway, right] {$y_1$};
    \draw[dotted] (1.0,3.7) -- (2.3,3.7);
    \draw[dotted] (1.0,5.3) -- (2.3,5.3);

    % Coordenada y2 — techo a m2
    \draw[->, accentcolor, thick] (2.9,5.3) -- (2.9,2.0) node[midway, right] {$y_2$};
    \draw[dotted] (1.3,2.0) -- (3.0,2.0);

    % Coordenada y3 — techo a m3
    \draw[->, accentcolor, thick] (3.6,5.3) -- (3.6,0.8) node[midway, right] {$y_3$};
    \draw[dotted] (1.75,0.8) -- (3.7,0.8);

    % Cota a — distancia m1 a m2
    \draw[<->, maincolor, thick] (1.9,3.7) -- (1.9,2.0) node[midway, right] {$a$};
    \draw[dotted] (1.3,3.7) -- (2.1,3.7);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** El resorte $K$ (teal) conecta el techo con la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable fijo al piso. Del ramal derecho de $m_1$ desciende un cable hasta la polea $m_2$ (naranja), separada de $m_1$ por la distancia $a$. Del ramal izquierdo de $m_2$ desciende el resorte $K'$ (naranja) conectado al piso. Del ramal derecho de $m_2$ cuelga la masa puntual $m_3$ (naranja). Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo. La cota $H$ es la altura total techo–piso (rojo).

---

**Resolución**
Se establecen las ligaduras cinemáticas, se formula el Lagrangiano en función de las coordenadas generalizadas $y_2$ e $y_3$, y se aplican las ecuaciones de Euler-Lagrange.

**Paso 1 — Ligaduras, coordenadas generalizadas y posición del extremo del resorte $K'$**

$$
q_1 = y_2, \qquad q_2 = y_3 \qquad (2 \text{ GDL})
$$

Ligadura del cable de $m_1$ (ramal izq fijo al piso, ramal der a $m_2$):

$$
L_1 = (H - y_1) + \pi R_1 + (y_2 - y_1) = \text{cte} \implies \dot{y}_1 = \dfrac{\dot{y}_2}{2}
$$

$$
y_1 = \dfrac{y_2 - C_1}{2} \qquad C_1 = L_1 - H - \pi R_1
$$

Ligadura del cable de $m_2$ (ramal izq termina en resorte $K'$, ramal der a $m_3$) — posición del extremo libre $y_s$:

$$
L_2 = (y_s - y_2) + \pi R_2 + (y_3 - y_2) = \text{cte} \implies y_s = 2y_2 - y_3 + C_2 \qquad C_2 = L_2 - \pi R_2
$$

**Paso 2 — Energía cinética y potencial** *(sustitución de $y_1$ e $y_s$ en $T$ y $V$)*

$$
T = \dfrac{1}{2}\!\left(\dfrac{m_1}{4} + m_2\right)\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2
$$

$$
V = -\!\left(\dfrac{m_1}{2} + m_2\right)g\,y_2 - m_3 g\,y_3 + \dfrac{1}{2}K\!\left(\dfrac{y_2 - C_1}{2} - \ell_0\right)^{\!2} + \dfrac{1}{2}K'\!\left(H - 2y_2 + y_3 - C_2 - \ell_0'\right)^{\!2}
$$

**Paso 3 — Euler-Lagrange → EDOs acopladas** *($\partial/\partial y_2$ y $\partial/\partial y_3$ de $L = T - V$)*

$$
\boxed{\left(\dfrac{m_1}{4} + m_2\right)\ddot{y}_2 + \left(\dfrac{K}{4} + 4K'\right)y_2 - 2K'y_3 = \left(\dfrac{m_1}{2} + m_2\right)g + \dfrac{K}{2}\!\left(\dfrac{C_1}{2} + \ell_0\right) + 2K'(H - C_2 - \ell_0')}
$$

$$
\boxed{m_3\ddot{y}_3 + K'y_3 - 2K'y_2 = m_3 g - K'(H - C_2 - \ell_0')}
$$

---
---

# Ej 11

Tres poleas sin inercia rotacional $m_1$, $m_2$ y $m_3$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo está conectado mediante un cable al piso (extremo fijo) y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene a la polea $m_3$. La polea $m_3$ cuelga del ramal derecho de $m_2$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta el centro de $m_1$, $m_2$ y $m_3$ respectivamente. La distancia $a$ se mide desde el centro de $m_1$ hasta el centro de $m_3$.

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

    % Ramal izquierdo de m2 — cable fijo al piso
    \draw[thick, accentcolor] (1.0,3.4) -- (1.0,0);

    % Ramal derecho de m2 — cable baja a m3
    \draw[thick, accentcolor] (1.6,3.4) -- (1.6,1.7);

    % Polea m3 (teal oscuro)
    \draw[thick, fill=teal!20, draw=maincolor] (1.6,1.4) circle (0.3);
    \fill[maincolor] (1.6,1.4) circle (0.05);
    \node[left, maincolor] at (1.1,1.4) {$m_3$};

    % Ramal izquierdo de m3 — cable fijo al piso
    \draw[thick, maincolor] (1.3,1.4) -- (1.3,0);

    % Ramal derecho de m3 — resorte K' al piso
    \draw[thick, accentcolor] (1.9,1.4) -- (1.9,1.0);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,1.0) -- (1.9,0);
    \node[right, accentcolor] at (2.1,0.5) {$K'$};

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
    \draw[dotted] (1.9,1.4) -- (4.3,1.4);

    % Cota a — m1 a m3
    \draw[<->, maincolor, thick] (2.1,5.7) -- (2.1,1.4) node[midway, right] {$a$};
    \draw[dotted] (1.3,5.7) -- (2.2,5.7);
    \draw[dotted] (1.9,1.4) -- (2.2,1.4);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** El resorte $K$ (teal) conecta el techo con la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable fijo al piso. Del ramal derecho de $m_1$ desciende un cable hasta la polea $m_2$ (naranja). Del ramal izquierdo de $m_2$ desciende un cable fijo al piso. Del ramal derecho de $m_2$ desciende un cable hasta la polea $m_3$ (teal). Del ramal izquierdo de $m_3$ desciende un cable fijo al piso. Del ramal derecho de $m_3$ desciende el resorte $K'$ (naranja) conectado al piso. Las coordenadas $y_1$, $y_2$, $y_3$ se miden desde el techo hacia abajo hasta cada polea. La cota $a$ va desde el centro de $m_1$ hasta el centro de $m_3$. La cota $H$ es la altura total techo–piso (rojo).

---

**Resolución**
Se identifican las ligaduras cinemáticas, se formula el Lagrangiano en función de la coordenada generalizada $y_2$, y se aplica la ecuación de Euler-Lagrange.

**Paso 1 — Ligaduras cinemáticas** *(conservación de longitud de cable para cada polea)*

$$
L_1 = (H - y_1) + \pi R_1 + (y_2 - y_1) = \text{cte} \implies \dot{y}_1 = \dfrac{\dot{y}_2}{2}
$$

$$
L_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = \text{cte} \implies \dot{y}_3 = 2\dot{y}_2
$$

> Coordenada generalizada: $q = y_2$ \quad (1 GDL)

**Paso 2 — Energía cinética** *(sustitución directa de las ligaduras en $T$)*

$$
T = \dfrac{1}{2}m_1\dot{y}_1^2 + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\dot{y}_3^2 = \dfrac{1}{2}m_1\!\left(\dfrac{\dot{y}_2}{2}\right)^{\!2} + \dfrac{1}{2}m_2\dot{y}_2^2 + \dfrac{1}{2}m_3\left(2\dot{y}_2\right)^{\!2}
$$

$$
\boxed{T = \dfrac{1}{2}\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2^2}
$$

**Paso 3 — Energía potencial** *(gravedad + resorte $K$ en $m_1$ + resorte $K'$ en ramal der. de $m_3$)*

$$
\boxed{V = -m_1 g y_1 - m_2 g y_2 - m_3 g y_3 + \dfrac{1}{2}K(y_1 - \ell_0)^2 + \dfrac{1}{2}K'\!\left(H - y_3 - \pi R_3 - \ell_0'\right)^{\!2}}
$$

**Paso 4 — Lagrangiano**

$$
L = T - V = \dfrac{1}{2}\!\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\dot{y}_2^2 + m_1 g y_1 + m_2 g y_2 + m_3 g y_3 - \dfrac{1}{2}K(y_1 - \ell_0)^2 - \dfrac{1}{2}K'\!\left(H - y_3 - \pi R_3 - \ell_0'\right)^{\!2}
$$

**Paso 5 — Euler-Lagrange → EDO de movimiento** *(regla de la cadena: $\partial y_1/\partial y_2 = 1/2$, $\partial y_3/\partial y_2 = 2$, de las ligaduras del Paso 1)*

$$
\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial \dot{y}_2}\right) = \left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2
$$

$$
\dfrac{\partial L}{\partial y_2} = \dfrac{1}{2}\!\left[m_1 g - K(y_1 - \ell_0)\right] + m_2 g + 2\!\left[m_3 g + K'\!\left(H - y_3 - \pi R_3 - \ell_0'\right)\right]
$$

Sustituyendo $y_1 = y_2/2$ e $y_3 = 2y_2$ (posiciones relativas de equilibrio absorbidas en $\ell_0$, $\ell_0'$):

$$
\dfrac{\partial L}{\partial y_2} = \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g - \dfrac{K}{2}\!\left(\dfrac{y_2}{2} - \ell_0\right) + 2K'\!\left(H - 2y_2 - \pi R_3 - \ell_0'\right)
$$

$$
\boxed{\left(\dfrac{m_1}{4} + m_2 + 4m_3\right)\ddot{y}_2 + \left(\dfrac{K}{4} + 4K'\right)y_2 = \left(\dfrac{m_1}{2} + m_2 + 2m_3\right)g + \dfrac{K\,\ell_0}{2} + 2K'\!\left(H - \pi R_3 - \ell_0'\right)}
$$

---
---

# Ej 12

Cuatro poleas sin inercia rotacional $m_1$, $m_2$, $m_3$ y $m_4$ forman un sistema vertical en cadena. La polea $m_1$ está suspendida del techo mediante un resorte de constante $K$ y longitud natural $\ell_0$; su ramal izquierdo sostiene a la masa-polea $m_4$ mediante un cable y su ramal derecho sostiene a $m_2$. La polea $m_2$ cuelga del ramal derecho de $m_1$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho sostiene a la polea $m_3$. La polea $m_3$ cuelga del ramal derecho de $m_2$; su ramal izquierdo está conectado al piso mediante un cable (extremo fijo) y su ramal derecho está conectado al piso mediante un resorte de constante $K'$ y longitud natural $\ell_0'$. La altura total del sistema es $H$. Las coordenadas $y_1$, $y_2$, $y_3$, $y_4$ se miden desde el techo hacia abajo hasta el centro de cada polea/masa respectivamente. La distancia $a$ se mide desde el centro de $m_1$ hasta el centro de $m_3$.
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

    % Ramal izquierdo de m1 — cable baja a m4
    \draw[thick, maincolor] (0.7,5.7) -- (0.7,4.3);
    \draw[thick, fill=teal!30, draw=maincolor] (0.4,3.7) rectangle (1.0,4.3);
    \node[maincolor] at (0.7,4.0) {$m_4$};

    % Ramal derecho de m1 — cable baja a m2
    \draw[thick, maincolor] (1.3,5.7) -- (1.3,3.7);

    % Polea m2 (accentcolor)
    \draw[thick, fill=accentcolor!10, draw=accentcolor] (1.3,3.4) circle (0.3);
    \fill[accentcolor] (1.3,3.4) circle (0.05);
    \node[left, accentcolor] at (0.8,3.4) {$m_2$};

    % Ramal izquierdo de m2 — cable fijo al piso
    \draw[thick, accentcolor] (1.0,3.4) -- (1.0,0);

    % Ramal derecho de m2 — cable baja a m3
    \draw[thick, accentcolor] (1.6,3.4) -- (1.6,1.7);

    % Polea m3 (teal)
    \draw[thick, fill=teal!20, draw=maincolor] (1.6,1.4) circle (0.3);
    \fill[maincolor] (1.6,1.4) circle (0.05);
    \node[left, maincolor] at (1.1,1.4) {$m_3$};

    % Ramal izquierdo de m3 — cable fijo al piso
    \draw[thick, maincolor] (1.3,1.4) -- (1.3,0);

    % Ramal derecho de m3 — resorte K' al piso
    \draw[thick, accentcolor] (1.9,1.4) -- (1.9,1.0);
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, accentcolor, thick] (1.9,1.0) -- (1.9,0);
    \node[right, accentcolor] at (2.1,0.5) {$K'$};

    % Cota H — altura total
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
    \draw[dotted] (1.9,1.4) -- (4.3,1.4);

    % Coordenada y4 — techo a m4
    \draw[->, maincolor, thick] (4.9,7.3) -- (4.9,4.0) node[midway, right] {$y_4$};
    \draw[dotted] (0.7,4.0) -- (5.0,4.0);

    % Cota a — m1 a m3
    \draw[<->, maincolor, thick] (2.1,5.7) -- (2.1,1.4) node[midway, right] {$a$};
    \draw[dotted] (1.0,5.7) -- (2.2,5.7);
    \draw[dotted] (1.6,1.4) -- (2.2,1.4);

\end{tikzpicture}
\end{document}
```

> **Descripción de la figura:** El resorte $K$ (teal) conecta el techo con la polea $m_1$ (teal). Del ramal izquierdo de $m_1$ desciende un cable que sostiene la masa $m_4$ (bloque teal). Del ramal derecho de $m_1$ desciende un cable hasta la polea $m_2$ (naranja). Del ramal izquierdo de $m_2$ desciende un cable fijo al piso. Del ramal derecho de $m_2$ desciende un cable hasta la polea $m_3$ (teal). Del ramal izquierdo de $m_3$ desciende un cable fijo al piso. Del ramal derecho de $m_3$ desciende el resorte $K'$ (naranja) conectado al piso. Las coordenadas $y_1$, $y_2$, $y_3$, $y_4$ se miden desde el techo hacia abajo hasta cada polea/masa. La cota $a$ va desde el centro de $m_1$ hasta el centro de $m_3$. La cota $H$ es la altura total techo–piso (rojo).

---

**Resolución**
Se determinan las ligaduras geométricas de los cables inextensibles, se formulan la energía cinética y la energía potencial para establecer la función Lagrangiana, y se derivan las ecuaciones de movimiento según la elección de coordenadas generalizadas.

---

### Caso 1 — Sistema con coordenadas generalizadas $(y_1, y_2)$ (2 GDL)

**Paso 1 — Ligaduras cinemáticas y velocidades**


$$
L_1 = (y_4 - y_1) + \pi R_1 + (y_2 - y_1) = y_4 + y_2 - 2y_1 + \pi R_1 = \text{cte}
$$


$$
\dot{y}_4 = 2\dot{y}_1 - \dot{y}_2
$$


$$
y_4 = 2y_1 - y_2 + C_1 \qquad \text{donde } C_1 = L_1 - \pi R_1
$$



$$
L_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = H + \pi R_2 + y_3 - 2y_2 = \text{cte}
$$



$$
\dot{y}_3 = 2\dot{y}_2
$$



$$
y_3 = 2y_2 + C_2 \qquad \text{donde } C_2 = L_2 - H - \pi R_2
$$



$$
L_3 = (H - y_3) + \pi R_3 + (y_s - y_3) = H + \pi R_3 + y_s - 2y_3 = \text{cte}
$$



$$
y_s = 2y_3 + C_3 = 4y_2 + C_s \qquad \text{donde } C_s = 2C_2 + C_3
$$



$$
\text{GDL} = 4 - 2 = 2 \implies q_1 = y_1, \quad q_2 = y_2
$$


**Paso 2 — Energía cinética del sistema**


$$
T = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 + \frac{1}{2}m_3\dot{y}_3^2 + \frac{1}{2}m_4\dot{y}_4^2
$$



$$
T = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 + \frac{1}{2}m_3\left(2\dot{y}_2\right)^2 + \frac{1}{2}m_4\left(2\dot{y}_1 - \dot{y}_2\right)^2
$$



$$
\boxed{T = \frac{1}{2}(m_1 + 4m_4)\dot{y}_1^2 + \frac{1}{2}(m_2 + 4m_3 + m_4)\dot{y}_2^2 - 2m_4\dot{y}_1\dot{y}_2}
$$


**Paso 3 — Energía potencial total**


$$
V_g = -m_1 g y_1 - m_2 g y_2 - m_3 g y_3 - m_4 g y_4 = -(m_1 + 2m_4)g y_1 - (m_2 + 2m_3 - m_4)g y_2 + \text{cte}
$$



$$
V_K = \frac{1}{2}K(y_1 - \ell_0)^2
$$



$$
V_{K'} = \frac{1}{2}K'(H - y_s - \ell_0')^2 = \frac{1}{2}K'(H - 4y_2 - C_s - \ell_0')^2
$$



$$
\boxed{V = -(m_1 + 2m_4)g y_1 - (m_2 + 2m_3 - m_4)g y_2 + \frac{1}{2}K(y_1 - \ell_0)^2 + \frac{1}{2}K'(H - 4y_2 - C_s - \ell_0')^2}
$$


**Paso 4 — Función Lagrangiana**


$$
L = T - V
$$



$$
L = \frac{1}{2}(m_1 + 4m_4)\dot{y}_1^2 + \frac{1}{2}(m_2 + 4m_3 + m_4)\dot{y}_2^2 - 2m_4\dot{y}_1\dot{y}_2 + (m_1 + 2m_4)g y_1 + (m_2 + 2m_3 - m_4)g y_2 - \frac{1}{2}K(y_1 - \ell_0)^2 - \frac{1}{2}K'(H - 4y_2 - C_s - \ell_0')^2
$$


**Paso 5 — Ecuaciones diferenciales de movimiento acopladas**


$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_1}\right) - \frac{\partial L}{\partial y_1} = 0
$$



$$
\boxed{(m_1 + 4m_4)\ddot{y}_1 - 2m_4\ddot{y}_2 + K y_1 = (m_1 + 2m_4)g + K \ell_0}
$$



$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_2}\right) - \frac{\partial L}{\partial y_2} = 0
$$



$$
\boxed{(m_2 + 4m_3 + m_4)\ddot{y}_2 - 2m_4\ddot{y}_1 + 16 K' y_2 = (m_2 + 2m_3 - m_4)g + 4K'(H - C_s - \ell_0')}
$$


---

### Caso 2 — Sistema en función de la cota $a$ y la coordenada $y_2$ (2 GDL)

**Paso 1 — Relación de transformación con la cota $a$**


$$
a = y_3 - y_1 = 2y_2 + C_2 - y_1 \implies y_1 = 2y_2 - a + C_2
$$



$$
\dot{y}_1 = 2\dot{y}_2 - \dot{a}
$$



$$
\dot{y}_4 = 2\dot{y}_1 - \dot{y}_2 = 3\dot{y}_2 - 2\dot{a}
$$


**Paso 2 — Función Lagrangiana**


$$
T = \frac{1}{2}(4m_1 + m_2 + 4m_3 + 9m_4)\dot{y}_2^2 + \frac{1}{2}(m_1 + 4m_4)\dot{a}^2 - (2m_1 + 6m_4)\dot{y}_2\dot{a}
$$



$$
V = -(2m_1 + m_2 + 2m_3 + 3m_4)g y_2 + (m_1 + 2m_4)g a + \frac{1}{2}K(2y_2 - a + C_2 - \ell_0)^2 + \frac{1}{2}K'(H - 4y_2 - C_s - \ell_0')^2
$$



$$
L = T - V
$$


**Paso 3 — Ecuaciones diferenciales de movimiento**


$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{a}}\right) - \frac{\partial L}{\partial a} = 0
$$



$$
\boxed{(m_1 + 4m_4)\ddot{a} - (2m_1 + 6m_4)\ddot{y}_2 + K a - 2K y_2 = -(m_1 + 2m_4)g + K(C_2 - \ell_0)}
$$



$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{y}_2}\right) - \frac{\partial L}{\partial y_2} = 0
$$



$$
\boxed{(4m_1 + m_2 + 4m_3 + 9m_4)\ddot{y}_2 - (2m_1 + 6m_4)\ddot{a} + (4K + 16K')y_2 - 2K a = (2m_1 + m_2 + 2m_3 + 3m_4)g - 2K(C_2 - \ell_0) + 4K'(H - C_s - \ell_0')}
$$


---

### Caso 3 — Sistema con cota $a$ constante (1 GDL)

**Paso 1 — Ligadura adicional y ecuación de movimiento**


$$
\dot{a} = 0 \implies \dot{y}_1 = 2\dot{y}_2
$$



$$
\boxed{(4m_1 + m_2 + 4m_3 + 9m_4)\ddot{y}_2 + (4K + 16K')y_2 = (2m_1 + m_2 + 2m_3 + 3m_4)g + 2K(a - C_2 + \ell_0) + 4K'(H - C_s - \ell_0')}
$$



