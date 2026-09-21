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
  \draw[->, thick, gray] (0,2.1) -- (2.75,2.1) node[midway, above] {$x$};
  \draw[dashed, gray] (2.75,1.8) -- (2.75,2.3);
  \draw[->, thick, gray] (7.2,0) -- (7.2,-1.4) node[right] {$y_2 = x$};
  \draw[->, thick, gray] (8.1,0) -- (8.1,-3.6) node[right] {$y_3$};
\end{tikzpicture}
\end{document}
```

Un bloque de masa $m_1$ desliza sin fricción sobre una superficie horizontal. Está conectado a una pared fija izquierda mediante un resorte horizontal de constante $K$, longitud natural $\ell_0$ y ancho de bloque $b_1$.

Un cable inextensible conecta $m_1$ con una masa $m_2$ que cuelga verticalmente. El cable pasa por una polea fija en el borde del bloque. La restricción del cable impone que la velocidad horizontal de $m_1$ es igual a la velocidad vertical de $m_2$.

Debajo de $m_2$ hay un resorte de constante $K'$, longitud natural $\ell_0'$, que conecta $m_2$ con una tercera masa $m_3$ que cuelga libremente debajo.

**Resolución**
Se determinan las ecuaciones diferenciales de movimiento aplicando las ecuaciones de Lagrange para un sistema de partículas acopladas con dos grados de libertad.

**Paso 0 — Identificación del sistema**
- Tipo de sistema: T4 (sistema de tres partículas).
- Cuerpos presentes: Masa $m_1$ (traslación horizontal), masa $m_2$ (traslación vertical acoplada por cable a $m_1$) y masa $m_3$ (traslación vertical acoplada por resorte a $m_2$).

**Paso 1 — Coordenadas generalizadas y GDL**
Coordenadas posibles iniciales:

$$
(x_1, y_2, y_3)
$$

donde $x_1$ es la posición horizontal de $m_1$, $y_2$ la posición vertical descendente de $m_2$ y $y_3$ la posición vertical descendente de $m_3$.

Ecuación de restricción holónoma por el cable inextensible:

$$
\dot{y}_2 = \dot{x}_1 \implies y_2 = x_1 + C
$$


Grados de libertad:

$$
N = (\text{coordenadas}) - (\text{restricciones}) = 3 - 1 = 2
$$


Coordenadas independientes elegidas:

$$
q_1 = x, \quad q_2 = y_3
$$

donde $x_1 = x$ e $y_2 = x$ (tomando como origen el nivel de la polea/superficie).

**Paso 2 — Energía cinética**
Energías cinéticas de cada cuerpo:

$$
T_1 = \frac{1}{2} m_1 \dot{x}^2
$$


$$
T_2 = \frac{1}{2} m_2 \dot{y}_2^2 = \frac{1}{2} m_2 \dot{x}^2
$$


$$
T_3 = \frac{1}{2} m_3 \dot{y}_3^2
$$


Energía cinética total del sistema:

$$
T = T_1 + T_2 + T_3
$$


$$
T = \frac{1}{2} (m_1 + m_2) \dot{x}^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$


**Paso 3 — Energía potencial**
Energía potencial gravitatoria tomando como nivel de referencia cero la superficie horizontal:

$$
V_{g1} = 0
$$


$$
V_{g2} = -m_2 g x
$$


$$
V_{g3} = -m_3 g y_3
$$


Energía potencial elástica de los dos resortes:

$$
V_{k1} = \frac{1}{2} K (x - \ell_0)^2
$$


$$
V_{k2} = \frac{1}{2} K' (y_3 - x - \ell_0')^2
$$


Energía potencial total:

$$
V = \frac{1}{2} K (x - \ell_0)^2 + \frac{1}{2} K' (y_3 - x - \ell_0')^2 - m_2 g x - m_3 g y_3
$$


**Paso 4 — Lagrange respecto de $x$**
Derivadas respecto a la velocidad generalizada $\dot{x}$:

$$
\frac{\partial T}{\partial \dot{x}} = (m_1 + m_2) \dot{x}
$$


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) = (m_1 + m_2) \ddot{x}
$$


Derivadas respecto a la coordenada generalizada $x$:

$$
\frac{\partial T}{\partial x} = 0
$$


$$
\frac{\partial V}{\partial x} = K (x - \ell_0) - K' (y_3 - x - \ell_0') - m_2 g
$$


Ecuación de Lagrange para $x$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} = -\frac{\partial V}{\partial x}
$$


$$
(m_1 + m_2) \ddot{x} - 0 = -\left[ K (x - \ell_0) - K' (y_3 - x - \ell_0') - m_2 g \right]
$$


$$
(m_1 + m_2) \ddot{x} + K (x - \ell_0) - K' (y_3 - x - \ell_0') = m_2 g
$$


$$
(m_1 + m_2) \ddot{x} + (K + K') x - K' y_3 = K \ell_0 - K' \ell_0' + m_2 g
$$


**Paso 4 — Lagrange respecto de $y_3$**
Derivadas respecto a la velocidad generalizada $\dot{y}_3$:

$$
\frac{\partial T}{\partial \dot{y}_3} = m_3 \dot{y}_3
$$


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) = m_3 \ddot{y}_3
$$


Derivadas respecto a la coordenada generalizada $y_3$:

$$
\frac{\partial T}{\partial y_3} = 0
$$


$$
\frac{\partial V}{\partial y_3} = K' (y_3 - x - \ell_0') - m_3 g
$$


Ecuación de Lagrange para $y_3$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) - \frac{\partial T}{\partial y_3} = -\frac{\partial V}{\partial y_3}
$$


$$
m_3 \ddot{y}_3 - 0 = -\left[ K' (y_3 - x - \ell_0') - m_3 g \right]
$$


$$
m_3 \ddot{y}_3 + K' (y_3 - x - \ell_0') = m_3 g
$$


$$
m_3 \ddot{y}_3 - K' x + K' y_3 = K' \ell_0' + m_3 g
$$


**Paso 5 — EDOs finales**

$$
\boxed{ (m_1 + m_2) \ddot{x} + (K + K') x - K' y_3 = K \ell_0 - K' \ell_0' + m_2 g }
$$


$$
\boxed{ m_3 \ddot{y}_3 - K' x + K' y_3 = K' \ell_0' + m_3 g }
$$

