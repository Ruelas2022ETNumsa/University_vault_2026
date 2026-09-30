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

|  Volumen $V$   | Tráfico cursado $A'$ | Congestión en el tiempo $E$ |
| :------------: | :------------------: | :-------------------------: |
| 250 min-Erlang |    4,167 Erlangs     |         0,25 (25 %)         |
