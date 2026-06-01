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

| N   | **Propiedad**     | **Enunciado**                                                                                               | **Notación**                             |
| --- | ----------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| 1   | **Reflexividad**  | Todo número es igual a sí mismo.                                                                            | $a=a$                                    |
| 2   | **Simetría**      | Si $a=b$, entonces $b=a$.                                                                                   | $a=b \Longleftrightarrow b=a$            |
| 3   | **Transitividad** | Si $a=b$ y $b=c$, entonces $a=c$.                                                                           | $a=b \wedge b=c \Longrightarrow a=c$    |

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

- **La resta** es posible porque el axioma del **inverso aditivo** asegura que para todo $a$ existe $-a$. Restar es sumar el opuesto: $a+(-a)=0$.
- **La división** es posible porque el axioma del **inverso multiplicativo** asegura que para todo $a\neq 0$ existe $a^{-1}$. Dividir es multiplicar por el recíproco: $\dfrac{a}{b}=a\cdot b^{-1},\quad b\neq 0$.


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

Los **teoremas básicos de los números reales** no son reglas arbitrarias, sino consecuencias lógicas que se derivan de los axiomas de cuerpo, orden y completitud. Son "leyes establecidas" que garantizan que el álgebra y el cálculo funcionen siempre igual.

Sean $a, b, c \in \mathbb{R}$

---

### 1. Teoremas Algebraicos (Derivados de los Axiomas de Cuerpo)

Estos aseguran la consistencia de las operaciones básicas:

| **Teorema**                 | **Enunciado**                                                                                                                          | **Notación**                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Leyes de simplificación** | Si a dos igualdades se les suma o multiplica el mismo valor, los términos restantes son iguales.                                       | $a+c=b+c \Rightarrow a=b$<br>$ac=bc\ \wedge\ c\neq 0 \Rightarrow a=b$                          |
| **Unicidad de elementos**   | El neutro aditivo $0$, el neutro multiplicativo $1$, el opuesto $-a$ y el recíproco $\frac{1}{a}$ son únicos para cada número.         | $\exists!\,0: a+0=a$<br>$\exists!\,1: a\cdot 1=a$<br>$\exists!\,{-a}: a+(-a)=0$<br>$\exists!\,a^{-1}: a\cdot a^{-1}=1$ |
| **Regla del producto nulo** | El producto de cualquier número por cero es cero. Además, si un producto es cero, al menos uno de los factores debe serlo.             | $a\cdot 0=0$<br>$ab=0 \Rightarrow (a=0\ \vee\ b=0)$                                            |
| **Leyes de los signos**     | El producto de dos negativos es positivo. Negar una diferencia invierte el orden de los términos.                                      | $(-a)(-b)=ab$<br>$-(a-b)=b-a$                                                                  |

La **regla del producto nulo** es el fundamento de resolver ecuaciones por factorización: si se logra escribir una expresión como un producto igual a cero, cada factor puede igualarse a cero por separado.

---

### 2. Teoremas de Desigualdad (Derivados de los Axiomas de Orden)

Establecen cómo se comporta el orden en la recta numérica:

| **Teorema**                  | **Enunciado**                                                                                                                   | **Notación**                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Transitividad**            | Si $a<b$ y $b<c$, entonces $a<c$.                                                                                               | $a<b\ \wedge\ b<c \Rightarrow a<c$                                                                        |
| **Tricotomía**               | Entre dos reales, exactamente una de tres relaciones es verdadera: menor, mayor o igual.                                        | $a<b\ \vee\ a=b\ \vee\ a>b$                                                                               |
| **Monotonía**                | Sumar el mismo número a ambos lados conserva la desigualdad. Multiplicar por un positivo la conserva; por un negativo, la invierte. | $a<b \Rightarrow a+c<b+c$<br>$a<b\ \wedge\ c>0 \Rightarrow ac<bc$<br>$a<b \Rightarrow {-a}>-b$           |
| **Cuadrados no negativos**   | Para todo real no nulo, su cuadrado es estrictamente positivo.                                                                  | $a\neq 0 \Rightarrow a^2>0$                                                                               |

La **monotonía con negativos** explica por qué al multiplicar o dividir ambos lados de una desigualdad por un número negativo se debe invertir el signo.

---

### 3. Teoremas de Valor Absoluto

El valor absoluto $|x|$ mide la distancia del número $x$ al origen en la recta real:

| **Teorema**                | **Enunciado**                                                                              | **Notación**                      |
| -------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------- |
| **Desigualdad triangular** | La distancia de una suma no puede ser mayor que la suma de las distancias individuales.    | $|x+y| \leq |x|+|y|$             |

Su nombre viene de la geometría: en un triángulo, la longitud de un lado nunca supera la suma de los otros dos. Es el resultado más importante de esta sección y reaparece constantemente en cálculo y análisis.

---

### 4. Teoremas de Estructura y Continuidad

Son los que distinguen a $\mathbb{R}$ de otros sistemas como $\mathbb{Q}$:

| **Teorema**                  | **Enunciado**                                                                                                              | **Notación**                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Propiedad Arquimediana**   | Los reales no tienen "techo". Para cualquier $x$, siempre existe un entero $n$ mayor que él.                               | $\forall\,x\in\mathbb{R},\ \exists\,n\in\mathbb{Z}: n>x$            |
| **Densidad**                 | Entre dos reales distintos, por más cerca que estén, siempre existen infinitos racionales e irracionales.                  | $a<b \Rightarrow \exists\,r\in\mathbb{Q}: a<r<b$                    |
| **Axioma del Supremo**       | Todo conjunto de reales acotado superiormente tiene un extremo superior (supremo) dentro de $\mathbb{R}$.                  | $\exists\,\sup S \in \mathbb{R}$                                    |

El **Axioma del Supremo** es lo que hace que $\mathbb{R}$ no tenga "huecos". Los racionales $\mathbb{Q}$ no lo cumplen: el conjunto $\{x\in\mathbb{Q}: x^2<2\}$ no tiene supremo en $\mathbb{Q}$, lo que significa que $\sqrt{2}$ no existe dentro de los racionales.



Teoremas sobre numeros reales
1. $a+b=a+c \rightarrow b=c$
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


