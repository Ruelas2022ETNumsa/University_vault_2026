*   **E6.** Las variables aleatorias $X, Y$ tiene la función de densidad de 
    distribución de probabilidad que se indica:
    $$f_{X,Y}(x,y) = \begin{cases} \frac{1}{2} & \text{si } -1 \le x \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Dibujar la región de probabilidad distinta de cero.
    **b)** Determinar la función de densidad marginal de $X$.
    **c)** Determine $P(X > 0)$.
    **d)** Determinar el valor esperado de $X$.

Para resolver este ejercicio, el cual corresponde a una variante del **Ejercicio 6** (identificado en las fuentes como el problema 4.5.1 de Yates & Goodman), asumiremos la región de soporte completa necesaria para que la función sea una densidad válida con la constante $1/2$.

### Enunciado del Ejercicio

Las variables aleatorias $X, Y$ tienen la siguiente función de densidad de distribución conjunta: $$f_{X,Y}(x,y) = \begin{cases} \frac{1}{2} & \text{si } -1 \le x \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

### Resolución Paso a Paso

#### a) Dibujar la región de probabilidad distinta de cero

La región de soporte está definida por las desigualdades $-1 \le x \le 1$, $y \le 1$ y, fundamentalmente, **$x \le y$**. Esto describe un **triángulo** en el plano con los siguientes vértices:

- $(-1, -1)$
- $(-1, 1)$
- $(1, 1)$

Esta región ocupa la mitad superior izquierda del cuadrado delimitado por $x, y \in [-1, 1]$.

#### b) Determinar la función de densidad marginal de $X$ ($f_X(x)$)

Para obtener la marginal de $X$, integramos la función conjunta respecto a $y$ sobre su rango de existencia. Para un valor fijo de $x$, $y$ varía desde $x$ hasta $1$: $$f_X(x) = \int_{x}^{1} \frac{1}{2} , dy = \frac{1}{2} [y]_x^1$$ $$\mathbf{f_X(x) = \frac{1}{2}(1 - x), \quad \text{para } -1 \le x \le 1}$$.

#### c) Determine $P(X > 0)$

Integramos la densidad marginal de $X$ calculada en el inciso anterior sobre el intervalo $(0, 1)$: $$P(X > 0) = \int_{0}^{1} \frac{1}{2}(1 - x) , dx = \frac{1}{2} \left[ x - \frac{x^2}{2} \right]_0^1$$ $$P(X > 0) = \frac{1}{2} \left( 1 - \frac{1}{2} \right) = \mathbf{\frac{1}{4} = 0.25}$$.

#### d) Determinar el valor esperado de $X$ ($E[X]$)

Aplicamos la definición de esperanza para una variable aleatoria continua: $$E[X] = \int_{-1}^{1} x \cdot f_X(x) , dx = \int_{-1}^{1} x \cdot \frac{1}{2}(1 - x) , dx$$ $$E[X] = \frac{1}{2} \int_{-1}^{1} (x - x^2) , dx = \frac{1}{2} \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_{-1}^1$$ Evaluando en los límites: $$E[X] = \frac{1}{2} \left[ \left( \frac{1}{2} - \frac{1}{3} \right) - \left( \frac{1}{2} + \frac{1}{3} \right) \right] = \frac{1}{2} \left[ -\frac{2}{3} \right] = \mathbf{-\frac{1}{3} \approx -0.3333}$$.

---

### Gráfica en Desmos

La gráfica muestra el soporte triangular donde la probabilidad es uniforme ($1/2$) y la curva de la densidad marginal de $X$.

```desmos
width=500; height=500;
---
y>=x|y<=1|x>=-1|#a5d8ff
y=x|RED|-1<=x<=1
y=1|RED|-1<=x<=1
x=-1|RED|-1<=y<=1
f(x)=0.5(1-x)|BLUE|-1<=x<=1
(-1,-1)|label:(-1,-1)|BLACK
(-1,1)|label:(-1,1)|BLACK
(1,1)|label:(1,1)|BLACK
```

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa la región de soporte conjunta $-1 \le x \le y \le 1$.
- **Línea Roja:** Delimita los bordes del triángulo de probabilidad.
- **Línea Azul ($f(x)$):** Representa la función de densidad marginal $f_X(x) = 0.5(1-x)$. Note que la probabilidad es mayor cuando $x$ es cercano a $-1$ y disminuye linealmente hasta llegar a cero en $x=1$.
- **Puntos etiquetados:** Indican los vértices del dominio de las variables aleatorias.