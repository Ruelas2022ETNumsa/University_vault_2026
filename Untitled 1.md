### 1. Circuito original, giro y mallas del girado

* **Grados de libertad ($N$):**
  * **Nodos:** 7 $A, B, C, D, E, F, G$.
  * **Aristas:** 9 ($R_1, C_2, E, R_{23}, L_3, R_{13}, C_{13}, C_1$ y el cable F–E).
  * $N = 9 - 7 + 1 = 3 \text{ mallas}$.

* **Mallas del circuito original y tabla de compartidos:**
  * Malla 1 (izquierda): A–B–G–E–F–A. Contiene $E$ y $L_3$.
  * Malla 2 (derecha-superior): B–C–G–B. Contiene $E$.
  * Malla 3 (derecha-inferior): G–C–D–E–G. Contiene $L_3$.

  | Elemento | Ubicación | Mallas que lo contienen | ¿Está compartido? |
  | :--- | :--- | :--- | :--- |
  | **Fuente $E$** | B–G | Malla 1 y Malla 2 | **Sí** |
  | **Inductancia $L_3$** | G–E | Malla 1 y Malla 3 | **Sí** |

  **Determinación:** SÍ se debe girar el circuito porque la fuente $E$ y la inductancia $L_3$ están compartidas entre mallas.

* **Cara exterior elegida para el circuito girado:**
  * Se elige la cara **A–B–G–E–F–A** como nueva cara exterior.
  * Al exteriorizarla, las aristas B–G (fuente $E$) y G–E (inductancia $L_3$) forman parte del perímetro exterior y pasan a pertenecer a una sola malla interior cada una.

* **Las 3 mallas del circuito girado:**
  * **Malla 1 (sin inductancia ni fuente – cuerpo simulado):** Malla interiorizada (A–B–C–D–E–F–A). Elementos: $R_1$ (A–B), $C_1$ (A–F), cable (F–E), $C_{12}$ (B–C, renombrado de $C_2$), $C_{13}$ (C–D) y $R_{13}$ (E–D).
  * **Malla 2 (con Fuente $E$):** Triángulo superior (B–C–G–B). Elementos: Fuente $E$ (B–G), $C_{12}$ (B–C) y $R_{23}$ (G–C).
  * **Malla 3 (con $L_3$):** Cuadrilátero inferior (G–C–D–E–G). Elementos: Inductancia $L_3$ (G–E), $R_{23}$ (G–C), $C_{13}$ (C–D) y $R_{13}$ (E–D).

  **Tabla del circuito girado:**
  | Elemento | Ubicación | Mallas que lo contienen | ¿Está compartido? |
  | :--- | :--- | :--- | :--- |
  | **Fuente $E$** | B–G | Solo Malla 2 | **No** |
  | **Inductancia $L_3$** | G–E | Solo Malla 3 | **No** |

---

### 2. Corriente por cada uno de los 8 elementos y comprobación con LKC

Tomando corrientes de malla $i_1, i_2, i_3$ en sentido horario:

1. **Resistor $R_1$** (A–B): $i_1$
2. **Capacitor $C_1$** (A–F): $i_1$
3. **Fuente $E$** (B–G): $i_2$
4. **Inductancia $L_3$** (G–E): $i_3$
5. **Capacitor $C_{12}$** (B–C): $i_1 - i_2$
6. **Capacitor $C_{13}$** (C–D): $i_1 - i_3$
7. **Resistor $R_{13}$** (E–D): $i_1 - i_3$
8. **Resistor $R_{23}$** (G–C): $i_3 - i_2$

**Comprobación con Ley de Corrientes de Kirchhoff $LKC$:**
* **Nodo B:**  
  Entra $i_1$ (por A–B). Salen $i_2$ (por B–G) e $(i_1 - i_2)$ (por B–C).  
  
$$
\sum i_{\text{entra}} - \sum i_{\text{sale}} = i_1 - \left[ i_2 + (i_1 - i_2) \right] = i_1 - i_1 = 0 \quad \checkmark
$$

* **Nodo E:**  
  Entra $i_1$ (por F–E). Salen $i_3$ (por E–G) e $(i_1 - i_3)$ (por E–D).  
  
$$
\sum i_{\text{entra}} - \sum i_{\text{sale}} = i_1 - \left[ i_3 + (i_1 - i_3) \right] = i_1 - i_1 = 0 \quad \checkmark
$$


---

### 3. Sistema mecánico equivalente

#### A. Cuerpos (masas) y Fuerzas
* **Cuerpo 1 (Malla 1):** Masa simulada $m_1 = 0$, velocidad $v_1 = i_1$.
* **Cuerpo 2 (Malla 2):** Masa simulada $m_2 = 0$, velocidad $v_2 = i_2$.
* **Cuerpo 3 (Malla 3):** Masa real $m_3 = L_3$, velocidad $v_3 = i_3$.
* **Fuerza:** Fuerza $F_2 = E$ aplicada sobre el **Cuerpo 2**.

#### B. Conexiones de cada elemento
1. **A la pared fija ($v = 0$):**
   * **Amortiguador $c_1 = R_1$** y **Resorte $k_1 = 1/C_1$** en paralelo: Conectados entre el **Cuerpo 1** y la pared fija.
   * **Fuerza $F_2 = E$:** Actúa sobre el **Cuerpo 2**.
   * **Masa $m_3 = L_3$:** Masa del **Cuerpo 3**.
2. **Entre cuerpos:**
   * **Resorte $k_{12} = 1/C_{12}$:** Entre el **Cuerpo 1** y el **Cuerpo 2** (velocidad relativa $v_1 - v_2$).
   * **Resorte $k_{13} = 1/C_{13}$** y **Amortiguador $c_{13} = R_{13}$** en paralelo: Entre el **Cuerpo 1** y el **Cuerpo 3** (velocidad relativa $v_1 - v_3$).
   * **Amortiguador $c_{23} = R_{23}$:** Entre el **Cuerpo 2** y el **Cuerpo 3** (velocidad relativa $v_3 - v_2$).

#### C. Verificación de representación (8 elementos)
* **A pared / Masa / Fuerza:** $R_1$ (c1), $C_1$ (k1), $E$ (F2), $L_3$ (m3).
* **Entre cuerpos:** $C_{12}$ (k12), $C_{13}$ (k13), $R_{13}$ (c13), $R_{23}$ (c23).
* **Total:** $4 + 4 = 8\text{ elementos representados}$.

---

### 4. Energías $T$, $V$ y $P$

Definiendo $q_r = \int i_r\, dt$:

* **Energía Cinética ($T$):**
  
$$
T = \frac{1}{2} L_3 i_3^2
$$


* **Energía Potencial ($V$):**
  
$$
V = \frac{1}{2 C_1} \left(\int i_1\, dt\right)^2 + \frac{1}{2 C_{12}} \left(\int i_1\, dt - \int i_2\, dt\right)^2 + \frac{1}{2 C_{13}} \left(\int i_1\, dt - \int i_3\, dt\right)^2 + E \int i_2\, dt
$$


* **Función de Disipación de Rayleigh ($P$):**
  
$$
P = \frac{1}{2} R_1 i_1^2 + \frac{1}{2} R_{13} (i_1 - i_3)^2 + \frac{1}{2} R_{23} (i_3 - i_2)^2
$$


---

### 5. Las tres ecuaciones de Lagrange

Aplicando $\frac{d}{dt}\left(\frac{\partial T}{\partial i_r}\right) = -\frac{\partial V}{\partial q_r} - \frac{\partial P}{\partial i_r}$ con $q_r = \int i_r\, dt$:

1. **Para $i_1$ (Malla 1):**
   
$$
(R_1 + R_{13}) i_1 - R_{13} i_3 + \left(\frac{1}{C_1} + \frac{1}{C_{12}} + \frac{1}{C_{13}}\right) \int i_1\, dt - \frac{1}{C_{12}} \int i_2\, dt - \frac{1}{C_{13}} \int i_3\, dt = 0
$$


2. **Para $i_2$ (Malla 2):**
   
$$
R_{23} i_2 - R_{23} i_3 - \frac{1}{C_{12}} \int i_1\, dt + \frac{1}{C_{12}} \int i_2\, dt = -E
$$


3. **Para $i_3$ (Malla 3):**
   
$$
L_3 \frac{di_3}{dt} - R_{13} i_1 - R_{23} i_2 + (R_{13} + R_{23}) i_3 - \frac{1}{C_{13}} \int i_1\, dt + \frac{1}{C_{13}} \int i_3\, dt = 0
$$


⚙️ ¿Quieres que elabore un diagrama en TikZ del circuito girado o del modelo mecánico de masas conectadas?
