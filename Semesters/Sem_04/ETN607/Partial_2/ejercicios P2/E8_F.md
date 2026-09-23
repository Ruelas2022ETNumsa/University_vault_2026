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
