# Ejercicio 1 2026

Si el código del país es 403 y el código de la ciudad es 33, para realizar una llamada internacional desde Bolivia cual es el procedimiento establecido para las llamadas al exterior, realizar la llamada.

---

## Solución

Se aplica el **Plan Fundamental de Numeración de 15 dígitos**. La llamada internacional saliente se arma así:

| Campo | Dígitos | Valor |
| ----- | :-----: | ----- |
| Acceso internacional | 2 | `00` |
| Carrier (operador) | 2 | `10` (ej. ENTEL) |
| Código de país | 3 | `403` |
| Código de ciudad | 2 | `33` |
| Número de abonado | 6 | `123456` (ej.) |

Check: 2 + 2 + 3 + 2 + 6 = **15 dígitos**.

**Marcación:** `00 10 403 33 123456` → `001040333123456`


REFERENCIA (no es parte de la respuesta; fuentes de internet, verificar con las diapositivas)

Zona telefónica actual (Bolivia): 2 = La Paz, Oruro, Potosi | 3 = Santa Cruz, Beni, Pando | 4 = Cochabamba, Chuquisaca, Tarija

Codigo de ciudad (2 digitos, plan anterior; las fuentes varian):

| Ciudad                  | Codigo                   |
| ----------------------- | ------------------------ |
| La Paz                  | 22                       |
| Oruro                   | 52                       |
| Potosi                  | 62                       |
| Sucre                   | 64                       |
| Cochabamba              | 44 (otra fuente: 42)     |
| Tarija                  | 66                       |
| Santa Cruz de la Sierra | 33 (es el del enunciado) |
| Trinidad                | 46 (346 con zona 3)      |
| Cobija                  | 842 (3 digitos)          |

Codigo de carrier / portador (formato 1X o XY):

| Operador        | Codigo |
| --------------- | ------ |
| Entel           | 10     |
| AXS             | 11     |
| COTAS           | 12     |
| Boliviatel      | 13     |
| Nuevatel (Viva) | 14     |
| ITS             | 15     |
| COTEL           | 16     |
| Telecel (Tigo)  | 17     |
| BossNet         | 20     |
| Unete           | 21     |
| Utecom          | 22     |

Nota: asignaciones antiguas (anos 90) daban 11 = AES, 12 = Teledata, 13 = Boliviatel. Tigo marca hoy 0017 (00 + 17).

# Ejercicio 2 2026

Una empresa de servicios de telefonía opera en una zona donde existen cuatro centrales telefónicas: A, B, C y una central de tránsito T. Durante un periodo de observación de una hora, se realizaron mediciones del tráfico cursado entre estas centrales.

Los resultados obtenidos fueron los siguientes:

- Entre la central A y la central B se registró un tráfico total de 73 Erlangs.
  - El tráfico alternativo o de desborde corresponde al 17,9 % del tráfico total.
  - El número de canales directos instalados entre las centrales A y B es de 51.
- Entre la central A y la central C se midió un tráfico total de 65 Erlangs.
  - El tráfico de desborde corresponde al 10,77 % del tráfico total.
  - El enlace directo entre las centrales A y C dispone de 46 canales.

Asimismo, se ha establecido que el grado de servicio requerido es B=0.5%, correspondiente a un criterio de bloqueo tipo Erlang B.

Con base de esta información: Determinar el número de canales que debe tener la central de tránsito T para absorber el tráfico de desborde y permitir la descongestión de las rutas directas, garantizando que las llamadas puedan completarse cumpliendo con el grado de servicio especificado.

---

## Solución

**Método:** el desborde es tráfico "a ráfagas" (varianza mayor que la media), por eso no basta sumar medias: se suman **media y varianza** de ambos desbordes y se aplica el tráfico aleatorio equivalente (Wilkinson) con las aproximaciones de Rapp.

### 1. Media del desborde

$$
m_{AB} = 73\ \text{Erlangs} \times 0{,}179 = 13{,}067\ \text{Erlangs}
$$

$$
m_{AC} = 65\ \text{Erlangs} \times 0{,}1077 = 7{,}0005\ \text{Erlangs}
$$

$$
M = 13{,}067 + 7{,}0005 = 20{,}0675\ \text{Erlangs}
$$

### 2. Varianza de cada desborde (Riordan)

$$
v = m\left(1 - m + \frac{A}{C' + 1 - A + m}\right)
$$

Unidades: $m$ y $A$ en Erlangs; $v$ en $\text{Erlangs}^2$; $C'$ en canales.

$C'$ = canales equivalentes que producen el bloqueo medido, es decir $E(A, C') = B$ (Erlang B): $C'_{AB} \approx 63{,}6\ \text{canales}$ (para $A=73\ \text{Erlangs}$, $B=0{,}179$) y $C'_{AC} \approx 63{,}4\ \text{canales}$ (para $A=65\ \text{Erlangs}$, $B=0{,}1077$).

$$
v_{AB} = 13{,}067\left(1 - 13{,}067 + \frac{73}{63{,}6 + 1 - 73 + 13{,}067}\right) = 13{,}067\,(-12{,}067 + 15{,}642) = 46{,}71\ \text{Erlangs}^2
$$

$$
v_{AC} = 7{,}0005\left(1 - 7{,}0005 + \frac{65}{63{,}4 + 1 - 65 + 7{,}0005}\right) = 7{,}0005\,(-6{,}0005 + 10{,}155) = 29{,}09\ \text{Erlangs}^2
$$

$$
V = 46{,}71 + 29{,}09 = 75{,}80\ \text{Erlangs}^2
$$

### 3. Equivalente de Rapp

$$
z = \frac{V}{M} = \frac{75{,}80}{20{,}0675} = 3{,}777 \quad \text{(relación varianza/media, sin unidad)}
$$

$$
A^* = V + 3z(z-1) = 75{,}80 + 3(3{,}777)(2{,}777) = 75{,}80 + 31{,}47 = 107{,}27\ \text{Erlangs}
$$

$$
N^* = \frac{A^*(M+z)}{M+z-1} - M - 1 = 107{,}27\cdot\frac{23{,}845}{22{,}845} - 21{,}0675 = 111{,}96 - 21{,}07 = 90{,}89\ \text{canales}
$$

### 4. Canales de la central de tránsito T

Pérdida objetivo sobre el desborde:

$$
E(A^*, N_{total}) = \frac{B\,M}{A^*} = \frac{0{,}005 \times 20{,}0675\ \text{Erlangs}}{107{,}27\ \text{Erlangs}} = 9{,}35\times10^{-4}
$$

Erlang B con $A^* = 107{,}27\ \text{Erlangs}$: $N=136\ \text{canales} \to 9{,}9\times10^{-4}$ (no cumple) y $N=137\ \text{canales} \to 7{,}8\times10^{-4}$ (cumple), luego $N_{total} = 137\ \text{canales}$.

$$
N_T = N_{total} - N^* = 137\ \text{canales} - 90{,}89\ \text{canales} = 46{,}1\ \text{canales}
$$

**Resultado: T necesita 47 canales.**

### Notas

- Los datos no son consistentes con Erlang B: $E(73,51) = 32{,}7\%$ y $E(65,46) = 32{,}1\%$, no 17,9 % y 10,77 %. Por eso se toman los porcentajes medidos como dato y los 51 y 46 canales no intervienen.
- El resultado es sensible al redondeo de $C'$: con decimales exactos salen $N_{total}=136$ y $N_T = 45{,}6$, es decir 46. Se toma 47 para garantizar el grado de servicio.
- Otros métodos: sumar solo las medias y aplicar Erlang B a 20,07 Erlangs da 32 canales (ignora las ráfagas); usar 51 y 46 canales con Erlang B da ≈ 72. Confirmar cuál usa la cátedra.

# Ejercicio 3 2026xxx

Sea un sistema telefónico caracterizado por la función E(A,N), donde A representa el tráfico ofrecido en Erlangs y N el número de circuitos disponibles.

Considerando que se tiene E(A, 50) y una calidad de servicio (probabilidad de bloqueo) de 0,001370, determinar:

a) La media del tráfico ofrecido.  
b) La varianza del tráfico.  
c) La intensidad de tráfico del sistema.  
d) El número de circuitos parciales requeridos.

Para la resolución del problema, utilizar las aproximaciones propuestas por Rapp, empleadas en el análisis y dimensionamiento de sistemas de tráfico telefónico.

---

## Análisis de Sistema y Aproximación de Rapp (ERT)

### Resolución de Ejercicio Práctico

## 1. Planteamiento del Problema

Se tiene un sistema telefónico (grupo primario) caracterizado por la función de pérdida de Erlang $E(A,N)$. Los datos proporcionados son:

- Número de circuitos disponibles: $N = 50$
- Calidad de servicio (Probabilidad de bloqueo): $E(A,50) = 0.001370$

El objetivo es determinar los parámetros del tráfico mediante la Teoría del Tráfico Aleatorio Equivalente (ERT) utilizando las aproximaciones de Rapp para el tráfico de desborde.

## 2. Resolución Paso a Paso

### Paso Previo: Determinación del Tráfico Primario Ofrecido (A)

Sabemos que el tráfico puro (Poisson) que ingresa al sistema principal se define por la ecuación de estado $E(A,50) = 0.001370$. Consultando las tablas estándar de Erlang B (o resolviendo la ecuación de forma iterativa), determinamos el tráfico original ofrecido:

$$
A \approx 34.63\ \text{Erlangs}
\tag{1}
$$

### a) La media del tráfico ofrecido (M)

En el contexto de la aproximación de Rapp para redes con desborde, el “tráfico ofrecido” al sistema secundario corresponde al tráfico que ha sido bloqueado en el grupo primario. La media de este tráfico de desborde ($M$) se calcula como:

$$
M = A \times E(A,N)
\tag{2}
$$

Sustituyendo los valores:

$$
M = 34.63 \times 0.001370 = 0.04744\ \text{Erlangs}
\tag{3}
$$

### b) La varianza del tráfico de desborde (V)

A diferencia del tráfico puro (cuya varianza es igual a su media), el tráfico de desborde es más ráfago y su varianza ($V$) se calcula mediante la fórmula exacta de Riordan:

$$
V =
M
\left(
1 - M +
\frac{A}{N+1-A+M}
\right)
\tag{4}
$$

Calculamos el término interior (relación varianza a media $Z$):

$$
Z =
1 - 0.04744 +
\frac{34.63}{50+1-34.63+0.04744}
$$

$$
= 0.95256 +
\frac{34.63}{16.41744}
$$

$$
\approx 0.95256 + 2.10934 = 3.0619
\tag{5}
$$

Por lo tanto, la varianza es:

$$
V = M \times Z = 0.04744 \times 3.0619 = 0.14526\ \text{Erlangs}
\tag{6}
$$

### c) La intensidad de tráfico del sistema equivalente ($A^*$)

Para dimensionar las rutas alternativas, Rapp propuso una aproximación matemática muy precisa para encontrar la intensidad de tráfico de un sistema primario “ficticio” equivalente ($A^*$):

$$
A^* \approx
V +
3
\left(
\frac{V}{M}
\right)
\left(
\frac{V}{M}-1
\right)
$$

$$
= V + 3Z(Z-1)
\tag{7}
$$

Reemplazando $Z = 3.0619$ y $V = 0.14526$:

$$
A^*
=
0.14526
+
3(3.0619)(3.0619-1)
$$

$$
=
0.14526
+
3(3.0619)(2.0619)
\tag{8}
$$

$$
A^*
=
0.14526 + 18.9404
=
19.085\ \text{Erlangs}
\tag{9}
$$

### d) El número de circuitos parciales requeridos ($N^*$)

Finalmente, el número de circuitos parciales o ficticios equivalentes ($N^*$), que junto con $A^*$ producirían el mismo desborde $M$ y varianza $V$, se halla despejando la relación general de Riordan:

$$
N^* =
\frac{A^*}
{\frac{V}{M}-1+M}
+
A^* - M - 1
\tag{10}
$$

Sustituyendo los valores calculados:

$$
N^* =
\frac{19.085}
{3.0619-1+0.04744}
+
19.085-0.04744-1
\tag{11}
$$

$$
N^* =
\frac{19.085}{2.10934}
+
18.03756
$$

$$
= 9.0478 + 18.03756
=
27.085\ \text{circuitos}
\tag{12}
$$

**Nota:** En ingeniería práctica, los circuitos parciales equivalentes no necesitan ser un número entero, por lo que se mantienen sus decimales para futuros cálculos de la troncal común.

## 3. Resumen de Resultados

- **a) Media del tráfico ofrecido ($M$):** 0.0474 Erl.
- **b) Varianza del tráfico ($V$):** 0.1453 Erl.
- **c) Intensidad de tráfico equivalente ($A^*$):** 19.085 Erl.
- **d) Circuitos parciales requeridos ($N^*$):** 27.085




# Ejercicio 4 2026

Una red de telefonía pública dispone de 4 canales de comunicación y está conformada por 100 fuentes de tráfico. Durante el periodo de observación, se ha determinado que la tasa de llegada de llamadas es constante es igual a 3000 llamadas por hora, mientras que el tiempo medio de ocupación de cada llamada es de 5 segundos.

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

**Modelo:** el enunciado da una tasa de llegada total constante ($\lambda = 3000\ \text{llamadas/hora}$), independiente de cuántas fuentes estén activas: llegadas de Poisson, por lo que se aplica **Erlang B** (modelo principal). Las 100 fuentes solo intervienen en Engset, que se resuelve al final como comparación.

### Modelo principal: Erlang B

**e) Tráfico ofrecido** (se calcula primero):

$$
A = \lambda\,\bar{t} = 3000\ \frac{\text{llamadas}}{\text{hora}} \times \frac{5\ \text{s}}{3600\ \text{s/hora}} = 4{,}1667\ \text{Erlangs}
$$

**a) Expresión general** (con $N = 4\ \text{canales}$):

$$
P(j) = \frac{A^j / j!}{\displaystyle\sum_{k=0}^{N} A^k / k!}
$$

Términos $A^k/k!$ con $A = 4{,}1667$:

| $k$ | $A^k/k!$ | Valor |
|---:|---|---:|
| 0 | $1$ | 1,0000 |
| 1 | $4{,}1667$ | 4,1667 |
| 2 | $4{,}1667^2/2!$ | 8,6806 |
| 3 | $4{,}1667^3/3!$ | 12,0563 |
| 4 | $4{,}1667^4/4!$ | 12,5587 |

$$
\sum = 1 + 4{,}1667 + 8{,}6806 + 12{,}0563 + 12{,}5587 = 38{,}4622
$$

**b) Probabilidades de estado:**

$$
P(0) = \frac{1}{38{,}4622} = 0{,}0260 \quad (2{,}60\%) \qquad P(1) = \frac{4{,}1667}{38{,}4622} = 0{,}1083 \quad (10{,}83\%)
$$

$$
P(2) = \frac{8{,}6806}{38{,}4622} = 0{,}2257 \quad (22{,}57\%) \qquad P(3) = \frac{12{,}0563}{38{,}4622} = 0{,}3135 \quad (31{,}35\%)
$$

$$
P(4) = \frac{12{,}5587}{38{,}4622} = 0{,}3265 \quad (32{,}65\%)
$$

**c) Congestión en el tiempo:** $E = P(4) = 0{,}3265$ (32,65 %).

**d) Congestión en las llamadas:** en Poisson coincide con la del tiempo, $B = E = 0{,}3265$ (32,65 %).

**f) Tráfico cursado:**

$$
A' = A(1-B) = 4{,}1667\ \text{Erlangs} \times (1 - 0{,}3265) = 2{,}8062\ \text{Erlangs}
$$

**g) Tráfico rechazado:**

$$
M = A \cdot B = 4{,}1667\ \text{Erlangs} \times 0{,}3265 = 1{,}3605\ \text{Erlangs}
$$

**h) Llamadas rechazadas en una hora:**

$$
NLLP = \frac{M \times 3600}{\bar{t}} = \frac{1{,}3605\ \text{Erlangs} \times 3600\ \text{s/hora}}{5\ \text{s}} = 979{,}56\ \text{llamadas/hora} \approx 980\ \text{llamadas/hora}
$$

### Modelo comparativo: Engset (100 fuentes)

Tráfico por fuente libre:

$$
b = \frac{\lambda}{F}\,\bar{t} = 30\ \frac{\text{llamadas}}{\text{hora}\cdot\text{fuente}} \times \frac{5}{3600}\ \text{hora} = 0{,}041667\ \frac{\text{Erlangs}}{\text{fuente}} = \frac{1}{24}
$$

$$
P(j) = \frac{\binom{100}{j}\,b^j}{\displaystyle\sum_{k=0}^{4}\binom{100}{k}\,b^k}
$$

Términos $\binom{100}{j}\,b^j$: $1$; $4{,}1667$; $8{,}5938$; $11{,}6970$; $11{,}8189$, con suma $37{,}2764$.

$$
P(0) = 0{,}0268 \quad P(1) = 0{,}1118 \quad P(2) = 0{,}2305 \quad P(3) = 0{,}3138 \quad P(4) = 0{,}3171
$$

**Congestión en el tiempo:** $E = P(4) = 0{,}3171$ (31,71 %).

**Congestión en las llamadas** (con $F-1 = 99$ fuentes; términos $1$; $4{,}125$; $8{,}4219$; $11{,}3461$; $11{,}3461$, suma $36{,}2391$):

$$
B = \frac{\binom{99}{4}\,b^4}{\displaystyle\sum_{k=0}^{4}\binom{99}{k}\,b^k} = \frac{11{,}3461}{36{,}2391} = 0{,}3131 \quad (31{,}31\%)
$$

**Tráfico cursado** (canales ocupados en promedio):

$$
A' = \sum_{j=0}^{4} j\,P(j) = 0{,}1118 + 0{,}4611 + 0{,}9414 + 1{,}2682 = 2{,}7825\ \text{Erlangs}
$$

**Tráfico ofrecido:**

$$
A = \frac{A'}{1-B} = \frac{2{,}7825\ \text{Erlangs}}{1 - 0{,}3131} = 4{,}0507\ \text{Erlangs}
$$

**Tráfico rechazado:**

$$
M = A - A' = 4{,}0507\ \text{Erlangs} - 2{,}7825\ \text{Erlangs} = 1{,}2682\ \text{Erlangs}
$$

**Llamadas rechazadas en una hora:**

$$
NLLP = \frac{M \times 3600}{\bar{t}} = \frac{1{,}2682\ \text{Erlangs} \times 3600\ \text{s/hora}}{5\ \text{s}} = 913{,}1\ \text{llamadas/hora}
$$

### Resumen

| Ítem | Erlang B (principal) | Engset (100 fuentes) |
|---|---:|---:|
| $P(0)$ | 2,60 % | 2,68 % |
| $P(1)$ | 10,83 % | 11,18 % |
| $P(2)$ | 22,57 % | 23,05 % |
| $P(3)$ | 31,35 % | 31,38 % |
| $P(4)$ | 32,65 % | 31,71 % |
| Congestión en el tiempo | 32,65 % | 31,71 % |
| Congestión en las llamadas | 32,65 % | 31,31 % |
| Tráfico ofrecido | 4,1667 Erlangs | 4,0507 Erlangs |
| Tráfico cursado | 2,8062 Erlangs | 2,7825 Erlangs |
| Tráfico rechazado | 1,3605 Erlangs | 1,2682 Erlangs |
| Llamadas rechazadas por hora | 979,56 | 913,1 |

Nota: confirmar con la cátedra cuál de los dos modelos se usa. Con el enunciado tal cual (tasa constante) corresponde Erlang B; si las 100 fuentes son el dato clave, se usa Engset.

