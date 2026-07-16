---
title: "Teoremas de desigualdades e inecuaciones"
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

%%
# galaxy-links
[[MAT101-T00-star]]
%%
