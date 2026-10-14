## Enunciado 8 (ej8T5) — Péndulo que se desenrolla de un cilindro fijo

Un cilindro fijo de radio R tiene un hilo inextensible y sin masa enrollado en su superficie. Del extremo libre del hilo cuelga una masa m. El origen está en el centro del cilindro, con x horizontal y y vertical hacia abajo. En θ = 0 el hilo sale tangente al cilindro en el punto $(R, 0)$ y cuelga vertical con una longitud libre l. Al girar un ángulo θ, la parte libre del hilo (tangente al cilindro) mide d = l + R·θ. Hay fricción en la masa, f = c·vⁿ.

**Se pide:**
1. N y coordenada generalizada.
2. Posición $x, y$ y velocidad de la masa en función de θ y θ̇.
3. T y V.
4. P para n = 1 y para n = 2.
5. La EDO de movimiento para n = 2 mediante Lagrange; indicar cómo cambia para n = 1.

---

### Solución

**1. N y coordenada**

$$
N = 2 - 1 = 1, \qquad q = \theta
$$

**2. Posición y velocidad** (con $d = l + R\theta$)

Punto de tangencia $Q = (R\cos\theta,\,-R\sin\theta)$, tramo libre en la dirección $(\sin\theta,\ \cos\theta)$:

$$
x = R\cos\theta + d\sin\theta, \qquad y = -R\sin\theta + d\cos\theta
$$

$$
\dot{x} = d\cos\theta\,\dot{\theta}, \qquad \dot{y} = -d\sin\theta\,\dot{\theta}, \qquad v = d\,|\dot{\theta}|
$$

**3. T y V** ($y$ hacia abajo, $V = 0$ en $y = 0$)

$$
T = \frac{1}{2}m\,d^2\dot{\theta}^2, \qquad V = -mgy = mgR\sin\theta - mg\,d\cos\theta
$$

**4. P** ($P = \dfrac{c\,v^{n+1}}{n+1}$)

$$
P_{n=1} = \frac{1}{2}c\,d^2\dot{\theta}^2, \qquad P_{n=2} = \frac{1}{3}c\,d^3|\dot{\theta}|^3
$$

**5. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta} - \frac{\partial P}{\partial \dot{\theta}}
$$

Derivadas:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m\,d^2\ddot{\theta} + 2mR\,d\,\dot{\theta}^2, \qquad \frac{\partial T}{\partial \theta} = mR\,d\,\dot{\theta}^2, \qquad \frac{\partial V}{\partial \theta} = mg\,d\sin\theta
$$

$$
\frac{\partial P_{n=2}}{\partial \dot{\theta}} = c\,d^3\dot{\theta}|\dot{\theta}|, \qquad \frac{\partial P_{n=1}}{\partial \dot{\theta}} = c\,d^2\dot{\theta}
$$

Sustituyendo ($n = 2$) y dividiendo entre $m\,d^2$:

$$
m\,d^2\ddot{\theta} + mR\,d\,\dot{\theta}^2 + mg\,d\sin\theta + c\,d^3\dot{\theta}|\dot{\theta}| = 0
$$

Para $n = 1$, el término de fricción pasa a $\dfrac{c}{m}\dot{\theta}$.

**6. Verificación**

Con $c = 0$: $\ddot{\theta} + \dfrac{R}{d}\dot{\theta}^2 + \dfrac{g}{d}\sin\theta = 0$ (péndulo de evolvente conservativo). Dimensional: $[c] = \text{kg/m}$ y todos los términos quedan en rad/s².

---

### Resultado final

$$
\boxed{\;n=2:\quad \ddot{\theta} = -\frac{R}{l+R\theta}\dot{\theta}^2 - \frac{g}{l+R\theta}\sin\theta - \frac{c}{m}(l+R\theta)\,\dot{\theta}|\dot{\theta}|\;}
$$

$$
\boxed{\;n=1:\quad \ddot{\theta} = -\frac{R}{l+R\theta}\dot{\theta}^2 - \frac{g}{l+R\theta}\sin\theta - \frac{c}{m}\,\dot{\theta}\;}
$$
