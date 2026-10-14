## Enunciado 6 (ej6T5) — Tres masas con resortes y amortiguadores (forma matricial)

Tres bloques se mueven en línea recta, con coordenadas x₁, x₂ y x₃ medidas desde sus posiciones de referencia. Las masas son m₁ = 2, m₂ = 3 y m₃ = 2. Las conexiones son:

- Pared – bloque 1: un resorte de constante 2 y un amortiguador de coeficiente 3.
- Bloque 1 – bloque 2: un resorte de constante 3 y un amortiguador de coeficiente 4.
- Bloque 1 – bloque 3: dos resortes en serie, de constantes 2 y 3.
- Bloque 2 – bloque 3: dos amortiguadores en serie, de coeficientes 2 y 2.
- Pared – bloque 2: dos resortes en paralelo, de constantes 1 y 2.

Sobre el bloque 2 actúa una fuerza externa F.

**Se pide:**
1. Resortes y amortiguadores equivalentes (serie y paralelo).
2. Las matrices M, C y K, y el sistema M·ẍ + C·ẋ + K·x = F.
3. Explicar el tratamiento del término constante k·l₀ en F_R = k(x − l₀) y por qué no aparece en las matrices.

---

### Solución

**1. Equivalentes**

$$
k_{13} = \left(\frac{1}{2} + \frac{1}{3}\right)^{-1} = \frac{6}{5}, \qquad c_{23} = \left(\frac{1}{2} + \frac{1}{2}\right)^{-1} = 1, \qquad k_{20} = 1 + 2 = 3
$$

**2. N y coordenadas**

$$
N = 3 - 0 = 3, \qquad q = (x_1,\, x_2,\, x_3)
$$

**3. T, V, P**

$$
T = \frac{1}{2}\left(2\dot{x}_1^2 + 3\dot{x}_2^2 + 2\dot{x}_3^2\right)
$$

$$
V = \frac{1}{2}\left[2x_1^2 + 3x_2^2 + 3(x_2 - x_1)^2 + \frac{6}{5}(x_3 - x_1)^2\right]
$$

$$
P = \frac{1}{2}\left[3\dot{x}_1^2 + 4(\dot{x}_2 - \dot{x}_1)^2 + 1\,(\dot{x}_3 - \dot{x}_2)^2\right]
$$

**4. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_i}\right) + \frac{\partial V}{\partial x_i} + \frac{\partial P}{\partial \dot{x}_i} = Q_i, \qquad Q = (0,\, F,\, 0)
$$

$$
\begin{aligned}
x_1:&\quad 2\ddot{x}_1 + (7\dot{x}_1 - 4\dot{x}_2) + \left(\tfrac{31}{5}x_1 - 3x_2 - \tfrac{6}{5}x_3\right) = 0 \\
x_2:&\quad 3\ddot{x}_2 + (-4\dot{x}_1 + 5\dot{x}_2 - \dot{x}_3) + \left(-3x_1 + 6x_2\right) = F \\
x_3:&\quad 2\ddot{x}_3 + (-\dot{x}_2 + \dot{x}_3) + \left(-\tfrac{6}{5}x_1 + \tfrac{6}{5}x_3\right) = 0
\end{aligned}
$$

**5. Término $k\cdot l_0$**

En $F_R = k(x - l_0) = kx - k l_0$, el término $k l_0$ es una fuerza constante. Se equilibra con las reacciones estáticas, así que solo cambia la posición de equilibrio y no la dinámica. Al medir $x_i$ desde el equilibrio, solo queda $kx$, por eso $k l_0$ no aparece en M, C ni K.

**6. Verificación**

Las matrices son simétricas y definidas positivas ($\det M = 12$, $\det C = 12$, $\det K = 25.2$). Unidades: $[M\ddot x] = [C\dot x] = [Kx] = \text{N}$.

---

### Resultado final

$$
\boxed{\;
\begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}\ddot{\mathbf{x}}
+
\begin{bmatrix} 7 & -4 & 0 \\ -4 & 5 & -1 \\ 0 & -1 & 1 \end{bmatrix}\dot{\mathbf{x}}
+
\begin{bmatrix} \frac{31}{5} & -3 & -\frac{6}{5} \\ -3 & 6 & 0 \\ -\frac{6}{5} & 0 & \frac{6}{5} \end{bmatrix}\mathbf{x}
=
\begin{bmatrix} 0 \\ F \\ 0 \end{bmatrix}
\;}
$$
