

##### Ej. Sistema formado por un carro de masa $M$ en movimiento horizontal y un péndulo de masa $m$ y longitud $l$ suspendido de él

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex]
    % Colores
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared e indicador de origen izquierdo
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,2.5);
    \draw[thick] (0,0) -- (0,2.5);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (5.5,0);
    \draw[thick] (0,0) -- (5.5,0);

    % Carro M
    \draw[fill=teal!10, draw=maincolor, thick] (1.8,0.3) rectangle (3.8,1.5);
    \node[maincolor] at (2.8,0.9) {$M$};

    % Ruedas del carro
    \draw[thick, fill=gray!30] (2.2,0.15) circle (0.15);
    \draw[thick, fill=gray!30] (3.4,0.15) circle (0.15);

    % Pivote del péndulo en el carro
    \fill[maincolor] (2.8,1.5) circle (0.05);

    % Péndulo m
    \draw[thick, accentcolor] (2.8,1.5) -- (4.0,0.1);
    \draw[fill=orange!20, draw=accentcolor, thick] (4.0,0.1) circle (0.2);
    \node[accentcolor, right=2pt] at (4.0,0.1) {$m$};
    \node[accentcolor, above right] at (3.3,0.7) {$l$};

    % Línea de referencia vertical para ángulo theta
    \draw[dashed, gray] (2.8,1.5) -- (2.8,-0.2);
    \draw[->, accentcolor, thick] (2.8,0.7) arc (-90:-49:0.8);
    \node[accentcolor] at (3.05,0.5) {$\theta$};

    % Coordenada X
    \draw[->, maincolor, thick] (0,2.0) -- (2.8,2.0) node[midway, above] {$X$};
    \draw[dotted] (2.8,1.5) -- (2.8,2.2);
    \draw[dotted] (0,2.3) -- (0,1.8);

\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación**
Sistema mecánico dinámico acoplado no lineal de dos grados de libertad compuesto por un carro de masa $M$ que se desplaza horizontalmente sobre una superficie lisa y un péndulo de masa $m$ y longitud $l$ articulado en el carro que oscila libremente bajo la acción de la gravedad. Tema: Ecuaciones de Lagrange (Modelo matemático / EDO).

**Paso 1 — Coordenadas y GDL**
Coordenadas absolutas de los cuerpos:
- Carro $M$: posición horizontal $X$.
- Péndulo $m$: posición $(x_2, y_2)$.

Ecuaciones de transformación cinemática:

$$
x_2 = X + l \sin\theta
$$


$$
y_2 = H + l \cos\theta
$$


Derivadas temporales de las coordenadas del péndulo:

$$
\dot{x}_2 = \dot{X} + l \cos\theta \cdot \dot{\theta}
$$


$$
\dot{y}_2 = -l \sin\theta \cdot \dot{\theta}
$$


Número de grados de libertad:

$$
\text{GDL} = 2 \quad \text{con coordenadas independientes } (X, \theta)
$$


**Paso 2 — Energía cinética**
Energía cinética del carro $M$:

$$
T_1 = \frac{1}{2} M \dot{X}^2
$$


Energía cinética de la masa $m$:

$$
T_2 = \frac{1}{2} m (\dot{x}_2^2 + \dot{y}_2^2)
$$


$$
T_2 = \frac{1}{2} m \left[ (\dot{X} + l \cos\theta \cdot \dot{\theta})^2 + (-l \sin\theta \cdot \dot{\theta})^2 \right]
$$


$$
T_2 = \frac{1}{2} m \left( \dot{X}^2 + 2\dot{X} l \cos\theta \cdot \dot{\theta} + l^2 \cos^2\theta \cdot \dot{\theta}^2 + l^2 \sin^2\theta \cdot \dot{\theta}^2 \right)
$$


$$
T_2 = \frac{1}{2} m \left( \dot{X}^2 + 2\dot{X} l \cos\theta \cdot \dot{\theta} + l^2 \dot{\theta}^2 \right)
$$


Energía cinética total del sistema $T_T$:

$$
T_T = T_1 + T_2 = \frac{1}{2} M \dot{X}^2 + \frac{1}{2} m \left( \dot{X}^2 + 2\dot{X} l \cos\theta \cdot \dot{\theta} + l^2 \dot{\theta}^2 \right)
$$


**Paso 3 — Energía potencial**
Tomando como nivel de referencia la cota superior fija:

$$
V = m g y_2 = m g (H + l \cos\theta)
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicando la ecuación de Lagrange para las coordenadas generalizadas independientes $X$ y $\theta$:

1. **Para la coordenada $X$:**

$$
\frac{d}{dt}\left( \frac{\partial T}{\partial \dot{X}} \right) - \frac{\partial T}{\partial X} = -\frac{\partial V}{\partial X}
$$


Derivada parcial respecto a $\dot{X}$:

$$
\frac{\partial T}{\partial \dot{X}} = M \dot{X} + \frac{m}{2}(2\dot{X} + 2 l \cos\theta \cdot \dot{\theta}) = (M + m)\dot{X} + m l \cos\theta \cdot \dot{\theta}
$$


Derivando con respecto al tiempo $t$:

$$
\frac{d}{dt}\left( \frac{\partial T}{\partial \dot{X}} \right) = M \ddot{X} + m(\ddot{X} - l \sin\theta \cdot \dot{\theta}^2 + l \cos\theta \cdot \ddot{\theta})
$$


Como $\frac{\partial T}{\partial X} = 0$ y $\frac{\partial V}{\partial X} = 0$, la ecuación diferencial resulta:

$$
M \ddot{X} + m(\ddot{X} - l \sin\theta \cdot \dot{\theta}^2 + l \cos\theta \cdot \ddot{\theta}) = 0
$$


2. **Para la coordenada $\theta$:**

$$
\frac{d}{dt}\left( \frac{\partial T}{\partial \dot{\theta}} \right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}
$$


Derivadas parciales de $T$ y $V$:

$$
\frac{\partial T}{\partial \dot{\theta}} = m l \dot{X} \cos\theta + m l^2 \dot{\theta}
$$


$$
\frac{d}{dt}\left( \frac{\partial T}{\partial \dot{\theta}} \right) = m l \ddot{X} \cos\theta - m l \dot{X} \sin\theta \cdot \dot{\theta} + m l^2 \ddot{\theta}
$$


$$
\frac{\partial T}{\partial \theta} = -m l \dot{X} \dot{\theta} \sin\theta
$$


$$
-\frac{\partial V}{\partial \theta} = m g l \sin\theta
$$


Sustituyendo en Lagrange y simplificando por $m l$:

$$
l \ddot{\theta} + \ddot{X} \cos\theta + g \sin\theta = 0
$$


**Paso 5 — EDOs finales**


$$
\boxed{M \ddot{X} + m(\ddot{X} - l \sin\theta \cdot \dot{\theta}^2 + l \cos\theta \cdot \ddot{\theta}) = 0}
$$



$$
\boxed{l \ddot{\theta} + \ddot{X} \cos\theta + g \sin\theta = 0}
$$

