## Enunciado 8 (ej8T5) — Péndulo que se desenrolla de un cilindro fijo

Un cilindro fijo de radio R tiene un hilo inextensible y sin masa enrollado en su superficie. Del extremo libre del hilo cuelga una masa m. El origen está en el centro del cilindro, con x horizontal y y vertical hacia abajo. En θ = 0 el hilo sale tangente al cilindro en el punto $(R, 0)$ y cuelga vertical con una longitud libre l. Al girar un ángulo θ, la parte libre del hilo (tangente al cilindro) mide d = l + R·θ. Hay fricción en la masa, f = c·vⁿ.

**Se pide:**
1. N y coordenada generalizada.
2. Posición $x, y$ y velocidad de la masa en función de θ y θ̇.
3. T y V.
4. P para n = 1 y para n = 2.
5. La EDO de movimiento para n = 2 mediante Lagrange; indicar cómo cambia para n = 1.

---

### 1. Datos y esquema
- **Cilindro fijo:** Radio $R$, centrado en el origen $(0,0)$.
- **Ejes cartesianos:** $x$ horizontal hacia la derecha, $y$ vertical hacia abajo (gravedad $\vec{g} = g \hat{j}$).
- **Condición inicial ($\theta = 0$):** El hilo se desprende tangencialmente del cilindro en el punto $(R, 0)$ y cuelga libremente hacia abajo con longitud $l$ [Wells, Cap. 3].
- **Geometría para $\theta > 0$:** Al desenrollarse un ángulo $\theta$, el punto de tangencia $Q(\theta)$ se desplaza sobre la circunferencia y la longitud del tramo libre recto es $d(\theta) = l + R\theta$.
- **Fuerza de fricción disipativa:** $f = c v^n$, actuando en dirección opuesta al movimiento de la masa $m$ [Goldstein, Cap. 1; Taylor, Cap. 2].

---

### 2. Grados de libertad $N$ y coordenada generalizada
- **Número de coordenadas cartesianas:** 2 ($x, y$).
- **Restricción holónoma ($k = 1$):** El hilo es inextensible y se mantiene tenso, formando la evolvente del cilindro de radio $R$:
  
$$
N = 2 - 1 = 1
$$

- **Coordenada generalizada elegida:** $q = \theta$ (ángulo de desenrollamiento) [Wells, Cap. 2].

---

### 3. Posición $(x, y)$ y velocidad en función de $\theta$ y $\dot{\theta}$

#### **Posición de la masa $m$:**
El punto de tangencia sobre el cilindro al girar un ángulo $\theta$ en sentido antihorario es $Q(\theta) = (R\cos\theta, -R\sin\theta)$. El segmento libre tangente de longitud $d(\theta) = l + R\theta$ sigue la dirección del vector unitario $\hat{u}_t(\theta) = \sin\theta \, \hat{i} + \cos\theta \, \hat{j}$.
Por suma vectorial de posición $\vec{r}(\theta) = \vec{r}_Q(\theta) + d(\theta)\hat{u}_t(\theta)$:

$$
x(\theta) = R \cos\theta + (l + R\theta) \sin\theta
$$


$$
y(\theta) = -R \sin\theta + (l + R\theta) \cos\theta
$$


#### **Componentes de la velocidad:**
Derivando las expresiones de posición respecto al tiempo $t$ mediante la regla de la cadena:

$$
\dot{x} = \frac{dx}{dt} = -R \sin\theta \, \dot{\theta} + R \dot{\theta} \sin\theta + (l + R\theta) \cos\theta \, \dot{\theta} = (l + R\theta) \cos\theta \, \dot{\theta}
$$


$$
\dot{y} = \frac{dy}{dt} = -R \cos\theta \, \dot{\theta} + R \dot{\theta} \cos\theta - (l + R\theta) \sin\theta \, \dot{\theta} = -(l + R\theta) \sin\theta \, \dot{\theta}
$$


#### **Módulo de la velocidad:**

$$
v^2 = \dot{x}^2 + \dot{y}^2 = (l + R\theta)^2 \cos^2\theta \, \dot{\theta}^2 + (l + R\theta)^2 \sin^2\theta \, \dot{\theta}^2 = (l + R\theta)^2 \dot{\theta}^2
$$


$$
v = (l + R\theta)|\dot{\theta}|
$$


---

### 4. $T$, $V$ y $P$ por separado

- **Energía cinética ($T$):** [Taylor, Cap. 7; Wells, Cap. 3]
  
$$
T = \frac{1}{2} m v^2 = \frac{1}{2} m (l + R\theta)^2 \dot{\theta}^2
$$


- **Energía potencial ($V$):** [Wells, Cap. 5; Goldstein, Cap. 1]
  Tomando el nivel de referencia gravitatorio $V = 0$ en el centro del cilindro ($y = 0$, $y$ positiva hacia abajo):
  
$$
V = -m g y(\theta) = m g R \sin\theta - m g (l + R\theta) \cos\theta
$$


- **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1, Ec. 1.67; Wells, Cap. 6, Ec. 6.17]
  Para una fuerza $f = c v^n$, la función disipativa es $P = \frac{c}{n+1} v^{n+1}$:
  - **Para $n = 1$ (fricción viscosa lineal, $f = c v$):**
    
$$
P_{n=1} = \frac{1}{2} c v^2 = \frac{1}{2} c (l + R\theta)^2 \dot{\theta}^2
$$

  - **Para $n = 2$ (fricción cuadrática, $f = c v^2$):**
    
$$
P_{n=2} = \frac{1}{3} c v^3 = \frac{1}{3} c (l + R\theta)^3 |\dot{\theta}|^3
$$


---

### 5. Derivadas de Lagrange y EDO de movimiento

Se aplica la ecuación de Lagrange extendida para sistemas disipativos [Goldstein, Cap. 1, Ec. 1.70]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} + \frac{\partial V}{\partial \theta} + \frac{\partial P}{\partial \dot{\theta}} = 0
$$


Calculando los términos de la ecuación:
1. **Derivada respecto a $\dot{\theta}$ y su derivada temporal:**
   
$$
\frac{\partial T}{\partial \dot{\theta}} = m (l + R\theta)^2 \dot{\theta}
$$

   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) = m (l + R\theta)^2 \ddot{\theta} + 2 m R (l + R\theta) \dot{\theta}^2
$$

2. **Derivada cinemática respecto a $\theta$:**
   
$$
\frac{\partial T}{\partial \theta} = m R (l + R\theta) \dot{\theta}^2
$$

3. **Término inercial neto:**
   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta} = m (l + R\theta)^2 \ddot{\theta} + m R (l + R\theta) \dot{\theta}^2
$$

4. **Derivada del potencial gravitatorio:**
   
$$
\frac{\partial V}{\partial \theta} = \frac{\partial}{\partial \theta} \left[ m g R \sin\theta - m g (l + R\theta) \cos\theta \right] = m g R \cos\theta - \left[ m g R \cos\theta - m g (l + R\theta) \sin\theta \right] = m g (l + R\theta) \sin\theta
$$

5. **Derivada de la función de disipación:**
   - **Para $n = 2$:**
     
$$
\frac{\partial P_{n=2}}{\partial \dot{\theta}} = c (l + R\theta)^3 \dot{\theta} |\dot{\theta}|
$$

   - **Para $n = 1$:**
     
$$
\frac{\partial P_{n=1}}{\partial \dot{\theta}} = c (l + R\theta)^2 \dot{\theta}
$$


---

### 6. EDO final (modelo matemático)

#### **Caso $n = 2$ (fricción cuadrática):**
Sustituyendo los términos en la ecuación de Lagrange:

$$
m (l + R\theta)^2 \ddot{\theta} + m R (l + R\theta) \dot{\theta}^2 + m g (l + R\theta) \sin\theta + c (l + R\theta)^3 \dot{\theta} |\dot{\theta}| = 0
$$


Dividiendo toda la ecuación entre el factor inercial $m (l + R\theta)^2$ y despejando la aceleración generalizada $\ddot{\theta}$:

$$
\ddot{\theta} = -\frac{R}{l + R\theta} \dot{\theta}^2 - \frac{g}{l + R\theta} \sin\theta - \frac{c}{m} (l + R\theta) \dot{\theta} |\dot{\theta}|
$$


#### **Cómo cambia para $n = 1$ (fricción viscosa lineal):**
El término disipativo cambia de $\frac{c}{m}(l + R\theta)\dot{\theta}|\dot{\theta}|$ a $\frac{c}{m}\dot{\theta}$. La EDO resultante es:

$$
\ddot{\theta} = -\frac{R}{l + R\theta} \dot{\theta}^2 - \frac{g}{l + R\theta} \sin\theta - \frac{c}{m} \dot{\theta}
$$


---

### 7. Verificación

#### **Análisis dimensional ($n = 2$):**
- Coeficiente de fricción cuadrática: $[c] = \frac{\text{N}}{(\text{m/s})^2} = \text{kg/m}$.
- Término acoplado de velocidad $\frac{R}{l + R\theta} \dot{\theta}^2$: $\frac{\text{m}}{\text{m}} \cdot \frac{\text{rad}^2}{\text{s}^2} = \text{rad/s}^2$.
- Término gravitatorio $\frac{g}{l + R\theta} \sin\theta$: $\frac{\text{m/s}^2}{\text{m}} = \text{rad/s}^2$.
- Término de arrastre $\frac{c}{m} (l + R\theta) \dot{\theta}^2$: $\frac{\text{kg/m}}{\text{kg}} \cdot \text{m} \cdot \frac{\text{rad}^2}{\text{s}^2} = \text{rad/s}^2$.
Todos los términos poseen dimensión de **aceleración angular** $[\text{rad/s}^2]$.

#### **Caso límite $c = 0$ (sistema conservativo):**
Haciendo $c = 0$, el modelo se reduce a:

$$
\ddot{\theta} + \frac{R}{l + R\theta} \dot{\theta}^2 + \frac{g}{l + R\theta} \sin\theta = 0
$$

Coincide exactamente con la EDO conservativa clásica del péndulo de evolvente sobre un cilindro circular fijo [Taylor, Cap. 7; Wells, Cap. 3].

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 1 \quad \text{con coordenada generalizada } q = \theta \\
2.\quad x(\theta) &= R \cos\theta + (l + R\theta) \sin\theta, \qquad \dot{x} = (l + R\theta)\cos\theta\,\dot{\theta} \\
y(\theta) &= -R \sin\theta + (l + R\theta) \cos\theta, \qquad \dot{y} = -(l + R\theta)\sin\theta\,\dot{\theta} \\
v &= (l + R\theta)|\dot{\theta}| \\
3.\quad T &= \frac{1}{2} m (l + R\theta)^2 \dot{\theta}^2 \\
V &= m g R \sin\theta - m g (l + R\theta) \cos\theta \\
4.\quad P_{n=1} &= \frac{1}{2} c (l + R\theta)^2 \dot{\theta}^2, \qquad P_{n=2} = \frac{1}{3} c (l + R\theta)^3 |\dot{\theta}|^3 \\
5.\quad \text{Para } n = 2: \quad \ddot{\theta} &= -\frac{R}{l + R\theta} \dot{\theta}^2 - \frac{g}{l + R\theta} \sin\theta - \frac{c}{m} (l + R\theta) \dot{\theta} |\dot{\theta}| \\
\text{Para } n = 1: \quad \ddot{\theta} &= -\frac{R}{l + R\theta} \dot{\theta}^2 - \frac{g}{l + R\theta} \sin\theta - \frac{c}{m} \dot{\theta}
\end{aligned}
$$


---

**Dudas o supuestos:** Se supone que el hilo permanece tenso en todo momento ($d(\theta) > 0$) y que no hay deslizamiento ni rozamiento del hilo al despegarse de la superficie del cilindro.

💡 ¿Deseas analizar la linealización para pequeñas oscilaciones alrededor de $\theta = 0$ o construir el modelo en el espacio de estados?
