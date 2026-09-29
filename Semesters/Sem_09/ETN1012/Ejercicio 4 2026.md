# Ejercicio 4 2026

Una red de telefonía pública dispone de 4 canales de comunicación y está conformada por 100 fuentes de tráfico. Durante el periodo de observación, se ha determinado que la tasa de llegada de llamadas es constante e igual a 3000 llamadas por hora, mientras que el tiempo medio de ocupación de cada llamada es de 5 segundos.

Con base en estos datos, determinar:

a) La expresión general de la probabilidad de estado P (j) del sistema.  
b) Las probabilidades de estado del sistema para: P (0), P (1), P (2), P (3), P (4).  
c) La congestión en el tiempo (probabilidad de que todos los canales estén ocupados).  
d) La congestión en las llamadas (probabilidad de bloqueo).  
e) El tráfico ofrecido al sistema (en Erlangs).  
f) El tráfico cursado por el sistema.  
g) El tráfico rechazado.  
h) El número de llamadas rechazadas durante una hora.

---

## Solución

**Modelo:** hay $F = 100$ fuentes (finitas), $N = 4$ canales y una tasa de llegada $\lambda = 3000\ \text{llamadas/hora}$. Con este mismo patrón de datos (fuentes, canales y $\lambda$), el ejemplo resuelto de las diapositivas usa **Engset**, por eso es el modelo de resolución.

**Notación:** $F$ = número de fuentes; $N$ = número de canales; $\bar{t}$ = tiempo medio de ocupación ($5\ \text{s}$); $a$ = tasa generada por fuente libre; $b$ = tráfico por fuente libre; $E$ = congestión en el tiempo; $B$ = congestión en las llamadas; $A$ = tráfico ofrecido; $A^l$ = tráfico cursado; $M$ = tráfico rechazado; $NLLP$ = número de llamadas perdidas por hora.

Definiciones: la congestión en el tiempo $E$ es la fracción del tiempo en que todos los canales están ocupados; la congestión en las llamadas $B$ es la fracción de intentos de llamada que encuentran todos los canales ocupados.

Tasa por fuente y tráfico por fuente libre:

$$
a = \frac{\lambda}{F} = \frac{3000\ \text{llamadas/hora}}{100} = 30\ \frac{\text{llamadas}}{\text{hora}\cdot\text{fuente}} = \frac{30}{3600} = 0{,}008333\ \frac{\text{llamadas}}{\text{s}\cdot\text{fuente}}
$$

$$
b = a\cdot\bar{t} = 0{,}008333\ \frac{\text{llamadas}}{\text{s}} \times 5\ \text{s} = 0{,}041667\ \frac{\text{Erlangs}}{\text{fuente}} = \frac{1}{24}
$$

**a) Expresión general:**

$$
P(j) = \frac{\binom{F}{j}\,b^j}{\displaystyle\sum_{i=0}^{N}\binom{F}{i}\,b^i}
$$

Para $F = 100$, $N = 4$ y $b = 1/24$:

$$
P(j) = \frac{\binom{100}{j}\,b^j}{\displaystyle\sum_{i=0}^{4}\binom{100}{i}\,b^i}
$$

**b) Probabilidades de estado.** Cada coeficiente binomial sale de $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$; por ejemplo, $\binom{100}{4} = \dfrac{100 \cdot 99 \cdot 98 \cdot 97}{4!} = 3\,921\,225$. Con $b^j = (1/24)^j$:

| $j$ | $\binom{100}{j}$ | $b^j$ | $\binom{100}{j}\,b^j$ |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1,0000 |
| 1 | 100 | $1/24$ | $100/24 = 4{,}1667$ |
| 2 | 4950 | $1/576$ | $4950/576 = 8{,}5938$ |
| 3 | 161 700 | $1/13\,824$ | $161\,700/13\,824 = 11{,}6970$ |
| 4 | 3 921 225 | $1/331\,776$ | $3\,921\,225/331\,776 = 11{,}8189$ |

$$
\sum = 1 + 4{,}1667 + 8{,}5938 + 11{,}6970 + 11{,}8189 = 37{,}2764
$$

$$
P(0) = \frac{1}{37{,}2764} = 0{,}0268 \qquad P(1) = \frac{4{,}1667}{37{,}2764} = 0{,}1118 \qquad P(2) = \frac{8{,}5938}{37{,}2764} = 0{,}2305
$$

$$
P(3) = \frac{11{,}6970}{37{,}2764} = 0{,}3138 \qquad P(4) = \frac{11{,}8189}{37{,}2764} = 0{,}3171
$$

**c) Congestión en el tiempo:** $E = P(N) = P(4) = 0{,}3171$ (31,71 %).

**d) Congestión en las llamadas** (se calcula con $F-1 = 99$ fuentes, porque la fuente que origina la llamada no puede estar ocupada):

$$
B = \frac{\binom{F-1}{N}\,b^N}{\displaystyle\sum_{J=0}^{N}\binom{F-1}{J}\,b^J}
$$

| $J$ | $\binom{99}{J}$ | $\binom{99}{J}\,b^J$ |
|---:|---:|---:|
| 0 | 1 | 1,0000 |
| 1 | 99 | $99/24 = 4{,}1250$ |
| 2 | 4851 | $4851/576 = 8{,}4219$ |
| 3 | 156 849 | $156\,849/13\,824 = 11{,}3461$ |
| 4 | 3 764 376 | $3\,764\,376/331\,776 = 11{,}3461$ |

$$
\sum = 1 + 4{,}125 + 8{,}4219 + 11{,}3461 + 11{,}3461 = 36{,}2391
$$

$$
B = \frac{11{,}3461}{36{,}2391} = 0{,}3131 \quad (31{,}31\%)
$$

Se cumple $B < E$ ($0{,}3131 < 0{,}3171$), como corresponde a Engset.

**f) Tráfico cursado** ($A^l$, canales ocupados en promedio):

$$
A^l = \frac{F\,b\,(1-B)}{1 + b\,(1-B)} = \frac{100 \times 0{,}041667 \times 0{,}6869}{1 + 0{,}041667 \times 0{,}6869} = \frac{2{,}8621}{1{,}0286} = 2{,}7825\ \text{Erlangs}
$$

Verificación con el promedio de canales ocupados:

$$
A^l = \sum_{j=0}^{4} j\,P(j) = 0(0{,}0268) + 1(0{,}1118) + 2(0{,}2305) + 3(0{,}3138) + 4(0{,}3171) = 0{,}1118 + 0{,}4611 + 0{,}9414 + 1{,}2682 = 2{,}7825\ \text{Erlangs}
$$

**e) Tráfico ofrecido** (se calcula después del cursado):

$$
A = \frac{A^l}{1-B} = \frac{2{,}7825\ \text{Erlangs}}{1 - 0{,}3131} = \frac{2{,}7825\ \text{Erlangs}}{0{,}6869} = 4{,}0507\ \text{Erlangs}
$$

**g) Tráfico rechazado:**

$$
M = A - A^l = 4{,}0507\ \text{Erlangs} - 2{,}7825\ \text{Erlangs} = 1{,}2682\ \text{Erlangs}
$$

**h) Llamadas rechazadas en una hora** ($NLLP$, número de llamadas perdidas):

$$
NLLP = \frac{M \times 3600}{\bar{t}} = \frac{1{,}2682\ \text{Erlangs} \times 3600\ \text{s/hora}}{5\ \text{s}} = 913{,}1\ \text{llamadas/hora}
$$

### Resumen

| Ítem                         | Resultado (Engset) |
| ---------------------------- | -----------------: |
| $P(0)$                       |             2,68 % |
| $P(1)$                       |            11,18 % |
| $P(2)$                       |            23,05 % |
| $P(3)$                       |            31,38 % |
| $P(4)$                       |            31,71 % |
| Congestión en el tiempo $E$  |            31,71 % |
| Congestión en las llamadas $B$ |          31,31 % |
| Tráfico ofrecido $A$         |     4,0507 Erlangs |
| Tráfico cursado $A^l$        |     2,7825 Erlangs |
| Tráfico rechazado $M$        |     1,2682 Erlangs |
| Llamadas rechazadas por hora |              913,1 |

Nota (comparación con Erlang B, fuentes infinitas): con $A = \lambda\,\bar{t} = 3000 \times 5/3600 = 4{,}1667\ \text{Erlangs}$ se obtiene $E = B = 32{,}65\%$, $A^l = 2{,}8062\ \text{Erlangs}$, $M = 1{,}3605\ \text{Erlangs}$ y $NLLP \approx 980\ \text{llamadas/hora}$. Como el ejemplo de las diapositivas con este patrón de datos usa Engset, las respuestas del ejercicio son las de Engset.
