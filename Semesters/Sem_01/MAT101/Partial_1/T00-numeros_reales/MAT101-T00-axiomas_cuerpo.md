---
title: "Axiomas de cuerpo de los números reales"
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

%%
galaxy-links
[[MAT101-T00-star]]
%%
