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
