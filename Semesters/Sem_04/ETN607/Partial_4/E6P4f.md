# E6P4 — Tetraedro (circuito plano): sistema mecánico y Lagrange

## Enunciado

Hallar el sistema mecánico equivalente del circuito (tetraedro) y plantear las ecuaciones de Lagrange. Se trabaja con el dibujo plano.

**Descripción de la figura**

Nodos A, B, C, D. Circuito plano: un triángulo exterior A-B-C con A arriba, B abajo a la izquierda y C abajo a la derecha, y el nodo D en el centro, unido a A, B y C. La región exterior no es una malla. No hay fuentes.

| Arista               | Elemento en la figura |
| -------------------- | --------------------- |
| B–A (lado izquierdo) | $R_1$                 |
| A–C (lado derecho)   | $L_2$                 |
| B–C (lado de abajo)  | $L_3$                 |
| A–D                  | $R_{12}$              |
| B–D                  | $R_{13}$              |
| D–C                  | $C_{23}$              |

---

## Reglas

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor $C$ = resorte $1/C$, resistencia $R$ = amortiguador, corriente = velocidad, carga = posición.
2. **Grados de libertad:** número de mallas = $N$. Para un circuito conexo, $N = \text{aristas} - \text{nodos} + 1$. La región exterior no es una malla.
3. **Compartidos:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se gira el circuito.
4. **Mallas:** una corriente de malla por malla. Las mallas con inductancia llevan su número ($L_2$ en la malla 2, $L_3$ en la malla 3). La malla sin inductancia es la 1 y es un cuerpo simulado de masa 0, que se conecta igual que cualquier cuerpo. Todas las corrientes van en sentido horario.
5. **Corrientes:** un elemento en una sola malla lleva la corriente de esa malla. Un elemento compartido por dos mallas lleva la diferencia de sus corrientes. Se comprueba con la ley de corrientes de Kirchhoff (LKC) en el nodo D.
6. **Conversión a mecánico:** la corriente de una malla es la velocidad de su cuerpo. Un elemento en una sola malla va entre su cuerpo y la pared fija. Un elemento compartido va entre los dos cuerpos de sus mallas.
7. **Energías:**

$$
T = \sum \frac{L}{2} i^2, \qquad V = \sum \frac{1}{2C}\left(\int i\,dt\right)^2, \qquad P = \sum \frac{R}{2} i^2
$$

   donde $i$ es la corriente de cada elemento.

8. **Ecuación de Lagrange**, una por cada corriente de malla $i_r$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_r}\right) = -\frac{\partial V}{\partial\left(\int i_r\,dt\right)} - \frac{\partial P}{\partial i_r}
$$

   Como $T$ no depende de las cargas, desaparece $\partial T/\partial q$.

---

## Solución por pasos

### Paso 1. Grados de libertad, mallas y compartidos

Aristas: 6 (A–B, A–C, B–C, A–D, B–D, C–D). Nodos: 4.

$$
N = 6 - 4 + 1 = 3 \text{ mallas} \qquad (i_1,\ i_2,\ i_3)
$$

Mallas en sentido horario:

| Malla | Recorrido | Elementos | Inductancia |
|---|---|---|---|
| **1** | A→D→B→A | $R_{12}$, $R_{13}$, $R_1$ | ninguna (cuerpo simulado) |
| **2** | A→C→D→A | $L_2$, $C_{23}$, $R_{12}$ | $L_2$ |
| **3** | B→D→C→B | $R_{13}$, $C_{23}$, $L_3$ | $L_3$ |

| Elemento | Arista | Mallas | ¿Compartido? |
|---|---|---|---|
| $L_2$ | A–C (borde exterior) | 2 | No |
| $L_3$ | B–C (borde exterior) | 3 | No |

**Conclusión:** no hay inductancias ni fuentes compartidas. **No hace falta girar el circuito.**

### Paso 2. Corriente por cada uno de los 6 elementos

Con las tres corrientes de malla en sentido horario:

| Elemento | Arista | Mallas | Corriente |
|---|---|---|---|
| $R_1$ | B→A | 1 | $i_1$ |
| $L_2$ | A→C | 2 | $i_2$ |
| $L_3$ | C→B | 3 | $i_3$ |
| $R_{12}$ | A→D | 1 y 2 | $i_{12} = i_1 - i_2$ |
| $R_{13}$ | B→D | 1 y 3 | $i_{13} = i_3 - i_1$ |
| $C_{23}$ | C→D | 2 y 3 | $i_{23} = i_2 - i_3$ |

Las tres corrientes compartidas se miden hacia el nodo D.

**Comprobación con LKC en el nodo D:**

$$
i_{12} + i_{13} + i_{23} = (i_1 - i_2) + (i_3 - i_1) + (i_2 - i_3) = 0
$$

### Paso 3. Sistema mecánico equivalente

**Cuerpos:**

| Cuerpo | Malla | Masa | Velocidad |
|---|---|---|---|
| 1 | 1 | 0 (simulado) | $v_1 = i_1$ |
| 2 | 2 | $L_2$ | $v_2 = i_2$ |
| 3 | 3 | $L_3$ | $v_3 = i_3$ |

**Fuerzas:** ninguna, porque el circuito no tiene fuentes.

**Elementos y conexiones:**

| Elemento | Se conecta entre | Velocidad relativa |
|---|---|---|
| Amortiguador $R_1$ | cuerpo 1 y pared fija | $v_1$ |
| Amortiguador $R_{12}$ | cuerpos 1 y 2 | $v_1 - v_2$ |
| Amortiguador $R_{13}$ | cuerpos 1 y 3 | $v_3 - v_1$ |
| Resorte $1/C_{23}$ | cuerpos 2 y 3 | $v_2 - v_3$ |

**Conexiones por cuerpo:**

- **Cuerpo 1 (masa 0):** $R_1$ a la pared, $R_{12}$ al cuerpo 2 y $R_{13}$ al cuerpo 3.
- **Cuerpo 2 (masa $L_2$):** $R_{12}$ al cuerpo 1 y $1/C_{23}$ al cuerpo 3.
- **Cuerpo 3 (masa $L_3$):** $R_{13}$ al cuerpo 1 y $1/C_{23}$ al cuerpo 2.

**Pared fija:** solo está unido a ella $R_1$ (cuerpo 1). Las masas $L_2$ y $L_3$ son los cuerpos, no elementos de pared.

**Verificación de los 6 elementos:**

| Grupo | Elementos | Cantidad |
|---|---|---|
| Masas | $L_2$, $L_3$ | 2 |
| A la pared | $R_1$ | 1 |
| Entre cuerpos | $R_{12}$, $R_{13}$, $1/C_{23}$ | 3 |
| **Total** | | **6** |

### Paso 4. Energías $T$, $V$ y $P$

$$
T = \frac{L_2}{2}\,i_2^2 + \frac{L_3}{2}\,i_3^2
$$

$$
V = \frac{1}{2C_{23}}\left(\int (i_2 - i_3)\,dt\right)^2
$$

$$
P = \frac{R_1}{2}\,i_1^2 + \frac{R_{12}}{2}\,(i_1 - i_2)^2 + \frac{R_{13}}{2}\,(i_3 - i_1)^2
$$

### Paso 5. Ecuaciones de Lagrange

**Para $i_1$ (malla 1):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_1}\right) = 0, \qquad \frac{\partial V}{\partial q_1} = 0, \qquad \frac{\partial P}{\partial i_1} = R_1 i_1 + R_{12}(i_1 - i_2) - R_{13}(i_3 - i_1)
$$

$$
0 = -R_1\,i_1 - R_{12}\,(i_1 - i_2) + R_{13}\,(i_3 - i_1)
$$

**Para $i_2$ (malla 2):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_2}\right) = L_2\frac{di_2}{dt}, \qquad \frac{\partial V}{\partial q_2} = \frac{1}{C_{23}}\int (i_2 - i_3)\,dt, \qquad \frac{\partial P}{\partial i_2} = -R_{12}(i_1 - i_2)
$$

$$
L_2\frac{di_2}{dt} = -\frac{1}{C_{23}}\int (i_2 - i_3)\,dt + R_{12}\,(i_1 - i_2)
$$

**Para $i_3$ (malla 3):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_3}\right) = L_3\frac{di_3}{dt}, \qquad \frac{\partial V}{\partial q_3} = -\frac{1}{C_{23}}\int (i_2 - i_3)\,dt, \qquad \frac{\partial P}{\partial i_3} = R_{13}(i_3 - i_1)
$$

$$
L_3\frac{di_3}{dt} = \frac{1}{C_{23}}\int (i_2 - i_3)\,dt - R_{13}\,(i_3 - i_1)
$$
