##### Ej. Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal. Está conectado a una pared fija izquierda mediante un resorte horizontal de constante $K$, longitud natural $\ell_0$ y ancho de bloque $b_1$. Un cable inextensible conecta $m_1$ con una masa $m_2$ que cuelga verticalmente. El cable pasa por una polea fija en el borde del bloque. La restricción del cable impone que la velocidad horizontal de $m_1$ es igual a la velocidad vertical de $m_2$. Debajo de $m_2$ hay un resorte de constante $K'$, longitud natural $\ell_0'$, que conecta $m_2$ con una tercera masa $m_3$ que cuelga libremente debajo.

```tikz
\usepackage{tikz}
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=0.9]
  % Pared fija izquierda
  \fill[gray!30] (-0.5,0) rectangle (0,2.5);
  \draw[thick] (0,0) -- (0,2.5);
  
  % Superficie horizontal
  \fill[gray!30] (0,-0.4) rectangle (6,0);
  \draw[thick] (0,0) -- (6,0);
  \draw[thick] (6,0) -- (6,-0.4);

  % Resorte K
  \draw[orange, thick, decorate, decoration={coil,aspect=0.4,segment length=5pt,amplitude=6pt}] (0,1) -- (2,1);
  \node[above, orange] at (1,1.2) {$K, \ell_0$};

  % Bloque m1
  \draw[fill=teal!30, teal!80!black, thick] (2,0.2) rectangle (3.5,1.8);
  \node at (2.75,1) {$m_1$};

  % Polea fija en el borde
  \draw[fill=gray!50, thick] (6,1) circle (0.3);
  \fill[black] (6,1) circle (0.05);

  % Cable inextensible
  \draw[thick] (3.5,1) -- (6,1) -- (6,-1);

  % Masa m2
  \draw[fill=teal!30, teal!80!black, thick] (5.4,-1.8) rectangle (6.6,-1);
  \node at (6,-1.4) {$m_2$};

  % Resorte K'
  \draw[orange, thick, decorate, decoration={coil,aspect=0.4,segment length=5pt,amplitude=5pt}] (6,-1.8) -- (6,-3.2);
  \node[right, orange] at (6.1,-2.5) {$K', \ell_0'$};

  % Masa m3
  \draw[fill=teal!30, teal!80!black, thick] (5.4,-4) rectangle (6.6,-3.2);
  \node at (6,-3.6) {$m_3$};

  % Coordenadas
  \draw[->, thick, gray] (0,2.1) -- (2.75,2.1) node[midway, above] {$x_1$};
  \draw[dashed, gray] (2.75,1.8) -- (2.75,2.3);
  \draw[->, thick, gray] (7.2,0) -- (7.2,-1.4) node[right] {$y_2$};
  \draw[->, thick, gray] (8.1,0) -- (8.1,-3.6) node[right] {$y_3$};
\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación del sistema**
- Tipo: T4 — sistema de tres partículas
- Cuerpos: $m_1$ (traslación horizontal), $m_2$ (traslación vertical, acoplada por cable), $m_3$ (traslación vertical, acoplada por resorte)

**Paso 1 — Coordenadas generalizadas y GDL**

Coordenadas posibles: $(x_1,\ y_2,\ y_3)$

Restricción holónoma por cable inextensible:

$$\dot{x}_1 = \dot{y}_2 \implies x_1 = y_2 + C_\rho$$

Grados de libertad:

$$N = 3 - 1 = 2$$

Coordenadas independientes: $q_1 = x_1$, $q_2 = y_3$

**Paso 2 — Energía cinética**

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

Aplicando $\dot{y}_2 = \dot{x}_1$:

$$T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{x}_1^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

**Paso 3 — Energía potencial**

Expresión general (gravitatoria + elástica), con $y_2 = x_1 - C_\rho$:

$$V = \frac{K}{2}\!\left(x_1 - \frac{b_1}{2} - \ell_0\right)^{\!2} - m_2 g\,(x_1 - C_\rho) - m_3 g\, y_3 + \frac{K'}{2}\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)^{\!2}$$

> Los términos $b_1/2$, $b_2/2$, $b_3/2$ corresponden a los semilargos de cada bloque que determinan la longitud libre de cada resorte. La constante $C_\rho$ proviene de integrar la restricción del cable.

**Paso 4 — Ecuaciones de Lagrange**

**Respecto de $x_1$:**

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}_1}\right) - \frac{\partial T}{\partial x_1} = -\frac{\partial V}{\partial x_1}$$

$$\frac{\partial V}{\partial x_1} = K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) - m_2 g - K'\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)$$

$$\boxed{m_1 \ddot{x}_1 + m_2 \ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

**Respecto de $y_3$:**

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{y}_3}\right) - \frac{\partial T}{\partial y_3} = -\frac{\partial V}{\partial y_3}$$

$$\frac{\partial V}{\partial y_3} = K'\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right) - m_3 g$$

$$\boxed{m_3\ddot{y}_3 = m_3 g - K'\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

Expandida:

$$\boxed{m_3\ddot{y}_3 = -K'\!\left(y_3 - x_1\right) + m_3 g - K'\!\!\left(C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

**Paso 5 — EDOs finales**

$$\boxed{m_1 \ddot{x}_1 + m_2 \ddot{x}_1 = -K\!\left(x_1 - \frac{b_1}{2} - \ell_0\right) + m_2 g + K'\!\left(y_3 - x_1 + C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$

$$\boxed{m_3\ddot{y}_3 = -K'\!\left(y_3 - x_1\right) + m_3 g - K'\!\!\left(C_\rho - \frac{b_2}{2} - \frac{b_3}{2} - \ell_0'\right)}$$
