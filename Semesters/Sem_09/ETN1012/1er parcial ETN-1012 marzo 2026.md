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