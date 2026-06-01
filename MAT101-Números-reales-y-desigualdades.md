---
title: "MAT101-Números-reales-y-desigualdades"
galaxy_body: planet
subject: MAT-101
semester: 1
partial: 1
topic: T01_numeros-reales
star: ""
moons: []
comets: []
tags: [MAT-101, galaxy-planet, P1]
date_created: 2026-05-30
status: activo
---

# Números reales y desigualdades
---
## Axiomas de cuerpo de los números reales
Los axiomas de cuerpo son el conjunto de reglas fundamentales que definen cómo operan la adición y la multiplicación en el sistema de los números reales.

Sean $a, b, c \in \mathbb{R}$

|  N  | **Axioma**                 | **Descripción**                                              | **Notación**                                               | **Concepto**                                                                                       |
| :-: | -------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
|  1  | **Clausura**               | Operar dos reales siempre<br>produce un real                 | $a+b \in \mathbb{R}$<br>$a \cdot b \in \mathbb{R}$         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b \in \mathbb{R}\ \wedge\ a \cdot b \in \mathbb{R}$          |
|  2  | **Conmutatividad**         | El orden de los operandos<br>no altera el resultado          | $a+b=b+a$<br>$a \cdot b=b \cdot a$                         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b=b+a\ \wedge\ a \cdot b=b \cdot a$                          |
|  3  | **Asociatividad**          | El agrupamiento no altera<br>el resultado                    | $(a+b)+c=a+(b+c)$<br>$(ab)\,c=a\,(bc)$                     | $\forall\, a,b,c \in \mathbb{R}:$<br>$(a+b)+c=a+(b+c)$<br>$\wedge\ (ab)c=a(bc)$                    |
|  4  | **Distributividad**        | La multiplicación se <br>distribuye sobre la suma            | $a(b+c)=ab+ac$                                             | $\forall\, a,b,c \in \mathbb{R}:$<br>$a(b+c)=ab+ac$                                                |
|  5  | **Elemento neutro**        | El 0 es neutro aditivo;<br>el 1 es neutro multiplicativo     | $a+0=a$<br>$a\cdot 1=a$                                    | $\exists!\, 0 \in \mathbb{R}: a+0=a$<br>$\wedge\ \exists!\, 1 \in \mathbb{R}: a\cdot 1=a$          |
|  6  | **Inverso aditivo**        | Todo real tiene un opuesto<br>que produce el neutro 0        | $a+(-a)=0$                                                 | $\forall\, a \in \mathbb{R},\ \exists\,{-a} \in \mathbb{R}:$<br>$a+(-a)=0$                         |
|  7  | **Inverso multiplicativo** | Todo real no nulo tiene un recíproco que produce el neutro 1 | $a \cdot a^{-1}=1,\quad a \neq 0$<br>$a^{-1}=\dfrac{1}{a}$ | $\forall\, a \in \mathbb{R}\setminus\{0\},\ \exists\, a^{-1} \in \mathbb{R}:$<br>$a\cdot a^{-1}=1$ |
**Los axiomas de cuerpo garantizan la consistencia aritmética y permiten la existencia unívoca de las operaciones de sustracción y división en** $\mathbb{R}$.

---
## Propiedades de igualdad
La igualdad es una relación fundamental en los números reales y permite establecer cuándo dos expresiones representan el mismo valor. Para operar correctamente con ella, se consideran las siguientes propiedades:

Sean $a, b, c \in \mathbb{R}$

| N   | **Axioma**        | **Descripción**                                                                                             | **Notación**  | **Concepto** |
| --- | ----------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------------ |
| 1   | **Reflexividad**  | Todo número es igual a sí mismo.                                                                            | a=a           | ∀a∈R:a=a     |
| 2   | **Simetría**      | Si un número es igual a otro, el segundo <br>es igual al primero.                                           | a=b⇒b=a       | a=b⟺b=a      |
| 3   | **Transitividad** | Si un número es igual a un segundo, y <br> este es igual a un tercero, el primero es <br> igual al tercero. | (a=b∧b=c)⇒a=c | a=b∧b=c⟹a=c  |

> **La igualdad es una relación de equivalencia que garantiza la unicidad de los elementos y la consistencia del cálculo en $\mathbb{R}$.**

### Principio de Sustitución

Si $a = b$, entonces $a$ puede ser reemplazado por $b$ en cualquier expresión o proposición matemática sin alterar su valor de verdad. Este principio es la base de la resolución de sistemas de ecuaciones y de la simplificación de expresiones según el texto de **Thomas**.

```desmos-graph
left=-5; right=5; bottom=-5; top=5;
width=400; height=200;
---
y=x^2-4|BLUE
y=0|DASHED|BLACK
(2,0)|label:x=2|BLACK
(-2,0)|label:x=-2|BLACK
y=(x-2)(x+2)|RED|DOTTED
```

_En el gráfico: La curva azul ($x^2-4$) interseca al eje negro en los puntos solución de la **ecuación** ($x=\pm 2$), mientras que la curva roja punteada coincide en cada punto con la azul, ilustrando la **identidad**._

> **La ecuación busca hallar incógnitas; la identidad establece una equivalencia estructural permanente.**

---
## Definiciones
La resta y la división no se definen como operaciones primarias o independientes, sino como **operaciones derivadas** de la adición y la multiplicación

| Operación               | Definición formal                                         | Notación              | Concepto                                                             |
| :---------------------- | :-------------------------------------------------------- | :-------------------- | :------------------------------------------------------------------- |
| **Resta** (Sustracción) | Es el número único $x$ tal que $a + x = b$.               | $b - a$               | Es la suma de $b$ con el **opuesto** de $a$: $b + (-a)$.             |
| **División**            | Es el número único $x$ tal que $ax = b$, para $a \neq 0$. | $b/a$ o $\frac{b}{a}$ | Es el producto de $b$ por el **recíproco** de $a$: $b \cdot a^{-1}$. |

### Conexión con los Axiomas

- **La resta** es posible porque el axioma de **existencia de negativos** asegura que para todo real $a$ existe un $-a$ tal que la suma es cero.
- **La división** es posible porque el axioma de **existencia del recíproco** asegura que para todo real $a \neq 0$ existe un $a^{-1}$ tal que el producto es uno.

Esto implica que "restar" es simplemente una forma abreviada de sumar un negativo, y "dividir" es una forma abreviada de multiplicar por un recíproco.

- **Resta** 
	$a-b=a+(-b)$
- **División**
	$\dfrac{a}{b}=a \cdot \dfrac{1}{b}=a \cdot b^{-1},\quad b \neq 0$

---

## Observaciones sobre tipos de igualdad en los números reales

En el análisis matemático, es crucial distinguir entre una igualdad que simplemente compara valores, una que impone una condición y una que expresa una equivalencia estructural.

Sean $a, b \in \mathbb{R}$ y $P(x), Q(x)$ expresiones algebraicas.

| Tipo                  | Ejemplo                | Descripción                            | Alcance                                       |
| :-------------------- | :--------------------- | -------------------------------------- | :-------------------------------------------- |
| **Igualdad numérica** | $2^3 = 8$              | Siempre verdadera                      | Siempre verdadera (o falsa).                  |
| **Ecuación**          | $x^2 - 4 = 0$          | Verdadera solo para algunos $x$        | Verdadera solo para su **conjunto solución**. |
| **Identidad**         | $x^2 - 4 = (x-2)(x+2)$ | Verdadera para todo $x \in \mathbb{R}$ | Verdadera para todo $x$ en el dominio.        |




---
## Teoremas básicos
Los **teoremas básicos de los números reales** no son reglas arbitrarias, sino consecuencias lógicas que se derivan de los axiomas de cuerpo, orden y completitud; Son "leyes establecidas" que garantizan que el álgebra y el cálculo funcionen siempre igual.

Sean $a, b, c, x \in \mathbb{R}$

### 1. Teoremas Algebraicos (Derivados de los Axiomas de Cuerpo)
Estos aseguran la consistencia de las operaciones básicas:



| **Teorema**                 |     |
| --------------------------- | --- |
| **Leyes de simplificación** |     |
|                             |     |


- **Leyes de simplificación:** Si $a + c = b + c$, entonces $a = b$. En la multiplicación, si $ac = bc$ y $c \neq 0$, entonces $a = b$.
- **Unicidad de elementos:** El elemento neutro ($0$ y $1$) y los elementos inversos (opuesto $-a$ y recíproco $1/a$) son únicos para cada número.
- **Regla del producto nulo:** El producto de cualquier número por cero es cero ($a \cdot 0 = 0$). Además, si $ab = 0$, entonces $a = 0$ o $b = 0$.
- **Leyes de los signos:** Por ejemplo, $(-a)(-b) = ab$ y $-(a-b) = b-a$.




1. $a+b=a+c \Rightarrow b=c$
2. $(a \cdot b=a \cdot c) \wedge a \neq 0 \Rightarrow b=c$
3. $a+x=b \Rightarrow x=b-a$
4. $(a \cdot x=b) \wedge a \neq 0 \Rightarrow x=\dfrac{b}{a}$
5. $a \cdot 0=0$
6. $a \cdot b=0 \Rightarrow (a=0 \vee b=0)$
7. $a=b \Rightarrow -a=-b$
8. $a(-b)=-(ab)$
9. $(-a)(-b)=ab$
10. $\dfrac{a}{b}+\dfrac{c}{b}=\dfrac{a+c}{b},\quad b \neq 0$

%%
galaxy-links

%%




---
# borrar

── MODO 1 · EXPLICACIÓN DE CONCEPTO ──

Los **teoremas básicos de los números reales** no son reglas arbitrarias, sino consecuencias lógicas que se derivan de los axiomas de cuerpo, orden y completitud. Mientras que los axiomas se aceptan sin demostración, los teoremas son "leyes establecidas" que garantizan que el álgebra y el cálculo funcionen siempre igual.

De acuerdo con el texto de **Apostol** y la teoría general, podemos agrupar estos teoremas en cuatro categorías fundamentales:

### 1. Teoremas Algebraicos (Derivados de los Axiomas de Cuerpo)

Estos aseguran la consistencia de las operaciones básicas:

- **Leyes de simplificación:** Si $a + c = b + c$, entonces $a = b$. En la multiplicación, si $ac = bc$ y $c \neq 0$, entonces $a = b$.
- **Unicidad de elementos:** El elemento neutro ($0$ y $1$) y los elementos inversos (opuesto $-a$ y recíproco $1/a$) son únicos para cada número.
- **Regla del producto nulo:** El producto de cualquier número por cero es cero ($a \cdot 0 = 0$). Además, si $ab = 0$, entonces $a = 0$ o $b = 0$.
- **Leyes de los signos:** Por ejemplo, $(-a)(-b) = ab$ y $-(a-b) = b-a$.

### 2. Teoremas de Desigualdad (Derivados de los Axiomas de Orden)

Establecen cómo se comporta la recta numérica:

- **Transitividad:** Si $a < b$ y $b < c$, entonces $a < c$.
- **Tricotomía:** Para cualquier par de números, solo puede ocurrir una de tres: $a < b$, $a > b$ o $a = b$.
- **Monotonía:** Sumar un número a ambos lados mantiene la desigualdad. Multiplicar por un **positivo** la mantiene, pero multiplicar por un **negativo** la invierte ($a < b \implies -a > -b$).
- **Cuadrados no negativos:** Para cualquier $a \neq 0$, se cumple que $a^2 > 0$.

### 3. Teoremas de Valor Absoluto

El valor absoluto $|x|$ mide la distancia al origen. Su teorema más famoso es:

- **Desigualdad Triangular:** $|x + y| \leq |x| + |y|$. La distancia de una suma no puede ser mayor que la suma de las distancias individuales.

### 4. Teoremas de Estructura y Continuidad

Son los que distinguen a los reales de otros sistemas como los racionales:

- **Propiedad Arquimediana:** Los números reales no tienen un "techo". Para cualquier número $x$, siempre existe un entero $n$ tal que $n > x$.
- **Densidad:** Entre dos números reales, por más cerca que estén, siempre existen infinitos números racionales e irracionales.
- **Axioma del Supremo:** Todo conjunto de números reales que esté acotado superiormente tiene un "extremo superior" o supremo dentro de los mismos reales.

```
left=-2; right=8; bottom=-1; top=2;
width=500; height=150;
---
y=0|BLACK
(1,0)|label:a|BLUE
(3,0)|label:b|BLUE
(6,0)|label:c|BLUE
{1<x<3: 0.2}|BLUE
{3<x<6: 0.2}|BLUE
{1<x<6: 0.5}|label:Si a < b y b < c entonces a < c|RED
```

_En el gráfico: La **transitividad** asegura que si el segmento (a,b) y el (b,c) existen, el camino directo (a,c) es coherente con el orden._

**Preguntas de comprensión:**

1. ¿Qué teorema básico de los reales justifica que podamos "cancelar" términos a ambos lados de una igualdad?
2. ¿Por qué el teorema de los cuadrados ($a^2 > 0$) impide que existan raíces cuadradas de números negativos dentro de los reales?
3. ¿Cómo usarías la **Propiedad Arquimediana** para demostrar que siempre podés encontrar un número de la forma $1/n$ tan pequeño como quieras?

[^1]: 
