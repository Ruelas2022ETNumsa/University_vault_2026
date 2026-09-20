# Ejercicios ETN607 — Parcial 2 (T4)

---

## E1 — Sistema masa-resorte horizontal con dos masas colgantes

### Descripción del sistema

Un bloque de masa $m_1$ está apoyado sobre una superficie horizontal sin fricción y conectado a una pared fija mediante un resorte horizontal de constante $K$ y longitud natural $\ell_0$. El resorte conecta la pared izquierda con el bloque. El bloque tiene ancho $b_1$.

Del bloque cuelga, por medio de un cable inextensible que pasa por una polea fija en el borde del bloque, una masa $m_2$. Debajo de $m_2$ hay un resorte de constante $K'$ y longitud natural $\ell_0'$ que conecta $m_2$ con una tercera masa $m_3$ que cuelga libremente.

El cable que une $m_1$ con $m_2$ es inextensible, de modo que la velocidad horizontal de $m_1$ es igual a la velocidad vertical de $m_2$.

Las masas $m_2$ y $m_3$ se mueven solo en la vertical. El bloque $m_1$ se mueve solo en la horizontal.

### Coordenadas y restricciones

- Coordenadas posibles: $x_1$ (posición horizontal de $m_1$), $y_2$ (posición vertical de $m_2$), $y_3$ (posición vertical de $m_3$)
- Restricción del cable inextensible: $\dot{x}_1 = \dot{y}_2$, por lo tanto $x_1 = y_2 + C$
- Grados de libertad: $N = 2$ (coordenadas independientes: $x_1$ e $y_3$)

### Se pide

Obtener las ecuaciones de movimiento (EDOs) del sistema usando las ecuaciones de Lagrange. Expresar $T$ y $V$ en función de las coordenadas generalizadas independientes. Obtener una EDO por cada grado de libertad.

---

## E2 — Bloque en plano inclinado conectado por cable a masa colgante

### Descripción del sistema

Un bloque de masa $m_1$ puede deslizarse sin fricción sobre un plano inclinado a $60°$ respecto de la horizontal. El plano está fijo a una pared. El bloque está conectado mediante un resorte horizontal de constante $K$ y longitud natural $\ell_0$ a la pared vertical izquierda. La longitud horizontal entre la pared y el punto de anclaje en el bloque es $B_2$, y la longitud natural del resorte en reposo deja una distancia $B_1$ libre.

Un cable inextensible conecta el bloque $m_1$ con una masa $m_2$ que cuelga verticalmente. El cable corre paralelo al plano inclinado hasta una polea en el vértice superior del plano, y luego baja verticalmente.

La restricción geométrica del cable y el plano a $60°$ implica que la velocidad vertical de $m_2$ es proporcional a la velocidad horizontal de $m_1$: $\dot{y}_2 = -\dfrac{1}{\sqrt{3}}\,\dot{x}_1$.

El sistema tiene un solo grado de libertad: $N = 1$. Se elige $x_1$ como coordenada generalizada.

**Nota del docente:** no conviene usar el centro de masa como referencia.

### Coordenadas y restricciones

- Coordenadas posibles: $x_1$ (desplazamiento horizontal del bloque), $y_2$ (posición vertical de $m_2$)
- Restricción: $\dot{y}_2 = -\dfrac{1}{\sqrt{3}}\,\dot{x}_1$
- Grados de libertad: $N = 1$

### Se pide

Obtener la ecuación de movimiento (EDO) del sistema usando Lagrange. Expresar $T$ y $V$ en función de $x_1$ únicamente. Obtener una sola EDO.

---

## E3 — Sistema de tres masas con dos resortes y polea

### Descripción del sistema

Una masa $m_1$ está suspendida verticalmente de un resorte de constante $K$ y longitud natural $\ell_0$, cuyo extremo superior está fijo al techo. Debajo de $m_1$ pasa un cable inextensible que rodea una polea de radio $R_2$ ubicada en la parte inferior de $m_1$. La polea tiene momento de inercia $J = 0$ (se desprecia). Del cable cuelgan una masa $m_2$ a un lado y una masa $m_3$ al otro lado.

Debajo del conjunto hay un resorte de constante $K'$ y longitud natural $\ell_0'$ que conecta la masa $m_2$ con el piso (o una referencia fija inferior).

La altura total del sistema es $H$. La longitud del cable es $\ell$.

El sistema tiene $N = 3 - 1 = 2$ grados de libertad. Se eligen como coordenadas generalizadas independientes $y_3$ (posición de $m_3$) y $a$ (posición relativa de $m_2$ respecto de la polea).

La restricción del cable impone: $H - y_2 + \pi R_2 + y_3 - y_3 = \ell$, de donde se obtiene $\dot{y}_2 = \dot{y}_3 / 2$ en la versión simplificada.

**Nota del docente:** el sistema tiene además la relación $y_2 = y_1 + a$ y $y_1 = y_2 - a$.

### Coordenadas y restricciones

- Coordenadas posibles: $y_1$, $y_2$, $y_3$, $a$
- Restricción cable: $H - y_2 + \pi R_2 + y_3 - y_3 = \ell$
- Coordenadas independientes: $y_3$ y $a$
- Grados de libertad: $N = 2$

### Se pide

Obtener las ecuaciones de movimiento del sistema usando Lagrange. Expresar $T$ y $V$ en función de $y_3$ y $a$. Obtener dos EDOs, una por cada coordenada generalizada.

---

## E4 — Carro con péndulo simple (péndulo sobre carro móvil)

### Descripción del sistema

Un carro de masa $M$ rueda sin fricción sobre una superficie horizontal plana. El carro puede desplazarse libremente en la dirección horizontal. Sobre el carro está articulado un péndulo simple: una varilla rígida de longitud $\ell$ con una masa puntual $m$ en su extremo. El péndulo puede oscilar libremente en el plano vertical que contiene el movimiento del carro.

El punto de articulación del péndulo está fijo al carro, a una altura $H$ sobre el suelo (el carro tiene altura $H$). Cuando el péndulo forma un ángulo $\theta$ con la vertical, la posición de la masa $m$ respecto del suelo es:

$$x_2 = x + \ell \sin\theta \qquad y_2 = H + \ell \cos\theta$$

donde $x$ es la posición horizontal del carro.

El sistema no tiene restricciones adicionales. Tiene $N = 2$ grados de libertad. Se eligen $x$ y $\theta$ como coordenadas generalizadas.

**Nota del docente:** este ejercicio genera un informe de 3 hojas (péndulo). En el informe se debe anular $\sin\theta$ para linealizar y regularizar ($\mathcal{X}$).

### Coordenadas

- $x$: posición horizontal del carro $M$
- $\theta$: ángulo del péndulo respecto de la vertical
- Grados de libertad: $N = 2$

### Se pide

Obtener las dos ecuaciones de movimiento del sistema usando Lagrange, una para $x$ y otra para $\theta$. Expresar $T = T_1 + T_2$ y $V$ en función de $x$, $\theta$ y sus derivadas. Las EDOs encuadradas son el resultado final. Verificar usando el Lagrangiano $L = T - V$.

---

## E5 — Péndulo doble (dos péndulos acoplados de igual longitud)

### Descripción del sistema

Dos masas puntuales $m_1$ y $m_2$ forman un péndulo doble planar. Ambas varillas tienen la misma longitud $\ell$.

- La masa $m_1$ está articulada al techo mediante una varilla rígida de longitud $\ell$. Forma un ángulo $\theta$ con la vertical.
- La masa $m_2$ está articulada al extremo de la primera varilla mediante otra varilla rígida de longitud $\ell$. Forma un ángulo $\phi$ con la vertical (medido desde la dirección de la primera varilla extendida).

Las posiciones de las masas respecto del punto de articulación superior son:

$$x_1 = \ell\sin\theta \qquad y_1 = -\ell\cos\theta$$

$$x_2 = \ell\sin\theta + \ell\sin\phi \qquad y_2 = -\ell\cos\theta - \ell\cos\phi$$

Las velocidades de $m_2$:

$$\dot{x}_2 = \ell\cos\theta\,\dot{\theta} + \ell\cos\phi\,\dot{\phi} \qquad \dot{y}_2 = \ell\sin\theta\,\dot{\theta} + \ell\sin\phi\,\dot{\phi}$$

El sistema no tiene restricciones adicionales. Tiene $N = 2$ grados de libertad. Se eligen $\theta$ y $\phi$ como coordenadas generalizadas.

### Coordenadas

- $\theta$: ángulo de la primera varilla respecto de la vertical
- $\phi$: ángulo de la segunda varilla respecto de la vertical
- Grados de libertad: $N = 2$

### Se pide

Obtener las dos ecuaciones de movimiento del sistema usando Lagrange, una para $\theta$ y otra para $\phi$. Expresar $T = T_1 + T_2$ y $V$ en función de $\theta$, $\phi$ y sus derivadas. Las EDOs encuadradas son el resultado final.

---

## Resumen

| Ejercicio | Sistema | Coord. generalizadas | N |
|---|---|---|---|
| E1 | Bloque horizontal + 2 masas colgantes + resortes | $x_1,\ y_3$ | 2 |
| E2 | Bloque en plano 60° + masa colgante | $x_1$ | 1 |
| E3 | 3 masas + polea + 2 resortes | $y_3,\ a$ | 2 |
| E4 | Carro + péndulo simple | $x,\ \theta$ | 2 |
| E5 | Péndulo doble (igual longitud) | $\theta,\ \phi$ | 2 |

Todos los ejercicios corresponden a **T4 — Ec. de Lagrange para un sistema de partículas**.
Fuentes de referencia: Wells Cap. 4–5 · Taylor Cap. 7 · Goldstein Cap. 1–2.
