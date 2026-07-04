---
cssclasses:
  - cornell-note
---

> [!title] Valor absoluto

> [!cue] ¿Cómo se define formalmente el valor absoluto de un número real?

**Definición.** Sea $x \in \mathbb{R}$:

$|x| = \left\{ \begin{array}{rcl} x & ; & x \geq 0 \\ -x & ; & x < 0 \end{array} \right.$

**Ejemplos:**
- $|3| = 3$
- $|-1{,}6| = 1{,}6$
- $|1{,}5| = \frac{3}{2} = 1{,}5$

> [!cue] ¿Cuál es la interpretación geométrica de $|x|$?

En la recta real, $|x|$ representa la **distancia** desde el punto $x$ hasta el origen $0$.
Más general: $|a - b|$ es la distancia entre $a$ y $b$.

Identidad clave: $|x| = \sqrt{x^2}$

> ⚠️ No confundir $\sqrt{x^2} = x$ (solo válido si $x \geq 0$) con la identidad general $\sqrt{x^2} = |x|$.

> [!cue] ¿Qué propiedades permiten eliminar las barras en una inecuación?

**Propiedades.** Sea $x, y \in \mathbb{R}$:

1. $|-x| = |x|$
2. $|x| \geq 0$
3. $|x \cdot y| = |x| \cdot |y|$
4. $\left| \dfrac{x}{y} \right| = \dfrac{|x|}{|y|}\,;\; y \neq 0$
5. $(|x| = a \wedge a > 0) \Rightarrow (x = a \vee x = -a)$
6. $|x|^2 = x^2$
7. $\sqrt{x^2} = |x|$
8. $(|x| < a \wedge a > 0) \Rightarrow -a < x < a$
9. $|x| > a \Rightarrow (x > a \vee x < -a)$
10. $|x + y| \leq |x| + |y|$ — Desigualdad triangular
11. $|x \cdot y| \geq x \cdot y$ — Desigualdad de Schwarz

**Palabras clave:** valor absoluto · distancia · magnitud · desigualdad triangular

> [!summary]
> El valor absoluto representa la magnitud no negativa de un número real, interpretándose geométricamente como su distancia al origen en la recta numérica.

##### Ej. Analizar la Verdad (V) o Falsedad (F) de:

$-6 = -6$ $4 - 10 = 9 - 15$ $2^2 - 2 \cdot 5 \cdot \left(\frac{5}{2}\right) + \left(\frac{5}{2}\right)^2 = 3^2 - 3 \cdot 5 \cdot \left(\frac{5}{2}\right) + \left(\frac{5}{2}\right)^2$ $\left(2 - \frac{5}{2}\right)^2 = \left(3 - \frac{5}{2}\right)^2$ $\sqrt{\left(2 - \frac{5}{2}\right)^2} = \sqrt{\left(3 - \frac{5}{2}\right)^2}$ $|2 - 2,5| = |3 - 2,5|$ $|-0,5| = |0,5|$ $\frac{1}{2} = \frac{1}{2} \quad V$

> [!note] Complemento (Nivel B)
> 
> La definición formal de valor absoluto establece que para todo número real $x$, el valor $|x|$ es el máximo entre $x$ y $-x$; es decir, $|x| = \max{x, -x}$.
> 
> **Interpretación geométrica:** En la recta real, $|x|$ representa la **distancia** desde el punto $x$ hasta el origen $0$. De manera más general, la expresión $|a - b|$ representa la distancia entre los puntos $a$ y $b$.
> 
> **Teorema de existencia:** Si $a \geq 0$, entonces $|x| \leq a$ si y solo si $-a \leq x \leq a$. Este teorema es fundamental para la resolución de inecuaciones con valor absoluto, ya que permite transformar una desigualdad con valor absoluto en una desigualdad simultánea (o intervalo) sin barras.