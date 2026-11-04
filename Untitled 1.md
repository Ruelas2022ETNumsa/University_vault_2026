### 1. Grados de libertad $N$, mallas y tabla de inductancias

* **Número de mallas (grados de libertad):**
  
$$
\text{Aristas} = 6 \text{ (A–B, A–C, B–C, A–D, B–D, C–D)}, \qquad \text{Nodos} = 4
$$

  
$$
N = \text{aristas} - \text{nodos} + 1 = 6 - 4 + 1 = 3 \text{ mallas}
$$


* **Descripción de las 3 mallas interiores (sentido horario):**
  * **Malla 1 (sin inductancia – cuerpo simulado):** Malla superior izquierda (nodos A–B–D–A). Contiene a $R_1$ (A–B), $R_{13}$ (B–D) y $R_{12}$ (D–A).
  * **Malla 2 (con $L_2$):** Malla superior derecha (nodos A–D–C–A). Contiene a $R_{12}$ (A–D), $C_{23}$ (D–C) y $L_2$ (C–A).
  * **Malla 3 (con $L_3$):** Malla inferior (nodos B–C–D–B). Contiene a $L_3$ (B–C), $C_{23}$ (C–D) y $R_{13}$ (D–B).

* **Tabla de inductancias:**

| Elemento | Ubicación / Arista | Mallas que lo contienen | ¿Está compartido? |
| :--- | :--- | :--- | :--- |
| **$L_2$** | A–C (borde exterior derecho) | Solo Malla 2 | **No** |
| **$L_3$** | B–C (borde exterior inferior) | Solo Malla 3 | **No** |

*Conclusión:* Ninguna inductancia está compartida entre dos mallas. **No es necesario girar el circuito.**

---

### 2. Corrientes por cada elemento y verificación con LKC en el nodo D

Asumiendo corrientes de malla $i_1, i_2, i_3$ en sentido horario:

* **Elementos en una sola malla:**
  1. **Resistor $R_1$** (A–B): $i_1$ (de A hacia B)
  2. **Inductancia $L_2$** (A–C): $i_2$ (de C hacia A)
  3. **Inductancia $L_3$** (B–C): $i_3$ (de B hacia C)

* **Elementos compartidos (medidos hacia el nodo D):**
  4. **Resistor $R_{12}$** (A–D): La Malla 2 va de A a D ($+i_2$) y la Malla 1 va de D a A ($-i_1$).  
     
$$
i_{A\text{–}D} = i_2 - i_1
$$

  5. **Resistor $R_{13}$** (B–D): La Malla 1 va de B a D ($+i_1$) y la Malla 3 va de D a B ($-i_3$).  
     
$$
i_{B\text{–}D} = i_1 - i_3
$$

  6. **Capacitor $C_{23}$** (C–D): La Malla 3 va de C a D ($+i_3$) y la Malla 2 va de D a C ($-i_2$).  
     
$$
i_{C\text{–}D} = i_3 - i_2
$$


* **Comprobación con LKC en el nodo D:**
  
$$
\sum i_{\text{hacia D}} = i_{A\text{–}D} + i_{B\text{–}D} + i_{C\text{–}D} = (i_2 - i_1) + (i_1 - i_3) + (i_3 - i_2) = 0
$$

  *(Se verifica exactamente 0).*

---

### 3. Sistema mecánico equivalente

#### A. Cuerpos (masas) y Fuerzas
* **Cuerpo 1 (Malla 1):** Masa simulada $m_1 = 0$ (sin inductancia), velocidad $v_1 = i_1$.
* **Cuerpo 2 (Malla 2):** Masa real $m_2 = L_2$, velocidad $v_2 = i_2$.
* **Cuerpo 3 (Malla 3):** Masa real $m_3 = L_3$, velocidad $v_3 = i_3$.
* **Fuerzas:** No existen fuentes en el circuito, por lo que $F_1 = F_2 = F_3 = 0$.

#### B. Conexiones de cada elemento
1. **A la pared fija ($v = 0$):**
   * **Amortiguador $c_1 = R_1$:** Entre el **Cuerpo 1** y la pared fija (corriente $i_1$).
   * **Masa $m_2 = L_2$:** Masa del **Cuerpo 2**.
   * **Masa $m_3 = L_3$:** Masa del **Cuerpo 3**.

2. **Entre cuerpos:**
   * **Amortiguador $c_{12} = R_{12}$:** Entre **Cuerpo 1** y **Cuerpo 2** (velocidad relativa $v_1 - v_2$).
   * **Amortiguador $c_{13} = R_{13}$:** Entre **Cuerpo 1** y **Cuerpo 3** (velocidad relativa $v_1 - v_3$).
   * **Resorte $k_{23} = 1/C_{23}$:** Entre **Cuerpo 2** y **Cuerpo 3** (velocidad relativa $v_2 - v_3$).

#### C. Verificación de representación (6 elementos)
* 1 amortiguador a pared ($R_1$), 2 masas ($L_2, L_3$), 2 amortiguadores entre cuerpos ($R_{12}, R_{13}$) y 1 resorte entre cuerpos ($C_{23}$).  
* **Total:** $1 + 2 + 2 + 1 = 6\text{ elementos representados}$.

---

### 4. Energías $T$, $V$ y $P$

Definiendo la carga de malla $q_r = \int i_r\, dt$:

* **Energía Cinética ($T$):**
  
$$
T = \frac{1}{2} L_2 i_2^2 + \frac{1}{2} L_3 i_3^2
$$


* **Energía Potencial ($V$):**
  
$$
V = \frac{1}{2 C_{23}} \left( \int i_2\, dt - \int i_3\, dt \right)^2 = \frac{1}{2 C_{23}} (q_2 - q_3)^2
$$


* **Función de Disipación de Rayleigh ($P$):**
  
$$
P = \frac{1}{2} R_1 i_1^2 + \frac{1}{2} R_{12} (i_1 - i_2)^2 + \frac{1}{2} R_{13} (i_1 - i_3)^2
$$


---

### 5. Ecuaciones de Lagrange

Aplicando $\frac{d}{dt}\left(\frac{\partial T}{\partial i_r}\right) + \frac{\partial P}{\partial i_r} + \frac{\partial V}{\partial q_r} = 0$:

1. **Para $i_1$ (Malla 1):**
   
$$
\frac{d}{dt}(0) + \left[ R_1 i_1 + R_{12} (i_1 - i_2) + R_{13} (i_1 - i_3) \right] + 0 = 0
$$

   
$$
(R_1 + R_{12} + R_{13}) i_1 - R_{12} i_2 - R_{13} i_3 = 0
$$


2. **Para $i_2$ (Malla 2):**
   
$$
L_2 \frac{di_2}{dt} - R_{12} (i_1 - i_2) + \frac{1}{C_{23}} \left( \int i_2\, dt - \int i_3\, dt \right) = 0
$$

   
$$
L_2 \frac{di_2}{dt} - R_{12} i_1 + R_{12} i_2 + \frac{1}{C_{23}} \int i_2\, dt - \frac{1}{C_{23}} \int i_3\, dt = 0
$$


3. **Para $i_3$ (Malla 3):**
   
$$
L_3 \frac{di_3}{dt} - R_{13} (i_1 - i_3) - \frac{1}{C_{23}} \left( \int i_2\, dt - \int i_3\, dt \right) = 0
$$

   
$$
L_3 \frac{di_3}{dt} - R_{13} i_1 + R_{13} i_3 - \frac{1}{C_{23}} \int i_2\, dt + \frac{1}{C_{23}} \int i_3\, dt = 0
$$


⚙️ ¿Deseas que genere el código TikZ para graficar el diagrama del circuito plano o el esquema de las masas conectadas?
