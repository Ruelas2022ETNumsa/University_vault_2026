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
