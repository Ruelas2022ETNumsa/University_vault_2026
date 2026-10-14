## Enunciado 7 (ej7T5) — Doble péndulo con fricción

Dos masas puntuales m₁ y m₂ forman un doble péndulo plano. La masa 1 cuelga de un punto fijo mediante una varilla rígida sin masa de longitud l; la masa 2 cuelga de la masa 1 mediante otra varilla de longitud l. Los ángulos θ₁ y θ₂ se miden desde la vertical (y positiva hacia abajo), cada uno respecto de su propia vertical local. Hay fricción en cada masa, proporcional a la velocidad de esa masa, con coeficientes c₁ (masa 1) y c₂ (masa 2).

**Se pide:**
1. N y coordenadas generalizadas.
2. Posición y velocidad de cada masa.
3. T, V y P (n = 1).
4. Las dos EDO acopladas mediante Lagrange.
5. Verificar el caso límite c₁ = c₂ = 0.
6. Opcional: obtener las ecuaciones con MATLAB simbólico (+15 pts).

---

### Solución

**1. N y coordenadas**

Coordenadas $(x_1, y_1, x_2, y_2)$ con 2 restricciones (longitudes de varillas).

$$
N = 4 - 2 = 2, \qquad q = (\theta_1,\, \theta_2)
$$

**2. Posición y velocidad**

$$
x_1 = l\sin\theta_1, \quad y_1 = l\cos\theta_1 \;\Rightarrow\; v_1^2 = l^2\dot{\theta}_1^2
$$

$$
x_2 = l\sin\theta_1 + l\sin\theta_2, \quad y_2 = l\cos\theta_1 + l\cos\theta_2
$$

$$
v_2^2 = l^2\left[\dot{\theta}_1^2 + \dot{\theta}_2^2 + 2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)\right]
$$

**3. T, V, P**

$$
T = \frac{m_1}{2}v_1^2 + \frac{m_2}{2}v_2^2 = \frac{1}{2}(m_1 + m_2)l^2\dot{\theta}_1^2 + \frac{1}{2}m_2 l^2\dot{\theta}_2^2 + m_2 l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)
$$

$$
V = -m_1 g y_1 - m_2 g y_2 = -(m_1 + m_2)gl\cos\theta_1 - m_2 g l\cos\theta_2
$$

$$
P_{n=1} = \frac{c_1}{2}v_1^2 + \frac{c_2}{2}v_2^2 = \frac{1}{2}(c_1 + c_2)l^2\dot{\theta}_1^2 + \frac{1}{2}c_2 l^2\dot{\theta}_2^2 + c_2 l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)
$$

**4. Lagrange** ($\Delta = \theta_1 - \theta_2$)

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}_i}\right) - \frac{\partial T}{\partial \theta_i} = -\frac{\partial V}{\partial \theta_i} - \frac{\partial P}{\partial \dot{\theta}_i}
$$

Para $\theta_1$:

$$
\frac{\partial T}{\partial \dot{\theta}_1} = (m_1 + m_2)l^2\dot{\theta}_1 + m_2 l^2\dot{\theta}_2\cos\Delta, \qquad \frac{\partial T}{\partial \theta_1} = -m_2 l^2\dot{\theta}_1\dot{\theta}_2\sin\Delta
$$

$$
\frac{\partial V}{\partial \theta_1} = (m_1 + m_2)gl\sin\theta_1, \qquad \frac{\partial P}{\partial \dot{\theta}_1} = (c_1 + c_2)l^2\dot{\theta}_1 + c_2 l^2\dot{\theta}_2\cos\Delta
$$

Para $\theta_2$:

$$
\frac{\partial T}{\partial \dot{\theta}_2} = m_2 l^2\dot{\theta}_2 + m_2 l^2\dot{\theta}_1\cos\Delta, \qquad \frac{\partial T}{\partial \theta_2} = m_2 l^2\dot{\theta}_1\dot{\theta}_2\sin\Delta
$$

$$
\frac{\partial V}{\partial \theta_2} = m_2 gl\sin\theta_2, \qquad \frac{\partial P}{\partial \dot{\theta}_2} = c_2 l^2\dot{\theta}_2 + c_2 l^2\dot{\theta}_1\cos\Delta
$$

Al derivar en el tiempo, los términos con $\dot\theta_1\dot\theta_2\sin\Delta$ se cancelan y quedan $+m_2 l^2\dot\theta_2^2\sin\Delta$ en la primera ecuación y $-m_2 l^2\dot\theta_1^2\sin\Delta$ en la segunda.

**5. Verificación**

Con $c_1 = c_2 = 0$ ($P = 0$) quedan las ecuaciones conservativas del doble péndulo plano.

---

### Resultado final

$$
\boxed{\;
\begin{aligned}
&(m_1 + m_2)l^2\ddot{\theta}_1 + m_2 l^2\ddot{\theta}_2\cos\Delta + m_2 l^2\dot{\theta}_2^2\sin\Delta + (m_1 + m_2)gl\sin\theta_1 + (c_1 + c_2)l^2\dot{\theta}_1 + c_2 l^2\dot{\theta}_2\cos\Delta = 0 \\[4pt]
&m_2 l^2\ddot{\theta}_2 + m_2 l^2\ddot{\theta}_1\cos\Delta - m_2 l^2\dot{\theta}_1^2\sin\Delta + m_2 gl\sin\theta_2 + c_2 l^2\dot{\theta}_2 + c_2 l^2\dot{\theta}_1\cos\Delta = 0
\end{aligned}
\;}
$$
