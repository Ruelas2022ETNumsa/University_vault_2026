## Enunciado 5 (ej5T5) — Cuña y bloque con tres fricciones

Dentro de un recinto de ancho d hay dos cuerpos:

- El **cuerpo 1** (masa m₁) se mueve **solo en vertical**, guiado por la pared izquierda. Su punta toca la cuña a una distancia horizontal fija B de la pared izquierda, y su altura sobre el piso es y₁ (positiva hacia arriba).
- El **cuerpo 2** (masa m₂) es una cuña de ángulo α y base horizontal b que se mueve **solo en horizontal** sobre el piso. Su esquina inferior izquierda está a la distancia x₂ del origen (esquina inferior izquierda del recinto). La cuña está unida a la pared derecha por un resorte de constante k, con longitud d − x₂ − b y longitud natural nula.

El cuerpo 1 apoya sobre la cara inclinada de la cuña. Hay tres fricciones viscosas lineales $n = 1$:
- c₁: entre el cuerpo 1 y la pared izquierda.
- c₂: entre la cuña y el piso.
- c₃: entre el cuerpo 1 y la cuña, en la cara inclinada.

**Se pide:**
1. N y coordenada generalizada (se sugiere y₁).
2. La ecuación de restricción que relaciona x₂ con y₁.
3. T, V y P en función de y₁ y ẏ₁. Justificar qué velocidad relativa interviene en la fricción c₃.
4. La EDO de movimiento mediante Lagrange.

---

### 1. Datos y esquema
- **Cuerpo 1 (bloque vertical):** Masa $m_1$, restringido a moverse **únicamente en dirección vertical** a una distancia horizontal fija $B$ de la pared izquierda ($x_1 = B$). Su altura sobre el piso es $y_1(t)$ ($y$ positiva hacia arriba).
- **Cuerpo 2 (cuña):** Masa $m_2$, ángulo $\alpha$, base horizontal $b$. Se mueve **únicamente en dirección horizontal** sobre el piso ($y = 0$). Su esquina inferior izquierda está en $x_2(t)$ respecto a la pared izquierda.
- **Recinto y resorte:** Ancho del recinto $d$ (pared izquierda en $x=0$, pared derecha en $x=d$). Resorte en la pared derecha con constante $k$ y longitud natural $l_0 = 0$, conectado a la esquina trasera de la cuña (longitud instantánea $L_{res} = d - x_2 - b$).
- **Fricciones viscosas lineales ($n=1$):**
  - $c_1$: entre cuerpo 1 y pared izquierda (dirección vertical).
  - $c_2$: entre cuña y el piso (dirección horizontal).
  - $c_3$: entre cuerpo 1 y cuña (cara inclinada a ángulo $\alpha$).

---

### 2. Grados de libertad $N$ y coordenada generalizada
- **Coordenadas cartesianas iniciales:** 2 ($y_1$ para el cuerpo 1, $x_2$ para la cuña).
- **Restricción holónoma por contacto en la cara inclinada ($k = 1$):**
  El punto de contacto se ubica a distancia horizontal $B$ del origen. La distancia horizontal desde la esquina inferior izquierda de la cuña ($x_2$) hasta la punta del cuerpo 1 es $(B - x_2)$. Dado el ángulo $\alpha$ de la cuña:
  
$$
y_1 = (B - x_2)\tan\alpha
$$

- **Grados de libertad ($N$):**
  
$$
N = 2 - 1 = 1
$$

- **Coordenada generalizada elegida:** $q = y_1$ [Wells, Cap. 2].

---

### 3. Restricciones, posiciones y velocidades en función de $y_1$ y $\dot{y}_1$

#### **Ecuación de restricción:**

$$
x_2(y_1) = B - y_1 \cot\alpha
$$

Derivando respecto al tiempo $t$:

$$
\dot{x}_2 = -\dot{y}_1 \cot\alpha
$$


#### **Velocidad del cuerpo 1:**

$$
\vec{v}_1 = \dot{y}_1 \hat{j} \implies v_1^2 = \dot{y}_1^2
$$


#### **Velocidad de la cuña (cuerpo 2):**

$$
\vec{v}_2 = \dot{x}_2 \hat{i} = -\dot{y}_1 \cot\alpha \, \hat{i} \implies v_2^2 = \dot{y}_1^2 \cot^2\alpha
$$


#### **Velocidad relativa en la cara inclinada (para la fricción $c_3$):**
La velocidad relativa del cuerpo 1 respecto a la cuña es:

$$
\vec{v}_{rel} = \vec{v}_1 - \vec{v}_2 = \dot{y}_1 \cot\alpha \, \hat{i} + \dot{y}_1 \hat{j}
$$

El vector unitario tangente a la cara inclinada de la cuña es $\hat{u} = \cos\alpha \, \hat{i} + \sin\alpha \, \hat{j}$. Reescribiendo $\vec{v}_{rel}$:

$$
\vec{v}_{rel} = \dot{y}_1 \left( \frac{\cos\alpha}{\sin\alpha} \hat{i} + \hat{j} \right) = \frac{\dot{y}_1}{\sin\alpha} (\cos\alpha \, \hat{i} + \sin\alpha \, \hat{j}) = \frac{\dot{y}_1}{\sin\alpha} \hat{u}
$$

Por tanto, el módulo al cuadrado de la velocidad relativa a lo largo de la rampa es:

$$
v_{rel}^2 = \frac{\dot{y}_1^2}{\sin^2\alpha} = \dot{y}_1^2 \csc^2\alpha = \dot{y}_1^2 (1 + \cot^2\alpha)
$$

**Justificación:** Esta es la velocidad con la que el punto de apoyo del cuerpo 1 se desliza a lo largo de la cara inclinada de la cuña. Al estar restringido el contacto a permanecer sobre la superficie inclinada, $\vec{v}_{rel}$ es estrictamente colineal con la rampa.

---

### 4. $T$, $V$ y $P$ por separado

#### **Energía cinética ($T$):** [Wells, Cap. 2 y Cap. 3]

$$
T = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \left(\dot{y}_1 \cot\alpha\right)^2
$$


$$
T = \frac{1}{2} \left( m_1 + m_2 \cot^2\alpha \right) \dot{y}_1^2
$$


#### **Energía potencial ($V$):** [Wells, Cap. 5; Goldstein, Cap. 1]
Tomando el nivel de referencia gravitatorio en el piso ($y = 0$). El centro de masa de la cuña $m_2$ permanece a altura constante, por lo que no contribuye a la variación del potencial gravitatorio:

$$
V = m_1 g y_1 + \frac{1}{2} k (d - x_2 - b)^2
$$

Sustituyendo $x_2 = B - y_1 \cot\alpha$:

$$
d - x_2 - b = (d - B - b) + y_1 \cot\alpha
$$


$$
V = m_1 g y_1 + \frac{1}{2} k \left[ (d - B - b) + y_1 \cot\alpha \right]^2
$$


#### **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1, Ec. 1.67; Wells, Cap. 6, Ec. 6.16]
Para tres fricciones viscosas lineales ($n=1$), $P = \frac{1}{2} \sum c_k v_k^2$:

$$
P = \frac{1}{2} c_1 v_1^2 + \frac{1}{2} c_2 v_2^2 + \frac{1}{2} c_3 v_{rel}^2
$$


$$
P = \frac{1}{2} c_1 \dot{y}_1^2 + \frac{1}{2} c_2 \left(\dot{y}_1 \cot\alpha\right)^2 + \frac{1}{2} c_3 \left(\frac{\dot{y}_1}{\sin\alpha}\right)^2
$$


$$
P = \frac{1}{2} \left[ c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right] \dot{y}_1^2
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida con función de disipación de Rayleigh [Goldstein, Cap. 1, Ec. 1.70]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) - \frac{\partial T}{\partial y_1} + \frac{\partial V}{\partial y_1} + \frac{\partial P}{\partial \dot{y}_1} = 0
$$


Calculando término a término:
1. **Derivada inercial:**
   
$$
\frac{\partial T}{\partial \dot{y}_1} = \left( m_1 + m_2 \cot^2\alpha \right) \dot{y}_1 \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) = \left( m_1 + m_2 \cot^2\alpha \right) \ddot{y}_1
$$

2. **Derivada cinemática respecto a la posición:**
   
$$
\frac{\partial T}{\partial y_1} = 0
$$

3. **Derivada de la energía potencial:**
   
$$
\frac{\partial V}{\partial y_1} = m_1 g + k \cot\alpha \left[ (d - B - b) + y_1 \cot\alpha \right] = m_1 g + k (d - B - b)\cot\alpha + k \cot^2\alpha \, y_1
$$

4. **Derivada de la función de disipación:**
   
$$
\frac{\partial P}{\partial \dot{y}_1} = \left[ c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right] \dot{y}_1
$$


---

### 6. EDO final (modelo matemático)
Sustituyendo los términos en la ecuación de Lagrange:

$$
\left( m_1 + m_2 \cot^2\alpha \right) \ddot{y}_1 + \left( c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right) \dot{y}_1 + k \cot^2\alpha \, y_1 + m_1 g + k (d - B - b)\cot\alpha = 0
$$


Despejando la aceleración generalizada $\ddot{y}_1$:

$$
\ddot{y}_1 = -\frac{\left( c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right) \dot{y}_1 + k \cot^2\alpha \, y_1 + m_1 g + k (d - B - b)\cot\alpha}{m_1 + m_2 \cot^2\alpha}
$$


---

### 7. Verificación

#### **Análisis dimensional:**
- Masa equivalente: $m_{eq} = m_1 + m_2 \cot^2\alpha$ $[\text{kg}]$.
- Coeficiente de amortiguamiento equivalente: $c_{eq} = c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha$ $[\text{kg/s}]$.
- Rigidez equivalente: $k_{eq} = k \cot^2\alpha$ $[\text{N/m} = \text{kg/s}^2]$.
- Fuerza constante equivalente: $F_0 = m_1 g + k(d - B - b)\cot\alpha$ $[\text{N} = \text{kg}\cdot\text{m/s}^2]$.
- Término de aceleración: $\left[\frac{c_{eq}}{m_{eq}} \dot{y}_1\right] = \frac{\text{kg/s}}{\text{kg}} \cdot \frac{\text{m}}{\text{s}} = \text{m/s}^2$. Todos los términos del modelo poseen unidades homogéneas de aceleración $[\text{m/s}^2]$.

#### **Caso límite $c_1 = c_2 = c_3 = 0$ (sistema conservativo sin fricción):**
Haciendo $c_i = 0$, la función de disipación se anula ($P = 0$) y la EDO se reduce a:

$$
(m_1 + m_2 \cot^2\alpha) \ddot{y}_1 + k \cot^2\alpha \, y_1 = -m_1 g - k(d - B - b)\cot\alpha
$$

Se recupera exactamente el modelo conservativo de un oscilador armónico de 1 GDL sometido a pretensión elástica e inercia acoplada [Wells, Cap. 3].

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 1 \quad \text{con coordenada generalizada } q = y_1 \\
2.\quad x_2 &= B - y_1 \cot\alpha \\
3.\quad T &= \frac{1}{2} \left( m_1 + m_2 \cot^2\alpha \right) \dot{y}_1^2 \\
V &= m_1 g y_1 + \frac{1}{2} k \left[ (d - B - b) + y_1 \cot\alpha \right]^2 \\
P &= \frac{1}{2} \left( c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right) \dot{y}_1^2 \\
\text{Velocidad relativa en } c_3: \quad & v_{rel} = \frac{|\dot{y}_1|}{\sin\alpha} = |\dot{y}_1|\csc\alpha \\
4.\quad \ddot{y}_1 &= -\frac{\left( c_1 + c_2 \cot^2\alpha + c_3 \csc^2\alpha \right) \dot{y}_1 + k \cot^2\alpha \, y_1 + m_1 g + k (d - B - b)\cot\alpha}{m_1 + m_2 \cot^2\alpha}
\end{aligned}
$$


---

**Dudas o supuestos:** Se asume que el cuerpo 1 mantiene contacto permanente con la cara inclinada de la cuña sin desprendimiento y que el resorte opera en régimen lineal dentro de su rango elástico.

💡 ¿Te gustaría calcular la posición de equilibrio estático $y_{1,e}$ o estudiar la respuesta en el espacio de estados?
