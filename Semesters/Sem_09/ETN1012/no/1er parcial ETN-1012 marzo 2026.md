# Ejercicio 1 2026

Si el código del país es 403 y el código de la ciudad es 33, para realizar una llamada internacional desde Bolivia cual es el procedimiento establecido para las llamadas al exterior, realizar la llamada.

---

## 1 Planteamiento del Problema
Se requiere establecer el procedimiento normado y la estructura de marcación para realizar
una llamada internacional desde Bolivia hacia un destino extranjero, dados los siguientes datos
técnicos de destino:
- Código del país destino: 403
- Código de la ciudad/área: 33
## 2 Procedimiento Establecido (Plan de Numeración)
De acuerdo con el Plan Fundamental de Numeración y los esquemas de enrutamiento de cen-
trales en Bolivia, el formato estándar para cursar llamadas de Larga Distancia Internacional
(LDI) requiere el uso de un prefijo de salida internacional, seguido del código de identificación
del operador portador (carrier) elegido por el usuario, y finalmente los códigos de destino.
La estructura general y lógica de marcación es la siguiente:

00 + Id del Operador + Código de País + Código de Ciudad + Número de Abonado

Donde cada parámetro cumple una función en la sincronización y enrutamiento de la red:
- 00: Es el prefijo de acceso estándar para llamadas internacionales salientes desde Bolivia.
- Id del Operador: Es el código de dos dígitos (formato 1X) asignado a la empresa de tele-
comunicaciones de larga distancia.
- Código de País: Identificativo numérico asignado al país destino (para este caso, 403).
- Código de Ciudad: Código de zona o ciudad destino (para este caso, 33).
- Número de Abonado: La numeración del equipo terminal final.

## 3 Solución y Regla de Marcación Aplicada
Aplicando los datos específicos proporcionados en el planteamiento, la secuencia exacta que el
usuario debe marcar o enviar a la central de conmutación es:

00 - 1X - 403 - 33 - [Número del Abonado]

Ejemplo Práctico de Enrutamiento
Si el abonado que origina la llamada decide utilizar la red del operador ENTEL (cuyo código de
portador es 10) y el número local de la persona en la ciudad destino es 1234567, la marcación
integral a realizar será:

00 10 403 33 1234567

Tabla de Referencia: Códigos de Operadores de Larga Distancia
Para reemplazar el valor 1X en la fórmula de marcación, el origen debe seleccionar una ruta
válida mediante los siguientes códigos:

| Operador (Carrier) | Código de Larga Distancia (1X) |
| ------------------ | ------------------------------ |
| ENTEL              | 10                             |
| NUEVATEL (VIVA)    | 11                             |
| TELECEL (TIGO)     | 12                             |
| COTAS              | 13                             |
| AXS Bolivia        | 17                             |

## 4 Conclusión
El procedimiento para cursar la llamada al exterior con los códigos dados consiste estrictamente
en anteponer la secuencia de escape de salida internacional (00) y el selector de operador (1X),
antes de ingresar los identificadores del país (403) y ciudad (33). Esta estructura garantiza que
la central conmute correctamente los trenes de bits hacia la troncal internacional adecuada


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

## Dimensionamiento de Central de Tránsito (Desborde)

### Resolución de Ejercicio Práctico

## 1. Datos del Problema

Una empresa de servicios de telefonía opera con cuatro centrales: tres centrales locales (A, B, C) y una central de tránsito (T). Las mediciones de la hora cargada arrojan los siguientes resultados:

### Ruta Directa A → B

- Tráfico total ofrecido ($A_{AB}$): 73 Erlangs
- Porcentaje de desborde: 17.0%
- Canales directos instalados ($N_{AB}$): 51 canales

### Ruta Directa A → C

- Tráfico total ofrecido ($A_{AC}$): 65 Erlangs
- Porcentaje de desborde: 10.77%
- Canales directos instalados ($N_{AC}$): 40 canales

### Requisitos de Calidad de Servicio

- Grado de servicio requerido (Probabilidad de Bloqueo): $B = 0.5\%$ (es decir, $E = 0.005$).

> **Nota:** Se asume que el texto original "8+0,5%" corresponde a un error tipográfico de reconocimiento óptico (OCR) para "B=0,5%", estándar en el dimensionamiento Erlang B.

---

## 2. Cálculo del Tráfico de Desborde

En un esquema de enrutamiento alternativo, el tráfico que no encuentra canales libres en la ruta directa de alto uso rebalsa y es enviado por una ruta alternativa a través de la central de tránsito T.

Procedemos a calcular el volumen de tráfico de desborde ($D$) para cada ruta:

### Desborde de la ruta A-B ($D_{AB}$)

$$
D_{AB} = A_{AB} \times \left(\frac{\%\,\text{Desborde}}{100}\right)
$$

$$
D_{AB} = 73\ \text{Erl} \times 0.170 = 12.41\ \text{Erlangs}
$$

### Desborde de la ruta A-C ($D_{AC}$)

$$
D_{AC} = A_{AC} \times \left(\frac{\%\,\text{Desborde}}{100}\right)
$$

$$
D_{AC} = 65\ \text{Erl} \times 0.1077 = 7.0005\ \text{Erlangs} \approx 7.00\ \text{Erlangs}
$$

---

## 3. Tráfico Total Ofrecido a la Central de Tránsito

La central de tránsito T tiene la función de absorber todo el tráfico que ha sido bloqueado en las rutas directas para poder completar las llamadas. El tráfico total ofrecido a la troncal de tránsito ($A_T$) es la suma algebraica de los desbordes:

$$
A_T = D_{AB} + D_{AC}
$$

$$
A_T = 12.41\ \text{Erl} + 7.00\ \text{Erl}
= 19.41\ \text{Erlangs}
$$

---

## 4. Dimensionamiento de la Central de Tránsito

Para determinar el número de canales o circuitos ($N_T$) necesarios hacia la central de tránsito, utilizamos el modelo de Erlang B, buscando que para un tráfico de $A = 19.41$ Erlangs, la probabilidad de bloqueo sea menor o igual a $0.005$.

La fórmula teórica de Erlang B es:

$$
E(N,A) =
\frac{\dfrac{A^N}{N!}}
{\displaystyle\sum_{i=0}^{N}\frac{A^i}{i!}}
\leq 0.005
$$

Evaluando en las tablas estándar de Erlang B para $A = 19.41$ Erl, buscamos la cantidad de canales $N$:

- Para $N = 29$ canales → $E \approx 0.0084$ (Bloqueo del 0.84% - No cumple, es mayor a 0.5%).
- Para $N = 30$ canales → $E \approx 0.0053$ (Bloqueo del 0.53% - No cumple, está ligeramente por encima).
- Para $N = 31$ canales → $E \approx 0.0033$ (Bloqueo del 0.33% - Sí cumple, garantiza la descongestión exigida).

---

## 5. Conclusión

Para garantizar que las llamadas de desborde desde las centrales locales puedan completarse cumpliendo con el estricto grado de servicio del 0.5%, la central de tránsito T debe disponer de al menos **31 canales** para absorber eficientemente los **19.41 Erlangs** de tráfico acumulado.

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

