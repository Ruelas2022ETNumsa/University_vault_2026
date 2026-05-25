
---

### 📝 Enunciado del Ejercicio 1

Sean las variables aleatorias continuas $X$ e $Y$ cuya función de densidad de probabilidad (PDF) conjunta está definida por la siguiente expresión:

$$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 2; \quad x \le y \le 4-x \ 0 & \text{en otro caso} \end{cases}$$

**Se solicita desarrollar lo siguiente:**

- **a)** Determinar analíticamente el valor de la constante de normalización $k$.
- **b)** Obtener las funciones de densidad marginales $f_X(x)$ y $f_Y(y)$.
- **c)** Verificar si existe independencia estadística entre $X$ e $Y$.
- **d)** Calcular la probabilidad de que se cumpla el evento ${Y \le \sqrt{x}}$.

---

### 🟢 a) Determinación del valor de la constante $k$

#### 1. Identificación de datos y concepto técnico

Para que una función sea considerada una PDF válida, debe cumplir con la **propiedad de normalización**, que establece que el volumen total bajo la superficie de la función en su región de soporte debe ser igual a **1**.

#### 2. Planteamiento de la fórmula de integración

Planteamos la integral doble sobre la región de soporte: $$\int_{0}^{2} \int_{x}^{4-x} kx , dy , dx = 1$$

#### 3. Desarrollo algebraico paso a paso

**Paso 3.1: Integración interna (respecto a $y$)** Mantenemos $x$ como una constante y aplicamos la regla fundamental del cálculo: $$\int_{x}^{4-x} kx , dy = kx \int_{x}^{4-x} dy = kx [y]_x^{4-x}$$ Sustituimos los límites superior e inferior: $$kx [ (4 - x) - (x) ] = kx (4 - 2x) = 4kx - 2kx^2$$

**Paso 3.2: Integración externa (respecto a $x$)** Integramos el resultado anterior en el rango definido para $x$ (de $0$ a $2$): $$\int_{0}^{2} (4kx - 2kx^2) , dx = k \int_{0}^{2} (4x - 2x^2) , dx$$ Aplicamos la regla de integración de potencias ($\int x^n dx = \frac{x^{n+1}}{n+1}$): $$k \left[ \frac{4x^2}{2} - \frac{2x^3}{3} \right]_0^2 = k \left[ 2x^2 - \frac{2}{3}x^3 \right]_0^2$$ Evaluamos los límites: $$k \left( 2(2)^2 - \frac{2}{3}(2)^3 \right) - k(0) = k \left( 8 - \frac{16}{3} \right)$$ Realizamos la operación fraccionaria ($8 = \frac{24}{3}$): $$k \left( \frac{24 - 16}{3} \right) = \frac{8k}{3}$$

#### 4. Resultado final de $k$

Igualamos a la unidad para satisfacer la condición de normalización: $$\frac{8k}{3} = 1 \implies \mathbf{k = \frac{3}{8} = 0.375}$$

---

### 🔵 b) Funciones de densidad marginales

#### 1. Densidad marginal de $X$ ($f_X(x)$)

**Fórmula:** Se obtiene integrando la función conjunta respecto a $y$ sobre su rango de soporte. $$f_X(x) = \int_{x}^{4-x} \frac{3}{8}x , dy$$ Aprovechando el cálculo del inciso anterior: $$f_X(x) = \frac{3}{8}x(4 - 2x) = \frac{3}{8}x \cdot 2(2 - x)$$ $$\mathbf{f_X(x) = \frac{3}{4}x(2 - x), \quad \text{para } 0 \le x \le 2}$$

#### 2. Densidad marginal de $Y$ ($f_Y(y)$)

**Análisis del dominio:** La región de soporte es un triángulo con vértices en $(0,0)$, $(2,2)$ y $(0,4)$. El rango de $Y$ abarca desde $0$ hasta $4$. Debido a que la frontera derecha de $x$ cambia en $y = 2$, debemos dividir el cálculo:

- **Región 1 ($0 \le y \le 2$):** El límite superior de $x$ es la recta $y = x \implies x = y$. $$f_Y(y) = \int_{0}^{y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^y = \frac{3}{16}y^2$$
- **Región 2 ($2 \le y \le 4$):** El límite superior de $x$ es la recta $y = 4 - x \implies x = 4 - y$. $$f_Y(y) = \int_{0}^{4-y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^{4-y} = \frac{3}{16}(4 - y)^2$$

**Resultado final:** $$\mathbf{f_Y(y) = \begin{cases} \frac{3}{16}y^2 & \text{si } 0 \le y \le 2 \ \frac{3}{16}(4-y)^2 & \text{si } 2 \le y \le 4 \ 0 & \text{en otro caso} \end{cases}}$$

---

### 🟡 c) Determinación de independencia estadística

#### 1. Criterio técnico

Dos variables aleatorias son independientes si y solo si su PDF conjunta es igual al producto de sus PDFs marginales para todo punto en el plano: $$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

#### 2. Verificación por punto de prueba

Seleccionamos un punto dentro del soporte, por ejemplo $x = 1, y = 2$:

- **PDF Conjunta:** $f_{X,Y}(1,2) = \frac{3}{8}(1) = \mathbf{0.375}$.
- **Marginal de $X$:** $f_X(1) = \frac{3}{4}(1)(2-1) = 0.75$.
- **Marginal de $Y$:** $f_Y(2) = \frac{3}{16}(2)^2 = 0.75$.

Multiplicamos las marginales: $0.75 \times 0.75 = \mathbf{0.5625}$.

#### 3. Conclusión

Como $0.375 \neq 0.5625$, se concluye que **$X$ e $Y$ son estadísticamente dependientes**.

---

> [!check] c) Alternativo — Verificación algebraica (Formulario)
>
> El formulario establece que $X$ e $Y$ son independientes si y solo si $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ para **todo** $(x,y)$ en el soporte.
>
> **Paso 1 — Expresiones obtenidas en el inciso b):**
>
> $f_X(x) = \frac{3}{4}x(2-x), \quad 0 \le x \le 2$
>
> $f_Y(y) = \begin{cases} \dfrac{3}{16}y^2 & 0 \le y \le 2 \\ \dfrac{3}{16}(4-y)^2 & 2 \le y \le 4 \end{cases}$
>
> **Paso 2 — Calcular el producto $f_X(x) \cdot f_Y(y)$ en la región $0 \le y \le 2$:**
>
> $f_X(x) \cdot f_Y(y) = \frac{3}{4}x(2-x) \cdot \frac{3}{16}y^2 = \frac{9}{64}x(2-x)y^2$
>
> **Paso 3 — Comparar con la PDF conjunta:**
>
> $f_{X,Y}(x,y) = \frac{3}{8}x$
>
> El producto depende de $(2-x)$ e $y^2$, mientras que la conjunta solo depende de $x$. Son expresiones distintas para cualquier punto general del soporte.
>
> **Conclusión:** $f_{X,Y}(x,y) \neq f_X(x) \cdot f_Y(y)$ — $X$ e $Y$ son **estadísticamente dependientes**.

---

### 🟠 d) Probabilidad $P(Y \le \sqrt{x})$

#### 1. Análisis de límites e intersección

Debemos encontrar la región donde se intersectan el soporte original y la condición del evento.

- **Soporte:** $x \le y \le 4-x$.
- **Evento:** $y \le \sqrt{x}$.

Para que exista probabilidad no nula, debe cumplirse $x \le y \le \sqrt{x}$. Esta desigualdad es válida únicamente si $x \le \sqrt{x}$, lo cual ocurre en el intervalo **$0 \le x \le 1$**. En este rango, la curva $y = \sqrt{x}$ está por encima de la recta $y = x$.

#### 2. Planteamiento de la integral

$$P(Y \le \sqrt{x}) = \int_{0}^{1} \int_{x}^{\sqrt{x}} \frac{3}{8}x , dy , dx$$

#### 3. Desarrollo de la integración

**Paso 3.1: Integral interna** $$\int_{x}^{\sqrt{x}} \frac{3}{8}x , dy = \frac{3}{8}x [y]_x^{\sqrt{x}} = \frac{3}{8}x (\sqrt{x} - x) = \frac{3}{8}(x^{3/2} - x^2)$$

**Paso 3.2: Integral externa** $$\int_{0}^{1} \frac{3}{8}(x^{3/2} - x^2) , dx = \frac{3}{8} \left[ \frac{2}{5}x^{5/2} - \frac{x^3}{3} \right]_0^1$$ Sustituyendo el límite superior $x=1$: $$\frac{3}{8} \left( \frac{2}{5} - \frac{1}{3} \right) = \frac{3}{8} \left( \frac{6 - 5}{15} \right) = \frac{3}{8} \cdot \frac{1}{15}$$ $$\frac{3}{120} = \mathbf{\frac{1}{40} = 0.025}$$

**Resultado:** La probabilidad del evento es **0.025**.

---

### 📊 Gráfica en Desmos

Utiliza el siguiente bloque de código para visualizar la región de soporte y el área de integración del inciso d).

```desmos-graph
left=-0.5; right=4.5;
bottom=-0.5; top=4.5;
---
y>=x|x>=0|y<=4-x|#a5d8ff
y<=\sqrt{x}|y>=x|x>=0|x<=1|#ff7b7b
y=x|0<=x<=2|BLUE|DASHED
y=4-x|0<=x<=2|BLUE|DASHED
y=\sqrt{x}|0<=x<=1|PURPLE
(0,0)|label:(0,0)|BLACK
(2,2)|label:(2,2)|RED
(0,4)|label:(0,4)|BLUE
```

**Explicación de la gráfica:**

- **Área Azul (#a5d8ff):** Representa el soporte triangular de la distribución conjunta.
- **Área Roja (#ff7b7b):** Es la pequeña porción entre $(0,0)$ y $(1,1)$ donde se cumple que $y \le \sqrt{x}$ dentro del soporte. El volumen sobre esta área roja es lo que da como resultado $0.025$.
- **Línea Púrpura:** Es la función frontera $y = \sqrt{x}$ del evento solicitado.