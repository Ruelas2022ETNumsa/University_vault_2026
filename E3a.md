*   **E3.** Determinar si las variables aleatorias $X, Y$ cuya densidad 
    de distribución conjunta:
    $$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; 0 \le y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Son estadísticamente independientes.
    **b)** Calcular la varianza de $X+Y$.

Para resolver el ejercicio **E3** de la **Práctica 2**, seguiremos los procedimientos para verificar la independencia y calcular la varianza de una suma de variables aleatorias detallados en las fuentes.

### Resolución Paso a Paso

La función de densidad conjunta es: $$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

#### a) Determinación de la Independencia Estadística

Para que $X$ e $Y$ sean independientes, debe cumplirse que $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ para todo su rango.

1. **Hallar la densidad marginal de $X$ ($f_X(x)$):** Integramos la función conjunta respecto a $y$ en su rango $$: $$f_X(x) = \int_{0}^{1} 4xy , dy = 4x \left[ \frac{y^2}{2} \right]_0^1 = 4x \left( \frac{1}{2} \right) = \mathbf{2x, \quad \text{para } 0 \le x \le 1}$$
    
2. **Hallar la densidad marginal de $Y$ ($f_Y(y)$):** Integramos la función conjunta respecto a $x$ en su rango $$: $$f_Y(y) = \int_{0}^{1} 4xy , dx = 4y \left[ \frac{x^2}{2} \right]_0^1 = 4y \left( \frac{1}{2} \right) = \mathbf{2y, \quad \text{para } 0 \le y \le 1}$$
    
3. **Verificar la condición de independencia:** Multiplicamos las marginales: $f_X(x) \cdot f_Y(y) = (2x) \cdot (2y) = 4xy$. Como el producto es igual a la función conjunta ($4xy = 4xy$), **las variables aleatorias $X$ e $Y$ son estadísticamente independientes**.
    

---

#### b) Calcular la varianza de $X+Y$

Como $X$ e $Y$ son independientes, la varianza de la suma es igual a la suma de las varianzas: $VAR[X+Y] = VAR[X] + VAR[Y]$.

1. **Calcular la varianza de $X$ ($VAR[X]$):**
    
    - **Esperanza $E[X]$:** $\int_0^1 x(2x) , dx = [ \frac{2x^3}{3} ]_0^1 = \frac{2}{3}$.
    - **Segundo momento $E[X^2]$:** $\int_0^1 x^2(2x) , dx = [ \frac{2x^4}{4} ]_0^1 = \frac{1}{2}$.
    - **Varianza $VAR[X]$:** $E[X^2] - (E[X])^2 = \frac{1}{2} - (\frac{2}{3})^2 = \frac{1}{2} - \frac{4}{9} = \mathbf{\frac{1}{18}}$.
2. **Calcular la varianza de $Y$ ($VAR[Y]$):** Dada la simetría de la función y del rango, el cálculo es idéntico al de $X$: **$VAR[Y] = \frac{1}{18}$**.
    
3. **Varianza de la suma:** $$VAR[X+Y] = \frac{1}{18} + \frac{1}{18} = \frac{2}{18} = \mathbf{\frac{1}{9} \approx 0.1111}$$
    

---

### Gráfica en Desmos

La región de soporte es un cuadrado unitario en el primer cuadrante. Se grafican también las funciones de densidad marginal.

```desmos-graph
width=500; height=500;
---
0<=x<=1{0<=y<=1}|#a5d8ff
x=1|BLUE|0<=y<=1
y=1|BLUE|0<=x<=1
f(x)=2x|RED|0<=x<=1
g(x)=2x|GREEN|0<=x<=1
```

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Soporte de la densidad conjunta ($0 \le x, y \le 1$).
- **Línea Roja ($f(x)$):** Función de densidad marginal de $X$, $f_X(x)=2x$.
- **Línea Verde ($g(x)$):** Función de densidad marginal de $Y$ (representada sobre el eje para visualización), $f_Y(y)=2y$.
- **Líneas Azules:** Límites de la región de probabilidad definida en el enunciado.