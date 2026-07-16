---
title: "Axiomas de orden de los números reales  (ℝ)"
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

%%
# galaxy-links
[[MAT101-T00-star]]
%%