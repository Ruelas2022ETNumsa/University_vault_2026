
%%< correcciones hechas: Se incorporó la formulación matemática rigurosa de las coordenadas hiperbólicas cilíndricas (u, v, z) con sus rangos de definición. Se dedujeron los factores de escala (h_u, h_v, h_z) paso a paso a partir del elemento de línea ds^2 y el tensor métrico, y se obtuvo la expresión final para la velocidad y la energía cinética clásica. Se incluyó una nota de corrección teórica basada en Wells (Cap. 2.2 y 2.4) y Goldstein (Cap. 1.4) detallando la ortogonalidad del sistema y su aplicación en problemas con límites elípticos e hiperbólicos confocales. %%

## e) Hiperbólicas cilíndricas

`````cornell
::cue
Coordenadas hiperbólicas cilíndricas · Factores de escala · Elemento de línea · Energía cinética · Sistema ortogonal · Tensor métrico

¿Cómo se definen las ecuaciones de transformación para el sistema de coordenadas hiperbólicas cilíndricas?
¿Cómo se calculan los factores de escala $h_u$ y $h_v$ empleando las derivadas de los vectores de posición?
¿Cuál es la forma del elemento de línea $ds^2$ y de la energía cinética clásica $T$ en este sistema?

$T = \frac{1}{2}m\left[ a^2(\text{senh}^2 u + \text{sen}^2 v)(\dot{u}^2 + \dot{v}^2) + \dot{z}^2 \right]$

ver también: T2 — Sistemas de coordenadas ortogonales

::note
**e) Hiperbólicas cilíndricas $(u, v, z)$**

Este sistema curvilíneo ortogonal se construye extendiendo las coordenadas hiperbólicas del plano $xy$ a lo largo del eje $Z$ cartesiano. Un punto $P$ en el espacio se define por las coordenadas $(u, v, z)$, donde los rangos admisibles de las variables son:
$$u \geq 0, \quad 0 \leq v < 2\pi, \quad -\infty < z < \infty$$

Las ecuaciones de transformación a coordenadas cartesianas rectangulares $(x, y, z)$ están dadas por:
$$
\begin{array}{l}
x = a\,\text{cosh}\,u\,\text{cos}\,v \\
y = a\,\text{senh}\,u\,\text{sen}\,v \\
z = z
\end{array}
$$
Donde $a$ es un parámetro de escala constante que representa la semidistancia focal de las hipérbolas y elipses confocales en el plano $xy$.

**Deducción de los factores de escala ($h_u, h_v, h_z$):**
El vector de posición es:
$$\vec{R} = a\,\text{cosh}\,u\,\text{cos}\,v\,\hat{\mathbf{i}} + a\,\text{senh}\,u\,\text{sen}\,v\,\hat{\mathbf{j}} + z\,\hat{\mathbf{k}}$$

Los factores de escala se obtienen mediante la norma de los vectores tangentes:
$$h_i = \left| \frac{\partial \vec{R}}{\partial q_i} \right| = \sqrt{\left(\frac{\partial x}{\partial q_i}\right)^2 + \left(\frac{\partial y}{\partial q_i}\right)^2 + \left(\frac{\partial z}{\partial q_i}\right)^2}$$

1. Para la coordenada $u$:
$$\frac{\partial x}{\partial u} = a\,\text{senh}\,u\,\text{cos}\,v, \quad \frac{\partial y}{\partial u} = a\,\text{cosh}\,u\,\text{sen}\,v, \quad \frac{\partial z}{\partial u} = 0$$
$$h_u = a\sqrt{\text{senh}^2 u\,\text{cos}^2 v + \text{cosh}^2 u\,\text{sen}^2 v}$$
Utilizando la identidad $\text{cosh}^2 u = 1 + \text{senh}^2 u$:
$$h_u = a\sqrt{\text{senh}^2 u\,\text{cos}^2 v + (1 + \text{senh}^2 u)\text{sen}^2 v} = a\sqrt{\text{senh}^2 u(\text{cos}^2 v + \text{sen}^2 v) + \text{sen}^2 v}$$
$$\therefore h_u = a\sqrt{\text{senh}^2 u + \text{sen}^2 v} = a\sqrt{\text{cosh}^2 u - \text{cos}^2 v}$$

2. Para la coordenada $v$:
$$\frac{\partial x}{\partial v} = -a\,\text{cosh}\,u\,\text{sen}\,v, \quad \frac{\partial y}{\partial v} = a\,\text{senh}\,u\,\text{cos}\,v, \quad \frac{\partial z}{\partial v} = 0$$
$$h_v = a\sqrt{\text{cosh}^2 u\,\text{sen}^2 v + \text{senh}^2 u\,\text{cos}^2 v}$$
Utilizando la identidad $\text{senh}^2 u = \text{cosh}^2 u - 1$:
$$h_v = a\sqrt{\text{cosh}^2 u\,\text{sen}^2 v + (\text{cosh}^2 u - 1)\text{cos}^2 v} = a\sqrt{\text{cosh}^2 u(\text{sen}^2 v + \text{cos}^2 v) - \text{cos}^2 v}$$
$$\therefore h_v = a\sqrt{\text{cosh}^2 u - \text{cos}^2 v} = a\sqrt{\text{senh}^2 u + \text{sen}^2 v}$$

3. Para la coordenada $z$:
$$h_z = 1$$

El elemento de arco diferencial al cuadrado ($ds^2$) se expresa como:
$$ds^2 = h_u^2 du^2 + h_v^2 dv^2 + h_z^2 dz^2 = a^2(\text{senh}^2 u + \text{sen}^2 v)(du^2 + dv^2) + dz^2$$

**Velocidad y Energía Cinética ($T$):**
El vector velocidad instantánea en la base curvilínea ortogonal es:
$$\vec{v} = h_u \dot{u}\hat{\mathbf{e}}_u + h_v \dot{v}\hat{\mathbf{e}}_v + h_z \dot{z}\hat{\mathbf{e}}_z = a\sqrt{\text{senh}^2 u + \text{sen}^2 v}\dot{u}\hat{\mathbf{e}}_u + a\sqrt{\text{senh}^2 u + \text{sen}^2 v}\dot{v}\hat{\mathbf{e}}_v + \dot{z}\hat{\mathbf{e}}_z$$

La rapidez al cuadrado es:
$$v^2 = a^2(\text{senh}^2 u + \text{sen}^2 v)(\dot{u}^2 + \dot{v}^2) + \dot{z}^2$$

Por tanto, la energía cinética $T$ de una partícula de masa $m$ es:
$$T = \frac{1}{2}m\left[ a^2(\text{senh}^2 u + \text{sen}^2 v)(\dot{u}^2 + \dot{v}^2) + \dot{z}^2 \right]$$

```ad-note
title: Nota de corrección: Ortogonalidad y simetría confocal hiperbólica
collapse: closed
Según **Wells (Cap. 2.2 y 2.4)** y **Goldstein (Cap. 1.4)**, el sistema de coordenadas hiperbólicas cilíndricas es ortogonal, lo cual se comprueba porque los vectores de base son mutuamente perpendiculares ($\hat{\mathbf{e}}_u \cdot \hat{\mathbf{e}}_v = 0$), lo que resulta en un tensor métrico diagonal:
$$g_{ij} = \begin{bmatrix} a^2(\text{senh}^2 u + \text{sen}^2 v) & 0 & 0 \\ 0 & a^2(\text{senh}^2 u + \text{sen}^2 v) & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
Este sistema curvilíneo es de gran utilidad en problemas físicos que poseen fronteras elípticas o hiperbólicas confocales (como la difracción en rendijas, el flujo de fluidos alrededor de obstáculos elípticos o problemas electrostáticos con electrodos elípticos), ya que las superficies coordinadas $u = \text{cte}$ corresponden a cilindros elípticos, mientras que las superficies $v = \text{cte}$ definen cilindros hiperbólicos confocales con focos en $(\pm a, 0, z)$.
```
`````

>[!summary] Formulación matemática de las coordenadas hiperbólicas cilíndricas y obtención de sus factores de escala y energía cinética a partir del tensor métrico.

***

¿Deseas continuar con la transcripción del siguiente subtítulo del apunte (`f) Otros HASTA g) Coordenadas No Lineales`) o prefieres revisar algún otro bloque de este tema? 🔍