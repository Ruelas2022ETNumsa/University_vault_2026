*   **E5.** Dada la función de densidad de distribución de probabilidad 
    conjunta como se indica a continuación:
    $$f_{W,X,Y,Z}(w,x,y,z) = \begin{cases} 16wxyz & \text{si } 0 \le w \le 1, 0 \le x \le 1, 0 \le y \le 1, 0 \le z \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Hallar la probabilidad de $W \le 3$ y que $Y \le \frac{1}{2}$.
    **b)** Encontrar la función de densidad marginal de $W$.

Para resolver el ejercicio **E5** de la **Práctica 2**, utilizaremos las propiedades de las funciones de densidad de probabilidad (PDF) para múltiples variables aleatorias continuas, tal como se describe en el formulario y los libros de texto de referencia.

### 1. Análisis de la función conjunta

La función de densidad conjunta es: $$f_{W,X,Y,Z}(w,x,y,z) = \begin{cases} 16wxyz & \text{si } 0 \le w, x, y, z \le 1 \ 0 & \text{en otro caso} \end{cases}$$ Se observa que la función es **factorizable** en términos independientes: $f(w,x,y,z) = (2w)(2x)(2y)(2z)$. Esto indica que las variables $W, X, Y$ y $Z$ son **estadísticamente independientes** entre sí dentro del hipercubo unitario $^4$.

---

### a) Hallar la probabilidad de $W \le 3$ y que $Y \le \frac{1}{2}$

Para calcular esta probabilidad, debemos integrar la función conjunta sobre la región especificada.

**Nota sobre los límites:** Aunque el enunciado pide $W \le 3$, la variable $W$ solo está definida en el intervalo . Por lo tanto, la condición $W \le 3$ abarca **todo** su rango de existencia ($0 \le W \le 1$).

$$P(W \le 3, Y \le 1/2) = \int_{0}^{1} \int_{0}^{1} \int_{0}^{1/2} \int_{0}^{1} 16wxyz , dz , dy , dx , dw$$

Debido a la independencia de las variables, podemos separar las integrales:

1. **Para W:** $\int_0^1 2w , dw = [w^2]_0^1 = 1$.
2. **Para Y:** $\int_0^{1/2} 2y , dy = [y^2]_0^{1/2} = (1/2)^2 = 1/4$.
3. **Para X y Z:** Al no haber restricciones adicionales, su probabilidad sobre el rango completo  es $1$.

$$P(W \le 3, Y \le 1/2) = (1) \cdot (1) \cdot \left(\frac{1}{4}\right) \cdot (1) = \mathbf{\frac{1}{4} = 0.25}$$

> [!check] Correcto
> La condición $W \le 3$ cubre todo el dominio $[0,1]$, por lo que su integral es 1. La factorización es válida porque el dominio es un hipercubo rectangular. Resultado $1/4$ ✓.

---

### b) Encontrar la función de densidad marginal de $W$

La densidad marginal de una variable se obtiene integrando la función conjunta respecto a todas las demás variables sobre sus respectivos rangos de definición:

$$f_W(w) = \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} 16wxyz , dx , dy , dz$$ $$f_W(w) = 16w \left( \int_{0}^{1} x , dx \right) \left( \int_{0}^{1} y , dy \right) \left( \int_{0}^{1} z , dz \right)$$

Calculando las integrales simples:

- $\int_0^1 x , dx = \frac{1}{2}$ (lo mismo para $y$ y $z$).

Sustituyendo: $$f_W(w) = 16w \cdot \left(\frac{1}{2}\right) \cdot \left(\frac{1}{2}\right) \cdot \left(\frac{1}{2}\right) = \frac{16w}{8}$$ $\mathbf{f_W(w) = 2w, \quad \text{para } 0 \le w \le 1}$

> [!check] Correcto
> La factorización de la integral triple es válida. Cada integral $\int_0^1 x\,dx = 1/2$, por lo que $16w \cdot (1/2)^3 = 2w$ ✓. Verificación: $\int_0^1 2w\,dw = 1$ ✓.

---

### Gráfica en Desmos

Representamos la función de densidad marginal de $W$ calculada ($f_W(w) = 2w$) y sombreamos el área que representa la probabilidad total de $W$ en su dominio.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=2.3;
width=500; height=500;
---
f(x)=2x|RED|0<=x<=1
x>=0|x<=1|y>=0|y<=2x|#a5d8ff
(0,0)|label:(0,0)|BLACK
(1,2)|label:(1,2)|BLACK
x=1|BLUE|DASHED|0<=y<=2
```

> [!correction] Corrección — Gráfica
> **Error identificado:** La sintaxis `0<=y<=2x{0<=x<=1}` no es válida en Desmos. Además faltaban los parámetros de ventana.
>
> **Corrección:** Se reemplazó por `x>=0|x<=1|y>=0|y<=2x` y se agregaron `left`, `right`, `bottom`, `top`.

**Explicación de la gráfica:**

- **Línea Roja ($f(x)$):** Representa la función de densidad marginal $f_W(w) = 2w$. Note que el valor máximo es 2 cuando $w=1$.
- **Área sombreada (#a5d8ff):** Representa el área bajo la curva de la densidad marginal. El área total de este triángulo es $\frac{1 \cdot 2}{2} = 1$, cumpliendo con la propiedad de normalización.
- **Línea Azul punteada:** Marca el límite del dominio de la variable aleatoria ($w=1$).