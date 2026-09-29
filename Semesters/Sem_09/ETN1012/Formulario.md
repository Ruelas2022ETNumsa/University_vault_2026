# Formulario Completo de Ingeniería de Tráfico Telefónico (ETN1012)

Este formulario contiene las definiciones, estructuras y ecuaciones extractadas **únicamente de las diapositivas y documentos cargados** de la asignatura. Se respeta rigurosamente la notación original de las diapositivas.

---

## $a$ Plan de Numeración y Señalización

### 1. Estructura del Plan de Numeración Nacional e Internacional (15 Dígitos)
* **Estructura y notación:**
  * **Plan cerrado a 7 dígitos:** Utilizado para comunicaciones locales dentro de un mismo operador de telefonía fija $ASL$.
  * **8 dígitos:** Para llamadas de teléfono fijo a celular dentro de la misma ciudad.
  * **Nacional:** $0 + \text{Código Carrier} + 591 (\text{Código País}) + \text{Número de abonado}$.
  * **Internacional:** $00 + \text{Código Carrier} + \text{Código de País} + \text{Número de teléfono}$.
* **Significado de cada dígito en la estructura de 15 dígitos:**
  * Dígitos 1, 2, 3, 4: Código del usuario.
  * Dígito 5: Código de la central.
  * Dígito 6: Código de la zona (no se repite en una misma ciudad).
  * Dígitos 7 y 8: Departamento o región del país.
  * Dígitos 9, 10 y 11: Código del país (ej. $591$ para Bolivia).
  * Dígitos 12 y 13: Código del Carrier (transporte de información, ej. $10$ ENTEL, $16$ COTEL).
  * Dígitos 14 y 15: Ceros de acceso de red ($0$ para nacional, $00$ para internacional).
* **Caso de uso:** Identificación inequívoca de abonados y enrutamiento jerárquico a nivel local, nacional e internacional.
* **Fuente:** *"1.- CONCEPTO DE REDES PARA TELEFONIA.pdf"* (Tema: Planes Fundamentales Técnicos) y *"2.- PLANTA INTERNA Y EXTERNA.pdf"* (Tema: Aplicación del Plan de Numeración).

---

### 2. Plan de Señalización
* **Definición y funciones:**
  * Originar acciones en los sistemas de conmutación.
  * Alertar al abonado o servicio llamado.
  * Conectar correctamente al abonado llamante con el llamado.
* **Tipos descritos:** Señalización por canal común **SCC7** y canal asociado; señalización entre abonado y central (discado por pulsos y multifrecuencia).
* **Caso de uso:** Intercambio de señales de control entre abonado-central y central-central.
* **Fuente:** *"1.- CONCEPTO DE REDES PARA TELEFONIA.pdf"* (Tema: Señalización).

---

## $b$ Tráfico: Definiciones y Relaciones

### 1. Volumen de Tráfico ($V$)
* **Fórmula:**
  
$$
V = \sum_{j=1}^n t_j
$$

* **Significado de símbolos y unidades:**
  * $V$: Volumen de tráfico [minutos-Erlang o segundos-Erlang].
  * $t_j$: Tiempo de ocupación de la $j$-ésima toma [minutos o segundos].
  * $n$: Número de tomas o intentos de comunicación.
* **Caso de uso:** Cálculo de la suma acumulada de tiempos de ocupación durante un período de observación $T$.
* **Fuente:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"* (Tema: Ingeniería de Tráfico Básico).

---

### 2. Tasa de Tomas ($i$)
* **Fórmula:**
  
$$
i = \frac{n}{T}
$$

* **Significado de símbolos y unidades:**
  * $i$: Tasa de tomas (escrita también como *"taza de tomas"*) [tomas/minuto o tomas/hora].
  * $n$: Número de tomas.
  * $T$: Período de observación [minutos u horas].
* **Caso de uso:** Medición de la frecuencia de intentos de toma sobre un grupo de circuitos.
* **Fuente:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"*.

---

### 3. Tiempo Medio de Ocupación ($t'$, $H$, $\bar{t}$)
> **Nota de notación doble/triple:** La misma magnitud de tiempo medio de ocupación se escribe de tres formas distintas en las diapositivas: $t'$ en Tráfico Básico, $H$ en Fórmulas de Tráfico y $\bar{t}$ en Tráfico Avanzado.

* **Fórmulas:**
  * Forma 1 ($t'$):
    
$$
t' = \frac{V}{n} = \left( \sum_{j=1}^n t_j \right) \frac{1}{n}
$$

  * Forma 2 ($H$):
    
$$
H \quad \text{[segundos]}
$$

  * Forma 3 ($\bar{t}$):
    
$$
\bar{t} \quad \text{[segundos]}
$$

* **Significado de símbolos y unidades:**
  * $t', H, \bar{t}$: Tiempo medio de ocupación [segundos o minutos por toma].
  * $V$: Volumen de tráfico [minutos-Erlang o segundos-Erlang].
  * $n$: Número de tomas.
* **Caso de uso:** Duración promedio de holding/ocupación de los canales por llamada.
* **Fuentes:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"* ($t'$), *"5.2 FORMULAS DE ING.TRAFICO.pdf"* ($H$) y *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* ($\bar{t}$).

---

### 4. Tráfico Cursado ($A'$, $A^l$)
> **Nota de notación doble:** En las diapositivas de Tráfico Básico se denota como $A'$, mientras que en Tráfico Avanzado y Engset se denota como $A^l$.

* **Fórmulas:**
  * Forma 1 ($A'$):
    
$$
A' = \frac{V}{T} = i \cdot t' = \frac{n \cdot t'}{T}
$$

  * Forma 2 ($A^l$):
    
$$
A^l = A (1 - B)
$$

* **Significado de símbolos y unidades:**
  * $A', A^l$: Tráfico cursado [Erlangs].
  * $V$: Volumen de tráfico [minutos-Erlang].
  * $T$: Período de observación [minutos u horas].
  * $i$: Tasa de tomas.
  * $A$: Tráfico ofrecido [Erlangs].
  * $B$: Congestión en las llamadas.
* **Caso de uso:** Determinación del tráfico real efectivamente procesado por los canales.
* **Fuentes:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"* ($A'$) y *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* ($A^l$).

---

### 5. Tráfico Ofrecido ($A$)
> **Nota de notación múltiple:** Aparecen tres fórmulas distintas según los datos iniciales dados.

* **Fórmulas:**
  * Forma 1 (a partir de tasa de llegada $\lambda$ y tiempo medio $\bar{t}$):
    
$$
A = \lambda \bar{t}
$$

  * Forma 2 (a partir del tráfico cursado $A^l$ y la pérdida $B$):
    
$$
A = \frac{A^l}{1 - B}
$$

  * Forma 3 (a partir de número de usuarios $M$, tiempo $H$ y factor $L$):
    
$$
A = \frac{M \cdot H \cdot L}{3600} \quad \text{[Erlangs]}
$$

* **Significado de símbolos y unidades:**
  * $A$: Tráfico ofrecido [Erlangs].
  * $\lambda$: Tasa de llegada de llamadas [llamadas/hora o llamadas/segundo].
  * $\bar{t}$: Tiempo medio de ocupación [horas o segundos].
  * $A^l$: Tráfico cursado [Erlangs].
  * $B$: Congestión en las llamadas.
  * $M$: Número de usuarios o fuentes libres.
  * $H$: Tiempo medio de ocupación [segundos].
  * $L$: Factor de ocupación ($L = 1$, indicando que al menos una llamada debe cursarse cuando todas las líneas están ocupadas).
* **Caso de uso:** Carga teórica total requerida para el dimensionamiento y diseño del sistema.
* **Fuentes:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"*, *"2.-ING. DE TRAFICO AVANZADO_4.pdf"* y *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

### 6. Tráfico Rechazado ($M$)
> **Nota de ambigüedad de notación:** La letra $M$ se usa en las diapositivas tanto para representar el **Tráfico Rechazado** en sistemas básicos/Engset como para representar la **Media del Tráfico de Desbordamiento** en la teoría de Wilkinson.

* **Fórmula:**
  
$$
M = A - A^l
$$

* **Significado de símbolos y unidades:**
  * $M$: Tráfico rechazado [Erlangs].
  * $A$: Tráfico ofrecido [Erlangs].
  * $A^l$: Tráfico cursado [Erlangs].
* **Caso de uso:** Medida de la intensidad de tráfico que no pudo ser atendida por falta de canales libres.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 7. Número de Llamadas Perdidas ($NLLP$)
* **Fórmula:**
  
$$
NLLP = \frac{M \cdot 3600}{\bar{t}}
$$

* **Significado de símbolos y unidades:**
  * $NLLP$: Número de llamadas perdidas [llamadas/hora].
  * $M$: Tráfico rechazado [Erlangs].
  * $\bar{t}$: Tiempo medio de ocupación [segundos].
  * $3600$: Factor de conversión de segundos a hora.
* **Caso de uso:** Cuantificación horaria de las llamadas rechazadas o caídas.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

## $c$ Erlang B y su Recurrencia

### 1. Probabilidad de Pérdida Erlang B ($P(B)$ o $E(C,A)$)
* **Fórmulas:**
  * Expresión de probabilidad $P(j)$ para el $j$-ésimo canal ocupado:
    
$$
P(j) = \frac{\frac{A^j}{j!}}{\sum_{k=0}^N \frac{A^k}{k!}}
$$

  * Probabilidad de pérdida en $N$ canales ($P(B)$):
    
$$
P(B) = \frac{\frac{A^N}{N!}}{\sum_{k=0}^N \frac{A^k}{k!}}
$$

* **Significado de símbolos y unidades:**
  * $P(B), E(C,A), E(N,A), E_1$: Probabilidad de bloqueo o pérdida de Erlang B [adimensional / porcentaje].
  * $A$: Tráfico ofrecido [Erlangs].
  * $N$ o $C$: Número total de canales del grupo.
  * $j, k$: Estado del sistema (número de canales ocupados).
* **Caso de uso:** Dimensionamiento de grupos de circuitos con fuentes infinitas, tráfico poissoniano y llamadas perdidas eliminadas.
* **Fuentes:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 2. Aclaración sobre la Recurrencia de Erlang B
* **Aclaración directa sobre el contenido de las diapositivas:** La fórmula explícita de recurrencia estándar de Erlang B (dada por $E(N,A) = \frac{A \cdot E(N-1,A)}{N + A \cdot E(N-1,A)}$) **NO se encuentra escrita numéricamente ni algebraicamente en ninguna de las diapositivas del curso**.
* Sin embargo, las diapositivas emplean la relación recursiva de forma implícita para calcular la carga del $j$-ésimo canal usando los términos $E(j-1, A)$ y $E(j, A)$ tabulados.

---

## $d$ Congestión en el Tiempo y Congestión en las Llamadas

### 1. Definiciones en Ingeniería de Tráfico Básico

* **Congestión en el Tiempo ($E$):**
  * **Fórmula:**
    
$$
E = \frac{t}{T}
$$

  * **Símbolos y unidades:**
    * $E$: Congestión en el tiempo [proporción o %].
    * $t$: Suma de los períodos en que **todos los circuitos permanecen ocupados simultáneamente** [minutos o segundos].
    * $T$: Tiempo de observación total [minutos o segundos].
  * **Caso de uso:** Proporción de tiempo en que la totalidad de los circuitos del grupo están saturados.
  * **Fuente:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"*.

* **Congestión en las Llamadas ($B$):**
  * **Fórmula:**
    
$$
B = \frac{P}{N}
$$

  * **Símbolos y unidades:**
    * $B$: Congestión en las llamadas [proporción o %].
    * $P$: Número de intentos de llamadas que encuentran todos los circuitos ocupados.
    * $N$: Suma de las llamadas cursadas + intentos de llamadas perdidas (total de intentos de llamadas).
  * **Caso de uso:** Porcentaje de intentos de llamadas bloqueadas por falta de circuitos.
  * **Fuente:** *"3.- INGENIERIA DE TRAFICO BASICO PARA TELEFONIA.pdf"*.

---

## $e$ Engset / Fuentes Finitas

### 1. Parámetros de Fuentes Libres ($a$ y $b$)
* **Fórmulas:**
  * $a$: Tasa generada por fuente libre [llamadas/segundo].
  * $b$: Tráfico por fuente libre [Erlangs]:
    
$$
b = a \cdot \bar{t}
$$

* **Significado de símbolos y unidades:**
  * $b$: Tráfico generado por cada fuente que se encuentra libre [Erlangs].
  * $a$: Tasa de generación individual [llamadas/segundo].
  * $\bar{t}$: Tiempo medio de ocupación [segundos].
* **Caso de uso:** Condición de entrada para evaluar sistemas con número finito de usuarios $F$.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 2. Función de Probabilidad de Estado $P(j)$ en Engset
* **Fórmula:**
  
$$
P(j) = \frac{\binom{F}{j} b^j}{\sum_{i=0}^N \binom{F}{i} b^i}
$$

* **Significado de símbolos y unidades:**
  * $P(j)$: Probabilidad de que exactamente $j$ canales estén ocupados.
  * $F$: Número total de fuentes u orígenes.
  * $N$: Número de canales del grupo de circuitos.
  * $b$: Tráfico por fuente libre [Erlangs].
  * $\binom{F}{j}$: Combinatoria de $F$ tomado de $j$ en $j$.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 3. Congestión en el Tiempo ($E$) en Engset
* **Fórmula:**
  
$$
E = P(N) = \frac{\binom{F}{N} b^N}{\sum_{i=0}^N \binom{F}{i} b^i}
$$

* **Significado de símbolos y unidades:**
  * $E$: Congestión en el tiempo [adimensional / %].
  * $F$: Número total de fuentes.
  * $N$: Número de canales.
  * $b$: Tráfico por fuente libre [Erlangs].
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 4. Congestión en las Llamadas ($B$) en Engset
* **Fórmula:**
  
$$
B = \frac{\binom{F-1}{N} b^N}{\sum_{J=0}^N \binom{F-1}{J} b^J}
$$

* **Significado de símbolos y unidades:**
  * $B$: Congestión en las llamadas en Engset (donde $B < E$).
  * $F$: Número total de fuentes.
  * $N$: Número de canales.
  * $b$: Tráfico por fuente libre [Erlangs].
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 5. Tráfico Cursado ($A^l$) y Tráfico Ofrecido ($A$) en Engset
* **Fórmulas:**
  * Tráfico Cursado ($A^l$):
    
$$
A^l = \frac{F \cdot b \cdot (1 - B)}{1 + b \cdot (1 - B)}
$$

  * Tráfico Ofrecido ($A$):
    
$$
A = \frac{A^l}{1 - B}
$$

* **Significado de símbolos y unidades:**
  * $A^l$: Tráfico cursado en el modelo de fuentes finitas [Erlangs].
  * $A$: Tráfico ofrecido equivalente [Erlangs].
  * $F$: Número total de fuentes.
  * $b$: Tráfico por fuente libre.
  * $B$: Congestión en las llamadas.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

## $f$ Desborde: Media, Varianza (Riordan) y Tráfico Aleatorio Equivalente (Wilkinson)

### 1. Media del Tráfico de Desbordamiento ($M$)
* **Fórmula:**
  
$$
M = A \cdot E(C, A)
$$

* **Significado de símbolos y unidades:**
  * $M$: Media del tráfico de desbordamiento [Erlangs].
  * $A$: Tráfico poissoniano ofrecido a la ruta de primera elección [Erlangs].
  * $C$: Número de canales de la ruta de primera elección.
  * $E(C,A)$: Probabilidad de pérdida dada por la fórmula Erlang B o Tabla 2.
* **Caso de uso:** Promedio del volumen de tráfico que desborda de un grupo directo de primera elección al no hallar canal libre.
* **Fuente:** *"5.- ING. DE TRAFICO AVANZADO_1.pdf"* y *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

### 2. Varianza del Tráfico de Desbordamiento ($V$) — Fórmula de Riordan
* **Fórmula:**
  
$$
V = M \left( 1 - M + \frac{A}{C + 1 - A + M} \right)
$$

* **Significado de símbolos y unidades:**
  * $V$: Varianza del tráfico de desbordamiento.
  * $M$: Media del tráfico de desbordamiento [Erlangs].
  * $A$: Tráfico poissoniano ofrecido a la ruta de 1ra elección [Erlangs].
  * $C$: Número de canales de la ruta de 1ra elección.
* **Caso de uso:** Caracterización de la variabilidad o "picos" del tráfico no poissoniano que desborda hacia las rutas alternativas.
* **Fuente:** *"5.- ING. DE TRAFICO AVANZADO_1.pdf"* y *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

### 3. Tráfico de Desbordamiento Combinado (Teoría de Wilkinson)
* **Fórmulas:**
  * Media combinada ($M$):
    
$$
M = \sum_{i=1}^r m_i
$$

  * Varianza combinada ($V$):
    
$$
V = \sum_{i=1}^r v_i
$$

  * Donde para cada flujo individual $i$:
    
$$
m_i = A_i \cdot E(C_i, A_i)
$$

    
$$
v_i = m_i \left( 1 - m_i + \frac{A_i}{C_i + 1 - A_i + m_i} \right)
$$

* **Significado de símbolos y unidades:**
  * $M$: Media acumulada total de desborde ofrecida al grupo común [Erlangs].
  * $V$: Varianza acumulada total de desborde.
  * $m_i$: Media del flujo de desborde individual $i$ [Erlangs].
  * $v_i$: Varianza del flujo de desborde individual $i$.
  * $A_i$: Tráfico offered a la $i$-ésima ruta directa de 1ra elección.
  * $C_i$ (escrito también como $N_{AB}, N_{AC}$): Canales del $i$-ésimo grupo de 1ra elección.
  * $r$: Número de rutas directas independientes que desbordan al grupo común.
* **Caso de uso:** Sumatoria estadística de parámetros de múltiples flujos de desborde independientes ofrecidos a un grupo tándem/tránsito común.
* **Fuente:** *"5.- ING. DE TRAFICO AVANZADO_1.pdf"* y *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

## $g$ Aproximaciones de Rapp ($A^*$ y $N^*$)

> **Nota de notación exacta en diapositivas:** En la teoría clásica de Rapp las magnitudes equivalentes se simbolizan como $A^*$ y $N^*$. Sin embargo, **las diapositivas cargadas las escriben directamente como $A$ y $C$**.

### 1. Tráfico Equivalente Ofrecido de Rapp ($A$)
* **Fórmula (copiada exactamente de la diapositiva):**
  
$$
A = V + 3 \frac{V}{M} \left( \frac{V}{M} - 1 \right)
$$

* **Significado de símbolos y unidades:**
  * $A$: Tráfico equivalente poissoniano del sistema ($A^*$) [Erlangs].
  * $V$: Varianza combinada del tráfico de desbordamiento.
  * $M$: Media combinada del tráfico de desbordamiento [Erlangs].
* **Caso de uso:** Determinar el tráfico ofrecido equivalente de un grupo ficticio para aplicar tablas de Erlang B.
* **Fuente:** *"5.2 FORMULAS DE ING.TRAFICO.pdf"* (Tema: Determinación del A y C mediante Rapp).

---

### 2. Número de Canales Parciales / Equivalentes de Rapp ($C$)
* **Fórmula (copiada exactamente de la diapositiva):**
  
$$
C = \frac{A \left( M + \frac{V}{M} \right)}{M + \frac{V}{M} - 1} - M - 1
$$

* **Significado de símbolos y unidades:**
  * $C$: Número de canales del grupo ficticio/equivalente ($N^*$).
  * $A$: Tráfico equivalente calculado por la primera fórmula de Rapp [Erlangs].
  * $M$: Media combinada del desborde.
  * $V$: Varianza combinada del desborde.
* **Caso de uso:** Determinar la cantidad ficticia de canales necesarios para simular la generación del tráfico de desborde.
* **Fuente:** *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

### 3. Dimensionamiento de Canales a la Central de Tránsito ($N_{AT}$)
* **Fórmulas:**
  
$$
E(N_{AT} + C, A) = B_2 \cdot \frac{M}{A}
$$

  
$$
N_{AT} + C = f[A, E(N_{AT} + C, A)]
$$

* **Significado de símbolos y unidades:**
  * $N_{AT}$: Número de canales reales requeridos desde la central hasta la central de tránsito.
  * $C$: Número de canales equivalentes de Rapp.
  * $A$: Tráfico equivalente de Rapp [Erlangs].
  * $M$: Media combinada del desborde [Erlangs].
  * $B_2$: Probabilidad de pérdida permitida en la ruta final o de tránsito.
  * $E(N_{AT} + C, A)$: Nuevo grado de pérdida (denotado en la diapositiva como *"nuevo B"*).
* **Procedimiento según la diapositiva:**
  1. Se calcula el nuevo valor de pérdida: $\text{nuevo } B = B_2 \frac{M}{A}$.
  2. Con el tráfico $A$ y el $\text{nuevo } B$, se entra a la **Tabla 3** (o tablas de Erlang B) para buscar el valor de canales totales $N_{AT} + C$.
  3. Se despeja $N_{AT}$ mediante: $N_{AT} = (N_{AT} + C) - C$.
* **Fuente:** *"5.2 FORMULAS DE ING.TRAFICO.pdf"*.

---

## $h$ Otras Fórmulas Presentes en las Diapositivas

### 1. Carga en el $j$-ésimo Canal ($a(j)$ o $a_j$)
* **Fórmula:**
  
$$
a(j) = A [E(j-1, A) - E(j, A)]
$$

  o escrito también como:
  
$$
a_j = A [E(j-1, A) - E(j, A)]
$$

* **Significado de símbolos y unidades:**
  * $a_j, a(j)$: Carga o tráfico cursado individualmente por el $j$-ésimo canal [Erlangs].
  * $A$: Tráfico ofrecido al grupo [Erlangs].
  * $E(j, A)$: Pérdida Erlang B para $j$ canales con tráfico $A$ (donde $E(0, A) = 1$).
* **Caso de uso:** Cálculo de la contribución o nivel de trabajo individual de cada circuito dispuesto en búsqueda secuencial.
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"* y *"2.-ING. DE TRAFICO AVANZADO_4.pdf"*.

---

### 2. Flujo Cursado en el Canal $N$ / Flujo de Salida ($F(N, A)$)
* **Fórmula:**
  
$$
F(N, A) = A [E(N, A) - E(N+1, A)]
$$

* **Significado de símbolos y unidades:**
  * $F(N, A)$: Carga absorbida específicamente por el último canal $N$.
  * $A$: Tráfico ofrecido [Erlangs].
* **Fuente:** *"1.-ING. DE TRAFICO AVANZADO_3.pdf"*.

---

## Respuestas a las 3 Preguntas Específicas

### Pregunta A
**Cuando el problema da una tasa de llegada total constante ($\lambda$) y además un número de fuentes, ¿qué modelo se usa: Erlang B o Engset? ¿Cómo se define ahí la congestión en las llamadas?**

* **Respuesta:**
  Según el ejemplo resuelto en la diapositiva del tema *"Ejercicio de aplicación"* (donde se especifican $F = 1000$ fuentes, $N = 2$ canales y $\lambda = 6000 \text{ llamadas/hora}$), se utiliza el **modelo de Engset (fuentes finitas)** para calcular la congestión en el tiempo $E$ y la congestión en las llamadas $B$. La tasa $\lambda$ y el tiempo medio de ocupación $\bar{t}$ se usan primeramente para hallar el tráfico $A = \lambda \bar{t}$ o la carga por fuente $b$.
  En dicho modelo, la **congestión en las llamadas ($B$)** se define explícitamente mediante la fórmula de Engset:
  
$$
B = \frac{\binom{F-1}{N} b^N}{\sum_{J=0}^N \binom{F-1}{J} b^J}
$$

* **Cita de diapositivas:** *"2.-ING. DE TRAFICO AVANZADO_4.pdf"* (Diapositivas de Ejercicio de Aplicación, incisos a, c y d).

---

### Pregunta B
**Para dimensionar la central de tránsito con el desborde de dos rutas, ¿el método que se enseña es sumar solo las medias y aplicar Erlang B, o sumar media y varianza y aplicar Wilkinson/Rapp? Si es el segundo, ¿cómo se obtiene la varianza de cada ruta y qué datos se usan (tráfico ofrecido, canales, porcentaje de desborde)?**

* **Respuesta:**
  El método enseñado es el **segundo**: **sumar la media y la varianza** de los flujos de desborde individuales (Teoría de Equivalente Aleatorio de Wilkinson) y aplicar las **fórmulas de Rapp**.

  La varianza de cada ruta $v_i$ se obtiene mediante los siguientes pasos y datos:
  1. **Datos utilizados:** Tráfico offered a la ruta de primera elección ($A_i$), número de canales de esa ruta directa ($C_i$ o $N_{AB}, N_{AC}$) y el porcentaje/probabilidad de desborde $E(C_i, A_i)$ obtenido de las tablas de Erlang B.
  2. **Cálculo de la media parcial $m_i$:**
     
$$
m_i = A_i \cdot E(C_i, A_i)
$$

  3. **Cálculo de la varianza parcial $v_i$ (Fórmula de Riordan):**
     
$$
v_i = m_i \left( 1 - m_i + \frac{A_i}{C_i + 1 - A_i + m_i} \right)
$$

  4. **Sumatoria combinada:** Se calcula $M = \sum m_i$ y $V = \sum v_i$, para posteriormente ingresar a las ecuaciones de Rapp ($A$ y $C$) y dimensionar la ruta a la central de tránsito $N_{AT}$.
* **Cita de diapositivas:** *"5.- ING. DE TRAFICO AVANZADO_1.pdf"* (Sección 3: Tráfico de Desbordamiento Combinado) y *"5.2 FORMULAS DE ING.TRAFICO.pdf"* (Sección 3).

---

### Pregunta C
**En las aproximaciones de Rapp, ¿qué significan exactamente "media del tráfico ofrecido" y "intensidad de tráfico del sistema"? ¿Corresponden a M y A*, o a A?**

* **Respuesta:**
  De acuerdo con la notación literal usada en las diapositivas:
  * **$M$ ("media del tráfico de desbordamiento"):** Es la sumatoria de las medias parciales de desborde ($M = \sum m_i$), que representa la cantidad promedio de tráfico que no cupo en los grupos directos y se ofrece al grupo de tránsito.
  * **$A$ ("intensidad de tráfico del sistema / tráfico equivalente"):** Corresponde algebraicamente al **$A^*$ teórico** de la literatura clásica de Rapp, pero **en las diapositivas de la materia se denota directamente con la letra $A$** (sin asterisco). Representa el tráfico poissoniano equivalente ofrecido a un grupo ficticio de $C$ (equivalente a $N^*$) canales que produciría el mismo desborde con media $M$ y varianza $V$.
* **Cita de diapositivas:** *"5.2 FORMULAS DE ING.TRAFICO.pdf"* (Diapositivas 3 y 4 del tema Rapp).
