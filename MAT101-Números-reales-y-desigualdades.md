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
|:---:| -------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
|  1  | **Clausura**               | Operar dos reales siempre<br>produce un real                 | $a+b \in \mathbb{R}$<br>$a \cdot b \in \mathbb{R}$         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b \in \mathbb{R}\ \wedge\ a \cdot b \in \mathbb{R}$          |
|  2  | **Conmutatividad**         | El orden de los operandos<br>no altera el resultado          | $a+b=b+a$<br>$a \cdot b=b \cdot a$                         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b=b+a\ \wedge\ a \cdot b=b \cdot a$                          |
|  3  | **Asociatividad**          | El agrupamiento no altera<br>el resultado                    | $(a+b)+c=a+(b+c)$<br>$(ab)\,c=a\,(bc)$                     | $\forall\, a,b,c \in \mathbb{R}:$<br>$(a+b)+c=a+(b+c)$<br>$\wedge\ (ab)c=a(bc)$                    |
|  4  | **Distributividad**        | La multiplicación se<br>distribuye sobre la suma             | $a(b+c)=ab+ac$                                             | $\forall\, a,b,c \in \mathbb{R}:$<br>$a(b+c)=ab+ac$                                                |
|  5  | **Elemento neutro**        | El 0 es neutro aditivo;<br>el 1 es neutro multiplicativo     | $a+0=a$<br>$a\cdot 1=a$                                    | $\exists!\, 0 \in \mathbb{R}: a+0=a$<br>$\wedge\ \exists!\, 1 \in \mathbb{R}: a\cdot 1=a$          |
|  6  | **Inverso aditivo**        | Todo real tiene un opuesto<br>que produce el neutro 0        | $a+(-a)=0$                                                 | $\forall\, a \in \mathbb{R},\ \exists\,{-a} \in \mathbb{R}:$<br>$a+(-a)=0$                         |
|  7  | **Inverso multiplicativo** | Todo real no nulo tiene un<br>recíproco que produce el neutro 1 | $a \cdot a^{-1}=1,\quad a \neq 0$<br>$a^{-1}=\dfrac{1}{a}$ | $\forall\, a \in \mathbb{R}\setminus\{0\},\ \exists\, a^{-1} \in \mathbb{R}:$<br>$a\cdot a^{-1}=1$ |

>**Los axiomas de cuerpo garantizan la consistencia aritmética y permiten la existencia unívoca de las operaciones de sustracción y división en** $\mathbb{R}$.

**Preguntas de comprensión:**
1. ¿Por qué es necesario especificar en los axiomas que el 0 y el 1 deben ser números distintos?
2. ¿Qué operación matemática quedaría invalidada si no existiera el axioma del recíproco para números distintos de cero?
3. ¿Cómo se relacionan estos axiomas con la posibilidad de definir la resta y la división en los números reales?

**Preguntas de comprensión:**
1. ¿Qué pasaría con la operación de división si quisiéramos incluir el número 0 en un "axioma de clausura para la división"?
2. ¿Por qué el conjunto de los números irracionales, por sí solo, no cumple con el axioma de clausura bajo la suma? (Pensá en $\sqrt{2}+(-\sqrt{2})$).
3. ¿Cómo ayuda la propiedad de clausura a que podamos definir funciones reales de variable real sin que los resultados sean valores "indefinidos"?

**Preguntas de comprensión:**
1. Si tomamos el conjunto de los números enteros, ¿se cumple la clausura bajo la operación de división?
2. ¿Qué sucede con la clausura en los números reales cuando intentamos calcular la raíz cuadrada de un número negativo?
3. ¿Por qué la clausura es necesaria para poder definir funciones de variable real sin que los resultados queden indefinidos?

**Preguntas de comprensión:**

1. ¿Por qué decimos que los números naturales **no** tienen clausura bajo la resta? (Pensá en 3−5).
2. Si el resultado de una operación fuera un número imaginario (como $\sqrt{-1}$​), ¿se habría cumplido el axioma de clausura en los números reales?
3. ¿Cómo ayuda la clausura a un ingeniero al programar un algoritmo de cálculo numérico?

**Preguntas de comprensión:**

1. ¿Por qué el conjunto de los números naturales **no** tiene clausura bajo la resta? (Pensá en el resultado de 2−5).
2. Si intentamos dividir un número real por 0, ¿por qué esto no se considera una falla de la "clausura", sino una operación no definida?
3. ¿Cómo ayuda la propiedad de clausura a un ingeniero al momento de asegurar que un sistema de ecuaciones reales tendrá soluciones dentro del mismo campo?

---
## Propiedades de igualdad
La igualdad es una relación fundamental en los números reales y permite establecer cuándo dos expresiones representan el mismo valor. Para operar correctamente con ella, se consideran las siguientes propiedades:

Sean $a, b, c \in \mathbb{R}$

| N   | **Propiedad**     | **Enunciado**                                     | **Notación**                          |
| --- | ----------------- | ------------------------------------------------- | ------------------------------------- |
| 1   | **Reflexividad**  | Todo número es igual a sí mismo.                  | $a=a$                                 |
| 2   | **Simetría**      | Si $a=b$, entonces $b=a$.                         | $a=b \Longleftrightarrow b=a$         |
| 3   | **Transitividad** | Si $a=b$ y $b=c$, entonces $a=c$.                 | $a=b \wedge b=c \Longrightarrow a=c$  |

> **La igualdad es una relación de equivalencia que garantiza la unicidad de los elementos y la consistencia del cálculo en $\mathbb{R}$.**

### Principio de Sustitución

Si $a = b$, entonces $a$ puede ser reemplazado por $b$ en cualquier expresión o proposición matemática sin alterar su valor de verdad. 
**Ejemplos**

Si $a=3$, entonces $2a+5=2(3)+5=11$.
Si $x+y=10$ , entonces $(x+y)^2=10^2=100$.

Esta propiedad permite manipular ecuaciones, simplificar expresiones y evaluar funciones de forma consistente.

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

**Preguntas de comprensión:**

1. ¿Por qué es fundamental la propiedad transitiva para poder resolver una cadena de igualdades en un problema de ingeniería?
2. Si definimos una relación que no es simétrica (como "es mayor que"), ¿por qué no podemos considerarla una forma de igualdad?
3. ¿Cómo se relaciona el hecho de que la suma esté "unívocamente determinada" con la posibilidad de sumar lo mismo a ambos lados de una ecuación?

**Preguntas de comprensión:**

1. ¿Por qué es necesario que una función esté "unívocamente determinada" para que el Principio de Sustitución funcione correctamente?
2. En una identidad como $(x+1)^{2}=x{2}+2x+1$, ¿qué sucede si sustituimos $x$ por cualquier número real?
3. Al resolver un sistema de ecuaciones por el método de sustitución, ¿qué propiedad de la igualdad estamos explotando realmente?

---
## Definiciones
La resta y la división no se definen como operaciones primarias o independientes, sino como **operaciones derivadas** de la adición y la multiplicación.

| Operación               | Definición formal                                         | Notación              | Concepto                                                              |
| :---------------------- | :-------------------------------------------------------- | :-------------------- | :-------------------------------------------------------------------- |
| **Resta** (Sustracción) | Es el número único $x$ tal que $a + x = b$.               | $b - a$               | Es la suma de $b$ con el **opuesto** de $a$: $b + (-a)$.              |
| **División**            | Es el número único $x$ tal que $ax = b$, para $a \neq 0$. | $b/a$ o $\frac{b}{a}$ | Es el producto de $b$ por el **recíproco** de $a$: $b \cdot a^{-1}$. |

### Conexión con los Axiomas

- **La resta** es posible porque el axioma del **inverso aditivo** asegura que para todo $a$ existe $-a$. Restar es sumar el opuesto: $a-b=a+(-b)$.
- **La división** es posible porque el axioma del **inverso multiplicativo** asegura que para todo $a\neq 0$ existe $a^{-1}$. Dividir es multiplicar por el recíproco: $\dfrac{a}{b}=a\cdot b^{-1},\quad b\neq 0$.

**Preguntas de comprensión:**

1. ¿Por qué el número $0$ no puede ser el divisor $(a)$ en la definición de división de los números reales?
2. Según la definición de resta de Apostol, ¿cómo se demuestra que $0−a$ es igual a $−a$?
3. Si la resta se define a través de la suma, ¿qué propiedad de la igualdad garantiza que el resultado x sea único?

---

## Observaciones sobre tipos de igualdad en los números reales

En el análisis matemático, es crucial distinguir entre una igualdad que simplemente compara valores, una que impone una condición y una que expresa una equivalencia estructural.

Sean $a, b \in \mathbb{R}$ y $P(x), Q(x)$ expresiones algebraicas.

| Tipo                  | Ejemplo                 | Descripción                            | Alcance                                       |
| :-------------------- | :---------------------- | -------------------------------------- | :-------------------------------------------- |
| **Igualdad numérica** | $2^3 = 8$               | Siempre verdadera                      | Siempre verdadera (o falsa).                  |
| **Ecuación**          | $x^2 - 4 = 0$           | Verdadera solo para algunos $x$        | Verdadera solo para su **conjunto solución**. |
| **Identidad**         | $x^2 - 4 = (x-2)(x+2)$ | Verdadera para todo $x \in \mathbb{R}$ | Verdadera para todo $x$ en el dominio.        |

---
## Teoremas básicos

Los **teoremas básicos de los números reales** no son reglas arbitrarias, sino consecuencias lógicas que se derivan de los axiomas de cuerpo, orden y completitud. Son "leyes establecidas" que garantizan que el álgebra y el cálculo funcionen siempre igual.

Sean $a, b, c \in \mathbb{R}$

---

### 1. Teoremas Algebraicos (Derivados de los Axiomas de Cuerpo)

Estos aseguran la consistencia de las operaciones básicas:

| **Teorema**                 | **Enunciado**                                                                                                      | **Notación**                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Leyes de simplificación** | Si a dos igualdades se les suma o multiplica el mismo valor, los términos restantes son iguales.                   | $a+c=b+c \Rightarrow a=b$<br>$ac=bc\ \wedge\ c\neq 0 \Rightarrow a=b$                                                  |
| **Unicidad de elementos**   | El neutro $0$, el neutro $1$, el opuesto $-a$ y el recíproco $a^{-1}$ son únicos para cada número.                 | $\exists!\,0: a+0=a$<br>$\exists!\,1: a\cdot 1=a$<br>$\exists!\,{-a}: a+(-a)=0$<br>$\exists!\,a^{-1}: a\cdot a^{-1}=1$ |
| **Regla del producto nulo** | El producto de cualquier número por cero es cero. Si un producto es cero, al menos uno de los factores debe serlo. | $a\cdot 0=0$<br>$ab=0 \Rightarrow (a=0\ \vee\ b=0)$                                                                    |
| **Leyes de los signos**     | El producto de dos negativos es positivo. Negar una diferencia invierte el orden de los términos.                  | $(-a)(-b)=ab$<br>$a(-b)=-(ab)$<br>$-(-a)=a$<br>$-(a-b)=b-a$                                                            |
>La **regla del producto nulo** es el fundamento de resolver ecuaciones por factorización: si se logra escribir una expresión como un producto igual a cero, cada factor puede igualarse a cero por separado.

---

### 2. Teoremas de Desigualdad (Derivados de los Axiomas de Orden)

Establecen cómo se comporta el orden en la recta numérica:

| **Teorema**                | **Enunciado**                                                                                                                       | **Notación**                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Transitividad**          | Si $a<b$ y $b<c$, entonces $a<c$.                                                                                                   | $a<b\ \wedge\ b<c \Rightarrow a<c$                                                             |
| **Tricotomía**             | Entre dos reales, exactamente una de tres relaciones es verdadera: menor, mayor o igual.                                            | $a<b\ \vee\ a=b\ \vee\ a>b$                                                                    |
| **Monotonía**              | Sumar el mismo número a ambos lados conserva la desigualdad. Multiplicar por un positivo la conserva; por un negativo, la invierte. | $a<b \Rightarrow a+c<b+c$<br>$a<b\ \wedge\ c>0 \Rightarrow ac<bc$<br>$a<b \Rightarrow {-a}>-b$ |
| **Cuadrados no negativos** | Para todo real no nulo, su cuadrado es estrictamente positivo.                                                                      | $a\neq 0 \Rightarrow a^2>0$                                                                    |
>La **monotonía con negativos** explica por qué al multiplicar o dividir ambos lados de una desigualdad por un número negativo se debe invertir el signo.

---

### 3. Teoremas de Valor Absoluto

El valor absoluto $|x|$ mide la distancia del número $x$ al origen en la recta real:

| **Teorema**                | **Enunciado**                                                                           | **Notación**                 |
| -------------------------- | --------------------------------------------------------------------------------------- | ---------------------------- |
| **Desigualdad triangular** | La distancia de una suma no puede ser mayor que la suma de las distancias individuales. | $\|x+y\| \leq \|x\| + \|y\|$ |
>Su nombre viene de la geometría: en un triángulo, la longitud de un lado nunca supera la suma de los otros dos. Es el resultado más importante de esta sección y reaparece constantemente en cálculo y análisis.

---

### 4. Teoremas de Estructura y Continuidad

Son los que distinguen a $\mathbb{R}$ de otros sistemas como $\mathbb{Q}$:

| **Teorema**                | **Enunciado**                                                                                                          | **Notación**                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Propiedad Arquimediana** | Los reales no tienen "techo". Para cualquier $x$, siempre existe un entero $n$ mayor que él.                           | $\forall\,x\in\mathbb{R},\ \exists\,n\in\mathbb{Z}: n>x$ |
| **Densidad**               | Entre dos reales distintos, por más cerca que estén, siempre existen infinitos racionales e irracionales.              | $a<b \Rightarrow \exists\,r\in\mathbb{Q}: a<r<b$          |
| **Axioma del Supremo**     | Todo conjunto de reales acotado superiormente tiene un extremo superior (supremo) dentro de $\mathbb{R}$.              | $\exists\,\sup S \in \mathbb{R}$                          |

>El **Axioma del Supremo** es lo que hace que $\mathbb{R}$ no tenga "huecos". Los racionales $\mathbb{Q}$ no lo cumplen: el conjunto $\{x\in\mathbb{Q}: x^2<2\}$ no tiene supremo en $\mathbb{Q}$, lo que significa que $\sqrt{2}$ no existe dentro de los racionales.

---

### Resumen de Teoremas Útiles

Tabla de referencia rápida con los teoremas más operativos: los que aparecen al resolver ejercicios, simplificar expresiones y trabajar con fracciones. Sean $a, b, c, d \in \mathbb{R}$.

| **#** | **Nombre**                        | **Notación**                                                   |
|:-----:| --------------------------------- | -------------------------------------------------------------- |
|   1   | Cancelación aditiva               | $a+c=b+c \Rightarrow a=b$                                      |
|   2   | Cancelación multiplicativa        | $ac=bc\ \wedge\ c\neq 0 \Rightarrow a=b$                       |
|   3   | Solución única aditiva            | $a+x=b \Rightarrow x=b-a$                                      |
|   4   | Solución única multiplicativa     | $ax=b\ \wedge\ a\neq 0 \Rightarrow x=\dfrac{b}{a}$             |
|   5   | Producto por cero                 | $a\cdot 0=0$                                                   |
|   6   | Regla del producto nulo           | $ab=0 \Rightarrow (a=0\ \vee\ b=0)$                            |
|   7   | Igualdad de opuestos              | $a=b \Rightarrow -a=-b$                                        |
|   8   | Signo en el producto              | $a(-b)=-(ab)$                                                  |
|   9   | Doble negativo                    | $(-a)(-b)=ab$                                                  |
|  10   | Fracciones — igual denominador    | $\dfrac{a}{b}+\dfrac{c}{b}=\dfrac{a+c}{b},\quad b\neq 0$       |
|  11   | Fracciones — distinto denominador | $\dfrac{a}{b}+\dfrac{c}{d}=\dfrac{ad+cb}{bd},\quad b,d\neq 0$  |
|  12   | Producto de fracciones            | $\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd},\quad b,d\neq 0$ |
|  13   | División de fracciones            | $\dfrac{a/b}{c/d}=\dfrac{ad}{cb},\quad b,c,d\neq 0$            |


**Preguntas de comprensión:**

1. ¿Qué teorema básico de los reales justifica que podamos "cancelar" términos a ambos lados de una igualdad?
2. ¿Por qué el teorema de los cuadrados $(a^{2} > 0)$ impide que existan raíces cuadradas de números negativos dentro de los reales?
3. ¿Cómo usarías la **Propiedad Arquimediana** para demostrar que siempre podés encontrar un número de la forma $1/n$ tan pequeño como quieras?

---

## Axiomas de Orden de los números reales

Son las reglas que nos permiten comparar dos números reales y establecer una jerarquía entre ellos. Gracias a estos axiomas, podemos afirmar que los números reales se disponen en una **recta numérica** con una dirección definida.

Formalmente, el sistema de los números reales se basa en la existencia de un subconjunto especial llamado **números positivos** ($\mathbb{R}^+$). A partir de este concepto primitivo, se construyen las relaciones "mayor que" ($>$) y "menor que" ($<$).

Sean $a, b \in \mathbb{R}$

|  N  | Axioma                      | Descripción                                                       | Notación                                                                       | Concepto (Símbolos)                                                                  |
|:---:|:--------------------------- |:----------------------------------------------------------------- |:------------------------------------------------------------------------------ |:------------------------------------------------------------------------------------ |
|  1  | **Clausura de la suma**     | La suma de dos positivos es positiva.                             | $a, b \in \mathbb{R}^+ \Rightarrow a+b \in \mathbb{R}^+$                       | $\forall a,b \in \mathbb{R}^+ : (a+b) \in \mathbb{R}^+$                              |
|  2  | **Clausura del producto**   | El producto de dos positivos es positivo.                         | $a, b \in \mathbb{R}^+ \Rightarrow ab \in \mathbb{R}^+$                        | $\forall a,b \in \mathbb{R}^+ : (ab) \in \mathbb{R}^+$                               |
|  3  | **Tricotomía de positivos** | Para cualquier real no nulo, o él es positivo o su opuesto lo es. | $a \neq 0 \Rightarrow a \in \mathbb{R}^+ \underline{\vee} -a \in \mathbb{R}^+$ | $\forall a \in \mathbb{R}, a \neq 0 : a \in \mathbb{R}^+ \oplus -a \in \mathbb{R}^+$ |
|  4  | **Exclusión del cero**      | El cero no es un número positivo.                                 | $0 \notin \mathbb{R}^+$                                                        | $0 \notin \mathbb{R}^+$                                                              |

### Definición de la relación de orden

Una vez aceptados estos axiomas, definimos formalmente los símbolos de desigualdad:

- **Menor que:** $a < b \iff b - a \in \mathbb{R}^+$
- **Mayor que:** $a > b \iff a - b \in \mathbb{R}^+$

### Propiedades fundamentales derivadas

De los axiomas anteriores se derivan los teoremas que usamos habitualmente en ingeniería:

1. **Transitividad:** Si $a < b$ y $b < c$, entonces $a < c$.
2. **Monotonía de la suma:** Si $a < b$, entonces $a + c < b + c$.
3. **Monotonía del producto:** Si $a < b$ y $c > 0$, entonces $ac < bc$. (Si $c < 0$, la desigualdad se invierte: $ac > bc$).

> **Los axiomas de orden convierten a $\mathbb{R}$ en un campo ordenado, permitiendo el uso de desigualdades y la representación en la recta real.**

**Preguntas de comprensión:**

1. ¿Por qué el axioma de tricotomía impide que un número sea positivo y negativo al mismo tiempo?
2. Si multiplicamos la desigualdad $x<5$ por $−2$, ¿cuál es el fundamento axiomático para invertir el símbolo?
3. ¿Cómo usarías la definición formal $(b−a \in \mathbb{R}^{+})$ para demostrar que si $a<b$, entonces $−b<−a$?

---

## Teoremas de desigualdades e inecuaciones

En el sistema de los números reales, las desigualdades no son solo comparaciones, sino que forman una estructura matemática regida por los **axiomas de orden**. A partir de estos axiomas se derivan los teoremas que permiten resolver inecuaciones y realizar estimaciones en cálculo.

Podemos agrupar estos teoremas en tres categorías fundamentales, si $a,b,c,x \in \mathbb{R}$:

### 1. Teoremas de Orden (Reglas Operativas)

Los teoremas de orden son consecuencias lógicas de los axiomas de orden de los números reales. Estas reglas permiten manipular desigualdades de forma segura en el álgebra y el cálculo, asegurando que las comparaciones de magnitud entre números sigan siendo válidas tras realizar operaciones.

Sean $a, b, c, x \in \mathbb{R}$:

|  N  | Teorema o propiedad          | Descripción                                                                                | Notación                                          | Concepto (Símbolos)                                           |
| :-: | :--------------------------- | :----------------------------------------------------------------------------------------- | :------------------------------------------------ | :------------------------------------------------------------ |
|  1  | **Propiedad de Tricotomía**  | Para cualquier par de reales, solo una de<br>tres relaciones es posible.                   | $a < b \lor a = b \lor a > b$                     | $\forall a,b \in \mathbb{R}: (a<b) \oplus (a=b) \oplus (b<a)$ |
|  2  | **Propiedad Transitiva**     | Si un número es menor a un segundo y este<br>a un tercero, el primero es menor al tercero. | $a < b \land b < c \Rightarrow a < c$             | $a < b \land b < c \implies a < c$                            |
|  3  | **Monotonía de la Suma**     | Sumar o restar el mismo número a ambos<br>lados mantiene la desigualdad.                   | $a < b \Rightarrow a + c < b + c$                 | $a < b \implies a + c < b + c$                                |
|  4  | **Producto por Positivo**    | Multiplicar por un número mayor a cero<br>mantiene el sentido de la desigualdad.           | $a < b \land c > 0 \Rightarrow ac < bc$           | $a < b \land c > 0 \implies ac < bc$                          |
|  5  | **Producto por Negativo**    | Multiplicar por un número menor a cero<br>**invierte** el sentido de la desigualdad.       | $a < b \land c < 0 \Rightarrow ac > bc$           | $a < b \land c < 0 \implies ac > bc$                          |
|  6  | **Teorema de Cuadrados**     | El cuadrado de cualquier número real no<br>nulo es siempre positivo.                       | $a \neq 0 \Rightarrow a^2 > 0$                    | $\forall a \in \mathbb{R}, a \neq 0 : a^2 > 0$                |
|  7  | **Inversos Multiplicativos** | Si dos números tienen el mismo signo, sus<br>recíprocos invierten el orden.                | $0 < a < b \Rightarrow \frac{1}{b} < \frac{1}{a}$ | $0 < a < b \implies a^{-1} > b^{-1}$                          |
  
```desmos-graph
left=-3; right=3; bottom=-1; top=3;
width=350; height=150;
---
y=x^2|#2d70b3
y=0|#000000
(0,0)|label:El cuadrado siempre es >= 0|#000000
a=1.5
b=2.5
c=-1
(a,a^2)|#c74440
(b,b^2)|#c74440
\{a<x<b: 0\}|#fa7e19
\{c*b<x<c*a: 0\}|#388c46
(a,0)|label:a|#000000
(b,0)|label:b|#000000
(c*a,0)|label:ca|#388c46
(c*b,0)|label:cb|#388c46
```

_En el gráfico: La curva azul ($y=x^2$) ilustra que cualquier número real elevado al cuadrado resulta en un valor no negativo. En el eje $x$, se observa cómo si $a < b$, al multiplicar por $c = -1$, las posiciones se invierten resultando en $cb < ca$._

> **Los teoremas de orden permiten la resolución de inecuaciones y fundamentan la noción de distancia en la recta real.**

**Preguntas de comprensión:**

1. ¿Por qué el teorema del producto por negativo es crucial al resolver una inecuación como $−2x<10$?
2. ¿Cómo garantiza la propiedad transitiva que podamos organizar a todos los números reales en una sola línea recta?
3. Si sabemos que $x^{2}>0$ para todo $x\neq 0$, ¿qué podemos concluir sobre la existencia de raíces reales para números negativos?



### 2. Teoremas de Valor Absoluto

El valor absoluto $|x|$ mide la distancia al origen y es vital para definir límites y continuidad.

- **Propiedad Fundamental:** $|x| \leq a$ es equivalente a $-a \leq x \leq a$ (siempre que $a \geq 0$).
- **Desigualdad Triangular:** El valor absoluto de una suma no supera la suma de los valores absolutos: $|a + b| \leq |a| + |b|$
- **Variante de la Resta:** $|a - b| \geq | ( |a| - |b| ) |$.

A partir de su definición, se derivan teoremas fundamentales que permiten resolver ecuaciones e inecuaciones con módulos y establecer acotaciones en el cálculo.

Sean $a, b, c, x \in \mathbb{R}$:

|  N  | Teorema o propiedad         | Descripción                                                                                | Notación                                               | Concepto (Símbolos)                                                                                 |
|:---:|:--------------------------- |:------------------------------------------------------------------------------------------ |:------------------------------------------------------ |:--------------------------------------------------------------------------------------------------- |
|  1  | **No negatividad**          | El valor absoluto de cualquier real es siempre cero o positivo.                            | $\|x\| \geq 0$                                         | $\forall \|x\| \in \mathbb{R} : x \geq 0$                                                           |
|  2  | **Propiedad del producto**  | El módulo de un producto es el producto de los módulos de los factores.                    | $\|ab\| = \|a\| \cdot \|b\|$                           | $\forall a,b \in \mathbb{R} : \|ab\| = \|a\| \cdot \|b\|$                                           |
|  3  | **Propiedad del cociente**  | El módulo de una división es el cociente de los módulos (si el divisor no es nulo).        | $\dfrac{\|a\|}{\|b\|} = \bigg \| \dfrac{a}{b}\bigg \|$ | $\forall a \in \mathbb{R}, \forall b \neq 0 : \dfrac{\|a\|}{\|b\|} = \bigg \| \dfrac{a}{b}\bigg \|$ |
|  4  | **Relación con la raíz**    | La raíz cuadrada del cuadrado de un número es igual a su valor absoluto.                   | $\sqrt{x^{2}} =\|x\|$                                  | $\forall x \in \mathbb{R} : \sqrt{x^2} = \|x\|$                                                     |
|  5  | **Propiedad de Intervalos** | Estar acotado por un módulo equivale a estar contenido en un intervalo simétrico.          | $x \leq \|a\| \iff -a \leq x \leq a$                   | $a \geq 0 \land x \leq a \iff x \in [-a, a]$                                                        |
|  6  | **Desigualdad Triangular**  | El módulo de una suma no supera la suma de los módulos individuales.                       | $\|a + b\| \leq \|a\| + \|b\|$                         | $\forall a,b \in \mathbb{R} : \|a + b\| \leq \|a\| + \|b\|$                                         |
|  7  | **Variante de la resta**    | La diferencia de módulos es menor o igual al módulo de la diferencia.                      | $\|a - b\| \geq \|a\| - \|b\|$                         | $\forall a,b \in \mathbb{R} : \|a - b\| \geq \|a\| - \|b\|$                                         |
|  8  | **Intervalo Abierto**       | Estar acotado superiormente por un módulo define un intervalo simétrico entre $-a$ y $a$.  | $\vert x \vert < a$ $\iff -a < x < a$                    | $a > 0 \implies x \in (-a, a)$                                                                      |
|  9  | **Intervalos Exteriores**   | Superar un módulo implica que el número está fuera de la zona central, hacia los extremos. | $\vert x \vert > a$ $\iff x > a \lor x < -a$             | $a > 0 \implies x \in (-\infty, -a) \cup (a, \infty)$                                               |

- Cuando decimos $\vert x \vert < a$, estamos buscando todos los números cuya distancia al centro es "corta", lo que genera un **intervalo acotado** (un entorno).
- Cuando decimos $\vert x \vert > a$, buscamos números que están "lejos" del origen, lo que genera dos **semirrectas infinitas**.

----
---
---

── MODO 1 · EXPLICACIÓN DE CONCEPTO ──

En el sistema de los números reales, tanto la **Desigualdad de Cauchy-Schwarz** como las propiedades de los intervalos con valor absoluto son herramientas analíticas fundamentales. La primera permite relacionar productos y sumas (o vectores y normas), mientras que las segundas definen la noción de cercanía o distancia en la recta real.

### 1. Desigualdad de Cauchy-Schwarz

Esta desigualdad establece que el valor absoluto del producto de dos conjuntos de números (o el producto escalar de dos vectores) nunca supera al producto de sus magnitudes individuales. Es la base para demostrar la desigualdad triangular y para definir el ángulo entre vectores.

### 2. Valor Absoluto e Intervalos

El valor absoluto $\vert x \vert$ representa la **distancia** de un número al origen.

- Cuando decimos $\vert x \vert < a$, estamos buscando todos los números cuya distancia al centro es "corta", lo que genera un **intervalo acotado** (un entorno).
- Cuando decimos $\vert x \vert > a$, buscamos números que están "lejos" del origen, lo que genera dos **semirrectas infinitas**.

A continuación, presento la tabla con la formalización solicitada:

| N | Teorema o Propiedad | Descripción | Notación | Concepto (Símbolos) |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Cauchy-Schwarz** | El cuadrado de una suma de productos es menor o igual al producto de las sumas de los cuadrados. | $(\sum a_k b_k)^2 \leq (\sum a_k^2)(\sum b_k^2)$ | $\forall A, B \in V_n : \vert A \cdot B \vert \leq \Vert A \Vert \Vert B \Vert$ |
| 2 | **Intervalo Abierto** | Estar acotado superiormente por un módulo define un intervalo simétrico entre $-a$ y $a$. | $\vert x \vert < a \iff -a < x < a$ | $a > 0 \implies x \in (-a, a)$ |
| 3 | **Intervalos Exteriores** | Superar un módulo implica que el número está fuera de la zona central, hacia los extremos. | $\vert x \vert > a \iff x > a \lor x < -a$ | $a > 0 \implies x \in (-\infty, -a) \cup (a, \infty)$ |

```desmos-graph
left=-8; right=8; bottom=-1; top=7;
width=500; height=300;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=3|#000000|DASHED
-3<x<3|y<=3|y>=0|#a5d8ff
x<-3|y<=5|y>=0|#ff7b7b
x>3|y<=5|y>=0|#ff7b7b
(0,4)|label:abs(x) > a (Rojo)|#c74440
(0,1.5)|label:abs(x) < a (Azul)|#2d70b3
```

_En el gráfico: La zona azul  representa la propiedad $\vert x \vert < 3$, donde los valores están "atrapados" cerca del centro. Las zonas rojas representan $\vert x \vert > 3$, donde los valores escapan hacia el infinito._





```desmos-graph
left=-8; right=8; bottom=-2; top=2;
width=700; height=180;
---

a=3

y=0
y=1

(-a,0)|label:-a
(a,0)|label:a

(-a,1)|label:-a
(a,1)|label:a

y=0 {-a<x<a}

y=1 {x<-a}
y=1 {x>a}
```


---
---
---

















```desmos-graph
left=-4; right=4; bottom=-1; top=4;
width=350; height=150;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3


y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,2)|label:(-a, a)|#c74440
(2,2)|label:(a, a)|#c74440
```


_En el gráfico: La función azul $|x|$ muestra cómo los valores negativos se reflejan al semieje positivo. La región sombreada ilustra el **Teorema 5**, donde $|x| \leq 2$ define el intervalo entre $-2$ y $2$._

> **El valor absoluto define la métrica (distancia) en $\mathbb{R}$ y es la herramienta base para el concepto de límite mediante entornos.**

**Preguntas de comprensión:**

1. ¿Por qué el Teorema 4 ($\sqrt{x^2} = |x|$) es una identidad y no simplemente $\sqrt{x^2} = x$?
2. En la Desigualdad Triangular (Teorema 6), ¿en qué caso específico se cumple la igualdad exacta ($|a+b| = |a|+|b|$)?
3. Si aplicamos el Teorema 5 a una inecuación del tipo $|x| > a$, ¿cómo se traduce esto a intervalos en la recta real?

**Preguntas de comprensión:**

1. En la desigualdad de Cauchy-Schwarz, ¿qué debe ocurrir entre los vectores (o secuencias de números) para que se cumpla la igualdad exacta?
2. ¿Por qué si $a < 0$, la propiedad $\vert x \vert < a$ no tiene ninguna solución en el conjunto de los números reales?
3. Si cambiamos $\vert x \vert < a$ por $\vert x - c \vert < \delta$, ¿cómo se desplaza el centro del intervalo en la recta numérica?

### 3. Desigualdades "Notables"


---
bb



## Desigualdades "Notables"

Las desigualdades notables son herramientas analíticas avanzadas que permiten establecer cotas y límites superiores en diversas ramas del cálculo y el análisis vectorial. A diferencia de las reglas de orden básicas, estas propiedades relacionan potencias, raíces y productos de formas no triviales.

Sean $a, b, c, x \in \mathbb{R}$:


|  N  | Teorema o propiedad                | Descripción                                                                                  | Notación                                         | Concepto (Símbolos)                                                        |
| :-: | ---------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------- |
|  1  | **Cuadrados no negativos**         | El cuadrado de cualquier número real nunca es negativo.                                      | $a^2 \geq 0$                                     | $\forall a \in \mathbb{R}: a^2 \geq 0$                                     |
|  2  | **Desigualdad de Bernoulli**       | Establece una cota inferior lineal para una potencia con base mayor a $-1$.                  | $(1+x)^n \geq 1+nx$                              | $x>-1,\; n\in\mathbb{Z}^{+}$ $\implies (1+x)^n \geq 1+nx$                    |
|  3  | **Medias Aritmética y Geométrica** | La media geométrica de números no negativos nunca excede a su media aritmética.              | $\sqrt{ab} \leq \dfrac{a+b}{2}$                  | $a,b\geq0$ $\implies \sqrt{ab}\leq\frac{a+b}{2}$                             |
|  4  | **Cauchy-Schwarz**                 | El cuadrado del producto escalar de dos vectores es menor o igual al producto de sus normas. | $(\sum a_k b_k)^2 \leq (\sum a_k^2)(\sum b_k^2)$ | $\forall A,B\in V_n:\ \vert A\cdot B\vert \leq \vert A\vert\,\vert B\vert$ |
|  5  | **Desigualdad Triangular**         | La distancia de una suma no puede superar la suma de las distancias individuales.            | $\vert a+b\vert \leq \vert a\vert+\vert b\vert$  | $\forall a,b\in\mathbb{R}:\ \vert a+b\vert \leq \vert a\vert+\vert b\vert$ |


```desmos-graph
left=-2; right=5; bottom=-1; top=4;
width=500; height=300;
---
y=\sqrt{x}|x>=0|#2d70b3
y=(x+1)/2|#c74440
y<=(x+1)/2|y>=\sqrt{x}|x>=0|#b2f2bb
(1,1)|label:Igualdad si a=b|#000000
```
_En el gráfico: Se visualiza la **Desigualdad de las Medias (N°3)** tomando $b=1$. La recta roja ($\frac{x+1}{2}$) siempre está por encima o toca a la curva azul ($\sqrt{x}$), demostrando que la media aritmética es siempre superior o igual a la geométrica._


```desmos-graph
left=-2; right=6; bottom=-1; top=4;
width=500; height=300;
---
y=x|#2d70b3
y=x^2|#c74440
y=x^2|y<=x|x>=0|x<=1|#b2f2bb
(1,1)|label:x=1|#000000
```

_En el gráfico: Se observa que en el intervalo $(0,1)$, la inecuación $x^2 < x$ es verdadera (área verde), pero para $x > 1$ la relación se invierte ($x^2 > x$), ilustrando cómo cambian las desigualdades según el dominio._

> **Estas desigualdades son el pilar fundamental para las demostraciones de convergencia y la definición formal de normas en espacios vectoriales.**

**Preguntas de comprensión:**

1. ¿Cuál es el fundamento axiomático que justifica cambiar el sentido de una inecuación al multiplicar por $-1$?.
2. Según la desigualdad de Bernoulli, si $x=0.1$ y $n=2$, ¿qué relación numérica se establece?.
3. ¿Por qué la propiedad de transitividad es indispensable para representar los números reales en una recta numérica?.

**Preguntas de comprensión:**

1. ¿Bajo qué condición específica la Desigualdad de las Medias deja de ser una desigualdad y se convierte en una igualdad exacta?
2. ¿Por qué la Desigualdad de Bernoulli (N°2) requiere que $x$ sea estrictamente mayor a -1 para ser válida?
3. ¿Cómo podrías usar el Teorema de los Cuadrados (N°1) para demostrar que la expresión $a^2 + b^2 \geq 2ab$ es siempre cierta?










%%
galaxy-links
%%
