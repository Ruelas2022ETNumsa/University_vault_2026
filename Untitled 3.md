--- start-multi-column: cornell-T0-003

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

## La recta real e intervalos

📝 **Desarrollo**

Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```desmos-graph
left=-5;right=5;bottom=-1;top=1;
width=320;height=100;
---
y=0|#000000
(-2,0)|label:-2|#000000
(-1,0)|label:-1|#000000
(0,0)|label:0|#000000
(1,0)|label:1|#000000
(1.414,0)|label:\sqrt{2}|#000000
(2,0)|label:2|#000000
(3,0)|label:3|#000000
(3.141,0)|label:\pi|#000000
```

Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**
    - $[a, b] = {x \in \mathbb{R} / a \le x \le b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<=x<=4|#005F73
(1,0)|#005F73|label:a
(4,0)|#005F73|label:b
```

2. **Intervalo abierto**
    - $]a, b[ = {x \in \mathbb{R} / a < x < b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<x<4|#005F73
(1,0)|open|#005F73|label:a
(4,0)|open|#005F73|label:b
```

3. **Intervalo semiabierto**
    - $[a, b[ = {x \in \mathbb{R} / a \le x < b}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|1<=x<4|#005F73
(1,0)|#005F73|label:a
(4,0)|open|#005F73|label:b
```

4. **Intervalos infinitos**
    - $[a, +\infty[ = {x \in \mathbb{R} / x \ge a}$

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x>=2|#005F73
(2,0)|#005F73|label:a
```

```desmos-graph
- $]-\infty, b[ = \{x \in \mathbb{R} / x < b\}$
```

```desmos-graph
left=-1;right=5;bottom=-1;top=1;
width=320;height=60;
---
y=0|#000000|DASHED
0<=y<=0|x<3|#005F73
(3,0)|open|#005F73|label:b
```

> [!note] En el manuscrito se etiqueta a los límites $a$ y $b$ de los intervalos como "valores extremos".

--- end-column ---

🔑 **Claves**

Correspondencia biunívoca · Recta real · Intervalo · Subconjunto · Extremos

¿Qué implica la correspondencia "uno a uno" entre $\mathbb{R}$ y la recta? ¿Cómo se define formalmente un intervalo como subconjunto de $\mathbb{R}$? ¿Qué diferencia gráfica y simbólica existe entre extremos abiertos y cerrados?

Intervalo: $I \subseteq \mathbb{R}$

ver también: [[Axiomas de orden]]

no confundir $]a, b[$ (notación de corchetes invertidos) con $(a, b)$ (notación de paréntesis).

%%```desmos-graph```%%

--- end-multi-column ---

> **Resumen:** Los intervalos son subconjuntos de la recta real que agrupan números comprendidos entre dos extremos, cuya inclusión se representa mediante corchetes (cerrados) o su exclusión mediante corchetes invertidos o paréntesis (abiertos).

> [!note] Complemento (Nivel B)
> 
> Formalmente, la **recta real** (o eje real) es la representación geométrica donde cada punto de la recta corresponde a un único número real y viceversa.
> 
> Los intervalos se clasifican en:
> 
> 1. **Intervalos finitos:** Corresponden a segmentos de recta. Los puntos $a$ y $b$ se denominan **puntos frontera**, mientras que los puntos entre ellos son **puntos interiores**.
> 2. **Intervalos infinitos:** Representan rayos (semirrectas) o la totalidad de la recta real $(-\infty, \infty)$.
> 
> El símbolo $\infty$ (infinito) no es un número real, sino una notación para indicar que el conjunto no está acotado en una dirección determinada.




---


--- start-multi-column: cornell-T0-003

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

## Valor absoluto

📝 **Desarrollo** Definición. Sea $x \in \mathbb{R}$ $|x| =$ Valor absoluto de $x$

$$|x| = \left{ \begin{array}{rcl} x & ; & x \geq 0 \ -x & ; & x < 0 \end{array} \right.$$

**Ejemplos:**

- $|3| = 3$
- $|-1,6| = 1,6$
- $|1,5| = \frac{3}{2} = 1,5$

### Propiedades

Sea $x, y \in \mathbb{R}$

1. $|-x| = |x|$
2. $|x| \geq 0$
3. $|x \cdot y| = |x| \cdot |y|$
4. $\left| \frac{x}{y} \right| = \frac{|x|}{|y|} ; y \neq 0$
5. $(|x| = a \wedge a > 0) \Rightarrow (x = a \vee x = -a)$
6. $|x|^2 = |x|^2 = x^2$
7. $\sqrt{x^2} = |x|$
8. $(|x| < a \wedge a > 0) \Rightarrow -a < x < a$
9. $|x| > a \Rightarrow (x > a \vee x < -a)$
10. $|x + y| \leq |x| + |y|$ $\rightarrow$ Desigualdad triangular
11. $|x \cdot y| \geq x \cdot y$ $\rightarrow$ Desigualdad de Schwarz

--- end-column ---

🔑 **Claves**

valor absoluto · distancia · magnitud · desigualdad triangular

¿Cómo se define formalmente el valor absoluto de un número real? ¿Cuál es la interpretación geométrica de $|x|$? ¿Qué propiedades permiten eliminar las barras de valor absoluto en una inecuación?

$|x| = \sqrt{x^2}$ $\sqrt{x^2} = |x|$

No confundir $\sqrt{x^2} = x$ (solo válido si $x \geq 0$) con la identidad general $\sqrt{x^2} = |x|$.

--- end-multi-column

> **Resumen:** El valor absoluto representa la magnitud no negativa de un número real, interpretándose geométricamente como su distancia al origen en la recta numérica.

##### Ej. Analizar la Verdad (V) o Falsedad (F) de:

$-6 = -6$ $4 - 10 = 9 - 15$ $2^2 - 2 \cdot 5 \cdot \left(\frac{5}{2}\right) + \left(\frac{5}{2}\right)^2 = 3^2 - 3 \cdot 5 \cdot \left(\frac{5}{2}\right) + \left(\frac{5}{2}\right)^2$ $\left(2 - \frac{5}{2}\right)^2 = \left(3 - \frac{5}{2}\right)^2$ $\sqrt{\left(2 - \frac{5}{2}\right)^2} = \sqrt{\left(3 - \frac{5}{2}\right)^2}$ $|2 - 2,5| = |3 - 2,5|$ $|-0,5| = |0,5|$ $\frac{1}{2} = \frac{1}{2} \quad V$

> [!note] Complemento (Nivel B)
> 
> La definición formal de valor absoluto establece que para todo número real $x$, el valor $|x|$ es el máximo entre $x$ y $-x$; es decir, $|x| = \max{x, -x}$.
> 
> **Interpretación geométrica:** En la recta real, $|x|$ representa la **distancia** desde el punto $x$ hasta el origen $0$. De manera más general, la expresión $|a - b|$ representa la distancia entre los puntos $a$ y $b$.
> 
> **Teorema de existencia:** Si $a \geq 0$, entonces $|x| \leq a$ si y solo si $-a \leq x \leq a$. Este teorema es fundamental para la resolución de inecuaciones con valor absoluto, ya que permite transformar una desigualdad con valor absoluto en una desigualdad simultánea (o intervalo) sin barras.
