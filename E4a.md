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