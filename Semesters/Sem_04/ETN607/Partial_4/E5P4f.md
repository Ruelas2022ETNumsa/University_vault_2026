# E5P4 — Circuito de 3 mallas: sistema mecánico y Lagrange

## Enunciado

Hallar el sistema mecánico equivalente del circuito y plantear las ecuaciones de Lagrange.

**Descripción de la figura**

Nodos A a H. Las fuentes son círculos. El circuito es plano: el lado izquierdo es la fuente, arriba van A-B-C, a la derecha C-D-E, abajo E-F-G, y el nodo H es el centro, unido a B, D y F.

- **A–B:** resistor $R_1$.
- **B–C:** inductancia $L_2$.
- **C–D:** capacitor $C_2$.
- **D–E:** cable.
- **E–F:** inductancia $L_3$.
- **F–G:** resistor $2R_1$.
- **G–A:** fuente $E_1$ (lado izquierdo, sin polaridad marcada).
- **B–H:** resistor $R_{12}$.
- **H–D:** resistor $R_{23}$.
- **H–F:** capacitor $C_{13}$.

> Observaciones sobre la hoja del docente:
> - En su dibujo mecánico el resorte entre el cuerpo 1 y $L_3$ no tiene etiqueta. Es $1/C_{13}$.
> - El docente no marca polaridad en $E_1$. Se toma como base su resultado: $V$ lleva $+E_1\int i_1\,dt$, como en la analogía, y por eso $E_1$ aparece con signo negativo en la ecuación de $i_1$.
> - En su dibujo mecánico la flecha de $E_1$ apunta en el sentido de $v_1$, pero con $+E_1\int i_1\,dt$ en $V$ la fuerza generalizada sale con signo contrario. Es una inconsistencia de la hoja, no se corrige: se sigue su ecuación.

---

## Reglas

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor $C$ = resorte $1/C$, resistencia $R$ = amortiguador, corriente = velocidad, carga = posición.
2. **Grados de libertad:** número de mallas = $N$. Para un circuito conexo, $N = \text{aristas} - \text{nodos} + 1$.
3. **Compartidos:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se gira el circuito.
4. **Mallas:** una corriente de malla por malla. Las mallas con inductancia llevan su número ($L_2$ en la malla 2, $L_3$ en la malla 3). La malla sin inductancia es la 1 y es un cuerpo simulado de masa 0, que se conecta igual que cualquier cuerpo. Todas las corrientes van en sentido horario.
5. **Corrientes:** un elemento en una sola malla lleva la corriente de esa malla. Un elemento compartido por dos mallas lleva la diferencia de sus corrientes.
6. **Conversión a mecánico:** la corriente de una malla es la velocidad de su cuerpo. Un elemento en una sola malla va entre su cuerpo y la pared fija. Un elemento compartido va entre los dos cuerpos de sus mallas. Elementos en serie en el circuito pasan a paralelo en el mecánico. Dos resistencias en la misma malla, hacia la pared, se suman como un solo amortiguador.
7. **Energías:**

$$
T = \sum \frac{L}{2} i^2, \qquad V = \sum \frac{1}{2C}\left(\int i\,dt\right)^2 + E\int i\,dt, \qquad P = \sum \frac{R}{2} i^2
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

Aristas: 10 (contando el cable D–E). Nodos: 8.

$$
N = 10 - 8 + 1 = 3 \text{ mallas} \qquad (i_1,\ i_2,\ i_3)
$$

| Malla | Nodos | Elementos | Inductancia |
|---|---|---|---|
| **1** | G-A-B-H-F | $E_1$, $R_1$, $R_{12}$, $C_{13}$, $2R_1$ | ninguna (cuerpo simulado) |
| **2** | B-C-D-H | $L_2$, $C_2$, $R_{23}$, $R_{12}$ | $L_2$ |
| **3** | H-D-E-F | $R_{23}$, cable, $L_3$, $C_{13}$ | $L_3$ |

| Elemento | Rama | Mallas | ¿Compartido? |
|---|---|---|---|
| $E_1$ | G–A | 1 | No |
| $L_2$ | B–C | 2 | No |
| $L_3$ | E–F | 3 | No |

**Conclusión:** no hay inductancias ni fuentes compartidas. **No hace falta girar el circuito.**

### Paso 2. Corriente por cada uno de los 9 elementos

Con las tres corrientes de malla en sentido horario:

| Elemento | Rama | Mallas | Corriente |
|---|---|---|---|
| $E_1$ | G–A | 1 | $i_1$ |
| $R_1$ | A–B | 1 | $i_1$ |
| $2R_1$ | F–G | 1 | $i_1$ |
| $L_2$ | B–C | 2 | $i_2$ |
| $C_2$ | C–D | 2 | $i_2$ |
| $L_3$ | E–F | 3 | $i_3$ |
| $R_{12}$ | B–H | 1 y 2 | $i_1 - i_2$ |
| $C_{13}$ | H–F | 1 y 3 | $i_1 - i_3$ |
| $R_{23}$ | H–D | 2 y 3 | $i_2 - i_3$ |

### Paso 3. Sistema mecánico equivalente

**Cuerpos:**

| Cuerpo | Malla | Masa | Velocidad |
|---|---|---|---|
| 1 | 1 | 0 (simulado) | $v_1 = i_1$ |
| 2 | 2 | $L_2$ | $v_2 = i_2$ |
| 3 | 3 | $L_3$ | $v_3 = i_3$ |

**Fuerza:** $F_1 = E_1$ sobre el cuerpo 1.

**Elementos y conexiones:**

| Elemento | Se conecta entre | Velocidad relativa |
|---|---|---|
| Amortiguador $3R_1$ ($R_1 + 2R_1$ sumados) | cuerpo 1 y pared fija | $v_1$ |
| Resorte $1/C_2$ | cuerpo 2 y pared fija | $v_2$ |
| Amortiguador $R_{12}$ | cuerpos 1 y 2 | $v_1 - v_2$ |
| Resorte $1/C_{13}$ | cuerpos 1 y 3 | $v_1 - v_3$ |
| Amortiguador $R_{23}$ | cuerpos 2 y 3 | $v_2 - v_3$ |

**Conexiones por cuerpo:**

- **Cuerpo 1 (masa 0):** $3R_1$ a la pared, $R_{12}$ al cuerpo 2, $1/C_{13}$ al cuerpo 3 y la fuerza $F_1 = E_1$.
- **Cuerpo 2 (masa $L_2$):** $1/C_2$ a la pared, $R_{12}$ al cuerpo 1 y $R_{23}$ al cuerpo 3.
- **Cuerpo 3 (masa $L_3$):** $1/C_{13}$ al cuerpo 1 y $R_{23}$ al cuerpo 2.

**Pared fija:** solo están unidos a ella $3R_1$ (cuerpo 1) y $1/C_2$ (cuerpo 2). Las masas $L_2$ y $L_3$ son los cuerpos, no elementos de pared.

**Verificación de los 9 elementos:**

| Grupo | Elementos | Cantidad |
|---|---|---|
| Masas y fuerza | $L_2$, $L_3$, $E_1$ | 3 |
| A la pared | $R_1$ y $2R_1$ (como $3R_1$), $C_2$ | 3 |
| Entre cuerpos | $R_{12}$, $C_{13}$, $R_{23}$ | 3 |
| **Total** | | **9** |

### Paso 4. Energías $T$, $V$ y $P$

Con $q_r = \int i_r\,dt$:

$$
T = \frac{L_2}{2}\,i_2^2 + \frac{L_3}{2}\,i_3^2
$$

$$
V = \frac{1}{2C_2}\left(\int i_2\,dt\right)^2 + \frac{1}{2C_{13}}\left(\int (i_1 - i_3)\,dt\right)^2 + E_1\int i_1\,dt
$$

$$
P = \frac{3R_1}{2}\,i_1^2 + \frac{R_{23}}{2}\,(i_2 - i_3)^2 + \frac{R_{12}}{2}\,(i_1 - i_2)^2
$$

### Paso 5. Ecuaciones de Lagrange

**Para $i_1$ (malla 1):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_1}\right) = 0, \qquad \frac{\partial V}{\partial q_1} = \frac{1}{C_{13}}\int (i_1 - i_3)\,dt + E_1, \qquad \frac{\partial P}{\partial i_1} = 3R_1 i_1 + R_{12}(i_1 - i_2)
$$

$$
0 = -\frac{1}{C_{13}}\int (i_1 - i_3)\,dt - E_1 - 3R_1\,i_1 - R_{12}\,(i_1 - i_2)
$$

**Para $i_2$ (malla 2):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_2}\right) = L_2\frac{di_2}{dt}, \qquad \frac{\partial V}{\partial q_2} = \frac{1}{C_2}\int i_2\,dt, \qquad \frac{\partial P}{\partial i_2} = R_{23}(i_2 - i_3) - R_{12}(i_1 - i_2)
$$

$$
L_2\frac{di_2}{dt} = -\frac{1}{C_2}\int i_2\,dt - R_{23}\,(i_2 - i_3) + R_{12}\,(i_1 - i_2)
$$

**Para $i_3$ (malla 3):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_3}\right) = L_3\frac{di_3}{dt}, \qquad \frac{\partial V}{\partial q_3} = -\frac{1}{C_{13}}\int (i_1 - i_3)\,dt, \qquad \frac{\partial P}{\partial i_3} = -R_{23}(i_2 - i_3)
$$

$$
L_3\frac{di_3}{dt} = \frac{1}{C_{13}}\int (i_1 - i_3)\,dt + R_{23}\,(i_2 - i_3)
$$
