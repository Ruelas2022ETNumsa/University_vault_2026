- Introducción
- Estados y probabilidades de estado
- Matriz de probabilidades de transición
- Predicción de la participación futura en el mercado
- Análisis de Markov en la operación de maquinaria
- Condiciones de equilibrio
- Estados absorbentes y la matriz fundamental: Aplicación a cuentas por cobrar.

---

# **INTRODUCCIÓN**

##### **ANALISIS DE MARKOV**

Es una técnica que maneja las probabilidades de ocurrencias futuras mediante el análisis de las probabilidad conocidas en el presente._Hay cuatro suposiciones en el análisis de Markov._

1. Existe un número limitado o finito de estados posibles.
2. La probabilidad de cambiar de estados permanece igual con el paso del tiempo.
3. Podemos predecir cualquier estado futuro a partir de los estados anteriores y de la matriz de probabilidades de transición.
4. El tamaño y la composición del sistema (es decir, el número total de fabricantes y clientes) no cambia durante el análisis. 

---

## **ESTADOS Y PROBABILIDADES DE LOS ESTADOS**

**Los estados sirven para identificar todas las condiciones posibles de un proceso o sistema.**

_Por ejemplo,_ Si hay solamente tres tiendas de abarrotes en un pueblo pequeño, un residente puede ser cliente de cualquiera de las tres tiendas en cierto momento. Por lo tanto, hay tres estados correspondientes a las tres tiendas.

 **Dos suposiciones adicionales del análisis de Markov son que los estados son colectivamente exhaustivos y mutuamente excluyentes.**

### **COLECTIVAMENTE EXHAUSTIVOS**

Significa que podemos numerar todos los estados posibles de un sistema o proceso.

POR EJEMPLO: Nuestro estudio del análisis de Markov supone que hay un número finito de estados para cualquier sistema. 
### **MUTUAMENTE EXCLUYENTES**

Significa que un sistema puede estar tan solo en un estado en cualquier momento.

POR EJEMPLO: significa que una persona únicamente puede ser cliente de _una de las tres tiendas de_ abarrotes en un punto en el tiempo.

---

Después de identificar los estados, el siguiente paso consiste en determinar la probabilidad de que el sistema esté en dicho estado, cuya información se coloca entonces en un **vector de probabilidades de estado.**

$$\pi(i) = \text{vector de probabilidades de estado para el periodo } i$$
$$= (\pi_1, \pi_2, \pi_3, \dots, \pi_n)$$
donde 
$$n = \text{número de estados}$$
$$\pi_{1}, \pi_{2}, \dots, \pi_{n} =\text{ son las probabilidades de estar en los estados } 1, 2, \dots, n, \text{ respectivamente.}$$

---

### **Vector de probabilidades de estado para el ejemplo de las tres tiendas de abarrotes**

#### **PROBLEMA**
Veamos el vector de estados para los clientes en el pequeño pueblo con tres tiendas de abarrotes. Puede haber un total de 100,000 personas que compran en las tres tiendas durante un mes dado. Unas 40,000 personas compran en American Food Store, que se llamará estado 1. Por otro lado, 30,000 pueden comprar en Food Mart, que se llamará estado 2; y 30,000 pueden comprar en Atlas Foods, que será el estado 3. La probabilidad de que una persona compre en una de las tres tiendas es la siguiente:

>_El vector de probabilidades de estado representa la participación en el mercado._

| Estado 1: American Food Store | $40,000/100,000 = 0.40 = 40\%$ |
| ----------------------------- | ------------------------------ |
| Estado 2: Food Mart           | $30,000/100,000 = 0.30 = 30\%$ |
| Estado 3: Atlas Foods         | $30,000/100,000 = 0.30 = 30\%$ |
Estas probabilidades se colocan en el vector de probabilidades de estado como:$$\pi(1) = (0.4, 0.3, 0.3)$$donde 
$\pi(1) = \text{vector de probabilidades de estado para tres tiendas en el periodo 1}$ $\pi_1 = 0.4 = \text{probabilidad de que una persona compre en American Food, estado 1}$ $\pi_2 = 0.3 = \text{probabilidad de que una persona compre en Food Mart, estado 2}$ $\pi_3 = 0.3 = \text{probabilidad de que una persona compre en Atlas Foods, estado 3}$

También debería observarse que las probabilidades en el vector de estado para las tres tiendas de abarrotes representan la **participación en el mercado para las mismas en el primer periodo**. Así, en el periodo 1 American Food tiene 40% el mercado; Food Mart 30%; y Atlas Foods 30%. Cuando se trata de participación en el mercado, estos se pueden utilizar en vez de los valores de probabilidad.

##### American Food $\#1$ (0.4)
En este ejemplo, se realizó un estudio para determinar la lealtad de los clientes. Se determinó que 80% de los clientes que compran en American Food un mes regresarán a esa tienda el siguiente. Del otro 20% de sus clientes, 10% cambia a Food Mart y 10% a Atlas Foods en su siguiente compra.
###### Multiplicando el porcentaje en decimal del estudio por el porcentaje inicial.

Multiplicando: 
0.8 (0.4) = 0.32
0.1 (0.4) = 0.04
0.1 (0.4) = 0.04

##### American Mart $\#2$ (0.3)
En Food Mart, 70% regresan, 10% cambia a American Food y 20% a Atlas Foods.

###### Multiplicando el porcentaje en decimal del estudio por el porcentaje inicial.

Multiplicando: 
0.3 (0.1) = 0.03
0.3 (0.7) = 0.21
0.3 (0.2) = 0.06

##### Atlas Foods $\#3$ (0.3)

De los clientes que compran este mes en Atlas Foods, 60% regresan, pero 20% cambiará a American Food y 20% a Food Mart.

###### Multiplicando el porcentaje en decimal del estudio por el porcentaje inicial.

Multiplicando: 
0.3 (0.2) = 0.06
0.3 (0.2) = 0.06
0.3 (0.6) = 0.18

##### **CONCLUYENDO**

La participación de mercado de 40% para American Food este mes, 32% regresa, 4% compra en Food Mart y 4% compra en Atlas Foods.

Para encontrar la participación de mercado de American el siguiente mes, sumamos este 32% de clientes que regresan mas el 3% de quienes vienen de Food Mart mas el 6% de quienes vienen de Atlas Foods.

**Entonces, American Food tendrá 41% del mercado el próximo mes.**

---

## **MATRIZ DE PROBABILIDADES DE TRANSICIÓN**

>**La matriz de probabilidades de transición nos permite ir de un estado a actual a un estado futuro.**

**Sea $P_{ij} = \text{Probabilidad condicional de estar en el estado j en el futuro, dado que el estado actual es i}$**

_Por ejemplo, $P_{12}$ es la probabilidad de estar en el estado 2 en el futuro, dado que el evento estaba en el estado 1 en el periodo anterior._

_Definimos $P = \text{matriz de probabilidades de transición}$_

$$P = 
\begin{bmatrix}  
P_{11} & P_{12} & P_{13} & \dots & P_{1n}  \\
P_{21} & P_{22} & P_{23} & \dots & P_{2n} \\
\vdots & \vdots & \vdots & & \vdots \\
 P_{m1} & P_{m2} & P_{m3} & \dots & P_{mn} 
\end{bmatrix}$$

---

## **Probabilidades de transición para las tres tiendas de abarrotes**

Usamos los datos históricos de las tres tiendas para determinar qué porcentaje de clientes cambiaría cada mes. Ponemos estas probabilidades de transición en la siguiente matriz:


$$
P=
\begin{bmatrix}
0.8 & 0.1 & 0.1 \\
0.1 & 0.7 & 0.2 \\
0.2 & 0.2 & 0.6
\end{bmatrix}
\qquad
\begin{array}{l}
&\text{Estado 1, American Foods}\\
&\text{Food Mart es el estado 2}\\
&\text{Atlas Foods es el estado 3}
\end{array}
$$
El significado de sus probabilidades se expresa en términos de los diferentes estados, como sigue:

**Renglón 1**
0.8 = $P_{11}$ = probabilidad de estar en el estado 1 después de estar en el estado 1 el periodo anterior
0.1 = $P_{12}$ = probabilidad de estar en el estado 2 después de estar en el estado 1 el periodo anterior
0.1 = $P_{13}$ = probabilidad de estar en el estado 3 después de estar en el estado 1 el periodo anterior

**Renglón 2**
0.1 = $P_{21}$ = probabilidad de estar en el estado 1 después de estar en el estado 2 el periodo anterior
0.7 = $P_{22}$ = probabilidad de estar en el estado 2 después de estar en el estado 2 el periodo anterior
0.2 = $P_{23}$ = probabilidad de estar en el estado 3 después de estar en el estado 2 el periodo anterior

**Renglón 3**

0.2 = $P_{31}$ = probabilidad de estar en el estado 1 después de estar en el estado 3 el periodo anterior
0.2 = $P_{32}$ = probabilidad de estar en el estado 2 después de estar en el estado 3 el periodo anterior
0.6 = $P_{33}$ = probabilidad de estar en el estado 3 después de estar en el estado 3 el periodo anterior

 >**Los valores de probabilidad para cualquier renglón deben sumar 1.**

---
 
## **Predicción de la participación futura en el mercado**

Uno de los propósitos del análisis de Markov es predecir el futuro. Dado el vector de probabilidades de estado y la matriz de probabilidades de transición, no es muy difícil determinar las probabilidades de estado en una fecha futura.

>Con ese tipo de análisis, podemos comparar la probabilidad de que un individuo compre en una de las tiendas en el futuro.

> Como tal probabilidad es equivalente a la participación en el mercado, es posible determinar participación futura en el mercado para American Food, Food Mart y Atlas Foods. Cuando el periodo actual es 0, calcular las probabilidades de estado para el siguiente periodo (periodo 1) se hace como sigue:

$$\pi(1) = \pi(0)P\tag{15-3}$$
Más aún, si estamos en cualquier periodo $n$, calculamos las probabilidades de estado para el periodo $n+1$ como:
$$\pi(n+1) = \pi(n)P\tag{15-4}$$
La ecuación 15-3 sirve para contestar la pregunta de las participaciones de mercado del siguiente periodo para las tiendas. Los cálculos son:

$$
\begin{array}{rcl}
\pi(1) &=& \pi(0)P \\[4pt]
&=& (0.4,\,0.3,\,0.3)
\begin{bmatrix}
0.8 & 0.1 & 0.1 \\
0.1 & 0.7 & 0.2 \\
0.2 & 0.2 & 0.6
\end{bmatrix} \\[8pt]
&=& \bigl[\;
(0.4)(0.8)+(0.3)(0.1)+(0.3)(0.2), \\[2pt]
&& (0.4)(0.1)+(0.3)(0.7)+(0.3)(0.2), \\[2pt]
&& (0.4)(0.1)+(0.3)(0.2)+(0.3)(0.6)
\; \bigr ] \\[8pt]
&=& (0.41,\,0.31,\,0.28)
\end{array}
$$

>Como se observa, la participación de mercado para American Food y Food Mart aumenta, en tanto que la de Atlas Food disminuye. ¿Continuará esta tendencia en el siguiente periodo y en el que le sigue? De la ecuación 15-4, derivamos un modelo que nos dirá cuáles serán las probabilidades en cualquier periodo futuro. Considere dos periodos a partir de ahora:

$$\pi(2) = \pi(1)P$$
Como sabemos que
$$\pi(1) = \pi(0)P$$
Tenemos $$\pi(2) = [\pi(1)]P = [\pi(0)P]P = \pi(0)PP = \pi(0)P^2$$
En general, $$\pi(n) = \pi(0)P^{n}\tag{15-5}$$
>Entonces, las probabilidades de estado n periodos en el futuro se obtienen de las probabilidades de estado actuales y la matriz de probabilidades de transición.

---

## **Análisis de Markov en operación de maquinaria**

Paul Tolsky, dueño de Tolsky Works, registró durante varios años la operación de sus fresadoras. En los dos últimos años, 80% de las veces la fresadora funcionaba correctamente en el mes actual, si había funcionado correctamente el mes anterior. Esto también significa que tan solo 20% del tiempo el funcionamiento de la máquina era incorrecto para cualquier mes, cuando estaba funcionando correctamente el mes anterior.

>En otras palabras, esta máquina puede corregirse cuando no ha funcionado bien en el pasado y esto ocurre 10% de las veces. Estos valores ahora se utilizan para construir la matriz de probabilidades de transición. De nuevo, el estado 1 es una situación donde la máquina funciona correctamente; y el estado 2, donde la máquina no lo hace.

$$P = 
\begin{bmatrix} 
0.8 & 0.2  \\
0.1 & 0.9 
\end{bmatrix}$$ 
donde 
$P_{11} = 0.8 = \text{probabilidad de que la máquina funcione correctamente este mes, dado que funcionaba correctamente el mes pasado}$
$P_{12} = 0.2 = \text{probabilidad de que la máquina no funcione correctamente este mes, dado que funcionaba correctamente el mes pasado}$
$P_{21} = 0.1 = \text{probabilidad de que la máquina funcione correctamente este mes, dado que no funcionaba correctamente el mes pasado}$
$P_{22} = 0.9 = \text{probabilidad de que la máquina no funcione correctamente este mes, dado que no funcionaba correctamente el mes pasado}$

>Las dos probabilidades del renglón superior son las probabilidades de funcionamiento correcto y funcionamiento incorrecto, dado que la máquina funcionaba correctamente el periodo anterior.

>- ¿Cuál es la probabilidad de que la máquina de Tolsky funcione correctamente dentro de un mes?
>- ¿Cuál es la probabilidad de que la máquina funcione correctamente dentro de dos meses?



$\pi(1) = \pi(0)P$ $= (1, 0) \begin{bmatrix} 0.8 & 0.2 \ 0.1 & 0.9 \end{bmatrix}$ $= [(1)(0.8) + (0)(0.1), (1)(0.2) + (0)(0.9)]$ $= (0.8, 0.2)$


$$\begin{array}{rcl}
\pi(1) &=& \pi(0)P \\[4pt]
&=& (1,\,0)
\begin{bmatrix}
0.8 & 0.2 \\
0.1 & 0.9
\end{bmatrix} \\[8pt]
&=& \bigl(
(1)(0.8)+(0)(0.1), \\
&& (1)(0.2)+(0)(0.9)
\bigr) \\[8pt]
&=& (0.8,\,0.2)
\end{array}
$$

>La probabilidad de que la máquina funcione correctamente dentro de un mes es de 0.80. La probabilidad de que no funcione correctamente en un mes es de 0.20.

>**Ahora utilizamos estos resultados para determinar la probabilidad de que la máquina funcione correctamente dentro de dos meses. El análisis es exactamente el mismo.**

$$
\begin{array}{rcl}
\pi(2) &=& \pi(1)P \\[4pt]
&=& (0.8,\,0.2)
\begin{bmatrix}
0.8 & 0.2 \\
0.1 & 0.9
\end{bmatrix} \\[8pt]
&=& \bigl[(0.8)(0.8)+(0.2)(0.1),\,
(0.8)(0.2)+(0.2)(0.9)\bigr] \\[8pt]
&=& (0.66,\,0.34)
\end{array}
$$

>- **Significa que dentro de dos meses hay una probabilidad de 0.66 de que la máquina todavía funcione correctamente.**
>- **La probabilidad de que la máquina no funcione correctamente es de 0.34.**

---

## **Condiciones de Equilibrio**

Al considerar el ejemplo de la máquina de Tolsky, es fácil pensar que con el paso del tiempo todas las participaciones de mercado o las probabilidades de estado serán 0 o 1. En general no ocurre así. Es normal encontrar el **porcentaje de equilibrio de los valores o las probabilidades de mercado. Las** probabilidades se llaman **probabilidades de estado estable o probabilidades de equilibrio.**

Una manera de calcular el estado estable del mercado es utilizar el análisis de Markov para un número grande de periodos. Es posible ver si los valores futuros se acercan a un valor estable. Por ejemplo, es posible repetir el análisis de Markov para la máquina de Tolsky durante 15 periodos. No es difícil hacerlo a mano. Los resultados del cálculo se muestran en la tabla:

|PERIODO|ESTADO 1|ESTADO 2|
|:--|:--|:--|
|1|1.000000|0.000000|
|2|0.800000|0.200000|
|3|0.660000|0.340000|
|4|0.562000|0.438000|
|5|0.493400|0.506600|
|6|0.445380|0.554620|
|7|0.411766|0.588234|
|8|0.388236|0.611763|
|9|0.371765|0.628234|
|10|0.360235|0.639754|
|11|0.352165|0.647834|
|12|0.346515|0.653484|
|13|0.342560|0.657439|
|14|0.339792|0.660207|
|15|0.337854|0.662145|

La máquina comienza con un funcionamiento correcto (en el estado 1) en el primer periodo. En el periodo 5, hay una probabilidad de tan solo 0.4934 de que la máquina todavía funcione correctamente y, para el periodo 10, esta probabilidad es solamente de 0.360235. En el periodo 15, la probabilidad de que la máquina todavía tenga un funcionamiento correcto es cercana a 0.34. La probabilidad de que la máquina todavía funcione bien en un periodo futuro disminuye, pero lo hace a una tasa determinada. ¿Qué se esperaría a la larga? Si hacemos los cálculos para 100 periodos, ¿qué pasaría? ¿Habrá un equilibrio en este caso? Si la respuesta es sí, ¿cuál sería? Viendo la tabla 15.1, parece que habrá un equilibrio en 0.333333, o bien, 1/3. Pero, ¿cómo estaríamos seguros?

Por definición, una **condición de equilibrio** existe si las probabilidades de estado o las participaciones de mercado no cambian después de muchos periodos. Entonces, el equilibrio, en este caso las probabilidades de estado para un periodo futuro, debe ser igual que las probabilidades de estado para el periodo actual. Este hecho es la clave para obtener las probabilidades de estado estable, cuya relación se expresa como: De la ecuación $\pi(n+1) = \pi(n)P$ siempre es cierto que (siguiente periodo) (este periodo)P

En el equilibrio, vemos que
 $$\pi(n+1) = \pi(n)$$
Por lo tanto, en el equilibrio, 
$$\pi(n+1) = \pi(n)P = \pi(n)$$
De manera que $$\pi(n) = \pi(n)P$$
o, eliminando el término en $n$, $$\pi = \pi P$$

>**En el equilibrio, las probabilidades de estado para el siguiente periodo son iguales a las probabilidades de estado para este periodo.** 

Esta ecuación establece que, en el equilibrio, las probabilidades de estado para el siguiente periodo son las mismas que las probabilidades de estado para el periodo actual.

Para la máquina de Tolsky, esto se expresa como sigue: $$\pi = \pi P$$
$$(\pi_1, \pi_2) = (\pi_1, \pi_2) \begin{bmatrix} 0.8 & 0.2 \\ 0.1 & 0.9 \end{bmatrix}$$ Aplicando la multiplicación de matrices $$(\pi_1, \pi_2) = [\;(\pi_1)(0.8) + (\pi_2)(0.1), (\pi_1)(0.2) + (\pi_2)(0.9)\;]$$

El primer término del lado izquierdo, $\pi_1$, es igual al primer término del lado derecho, $(\pi_1)(0.8) + (\pi_2)(0.1)$. Además, el segundo término del lado izquierdo, $\pi_2$, es igual al segundo término del lado derecho, $(\pi_1)(0.2) + (\pi_2)(0.9)$. Esto da lo siguiente:
 $$\pi_1 = 0.8\pi_1 + 0.1\pi_2\tag{a}$$
$$\pi_2 = 0.2\pi_1 + 0.9\pi_2\tag{b}$$ 
También sabemos que las probabilidades de estado, $\pi_1$ y $\pi_2$ en este caso, deben sumar 1. Expresamos esto como sigue:
 $$\pi_1 + \pi_2 + \dots + \pi_n = 1\tag{c}$$
 Para la máquina de Tolsky, tenemos $$\pi_1 + \pi_2 = 1$$

Ahora tenemos tres ecuaciones (a, b y c) para la máquina. Sabemos que debe cumplirse la ecuación c. Entonces, eliminamos la ecuación a o la b, y resolvemos las dos ecuaciones que quedan para obtener $\pi_1$ y $\pi_2$. Es necesario eliminar una de las ecuaciones, de manera que tengamos dos incógnitas y dos ecuaciones. Si estuviéramos buscando las condiciones de equilibrio que incluyeran tres estados, tendríamos cuatro ecuaciones. De nuevo, será necesario eliminar una de las ecuaciones para terminar con tres ecuaciones y tres incógnitas.

El motivo por el cual podemos eliminar una de las ecuaciones es que están matemáticamente interrelacionadas. En otras palabras, una de las ecuaciones es redundante al especificar las relaciones entre las diferentes ecuaciones de equilibrio.

Eliminemos de manera arbitraria la ecuación a. Así, resolveremos las siguientes dos ecuaciones: $$\pi_2 = 0.2\pi_1 + 0.9\pi_2$$
$$\pi_1 + \pi_2 = 1$$
Reordenando la primera ecuación, $0.1\pi_2 = 0.2\pi_1$ o bien, $\pi_2 = 2\pi_1$ 

Al sustituir esto en la ecuación d, obtenemos $\pi_1 + \pi_2 = 1$ o bien, $\pi_1 + 2\pi_1 = 1$ 

o bien, $3\pi_1 = 1 \Rightarrow \pi_1 = 1/3 = 0.33333333$ 

Entonces, $\pi_2 = 2/3 = 0.66666667$

Como se observa, la **probabilidad del estado estable** para el estado 1 es 0.33333333, y la probabilidad del estado de equilibrio para el estado 2 es 0.66666667, que son los valores que se esperan al ver los resultados de la tabla. El análisis indica que tan solo es necesario conocer la matriz de transición para determinar las participaciones en el mercado en equilibrio. Los valores iniciales para las probabilidades de estado o la participación en el mercado no influyen en las probabilidades del estado en equilibrio. El análisis para determinar las probabilidades del estado en equilibrio o las participaciones en el mercado es el mismo cuando hay más de tres estados.

# **Estados absorbentes y matriz fundamental: Cuentas por cobrar**

En los ejemplos estudiados hasta ahora, suponemos que es posible que el proceso o sistema vaya de un estado a cualquier otro, entre cualesquiera dos periodos. Sin embargo, en algunos casos no se puede ir a otro estado en el futuro. En otras palabras, cuando se encuentra en un estado dado, este lo "absorbe", y permanecerá en ese estado. Cualquier estado que tiene tal propiedad se llama **estado absorbente** un ejemplo es la aplicación de las cuentas por cobrar.

Un sistema de cuentas por cobrar generalmente coloca las deudas o las cuentas por cobrar de sus clientes en una de varias categorías o estados, dependiendo de lo atrasada que esté la cuenta sin pagar más antigua. Desde luego, las categorías o los estados exactos dependen de la política establecida por cada compañía. Cuatro estados o categorías típicos para una aplicación de cuentas por cobrar son los siguientes:

- Estado 1 ($\pi_1$): pagadas, todas las cuentas
- Estado 2 ($\pi_2$): deuda incobrable, atrasada por más de tres meses
- Estado 3 ($\pi_3$): atrasada menos de un mes
- Estado 4 ($\pi_4$): atrasada entre uno y tres meses

1. sdf


- Igual que en otros procesos de Markov, establecemos una matriz de probabilidades de transición para los cuatro estados. 
- La probabilidad de estar en la categoría pagada para cualquier cuenta en un mes futuro, dado que el cliente está en la categoría de pagada por una compra este mes, es de 100% o 1. 
- Para cualquier estado absorbente, la probabilidad de que un cliente esté en ese estado en el futuro es de 1, en tanto que la probabilidad de que un cliente esté en otro estado es de 0.
- Antes de elaborar esa matriz (a matriz de probabilidades de transición), necesitamos conocer las probabilidades para los otros dos estados: deuda de menos de un mes y deuda de uno a tres meses de antigüedad.

|ESTE MES|PAGADA|DEUDA INCOBRABLE|< 1 MES|1 A 3 MESES|
|:--|:--|:--|:--|:--|
|Pagada|1|0|0|0|
|Deuda incobrable|0|1|0|0|
|Menos de 1 mes|0.6|0|0.2|0.2|
|1 a 3 meses|0.4|0.1|0.3|0.2|

Entonces, $P = \begin{bmatrix} 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \ 0.6 & 0 & 0.2 & 0.2 \ 0.4 & 0.1 & 0.3 & 0.2 \end{bmatrix}$

Las condiciones de equilibrio son aún más interesantes. Desde luego, a la larga, todos estarán en la categoría de pagada o deuda incobrable, lo cual se debe a que las categorías son estados absorbentes. ¿Pero cuántas personas, o cuánto dinero, estarán en cada categoría? Si encontramos la cantidad total de dinero que quedará como pagada o deuda incobrable, ayudamos a la compañía a manejar sus deudas incobrables y sus flujos de efectivo. Un análisis así requiere lo que se conoce como **matriz fundamental**.

---

### **Página 22**

Para obtener la matriz fundamental, es necesario hacer una **partición de la matriz de probabilidades de transición, P**, como: $P = \begin{bmatrix} I & 0 \ A & B \end{bmatrix}$ donde $I = \begin{bmatrix} 1 & 0 \ 0 & 1 \end{bmatrix}$ (matriz identidad) $0 = \begin{bmatrix} 0 & 0 \ 0 & 0 \end{bmatrix}$ (matriz con tan solo ceros) $A = \begin{bmatrix} 0.6 & 0 \ 0.4 & 0.1 \end{bmatrix}$ $B = \begin{bmatrix} 0.2 & 0.2 \ 0.3 & 0.2 \end{bmatrix}$

La matriz fundamental se calcula como: **$F = (I - B)^{-1}$** Donde **F es la matriz fundamental**. Veamos cómo se calcula para la aplicación de cuentas por cobrar: $F = \left( \begin{bmatrix} 1 & 0 \ 0 & 1 \end{bmatrix} - \begin{bmatrix} 0.2 & 0.2 \ 0.3 & 0.2 \end{bmatrix} \right)^{-1}$ Al restar $B$ de $I$: $F = \begin{bmatrix} 0.8 & -0.2 \ -0.3 & 0.8 \end{bmatrix}^{-1}$

La matriz inversa de $\begin{bmatrix} a & b \ c & d \end{bmatrix}$ es $\begin{bmatrix} a & b \ c & d \end{bmatrix}^{-1} = \begin{bmatrix} d/r & -b/r \ -c/r & a/r \end{bmatrix}$ donde $r = ad - bc$. Para encontrar la matriz $F$: $r = ad - bc = (0.8)(0.8) - (-0.2)(-0.3) = 0.64 - 0.06 = 0.58$ $F = \begin{bmatrix} 0.8/0.58 & -(-0.2)/0.58 \ -(-0.3)/0.58 & 0.8/0.58 \end{bmatrix} = \begin{bmatrix} 1.38 & 0.34 \ 0.52 & 1.38 \end{bmatrix}$

---

### **Página 23**

Ahora estamos en posición de usar la matriz fundamental para calcular la cantidad de dinero en deuda incobrable que esperaríamos a la larga. Primero necesitamos multiplicar la matriz fundamental, $F$, por la matriz $A$. Esto se logra como sigue: $FA = \begin{bmatrix} 1.38 & 0.34 \ 0.52 & 1.38 \end{bmatrix} \times \begin{bmatrix} 0.6 & 0 \ 0.4 & 0.1 \end{bmatrix}$ es decir; $FA = \begin{bmatrix} 0.97 & 0.03 \ 0.86 & 0.14 \end{bmatrix}$

La nueva matriz **FA** tiene un significado importante. Indica la probabilidad de que una cantidad que está en uno de los estados no absorbentes termine en uno de ellos. El renglón superior indica las probabilidades de que una cantidad en la categoría de menos de un mes termine en la categoría de pagada (0.97) o deuda incobrable (0.03).

Sea la matriz **M** la cantidad de dinero que está en cada estado no absorbente: $M = (M_1, M_2, M_3, \dots, M_n)$ Suponga que hay $2,000 en la categoría de menos de un mes, y $5,000 en la de uno a tres meses. $M = (2,000, 5,000)$ Las cantidades que terminarán como pagada y como deuda incobrable se calculan multiplicando $M$ por $FA$: $MFA = (2,000, 5,000) \begin{bmatrix} 0.97 & 0.03 \ 0.86 & 0.14 \end{bmatrix} = (6,240, 760)$

**Entonces, del total de $7,000, $6,240 se pagarán al final y $760 terminarán como deuda incobrable.**