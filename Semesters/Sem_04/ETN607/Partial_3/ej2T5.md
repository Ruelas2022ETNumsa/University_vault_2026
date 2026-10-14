## Enunciado 2 (ej2T5) — Partícula sobre una barra parabólica

Una partícula de masa m se mueve obligada sobre una barra con forma de parábola y = 4x², en un plano vertical (y positiva hacia arriba, gravedad g). Entre la partícula y la barra hay fricción viscosa lineal, f = c·v (n = 1).

**Se pide:**
1. Grados de libertad N y la coordenada generalizada elegida (la restricción reduce N de 2 a 1).
2. ẏ en función de x y ẋ.
3. T, V y P en función de x y ẋ.
4. La EDO de movimiento (modelo matemático) mediante Lagrange.

---

### Solución

**1. N y coordenada**

Restricción: $y = 4x^2$ (1 restricción).

$$
N = 2 - 1 = 1, \qquad q = x
$$

**2. Velocidad**

$$
\dot{y} = 8x\dot{x}
$$

**3. T, V, P**

$$
v^2 = \dot{x}^2 + \dot{y}^2 = \dot{x}^2\left(1 + 64x^2\right)
$$

$$
T = \frac{m}{2}\dot{x}^2\left(1 + 64x^2\right), \qquad V = mgy = 4mgx^2
$$

$$
P_{n=1} = \frac{c\,v^{2}}{2} = \frac{c}{2}\dot{x}^2\left(1 + 64x^2\right)
$$

**4. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} = -\frac{\partial V}{\partial x} - \frac{\partial P}{\partial \dot{x}}
$$

Derivadas:

$$
\frac{\partial T}{\partial \dot{x}} = m\dot{x}\left(1 + 64x^2\right) \;\Rightarrow\; \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) = m\left[\ddot{x}\left(1 + 64x^2\right) + 128x\dot{x}^2\right]
$$

$$
\frac{\partial T}{\partial x} = 64mx\dot{x}^2, \qquad \frac{\partial V}{\partial x} = 8mgx, \qquad \frac{\partial P}{\partial \dot{x}} = c\dot{x}\left(1 + 64x^2\right)
$$

Sustituyendo:

$$
m\ddot{x}\left(1 + 64x^2\right) + 64mx\dot{x}^2 = -8mgx - c\dot{x}\left(1 + 64x^2\right)
$$

**5. Verificación**

Con $c = 0$ se obtiene el alambre parabólico sin fricción. Chequeo de energía: $\dfrac{d(T+V)}{dt} = -2P$.

---

### Resultado final

$$
\boxed{\;m\left(1 + 64x^2\right)\ddot{x} + 64mx\dot{x}^2 + c\left(1 + 64x^2\right)\dot{x} + 8mgx = 0\;}
$$
