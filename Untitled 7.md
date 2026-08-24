### Ejercicio 1 — Resorte péndulo

![[paso607-24-08-2026_17-16-06.png]]

**Sistema:** Una masa $m$ cuelga de un resorte de constante $k$ y longitud natural $l_0$, fijado al techo. La masa puede oscilar (ángulo $\theta$ desde la vertical) y el resorte puede extenderse o comprimirse (longitud instantánea $r$). El sistema opera en el plano vertical — dos grados de libertad: $r$ y $\theta$.

---

#### Paso 1 — Establecer coordenadas

El eje $y$ apunta hacia abajo (dirección de la gravedad). Las coordenadas cartesianas en función de $(r, \theta)$ son:

$$
x = r\sin\theta \qquad y = r\cos\theta
$$

Derivando para obtener las velocidades:

$$
\dot x = \dot r\sin\theta + r\dot\theta\cos\theta \qquad
\dot y = \dot r\cos\theta - r\dot\theta\sin\theta
$$

---

#### Paso 2 — Energía cinética $T$

$$
T = \frac{1}{2}m(\dot x^2 + \dot y^2)
$$

Expandiendo $\dot x^2 + \dot y^2$ y simplificando (los términos cruzados se cancelan):

$$
\dot x^2 + \dot y^2 = \dot r^2 + r^2\dot\theta^2
$$

Por lo tanto:

$$
T = \frac{1}{2}m\left(\dot r^2 + r^2\dot\theta^2\right)
$$

> Esta es la expresión estándar de la energía cinética en coordenadas polares planas.

---

#### Paso 3 — Energía potencial $V$

Hay dos fuentes de energía potencial:

- **Resorte** (elástica): $\dfrac{1}{2}k(r - l_0)^2$
- **Gravedad** (con $y$ hacia abajo, $y = r\cos\theta$): $-mgy = -mgr\cos\theta$

$$
V = \frac{1}{2}k(r-l_0)^2 - mgr\cos\theta
$$

---

#### Paso 4 — Lagrangiano $L = T - V$

$$
L = \frac{1}{2}m\left(\dot r^2 + r^2\dot\theta^2\right) - \frac{1}{2}k(r-l_0)^2 + mgr\cos\theta
$$

---

#### Paso 5 — Ecuación de Euler-Lagrange para $r$

La ecuación de Euler-Lagrange es:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot r}\right) - \frac{\partial L}{\partial r} = 0
$$

**Calculando cada término:**

$$
\frac{\partial L}{\partial\dot r} = m\dot r
\qquad\Rightarrow\qquad
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot r}\right) = m\ddot r
$$

$$
\frac{\partial L}{\partial r} = mr\dot\theta^2 - k(r-l_0) + mg\cos\theta
$$

> El término $mr\dot\theta^2$ viene de derivar $\frac{1}{2}mr^2\dot\theta^2$ respecto a $r$. El término $-k(r-l_0)$ es la fuerza elástica. El término $mg\cos\theta$ es la componente de la gravedad en dirección radial.

**Aplicando la ecuación:**

$$
m\ddot r - \left[mr\dot\theta^2 - k(r-l_0) + mg\cos\theta\right] = 0
$$

> [!important]
> $$
> \boxed{m(\ddot r - r\dot\theta^2) = -k(r-l_0) + mg\cos\theta}
> $$

**Lectura física:** el lado izquierdo es la aceleración radial neta (traslación menos la centrífuga); el lado derecho son las fuerzas en dirección $r$ — el resorte restituye hacia $l_0$ y la gravedad empuja radialmente hacia afuera cuando $\theta < 90°$.

---

#### Paso 6 — Ecuación de Euler-Lagrange para $\theta$

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot\theta}\right) - \frac{\partial L}{\partial\theta} = 0
$$

**Calculando cada término:**

$$
\frac{\partial L}{\partial\dot\theta} = mr^2\dot\theta
\qquad\Rightarrow\qquad
\frac{d}{dt}\left(mr^2\dot\theta\right) = m(2r\dot r\dot\theta + r^2\ddot\theta)
$$

> La derivada de $r^2\dot\theta$ respecto al tiempo requiere regla del producto: $2r\dot r\dot\theta + r^2\ddot\theta$.

$$
\frac{\partial L}{\partial\theta} = -mgr\sin\theta
$$

**Aplicando la ecuación:**

$$
m(2r\dot r\dot\theta + r^2\ddot\theta) + mgr\sin\theta = 0
$$

> [!important]
> $$
> \boxed{m(2r\dot r\dot\theta + r^2\ddot\theta) = -mgr\sin\theta}
> $$

---

#### Paso 7 — Caso particular: péndulo simple ($r = l = \text{cte}$)

Si el resorte no se extiende y la longitud es fija $r = l$, entonces $\dot r = 0$ y $\ddot r = 0$. La ecuación de $\theta$ se simplifica:

$$
m(0 + l^2\ddot\theta) = -mgl\sin\theta
$$

Dividiendo por $ml$:

> [!important]
> $$
> \boxed{l\ddot\theta = -g\sin\theta}
> $$

> Este es el resultado clásico del péndulo simple. En el buffer figuraba $l^2\ddot\theta = -gl\sin\theta$ — ambas formas son equivalentes algebraicamente pero la forma canónica es $l\ddot\theta = -g\sin\theta$.
