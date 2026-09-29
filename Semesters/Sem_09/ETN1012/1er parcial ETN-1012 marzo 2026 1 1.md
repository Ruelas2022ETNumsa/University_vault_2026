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

Zona telefónica actual (Bolivia): 2 = La Paz, Oruro, Potosí | 3 = Santa Cruz, Beni, Pando | 4 = Cochabamba, Chuquisaca, Tarija

Código de ciudad (2 dígitos, plan anterior; las fuentes varían):

| Ciudad                  | Código                   |
| ----------------------- | ------------------------ |
| La Paz                  | 22                       |
| Oruro                   | 52                       |
| Potosí                  | 62                       |
| Sucre                   | 64                       |
| Cochabamba              | 44 (otra fuente: 42)     |
| Tarija                  | 66                       |
| Santa Cruz de la Sierra | 33 (es el del enunciado) |
| Trinidad                | 46 (346 con zona 3)      |
| Cobija                  | 842 (3 dígitos)          |

Código de carrier / portador (formato 1X o XY):

| Operador        | Código |
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

Nota: asignaciones antiguas (años 90) daban 11 = AES, 12 = Teledata, 13 = Boliviatel. Tigo marca hoy 0017 (00 + 17).

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

$C'$ = canales equivalentes que producen el bloqueo medido, es decir $E(A, C') = B$. Se obtiene con la recurrencia de Erlang B,

$$
E(A,n) = \frac{A\,E(A,n-1)}{n + A\,E(A,n-1)}, \qquad E(A,0) = 1
$$

y se interpola entre los dos valores enteros de $n$ que encierran el bloqueo medido:

- Para $A = 73\ \text{Erlangs}$ y $B = 0{,}179$: $E(73;63) = 0{,}1855$ y $E(73;64) = 0{,}1746$, luego

$$
C'_{AB} = 63 + \frac{0{,}1855 - 0{,}179}{0{,}1855 - 0{,}1746} = 63 + \frac{0{,}0065}{0{,}0109} = 63{,}60\ \text{canales}
$$

- Para $A = 65\ \text{Erlangs}$ y $B = 0{,}1077$: $E(65;63) = 0{,}1121$ y $E(65;64) = 0{,}1022$, luego

$$
C'_{AC} = 63 + \frac{0{,}1121 - 0{,}1077}{0{,}1121 - 0{,}1022} = 63 + \frac{0{,}0044}{0{,}0099} = 63{,}44\ \text{canales}
$$

Desborde A→B, paso a paso:

$$
C'_{AB} + 1 - A + m_{AB} = 63{,}60 + 1 - 73 + 13{,}067 = 4{,}667 \qquad \frac{A}{4{,}667} = \frac{73}{4{,}667} = 15{,}6417
$$

$$
1 - m_{AB} + 15{,}6417 = 1 - 13{,}067 + 15{,}6417 = 3{,}5747
$$

$$
v_{AB} = m_{AB} \times 3{,}5747 = 13{,}067 \times 3{,}5747 = 46{,}71\ \text{Erlangs}^2
$$

Desborde A→C, paso a paso:

$$
C'_{AC} + 1 - A + m_{AC} = 63{,}44 + 1 - 65 + 7{,}0005 = 6{,}4405 \qquad \frac{A}{6{,}4405} = \frac{65}{6{,}4405} = 10{,}0924
$$

$$
1 - m_{AC} + 10{,}0924 = 1 - 7{,}0005 + 10{,}0924 = 4{,}0919
$$

$$
v_{AC} = m_{AC} \times 4{,}0919 = 7{,}0005 \times 4{,}0919 = 28{,}65\ \text{Erlangs}^2
$$

Las varianzas se suman:

$$
V = v_{AB} + v_{AC} = 46{,}71 + 28{,}65 = 75{,}36\ \text{Erlangs}^2
$$

### 3. Equivalente de Rapp

Relación varianza/media:

$$
z = \frac{V}{M} = \frac{75{,}36}{20{,}0675} = 3{,}755 \quad \text{(sin unidad)}
$$

Tráfico equivalente (Rapp), primero el término $3z(z-1)$:

$$
3z(z-1) = 3\,(3{,}755)\,(2{,}755) = 11{,}265 \times 2{,}755 = 31{,}04
$$

$$
A^* = V + 3z(z-1) = 75{,}36 + 31{,}04 = 106{,}40\ \text{Erlangs}
$$

Canales equivalentes (Rapp), primero los términos: $M + z = 20{,}0675 + 3{,}755 = 23{,}8225$ y $M + z - 1 = 22{,}8225$.

$$
N^* = \frac{A^*(M+z)}{M+z-1} - (M+1) = 106{,}40 \times \frac{23{,}8225}{22{,}8225} - 21{,}0675 = 106{,}40 \times 1{,}0438 - 21{,}0675 = 111{,}06 - 21{,}07 = 89{,}99\ \text{canales}
$$

### 4. Canales de la central de tránsito T

Pérdida objetivo sobre el desborde:

$$
E(A^*, N_{total}) = \frac{B\,M}{A^*} = \frac{0{,}005 \times 20{,}0675\ \text{Erlangs}}{106{,}40\ \text{Erlangs}} = \frac{0{,}1003}{106{,}40} = 9{,}43\times10^{-4}
$$

Se busca el menor $N$ que cumpla, evaluando Erlang B con $A^* = 106{,}40\ \text{Erlangs}$ (recurrencia o tabla): $N=135\ \text{canales} \to 9{,}98\times10^{-4}$ (no cumple, es mayor que $9{,}43\times10^{-4}$) y $N=136\ \text{canales} \to 7{,}8\times10^{-4}$ (cumple), luego $N_{total} = 136\ \text{canales}$.

$$
N_T = N_{total} - N^* = 136\ \text{canales} - 89{,}99\ \text{canales} = 46{,}01\ \text{canales}
$$

$N_T \approx 46{,}0$ canales; como debe ser entero y el valor supera ligeramente 46, se toman 47 canales por seguridad.

**Resultado: T necesita 47 canales.**

### Notas

- Los datos no son consistentes con Erlang B: $E(73,51) = 32{,}7\%$ y $E(65,46) = 32{,}1\%$, no 17,9 % y 10,77 %. Por eso se toman los porcentajes medidos como dato y los 51 y 46 canales no intervienen.
- El resultado es sensible al redondeo de $C'$: con $C'$ redondeado a 63,6 y 63,4 sale $N_{total} = 137$ y $N_T = 46{,}1$; sin redondeos intermedios, $N_T = 45{,}6$. La respuesta queda entre 46 y 47 canales; se toma 47 para no quedar por debajo del grado de servicio.
- Otros métodos: sumar solo las medias y aplicar Erlang B a 20,07 Erlangs da 32 canales (ignora las ráfagas); usar 51 y 46 canales con Erlang B da ≈ 72. Confirmar cuál usa la cátedra.

# Ejercicio 3 2026

Sea un sistema telefónico caracterizado por la función E(A,N), donde A representa el tráfico ofrecido en Erlangs y N el número de circuitos disponibles.

Considerando que se tiene E(A, 50) y una calidad de servicio (probabilidad de bloqueo) de 0,001370, determinar:

a) La media del tráfico ofrecido.  
b) La varianza del tráfico.  
c) La intensidad de tráfico del sistema.  
d) El número de circuitos parciales requeridos.

Para la resolución del problema, utilizar las aproximaciones propuestas por Rapp, empleadas en el análisis y dimensionamiento de sistemas de tráfico telefónico.

---

## Solución

**Método:** el grupo primario $E(A,50)$ deja desbordar una parte pequeña del tráfico, y ese desborde no es de Poisson. Se calculan su media $M$ y su varianza $V$ (Riordan) y se reemplaza por un sistema equivalente $(A^*, N^*)$ con las aproximaciones de Rapp.

### Paso previo: tráfico ofrecido $A$

Se busca $A$ tal que $E(A,50) = 0{,}001370$. Con la recurrencia de Erlang B,

$$
E(A,n) = \frac{A\,E(A,n-1)}{n + A\,E(A,n-1)}, \qquad E(A,0) = 1
$$

se evalúa $n = 50$ para dos valores de $A$ que encierran el bloqueo dado: $E(33{,}1;\,50) = 0{,}001362$ y $E(33{,}2;\,50) = 0{,}001433$. Interpolando:

$$
A = 33{,}1 + 0{,}1\times\frac{0{,}001370 - 0{,}001362}{0{,}001433 - 0{,}001362} = 33{,}1 + 0{,}1\times\frac{0{,}000008}{0{,}000071} = 33{,}11\ \text{Erlangs}
$$

Comprobación: $E(33{,}11;\,50) = 0{,}001369 \approx 0{,}001370$.

### a) Media del tráfico ($M$)

Es el tráfico que desborda del grupo primario:

$$
M = A \cdot E(A,N) = 33{,}11\ \text{Erlangs} \times 0{,}001370 = 0{,}04536\ \text{Erlangs}
$$

### b) Varianza del tráfico ($V$)

Fórmula de Riordan:

$$
V = M\left(1 - M + \frac{A}{N + 1 - A + M}\right)
$$

Paso a paso:

$$
N + 1 - A + M = 50 + 1 - 33{,}11 + 0{,}04536 = 17{,}93536 \qquad \frac{A}{17{,}93536} = \frac{33{,}11}{17{,}93536} = 1{,}8461
$$

$$
z = 1 - M + 1{,}8461 = 1 - 0{,}04536 + 1{,}8461 = 2{,}8007 \quad \text{(relación varianza/media, sin unidad)}
$$

$$
V = M \times z = 0{,}04536\ \text{Erlangs} \times 2{,}8007 = 0{,}1270\ \text{Erlangs}^2
$$

### c) Intensidad de tráfico equivalente ($A^*$)

Rapp:

$$
A^* = V + 3z(z-1)
$$

Primero el término $3z(z-1)$:

$$
3z(z-1) = 3\,(2{,}8007)\,(1{,}8007) = 8{,}4021 \times 1{,}8007 = 15{,}130
$$

$$
A^* = 0{,}1270 + 15{,}130 = 15{,}257\ \text{Erlangs}
$$

### d) Circuitos parciales requeridos ($N^*$)

Rapp:

$$
N^* = \frac{A^*(M+z)}{M+z-1} - (M+1)
$$

Primero los términos: $M + z = 0{,}04536 + 2{,}8007 = 2{,}8461$ y $M + z - 1 = 1{,}8461$.

$$
N^* = 15{,}257 \times \frac{2{,}8461}{1{,}8461} - 1{,}04536 = 15{,}257 \times 1{,}5417 - 1{,}04536 = 23{,}521 - 1{,}045 = 22{,}48\ \text{circuitos}
$$

### Resumen

| Parámetro | Símbolo | Valor | Unidad |
|---|:---:|---:|---|
| a) Media del tráfico (desborde) | $M$ | 0,0454 | Erlangs |
| b) Varianza del tráfico | $V$ | 0,1270 | $\text{Erlangs}^2$ |
| c) Intensidad de tráfico equivalente | $A^*$ | 15,26 | Erlangs |
| d) Circuitos parciales requeridos | $N^*$ | 22,48 | circuitos |

Nota: $N^*$ no se redondea, se conserva con decimales para el cálculo posterior de la troncal común.





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

$$
D = \frac{4{,}1667^0}{0!} + \frac{4{,}1667^1}{1!} + \frac{4{,}1667^2}{2!} + \frac{4{,}1667^3}{3!} + \frac{4{,}1667^4}{4!}
$$

| $k$ | $A^k$ | $k!$ | $A^k/k!$ |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1,0000 |
| 1 | 4,1667 | 1 | 4,1667 |
| 2 | 17,3611 | 2 | 8,6806 |
| 3 | 72,3380 | 6 | 12,0563 |
| 4 | 301,4083 | 24 | 12,5587 |

$$
D = 1 + 4{,}1667 + 8{,}6806 + 12{,}0563 + 12{,}5587 = \mathbf{38{,}4622}
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

**c) Congestión en el tiempo:**

$$
E = P(N) = P(4) = \mathbf{0{,}32652} \quad (\mathbf{32{,}652\%})
$$

**d) Congestión en las llamadas:** en Poisson coincide con la del tiempo, $B = E = 0{,}3265$ (32,65 %).

**f) Tráfico cursado:**

$$
A' = A(1-B) = 4{,}1667\ \text{Erlangs} \times (1 - 0{,}32652) = 4{,}1667\ \text{Erlangs} \times 0{,}67348 = 2{,}8062\ \text{Erlangs}
$$

**g) Tráfico rechazado:**

$$
M = A \cdot B = 4{,}1667\ \text{Erlangs} \times 0{,}32652 = 1{,}3605\ \text{Erlangs}
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

Cada coeficiente binomial sale de $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$; por ejemplo, $\binom{100}{4} = \dfrac{100 \cdot 99 \cdot 98 \cdot 97}{4!} = 3\,921\,225$. Con $b^j = (1/24)^j$:

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

**Congestión en el tiempo:** $E = P(4) = 0{,}3171$ (31,71 %).

**Congestión en las llamadas** (se calcula con $F-1 = 99$ fuentes, porque la fuente que origina la llamada no puede estar ocupada):

| $j$ | $\binom{99}{j}$ | $\binom{99}{j}\,b^j$ |
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
B = \frac{\binom{99}{4}\,b^4}{\displaystyle\sum_{k=0}^{4}\binom{99}{k}\,b^k} = \frac{11{,}3461}{36{,}2391} = 0{,}3131 \quad (31{,}31\%)
$$

**Tráfico cursado** (canales ocupados en promedio):

$$
A' = \sum_{j=0}^{4} j\,P(j) = 0(0{,}0268) + 1(0{,}1118) + 2(0{,}2305) + 3(0{,}3138) + 4(0{,}3171) = 0{,}1118 + 0{,}4611 + 0{,}9414 + 1{,}2682 = 2{,}7825\ \text{Erlangs}
$$

**Tráfico ofrecido:**

$$
A = \frac{A'}{1-B} = \frac{2{,}7825\ \text{Erlangs}}{1 - 0{,}3131} = \frac{2{,}7825\ \text{Erlangs}}{0{,}6869} = 4{,}0507\ \text{Erlangs}
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

| Ítem                         | Erlang B (principal) | Engset (100 fuentes) |
| ---------------------------- | -------------------: | -------------------: |
| $P(0)$                       |               2,60 % |               2,68 % |
| $P(1)$                       |              10,83 % |              11,18 % |
| $P(2)$                       |              22,57 % |              23,05 % |
| $P(3)$                       |              31,35 % |              31,38 % |
| $P(4)$                       |              32,65 % |              31,71 % |
| Congestión en el tiempo      |              32,65 % |              31,71 % |
| Congestión en las llamadas   |              32,65 % |              31,31 % |
| Tráfico ofrecido             |       4,1667 Erlangs |       4,0507 Erlangs |
| Tráfico cursado              |       2,8062 Erlangs |       2,7825 Erlangs |
| Tráfico rechazado            |       1,3605 Erlangs |       1,2682 Erlangs |
| Llamadas rechazadas por hora |               979,56 |                913,1 |

Nota: confirmar con la cátedra cuál de los dos modelos se usa. Con el enunciado tal cual (tasa constante) corresponde Erlang B; si las 100 fuentes son el dato clave, se usa Engset.


