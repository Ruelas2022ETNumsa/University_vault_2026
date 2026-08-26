$$
\text{Sistema: péndulo longitud fija } \ell, \text{ resorte } (k, \ell_0) \text{ desde el piso, } N=1, \; q = \theta
$$

**Coordenadas de la masa** (origen en el piso, $y$ hacia arriba):

$$
x = \ell\sin\theta \qquad y = H - \ell\cos\theta
$$

**Longitud del resorte** — ley de cosenos en triángulo $(H, \ell, r)$:

$$
r = \sqrt{x^2 + y^2} = \sqrt{\ell^2\sin^2\theta + (H-\ell\cos\theta)^2} = \sqrt{H^2 + \ell^2 - 2H\ell\cos\theta}
$$

**Velocidades** ($\dot{r}=0$ porque $\ell$ es fijo, $\dot{z}=0$):

$$
\dot{x} = \ell\dot{\theta}\cos\theta \qquad \dot{y} = \ell\dot{\theta}\sin\theta
$$

$$
T = \frac{m}{2}(\dot{x}^2+\dot{y}^2) = \frac{m}{2}\ell^2\dot{\theta}^2\underbrace{(\cos^2\theta+\sin^2\theta)}_{=1} = \frac{m}{2}\ell^2\dot{\theta}^2
$$

**Energía potencial:**

$$
V = mgy + \frac{1}{2}k(r-\ell_0)^2 = mg(H-\ell\cos\theta) + \frac{1}{2}k(r-\ell_0)^2
$$

**Lagrangiano $L = T - V$:**

$$
L = \frac{m}{2}\ell^2\dot{\theta}^2 - mg(H-\ell\cos\theta) - \frac{1}{2}k(r-\ell_0)^2
$$

**Derivadas:**

$$
\frac{\partial L}{\partial\dot{\theta}} = m\ell^2\dot{\theta} \qquad \Rightarrow \qquad \frac{d}{dt}\!\left(\frac{\partial L}{\partial\dot{\theta}}\right) = m\ell^2\ddot{\theta}
$$

$$
\frac{\partial r}{\partial\theta}: \quad 2r\frac{\partial r}{\partial\theta} = 2H\ell\sin\theta \quad \Rightarrow \quad \frac{\partial r}{\partial\theta} = \frac{H\ell\sin\theta}{r}
$$

$$
\frac{\partial L}{\partial\theta} = -mg\ell\sin\theta - k(r-\ell_0)\cdot\frac{H\ell\sin\theta}{r} = -mg\ell\sin\theta - kH\ell\sin\theta\!\left(1-\frac{\ell_0}{r}\right)
$$

**GDE** $\;\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial\dot{\theta}}\right) - \dfrac{\partial L}{\partial\theta} = 0$:

$$
m\ell^2\ddot{\theta} - \left[-mg\ell\sin\theta - kH\ell\sin\theta\!\left(1-\frac{\ell_0}{r}\right)\right] = 0
$$

$$
\boxed{m\ell^2\ddot{\theta} + \left[mg + kH\!\left(1-\frac{\ell_0}{r}\right)\right]\ell\sin\theta = 0}
$$

$$
r = \sqrt{H^2 + \ell^2 - 2H\ell\cos\theta}
$$