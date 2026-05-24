Basándose en el documento **"Práctica 2 de Variables Aleatorias Continuas Múltiples"**, a continuación se presenta el enunciado oficial del **Ejercicio 1** y su resolución siguiendo los pasos metodológicos del formulario de la materia.

### Enunciado del Ejercicio 1 (Fuente: Práctica Nº2)

Encontrar el valor de $k$ en la siguiente función $f_{X,Y}(x,y)$ y también la función de distribución marginal de $X$: $$f_{X,Y}(x,y) = \begin{cases} \frac{k}{(1+x+y)^4} & \text{si } 0 \le x \le \infty; 0 \le y \le \infty \ 0 & \text{en otro caso} \end{cases}$$

---

### Resolución

Para resolver este ejercicio, aplicamos las propiedades de las funciones de densidad conjunta y marginal detalladas en las fuentes.

#### 1. Determinar el valor de $k$

Para que $f_{X,Y}(x,y)$ sea una función de densidad válida, la integral doble sobre todo su rango debe ser igual a 1: $$\int_{0}^{\infty} \int_{0}^{\infty} \frac{k}{(1+x+y)^4} , dy , dx = 1$$

- **Integración respecto a $y$:** Mantenemos $x$ constante e integramos: $$\int_{0}^{\infty} k(1+x+y)^{-4} , dy = \left[ \frac{k(1+x+y)^{-3}}{-3} \right]_{0}^{\infty}$$ Evaluando en los límites: $0 - \left( -\frac{k}{3(1+x)^3} \right) = \frac{k}{3(1+x)^3}$.
    
- **Integración respecto a $x$:** Ahora integramos el resultado anterior: $$\int_{0}^{\infty} \frac{k}{3}(1+x)^{-3} , dx = \left[ \frac{k}{3} \cdot \frac{(1+x)^{-2}}{-2} \right]_{0}^{\infty} = \left[ -\frac{k}{6(1+x)^2} \right]_{0}^{\infty}$$ Evaluando: $0 - \left( -\frac{k}{6(1)^2} \right) = \frac{k}{6}$.
    
- **Cálculo final de $k$:** Igualamos a 1 para normalizar la probabilidad: $$\frac{k}{6} = 1 \implies \mathbf{k = 6}$$
    

#### 2. Función de densidad marginal de $X$ ($f_X(x)$)

La densidad marginal de $X$ se obtiene integrando la función conjunta respecto a $y$ sobre todo su rango: $$f_X(x) = \int_{0}^{\infty} \frac{6}{(1+x+y)^4} , dy$$ Utilizando el resultado de la integral interna anterior con $k=6$: $$f_X(x) = \frac{6}{3(1+x)^3} = \mathbf{\frac{2}{(1+x)^3}, \quad \text{para } x \ge 0}$$

---

### Gráfica en Desmos

La región de probabilidad es el **primer cuadrante** ($x \ge 0, y \ge 0$). Se incluye también la curva de la densidad marginal $f_X(x)$.

```desmos-graph
left=-0.5; right=5; bottom=-0.5; top=5;
width=500; height=500;
---
x>=0|y>=0|#a5d8ff
f(x)=\frac{2}{(1+x)^3}|RED|0<=x<=5
(0,0)|label:(0,0)|BLACK
```

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el dominio del primer cuadrante donde la función de densidad es distinta de cero ($0 \le x \le \infty$ y $0 \le y \le \infty$).
- **Línea Roja ($f(x)$):** Representa la función de densidad marginal calculada, $f_X(x) = \frac{2}{(1+x)^3}$, que muestra cómo decae la probabilidad a medida que $x$ aumenta.
- **Punto (0,0):** Indica el origen de la región de soporte de las variables aleatorias.



```desmos-graph
left=-0.5; right=5; bottom=-0.5; top=5;
width=500; height=500;
---
y>0|x>0|#a5d8ff
f(x)=\frac{2}{(1+x)^3}|RED|0<=x<=5
(0,0)|label:(0,0)|BLACK
```


```desmos-graph
left=-0.5; right=5;
bottom=-0.1; top=2.2;
width=500; height=400;
---
y>0|x>0|#a5d8ff
f(x)=\frac{2}{(1+x)^3}|RED|0<=x<=5
(0,0)|label:(0,0)|BLACK
```