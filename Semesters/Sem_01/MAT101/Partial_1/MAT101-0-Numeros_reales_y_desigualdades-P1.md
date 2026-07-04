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

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Axiomas de cuerpo de los números reales (ℝ)

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
    - $a^{-1} = \frac{1}{a}$ es el inverso de $a$.
7. **Distributividad**
    - $a(b + c) = ab + ac$

--- end-column ---

🔑 **Claves**

Axiomas · Cuerpo · Reales · Neutros · Inversos

¿Cuáles son las reglas básicas que rigen la suma y multiplicación? ¿Qué elementos permiten la existencia de operaciones inversas? ¿Cómo se relacionan la suma y el producto aritmético?

$a + (-a) = 0$ $a \cdot a^{-1} = 1, a \neq 0$

ver también: Axiomas de orden

No confundir el neutro aditivo ($0$) con el neutro multiplicativo ($1$).

**C**lausura, **C**onmutativa, **A**sociativa, **N**eutros, **N**egativos, **I**nversos, **D**istributiva (**CCANNID**)

--- end-multi-column ---

> **Resumen:** Definición de los siete axiomas fundamentales que establecen a los números reales como un cuerpo algebraico bajo las operaciones de adición y multiplicación.

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

--- start-multi-column: cornell-T0-002

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Axiomas de igualdad

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

--- end-column ---

🔑 **Claves**

Igualdad · Ecuación · Identidad · Transitividad

¿Qué propiedades rigen la relación de equivalencia en $\mathbb{R}$? ¿Cuál es la diferencia técnica entre una ecuación y una identidad? ¿Cómo se definen formalmente la resta y la división?

$(a = b \land b = c) \Rightarrow a = c$

ver también: Axiomas de cuerpo

No confundir una Identidad (válida para todo el dominio) con una Ecuación (válida para valores específicos).

--- end-multi-column ---

> **Resumen:** Establece las propiedades lógicas de la igualdad (reflexiva, simétrica y transitiva) y clarifica que la resta y división son extensiones de la suma y multiplicación por el opuesto/recíproco.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con **Thomas (Apéndice 6)** y **Apostol (Cap. 0, sección I 3.2)**, la estructura de los números reales se basa en el concepto de **Cuerpo ordenado**.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Propiedad de sustitución:** Aunque no se lista explícitamente en el manuscrito, es un axioma implícito de la igualdad: si $a = b$, entonces $a$ puede ser reemplazado por $b$ en cualquier proposición matemática sin alterar el valor de verdad de la misma.
> 2. **Unicidad de operaciones:** Apostol enfatiza que la suma $x + y$ y el producto $xy$ están **unívocamente determinados** por sus elementos. Esto garantiza que si $a = b$, entonces $a + c = b + c$ y $ac = bc$.
> 3. **Definiciones derivadas:** La resta y la división no se consideran operaciones independientes en la axiomática pura, sino que se definen estrictamente a través de la existencia de **opuestos** ($a - b := a + (-b)$) y **recíprocos** ($\frac{a}{b} := a \cdot b^{-1}$), tal como sugiere la nota del manuscrito.

---

--- start-multi-column: cornell-T0-003

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Teoremas sobre números reales (ℝ)

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

### Prueba de (1)

$a + b = a + c \Rightarrow b = c$ Hipótesis: $a + b = a + c$ Tesis: $b = c$

Demostración: 
$$\begin{array}{rcl}
b & = & b \quad &(\text{ax. reflexivo}) \\
& = & b + 0 \quad &(\text{ax. } \exists \text{ neutro}) \\
& = & b + [a + (-a)] \quad &(\text{ax. } \exists \text{ negativo}) \\
& = & (b + a) + (-a) \quad &(\text{ax. asociativo}) \\
& = & (a + b) + (-a) \quad &(\text{ax. conmutativo}) \\
& = & (a + c) + (-a) \quad &(\text{Hipótesis}) \\
& = & (c + a) + (-a) \quad &(\text{ax. conmutativo}) \\
& = & c + [a + (-a)] \quad &(\text{ax. asociativo}) \\
& = & c + 0 \quad &(\text{ax. } \exists \text{ negativo}) \\
& = & c \quad &(\text{ax. } \exists \text{ neutro}) \\
b & = & c \quad & (\text{LQQD})
\end{array}$$

--- end-column ---

🔑 **Claves**

Teoremas · Simplificación · Elemento cero · Opuestos · Recíprocos

¿Cómo se demuestra formalmente la ley de cancelación? ¿Qué ocurre al multiplicar cualquier número real por cero? ¿Cuáles son las propiedades de los signos en la multiplicación?

$a \cdot b = 0 \Rightarrow (a = 0 \lor b = 0)$ $a + b = a + c \Rightarrow b = c$

ver también: Axiomas de cuerpo

No confundir la ley de cancelación de la suma con la del producto; esta última requiere estrictamente que el factor sea distinto de cero ($a \neq 0$).

--- end-multi-column ---

> **Resumen:** Conjunto de 13 teoremas fundamentales derivados de los axiomas de cuerpo que rigen las operaciones algebraicas, incluyendo leyes de cancelación, propiedades del cero y aritmética de fracciones.

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

--- start-multi-column: cornell-T0-004

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Axiomas de orden de los números reales  (ℝ)

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

--- end-column ---

🔑 **Claves**

Orden · Positividad · Tricotomía · Reales positivos

¿Cuáles son las condiciones para que la suma y el producto conserven el orden? ¿Qué significa que un conjunto sea "ordenado"? ¿Cómo se define formalmente un número negativo en función de los positivos?

$a > 0 \Leftrightarrow a \in \mathbb{R}^+$ $x < y \Leftrightarrow y - x \in \mathbb{R}^+$

ver también: Axiomas de cuerpo

No confundir la relación de orden ($<, >$) con la pertenencia a un subconjunto ($\mathbb{R}^+$). El orden se deriva de la positividad.

--- end-multi-column ---

> **Resumen:** Los axiomas de orden postulan la existencia de un subconjunto de números positivos ($\mathbb{R}^+$) cerrado bajo la suma y el producto, permitiendo definir las relaciones de desigualdad y la estructura de cuerpo ordenado para $\mathbb{R}$.

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

--- start-multi-column: cornell-T0-005

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Teoremas de desigualdades e inecuaciones

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
    - $0 < a < b \Rightarrow \frac{1}{a} > \frac{1}{b}$

--- end-column ---

🔑 **Claves**

Desigualdad · Inecuación · Regla de signos · Inversos

¿Cómo afecta multiplicar por un número negativo a una desigualdad? ¿Qué condiciones deben cumplirse para que el producto de dos reales sea positivo? ¿Cómo se comportan los inversos multiplicativos en una relación de orden?

$a > b \land c < 0 \Rightarrow ac < bc$ $0 < a < b \Rightarrow \frac{1}{a} > \frac{1}{b}$

ver también: Axiomas de orden

No confundir la elevación a una potencia par (requiere base positiva para mantener el orden) con la potencia impar (mantiene el orden siempre).

**S**uma, **A**dición, **M**ultiplicación (pos/neg), **R**egla de signos, **C**uadrado, **U**nidad, **I**nversos, **E**levación (2/3)

--- end-multi-column ---

> **Resumen:** Conjunto de 12 leyes operativas que rigen el comportamiento de las desigualdades ante operaciones aritméticas y potencias en el conjunto de los números reales.

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

## La recta real intervalos

--- start-multi-column: cornell-T0-006

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```desmos-graph
left=-5; right=5; bottom=-1; top=1;
width=320; height=150;
---
y=0 | #262626
(-2,0) | label: -2 | #262626
(-1,0) | label: -1 | #262626
(0,0) | label: 0 | #262626
(1,0) | label: 1 | #262626
(1.414,0) | label: \sqrt{2} | #262626
(2,0) | label: 2 | #262626
(2.718,0) | label: e | #262626
(3,0) | label: 3 | #262626
(3.141,0) | label: \pi | #262626
```

- **Un intervalo es un subconjunto de la recta real**

1. **Intervalo cerrado**
    - $x = [a, b] = {x / a \le x \le b}$
2. **Intervalo abierto**
    - $x = ]a, b[ = {x / a < x < b}$
3. **Intervalo semiabierto**
    - $x = ]a, b] = {x / a < x \le b}$
4. **Intervalos infinitos**
    - $x = [a, +\infty[ = {x / x \ge a}$
    - $x = ]-\infty, b[ = {x / x < b}$

> [!note] Valores extremos Los puntos $a$ y $b$ se denominan extremos de los intervalos.

```desmos-graph
left=-1; right=6; bottom=-1; top=5;
width=320; height=250;
---
a=1
b=4
y=0 | a <= x <= b | #C1121F
(a,0) | #C1121F
(b,0) | #C1121F
(0.2,0) | label: "[a, b]" | #C1121F | hidden

y=1 | a < x < b | #1D4ED8
(1,1) | open | #1D4ED8
(4,1) | open | #1D4ED8
(0.2,1) | label: "]a, b[" | #1D4ED8 | hidden

y=2 | a < x <= b | #059669
(1,2) | open | #059669
(b,2) | #059669
(0.2,2) | label: "]a, b]" | #059669 | hidden

y=3 | x >= a | #D97706
(a,3) | #D97706
(0.2,3) | label: "[a, \infty[" | #D97706 | hidden

y=4 | x < b | #7C3AED
(4,4) | open | #7C3AED
(0.2,4) | label: "]-\infty, b[" | #7C3AED | hidden
```

--- end-column ---

🔑 **Claves**

Correspondencia biunívoca · Subconjunto · Recta real · Intervalos · Extremos

¿Cómo se relaciona el conjunto de los números reales con la geometría? ¿Cuál es la diferencia notacional y gráfica entre un intervalo abierto y uno cerrado? ¿Qué caracteriza a un intervalo infinito?

${x / a \le x \le b}$

ver también: [[Conjuntos]]

no confundir $]a, b[$ con $(a, b)$ en contextos de puntos del plano.

%`desmos-graph %`

--- end-multi-column

> **Resumen:** La recta real es la representación geométrica de $\mathbb{R}$, donde los intervalos son segmentos de recta definidos por sus valores extremos y su inclusión o exclusión.

> [!note] Complemento (Nivel B)
> 
> **Definición formal de intervalo:** Un subconjunto $I$ de la recta real $\mathbb{R}$ se denomina **intervalo** si contiene al menos dos números y tiene la propiedad de que, para cualquier par de elementos $x, y \in I$, todo número real $z$ tal que $x < z < y$ también pertenece a $I$.
> 
> De acuerdo con Thomas, los intervalos se clasifican según su acotación y la inclusión de sus puntos frontera:
> 
> 1. **Intervalos finitos:** Tienen longitud finita $b - a$.
>     - **Cerrado:** Contiene ambos extremos $[a, b]$.
>     - **Abierto:** No contiene los extremos $(a, b)$ o $]a, b[$.
>     - **Semiabierto:** Contiene solo uno de los extremos, ej. $(a, b]$ o $[a, b)$.
> 2. **Intervalos infinitos:** Se extienden ilimitadamente en una o ambas direcciones.
>     - El conjunto de todos los números reales $\mathbb{R}$ es el intervalo $(-\infty, \infty)$, el cual se considera simultáneamente abierto y cerrado.


















---
---

### erorres de notebook
1. {} esta mal deberia ser \{   \ }
$\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1} = 1$
2. <\array} esta mal deberia ser \end{array}
$$\begin{array}{rcl} a + b & = & a + c \ (-a) + (a + b) & = & (-a) + (a + c) \ [(-a) + a] + b & = & [(-a) + a] + c \ 0 + b & = & 0 + c \ b & = & c </array}$$

3. demostraciones deben estar fuera de cornell? notebooklm las transcribio dentro

4. NOTEBOOKLM olvida la estructura de los array no coloca el doble `\\` para el salto de linea creo que esta tarea sera delegada a claude corregir los arrays

5. en cornell en desarollo entrego este bloque desmos
   %`desmos-graph %y=0|#444 %(-2,0)|label:-2|#444 %(-1,0)|label:-1|#444 %(0,0)|label:0|#444 %(0.5,0)|label:1/2|#444 %(1,0)|label:1|#444 %(1.414,0)|label:\sqrt{2}|#444 %(2,0)|label:2|#444 %(2.718,0)|label:e|#444 %(3,0)|label:3|#444 %(3.141,0)|label:\pi|#444 %`







---

%%


galaxy-links

%%
