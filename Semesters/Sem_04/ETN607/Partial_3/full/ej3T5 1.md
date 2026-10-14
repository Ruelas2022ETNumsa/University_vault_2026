## Enunciado 3 (ej3T5) — Péndulo simple con fricción viscosa

Una masa puntual m cuelga de una varilla rígida sin masa de longitud l, articulada en un punto fijo. El péndulo oscila en un plano vertical, con ángulo θ medido desde la vertical (y positiva hacia abajo). Hay fricción viscosa lineal, f = c·v $n = 1$, sobre la masa.

**Se pide:**
1. N y coordenada generalizada (en polares, r = l y ṙ = 0).
2. T, V y P.
3. La EDO de movimiento (no lineal) mediante Lagrange.
4. Linealizar para ángulos pequeños.
5. Pasar a espacio de estados con u₁ = θ y u₂ = θ̇, y escribir la forma matricial u̇ = A·u + F.
6. Verificación dimensional del coeficiente de fricción en la ecuación final.

### 1. Datos y esquema
- **Masa de la partícula:** $m$
- **Longitud de la varilla rígida sin masa:** $l$
- **Sistema de coordenadas:** Polares planas $(r, \theta)$ con origen en el pivote fijo.
- **Orientación de ejes:** $y$ positiva hacia abajo, $x$ horizontal hacia la derecha.
- **Ángulo de oscilación:** $\theta$ medido desde la vertical descendente.
- **Fuerza de fricción viscosa lineal ($n=1$):**
  
$$
\vec{f} = -c \vec{v} = -c l \dot{\theta} \hat{e}_\theta
$$

  con magnitud $f = c v$, opuesta a la velocidad instantánea [Taylor, Cap. 2; Goldstein, Cap. 1].

---

### 2. Grados de libertad $N$ y coordenadas generalizadas
- **Número de coordenadas cartesianas/polares:** 2 ($r, \theta$).
- **Restricción holónoma ($k = 1$):** Varilla inextensible de longitud constante $l$:
  
$$
r - l = 0 \implies r = l, \quad \dot{r} = 0
$$

- **Grados de libertad ($N$):**
  
$$
N = 2 - 1 = 1
$$

- **Coordenada generalizada:** $q = \theta$ [Wells, Cap. 2; Taylor, Cap. 7].

---

### 3. Restricciones y posición/velocidad
- **Vector de posición en cartesianas:**
  
$$
\vec{r} = (l \sin\theta)\hat{i} + (l \cos\theta)\hat{j}
$$

- **Vector de velocidad:**
  
$$
\vec{v} = \dot{\vec{r}} = (l \cos\theta \, \dot{\theta})\hat{i} - (l \sin\theta \, \dot{\theta})\hat{j} = l \dot{\theta} \hat{e}_\theta
$$

- **Módulo al cuadrado de la velocidad:**
  
$$
v^2 = |\vec{v}|^2 = l^2 \dot{\theta}^2
$$


---

### 4. $T$, $V$ y $P$ por separado
- **Energía cinética ($T$):** [Taylor, Cap. 7; Wells, Cap. 3]
  
$$
T = \frac{1}{2} m v^2 = \frac{1}{2} m l^2 \dot{\theta}^2
$$


- **Energía potencial ($V$):** [Goldstein, Cap. 1; Taylor, Cap. 7]
  Tomando el nivel de referencia $V = 0$ en el punto de articulación ($y = 0$):
  
$$
V = -m g y = -m g l \cos\theta
$$


- **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1, Ec. 1.67; Wells, Cap. 6, Ec. 6.16]
  Para fricción viscosa lineal ($n = 1$), $P = \frac{1}{2} c v^2$:
  
$$
P = \frac{1}{2} c \left(l^2 \dot{\theta}^2\right) = \frac{1}{2} c l^2 \dot{\theta}^2
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida para sistemas disipativos [Goldstein, Cap. 1, Ec. 1.70]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} + \frac{\partial V}{\partial \theta} + \frac{\partial P}{\partial \dot{\theta}} = 0
$$


Calculando término a término:
1. **Derivada parcial de $T$ respecto a $\dot{\theta}$ y su derivada temporal:**
   
$$
\frac{\partial T}{\partial \dot{\theta}} = m l^2 \dot{\theta} \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m l^2 \ddot{\theta}
$$


2. **Derivada parcial de $T$ respecto a $\theta$:**
   
$$
\frac{\partial T}{\partial \theta} = 0
$$


3. **Derivada parcial de $V$ respecto a $\theta$:**
   
$$
\frac{\partial V}{\partial \theta} = \frac{\partial}{\partial \theta}\left(-m g l \cos\theta\right) = m g l \sin\theta
$$


4. **Derivada parcial de $P$ respecto a $\dot{\theta}$:**
   
$$
\frac{\partial P}{\partial \dot{\theta}} = \frac{\partial}{\partial \dot{\theta}}\left(\frac{1}{2} c l^2 \dot{\theta}^2\right) = c l^2 \dot{\theta}
$$


---

### 6. EDO final (modelo matemático no lineal)
Sustituyendo los términos calculados en la ecuación de Lagrange:

$$
m l^2 \ddot{\theta} + c l^2 \dot{\theta} + m g l \sin\theta = 0
$$


Dividiendo entre la inercia rotacional $m l^2$ y despejando la aceleración generalizada $\ddot{\theta}$:

$$
\ddot{\theta} = -\frac{c}{m} \dot{\theta} - \frac{g}{l} \sin\theta
$$


---

### 7. Linealización y Espacio de Estados

#### **Linealización para ángulos pequeños ($\theta \ll 1$ rad):**
Usando la aproximación de Taylor $\sin\theta \approx \theta$:

$$
\ddot{\theta} + \frac{c}{m} \dot{\theta} + \frac{g}{l} \theta = 0
$$


#### **Formulación en Espacio de Estados:**
Definiendo las variables de estado $u_1 = \theta$ y $u_2 = \dot{\theta}$:

$$
\dot{u}_1 = \dot{\theta} = u_2
$$


$$
\dot{u}_2 = \ddot{\theta} = -\frac{g}{l} u_1 - \frac{c}{m} u_2
$$


En la forma matricial $\dot{\mathbf{u}} = \mathbf{A}\mathbf{u} + \mathbf{F}$:

$$
\begin{bmatrix} \dot{u}_1 \\ \dot{u}_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -\dfrac{g}{l} & -\dfrac{c}{m} \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$


donde las matrices del modelo dinámico son:

$$
\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\dfrac{g}{l} & -\dfrac{c}{m} \end{bmatrix}, \qquad \mathbf{F} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$


---

### 8. Verificación

#### **Análisis dimensional del coeficiente de fricción y términos:**
- Fuerza de fricción $f = c v \implies [c] = \frac{[f]}{[v]} = \frac{\text{N}}{\text{m/s}} = \frac{\text{kg}\cdot\text{m/s}^2}{\text{m/s}} = \text{kg/s}$.
- Término amortiguador $\frac{c}{m} \dot{\theta}$:
  
$$
\left[\frac{c}{m} \dot{\theta}\right] = \frac{\text{kg/s}}{\text{kg}} \cdot \frac{\text{rad}}{\text{s}} = \frac{\text{rad}}{\text{s}^2} = \text{s}^{-2}
$$

- Término restitutivo $\frac{g}{l} \theta$:
  
$$
\left[\frac{g}{l} \theta\right] = \frac{\text{m/s}^2}{\text{m}} \cdot \text{rad} = \frac{\text{rad}}{\text{s}^2} = \text{s}^{-2}
$$

- Todos los términos de la EDO linealizada poseen dimensión de **aceleración angular** $[\text{rad/s}^2]$, lo que confirma la homogeneidad dimensional del modelo.

#### **Caso límite $c = 0$ (sistema conservativo sin fricción):**
Haciendo $c = 0$, la ecuación diferencial no lineal se reduce a:

$$
\ddot{\theta} + \frac{g}{l} \sin\theta = 0
$$

que corresponde exactamente a la EDO clásica del péndulo simple ideal no lineal [Taylor, Cap. 7, Ec. 7.33].

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 1 \quad \text{con coordenada generalizada } q = \theta \\
2.\quad T &= \frac{1}{2} m l^2 \dot{\theta}^2 \\
V &= -m g l \cos\theta \\
P &= \frac{1}{2} c l^2 \dot{\theta}^2 \\
3.\quad \ddot{\theta} &= -\frac{c}{m} \dot{\theta} - \frac{g}{l} \sin\theta \quad \text{(EDO no lineal)} \\
4.\quad \ddot{\theta} &+ \frac{c}{m} \dot{\theta} + \frac{g}{l} \theta = 0 \quad \text{(EDO linealizada)} \\
5.\quad \begin{bmatrix} \dot{u}_1 \\ \dot{u}_2 \end{bmatrix} &= \begin{bmatrix} 0 & 1 \\ -\frac{g}{l} & -\frac{c}{m} \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
6.\quad [c] &= \text{kg/s} \implies \left[\frac{c}{m}\dot{\theta}\right] = \text{rad/s}^2 \quad \text{(homogéneo con }\ddot{\theta}\text{)}.
\end{aligned}
$$


---

**Dudas o supuestos:** Se supone que el movimiento permanece confinado en el plano vertical, la varilla es indeformable y la resistencia del aire opera estrictamente en régimen viscoso lineal ($n=1$).

💡 ¿Te gustaría calcular los autovalores de la matriz $\mathbf{A}$ para clasificar la respuesta en amortiguada, críticamente amortiguada o sobreamortiguada?
