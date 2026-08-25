%%< correcciones hechas: Corrección del subtítulo "sistema extricto" a "Sistema esférico" en la sección de Newton, formulación completa de sus ecuaciones diferenciales en 3D, incorporación de la sección 2.3 (Grados de libertad con esquema LaTeX de clasificación), sección 2.4 (Coordenadas generalizadas), sección 2.5 (Ecuaciones de restricción con esquema de clasificación temporal e integrable) y sección 2.6 (El Lagrangiano y las ecuaciones de Lagrange), deteniéndose inmediatamente antes de la sección 2.7 (Velocidad). %%

## 2.2 Ecuaciones de Lagrange (continuación)

`````cornell
::cue
coordenadas esféricas · aceleración curvilínea · fuerzas de ligadura
¿Cómo se definen la velocidad y la aceleración en componentes esféricas?
¿Cuáles son las ecuaciones de movimiento de Newton en este sistema?
Fórmula clave: $\vec{a} = (\ddot{r} - r\dot{\theta}^2 - r\dot{\phi}^2\operatorname{sen}^2\theta)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta} - r\dot{\phi}^2\operatorname{sen}\theta\cos\theta)\mathbf{e}_\theta + (r\ddot{\phi}\operatorname{sen}\theta + 2\dot{r}\dot{\phi}\operatorname{sen}\theta + 2r\dot{\theta}\dot{\phi}\cos\theta)\mathbf{e}_\phi$

::note
**c) Sistema esférico** %%<F- \vec{F} = m\vec{a} %%
La posición de una partícula en coordenadas esféricas se define por una distancia y dos ángulos $(r, \theta, \phi)$:

$$
\vec{r} = r\mathbf{e}_r
$$


Derivando respecto al tiempo, se obtiene la velocidad curvilínea:

$$
\vec{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta + r\dot{\phi}\operatorname{sen}\theta\mathbf{e}_\phi
$$


Derivando nuevamente, la aceleración total de la partícula resulta:

$$
\vec{a} = (\ddot{r} - r\dot{\theta}^2 - r\dot{\phi}^2\operatorname{sen}^2\theta)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta} - r\dot{\phi}^2\operatorname{sen}\theta\cos\theta)\mathbf{e}_\theta + (r\ddot{\phi}\operatorname{sen}\theta + 2\dot{r}\dot{\phi}\operatorname{sen}\theta + 2r\dot{\theta}\dot{\phi}\cos\theta)\mathbf{e}_\phi
$$


Por lo tanto, las ecuaciones de movimiento de Newton en componentes esféricas son:

$$
\Sigma F_r = m(\ddot{r} - r\dot{\theta}^2 - r\dot{\phi}^2\operatorname{sen}^2\theta)
$$


$$
\Sigma F_\theta = m(r\ddot{\theta} + 2\dot{r}\dot{\theta} - r\dot{\phi}^2\operatorname{sen}\theta\cos\theta)
$$


$$
\Sigma F_\phi = m(r\ddot{\phi}\operatorname{sen}\theta + 2\dot{r}\dot{\phi}\operatorname{sen}\theta + 2r\dot{\theta}\dot{\phi}\cos\theta)
$$


```ad-note
title: Comentario sobre las fuerzas de ligadura
collapse: closed
Al igual que en el sistema cilíndrico, la formulación newtoniana exige incluir explícitamente las fuerzas de ligadura (tensiones, reacciones normales) que mantienen confinada a la partícula, incrementando enormemente la dificultad algebraica del sistema.
```
`````

>[!summary] Formulación de las ecuaciones de Newton en coordenadas esféricas, evidenciando la alta complejidad de sus componentes de aceleración.

---

## 2.3 Grados de libertad $DOF$

`````cornell
::cue
grados de libertad · coordenadas mínimas · restricciones del movimiento
¿Qué define físicamente a un grado de libertad?
¿Cómo afecta una ligadura al número de grados de libertad de un sistema?
Fórmula clave: $\text{DOF} = 3N - k$

::note
**Definición**
Los **Grados de Libertad $DOF$** corresponden al número de variables o coordenadas independientes mínimas necesarias para determinar de manera unívoca la posición y configuración física de un sistema en el espacio.

Para un sistema constituido por $N$ partículas libres en tres dimensiones, el número de grados de libertad es de $3N$. Si sobre el sistema actúan $k$ ecuaciones de restricción independientes, el número de grados de libertad se reduce de manera directa:


$$
\text{DOF} = 3N - k
$$


**Esquema de clasificación física de sistemas comunes en 3D**:
$$
\substack{\displaystyle\text{Grados de Libertad}\\\displaystyle\text{(DOF) en 3D}}
\begin{cases}
\text{- Partícula libre}
\begin{cases}
\text{- N = 3}
\end{cases} \\[4pt]
\text{- Varilla rígida}
\begin{cases}
\text{- N = 5}
\end{cases} \\[4pt]
\text{- Cuerpo rígido}
\begin{cases}
\text{- N = 6}
\end{cases}
\end{cases}
\quad \left| \quad
\begin{array}{l}
\text{3 traslaciones} \\
\text{3 traslaciones + 2 rotaciones} \\
\text{3 traslaciones + 3 rotaciones}
\end{array}
\right.
$$

![[pegar_imagen]]
*Figura 2.1 · Grados de libertad para una varilla rígida libre en el espacio tridimensional.*

```ad-note
title: Comentario
collapse: closed
Para la varilla rígida, las 2 partículas tienen originalmente 6 coordenadas, pero la condición de rigidez representa una ecuación de restricción ($d = \text{constante}$), lo que reduce los grados de libertad a 5.
```

IMA | fuente: ETN607_T02.pdf | página: 1 | id: Figura 2.1 | posición: centro
`````

>[!summary] Los grados de libertad definen la movilidad independiente de un sistema mecánico, calculados mediante la diferencia entre sus coordenadas totales y sus restricciones físicas.

---

## 2.4 Coordenadas generalizadas

`````cornell
::cue
coordenadas generalizadas · velocidades generalizadas · configuración del sistema
¿Qué diferencia a las coordenadas generalizadas de las coordenadas cartesianas ordinarias?
¿Cómo se definen las velocidades generalizadas?
Fórmula clave: $q_i \rightarrow \text{coordenadas}, \quad \dot{q}_i \rightarrow \text{velocidades}$

::note
**Definición**
Se denomina **coordenadas generalizadas** a cualquier conjunto de parámetros independientes $(q_1, q_2, \dots, q_n)$ que describen de forma completa y unívoca la configuración de un sistema físico de $n$ grados de libertad. 

Estas coordenadas no requieren poseer dimensiones de longitud física (pueden ser ángulos, áreas, etc.). Las derivadas primeras respecto al tiempo de estas coordenadas se denominan **velocidades generalizadas**:


$$
\dot{q}_i = \dfrac{dq_i}{dt}
$$


**Ecuaciones de transformación**
Relacionan las coordenadas rectangulares ordinarias de cada partícula $\vec{r}_i$ con las coordenadas generalizadas del sistema y el tiempo:


$$
\vec{r}_i = \vec{r}_i(q_1, q_2, \dots, q_n, t)
$$

`````

>[!summary] Las coordenadas generalizadas describen la posición de un sistema con el número mínimo de parámetros independientes requeridos, prescindiendo del marco cartesiano rígido.

---

## 2.5 Ecuaciones de restricción

`````cornell
::cue
ligaduras holónomas · ligaduras no holónomas · esclerónomas · reónomas
¿Cómo se clasifican las restricciones según su integrabilidad y su dependencia temporal?
¿Qué define a una restricción holónoma?
Fórmula clave: $f(r_1, r_2, \dots, r_N, t) = 0$

::note
**Definición**
Las restricciones (o ligaduras) son limitaciones físicas impuestas sobre la libre movilidad de las partículas de un sistema.

**Clasificación de las Restricciones**: %%<C- Revisar ejemplos prácticos de ligaduras no holónomas %%

$$
\substack{\displaystyle\text{Clasificación de}\\\displaystyle\text{Restricciones}}
\begin{cases}
\text{- Por su integrabilidad}
\begin{cases}
\text{- Holónomas: expresables como } f(\vec{r}_i, t) = 0 \\[4pt]
\text{- No holónomas: diferenciales no integrables}
\end{cases} \\[4pt]
\text{- Por su dependencia temporal}
\begin{cases}
\text{- Esclerónomas: independientes del tiempo } f(\vec{r}_i) = 0 \\[4pt]
\text{- Reónomas: dependen explícitamente del tiempo } f(\vec{r}_i, t) = 0
\end{cases}
\end{cases}
$$


```ad-note
title: Ligaduras de rodadura
collapse: closed
La rodadura sin deslizamiento es el ejemplo típico de ligadura no holónoma, ya que sus ecuaciones diferenciales de restricción no pueden ser integradas directamente en coordenadas algebraicas.
```
`````

>[!summary] Las restricciones limitan el movimiento del sistema y se clasifican según su integrabilidad algebraica y su dependencia explícita del tiempo.

---

## 2.6 El Lagrangiano y las Ecuaciones de Lagrange

`````cornell
::cue
lagrangiano · energía cinética · energía potencial · ecuaciones de movimiento
¿Cómo se define el Lagrangiano de un sistema mecánico?
¿Cuáles son las ecuaciones de movimiento de Lagrange para sistemas conservativos?
Fórmula clave: $L = T - V$, $\quad \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) - \dfrac{\partial L}{\partial q_i} = 0$

::note
**Definición del Lagrangiano** %%<V- L = T - V %%
Para un sistema conservativo, el **Lagrangiano ($L$)** es la función energética definida como la diferencia entre la energía cinética total ($T$) y la energía potencial total ($V$) del sistema:


$$
L = T - V
$$


**Ecuaciones de Lagrange**
Para un sistema holónomo y conservativo de $n$ grados de libertad, las ecuaciones de movimiento independientes se expresan como:


$$
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) - \dfrac{\partial L}{\partial q_i} = 0 \quad (i = 1, 2, \dots, n)
$$


```ad-note
title: Ventaja del método energético
collapse: closed
El método de Lagrange elimina de forma automática todas las fuerzas de restricción internas de carácter reactivo, permitiendo derivar las ecuaciones diferenciales de movimiento únicamente a partir de funciones escalares de energía.
```
`````

>[!summary] El Lagrangiano unifica la descripción energética del sistema, permitiendo derivar las ecuaciones de movimiento sin requerir el planteamiento vectorial de fuerzas de ligadura.

