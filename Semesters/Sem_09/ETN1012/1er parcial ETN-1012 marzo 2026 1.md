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
m_{AB} = 73 \times 0{,}179 = 13{,}067 \qquad m_{AC} = 65 \times 0{,}1077 = 7{,}0005
$$

$$
M = 13{,}067 + 7{,}0005 = 20{,}0675\ \text{Erl}
$$

### 2. Varianza de cada desborde (Riordan)

$$
v = m\left(1 - m + \frac{A}{C' + 1 - A + m}\right)
$$

$C'$ = canales equivalentes que producen el bloqueo medido, es decir $E(A, C') = B$ (Erlang B): $C'_{AB} \approx 63{,}6$ (para $A=73$, $B=0{,}179$) y $C'_{AC} \approx 63{,}4$ (para $A=65$, $B=0{,}1077$).

$$
v_{AB} = 13{,}067\left(1 - 13{,}067 + \frac{73}{63{,}6 + 1 - 73 + 13{,}067}\right) = 13{,}067\,(-12{,}067 + 15{,}642) = 46{,}71
$$

$$
v_{AC} = 7{,}0005\left(1 - 7{,}0005 + \frac{65}{63{,}4 + 1 - 65 + 7{,}0005}\right) = 7{,}0005\,(-6{,}0005 + 10{,}155) = 29{,}09
$$

$$
V = 46{,}71 + 29{,}09 = 75{,}80
$$

### 3. Equivalente de Rapp

$$
z = \frac{V}{M} = \frac{75{,}80}{20{,}0675} = 3{,}777
$$

$$
A^* = V + 3z(z-1) = 75{,}80 + 3(3{,}777)(2{,}777) = 75{,}80 + 31{,}47 = 107{,}27\ \text{Erl}
$$

$$
N^* = \frac{A^*(M+z)}{M+z-1} - M - 1 = 107{,}27\cdot\frac{23{,}845}{22{,}845} - 21{,}0675 = 111{,}96 - 21{,}07 = 90{,}89
$$

### 4. Canales de la central de tránsito T

Pérdida objetivo sobre el desborde:

$$
E(A^*, N_{total}) = \frac{B\,M}{A^*} = \frac{0{,}005 \times 20{,}0675}{107{,}27} = 9{,}35\times10^{-4}
$$

Erlang B con $A^* = 107{,}27$: $N=136 \to 9{,}9\times10^{-4}$ (no cumple) y $N=137 \to 7{,}8\times10^{-4}$ (cumple), luego $N_{total} = 137$.

$$
N_T = N_{total} - N^* = 137 - 90{,}89 = 46{,}1
$$

**Resultado: T necesita 47 canales.**

### Notas

- Los datos no son consistentes con Erlang B: $E(73,51) = 32{,}7\%$ y $E(65,46) = 32{,}1\%$, no 17,9 % y 10,77 %. Por eso se toman los porcentajes medidos como dato y los 51 y 46 canales no intervienen.
- El resultado es sensible al redondeo de $C'$: con decimales exactos salen $N_{total}=136$ y $N_T = 45{,}6$, es decir 46. Se toma 47 para garantizar el grado de servicio.
- Otros métodos: sumar solo las medias y aplicar Erlang B a 20,07 Erl da 32 canales (ignora las ráfagas); usar 51 y 46 canales con Erlang B da ≈ 72. Confirmar cuál usa la cátedra.

# Ejercicio 3 2026

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

## Solución del Problema de Teoría de Colas — Modelo de Engset

## 1. Introducción

En este documento se resuelve un problema de teoría de colas utilizando el modelo de Engset, que es adecuado para sistemas con un número finito de fuentes. Se analiza un sistema de telefonía con 100 fuentes y 4 canales.

## 2. Datos del Problema

- Canales: $C = 4$
- Fuentes: $N = 100$
- Tasa de llegada total: $\lambda = 3000$ llamadas/hora
- Tiempo medio de ocupación: $h = 5$ segundos

$$
h = \frac{5}{3600}\text{ hora}
$$

## 3. Tráfico Ofrecido por Fuente

La tasa de llegada por fuente es:

$$
\alpha = \frac{\lambda}{N}
$$

$$
\alpha = \frac{3000}{100}
$$

$$
\alpha = 30\text{ llamadas/hora/fuente}
$$

El tráfico ofrecido por fuente (en Erlangs):

$$
a = \alpha \cdot h
$$

$$
a = 30 \times \frac{5}{3600}
$$

$$
a = \frac{150}{3600}
$$

$$
a = \frac{1}{24}
$$

$$
a \approx 0,04167\text{ Erl/fuente}
$$

El tráfico total ofrecido:

$$
A = N \cdot a
$$

$$
A = 100 \times \frac{1}{24}
$$

$$
A = \frac{100}{24}
$$

$$
A \approx 4,1667\text{ Erl}
$$

## 4. Expresión General de $P(j)$ — Modelo de Engset

Para fuentes finitas, la distribución de estados es binomial truncada:

$$
P(j) =
\frac{
\binom{N}{j}a^j
}{
\displaystyle\sum_{k=0}^{C}\binom{N}{k}a^k
}
$$

$$
j = 0,1,2,\ldots,C
$$

## 5. Cálculo de los Coeficientes

**Cuadro 1: Cálculo de los términos para $P(j)$**

| $j$ | $\binom{100}{j}$ | $a^j$ | Término |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1.000000 |
| 1 | 100 | $\frac{1}{24}$ | 4.166667 |
| 2 | 4950 | $\left(\frac{1}{24}\right)^2$ | 8.593750 |
| 3 | 161700 | $\left(\frac{1}{24}\right)^3$ | 11.701389 |
| 4 | 3921225 | $\left(\frac{1}{24}\right)^4$ | 11.953776 |

Suma total:

$$
\Sigma = 37,415582
$$

## 6. Probabilidades de Estado

$$
P(0) = \frac{1}{37,4156}
$$

$$
P(0) = 0,02673 \approx 2,67\%
$$

$$
P(1) = \frac{4,16667}{37,4156}
$$

$$
P(1) = 0,11137 \approx 11,14\%
$$

$$
P(2) = \frac{8,59375}{37,4156}
$$

$$
P(2) = 0,22968 \approx 22,97\%
$$

$$
P(3) = \frac{11,70139}{37,4156}
$$

$$
P(3) = 0,31270 \approx 31,27\%
$$

$$
P(4) = \frac{11,95378}{37,4156}
$$

$$
P(4) = 0,31948 \approx 31,95\%
$$

## 7. Congestión en el Tiempo

Es la probabilidad de que todos los canales estén ocupados:

$$
B_t = P(C) = P(4)
$$

$$
B_t = 0,31948 \approx 31,95\%
$$

## 8. Congestión en las Llamadas

En el modelo de Engset, la congestión en las llamadas se calcula usando la distribución con $N-1$ fuentes:

$$
B_c =
\frac{
\binom{N-1}{C}a^C
}{
\displaystyle\sum_{k=0}^{C}\binom{N-1}{k}a^k
}
$$

Con $N-1=99$ fuentes:

$$
B_c =
\frac{11,474843}{36,027100}
$$

$$
B_c = 0,31848 \approx 31,85\%
$$

## 9. Tráfico Cursado y Rechazado

**Tráfico cursado:**

$$
A_c = A\cdot(1-B_c)
$$

$$
A_c = 4,1667\times0,68152
$$

$$
A_c \approx 2,8397\text{ Erl}
$$

**Tráfico rechazado:**

$$
A_r = A\cdot B_c
$$

$$
A_r = 4,1667\times0,31848
$$

$$
A_r \approx 1,3270\text{ Erl}
$$

## 10. Llamadas Rechazadas por Hora

$$
N_r = \lambda\cdot B_c
$$

$$
N_r = 3000\times0,31848
$$

$$
N_r \approx 955\text{ llamadas/hora}
$$

## 11. Resumen de Resultados

**Cuadro 2: Resumen de resultados**

| Ítem | Resultado |
|---|---:|
| $P(0)$ | 2.67 % |
| $P(1)$ | 11.14 % |
| $P(2)$ | 22.97 % |
| $P(3)$ | 31.27 % |
| $P(4)$ | 31.95 % |
| Congestión en el tiempo ($B_t$) | 31.95 % |
| Congestión en llamadas ($B_c$) | 31.85 % |
| Tráfico ofrecido | 4.1667 Erl |
| Tráfico cursado | 2.8397 Erl |
| Tráfico rechazado | 1.3270 Erl |
| Llamadas rechazadas/hora | 955 |

## 12. Conclusión

En este documento se resolvió el problema de teoría de colas utilizando el modelo de Engset, adecuado para sistemas con fuentes finitas. Se calcularon las probabilidades de estado, la congestión en el tiempo y en las llamadas, así como el tráfico cursado y rechazado.

