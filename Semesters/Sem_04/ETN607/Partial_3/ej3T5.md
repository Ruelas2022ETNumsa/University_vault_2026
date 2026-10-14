## Enunciado 3 (ej3T5) — Péndulo simple con fricción viscosa

Una masa puntual m cuelga de una varilla rígida sin masa de longitud l, articulada en un punto fijo. El péndulo oscila en un plano vertical, con ángulo θ medido desde la vertical (y positiva hacia abajo). Hay fricción viscosa lineal, f = c·v (n = 1), sobre la masa.

**Se pide:**
1. N y coordenada generalizada (en polares, r = l y ṙ = 0).
2. T, V y P.
3. La EDO de movimiento (no lineal) mediante Lagrange.
4. Linealizar para ángulos pequeños.
5. Pasar a espacio de estados con u₁ = θ y u₂ = θ̇, y escribir la forma matricial u̇ = A·u + F.
6. Verificación dimensional del coeficiente de fricción en la ecuación final.

---

### Solución

**1. N y coordenada**

Polares $(r, \theta)$ con restricción $r = l$, $\dot{r} = 0$.

$$
N = 2 - 1 = 1, \qquad q = \theta
$$

**2. T, V, P**

$$
v^2 = \dot{r}^2 + r^2\dot{\theta}^2 = l^2\dot{\theta}^2
$$

$$
T = \frac{m}{2}l^2\dot{\theta}^2, \qquad V = -mgy = -mgl\cos\theta
$$

$$
P_{n=1} = \frac{c\,v^{2}}{2} = \frac{c}{2}l^2\dot{\theta}^2
$$

**3. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = -\frac{\partial V}{\partial \theta} - \frac{\partial P}{\partial \dot{\theta}}
$$

Con $\partial T/\partial\theta = 0$, $\partial V/\partial\theta = mgl\sin\theta$, $\partial P/\partial\dot\theta = cl^2\dot\theta$:

$$
ml^2\ddot{\theta} = -mgl\sin\theta - cl^2\dot{\theta}
\;\;\Rightarrow\;\;
\ddot{\theta} = -\frac{g}{l}\sin\theta - \frac{c}{m}\dot{\theta}
\quad\text{(no lineal, 2.º orden)}
$$

**4. Linealización** ($\sin\theta \approx \theta$)

$$
\ddot{\theta} + \frac{c}{m}\dot{\theta} + \frac{g}{l}\theta = 0
$$

**5. Espacio de estados** ($u_1 = \theta$, $u_2 = \dot\theta$)

$$
\dot{u}_1 = u_2, \qquad \dot{u}_2 = -\frac{g}{l}u_1 - \frac{c}{m}u_2
$$

$$
\begin{bmatrix}\dot{u}_1\\ \dot{u}_2\end{bmatrix}
=
\begin{bmatrix}0 & 1\\ -\dfrac{g}{l} & -\dfrac{c}{m}\end{bmatrix}
\begin{bmatrix}u_1\\ u_2\end{bmatrix}
+
\begin{bmatrix}F_1\\ F_2\end{bmatrix},
\qquad F_1 = F_2 = 0
$$

**6. Verificación dimensional**

$[c] = \text{N}/(\text{m/s}) = \text{kg/s}$, entonces $[c/m] = \text{s}^{-1}$ y $\left[\dfrac{c}{m}\dot\theta\right] = \text{rad/s}^2$, igual que $\ddot\theta$ y $\dfrac{g}{l}\theta$. Con $c = 0$ se recupera el péndulo simple $\ddot\theta + \dfrac{g}{l}\sin\theta = 0$.

---

### Resultado final

$$
\boxed{\;\ddot{\theta} = -\frac{g}{l}\sin\theta - \frac{c}{m}\dot{\theta}\;}
\qquad
\boxed{\;\dot{\mathbf{u}} = \begin{bmatrix}0 & 1\\ -\dfrac{g}{l} & -\dfrac{c}{m}\end{bmatrix}\mathbf{u}\;}
$$
