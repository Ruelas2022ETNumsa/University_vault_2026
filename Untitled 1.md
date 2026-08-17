## Sistema de coordenadas

``````ad-note
title: Complemento (Nivel C)

1. Definición formal
La posición de un punto $p$ puede ser localizada por varios conjuntos de magnitudes (longitudes, ángulos, funciones trigonométricas, áreas, etc.). Cada par o conjunto constituye un sistema de coordenadas [2, p. 12].

2. Idea clave y propiedades
* Las ecuaciones de transformación permiten expresar las coordenadas de un punto entre distintos sistemas, siendo fundamentales para representar magnitudes físicas en el sistema más conveniente [2, p. 13].
* **Invarianza y ortogonalidad**: En transformaciones entre sistemas cartesianos, el módulo de un vector es invariante ($x'_i x'_i = x_i x_i$) y los coeficientes de la transformación satisfacen la condición de ortogonalidad $a_{ij} a_{ik} = \delta_{jk}$ [5, p. 139].
* **Sistemas móviles**: Las ecuaciones de transformación pueden depender explícitamente del tiempo ($x_i = x_i(q_1, \dots, q_n, t)$) si el sistema de referencia está en movimiento [2, p. 11].

3. Figura o diagrama
[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=11]]
*Fig. 2-1*
*Sistemas rectangulares bidimensionales y sus relaciones de transformación.*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 11 | id: Fig. 2-1 | posición: superior
justificación: Esta figura muestra la relación geométrica y los ángulos de rotación entre dos sistemas de coordenadas rectangulares con un origen común.%%

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]
*Fig. 2-3*
*Coordenadas cilíndricas $(\rho, \phi, z)$.*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 12 | id: Fig. 2-3 | posición: centro
justificación: Ilustra la definición geométrica de las coordenadas cilíndricas en relación con el sistema cartesiano.%%

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]
*Fig. 2-4*
*Coordenadas esféricas $(r, \theta, \phi)$.*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 12 | id: Fig. 2-4 | posición: centro
justificación: Representa la definición de las coordenadas polares esféricas y su relación con las componentes cartesianas.%%

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]
  % Ejes originales X1, Y1
  \draw[thick, ->, >=stealth, teal] (0,0) -- (3,0) node[right] {$X_1$};
  \draw[thick, ->, >=stealth, teal] (0,0) -- (0,3) node[above] {$Y_1$};
  
  % Ejes rotados X2, Y2
  \draw[thick, ->, >=stealth, orange] (0,0) -- (30:3) node[right] {$X_2$};
  \draw[thick, ->, >=stealth, orange] (0,0) -- (120:3) node[above] {$Y_2$};
  
  % Punto P
  \fill[teal] (30:2) ++(120:1) circle (2pt) node[above right] {$P(x_1, y_1)$};
  \draw[dashed, gray] (30:2) ++(120:1) -- (30:2) node[below] {$x_2$};
  \draw[dashed, gray] (30:2) ++(120:1) -- (120:1) node[left] {$y_2$};
  
  % Angulo de rotacion \alpha
  \draw[thick, teal!60] (0.8,0) arc (0:30:0.8) node[midway, right=1pt] {$\alpha$};
  \draw[thick, teal!60] (0,0.8) arc (90:120:0.8) node[midway, above=1pt] {$\alpha$};
\end{tikzpicture}
\end{document}
```

4. Ejercicios resueltos
##### Ej. Obtención de las ecuaciones de transformación para un sistema rectangular rotado en el plano
Un sistema rectangular $(X_2, Y_2)$ tiene su origen coincidente con el sistema $(X_1, Y_1)$, pero sus ejes están rotados un ángulo constante $\alpha$ en sentido antihorario. Encontrar las ecuaciones de transformación que expresan las coordenadas de un punto en $(X_1, Y_1)$ en función de las coordenadas en $(X_2, Y_2)$ y verificar que la transformación es ortogonal.

**Resolución:**
Las coordenadas en el sistema $X_1, Y_1$ se relacionan geométricamente con las de $X_2, Y_2$ mediante:
$$
\begin{array}{rcl}
x_1 & = & x_2 \cos \alpha - y_2 \sin \alpha \\
y_1 & = & x_2 \sin \alpha + y_2 \cos \alpha
\end{array}
$$
La matriz de transformación $\mathbf{A}$ asociada es:
$$
\begin{array}{rcl}
\mathbf{A} & = & \begin{pmatrix} \cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha \end{pmatrix}
\end{array}
$$
Verificamos la condición de ortogonalidad del sistema aplicando $\mathbf{A}^T \mathbf{A} = \mathbf{I}$:
$$
\begin{array}{rcl}
\mathbf{A}^T \mathbf{A} & = & \begin{pmatrix} \cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha \end{pmatrix} \begin{pmatrix} \cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha \end{pmatrix} \\
& = & \begin{pmatrix} \cos^2 \alpha + \sin^2 \alpha & -\cos \alpha \sin \alpha + \sin \alpha \cos \alpha \\ -\sin \alpha \cos \alpha + \cos \alpha \sin \alpha & \sin^2 \alpha + \cos^2 \alpha \end{pmatrix} \\
& = & \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbf{I}
\end{array}
$$

##### Ej. Transformación a coordenadas cilíndricas y cálculo de la velocidad
Expresar las coordenadas cartesianas $(x, y, z)$ de una partícula en términos de las coordenadas cilíndricas $(\rho, \phi, z)$ y determinar el cuadrado de la velocidad $\vec{v}^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$ en este sistema de coordenadas.

**Resolución:**
Las relaciones de transformación de coordenadas a cilíndricas son:
$$
\begin{array}{rcl}
x & = & \rho \cos \phi \\
y & = & \rho \sin \phi \\
z & = & z
\end{array}
$$
Derivando respecto al tiempo $t$ utilizando la regla de la cadena:
$$
\begin{array}{rcl}
\dot{x} & = & \dot{\rho} \cos \phi - \rho \dot{\phi} \sin \phi \\
\dot{y} & = & \dot{\rho} \sin \phi + \rho \dot{\phi} \cos \phi \\
\dot{z} & = & \dot{z}
\end{array}
$$
Elevando al cuadrado cada componente de la velocidad:
$$
\begin{array}{rcl}
\dot{x}^2 & = & \dot{\rho}^2 \cos^2 \phi + \rho^2 \dot{\phi}^2 \sin^2 \phi - 2 \rho \dot{\rho} \dot{\phi} \cos \phi \sin \phi \\
\dot{y}^2 & = & \dot{\rho}^2 \sin^2 \phi + \rho^2 \dot{\phi}^2 \cos^2 \phi + 2 \rho \dot{\rho} \dot{\phi} \cos \phi \sin \phi \\
\dot{z}^2 & = & \dot{z}^2
\end{array}
$$
Sumando miembro a miembro para obtener la velocidad al cuadrado:
$$
\begin{array}{rcl}
\vec{v}^2 & = & \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \\
& = & \dot{\rho}^2 (\cos^2 \phi + \sin^2 \phi) + \rho^2 \dot{\phi}^2 (\sin^2 \phi + \cos^2 \phi) + \dot{z}^2 \\
& = & \dot{\rho}^2 + \rho^2 \dot{\phi}^2 + \dot{z}^2
\end{array}
$$
``````

