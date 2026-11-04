# E8P4 — Sistema de dos poleas con extremo libre (polea 2): Lagrange y circuito equivalente

## Enunciado

Dado el sistema mecánico de dos poleas, con el extremo libre de la cuerda cargado por una fuerza, plantear Lagrange y hallar el circuito eléctrico equivalente.

**Descripción de la figura**

- Techo fijo arriba y piso fijo abajo, a distancia $H$ del techo.
- $y_1$, $y_2$, $y_3$: posiciones medidas hacia abajo desde el techo.
- **Polea 1:** masa $m_1$, radio $R_1$, centro en $y_1$. Cuelga del techo por un resorte $k$ (longitud natural $l_0$).
- **Polea 2:** masa $m_2$, radio $R_2$, centro en $y_2$. Cuelga de la cuerda, unida a su centro. Bajo ella hay dos líneas verticales hasta el piso, ambas con símbolo de resorte. La hoja las trata como un solo resorte $k'$ (longitud natural $l_0'$) que rodea la polea 2 (arco $\pi R_2$), de longitud $2H - 2y_2 + \pi R_2$.
- **Amortiguadores:** $c_1$ (polea 1, actúa con la velocidad $\dot{y}_1$) y $c_2$ (polea 2, actúa con $\dot{y}_2$). No están dibujados en la figura, pero la hoja los usa en $P$ y en el circuito.
- **Cuerda** de longitud $l$: sube desde el centro de la polea 2 hasta la polea 1, la rodea (arco $\pi R_1$) y baja hasta su extremo libre, en $y_3$.
- **Cuerpo 3:** el extremo libre de la cuerda, en $y_3$. Es un cuerpo ficticio de masa $m_3 = 0$ (se agrega para tener la coordenada $y_3$).
- Fuerza $F(t)$ sobre el extremo libre, hacia abajo (mismo sentido en que crece $y_3$).
- Los pesos se desprecian.

> **Errores y detalles de la hoja del docente:**
> - **Signo de $F$:** pone $V = \dots + F(t)\,y_3$, y eso deja $-F(t)$ en la ecuación de $y_3$. Pero $F$ empuja hacia abajo, en el sentido en que crece $y_3$, así que debe quedar $+F(t)$ (es decir, $V = -F\,y_3$ o $Q_3 = +F$).
> - **Circuito sin fuente:** en su circuito equivalente no dibuja la fuente $F$. Debe ir en la malla del cuerpo 3, la de $m_3$.
> - **Nombres de los resortes:** en una línea de $V$ escribe $k_2$ y en la ecuación de $y_2$ escribe $2k$, pero se trata de $k$ (polea 1) y de $k'$ (bajo la polea 2), respectivamente.
> - **Ecuaciones incompletas:** la ecuación de $y_2$ queda cortada con puntos suspensivos y la de $y_3$ no se rotula. Además tacha $m_3\ddot{y}_3$ sin desarrollar la masa ficticia.
> - **Mallas:** numera las mallas 1 y 2 y dibuja la malla derecha antihoraria con $i = \dot{y}_3$. Aquí se numeran 2 y 3 (la malla de cada cuerpo) y todas van en sentido horario, con $i_3 = -\dot{y}_3$.
> - **Dibujo:** solo dibuja resortes (uno arriba y dos símbolos de resorte bajo la polea 2). Los amortiguadores $c_1$ y $c_2$ no están dibujados, aunque la hoja los usa en $P$ y en el circuito. Se sigue la hoja.

---

## Reglas

1. **Analogía de voltajes:** fuerza = fuente, masa $M$ = inductancia $L$, resorte $K$ = capacitor $1/C$, amortiguador $c$ = resistencia $R$, velocidad = corriente, posición = carga.
2. **Grados de libertad:** $N$ = número de cuerpos − número de ligaduras. Cada ligadura relaciona las posiciones de los cuerpos.
3. **Desviaciones:** $y_1$, $y_2$ e $y_3$ se miden como desviaciones respecto del equilibrio, así las constantes (longitudes naturales y $H$) se cancelan. La ligadura derivada da $\dot{y}_1$ en función de $\dot{y}_2$ y $\dot{y}_3$.
4. **Energías** en función de las coordenadas generalizadas:

$$
T = \sum \frac{m}{2} v^2, \qquad V = \sum \frac{K}{2} (\text{deformación})^2, \qquad P = \sum \frac{c}{2} (\text{velocidad del amortiguador})^2
$$

   En $V$ la deformación de cada resorte se calcula con la longitud que lo estira. En $P$ se usa la velocidad en el extremo del amortiguador.

5. **Ecuación de Lagrange**, una por cada coordenada generalizada $q$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}}\right) - \frac{\partial T}{\partial q} = -\frac{\partial V}{\partial q} - \frac{\partial P}{\partial \dot{q}} + Q
$$

   Como $T$ no depende de $q$, desaparece $\partial T / \partial q$.

6. **Fuerza generalizada:**

$$
Q = F \cdot \frac{\partial y_{\text{punto de aplicación}}}{\partial q}
$$

   Es positiva si $F$ empuja en el sentido en que crece la coordenada.

7. **Conversión a circuito:** cada EDO es la ecuación de una malla, de la forma $L\ddot{q} + R\dot{q} + \frac{1}{C}q = E$. La corriente de una malla es la velocidad de su cuerpo y todas van en sentido horario. Un elemento que depende de una sola variable va en su malla. Un elemento que depende de la combinación de las dos variables va en una rama compartida entre las dos mallas, que lleva la diferencia de sus corrientes.
8. **Fuente:** con $V = +E\int i\,dt$ (convención de `analogia.md`), $E$ sale con signo negativo en la ecuación de su malla.

---

## Solución por pasos

### Paso 1. Grados de libertad, ligadura y velocidades

- **Cuerpos:** 3 (polea 1, polea 2 y extremo libre 3). **Ligaduras:** 1 (la cuerda de longitud $l$).
- $N = 3 - 1 = 2$. Coordenadas generalizadas: $y_2$ e $y_3$.

**Ligadura de la cuerda:**

$$
(y_2 - y_1) + \pi R_1 + (y_3 - y_1) = l \quad\Longrightarrow\quad y_1 = \frac{1}{2}\left(y_2 + y_3 + \pi R_1 - l\right)
$$

Las constantes se cancelan en el equilibrio (regla 3), así que con desviaciones:

$$
y_1 = \frac{1}{2}(y_2 + y_3) \qquad\Longrightarrow\qquad \dot{y}_1 = \frac{1}{2}(\dot{y}_2 + \dot{y}_3)
$$

### Paso 2. $T$, $V$ y $P$ en función de $y_2$ e $y_3$

**Energía cinética** (con $m_3 = 0$):

$$
T = \frac{1}{2} m_1 \dot{y}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2 = \frac{m_1}{8}\,(\dot{y}_2 + \dot{y}_3)^2 + \frac{m_2}{2}\,\dot{y}_2^2
$$

**Energía potencial:**
- Resorte $k$ (polea 1): deformación $y_1 = \frac{1}{2}(y_2 + y_3)$.
- Resorte $k'$ (polea 2): rodea la polea 2 y baja al piso en dos tramos. Cuando la polea baja $y_2$, cada tramo se acorta $y_2$, así que la deformación total es $2y_2$.

$$
V = \frac{k}{2}\left[\frac{1}{2}(y_2 + y_3)\right]^2 + \frac{k'}{2}(2y_2)^2 = \frac{k}{8}\,(y_2 + y_3)^2 + 2k'\,y_2^2
$$

**Función de disipación:**
- Amortiguador $c_1$: velocidad $\dot{y}_1 = \frac{1}{2}(\dot{y}_2 + \dot{y}_3)$.
- Amortiguador $c_2$: velocidad $\dot{y}_2$.

$$
P = \frac{c_1}{2}\left[\frac{1}{2}(\dot{y}_2 + \dot{y}_3)\right]^2 + \frac{c_2}{2}\,\dot{y}_2^2 = \frac{c_1}{8}\,(\dot{y}_2 + \dot{y}_3)^2 + \frac{c_2}{2}\,\dot{y}_2^2
$$

### Paso 3. Fuerzas generalizadas

$F(t)$ actúa sobre el extremo libre, en el sentido en que crece $y_3$.

$$
Q_2 = F \cdot \frac{\partial y_3}{\partial y_2} = 0, \qquad Q_3 = F \cdot \frac{\partial y_3}{\partial y_3} = F(t)
$$

### Paso 4. Ecuaciones de Lagrange

**Para $y_2$:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_2}\right) = \frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) + m_2\,\ddot{y}_2, \qquad \frac{\partial T}{\partial y_2} = 0
$$

$$
\frac{\partial V}{\partial y_2} = \frac{k}{4}\,(y_2 + y_3) + 4k'\,y_2, \qquad \frac{\partial P}{\partial \dot{y}_2} = \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3) + c_2\,\dot{y}_2, \qquad Q_2 = 0
$$

$$
m_2\,\ddot{y}_2 + c_2\,\dot{y}_2 + 4k'\,y_2 + \frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) + \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3) + \frac{k}{4}\,(y_2 + y_3) = 0 \qquad \text{(EDO 1)}
$$

**Para $y_3$:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) = \frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3), \qquad \frac{\partial T}{\partial y_3} = 0
$$

$$
\frac{\partial V}{\partial y_3} = \frac{k}{4}\,(y_2 + y_3), \qquad \frac{\partial P}{\partial \dot{y}_3} = \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3), \qquad Q_3 = F(t)
$$

$$
\frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) + \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3) + \frac{k}{4}\,(y_2 + y_3) = F(t) \qquad \text{(EDO 2)}
$$

### Paso 5. Circuito equivalente

**Mallas y corrientes** (todas en sentido horario):

| Malla | Cuerpo | Corriente | Carga |
|---|---|---|---|
| 2 | polea 2 | $i_2 = \dot{y}_2$ | $q_2 = y_2$ |
| 3 | extremo libre (masa ficticia 0) | $i_3 = -\dot{y}_3$ | $q_3 = -y_3$ |

La combinación $y_2 + y_3$ es la que aparece en los términos de la polea 1. Una rama compartida lleva la diferencia de corrientes, así que se toma $i_3 = -\dot{y}_3$ para que la rama compartida lleve:

$$
i_2 - i_3 = \dot{y}_2 + \dot{y}_3, \qquad q_2 - q_3 = y_2 + y_3
$$

**Elementos.** Los de la polea 1 ($m_1$, $c_1$, $k$) se mueven con $\dot{y}_1 = \frac{1}{2}(i_2 - i_3)$, y por eso aparecen con el factor $\frac{1}{4}$ en la rama compartida:

| Ubicación | Elemento mecánico | Elemento eléctrico | Valor |
|---|---|---|---|
| Solo malla 2 | masa $m_2$ | inductancia $L_2$ | $L_2 = m_2$ |
| Solo malla 2 | amortiguador $c_2$ | resistencia $R_2$ | $R_2 = c_2$ |
| Solo malla 2 | resorte $4k'$ | capacitor $C_2$ | $C_2 = \dfrac{1}{4k'}$ |
| Solo malla 3 | masa ficticia $m_3$ | inductancia $L_3$ | $L_3 = m_3 = 0$ |
| Solo malla 3 | fuerza $F(t)$ | fuente $E$ | $E = F(t)$ |
| Rama compartida 2–3 | masa $\frac{m_1}{4}$ | inductancia $L_{23}$ | $L_{23} = \dfrac{m_1}{4}$ |
| Rama compartida 2–3 | amortiguador $\frac{c_1}{4}$ | resistencia $R_{23}$ | $R_{23} = \dfrac{c_1}{4}$ |
| Rama compartida 2–3 | resorte $\frac{k}{4}$ | capacitor $C_{23}$ | $C_{23} = \dfrac{4}{k}$ |

**Verificación de los elementos mecánicos:**

| Grupo | Elementos | Cantidad |
|---|---|---|
| Masas | $m_1$, $m_2$, $m_3$ (ficticia) | 3 |
| Resortes | $k$, $k'$ | 2 |
| Amortiguadores | $c_1$, $c_2$ | 2 |
| Fuerza | $F$ | 1 |
| **Total** | | **8** |

Los 8 quedaron representados en la tabla: $m_1$, $c_1$ y $k$ en la rama compartida, $m_2$, $c_2$ y $k'$ en la malla 2, y $m_3$ y $F$ en la malla 3.

**Comprobación de las ecuaciones de malla** (Lagrange del circuito con $V = \dots + E\,q_3$):

*Malla 2:*

$$
L_2\frac{di_2}{dt} + L_{23}\frac{d(i_2 - i_3)}{dt} + R_2 i_2 + R_{23}(i_2 - i_3) + \frac{1}{C_2}q_2 + \frac{1}{C_{23}}(q_2 - q_3) = 0
$$

Con $i_2 = \dot{y}_2$, $i_2 - i_3 = \dot{y}_2 + \dot{y}_3$ y $q_2 - q_3 = y_2 + y_3$:

$$
m_2\,\ddot{y}_2 + c_2\,\dot{y}_2 + 4k'\,y_2 + \frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) + \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3) + \frac{k}{4}\,(y_2 + y_3) = 0
$$

Es la EDO 1. ✓

*Malla 3:*

$$
L_3\frac{di_3}{dt} - L_{23}\frac{d(i_2 - i_3)}{dt} = \frac{1}{C_{23}}(q_2 - q_3) - E + R_{23}(i_2 - i_3)
$$

Con $L_3 = 0$ y $E = F$:

$$
-\frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) = \frac{k}{4}\,(y_2 + y_3) - F(t) + \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3)
$$

$$
\frac{m_1}{4}\,(\ddot{y}_2 + \ddot{y}_3) + \frac{c_1}{4}\,(\dot{y}_2 + \dot{y}_3) + \frac{k}{4}\,(y_2 + y_3) = F(t)
$$

Es la EDO 2. ✓

**Sentido de la fuente:** con $i_3 = -\dot{y}_3$ y $q_3 = -y_3$, el término $E\,q_3$ de $V$ es $-F\,y_3$, que es el potencial correcto de una fuerza $F$ hacia abajo. Por eso $E = +F$ y en la ecuación de la malla 3 aparece como $-E$.
