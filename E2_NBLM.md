##### Ej. Sistema mecánico formado por dos cuñas $m_1$ y $m_2$ en contacto por interfaz inclinada a $60^\circ$ con resorte $K$

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
    % Colores
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda (guía vertical para cuerpo 2)
    \fill[pattern=north east lines] (-0.3,0) rectangle (0,3.5);
    \draw[thick] (0,0) -- (0,3.5);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (6,0);
    \draw[thick] (0,0) -- (6,0);

    % Pared derecha (apoyo del resorte)
    \fill[pattern=north east lines] (6,0) rectangle (6.3,1.5);
    \draw[thick] (6,0) -- (6,1.5);

    % Cuerpo 1 (cuña/bloque m1)
    \draw[fill=teal!10, draw=maincolor, thick] (2.0,0) -- (4.5,0) -- (4.5,1.732) -- (3.0,1.732) -- cycle;
    \node[maincolor] at (3.5,0.7) {$m_1$};

    % Resorte K conectado a m1
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=3mm, coil}, decorate, maincolor, thick] (4.5,0.866) -- (6,0.866);
    \node[above, maincolor] at (5.25,1.0) {$K$};

    % Cuerpo 2 (bloque/cuña m2)
    \draw[fill=orange!10, draw=accentcolor, thick] (0,1.155) -- (2.0,2.887) -- (0,2.887) -- cycle;
    \node[accentcolor] at (0.6,2.3) {$m_2$};

    % Ángulo de 60°
    \draw[thick, accentcolor] (2.0,0) ++(0.6,0) arc (0:60:0.6);
    \node[accentcolor] at (2.8,0.3) {$60^\circ$};

    % Coordenadas y cotas
    \draw[->, maincolor, thick] (0,-0.6) -- (2.0,-0.6) node[midway, below] {$X_1$};
    \draw[dotted] (2.0,0) -- (2.0,-0.8);
    \draw[dotted] (0,0) -- (0,-0.8);

    \draw[->, accentcolor, thick] (-0.6,3.2) -- (-0.6,1.155) node[midway, left] {$y_2$};
    \draw[dotted] (0,1.155) -- (-0.8,1.155);
    \draw[dotted] (0,3.2) -- (-0.8,3.2);

\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación**
Sistema mecánico translacional no linealmente acoplado cinemáticamente, compuesto por dos bloques cuña ($m_1$ y $m_2$) en contacto por una interfaz plana inclinada a $60^\circ$. El cuerpo 1 ($m_1$) se desplaza únicamente en dirección horizontal sobre la superficie lisa acoplado a un resorte $K$. El cuerpo 2 ($m_2$) está guiado verticalmente por la pared izquierda y se desplaza exclusivamente de forma vertical apoyado sobre la superficie inclinada de $m_1$. Tema: Ecuaciones de Lagrange.

**Paso 1 — Coordenadas y GDL**
Coordenadas posibles del sistema:


$$
N = (X_1, y_2)
$$


Donde $X_1$ es la posición horizontal de $m_1$ e $y_2$ es la posición vertical de $m_2$.

Restricción geométrica por contacto en la interfaz inclinada a $60^\circ$:


$$
\tan 60^\circ = \sqrt{3} = \frac{y_2}{B_2 - X_1} \implies B_2 - X_1 = \sqrt{3} y_2 \implies y_2 = \frac{B_2 - X_1}{\sqrt{3}}
$$


Derivando con respecto al tiempo:


$$
\dot{y}_2 = -\frac{1}{\sqrt{3}} \dot{X}_1
$$


Número de grados de libertad:


$$
\text{GDL} = N - \text{restricciones} = 2 - 1 = 1
$$


Coordenada independiente seleccionada: $X_1$.

**Paso 2 — Energía cinética**
Energía cinética total del sistema expresada con las coordenadas iniciales:


$$
T = \frac{1}{2} m_1 \dot{X}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2
$$


Sustituyendo la restricción cinemática $\dot{y}_2 = -\frac{1}{\sqrt{3}} \dot{X}_1$:


$$
T = \frac{1}{2} m_1 \dot{X}_1^2 + \frac{1}{2} m_2 \left(-\frac{\dot{X}_1}{\sqrt{3}}\right)^2 = \frac{1}{2} \left(m_1 + \frac{m_2}{3}\right) \dot{X}_1^2
$$


**Paso 3 — Energía potencial**
Energía potencial elástica y gravitatoria del sistema:


$$
V = m_1 g (0) + \frac{1}{2} K (B - B_1 - X_1 - l_0)^2 + m_2 g y_2
$$


Sustituyendo la restricción $y_2 = \frac{B_2 - X_1}{\sqrt{3}}$:


$$
V = \frac{1}{2} K (B - B_1 - X_1 - l_0)^2 + m_2 g \left(\frac{B_2 - X_1}{\sqrt{3}}\right)
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicando la ecuación de Lagrange para la coordenada generalizada independiente $X_1$:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{X}_1}\right) - \frac{\partial T}{\partial X_1} = -\frac{\partial V}{\partial X_1}
$$


Calculando las derivadas parciales de $T$:


$$
\frac{\partial T}{\partial \dot{X}_1} = \left(m_1 + \frac{m_2}{3}\right) \dot{X}_1 \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{X}_1}\right) = \left(m_1 + \frac{m_2}{3}\right) \ddot{X}_1
$$



$$
\frac{\partial T}{\partial X_1} = 0
$$


Calculando la derivada parcial de $V$:


$$
-\frac{\partial V}{\partial X_1} = +K(B - B_1 - X_1 - l_0) + \frac{m_2 g}{\sqrt{3}}
$$


**Paso 5 — EDOs finales**


$$
\boxed{\left(m_1 + \frac{m_2}{3}\right) \ddot{X}_1 = +K(B - B_1 - X_1 - l_0) + \frac{m_2 g}{\sqrt{3}}}
$$

