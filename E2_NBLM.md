Tema detectado: T4 — Sistema de bloque con resorte horizontal y masa suspendida por cable

##### Ej. Un bloque de masa $m_1$ desliza sin fricción sobre un plano inclinado a $\theta$ respecto de la horizontal. El plano está fijo. El bloque está conectado a una pared vertical mediante un resorte horizontal de constante $K$ y longitud natural $\ell_0$. La distancia horizontal total de referencia es $d$ y la parte libre es $x_1$. Un cable inextensible conecta $m_1$ con una masa $m_2$ que cuelga verticalmente. El cable corre a lo largo del plano hasta una polea en el vértice y luego baja verticalmente. Nota: el cuerpo 1 solo se mueve en horizontal. El cuerpo 2 solo se mueve en vertical.

```tikz
\usepackage{tikz}
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=0.9]
  % Pared fija izquierda
  \fill[gray!30] (-0.5,0) rectangle (0,2.5);
  \draw[thick] (0,0) -- (0,2.5);

  % Superficie / Guía horizontal
  \fill[gray!30] (0,-0.3) rectangle (5,0);
  \draw[thick] (0,0) -- (5,0);

  % Resorte horizontal K
  \draw[orange, thick, decorate, decoration={coil,aspect=0.4,segment length=5pt,amplitude=6pt}] (0,1) -- (2,1);
  \node[above, orange] at (1,1.2) {$K, \ell_0$};

  % Bloque m1
  \draw[fill=teal!30, teal!80!black, thick] (2,0.2) rectangle (3.5,1.8);
  \node at (2.75,1) {$m_1$};

  % Plano inclinado de referencia (ángulo theta)
  \draw[dashed, gray] (2,0) -- (5,1.732) -- (5,0) -- cycle;
  \draw[gray] (2.6,0) arc (0:30:0.6) node[midway, right] {$\theta$};

  % Polea fija en el vértice
  \draw[fill=gray!50, thick] (5,1.732) circle (0.25);
  \fill[black] (5,1.732) circle (0.04);

  % Cable inextensible
  \draw[thick] (3.5,1) -- (5,1.732) -- (5,-0.5);

  % Masa m2
  \draw[fill=teal!30, teal!80!black, thick] (4.5,-1.5) rectangle (5.5,-0.5);
  \node at (5,-1) {$m_2$};

  % Ejes y cotas
  \draw[->, thick, gray] (0,2.1) -- (2.75,2.1) node[midway, above] {$x_1$};
  \draw[dashed, gray] (2.75,1.8) -- (2.75,2.3);
  \draw[->, thick, gray] (6,1.732) -- (6,-1) node[right] {$y_2$};
  \draw[dashed, gray] (5,-1) -- (6.2,-1);
\end{tikzpicture}
\end{document}
```

Un bloque de masa $m_1$ desliza sin fricción sobre un plano inclinado a $\theta$ respecto de la horizontal. El plano está fijo. El bloque está conectado a una pared vertical mediante un resorte horizontal de constante $K$ y longitud natural $\ell_0$. La distancia horizontal total de referencia es $d$ y la parte libre es $x_1$.

Un cable inextensible conecta $m_1$ con una masa $m_2$ que cuelga verticalmente. El cable corre a lo largo del plano hasta una polea en el vértice y luego baja verticalmente.

Nota: el cuerpo 1 solo se mueve en horizontal. El cuerpo 2 solo se mueve en vertical.

**Resolución**
Se obtiene la ecuación diferencial de movimiento aplicando las ecuaciones de Lagrange para un sistema acoplado con un grado de libertad.

**Paso 0 — Identificación del sistema**
- Tipo de sistema: T4 (sistema de dos partículas).
- Cuerpos presentes: Masa $m_1$ (traslación horizontal) y masa $m_2$ (traslación vertical).
- Tipo de movimiento: $m_1$ realiza movimiento rectilíneo horizontal y $m_2$ realiza movimiento rectilíneo vertical acoplado por cable.

**Paso 1 — Coordenadas generalizadas y GDL**
Coordenadas posibles iniciales:

$$
(x_1, y_2)
$$

donde $x_1$ es la posición horizontal del bloque $m_1$ respecto a la pared izquierda e $y_2$ es la posición vertical descendente de la masa $m_2$ respecto al nivel de la polea.

Ecuación de restricción holónoma impuesta por el cable inextensible de longitud $L$:

$$
(d - x_1) + y_2 = L \implies y_2 = x_1 + L - d
$$


Derivando respecto al tiempo:

$$
\dot{y}_2 = \dot{x}_1
$$


Grados de libertad:

$$
N = (\text{coordenadas}) - (\text{restricciones}) = 2 - 1 = 1
$$


Coordenada generalizada independiente elegida:

$$
q_1 = x
$$

donde $x_1 = x$ e $y_2 = x$ (salvo constantes aditivas).

**Paso 2 — Energía cinética**
Energías cinéticas de cada cuerpo:

$$
T_1 = \frac{1}{2} m_1 \dot{x}_1^2 = \frac{1}{2} m_1 \dot{x}^2
$$


$$
T_2 = \frac{1}{2} m_2 \dot{y}_2^2 = \frac{1}{2} m_2 \dot{x}^2
$$


Energía cinética total del sistema:

$$
T = T_1 + T_2
$$


$$
T = \frac{1}{2} m_1 \dot{x}^2 + \frac{1}{2} m_2 \dot{x}^2
$$


$$
T = \frac{1}{2} (m_1 + m_2) \dot{x}^2
$$


**Paso 3 — Energía potencial**
Energía potencial elástica del resorte horizontal de constante $K$:

$$
V_K = \frac{1}{2} K (x - \ell_0)^2
$$


Energía potencial gravitatoria:
- Para $m_1$: al ser su movimiento estrictamente horizontal, su altura permanece constante $\implies V_{g1} = 0$.
- Para $m_2$: tomando nivel de referencia cero en el eje horizontal de la polea, la cota vertical hacia abajo es $y_2 = x$:

$$
V_{g2} = -m_2 g y_2 = -m_2 g x
$$


Energía potencial total:

$$
V = V_K + V_{g1} + V_{g2}
$$


$$
V = \frac{1}{2} K (x - \ell_0)^2 - m_2 g x
$$


**Paso 4 — Lagrange respecto de $x$**
Derivada parcial de $T$ respecto a $\dot{x}$:

$$
\frac{\partial T}{\partial \dot{x}} = (m_1 + m_2) \dot{x}
$$


Derivada temporal de la derivada parcial anterior:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) = (m_1 + m_2) \ddot{x}
$$


Derivada parcial de $T$ respecto a $x$:

$$
\frac{\partial T}{\partial x} = 0
$$


Derivada parcial de $V$ respecto a $x$:

$$
\frac{\partial V}{\partial x} = K (x - \ell_0) - m_2 g
$$


Aplicando la ecuación de Lagrange:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} = -\frac{\partial V}{\partial x}
$$


$$
(m_1 + m_2) \ddot{x} - 0 = -\left[ K (x - \ell_0) - m_2 g \right]
$$


$$
(m_1 + m_2) \ddot{x} = -K (x - \ell_0) + m_2 g
$$


$$
(m_1 + m_2) \ddot{x} + K (x - \ell_0) = m_2 g
$$


$$
(m_1 + m_2) \ddot{x} + K x - K \ell_0 = m_2 g
$$


$$
(m_1 + m_2) \ddot{x} + K x = K \ell_0 + m_2 g
$$


**Paso 5 — EDOs finales**

$$
\boxed{ (m_1 + m_2) \ddot{x} + K x = K \ell_0 + m_2 g }
$$

