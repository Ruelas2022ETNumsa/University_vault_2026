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
