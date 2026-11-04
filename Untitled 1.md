### 1. Cara exterior elegida y las 5 mallas

El circuito es conexo y tiene 8 nodos y 12 aristas, por lo que posee:

$$
\text{Grados de libertad } N = 12 - 8 + 1 = 5 \text{ mallas}
$$


- **Cara exterior elegida:** Cara **EFGH** (al elegirla como cara exterior, no es una malla interior y sus elementos forman el perímetro exterior).
- **Mallas (5 mallas interiores):**
  - **Malla 1 (Cara ABCD - sin inductancia):** Aristas A–B ($R_{ab}$), B–C ($R_{bc}$), C–D ($R_{cd}$) y D–A ($R_{ad}$).
  - **Malla 2 (Cara ABFE - sin inductancia):** Aristas A–B ($R_{ab}$), B–F ($C_{bf}$), F–E ($R_{ef}$) y E–A ($R_{ae}$).
  - **Malla 3 (Cara BCGF - con inductancia $L_3$):** Aristas B–C ($R_{bc}$), C–G ($R_{cg}$), G–F ($L_3$) y F–B ($C_{bf}$).
  - **Malla 4 (Cara CDHG - con inductancia $L_4$):** Aristas C–D ($R_{cd}$), D–H ($C_{dh}$), H–G ($L_4$) y G–C ($R_{cg}$).
  - **Malla 5 (Cara DAEH - con inductancia $L_5$ y fuente $S$):** Aristas D–A ($R_{ad}$), A–E ($R_{ae}$), E–H ($L_5$ en serie con $S$) y H–D ($C_{dh}$).

---

### 2. Tabla de inductancias y fuentes y revisión de compartidos

| Elemento | Ubicación / Arista | Mallas que lo contienen | ¿Está compartido entre mallas? |
| :--- | :--- | :--- | :--- |
| **$L_3$** | F–G | Solo Malla 3 | **No** |
| **$L_4$** | G–H | Solo Malla 4 | **No** |
| **$L_5$** | E–H | Solo Malla 5 | **No** |
| **Fuente $S$** | E–H (en serie con $L_5$) | Solo Malla 5 | **No** |

*Conclusión:* Al elegir la cara **EFGH** como cara exterior, **ninguna inductancia ni fuente está compartida** entre mallas. No se requiere girar el cubo.

---

### 3. Corriente por cada uno de los 12 elementos

- **Elementos en una sola malla (perímetro exterior EFGH):**
  1. **Resistor $R_{ef}$** (Arista E–F): Malla 2 $\rightarrow i_2$
  2. **Inductancia $L_3$** (Arista F–G): Malla 3 $\rightarrow i_3$
  3. **Inductancia $L_4$** (Arista G–H): Malla 4 $\rightarrow i_4$
  4. **Inductancia $L_5$ y Fuente $S$** (Arista E–H): Malla 5 $\rightarrow i_5$

- **Elementos compartidos entre dos mallas:**
  5. **Resistor $R_{ab}$** (Arista A–B): Compartido por Malla 1 y Malla 2 $\rightarrow i_1 - i_2$
  6. **Resistor $R_{bc}$** (Arista B–C): Compartido por Malla 1 y Malla 3 $\rightarrow i_1 - i_3$
  7. **Resistor $R_{cd}$** (Arista C–D): Compartido por Malla 1 y Malla 4 $\rightarrow i_1 - i_4$
  8. **Resistor $R_{ad}$** (Arista D–A): Compartido por Malla 1 y Malla 5 $\rightarrow i_1 - i_5$
  9. **Capacitor $C_{bf}$** (Arista B–F): Compartido por Malla 2 y Malla 3 $\rightarrow i_2 - i_3$
  10. **Resistor $R_{cg}$** (Arista C–G): Compartido por Malla 3 y Malla 4 $\rightarrow i_3 - i_4$
  11. **Capacitor $C_{dh}$** (Arista D–H): Compartido por Malla 4 y Malla 5 $\rightarrow i_4 - i_5$
  12. **Resistor $R_{ae}$** (Arista A–E): Compartido por Malla 2 y Malla 5 $\rightarrow i_2 - i_5$

---

### 4. Sistema mecánico equivalente

#### A. Cuerpos (masas) y Fuerzas
- **Cuerpo 1 (Malla 1):** Masa simulada $m_1 = 0$, velocidad $v_1 = i_1$.
- **Cuerpo 2 (Malla 2):** Masa simulada $m_2 = 0$, velocidad $v_2 = i_2$.
- **Cuerpo 3 (Malla 3):** Masa real $m_3 = L_3$, velocidad $v_3 = i_3$.
- **Cuerpo 4 (Malla 4):** Masa real $m_4 = L_4$, velocidad $v_4 = i_4$.
- **Cuerpo 5 (Malla 5):** Masa real $m_5 = L_5$, velocidad $v_5 = i_5$.
- **Fuerzas:** Fuerza $F_5 = S$ aplicada directamente sobre el **Cuerpo 5**.

#### B. Conexiones de cada elemento

1. **A la pared fija ($v = 0$):**
   - **Amortiguador $c_{ef} = R_{ef}$** (Arista E–F): Conectado entre la pared fija y el **Cuerpo 2** ($v_2$).
   - **Masa $m_3 = L_3$** (Arista F–G): Masa del **Cuerpo 3** ($v_3$).
   - **Masa $m_4 = L_4$** (Arista G–H): Masa del **Cuerpo 4** ($v_4$).
   - **Masa $m_5 = L_5$** y **Fuerza $F_5 = S$** (Arista E–H): Masa del **Cuerpo 5** ($v_5$) con fuerza aplicada $F_5$.

2. **Entre cuerpos:**
   - **Amortiguador $c_{ab} = R_{ab}$** (Arista A–B): Entre **Cuerpo 1** y **Cuerpo 2** ($v_1 - v_2$).
   - **Amortiguador $c_{bc} = R_{bc}$** (Arista B–C): Entre **Cuerpo 1** y **Cuerpo 3** ($v_1 - v_3$).
   - **Amortiguador $c_{cd} = R_{cd}$** (Arista C–D): Entre **Cuerpo 1** y **Cuerpo 4** ($v_1 - v_4$).
   - **Amortiguador $c_{ad} = R_{ad}$** (Arista D–A): Entre **Cuerpo 1** y **Cuerpo 5** ($v_1 - v_5$).
   - **Resorte $k_{bf} = 1/C_{bf}$** (Arista B–F): Entre **Cuerpo 2** y **Cuerpo 3** ($v_2 - v_3$).
   - **Amortiguador $c_{cg} = R_{cg}$** (Arista C–G): Entre **Cuerpo 3** y **Cuerpo 4** ($v_3 - v_4$).
   - **Resorte $k_{dh} = 1/C_{dh}$** (Arista D–H): Entre **Cuerpo 4** y **Cuerpo 5** ($v_4 - v_5$).
   - **Amortiguador $c_{ae} = R_{ae}$** (Arista A–E): Entre **Cuerpo 2** y **Cuerpo 5** ($v_2 - v_5$).

#### C. Verificación de las 12 aristas
- **4 aristas exteriores (a pared / masas individuales):** E–F ($R_{ef}$), F–G ($L_3$), G–H ($L_4$), E–H ($L_5 + S$).
- **4 aristas de la cara superior ABCD (entre Cuerpo 1 y Cuerpos 2, 3, 4, 5):** A–B ($R_{ab}$), B–C ($R_{bc}$), C–D ($R_{cd}$), D–A ($R_{ad}$).
- **4 aristas verticales (entre masas adyacentes):** B–F ($C_{bf}$), C–G ($R_{cg}$), D–H ($C_{dh}$), A–E ($R_{ae}$).
- **Total:** $4 + 4 + 4 = 12\text{ aristas representadas}$.

⚙️ ¿Te gustaría que dibuje el diagrama esquemático en TikZ del circuito desplegado o del sistema mecánico de 5 cuerpos resultante?
