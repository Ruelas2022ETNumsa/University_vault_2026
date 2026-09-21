##### Ej. Sistema de péndulo doble plano formado por dos masas $m_1$ y $m_2$ suspendidas secuencialmente por varillas de longitud $l$ en el campo gravitatorio

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    % Colores
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
    \node[maincolor, above left] at (0.6,-0.9) {$l$};

    % Ángulo theta
    \draw[dashed, gray] (1.2,-1.8) -- (1.2,-3.8);
    \draw[->, maincolor, thick] (0,-1.0) arc (-90:-56:1.0);
    \node[maincolor] at (0.25,-1.2) {$\theta$};

    % Segundo péndulo (m2, l, phi)
    \draw[thick, accentcolor] (1.2,-1.8) -- (2.6,-3.2);
    \draw[fill=orange!20, draw=accentcolor, thick] (2.6,-3.2) circle (0.18);
    \node[accentcolor, right=2pt] at (2.6,-3.2) {$m_2$};
    \node[accentcolor, above left] at (1.9,-2.5) {$l$};

    % Ángulo phi
    \draw[->, accentcolor, thick] (1.2,-2.8) arc (-90:-45:1.0);
    \node[accentcolor] at (1.45,-3.0) {$\phi$};

\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación**
Sistema mecánico dinámico no lineal de dos grados de libertad correspondiente a un péndulo doble plano. Se compone de dos masas puntuales ($m_1$ y $m_2$) unidas secuencialmente por dos varillas/hilos inextensibles y sin masa de igual longitud $l$, oscilando libremente bajo la acción de la gravedad. Tema: Ecuaciones de Lagrange.

**Paso 1 — Coordenadas y GDL**
Posiciones rectangulares de cada masa respecto al soporte articulado superior (origen $(0,0)$) tomando el eje $y$ orientado hacia abajo:

- Para la masa $m_1$:
  
$$
x_1 = l \sin\theta
$$

  
$$
y_1 = l \cos\theta
$$


- Para la masa $m_2$:
  
$$
x_2 = l \sin\theta + l \sin\phi
$$

  
$$
y_2 = l \cos\theta + l \cos\phi
$$


Derivadas temporales de las posiciones de la masa $m_2$:

$$
\dot{x}_2 = l \cos\theta \cdot \dot{\theta} + l \cos\phi \cdot \dot{\phi}
$$


$$
\dot{y}_2 = -l \sin\theta \cdot \dot{\theta} - l \sin\phi \cdot \dot{\phi}
$$


Número de grados de libertad:

$$
\text{GDL} = 2 \quad \text{con coordenadas independientes } (\theta, \phi)
$$


**Paso 2 — Energía cinética**
Energía cinética de la masa $m_1$:

$$
T_1 = \frac{1}{2} m_1 (\dot{x}_1^2 + \dot{y}_1^2) = \frac{1}{2} m_1 l^2 \dot{\theta}^2
$$


Energía cinética de la masa $m_2$:

$$
T_2 = \frac{1}{2} m_2 (\dot{x}_2^2 + \dot{y}_2^2) = \frac{1}{2} m_2 l^2 \left[ \dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) + \dot{\phi}^2 \right]
$$


Energía cinética total del sistema $T$:

$$
T = \frac{1}{2} m_1 l^2 \dot{\theta}^2 + \frac{1}{2} m_2 l^2 \left[ \dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) + \dot{\phi}^2 \right]
$$


**Paso 3 — Energía potencial**
Tomando como nivel de referencia $y = 0$ en el soporte fijo superior (con dirección $y$ descendente):

$$
V = -m_1 g y_1 - m_2 g y_2 = -m_1 g l \cos\theta - m_2 g l (\cos\theta + \cos\phi)
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicando la ecuación de Lagrange para cada coordenada generalizada independiente $q_r \in \{\theta, \phi\}$:

1. **Para la coordenada $\theta$:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}
$$


Derivada parcial respecto a $\dot{\theta}$:

$$
\frac{\partial T}{\partial \dot{\theta}} = (m_1 + m_2) l^2 \dot{\theta} + m_2 l^2 \dot{\phi} \cos(\theta - \phi)
$$


Derivada temporal:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) = (m_1 + m_2) l^2 \ddot{\theta} + m_2 l^2 \ddot{\phi} \cos(\theta - \phi) - m_2 l^2 \dot{\phi} \sin(\theta - \phi)(\dot{\theta} - \dot{\phi})
$$


Derivadas parciales de $T$ y $V$ respecto a $\theta$:

$$
\frac{\partial T}{\partial \theta} = -m_2 l^2 \dot{\theta}\dot{\phi} \sin(\theta - \phi)
$$


$$
-\frac{\partial V}{\partial \theta} = -(m_1 + m_2) g l \sin\theta
$$


Sustituyendo y simplificando:

$$
(m_1 + m_2) l^2 \ddot{\theta} + m_2 l^2 \ddot{\phi} \cos(\theta - \phi) + m_2 l^2 \dot{\phi}^2 \sin(\theta - \phi) + (m_1 + m_2) g l \sin\theta = 0
$$


2. **Para la coordenada $\phi$:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\phi}}\right) - \frac{\partial T}{\partial \phi} = -\frac{\partial V}{\partial \phi}
$$


Derivadas parciales respecto a $\dot{\phi}$ y $\phi$:

$$
\frac{\partial T}{\partial \dot{\phi}} = m_2 l^2 \dot{\phi} + m_2 l^2 \dot{\theta} \cos(\theta - \phi)
$$


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\phi}}\right) = m_2 l^2 \ddot{\phi} + m_2 l^2 \ddot{\theta} \cos(\theta - \phi) - m_2 l^2 \dot{\theta} \sin(\theta - \phi)(\dot{\theta} - \dot{\phi})
$$


$$
\frac{\partial T}{\partial \phi} = m_2 l^2 \dot{\theta}\dot{\phi} \sin(\theta - \phi)
$$


$$
-\frac{\partial V}{\partial \phi} = -m_2 g l \sin\phi
$$


Sustituyendo y simplificando:

$$
m_2 l^2 \ddot{\phi} + m_2 l^2 \ddot{\theta} \cos(\theta - \phi) - m_2 l^2 \dot{\theta}^2 \sin(\theta - \phi) + m_2 g l \sin\phi = 0
$$


**Paso 5 — EDOs finales**


$$
\boxed{(m_1 + m_2) l^2 \ddot{\theta} + m_2 l^2 \ddot{\phi} \cos(\theta - \phi) + m_2 l^2 \dot{\phi}^2 \sin(\theta - \phi) + (m_1 + m_2) g l \sin\theta = 0}
$$



$$
\boxed{m_2 l^2 \ddot{\phi} + m_2 l^2 \ddot{\theta} \cos(\theta - \phi) - m_2 l^2 \dot{\theta}^2 \sin(\theta - \phi) + m_2 g l \sin\phi = 0}
$$

