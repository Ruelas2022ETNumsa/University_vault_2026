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

---

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

---

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


---

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

---

## Enunciado 5 (ej5T5) — Cuña y bloque con tres fricciones

Dentro de un recinto de ancho d hay dos cuerpos:

- El **cuerpo 1** (masa m₁) se mueve **solo en vertical**, guiado por la pared izquierda. Su punta toca la cuña a una distancia horizontal fija B de la pared izquierda, y su altura sobre el piso es y₁ (positiva hacia arriba).
- El **cuerpo 2** (masa m₂) es una cuña de ángulo α y base horizontal b que se mueve **solo en horizontal** sobre el piso. Su esquina inferior izquierda está a la distancia x₂ del origen (esquina inferior izquierda del recinto). La cuña está unida a la pared derecha por un resorte de constante k, con longitud d − x₂ − b y longitud natural nula.

El cuerpo 1 apoya sobre la cara inclinada de la cuña. Hay tres fricciones viscosas lineales (n = 1):
- c₁: entre el cuerpo 1 y la pared izquierda.
- c₂: entre la cuña y el piso.
- c₃: entre el cuerpo 1 y la cuña, en la cara inclinada.

**Se pide:**
1. N y coordenada generalizada (se sugiere y₁).
2. La ecuación de restricción que relaciona x₂ con y₁.
3. T, V y P en función de y₁ y ẏ₁. Justificar qué velocidad relativa interviene en la fricción c₃.
4. La EDO de movimiento mediante Lagrange.

---

### Solución

**1. N y coordenada**

Coordenadas $(y_1, x_2)$ con 1 restricción de contacto.

$$
N = 2 - 1 = 1, \qquad q = y_1
$$

**2. Restricción**

$$
\tan\alpha = \frac{y_1}{B - x_2} \;\Rightarrow\; x_2 = B - \frac{y_1}{\tan\alpha} = B - y_1\cot\alpha, \qquad \dot{x}_2 = -\dot{y}_1\cot\alpha
$$

**3. T, V, P**

$$
T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{x}_2^2 = \frac{1}{2}\left(m_1 + m_2\cot^2\alpha\right)\dot{y}_1^2
$$

$$
V = m_1 g y_1 + \frac{k}{2}(d - x_2 - b)^2 = m_1 g y_1 + \frac{k}{2}\left[(d - B - b) + y_1\cot\alpha\right]^2
$$

La fricción $c_3$ depende de la velocidad **relativa** entre los cuerpos en la cara inclinada (su módulo, no la suma de componentes):

$$
\vec{v}_{rel} = \vec{v}_1 - \vec{v}_2 = (\dot{y}_1\cot\alpha,\; \dot{y}_1) \;\Rightarrow\; v_{rel}^2 = \dot{y}_1^2\left(1 + \cot^2\alpha\right) = \frac{\dot{y}_1^2}{\sin^2\alpha}
$$

$$
P_{n=1} = \frac{c_1}{2}\dot{y}_1^2 + \frac{c_2}{2}\dot{x}_2^2 + \frac{c_3}{2}v_{rel}^2 = \frac{1}{2}\left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1^2
$$

**4. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) - \frac{\partial T}{\partial y_1} = -\frac{\partial V}{\partial y_1} - \frac{\partial P}{\partial \dot{y}_1}
$$

$$
\frac{\partial T}{\partial y_1} = 0, \qquad \frac{\partial V}{\partial y_1} = m_1 g + k\cot\alpha\left[(d - B - b) + y_1\cot\alpha\right]
$$

$$
\frac{\partial P}{\partial \dot{y}_1} = \left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1
$$

**5. Verificación**

Con $c_i = 0$ queda un oscilador conservativo de 1 GDL. Válido solo con contacto: $0 \le y_1 \le b\tan\alpha$.

---

### Resultado final

$$
\boxed{\;\left(m_1 + m_2\cot^2\alpha\right)\ddot{y}_1 + \left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1 + k\cot^2\alpha\; y_1 + m_1 g + k(d - B - b)\cot\alpha = 0\;}
$$

---

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

---

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

---

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
