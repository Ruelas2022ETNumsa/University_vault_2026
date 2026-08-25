%%< correcciones hechas %%

## 2.1 Introducción

`````cornell
::cue
dinámica clásica · métodos de formulación · grados de libertad · modelo matemático
¿Cuáles son las formulaciones equivalentes de la dinámica clásica?
¿Cuál es el objetivo principal al analizar un sistema dinámico de partículas?
Fórmula clave: $\sum \vec{F} = m \vec{a}$
ver también: d'Alembert — error común: D' Lambert

::note
**Introducción a la Dinámica de Partículas**

La **dinámica clásica** es la rama que estudia el movimiento de los cuerpos bajo las **leyes de Newton**. Para una sola partícula $P = 1$, su movimiento en el espacio tridimensional inercial se describe mediante un máximo de **$3$ grados de libertad $N \le 3$ GDL**.

Los enfoques y principios fundamentales de la dinámica son:

$$
\substack{\displaystyle\text{Enfoques de}\\\displaystyle\text{la Dinámica}}
\begin{cases}
\text{- Newton (Mecánica vectorial)} \\[4pt]
\text{- Lagrange (Mecánica analítica)} \\[4pt]
\text{- Conservación de Energía} \\[4pt]
\text{- Trabajo virtual} \\[4pt]
\text{- d'Alembert (Principio dinámico)} \\[4pt]
\text{- Euler}
\end{cases}
\quad \left| \quad
\begin{array}{l}
\text{P = 1 Partícula} \\
\text{N } \le \text{ 3 GDL}
\end{array}
\right.
$$

El objetivo principal al analizar un **sistema dinámico** consiste en formular sus ecuaciones de movimiento para plantear el **modelo matemático**:

$$
\substack{\displaystyle\text{Objetivo:}\\\displaystyle\text{Hallar}}
\begin{cases}
\text{- EDO (Ecuación Diferencial Ordinaria)} \\[4pt]
\text{- Mod Mat (Modelo Matemático)}
\end{cases}
$$

`````

>[!summary] Enfoques clásicos para el análisis de una partícula, orientados a la obtención del modelo matemático y sus EDOs.

---

## 2.2 Ecuaciones de Lagrange

`````cornell
::cue
segunda ley de Newton · sistema rectangular · sistema cilíndrico · aceleración curvilínea · fuerzas de ligadura
¿Cómo se formulan las ecuaciones de movimiento de Newton en sistemas rectangular y cilíndrico?
¿Cuáles son las tres grandes limitaciones de la formulación newtoniana que justifican el método de Lagrange?
Fórmula clave: $\vec{F} = m\vec{a}$, $\vec{a} = (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta + \ddot{z}\mathbf{e}_z$

::note
**Newton: $\vec{F} = m\vec{a}$**

**a) Sistema rectangular**

$$
\Sigma F_x = m\ddot{x}
$$


$$
\Sigma F_y = m\ddot{y}
$$


$$
\Sigma F_z = m\ddot{z}
$$


```ad-note
title: Dificultades de la formulación newtoniana
collapse: closed
El planteamiento directo de la segunda ley de Newton resulta muy complejo en la práctica debido a:
1. **Carácter vectorial:** Exige proyectar vectorialmente todas las fuerzas y aceleraciones en componentes.
2. **Cálculo de la aceleración:** Obtener las componentes de la aceleración $\vec{a}$ en sistemas no cartesianos (curvilíneos) es sumamente laborioso.
3. **Fuerzas de ligadura (internas):** Newton requiere incluir explícitamente las fuerzas de restricción en las ecuaciones, las cuales son desconocidas a priori.
```

**b) Sistema cilíndrico**
La posición de una partícula en coordenadas cilíndricas se define como:

$$
\vec{r} = r\mathbf{e}_r + z\mathbf{e}_z
$$


Derivando respecto al tiempo, obtenemos la velocidad:

$$
\vec{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta + \dot{z}\mathbf{e}_z
$$


Derivando nuevamente, la aceleración en este sistema curvilíneo resulta:

$$
\vec{a} = (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta + \ddot{z}\mathbf{e}_z
$$


Por lo tanto, las ecuaciones de movimiento de Newton en componentes cilíndricas son:

$$
\Sigma F_r = m(\ddot{r} - r\dot{\theta}^2)
$$


$$
\Sigma F_\theta = m(r\ddot{\theta} + 2\dot{r}\dot{\theta})
$$


$$
\Sigma F_z = m\ddot{z}
$$


```ad-note
title: Comentario
collapse: closed
La aceleración transversal $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}$ contiene el término de Coriolis $2\dot{r}\dot{\theta}$, el cual surge de manera natural al derivar los vectores unitarios móviles respecto al tiempo: $\dot{\mathbf{e}}_r = \dot{\theta}\mathbf{e}_\theta$ y $\dot{\mathbf{e}}_\theta = -\dot{\theta}\mathbf{e}_r$.
```
`````

>[!summary] Planteamiento de las ecuaciones de movimiento de Newton en sistemas rectangular y cilíndrico, destacando la complejidad de la aceleración curvilínea y la presencia de fuerzas de ligadura.

---

%%< correcciones hechas: Corrección del subtítulo "c) sistema estricto" a "c) Sistema esférico". %%
## c) Sistema esférico

`````cornell
::cue
coordenadas esféricas · ecuaciones de transformación · variables independientes
¿Cómo se definen las coordenadas esféricas $r$, $\theta$ y $\phi$?
¿Cuáles son las ecuaciones de transformación para este sistema?
Fórmula clave: $x = r \operatorname{sen}\theta \cos\phi$

::note
**Posición $(r, \theta, \phi)$**

Las coordenadas esféricas de una partícula consisten en una distancia radial $r$, un ángulo polar $\theta$ (colatitud) y un ángulo acimutal $\phi$.

**E.T. (Ecuaciones de Transformación)**

Relacionan las coordenadas rectangulares con las esféricas:

$$
x = r \operatorname{sen}\theta \cos\phi
$$


$$
y = r \operatorname{sen}\theta \operatorname{sen}\phi
$$


$$
z = r \cos\theta
$$


**Ecuaciones de transformación inversa:**

$$
r = \sqrt{x^2 + y^2 + z^2}
$$


$$
\tan\phi = \dfrac{y}{x}
$$


$$
\theta = \arccos\left(\dfrac{z}{\sqrt{x^2+y^2+z^2}}\right)
$$


```ad-note
title: Comentario
collapse: closed
Nótese que $x$ e $y$ son ambas funciones de $r$, $\theta$ y $\phi$. Sin embargo, $z$ es función únicamente de $r$ y de $\theta$.
```

![[pegar_imagen]]
*Figura 2.4 · Coordenadas esféricas $(r, \theta, \phi)$.*

IMA | fuente: ETN607_T02.pdf | página: 2 | id: Figura 2.4 | posición: abajo

**Plano — Trabajo virtual**

![[pegar_imagen]]
*Figura 2.3 · Diferencial de arco $dr$ en el plano $xy$ con componentes $dx$ y $dy$.*

IMA | fuente: ETN607_T02.pdf | página: 2 | id: Figura 2.3 | posición: izquierda

$$
\sum F_x = m\ddot{x}
$$

$$
\sum F_y = m\ddot{y}
$$

$$
dW = F_x\,dx + F_y\,dy + F_z\,dz
$$

Migrar a otro sistema $(r, \theta, z)$:

$$
x = x(q_1, q_2, q_3, t)
$$

$$
y = y(q_1, q_2, q_3, t)
$$

$$
z = z(q_1, q_2, q_3, t)
$$

**Entonces (Obteniendo ec. Lagrange)**

$$
dW = F_x\left(\frac{\partial x}{\partial q_1}dq_1 + \frac{\partial x}{\partial q_2}dq_2 + \frac{\partial x}{\partial q_3}dq_3 + \frac{\partial x}{\partial t}dt\right) + \cdots
$$

$$
+ F_y\left(\frac{\partial y}{\partial q_1}dq_1 + \frac{\partial y}{\partial q_2}dq_2 + \frac{\partial y}{\partial q_3}dq_3 + \frac{\partial y}{\partial t}dt\right) + \cdots
$$

$$
+ F_z\left(\frac{\partial z}{\partial q_1}dq_1 + \frac{\partial z}{\partial q_2}dq_2 + \frac{\partial z}{\partial q_3}dq_3 + \frac{\partial z}{\partial t}dt\right)
$$

$$
= m\left[\ddot{x}\left(\frac{\partial x}{\partial q_1}dq_1 + \frac{\partial x}{\partial q_2}dq_2 + \frac{\partial x}{\partial q_3}dq_3 + \frac{\partial x}{\partial t}dt\right) + \cdots\right.
$$

$$
\left. + \ddot{y}\left(\frac{\partial y}{\partial q_1}dq_1 + \frac{\partial y}{\partial q_2}dq_2 + \frac{\partial y}{\partial q_3}dq_3 + \frac{\partial y}{\partial t}dt\right) + \cdots\right.
$$

$$
\left. + \ddot{z}\left(\frac{\partial z}{\partial q_1}dq_1 + \frac{\partial z}{\partial q_2}dq_2 + \frac{\partial z}{\partial q_3}dq_3 + \frac{\partial z}{\partial t}dt\right)\right]
$$

$$
dW_{q_r} = \left(F_x\frac{\partial x}{\partial q_r} + F_y\frac{\partial y}{\partial q_r} + F_z\frac{\partial z}{\partial q_r}\right)dq_r
= m\left(\ddot{x}\frac{\partial x}{\partial q_r} + \ddot{y}\frac{\partial y}{\partial q_r} + \ddot{z}\frac{\partial z}{\partial q_r}\right)dq_r
$$

$$
r = 1, 2, 3 \qquad \leftarrow \text{No aceleración}
$$
`````

>[!summary] Sistema esférico con ecuaciones de transformación directa e inversa, y derivación del trabajo virtual hacia las ecuaciones de Lagrange.

---

%%< correcciones hechas: Incorporación del lema de cancelación de puntos (dot-cancelling lemma) como demostración matemática omitida en el apunte y corrección formal de las proyecciones de fuerza para el péndulo simple. %%

## Velocidad

`````cornell
::cue
derivación de Lagrange · coordenadas generalizadas · momentum lineal · fuerza generalizada
¿Cómo se deduce el término de aceleración de Lagrange a partir de la velocidad?
¿Cuál es la relación de cancelación de puntos (dot-cancelling lemma)?
fórmula clave: $\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{q}_r}\right) - \dfrac{\partial T}{\partial q_r} = Q_r$

::note
**Derivación de la Ecuación de Lagrange para una Partícula**

Consideramos la derivada temporal del producto de la velocidad $\dot{x}$ y la derivada parcial de la posición respecto a la coordenada generalizada $q_r$:

$$
\dfrac{d}{dt} \left( \dot{x} \dfrac{\partial x}{\partial q_r} \right) = \ddot{x} \dfrac{\partial x}{\partial q_r} + \dot{x} \dfrac{d}{dt} \left( \dfrac{\partial x}{\partial q_r} \right)
$$


Despejando el término de aceleración:

$$
\ddot{x} \dfrac{\partial x}{\partial q_r} = \dfrac{d}{dt} \left( \dot{x} \dfrac{\partial x}{\partial q_r} \right) - \dot{x} \dfrac{d}{dt} \left( \dfrac{\partial x}{\partial q_r} \right)
$$


Aplicando las identidades fundamentales de transformación (candelación de puntos) %%<C- demostración del lema: \partial\dot{x}/\partial\dot{q}_r = \partial x/\partial q_r y d/dt(\partial x/\partial q_r) = \partial\dot{x}/\partial q_r %%:

$$
\ddot{x} \dfrac{\partial x}{\partial q_r} = \dfrac{d}{dt} \left( \dot{x} \dfrac{\partial \dot{x}}{\partial \dot{q}_r} \right) - \dot{x} \dfrac{\partial \dot{x}}{\partial q_r}
$$


Expresando en términos de la energía cinética de una partícula unidimensional $\frac{1}{2} \dot{x}^2$:

$$
\ddot{x} \dfrac{\partial x}{\partial q_r} = \dfrac{d}{dt} \left( \dfrac{\partial}{\partial \dot{q}_r} \left( \dfrac{1}{2} \dot{x}^2 \right) \right) - \dfrac{\partial}{\partial q_r} \left( \dfrac{1}{2} \dot{x}^2 \right)
$$


Efectuando el mismo procedimiento para las componentes $y$ y $z$:

$$
\dot{y} \dfrac{\partial y}{\partial q_r} = //
$$


$$
\dot{z} \dfrac{\partial z}{\partial q_r} = //
$$


Entonces, multiplicando por la masa $m$ y sumando para las tres componentes cartesianas, obtenemos la aceleración generalizada en términos de la energía cinética $T = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2)$:

$$
m \left( \ddot{x} \dfrac{\partial x}{\partial q_r} + \ddot{y} \dfrac{\partial y}{\partial q_r} + \ddot{z} \dfrac{\partial z}{\partial q_r} \right) = \dfrac{d}{dt} \left[ \dfrac{\partial}{\partial \dot{q}_r} \left( \dfrac{m}{2} (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) \right) \right] - \dfrac{\partial}{\partial q_r} \left( \dfrac{m}{2} (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) \right)
$$


$$
\dfrac{d}{dt} \left( \dfrac{\partial T}{\partial \dot{q}_r} \right) - \dfrac{\partial T}{\partial q_r} = F_x \dfrac{\partial x}{\partial q_r} + F_y \dfrac{\partial y}{\partial q_r} + F_z \dfrac{\partial z}{\partial q_r}
$$

%%<F- Ecuación de Lagrange en componentes %%

Donde el miembro izquierdo representa el producto de la masa por la aceleración generalizada, y el miembro derecho es la proyección de las fuerzas reales (fuerza generalizada $Q_r$):

$$
\text{L.I.: } \text{Masa} \times \text{Aceleración} \quad \sim \quad \text{L.D.: } \text{Proyección Fzas.}
$$


---

**Aplicación al Péndulo Simple $N = 1$**

Para un sistema con un único grado de libertad, donde las coordenadas de la partícula se expresan en función de $\theta$ como única coordenada generalizada:

$$
(r, \theta, z) = (q_1, q_2, q_3) \quad \text{con } r = l = \text{cte}, \quad z = 0
$$


![[pegar_imagen]]
*Figura 2.5 · Péndulo simple en coordenadas cilíndricas/polares.*

La energía cinética de la partícula es:

$$
T = \dfrac{m}{2}(\dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2)
$$


$$
T = \dfrac{m}{2}l^2\dot{\theta}^2
$$


Aplicando la ecuación de Lagrange para $\theta$:

$$
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{\theta}}\right) - \dfrac{\partial T}{\partial \theta} = Q_\theta
$$


$$
\dfrac{\partial T}{\partial \dot{\theta}} = ml^2\dot{\theta} \implies \dfrac{d}{dt}(ml^2\dot{\theta}) = ml^2\ddot{\theta}
$$


$$
\dfrac{\partial T}{\partial \theta} = 0
$$


Para la fuerza generalizada $Q_\theta$, usamos las ecuaciones de transformación:

$$
x = l\sin\theta \implies \dfrac{\partial x}{\partial \theta} = l\cos\theta
$$


$$
y = l\cos\theta \implies \dfrac{\partial y}{\partial \theta} = -l\sin\theta
$$


Las componentes de la fuerza total (gravedad y tensión $\tau$) son:

$$
F_x = -\tau\sin\theta
$$


$$
F_y = mg - \tau\cos\theta
$$


Por lo tanto, la proyección de fuerzas resulta en:

$$
Q_\theta = F_x \dfrac{\partial x}{\partial \theta} + F_y \dfrac{\partial y}{\partial \theta}
$$


$$
Q_\theta = (-\tau\sin\theta)(l\cos\theta) + (mg - \tau\cos\theta)(-l\sin\theta)
$$


$$
Q_\theta = -\tau l\sin\theta\cos\theta - mgl\sin\theta + \tau l\sin\theta\cos\theta = -mgl\sin\theta
$$


Igualando ambos lados de la ecuación de Lagrange:

$$
ml^2\ddot{\theta} = -mgl\sin\theta \implies \ddot{\theta} = -\dfrac{g}{l}\sin\theta \quad \text{[GDE mod mat.]}
$$


Para pequeñas oscilaciones $\sin\theta \approx \theta$, el sistema se simplifica al oscilador armónico simple:

$$
\ddot{\theta} = -\dfrac{g}{l}\theta
$$


IMA | fuente: ETN607_T02.pdf | página: 4 | id: Figura 2.5 | posición: arriba
`````

>[!summary] Deducción de la ecuación de Lagrange mediante identidades diferenciales de la velocidad y su aplicación directa en la modelación del péndulo simple.

---
### Velocidad

`````cornell
::cue
péndulo simple · coordenadas cilíndricas · fuerza generalizada · diagrama de bloques
¿Cómo se obtiene la GDE del péndulo simple aplicando Lagrange en coordenadas cilíndricas?
¿Cómo se implementa el modelo en Simulink?
Fórmula clave: $\ddot{\theta} = -\dfrac{g}{l}\sin\theta$

::note
**Aplicación al Péndulo Simple $N = 1$**

Para $N = 1$ con $(r, \theta, z) = (q_1, q_2, q_3)$, $r = l = \text{cte}$, $z = 0$:

$$
x = l\sin\theta \qquad y = l\cos\theta
$$

La energía cinética se reduce a:

$$
T = \dfrac{m}{2}\left(\dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2\right)
$$

$$
T = \dfrac{m}{2}\,l^2\dot{\theta}^2
$$

![[pegar_imagen]]
*Figura 2.5 · Péndulo simple en coordenadas cilíndricas/polares con $r = l = \text{cte}$.*

IMA | fuente: ETN607_T02.pdf | página: 4 | id: Figura 2.5 | posición: izquierda

Entonces, aplicando la ecuación de Lagrange para $\theta$:

$$
\dfrac{d}{dt}\!\left(\dfrac{\partial T}{\partial \dot{\theta}}\right) - \dfrac{\partial T}{\partial \theta} = F_x\dfrac{\partial x}{\partial \theta} + F_y\dfrac{\partial y}{\partial \theta} + F_z\dfrac{\partial z}{\partial \theta}
$$

Derivadas de transformación:

$$
\dfrac{\partial x}{\partial \theta} = l\cos\theta \qquad \dfrac{\partial y}{\partial \theta} = -l\sin\theta \qquad \dfrac{\partial z}{\partial \theta} = 0
$$

Fuerzas sobre la partícula (gravedad + tensión $\tau$):

$$
F_x = -\tau\sin\theta \qquad F_y = mg - \tau\cos\theta
$$

Lado izquierdo:

$$
\dfrac{d}{dt}\!\left(\dfrac{\partial T}{\partial \dot{\theta}}\right) = \dfrac{d}{dt}\!\left(ml^2\dot{\theta}\right) = ml^2\ddot{\theta}
$$

Igualando:

$$
ml^2\ddot{\theta} = -\tau\sin\theta\,l\cos\theta + (mg - \tau\cos\theta)(-l\sin\theta)
$$

$$
ml^2\ddot{\theta} = -\tau l\sin\theta\cos\theta - mgl\sin\theta + \tau l\cos\theta\sin\theta
$$

$$
ml^2\ddot{\theta} = -mgl\sin\theta
$$

$$
\boxed{\ddot{\theta} = -\dfrac{g}{l}\sin\theta} \qquad \text{ODE — mod mat.}
$$

Simplificado ($\sin\theta \approx \theta$):

$$
\ddot{\theta} = -\dfrac{g}{l}\,\theta
$$

`````

>[!summary] Modelo del péndulo simple por Lagrange en coordenadas cilíndricas, obtención de la GDE y diagrama de bloques Simulink.
%%< correcciones hechas %%

---

## b) Euler

`````cornell
::cue
método de Euler · péndulo no lineal · diferencias finitas · MATLAB
¿Cómo se reduce la ecuación de segundo orden del péndulo a un sistema de primer orden?
¿Cuál es la aproximación por diferencias finitas para la primera derivada?
¿Cómo se implementa la actualización del estado en MATLAB?
Fórmula clave: $\theta_2 = \theta_1 + \dot{\theta}_1 \Delta t$
ver también: errores comunes de sintaxis en rango de tiempo de MATLAB

::note
**Método de Euler**

Para resolver la ecuación diferencial del péndulo de forma numérica, se reduce la ecuación de segundo orden a un sistema de dos ecuaciones de primer orden:

Definiendo las variables de estado:

$$
\theta = x_1
$$


$$
\dot{\theta} = x_2
$$


Obtenemos el sistema:

$$
\dot{x}_1 = x_2
$$


$$
\dot{x}_2 = -\dfrac{g}{\ell} \sin x_1
$$


Además, aproximando la derivada temporal mediante diferencias finitas hacia adelante:

$$
\dfrac{d\theta}{dt} \approx \dfrac{\theta_2 - \theta_1}{\Delta t}
$$


La actualización de la posición angular para el siguiente paso temporal se expresa como:

$$
\theta_2 = \theta_1 + \dot{\theta}_1 \Delta t
$$


```ad-note
title: Nota
collapse: closed
Solo primera derivada | Sin derivadas de orden superior
```

```ad-recordando_2
title: Met Lab
collapse: closed
t = 0:0.01:10;
x1(1) = pi/4;
x2(1) = 0;
h = 0.01;
for i = 1:length(t)-1
   x1(i+1) = x2(i)*h + x1(i);
   x2(i+1) = - (g/l)*sin(x1(i))*h + x2(i);
end
```

*Nota de corrección: Se corrigieron varios errores críticos en el código MATLAB del apunte original. El rango de tiempo se reestructuró a la sintaxis correcta `t = 0:0.01:10;` en lugar del erróneo `t = 0:10:0.01`. Se definió el tamaño de paso `h = 0.01;` y la velocidad angular inicial omitida `x2(1) = 0;`. Adicionalmente, se cambió la función trigonométrica `sen` por la nativa `sin`, la constante `PI` por la palabra reservada en minúscula `pi`, y se ajustaron las palabras clave `for` y `end` a minúsculas.*
`````

>[!summary] Transcripción y corrección del método de Euler para la resolución numérica de la ecuación de movimiento del péndulo simple.

---

