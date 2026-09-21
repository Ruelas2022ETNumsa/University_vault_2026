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
