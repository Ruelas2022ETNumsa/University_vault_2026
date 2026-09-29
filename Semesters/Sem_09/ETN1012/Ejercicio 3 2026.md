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
