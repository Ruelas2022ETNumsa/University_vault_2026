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













---- erorres de notebook
1. {} esta mal deberia ser \{   \ }
$\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1} = 1$
2. <\array} esta mal deberia ser \end{array}
$$\begin{array}{rcl} a + b & = & a + c \ (-a) + (a + b) & = & (-a) + (a + c) \ [(-a) + a] + b & = & [(-a) + a] + c \ 0 + b & = & 0 + c \ b & = & c </array}$$

3. demostraciones deben estar fuera de cornell? notebooklm las transcribio dentro

4. NOTEBOOKLM olvida la estructura de los array no coloca el doble `\\` para el salto de linea creo que esta tarea sera delegada a claude corregir los arrays









---

%%


galaxy-links

%%
