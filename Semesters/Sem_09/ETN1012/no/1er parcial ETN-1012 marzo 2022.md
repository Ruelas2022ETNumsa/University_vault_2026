# Ejercicio 1 2022
Explicar de forma sencilla el concepto de sincronización. (10 puntos).

---

En las redes de telefonía digital, la **sincronización** es el proceso fundamental de coordinar el tiempo (temporización) tanto para la transmisión de **bits** como para la organización de las **tramas** de datos. Su objetivo principal es evitar desajustes de tiempo conocidos como **deslizamientos** durante la comunicación.

Para lograr que toda la red trabaje de manera coordinada, el proceso se realiza mediante la siguiente estructura:

* **Jerarquía de Relojes (Master y Esclavos)**: Cada central telefónica cuenta con un reloj que establece su base de tiempo. Dentro de la red, la **central madre** posee el **reloj master (maestro)**, mientras que las demás centrales actúan como **esclavas** y deben sincronizarse obligatoriamente con el reloj master. Esta jerarquía permite monitorear y controlar la **tasa de deslizamiento** del sistema.
* **Funciones de la Base de Tiempo**: Una vez coordinada la base de tiempo, cumple dos funciones operativas clave en la central:
  1. **Recepción**: Permite recibir correctamente los trenes de bits que provienen de otras centrales digitales.
  2. **Envío y Conmutación**: Controla los equipos de la central para conmutar y enviar los trenes de bits de forma ordenada hacia otras centrales o hacia los abonados (usuarios finales).

# Ejercicio 2 2022
Explicar el concepto del plan de numeración con un ejemplo para una llamada internacional a cualquier país de Bolivia. (10 puntos).

---

El **plan de numeración** es un plan técnico fundamental que tiene como función principal **identificar inequívocamente a cada abonado** dentro de la red telefónica, permitiendo que las llamadas se conecten de manera precisa a su destino sin riesgo de confusión.

Para estructurar los números a escala global y nacional, este plan utiliza una jerarquía de hasta **15 dígitos**.

### Estructura del Plan de Numeración (15 Dígitos)

El esquema de 15 dígitos desglosa la llamada desde el nivel internacional hasta el usuario final:

1. **Dígitos 15 y 14 (Acceso)**: Corresponden a los ceros de acceso. Se utiliza un cero (`0`) para llamadas nacionales y dos ceros (`00`) para llamadas internacionales.
2. **Dígitos 13 y 12 (Carrier)**: Identifican el código de la empresa u operador de transporte de información (por ejemplo, `10` para ENTEL o `16` para COTEL).
3. **Dígitos 11, 10 y 9 (Código de País)**: Conforman el código internacional del país de destino (por ejemplo, `591` para Bolivia).
4. **Dígitos 8 y 7 (Departamento o Región)**: Pertenecen al código específico del departamento o región de destino.
5. **Dígitos 6 al 1 (Central y Usuario)**: Identifican la central de zona y el número específico del abonado.

### Ejemplo de Llamada Internacional

Siguiendo el plan de 15 dígitos, si se realiza una llamada internacional hacia la ciudad de La Paz, Bolivia, dirigida al número local `2794040`, la marcación se realiza en el siguiente orden:

* **Acceso internacional (Dígitos 15 y 14)**: Marcar `00`.
* **Código de Carrier (Dígitos 13 y 12)**: Marcar `10` o `16`.
* **Código de País (Dígitos 11, 10 y 9)**: Marcar `591` (código de Bolivia).
* **Código de Departamento (Dígitos 8 y 7)**: Marcar `22`.
* **Número de abonado (Dígitos 6 al 1)**: Marcar `794040`.

Al contabilizar la secuencia completa $**`00 + 10 + 591 + 22 + 794040`**$, se emplean exactamente los **15 dígitos** del plan de numeración para enrutar la llamada correctamente.

# Ejercicio 3 2022
¿El plan de señalización que contenidos básicos debe tener? (10 puntos).

---

El **plan de señalización** es un plan técnico fundamental cuyo propósito principal es originar las acciones necesarias en los sistemas de conmutación, alertar al abonado o servicio llamado y establecer la conexión correcta entre el usuario llamante y el llamado.

Para lograr esto, los **contenidos básicos** que debe contemplar un plan de señalización son:

1. **Lista de señales a intercambiar**: Definición explícita de todas las señales que se transmiten en la red, distinguiendo entre el intercambio entre abonado y central (y viceversa) y el intercambio entre distintas centrales.
2. **Tipos de señalización implementados**: Descripción de las arquitecturas de señalización utilizadas en la red, principalmente la **señalización por canal común** (como el sistema SS7 / SCC7) y la **señalización por canal asociado** $CAS$.
3. **Señalización entre abonado y central (y viceversa)**: Definición de los métodos de marcación y tonos utilizados por el usuario hacia la central (como la marcación por multifrecuencia o por pulsos) y las señales de estado enviadas desde la central al usuario (tono de invitación a marcar, tono de llamada, etc.).

# Ejercicio 4 2022
De la gráfica de circuitos de ocupación individual; dibujar la ocupación simultánea, calcular el tráfico cursado y calcular el congestionamiento en el tiempo. (20 puntos).

![[Ejercicio 4 2022-28-09-2026_18-02-52.png]]

---



# Ejercicio 5 2022
Con los datos E $-,60$ y una calidad de servicio 0.002, determinar la Media, Varianza, Tráfico y numero de Canales. (25 puntos)

---

Para determinar la **Media ($M$)**, la **Varianza ($V$)**, el **Tráfico ($A$)** y el **Número de Canales ($C$)**, utilizamos las fórmulas de la teoría de tráfico de desbordamiento (Teoría del Equivalente Aleatorio de Wilkinson) y las tablas de Erlang B.

En la notación estándar de tráfico telefónico, la probabilidad de pérdida de Erlang B se denota como $E(C, A)$, donde $C$ representa el número de canales y $A$ el tráfico ofrecido en Erlangs.

### Fórmulas Base

1. **Media ($M$)**:
   
$$
M = A \cdot E(C, A)
$$


2. **Varianza ($V$)**:
   
$$
V = M \cdot \left(1 - M + \frac{A}{C + 1 - A + M}\right)
$$

### Caso 1: Si $C = 60$ canales y $E = 0.002$

Si el valor dado $60$ corresponde al número de canales $$C = 60$$ con una calidad de servicio de $E = 0.002$:

1. **Tráfico ofrecido ($A$)**:
   Consultando la **Tabla 3 de Erlang B** (*"$E$ y $A_o$ dado $n$"*) para $n = 60$ canales y una probabilidad de pérdida $E = 0.0020$, se obtiene un tráfico de **$A = 42.35\text{ Erlangs}$**.

2. **Cálculo de la Media ($M$)**:
   
$$
M = 42.35 \times 0.002 = \mathbf{0.0847\text{ Erlangs}}
$$


3. **Cálculo de la Varianza ($V$)**:
   
$$
V = 0.0847 \cdot \left(1 - 0.0847 + \frac{42.35}{60 + 1 - 42.35 + 0.0847}\right)
$$

   
$$
V = 0.0847 \cdot \left(0.9153 + \frac{42.35}{18.7347}\right) = 0.0847 \cdot (0.9153 + 2.2605) = \mathbf{0.2690\text{ Erlangs}^2}
$$


**Resumen Caso 1**:
* **Tráfico ($A$)**: $42.35\text{ Erlangs}$
* **Número de Canales ($C$)**: $60\text{ canales}$
* **Media ($M$)**: $0.0847\text{ Erlangs}$
* **Varianza ($V$)**: $0.2690\text{ Erlangs}^2$

### Caso 2: Si $A = 60$ Erlangs y $E = 0.002$

Si el valor dado $60$ corresponde al tráfico ofrecido $$A = 60\text{ Erlangs}$$ con $E = 0.002$:

1. **Número de Canales ($C$)**:
   Consultando la **Tabla 3 de Erlang B** para $A = 60\text{ Erlangs}$ y $E = 0.0020$, se observa que para $n = 81$ canales el tráfico admisible es $A = 59.72\text{ Erlangs}$, y para $n = 82$ canales es $A = 60.60\text{ Erlangs}$. Para garantizar la calidad de servicio $$E \le 0.002$$, se adopta **$C = 82\text{ canales}$**.

2. **Cálculo de la Media ($M$)**:
   
$$
M = 60 \times 0.002 = \mathbf{0.1200\text{ Erlangs}}
$$


3. **Cálculo de la Varianza ($V$)**:
   
$$
V = 0.12 \cdot \left(1 - 0.12 + \frac{60}{82 + 1 - 60 + 0.12}\right)
$$

   
$$
V = 0.12 \cdot \left(0.88 + \frac{60}{23.12}\right) = 0.12 \cdot (0.88 + 2.5952) = \mathbf{0.4170\text{ Erlangs}^2}
$$

   *(Si se utiliza $C = 81$ canales, el resultado de la varianza es $V = 0.4311\text{ Erlangs}^2$)*.

**Resumen Caso 2**:
* **Tráfico ($A$)**: $60.00\text{ Erlangs}$
* **Número de Canales ($C$)**: $82\text{ canales}$ *(o $81$ canales según aproximación)*
* **Media ($M$)**: $0.1200\text{ Erlangs}$
* **Varianza ($V$)**: $0.4170\text{ Erlangs}^2$

# Ejercicio 6 2022
Tenemos 4 centrales A, B, C y T se ha observado que 5256 usuarios ocuparon 51 circuitos, utilizando un tiempo de ocupación media de 50 segundos generando un tráfico de desborde de 13 Erlangs de la central A con destino a la central B, por otro lado, se ha medido el trafico total de la central A con destino a la central C de 65 Erlangs utilizando 46 circuitos, y 504 usuarios utilizaron un tiempo de ocupación media de 50 segundos la ruta de desborde, se pudo verificar el grado de servicio B2 = 0.5%. Determinar el número de circuitos que se necesitan de la central A con destino a la central T (tránsito) para evitar llamadas perdidas que se generan en la central A con destino a la central B y C. (25 puntos) 

---

Para resolver este problema de dimensionamiento mediante la **Teoría del Equivalente Aleatorio de Wilkinson** y las **fórmulas de Rapp**, desglosaremos los cálculos paso a paso utilizando los datos de las rutas directas de la central A hacia las centrales B y C.

---

### Paso 1: Cálculo del Tráfico y Desborde de la Ruta A $\rightarrow$ B

1. **Tráfico ofrecido directo ($A_1$)**:
   
$$
A_1 = \frac{M \cdot H \cdot L}{3600} = \frac{5256 \text{ usuarios} \times 50 \text{ seg}}{3600} = \mathbf{73.00 \text{ Erlangs}} \quad
$$

2. **Canales directos**: $C_1 = 51 \text{ circuitos}$.
3. **Tráfico de desborde medido ($m_1$)**: $m_1 = \mathbf{13.00 \text{ Erlangs}}$.
4. **Tráfico equivalente ($A_{1,eq}$) y Varianza ($v_1$)**:
   Para cumplir la condición de equilibrio $m = A \cdot E(C, A)$, el tráfico equivalente $A_{1,eq}$ que genera un desborde de $13 \text{ Erlangs}$ sobre $51 \text{ circuitos}$ es $A_{1,eq} \approx 60.98 \text{ Erlangs}$.
   
$$
v_1 = m_1 \cdot \left(1 - m_1 + \frac{A_{1,eq}}{C_1 + 1 - A_{1,eq} + m_1}\right) = 13 \cdot \left(1 - 13 + \frac{60.98}{51 + 1 - 60.98 + 13}\right) = \mathbf{41.20 \text{ Erlangs}^2} \quad
$$


---

### Paso 2: Cálculo del Tráfico y Desborde de la Ruta A $\rightarrow$ C

1. **Tráfico ofrecido directo ($A_2$)**: $A_2 = 65.00 \text{ Erlangs}$.
2. **Canales directos**: $C_2 = 46 \text{ circuitos}$.
3. **Tráfico de desborde medido ($m_2$)**:
   
$$
m_2 = \frac{504 \text{ usuarios} \times 50 \text{ seg}}{3600} = \mathbf{7.00 \text{ Erlangs}} \quad
$$

4. **Tráfico equivalente ($A_{2,eq}$) y Varianza ($v_2$)**:
   El tráfico equivalente $A_{2,eq}$ que genera $7 \text{ Erlangs}$ sobre $46 \text{ circuitos}$ es $A_{2,eq} \approx 48.84 \text{ Erlangs}$.
   
$$
v_2 = m_2 \cdot \left(1 - m_2 + \frac{A_{2,eq}}{C_2 + 1 - A_{2,eq} + m_2}\right) = 7 \cdot \left(1 - 7 + \frac{48.84}{46 + 1 - 48.84 + 7}\right) = \mathbf{24.26 \text{ Erlangs}^2} \quad
$$


---

### Paso 3: Tráfico de Desborde Combinado hacia la Central de Tránsito $T$

1. **Media combinada ($M$)**:
   
$$
M = m_1 + m_2 = 13 + 7 = \mathbf{20.00 \text{ Erlangs}} \quad
$$

2. **Varianza combinada ($V$)**:
   
$$
V = v_1 + v_2 = 41.20 + 24.26 = \mathbf{65.45 \text{ Erlangs}^2} \quad
$$

3. **Relación Varianza/Media ($Z$)**:
   
$$
Z = \frac{V}{M} = \frac{65.45}{20.00} = \mathbf{3.2727}
$$


---

### Paso 4: Aplicación de la Fórmula de Rapp

1. **Tráfico equivalente total ($A_{eq}$)**:
   
$$
A_{eq} = V + 3 \cdot Z \cdot (Z - 1) = 65.45 + 3 \cdot (3.2727) \cdot (3.2727 - 1) = \mathbf{87.77 \text{ Erlangs}} \quad
$$

2. **Número de canales equivalentes ($C_{eq}$)**:
   
$$
C_{eq} = \frac{A_{eq} \cdot \left(M + Z\right)}{M + Z - 1} - M - 1 = \frac{87.77 \cdot (20 + 3.2727)}{20 + 3.2727 - 1} - 20 - 1 = \mathbf{70.71 \text{ canales}} \quad
$$


---

### Paso 5: Determinación de Canales Hacia la Central de Tránsito ($N_{AT}$)

1. **Probabilidad de pérdida ajustada ($E_{nuevo}$)** para $B2 = 0.5\% = 0.005$:
   
$$
E_{nuevo} = B2 \cdot \frac{M}{A_{eq}} = 0.005 \cdot \frac{20.00}{87.77} = \mathbf{0.001139} \quad
$$

2. **Canales totales requeridos ($N_{total}$)**:
   Buscando en la **Tabla 3 de Erlang B** con $A = 87.77 \text{ Erlangs}$ y $E \le 0.001139$, se obtienen **$N_{total} = 114 \text{ canales}$**.
3. **Número de circuitos de la Central A a la Central T ($N_{AT}$)**:
   
$$
N_{AT} = N_{total} - C_{eq} = 114 - 70.71 = 43.29 \implies \mathbf{44 \text{ circuitos}} \quad
$$


---

### Resumen del Resultado

Para evitar llamadas perdidas y mantener un grado de servicio de $B2 = 0.5\%$, se necesitan **44 circuitos** de la **central A con destino a la central T (tránsito)**.

*(Nota: Si en tu materia calculan el desborde puramente teórico con Erlang B desde el tráfico offered nominal en lugar de usar los datos medidos de desborde $13$ y $7$ Erlangs, $m_1 = 23.87$ y $m_2 = 20.89$, resultando en $N_{AT} = 72 \text{ circuitos}$)*.
