# Tema 1: Conceptos generales 1

## Introducción

``````cornell
::cue
Sistemas dinámicos ·

¿Qué tipos de sistemas se estudian?
¿Qué es un sistema dinámico?
Métodos de análisis.

::note

$$
\substack{\displaystyle\text{Sistemas}\\\displaystyle\text{dinámicos}}
\begin{cases}
    \text{- Mecánicos}
    \begin{cases}
        \text{- Traslacionales} \\
        \text{- Rotacionales}
    \end{cases} \\[4pt]
    \text{- Circuitos eléctricos} \\[4pt]
    \text{- Sistemas hidráulicos}
\end{cases}
\quad
\left|
\quad
\begin{array}{l}
    \text{Leyes de Newton} \\
    {\color{orange}{\text{Lagrange}^{*}}}\\
    \substack{\displaystyle\text{Conservación} \\\displaystyle\text{de la energía}}\\
    \text{Newton-Euler} \\
    \text{D'Alembert} \\
    \text{Trabajo virtual}
\end{array}
\right.
$$

Cuerpos que cambian de posición a diferentes velocidades con el tiempo.

> [!note]
> **Nota de corrección:** De acuerdo con Taylor (Cap. 1.2) y Goldstein (Cap. 1.4), las cinco formulaciones de la mecánica clásica (Newton, Lagrange, Hamilton, D'Alembert y Hamilton-Principio) son físicamente equivalentes y derivables entre sí usando el concepto de trabajo virtual. El método de Lagrange es especialmente potente y sencillo para resolver sistemas complejos y electromecánicos.

``````

>[!summary] Definición de sistemas dinámicos y enumeración de los métodos fundamentales de análisis en mecánica aplicada.

## Objetivo

`````cornell
::cue
Finalidad del análisis · 
¿Qué tipo de ecuaciones se buscan hallar? ·
¿Cuál es el objetivo principal al formular las ecuaciones de movimiento?

Tratamiento de ligaduras.
Funciones escalares.

::note

$$
\text{Hallar}
\quad
\begin{cases}
    \text{- EDO (Ecuación diferencial ordinaria)} \\
    \text{- ODE (Ordinary differential equation)}
\end{cases}
$$

Busca formular las ecuaciones de movimiento de modo que se eliminen las fuerzas de ligadura desconocidas, mediante funciones escalares de energía.

---

![[ETN607T01.pdf#page=1&rect=94,225,516,365|ETN607T01, p.1]]
*Figura 1.1 · Ejemplo clásico de como las fuerzas dinámicas de alta frecuencia pueden alterar por completo la estabilidad de un punto de equilibrio. Péndulo invertido*

> [!note]
> **Nota de corrección:
> ** Conforme a **Goldstein (Cap. 1.3)**, las ligaduras introducen dos dificultades principales: la **interdependencia de las coordenadas** y el hecho de que las **fuerzas de ligadura no se conocen *a priori***. El formalismo lagrangiano supera estas dificultades al emplear **coordenadas generalizadas independientes** (que incorporan automáticamente las ligaduras holónomas) y al **eliminar las fuerzas de ligadura** de las ecuaciones de movimiento, basándose en magnitudes escalares de energía $$L = T - V$$.

`````
### Objetivo — fuerzas de ligadura y funciones escalares de energía

````ad-note
title: Complemento (Definición formal·Idea clave)
collapse: open
1. Definición formal
El procedimiento de Lagrange esta basado, en gran parte, en magnitudes escalares: energia cinetica, energia potencial, trabajo virtual, y en muchos casos, la funcion de potencia. Todas ellas pueden expresarse generalmente sin ninguna dificultad en cualquier sistema de coordenadas adecuado. Las fuerzas de restriccion, para los casos de restricciones holonomas lisas, quedan eliminadas automaticamente y no aparecen en las ecuaciones de Lagrange. [[Dare A. Wells-Dinamica de Lagrange-1972-McGraw-Hill-esp.pdf#page=2]]

2. Idea clave
El método de Lagrange reduce la complejidad del análisis dinámico al basarse en funciones de energía escalares, logrando eliminar de forma automática las fuerzas de ligadura sin necesidad de recurrir al formalismo vectorial.
````

>[!summary] Formulación de ecuaciones diferenciales de movimiento $EDO$ optimizadas mediante energía para eliminar incógnitas de ligadura.

## Métodos

`````cornell
::cue
Experimento péndulo · ODE · Restricciones · Coordenadas polares
¿Cómo se definen los grados de libertad en el experimento del péndulo?
¿Qué papel juegan las ecuaciones de restricción en el movimiento coplanar?

$r = l$
$\dot{r} = 0$

::note

**Experimento pendulo ODE**

![[ETN607T01.pdf#page=2&rect=63,551,518,736|ETN607T01, p.2]]

*Figura 1.2 · Representación del péndulo simple con indicación de movimiento radial y velocidad.*

*Figura 1.3 · Restricciones mecánicas para un péndulo de longitud constante en movimiento planar.*

$$
\begin{array}{l}
	\dot{r} = 0 \\
	\ddot{r} = 0 \\
	\dot{z} = 0 \\
	\ddot{z} = 0
\end{array}
$$

```ad-note
title: Nota de corrección: Holonomicidad de las ligaduras
collapse: closed
De acuerdo con **Goldstein (Cap. 1.3)** y **Taylor (Cap. 7.1)**, las restricciones de posición para este péndulo simple son de tipo holónomo y esclerónomo ($r = l$ y $z = 0$). Al derivarse respecto al tiempo, se obtienen las restricciones de velocidad y aceleración correspondientes:
$$\dot{r} = 0 \quad \text{y} \quad \ddot{r} = 0$$
$$\dot{z} = 0 \quad \text{y} \quad \ddot{z} = 0$$
Estas relaciones reducen los grados de libertad del punto material de $3$ a $3 - 2 = 1$, dejando únicamente al ángulo $\theta$ como coordenada generalizada independiente y eliminando la necesidad de calcular a priori la tensión en la cuerda (fuerza de ligadura).
```

`````

>[!summary] Presentación del experimento del péndulo simple y la definición de sus restricciones mecánicas en coordenadas polares.

### a) Newton

`````cornell
::cue
Aceleración en polares · Fuerza tangencial · Segunda ley de Newton · Péndulo simple

¿Cómo se descompone la aceleración de una partícula en coordenadas cilíndricas/polares?
¿Cómo se aplica la segunda ley de Newton para obtener la ecuación de movimiento del péndulo?

$\vec{a} = a_r\hat{e}_r + a_\theta\hat{e}_\theta + a_z\hat{e}_z$

---

![[ETN607T01.pdf#page=2&rect=69,240,275,395|ETN607T01, p.2]]

*Figura 1.4 · Diagrama de cuerpo libre y fuerzas tangenciales en el péndulo simple.*

::note
**a) Newton**

La aceleración de una partícula en coordenadas cilíndricas se define como:

$$
\vec{a}
=
\underbrace{(\ddot{r} - r\dot{\theta}^2)\hat{e}_r}_{\substack{\displaystyle \text{movimiento}\\\displaystyle \text{radial}}}
+
\underbrace{(r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{e}_\theta}_{\substack{\displaystyle \text{movimiento}\\\displaystyle \text{tangencial}}}
+
\underbrace{\ddot{z}\hat{e}_z}_{\substack{\displaystyle \text{movimiento}\\\displaystyle \text{normal}}}
$$

Como el péndulo está restringido a una trayectoria circular de radio constante $r = l$ y movimiento planar $z = 0$, la aceleración tangencial se reduce a:

$$a_{\theta} = l\ddot{\theta} + 2(0)\dot{\theta}$$

---

A partir del diagrama, la fuerza tangencial es:

$$
F_\theta = -mg\sin\theta
$$

Aplicando la segunda ley de Newton $$\Sigma F = ma$$ en la dirección tangencial:

$$
\begin{array}{rcl}
-mg\sin\theta & = & ml\ddot{\theta} \\[4pt]
\therefore\quad \color{orange}{\ddot{\theta}}
& \color{orange}{=}
& \color{orange}{-\dfrac{g}{l}\sin\theta}
\end{array}
$$


```ad-note
title: Nota de corrección: Fuerzas de ligadura y el método de Newton
collapse: closed
Según **Taylor (Cap. 7.4)** y **Goldstein (Cap. 1.3)**, el método vectorial de Newton requiere plantear todas las componentes de la fuerza, incluyendo aquellas asociadas a las ligaduras (restricciones). En la dirección radial, la segunda ley de Newton establece:
$$\Sigma F_r = m a_r \implies T - mg\,\text{cos}\,\theta = m(\ddot{r} - r\dot{\theta}^2)$$
Como el radio es constante ($r = l$), esto nos da la tensión de la cuerda (fuerza de ligadura):
$$T = m(g\,\text{cos}\,\theta - l\dot{\theta}^2)$$
La gran desventaja del enfoque newtoniano es que las fuerzas de ligadura no se conocen *a priori* y deben calcularse explícitamente resolviendo las ecuaciones acopladas. En cambio, el enfoque lagrangiano elimina de manera automática estas fuerzas al proyectar el movimiento sobre coordenadas generalizadas independientes (como el ángulo $\theta$), reduciendo notablemente la complejidad del análisis.
```

`````

>[!summary] Deducción de la ecuación de movimiento del péndulo simple mediante la segunda ley de Newton en la dirección tangencial, evidenciando las limitaciones en el tratamiento de fuerzas de ligadura.

---

## 1. Newton: Condiciones Formales y Péndulo en Coordenadas Cilíndricas

``````ad-note
title: Complemento (Nivel B/C)

1. Definición formal
**Las leyes fundamentales de la mecánica clásica se sustentan sobre las tres leyes de Newton y el concepto de trabajo virtual.** Para una partícula de masa constante $m$, la segunda ley de Newton se define vectorialmente en un marco inercial como:

$$
\vec{F} = m \frac{d\vec{v}}{dt}
$$


2. Idea clave
**La validez de las ecuaciones vectoriales de Newton exige el cumplimiento estricto de cinco condiciones fundamentales relacionadas con el marco de referencia (Condición A), la constancia de la masa (Condición B), y los límites físicos de velocidad, escala y gravedad de la dinámica clásica (Condiciones C, D y E).** 
* **Condición A (Marco Inercial)**: El movimiento debe medirse con respecto a un sistema de coordenadas inmóvil o en movimiento de traslación uniforme sin rotación respecto a las estrellas fijas. Cualquier marco acelerado o rotatorio es no-inercial.
* **Condición B (Masa Constante)**: Si la masa es variable, la ley vectorial debe expresarse como $\vec{F} = \frac{d}{dt}(m\vec{v})$.
* **Condición C (Límite Relativista)**: Las velocidades deben ser muy bajas en comparación con la velocidad de la luz $c$.
* **Condición D (Límite Cuántico)**: Las escalas espaciales deben ser macroscópicas comparadas con las dimensiones atómicas.
* **Condición E (Límite de Gravitación)**: Los campos gravitatorios no deben ser extremadamente intensos ni los intervalos de tiempo del orden de siglos o más.

3. Figura o diagrama


```tikz
\begin{document}
\begin{tikzpicture}[scale=1.3]

  % Cilindro imaginario
  \draw[dashed, gray] (0,1) ellipse (1.5 and 0.4);
  \draw[dashed, gray] (0,-2) ellipse (1.5 and 0.4);
  \draw[dashed, gray] (-1.5,1) -- (-1.5,-2);
  \draw[dashed, gray] (1.5,1) -- (1.5,-2);

  % Eje z
  \draw[->, gray, dashed] (0,1.6) -- (0,-2.6) node[below]{$z$};

  % Origen
  \fill[black] (0,1) circle (1.5pt);
  \node[left=4pt] at (0,1) {$O$};

  % Hilo del péndulo
  \draw[thick, teal] (0,1) -- (1.1,-1.2) node[midway, above right]{$l$};

  % Masa
  \fill[teal] (1.1,-1.2) circle (0.12);
  \node[right=5pt] at (1.1,-1.7) {$m(r,\theta,z)$};

  % Proyección radial r
  \draw[dashed, gray] (0,-1.2) -- (1.1,-1.2) node[midway, above]{$r$};

  % Segmento vertical (altura z de la masa)
  \draw[dashed, gray] (0,1) -- (0,-1.2) node[midway, left]{$\Delta z$};

  % Vectores unitarios
  \draw[->, thick, orange] (1.1,-1.2) -- (1.8,-1.2) node[right]{$\hat{e}_r$};
  \draw[->, thick, orange] (1.1,-1.2) -- (1.1,-0.5) node[above]{$\hat{e}_z$};
  \draw[->, thick, orange] (1.1,-1.2) -- (0.5,-1.7) node[below left]{$\hat{e}_\theta$};

  % Fuerzas
  \draw[->, thick, olive] (1.1,-1.2) -- (1.1,-2.1) node[below]{$mg$};
  \draw[->, thick, violet] (1.1,-1.2) -- (0.55,-0.1) node[left]{$\vec{T}$};

\end{tikzpicture}
\end{document}
```
4. Ejercicios resueltos (solo nivel C)
##### Ej. Péndulo esférico en coordenadas cilíndricas con tensión y ecuaciones de movimiento vectoriales
**Enunciado:** Una partícula de masa $m$ está suspendida de un punto de soporte fijo $O$ por medio de un hilo inextensible de longitud $l$. El movimiento no está restringido a un plano (péndulo esférico). Utilizando coordenadas cilíndricas $(r, \theta, z)$ con el eje $z$ vertical positivo hacia abajo y el origen en $O$:
a) Plantee las ecuaciones vectoriales de movimiento de la partícula aplicando la segunda ley de Newton.
b) Demuestre la conservación del momentum angular con respecto al eje $z$.
c) Deduzca una expresión para la tensión $T$ en el hilo en términos de la velocidad y de la altura $z$.

**Resolución:**
La posición de la partícula en coordenadas cilíndricas es:
$$ \vec{R} = r \hat{e}_r + z \hat{e}_z $$
Sometida a la ligadura holónoma de longitud constante:
$$ r^2 + z^2 = l^2 $$
La velocidad y la aceleración se expresan como:
$$ \vec{v} = \dot{r} \hat{e}_r + r \dot{\theta} \hat{e}_\theta + \dot{z} \hat{e}_z $$
$$ \vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{e}_\theta + \ddot{z}\hat{e}_z $$

Las fuerzas aplicadas son el peso de la partícula $$\vec{F}_g = mg \hat{e}_z$$, con $z$ vertical hacia abajo$ y la tensión de la cuerda $\vec{T}$, la cual actúa radialmente hacia el origen $O$:
$$ \vec{F}_g = mg \hat{e}_z $$
$$ \vec{T} = -T \hat{u}_r = -T \left( \frac{\vec{R}}{l} \right) = -T \left( \frac{r}{l} \hat{e}_r + \frac{z}{l} \hat{e}_z \right) $$

Aplicando la segunda ley de Newton $\vec{F}_{net} = \vec{T} + \vec{F}_g = m\vec{a}$ por componentes:
1) En la dirección radial $\hat{e}_r$:
$$ -T\frac{r}{l} = m(\ddot{r} - r\dot{\theta}^2) \quad \text{(ec. 1)} $$
2) En la dirección angular $\hat{e}_\theta$:
$$ 0 = m(r\ddot{\theta} + 2\dot{r}\dot{\theta}) \quad \text{(ec. 2)} $$
3) En la dirección vertical $\hat{e}_z$:
$$ -T\frac{z}{l} + mg = m\ddot{z} \quad \text{(ec. 3)} $$

Para la parte b), de (ec. 2) multiplicamos por $r$:
$$ r(r\ddot{\theta} + 2\dot{r}\dot{\theta}) = 0 \implies \frac{d}{dt}(r^2\dot{\theta}) = 0 $$
Multiplicando por la masa $m$, se comprueba que el momentum angular con respecto al eje vertical $z$ es constante:
$$ L_z = m r^2 \dot{\theta} = \text{constante} $$

Para la parte c), multiplicamos (ec. 1) por $r$, (ec. 3) por $z$ y sumamos ambas relaciones vectoriales:
$$ -T\left( \frac{r^2 + z^2}{l} \right) + mgz = m(r\ddot{r} + z\ddot{z} - r^2\dot{\theta}^2) $$
Derivando dos veces la ecuación de ligadura $r^2 + z^2 = l^2$ respecto al tiempo:
$$ r\dot{r} + z\dot{z} = 0 \implies r\ddot{r} + z\ddot{z} = -(\dot{r}^2 + \dot{z}^2) $$
Reemplazando esta identidad en la suma de componentes:
$$ -T l + mgz = m\left[-(\dot{r}^2 + \dot{z}^2) - r^2\dot{\theta}^2\right] $$

Sustituyendo el escalar de velocidad al cuadrado $v^2 = \dot{r}^2 + r^2\dot{\theta}^2 + \dot{z}^2$, se simplifica a:
$$ -T l + mgz = -m v^2 \implies T = \frac{m v^2 + m g z}{l} $$

Dado que $z = l\cos\alpha$ donde $\alpha$ es el ángulo que forma el hilo con la vertical, obtenemos la tensión en el hilo:
$$ T = \frac{m v^2}{l} + mg \cos\alpha $$
``````

---


### b) Lagrange (escalar)

`````cornell
::cue
Energía cinética $T$ · Energía potencial $V$ · Ecuación de Lagrange escalar · Péndulo simple · Magnitudes escalares

¿Cómo se determinan las energías cinética y potencial para el péndulo simple en coordenadas polares?
¿Cómo se aplica la ecuación de Lagrange escalar para obtener la ecuación de movimiento?
¿Qué ventajas ofrece trabajar con magnitudes escalares en la formulación de Lagrange en comparación con Newton?

$$\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}$$

::note

$$
T = \frac{m}{2} v^2 \rightarrow \frac{m}{2} (l\dot{\theta})^2
$$

$$
V = -m g l \cos\theta
$$

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta}
$$

$$
m l^2 \ddot{\theta} = -(l mg \sin\theta) \quad 
$$

$$
\therefore\quad \color{orange}{\ddot{\theta}}
\color{orange}{=}
\color{orange}{-\dfrac{g}{l}\sin\theta}
$$

```ad-recordando_2
title: Nota de corrección: Ventajas de las magnitudes escalares y derivación del potencial
collapse: closed
De acuerdo con **Wells (Cap. 1.2 y 1.3)** y **Goldstein (Cap. 1.4)**, el procedimiento de Lagrange se fundamenta en magnitudes escalares ($T, V$), lo que elimina la necesidad de recurrir a métodos vectoriales formales y facilita enormemente la deducción de las ecuaciones de movimiento en cualquier sistema de coordenadas. En un sistema conservativo, las fuerzas generalizadas se obtienen de forma directa como derivadas de la energía potencial:
$$Q_j = -\frac{\partial V}{\partial q_j}$$
Permitiendo formular la ecuación del movimiento directamente como:
$$\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}_j}\right) - \frac{\partial T}{\partial q_j} = -\frac{\partial V}{\partial q_j}$$
Esta formulación elimina de manera automática las fuerzas de restricción holónomas y lisas (como la tensión en la cuerda del péndulo), simplificando drásticamente el análisis.
```

`````

>[!summary] **Obtención de la ecuación de movimiento del péndulo simple aplicando las ecuaciones de Lagrange a partir de sus energías escalar cinemática y potencial.**
### c) Conservación de la energía

`````cornell
::cue
Conservación de la energía · Energía mecánica · Péndulo simple · Ecuación de movimiento
¿Cómo se aplica el principio de conservación de la energía mecánica para determinar la ecuación de movimiento del péndulo simple?
¿De qué manera la derivada temporal de la energía total simplifica la obtención de la ecuación de movimiento?
$$\frac{d}{dt}(u) = 0$$

::note

$$
T = \frac{m}{2} v^{2} \rightarrow \frac{m}{2} (l\dot{\theta})^2
$$

$$
V = -mg l \cos\theta
$$

$$
\text{Con: } \left\{ \begin{array}{l} u = T + V = \text{cte} \\ \text{Energía mecánica} = \text{Energía Cinética} + \text{Energía Potencial} \end{array} \right.
$$

$$
\frac{d}{dt}(u) = 0 \quad \rightarrow \quad \frac{d}{dt}\left(\frac{1}{2}m(l\dot{\theta})^2 - mgl\cos\theta\right) = 0
$$

$$
\frac{m}{2} l^2 2\dot{\theta}\ddot{\theta} + mgl\dot{\theta}\sin\theta = 0
$$

$$
\therefore\quad \color{orange}{\ddot{\theta}}
\color{orange}{=}
\color{orange}{-\dfrac{g}{l}\sin\theta}
$$

```ad-recordando_2
title: Nota de corrección: Conservación de la energía y primera integral de movimiento
collapse: closed
Según **Goldstein (Cap. 1.1)** y **Taylor (Cap. 4.5)**, en un sistema donde las fuerzas aplicadas son completamente conservativas (es decir, derivables de un potencial escalar $\vec{F} = -\nabla V$ que no depende explícitamente del tiempo, $\partial V / \partial t = 0$), se cumple que:
$$\vec{F} \cdot d\vec{r} = -dV$$
Al integrar, el trabajo realizado por estas fuerzas equivale a la diferencia de potencial $W_{12} = V_1 - V_2$, mientras que el teorema del trabajo y la energía cinética establece que $W_{12} = T_2 - T_1$. Igualando ambas expresiones se obtiene la ley de conservación de la energía:
$$T_1 + V_1 = T_2 + V_2 \implies T + V = \text{constante}$$
En la resolución de ecuaciones diferenciales de segundo orden, esta relación constituye una **primera integral de movimiento** (o de la energía), la cual reduce el orden de la ecuación y permite resolver el movimiento de manera directa a través de una sola integración (cuadratura):
$$\frac{m}{2} \left(l \dot{\theta}\right)^2 - mgl\,\text{cos}\,\theta = u$$
Esto simplifica sustancialmente el análisis en comparación con el planteamiento de Newton, eliminando además cualquier necesidad de calcular fuerzas de ligadura.
```
`````

>[!summary] Obtención de la ecuación de movimiento del péndulo simple mediante el principio de conservación de la energía, operando como una primera integral de movimiento.

### d) Simulink
`````cornell
::cue
Simulink · Ecuación diferencial ordinaria · Diagrama de bloques · Computador
¿Cómo se modela la ecuación de movimiento del péndulo simple en Simulink?
¿Qué función cumplen los bloques de integración en la resolución de una EDO?
$$\ddot{\theta} = \frac{-g\sin\theta}{l}$$

::note

Resolver EDO mediante computador

![[ETN607T01.pdf#page=3&rect=105,199,484,466|ETN607T01, p.3]]
*Figura 1.5 · Diagrama de bloques y gráfica de la solución en Simulink.*

```ad-note
title: Nota de corrección: Solución numérica y la insolubilidad de las EDO
collapse: closed
De acuerdo con **Wells (Cap. 1.8)**, aunque es posible formular con precisión las ecuaciones diferenciales del movimiento para casi cualquier sistema dinámico, en la gran mayoría de los casos reales estas resultan ser tan complejas (debido a no linealidades o acoplamientos fuertes) que es imposible resolverlas analíticamente de forma exacta. En estas circunstancias, el uso de herramientas de computación y simulación numérica (como Simulink/MATLAB) es indispensable, ya que permiten resolver numéricamente estas ecuaciones difíciles de manera rápida, sistemática y con un mínimo esfuerzo físico y de cálculo.
```

`````

```ad-importante_1
title: Tarea: Tarea opcional
collapse: closed
Resolver mediante simulink. enviar 2 archivos
screenshot y el de simulink
```

>[!summary] Resolución numérica de la ecuación diferencial del péndulo simple mediante diagramas de bloques en Simulink como alternativa a la insolubilidad analítica.

---

## Condiciones (Masa, Velocidad, Tiempo)

`````cornell
::cue
Condiciones límites · Masa · Velocidad · Tiempo · Escala física · Caos determinista · Relatividad · Límite cuántico

¿Cuáles son las condiciones límites de validez de las leyes de Newton?
¿A qué disciplinas corresponden los extremos de masa, velocidad y tiempo?
¿Qué causa que el tiempo se vuelva "impredecible" en la mecánica clásica no lineal?

::note

$$
\substack{\displaystyle\text{Condiciones}\\\displaystyle\text{límites}}
\begin{cases}
	\text{— Masa}
	\begin{cases}
		\text{— No muy grande} \rightarrow \text{Astronomía} \\
		\text{— No muy pequeño} \rightarrow \text{Mecánica cuántica}
	\end{cases} \\[10pt]
	\text{— Velocidad}
	\begin{cases}
		\text{— No muy grande} \rightarrow \text{Mecánica relativista} \\
		\text{— No muy pequeño} \rightarrow \text{Estática}
	\end{cases} \\[10pt]
	\text{— Tiempo}
	\begin{cases}
		\text{— No muy grande} \rightarrow \text{Astronomía} \\
		\text{— No muy pequeño} \rightarrow \text{Impredecible}
	\end{cases}
\end{cases}
$$

---

![[ETN607T01.pdf#page=4&rect=104,416,483,578|ETN607T01, p.4]]

*Figura 1.6 · El péndulo es similar a un sistema hidráulico.*

```ad-note
title: Nota de corrección: Fronteras físicas de la Dinámica Clásica
collapse: closed
Según lo expuesto por **Wells (Cap. 1.6)** y **Taylor (Cap. 1.3 y 12.1)**, la mecánica de Newton no posee validez universal y se encuentra limitada por tres fronteras físicas fundamentales del universo:
1. **Frontera de la masa (Límite cuántico)**: Para masas del orden atómico o subatómico ($m \approx 10^{-30}\,\text{kg}$), la escala de acción del sistema se aproxima a la constante de Planck ($h$). El principio de incertidumbre de Heisenberg invalida la noción clásica de trayectoria determinista, obligando a usar la Mecánica Cuántica.
2. **Frontera de la velocidad (Límite relativista)**: Cuando la velocidad se aproxima a la de la luz ($v \to c$), la masa de la partícula ya no se mantiene constante, sino que se incrementa relativistamente según $m = \gamma m_0$. En este régimen, las ecuaciones clásicas fallan y debe aplicarse la Relatividad Especial.
3. **Frontera del tiempo y la gravedad (Caos y Relatividad General)**: Para masas inmensas y lapsos de tiempo extremadamente largos (escalas cosmológicas o astronómicas acumuladas), la teoría de la Relatividad General de Einstein proporciona predicciones correctas allí donde la gravedad de Newton desvía sus resultados (como en la precesión del perihelio de Mercurio). Por otra parte, en sistemas clásicos no lineales, el factor tiempo se vuelve dinámicamente **impredecible** debido al **caos determinista** (Taylor Cap. 12), donde una sensibilidad extrema a las condiciones iniciales destruye la predictibilidad del sistema a largo plazo.
```

`````

>[!summary] Determinación de las condiciones límites físicas de masa, velocidad y tiempo para la validez de la mecánica clásica, ilustrando analogías mediante sistemas dinámicos equivalentes.

## Sistemas de coordenadas

`````cornell
::cue
Sistemas de coordenadas · Sistema de referencia · Posición en el espacio · Ecuaciones de transformación · Diferencia física y matemática

¿Qué es un sistema de coordenadas y cuál es su utilidad en la dinámica clásica?
¿Cuál es la diferencia fundamental entre un sistema de referencia y un sistema de coordenadas?
¿Cómo influye la elección del sistema de coordenadas en la complejidad de las ecuaciones de movimiento?

$$\vec{r} = x\mathbf{e}_x + y\mathbf{e}_y + z\mathbf{e}_z$$

$$\vec{r} = x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}$$

::note

Para definir o describir el movimiento de un cuerpo o partícula, es indispensable fijar primero un **sistema de referencia** o **sistema de coordenadas** que permita localizar su posición en el espacio.

Un sistema de coordenadas es un conjunto de valores y reglas matemáticas que establecen la posición de un punto de manera unívoca respecto a un origen elegido.

La elección de un sistema de coordenadas adecuado depende principalmente de la geometría y la simetría del problema dinámico, facilitando de manera notable la formulación y resolución de las ecuaciones de movimiento.

---

Objetivo movimiento (Posición)

Coordenadas = Conjunto de variables en Posición respecto origen (Estático)

---

![[ETN607T01.pdf#page=4&rect=88,52,479,293|ETN607T01, p.4]]

*Figura 1.7 · Representación geométrica de un punto en el espacio de tres dimensiones respecto a un sistema de coordenadas.*

```ad-note
title: Nota de corrección: Sistema de referencia vs. Sistema de coordenadas
collapse: closed
Según **Taylor (Cap. 1.2)** y **Alonso & Finn (Cap. 2.1)**, existe una distinción crítica y a menudo ignorada entre estos dos conceptos:
1. El **sistema de referencia** (o referencial) es un ente físico (un cuerpo rígido o conjunto de puntos reales de referencia, como la superficie terrestre, un vagón en movimiento o las estrellas fijas) con respecto al cual se mide la posición de las partículas. Es el marco físico que determina si se trata de un sistema inercial o no-inercial.
2. El **sistema de coordenadas** es la elección de la descripción matemática o geométrica (por ejemplo, coordenadas rectangulares cartesianas, cilíndricas o esféricas) que se utiliza para parametrizar las posiciones de los cuerpos dentro del sistema de referencia físico.
Un mismo sistema de referencia puede albergar múltiples sistemas de coordenadas de manera simultánea. Mientras que la aceleración física de un cuerpo y el carácter inercial dependen exclusivamente del sistema de referencia elegido (segunda ley de Newton), la complejidad analítica de las ecuaciones de movimiento depende de la elección matemática del sistema de coordenadas.
```



`````

>[!summary] Definición de sistemas de coordenadas como herramienta geométrica para localizar puntos en el espacio según la simetría del movimiento.

### a) Rectangular Cartesiano $(x, y, z)$

``````cornell
::cue

Coordenadas cartesianas · Vector de posición · Velocidad en componentes · Ecuaciones de transformación

¿Cómo se define el vector de posición de una partícula en coordenadas rectangulares cartesianas?
¿Cómo se expresa el vector velocidad y su rapidez al cuadrado en componentes cartesianas?
¿Cuáles son las ecuaciones de transformación fundamentales de coordenadas cartesianas a cilíndricas?

$$\vec{R} = x\,\hat{\mathbf{i}} + y\,\hat{\mathbf{j}} + z\,\hat{\mathbf{k}}$$

---

![[ETN607T01.pdf#page=5&rect=73,542,345,756|ETN607T01, p.5]]
**Figura 1.8 · Representación de un punto P en el espacio tridimensional cartesiano y su vector de posición $\vec{R}$.**

---

![[ETN607T01.pdf#page=5&rect=367,422,548,543|ETN607T01, p.5]]

**Figura 1.9 · Definición del vector desplazamiento y velocidad.**

::note
Este sistema consta de tres ejes mutuamente perpendiculares $$X, Y, Z$$ que se cortan en un origen elegido $O$. La posición de una partícula o punto $P$ se define por:

$$
\vec{R} = x\,\hat{\mathbf{i}} + y\,\hat{\mathbf{j}} + z\,\hat{\mathbf{k}} \quad \left| \quad
\begin{array}{l}
x = \text{cte} \\
y = \text{cte} \\
z = \text{cte}
\end{array}
\right.
$$

---

El vector velocidad $\vec{v}$ de la partícula se define como la derivada temporal del vector de posición $\vec{R}$:

$$
\vec{v} = \frac{d\vec{R}}{dt} = \lim_{\Delta t \to 0} \frac{\Delta\vec{R}}{\Delta t}
$$

---

En componentes cartesianas, dado que los versores de base $\hat{\mathbf{i}}$, $\hat{\mathbf{j}}$, $\hat{\mathbf{k}}$ son constantes en dirección y magnitud:

$$
\vec{v} = \dot{x}\hat{\mathbf{i}} + \dot{y}\hat{\mathbf{j}} + \dot{z}\hat{\mathbf{k}}
$$

Donde la rapidez de la partícula al cuadrado es:

$$
v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2
$$


**Ecuaciones de transformación**
Para relacionar las coordenadas rectangulares $(x, y, z)$ con las coordenadas cilíndricas $(\rho, \theta, z)$, se utilizan las siguientes relaciones geométricas:

$$
\begin{array}{l}
\rho^2 = x^2 + y^2 \\
\tan\theta = \frac{y}{x} \\
z = z
\end{array}
$$

```ad-note
title: Nota de corrección: Constancia de versores cartesianos
collapse: closed
De acuerdo con **Alonso & Finn (Cap. 3.3)** y **Wells (Cap. 2.2)**, al definir la velocidad en un sistema de coordenadas inercial, los versores cartesianos ($\hat{\mathbf{i}}, \hat{\mathbf{j}}, \hat{\mathbf{k}}$) permanecen constantes en el tiempo, lo que simplifica la derivada temporal directa de las componentes ($\vec{v} = \dot{x}\hat{\mathbf{i}} + \dot{y}\hat{\mathbf{j}} + \dot{z}\hat{\mathbf{k}}$). Esto marca una diferencia fundamental con sistemas móviles o curvilíneos (como el cilíndrico o esférico), donde los versores de base cambian de dirección y requieren términos de derivada adicionales (Coriolis y arrastre).
```

``````

>[!summary] Definición del sistema rectangular cartesiano, su vector de posición, velocidad en componentes cartesianas y transformaciones fundamentales.


### b) Cilíndrico 3D (Polar 2D) $(r, \theta, z)$

``````cornell
::cue

![[ETN607T01.pdf#page=5&rect=72,200,340,390|ETN607T01, p.5]]

*Figura 1.10 · Punto P en coordenadas cilíndricas con su base de vectores unitarios local.*

---

![[ETN607T01.pdf#page=5&rect=83,88,277,197|ETN607T01, p.5]]
*Figura 1.11 · Versores en coordenadas polares.*

::note

Posición $(r, \theta, z)$

$$\vec{R} = r \hat{e}_{r} + z \hat{e}_{u}$ $\begin{cases} \hat{e}_{r} \text{ no constante} \\ \hat{e}_{u} \text{ constante} \\ \hat{e}_{\theta} \text{ no constante} \end{cases}$$

Ecuaciones de transformación
$$x = r \cos \theta$$
$$y = r \sin \theta$$
$$z = z$$

``````

### c) Esférico 3D (Polar 2D) $(\rho, \theta, \phi)$

``````cornell
::cue

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

``````

### d) Parabólicas Cilíndricas
### e) Hiperbólicas Cilíndricas
### f) Otros

### g) Coordenadas No Lineales (3D) $(A, \theta, Z)$

``````cornell
::cue

![[ETN607T01.pdf#page=6&rect=89,196,208,292|ETN607T01, p.6]]

::note

Posición $(A, \theta, Z)$

$$\vec{R} \quad \text{ Newton}$$

$$\vec{v} = \dfrac{d\vec{R}}{dt}$$

E.T.
$$A = \dfrac{xy}{2}$$
$$\text{tg}\,\theta = \dfrac{y}{x}$$
$$z = z$$

Multiplico

$$\text{tg}\,\theta \cdot A = \dfrac{y^{2}}{2} \Rightarrow y = \pm \sqrt{2 A \text{tg}\,\theta}$$

$$\text{ Divido}$$

$$\dfrac{A}{\text{tg}\,\theta} = \dfrac{x^{2}}{2} \Rightarrow x = \pm \sqrt{\dfrac{2 A}{\text{tg}\,\theta}}$$

``````

```ad-nota_2
title: Comentario
collapse: closed
$$A \rightarrow \text{Distancia}^{2}$$
$$\theta \rightarrow \text{Angulo}$$
$$Z \rightarrow \text{Dist.}$$
```

##### Ej. $x = 4 \, , \, y = 3 \, , \, z = 0$
a) $(4 \, , \, 3 \, , \, 0) \dots (x, y, z)$
b) $(5 \, , \, 36.87^{\circ} \, , \, 0) \dots (r, \theta, z)$
c) $(5 \, , \, 36.87^{\circ} \, , \, 90^{\circ}) \dots (\rho, \theta, \phi)$
g) $(6 \, , \, 36.87 \, , \, 0) \dots (A, \theta, Z)$

---

## Rotacion y traslacion Ejes cartesianos

`````cornell
::cue
rotación de ejes · traslación · ejes cartesianos · matriz de transformación
¿Cómo se relacionan las coordenadas de dos sistemas cartesianos rotados y trasladados?
¿Cuál es la matriz de transformación para una rotación en el plano $xy$?
¿Cómo se expresa la transformación inversa en forma matricial?
$$
\begin{bmatrix}
	x \\ y \\ z 
\end{bmatrix}
=
\begin{bmatrix}
	\cos\mu & -\sin\mu & 0 \\
	\sin\mu & \cos\mu & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	u \\ v \\ w
\end{bmatrix}
$$
---

![[ETN607T01.pdf#page=7&rect=58,370,255,567|ETN607T01, p.7]]

::note
Considerando un sistema de coordenadas $uvw$ rotado un ángulo $\mu$ respecto a un sistema de referencia $xyz$ original:

$$x = u \cos\mu - v \sin\mu$$

$$y = u \sin\mu + v \cos\mu$$

La relación de transformación en forma matricial directa es:

$$
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
=
\begin{bmatrix}
	\cos\mu & -\sin\mu & 0 \\
	\sin\mu & \cos\mu & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
$$

Y la transformación inversa correspondiente:

$$
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
=
\begin{bmatrix}
	\cos\mu & \sin\mu & 0 \\
	-\sin\mu & \cos\mu & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
$$
`````

>[!summary] Relación de transformación de coordenadas mediante matrices de rotación y traslación entre sistemas cartesianos.

---

### a) Rotacion X $\alpha$

`````cornell
::cue
rotación en X · eje X · matriz de transformación
¿Cómo se define la matriz de rotación alrededor del eje $X$?
¿Cómo se expresa la transformación inversa de coordenadas para una rotación en $X$?
$\mathbf{R}_x(\alpha)$

::note
Considerando una rotación de un ángulo $\alpha$ alrededor del eje $X$:

$$
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
=
\begin{bmatrix}
	1 & 0 & 0 \\
	0 & \cos\alpha & -\text{sen}\,\alpha \\
	0 & \text{sen}\,\alpha & \cos\alpha
\end{bmatrix}
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
$$

La transformación inversa correspondiente es:

$$
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
=
\begin{bmatrix}
	1 & 0 & 0 \\
	0 & \cos\alpha & \text{sen}\,\alpha \\
	0 & -\text{sen}\,\alpha & \cos\alpha
\end{bmatrix}
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
$$

`````

>[!summary] Rotación de coordenadas alrededor del eje $X$ en un ángulo $\alpha$ y su correspondiente transformación inversa.

---
### b) Rotacion Y $\beta$

`````cornell
::cue
rotación en Y · eje Y · matriz de transformación
¿Cómo se define la matriz de rotación alrededor del eje $Y$?
¿Cómo se expresa la transformación inversa de coordenadas para una rotación en $Y$?
$\mathbf{R}_y(\beta)$

::note
Considerando una rotación de un ángulo $\beta$ alrededor del eje $Y$:

$$
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
=
\begin{bmatrix}
	\cos\beta & 0 & \text{sen}\,\beta \\
	0 & 1 & 0 \\
	-\text{sen}\,\beta & 0 & \cos\beta
\end{bmatrix}
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
$$

La transformación inversa correspondiente es:

$$
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
=
\begin{bmatrix}
	\cos\beta & 0 & -\text{sen}\,\beta \\
	0 & 1 & 0 \\
	\text{sen}\,\beta & 0 & \cos\beta
\end{bmatrix}
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
$$

`````

>[!summary] Rotación de coordenadas alrededor del eje $Y$ en un ángulo $\beta$ y su correspondiente transformación inversa.

---

### c) Rotacion Z $\gamma$

`````cornell
::cue
rotación en Z · eje Z · matriz de transformación
¿Cómo se define la matriz de rotación alrededor del eje $Z$?
¿Cómo se expresa la transformación inversa de coordenadas para una rotación en $Z$?
$$\mathbf{R}_z(\gamma)$$

::note
Considerando una rotación de un ángulo $\gamma$ alrededor del eje $Z$:

$$
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
=
\begin{bmatrix}
	\cos\gamma & -\text{sen}\,\gamma & 0 \\
	\text{sen}\,\gamma & \cos\gamma & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
$$

La transformación inversa correspondiente es:

$$
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
=
\begin{bmatrix}
	\cos\gamma & \text{sen}\,\gamma & 0 \\
	-\text{sen}\,\gamma & \cos\gamma & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	x \\y \\z
\end{bmatrix}
$$

`````

>[!summary] Rotación de coordenadas alrededor del eje $Z$ en un ángulo $\gamma$ y su correspondiente transformación inversa.

---

### d) Traslacion Z

`````cornell
::cue
traslación de ejes · vector de desplazamiento · 
¿Cómo se define matemáticamente una traslación en el espacio? · ¿Cuál es la relación entre los sistemas de coordenadas fijo y móvil?
$$\mathbf{r}' = \mathbf{a} + \mathbf{r}$$

---

![[ETN607T01.pdf#page=8&rect=60,598,234,761|ETN607T01, p.8]]
*Figura 1.14 · Esquema de traslación de ejes en el espacio*

::note

$$
\begin{bmatrix}
	x' \\ y' \\ z'
\end{bmatrix}
=
\begin{bmatrix}
	a \\ b \\ c
\end{bmatrix}
+
\begin{bmatrix}
	u \\ v \\ w
\end{bmatrix}
$$

$$
\begin{bmatrix}
	u \\ v \\ w
\end{bmatrix}
=
\begin{bmatrix}
	x' \\ y' \\ z'
\end{bmatrix}
-
\begin{bmatrix}
	a \\ b \\ c
\end{bmatrix}
$$
`````

>[!summary] La traslación de coordenadas representa un desplazamiento lineal del origen entre dos marcos de referencia paralelos, donde el nuevo vector de posición es la suma del vector de desplazamiento del origen y el vector original.

```ad-adiciones_1
title: Experimento
collapse: closed

![[ETN607T01.pdf#page=8&rect=82,392,494,560|ETN607T01, p.8]]

*Figura E1* , *Figura E2*
 
![[ETN607T01.pdf#page=8&rect=85,220,291,372|ETN607T01, p.8]]
*Figura E3*
$$P_i (0,0,0)$$
$$P_f (1,1,1)$$
 
$$3 = 2^2 + 2^2 - 2(2)(2) \cos \phi$$
 
$$\phi = 51.32^\circ$$
```

---

### e) Rotaciones Sucesivas

`````cornell
::cue
composición de matrices ·
¿Cómo se representa el cambio de coordenadas ante rotaciones sucesivas?
$$\mathbf{u} = R_y(\beta) \cdot R_z(\mu) \cdot \mathbf{X}$$

::note

Rotaciones$^2$ $Z$ $\quad$ Rotaciones$^2$ $y$

$$
\begin{bmatrix}
	u \\v \\w
\end{bmatrix}
=
\begin{bmatrix}
	\cos \beta & 0 & \sin \beta \\
	0 & 1 & 0 \\
	-\sin \beta & 0 & \cos \beta
\end{bmatrix}
\begin{bmatrix}
	\cos \mu & -\sin \mu & 0 \\
	\sin \mu & \cos \mu & 0 \\
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	X \\Y \\Z
\end{bmatrix}
$$
`````

> [!summary] La orientación final se obtiene mediante el producto de las matrices de rotación individuales aplicadas al vector de posición original.

---

## Velocidad - Vector

`````cornell
::cue
Vector velocidad · 
¿Cómo se define el vector velocidad en términos del vector posición?
$$\vec{v} = \frac{d\vec{R}}{dt}$$

::note
$$ \vec{v} = \dfrac{d\vec{R}}{dt} $$
`````

>[!summary] Definición del vector velocidad como la derivada temporal del vector posición.

---

### a) Coordenadas rectangulares

`````cornell
::cue
Vector posición · Vector velocidad · Coordenadas cartesianas
¿Cómo se expresan los vectores de posición y velocidad en coordenadas rectangulares?
$$\vec{v} = \dot{x} \hat{i} + \dot{y} \hat{j} + \dot{z} \hat{k}$$

::note
$$ \vec{R} = x\hat{i} + y\hat{j} + z\hat{k} $$

$$ \vec{v} = \dot{x}\hat{i} + \dot{y}\hat{j} + \dot{z}\hat{k} $$ 

modulo:

$$ v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2 $$
`````

>[!summary] Definición y componentes de los vectores de posición y velocidad, junto con su magnitud escalar, en el sistema rectangular cartesiano.

---

### b) Coordenadas cilindricas

`````cornell
::cue
[Vectores unitarios · Velocidad areolar · Aceleración]
¿Cuáles son los componentes de la velocidad en coordenadas cilíndricas?
¿Cómo varían los vectores unitarios con el tiempo?
$$\vec{a} = (\ddot{r} - r\dot{\theta}^{2})\hat{e}_{r} + (2\dot{r}\dot{\theta} + r\ddot{\theta})\hat{e}_{\theta} + \ddot{z}\hat{e}_{z}$$
---
![[ETN607T01.pdf#page=9&rect=73,294,284,455|ETN607T01, p.9]]
*Figura 1.15*

::note
$$
\vec{R} = r\hat{e}_{r} + z\hat{e}_{z} \quad
\begin{cases}
	\hat{e}_{r} & \text{No constante} \\
	\hat{e}_{z} & \text{Constante}
\end{cases}
$$

$$\vec{v} = \dot{r}\hat{e}_{r} + r\dot{\theta}\hat{e}_{\theta} + \dot{z}\hat{e}_{z}$$

---

$$\hat{e}_{r} = 1\cos\theta\hat{i} + 1\text{sen}\theta\hat{j}$$

````marginalia
$$\hat{e}_{\theta} = -\text{sen}\theta\hat{i} + \cos\theta\hat{j}$$%%<C- revisar %%
````

$$\dot{\hat{e}}_{r} = -\text{sen}\theta\dot{\theta}\hat{i} + \cos\theta\dot{\theta}\hat{j} = \dot{\theta}\hat{e}_{\theta}$$

$$\dot{\hat{e}}_{\theta} = -\text{sen}\theta\dot{\theta}\hat{j} - \cos\theta\dot{\theta}\hat{i} = -\dot{\theta}\hat{e}_{r}$$

---

$$\vec{v} = \dot{r}\hat{e}_{r} + (r\dot{\theta})\hat{e}_{\theta} + \dot{z}\hat{e}_{z}$$


```marginalia
$$v^{2} = \dot{r}^{2} + r^{2}\dot{\theta}^{2} + \dot{z}^{2}$$
%%<C- //$()^{2}$%%
```
```marginalia
$${\color{orange}
r^{2}\dot{\theta}^{2} : (v_{T} = \omega R)^{2}
}$$
%%<C-//$(2')$%%
```
---

$$\vec{a} = \ddot{r}\hat{e}_{r} + \dot{r}\dot{\hat{e}}_{r} + (\dot{r}\dot{\theta} + r\ddot{\theta})\hat{e}_{\theta} + (r\dot{\theta})\dot{\hat{e}}_{\theta} + \ddot{z}\hat{e}_{z}$$

$$\vec{a} = \ddot{r}\hat{e}_{r} + \dot{r}\dot{\theta}\hat{e}_{\theta} + (\dot{r}\dot{\theta} + r\ddot{\theta})\hat{e}_{\theta} - r\dot{\theta}^{2}\hat{e}_{r} + \ddot{z}\hat{e}_{z}$$


```marginalia
$$\vec{a} = (\ddot{r} - r\dot{\theta}^{2})\hat{e}_{r} + (2\dot{r}\dot{\theta} + r\ddot{\theta})\hat{e}_{\theta} + \ddot{z}\hat{e}_{z}$$
%%<C- //$(2'')$%%
```
`````

>[!summary] En coordenadas cilíndricas, la velocidad y aceleración incluyen términos debidos a la rotación del sistema de referencia local $\hat{e}_r, \hat{e}_\theta$.

``````ad-note
title: Complemento (Nivel C)
collapse: open
#### Versores en coordenadas cilíndricas

1. Definición formal
Los vectores unitarios $\hat{e}_r$ y $\hat{e}_\theta$ se definen en función de los incrementos de las coordenadas: $\hat{e}_r$ es el vector unitario que apunta en la dirección en que nos movemos cuando $r$ aumenta con $\theta$ y $z$ fijos, mientras que $\hat{e}_\theta$ es el vector unitario que apunta en la dirección del movimiento cuando $\theta$ aumenta con $r$ y $z$ fijos.

2. Idea clave
A diferencia de los vectores unitarios cartesianos $$\hat{i}, \hat{j}, \hat{k}$$, los versores $\hat{e}_r$ y $\hat{e}_\theta$ cambian sus direcciones a medida que el vector de posición $\vec{r}$ se desplaza, lo que genera derivadas temporales no nulas.

3. Figura o diagrama
```tikz
\usepackage{tikz}
\usepackage{tikz-3dplot}
\begin{document}
\tdplotsetmaincoords{70}{110}
\begin{tikzpicture}[tdplot_main_coords, scale=2]
    % Ejes
    \draw[->] (0,0,0) -- (1.5,0,0) node[anchor=north east]{$x$};
    \draw[->] (0,0,0) -- (0,1.5,0) node[anchor=north west]{$y$};
    \draw[->] (0,0,0) -- (0,0,1.5) node[anchor=south]{$z$};
    
    % Punto P
    \coordinate (P) at (1,1,1);
    \draw[dashed] (1,1,1) -- (1,1,0);
    \draw[dashed] (0,0,0) -- (1,1,0) node[midway, below]{$r$};
    \draw[->, orange, thick] (0,0,0) -- (P) node[midway, left]{$\vec{R}$};
    
    % Versores
    \draw[->, teal, ultra thick] (P) -- (1.4,1.4,1) node[anchor=west]{$\hat{e}_r$};
    \draw[->, teal, ultra thick] (P) -- (0.7,1.3,1) node[anchor=south east]{$\hat{e}_\theta$};
    \draw[->, teal, ultra thick] (P) -- (1,1,1.4) node[anchor=west]{$\hat{e}_z$};
    
    % Ángulo theta
    \draw[->] (0.5,0,0) arc (0:45:0.5);
    \node at (0.6,0.2,0) {$\theta$};
\end{tikzpicture}
\end{document}
```

4. Derivadas temporales y cinemática
Para obtener la velocidad y aceleración, primero se definen las derivadas de los versores considerando su rotación:
$$\begin{array}{l}
	\dot{e}_r = \dot{\theta} \hat{e}_\theta \\
	\dot{e}_\theta = -\dot{\theta} \hat{e}_r
\end{array}$$

Partiendo del vector de posición $\vec{R} = r \hat{e}_r + z \hat{k}$, se deriva respecto al tiempo:

##### Obtención de la Velocidad

$$\vec{v} = \frac{d\vec{R}}{dt} = \dot{r} \hat{e}_r + r \dot{e}_r + \dot{z} \hat{k} = \dot{r} \hat{e}_r + r \dot{\theta} \hat{e}_\theta + \dot{z} \hat{k}$$

##### Obtención de la Aceleración
Derivando nuevamente el vector velocidad:

$$\vec{a} = \frac{d\vec{v}}{dt} = (\ddot{r}\hat{e}_r + \dot{r}\dot{e}_r) + (\dot{r}\dot{\theta}\hat{e}_\theta + r\ddot{\theta}\hat{e}_\theta + r\dot{\theta}\dot{e}_\theta) + \ddot{z}\hat{k}$$

Sustituyendo $\dot{e}_r$ y $\dot{e}_\theta$ y agrupando términos:

$$\vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{e}_\theta + \ddot{z}\hat{k}$$

5. Ejercicio resuelto
##### Ej. Componentes de aceleración para una cuenta en un alambre circular giratorio.
Un alambre circular de radio $R$ gira con velocidad angular constante $\Omega$. Una cuenta se mueve sobre él. Determine la aceleración en el sistema rotatorio $\hat{e}_\theta$.
En este caso, $r = R$ (constante), por lo que $\dot{r} = \ddot{r} = 0$. La velocidad angular es $\dot{\theta} = \Omega$.
Sustituyendo en la fórmula general de aceleración:

$$
\begin{array}{l}
	a_r = 0 - R\Omega^2 = -R\Omega^2 \\
	a_\theta = R(0) + 2(0)(\Omega) = 0 \\
	a_z = 0
\end{array}
$$

La aceleración es puramente radial (centrípeta): $\vec{a} = -R\Omega^2 \hat{e}_r$.
``````

---

### c) Coordenadas esféricas

`````cornell
::cue
Vector posición · Vector velocidad · Coordenadas esféricas
¿Cómo se definen los vectores de posición y velocidad en el sistema esférico?
$$\vec{v} = \dot{\rho} \hat{e}_{\rho} + \rho \dot{\theta} \hat{e}_{\theta} + \rho \dot{\phi} \sin \theta \hat{e}_{\phi}$$

---

![[ETN607T01.pdf#page=10&rect=73,565,284,727|ETN607T01, p.10]]
*Figura 1.16 · Esquema de coordenadas esféricas 3D*

::note
$$ \vec{R} = \rho \hat{e}_{\rho} $$

$$ \vec{v} = \dot{\rho} \hat{e}_{\rho} + \rho \dot{\hat{e}}_{\rho} $$

$$ \hat{e}_{\rho} = \sin \theta \cos \phi \hat{i} + \sin \theta \sin \phi \hat{j} + \cos \theta \hat{k} $$

$$ \hat{e}_{\phi} = -\sin \phi \hat{i} + \cos \phi \hat{j} $$

---

$$
\hat{e}_{\theta} = \hat{e}_{\phi} \times \hat{e}_{\rho} =
\begin{vmatrix}
	\hat{i} & \hat{j} & \hat{k} \\
	-\sin \phi & \cos \phi & 0 \\
	\sin \theta \cos \phi & \sin \theta \sin \phi & \cos \theta
\end{vmatrix}
$$

$$\hat{e}_{\theta} = \cos \theta \cos \phi \hat{i} + \cos \theta \sin \phi \hat{j} - \sin \theta \hat{k}$$

$$\dot{\hat{e}}_{\rho} = (\cos \theta \dot{\theta} \cos \phi - \sin \theta \sin \phi \dot{\phi}) \hat{i} + (\cos \theta \dot{\theta} \sin \phi + \sin \theta \cos \phi \dot{\phi}) \hat{j} - \dots$$
$$\dots - \sin \theta \dot{\theta} \hat{k}$$

$$\dot{\hat{e}}_{\rho} = \dot{\phi} \sin \theta \hat{e}_{\phi} + \dot{\theta} \hat{e}_{\theta}$$

```marginalia
$$\vec{v} = \dot{\rho} \hat{e}_{\rho} + \rho \dot{\theta} \hat{e}_{\theta} + \rho \dot{\phi} \sin \theta \hat{e}_{\phi} $$ 
%%<C- $C_3'$%%
```
```marginalia
$$ v^2 = \dot{\rho}^2 + \rho^2 \dot{\theta}^2 + \rho^2 \dot{\phi}^2 \sin^2 \theta $$ %%<C- $C_3''$%%
```
`````

>[!summary] Definición cinemática del vector velocidad en coordenadas esféricas mediante la derivación de vectores unitarios rotacionales.

---

## Velocidad escalar

`````cornell
::cue
magnitud de velocidad · coordenadas curvilíneas · Matlab
¿Cómo se define la velocidad escalar en términos de componentes cartesianas?
¿Cuál es el procedimiento para obtener la velocidad escalar en coordenadas cilíndricas?
¿Cómo se implementa la derivada simbólica en Matlab para coordenadas esféricas?
$$v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$$
ver también: $C_2'$ — transformaciones de coordenadas

::note

siempre
```marginalia
$$v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$$ %%< ! Eliminar $x, y, z$ %%
```
---

a) $\checkmark$

---

b)
$$
\begin{array}{l} 
	x = r \cos \theta \implies \dot{x} = \dot{r} \cos \theta - r \sin \theta \dot{\theta} \\ 
	y = r \sin \theta \implies \dot{y} = \dot{r} \sin \theta + r \cos \theta \dot{\theta} \\ 
	z = z \implies \dot{z} = \dot{z} 
\end{array}
$$

$$v^2 = \dot{r}^2 \cos^2 \theta - 2 \dot{r} \dot{\theta} r \sin \theta \cos \theta + r^2 \dot{\theta}^2 \sin^2 \theta + \dot{r}^2 \sin^2 \theta + 2 \dot{r} \dot{\theta} r \sin \theta \cos \theta \dots$$
$$\dots + r^2 \dot{\theta}^2 \cos^2 \theta + \dot{z}^2$$

```marginalia
$$v^2 = \dot{r}^2 + r^2 \dot{\theta}^2 + \dot{z}^2$$ %%<C- ver $C_2'$%%
```

---

c) 
$$
\begin{array}{l}
x = \ell \sin\theta \cos\phi
\quad ; \quad
\dot{x} =
\dot{\ell}\sin\theta\cos\phi
+ \ell\cos\theta\,\dot{\theta}\cos\phi
- \ell\sin\theta\sin\phi\,\dot{\phi}
\\[6pt]
y = \ell\sin\theta\sin\phi
\\[6pt]
z = \ell\cos\theta
\end{array}
$$
`````

>[!summary] Determinación de la velocidad escalar mediante la expansión de derivadas en coordenadas cilíndricas y esféricas y su representación simbólica.

````ad-importante_1
title: Tarea (MatLab)
collapse: closed

```matlab
syms t r(t) th(t) f(t)
X = r * sin(th) * cos(f) ;
y
z
dx = diff(X, t, 1)
```
````

---

### Llevando a 2D para intentar resolverlos.

`````cornell
::cue
Cálculo 2D · Área y ángulo · 
¿Cómo se determina el cuadrado de la velocidad en función de $A$ y $\theta$?
$$v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$$

---

![[ETN607T01.pdf#page=11&rect=65,122,250,237|ETN607T01, p.11]]
*Figura 1.17*

::note
$$v(A, \theta) = ?$$

---
```marginalia
a) $\vec{v}$ No se puede $\vec{R}$ %%<C- Newton %%
```

---

b) $v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$

$$A = \frac{xy}{2}$$

$$\tan \theta = \frac{y}{x}$$

$$y = \pm \sqrt{2A \tan \theta} \implies \dot{y} = \frac{2 (\dot{A} \tan \theta + A \sec^2 \theta \dot{\theta})}{2 \sqrt{2A \tan \theta}}$$

$$x = \pm \sqrt{\frac{2A}{\tan \theta}} \implies \dot{x} = \frac{2}{2} \sqrt{\frac{\tan \theta}{2A}} \left( \frac{\dot{A} \tan \theta - A \sec^2 \theta \dot{\theta}}{\tan^2 \theta} \right)$$

$$ v^2 = \frac{[\dot{A} \tan \theta + A \sec^2 \theta \dot{\theta}]^2}{2A \tan \theta} + \frac{\tan \theta}{2A} \left( \frac{\dot{A} \tan \theta - A \sec^2 \theta \dot{\theta}}{\tan^2 \theta} \right)^2 $$
`````

>[!summary] Determinación de las componentes de velocidad escalar mediante la parametrización de coordenadas en función del área y el ángulo.

---

## Energia Cinetica

`````cornell
::cue
Energía cinética · Escalar · Velocidad
¿Cuál es la expresión escalar de la energía cinética tras el desarrollo de la velocidad?
$$T = \frac{1}{2} m v^2$$

::note
$$T = \frac{1}{2} m v^2 \ \text{(Escalar)}$$
`````

> [!summary] Expresión de la energía cinética en su forma escalar como producto de la mitad de la masa por la velocidad al cuadrado.

---

## Grados de libertad $DOF$

`````cornell
::cue
Grados de libertad · DOF · Restricciones
¿Cuántos DOF posee una partícula, una varilla y un cuerpo rígido en el espacio?
¿Qué efecto tienen los cables y las rótulas sobre los grados de libertad?
N = 3, 5, 6

::note
a) Particula $N=3$

---

b) Varilla $N=5$
![[ETN607T01.pdf#page=12&rect=152,240,346,386|ETN607T01, p.12]]
*Figura 1.18*

---

c) Cuerpo $N=6$
![[ETN607T01.pdf#page=12&rect=139,67,310,186|ETN607T01, p.12]]
*Figura 1.19*

---

d) Cable quita 1

e) Rotula quita 3

![[ETN607T01.pdf#page=13&rect=79,553,276,725|ETN607T01, p.13]]
*Figura 1.20 · Dedo N=4, Mano N=19*

---

![[ETN607T01.pdf#page=13&rect=308,554,493,725|ETN607T01, p.13]]
*Figura 1.21*

`````

> [!summary] Definición de los grados de libertad $DOF$ para sistemas básicos y el impacto de restricciones mecánicas específicas en la reducción de la movilidad.











