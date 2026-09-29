# Ejercicio 1 2026

Si el código del país es 403 y el código de la ciudad es 33, para realizar una llamada internacional desde Bolivia cual es el procedimiento establecido para las llamadas al exterior, realizar la llamada.

---

## Solución

Se aplica el **Plan Fundamental de Numeración de 15 dígitos**. Según el formulario, la llamada internacional saliente es:

$$
00 + \text{Código Carrier} + \text{Código de País} + \text{Número de teléfono}
$$

donde el número de teléfono incluye el código de ciudad (dígitos 7 y 8) y el número de abonado (zona, central y usuario).

| Campo | Dígitos del plan | Cantidad | Valor |
| ----- | :--------------: | :------: | ----- |
| Acceso internacional | 14 y 15 | 2 | `00` |
| Código del Carrier | 12 y 13 | 2 | `10` (supuesto: ENTEL) |
| Código de país | 9, 10 y 11 | 3 | `403` |
| Código de ciudad / región | 7 y 8 | 2 | `33` |
| Zona | 6 | 1 | `1` (ej.) |
| Central | 5 | 1 | `2` (ej.) |
| Usuario | 1, 2, 3 y 4 | 4 | `3456` (ej.) |

Check: 2 + 2 + 3 + 2 + 1 + 1 + 4 = **15 dígitos**.

Supuestos: el enunciado no da el carrier ni el número de abonado; se toma ENTEL (`10`) y el abonado `123456` como ejemplo.

**Marcación:** `00 10 403 33 1 2 3456` → `001040333123456`

---

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

**Método:** el desborde es tráfico "a ráfagas" (varianza mayor que la media), por eso no basta sumar medias: se suman **media y varianza** de ambos desbordes (Wilkinson) y se aplican las aproximaciones de Rapp. Notación de las diapositivas: $A_i$ y $C_i$ = tráfico ofrecido y canales de la ruta directa $i$; $m_i$, $v_i$ = media y varianza de su desborde; $M$, $V$ = media y varianza combinadas; $A$ y $C$ (sin subíndice) = tráfico y canales equivalentes de Rapp; $N_{AT}$ = canales hacia la central de tránsito; $B_2$ = pérdida permitida en la ruta de tránsito.

### 1. Media del desborde

$$
m_i = A_i \cdot E(C_i, A_i)
$$

Aquí el porcentaje de desborde del enunciado es el dato de $E(C_i,A_i)$:

$$
m_{AB} = 73\ \text{Erlangs} \times 0{,}179 = 13{,}067\ \text{Erlangs}
$$

$$
m_{AC} = 65\ \text{Erlangs} \times 0{,}1077 = 7{,}0005\ \text{Erlangs}
$$

$$
M = \sum_{i=1}^{r} m_i = 13{,}067 + 7{,}0005 = 20{,}0675\ \text{Erlangs}
$$

### 2. Varianza de cada desborde (Riordan)

$$
v_i = m_i\left(1 - m_i + \frac{A_i}{C_i + 1 - A_i + m_i}\right)
$$

Unidades: $m_i$ y $A_i$ en Erlangs; $v_i$ en $\text{Erlangs}^2$; $C_i$ en canales.

**Aplicación literal con los canales del enunciado ($C_{AB}=51$, $C_{AC}=46$):** el denominador resulta negativo ($51 + 1 - 73 + 13{,}067 = -7{,}933$ y $46 + 1 - 65 + 7{,}0005 = -10{,}9995$) y se obtiene $v_{AB} \approx -277{,}9$, $v_{AC} \approx -83{,}4$, es decir $V \approx -361{,}3\ \text{Erlangs}^2$. Una varianza negativa no tiene sentido físico: los datos del enunciado no son coherentes con Erlang B ($E(73,51) = 32{,}7\%$ y $E(65,46) = 32{,}1\%$, no 17,9 % y 10,77 %).

**Recurso usado para continuar (no está en el formulario):** se reemplaza $C_i$ por $C'_i$, los canales equivalentes que producen el bloqueo medido, es decir $E(A_i, C'_i) = B_i$. Se obtiene con la recurrencia de Erlang B,

$$
E(A,n) = \frac{A\,E(A,n-1)}{n + A\,E(A,n-1)}, \qquad E(A,0) = 1
$$

y se interpola entre los dos valores enteros de $n$ que encierran el bloqueo medido:

- Para $A_{AB} = 73\ \text{Erlangs}$ y $B = 0{,}179$: $E(73;63) = 0{,}1855$ y $E(73;64) = 0{,}1746$, luego

$$
C'_{AB} = 63 + \frac{0{,}1855 - 0{,}179}{0{,}1855 - 0{,}1746} = 63 + \frac{0{,}0065}{0{,}0109} = 63{,}60\ \text{canales}
$$

- Para $A_{AC} = 65\ \text{Erlangs}$ y $B = 0{,}1077$: $E(65;63) = 0{,}1121$ y $E(65;64) = 0{,}1022$, luego

$$
C'_{AC} = 63 + \frac{0{,}1121 - 0{,}1077}{0{,}1121 - 0{,}1022} = 63 + \frac{0{,}0044}{0{,}0099} = 63{,}44\ \text{canales}
$$

Desborde A→B, paso a paso:

$$
C'_{AB} + 1 - A_{AB} + m_{AB} = 63{,}60 + 1 - 73 + 13{,}067 = 4{,}667 \qquad \frac{A_{AB}}{4{,}667} = \frac{73}{4{,}667} = 15{,}6417
$$

$$
1 - m_{AB} + 15{,}6417 = 1 - 13{,}067 + 15{,}6417 = 3{,}5747
$$

$$
v_{AB} = m_{AB} \times 3{,}5747 = 13{,}067 \times 3{,}5747 = 46{,}71\ \text{Erlangs}^2
$$

Desborde A→C, paso a paso:

$$
C'_{AC} + 1 - A_{AC} + m_{AC} = 63{,}44 + 1 - 65 + 7{,}0005 = 6{,}4405 \qquad \frac{A_{AC}}{6{,}4405} = \frac{65}{6{,}4405} = 10{,}0924
$$

$$
1 - m_{AC} + 10{,}0924 = 1 - 7{,}0005 + 10{,}0924 = 4{,}0919
$$

$$
v_{AC} = m_{AC} \times 4{,}0919 = 7{,}0005 \times 4{,}0919 = 28{,}65\ \text{Erlangs}^2
$$

Las varianzas se suman:

$$
V = \sum_{i=1}^{r} v_i = 46{,}71 + 28{,}65 = 75{,}36\ \text{Erlangs}^2
$$

### 3. Aproximaciones de Rapp ($A$ y $C$ equivalentes)

Relación varianza/media:

$$
\frac{V}{M} = \frac{75{,}36}{20{,}0675} = 3{,}755 \quad \text{(sin unidad)}
$$

Tráfico equivalente:

$$
A = V + 3\,\frac{V}{M}\left(\frac{V}{M} - 1\right)
$$

Primero el término $3\,\frac{V}{M}\left(\frac{V}{M}-1\right) = 3\,(3{,}755)\,(2{,}755) = 11{,}265 \times 2{,}755 = 31{,}04$:

$$
A = 75{,}36 + 31{,}04 = 106{,}40\ \text{Erlangs}
$$

Canales equivalentes:

$$
C = \frac{A\left(M + \frac{V}{M}\right)}{M + \frac{V}{M} - 1} - M - 1
$$

Primero los términos: $M + V/M = 20{,}0675 + 3{,}755 = 23{,}8225$ y $M + V/M - 1 = 22{,}8225$.

$$
C = 106{,}40 \times \frac{23{,}8225}{22{,}8225} - 20{,}0675 - 1 = 106{,}40 \times 1{,}0438 - 21{,}0675 = 111{,}06 - 21{,}07 = 89{,}99\ \text{canales}
$$

### 4. Canales hacia la central de tránsito T ($N_{AT}$)

Nuevo grado de pérdida sobre el desborde, con $B_2 = 0{,}5\%$:

$$
\text{nuevo } B = E(N_{AT} + C,\,A) = B_2\,\frac{M}{A} = \frac{0{,}005 \times 20{,}0675\ \text{Erlangs}}{106{,}40\ \text{Erlangs}} = \frac{0{,}1003}{106{,}40} = 9{,}43\times10^{-4}
$$

Con $A = 106{,}40\ \text{Erlangs}$ se busca el menor número de canales totales que cumpla (Erlang B, tabla o recurrencia): $N = 135\ \text{canales} \to 9{,}98\times10^{-4}$ (no cumple, es mayor que $9{,}43\times10^{-4}$) y $N = 136\ \text{canales} \to 7{,}8\times10^{-4}$ (cumple), luego $N_{AT} + C = 136\ \text{canales}$.

$$
N_{AT} = (N_{AT} + C) - C = 136\ \text{canales} - 89{,}99\ \text{canales} = 46{,}01\ \text{canales}
$$

$N_{AT} \approx 46{,}0$ canales; como debe ser entero y el valor supera ligeramente 46, se toman 47 canales por seguridad.

**Resultado: T necesita 47 canales.**

### Notas

- La varianza de cada desborde no se puede obtener con el formulario tal cual (da negativa, ver paso 2); el uso de $C'_i$ es un recurso propio, no del formulario.
- El resultado es sensible al redondeo de $C'$: con $C'$ redondeado a 63,6 y 63,4 sale $N_{AT} + C = 137$ y $N_{AT} = 46{,}1$; sin redondeos intermedios, $N_{AT} = 45{,}6$. La respuesta queda entre 46 y 47 canales; se toma 47 para no quedar por debajo del grado de servicio.
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

**Método:** el grupo primario $E(A_1, C_1)$ deja desbordar una parte pequeña del tráfico, y ese desborde no es de Poisson. Se calculan su media $M$ y su varianza $V$ (Riordan) y se reemplaza por un sistema equivalente $(A, C)$ con las aproximaciones de Rapp.

**Notación de las diapositivas:** $A_1$ = tráfico ofrecido al grupo primario y $C_1 = 50$ = sus canales reales; $M$ y $V$ = media y varianza del desborde; $A$ y $C$ (sin subíndice) = tráfico y circuitos equivalentes de Rapp.

### Paso previo: tráfico ofrecido $A_1$

Se busca $A_1$ tal que $E(C_1, A_1) = E(50, A_1) = 0{,}001370$ (tabla de Erlang B; aquí se calcula con la recurrencia como herramienta de cálculo):

$$
E(A,n) = \frac{A\,E(A,n-1)}{n + A\,E(A,n-1)}, \qquad E(A,0) = 1
$$

Se evalúa $n = 50$ para dos valores de $A$ que encierran el bloqueo dado: $E(33{,}1;\,50) = 0{,}001362$ y $E(33{,}2;\,50) = 0{,}001433$. Interpolando:

$$
A_1 = 33{,}1 + 0{,}1\times\frac{0{,}001370 - 0{,}001362}{0{,}001433 - 0{,}001362} = 33{,}1 + 0{,}1\times\frac{0{,}000008}{0{,}000071} = 33{,}11\ \text{Erlangs}
$$

Comprobación: $E(33{,}11;\,50) = 0{,}001369 \approx 0{,}001370$.

### a) Media del tráfico ($M$)

Es el tráfico que desborda del grupo primario:

$$
M = A_1 \cdot E(C_1, A_1) = 33{,}11\ \text{Erlangs} \times 0{,}001370 = 0{,}04536\ \text{Erlangs}
$$

### b) Varianza del tráfico ($V$)

Fórmula de Riordan:

$$
V = M\left(1 - M + \frac{A_1}{C_1 + 1 - A_1 + M}\right)
$$

Paso a paso:

$$
C_1 + 1 - A_1 + M = 50 + 1 - 33{,}11 + 0{,}04536 = 17{,}93536 \qquad \frac{A_1}{17{,}93536} = \frac{33{,}11}{17{,}93536} = 1{,}8461
$$

$$
\frac{V}{M} = 1 - M + 1{,}8461 = 1 - 0{,}04536 + 1{,}8461 = 2{,}8007 \quad \text{(relación varianza/media, sin unidad)}
$$

$$
V = M \times \frac{V}{M} = 0{,}04536\ \text{Erlangs} \times 2{,}8007 = 0{,}1270\ \text{Erlangs}^2
$$

### c) Intensidad de tráfico del sistema ($A$, Rapp)

$$
A = V + 3\,\frac{V}{M}\left(\frac{V}{M} - 1\right)
$$

Primero el término $3\,\frac{V}{M}\left(\frac{V}{M}-1\right) = 3\,(2{,}8007)\,(1{,}8007) = 8{,}4021 \times 1{,}8007 = 15{,}130$:

$$
A = 0{,}1270 + 15{,}130 = 15{,}257\ \text{Erlangs}
$$

### d) Circuitos parciales requeridos ($C$, Rapp)

$$
C = \frac{A\left(M + \frac{V}{M}\right)}{M + \frac{V}{M} - 1} - M - 1
$$

Primero los términos: $M + V/M = 0{,}04536 + 2{,}8007 = 2{,}8461$ y $M + V/M - 1 = 1{,}8461$.

$$
C = 15{,}257 \times \frac{2{,}8461}{1{,}8461} - 0{,}04536 - 1 = 15{,}257 \times 1{,}5417 - 1{,}045 = 23{,}521 - 1{,}045 = 22{,}48\ \text{circuitos}
$$

### Resumen

| Parámetro | Símbolo | Valor | Unidad |
|---|:---:|---:|---|
| a) Media del tráfico (desborde) | $M$ | 0,0454 | Erlangs |
| b) Varianza del tráfico | $V$ | 0,1270 | $\text{Erlangs}^2$ |
| c) Intensidad de tráfico (Rapp) | $A$ | 15,26 | Erlangs |
| d) Circuitos parciales requeridos | $C$ | 22,48 | circuitos |

Nota: $C$ no se redondea, se conserva con decimales para el cálculo posterior de la troncal común.

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
