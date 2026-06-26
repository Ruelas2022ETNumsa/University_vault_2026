## Función par

$y = x^{4} - 4x^{2} + 3$

```desmos-graph
y = x^4 - 4x^2 + 3
```

---

## Función impar

$f(x)=2x^{5}+6x^{3}-8x$

```desmos-graph
f(x)=2x^{5}+6x^{3}-8x
```

---

## Función tangente

$f(x)=\tan(x)$

**Desmos**

```desmos-graph
y=\tan(x)
```

$f(x)=\dfrac{1}{\tan(x)}$

```desmos-graph
y=\frac{1}{x}
```

---

## Función de primer grado

$f(x)=2x+1$

**Desmos**

```desmos-graph
y=2x+1
```

---

## Función de segundo grado

$f(x)=x^2-4x+3$

**Desmos**

```desmos-graph
y=x^2-4x+3
```

## Función potencial generalizada

$$y=x^{\frac{3}{2}}$$

```desmos-graph
y=x^{3/2}
```

ojo que en desmos y=x^(3/2) no da, parace que si esta adecuado a la notacion de latex con unas excepciones.

## Función potencial generalizada

$$y=x^{-\frac{1}{2}}$$

```desmos-graph
y=x^{-1/2}
```


## Función potencial generalizada

$$y=x^{\frac{2}{3}}$$

```desmos-graph
y=x^{2/3}
```

## Función potencial generalizada

$$y=x^{-\frac{2}{3}}$$

```desmos-graph
y=x^{-2/3}
```

---

## Función de tercer grado

$f(x)=x^3-3x$

**Desmos**

```desmos-graph
y=x^3-3x
```

---

## Función exponencial base 2

$f(x)=2^x$

**Desmos**

```desmos-graph
y=2^x
```

---

## Función exponencial natural

$f(x)=e^x$

**Desmos**

```desmos-graph
y=e^x
```

---

## Función logarítmica base 10

$f(x)=\log_{10}(x)$

**Desmos**

```desmos-graph
y=\log(x)
```

---

## Función logarítmica natural (base e)

$f(x)=\ln(x)$

**Desmos**

```desmos-graph
y=\ln(x)
```

---

## Función seno

$f(x)=\sin(x)$

```desmos-graph
y=\sin(x)
```

## Función coseno

$f(x)=\cos(x)$

```desmos-graph
y=\cos(x)
```

## Función tangente

$f(x)=\tan(x)$

```desmos-graph
y=\tan(x)
```

---

## Función arco seno

$f(x)=\arcsin(x)$

```desmos-graph
y=\arcsin(x)
```


## Función arco seno

$$y=\arcsin(x)$$

```desmos-graph
y=\arcsin(x)
y=\sin(x)\left\{-1\le x\le1\right\}
y=x\left\{-2\le x\le2\right\}
```


## Función arco seno

$$y=\arcsin(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=500; height=500;
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

$f(x)=\arccos(x)$

```desmos-graph
y=\arccos(x)
```

## Función arco coseno

$$y=\arccos(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=500; height=500;
---
y=\cos(x)|-3<=x<=3|#5E81AC|DASHED
y=x|-3<=x<=3|#777777|DASHED
y=\arccos(x)|-1<=x<=1|#e74440|SOLID
y=-\arccos(x)|-1<=x<=1|#A65C59|DASHED
```




## Función arco tangente

$f(x)=\arctan(x)$

```desmos-graph
y=\arctan(x)
```

---

## Función seno hiperbólico

$f(x)=\sinh(x)$

```desmos-graph
y=\sinh(x)
```

## Función coseno hiperbólico

$f(x)=\cosh(x)$

```desmos-graph
y=\cosh(x)
```

---

## Función valor absoluto

$f(x)=|x|$

```desmos-graph
y=\abs(x)
```

## Función recta

$f(x)=|2x-3|$

```desmos-graph
y=\abs(2x-3)
```

## Función valor absoluto de una ecuación de segundo grado

$f(x)=|x^2-4x+3|$

```desmos-graph
y=\abs(x^{2}-4x+3)
```

$y=|x||x-4|$

```desmos-graph
y=\abs(x)\abs(x-4)
```

$$y=\left||x^2-4|-4\right|$$

```desmos-graph
y=\abs(\abs(x^{2}-4)-4)
```


---

## Función parte entera

$f(x)=\lfloor x\rfloor$

```desmos-graph
y=\floor(x)
```

$f_{x}=x^{2}$

```desmos-graph
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
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))
```

$$y=\{x-1\}$$

```desmos-graph
y=\min(\operatorname{mod}(x-1,1),1-\operatorname{mod}(x-1,1))
```

$$y=\{x^2\}$$

```desmos-graph
y=\min(\operatorname{mod}(x^{2},1),1-\operatorname{mod}(x^{2},1))
```

---

## Función escalón unitario

$$
u(x)=
\begin{cases}
0, & x<0,\\[4pt]
1, & x\ge 0.
\end{cases}
$$

```desmos-graph
y=\left\{x<0:0,\ x\ge0:1\right\}
```


---


# cosas que le tuve que aclarar a chat gpt

en las graficas desmos:
- en las pontencias usar {} por ejemplo x^{potencia} nunca x^(potencia)
- 
  