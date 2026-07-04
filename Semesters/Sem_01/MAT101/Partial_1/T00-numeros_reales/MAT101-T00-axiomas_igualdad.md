---
title: "Axiomas de igualdad"
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

%%
galaxy-links
[[MAT101-T00-star]]
%%
