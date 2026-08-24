**%%< correcciones hechas: Corrección del subtítulo "velocidad" a "b) Velocidad - Vector" en la página 3 de la fuente ETN607T02.pdf, incorporando el bloque Cornell, el vector velocidad para coordenadas rectangulares, cilíndricas y esféricas (según la notación de la materia) y la Figura 2.5 correspondiente. %%**

## b) Velocidad - Vector

`````cornell
::cue
vector velocidad · coordenadas generalizadas · derivadas temporales · vectores unitarios
¿Cómo se define el vector velocidad instantánea de una partícula?
¿Cuáles son las expresiones para el vector velocidad en sistemas cilíndricos y esféricos?
Fórmula clave: $\vec{v} = \dot{r}\hat{e}_r + r\dot{\theta}\hat{e}_\theta + \dot{z}\hat{e}_z$

::note
**Velocidad - Vector**

El vector velocidad instantánea de una partícula se define operacionalmente como la derivada temporal de su vector de posición:

$$
\vec{v} = \dfrac{d\vec{R}}{dt} = \dot{\vec{R}}
$$


**a) Coordenadas rectangulares**
El vector de posición y su derivada temporal vienen dados por:

$$
\vec{R} = x\hat{i} + y\hat{j} + z\hat{k}
$$


$$
\vec{v} = \dot{x}\hat{i} + \dot{y}\hat{j} + \dot{z}\hat{k}
$$


$$
v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2
$$


**b) Coordenadas cilíndricas**
El vector de posición y la velocidad en coordenadas cilíndricas se expresan como:

$$
\vec{R} = r\hat{e}_r + z\hat{e}_z
$$

Considerando que los vectores unitarios son móviles, sus derivadas temporales son:

$$
\dot{\hat{e}}_r = \dot{\theta}\hat{e}_\theta \quad (\hat{e}_r \text{ no es constante})
$$


$$
\dot{\hat{e}}_z = 0 \quad (\hat{e}_z \text{ es constante})
$$

Sustituyendo y derivando el vector de posición, se obtiene el vector velocidad cilíndrico:

$$
\vec{v} = \dot{r}\hat{e}_r + r\dot{\theta}\hat{e}_\theta + \dot{z}\hat{e}_z
$$


$$
v^2 = \dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2
$$


```ad-note
title: Nota de velocidad transversal
collapse: closed
El término \\(r\dot{\theta}\\) corresponde a la velocidad transversal \\((v_\theta = \omega r)\\) de la partícula.
```

**c) Coordenadas esféricas**
Para el sistema esférico $(r, \theta, \phi)$, el vector de posición y su respectiva velocidad son:

$$
\vec{R} = r\hat{e}_r
$$


$$
\vec{v} = \dot{r}\hat{e}_r + r\dot{\theta}\hat{e}_\theta + r\dot{\phi}\operatorname{sen}\theta\hat{e}_\phi
$$


$$
v^2 = \dot{r}^2 + r^2\dot{\theta}^2 + r^2\dot{\phi}^2\operatorname{sen}^2\theta
$$


![[pegar_imagen]]
*Figura 2.5 · Vector velocidad en coordenadas cilíndricas $(r, \theta, z)$.*

IMA | fuente: ETN607_T02.pdf | página: 3 | id: Figura 2.5 | posición: abajo
`````

>[!summary] Transcripción y corrección matemática del vector velocidad instantánea de una partícula bajo coordenadas rectangulares, cilíndricas y esféricas.

***

*Nota de corrección: Se corrigió la transcripción original para asegurar la consistencia del vector velocidad en coordenadas curvilíneas. Se detallaron las derivadas de los vectores unitarios móviles cilíndricos $(\dot{\hat{e}}_r = \dot{\theta}\hat{e}_\theta)$ y se incorporó el desglose completo del vector velocidad cilíndrico y esférico tridimensional, alineándolos con la notación vectorial rigurosa de la materia y de Wells.*

***

¿Deseas que procedamos a revisar y estructurar la siguiente página o algún ejercicio en específico de este tema en Simulink? 📈

