##### Ej. Sistema de dos cuñas con pared inclinada, resorte y fuerza externa — 1 GDL

**Enunciado:**
Una cuña $m_1$ de forma trapezoidal (caras superior e inferior horizontales, cara izquierda inclinada a $60°$ y cara derecha vertical) queda suspendida entre una rampa fija inclinada a $60°$ y la cara superior inclinada a $45°$ de la cuña $m_2$. La cuña $m_2$ es un trapecio rectángulo que descansa sobre el piso horizontal: vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical conectada mediante un resorte de constante $K$ a la pared derecha fija, y cara inferior horizontal apoyada sobre el piso. Sobre $m_1$ actúa una fuerza externa $F$ dirigida verticalmente hacia abajo. El sistema desliza sin fricción y tiene 1 grado de libertad. Se definen $x_1$ como la distancia horizontal desde el origen (base de la rampa) al borde inferior-izquierdo de $m_1$, $x_2$ como la distancia horizontal desde el origen al vértice inferior-izquierdo de $m_2$, $y_1$ como la altura del borde inferior de $m_1$ sobre el piso, $y_2$ como la altura del punto de contacto entre $m_1$ y $m_2$ sobre el piso (función de $x_2$), $B_1$ el ancho horizontal de $m_1$, $B_2$ el ancho horizontal de $m_2$, y $d = B_1 - x_1 - x_2$ la separación horizontal entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$, donde $B_1$ se mide desde el origen hasta la proyección horizontal del borde inferior-derecho de $m_1$ en posición de referencia. Hallar la ecuación de movimiento de Lagrange del sistema.

**Descripción de la figura:**
La figura muestra el sistema en su configuración general con todas las cotas relevantes.

Estructura fija: la pared izquierda es una rampa inclinada a $60°$ respecto a la horizontal (superficie rayada). El piso es horizontal (superficie rayada). La pared derecha es vertical (superficie rayada).

Bloque $m_1$: trapecio con cara superior horizontal, cara inferior horizontal, cara izquierda inclinada a $60°$ apoyada contra la rampa fija, y cara derecha vertical. Flota sin tocar el piso. La fuerza $F$ actúa verticalmente hacia abajo sobre su cara superior. El punto rojo sobre su borde inferior-izquierdo indica el punto de contacto con la rampa. El punto verde sobre su borde inferior-derecho indica el punto de contacto con la cara inclinada de $m_2$.

Bloque $m_2$: trapecio rectángulo con vértice inferior-izquierdo apoyado en el piso, cara superior inclinada a $45°$ sobre la que desliza $m_1$, cara derecha vertical y cara inferior horizontal apoyada sobre el piso. El resorte $K$ conecta horizontalmente la cara derecha de $m_2$ con la pared derecha fija.

Cotas indicadas en la figura: $y_1$ (flecha vertical roja, altura del borde inferior de $m_1$ sobre el piso, medida en el lado izquierdo), $y_2$ (flecha vertical verde, altura del punto de contacto $m_1$-$m_2$ sobre el piso, medida en el punto verde), $x_1$ (flecha horizontal roja, distancia del borde inferior-izquierdo de $m_1$ al origen), $x_2$ (flecha horizontal roja, distancia del vértice inferior-izquierdo de $m_2$ al origen), $d$ (flecha horizontal verde, separación $d = B_1 - x_1 - x_2$ entre el borde inferior-derecho de $m_1$ y el vértice inferior-izquierdo de $m_2$; con $\tan 45° = y_1/d = 1$ resulta $y_2 = d$), $B_1$ (flecha horizontal violeta, ancho de $m_1$), $B_2$ (flecha horizontal violeta, ancho de $m_2$). Los ángulos $60°$ y $45°$ están marcados en la base de la rampa y en la base de la interfaz inclinada respectivamente.


```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}

\begin{document}

\begin{tikzpicture}[scale=1.1, >=latex]

%================================================
% PARED IZQUIERDA - 60°
%================================================
\fill[pattern=north east lines]
(0,0)
-- (-1.73,3)
-- (-1.30,3)
-- (0,0)
-- cycle;

\draw[thick]
(0,0) -- (-1.73,3);

%================================================
% PISO
%================================================
\fill[pattern=north east lines]
(0,-0.3) rectangle (8.5,0);

\draw[thick]
(0,0) -- (8.5,0);

%================================================
% BLOQUE 2
%================================================
\fill[white]
(2.5,0)
-- (5.5,3)
-- (7.0,3)
-- (7.0,0)
-- cycle;

\draw[thick]
(2.5,0)
-- (5.5,3)
-- (7.0,3)
-- (7.0,0)
-- cycle;

\node at (5.5,1.3) {\Large 2};

%================================================
% BLOQUE 1
% SUSPENDIDO SOBRE EL PISO
%================================================
\fill[white]
(-0.58,1.0)
-- (3.50,1.0)
-- (4.70,2.20)
-- (-1.27,2.20)
-- cycle;

\draw[thick]
(-0.58,1.0)
-- (3.50,1.0)
-- (4.70,2.20)
-- (-1.27,2.20)
-- cycle;

\node at (1.65,1.60) {\Large 1};

%================================================
% FUERZA SOBRE EL BLOQUE 1
%================================================
\draw[->, very thick]
(1.65,3.2) -- (1.65,2.20);

%================================================
% PUNTOS DE REFERENCIA
%================================================
\fill[red]
(-0.58,1.0) circle (2pt);

\fill[green!60!black]
(3.50,1.0) circle (2pt);

%================================================
% ÁNGULO DE LA PARED: 60°
%================================================
\draw[thick]
(0,0) ++(180:0.55)
arc (180:120:0.55);

\node at (-0.38,0.30) {$60^\circ$};

%================================================
% ÁNGULO DEL BLOQUE 2: 45°
%================================================
\draw[thick]
(2.5,0) ++(0.55,0)
arc (0:45:0.55);

\node at (3.05,0.25) {$45^\circ$};

%================================================
% RESORTE
%================================================
\draw[
    thick,
    decorate,
    decoration={
        coil,
        aspect=0.35,
        segment length=5pt,
        amplitude=5pt
    }
]
(7.0,1.5) -- (8.5,1.5);

%================================================
% PARED DERECHA
%================================================
\fill[pattern=north east lines]
(8.5,0) rectangle (8.8,3.0);

\draw[thick]
(8.5,0) -- (8.5,3.0);

%================================================
% ALTURA y_1
% Desde el piso hasta el bloque 1
%================================================
\draw[red, <->, thick]
(-2.0,0) -- (-2.0,1.0);

\draw[red, dashed]
(-2.0,1.0) -- (-0.58,1.0);

\draw[red, dashed]
(-2.0,0) -- (0,0);

\node[red] at (-2.25,0.5) {$y_1$};

%================================================
% ALTURA y_2
% Desde el piso hasta el punto del bloque 2
%================================================
\draw[green!60!black, <->, thick]
(3.50,-0.05) -- (3.50,1.0);

\draw[green!60!black, dashed]
(3.50,1.0) -- (4.10,1.0);

\node[green!60!black] at (3.75,0.5) {$y_2$};

%================================================
% DISTANCIA d
%================================================
\draw[green!60!black, <->, thick]
(3.50,-0.55) -- (4.70,-0.55);

\draw[green!60!black, dashed]
(3.50,0) -- (3.50,-0.55);

\draw[green!60!black, dashed]
(4.70,1.0) -- (4.70,-0.55);

\node[green!60!black] at (4.10,-0.75) {$d$};

%================================================
% x_1
%================================================
\draw[red, <->, thick]
(-0.58,-0.55) -- (0,-0.55);

\draw[red, dashed]
(-0.58,1.0) -- (-0.58,-0.55);

\node[red] at (-0.29,-0.75) {$x_1$};

%================================================
% x_2
%================================================
\draw[red, <->, thick]
(0,-0.95) -- (2.5,-0.95);

\draw[red, dashed]
(2.5,0) -- (2.5,-0.95);

\node[red] at (1.25,-1.15) {$x_2$};

%================================================
% B_1
%================================================
\draw[violet, <->, thick]
(0,-0.40) -- (2.5,-0.40);

\node[violet] at (1.25,-0.60) {$B_1$};

%================================================
% B_2
%================================================
\draw[violet, <->, thick]
(2.5,-0.40) -- (4.5,-0.40);

\draw[violet, dashed]
(8.5,0) -- (8.5,-0.40);

\node[violet] at (5.5,-0.60) {$B_2$};

\end{tikzpicture}

\end{document}
```

---

**Solución:**

## 1. Relaciones geométricas de vínculo

El sistema tiene 2 cuerpos móviles pero las restricciones geométricas impuestas por las superficies de contacto reducen los grados de libertad a 1. Se elige $x_2$ como coordenada generalizada.

**Vínculo de la rampa (60°):**

La cara izquierda de $m_1$ desliza sobre la rampa fija inclinada a $60°$. La relación entre la altura de $m_1$ y su posición horizontal es:

$$\tan 60° = \frac{y_1}{x_1} \implies y_1 = x_1 \tan 60°$$

**Vínculo de la interfaz $m_1$–$m_2$ (45°):**

El punto de contacto entre el borde inferior-derecho de $m_1$ y la cara inclinada a $45°$ de $m_2$ impone:

$$\tan 45° = \frac{y_2}{d} = \frac{y_1}{B_1 - x_1 - x_2}$$

Como $\tan 45° = 1$:

$$y_1 = d = B_1 - x_1 - x_2$$

Igualando las dos expresiones de $y_1$:

$$x_1 \tan 60° = B_1 - x_1 - x_2$$

$$x_1 (\tan 60° + 1) = B_1 - x_2$$

$$x_1 = \frac{B_1 - x_2}{1 + \tan 60°}$$

Con $\tan 60° = \sqrt{3}$:

$$x_1 = \frac{B_1 - x_2}{1 + \sqrt{3}}$$

Esta es la relación de vínculo que expresa $x_1$ en función de la coordenada generalizada $x_2$. Derivando:

$$\dot{x}_1 = \frac{-\dot{x}_2}{1 + \sqrt{3}}$$

Y para $y_1$:

$$y_1 = x_1 \sqrt{3} = \frac{\sqrt{3}(B_1 - x_2)}{1 + \sqrt{3}}$$

$$\dot{y}_1 = \frac{-\sqrt{3}\,\dot{x}_2}{1 + \sqrt{3}}$$

---

## 2. Energía cinética

$m_1$ se mueve en el plano con velocidades $\dot{x}_1$ e $\dot{y}_1$. $m_2$ solo se desplaza horizontalmente ($\dot{y}_2 = 0$ ya que su base está sobre el piso):

$$T = \frac{m_1}{2}(\dot{x}_1^2 + \dot{y}_1^2) + \frac{m_2}{2}\dot{x}_2^2$$

Sustituyendo $\dot{x}_1$ e $\dot{y}_1$ en función de $\dot{x}_2$:

$$\dot{x}_1^2 + \dot{y}_1^2 = \frac{\dot{x}_2^2}{(1+\sqrt{3})^2} + \frac{3\,\dot{x}_2^2}{(1+\sqrt{3})^2} = \frac{(1+3)\,\dot{x}_2^2}{(1+\sqrt{3})^2} = \frac{4\,\dot{x}_2^2}{(1+\sqrt{3})^2}$$

Entonces:

$$T = \frac{m_1}{2} \cdot \frac{4\,\dot{x}_2^2}{(1+\sqrt{3})^2} + \frac{m_2}{2}\dot{x}_2^2 = \frac{1}{2}\left[\frac{4m_1}{(1+\sqrt{3})^2} + m_2\right]\dot{x}_2^2$$

Definiendo la masa efectiva:

$$M^* = \frac{4m_1}{(1+\sqrt{3})^2} + m_2$$

$$T = \frac{1}{2}M^*\dot{x}_2^2$$

---

## 3. Energía potencial

Las contribuciones a la energía potencial son: el peso de $m_1$ (que varía con $y_1$), el peso de $m_2$ (constante, altura cero sobre el piso), y el resorte $K$ conectado a $m_2$.

Tomando el piso como referencia de altura:

$$V = m_1 g\, y_1 + \frac{1}{2}K\,(x_2 - x_{2,0})^2$$

donde $x_{2,0}$ es la posición de equilibrio natural del resorte. Expresando en función de $x_2$:

$$V = m_1 g \cdot \frac{\sqrt{3}(B_1 - x_2)}{1+\sqrt{3}} + \frac{1}{2}K\,(x_2 - x_{2,0})^2$$

---

## 4. Lagrangiano y ecuación de movimiento

$$L = T - V = \frac{1}{2}M^*\dot{x}_2^2 - m_1 g \cdot \frac{\sqrt{3}(B_1 - x_2)}{1+\sqrt{3}} - \frac{1}{2}K(x_2 - x_{2,0})^2$$

Aplicando la ecuación de Lagrange para $q = x_2$:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_2} - \frac{\partial L}{\partial x_2} = Q_{x_2}$$

donde $Q_{x_2}$ es la fuerza generalizada asociada a la fuerza externa $F$.

**Término cinético:**

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}_2} = M^*\ddot{x}_2$$

**Término potencial:**

$$\frac{\partial L}{\partial x_2} = \frac{m_1 g \sqrt{3}}{1+\sqrt{3}} - K(x_2 - x_{2,0})$$

**Fuerza generalizada $Q_{x_2}$:**

La fuerza $F$ actúa verticalmente hacia abajo sobre $m_1$. El trabajo virtual es:

$$\delta W = -F\,\delta y_1 = -F \cdot \frac{-\sqrt{3}}{1+\sqrt{3}}\,\delta x_2 = \frac{F\sqrt{3}}{1+\sqrt{3}}\,\delta x_2$$

Por lo tanto:

$$Q_{x_2} = \frac{F\sqrt{3}}{1+\sqrt{3}}$$

**Ecuación de movimiento:**

$$M^*\ddot{x}_2 - \frac{m_1 g \sqrt{3}}{1+\sqrt{3}} + K(x_2 - x_{2,0}) = \frac{F\sqrt{3}}{1+\sqrt{3}}$$

$$\boxed{M^*\ddot{x}_2 + K(x_2 - x_{2,0}) = \frac{\sqrt{3}}{1+\sqrt{3}}(m_1 g + F)}$$

con $M^* = \dfrac{4m_1}{(1+\sqrt{3})^2} + m_2$.

---
