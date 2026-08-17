## 2.2 Sistemas de Coordenadas

`````ad-note
title: Complemento (Nivel C)

1. Definición formal
Un sistema de coordenadas es un conjunto de cantidades (tales como longitudes, ángulos, funciones trigonométricas o áreas) que permiten localizar la posición de un punto o la configuración de un sistema físico con respecto a un marco de referencia determinado.

2. Idea clave
Cada coordenada de un sistema de referencia es, por regla general, una función de todas y cada una de las coordenadas del otro sistema y del tiempo en caso de que los marcos de referencia se encuentren en movimiento relativo.

3. Figura o diagrama

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=11]]
*Fig. 2-3*
*Cylindrical Coordinates*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 11 | id: Fig. 2-3 | posición: superior
justificación: Esta figura ilustra la relación geométrica entre las coordenadas cartesianas y las cilíndricas.%%

[[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=11]]
*Fig. 2-4*
*Spherical Coordinates*
%%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 11 | id: Fig. 2-4 | posición: inferior
justificación: Esta figura muestra la definición espacial de las coordenadas esféricas y su proyección cartesiana.%%

4. Ejercicios resueltos

##### Ej. 1 Ecuaciones de transformación entre coordenadas cartesianas y cilíndricas
Deducir las relaciones de transformación y mostrar la correspondencia de velocidad entre el sistema cartesiano de tres dimensiones y el sistema cilíndrico de coordenadas.

**Resolución:**
Las relaciones que vinculan las coordenadas cartesianas $(x, y, z)$ con las cilíndricas $(p, \phi, z)$ se expresan de la siguiente forma:
\begin{array}{rcl}
x & = & p \cos \phi \\
y & = & p \sin \phi \\
z & = & z
\end{array}

Diferenciando con respecto al tiempo, las componentes cartesianas de la velocidad en función de las coordenadas y velocidades cilíndricas resultan:
\begin{array}{rcl}
\dot{x} & = & \dot{p} \cos \phi - p \dot{\phi} \sin \phi \\
\dot{y} & = & \dot{p} \sin \phi + p \dot{\phi} \cos \phi \\
\dot{z} & = & \dot{z}
\end{array}

##### Ej. 2 Ecuaciones de transformación en coordenadas esféricas
Deducir las ecuaciones de transformación para el sistema esférico de coordenadas $(r, \theta, \phi)$ con respecto al sistema cartesiano.

**Resolución:**
De acuerdo con la geometría del sistema esférico, donde $r$ es el radio vector, $\theta$ es la colatitud y $\phi$ es la longitud, las ecuaciones de transformación son:
\begin{array}{rcl}
x & = & r \sin \theta \cos \phi \\
y & = & r \sin \theta \sin \phi \\
z & = & r \cos \theta
\end{array}
`````
