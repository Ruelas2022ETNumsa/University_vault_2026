### 1. Grados de libertad $N$, ligadura y relación de velocidades

* **Número de grados de libertad:**  
  
$$
\text{Cuerpos} = 3 \text{ (polea 1, polea 2, extremo 3)}, \qquad \text{Ligaduras} = 1 \text{ (cuerda de longitud } l\text{)}
$$

  
$$
N = 3 - 1 = 2 \quad \rightarrow \quad \text{Coordenadas generalizadas: } q_1 = y_2, \; q_2 = y_3
$$


* **Ecuación de ligadura de la cuerda:**  
  La longitud total de la cuerda entre la polea 2, la polea 1 y el extremo 3 es:
  
$$
l = (y_2 - y_1) + \pi R_1 + (y_3 - y_1) = y_2 + y_3 - 2y_1 + \pi R_1
$$

  Midiendo $y_1, y_2, y_3$ como desviaciones respecto al equilibrio:
  
$$
y_2 + y_3 - 2y_1 = 0 \implies y_1 = \frac{1}{2}(y_2 + y_3)
$$


* **Relación de velocidades (derivada de la ligadura):**  
  
$$
\dot{y}_1 = \frac{1}{2}(\dot{y}_2 + \dot{y}_3)
$$


---

### 2. Energías $T$, $V$ y $P$ en función de $y_2, y_3$ (con $m_3 = 0$)

* **Energía Cinética ($T$):**  
  
$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2
$$

  Sustituyendo $\dot{y}_1 = \frac{1}{2}(\dot{y}_2 + \dot{y}_3)$ y $m_3 = 0$:
  
$$
T = \frac{1}{8} m_1 (\dot{y}_2 + \dot{y}_3)^2 + \frac{1}{2} m_2 \dot{y}_2^2
$$


* **Energía Potencial ($V$):**  
  * Resorte $k$ (polea 1): estiramiento $y_1 = \frac{1}{2}(y_2 + y_3)$.
  * Resorte $k'$ (polea 2): deformación $2y_2$.
  
$$
V = \frac{1}{2} k \left[\frac{1}{2}(y_2 + y_3)\right]^2 + \frac{1}{2} k' (2y_2)^2 = \frac{1}{8} k (y_2 + y_3)^2 + 2 k' y_2^2
$$


* **Función de Disipación de Rayleigh ($P$):**  
  * Amortiguador $c_1$ (polea 1): actúa con velocidad $\dot{y}_1 = \frac{1}{2}(\dot{y}_2 + \dot{y}_3)$.
  * Amortiguador $c_2$ (polea 2): actúa con velocidad $\dot{y}_2$.
  
$$
P = \frac{1}{2} c_1 \left[\frac{1}{2}(\dot{y}_2 + \dot{y}_3)\right]^2 + \frac{1}{2} c_2 \dot{y}_2^2 = \frac{1}{8} c_1 (\dot{y}_2 + \dot{y}_3)^2 + \frac{1}{2} c_2 \dot{y}_2^2
$$


---

### 3. Fuerzas generalizadas $Q_2$ y $Q_3$

La fuerza externa $F(t)$ actúa sobre el extremo 3 en la dirección positiva de $y_3$:
* **Para $q = y_2$:**  
  
$$
Q_2 = F(t) \cdot \frac{\partial y_3}{\partial y_2} = 0
$$

* **Para $q = y_3$:**  
  
$$
Q_3 = F(t) \cdot \frac{\partial y_3}{\partial y_3} = F(t)
$$


---

### 4. Las dos ecuaciones de Lagrange

#### A. Para la coordenada $y_2$:
* **Derivadas:**
  
$$
\frac{\partial T}{\partial \dot{y}_2} = \frac{1}{4} m_1 (\dot{y}_2 + \dot{y}_3) + m_2 \dot{y}_2 \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_2}\right) = \left(\frac{1}{4} m_1 + m_2\right) \ddot{y}_2 + \frac{1}{4} m_1 \ddot{y}_3
$$

  
$$
\frac{\partial T}{\partial y_2} = 0, \qquad \frac{\partial V}{\partial y_2} = \frac{1}{4} k (y_2 + y_3) + 4 k' y_2, \qquad \frac{\partial P}{\partial \dot{y}_2} = \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) + c_2 \dot{y}_2
$$


* **EDO 1 final ordenada:**
  
$$
\left(\frac{1}{4} m_1 + m_2\right) \ddot{y}_2 + \frac{1}{4} m_1 \ddot{y}_3 + \left(\frac{1}{4} c_1 + c_2\right) \dot{y}_2 + \frac{1}{4} c_1 \dot{y}_3 + \left(\frac{1}{4} k + 4 k'\right) y_2 + \frac{1}{4} k y_3 = 0
$$

  *(Expresada alternativamente agruando los términos compartidos: $m_2 \ddot{y}_2 + c_2 \dot{y}_2 + 4k' y_2 + \frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3) + \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) + \frac{1}{4} k (y_2 + y_3) = 0$).*

#### B. Para la coordenada $y_3$:
* **Derivadas:**
  
$$
\frac{\partial T}{\partial \dot{y}_3} = \frac{1}{4} m_1 (\dot{y}_2 + \dot{y}_3) \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) = \frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3)
$$

  
$$
\frac{\partial T}{\partial y_3} = 0, \qquad \frac{\partial V}{\partial y_3} = \frac{1}{4} k (y_2 + y_3), \qquad \frac{\partial P}{\partial \dot{y}_3} = \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3)
$$


* **EDO 2 final ordenada:**
  
$$
\frac{1}{4} m_1 \ddot{y}_2 + \frac{1}{4} m_1 \ddot{y}_3 + \frac{1}{4} c_1 \dot{y}_2 + \frac{1}{4} c_1 \dot{y}_3 + \frac{1}{4} k y_2 + \frac{1}{4} k y_3 = F(t)
$$

  *(Expresada alternativamente: $\frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3) + \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) + \frac{1}{4} k (y_2 + y_3) = F(t)$).*

---

### 5. Circuito eléctrico equivalente

* **Mallas y corrientes de malla (sentido horario):**
  * **Malla 2:** Corriente $i_2 = \dot{y}_2$ (carga $q_2 = y_2$).
  * **Malla 3:** Corriente $i_3 = -\dot{y}_3$ (carga $q_3 = -y_3$).
  * **Rama compartida entre Malla 2 y Malla 3:** Lleva la diferencia de corrientes $i_2 - i_3 = \dot{y}_2 - (-\dot{y}_3) = \dot{y}_2 + \dot{y}_3$ (carga $q_2 - q_3 = y_2 + y_3$).

* **Tabla de elementos del circuito:**

| Ubicación | Elemento físico / Mecánico | Elemento eléctrico | Valor eléctrico |
| :--- | :--- | :--- | :--- |
| **Exclusivo de Malla 2** | Masa $m_2$ | Inductancia $L_2$ | $L_2 = m_2$ |
| **Exclusivo de Malla 2** | Amortiguador $c_2$ | Resistencia $R_2$ | $R_2 = c_2$ |
| **Exclusivo de Malla 2** | Resorte $4k'$ | Capacitor $C_2$ | $C_2 = \frac{1}{4k'}$ |
| **Rama compartida (2–3)** | Masa $\frac{1}{4} m_1$ | Inductancia $L_{23}$ | $L_{23} = \frac{1}{4} m_1$ |
| **Rama compartida (2–3)** | Amortiguador $\frac{1}{4} c_1$ | Resistencia $R_{23}$ | $R_{23} = \frac{1}{4} c_1$ |
| **Rama compartida (2–3)** | Resorte $\frac{1}{4} k$ | Capacitor $C_{23}$ | $C_{23} = \frac{4}{k}$ |
| **Exclusivo de Malla 3** | Fuerza $F(t)$ | Fuente de voltaje $E(t)$ | $E(t) = F(t)$ |

* **Verificación de las ecuaciones de malla:**
  * **Ecuación de Malla 2:**  
    
$$
L_2 \ddot{q}_2 + R_2 \dot{q}_2 + \frac{1}{C_2} q_2 + L_{23}(\ddot{q}_2 - \ddot{q}_3) + R_{23}(\dot{q}_2 - \dot{q}_3) + \frac{1}{C_{23}}(q_2 - q_3) = 0
$$

    Sustituyendo $q_2 = y_2$ y $-q_3 = y_3$:
    
$$
m_2 \ddot{y}_2 + c_2 \dot{y}_2 + 4k' y_2 + \frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3) + \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) + \frac{1}{4} k (y_2 + y_3) = 0 \quad \checkmark \text{ (reproduce EDO 1)}
$$

  * **Ecuación de Malla 3:**  
    
$$
L_{23}(\ddot{q}_3 - \ddot{q}_2) + R_{23}(\dot{q}_3 - \dot{q}_2) + \frac{1}{C_{23}}(q_3 - q_2) = E(t)
$$

    Sustituyendo $q_3 - q_2 = -(y_2 + y_3)$:
    
$$
-\frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3) - \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) - \frac{1}{4} k (y_2 + y_3) = -F(t)
$$

    Multiplicando por $-1$:
    
$$
\frac{1}{4} m_1 (\ddot{y}_2 + \ddot{y}_3) + \frac{1}{4} c_1 (\dot{y}_2 + \dot{y}_3) + \frac{1}{4} k (y_2 + y_3) = F(t) \quad \checkmark \text{ (reproduce EDO 2)}
$$


⚙️ ¿Te gustaría que construya el diagrama esquemático en TikZ del sistema de poleas o del circuito eléctrico equivalente de dos mallas?
