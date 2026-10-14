## Enunciado 2 (ej2T5) — Partícula sobre una barra parabólica

Una partícula de masa m se mueve obligada sobre una barra con forma de parábola y = 4x², en un plano vertical (y positiva hacia arriba, gravedad g). Entre la partícula y la barra hay fricción viscosa lineal, f = c·v (n = 1).

**Se pide:**
1. Grados de libertad N y la coordenada generalizada elegida (la restricción reduce N de 2 a 1).
2. ẏ en función de x y ẋ.
3. T, V y P en función de x y ẋ.
4. La EDO de movimiento (modelo matemático) mediante Lagrange.

---

### 1. Datos y esquema
- **Masa de la partícula:** $m$
- **Geometría del riel/barra:** Parábola $y = 4x^2$ en el plano vertical $(x, y)$.
- **Aceleración de la gravedad:** $\vec{g} = -g \hat{j}$ ($y$ positiva hacia arriba).
- **Fuerza de fricción viscosa lineal ($n=1$):**
  
$$
\vec{f} = -c \vec{v} = -c (\dot{x}\hat{i} + \dot{y}\hat{j})
$$

  con magnitud $f = c v$, siempre opuesta a la velocidad instantánea $\vec{v}$ [Taylor, Cap. 2; Goldstein, Cap. 1].
- **Sistema de referencia:** Plano cartesiano vertical con origen en el vértice de la parábola $(0,0)$.

---

### 2. Grados de libertad $N$ y coordenada generalizada
- **Número de coordenadas cartesianas:** 2 ($x, y$).
- **Restricción holónoma ($k = 1$):**
  
$$
y - 4x^2 = 0
$$

- **Grados de libertad ($N$):**
  
$$
N = 2 - 1 = 1
$$

- **Coordenada generalizada elegida:** $q = x$ [Wells, Cap. 2 y Cap. 3].

---

### 3. Restricciones y velocidad $\dot{y}(x, \dot{x})$
A partir de la ecuación de restricción holónoma $y = 4x^2$, derivando respecto al tiempo $t$ mediante la regla de la cadena:

$$
\dot{y} = \frac{d}{dt}(4x^2) = 8 x \dot{x}
$$


---

### 4. $T$, $V$ y $P$ por separado (en función de $x$ y $\dot{x}$)

#### **Energía cinética ($T$):** [Wells, Cap. 2, Ec. 2.40; Cap. 3]
El módulo al cuadrado de la velocidad instantánea es:

$$
v^2 = \dot{x}^2 + \dot{y}^2 = \dot{x}^2 + (8x\dot{x})^2 = \dot{x}^2 (1 + 64 x^2)
$$


Sustituyendo en la expresión general de $T$:

$$
T = \frac{1}{2} m v^2 = \frac{1}{2} m \dot{x}^2 \left(1 + 64 x^2\right)
$$


#### **Energía potencial ($V$):** [Wells, Cap. 5; Goldstein, Cap. 1]
Tomando el nivel de referencia gravitatorio en $V(x, 0) = 0$:

$$
V = m g y = 4 m g x^2
$$


#### **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1; Wells, Cap. 6, Ec. 6.17]
Para fricción viscosa lineal ($n = 1$), $P = \frac{1}{2} c v^2$:

$$
P = \frac{1}{2} c \left(\dot{x}^2 + \dot{y}^2\right) = \frac{1}{2} c \dot{x}^2 \left(1 + 64 x^2\right)
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida con disipación de Rayleigh [Goldstein, Cap. 1, Ec. 1.70; Wells, Cap. 6]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} + \frac{\partial V}{\partial x} + \frac{\partial P}{\partial \dot{x}} = 0
$$


Calculando cada término individualmente:
1. **Derivada parcial de $T$ respecto a $\dot{x}$:**
   
$$
\frac{\partial T}{\partial \dot{x}} = m \dot{x} (1 + 64 x^2)
$$


2. **Derivada temporal de $\frac{\partial T}{\partial \dot{x}}$:**
   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) = m \ddot{x} (1 + 64 x^2) + m \dot{x} (128 x \dot{x}) = m \ddot{x} (1 + 64 x^2) + 128 m x \dot{x}^2
$$


3. **Derivada parcial de $T$ respecto a $x$:**
   
$$
\frac{\partial T}{\partial x} = \frac{1}{2} m \dot{x}^2 (128 x) = 64 m x \dot{x}^2
$$


4. **Término inercial neto:**
   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} = m \ddot{x} (1 + 64 x^2) + 64 m x \dot{x}^2
$$


5. **Derivada parcial de $V$ respecto a $x$:**
   
$$
\frac{\partial V}{\partial x} = \frac{d}{dx}\left(4 m g x^2\right) = 8 m g x
$$


6. **Derivada parcial de $P$ respecto a $\dot{x}$:**
   
$$
\frac{\partial P}{\partial \dot{x}} = c \dot{x} (1 + 64 x^2)
$$


---

### 6. EDO final (modelo matemático)
Sustituyendo los términos en la ecuación de Lagrange:

$$
m \ddot{x} (1 + 64 x^2) + 64 m x \dot{x}^2 + 8 m g x + c \dot{x} (1 + 64 x^2) = 0
$$


Despejando la aceleración generalizada $\ddot{x}$:

$$
\ddot{x} = -\frac{64 x \dot{x}^2 + 8 g x}{1 + 64 x^2} - \frac{c}{m} \dot{x}
$$


---

### 7. Verificación

#### Análisis dimensional:
- En la parábola $y = b x^2$ con $b = 4$, la constante $b$ tiene dimensiones $[b] = \text{m}^{-1}$.
- El factor $64 x^2 = (2b)^2 x^2$ es adimensional.
- Término $64 x \dot{x}^2$: $[b^2 x \dot{x}^2] = \text{m}^{-2} \cdot \text{m} \cdot (\text{m}^2/\text{s}^2) = \text{m/s}^2$ (aceleración).
- Término $8 g x$: $[2b g x] = \text{m}^{-1} \cdot (\text{m/s}^2) \cdot \text{m} = \text{m/s}^2$ (aceleración).
- Término $\frac{c}{m} \dot{x}$: con $[c] = \text{kg/s}$, se tiene $\left[\frac{c}{m} \dot{x}\right] = \text{s}^{-1} \cdot (\text{m/s}) = \text{m/s}^2$ (aceleración).
- Todos los términos del modelo matemático son homogéneos en unidades de aceleración $[\text{m/s}^2]$.

#### Caso límite $c = 0$ (sistema conservativo sin fricción):
Haciendo $c = 0$, la EDO se reduce a:

$$
m (1 + 64 x^2) \ddot{x} + 64 m x \dot{x}^2 + 8 m g x = 0
$$

Coincide exactamente con el modelo clásico de una partícula sobre un alambre parabólico libre de rozamiento $y = b x^2$ adaptado a $b = 4$ [Wells, Cap. 3, Ejemplo 3.2].

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 1 \quad \text{con coordenada generalizada } q = x \\
2.\quad \dot{y} &= 8 x \dot{x} \\
3.\quad T &= \frac{1}{2} m \dot{x}^2 \left(1 + 64 x^2\right) \\
V &= 4 m g x^2 \\
P &= \frac{1}{2} c \dot{x}^2 \left(1 + 64 x^2\right) \\
4.\quad \ddot{x} &= -\frac{64 x \dot{x}^2 + 8 g x}{1 + 64 x^2} - \frac{c}{m} \dot{x} \quad \text{o bien} \quad m(1 + 64 x^2)\ddot{x} + 64 m x \dot{x}^2 + c(1 + 64 x^2)\dot{x} + 8 m g x = 0.
\end{aligned}
$$


---

**Dudas o supuestos:** Se supone movimiento confinado estrictamente al plano vertical $(x, y)$ sin desprendimiento ni rozamiento por contacto seco con la barra (solo fricción viscosa $n=1$).

💡 ¿Te gustaría analizar la linealización para pequeñas oscilaciones alrededor de $x = 0$ o construir el modelo en el espacio de estados?
