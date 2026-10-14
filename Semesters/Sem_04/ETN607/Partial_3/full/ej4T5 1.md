## Enunciado 4 (ej4T5) — Poleas, resorte y cables (sistema no inercial)

Entre el techo y el piso hay una distancia H. Del techo cuelga un **resorte** (constante k, longitud natural l₀) que sostiene la **polea 1**. Se miden hacia abajo desde el techo las posiciones y₁ (polea 1), y₂ (polea 2) e y₃ (masa 3).

- Un **cable 1** (longitud l₁) parte de un punto fijo del piso, sube, rodea la polea 1 (radio R₁, media vuelta) y baja hasta sostener el centro de la **polea 2**.
- Un **cable 2** (longitud l₂) parte de otro punto fijo del piso, sube, rodea la polea 2 (radio R₂, media vuelta) y baja una distancia a hasta sostener la **masa 3**, de modo que a = y₃ − y₂.

Las masas de la polea 1, la polea 2 y el bloque 3 son m₁, m₂ y m₃. Las poleas tienen momento de inercia nulo $I₁ = I₂ = 0$. Los cables son inextensibles y sin masa. Cada masa sufre fricción viscosa lineal $n = 1$ con coeficientes c₁, c₂ y c₃ respectivamente.

**Se pide:**
1. N = (cantidad de masas) − (cantidad de cables); elegir la coordenada generalizada (se sugiere a).
2. Las ecuaciones de restricción de cada cable.
3. y₁, y₂, y₃ y sus velocidades en función de a y ȧ.
4. T, V y P.
5. La EDO de movimiento en a mediante Lagrange.

---
### 1. Datos y esquema
- **Techo:** Fijo en $y = 0$.
- **Piso:** Fijo a una distancia $y = H$ respecto al techo.
- **Sistema de coordenadas:** Vertical con origen en el techo ($y = 0$) y eje positivo hacia abajo.
- **Posiciones:**
  - $y_1(t)$: posición del centro de la polea 1 (masa $m_1$).
  - $y_2(t)$: posición del centro de la polea 2 (masa $m_2$).
  - $y_3(t)$: posición de la masa $m_3$.
  - $a(t) = y_3(t) - y_2(t)$: distancia entre la polea 2 y la masa 3.
- **Resorte superior:** Constante $k$, longitud natural $l_0$, entre el techo y la polea 1 (longitud $y_1$).
- **Cables inextensibles:**
  - **Cable 1 ($l_1$):** del piso ($y=H$), rodea la polea 1 ($R_1$) y baja a la polea 2 ($y_2$).
  - **Cable 2 ($l_2$):** del piso ($y=H$), rodea la polea 2 ($R_2$) y baja a la masa $m_3$ ($y_3$).
- **Inercias y fricciones:** $I_1 = I_2 = 0$. Fricción viscosa lineal ($n=1$) con coeficientes $c_1, c_2, c_3$ [Taylor, Cap. 2; Goldstein, Cap. 1].

---

### 2. Grados de libertad $N$ y coordenada generalizada
- **Número de coordenadas de posición:** 3 ($y_1, y_2, y_3$).
- **Número de restricciones holónomas (cables):** 2 ($k = 2$).
- **Grados de libertad ($N$):**
  
$$
N = (\text{cantidad de masas}) - (\text{cantidad de cables}) = 3 - 2 = 1
$$

- **Coordenada generalizada elegida:** $q = a$ [Wells, Cap. 2 y Cap. 4].

---

### 3. Ecuaciones de restricción, posiciones y velocidades

#### **Ecuación de restricción del Cable 2 ($l_2$):**

$$
l_2 = (H - y_2) + \pi R_2 + (y_3 - y_2) = H - 2y_2 + y_3 + \pi R_2 = \text{constante}
$$

Como $y_3 - y_2 = a \implies y_3 = y_2 + a$:

$$
l_2 = H - y_2 + a + \pi R_2 \implies y_2 = H + a + \pi R_2 - l_2
$$

Derivando respecto al tiempo:

$$
\dot{y}_2 = \dot{a}
$$


Sustituyendo $y_2$ en $y_3$:

$$
y_3 = H + 2a + \pi R_2 - l_2 \implies \dot{y}_3 = 2\dot{a}
$$


#### **Ecuación de restricción del Cable 1 ($l_1$):**

$$
l_1 = (H - y_1) + \pi R_1 + (y_2 - y_1) = H - 2y_1 + y_2 + \pi R_1 = \text{constante}
$$

Despejando $y_1$ y sustituyendo $y_2$:

$$
2y_1 = H + (H + a + \pi R_2 - l_2) + \pi R_1 - l_1
$$


$$
y_1 = H + \frac{a}{2} + \frac{\pi R_1 + \pi R_2 - l_1 - l_2}{2}
$$

Derivando respecto al tiempo:

$$
\dot{y}_1 = \frac{1}{2}\dot{a}
$$


#### **Resumen de expresiones en función de $a$ y $\dot{a}$:**

$$
y_1 = \frac{a}{2} + C_1, \qquad \dot{y}_1 = \frac{1}{2}\dot{a}
$$


$$
y_2 = a + C_2, \qquad \dot{y}_2 = \dot{a}
$$


$$
y_3 = 2a + C_2, \qquad \dot{y}_3 = 2\dot{a}
$$

donde $C_1 = H + \frac{\pi R_1 + \pi R_2 - l_1 - l_2}{2}$ y $C_2 = H + \pi R_2 - l_2$.

---

### 4. $T$, $V$ y $P$ por separado

#### **Energía cinética ($T$):** [Wells, Cap. 2 y Cap. 4]
Con $I_1 = I_2 = 0$:

$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$


$$
T = \frac{1}{2} m_1 \left(\frac{\dot{a}}{2}\right)^2 + \frac{1}{2} m_2 \dot{a}^2 + \frac{1}{2} m_3 (2\dot{a})^2 = \frac{1}{2} \left( \frac{m_1}{4} + m_2 + 4m_3 \right) \dot{a}^2
$$


#### **Energía potencial ($V$):** [Wells, Cap. 4 y Cap. 5]
Con nivel de referencia en el techo ($y=0$):

$$
V = \frac{1}{2} k (y_1 - l_0)^2 - m_1 g y_1 - m_2 g y_2 - m_3 g y_3
$$


$$
V = \frac{1}{2} k \left( \frac{a}{2} + C_1 - l_0 \right)^2 - m_1 g \left( \frac{a}{2} + C_1 \right) - m_2 g \left( a + C_2 \right) - m_3 g \left( 2a + C_2 \right)
$$


#### **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1; Wells, Cap. 6, Ec. 6.16]
Para fricción viscosa lineal ($n = 1$):

$$
P = \frac{1}{2} c_1 \dot{y}_1^2 + \frac{1}{2} c_2 \dot{y}_2^2 + \frac{1}{2} c_3 \dot{y}_3^2
$$


$$
P = \frac{1}{2} c_1 \left(\frac{\dot{a}}{2}\right)^2 + \frac{1}{2} c_2 \dot{a}^2 + \frac{1}{2} c_3 (2\dot{a})^2 = \frac{1}{2} \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a}^2
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida con disipación de Rayleigh [Goldstein, Cap. 1, Ec. 1.70]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{a}}\right) - \frac{\partial T}{\partial a} + \frac{\partial V}{\partial a} + \frac{\partial P}{\partial \dot{a}} = 0
$$


Calculando los términos:
1. **Derivada inercial:**
   
$$
\frac{\partial T}{\partial \dot{a}} = \left( \frac{m_1}{4} + m_2 + 4m_3 \right) \dot{a} \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{a}}\right) = \left( \frac{m_1}{4} + m_2 + 4m_3 \right) \ddot{a}
$$

2. **Derivada respecto a $a$:**
   
$$
\frac{\partial T}{\partial a} = 0
$$

3. **Derivada del potencial:**
   
$$
\frac{\partial V}{\partial a} = \frac{1}{4} k a + \frac{1}{2} k (C_1 - l_0) - \left( \frac{m_1}{2} + m_2 + 2m_3 \right) g
$$

4. **Derivada de la función de disipación:**
   
$$
\frac{\partial P}{\partial \dot{a}} = \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a}
$$


---

### 6. EDO final (modelo matemático)
Sustituyendo en la ecuación de Lagrange:

$$
\left( \frac{m_1}{4} + m_2 + 4m_3 \right) \ddot{a} + \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a} + \frac{1}{4} k a + \frac{1}{2} k (C_1 - l_0) - \left( \frac{m_1}{2} + m_2 + 2m_3 \right) g = 0
$$


Despejando la aceleración generalizada $\ddot{a}$:

$$
\ddot{a} = \frac{\left( \frac{m_1}{2} + m_2 + 2m_3 \right) g - \frac{1}{2} k (C_1 - l_0) - \frac{1}{4} k a - \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a}}{\frac{m_1}{4} + m_2 + 4m_3}
$$


---

### 7. Verificación

#### Análisis dimensional:
- Inercia equivalente $m_{eq} = \frac{m_1}{4} + m_2 + 4m_3$ $[\text{kg}]$.
- Amortiguamiento equivalente $c_{eq} = \frac{c_1}{4} + c_2 + 4c_3$ $[\text{kg/s}]$.
- Rigidez equivalente $k_{eq} = \frac{k}{4}$ $[\text{N/m} = \text{kg/s}^2]$.
- Todos los términos divididos por $m_{eq}$ tienen dimensión de aceleración $[\text{m/s}^2]$.

#### Caso límite $c_1 = c_2 = c_3 = 0$ (sistema conservativo):
Haciendo $c_i = 0$, la EDO se reduce a:

$$
m_{eq} \ddot{a} + k_{eq} a = \left( \frac{m_1}{2} + m_2 + 2m_3 \right) g - \frac{1}{2} k (C_1 - l_0)
$$

Se recupera exactamente el modelo conservativo de un oscilador armónico de 1 GDL sometido a fuerza gravitacional constante y pretensión elástica.

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 3 - 2 = 1 \quad \text{con coordenada generalizada } q = a \\
2.\quad \text{Cable 1: } & H - 2y_1 + y_2 + \pi R_1 = l_1 \\
\text{Cable 2: } & H - 2y_2 + y_3 + \pi R_2 = l_2 \\
3.\quad y_1 &= \frac{a}{2} + C_1, \quad \dot{y}_1 = \frac{1}{2}\dot{a} \\
y_2 &= a + C_2, \quad \dot{y}_2 = \dot{a} \\
y_3 &= 2a + C_2, \quad \dot{y}_3 = 2\dot{a} \\
4.\quad T &= \frac{1}{2} \left( \frac{m_1}{4} + m_2 + 4m_3 \right) \dot{a}^2 \\
V &= \frac{1}{2} k \left( \frac{a}{2} + C_1 - l_0 \right)^2 - m_1 g \left( \frac{a}{2} + C_1 \right) - m_2 g \left( a + C_2 \right) - m_3 g \left( 2a + C_2 \right) \\
P &= \frac{1}{2} \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a}^2 \\
5.\quad \ddot{a} &= \frac{\left( \frac{m_1}{2} + m_2 + 2m_3 \right) g - \frac{1}{2} k (C_1 - l_0) - \frac{1}{4} k a - \left( \frac{c_1}{4} + c_2 + 4c_3 \right) \dot{a}}{\frac{m_1}{4} + m_2 + 4m_3}
\end{aligned}
$$


---

**Dudas o supuestos:** Se supone que los cables se mantienen permanentemente bajo tensión y no sufren deslizamiento sobre las poleas.

💡 ¿Deseas determinar la posición de equilibrio estático $a_e$ o formular el espacio de estados matricial de este sistema?
