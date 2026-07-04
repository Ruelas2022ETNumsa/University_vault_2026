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
cssclasses:
  - cornell-note
---

# Números reales y desigualdades

> [!title] Axiomas de cuerpo de los números reales (ℝ)

> [!cue] ¿Cuáles son las reglas básicas que rigen la suma y multiplicación?
>. 
> .
> .
>[!cue]¿Qué elementos permiten la existencia de 
>operaciones inversas?

Si $a, b, c \in \mathbb{R}$:
1. **Clausura**
    $a + b \in \mathbb{R}$ y $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
	- $a + b = b + a$
	- $a \cdot b = b \cdot a$
3. **Asociatividad**
	- $(a + b) + c = a + (b + c)$
	- $(a \cdot b) \cdot c = a \cdot (b \cdot c)$


> [!cue] ¿Qué elementos permiten la existencia de operaciones inversas?

4. **Existencia de neutros**
	- $\exists\;0 \in \mathbb{R} : a + 0 = a$ — neutro aditivo
	- $\exists\;1 \in \mathbb{R} : a \cdot 1 = a$ — neutro multiplicativo
5. **Existencia de negativos** — $\forall a \in \mathbb{R},\; \exists\, {-a} \in \mathbb{R} : a + (-a) = 0$
6. **Existencia de inversos** — $\forall a \in \mathbb{R} - \{0\},\; \exists\, a^{-1} \in \mathbb{R} : a \cdot a^{-1} = 1$
7.  **Distributividad** — $a(b + c) = ab + ac$

> ⚠️ No confundir el neutro aditivo ($0$) con el neutro multiplicativo ($1$).

> [!cue] ¿Cómo se relacionan la suma y el producto aritmético?

La **distributividad** es el único axioma que vincula ambas operaciones:
$a(b+c) = ab + ac$

Identidades clave:
- $a + (-a) = 0$
- $a \cdot a^{-1} = 1,\quad a \neq 0$

**Mnemotécnico — CCANNID:**
**C**lausura · **C**onmutativa · **A**sociativa · **N**eutros · **N**egativos · **I**nversos · **D**istributiva

> 🔗 ver también: Axiomas de orden

**Palabras clave:** Axiomas · Cuerpo · Reales · Neutros · Inversos

> [!summary]
> Los siete axiomas de cuerpo establecen a $\mathbb{R}$ como estructura algebraica bajo suma y multiplicación, garantizando clausura, conmutatividad, asociatividad, neutros, inversos y distributividad.

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