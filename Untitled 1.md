
### c) Esférico 3D (Polar 2D) $(\rho, \theta, \phi)$

``````cornell
::cue
Coordenadas esféricas · Vector de posición · Ecuaciones de transformación · Derivadas de versores · Componentes de velocidad · Aceleración en esféricas

¿Cómo se define el vector de posición de una partícula en coordenadas esféricas utilizando \rho como la variable radial?
¿Cuáles son las ecuaciones de transformación entre el sistema rectangular cartesiano y el esférico?
¿Cómo se obtienen las derivadas temporales de los versores de la base móvil en coordenadas esféricas?
¿Cuáles son las expresiones para la velocidad, rapidez al cuadrado y aceleración en este sistema de coordenadas?

$\vec{R} = \rho\hat{\mathbf{e}}_\rho$

---

![[ETN607T01.pdf#page=6&rect=55,554,346,762|ETN607T01, p.6]]
*Figura 1.12 · Coordenadas esféricas aplicadas a un volumen diferencial.*

::note

Posición $(\rho, \theta, \phi)$
$$\vec{R} = \rho \hat{e}_{\rho}$$
$$\vec{v} = \dfrac{d\vec{R}}{dt}$$

Ecuaciones de transformación
$$x = \rho \sin \theta \cos \phi$$
$$y = \rho \sin \theta \sin \phi$$
$$z = \rho \cos \theta$$

Ecuaciones de transformación
$$\rho^{2} = x^{2} + y^{2} + z^{2}$$
$$\text{tg}\,\phi = \dfrac{y}{x}$$
$$\theta = \text{arc}\,\cos \left( \dfrac{z}{\sqrt{x^{2}+y^{2}+z^{2}}} \right)$$

```ad-nota_3
title: Desarrollo formal
collapse: closed
**Coordenadas**
Posición: $(\rho, \theta, \phi)$

$$
\vec{R} = \rho\hat{\mathbf{e}}_\rho \quad \left| \quad
\begin{array}{l}
\hat{\mathbf{e}}_\rho \text{ no es de cte.} \\
\hat{\mathbf{e}}_\theta \text{ no es de cte.} \\
\hat{\mathbf{e}}_\phi \text{ no es de cte.}
\end{array}
\right.
$$


**Ecuaciones de transformación**

$$
\begin{aligned}
x &= \rho\,\text{sen}\,\theta\,\text{cos}\,\phi \\
y &= \rho\,\text{sen}\,\theta\,\text{sen}\,\phi \\
z &= \rho\,\text{cos}\,\theta
\end{aligned}
$$


![[pegar_imagen]]
*Figura 1.12 · Representación de un punto P en coordenadas esféricas tridimensionales.*

**Deducción de los versores y sus derivadas temporales**
Expresando los versores de la base esférica móvil en términos de la base cartesiana fija $(\hat{\mathbf{i}}, \hat{\mathbf{j}}, \hat{\mathbf{k}})$:

$$
\hat{\mathbf{e}}_\rho = \text{sen}\,\theta\,\text{cos}\,\phi\,\hat{\mathbf{i}} + \text{sen}\,\theta\,\text{sen}\,\phi\,\hat{\mathbf{j}} + \text{cos}\,\theta\,\hat{\mathbf{k}}
$$


$$
\hat{\mathbf{e}}_\theta = \text{cos}\,\theta\,\text{cos}\,\phi\,\hat{\mathbf{i}} + \text{cos}\,\theta\,\text{sen}\,\phi\,\hat{\mathbf{j}} - \text{sen}\,\theta\,\hat{\mathbf{k}}
$$


$$
\hat{\mathbf{e}}_\phi = -\text{sen}\,\phi\,\hat{\mathbf{i}} + \text{cos}\,\phi\,\hat{\mathbf{j}}
$$


Derivando parcialmente respecto a $\theta$ y $\phi$:

$$
\frac{\partial \hat{\mathbf{e}}_\rho}{\partial \theta} = \hat{\mathbf{e}}_\theta, \quad \frac{\partial \hat{\mathbf{e}}_\rho}{\partial \phi} = \text{sen}\,\theta\,\hat{\mathbf{e}}_\phi
$$


$$
\frac{\partial \hat{\mathbf{e}}_\theta}{\partial \theta} = -\hat{\mathbf{e}}_\rho, \quad \frac{\partial \hat{\mathbf{e}}_\theta}{\partial \phi} = \text{cos}\,\theta\,\hat{\mathbf{e}}_\phi
$$


$$
\frac{\partial \hat{\mathbf{e}}_\phi}{\partial \theta} = 0, \quad \frac{\partial \hat{\mathbf{e}}_\phi}{\partial \phi} = -(\text{sen}\,\theta\,\hat{\mathbf{e}}_\rho + \text{cos}\,\theta\,\hat{\mathbf{e}}_\theta)
$$


Aplicando la regla de la cadena para obtener las derivadas temporales totales:

$$
\dot{\hat{\mathbf{e}}}_\rho = \dot{\theta}\hat{\mathbf{e}}_\theta + \dot{\phi}\,\text{sen}\,\theta\,\hat{\mathbf{e}}_\phi
$$


$$
\dot{\hat{\mathbf{e}}}_\theta = -\dot{\theta}\hat{\mathbf{e}}_\rho + \dot{\phi}\,\text{cos}\,\theta\,\hat{\mathbf{e}}_\phi
$$


$$
\dot{\hat{\mathbf{e}}}_\phi = -\dot{\phi}(\text{sen}\,\theta\,\hat{\mathbf{e}}_\rho + \text{cos}\,\theta\,\hat{\mathbf{e}}_\theta)
$$


**Velocidad**
El vector velocidad $\vec{v}$ se obtiene diferenciando el vector de posición respecto al tiempo:

$$
\vec{v} = \dot{\vec{R}} = \dot{\rho}\hat{\mathbf{e}}_\rho + \rho\dot{\hat{\mathbf{e}}}_\rho = \dot{\rho}\hat{\mathbf{e}}_\rho + \rho\dot{\theta}\hat{\mathbf{e}}_\theta + \rho\dot{\phi}\,\text{sen}\,\theta\,\hat{\mathbf{e}}_\phi
$$


La rapidez al cuadrado (magnitud de la velocidad al cuadrado) es:

$$
v^2 = \dot{\rho}^2 + \rho^2\dot{\theta}^2 + \rho^2\,\text{sen}^2\theta\dot{\phi}^2
$$


**Aceleración**
Derivando sucesivamente el vector velocidad respecto al tiempo, se obtienen las componentes de la aceleración total $\vec{a} = a_\rho\hat{\mathbf{e}}_\rho + a_\theta\hat{\mathbf{e}}_\theta + a_\phi\hat{\mathbf{e}}_\phi$:

$$
a_\rho = \ddot{\rho} - \rho\dot{\theta}^2 - \rho\dot{\phi}^2\,\text{sen}^2\theta
$$


$$
a_\theta = \rho\ddot{\theta} + 2\dot{\rho}\dot{\theta} - \rho\dot{\phi}^2\,\text{sen}\,\theta\,\text{cos}\,\theta
$$


$$
a_\phi = \rho\ddot{\phi}\,\text{sen}\,\theta + 2\dot{\rho}\dot{\phi}\,\text{sen}\,\theta + 2\rho\dot{\theta}\dot{\phi}\,\text{cos}\,\theta
$$
```

```ad-note
title: Nota de corrección: Fundamentación física de la cinemática esférica
collapse: closed
De acuerdo con **Taylor (Cap. 1.7 y 4.8)** y **Goldstein (Cap. 1.2 y 1.4)**, el vector de posición de un punto en coordenadas esféricas se proyecta de manera exclusiva en la dirección radial $\hat{\mathbf{e}}_\rho$ como $\vec{R} = \rho\hat{\mathbf{e}}_\rho$. Al derivar con respecto al tiempo, el carácter móvil de los ejes coordenados genera de forma natural las componentes transversales de la velocidad y de la aceleración. Los términos de Coriolis y la aceleración centrípeta se derivan rigurosamente a partir de la variación temporal de la base móvil $(\hat{\mathbf{e}}_\rho, \hat{\mathbf{e}}_\theta, \hat{\mathbf{e}}_\phi)$ aquí deducida, garantizando la consistencia y ortogonalidad geométrica del sistema físico.
```
``````

>[!summary] Definición del sistema de coordenadas esféricas tridimensionales utilizando la variable radial $\rho$, sus ecuaciones de transformación, y la deducción matemática completa de su velocidad, rapidez y aceleración.
