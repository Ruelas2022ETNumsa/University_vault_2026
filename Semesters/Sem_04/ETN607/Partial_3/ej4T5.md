## Enunciado 4 (ej4T5) — Poleas, resorte y cables (a: coordenada relativa)

Entre el techo y el piso hay una distancia H. Del techo cuelga un **resorte** (constante k, longitud natural l₀) que sostiene la **polea 1**. Se miden hacia abajo desde el techo las posiciones y₁ (polea 1), y₂ (polea 2) e y₃ (masa 3).

- Un **cable 1** (longitud l₁) parte de un punto fijo del piso, sube, rodea la polea 1 (radio R₁, media vuelta) y baja hasta sostener el centro de la **polea 2**.
- Un **cable 2** (longitud l₂) parte de otro punto fijo del piso, sube, rodea la polea 2 (radio R₂, media vuelta) y baja una distancia a hasta sostener la **masa 3**, de modo que a = y₃ − y₂.

Las masas de la polea 1, la polea 2 y el bloque 3 son m₁, m₂ y m₃. Las poleas tienen momento de inercia nulo (I₁ = I₂ = 0). Los cables son inextensibles y sin masa. Cada masa sufre fricción viscosa lineal (n = 1) con coeficientes c₁, c₂ y c₃ respectivamente.

**Se pide:**
1. N = (cantidad de masas) − (cantidad de cables); elegir la coordenada generalizada (se sugiere a).
2. Las ecuaciones de restricción de cada cable.
3. y₁, y₂, y₃ y sus velocidades en función de a y ȧ.
4. T, V y P.
5. La EDO de movimiento en a mediante Lagrange.

---

### Solución

**1. N y coordenada**

$$
N = 3 - 2 = 1, \qquad q = a = y_3 - y_2
$$

**2. Restricciones (cables)**

$$
\text{Cable 1: } (H - y_1) + \pi R_1 + (y_2 - y_1) = l_1
$$

$$
\text{Cable 2: } (H - y_2) + \pi R_2 + a = l_2
$$

**3. Posiciones y velocidades en función de $a$**

$$
y_2 = H + \pi R_2 + a - l_2 \;\Rightarrow\; \dot{y}_2 = \dot{a}
$$

$$
y_3 = y_2 + a = H + \pi R_2 + 2a - l_2 \;\Rightarrow\; \dot{y}_3 = 2\dot{a}
$$

$$
y_1 = \tfrac{1}{2}\left(2H + \pi R_1 + \pi R_2 + a - l_1 - l_2\right) \;\Rightarrow\; \dot{y}_1 = \frac{\dot{a}}{2}
$$

**4. T, V, P**

$$
T = \frac{m_1}{2}\left(\frac{\dot{a}}{2}\right)^2 + \frac{m_2}{2}\dot{a}^2 + \frac{m_3}{2}(2\dot{a})^2 = \frac{1}{2}\left(\frac{m_1}{4} + m_2 + 4m_3\right)\dot{a}^2
$$

$$
V = \frac{k}{2}(y_1 - l_0)^2 - m_1 g y_1 - m_2 g y_2 - m_3 g y_3
$$

$$
P_{n=1} = \frac{1}{2}\left(\frac{c_1}{4} + c_2 + 4c_3\right)\dot{a}^2
$$

**5. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{a}}\right) - \frac{\partial T}{\partial a} = -\frac{\partial V}{\partial a} - \frac{\partial P}{\partial \dot{a}}
$$

Con $\partial T/\partial a = 0$ y, usando $dy_1/da = 1/2$, $dy_2/da = 1$, $dy_3/da = 2$:

$$
\frac{\partial V}{\partial a} = \frac{k}{2}(y_1 - l_0) - \left(\frac{m_1}{2} + m_2 + 2m_3\right)g, \qquad y_1 - l_0 = \frac{a}{2} + C_1 - l_0
$$

con $C_1 = H + \dfrac{\pi R_1 + \pi R_2 - l_1 - l_2}{2}$ (constante).

**6. Verificación**

Equilibrio estático ($\ddot a = \dot a = 0$): $k(y_1 - l_0) = (m_1 + 2m_2 + 4m_3)g$. Con $c_i = 0$ queda un oscilador armónico de 1 GDL con fuerza constante.

---

### Resultado final

$$
\boxed{\;\left(\frac{m_1}{4} + m_2 + 4m_3\right)\ddot{a} + \left(\frac{c_1}{4} + c_2 + 4c_3\right)\dot{a} + \frac{k}{4}a + \frac{k}{2}\left(C_1 - l_0\right) - \left(\frac{m_1}{2} + m_2 + 2m_3\right)g = 0\;}
$$
