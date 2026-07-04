---
title: "MAT101-0-Numeros_reales_y_desigualdades-P1"
galaxy_body: supernova
subject: MAT101
semester: 1
partial: 1
topic: 
topic_name: 
class_parts:
  - ""
related_planets: []
tags: [MAT101, galaxy-supernova, P1]
date_created: 2026-07-03
status: completo
---

# Números reales y desigualdades

## Axiomas de cuerpo de los números reales (ℝ)

````cornell
::cue

Axiomas · Cuerpo · Reales · Neutros · Inversos<br>
¿Cuáles son las reglas básicas que rigen la suma y multiplicación?<br>
¿Qué elementos permiten la existencia de operaciones inversas?<br>
¿Cómo se relacionan la suma y el producto aritmético?<br>
$a + (-a) = 0$ $a \cdot a^{-1} = 1, a \neq 0$<br>
ver también: Axiomas de orden<br>
No confundir el neutro aditivo ($0$) con el neutro multiplicativo ($1$).<br>
**C**lausura, **C**onmutativa, **A**sociativa, **N**eutros, **N**egativos, **I**nversos,
**D**istributiva (**CCANNID**)

::note

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    - $a + b \in \mathbb{R}$ y $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    - $(a + b) + c = a + (b + c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    - i. $\exists \; 0 \in \mathbb{R} : a + 0 = a$
        - $0$ es el neutro para la suma "$+$".
    - ii. $\exists \; 1 \in \mathbb{R} : a \cdot 1 = a$
        - $1$ es el neutro para la multiplicación "$\times$".
5. **Existencia de negativos**
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} : a + (-a) = 0$
    - $-a$ es el negativo de $a$.
6. **Existencia de inversos**
    - $\forall a \in \mathbb{R} - \{0\}, \exists \; a^{-1} \in \mathbb{R} : a \cdot a^{-1} = 1$
    - $a^{-1} = \dfrac{1}{a}$ es el inverso de $a$.
7. **Distributividad**
    - $a(b + c) = ab + ac$

````


> [!summary] Definición de los siete axiomas fundamentales que establecen a los números reales como un cuerpo algebraico bajo las operaciones de adición y multiplicación.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. 0, sección I 3.2)**, el sistema de los números reales se postula como un conjunto de elementos sobre los cuales se definen dos operaciones (adición y multiplicación) que cumplen unívocamente con las propiedades de cuerpo.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Unicidad de resultados:** La suma $x+y$ y el producto $xy$ están unívocamente determinados por $x$ e $y$.
> 2. **Distinción de neutros:** El Axioma 4 de Apostol especifica explícitamente que existen dos números reales **distintos**, indicados por $0$ y $1$, tales que $0+x=x$ y $1 \cdot x = x$ para cada número real $x$.
> 3. **Existencia del recíproco:** Se enfatiza que para cada número real $x \neq 0$ existe un número real $y$ (denotado $x^{-1}$ o $1/x$) tal que $xy = 1$.
> 4. **Identidad de los elementos:** Apostol aclara en una nota que los números $0$ y $1$ utilizados para definir los negativos e inversos en los axiomas 5 y 6 son exactamente los mismos elementos neutros definidos en el axioma 4.

---

## Axiomas de igualdad

````cornell
::cue

Igualdad · Ecuación · Identidad · Transitividad<br>
¿Qué propiedades rigen la relación de equivalencia en $\mathbb{R}$?<br>
¿Cuál es la diferencia técnica entre una ecuación y una identidad?<br>
¿Cómo se definen formalmente la resta y la división?<br>
$(a = b \land b = c) \Rightarrow a = c$<br>
ver también: Axiomas de cuerpo<br>
No confundir una Identidad (válida para todo el dominio) con una Ecuación (válida para valores específicos).

::note

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    - $a = a$
2. **Simetría**
    - $a = b \Rightarrow b = a$
3. **Transitividad**
    - $(a = b \land b = c) \Rightarrow a = c$

> [!note] Resta y división son solo casos especiales de "$+$" y "$\times$":
> 
> - **Resta**
>     - $a - b = a + (-b)$
> - **División**
>     - $\dfrac{a}{b} = a \cdot \dfrac{1}{b} = a \cdot b^{-1}, \quad b \neq 0$

**No confundir:**

- $2^3 = 8 \Rightarrow$ Igualdad $\to$ verdad evidente.
- $x^2 - 4 = 0 \Rightarrow$ Ecuación $\to$ verdad para algunas $x$.
- $x^2 - 4 = (x - 2)(x + 2) \Rightarrow$ Identidad $\to$ verdad para toda $x \in \mathbb{R}$.
````

> [!summary] Establece las propiedades lógicas de la igualdad (reflexiva, simétrica y transitiva) y clarifica que la resta y división son extensiones de la suma y multiplicación por el opuesto/recíproco.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con **Thomas (Apéndice 6)** y **Apostol (Cap. 0, sección I 3.2)**, la estructura de los números reales se basa en el concepto de **Cuerpo ordenado**.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Propiedad de sustitución:** Aunque no se lista explícitamente en el manuscrito, es un axioma implícito de la igualdad: si $a = b$, entonces $a$ puede ser reemplazado por $b$ en cualquier proposición matemática sin alterar el valor de verdad de la misma.
> 2. **Unicidad de operaciones:** Apostol enfatiza que la suma $x + y$ y el producto $xy$ están **unívocamente determinados** por sus elementos. Esto garantiza que si $a = b$, entonces $a + c = b + c$ y $ac = bc$.
> 3. **Definiciones derivadas:** La resta y la división no se consideran operaciones independientes en la axiomática pura, sino que se definen estrictamente a través de la existencia de **opuestos** ($a - b := a + (-b)$) y **recíprocos** ($\dfrac{a}{b} := a \cdot b^{-1}$), tal como sugiere la nota del manuscrito.

---

## Teoremas sobre números reales (ℝ)

````cornell
::cue

Teoremas · Simplificación · Elemento cero · Opuestos · Recíprocos<br>
¿Cómo se demuestra formalmente la ley de cancelación?<br>
¿Qué ocurre al multiplicar cualquier número real por cero?<br>
¿Cuáles son las propiedades de los signos en la multiplicación?<br>
$a \cdot b = 0 \Rightarrow (a = 0 \lor b = 0)$ $a + b = a + c \Rightarrow b = c$<br>
ver también: Axiomas de cuerpo<br>
No confundir la ley de cancelación de la suma con la del producto; esta última requiere estrictamente que el factor sea distinto de cero ($a \neq 0$).

::note

Si: $a, b, c, d, x \in \mathbb{R}$

1. $a + b = a + c \Rightarrow b = c$
2. $(a \cdot b = a \cdot c) \land a \neq 0 \Rightarrow b = c$
3. $a + x = b \Rightarrow x = b - a$
4. $(a \cdot x = b \land a \neq 0) \Rightarrow x = b/a$
5. $a \cdot 0 = 0$
6. $a \cdot b = 0 \Rightarrow (a = 0 \lor b = 0)$
7. $a = b \Rightarrow -a = -b$
8. $a(-b) = -(ab)$
9. $(-a)(-b) = ab$
10. $\dfrac{a}{b} + \dfrac{c}{b} = \dfrac{a+c}{b}$
11. $\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{ad + cb}{bd}$
12. $\left(\dfrac{a}{b}\right)\left(\dfrac{c}{d}\right) = \dfrac{ac}{bd}$
13. $\dfrac{a/b}{c/d} = \dfrac{ad}{cb}$

````

### Prueba de (1)

**Hipótesis:** $a + b = a + c$ — **Tesis:** $b = c$

$$\begin{array}{rcll}
b & = & b & (\text{ax. reflexivo}) \\
& = & b + 0 & (\text{ax. } \exists \text{ neutro}) \\
& = & b + [a + (-a)] & (\text{ax. } \exists \text{ negativo}) \\
& = & (b + a) + (-a) & (\text{ax. asociativo}) \\
& = & (a + b) + (-a) & (\text{ax. conmutativo}) \\
& = & (a + c) + (-a) & (\text{Hipótesis}) \\
& = & (c + a) + (-a) & (\text{ax. conmutativo}) \\
& = & c + [a + (-a)] & (\text{ax. asociativo}) \\
& = & c + 0 & (\text{ax. } \exists \text{ negativo}) \\
& = & c & (\text{ax. } \exists \text{ neutro}) \\
b & = & c & (\text{LQQD})
\end{array}$$

> [!summary] Conjunto de 13 teoremas fundamentales derivados de los axiomas de cuerpo que rigen las operaciones algebraicas, incluyendo leyes de cancelación, propiedades del cero y aritmética de fracciones.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. 0, sección I 3.2)**, estas propiedades se clasifican como consecuencias inmediatas de los axiomas de cuerpo.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Unicidad de los neutros:** Los teoremas 1.1 y 1.7 de Apostol demuestran formalmente que los elementos neutros ($0$ y $1$) son únicos. Si existiera otro elemento con la misma propiedad, la ley de simplificación obligaría a que ambos fueran idénticos.
> 2. **Propiedad del producto nulo:** El Teorema I.11 especifica que un producto es cero **si y solo si** al menos uno de los factores es cero. Esto es fundamental para la resolución de ecuaciones por factorización.
> 3. **Existencia de la sustracción y división:** Apostol define estas operaciones no como axiomas, sino como teoremas de "posibilidad". La sustracción se define por la existencia de un único $x$ tal que $a + x = b$ (Teorema I.2), y la división por un único $x$ tal que $ax = b$ con $a \neq 0$ (Teorema I.8).

---

## Axiomas de orden de los números reales  (ℝ)

````cornell

::cue

Orden · Positividad · Tricotomía · Reales positivos<br>
¿Cuáles son las condiciones para que la suma y el producto conserven el orden?<br>
¿Qué significa que un conjunto sea "ordenado"?<br>
¿Cómo se define formalmente un número negativo en función de los positivos?<br>
$a > 0 \Leftrightarrow a \in \mathbb{R}^+$ $x < y \Leftrightarrow y - x \in \mathbb{R}^+$<br>
ver también: Axiomas de cuerpo<br>
No confundir la relación de orden ($<, >$) con la pertenencia a un subconjunto ($\mathbb{R}^+$). El orden se deriva de la positividad.

::note

Si $a, b \in \mathbb{R}$:

1. **Axioma 1**
    - $a, b \in \mathbb{R}^+ \Rightarrow$
        - i. $a + b \in \mathbb{R}^+$
        - ii. $a \cdot b \in \mathbb{R}^+$
2. **Axioma 2**
    - Si $a \in \mathbb{R} - \{0\} \Rightarrow (a \in \mathbb{R}^+ \lor -a \in \mathbb{R}^{-})$
3. **Axioma 3**
    - $0 \notin \mathbb{R}^+$

> [!note] Estos axiomas garantizan que el conjunto $\mathbb{R}$ es **ordenado!!**

- $4 > 2 > 1 > 0 > -3$
    
- $-4 < -1 < 1 < 0 < 10$
    
- $\mathbb{R}^+ =$ nros. reales positivos.
    
- $\mathbb{R}^- =$ nros. reales negativos.
    

**Definiciones (Def):**

1. $>$ $\to$ mayor que; $<$ $\to$ menor que.
2. $a > b \Leftrightarrow b < a$
3. $a \geq b \Leftrightarrow (a > b \lor a = b)$
4. $a \leq b \Leftrightarrow b \geq a$
5. $a < 0 \Leftrightarrow a \in \mathbb{R}^-$
6. $a > 0 \Leftrightarrow a \in \mathbb{R}^+$

> [!note] 2, 3 y 4 tienen su equivalente en conjuntos.

````

> [!summary] Los axiomas de orden postulan la existencia de un subconjunto de números positivos ($\mathbb{R}^+$) cerrado bajo la suma y el producto, permitiendo definir las relaciones de desigualdad y la estructura de cuerpo ordenado para $\mathbb{R}$.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. 0, sección I 3.4)**, el sistema de los números reales se define como un **cuerpo ordenado**. El concepto de "orden" no se introduce directamente, sino que se construye a partir del concepto primitivo de **número positivo**.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Propiedad de Tricotomía:** El Axioma 2 del manuscrito es una forma de la Ley de Tricotomía. Apostol especifica que para cualquier número real $x \neq 0$, se cumple exactamente una de las dos condiciones: $x$ es positivo o $-x$ es positivo.
> 2. **Definición formal de desigualdad:** La relación "menor que" ($x < y$) se define formalmente como la condición de que la diferencia $y - x$ sea un número positivo ($y - x \in \mathbb{R}^+$).
> 3. **Interpretación geométrica:** En la recta real, decir que $x < y$ equivale a decir que el punto $x$ se encuentra a la izquierda del punto $y$. Los números positivos están a la derecha del origen ($0$) y los negativos a su izquierda.

---

## Teoremas de desigualdades e inecuaciones

````cornell
::cue

Desigualdad · Inecuación · Regla de signos · Inversos<br>

¿Cómo afecta multiplicar por un número negativo a una desigualdad?<br>
¿Qué condiciones deben cumplirse para que el producto de dos reales sea positivo?<br>
¿Cómo se comportan los inversos multiplicativos en una relación de orden?<br>
$a > b \land c < 0 \Rightarrow ac < bc$ $0 < a < b \Rightarrow \dfrac{1}{a} > \dfrac{1}{b}$<br>
ver también: Axiomas de orden<br>
No confundir la elevación a una potencia par (requiere base positiva para mantener el orden) con la potencia impar (mantiene el orden siempre).<br>
**S**uma, **A**dición, **M**ultiplicación (pos/neg), **R**egla de signos, **C**uadrado, **U**nidad, **I**nversos, **E**levación (2/3)

::note

Si $a, b, c, d \in \mathbb{R}$:

1. **Suma de desigualdades**
    - $a > b \land c > d \Rightarrow a + c > b + d$
2. **Adición de una constante**
    - $a > b \land c \in \mathbb{R} \Rightarrow a + c > b + c$
3. **Multiplicación por positivo**
    - $a > b \land c > 0 \Rightarrow ac > bc$
4. **Multiplicación por negativo**
    - $a > b \land c < 0 \Rightarrow ac < bc$
    > [!note] Se invierte el sentido de la desigualdad.
5. **Regla de signos (Producto positivo)**
    - $a \cdot b > 0 \Rightarrow (a > 0 \land b > 0) \lor (a < 0 \land b < 0)$
6. **Regla de signos (Producto negativo)**
    - $a \cdot b < 0 \Rightarrow (a > 0 \land b < 0) \lor (a < 0 \land b > 0)$
7. **Cuadrado de un real**
    - $a^{2} \geq 0, \quad \forall \;a \in \mathbb{R}$
8. **Positividad de la unidad**
    - $1 > 0$
9. **Inverso de un positivo**
    - $a > 0 \Rightarrow a^{-1} > 0$
10. **Elevación al cuadrado**
    - $a > b > 0 \Rightarrow a^2 > b^2$
11. **Elevación al cubo**
    - $a > b \Rightarrow a^3 > b^3$
12. **Inversos multiplicativos**
    - $0 < a < b \Rightarrow \dfrac{1}{a} > \dfrac{1}{b}$



````

> [!summary] Conjunto de 12 leyes operativas que rigen el comportamiento de las desigualdades ante operaciones aritméticas y potencias en el conjunto de los números reales.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. 0, sección I 3.4)**, todas estas propiedades son consecuencias lógicas de la estructura de cuerpo ordenado de $\mathbb{R}$.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Definición de orden (Apostol I.3.4)**: La relación $x < y$ (o $y > x$) se define estrictamente como la condición de que la diferencia $y - x$ sea un número positivo ($y - x \in \mathbb{R}^+$).
> 2. **Ley de Tricotomía (Teorema I.16)**: Para cualquier par de números reales $a$ y $b$, se cumple exactamente una (y solo una) de las siguientes relaciones: $a < b$, $b < a$ o $a = b$.
> 3. **Propiedad Transitiva (Teorema I.17)**: Si $x < y$ y $y < z$, entonces $x < z$. Esta propiedad es fundamental para el encadenamiento de desigualdades e inecuaciones.
> 4. **Teoremas de potencias y signos**: Apostol demuestra formalmente que si $a \neq 0$, entonces $a^2 > 0$ (Teorema I.20). De este hecho se deriva inmediatamente que $1 > 0$, ya que $1 = 1^2$ (Teorema I.21).
> 5. **Interpretación de inversos**: El teorema I.23 de Apostol confirma que si $a < b$, entonces $-a > -b$, lo que fundamenta la regla del cambio de sentido al multiplicar por $-1$.

---

## La recta real e intervalos

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
y=0|#000000
(-2,0)|label:-2|#000000
(-1,0)|label:-1|#000000
(0,0)|label:0|#000000
(1,0)|label:1|#000000
(1.414,0)|label:√2|#000000
(2,0)|label:2|#000000
(3,0)|label:3|#000000
(3.141,0)|label:π|#000000
```

Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**
    - $[a, b] = \{x \in \mathbb{R} \mid a \le x \le b\}$

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
    - $]a, b[ = \{x \in \mathbb{R} \mid a < x < b\}$

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
    - $[a, b[ = \{x \in \mathbb{R} \mid a \le x < b\}$

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
    - $[a, +\infty[ = \{x \in \mathbb{R} \mid x \ge a\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x>=2|#005F73
(2,0)|#005F73|label:a
```


- $]-\infty, b[ = \{x \in \mathbb{R} / x < b\}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x<3|#005F73
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

---

## Valor absoluto

```cornell
::cue
valor absoluto · distancia · módulo · magnitud<br>
¿Cómo se define el valor absoluto de un número real de forma analítica?<br>
¿Qué interpretación geométrica tiene el valor absoluto en la recta real?<br>
¿Cuáles son las propiedades fundamentales que rigen las operaciones con barras de valor absoluto?<br>
$|x| = \sqrt{x^2}$<br>
ver también: intervalos<br>
no confundir $|x| < a$ con la unión de intervalos.<br>
mnemónico: **S**implemente **P**ara **M**i **D**iversión **I**ntenté **C**omprar **R**opa **M**uy **M**oderna, **T**rajes **S**ueltos. (Signos, Positividad, Multiplicación, División, Igualdad, Cuadrado, Raíz, Menor, Mayor, Triangular, Schwarz).


::note
**Definición**
Sea $x \in \mathbb{R}$
$|x| = \text{Valor absoluto de } x$

$$|x| = \begin{cases} x \;; & x \ge 0 \\ -x \;; & x < 0 \end{cases}$$

**Ejemplos**
- $|3| = 3$
- $|1,5| = \dfrac{3}{2} = 1,5$
- $|-1,6| = 1,6$
etc.

**Propiedades**
Si $x, y \in \mathbb{R}$

1. **Signo opuesto**
	- $|-x| = |x|$
2. **No negatividad**
	- $|x| \ge 0$
3. **Producto**
	- $|xy| = |x||y|$
4. **Cociente**
	- $\left| \dfrac{x}{y} \right| = \dfrac{|x|}{|y|} \; ; \; y \ne 0$
5. **Igualdad**
	- $(|x| = a \wedge a > 0) \implies (x = a \vee x = -a)$
6. **Cuadrado**
	- $|x^2| = |x|^2 = x^2$
7. **Raíz cuadrada**
	- $\sqrt{x^2} = |x|$
8. **Menor que (intervalo)**
	- $(|x| \le a \wedge a > 0) \implies (-a \le x \le a)$
9. **Mayor que (unión)**
	- $|x| \ge a \implies (x \ge a \vee x \le -a)$
10. **Desigualdad triangular**
	- $|x + y| \le |x| + |y|$
11. **Desigualdad de Schwarz**
	- $|xy| \ge xy$

> [!note] Nota manuscrita
> En el desarrollo se observa la importancia de la propiedad $\sqrt{x^2} = |x|$ para evitar la contradicción $2 = 3$.

```

> [!summary] El valor absoluto define la magnitud no negativa de un número real, representable como su distancia al origen y sujeta a propiedades algebraicas de orden y desigualdad.

##### Ej. Analizar la V o F de:
$$\begin{array}{rcll}
  -6 & = & -6 \\
  4 - 10 & = & 9 - 15 \\
  2^2 - 2 \cdot 2 \cdot \dfrac{5}{2} + \left(\dfrac{5}{2}\right)^2 & = & 3^2 - 2 \cdot 3 \cdot \dfrac{5}{2} + \left(\dfrac{5}{2}\right)^2 & (\text{completando cuadrados}) \\
  \left( 2 - \dfrac{5}{2} \right)^2 & = & \left( 3 - \dfrac{5}{2} \right)^2 \\
  \sqrt{\left( 2 - \dfrac{5}{2} \right)^2} & = & \sqrt{\left( 3 - \dfrac{5}{2} \right)^2} \\
  \left| 2 - \dfrac{5}{2} \right| & = & \left| 3 - \dfrac{5}{2} \right| & (\text{aplicando prop. 7}) \\
  \left| -\dfrac{1}{2} \right| & = & \left| \dfrac{1}{2} \right| \\
  \dfrac{1}{2} & = & \dfrac{1}{2} & (V)
\end{array}$$

> [!note] Complemento (Nivel B)
> 
> De acuerdo con la bibliografía consultada, se refuerzan los siguientes conceptos:
> 
> 1. **Definición Geométrica:** El valor absoluto de un número real $a$ se define formalmente como la distancia desde $a$ hasta 0 en la recta numérica real. Dado que las distancias nunca son negativas, $|a| \ge 0$ para cualquier número.
> 2. **Distancia entre puntos:** Para cualesquiera dos números reales $x$ e $y$, el valor $|x - y|$ representa la distancia geométrica entre los puntos $x$ e $y$ sobre la recta real.
> 3. **Propiedad de la raíz:** Es un error común simplificar $\sqrt{x^2} = x$ sin considerar el signo. La definición correcta es $\sqrt{x^2} = |x|$, asegurando un resultado no negativo independientemente del signo de la base original.
> 4. **Desigualdad Triangular:** Esta propiedad establece que el valor absoluto de la suma de dos números no puede exceder la suma de sus valores absolutos ($|a + b| \le |a| + |b|$). La igualdad se cumple únicamente si $a$ y $b$ tienen el mismo signo o si alguno es cero.

---

# Solución de inecuaciones en variable $x$

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
y=0 |x>2| #005F73
(2,0) | open | #005F73
x > 2 \{y=0\} | #005F73
(2, 0) | label: (d-b)/(a-c)
```

$C_s = \left] \dfrac{d - b}{a - c}, +\infty \right[ = \left\{ x \in \mathbb{R} \mid x > \dfrac{d - b}{a - c} \right\}$

> [!note] El manuscrito presenta el despeje asumiendo que el coeficiente resultante es positivo para mantener el sentido de la desigualdad.

````

> [!summary](Procedimiento para resolver desigualdades de primer grado mediante el aislamiento de la variable y la determinación del intervalo solución en la recta real.)

##### Ej. Hallar el $C_s$: $(4x - 3)^2 \leq (4x + 1)^2$

$$\begin{array}{rcl}
 16x^2 - 24x + 9 & \leq & 16x^2 + 8x + 1 \\ 8 & \leq & 32x \\ \dfrac{8}{32} & \leq & x \\ x & \geq & \dfrac{1}{4} \end{array}
 $$

**$C_s$**

```desmos-graph
left=-1; right=3; bottom=-1; top=1;
width=320; height=80;
---
y=0 |x >= 0.25 | #005F73
(0.25, 0) | #005F73
x >= 0.25 \{y=0\} | #005F73
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

## Método de signos para solución de inecuaciones

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
y=0|#000000
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

---


De los apuntes de la materia (**apuntesT0**), se presenta la resolución del ejercicio de inecuaciones con condiciones, finalizando así el tema de Números Reales antes del inicio de Funciones Reales.

##### ej. Resolución de inecuación con condiciones

La condición: $$\begin{array}{rcccl} x(x+1) & \ge & 0 \ \end{array}$$

Evaluación por puntos críticos: $x = 0$ $x = -1$

Prueba de signos: Si $x = 1 \implies (+)(+) = (+) \ge 0 \quad (\text{Verdadera})$ Si $x = -1, 0 \implies 0 \ge 0 \quad (\text{Verdadera})$

> [!important] ¡Toda condición siempre se debe $\cap$ (intersecar) con el $C_s$ hallado!

$$C_s = ]-3, -1] \cup [0, 2[$$

```
left=-5; right=5; bottom=-1.5; top=1.5;
width=320; height=100;
---
y=0|-3<x<=-1|#005F73
y=0|0<=x<2|#005F73
(-3,0)|open|#005F73
(-1,0)|#005F73
(0,0)|#005F73
(2,0)|open|#005F73
```

> [!summary] Determinación del conjunto solución final mediante la intersección de los intervalos obtenidos con las condiciones de restricción impuestas por la inecuación original.

> [!note] Complemento (Nivel B)
> 
> **Definición de resolución de desigualdades** Resolver una desigualdad significa determinar el conjunto de números $x$ para los que la desigualdad es verdadera. A este conjunto resultante se le denomina **conjunto solución** ($C_s$). En problemas complejos, el $C_s$ final surge de la intersección ($\cap$) entre la solución algebraica del cuerpo de la inecuación y las restricciones o condiciones de existencia definidas por los términos de la misma.












---
---

### erorres de notebook
1. {} esta mal deberia ser \{   \ }
$\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1} = 1$
2. <\array} esta mal deberia ser \end{array}
$$\begin{array}{rcl} a + b & = & a + c \ (-a) + (a + b) & = & (-a) + (a + c) \ [(-a) + a] + b & = & [(-a) + a] + c \ 0 + b & = & 0 + c \ b & = & c </array}$$

3. demostraciones deben estar fuera de cornell? notebooklm las transcribio dentro

4. NOTEBOOKLM olvida la estructura de los array no coloca el doble `\\` para el salto de linea creo que esta tarea sera delegada a claude corregir los arrays

##### cosas por hacer
en las guias colocar desmos-graph para que notebooklm lo haga tambien


---

%%


galaxy-links

%%
