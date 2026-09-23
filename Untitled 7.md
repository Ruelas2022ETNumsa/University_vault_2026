##### Ej. Sistema de dos cuñas con pared inclinada, resorte y fuerza externa — 1 GDL

**Enunciado:**
Una cuña $m_1$ de forma trapezoidal (caras superior e inferior horizontales, cara izquierda inclinada a $60°$ y cara derecha vertical) queda suspendida entre una rampa fija inclinada a $60°$ y la cara superior inclinada a $45°$ de la cuña $m_2$. La cuña $m_2$ es un trapecio rectángulo que descansa sobre el piso horizontal: vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical conectada mediante un resorte de constante $K$ a la pared derecha fija, y cara inferior horizontal apoyada sobre el piso. Sobre $m_1$ actúa una fuerza externa $F$ dirigida verticalmente hacia abajo. El sistema desliza sin fricción y tiene 1 grado de libertad. Se definen $x_1$ como la distancia horizontal desde el origen (base de la rampa) al borde inferior-izquierdo de $m_1$, $x_2$ como la distancia horizontal desde el origen al vértice inferior-izquierdo de $m_2$, $y_1$ como la altura del borde inferior de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto entre $m_1$ y $m_2$ sobre el piso (función de $x_2$), $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = x_2 - x_1$ la separación horizontal entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$. Hallar la ecuación de movimiento de Lagrange del sistema.

**Descripción de la figura:**
La figura muestra el sistema en su configuración general con todas las cotas relevantes.

Estructura fija: la pared izquierda es una rampa inclinada a $60°$ respecto a la horizontal (superficie rayada). El piso es horizontal (superficie rayada). La pared derecha es vertical (superficie rayada).

Bloque $m_1$: trapecio con cara superior horizontal, cara inferior horizontal, cara izquierda inclinada a $60°$ apoyada contra la rampa fija, y cara derecha vertical. Flota sin tocar el piso. La fuerza $F$ actúa verticalmente hacia abajo sobre su cara superior. El punto rojo sobre su borde inferior-izquierdo indica el punto de contacto con la rampa. El punto verde sobre su borde inferior-derecho indica el punto de contacto con la cara inclinada de $m_2$.

Bloque $m_2$: trapecio rectángulo con vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical y cara inferior horizontal apoyada sobre el piso. El resorte $K$ conecta horizontalmente la cara derecha de $m_2$ con la pared derecha fija.

Cotas indicadas en la figura: $y_1$ (flecha vertical roja, altura del borde inferior de $m_1$ sobre el piso, medida en el lado izquierdo), $y_2$ (flecha vertical verde, altura del punto de contacto $m_1$-$m_2$ sobre el piso, medida en el punto verde), $x_1$ (flecha horizontal roja, distancia del borde inferior-izquierdo de $m_1$ al origen), $x_2$ (flecha horizontal roja, distancia del vértice inferior-izquierdo de $m_2$ al origen), $d$ (flecha horizontal verde, separación $x_2 - x_1$ entre los bordes en contacto), $B_1$ (flecha horizontal violeta, ancho de $m_1$), $B_2$ (flecha horizontal violeta, ancho de $m_2$). Los ángulos $60°$ y $45°$ están marcados en la base de la rampa y en la base de la interfaz inclinada respectivamente.


---


NBLM1:
##### Ej. Una cuña $m_1$ de forma trapezoidal (caras superior e inferior horizontales, cara izquierda inclinada a $60°$ y cara derecha vertical) queda suspendida entre una rampa fija inclinada a $60°$ y la cara superior inclinada a $45°$ de la cuña $m_2$. La cuña $m_2$ es un trapecio rectángulo que descansa sobre el piso horizontal: vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical conectada mediante un resorte de constante $K$ a la pared derecha fija, y cara inferior horizontal apoyada sobre el piso. Sobre $m_1$ actúa una fuerza externa $F$ dirigida verticalmente hacia abajo. El sistema desliza sin fricción y tiene 1 grado de libertad. Se definen $x_1$ como la distancia horizontal desde el origen (base de la rampa) al borde inferior-izquierdo de $m_1$, $x_2$ como la distancia horizontal desde el origen al vértice inferior-izquierdo de $m_2$, $y_1$ como la altura del borde inferior de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto entre $m_1$ y $m_2$ sobre el piso (función de $x_2$), $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = x_2 - x_1$ la separación horizontal entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$. Hallar la ecuación de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
  % Suelo y pared derecha
  \fill[pattern=north east lines] (-0.5,-0.3) rectangle (8,0);
  \draw[thick] (-0.5,0) -- (8,0);

  % Rampa 60 deg
  \fill[pattern=north east lines] (-0.5,0) -- (2,4.33) -- (1.6,4.33) -- (-0.5,0.7) -- cycle;
  \draw[thick] (0,0) -- (2,4.33);

  % Pared derecha
  \fill[pattern=north east lines] (7.5,0) rectangle (7.8,3);
  \draw[thick] (7.5,0) -- (7.5,3);

  % Angulos
  \draw[teal, thick] (0.6,0) arc (0:60:0.6);
  \node[teal] at (0.9,0.3) {\small $60^\circ$};

  % Cuña m2 (trapecio rectángulo con cara 45 deg)
  \draw[thick, fill=orange!15] (3.5,0) -- (6.0,2.5) -- (6.0,0) -- cycle;
  \draw[orange, thick] (4.1,0) arc (0:45:0.6);
  \node[orange] at (4.5,0.25) {\small $45^\circ$};
  \node at (5.2,0.7) {$m_2$};

  % Cuña m1
  \draw[thick, fill=teal!20] (1.0,1.732) -- (2.5,1.732) -- (2.5,2.732) -- (1.577,2.732) -- cycle;
  \node at (1.9,2.2) {$m_1$};

  % Puntos de contacto
  \fill[red] (1.0,1.732) circle (2pt);
  \fill[teal] (2.5,1.732) circle (2pt);

  % Fuerza F
  \draw[->, very thick, red] (2.0,3.5) -- (2.0,2.732) node[above=8pt] {$F$};

  % Resorte K
  \draw[thick] (6.0,1.0) -- (6.2,1.0) -- (6.3,1.2) -- (6.5,0.8) -- (6.7,1.2) -- (6.9,0.8) -- (7.1,1.2) -- (7.3,0.8) -- (7.4,1.0) -- (7.5,1.0);
  \node[above] at (6.75,1.2) {$K$};

  % Cotas
  \draw[dashed, gray] (1.0,0) -- (1.0,1.732);
  \draw[dashed, gray] (2.5,0) -- (2.5,1.732);
  \draw[dashed, gray] (3.5,0) -- (3.5,1.732);

  \draw[<->, red] (0,-0.3) -- (1.0,-0.3) node[midway, below] {$x_1$};
  \draw[<->, red] (0,-0.7) -- (3.5,-0.7) node[midway, below] {$x_2$};
  \draw[<->, violet] (1.0,1.4) -- (2.5,1.4) node[midway, above] {$B_1$};
  \draw[<->, red] (-0.3,0) -- (-0.3,1.732) node[midway, left] {$y_1$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Se formulan la cinética y potencial en función de la coordenada generalizada $x_1$ tras establecer la ligadura geométrica entre $x_1$ y $x_2$.

**Paso 1 — Relación de restricción cinemática entre las coordenadas $x_1$ y $x_2$**


$$
y_1 = x_1 \tan 60^\circ = \sqrt{3} x_1
$$



$$
\dot{y}_1 = \sqrt{3} \dot{x}_1
$$



$$
y_2 = (x_1 + B_1 - x_2) \tan 45^\circ = x_1 + B_1 - x_2
$$



$$
\sqrt{3} x_1 = x_1 + B_1 - x_2
$$



$$
x_2 = (1 - \sqrt{3}) x_1 + B_1
$$



$$
\dot{x}_2 = (1 - \sqrt{3}) \dot{x}_1
$$


**Paso 2 — Expresión de la energía cinética total $T$ del sistema**


$$
T_1 = \frac{1}{2} m_1 (\dot{x}_1^2 + \dot{y}_1^2) = \frac{1}{2} m_1 (\dot{x}_1^2 + 3 \dot{x}_1^2) = 2 m_1 \dot{x}_1^2
$$



$$
T_2 = \frac{1}{2} m_2 \dot{x}_2^2 = \frac{1}{2} m_2 (1 - \sqrt{3})^2 \dot{x}_1^2 = \frac{1}{2} m_2 (4 - 2\sqrt{3}) \dot{x}_1^2 = (2 - \sqrt{3}) m_2 \dot{x}_1^2
$$



$$
T = T_1 + T_2 = \left[ 2 m_1 + (2 - \sqrt{3}) m_2 \right] \dot{x}_1^2
$$


**Paso 3 — Expresión de la energía potencial total $V$ del sistema**


$$
V_{\text{ext}} = (m_1 g + F) y_1 = \sqrt{3} (m_1 g + F) x_1
$$



$$
V_k = \frac{1}{2} K (x_2 - x_{2,0})^2 = \frac{1}{2} K \left[ (1 - \sqrt{3}) (x_1 - x_{1,0}) \right]^2 = \frac{1}{2} K (4 - 2\sqrt{3}) (x_1 - x_{1,0})^2
$$



$$
V = \sqrt{3} (m_1 g + F) x_1 + (2 - \sqrt{3}) K (x_1 - x_{1,0})^2
$$


**Paso 4 — Función Lagrangiana $L = T - V$ del sistema**


$$
L = \left[ 2 m_1 + (2 - \sqrt{3}) m_2 \right] \dot{x}_1^2 - \sqrt{3} (m_1 g + F) x_1 - (2 - \sqrt{3}) K (x_1 - x_{1,0})^2
$$


**Paso 5 — Ecuación diferencial de movimiento de Lagrange**


$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_1} \right) - \frac{\partial L}{\partial x_1} = 0
$$



$$
\frac{\partial L}{\partial \dot{x}_1} = 2 \left[ 2 m_1 + (2 - \sqrt{3}) m_2 \right] \dot{x}_1 = \left[ 4 m_1 + 2(2 - \sqrt{3}) m_2 \right] \dot{x}_1
$$



$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{x}_1} \right) = \left[ 4 m_1 + 2(2 - \sqrt{3}) m_2 \right] \ddot{x}_1
$$



$$
\frac{\partial L}{\partial x_1} = -\sqrt{3} (m_1 g + F) - 2 (2 - \sqrt{3}) K (x_1 - x_{1,0}) = -\sqrt{3} (m_1 g + F) - (4 - 2\sqrt{3}) K (x_1 - x_{1,0})
$$



$$
\left[ 4 m_1 + 2(2 - \sqrt{3}) m_2 \right] \ddot{x}_1 + (4 - 2\sqrt{3}) K (x_1 - x_{1,0}) + \sqrt{3} (m_1 g + F) = 0
$$



$$
\boxed{\left[ 4 m_1 + 2(2 - \sqrt{3}) m_2 \right] \ddot{x}_1 + (4 - 2\sqrt{3}) K (x_1 - x_{1,0}) + \sqrt{3} (m_1 g + F) = 0}
$$


---

NBLM2:

##### Ej. Una cuña $m_1$ de forma trapezoidal (caras superior e inferior horizontales, cara izquierda inclinada a $60°$ y cara derecha vertical) queda suspendida entre una rampa fija inclinada a $60°$ y la cara superior inclinada a $45°$ de la cuña $m_2$. La cuña $m_2$ es un trapecio rectángulo que descansa sobre el piso horizontal: vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical conectada mediante un resorte de constante $K$ a la pared derecha fija, y cara inferior horizontal apoyada sobre el piso. Sobre $m_1$ actúa una fuerza externa $F$ dirigida verticalmente hacia abajo. El sistema desliza sin fricción y tiene 1 grado de libertad. Se definen $x_1$ como la distancia horizontal desde el origen (base de la rampa) al borde inferior-izquierdo de $m_1$, $x_2$ como la distancia horizontal desde el origen al vértice inferior-izquierdo de $m_2$, $y_1$ como la altura del borde inferior de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto entre $m_1$ y $m_2$ sobre el piso (función de $x_2$), $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = x_2 - x_1$ la separación horizontal entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$. Hallar la ecuación de movimiento de Lagrange del sistema.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Rampa fija izquierda (60 deg)
    \fill[pattern=north east lines] (0,0) -- (2.6,4.503) -- (2.3,4.676) -- (-0.3,0) -- cycle;
    \draw[thick] (0,0) -- (2.6,4.503);

    % Piso horizontal
    \fill[pattern=north east lines] (-0.5,-0.3) rectangle (6.8,0);
    \draw[thick] (-0.5,0) -- (6.8,0);

    % Pared derecha vertical
    \fill[pattern=north east lines] (6.8,0) rectangle (7.1,3.8);
    \draw[thick] (6.8,0) -- (6.8,3.8);

    % Bloque m2 (trapecio rectángulo naranja)
    \draw[fill=orange!10, draw=accentcolor, thick] (0.8,0) -- (4.2,0) -- (4.2,3.4) -- cycle;
    \node[accentcolor] at (2.8,1.0) {$m_2$};

    % Bloque m1 (trapecio teal)
    \draw[fill=teal!10, draw=maincolor, thick] (1.366,2.366) -- (3.166,2.366) -- (3.166,3.366) -- (1.943,3.366) -- cycle;
    \node[maincolor] at (2.4,2.866) {$m_1$};

    % Puntos de contacto
    \fill[red] (1.366,2.366) circle (0.07);
    \fill[green!70!black] (3.166,2.366) circle (0.07);

    % Fuerza F
    \draw[->, red, ultra thick] (2.55,4.1) -- (2.55,3.366) node[midway, right] {$F$};

    % Resorte K
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (4.2,1.7) -- (6.8,1.7);
    \node[above, maincolor] at (5.5,1.9) {$K$};

    % Ángulos
    \draw[thick] (0.5,0) arc (0:60:0.5);
    \node at (0.8,0.3) {$60^\circ$};

    \draw[thick] (1.4,0) arc (0:45:0.6);
    \node at (1.8,0.25) {$45^\circ$};

    % Cotas x1, x2, d
    \draw[->, maincolor, thick] (0,-0.5) -- (1.366,-0.5) node[midway, below] {$x_1$};
    \draw[dotted] (0,0) -- (0,-0.7);
    \draw[dotted] (1.366,2.366) -- (1.366,-0.7);

    \draw[->, maincolor, thick] (0,-1.1) -- (0.8,-1.1) node[midway, below] {$x_2$};
    \draw[dotted] (0.8,0) -- (0.8,-1.3);

    \draw[<->, accentcolor, thick] (0.8,-0.5) -- (1.366,-0.5) node[midway, above=-2pt] {$d$};

    % Cotas y1, y2
    \draw[->, red, thick] (1.366,0) -- (1.366,2.366) node[midway, left] {$y_1$};

    \draw[->, green!70!black, thick] (3.166,0) -- (3.166,2.366) node[midway, right] {$y_2$};
    \draw[dotted] (3.166,2.366) -- (3.166,0);

    % Ancho B1, B2
    \draw[<->, maincolor] (1.366,3.6) -- (3.166,3.6) node[midway, above] {$B_1$};
    \draw[dotted] (1.366,3.366) -- (1.366,3.7);
    \draw[dotted] (3.166,3.366) -- (3.166,3.7);

    \draw[<->, accentcolor] (0.8,-1.7) -- (4.2,-1.7) node[midway, below] {$B_2$};
    \draw[dotted] (4.2,0) -- (4.2,-1.9);

\end{tikzpicture}
\end{document}
```

**Resolución**
Se establecen las restricciones geométricas de contacto, se formula el Lagrangiano del sistema en función de la coordenada generalizada $x_2$ y se obtiene la ecuación diferencial mediante la ecuación de Euler-Lagrange.

**Paso 1 — Ligaduras cinemáticas y relaciones entre coordenadas**

Contacto del vértice inferior-izquierdo de $m_1$ sobre la rampa fija inclinada a $60°$:

$$
y_1 = x_1 \tan 60° = \sqrt{3} x_1
$$


Contacto del vértice inferior-derecho de $m_1$ sobre la superficie inclinada a $45°$ de $m_2$:

$$
y_2 = y_1 = (x_1 + B_1 - x_2) \tan 45° = x_1 + B_1 - x_2
$$


Igualación de las expresiones de la altura $y_1$:

$$
\sqrt{3} x_1 = x_1 + B_1 - x_2 \implies (\sqrt{3} - 1) x_1 = B_1 - x_2
$$



$$
x_1 = \dfrac{\sqrt{3} + 1}{2} (B_1 - x_2)
$$



$$
y_1 = \dfrac{3 + \sqrt{3}}{2} (B_1 - x_2)
$$


Relación entre las velocidades del sistema:

$$
\dot{x}_1 = -\dfrac{\sqrt{3} + 1}{2} \dot{x}_2
$$



$$
\dot{y}_1 = -\dfrac{3 + \sqrt{3}}{2} \dot{x}_2
$$


**Paso 2 — Energía cinética del sistema**

Para la cuña $m_1$ en traslación 2D:

$$
v_{1x}^2 + v_{1y}^2 = \dot{x}_1^2 + (\sqrt{3}\dot{x}_1)^2 = 4 \dot{x}_1^2 = 4 \left( \dfrac{\sqrt{3} + 1}{2} \right)^{\!2} \dot{x}_2^2 = (4 + 2\sqrt{3}) \dot{x}_2^2 = 2(2 + \sqrt{3})\dot{x}_2^2
$$



$$
T_1 = \dfrac{1}{2} m_1 (v_{1x}^2 + v_{1y}^2) = (2 + \sqrt{3}) m_1 \dot{x}_2^2
$$


Para la cuña $m_2$ en traslación horizontal:

$$
T_2 = \dfrac{1}{2} m_2 \dot{x}_2^2
$$


Energía cinética total $T$:

$$
T = \dfrac{1}{2} \left[ m_2 + 2(2 + \sqrt{3}) m_1 \right] \dot{x}_2^2 = \dfrac{1}{2} \left[ m_2 + (4 + 2\sqrt{3}) m_1 \right] \dot{x}_2^2
$$


**Paso 3 — Energía potencial del sistema**

Potencial gravitatorio y fuerza externa constante $F$ actuando sobre $m_1$:

$$
V_1 = (m_1 g + F) y_1 = \dfrac{3 + \sqrt{3}}{2} (m_1 g + F) (B_1 - x_2)
$$


Potencial elástico del resorte $K$ sobre $m_2$:

$$
V_2 = \dfrac{1}{2} K (x_2 - x_0)^2
$$


Energía potencial total $V$:

$$
V = \dfrac{3 + \sqrt{3}}{2} (m_1 g + F) (B_1 - x_2) + \dfrac{1}{2} K (x_2 - x_0)^2
$$


**Paso 4 — Función Lagrangiana $L = T - V$**


$$
L = \dfrac{1}{2} \left[ m_2 + (4 + 2\sqrt{3}) m_1 \right] \dot{x}_2^2 - \dfrac{3 + \sqrt{3}}{2} (m_1 g + F) (B_1 - x_2) - \dfrac{1}{2} K (x_2 - x_0)^2
$$


**Paso 5 — Ecuación de movimiento de Lagrange**

Ecuación de Euler-Lagrange respecto a $q = x_2$:

$$
\dfrac{d}{dt} \!\left( \dfrac{\partial L}{\partial \dot{x}_2} \right) - \dfrac{\partial L}{\partial x_2} = 0
$$


Derivadas parciales de la función Lagrangiana:

$$
\dfrac{\partial L}{\partial \dot{x}_2} = \left[ m_2 + (4 + 2\sqrt{3}) m_1 \right] \dot{x}_2 \implies \dfrac{d}{dt} \!\left( \dfrac{\partial L}{\partial \dot{x}_2} \right) = \left[ m_2 + (4 + 2\sqrt{3}) m_1 \right] \ddot{x}_2
$$



$$
\dfrac{\partial L}{\partial x_2} = \dfrac{3 + \sqrt{3}}{2} (m_1 g + F) - K (x_2 - x_0)
$$



$$
\boxed{\left[ m_2 + (4 + 2\sqrt{3}) m_1 \right] \ddot{x}_2 + K (x_2 - x_0) = \dfrac{3 + \sqrt{3}}{2} (m_1 g + F)}
$$

