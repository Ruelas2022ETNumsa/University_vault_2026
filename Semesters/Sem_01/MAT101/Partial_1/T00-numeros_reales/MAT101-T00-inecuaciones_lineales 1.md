---
title: "Solución de inecuaciones en variable x"
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
Inecuaciones lineales<br>
inecuaciones · primer grado · conjunto solución · despeje · intervalos<br>
¿Qué es una inecuación de primer grado?<br>
¿Cuál es el procedimiento para hallar el conjunto solución?<br>
¿Cómo se representa gráficamente el $C_s$?<br>
$ax + b \gtreqless cx + d$<br>
ver también: intervalos

::note
### Inecuación de $1^{\text{er}}$ grado

**Forma**
- $ax + b \gtreqless cx + d$
- $a, b, c, d \in \mathbb{R}$

Se recomienda despejar $x$ con propiedades:
$$\begin{array}{rcll}
  ax - cx & > & d - b & \\
  (a - c)x & > & d - b & (\text{si } a - c > 0) \\
  x & > & \dfrac{d - b}{a - c} &
\end{array}$$

$C_s$: conjunto solución de la inecuación.

```desmos-graph
left=-2; right=6; bottom=-1; top=1;
width=320; height=80;
---
x>2| #005F73
(2,0) | open | #005F73
x > 2 |y=0| #005F73
(2, 0.5) |hidden| label: (d-b)/(a-c)
```

$C_s = \left] \dfrac{d - b}{a - c}, +\infty \right[ = \left\{ x \in \mathbb{R} \mid x > \dfrac{d - b}{a - c} \right\}$

> [!note] El manuscrito presenta el despeje asumiendo que el coeficiente resultante es positivo para mantener el sentido de la desigualdad.

````

> [!summary] Procedimiento para resolver desigualdades de primer grado mediante el aislamiento de la variable y la determinación del intervalo solución en la recta real.

##### Ej. Hallar el $C_s$: $(4x - 3)^2 \leq (4x + 1)^2$

$$\begin{array}{rcl}
 16x^2 - 24x + 9 & \leq & 16x^2 + 8x + 1 \\ 8 & \leq & 32x \\ \dfrac{8}{32} & \leq & x \\ x & \geq & \dfrac{1}{4} \end{array}
 $$

**$C_s$**

```desmos-graph
left=-1; right=3; bottom=-1; top=1;
width=320; height=80;
---
x >= 0.25 | #005F73
(0.25, 0) | #005F73
x >= 0.25 |y=0| #005F73
(0.25, 0) | label:1/4
```

$C_s=\left[\dfrac{1}{4},+\infty\right[  =\left\{\,x\in\mathbb{R}\;\middle|\;x\ge\dfrac{1}{4}\,\right\}$


> [!note] Complemento (Nivel B)
> 
> De acuerdo con James Stewart, resolver una desigualdad significa determinar el conjunto de números reales para los cuales el enunciado es verdadero. Este conjunto se denomina **conjunto solución**.
> 
> Al manipular desigualdades, se deben seguir reglas fundamentales que difieren de las igualdades de la siguiente manera:
> 
> 1. **Suma y resta**: Si $a \leq b$, entonces $a + c \leq b + c$ para cualquier $c \in \mathbb{R}$.
> 2. **Multiplicación por positivo**: Si $a \leq b$ y $c > 0$, entonces $ac \leq bc$.
> 3. **Multiplicación por negativo**: Si $a \leq b$ y $c < 0$, entonces $ac \geq bc$. El sentido de la desigualdad **se invierte**.
> 4. **Recíprocos**: Si $a$ y $b$ son positivos y $a \leq b$, entonces $\dfrac{1}{a} \geq \dfrac{1}{b}$.

---

### Método de signos para solución de inecuaciones

````cornell
::cue

Generalización de inecuaciones<br>
inecuaciones · método de signos · puntos críticos · intervalos<br>
¿Cuál es el procedimiento sistemático para resolver inecuaciones de grado superior? ¿Cómo se determina la pertenencia de un intervalo al conjunto solución?<br>
$\dfrac{P(x)}{Q(x)} \gtrless 0$<br>
ver también: inecuaciones de primer grado<br>
no confundir: puntos críticos con soluciones finales sin verificar la restricción del denominador

::note

Generalizando.

**Forma general**
- $M_{(x)} \gtrless N_{(x)}$

**Pasos para resolver**
1. Formar comparación con cero ($0$) con $+ / (-)$
	- $\dfrac{P(x)}{Q(x)} > 0$
2. Factorizar totalmente $P$ y $Q$:
	- $\dfrac{(x - a_1)(x - a_2)\dots(x - a_k)}{(x - b_1)(x - b_2)\dots(x - b_n)} > 0$
3. Se representan en la recta real $a_i, \dots, b_j$ quedando definidos $n$ intervalos $I_1, I_2, I_3 \dots I_n$.
```desmos-graph
left=-5;right=5;bottom=-1;top=1;
width=320;height=120;
---
y=0|#005F73
(-4,0.3)|label:I_1|hidden|#005F73
(-1,0.3)|label:I_2|hidden|#005F73
(1.5,0.3)|label:I_3|hidden|#005F73
(4,0.3)|label:I_4|hidden|#005F73
(-2.5,0)|open|#C1121F|label:a_1
(0,0)|open|#C1121F|label:b_1
(3,0)|open|#C1121F|label:a_2
```
4. **Prueba de signos:**
	- De $I_1$ se toma un valor (¡no extremo!) y se prueba signos reemplazando en el paso 2.
	- $\dfrac{(+)(-)\dots(+)}{(-)(+)\dots(+)} = \dfrac{(-)}{(+)} > 0$
5. Resultan 2 posibilidades:
	- **$1^\circ$ Si $(+) > 0 \rightarrow V$ (verdad):** Se concluye que $I_i \in C_s$.
	- **$2^\circ$ Si $(-) > 0 \rightarrow F$ (falsedad):** Se concluye que $I_i \notin C_s$.
	- Se repite el procedimiento para $I_2, I_3$, etc.
6. El $C_s$ buscado se da por la unión ($\cup$).

````

> [!summary] Método algorítmico para resolver inecuaciones no lineales mediante la determinación de signos en intervalos delimitados por los ceros del numerador y denominador.

> [!note] Complemento (Nivel B)
> 
> El **Método de Intervalos** (o de signos) se fundamenta en la propiedad de que una función racional solo puede cambiar de signo en los puntos donde su numerador es cero (raíces) o su denominador es cero (puntos de indefinición).
> 
> Según Stewart, estos puntos críticos dividen la recta real en intervalos de prueba. Dado que los polinomios son funciones continuas en sus dominios, el signo de la expresión se mantiene constante dentro de cada intervalo. Por ello, basta con elegir un **valor de prueba** arbitrario dentro de cada región para validar si todo el intervalo satisface la desigualdad original.
> 
> **Propiedad de los puntos críticos:**
> 
> - Los ceros provenientes del denominador ($Q(x)=0$) **nunca** se incluyen en el conjunto solución (siempre generan intervalos abiertos), independientemente de si la desigualdad incluye el signo igual ($\geq, \leq$), para evitar la división por cero.

---

%%
# galaxy-links
[[MAT101-T00-star]]
%%
