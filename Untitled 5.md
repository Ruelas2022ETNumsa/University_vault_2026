--- start-multi-column: cornell-T0-003

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

## Valor absoluto

📝 **Desarrollo** Definición. Sea $x \in \mathbb{R}$ $|x| =$ Valor absoluto de $x$

$$
|x|=
\begin{cases}
x,  & x \ge 0\\
-x, & x < 0
\end{cases}
$$

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







## Valor absoluto

````cornell
::cue
Valor absoluto · Distancia · Desigualdad triangular · Propiedades

¿Cómo se define formalmente el valor absoluto de un número real?

¿Qué interpretación geométrica tiene la expresión $|a - b|$?

¿Cuáles son las propiedades fundamentales para resolver ecuaciones e inecuaciones con valor absoluto?

$|x| = \begin{cases} x & \text{si } x \ge 0 \\ -x & \text{si } x < 0 \end{cases}$

ver también: [[La recta real e intervalos]]

::note
**Def.** $x \in \mathbb{R}$
$|x| = \text{Valor absoluto de } x$
$$|x| = \begin{cases} x ; & x \ge 0 \\ -x ; & x < 0 \end{cases}$$

- **Por ejemplo:**
$|3| = 3$
$|-1.6| = 1.6$
$|1.5| = \frac{3}{2} = 1.5$
etc.

**Propiedades**
- $x, y \in \mathbb{R}$
1. **Simetría**
	- $|-x| = |x|$
2. **No negatividad**
	- $|x| \ge 0$
3. **Producto**
	- $|xy| = |x||y|$
4. **Cociente**
	- $\left| \frac{x}{y} \right| = \frac{|x|}{|y|} ; y \neq 0$
5. **Igualdad**
	- $(|x| = a \wedge a > 0) \Rightarrow (x = a \vee x = -a)$
6. **Potencia cuadrada**
	- $|x|^2 = x^2$
7. **Raíz cuadrada del cuadrado**
	- $\sqrt{x^2} = |x|$
8. **Intervalo abierto (menor que)**
	- $(|x| < a \wedge a > 0) \Rightarrow (x < a \wedge x > -a) \to -a < x < a$
9. **Intervalo abierto (mayor que)**
	- $|x| > a \Rightarrow (x > a \vee x < -a)$
10. **Desigualdad triangular**
	- $|x + y| \le |x| + |y|$
11. **Desigualdad de Schwarz**
	- $|x \cdot y| \ge xy$

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=320; height=240;
---
y=\abs(x)|#005F73
(0,0)|label: |#005F73
```

````

> **Resumen:** El valor absoluto representa la distancia de un número al origen, caracterizándose por ser siempre no negativo y cumplir propiedades de distribución respecto al producto y cociente, además de la desigualdad triangular.

##### Ej. Analizar la V o F de:

$$\begin{array}{rcll} -6 & = & -6 & \ 4 - 10 & = & 9 - 15 & \ 2^2 - 2 \cdot 5(\frac{5}{2}) + (\frac{5}{2})^2 & = & 3^2 - 3 \cdot 5(\frac{5}{2}) + (\frac{5}{2})^2 & (\text{completando cuadrados}) \ (2 - \frac{5}{2})^2 & = & (3 - \frac{5}{2})^2 & \ \sqrt{(2 - \frac{5}{2})^2} & = & \sqrt{(3 - \frac{5}{2})^2} & \ |2 - \frac{5}{2}| & = & |3 - \frac{5}{2}| & (\text{por Prop. 7}) \ |-\frac{1}{2}| & = & |\frac{1}{2}| & \ \frac{1}{2} & = & \frac{1}{2} & (\text{LQQD}) \end{array}$$ $\therefore V$

> [!note] Complemento (Nivel B)
> 
> De acuerdo con las fuentes de **Apostol** y **Stewart**, el valor absoluto de un número real $x$ se define formalmente como la distancia entre $x$ y el $0$ en la recta real.
> 
> **Interpretación geométrica de la distancia:** Si $a$ y $b$ son puntos en la recta real, la distancia entre ellos es $d(a, b) = |a - b|$. Esta cantidad es siempre idéntica a $|b - a|$ debido a la propiedad de simetría $|x| = |-x|$.
> 
> **Propiedad de la raíz (Refuerzo):** Es vital recordar que $\sqrt{a^2} = |a|$. No es correcto afirmar que $\sqrt{a^2} = a$ a menos que se garantice de antemano que $a \ge 0$.
> 
> **Propiedades adicionales omitidas en el manuscrito:**
> 
> 1. **Módulo de la diferencia:** $| |a| - |b| | \le |a - b|$.
> 2. **Desigualdad triangular extendida:** $\left| \sum_{k=1}^{n} a_k \right| \le \sum_{k=1}^{n} |a_k|$.