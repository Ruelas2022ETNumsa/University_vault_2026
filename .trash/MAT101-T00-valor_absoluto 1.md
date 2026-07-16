---
title: "Valor absoluto"
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

%%
# galaxy-links
[[MAT101-T00-star]]
%%
