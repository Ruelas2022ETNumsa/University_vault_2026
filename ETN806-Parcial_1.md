# FORMULARIO VARIABLES ALEATORIAS DISCRETAS MULTIPLES (PARCIAL 1)
---
## ESPACIO MUESTRAL

$$  
S \ \text{o} \ \Omega  
$$
## ESPACIO DEL RANGO

$$  
S_x \ \text{o} \ Im(X)  
$$
---
## ESPERANZA MATEMÁTICA

$$  
E[X]=\mu_x=\sum_{x\in S_x}xP_x(x)  
$$

## VARIANZA

$$  
VAR[X]=\sum_{x\in S_x}(x-\mu_x)^2P_x(x)  
$$

## DESVIACIÓN ESTÁNDAR

$$  
\sigma=\sqrt{VAR[X]}=  
\sqrt{\sum_{x\in S_x}(x-\mu_x)^2P_x(x)}  
$$

## DISTRIBUCIÓN MARGINAL

Para X:
$$  
P_x(x)=\sum P_{X,Y}(x,y)  
$$

Para Y:
$$  
P_y(y)=\sum P_{X,Y}(x,y)  
$$

## ESPERANZA PARA UNA FUNCIÓN
$$  
E[W]=E[G(x,y)]

\sum_{x\in S_x}\sum_{y\in S_y}  
G(x,y)P_{X,Y}(x,y)  
$$

## COVARIANZA
$$  
COV[X,Y]=
E[(x-\mu_x)(y-\mu_y)]=
\sum (x-\mu_x)(y-\mu_y)P(x,y)  
$$

$$  
COV[X,Y]=
E[XY]-E[X]E[Y]  
$$

## CORRELACIÓN

$$  
\gamma_{x,y}=
E[XY]=
\sum xyP_{X,Y}(x,y)  
$$

---
## COEFICIENTE DE CORRELACIÓN
 $$  
\rho_{x,y}=
\frac{COV[X,Y]}  
{\sqrt{VAR[X]\cdot VAR[Y]}}  
$$

## DISTRIBUCIÓN CONDICIONAL
 $$  
P_{X/Y}(x/y)=
Prob(X=x/Y=y)  
$$

$$  
P_{X/Y}(x/y)=
\frac{P_{X,Y}(x,y)}  
{P_y(y)}  
$$
$$  
P_{Y/X}(y/x)=
\frac{P_{X,Y}(x,y)}  
{P_x(x)}  
$$

Valor esperado de X dado Y:
$$  
E[X/Y=y]=
\sum_{x\in S_x}  
xP_{X/Y}(x/y)  
$$

---
## ESTADÍSTICAMENTE INDEPENDIENTES

$$  
P_{X,Y}(x,y)=
P_x(x)P_y(y)  
$$
$$  
\gamma_{X,Y}=
E[XY]=
E[X]E[Y]  
$$

$$  
E[X/Y]=E[X]  
\qquad  
E[Y/X]
E[Y]  
$$

$$  
COV[X,Y]=\rho_{x,y}=
0  
$$

$$  
VAR[X+Y]=
VAR[X]+VAR[Y]  
$$

---
---

# 📝 Enunciado del Ejercicio 1 (1er parcial)

Si la distribución de probabilidad conjunta de x,y está dada por $f=\frac{(x+y)}{30}$ para $x = 0, 1, 2, 3$ y $y = 0, 1, 2$ .Calcular la probabilidad para x mayor a y

## Solución

Para calcular la probabilidad de que **$X$ sea mayor a $Y$** ($P(X > Y)$) con la función de distribución conjunta $f(x, y) = \frac{x+y}{30}$, debemos identificar y sumar las probabilidades de todos los pares $(x, y)$ que cumplen con dicha condición dentro de los rangos establecidos ($x = 0, 1, 2, 3$ y $y = 0, 1, 2$).

Los pares ordenados $(x, y)$ que satisfacen la desigualdad **$x > y$** son los siguientes:

- **Para $x = 1$:** El único valor posible es $y = 0$. La probabilidad es $f(1, 0) = \frac{1+0}{30} = \mathbf{\frac{1}{30}}$.
- **Para $x = 2$:** Los valores son $y = 0$ y $y = 1$.
    - $f(2, 0) = \frac{2+0}{30} = \mathbf{\frac{2}{30}}$.
    - $f(2, 1) = \frac{2+1}{30} = \mathbf{\frac{3}{30}}$.
- **Para $x = 3$:** Los valores son $y = 0, y = 1$ y $y = 2$.
    - $f(3, 0) = \frac{3+0}{30} = \mathbf{\frac{3}{30}}$.
    - $f(3, 1) = \frac{3+1}{30} = \mathbf{\frac{4}{30}}$.
    - $f(3, 2) = \frac{3+2}{30} = \mathbf{\frac{5}{30}}$.

**Cálculo final:** Sumamos todas las probabilidades obtenidas para estos puntos específicos: $$P(X > Y) = \frac{1}{30} + \frac{2}{30} + \frac{3}{30} + \frac{3}{30} + \frac{4}{30} + \frac{5}{30} = \mathbf{\frac{18}{30}}=\frac{3}{5}$$
Simplificando la fracción, el resultado es **$3/5$** o **$0.6$** (lo que equivale al **60%** de probabilidad).

---

# 📝 Enunciado del Ejercicio 2 (1er parcial)

Un experimento aleatorio conociste en probar dos circuitos integrados, uno tras de otro en cada prueba la probabilidad de que el circuito sea rechazado es $p$ . Sea $x$ en numero de rechazos 0 o 1 en la 1ra prueba y sea Y el numero de rechazos en la 2da prueba. Determine la función de distribución de probabilidad conjunta de $x$ y $y$ , la función de correlación entre las variables y el valor esperado de la suma es decir $E[ x+y ]$

## solución

Para resolver este experimento sobre la prueba secuencial de dos circuitos integrados, utilizaremos las propiedades de las **variables aleatorias discretas independientes** (procesos de Bernoulli) detalladas en las fuentes:

### 1. Función de distribución de probabilidad conjunta

Dado que las pruebas son sucesivas e independientes, la probabilidad de que ambos eventos ocurran simultáneamente es el producto de sus probabilidades individuales: $P(X=x, Y=y) = P(X=x)P(Y=y)$.

Definiendo la probabilidad de rechazo como $p$ y la de aceptación como $q = 1 - p$, los rangos de $X$ (primer test) y $Y$ (segundo test) son $\{0, 1\}$. La distribución conjunta se presenta en la siguiente tabla:

|$X \setminus Y$|0 (Aceptado)|1 (Rechazado)|Total Marginal ($X$)|
|:--|:-:|:-:|:-:|
|**0 (Aceptado)**|$(1-p)^2$|$(1-p)p$|$1-p$|
|**1 (Rechazado)**|$p(1-p)$|$p^2$|$p$|
|**Total Marginal ($Y$)**|$1-p$|$p$|**1**|

La **función de masa de probabilidad conjunta** se expresa matemáticamente como: $$f(x, y) = p^{x+y} (1-p)^{2-(x+y)} \quad \text{para } x,y \in \{0,1\}$$

### 2. Función de correlación ($\gamma_{X,Y}$)

Según la nomenclatura oficial de la materia y el formulario de la práctica, la **correlación** se define como el valor esperado del producto de las variables ($E[XY]$): $$\gamma_{X,Y} = EXY = \sum_{x} \sum_{y} xy \cdot P(X=x, Y=y)$$

Calculando los términos para cada par $(x, y)$:

- Para (0,0), (0,1) y (1,0), el producto $xy$ es **0**.
- Para (1,1): $1 \cdot 1 \cdot p^2 = p^2$.

Sumando los resultados, la **correlación es $p^2$**. Al ser variables independientes, se verifica también mediante la propiedad $E[XY] = E[X]E[Y] = p \cdot p = p^2$. _(Nota: El **coeficiente** de correlación lineal $\rho_{X,Y}$ para este caso es **0** debido a la independencia de las variables)._

### 3. Valor esperado de la suma $E[X+Y]$

Para hallar este valor, aplicamos la **propiedad de linealidad de la esperanza**, que establece que la esperanza de una suma es la suma de las esperanzas individuales: $$E[X+Y] = E[X] + E[Y]$$

1. **Cálculo de $E[X]$:** Al ser una variable de Bernoulli donde el rechazo tiene probabilidad $p$, $E[X] = 0(1-p) + 1(p) = p$.
2. **Cálculo de $E[Y]$:** De igual forma, $E[Y] = p$.
3. **Resultado:** $E[X+Y] = p + p = \mathbf{2p}$.

Este resultado indica que, en promedio, el número total de rechazos tras probar los dos circuitos será el **doble de la probabilidad de rechazo individual**.



# 📝 Enunciado del Ejercicio 3 (1er parcial)***

Se seleccionan a azar 2 repuestos para un dispositivo de una caja que contiene 3 repuestos marca Huawei, 2 Marca tecno y 3 marca infinix si x el  numero de repuestos marca Huawei y sea y el numero de repuestos marca tecno que se seleccionan calculé la tabla de distribución y coeficiente de correlación

## solución

Para resolver este problema, identificamos que el experimento consiste en seleccionar **2 repuestos de un total de 8** (3 Huawei, 2 Tecno, 3 Infinix) sin reemplazo, lo cual sigue una **distribución hipergeométrica multivariada**.

### 1. Tabla de Distribución de Probabilidad Conjunta

Definimos **X** como el número de repuestos Huawei y **Y** como el número de repuestos Tecno. El número total de formas de seleccionar 2 repuestos de 8 es $\binom{8}{2} = 28$. Los valores posibles para el par $(x, y)$ deben cumplir que $0 \leq x+y \leq 2$.

Utilizando la fórmula de combinaciones para cada celda $f(x, y) = P(X=x, Y=y)$:

- **f(0,0):** 0 Huawei, 0 Tecno (2 Infinix) $\rightarrow \binom{3}{0}\binom{2}{0}\binom{3}{2} / 28 = 3/28$.
- **f(1,0):** 1 Huawei, 0 Tecno (1 Infinix) $\rightarrow \binom{3}{1}\binom{2}{0}\binom{3}{1} / 28 = 9/28$.
- **f(2,0):** 2 Huawei, 0 Tecno (0 Infinix) $\rightarrow \binom{3}{2}\binom{2}{0}\binom{3}{0} / 28 = 3/28$.
- **f(0,1):** 0 Huawei, 1 Tecno (1 Infinix) $\rightarrow \binom{3}{0}\binom{2}{1}\binom{3}{1} / 28 = 6/28$.
- **f(1,1):** 1 Huawei, 1 Tecno (0 Infinix) $\rightarrow \binom{3}{1}\binom{2}{1}\binom{3}{0} / 28 = 6/28$.
- **f(0,2):** 0 Huawei, 2 Tecno (0 Infinix) $\rightarrow \binom{3}{0}\binom{2}{2}\binom{3}{0} / 28 = 1/28$.

**Tabla resumida (frecuencias sobre 28):**

|Y \ X|0|1|2|Marginal (Y)|
|:--|:-:|:-:|:-:|:-:|
|**0**|$3/28$|$9/28$|$3/28$|**$15/28$**|
|**1**|$6/28$|$6/28$|$0$|**$12/28$**|
|**2**|$1/28$|$0$|$0$|**$1/28$**|
|**Marginal (X)**|**$10/28$**|**$15/28$**|**$3/28$**|**1**|

---

### 2. Cálculo del Coeficiente de Correlación ($\rho_{XY}$)***

Para hallar el coeficiente, necesitamos la covarianza y las desviaciones estándar.

- **Esperanzas Matemáticas:**
    - $E[X] = 0(10/28) + 1(15/28) + 2(3/28) = 21/28 = \mathbf{3/4}$
    - $E[Y] = 0(15/28) + 1(12/28) + 2(1/28) = 14/28 = \mathbf{1/2}$
    - $E[XY] = \sum \sum xy f(x,y) = (1)(1)(6/28) = \mathbf{3/14}$
- **Covarianza:**
    - $Cov(X, Y) = E[XY] - E[X]E[Y] = 3/14 - (3/4)(1/2) = 3/14 - 3/8 = \mathbf{-9/56}$
- **Varianzas:**
    - $Var(X) = [1^2(15/28) + 2^2(3/28)] - (3/4)^2 = 27/28 - 9/16 = \mathbf{45/112}$
    - $Var(Y) = [1^2(12/28) + 2^2(1/28)] - (1/2)^2 = 16/28 - 1/4 = \mathbf{9/28}$

**Resultado Final:** El **coeficiente de correlación** se calcula como: $$\rho_{XY} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y} = \frac{-9/56}{\sqrt{(45/112)(9/28)}} = -\frac{1}{\sqrt{5}} \approx \mathbf{-0.4472}$$ _(Nota: Aunque el cálculo matemático exacto da $-1/\sqrt{5}$, una de las fuentes proporciona como respuesta final $-1/5$, lo cual podría deberse a un redondeo o error tipográfico en dicho texto)._


# PRACTICA N°1

# PROCESOS ESTOCASTICOS

# VARIABLES ALEATORIAS DISCRETAS MULTIPLES

1. Una compañía de teléfonos cobra 20 centavos por llamada de voz y 30 centavos por una llamada de fax; si la variable aleatoria C representa el costo de una llamada telefónica y la probabilidad de que una llamada de voz $P[V]=0.6$ y que sea de fax $P[F]=0.4$ determine:
    a) La distribución de probabilidad de la variable C
    b) El valor esperado y la desviación estándar de C

2. Considere una variable aleatoria X y una combinación lineal de esta:
    $Y=aX+b$.
    Calcular el coeficiente de correlación lineal de "X" y "Y".

3. Sean "X" y "Y" variables aleatorias discretas, con esperanza finita. Demostrar la siguiente igualdad
$$  
E[E[Y/X]]=E[Y]  
$$

4. Sean $X_1$ y $X_2$ dos variables aleatorias independientes. Sean $Y_1=X_1-X_2$ y $Y_2=X_1+X_2$. Hallar la condición que deben cumplir $X_1$ y $X_2$ para qué $Y_1$ y $Y_2$ sean no correlacionados.

5. Un experimento aleatorio consiste en probar dos circuitos integrados, uno tras otro; en cada prueba la probabilidad de que el circuito sea rechazado es "p". Sea X el numero de rechazos (ya sea 0 o 1) en la primera prueba y sea Y el numero de rechazos en la segunda prueba. Determine la función de distribución de probabilidad conjunta de "X" y "Y"; la función de correlación entre las variables y el valor esperado de la suma, es decir $E[X+Y]$

6. Un experimento aleatorio consiste en el lanzamiento de una moneda 3 veces, si se define la variable aleatoria X como el numero total de sellos obtenidos y la variable aleatoria Y como el número de caras obtenidas en el último lanzamiento, encontrar la función de distribución de probabilidad conjunta y las distribuciones marginales todas expresadas en forma de lista.
    
7. Las variables "X" y "Y" tiene la distribución de probabilidad conjunta dada por
    

$$  
P_{X,Y}(x,y)=  
\begin{cases}  
cxy & : x=1,2,4 \qquad y=1,3\   \\
0 & : \text{en otro caso}  
\end{cases}  
$$

a) Cual es el valor de la constante c
b) Cual es la probabilidad de que $Y<X$
c) Cuales son las probabilidades marginales
d) Calcule los valores esperados $E[X]$ y $E[Y]$
e) Determine las desviaciones estándar $\sigma_x$ y $\sigma_y$

8. Las variables aleatorias "X" y "Y" tiene distribución de probabilidad conjunta dada por $P_{X,Y}(x,y)=c|x+y|$ para $x=-2,0,2$ ;  $y=-1,0,1$ y $P_{X,Y}(x,y)=0$ para otro caso.

a) Calcular la función de distribución de probabilidad de $P_w(w)$ cuándo $W=X+2Y$
b) El valor esperado de W.
c) La probabilidad de $P[W>0]$

9. Determinar la función de probabilidad conjunta de las variables aleatorias A y B, la función de distribución de probabilidad condicional
    

$$  
P_{A/B}(a/0)  
$$

cuando $B=0$ y calcular la

$$  
COV[A,B]  
$$

sabiendo que la función de distribución de probabilidad de la variable aleatoria A y la función de distribución de probabilidad condicional de B dado A son:

$$  
P_A(a)=  
\begin{cases}  
0.4 & ;a=0\  
0.6 & ;a=2\  
0 & ;\text{en otro caso}  
\end{cases}  
$$

$$  
P_{B/A}(b/0)=  
\begin{cases}  
0.8 & ;b=0\  
0.2 & ;b=1\  
0 & ;\text{en otro caso}  
\end{cases}  
$$

$$  
P_{B/A}(b/2)=  
\begin{cases}  
0.5 & ;b=0\  
0.5 & ;b=1\  
0 & ;\text{en otro caso}  
\end{cases}  
$$

10. La función de probabilidad conjunta para dos variables aleatorias "X" y "Y" esta dada por la matriz que se indica a continuación; determine el valor esperado condicional
    

$$  
E[X/Y=y]  
$$

para cada valor de Y.

|$P_{X,Y}(x,y)$|$y=0$|$y=1$|$y=2$|
|---|--:|--:|--:|
|$x=0$|0.01|0|0|
|$x=1$|0.09|0.09|0|
|$x=2$|0|0|0.81|

