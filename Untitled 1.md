# tamaño desmos

**Pequeño — gráficas simples (rectas numéricas, intervalos, un punto):**  
`width=300; height=200;`

**Mediano — uso general (funciones, parábolas, trigonométricas, regiones):**  
`width=400; height=350;`

**Grande — gráficas con muchos detalles (múltiples curvas, etiquetas, regiones sombreadas):**  
`width=550; height=450;`

El punto crítico es la relación ancho/alto — para funciones estándar un ratio cercano a 1:1 o 4:3 se ve bien. Para rectas numéricas el ratio horizontal es mejor (3:1 o 4:2).


## Función par

$y = x^{4} - 4x^{2} + 3$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=5;
---
y = x^4 - 4x^2 + 3
```

---

## Función impar

$f(x)=2x^{5}+6x^{3}-8x$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-5; top=5;
---
f(x)=2x^{5}+6x^{3}-8x
```

---

## Función tangente

$f(x)=\tan(x)$

```desmos-graph
width=400; height=350;
---
y=\tan(x)
```

$f(x)=\dfrac{1}{\tan(x)}$

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\frac{1}{x}
```




---

## Función de primer grado

$f(x)=2x+1$

**Desmos**

```desmos-graph
width=300; height=200;
---
y=2x+1
```

---

## Función de segundo grado

$f(x)=x^2-4x+3$

**Desmos**

```desmos-graph
width=300; height=200;

left=-3; right=7; bottom=-2; top=7;


---
y=x^2-4x+3
```

## Función potencial generalizada

$$y=x^{\frac{3}{2}}$$

```desmos-graph
width=300; height=200;
---
y=x^{3/2}
```

ojo que en desmos y=x^(3/2) no da, parace que si esta adecuado a la notacion de latex con unas excepciones.

## Función potencial generalizada

$$y=x^{-\frac{1}{2}}$$

```desmos-graph
width=300; height=200;
left=-0.5; right=7; bottom=-0.5; top=5;
---
y=x^{-1/2}
```


## Función potencial generalizada

$$y=x^{\frac{2}{3}}$$

```desmos-graph

width=300; height=200;
left=-10; right=10; bottom=-0.5; top=5;
---
y=x^{2/3}
```

## Función potencial generalizada

$$y=x^{-\frac{2}{3}}$$

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=5;
---

y=x^{-2/3}
```

---

## Función de tercer grado

$f(x)=x^3-3x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-4; top=4;
---
y=x^3-3x
```

---

## Función exponencial base 2

$f(x)=2^x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=2^x
```

---

## Función exponencial natural

$f(x)=e^x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=e^x
```

---

## Función logarítmica base 10

$f(x)=\log_{10}(x)$

**Desmos**

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-2; top=0.5;
---
y=\log(x)
```

---

## Función logarítmica natural (base e)

$f(x)=\ln(x)$

**Desmos**

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-3; top=2;
---
y=\ln(x)
```

---

## Función seno

$f(x)=\sin(x)$

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\sin(x)
```

## Función coseno

$f(x)=\cos(x)$

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\cos(x)
```

## Función tangente

$f(x)=\tan(x)$

```desmos-graph
width=400; height=350;
---
y=\tan(x)
```

---

## Función arco seno

$$y=\arcsin(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\sin(x)   |-3<=x<=3|#5E81AC|DASHED
y=x         |-3<=x<=3|#777777|DASHED
y=-\arcsin(x)-3.1416|-1<=x<=1|#A65C59|dashed
y=-\arcsin(x)+3.1416|-1<=x<=1|#A65C59|dashed
y=\arcsin(x)|-1<=x<=1|#D97706|solid

(1,3.1416/2)|label:(1,pi/2)|#D97706|cross
(-1,-3.1416/2)|label:-(1,pi/2)|#D97706|cross
```

## Función arco coseno

$$y=\arccos(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\cos(x)|-3<=x<=3|#5E81AC|DASHED
y=x|-3<=x<=3|#777777|DASHED
y=\arccos(x)|-1<=x<=1|#D97706|SOLID
y=-\arccos(x)|-1<=x<=1|#A65C59|DASHED

(1,0)|label:(1,0)|#D97706|cross
(0,1.5708)|label:(0,pi/2)|#D97706|cross
(-1,3.1416)|label:(-1,pi)|#D97706|cross
```

## Función arco tangente

$f(x)=\arctan(x)$

```desmos-graph
left=-3; right=3; bottom=-3; top=3;
width=400; height=350;
---
y=\tan(x)   |-1.55<=x<=1.55|#5E81AC|DASHED
y=x|-7<=x<=7|#777777|DASHED
y=\arctan(x)|-7<=x<=7|#D97706|SOLID

x=-1.5708|-7<=y<=7|#5E81AC|DASHED
x=1.5708 |-7<=y<=7|#5E81AC|DASHED

y=-1.5708|-7<=x<=7|#A65C59|DASHED
y=1.5708 |-7<=x<=7|#A65C59|DASHED

(0,0)       |label:(0,0)|#D97706|cross
```



---

## Función seno hiperbólico

$f(x)=\sinh(x)$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\sinh(x)
```

## Función coseno hiperbólico

$f(x)=\cosh(x)$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=4;
---
y=\cosh(x)|#D97706
(0,1)|label:(0,1)|#D97706|cross
```

---

## Función valor absoluto

$f(x)=|x|$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=2;
---
y=\abs(x)
```

## Función recta

$f(x)=|2x-3|$

```desmos-graph
width=300; height=200;
left=-1; right=4; bottom=-0.5; top=4;
---
y=\abs(2x-3)
```

## Función valor absoluto de una ecuación de segundo grado

$f(x)=|x^{2}-4x+3|$

```desmos-graph
width=300; height=200;
left=-1; right=5; bottom=-0.5; top=3;
---
y=\abs(x^{2}-4x+3)
```

$y=|x||x-4|$

```desmos-graph
width=300; height=200;
left=-2; right=6; bottom=-0.5; top=5;
---
y=\abs(x)\abs(x-4)
```

$$y=\left||x^2-4|-4\right|$$

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=6;
---
y=\abs(\abs(x^{2}-4)-4)
```

---

## Función parte entera

$f(x)=\lfloor x\rfloor$

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\floor(x)
```

$f_{x}=x^{2}$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-0.5; top=6;
---
y=\floor(x^2)
```

---

## Función distancia

$$
\{x\}=
\begin{cases}
0, & \text{si } x\in\mathbb{Z},\\[4pt]
|x-a|, & \text{si } x\notin\mathbb{Z},\ a\in\mathbb{Z}\text{ es el entero más cercano.}
\end{cases}
$$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))
```

$$y=\{x^2\}$$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x^{2},1),1-\operatorname{mod}(x^{2},1))
```

---

## Función signo

$$
\operatorname{sgn}(x)=
\begin{cases}
-1, & \text{si } x<0,\\[4pt]
0, & \text{si } x=0,\\[4pt]
1, & \text{si } x>0.
\end{cases}
$$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\operatorname{sgn}(x)|#D97706

(0,0)|label:(-1,-1)|#D97706

(0,-1)|#D97706|open
(0,1)|#D97706|open
```

Sea

$$
u=x^4-5x^2+4.
$$

La función signo está definida por

$$
\operatorname{sgn}(u)=
\begin{cases}
-1,&u<0,\\[4pt]
0,&u=0,\\[4pt]
1,&u>0.
\end{cases}
$$

Primero se factoriza el polinomio:

$$
u=x^4-5x^2+4=(x^2-1)(x^2-4)
=(x-2)(x-1)(x+1)(x+2).
$$

Las raíces son

$$
x=-2,\,-1,\,1,\,2.
$$

| Intervalo o punto | Valor de prueba | Signo de $u=x^4-5x^2+4$ | Valor de $\operatorname{sgn}(u)$ |    Representación gráfica     |
|:-----------------:|:---------------:|:-----------------------:|:--------------------------------:|:-----------------------------:|
|  $(-\infty,-2)$   |      $-3$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |
|      $x=-2$       |      $-2$       |           $0$           |               $0$                |    Punto cerrado $(-2,0)$     |
|     $(-2,-1)$     |     $-1.5$      |           $-$           |               $-1$               | Segmento horizontal en $y=-1$ |
|      $x=-1$       |      $-1$       |           $0$           |               $0$                |    Punto cerrado $(-1,0)$     |
|     $(-1,1)$      |       $0$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |
|       $x=1$       |       $1$       |           $0$           |               $0$                |     Punto cerrado $(1,0)$     |
|      $(1,2)$      |      $1.5$      |           $-$           |               $-1$               | Segmento horizontal en $y=-1$ |
|       $x=2$       |       $2$       |           $0$           |               $0$                |     Punto cerrado $(2,0)$     |
|   $(2,\infty)$    |       $3$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |



```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=2;
---
y=\operatorname{sgn}(x^4-5x^2+4)|#D97706

(-2,0)|label:(-2,0)|#D97706
(-1,0)|label:(-1,0)|#D97706
(1,0)|label:(1,0)|#D97706
(2,0)|label:(2,0)|#D97706

(-2,1)|#D97706|open
(-2,-1)|#D97706|open

(-1,1)|#D97706|open
(-1,-1)|#D97706|open

(1,1)|#D97706|open
(1,-1)|#D97706|open

(2,1)|#D97706|open
(2,-1)|#D97706|open
```

> **Observación:** El caso $u=0$ únicamente determina los **puntos cerrados** de la gráfica, correspondientes a las raíces del polinomio. Matemáticamente, la función **no contiene segmentos verticales** en esos valores de $x$; solo existen los puntos abiertos provenientes de los intervalos adyacentes y el punto cerrado donde $u=0$. Algunos graficadores, como Desmos, dibujan pequeños segmentos verticales para resaltar la discontinuidad o debido a su algoritmo de renderizado, pero dichos segmentos **no forman parte de la gráfica de la función** desde el punto de vista matemático.

**ALTERNATIVA (GRAFICAMENTE CORRECTA )A LA FUNCION SIGNO**

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=2;
---
y=1|-3<=x<-2|#D97706
y=-1|-2<x<-1|#D97706
y=1|-1<x<1|#D97706
y=-1|1<x<2|#D97706
y=1|2<x<=3|#D97706

(-2,0)|label:(-2,0)|#D97706
(-1,0)|label:(-1,0)|#D97706
(1,0)|label:(1,0)|#D97706
(2,0)|label:(2,0)|#D97706

(-2,1)|#D97706|open
(-2,-1)|#D97706|open

(-1,1)|#D97706|open
(-1,-1)|#D97706|open

(1,1)|#D97706|open
(1,-1)|#D97706|open

(2,1)|#D97706|open
(2,-1)|#D97706|open
```







## Función escalón unitario

$$
u(x)=
\begin{cases}
0, & x<0,\\[4pt]
1, & x\ge 0.
\end{cases}
$$


```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-1; top=2;
---
y=0|-2<=x<0|#D97706
y=1|0<=x<=2|#D97706

(0,0)|#D97706|open
(0,1)|label:(0,1)|#D97706
```

ejemplos

$$
y=
\begin{cases}
0, & x<0,\\[4pt]
2x, & 0\le x\le3,\\[4pt]
6, & x\ge3.
\end{cases}
$$

### Análisis

```desmos-graph
width=300; height=200;
left=-2; right=5; bottom=-1; top=8;
---
y=0|-2<=x<0|#D97706
y=2x|0<=x<=3|#D97706
y=6|3<=x<=5|#D97706

(0,0)|label:(0,0)|#D97706
(3,6)|label:(3,6)|#D97706
```

Dada la función

$$
y=
\begin{cases}
0, & x<0,\\[4pt]
2x, & 0\le x\le3,\\[4pt]
6, & x\ge3.
\end{cases}
$$

se desea expresarla utilizando la función escalón unitario

$$
u(x-a)=
\begin{cases}
0, & x<a,\\[4pt]
1, & x\ge a.
\end{cases}
$$

### Paso 1. Identificar los puntos de cambio

La función cambia de expresión en

$$
x=0
\qquad\text{y}\qquad
x=3.
$$

Por tanto, se utilizarán los escalones

$$
u(x)
\qquad\text{y}\qquad
u(x-3).
$$

### Paso 2. Analizar el primer intervalo

Para

$$
x<0,
$$

la función vale

$$
y=0.
$$

Como antes de activar el primer escalón la función ya vale cero, no es necesario escribir ningún término adicional.

### Paso 3. Activar la recta

A partir de

$$
x=0,
$$

la función toma la forma

$$
y=2x.
$$

Para que esta expresión aparezca únicamente desde $x=0$, se multiplica por

$$
u(x).
$$

Así se obtiene

$$
2x\,u(x).
$$

Verificación:

- Si $x<0$

$$
u(x)=0,
$$

entonces

$$
2x\,u(x)=0.
$$

- Si $x\ge0$

$$
u(x)=1,
$$

entonces

$$
2x\,u(x)=2x.
$$

Hasta este punto la función queda

$$
y=2x\,u(x).
$$

### Paso 4. Cambiar la recta por la constante

En

$$
x=3
$$

la función deja de ser

$$
2x
$$

y pasa a ser

$$
6.
$$

La diferencia entre la nueva expresión y la anterior es

$$
6-2x.
$$

Esa diferencia debe agregarse únicamente cuando

$$
x\ge3,
$$

por lo que se multiplica por

$$
u(x-3).
$$

Se obtiene

$$
(6-2x)\,u(x-3).
$$

### Paso 5. Expresión final

Sumando ambos aportes,

$$
\boxed{
y=2x\,u(x)+(6-2x)\,u(x-3)
}
$$



















---


# cosas que le tuve que aclarar a chat gpt

en las graficas desmos:
- en las pontencias usar {} por ejemplo x^{potencia} nunca x^(potencia)
- 
  un hallazgo importante en desmos para algunas palabras reservadas se debe usar \ como

- \cos
    
- \frac{1}{3}
    

esto

```desmos-graph

y=2\cos(x)-\frac{x^2}{10}