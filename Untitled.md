## 2.2 Sistemas de Coordenadas y Ecuaciones de Transformación

`````ad-tip
1. **Definición formal**
**Las longitudes $x_1, y_1$ localizan el punto $p$ relativo al sistema de referencia $X_1, Y_1$. De la misma manera, $x_2, y_2$ localizan el mismo punto relativo al sistema $X_2, Y_2$. Cada par de estas longitudes constituye un conjunto de coordenadas.**

2. **Idea clave**
**La formulación matemática de las leyes de la dinámica depende de la elección del sistema de coordenadas, siendo las ecuaciones de transformación el nexo formal que permite expresar propiedades físicas independientemente del marco de referencia.**

3. **Figura o diagrama**

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]
*Fig. 2-5*
*Representación de ejes oblicuos $Q_1, Q_2$ y sus respectivas coordenadas en relación con un sistema cartesiano rectangular.*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 12 | id: Fig. 2-5 | posición: inferior de la página
justificación: Esta figura ilustra la relación geométrica entre coordenadas oblicuas y rectangulares necesarias para definir transformaciones generales.%%

4. **Propiedades y Notación Formal**
En la mecánica clásica se emplean diversos sistemas de coordenadas según la simetría del problema físico, cuyas relaciones fundamentales son las siguientes:

*   **Sistema Cartesiano Rectangular (Tridimensional):** Relaciona las coordenadas de un punto en dos sistemas con un origen común mediante los cosenos directores $l_i, m_i, n_i$:
    $$
    \begin{array}{rcl}
    x_1 & = & x_0 + l_1 x_2 + l_2 y_2 + l_3 z_2 \\
    y_1 & = & y_0 + m_1 x_2 + m_2 y_2 + m_3 z_2 \\
    z_1 & = & z_0 + n_1 x_2 + n_2 y_2 + n_3 z_2
    \end{array}
    $$
*   **Sistema Cilíndrico:** Coordenadas $(\rho, \phi, z)$, de gran utilidad para sistemas con simetría axial:
    $$
    \begin{array}{rcl}
    x & = & \rho \cos \phi \\
    y & = & \rho \sin \phi \\
    z & = & z
    \end{array}
    $$
*   **Sistema Esférico:** Coordenadas $(r, \theta, \phi)$, ideal para el estudio de campos de fuerzas centrales:
    $$
    \begin{array}{rcl}
    x & = & r \sin \theta \cos \phi \\
    y & = & r \sin \theta \sin \phi \\
    z & = & r \cos \theta
    \end{array}
    $$

5. **Ejercicios Resueltos**

**Ejercicio 1 (Ejes Móviles y en Rotación):**
Un sistema de coordenadas $X_2, Y_2$ se desplaza con velocidad constante de componentes $(v_x, v_y)$ respecto al sistema fijo $X_1, Y_1$. Simultáneamente, el sistema móvil rota con una velocidad angular constante $\omega$ tal que el ángulo de rotación respecto a los ejes originales es $\theta = \omega t$. Deduzca las ecuaciones de transformación para las coordenadas de un punto $P$.

**Solución:**
Teniendo en cuenta el desplazamiento del origen $(v_x t, v_y t)$ y aplicando la rotación del sistema de ejes para un ángulo dependiente del tiempo, las coordenadas $(x_1, y_1)$ en el sistema fijo se transforman a partir de las coordenadas del sistema móvil mediante:
$$
\begin{array}{rcl}
x_1 & = & v_x t + x_2 \cos(\omega t) - y_2 \sin(\omega t) \\
y_1 & = & v_y t + x_2 \sin(\omega t) + y_2 \cos(\omega t)
\end{array}
$$
Estas ecuaciones muestran de manera explícita cómo cada coordenada en el sistema fijo es función de las coordenadas del sistema móvil y de la variable tiempo $t$.

**Ejercicio 2 (Sistemas de Ejes Oblicuos):**
Establezca las ecuaciones de transformación para relacionar un sistema de ejes oblicuos $Q_1, Q_2$ que forman ángulos conocidos $\alpha$ y $\beta$ con el eje horizontal de un sistema cartesiano rectangular $X, Y$.

**Solución:**
A partir de las proyecciones geométricas sobre los ejes oblicuos, las coordenadas rectangulares $(x, y)$ de un punto $P$ se expresan en términos de las coordenadas oblicuas $(q_1, q_2)$ como:
$$
\begin{array}{rcl}
x & = & q_1 \cos \alpha + q_2 \cos \beta \\
y & = & q_1 \sin \alpha + q_2 \sin \beta
\end{array}
$$
Este sistema representa un conjunto de coordenadas generalizadas alternativas donde los ejes de referencia no son ortogonales, permitiendo simplificar problemas de simetría angular oblicua. El diagrama geométrico correspondiente se ilustra a continuación:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.2]
  % Ejes rectangulares X, Y
  \draw[->, thick, gray] (-0.5,0) -- (4,0) node[right] {$X$};
  \draw[->, thick, gray] (0,-0.5) -- (0,4) node[above] {$Y$};
  
  % Ejes oblicuos Q1, Q2
  \draw[->, thick, teal] (0,0) -- (40:4.5) node[right] {$Q_1$};
  \draw[->, thick, orange] (0,0) -- (75:4.2) node[above right] {$Q_2$};
  
  % Punto P
  \coordinate (P) at (2.5, 3);
  \fill[teal] (P) circle (2pt) node[above right] {$P(x,y) \equiv P(q_1, q_2)$};
  
  % Proyecciones a ejes oblicuos
  \draw[dashed, gray] (P) -- (40:1.64) node[below right, black] {$q_1$};
  \draw[dashed, gray] (P) -- (75:2.42) node[left, black] {$q_2$};
  
  % Proyecciones a ejes rectangulares
  \draw[dashed, lightgray] (P) -- (2.5, 0) node[below, black] {$x$};
  \draw[dashed, lightgray] (P) -- (0, 3) node[left, black] {$y$};
  
  % Ángulos alpha y beta
  \draw[teal, ->] (1,0) arc (0:40:1) node[midway, right] {$\alpha$};
  \draw[orange, ->] (0.7,0) arc (0:75:0.7) node[midway, above right] {$\beta$};
\end{tikzpicture}
\end{document}
```

`````

*   ¿Deseas que analicemos la **deducción de las velocidades y aceleraciones** en coordenadas cilíndricas o esféricas a partir de estas ecuaciones de transformación?