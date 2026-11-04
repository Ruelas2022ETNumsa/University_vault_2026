# E4P4 — Cuña y placa: Lagrange y circuito equivalente

## Enunciado

Dado el sistema mecánico de una cuña y una placa, plantear Lagrange y hallar el circuito eléctrico equivalente.

**Descripción de la figura**

- Recinto con piso fijo y dos paredes fijas (izquierda y derecha) separadas una distancia $D$.
- **Cuerpo 1 (cuña):** masa $m_1$. Bloque que se desliza horizontalmente sobre el piso. Su base tiene ancho $B_1$, su cara izquierda está inclinada $60^\circ$ respecto al piso y su cara derecha es vertical. La coordenada $x_1$ es la distancia horizontal entre la pared izquierda y la esquina inferior izquierda de la cuña. Un resorte $K$ (longitud natural $l_0$) une la cara derecha con la pared derecha. Su longitud es $D - x_1 - B_1$.
- **Cuerpo 2 (placa):** masa $m_2$. Se mueve solo en vertical, pegada a la pared izquierda. Su extremo inferior apoya sobre la cara inclinada de la cuña. La coordenada $y_2$ es la altura de ese extremo sobre el piso, hacia arriba. $B_2$ es la distancia horizontal fija entre la pared izquierda y el punto de contacto.
- **Amortiguadores** (no están dibujados, solo aparecen en $P$):
  - $c_1$ entre la cuña y el piso, con velocidad $\dot{x}_1$.
  - $c_2$ entre la placa y la pared izquierda, con velocidad $\dot{y}_2$.
  - $c_{12}$ en el contacto cuña–placa, con velocidad relativa $\dot{x}_1 - \dot{y}_2$.
- Gravedad $g$ hacia abajo. La cuña está a altura 0. No hay fuerza externa.

> Error del docente en su hoja: en la caja roja final el término de $c_{12}$ dice $c_{12}(1+\sqrt{3})$ y debería ser $c_{12}(1+\sqrt{3})^2$. En $P$ sí está bien escrito, como $(\dot{x}_1 + \sqrt{3}\,\dot{x}_1)^2$.
>
> Simplificación del docente: usa la diferencia escalar $\dot{x}_1 - \dot{y}_2$ como velocidad del contacto, aunque la cuña se mueve en horizontal y la placa en vertical. Se sigue su planteo.

---

## Reglas

1. **Analogía de voltajes:** fuerza = fuente, masa $M$ = inductancia $L$, resorte $K$ = capacitor $1/C$, amortiguador $C$ = resistencia $R$, velocidad = corriente, posición = carga.
2. **Grados de libertad:** $N$ = número de cuerpos − número de ligaduras. Cada ligadura relaciona las posiciones de los cuerpos.
3. **Ligadura geométrica:** el contacto de la placa está en la horizontal $B_2$ y sobre la cara inclinada. De la tangente de $60^\circ$ sale $y_2$ en función de $x_1$. Se define la constante $a = \sqrt{3}\,B_2$ y se deriva para obtener $\dot{y}_2$ en función de $\dot{x}_1$.
4. **Energías** en función de la coordenada generalizada, con posiciones absolutas (la gravedad y el resorte aportan términos constantes):

$$
T = \sum \frac{m}{2} v^2, \qquad V = \sum m g h + \sum \frac{K}{2} (\text{longitud} - l_0)^2, \qquad P = \sum \frac{C}{2} (\text{velocidad del amortiguador})^2
$$

   Para un amortiguador entre dos cuerpos se usa el cuadrado de la diferencia de velocidades. Las constantes aditivas de $V$ se eliminan al derivar.

5. **Ecuación de Lagrange:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}}\right) - \frac{\partial T}{\partial q} = -\frac{\partial V}{\partial q} - \frac{\partial P}{\partial \dot{q}} + Q
$$

   Como $T$ no depende de $q$, desaparece $\partial T / \partial q$. Aquí $Q = 0$.

6. **Conversión a circuito:** la EDO se ordena como:

$$
(\text{coef.})\,\ddot{q} + (\text{coef.})\,\dot{q} + K\,q = (\text{constante})
$$

   El coeficiente de $\ddot{q}$ es $L$, el de $\dot{q}$ es $R$ y el de $q$ es $1/C$. Los términos que no dependen de $q$ ni de sus derivadas pasan al miembro derecho y forman una fuente constante $E$. La corriente de la malla es $\dot{q}$.

---

## Solución por pasos

### Paso 1. Grados de libertad, ligadura y velocidades

- **Cuerpos:** 2 (cuña y placa). **Ligaduras:** 1 (contacto cuña–placa).
- $N = 2 - 1 = 1$. Coordenada generalizada: $q = x_1$.

**Ligadura geométrica:** la cara inclinada forma $60^\circ$ con el piso y el contacto está en $B_2$:

$$
\tan 60^\circ = \sqrt{3} = \frac{y_2}{B_2 - x_1} \quad\Longrightarrow\quad y_2 = \sqrt{3}\,B_2 - \sqrt{3}\,x_1 = a - \sqrt{3}\,x_1
$$

con $a = \sqrt{3}\,B_2$. Derivando:

$$
\dot{y}_2 = -\sqrt{3}\,\dot{x}_1
$$

### Paso 2. $T$, $V$ y $P$ en función de $x_1$

**Energía cinética:**

$$
T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 (3\dot{x}_1^2) = \frac{1}{2}(m_1 + 3m_2)\,\dot{x}_1^2
$$

**Energía potencial:**
- **Gravitatoria:** la cuña está a altura 0 y la placa a $y_2 = a - \sqrt{3}\,x_1$.
- **Elástica:** longitud del resorte $D - x_1 - B_1$, deformación $(D - B_1 - l_0) - x_1$.

$$
V = m_2 g\,(a - \sqrt{3}\,x_1) + \frac{1}{2} K\,(D - B_1 - l_0 - x_1)^2
$$

**Función de disipación:**
- $c_1$: velocidad $\dot{x}_1$.
- $c_2$: velocidad $\dot{y}_2 = -\sqrt{3}\,\dot{x}_1$.
- $c_{12}$: velocidad relativa $\dot{x}_1 - \dot{y}_2 = (1 + \sqrt{3})\,\dot{x}_1$.

$$
P = \frac{1}{2} c_1 \dot{x}_1^2 + \frac{1}{2} c_2 (3\dot{x}_1^2) + \frac{1}{2} c_{12} (1 + \sqrt{3})^2 \dot{x}_1^2
$$

$$
P = \frac{1}{2}\left[c_1 + 3c_2 + (1 + \sqrt{3})^2 c_{12}\right]\dot{x}_1^2, \qquad (1 + \sqrt{3})^2 = 4 + 2\sqrt{3}
$$

### Paso 3. Ecuación de Lagrange

Con $q = x_1$ y $Q = 0$:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_1}\right) - \frac{\partial T}{\partial x_1} = -\frac{\partial V}{\partial x_1} - \frac{\partial P}{\partial \dot{x}_1}
$$

**Derivadas:**

$$
\frac{\partial T}{\partial \dot{x}_1} = (m_1 + 3m_2)\,\dot{x}_1 \quad\Longrightarrow\quad \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_1}\right) = (m_1 + 3m_2)\,\ddot{x}_1, \qquad \frac{\partial T}{\partial x_1} = 0
$$

$$
\frac{\partial V}{\partial x_1} = -\sqrt{3}\,m_2 g - K\,(D - B_1 - l_0 - x_1)
$$

$$
\frac{\partial P}{\partial \dot{x}_1} = \left[c_1 + 3c_2 + (1 + \sqrt{3})^2 c_{12}\right]\dot{x}_1
$$

**Sustitución** (ecuación del docente):

$$
(m_1 + 3m_2)\,\ddot{x}_1 = K\,(D - x_1 - B_1 - l_0) + \sqrt{3}\,m_2 g - \left[c_1 + 3c_2 + (1 + \sqrt{3})^2 c_{12}\right]\dot{x}_1
$$

**Simplificación** (el docente anota que el término $K x_1$ se separa porque la razón es más simple): se pasa $K x_1$ a la izquierda y lo constante a la derecha.

**EDO final (modelo matemático):**

$$
(m_1 + 3m_2)\,\ddot{x}_1 + \left[c_1 + 3c_2 + (1 + \sqrt{3})^2 c_{12}\right]\dot{x}_1 + K\,x_1 = \sqrt{3}\,m_2 g + K\,(D - B_1 - l_0)
$$

### Paso 4. Circuito equivalente

Se compara con la forma $L\ddot{q} + R\dot{q} + \frac{1}{C}q = E$, con $q = x_1$:

| Mecánico | Eléctrico | Valor |
|---|---|---|
| $m_1 + 3m_2$ | Inductancia $L$ | $L = m_1 + 3m_2$ |
| $c_1 + 3c_2 + (1+\sqrt{3})^2 c_{12}$ | Resistencia $R$ | $R = c_1 + 3c_2 + (4 + 2\sqrt{3})\,c_{12}$ |
| $K$ | Capacitor $1/C$ | $C = \dfrac{1}{K}$ |
| término constante | Fuente constante $E$ | $E = \sqrt{3}\,m_2 g + K\,(D - B_1 - l_0)$ |

**Malla:** una sola malla en serie con la fuente constante $E$, $L$, $R$ y $C$.

**Corriente:** $i(t) = \dot{x}_1$. Como $E$ es positiva, empuja la corriente en el sentido positivo de $i$, que es el sentido en que crece $x_1$ (y la carga $q = x_1$).
