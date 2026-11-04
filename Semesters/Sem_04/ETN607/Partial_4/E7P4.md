# E7P4 — Circuito con giro: circuito girado, sistema mecánico y Lagrange

## Enunciado

Hallar el circuito equivalente girado y el sistema mecánico equivalente del circuito, y plantear las ecuaciones de Lagrange.

**Descripción de la figura**

Nodos A, B, C, D, E, F, G. Las fuentes son círculos. Circuito plano: un rectángulo exterior con A arriba a la izquierda, la esquina superior derecha unida hacia abajo al nodo C en el lado derecho, D abajo a la derecha, E sobre el lado de abajo y F abajo a la izquierda. B está sobre el lado de arriba. El nodo G está en el centro, debajo de B, y se une a C por una rama horizontal. La región exterior no es una malla.

| Arista                                       | Elemento en la figura                   |
| -------------------------------------------- | --------------------------------------- |
| A–B                                          | $R_1$                                   |
| B–C (por arriba, pasando por la esquina sup. derecha) | $C_2$                          |
| B–G                                          | fuente $E$ (sin polaridad marcada)      |
| G–C                                          | $R_{23}$                                |
| G–E                                          | $L_3$                                   |
| E–D                                          | $R_{13}$                                |
| C–D                                          | $C_{13}$                                |
| A–F                                          | $C_1$                                   |
| F–E                                          | cable                                   |

**Notas sobre la hoja del docente**

- **Nodo "NC":** el nodo que la hoja rotula NC es el nodo C.
- **Flecha de $E$ en el dibujo mecánico:** la flecha apunta en el sentido de $v$, pero con $V = +E\int i\,dt$ (convención de `analogia.md` y de la hoja) la ecuación de la malla 2 queda con $-E$, es decir, la fuerza actúa en contra de $v_2$. Es una inconsistencia del dibujo; se anota y se sigue la ecuación del docente.

---

## Reglas

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor $C$ = resorte $1/C$, resistencia $R$ = amortiguador, corriente = velocidad, carga = posición.
2. **Grados de libertad:** número de mallas = $N$. Para un circuito conexo, $N = \text{aristas} - \text{nodos} + 1$. La cara exterior no es una malla.
3. **Compartidos y giro:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se gira el circuito: se elige como cara exterior otra cara del dibujo plano, de modo que la inductancia o la fuente quede en el borde de la cara exterior y por tanto en una sola malla.
4. **Mallas del circuito girado:** una corriente de malla por malla, todas en sentido horario en el dibujo girado. La malla con $L_3$ es la 3, la que tiene $E$ es la 2 y la restante es la 1. Una malla sin inductancia es un cuerpo simulado de masa 0, que se conecta igual que cualquier cuerpo. Tras girar, los elementos compartidos se renombran con los números de sus mallas: $C_2$ pasa a $C_{12}$, y $R_{23}$, $C_{13}$ y $R_{13}$ conservan su nombre.
5. **Corrientes:** un elemento en una sola malla lleva la corriente de esa malla. Un elemento compartido por dos mallas lleva la diferencia de sus corrientes. Se comprueba con la ley de corrientes de Kirchhoff (LKC).
6. **Conversión a mecánico:** la corriente de una malla es la velocidad de su cuerpo. Un elemento en una sola malla va entre su cuerpo y la pared fija. Un elemento compartido va entre los dos cuerpos de sus mallas. Elementos en serie en el circuito pasan a paralelo en el mecánico.
7. **Energías:**

$$
T = \sum \frac{L}{2} i^2, \qquad V = \sum \frac{1}{2C}\left(\int i\,dt\right)^2 + E\int i\,dt, \qquad P = \sum \frac{R}{2} i^2
$$

   donde $i$ es la corriente de cada elemento y, en el término de la fuente, la corriente de la malla donde está la fuente.

8. **Ecuación de Lagrange**, una por cada corriente de malla $i_r$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_r}\right) = -\frac{\partial V}{\partial\left(\int i_r\,dt\right)} - \frac{\partial P}{\partial i_r}
$$

   Como $T$ no depende de las cargas, desaparece $\partial T/\partial q$.

---

## Solución por pasos

### Paso 1. Grados de libertad, mallas, compartidos y giro

Aristas: 9 (incluido el cable F–E). Nodos: 7.

$$
N = 9 - 7 + 1 = 3 \text{ mallas} \qquad (i_1,\ i_2,\ i_3)
$$

**Circuito original.** Caras interiores:

| Cara | Recorrido | Elementos |
|---|---|---|
| Izquierda | A–B–G–E–F | $R_1$, $E$, $L_3$, cable, $C_1$ |
| Derecha-superior | B–C–G | $C_2$, $R_{23}$, $E$ |
| Derecha-inferior | G–C–D–E | $R_{23}$, $C_{13}$, $R_{13}$, $L_3$ |

| Elemento | Arista | Caras que lo contienen | ¿Compartido? |
|---|---|---|---|
| $E$ | B–G | izquierda y derecha-superior | **Sí** |
| $L_3$ | G–E | izquierda y derecha-inferior | **Sí** |

**Conclusión:** $E$ y $L_3$ están compartidas, por lo que **hay que girar el circuito**.

**Cara exterior elegida:** la cara izquierda (A–B–G–E–F). Así $E$ (B–G) y $L_3$ (G–E) quedan en el borde de la cara exterior y cada una pertenece a una sola malla. La cara exterior original (A–B–C–D–E–F) pasa a ser la malla 1.

**Circuito girado.** Mallas en sentido horario:

| Malla | Recorrido | Elementos | Inductancia / fuente |
|---|---|---|---|
| **1** | A→B→C→D→E→F→A | $R_1$, $C_{12}$, $C_{13}$, $R_{13}$, $C_1$, cable | ninguna (cuerpo simulado) |
| **2** | C→B→G→C | $C_{12}$, $E$, $R_{23}$ | fuente $E$ |
| **3** | C→G→E→D→C | $R_{23}$, $L_3$, $R_{13}$, $C_{13}$ | $L_3$ |

| Elemento | Arista | Mallas | ¿Compartido? |
|---|---|---|---|
| $E$ | B–G | 2 | No |
| $L_3$ | G–E | 3 | No |

### Paso 2. Corriente por cada uno de los 8 elementos

El cable no cuenta.

| Elemento | Arista | Mallas | Corriente |
|---|---|---|---|
| $R_1$ | A→B | 1 | $i_1$ |
| $C_1$ | F→A | 1 | $i_1$ |
| $E$ | B→G | 2 | $i_2$ |
| $L_3$ | G→E | 3 | $i_3$ |
| $C_{12}$ | B→C | 1 y 2 | $i_{12} = i_1 - i_2$ |
| $C_{13}$ | C→D | 1 y 3 | $i_{13} = i_1 - i_3$ |
| $R_{13}$ | D→E | 1 y 3 | $i_{13} = i_1 - i_3$ |
| $R_{23}$ | C→G | 2 y 3 | $i_{23} = i_3 - i_2$ |

**Comprobación con LKC** (corrientes que llegan = corrientes que salen):

| Nodo | Llega | Sale | Resultado |
|---|---|---|---|
| B | $i_1$ (por $R_1$) | $i_2$ (por $E$) y $i_1 - i_2$ (por $C_{12}$) | $i_1 = i_2 + (i_1 - i_2)$ ✓ |
| C | $i_1 - i_2$ (por $C_{12}$) | $i_1 - i_3$ (por $C_{13}$) y $i_3 - i_2$ (por $R_{23}$) | $i_{12} = i_{13} + i_{23}$ ✓ |
| G | $i_2$ (por $E$) y $i_3 - i_2$ (por $R_{23}$) | $i_3$ (por $L_3$) | $i_3 = i_{23} + i_2$ ✓ |
| E | $i_3$ (por $L_3$) e $i_1 - i_3$ (por $R_{13}$) | $i_1$ (por el cable hacia F) | $i_1 = i_3 + (i_1 - i_3)$ ✓ |

### Paso 3. Sistema mecánico equivalente

**Cuerpos:**

| Cuerpo | Malla | Masa | Velocidad |
|---|---|---|---|
| 1 | 1 | 0 (simulado) | $v_1 = i_1$ |
| 2 | 2 | 0 (simulado) | $v_2 = i_2$ |
| 3 | 3 | $L_3$ | $v_3 = i_3$ |

**Fuerzas:** $F = E$ sobre el cuerpo 2 (en la ecuación de su malla aparece como $-E$; ver nota del enunciado).

**Elementos y conexiones:**

| Elemento | Se conecta entre | Velocidad relativa |
|---|---|---|
| Amortiguador $R_1$ | cuerpo 1 y pared fija | $v_1$ |
| Resorte $1/C_1$ | cuerpo 1 y pared fija | $v_1$ |
| Resorte $1/C_{12}$ | cuerpos 1 y 2 | $v_1 - v_2$ |
| Resorte $1/C_{13}$ | cuerpos 1 y 3 | $v_1 - v_3$ |
| Amortiguador $R_{13}$ | cuerpos 1 y 3 | $v_1 - v_3$ |
| Amortiguador $R_{23}$ | cuerpos 2 y 3 | $v_3 - v_2$ |

$R_1$ y $C_1$ están en serie dentro de la malla 1, por lo que quedan en paralelo hacia la pared. $C_{13}$ y $R_{13}$ están en serie entre las mallas 1 y 3, por lo que quedan en paralelo entre los cuerpos 1 y 3.

**Conexiones por cuerpo:**

- **Cuerpo 1 (masa 0):** $R_1$ y $1/C_1$ a la pared, $1/C_{12}$ al cuerpo 2, y $1/C_{13}$ y $R_{13}$ al cuerpo 3.
- **Cuerpo 2 (masa 0, fuerza $E$):** $1/C_{12}$ al cuerpo 1 y $R_{23}$ al cuerpo 3.
- **Cuerpo 3 (masa $L_3$):** $1/C_{13}$ y $R_{13}$ al cuerpo 1, y $R_{23}$ al cuerpo 2.

**Pared fija:** solo están unidos a ella $R_1$ y $1/C_1$ (cuerpo 1). La masa $L_3$ y la fuerza $E$ no son elementos de pared.

**Verificación de los 8 elementos:**

| Grupo | Elementos | Cantidad |
|---|---|---|
| Masa | $L_3$ | 1 |
| Fuerza | $E$ | 1 |
| A la pared | $R_1$, $1/C_1$ | 2 |
| Entre cuerpos | $1/C_{12}$, $1/C_{13}$, $R_{13}$, $R_{23}$ | 4 |
| **Total** | | **8** |

### Paso 4. Energías $T$, $V$ y $P$

$$
T = \frac{L_3}{2}\,i_3^2
$$

$$
V = \frac{1}{2C_1}\left(\int i_1\,dt\right)^2 + \frac{1}{2C_{12}}\left(\int (i_1 - i_2)\,dt\right)^2 + \frac{1}{2C_{13}}\left(\int (i_1 - i_3)\,dt\right)^2 + E\int i_2\,dt
$$

$$
P = \frac{R_1}{2}\,i_1^2 + \frac{R_{23}}{2}\,(i_3 - i_2)^2 + \frac{R_{13}}{2}\,(i_1 - i_3)^2
$$

### Paso 5. Ecuaciones de Lagrange

**Para $i_1$ (malla 1):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_1}\right) = 0, \qquad \frac{\partial V}{\partial q_1} = \frac{1}{C_1}\int i_1\,dt + \frac{1}{C_{12}}\int (i_1 - i_2)\,dt + \frac{1}{C_{13}}\int (i_1 - i_3)\,dt
$$

$$
\frac{\partial P}{\partial i_1} = R_1 i_1 + R_{13}(i_1 - i_3)
$$

$$
0 = -\frac{1}{C_1}\int i_1\,dt - \frac{1}{C_{12}}\int (i_1 - i_2)\,dt - \frac{1}{C_{13}}\int (i_1 - i_3)\,dt - R_1\,i_1 - R_{13}\,(i_1 - i_3)
$$

**Para $i_2$ (malla 2):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_2}\right) = 0, \qquad \frac{\partial V}{\partial q_2} = -\frac{1}{C_{12}}\int (i_1 - i_2)\,dt + E, \qquad \frac{\partial P}{\partial i_2} = -R_{23}(i_3 - i_2)
$$

$$
0 = \frac{1}{C_{12}}\int (i_1 - i_2)\,dt - E + R_{23}\,(i_3 - i_2)
$$

**Para $i_3$ (malla 3):**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial i_3}\right) = L_3\frac{di_3}{dt}, \qquad \frac{\partial V}{\partial q_3} = -\frac{1}{C_{13}}\int (i_1 - i_3)\,dt, \qquad \frac{\partial P}{\partial i_3} = R_{23}(i_3 - i_2) - R_{13}(i_1 - i_3)
$$

$$
L_3\frac{di_3}{dt} = \frac{1}{C_{13}}\int (i_1 - i_3)\,dt - R_{23}\,(i_3 - i_2) + R_{13}\,(i_1 - i_3)
$$
