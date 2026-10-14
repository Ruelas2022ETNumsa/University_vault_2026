## Enunciado 1 (ej1T5) — Tiro balístico con fricción cuadrática

Una partícula de masa m se lanza en el plano vertical (x, y) y se mueve bajo la gravedad (y positiva hacia arriba). Sobre ella actúa una fricción del aire cuadrática, f = c·v², con v² = ẋ² + ẏ², siempre opuesta a la velocidad (n = 2).

**Se pide:**
1. Grados de libertad N y coordenadas generalizadas.
2. T, V y P.
3. Las ecuaciones de movimiento de x(t) e y(t) mediante Lagrange.
4. Verificar que con c = 0 se recupera el tiro parabólico sin fricción.

---

### Solución

**1. N y coordenadas**

$$
N = 2 - 0 = 2, \qquad q = (x,\, y)
$$

**2. T, V, P** ($v^2 = \dot{x}^2 + \dot{y}^2$)

$$
T = \frac{m}{2}\left(\dot{x}^2 + \dot{y}^2\right), \qquad V = m g y
$$

$$
P_{n=2} = \frac{c\,v^{n+1}}{n+1} = \frac{c}{3}\left(\dot{x}^2 + \dot{y}^2\right)^{3/2}
$$

**3. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}}\right) - \frac{\partial T}{\partial q} = -\frac{\partial V}{\partial q} - \frac{\partial P}{\partial \dot{q}}
$$

Derivadas:

$$
\frac{\partial P}{\partial \dot{x}} = \frac{c}{3}\cdot\frac{3}{2}\left(\dot{x}^2 + \dot{y}^2\right)^{1/2} 2\dot{x} = c\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{x}, \qquad \frac{\partial P}{\partial \dot{y}} = c\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{y}
$$

Para $x$ ($\partial T/\partial x = 0,\ \partial V/\partial x = 0$):

$$
m\ddot{x} = -c\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{x}
$$

Para $y$ ($\partial T/\partial y = 0,\ \partial V/\partial y = mg$):

$$
m\ddot{y} = -mg - c\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{y}
$$

**4. Verificación**

Con $c = 0$: $\ddot{x} = 0$, $\ddot{y} = -g$ (tiro parabólico). Dimensional: $[c] = \text{N}/(\text{m/s})^2 = \text{kg/m}$.

---

### Resultado final

$$
\boxed{\;\ddot{x} = -\frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{x}, \qquad \ddot{y} = -g - \frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\;\dot{y}\;}
$$
