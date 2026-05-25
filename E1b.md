Este es el desarrollo detallado y pedagógico para resolver el primer ejercicio del **Segundo Examen Parcial** de la materia, utilizando como base los procedimientos establecidos en los manuales y formularios de referencia.

---

### 📝 Enunciado del Ejercicio 1

Sean las variables aleatorias $X$ y $Y$ cuya función de densidad de distribución conjunta está dada por:

$$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 2; \quad x \le y \le 4-x \ 0 & \text{en otro caso} \end{cases}$$

**Se pide:**

- **a)** Determinar el valor de la constante $k$.
- **b)** Hallar las funciones de densidad marginales $f_X(x)$ y $f_Y(y)$.
- **c)** Determinar si $X$ y $Y$ son estadísticamente independientes.
- **d)** Hallar la probabilidad $P(Y \le x)$.

---

### 🟢 a) Determinación del valor de $k$

#### 1. Identificación de datos y concepto

Para que una función sea una densidad de probabilidad (PDF) válida, el volumen total bajo la superficie de la función sobre toda su región de soporte debe ser igual a **1**.

#### 2. Planteamiento de la fórmula

La propiedad de normalización establece que: $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy , dx = 1$$

#### 3. Sustitución de límites y desarrollo algebraico

La región de soporte es un triángulo definido por $0 \le x \le 2$ y la variable $y$ limitada inferiormente por $y = x$ y superiormente por $y = 4 - x$.

**Paso 3.1: Integración interna (respecto a $y$)** Mantenemos $x$ como constante: $$\int_{x}^{4-x} kx , dy = kx \int_{x}^{4-x} dy = kx [y]_x^{4-x}$$ Sustituimos los límites de integración: $$kx [ (4 - x) - (x) ] = kx (4 - 2x) = 4kx - 2kx^2$$

**Paso 3.2: Integración externa (respecto a $x$)** Integramos el resultado anterior en el rango de $x$ (de $0$ a $2$): $$\int_{0}^{2} (4kx - 2kx^2) , dx = k \int_{0}^{2} (4x - 2x^2) , dx$$ Aplicamos la regla de integración de potencias ($\int x^n dx = \frac{x^{n+1}}{n+1}$): $$k \left[ \frac{4x^2}{2} - \frac{2x^3}{3} \right]_0^2 = k \left[ 2x^2 - \frac{2}{3}x^3 \right]_0^2$$ Sustituimos el límite superior $x = 2$ y restamos el límite inferior $x = 0$: $$k \left( 2(2)^2 - \frac{2}{3}(2)^3 \right) - 0 = k \left( 8 - \frac{16}{3} \right)$$ Realizamos la operación fraccionaria ($8 = \frac{24}{3}$): $$k \left( \frac{24 - 16}{3} \right) = \frac{8k}{3}$$

#### 4. Resultado final de $k$

Igualamos a 1 para cumplir la propiedad de normalización: $$\frac{8k}{3} = 1 \implies \mathbf{k = \frac{3}{8} = 0.375}$$

---

### 🔵 b) Funciones de densidad marginales

#### 1. Densidad marginal de $X$ ($f_X(x)$)

**Fórmula aplicada:** Integrar la conjunta respecto a $y$ sobre su rango de soporte. $$f_X(x) = \int_{x}^{4-x} \frac{3}{8}x , dy$$ Aprovechando el cálculo realizado en el inciso anterior: $$f_X(x) = \frac{3}{8}x(4 - 2x) = \frac{3}{8}x \cdot 2(2 - x)$$ $$\mathbf{f_X(x) = \frac{3}{4}x(2 - x), \quad \text{para } 0 \le x \le 2}$$

#### 2. Densidad marginal de $Y$ ($f_Y(y)$)

**Análisis del dominio:** Para integrar respecto a $x$, debemos observar el triángulo desde el eje $Y$. Los vértices son $(0,0)$, $(2,2)$ y $(0,4)$. El rango de $y$ es de $0$ a $4$. Debemos dividir la integral porque la frontera derecha de $x$ cambia en $y = 2$:

- **Caso 1: $0 \le y \le 2$** (Límite superior de $x$ es la recta $y = x \implies x = y$): $$f_Y(y) = \int_{0}^{y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^y = \frac{3}{16}y^2$$
- **Caso 2: $2 \le y \le 4$** (Límite superior de $x$ es la recta $y = 4 - x \implies x = 4 - y$): $$f_Y(y) = \int_{0}^{4-y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^{4-y} = \frac{3}{16}(4 - y)^2$$

**Resultado final marginal de $Y$:** $$\mathbf{f_Y(y) = \begin{cases} \frac{3}{16}y^2 & \text{si } 0 \le y \le 2 \ \frac{3}{16}(4-y)^2 & \text{si } 2 \le y \le 4 \ 0 & \text{en otro caso} \end{cases}}$$

---

### 🟡 c) Verificación de independencia estadística

#### 1. Concepto y fórmula

Dos variables son independientes si y solo si la densidad conjunta es igual al producto de sus densidades marginales para todo el dominio: $$f_{X,Y}(x,y) \stackrel{?}{=} f_X(x) \cdot f_Y(y)$$

#### 2. Sustitución de valores (Prueba de punto)

Tomamos un punto dentro del soporte, por ejemplo $x = 1, y = 1$:

- **PDF Conjunta:** $f_{X,Y}(1,1) = \frac{3}{8}(1) = 0.375$.
- **Marginal de $X$:** $f_X(1) = \frac{3}{4}(1)(2-1) = 0.75$.
- **Marginal de $Y$:** $f_Y(1) = \frac{3}{16}(1)^2 = 0.1875$.

Calculamos el producto: $0.75 \times 0.1875 = \mathbf{0.140625}$.

#### 3. Conclusión

Como $0.375 \neq 0.140625$, **$X$ y $Y$ no son independientes**. Además, el dominio es un triángulo donde los límites de una variable dependen de la otra, lo cual es condición suficiente de dependencia.

---

### 🟠 d) Hallar la probabilidad $P(Y \le x)$

#### 1. Razonamiento sobre el dominio

El soporte de la función conjunta está definido por la desigualdad $x \le y \le 4-x$. Esto implica que para cualquier punto donde la probabilidad sea distinta de cero, se cumple siempre que **$y \ge x$**.

#### 2. Cálculo

El evento ${Y \le x}$ pide la probabilidad de estar **debajo** de la recta $y = x$. Dado que la región de soporte comienza **en** la recta $y = x$ y se extiende hacia arriba ($y \ge x$), el área de intersección entre el evento y el soporte es simplemente la línea $y = x$. En variables aleatorias continuas, la probabilidad de un evento que ocurre sobre una línea (un conjunto de medida cero en un plano) es **0**.

**Resultado:** $$\mathbf{P(Y \le x) = 0}$$

---

### 📊 Gráfica en Desmos (Código para Obsidian)

A continuación se presenta el bloque de código para visualizar la región de probabilidad y las curvas de las densidades marginales.

```
left=-0.5; right=4.5;
bottom=-0.5; top=2.5;
---
f(x) = (3/4)*x*(2-x) | {0<=x<=2} | RED | label: f_X(x)
y >= x | {x >= 0} | {y <= 4-x} | #a5d8ff | label: Soporte (Triángulo)
y = x | BLUE | DASHED
y = 4-x | BLUE | DASHED
(0,0) | label: (0,0)
(2,2) | label: (2,2)
(0,4) | label: (0,4)
```

**Explicación de la gráfica:**

- **Área sombreada azul (#a5d8ff):** Representa el soporte triangular de la distribución conjunta en el primer cuadrante.
- **Línea Roja ($f(x)$):** Representa la función de densidad marginal de $X$, mostrando que la mayor concentración de probabilidad para $X$ ocurre en $x=1$ (el punto máximo de la parábola).
- **Líneas Azules punteadas:** Son las fronteras $y=x$ y $y=4-x$ que delimitan la región donde la PDF es distinta de cero. Note que el evento $P(Y \le x)$ está fuera (abajo) de esta región sombreada. Agradecimiento a las fuentes.