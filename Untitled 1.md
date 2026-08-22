
### b) Cilíndrico 3D (Polar 2D) $(r, \theta, z)$

``````cornell
::cue
Coordenadas cilíndricas · Vector de posición · Ecuaciones de transformación · Derivadas de versores · No constancia de base

¿Cómo se define el vector de posición en coordenadas cilíndricas?
¿Por qué la base unitaria en el plano no es constante en el tiempo?
¿Cuáles son las derivadas de los versores de la base con respecto al tiempo?
$$
\vec{R} = r\hat{\mathbf{e}}_r + z\hat{\mathbf{e}}_z
\dot{\hat{\mathbf{e}}}_r = \dot{\theta}\hat{\mathbf{e}}_\theta$$

ver también: T2 — Sistemas de coordenadas

---

![[ETN607T01.pdf#page=5&rect=83,88,277,197|ETN607T01, p.5]]
*Figura 1.11 · Versores en coordenadas polares.*

::note

**Coordenadas**
Posición de un punto: $(r, \theta, z)$
$$
\vec{R} = r\hat{\mathbf{e}}_r + z\hat{\mathbf{e}}_z
\quad \left| \quad
\begin{array}{l}
\hat{\mathbf{e}}_r \text{ no es cte.} \\
\hat{\mathbf{e}}_\theta \text{ no es cte.} \\
\hat{\mathbf{e}}_z \text{ es cte.}
\end{array}
\right.
$$


![[ETN607T01.pdf#page=5&rect=72,200,340,390|ETN607T01, p.5]]

*Figura 1.10 · Punto P en coordenadas cilíndricas con su base de vectores unitarios local.*

---

**Ecuaciones de transformación**
$$
\begin{array}{l}
x &=& r\,\text{cos}\,\theta \\
y &=& r\,\text{sen}\,\theta \\
z &=& z
\end{array}
$$

---

A partir de la geometría en el plano $xy$ (Figura 1.11), podemos expresar los versores móviles en términos de la base cartesiana fija:
$$
\hat{\mathbf{e}}_r = 1\,\text{cos}\,\theta\hat{\mathbf{i}} + 1\,\text{sen}\,\theta\hat{\mathbf{j}}
$$
$$
\hat{\mathbf{e}}_\theta = 1\,\text{cos}\,\theta\hat{\mathbf{j}} + 1\,\text{sen}\,\theta(-\hat{\mathbf{i}}) = -\text{sen}\,\theta\hat{\mathbf{i}} + \text{cos}\,\theta\hat{\mathbf{j}}
$$

Derivando con respecto al tiempo (aplicando la regla de la cadena, ya que dependen del tiempo a través del ángulo $\theta(t)$):
$$
\dot{\hat{\mathbf{e}}}_r = -\text{sen}\,\theta\dot{\theta}\hat{\mathbf{i}} + \text{cos}\,\theta\dot{\theta}\hat{\mathbf{j}} = \dot{\theta}(-\text{sen}\,\theta\hat{\mathbf{i}} + \text{cos}\,\theta\hat{\mathbf{j}}) = \dot{\theta}\hat{\mathbf{e}}_\theta
$$
$$
\dot{\hat{\mathbf{e}}}_\theta = -\text{cos}\,\theta\dot{\theta}\hat{\mathbf{i}} - \text{sen}\,\theta\dot{\theta}\hat{\mathbf{j}} = -\dot{\theta}(\text{cos}\,\theta\hat{\mathbf{i}} + \text{sen}\,\theta\hat{\mathbf{j}}) = -\dot{\theta}\hat{\mathbf{e}}_r
$$




```ad-note
title: Nota de corrección: La naturaleza física de los versores cilíndricos y el vector de posición
collapse: closed
De acuerdo con **Alonso & Finn (Cap. 3.5)** y **Goldstein (Cap. 1.4)**, un error conceptual común en física es intentar formular el vector de posición en coordenadas cilíndricas como $\vec{R} = r\hat{\mathbf{e}}_r + \theta\hat{\mathbf{e}}_\theta + z\hat{\mathbf{e}}_z$. Físicamente, el ángulo $\theta$ es un parámetro angular de orientación (no una magnitud con dimensión de longitud) y el vector de posición no tiene componente en la dirección tangencial $\hat{\mathbf{e}}_\theta$; este se reduce estrictamente a la suma de la proyección radial en el plano y la altura vertical:
$$\vec{R} = r\hat{\mathbf{e}}_r + z\hat{\mathbf{e}}_z$$

Sin embargo, al obtener la velocidad $\vec{v} = \dot{\vec{R}}$, se debe aplicar la derivada temporal completa considerando que la base cilíndrica móvil en el plano $xy$ cambia de orientación en el tiempo ($\dot{\hat{\mathbf{e}}}_r \neq 0$):
$$\vec{v} = \dot{r}\hat{\mathbf{e}}_r + r\dot{\hat{\mathbf{e}}}_r + \dot{z}\hat{\mathbf{e}}_z = \dot{r}\hat{\mathbf{e}}_r + r\dot{\theta}\hat{\mathbf{e}}_\theta + \dot{z}\hat{\mathbf{e}}_z$$
Donde el término $r\dot{\theta}\hat{\mathbf{e}}_\theta$ representa la velocidad tangencial (o transversal) originada exclusivamente por la rotación de la base, sentando la base de la cinemática de partículas en coordenadas curvilíneas.
```

``````
## b) Cilíndrico 3D (Polar 2D) $(r, \theta, z)$

`````cornell
::cue
Coordenadas cilíndricas · Posición · Ecuaciones de transformación · Derivadas de versores · Versores móviles

¿Cómo se define el vector de posición en coordenadas cilíndricas?
¿Qué versores son constantes y cuáles dependen de la posición?
¿Cuáles son las derivadas temporales de los versores de base?

$$\vec{R} = r\hat{\mathbf{e}}_r + z\hat{\mathbf{e}}_z$$

::note
![[pegar_imagen]]
*Figura 1.10 · Representación de un punto P en coordenadas cilíndricas tridimensionales.*

**Coordenadas**
Posición $(r, \theta, z)$


$$
\vec{R} = r\hat{\mathbf{e}}_r + z\hat{\mathbf{e}}_z \quad \left| \quad
\begin{array}{l}
\hat{\mathbf{e}}_r \text{ no de cte} \\
\hat{\mathbf{e}}_\theta \text{ no de cte} \\
\hat{\mathbf{e}}_z \text{ de cte}
\end{array}
\right.
$$


**Ecuaciones de transformación**

$$
\begin{array}{l}
x = r\,\text{cos}\,\theta \\
y = r\,\text{sen}\,\theta \\
z = z
\end{array}
$$


![[pegar_imagen]]
*Figura 1.11 · Relación geométrica de los versores polares en el plano bidimensional.*


$$
\hat{\mathbf{e}}_r = 1\,\text{cos}\,\theta\hat{\mathbf{i}} + 1\,\text{sen}\,\theta\hat{\mathbf{j}}
$$


$$
\hat{\mathbf{e}}_\theta = 1\,\text{cos}\,\theta\hat{\mathbf{j}} + 1\,\text{sen}\,\theta(-\hat{\mathbf{i}}) = -\text{sen}\,\theta\hat{\mathbf{i}} + \text{cos}\,\theta\hat{\mathbf{j}}
$$


Derivando con respecto al tiempo:

$$
\dot{\hat{\mathbf{e}}}_r = -\text{sen}\,\theta\dot{\theta}\hat{\mathbf{i}} + \text{cos}\,\theta\dot{\theta}\hat{\mathbf{j}} = \dot{\theta}(-\text{sen}\,\theta\hat{\mathbf{i}} + \text{cos}\,\theta\hat{\mathbf{j}}) = \dot{\theta}\hat{\mathbf{e}}_\theta
$$


$$
\dot{\hat{\mathbf{e}}}_\theta = -\text{cos}\,\theta\dot{\theta}\hat{\mathbf{i}} - \text{sen}\,\theta\dot{\theta}\hat{\mathbf{j}} = -\dot{\theta}(\text{cos}\,\theta\hat{\mathbf{i}} + \text{sen}\,\theta\hat{\mathbf{j}}) = -\dot{\theta}\hat{\mathbf{e}}_r
$$


IMA | fuente: ETN607T01.pdf | página: 5 | id: Figura 1.10 | posición: superior izquierda
IMA | fuente: ETN607T01.pdf | página: 5 | id: Figura 1.11 | posición: centro izquierda
`````

>[!summary] Definición del sistema de coordenadas cilíndricas tridimensional, vector de posición, ecuaciones de transformación y derivadas temporales de sus versores de base.

***

¿Deseas continuar con la transcripción del siguiente subtítulo (`c) Esférico 3D`) en la página 6 o prefieres aplicar alguna corrección sobre este bloque? 🔍


%%< correcciones hechas: Se corrigió la notación de los versores de la base a formato negrita y sombrero (\hat{\mathbf{e}}_r, \hat{\mathbf{e}}_\theta, \hat{\mathbf{e}}_z) según las guías. Se incorporó una nota de corrección teórica basada en Alonso & Finn (Cap. 3.5) y Goldstein (Cap. 1.4) para aclarar por qué el vector de posición no contiene un término tangencial (\theta\hat{\mathbf{e}}_\theta) a pesar de que el vector velocidad sí posee componente en dicha dirección debido a la derivada de la base móvil. %%

## b) Cilíndrico 3D (Polar 2D) (r, \theta, z)

`````cornell
::cue
.
::note
.
.

`````

>[!summary] Definición del sistema de coordenadas cilíndricas tridimensional, ecuaciones de transformación y derivación temporal de sus versores móviles.

***

¿Deseas que procedamos con el siguiente subtítulo ("c) Esférico 3D HASTA ...") o prefieres revisar algún detalle antes de continuar? 🔍