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

Coordenadas $(x, y)$ con 1 restricción (hilo inextensible y tenso).

$$
N = 2 - 1 = 1, \qquad q = \theta
$$

**2. Posición y velocidad**

El punto de tangencia es $Q = (R\cos\theta,\, -R\sin\theta)$ y el tramo libre, de longitud $d = l + R\theta$, tiene dirección tangente $(\sin\theta,\, \cos\theta)$:

$$
x = R\cos\theta + (l + R\theta)\sin\theta, \qquad y = -R\sin\theta + (l + R\theta)\cos\theta
$$

$$
\dot{x} = (l + R\theta)\cos\theta\,\dot{\theta}, \qquad \dot{y} = -(l + R\theta)\sin\theta\,\dot{\theta}
$$

(los términos $\pm R\dot\theta\sin\theta$ y $\pm R\dot\theta\cos\theta$ se cancelan)

$$
v^2 = (l + R\theta)^2\dot{\theta}^2
$$

**3. T, V**

$$
T = \frac{m}{2}(l + R\theta)^2\dot{\theta}^2, \qquad V = -mgy = mgR\sin\theta - mg(l + R\theta)\cos\theta
$$

**4. P** ($P = c\,v^{n+1}/(n+1)$)

$$
P_{n=1} = \frac{c}{2}(l + R\theta)^2\dot{\theta}^2, \qquad P_{n=2} = \frac{c}{3}(l + R\theta)^3|\dot{\theta}|^3
$$

**5. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta} - \frac{\partial P}{\partial \dot{\theta}}
$$

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m(l + R\theta)^2\ddot{\theta} + 2mR(l + R\theta)\dot{\theta}^2, \qquad \frac{\partial T}{\partial \theta} = mR(l + R\theta)\dot{\theta}^2
$$

$$
\frac{\partial V}{\partial \theta} = mg(l + R\theta)\sin\theta
$$

$$
\frac{\partial P_{n=2}}{\partial \dot{\theta}} = c(l + R\theta)^3\dot{\theta}|\dot{\theta}|, \qquad \frac{\partial P_{n=1}}{\partial \dot{\theta}} = c(l + R\theta)^2\dot{\theta}
$$

Dividiendo entre $m(l + R\theta)^2$:

$$
n = 2:\quad \ddot{\theta} = -\frac{R}{l + R\theta}\dot{\theta}^2 - \frac{g}{l + R\theta}\sin\theta - \frac{c}{m}(l + R\theta)\dot{\theta}|\dot{\theta}|
$$

**6. Para n = 1**

El último término pasa a ser $-\dfrac{c}{m}\dot{\theta}$.

**7. Verificación**

$[c] = \text{kg/m}$ para n = 2, y todos los términos quedan en rad/s². Con $c = 0$ se obtiene la ecuación del péndulo de evolvente: $(l + R\theta)\ddot\theta + R\dot\theta^2 + g\sin\theta = 0$.

---

### Resultado final

$$
\boxed{\;\ddot{\theta} = -\frac{R\,\dot{\theta}^2 + g\sin\theta}{l + R\theta} - \frac{c}{m}(l + R\theta)\dot{\theta}|\dot{\theta}|\;}\quad (n = 2)
$$

$$
\boxed{\;\ddot{\theta} = -\frac{R\,\dot{\theta}^2 + g\sin\theta}{l + R\theta} - \frac{c}{m}\dot{\theta}\;}\quad (n = 1)
$$
