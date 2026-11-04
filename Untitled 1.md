### 1. Mallas y tabla de inductancias y fuentes compartidas (circuito original)

El circuito posee **3 mallas independientes** ($N = 3$ grados de libertad):
- **Malla 1:** Malla exterior/izquierda, formada por la fuente $E_1$ y $R_1$ en P–Q, el cable Q–D, la rama B–D ($L_{13}, E_{13}$), la rama A–B ($L_{12}$) y la rama principal P–A ($L_1$).
- **Malla 2:** Triángulo superior del rombo (A–B–C–A), formado por $L_{12}$ (A–B), $C_{23}$ y $R_{23}$ (B–C) y $C_2$ (A–C).
- **Malla 3:** Triángulo inferior del rombo (B–C–D–B), formado por $C_{23}$ y $R_{23}$ (B–C), $R_3$ (C–D) y $L_{13}, E_{13}$ (B–D).

**Tabla de inductancias y fuentes (circuito original):**

| Elemento | Ubicación / Rama | Mallas que lo contienen | ¿Está compartido? |
| :--- | :--- | :--- | :--- |
| **$L_1$** | Rama principal (P–A) | Malla 1 | No |
| **$E_1$** | Rama de la fuente (P–Q) | Malla 1 | No |
| **$L_{12}$** | Lado izquierdo superior (A–B) | Malla 1 y Malla 2 | **Sí** |
| **$L_{13}$** | Lado izquierdo inferior (B–D) | Malla 1 y Malla 3 | **Sí** |
| **$E_{13}$** | Lado izquierdo inferior (B–D) | Malla 1 y Malla 3 | **Sí** |

**Determinación:** Dado que $L_{12}$, $L_{13}$ y $E_{13}$ están compartidos entre la Malla 1 y las mallas del rombo, según la Regla 3, **SÍ SE DEBE GIRAR EL CIRCUITO** (reflejar el rombo de izquierda a derecha, manteniendo A arriba y D abajo).

---

### 2. Descripción del circuito después de girar y revisión de compartidos

Al reflejar el rombo de izquierda a derecha (A arriba, D abajo):
- El nodo A permanece arriba y D abajo. El vértice izquierdo que toca a la Malla 1 pasa a ser el nodo C y el vértice derecho exterior pasa a ser el nodo B.

**Descripción de las ramas del circuito girado:**
- **Circuito exterior (Malla 1):**
  - Rama P–Q: Fuente $E_1$ en serie con la resistencia $R_1$.
  - Rama P–A: Inductancia $L_1$.
  - Rama Q–D: Cable.
- **Lado izquierdo del rombo (toca a la Malla 1):**
  - Rama A–C (arriba a la izquierda): Capacitor $C_2$.
  - Rama C–D (abajo a la izquierda): Resistor $R_3$.
- **Lado derecho del rombo (exterior a la derecha):**
  - Rama A–B (arriba a la derecha): Inductancia $L_{12}$.
  - Rama B–D (abajo a la derecha): Inductancia $L_{13}$ en serie con la fuente $E_{13}$ (junto a D).
- **Rama central del rombo:**
  - Rama C–B (horizontal central): Capacitor $C_{23}$ (lado C) en serie con resistor $R_{23}$ (lado B).

**Tabla de inductancias y fuentes (circuito girado):**

| Elemento | Ubicación / Rama | Mallas que lo contienen | ¿Está compartido? |
| :--- | :--- | :--- | :--- |
| **$L_1$** | Rama principal (P–A) | Malla 1 | No |
| **$E_1$** | Rama P–Q | Malla 1 | No |
| **$L_{12}$** | Rama A–B (derecha superior) | Malla 2 | No |
| **$L_{13}$** | Rama B–D (derecha inferior) | Malla 3 | No |
| **$E_{13}$** | Rama B–D (derecha inferior) | Malla 3 | No |

**Revisión:** En el circuito girado ninguna inductancia ni fuente está compartida entre dos mallas.

---

### 3. Corrientes de cada elemento y verificación por nodo

Aplicando la Regla 4:
- **Rama principal (P–A):** Corriente $i_1$ (de P hacia A).
- **Lado izquierdo del rombo (toca a la Malla 1):**
  - Rama A–C: Corriente $i_2$ (de A hacia C).
  - Rama C–D: Corriente $i_3$ (de C hacia D).

**Cálculo del resto de corrientes por Ley de Corrientes de Kirchhoff $LCK$:**
- **Nodo A:** Entra $i_1$, sale $i_2$ hacia C. Por la rama A–B sale $i_{AB} = i_1 - i_2$.
- **Nodo C:** Entra $i_2$, sale $i_3$ hacia D. Por la rama central C–B sale $i_{CB} = i_2 - i_3$.
- **Nodo B:** Entran $i_{AB} = i_1 - i_2$ e $i_{CB} = i_2 - i_3$. Por la rama B–D sale $i_{BD} = (i_1 - i_2) + (i_2 - i_3) = i_1 - i_3$.

**Resumen de corrientes por elemento:**
- **Fuente $E_1$ y Resistencia $R_1$:** Corriente $i_1$
- **Inductancia $L_1$:** Corriente $i_1$
- **Capacitor $C_2$:** Corriente $i_2$
- **Resistor $R_3$:** Corriente $i_3$
- **Inductancia $L_{12}$:** Corriente $i_1 - i_2$
- **Capacitor $C_{23}$ y Resistor $R_{23}$ (serie):** Corriente $i_2 - i_3$
- **Inductancia $L_{13}$ y Fuente $E_{13}$ (serie):** Corriente $i_1 - i_3$

**Verificación en el Nodo D:**
- Entran $i_3$ (por C–D) y $(i_1 - i_3)$ (por B–D).
- Suma total que entra a D: $i_3 + (i_1 - i_3) = i_1$.
- Coincide con la corriente $i_1$ que retorna por el cable Q–D hacia la fuente/resistencia $R_1$ ($i_{\text{entra}} = i_{\text{sale}} = i_1$).

---

### 4. Sistema mecánico equivalente

Aplicando la analogía de voltajes (inductancia = masa, fuente = fuerza, capacitor $C = \text{resorte } 1/C$, resistencia $R = \text{amortiguador } c$, corriente = velocidad):

**Velocidad de cada cuerpo (3 masas):**
- **Cuerpo 1 (masa $m_1 = L_1$):** Velocidad $v_1 = i_1$.
- **Cuerpo 2 (masa $m_2 = L_{12}$):** Velocidad $v_2 = i_1 - i_2$.
- **Cuerpo 3 (masa $m_3 = L_{13}$):** Velocidad $v_3 = i_1 - i_3$.

**Fuerzas aplicadas:**
- **Fuerza $F_1 = E_1$:** Actúa sobre el **Cuerpo 1** (asociada a $i_1$).
- **Fuerza $F_{13} = E_{13}$:** Actúa sobre el **Cuerpo 3** (asociada a $i_1 - i_3$).

**Conexiones de cada cuerpo (Reglas 5 y 6):**
- **Pared fija (referencia $v = 0$):**
  - **Amortiguador $c_1 = R_1$:** Conectado entre la pared fija y el **Cuerpo 1** (lleva la corriente única $i_1 = v_1$).
- **Cuerpo 1 ($m_1 = L_1$, velocidad $v_1$):**
  - **A la izquierda:** Conectado a la pared fija mediante el amortiguador $c_1 = R_1$ y sujeto a la fuerza aplicada $F_1 = E_1$.
  - **A la derecha hacia el Cuerpo 2:** Conectado al **Cuerpo 2** mediante el **resorte $k_2 = 1/C_2$** (lleva la corriente $i_2 = v_1 - v_2$).
  - **A la derecha hacia el Cuerpo 3:** Conectado al **Cuerpo 3** mediante el **amortiguador $c_3 = R_3$** (lleva la corriente $i_3 = v_1 - v_3$).
- **Cuerpo 2 ($m_2 = L_{12}$, velocidad $v_2$):**
  - **A la izquierda (desde Cuerpo 1):** Conectado al **Cuerpo 1** mediante el **resorte $k_2 = 1/C_2$**.
  - **A la derecha hacia el Cuerpo 3:** Conectado al **Cuerpo 3** mediante la combinación en paralelo (Regla 6) del **resorte $k_{23} = 1/C_{23}$** y el **amortiguador $c_{23} = R_{23}$** (llevan la corriente $i_2 - i_3 = v_3 - v_2$).
- **Cuerpo 3 ($m_3 = L_{13}$, velocidad $v_3$):**
  - **A la izquierda (desde Cuerpo 1):** Conectado al **Cuerpo 1** mediante el **amortiguador $c_3 = R_3$**.
  - **A la izquierda (desde Cuerpo 2):** Conectado al **Cuerpo 2** mediante el conjunto en paralelo del **resorte $k_{23} = 1/C_{23}$** y el **amortiguador $c_{23} = R_{23}$**.
  - **Fuerza aplicada:** Recibe la fuerza $F_{13} = E_{13}$ actuando sobre su masa.

⚙️ ¿Te gustaría que elabore el diagrama esquemático en TikZ del circuito girado o del sistema mecánico resultante?
