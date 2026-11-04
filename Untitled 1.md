### 1. Grados de libertad $N$, ligadura y relación de velocidades

* **Número de grados de libertad:**  
  
$$
\text{Nodos/Cuerpos} = 2 \text{ (polea 1 y polea 2)}, \qquad \text{Ligaduras} = 1 \text{ (cuerda de longitud } l \text{)}
$$

  
$$
N = 2 - 1 = 1 \quad \rightarrow \quad \text{Coordenada generalizada: } q = y_1
$$


* **Ecuación de ligadura de la cuerda:**  
  
$$
(H - y_1) + \pi R_1 + (y_2 - y_1) = l \implies H + \pi R_1 + y_2 - 2y_1 = l
$$

  Medida como desviación respecto al equilibrio (Regla 3):
  
$$
y_2 - 2y_1 = 0 \implies y_2 = 2y_1
$$


* **Relación de velocidades (derivada de la ligadura):**  
  
$$
\dot{y}_2 = 2\dot{y}_1
$$


---

### 2. $T$, $V$ y $P$ en función de $y_1$ y $\dot{y}_1$

* **Energía Cinética ($T$):**  
  
$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 (2\dot{y}_1)^2 = \frac{1}{2} (m_1 + 4m_2) \dot{y}_1^2
$$


* **Energía Potencial ($V$):**  
  * Resorte $k_1$: estiramiento $y_1$.  
  * Resorte $k_2$: rodea la polea 2 y baja al piso en dos tramos de longitud $(H - y_2)$; al bajar la polea una distancia $y_2$, ambos tramos se acortan $y_2$, por lo que su deformación total es $2y_2 = 4y_1$.
  
$$
V = \frac{1}{2} k_1 y_1^2 + \frac{1}{2} k_2 (2y_2)^2 = \frac{1}{2} k_1 y_1^2 + \frac{1}{2} k_2 (4y_1)^2 = \frac{1}{2} (k_1 + 16k_2) y_1^2
$$


* **Función de Disipación de Rayleigh ($P$):**  
  * Amortiguador $c_1$: actúa con velocidad $\dot{y}_1$.  
  * Amortiguador $c_2$: actúa con velocidad $\dot{y}_2 = 2\dot{y}_1$.
  
$$
P = \frac{1}{2} c_1 \dot{y}_1^2 + \frac{1}{2} c_2 \dot{y}_2^2 = \frac{1}{2} c_1 \dot{y}_1^2 + \frac{1}{2} c_2 (2\dot{y}_1)^2 = \frac{1}{2} (c_1 + 4c_2) \dot{y}_1^2
$$


---

### 3. Ecuación de Lagrange y EDO final

* **Fuerza generalizada ($Q$):**  
  Dado que $F(t)$ actúa sobre la polea 2 (en sentido positivo de $y_2$):
  
$$
Q = F(t) \cdot \frac{\partial y_2}{\partial y_1} = F(t) \cdot 2 = 2 F(t)
$$


* **Derivadas para la ecuación de Lagrange ($q = y_1$):**  
  
$$
\frac{\partial T}{\partial \dot{y}_1} = (m_1 + 4m_2) \dot{y}_1 \implies \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) = (m_1 + 4m_2) \ddot{y}_1
$$

  
$$
\frac{\partial T}{\partial y_1} = 0, \qquad \frac{\partial V}{\partial y_1} = (k_1 + 16k_2) y_1, \qquad \frac{\partial P}{\partial \dot{y}_1} = (c_1 + 4c_2) \dot{y}_1
$$


* **Sustitución en Lagrange:**  
  
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) - \frac{\partial T}{\partial y_1} = -\frac{\partial V}{\partial y_1} - \frac{\partial P}{\partial \dot{y}_1} + Q
$$

  
$$
(m_1 + 4m_2) \ddot{y}_1 = -(k_1 + 16k_2) y_1 - (c_1 + 4c_2) \dot{y}_1 + 2F(t)
$$


* **EDO final ordenada:**  
  
$$
(m_1 + 4m_2) \ddot{y}_1 + (c_1 + 4c_2) \dot{y}_1 + (k_1 + 16k_2) y_1 = 2F(t)
$$


---

### 4. Circuito eléctrico equivalente

Aplicando la analogía de voltajes e identificando los coeficientes con la forma $L \ddot{q} + R \dot{q} + \frac{1}{C} q = E(t)$:

* **Malla:** Circuito de **una sola malla en serie**.
* **Inductancia total ($L$):**  
  
$$
L = m_1 + 4m_2
$$

* **Resistencia total ($R$):**  
  
$$
R = c_1 + 4c_2
$$

* **Capacitancia total ($C$):**  
  
$$
\frac{1}{C} = k_1 + 16k_2 \implies C = \frac{1}{k_1 + 16k_2}
$$

* **Fuente de voltaje ($E(t)$):**  
  
$$
E(t) = 2F(t)
$$

* **Corriente de malla y sentido:**  
  La corriente de la malla es $i(t) = \dot{y}_1$. El sentido de la corriente coincide con la polaridad de la fuente que impulsa el flujo de carga $q = y_1$ en sentido positivo.

⚙️ ¿Deseas que elabore el esquema en TikZ del circuito $RLC$ equivalente o del diagrama de poleas?
