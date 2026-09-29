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

- Para $A_{AB} = 73\ \text{Erlangs}$ y $B = 0{,}179$: $E(73;63) = 0{,}18550$ y $E(73;64) = 0{,}17463$, luego

$$
C'_{AB} = 63 + \frac{0{,}18550 - 0{,}17900}{0{,}18550 - 0{,}17463} = 63 + \frac{0{,}00650}{0{,}01087} = 63{,}598\ \text{canales}
$$

- Para $A_{AC} = 65\ \text{Erlangs}$ y $B = 0{,}1077$: $E(65;63) = 0{,}11210$ y $E(65;64) = 0{,}10221$, luego

$$
C'_{AC} = 63 + \frac{0{,}11210 - 0{,}10770}{0{,}11210 - 0{,}10221} = 63 + \frac{0{,}00440}{0{,}00989} = 63{,}445\ \text{canales}
$$

Desborde A→B, paso a paso:

$$
C'_{AB} + 1 - A_{AB} + m_{AB} = 63{,}598 + 1 - 73 + 13{,}067 = 4{,}665 \qquad \frac{A_{AB}}{4{,}665} = \frac{73}{4{,}665} = 15{,}648
$$

$$
1 - m_{AB} + 15{,}648 = 1 - 13{,}067 + 15{,}648 = 3{,}581
$$

$$
v_{AB} = m_{AB} \times 3{,}581 = 13{,}067 \times 3{,}581 \approx 46{,}793\ \text{Erlangs}^2
$$

Desborde A→C, paso a paso:

$$
C'_{AC} + 1 - A_{AC} + m_{AC} = 63{,}445 + 1 - 65 + 7{,}0005 = 6{,}4455 \qquad \frac{A_{AC}}{6{,}4455} = \frac{65}{6{,}4455} = 10{,}085
$$

$$
1 - m_{AC} + 10{,}085 = 1 - 7{,}0005 + 10{,}085 = 4{,}0845
$$

$$
v_{AC} = m_{AC} \times 4{,}0845 = 7{,}0005 \times 4{,}0845 \approx 28{,}594\ \text{Erlangs}^2
$$

Las varianzas se suman:

$$
V = \sum_{i=1}^{r} v_i = 46{,}793 + 28{,}594 = 75{,}387\ \text{Erlangs}^2
$$

### 3. Aproximaciones de Rapp ($A$ y $C$ equivalentes)

Relación varianza/media:

$$
\frac{V}{M} = \frac{75{,}387}{20{,}0675} = 3{,}757 \quad \text{(sin unidad)}
$$

Tráfico equivalente:

$$
A = V + 3\,\frac{V}{M}\left(\frac{V}{M} - 1\right)
$$

Primero el término $3\,\frac{V}{M}\left(\frac{V}{M}-1\right) = 3\,(3{,}757)\,(2{,}757) = 11{,}271 \times 2{,}757 = 31{,}07$:

$$
A = 75{,}387 + 31{,}07 \approx 106{,}45\ \text{Erlangs}
$$

Canales equivalentes:

$$
C = \frac{A\left(M + \frac{V}{M}\right)}{M + \frac{V}{M} - 1} - M - 1
$$

Primero los términos: $M + V/M = 20{,}0675 + 3{,}757 = 23{,}8245$ y $M + V/M - 1 = 22{,}8245$.

$$
C = 106{,}45 \times \frac{23{,}8245}{22{,}8245} - 20{,}0675 - 1 = 106{,}45 \times 1{,}04381 - 21{,}0675 = 111{,}12 - 21{,}07 = 90{,}05\ \text{canales}
$$

### 4. Canales hacia la central de tránsito T ($N_{AT}$)

Nuevo grado de pérdida sobre el desborde, con $B_2 = 0{,}5\%$:

$$
\text{nuevo } B = E(N_{AT} + C,\,A) = B_2\,\frac{M}{A} = \frac{0{,}005 \times 20{,}0675\ \text{Erlangs}}{106{,}45\ \text{Erlangs}} = \frac{0{,}1003}{106{,}45} = 9{,}43\times10^{-4}
$$

Con $A = 106{,}45\ \text{Erlangs}$ se busca el menor número de canales totales que cumpla (Erlang B, tabla o recurrencia): $N = 135\ \text{canales} \to 1{,}014\times10^{-3}$ (no cumple, es mayor que $9{,}43\times10^{-4}$) y $N = 136\ \text{canales} \to 7{,}93\times10^{-4}$ (cumple), luego $N_{AT} + C = 136\ \text{canales}$.

$$
N_{AT} = (N_{AT} + C) - C = 136\ \text{canales} - 90{,}05\ \text{canales} = 45{,}95\ \text{canales}
$$

$N_{AT} = 45{,}95$ canales; como debe ser entero, se toman 46 canales.

**Resultado: T necesita 46 canales.**

### Notas

- Se siguen las fórmulas del formulario (Riordan, Wilkinson, Rapp y $N_{AT}$). La varianza de cada desborde no se puede obtener con el formulario tal cual (da negativa, ver paso 2); el uso de $C'_i$ es un recurso propio, no del formulario. Es el mismo recurso que se usa en el ejercicio 6 del parcial 2022, que tiene los mismos datos.
- Sensibilidad al redondeo: con $C'_{AB} = 63{,}60$ y $C'_{AC} = 63{,}44$ (dos decimales) sale $N_{AT} = 46{,}01$, que parecería pedir 47; sin redondeos intermedios sale $N_{AT} = 45{,}95$, así que la respuesta es 46 canales. Conviene arrastrar tres decimales en $C'$.
- Otros métodos: sumar solo las medias y aplicar Erlang B a 20,07 Erlangs da 32 canales (ignora las ráfagas); usar 51 y 46 canales con Erlang B da ≈ 72. Confirmar cuál usa la cátedra.
