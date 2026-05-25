 **E1.** Encontrar el valor de $k$ en la siguiente función 
    $f_{X,Y}(x,y)$ y también la función de distribución marginal de $X$:
    $$f_{X,Y}(x,y) = \begin{cases} \frac{k(1+x+y)}{(1+x)^4 (1+y)^4} & \text{si } 0 \le x \le \infty; 0 \le y \le \infty \\ 0 & \text{en otro caso} \end{cases}$$

Para resolver este ejercicio, seguiremos los pasos metodológicos establecidos en las fuentes para funciones de densidad de probabilidad (PDF) conjunta y marginal.

### 1. Determinar el valor de $k$

Para que $f_{X,Y}(x,y)$ sea una función de densidad válida, la integral doble sobre todo su dominio debe ser igual a 1. El rango de integración es de $0$ a $\infty$ para ambas variables.

La integral a resolver es: $$\int_{0}^{\infty} \int_{0}^{\infty} \frac{k(1+x+y)}{(1+x)^4 (1+y)^4} , dy , dx = 1$$

Podemos separar el numerador como $(1+x) + y$ para facilitar la integración respecto a $y$: $$k \int_{0}^{\infty} \frac{1}{(1+x)^4} \left[ \int_{0}^{\infty} \frac{1+x}{(1+y)^4} , dy + \int_{0}^{\infty} \frac{y}{(1+y)^4} , dy \right] dx = 1$$

- **Integración interna (respecto a $y$):**
    
    1. $(1+x) \int_{0}^{\infty} (1+y)^{-4} , dy = (1+x) \left[ \frac{(1+y)^{-3}}{-3} \right]_{0}^{\infty} = (1+x) \left( \frac{1}{3} \right) = \frac{1+x}{3}$.
    2. Para $\int_{0}^{\infty} y(1+y)^{-4} , dy$, usamos la sustitución $u=1+y$, resultando en $\int_{1}^{\infty} (u-1)u^{-4} , du = \left[ -\frac{1}{2u^2} + \frac{1}{3u^3} \right]_{1}^{\infty} = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$.
    
    - Suma de la integral interna: $\frac{1+x}{3} + \frac{1}{6} = \frac{2x+2+1}{6} = \frac{2x+3}{6}$.
- **Integración externa (respecto a $x$):** Ahora integramos el resultado anterior multiplicado por el factor de $x$ restante: $$\frac{k}{6} \int_{0}^{\infty} \frac{2x+3}{(1+x)^4} , dx = \frac{k}{6} \int_{0}^{\infty} \frac{2(1+x) + 1}{(1+x)^4} , dx$$ $$\frac{k}{6} \left[ 2 \int_{0}^{\infty} (1+x)^{-3} , dx + \int_{0}^{\infty} (1+x)^{-4} , dx \right] = \frac{k}{6} \left[ 2 \left( \frac{1}{2} \right) + \frac{1}{3} \right] = \frac{k}{6} \left( \frac{4}{3} \right) = \frac{2k}{9}$$
    
- **Cálculo de $k$:** Igualamos a 1: $\frac{2k}{9} = 1 \implies \mathbf{k = \frac{9}{2} = 4.5}$.
    

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. La separación del numerador $(1+x+y) = (1+x) + y$, las dos integrales impropias internas y la integración externa son correctas. $k = 9/2$.



```desmos-graph
left=-0.5; right=6; bottom=-0.1; top=1.2;
width=500; height=500;
---
x>=0|y>=0|#a5d8ff
f(x)=3(2x+3)/(4(1+x)^4)|RED|0<=x<=5
\frac{4.5(1+x+y)}{(1+x)^4(1+y)^4}=0.5|PURPLE|x>=0|y>=0
\frac{4.5(1+x+y)}{(1+x)^4(1+y)^4}=0.1|ORANGE|x>=0|y>=0
\frac{4.5(1+x+y)}{(1+x)^4(1+y)^4}=1|BLUE|x>=0|y>=0
f(x,y) = \frac{4.5(1+x+y)}{(1+x)^4(1+y)^4}
(0,0)|label:(0,0)|BLACK
```



---

### 2. Función de densidad marginal de $X$

La densidad marginal $f_X(x)$ se obtiene integrando la función conjunta respecto a $y$ sobre todo su rango. Aprovechando el cálculo de la integral interna realizado anteriormente con $k = 4.5$:

$$f_X(x) = \frac{4.5}{(1+x)^4} \cdot \left( \frac{2x+3}{6} \right)$$ Simplificando la expresión: $\mathbf{f_X(x) = \frac{3(2x+3)}{4(1+x)^4}, \quad \text{para } x \ge 0}$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. La integral interna $\frac{2x+3}{6}$ reutilizada del inciso anterior es correcta, y la simplificación $\frac{9/2}{(1+x)^4}\cdot\frac{2x+3}{6} = \frac{3(2x+3)}{4(1+x)^4}$ es correcta.

---

### Gráfica en Desmos

La región de probabilidad es el primer cuadrante ($x \ge 0, y \ge 0$). Se grafica el dominio y la curva de la densidad marginal de $X$ calculada.

```desmos-graph
left=-0.5; right=6; bottom=-0.1; top=1.2;
width=500; height=500;
---
x>=0|y>=0|#a5d8ff
f(x)=3(2x+3)/(4(1+x)^4)|RED|0<=x<=5
(0,0)|label:(0,0)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Al bloque `desmos-graph` le faltaban los parámetros de ventana (`left`, `right`, `bottom`, `top`) antes del separador `---`. Sin ellos Desmos usa zoom automático que puede no mostrar bien la curva.
>
> **Corrección:** Se agregaron `left=-0.5; right=6; bottom=-0.1; top=1.2;` para que la curva de $f_X(x)$ (que cae rápido desde $x=0$) quede bien visible en el primer cuadrante.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el soporte de la distribución conjunta en el primer cuadrante.
- **Línea Roja ($f(x)$):** Representa la función de densidad marginal $f_X(x)$, mostrando cómo la probabilidad se concentra cerca del origen y decae rápidamente conforme $x$ aumenta.
- **Punto (0,0):** Marca el inicio del dominio de definición de las variables.