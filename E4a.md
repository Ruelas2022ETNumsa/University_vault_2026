*   **E4.** Las funciones aleatorias $X, Y$ tiene la función de densidad de
    distribución conjunta que se indica calcular la varianza de $W = X+Y$:
    $$f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } x \ge 0, y \ge 0, x+y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$

Para resolver el ejercicio **E4** de la **Práctica 2**, seguiremos el procedimiento para calcular la varianza de una suma de variables aleatorias continuas utilizando el método de la función de densidad de la nueva variable $W = X+Y$.

### Paso 1: Definir la región de soporte y la función conjunta

La función de densidad conjunta está dada por: $$f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } x \ge 0, y \ge 0, x+y \le 1 \ 0 & \text{en otro caso} \end{cases}$$ Esta región representa un **triángulo** en el primer cuadrante con vértices en $(0,0)$, $(1,0)$ y $(0,1)$.

### Paso 2: Hallar la función de densidad de $W = X+Y$

Para encontrar la densidad de la suma $f_W(w)$, integramos la función conjunta sobre la recta $x+y=w$ dentro de los límites de soporte. Para el rango $0 \le w \le 1$: $f_W(w) = \int_{0}^{w} f_{X,Y}(x, w-x) \, dx = \int_{0}^{w} 2 \, dx = \mathbf{2w, \quad \text{para } 0 \le w \le 1}$ Este resultado se obtiene considerando que para un valor fijo de $w$, $x$ varía desde $0$ hasta $w$.

> [!check] Correcto
> $f_W(w)=2w$ es válida: $\int_0^1 2w\,dw=1$ ✓.

### Paso 3: Calcular el valor esperado $E[W]$

Utilizando la densidad $f_W(w)$ encontrada: $$E[W] = \int_{0}^{1} w \cdot f_W(w) , dw = \int_{0}^{1} w(2w) , dw = \int_{0}^{1} 2w^2 , dw$$ $E[W] = \left[ \frac{2w^3}{3} \right]_0^1 = \mathbf{\frac{2}{3}}$

> [!check] Correcto

### Paso 4: Calcular el segundo momento $E[W^2]$

$$E[W^2] = \int_{0}^{1} w^2 \cdot f_W(w) , dw = \int_{0}^{1} w^2(2w) , dw = \int_{0}^{1} 2w^3 , dw$$ $E[W^2] = \left[ \frac{2w^4}{4} \right]_0^1 = \mathbf{\frac{1}{2}}$

> [!check] Correcto

### Paso 5: Calcular la varianza de $W$

Aplicamos la fórmula de la varianza $VAR[W] = E[W^2] - (E[W])^2$: $$VAR[W] = \frac{1}{2} - \left( \frac{2}{3} \right)^2 = \frac{1}{2} - \frac{4}{9}$$ $VAR[W] = \frac{9 - 8}{18} = \mathbf{\frac{1}{18} \approx 0.0556}$

> [!check] Correcto
> Resultado verificado también por el método del formulario: $VAR[X]=VAR[Y]=1/18$, $COV[X,Y]=-1/36$, $VAR[X+Y]=1/18+1/18+2(-1/36)=1/18$ ✓.

---

## Resolución alternativa — Método del Formulario ($VAR[X+Y]$ desde la conjunta)

Este método aplica directamente las fórmulas del formulario: calcular las marginales, los momentos de cada variable, la covarianza y finalmente $VAR[X+Y]=VAR[X]+VAR[Y]+2\,COV[X,Y]$.

### Paso A: Densidades marginales

**Marginal de $X$:** integrar en $y$ de $0$ a $1-x$:
$f_X(x) = \int_0^{1-x} 2\,dy = 2(1-x), \quad 0 \le x \le 1$

**Marginal de $Y$:** por simetría:
$f_Y(y) = 2(1-y), \quad 0 \le y \le 1$

### Paso B: Momentos de $X$ (por simetría, los de $Y$ son idénticos)

$E[X] = \int_0^1 x\cdot 2(1-x)\,dx = 2\int_0^1(x-x^2)\,dx = 2\left[\frac{1}{2}-\frac{1}{3}\right] = \frac{1}{3}$

$E[X^2] = \int_0^1 x^2\cdot 2(1-x)\,dx = 2\int_0^1(x^2-x^3)\,dx = 2\left[\frac{1}{3}-\frac{1}{4}\right] = \frac{1}{6}$

$VAR[X] = E[X^2]-(E[X])^2 = \frac{1}{6}-\frac{1}{9} = \frac{3-2}{18} = \frac{1}{18}$

Por simetría: $E[Y]=\dfrac{1}{3}$, $VAR[Y]=\dfrac{1}{18}$.

### Paso C: Covarianza $COV[X,Y]$

$E[XY] = \int_0^1\int_0^{1-x} 2xy\,dy\,dx = \int_0^1 2x\left[\frac{y^2}{2}\right]_0^{1-x}dx = \int_0^1 x(1-x)^2\,dx$

$= \int_0^1(x - 2x^2 + x^3)\,dx = \frac{1}{2}-\frac{2}{3}+\frac{1}{4} = \frac{6-8+3}{12} = \frac{1}{12}$

$COV[X,Y] = E[XY]-\mu_X\mu_Y = \frac{1}{12}-\frac{1}{3}\cdot\frac{1}{3} = \frac{1}{12}-\frac{1}{9} = \frac{3-4}{36} = -\frac{1}{36}$

> La covarianza negativa confirma que $X$ e $Y$ son dependientes (dominio triangular: si $X$ es grande, $Y$ debe ser pequeño).

### Paso D: Varianza de la suma

$VAR[X+Y] = VAR[X]+VAR[Y]+2\,COV[X,Y] = \frac{1}{18}+\frac{1}{18}+2\left(-\frac{1}{36}\right) = \frac{2}{18}-\frac{2}{36} = \frac{4}{36}-\frac{2}{36} = \mathbf{\frac{1}{18}}$

> [!check] Ambos métodos coinciden
> Método de convolución: $VAR[W]=1/18$. Método del formulario: $VAR[X+Y]=1/18$. Resultado consistente ✓.

---

### Gráfica en Desmos

La gráfica muestra la región triangular de soporte de la densidad conjunta y la función de densidad resultante para $W$ (proyectada en el eje para visualización).

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x+y<=1|x>=0|y>=0|#a5d8ff
y=1-x|BLUE|0<=x<=1
f(x)=2x|RED|0<=x<=1
(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** El bloque estaba marcado como ` ```  ` genérico en lugar de ` ```desmos-graph `, por lo que Obsidian no lo renderiza. Además faltaban los parámetros de ventana.
>
> **Corrección:** Se cambió a ` ```desmos-graph ` y se agregaron `left=-0.2; right=1.3; bottom=-0.2; top=1.3;`.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el soporte de la distribución conjunta $f_{X,Y}(x,y)=2$ en la región triangular descrita.
- **Línea Azul ($y=1-x$):** El límite superior de la región de probabilidad.
- **Línea Roja ($f(x)$):** Representa la función de densidad de la suma $W = X+Y$, que es $f_W(w)=2w$ para $0 \le w \le 1$.
- **Puntos etiquetados:** Marcan los vértices del dominio de definición de las variables aleatorias.