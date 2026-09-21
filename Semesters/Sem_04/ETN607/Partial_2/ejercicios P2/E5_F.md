# E5_F

Dos masas puntuales $m_1$ y $m_2$ forman un péndulo doble planar. Ambas varillas rígidas sin masa tienen la misma longitud $\ell$. $m_1$ está articulada al techo y forma ángulo $\theta$ con la vertical; $m_2$ está articulada al extremo inferior de la primera varilla y forma ángulo $\phi$ con la vertical.

Hallar las ecuaciones de movimiento de Lagrange del sistema.

---

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

---

**Paso 0 — Identificación**
Sistema mecánico dinámico no lineal de dos grados de libertad correspondiente a un péndulo doble plano. Se compone de dos masas puntuales ($m_1$ y $m_2$) unidas secuencialmente por dos varillas rígidas inextensibles y sin masa de igual longitud $\ell$, oscilando libremente bajo la acción de la gravedad. Tema: Ecuaciones de Lagrange.

**Paso 1 — Coordenadas y GDL**
Posiciones rectangulares de cada masa respecto al soporte articulado superior (origen $(0,0)$) tomando el eje $y$ orientado hacia abajo:

- Para la masa $m_1$:

$$x_1 = \ell\sin\theta \qquad y_1 = \ell\cos\theta$$

- Para la masa $m_2$:

$$x_2 = \ell\sin\theta + \ell\sin\phi \qquad y_2 = \ell\cos\theta + \ell\cos\phi$$

Derivadas temporales de las posiciones de $m_2$:

$$\dot{x}_2 = \ell\cos\theta\,\dot{\theta} + \ell\cos\phi\,\dot{\phi}$$

$$\dot{y}_2 = -\ell\sin\theta\,\dot{\theta} - \ell\sin\phi\,\dot{\phi}$$

Número de grados de libertad:

$$\text{GDL} = 2 \quad \text{con coordenadas generalizadas } (\theta,\,\phi)$$

---

**Paso 2 — Energía cinética**

Energía cinética de $m_1$:

$$T_1 = \frac{1}{2}m_1\!\left(\dot{x}_1^2 + \dot{y}_1^2\right) = \frac{1}{2}m_1\ell^2\dot{\theta}^2$$

Energía cinética de $m_2$:

$$T_2 = \frac{1}{2}m_2\!\left(\dot{x}_2^2 + \dot{y}_2^2\right) = \frac{1}{2}m_2\ell^2\!\left[\dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta-\phi) + \dot{\phi}^2\right]$$

Energía cinética total:

$$\boxed{T = \frac{1}{2}m_1\ell^2\dot{\theta}^2 + \frac{1}{2}m_2\ell^2\!\left[\dot{\theta}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta-\phi) + \dot{\phi}^2\right]}$$

---

**Paso 3 — Energía potencial**

Tomando como referencia $y = 0$ en el soporte fijo superior con eje $y$ orientado hacia abajo — las masas tienen coordenada $y$ positiva y energía potencial negativa respecto al origen. Si el docente ubica la referencia por debajo del sistema, los signos se invierten pero las EDOs resultantes son idénticas.

$$\boxed{V = -m_1 g\ell\cos\theta - m_2 g\ell(\cos\theta + \cos\phi)}$$

---

**Paso 4 — Ecuaciones de Lagrange**

### Respecto de $\theta$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}$$

$$\frac{\partial T}{\partial \dot{\theta}} = (m_1 + m_2)\ell^2\dot{\theta} + m_2\ell^2\dot{\phi}\cos(\theta-\phi)$$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) = (m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) - m_2\ell^2\dot{\phi}\sin(\theta-\phi)(\dot{\theta}-\dot{\phi})$$

$$\frac{\partial T}{\partial \theta} = -m_2\ell^2\dot{\theta}\dot{\phi}\sin(\theta-\phi)$$

$$-\frac{\partial V}{\partial \theta} = -(m_1+m_2)g\ell\sin\theta$$

Sustituyendo y simplificando:

$$\boxed{(m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) + m_2\ell^2\dot{\phi}^2\sin(\theta-\phi) + (m_1+m_2)g\ell\sin\theta = 0}$$

### Respecto de $\phi$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\phi}}\right) - \frac{\partial T}{\partial \phi} = -\frac{\partial V}{\partial \phi}$$

$$\frac{\partial T}{\partial \dot{\phi}} = m_2\ell^2\dot{\phi} + m_2\ell^2\dot{\theta}\cos(\theta-\phi)$$

$$\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\phi}}\right) = m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}\sin(\theta-\phi)(\dot{\theta}-\dot{\phi})$$

$$\frac{\partial T}{\partial \phi} = m_2\ell^2\dot{\theta}\dot{\phi}\sin(\theta-\phi)$$

$$-\frac{\partial V}{\partial \phi} = -m_2 g\ell\sin\phi$$

Sustituyendo y simplificando:

$$\boxed{m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}^2\sin(\theta-\phi) + m_2 g\ell\sin\phi = 0}$$

---

**Paso 5 — EDOs finales**

$$\boxed{(m_1+m_2)\ell^2\ddot{\theta} + m_2\ell^2\ddot{\phi}\cos(\theta-\phi) + m_2\ell^2\dot{\phi}^2\sin(\theta-\phi) + (m_1+m_2)g\ell\sin\theta = 0}$$

$$\boxed{m_2\ell^2\ddot{\phi} + m_2\ell^2\ddot{\theta}\cos(\theta-\phi) - m_2\ell^2\dot{\theta}^2\sin(\theta-\phi) + m_2 g\ell\sin\phi = 0}$$
