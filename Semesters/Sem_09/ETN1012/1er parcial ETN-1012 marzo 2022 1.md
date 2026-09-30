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

El **plan de numeración** es un plan técnico que identifica inequívocamente a cada abonado y permite el enrutamiento jerárquico de las llamadas a nivel local, nacional e internacional. Usa una estructura de 15 dígitos:

| Dígitos | Significado |
| :-----: | ----------- |
| 14 y 15 | Ceros de acceso de red (`0` nacional, `00` internacional) |
| 12 y 13 | Código del Carrier (ej. `10` ENTEL, `16` COTEL) |
| 9, 10 y 11 | Código de país (`591` Bolivia) |
| 7 y 8 | Departamento o región |
| 6 | Zona |
| 5 | Central |
| 1, 2, 3 y 4 | Usuario |

Llamada internacional:

$$
00 + \text{Código Carrier} + \text{Código de País} + \text{Número de teléfono}
$$

**Ejemplo** (supuestos: destino La Paz, carrier ENTEL, código de ciudad `22`, abonado `794040`):

`00 + 10 + 591 + 22 + 794040` → **001059122794040**

Check: 2 + 2 + 3 + 2 + 6 = 15 dígitos.

# Ejercicio 3 2022
¿El plan de señalización que contenidos básicos debe tener? (10 puntos).

---

El **plan de señalización** debe definir las señales necesarias para:

- Originar acciones en los sistemas de conmutación.
- Alertar al abonado o servicio llamado.
- Conectar correctamente al abonado llamante con el llamado.

Contenidos básicos:

1. **Señalización entre abonado y central:** discado por pulsos y multifrecuencia.
2. **Señalización entre centrales:** por canal común (**SCC7**) y por canal asociado.

# Ejercicio 4 2022
De la gráfica de circuitos de ocupación individual; dibujar la ocupación simultánea, calcular el tráfico cursado y calcular el congestionamiento en el tiempo. (20 puntos).

![[Ejercicio 4 2022-28-09-2026_18-02-52.png]]

---

**Gráfica de ocupación individual del enunciado (Desmos):**

```desmos-graph
left=-4; right=63; bottom=0; top=8;
width=550; height=300;
---
(-2,1)|label:1|hidden|#474448
(-2,2)|label:2|hidden|#474448
(-2,3)|label:3|hidden|#474448
(-2,4)|label:4|hidden|#474448
(-2,5)|label:5|hidden|#474448
(-2,6)|label:6|hidden|#474448
(-2,7)|label:7|hidden|#474448
y=7|0<=x<=10|#005F73
y=7|15<=x<=20|#005F73
y=7|30<=x<=40|#005F73
y=7|50<=x<=60|#005F73
y=6|5<=x<=20|#005F73
y=6|25<=x<=35|#005F73
y=6|40<=x<=50|#005F73
y=5|0<=x<=10|#005F73
y=5|15<=x<=25|#005F73
y=5|30<=x<=35|#005F73
y=5|50<=x<=60|#005F73
y=4|5<=x<=20|#005F73
y=4|30<=x<=40|#005F73
y=4|45<=x<=55|#005F73
y=3|0<=x<=10|#005F73
y=3|15<=x<=20|#005F73
y=3|25<=x<=35|#005F73
y=3|45<=x<=55|#005F73
y=2|5<=x<=20|#005F73
y=2|25<=x<=35|#005F73
y=2|40<=x<=45|#005F73
y=2|50<=x<=60|#005F73
y=1|0<=x<=10|#005F73
y=1|15<=x<=20|#005F73
y=1|30<=x<=40|#005F73
y=1|45<=x<=50|#005F73
y=1|55<=x<=60|#005F73
```

**Ocupación individual (tramos leídos de la gráfica, en minutos):**

| Circuito | Tramos | $\sum t_j$ (min) |
|:-:|---|:-:|
| 1 | 0–10, 15–20, 30–40, 45–50, 55–60 | 35 |
| 2 | 5–20, 25–35, 40–45, 50–60 | 40 |
| 3 | 0–10, 15–20, 25–35, 45–55 | 35 |
| 4 | 5–20, 30–40, 45–55 | 35 |
| 5 | 0–10, 15–25, 30–35, 50–60 | 35 |
| 6 | 5–20, 25–35, 40–50 | 35 |
| 7 | 0–10, 15–20, 30–40, 50–60 | 35 |

**Ocupación simultánea** (circuitos ocupados en cada intervalo de 5 min):

| Intervalo (min) | 0–5 | 5–10 | 10–15 | 15–20 | 20–25 | 25–30 | 30–35 | 35–40 | 40–45 | 45–50 | 50–55 | 55–60 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Circuitos ocupados | 4 | 7 | 3 | 7 | 1 | 3 | 7 | 3 | 2 | 4 | 5 | 4 |

```desmos-graph
left=-3; right=63; bottom=-0.5; top=8;
width=550; height=300;
---
y=7|0<=x<=60|#A3A2A4|DASHED
x=0|0<=y<=4|#C1121F
y=4|0<=x<=5|#C1121F
x=5|4<=y<=7|#C1121F
y=7|5<=x<=10|#C1121F
x=10|3<=y<=7|#C1121F
y=3|10<=x<=15|#C1121F
x=15|3<=y<=7|#C1121F
y=7|15<=x<=20|#C1121F
x=20|1<=y<=7|#C1121F
y=1|20<=x<=25|#C1121F
x=25|1<=y<=3|#C1121F
y=3|25<=x<=30|#C1121F
x=30|3<=y<=7|#C1121F
y=7|30<=x<=35|#C1121F
x=35|3<=y<=7|#C1121F
y=3|35<=x<=40|#C1121F
x=40|2<=y<=3|#C1121F
y=2|40<=x<=45|#C1121F
x=45|2<=y<=4|#C1121F
y=4|45<=x<=50|#C1121F
x=50|4<=y<=5|#C1121F
y=5|50<=x<=55|#C1121F
x=55|4<=y<=5|#C1121F
y=4|55<=x<=60|#C1121F
(7.5,7.4)|label:5|hidden|#474448
(17.5,7.4)|label:5|hidden|#474448
(32.5,7.4)|label:5|hidden|#474448
```

En rojo, la ocupación simultánea (número de circuitos ocupados vs. tiempo). Las etiquetas 5 marcan los tramos (5–10, 15–20 y 30–35 min) con los 7 circuitos ocupados; congestión acumulada: $3 \times 5 = 15\ \text{min}$.

**Volumen de tráfico:**

$$
V = \sum_{j=1}^{n} t_j = 35 + 40 + 35 + 35 + 35 + 35 + 35 = 250\ \text{minutos-Erlang} \qquad (n = 27\ \text{tomas})
$$

**Tráfico cursado** ($T = 60\ \text{min}$):

$$
A' = \frac{V}{T} = \frac{250\ \text{min-Erlang}}{60\ \text{min}} = 4{,}167\ \text{Erlangs}
$$

Verificación con la ocupación simultánea: $\sum k\,\Delta t = 5\,(4+7+3+7+1+3+7+3+2+4+5+4) = 5 \times 50 = 250$.

**Congestión en el tiempo:** los 7 circuitos están ocupados a la vez en 5–10, 15–20 y 30–35 min, es decir $t = 3 \times 5 = 15\ \text{min}$:

$$
E = \frac{t}{T} = \frac{15\ \text{min}}{60\ \text{min}} = 0{,}25 \quad (25\%)
$$

| Volumen $V$ | Tráfico cursado $A'$ | Congestión en el tiempo $E$ |
|:---:|:---:|:---:|
| 250 min-Erlang | 4,167 Erlangs | 0,25 (25 %) |

# Ejercicio 5 2022
Con los datos E $-,60$ y una calidad de servicio 0.002, determinar la Media, Varianza, Tráfico y numero de Canales. (25 puntos)

---

**Datos** (se interpreta $E(A_1, C_1)$ con $C_1 = 60$ canales): $E(C_1, A_1) = 0{,}002$.

**Tráfico ofrecido** (tabla de Erlang B para $C_1 = 60$ y $E = 0{,}002$):

$$
A_1 = 42{,}35\ \text{Erlangs}
$$

**Media:**

$$
M = A_1 \cdot E(C_1, A_1) = 42{,}35 \times 0{,}002 = 0{,}0847\ \text{Erlangs}
$$

**Varianza (Riordan):**

$$
V = M\left(1 - M + \frac{A_1}{C_1 + 1 - A_1 + M}\right) = 0{,}0847\left(1 - 0{,}0847 + \frac{42{,}35}{60 + 1 - 42{,}35 + 0{,}0847}\right)
$$

$$
V = 0{,}0847\left(0{,}9153 + \frac{42{,}35}{18{,}7347}\right) = 0{,}0847\,(0{,}9153 + 2{,}2605) = 0{,}0847 \times 3{,}1758 = 0{,}2690\ \text{Erlangs}^2
$$

**Tráfico equivalente (Rapp):**

$$
\frac{V}{M} = \frac{0{,}2690}{0{,}0847} = 3{,}176
$$

$$
A = V + 3\,\frac{V}{M}\left(\frac{V}{M} - 1\right) = 0{,}2690 + 3\,(3{,}176)\,(2{,}176) = 0{,}2690 + 20{,}733 = 21{,}00\ \text{Erlangs}
$$

**Canales equivalentes (Rapp):**

$$
C = \frac{A\left(M + \frac{V}{M}\right)}{M + \frac{V}{M} - 1} - M - 1 = \frac{21{,}00\,(0{,}0847 + 3{,}176)}{0{,}0847 + 3{,}176 - 1} - 0{,}0847 - 1 = 21{,}00 \times \frac{3{,}2607}{2{,}2607} - 1{,}0847
$$

$$
C = 21{,}00 \times 1{,}4423 - 1{,}0847 = 30{,}29 - 1{,}08 = 29{,}20\ \text{canales}
$$

| Media $M$ | Varianza $V$ | Tráfico $A$ | Canales $C$ |
|:---:|:---:|:---:|:---:|
| 0,0847 Erlangs | 0,2690 $\text{Erlangs}^2$ | 21,00 Erlangs | 29,20 canales |

# Ejercicio 6 2022
Tenemos 4 centrales A, B, C y T se ha observado que 5256 usuarios ocuparon 51 circuitos, utilizando un tiempo de ocupación media de 50 segundos generando un tráfico de desborde de 13 Erlangs de la central A con destino a la central B, por otro lado, se ha medido el trafico total de la central A con destino a la central C de 65 Erlangs utilizando 46 circuitos, y 504 usuarios utilizaron un tiempo de ocupación media de 50 segundos la ruta de desborde, se pudo verificar el grado de servicio B2 = 0.5%. Determinar el número de circuitos que se necesitan de la central A con destino a la central T (tránsito) para evitar llamadas perdidas que se generan en la central A con destino a la central B y C. (25 puntos) 

---

**Ruta A→B** (en $A_1$: $M$ = número de usuarios, $H$ = tiempo medio de ocupación, $L = 1$)

$$
A_1 = \frac{M\,H\,L}{3600} = \frac{5256 \times 50}{3600} = 73\ \text{Erlangs} \qquad C_1 = 51 \qquad m_1 = 13\ \text{Erlangs}
$$

Con los datos tal cual ($A_1 = 73$, $C_1 = 51$, $m_1 = 13$) el denominador de Riordan es negativo y sale $v_1 < 0$. Se conservan $A_1$ y $m_1$ y se reemplaza $C_1$ por los canales equivalentes $C'_1$ que producen ese bloqueo, $E(A_1, C'_1) = m_1/A_1 = 13/73 = 0{,}17808$. Con la recurrencia de Erlang B: $E(73;63) = 0{,}18550$ y $E(73;64) = 0{,}17463$, luego

$$
C'_1 = 63 + \frac{0{,}18550 - 0{,}17808}{0{,}18550 - 0{,}17463} = 63{,}683\ \text{canales}
$$

$$
v_1 = m_1\left(1 - m_1 + \frac{A_1}{C'_1 + 1 - A_1 + m_1}\right) = 13\left(1 - 13 + \frac{73}{63{,}683 + 1 - 73 + 13}\right) = 13\left(-12 + \frac{73}{4{,}683}\right) = 13\,(-12 + 15{,}590) = 46{,}664\ \text{Erlangs}^2
$$

**Ruta A→C**

$$
A_2 = 65\ \text{Erlangs} \qquad C_2 = 46 \qquad m_2 = \frac{504 \times 50}{3600} = 7\ \text{Erlangs}
$$

Igual que en A→B: $E(A_2, C'_2) = m_2/A_2 = 7/65 = 0{,}10769$, con $E(65;63) = 0{,}11210$ y $E(65;64) = 0{,}10221$:

$$
C'_2 = 63 + \frac{0{,}11210 - 0{,}10769}{0{,}11210 - 0{,}10221} = 63{,}445\ \text{canales}
$$

$$
v_2 = m_2\left(1 - m_2 + \frac{A_2}{C'_2 + 1 - A_2 + m_2}\right) = 7\left(1 - 7 + \frac{65}{63{,}445 + 1 - 65 + 7}\right) = 7\left(-6 + \frac{65}{6{,}445}\right) = 7\,(-6 + 10{,}085) = 28{,}592\ \text{Erlangs}^2
$$

**Desborde combinado**

$$
M = m_1 + m_2 = 13 + 7 = 20\ \text{Erlangs}
$$

$$
V = v_1 + v_2 = 46{,}664 + 28{,}592 = 75{,}257\ \text{Erlangs}^2 \qquad \frac{V}{M} = \frac{75{,}257}{20} = 3{,}763
$$

**Rapp**

$$
A = V + 3\,\frac{V}{M}\left(\frac{V}{M} - 1\right) = 75{,}257 + 3\,(3{,}763)\,(2{,}763) = 75{,}257 + 31{,}19 = 106{,}45\ \text{Erlangs}
$$

$$
C = \frac{A\left(M + \frac{V}{M}\right)}{M + \frac{V}{M} - 1} - M - 1 = \frac{106{,}45\,(20 + 3{,}763)}{20 + 3{,}763 - 1} - 20 - 1 = 106{,}45 \times 1{,}0439 - 21 = 90{,}12\ \text{canales}
$$

**Canales hacia la central de tránsito**

$$
\text{nuevo } B = E(N_{AT} + C,\,A) = B_2\,\frac{M}{A} = 0{,}005 \times \frac{20}{106{,}45} = 9{,}39\times10^{-4}
$$

Con $A = 106{,}45\ \text{Erlangs}$ se busca el menor número de canales totales que cumpla $E \le 9{,}39\times10^{-4}$ (Erlang B, tabla o recurrencia): $N = 135 \to 1{,}012\times10^{-3}$ (no cumple) y $N = 136 \to 7{,}91\times10^{-4}$ (cumple), luego $N_{AT} + C = 136$ canales.

$$
N_{AT} = (N_{AT} + C) - C = 136 - 90{,}12 = 45{,}88 \implies \mathbf{46\ circuitos}
$$

**Resultado: la central A necesita 46 circuitos hacia la central de tránsito T.**

Notas:
- Se siguen las fórmulas del formulario (Riordan, Wilkinson, Rapp y $N_{AT}$). El único paso que no está en el formulario es reemplazar $C_i$ por $C'_i$, porque con $C_1 = 51$ y $C_2 = 46$ el denominador de Riordan es negativo (varianza negativa). Con $C'_i$ se conservan $A_i$ y $m_i$ del enunciado. Es el mismo recurso que se usa en el ejercicio 2 del parcial 2026, que tiene los mismos datos ($m = 13$ y $7$ Erlangs, $B_2 = 0{,}5\%$). Confirmar el criterio con la cátedra.
- Sensibilidad al redondeo: si $C'_1$ y $C'_2$ se redondean a dos decimales sale $N_{AT} = 45{,}75$, y la respuesta sigue siendo 46.
- Alternativa con el formulario puro ($m_i = A_i\,E(C_i,A_i)$ con $A_1 = 73$, $C_1 = 51$, $A_2 = 65$, $C_2 = 46$): $m_1 = 23{,}87$ y $m_2 = 20{,}89$ Erlangs, $N_{AT} \approx 72$ circuitos. No es la respuesta principal porque ignora el desborde medido del enunciado (13 y 7 Erlangs).
- Otro recurso posible, reemplazar $A_i$ por el tráfico equivalente que produce el desborde medido ($A_{1eq} \approx 60{,}98$ y $A_{2eq} \approx 48{,}85$ Erlangs), da $N_{AT} \approx 44$; se descarta porque cambia el tráfico ofrecido del enunciado.
