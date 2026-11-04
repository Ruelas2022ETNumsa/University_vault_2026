# Reglas — E1P4 a E4P4 (imp)

## E1P4 — Circuito con R₁: sistema mecánico equivalente

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor C = resorte 1/C, resistencia R = amortiguador, corriente = velocidad.
2. **Grados de libertad:** número de mallas = N.
3. **Compartidos:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se gira el circuito.
4. **Corrientes:** se asignan i₁, i₂, i₃ a ramas independientes y el resto se obtiene con la ley de corrientes de Kirchhoff (LKC) en los nodos.
5. **Conversión a mecánico:**
   - La corriente por una inductancia es la velocidad de su cuerpo.
   - Un elemento que lleva una sola corriente va entre su cuerpo y la pared fija.
   - Un elemento que lleva la diferencia de dos corrientes va entre los dos cuerpos correspondientes.
6. **Serie ↔ paralelo:** elementos en serie en el circuito pasan a paralelo en el sistema mecánico.

---

## E2P4 — Circuito cúbico: sistema mecánico equivalente

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor C = resorte 1/C, resistencia R = amortiguador, corriente = velocidad.
2. **Grados de libertad:** número de mallas = N. Para un circuito conexo, N = aristas − nodos + 1.
3. **Cubo:** se dibuja plano eligiendo una de sus 6 caras como cara exterior. La cara exterior **no** es una malla; las otras 5 caras sí.
4. **Compartidos:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se elige otra cara exterior (se gira el circuito).
5. **Numeración:** las mallas con inductancia llevan el número de su inductancia (3, 4 y 5). Las mallas sin inductancia son 1 y 2. Una malla sin inductancia es un **cuerpo simulado** de masa 0, que se conecta igual que cualquier cuerpo.
6. **Corrientes:** una corriente de malla por malla (i₁ a i₅). Un elemento en una sola malla lleva la corriente de esa malla. Un elemento compartido por dos mallas lleva la diferencia de sus corrientes.
7. **Conversión a mecánico:** la corriente de una malla es la velocidad de su cuerpo. Un elemento en una sola malla va entre su cuerpo y la pared fija. Un elemento compartido va entre los dos cuerpos de sus mallas.
8. **Serie ↔ paralelo:** elementos en serie en el circuito pasan a paralelo en el sistema mecánico.

---

## E3P4 — Sistema de dos poleas: Lagrange y circuito equivalente

1. **Analogía de voltajes:** fuerza = fuente, masa $M$ = inductancia $L$, resorte $K$ = capacitor $1/C$, amortiguador $C$ = resistencia $R$, velocidad = corriente, posición = carga.
2. **Grados de libertad:** $N$ = número de cuerpos − número de ligaduras. Cada ligadura relaciona las posiciones de los cuerpos.
3. **Desviaciones:** $y_1$ e $y_2$ se miden como desviaciones respecto del equilibrio, así las constantes (longitudes naturales y $H$) se cancelan. La ligadura derivada da $\dot{y}_2$ en función de $\dot{y}_1$.
4. **Energías** en función de la coordenada generalizada:

$$
T = \sum \frac{m}{2} v^2, \qquad V = \sum \frac{K}{2} (\text{deformación})^2, \qquad P = \sum \frac{C}{2} (\text{velocidad del amortiguador})^2
$$

   En $V$ la deformación de cada resorte se calcula con la longitud que lo estira. En $P$ se usa la velocidad en el extremo del amortiguador.

5. **Ecuación de Lagrange:**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}}\right) - \frac{\partial T}{\partial q} = -\frac{\partial V}{\partial q} - \frac{\partial P}{\partial \dot{q}} + Q
$$

   Como $T$ no depende de $q$, desaparece $\partial T / \partial q$.

6. **Fuerza generalizada:**

$$
Q = F \cdot \frac{\partial y_{\text{punto de aplicación}}}{\partial q}
$$

   Es positiva si $F$ empuja en el sentido en que crece la coordenada.

7. **Conversión a circuito:** la EDO queda de la forma:

$$
(\text{coef.})\,\ddot{q} + (\text{coef.})\,\dot{q} + (\text{coef.})\,q = (\text{fuerza})
$$

   Cada coeficiente es un elemento de una sola malla en serie: el de $\ddot{q}$ es $L$, el de $\dot{q}$ es $R$, el de $q$ es $1/C$, y el miembro derecho es la fuente. La corriente de la malla es $\dot{q}$.

---

## E4P4 — Cuña y placa: Lagrange y circuito equivalente

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
