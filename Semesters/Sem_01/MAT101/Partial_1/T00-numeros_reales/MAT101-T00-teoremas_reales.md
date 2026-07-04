---
title: "Teoremas sobre números reales (ℝ)"
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

%%
galaxy-links
[[MAT101-T00-star]]
%%
