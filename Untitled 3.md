--- start-multi-column: cornell-T0-003

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

## La recta real e intervalos

📝 **Desarrollo**

Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```desmos-graph
left=-5;right=5;bottom=-1;top=1;
width=320;height=100;
---
y=0|#000000
(-2,0)|label:-2|#000000
(-1,0)|label:-1|#000000
(0,0)|label:0|#000000
(1,0)|label:1|#000000
(1.414,0)|label:\sqrt{2}|#000000
(2,0)|label:2|#000000
(3,0)|label:3|#000000
(3.141,0)|label:\pi|#000000
```

Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**
    - $[a, b] = {x \in \mathbb{R} / a \le x \le b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<=x<=4|#005F73
(1,0)|#005F73|label:a
(4,0)|#005F73|label:b
```

2. **Intervalo abierto**
    - $]a, b[ = {x \in \mathbb{R} / a < x < b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<x<4|#005F73
(1,0)|open|#005F73|label:a
(4,0)|open|#005F73|label:b
```

3. **Intervalo semiabierto**
    - $[a, b[ = {x \in \mathbb{R} / a \le x < b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<=x<4|#005F73
(1,0)|#005F73|label:a
(4,0)|open|#005F73|label:b
```

4. **Intervalos infinitos**
    - $[a, +\infty[ = {x \in \mathbb{R} / x \ge a}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x>=2|#005F73
(2,0)|#005F73|label:a
```

```desmos-graph
- $]-\infty, b[ = \{x \in \mathbb{R} / x < b\}$
```

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x<3|#005F73
(3,0)|open|#005F73|label:b
```

> [!note] En el manuscrito se etiqueta a los límites $a$ y $b$ de los intervalos como "valores extremos".

--- end-column ---

🔑 **Claves**

Correspondencia biunívoca · Recta real · Intervalo · Subconjunto · Extremos

¿Qué implica la correspondencia "uno a uno" entre $\mathbb{R}$ y la recta? ¿Cómo se define formalmente un intervalo como subconjunto de $\mathbb{R}$? ¿Qué diferencia gráfica y simbólica existe entre extremos abiertos y cerrados?

Intervalo: $I \subseteq \mathbb{R}$

ver también: [[Axiomas de orden]]

no confundir $]a, b[$ (notación de corchetes invertidos) con $(a, b)$ (notación de paréntesis).

%%```desmos-graph```%%

--- end-multi-column ---

> **Resumen:** Los intervalos son subconjuntos de la recta real que agrupan números comprendidos entre dos extremos, cuya inclusión se representa mediante corchetes (cerrados) o su exclusión mediante corchetes invertidos o paréntesis (abiertos).

> [!note] Complemento (Nivel B)
> 
> Formalmente, la **recta real** (o eje real) es la representación geométrica donde cada punto de la recta corresponde a un único número real y viceversa.
> 
> Los intervalos se clasifican en:
> 
> 1. **Intervalos finitos:** Corresponden a segmentos de recta. Los puntos $a$ y $b$ se denominan **puntos frontera**, mientras que los puntos entre ellos son **puntos interiores**.
> 2. **Intervalos infinitos:** Representan rayos (semirrectas) o la totalidad de la recta real $(-\infty, \infty)$.
> 
> El símbolo $\infty$ (infinito) no es un número real, sino una notación para indicar que el conjunto no está acotado en una dirección determinada.