## Movimiento parabólico de una partícula

````ad-note
title: Complemento (Nivel C)

1. Definición formal
El movimiento de un proyectil es un caso de movimiento con aceleración constante en un plano, donde la aceleración horizontal es nula y la vertical es la de la gravedad $g$ [1]. La trayectoria descrita por la partícula es una parábola cuya ecuación se obtiene eliminando el tiempo de las ecuaciones de posición [2].

2. Idea clave
La trayectoria parabólica es el resultado de la superposición de un movimiento rectilíneo uniforme en el eje horizontal y un movimiento rectilíneo uniformemente acelerado en el eje vertical [1].

3. Figura o diagrama
```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]
  % Ejes
  \draw[->, thick, teal] (0,0) -- (5,0) node[right] {$x$};
  \draw[->, thick, teal] (0,0) -- (0,4) node[above] {$y$};
  
  % Trayectoria parabólica
  \draw[dashed, thick, teal] (0,0) parabola[bend pos=0.5] bend (2,2) (4,0);
  
  % Vectores iniciales
  \draw[->, very thick, orange] (0,0) -- (1,1) node[above right] {$\vec{v}_0$};
  \draw[thick, teal] (0.4,0) arc (0:45:0.4) node[right, pos=0.5] {$\alpha$};
  
  % Vértice (Altura máxima)
  \filldraw[teal] (2,2) circle (2pt);
  \draw[<->, teal] (2,0) -- (2,2) node[midway, left] {$h_{max}$};
  \node[above] at (2,2) {Vértice ($v_y = 0$)};
  
  % Aceleración
  \draw[->, thick, orange] (4.5,3) -- (4.5,2) node[right] {$\vec{g}$};
\end{tikzpicture}
\end{document}
```

4. Ejercicios resueltos

##### Ej. Determinación de la trayectoria y parámetros
Para una partícula lanzada con velocidad $v_0$ y ángulo $\alpha$ desde el origen:

**A. Ecuaciones de movimiento (Posición y Velocidad):**
Considerando $a_x = 0$ y $a_y = -g$ [1]:
$$\begin{array}{rcl} 
v_x(t) & = & v_0 \cos \alpha \\
v_y(t) & = & v_0 \sin \alpha - gt \\
x(t) & = & v_0 \cos \alpha \cdot t \\
y(t) & = & v_0 \sin \alpha \cdot t - \frac{1}{2}gt^2 
\end{array}$$

**B. Ecuación de la trayectoria $y(x)$:**
Despejando $t = \frac{x}{v_0 \cos \alpha}$ y sustituyendo en $y(t)$ [2]:
$$y = x \tan \alpha - \frac{g}{2v_0^2 \cos^2 \alpha}x^2$$
Esta ecuación tiene la forma $y = ax^2 + bx + c$, donde:
- $a = -\frac{g}{2v_0^2 \cos^2 \alpha}$ (relacionado con $g$, $v_0$ y el ángulo).
- $b = \tan \alpha$ (relacionado con el ángulo de lanzamiento).
- $c = y_0 = 0$ (posición inicial en el origen).

**C. Coordenadas del vértice $$x_v, y_v$$:**
El vértice corresponde a la altura máxima donde $v_y = 0$. El tiempo para alcanzarlo es $t = \frac{v_0 \sin \alpha}{g}$ [2].
$$\begin{array}{rcl}
x_v & = & \frac{v_0^2 \sin 2\alpha}{2g} \\
y_v & = & \frac{v_0^2 \sin^2 \alpha}{2g}
\end{array}$$
Físicamente, el vértice representa el punto de retorno en el eje vertical y el punto de simetría de la trayectoria en el vacío [2].

**D. Datos necesarios para determinación numérica:**
Para definir completamente la trayectoria se requieren:
1. Magnitud de la velocidad inicial $v_0$ [1].
2. Ángulo de lanzamiento $\alpha$ [1].
3. Aceleración de la gravedad $g$ (usualmente $9.8 \, m/s^2$) [3].
4. Posición inicial $(x_0, y_0)$ [1].

%%IMA-SRC | fuente: Alonso & Finn-Mecánica_Vol 1-1970-.pdf | página: 101-102 | id: Fig. 5-13 | posición: centro
justificación: Esta figura muestra la trayectoria parabólica y los vectores de velocidad y aceleración en diferentes puntos del movimiento.%%
````

