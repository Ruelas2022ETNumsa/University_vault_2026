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

# 📝 Enunciado del Ejercicio 1 (parcial)

Si la distribución de probabilidad conjunta de x,y está dada por $f=\frac{#}{#}(x+y)/30$ para x = 0 1 2 3 y y= 0 1 2 Calcular la probabilidad para x mayor a y



# Parcial







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

4. Sean $X_1$ y $X_2$ dos variables aleatorias independientes. Sean
    

$$  
Y_1=X_1-X_2  
$$

y

$$  
Y_2=X_1+X_2  
$$

Hallar la condición que deben cumplir $X_1$ y $X_2$ para qué $Y_1$ y $Y_2$ sean no correlacionados.

5. Un experimento aleatorio consiste en probar dos circuitos integrados, uno tras otro; en cada prueba la probabilidad de que el circuito sea rechazado es "p". Sea X el numero de rechazos (ya sea 0 o 1) en la primera prueba y sea Y el numero de rechazos en la segunda prueba. Determine la función de distribución de probabilidad conjunta de "X" y "Y"; la función de correlación entre las variables y el valor esperado de la suma, es decir
    

$$  
E[X+Y]  
$$

6. Un experimento aleatorio consiste en el lanzamiento de una moneda 3 veces, si se define la variable aleatoria X como el numero total de sellos obtenidos y la variable aleatoria Y como el número de caras obtenidas en el último lanzamiento, encontrar la función de distribución de probabilidad conjunta y las distribuciones marginales todas expresadas en forma de lista.
    
7. Las variables "X" y "Y" tiene la distribución de probabilidad conjunta dada por
    

$$  
P_{X,Y}(x,y)=  
\begin{cases}  
cxy & : x=1,2,4 \qquad y=1,3\  
0 & : \text{en otro caso}  
\end{cases}  
$$

a) Cual es el valor de la constante c

b) Cual es la probabilidad de que $Y<X$

c) Cuales son las probabilidades marginales

d) Calcule los valores esperados $E[X]$ y $E[Y]$

e) Determine las desviaciones estándar $\sigma_x$ y $\sigma_y$

8. Las variables aleatorias "X" y "Y" tiene distribución de probabilidad conjunta dada por
    

$$  
P_{X,Y}(x,y)=c|x+y|  
$$

para

$$  
x=-2,0,2  
$$

$$  
y=-1,0,1  
$$

y

$$  
P_{X,Y}(x,y)=0  
$$

para otro caso.

a) Calcular la función de distribución de probabilidad de $P_w(w)$ cuándo

$$  
W=X+2Y  
$$

b) El valor esperado de W.

c) La probabilidad de

$$  
P[W>0]  
$$

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

