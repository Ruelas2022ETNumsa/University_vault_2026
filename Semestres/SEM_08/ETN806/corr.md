# 1.

Se seleccionan al azar 2 repuestos de una caja con 3 **HUAWEI**, 2 **TECNO** y 3 **INFINIX**. Sea $X$ el número de repuestos HUAWEI e $Y$ el número de repuestos TECNO seleccionados. Calcule la tabla de distribución y el coeficiente de correlación.

---

## Solución

**Total de formas de selección:** $$\binom{8}{2} = 28$$

**Probabilidad conjunta** (distribución hipergeométrica multivariada): $$P_{X,Y}(x,y) = \frac{\binom{3}{x}\binom{2}{y}\binom{3}{2-x-y}}{28}$$

**Cálculo de cada celda:**

||$x=0$|$x=1$|$x=2$|$P_Y(y)$|
|:-:|:-:|:-:|:-:|:-:|
|$y=0$|$\frac{3}{28}$|$\frac{9}{28}$|$\frac{3}{28}$|$\frac{15}{28}$|
|$y=1$|$\frac{6}{28}$|$\frac{6}{28}$|$0$|$\frac{12}{28}$|
|$y=2$|$\frac{1}{28}$|$0$|$0$|$\frac{1}{28}$|
|$P_X(x)$|$\frac{10}{28}$|$\frac{15}{28}$|$\frac{3}{28}$|$1$|

---

**Esperanzas:** $$E[X] = 0\cdot\frac{10}{28}+1\cdot\frac{15}{28}+2\cdot\frac{3}{28} = \frac{21}{28} = \frac{3}{4}$$ $$E[Y] = 0\cdot\frac{15}{28}+1\cdot\frac{12}{28}+2\cdot\frac{1}{28} = \frac{14}{28} = \frac{1}{2}$$

**Correlación** (único término no nulo: $x=1,y=1$): $$\gamma_{X,Y} = E[XY] = 1\cdot1\cdot\frac{6}{28} = \frac{3}{14}$$

**Covarianza:** $$COV[X,Y] = E[XY]-E[X]E[Y] = \frac{3}{14}-\frac{3}{4}\cdot\frac{1}{2} = \frac{3}{14}-\frac{3}{8} = \frac{12-21}{56} = -\frac{9}{56}$$

**Varianzas:** $$E[X^2] = 1^2\cdot\frac{15}{28}+2^2\cdot\frac{3}{28} = \frac{27}{28} \implies VAR[X] = \frac{27}{28}-\left(\frac{3}{4}\right)^2 = \frac{108-63}{112} = \frac{45}{112}$$ $$E[Y^2] = 1^2\cdot\frac{12}{28}+2^2\cdot\frac{1}{28} = \frac{16}{28} \implies VAR[Y] = \frac{4}{7}-\frac{1}{4} = \frac{9}{28}$$

**Coeficiente de correlación:** $$\rho_{XY} = \frac{-9/56}{\sqrt{\dfrac{45}{112}\cdot\dfrac{9}{28}}} = \frac{-9/56}{\sqrt{\dfrac{405}{3136}}} = \frac{-9/56}{\dfrac{9\sqrt{5}}{56}} = \boxed{-\frac{1}{\sqrt{5}} \approx -0.4472}$$

---

# 2. (25%)

$$f_{X,Y}(x,y)=\begin{cases}\dfrac{2}{\pi}, & x^2+y^2 \le 1,\quad 0 \le y \le 1 \\
0, & \text{en otro caso}\end{cases}$$

Analice solo en los dos primeros cuadrantes. Encontrar $f_X(x)$ y $f_Y(y)$.

---

## Solución

La región de soporte es el **semicírculo unitario superior** ($-1\le x\le 1$, $0\le y\le 1$).

### a) Marginal de $X$

Para $x$ fijo, $y$ va de $0$ a $\sqrt{1-x^2}$: $$f_X(x) = \int_0^{\sqrt{1-x^2}}\frac{2}{\pi},dy = \frac{2}{\pi}\left[,y,\right]_0^{\sqrt{1-x^2}}$$

$$\boxed{f_X(x) = \frac{2\sqrt{1-x^2}}{\pi}, \quad -1\le x\le 1}$$

### b) Marginal de $Y$

Para $y$ fijo, $x$ va de $-\sqrt{1-y^2}$ a $\sqrt{1-y^2}$: $$f_Y(y) = \int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}}\frac{2}{\pi},dx = \frac{2}{\pi}\left[x\right]_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} = \frac{2}{\pi}\cdot 2\sqrt{1-y^2}$$

$$\boxed{f_Y(y) = \frac{4\sqrt{1-y^2}}{\pi}, \quad 0\le y\le 1}$$

**Verificación:** $\displaystyle\int_{-1}^{1}\frac{2}{\pi}\sqrt{1-x^2},dx = \frac{2}{\pi}\cdot\frac{\pi}{2}=1$ ✓ $\quad$ $\displaystyle\int_0^1\frac{4}{\pi}\sqrt{1-y^2},dy=\frac{4}{\pi}\cdot\frac{\pi}{4}=1$ ✓

```desmos-graph
left=-1.5; right=1.5; bottom=-0.3; top=1.5;
---
x^2+y^2<=1|y>=0|#a5d8ff
f(x)=\frac{2\sqrt{1-x^2}}{\pi}|-1<=x<=1|RED
g(y)=\frac{4\sqrt{1-y^2}}{\pi}|0<=y<=1|GREEN
```

- **Azul:** soporte semicircular.
- **Rojo:** $f_X(x)$, máximo en $x=0$.
- **Verde:** $f_Y(y)$, máximo en $y=0$.

---

# 3. (25%)

Experimento: lanzamiento de una moneda 3 veces. $X$ = número total de sellos; $Y$ = número de caras en el **último** lanzamiento. Encontrar la distribución conjunta y las marginales.

---

## Solución

Cada resultado tiene probabilidad $1/8$.

**Espacio muestral y mapeo:**

|Resultado|$X$ (sellos)|$Y$ (cara en 3°)|$(x,y)$|
|:-:|:-:|:-:|:-:|
|CCC|0|1|(0,1)|
|CCS|1|0|(1,0)|
|CSC|1|1|(1,1)|
|CSS|2|0|(2,0)|
|SCC|1|1|(1,1)|
|SCS|2|0|(2,0)|
|SSC|2|1|(2,1)|
|SSS|3|0|(3,0)|

**Tabla conjunta y marginales:**

|$Y\setminus X$|$0$|$1$|$2$|$3$|$P_Y(y)$|
|:-:|:-:|:-:|:-:|:-:|:-:|
|$0$|$0$|$\frac{1}{8}$|$\frac{2}{8}$|$\frac{1}{8}$|$\frac{1}{2}$|
|$1$|$\frac{1}{8}$|$\frac{2}{8}$|$\frac{1}{8}$|$0$|$\frac{1}{2}$|
|$P_X(x)$|$\frac{1}{8}$|$\frac{3}{8}$|$\frac{3}{8}$|$\frac{1}{8}$|$1$|

**Distribución conjunta:** $$P_{X,Y}(x,y) = \begin{cases} 1/8, & (x,y) \in {(0,1),(1,0),(2,1),(3,0)} \ 2/8, & (x,y) \in {(1,1),(2,0)} \ 0, & \text{en otro caso} \end{cases}$$

**Marginal de $X$** — $X\sim\text{Binomial}(3,\tfrac{1}{2})$: $$P_X(x) = \begin{cases} 1/8, & x=0 \ 3/8, & x=1 \ 3/8, & x=2 \ 1/8, & x=3 \ 0, & \text{otro caso} \end{cases}$$

**Marginal de $Y$** — $Y\sim\text{Bernoulli}(\tfrac{1}{2})$: $$P_Y(y) = \begin{cases} 1/2, & y=0 \ 1/2, & y=1 \ 0, & \text{otro caso} \end{cases}$$

**Independencia:** $P(X=3,Y=1)=0 \neq P_X(3)\cdot P_Y(1)=\dfrac{1}{16}$ → $X$ e $Y$ **no son independientes**.

---

# 4. (25%)

$$f_{X,Y}(x,y)=\begin{cases}e^{-y}, & x>0,\quad y>x \\
0, & \text{en otro caso}\end{cases}$$

Encontrar las distribuciones marginales y evaluar $P(X>2\mid Y<4)$.

---

## Solución

### Marginal de $X$

Para $x$ fijo, $y$ va de $x$ a $\infty$: $$f_X(x) = \int_x^\infty e^{-y},dy = \left[-e^{-y}\right]_x^\infty = e^{-x}$$

$$\boxed{f_X(x) = e^{-x}, \quad x>0}$$

### Marginal de $Y$

Para $y$ fijo, $x$ va de $0$ a $y$: $$f_Y(y) = \int_0^y e^{-y},dx = e^{-y}\cdot y$$

$$\boxed{f_Y(y) = ye^{-y}, \quad y>0}$$

### Probabilidad condicional $P(X>2\mid Y<4)$

$$P(X>2\mid Y<4) = \frac{P(X>2,;Y<4)}{P(Y<4)}$$

**Denominador** — integración por partes ($\int ye^{-y}dy = -e^{-y}(y+1)$): $$P(Y<4) = \int_0^4 ye^{-y},dy = \left[-e^{-y}(y+1)\right]_0^4 = 1-5e^{-4}$$

**Numerador** — región: $2<x<4$, $x<y<4$: $$P(X>2,Y<4) = \int_2^4\int_x^4 e^{-y},dy,dx$$

Integral interna: $$\int_x^4 e^{-y},dy = e^{-x}-e^{-4}$$

Integral externa: $$\int_2^4(e^{-x}-e^{-4}),dx = \left[-e^{-x}-xe^{-4}\right]_2^4 = (-e^{-4}-4e^{-4})-(-e^{-2}-2e^{-4}) = e^{-2}-3e^{-4}$$

**Resultado:** $$P(X>2\mid Y<4) = \frac{e^{-2}-3e^{-4}}{1-5e^{-4}} = \frac{0.1353-0.0549}{1-0.0916} = \frac{0.0804}{0.9084}$$

$$\boxed{P(X>2\mid Y<4)\approx 0.0885}$$