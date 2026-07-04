---
title: "La recta real e intervalos"
galaxy_body: planet
subject: MAT101
semester: 1
partial: 1
topic: T00
star: "[[MAT101-T00-star]]"
moons: []
comets: []
tags: [MAT101, galaxy-planet, P1, T00]
date_created: 2026-07-04
status: activo
---

````cornell

::cue

Correspondencia biunívoca · Recta real · Intervalo · Subconjunto · Extremos<br>
¿Qué significa que exista una correspondencia "uno a uno" entre $\mathbb{R}$ y la recta?<br>
¿Cómo se representa simbólicamente un intervalo infinito?<br>
¿Qué diferencia gráfica hay entre un extremo abierto y uno cerrado?<br>
Definición de intervalo: $I \subseteq \mathbb{R}$<br>
ver también: Axiomas de orden<br>
no confundir $]a, b[$ (notación europea) con $(a, b)$ (notación anglosajona).<br>

::note

Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```desmos-graph
left=-5;right=5;bottom=-1;top=1;
width=320;height=100;
---
y=0|#005F73
(-2,0)|label:-2|#005F73
(-1,0)|label:-1|#005F73
(0,0)|label:0|#005F73
(1,0)|label:1|#005F73
(1.414,0)|label:√2|#005F73
	(2,0)|label:2|#005F73
(3,0)|label:3|#005F73
(3.141,0)|label:π|#005F73
```

Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**
    - $[a, b] = \{x \in \mathbb{R} \mid a \le x \le b\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
1<=x<=4|#005F73
(1,0)|#005F73|label:a
(4,0)|#005F73|label:b
```

2. **Intervalo abierto**
    - $]a, b[ = \{x \in \mathbb{R} \mid a < x < b\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
1<x<4|#005F73
(1,0)|open|#005F73|label:a
(4,0)|open|#005F73|label:b
```

3. **Intervalo semiabierto**
    - $[a, b[ = \{x \in \mathbb{R} \mid a \le x < b\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---

1<=x<4|#005F73
(1,0)|#005F73|label:a
(4,0)|open|#005F73|label:b
```

4. **Intervalos infinitos**
    - $[a, +\infty[ = \{x \in \mathbb{R} \mid x \ge a\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
x>=2|#005F73
(2,0)|#005F73|label:a
```


- $]-\infty, b[ = \{x \in \mathbb{R} / x < b\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
x<3|#005F73
(3,0)|open|#005F73|label:b
```

> [!note] En los apuntes se menciona el término "valores extremos" asociado a los límites $a$ y $b$ de los intervalos.

````

> [!summary] Los intervalos son subconjuntos de la recta real que representan todos los números comprendidos entre dos extremos, cuya naturaleza (abierta o cerrada) depende de la inclusión o exclusión de dichos puntos.

> [!note] Complemento (Nivel B)
> 
> La correspondencia biunívoca mencionada implica que a cada número real le corresponde uno y sólo un punto de la recta y, recíprocamente, cada punto de la recta representa a un único número real.
> 
> Formalmente, los intervalos se clasifican en:
> 
> 1. **Intervalos finitos:** Aquellos que corresponden a segmentos de recta. Se subdividen en abiertos $(a, b)$, cerrados $[a, b]$ y semiabiertos $[a, b)$ o $(a, b]$. Los puntos $a$ y $b$ se denominan **puntos frontera**, mientras que los puntos entre ellos son **puntos interiores**.
> 2. **Intervalos infinitos:** Aquellos que corresponden a rayos (semirrectas) o a la totalidad de la recta real $(-\infty, \infty)$.
> 
> Se utiliza la notación $\infty$ (infinito) no como un número, sino como un símbolo para indicar que el conjunto no está acotado en esa dirección.

%%
galaxy-links
[[MAT101-T00-star]]
%%
