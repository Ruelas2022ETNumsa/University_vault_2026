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

- American Food $\#1$ (0.4)
	- 0.8
- American Mart $\#2$ (0.3)
- Atlas Foods $\#3$ (0.3)




En este ejemplo, se realizó un estudio para determinar la lealtad de los clientes. Se determinó que 80% de los clientes que compran en American Food un mes regresarán a esa tienda el siguiente. Del otro 20% de sus clientes, 10% cambia a Food Mart y 10% a Atlas Foods en su siguiente compra.

##### Multiplicando el porcentaje en decimal del estudio por el porcentaje inicial.

Multiplicando: 
0.3 (0.1) = 0.03
0.3 (0.7) = 0.21
0.3 (0.2) = 0.06

##### En Food Mart, 70% regresan, 10% cambia a American Food y 20% a Atlas Foods.

##### De los clientes que compran este mes en Atlas Foods, 60% regresan, pero 20% cambiará a American Food y 20% a Food Mart.

##### Multiplicando: 0.3 (0.2) = 0.06; 0.3 (0.2) = 0.06; 0.3 (0.6) = 0.18

---

### **Página 5**

# **CONCLUYENDO**

##### la participación de mercado de 40% para American Food este mes, 32% regresa, 4% compra en Food Mart y 4% compra en Atlas Foods.

##### Para encontrar la participación de mercado de American el siguiente mes, sumamos este 32% de clientes que regresan mas el 3% de quienes vienen de Food Mart mas el 6% de quienes vienen de Atlas Foods.

##### Entonces, American Food tendrá 41% del mercado el próximo mes.

# **MATRIZ DE PROBABILIDADES DE TRANSICIÓN**

##### **La matriz de probabilidades de transición nos permite ir de un estado a actual a un estado futuro.**

##### **Sea Pij = Probabilidad condicional de estar en el estado j en el futuro, dado que el estado actual es i**

##### _Por ejemplo, $P_{12}$ es la probabilidad de estar en el estado 2 en el futuro, dado que el evento estaba en el estado 1 en el periodo anterior._

##### _Definimos P = matriz de probabilidades de transición_

$P = \begin{bmatrix} P_{11} & P_{12} & P_{13} & \dots & P_{1n} \ P_{21} & P_{22} & P_{23} & \dots & P_{2n} \ \vdots & \vdots & \vdots & & \vdots \ P_{m1} & P_{m2} & P_{m3} & \dots & P_{mn} \end{bmatrix}$









# **Probabilidades de transición para las tres tiendas de abarrotes**

##### Usamos los datos históricos de las tres tiendas para determinar qué porcentaje de clientes cambiaría cada mes. Ponemos estas probabilidades de transición en la siguiente matriz:

##### Estado 1, American Foods

##### Food Mart es el estado 2

##### Atlas Foods es el estado 3