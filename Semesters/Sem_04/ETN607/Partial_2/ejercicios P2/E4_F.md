Un carro de masa $M$ rueda sin fricción sobre una superficie horizontal. Sobre el carro está articulado un péndulo simple de longitud $\ell$ con masa puntual $m$ en su extremo, que oscila en el plano vertical. El punto de articulación se encuentra a altura $H$ sobre el suelo.

Hallar las ecuaciones de movimiento de Lagrange del sistema (2 GDL: $x$, $\theta$).

---

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda (referencia origen)
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,3.0);
    \draw[thick] (0,0) -- (0,3.0);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (6.0,0);
    \draw[thick] (0,0) -- (6.0,0);

    % Carro M
    \draw[fill=teal!10, draw=maincolor, thick] (1.8,0.35) rectangle (3.8,1.5);
    \node[maincolor] at (2.8,0.92) {$M$};

    % Ruedas
    \draw[thick, fill=gray!30] (2.2,0.18) circle (0.18);
    \draw[thick, fill=gray!30] (3.4,0.18) circle (0.18);

    % Pivote del péndulo
    \fill[maincolor] (2.8,1.5) circle (0.06);

    % Línea vertical de referencia (ángulo theta)
    \draw[dashed, gray] (2.8,1.5) -- (2.8,2.8);

    % Varilla del péndulo — hacia arriba
    \draw[thick, accentcolor] (2.8,1.5) -- (4.1,2.65);
    \node[accentcolor, above right] at (3.45,2.1) {$\ell$};

    % Masa m (círculo) — arriba
    \draw[thick, fill=orange!20, draw=accentcolor] (4.1,2.65) circle (0.2);
    \node[accentcolor, right=4pt] at (4.1,2.65) {$m$};

    % Ángulo theta — desde vertical hacia arriba
    \draw[->, accentcolor] (2.8,2.15) arc (90:55:0.65);
    \node[accentcolor] at (3.1,2.35) {$\theta$};

    % Cota H — altura del pivote
    \draw[<->, gray] (4.8,0) -- (4.8,1.5) node[midway, right] {$H$};
    \draw[dotted] (3.8,1.5) -- (4.9,1.5);

    % Coordenada x — posición horizontal del carro
    \draw[->, maincolor, thick] (0,2.2) -- (2.8,2.2) node[midway, above] {$x$};
    \draw[dotted] (0,0) -- (0,2.4);
    \draw[dotted] (2.8,1.5) -- (2.8,2.4);

\end{tikzpicture}
\end{document}
```

---

## Coordenadas y GDL

Coordenadas posibles del sistema:

$$N = (x,\ \theta)$$

Sin restricciones adicionales — ambas coordenadas son independientes.

Número de grados de libertad:

$$\text{GDL} = 2 \quad \text{con coordenadas independientes } (x,\,\theta)$$

Posición absoluta de $m$:

$$x_2 = x + \ell\sin\theta \qquad y_2 = H + \ell\cos\theta$$

Velocidades de $m$:

$$\dot{x}_2 = \dot{x} + \ell\cos\theta\,\dot{\theta} \qquad \dot{y}_2 = -\ell\sin\theta\,\dot{\theta}$$

---

## Energía cinética

$$T_M = \frac{M}{2}\dot{x}^2$$

$$T_m = \frac{m}{2}(\dot{x}_2^2 + \dot{y}_2^2) = \frac{m}{2}\!\left(\dot{x}^2 + 2\dot{x}\ell\cos\theta\,\dot{\theta} + \ell^2\cos^2\theta\,\dot{\theta}^2 + \ell^2\sin^2\theta\,\dot{\theta}^2\right)$$

$$\boxed{T = \frac{M}{2}\dot{x}^2 + \frac{m}{2}\!\left(\dot{x}^2 + 2\dot{x}\ell\cos\theta\,\dot{\theta} + \ell^2\dot{\theta}^2\right)}$$

---

## Energía potencial

$$\boxed{V = mg(H + \ell\cos\theta)}$$

---

## Ecuaciones de Lagrange

### Para $x$

$$\frac{\partial T}{\partial \dot{x}} = (M+m)\dot{x} + m\ell\cos\theta\,\dot{\theta} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}}\right) = (M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2$$

$$\frac{\partial T}{\partial x} = 0 \qquad \frac{\partial V}{\partial x} = 0$$

$$\boxed{(M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2 = 0}$$

### Para $\theta$

$$\frac{\partial T}{\partial \dot{\theta}} = m\ell\dot{x}\cos\theta + m\ell^2\dot{\theta} \implies \frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m\ell\ddot{x}\cos\theta - m\ell\dot{x}\sin\theta\,\dot{\theta} + m\ell^2\ddot{\theta}$$

$$\frac{\partial T}{\partial \theta} = -m\ell\dot{x}\dot{\theta}\sin\theta \qquad -\frac{\partial V}{\partial \theta} = mg\ell\sin\theta$$

Sustituyendo en Lagrange (los términos $-m\ell\dot{x}\sin\theta\,\dot{\theta}$ y $+m\ell\dot{x}\dot{\theta}\sin\theta$ se anulan en este ejercicio, pero se mantienen por consistencia con el método general):

$$m\ell\ddot{x}\cos\theta - m\ell\dot{x}\sin\theta\,\dot{\theta} + m\ell^2\ddot{\theta} + m\ell\dot{x}\dot{\theta}\sin\theta = mg\ell\sin\theta$$

Simplificando por $m\ell$:

$$\boxed{\ell\ddot{\theta} + \ddot{x}\cos\theta - \dot{x}\sin\theta\,\dot{\theta} + \dot{x}\dot{\theta}\sin\theta + g\sin\theta = 0}$$

---

## EDOs finales

$$\boxed{(M+m)\ddot{x} + m\ell\cos\theta\,\ddot{\theta} - m\ell\sin\theta\,\dot{\theta}^2 = 0}$$

$$\boxed{\ell\ddot{\theta} + \ddot{x}\cos\theta - \dot{x}\sin\theta\,\dot{\theta} + \dot{x}\dot{\theta}\sin\theta + g\sin\theta = 0}$$
