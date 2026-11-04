# E3P4 — Sistema de dos poleas: Lagrange y circuito equivalente

## Enunciado

Dado el sistema mecánico de dos poleas, plantear Lagrange y hallar el circuito eléctrico equivalente.

**Figura:** (dibujar a mano)

Datos: $H$ distancia techo–piso; $y_1$, $y_2$ medidos hacia abajo desde el techo; cuerda de longitud $l$; $F(t)$ sobre la polea 2 hacia abajo; pesos despreciados.

> Errores del docente en su hoja: la segunda línea dice $y_2 = l - 1 + 2y_1 - \pi R_1$ y debería ser $l - H$. La línea intermedia de Lagrange tiene mal el signo de $k_1 y_1$: debería ser $-k_1 y_1 - 16 k_2 y_1$. El resultado final está bien.

---

## Solución por pasos

### Paso 1. Grados de libertad, ligadura y velocidades

- **Cuerpos:** 2 (polea 1 y polea 2). **Ligaduras:** 1 (la cuerda de longitud $l$).
- $N = 2 - 1 = 1$. Coordenada generalizada: $q = y_1$.

**Ligadura de la cuerda:**

$$
(H - y_1) + \pi R_1 + (y_2 - y_1) = l \quad\Longrightarrow\quad y_2 = l - H + 2y_1 - \pi R_1
$$

Las constantes se cancelan en el equilibrio (regla 3), así que con desviaciones:

$$
y_2 = 2y_1 \qquad\Longrightarrow\qquad \dot{y}_2 = 2\dot{y}_1
$$

### Paso 2. $T$, $V$ y $P$ en función de $y_1$

**Energía cinética:**

$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (2\dot{y}_1)^2 = \frac{1}{2}(m_1 + 4m_2)\,\dot{y}_1^2
$$

**Energía potencial:**
- Resorte $k_1$: deformación $y_1$.
- Resorte $k_2$: rodea la polea 2 y baja al piso en dos tramos (longitud $2H - 2y_2 + \pi R_2$). Cuando la polea baja $y_2$, cada tramo se acorta $y_2$, así que la deformación total es $2y_2 = 4y_1$.

$$
V = \frac{1}{2} k_1 y_1^2 + \frac{1}{2} k_2 (4y_1)^2 = \frac{1}{2}(k_1 + 16k_2)\,y_1^2
$$

**Función de disipación:**
- Amortiguador $c_1$: velocidad $\dot{y}_1$.
- Amortiguador $c_2$: velocidad $\dot{y}_2 = 2\dot{y}_1$.

$$
P = \frac{1}{2} c_1 \dot{y}_1^2 + \frac{1}{2} c_2 (2\dot{y}_1)^2 = \frac{1}{2}(c_1 + 4c_2)\,\dot{y}_1^2
$$

### Paso 3. Ecuación de Lagrange

**Fuerza generalizada:** $F(t)$ actúa sobre la polea 2, en el sentido en que crece $y_2$.

$$
Q = F \cdot \frac{\partial y_2}{\partial y_1} = 2F(t)
$$

**Derivadas:**

$$
\frac{\partial T}{\partial \dot{y}_1} = (m_1 + 4m_2)\,\dot{y}_1 \quad\Longrightarrow\quad \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) = (m_1 + 4m_2)\,\ddot{y}_1
$$

$$
\frac{\partial T}{\partial y_1} = 0, \qquad \frac{\partial V}{\partial y_1} = (k_1 + 16k_2)\,y_1, \qquad \frac{\partial P}{\partial \dot{y}_1} = (c_1 + 4c_2)\,\dot{y}_1
$$

**Sustitución:**

$$
(m_1 + 4m_2)\,\ddot{y}_1 = -(k_1 + 16k_2)\,y_1 - (c_1 + 4c_2)\,\dot{y}_1 + 2F(t)
$$

**EDO final (modelo matemático):**

$$
(m_1 + 4m_2)\,\ddot{y}_1 + (c_1 + 4c_2)\,\dot{y}_1 + (k_1 + 16k_2)\,y_1 = 2F(t)
$$

### Paso 4. Circuito equivalente

Se compara con la forma $L\ddot{q} + R\dot{q} + \frac{1}{C}q = E(t)$, con $q = y_1$:

| Mecánico | Eléctrico | Valor |
|---|---|---|
| $m_1 + 4m_2$ | Inductancia $L$ | $L = m_1 + 4m_2$ |
| $c_1 + 4c_2$ | Resistencia $R$ | $R = c_1 + 4c_2$ |
| $k_1 + 16k_2$ | Capacitor $1/C$ | $C = \dfrac{1}{k_1 + 16k_2}$ |
| $2F(t)$ | Fuente $E(t)$ | $E(t) = 2F(t)$ |

**Malla:** una sola malla en serie con la fuente $2F(t)$, $L$, $R$ y $C$.

**Corriente:** $i(t) = \dot{y}_1$, en sentido horario con la fuente a la izquierda (como en la hoja del docente). Como $F$ empuja hacia abajo, que es el sentido en que crece $y_2$, la fuente empuja la corriente en el sentido positivo de $i$, y $E = +2F$.
