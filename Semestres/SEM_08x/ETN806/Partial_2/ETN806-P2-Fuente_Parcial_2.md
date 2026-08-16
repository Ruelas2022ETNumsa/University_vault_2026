# 📋 FORMULARIO — PROCESOS ESTOCÁSTICOS

## Variables Aleatorias Continuas Múltiples

---

## 1. FUNCIÓN DE DENSIDAD DE PROBABILIDAD (1 variable)

### Propiedades

$$f(x) \geq 0$$

$$\int_{-\infty}^{\infty} f(x),dx = 1$$

### Probabilidad en un intervalo

$$P(a \leq X \leq b) = \int_{a}^{b} f(x),dx$$

> **Nota:** En variables continuas $P(X = a) = 0$

---

## 2. ESPERANZA MATEMÁTICA (1 variable)

$$E[X] = \mu_X = \int_{-\infty}^{\infty} x, f(x),dx$$

---

## 3. VARIANZA (1 variable)

$$VAR[X] = \int_{-\infty}^{\infty}(x - \mu_X)^2, f(x),dx$$

### Fórmula alternativa (más práctica)

$$VAR[X] = E[X^2] - \mu_X^2$$

donde: $$E[X^2] = \int_{-\infty}^{\infty} x^2, f(x),dx$$

---

## 4. DESVIACIÓN ESTÁNDAR (1 variable)

$$\sigma = \sqrt{VAR[X]}$$

---

## 5. FUNCIÓN DE DENSIDAD CONJUNTA (2 variables)

### Propiedades

$$f_{X,Y}(x,y) \geq 0$$

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y),dx,dy = 1$$

### Probabilidad en una región $R$

$$P\big((X,Y) \in R\big) = \iint_{R} f_{X,Y}(x,y),dx,dy$$

### Relación con la distribución acumulativa conjunta

$$f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}(x,y)}{\partial x,\partial y}$$

---

## 6. FUNCIÓN DE DISTRIBUCIÓN ACUMULATIVA CONJUNTA

$$F_{X,Y}(x,y) = P{X \leq x,; Y \leq y} = \int_{-\infty}^{x}\int_{-\infty}^{y} f_{X,Y}(u,v),dv,du$$

### Propiedades

| Propiedad          | Expresión                                     |
| ------------------ | --------------------------------------------- |
| Rango              | $0 \leq F_{X,Y}(x,y) \leq 1$                  |
| Marginal de X      | $F_X(x) = F_{X,Y}(x,\infty)$                  |
| Marginal de Y      | $F_Y(y) = F_{X,Y}(\infty,y)$                  |
| Límites inferiores | $F_{X,Y}(-\infty,y) = F_{X,Y}(x,-\infty) = 0$ |
| Límite superior    | $F_{X,Y}(\infty,\infty) = 1$                  |

---

## 7. DENSIDAD DE DISTRIBUCIÓN MARGINAL

$$\boxed{f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y),dy}$$

$$\boxed{f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y),dx}$$

---

## 8. INDEPENDENCIA ESTADÍSTICA

$X$ e $Y$ son **estadísticamente independientes** si y solo si:

$$\boxed{f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)}$$

> **Procedimiento:** Calcular $f_X(x)$ y $f_Y(y)$ por separado, multiplicarlas y verificar si el resultado es igual a $f_{X,Y}(x,y)$.

---

## 9. VALOR ESPERADO (2 variables)

Para $W = g(X,Y)$:

$$E[W] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} g(X,Y), f_{X,Y}(x,y),dy,dx$$

### Linealidad de la esperanza

$$E[X + Y] = E[X] + E[Y]$$

---

## 10. VARIANZA Y COVARIANZA EN SUMA

### Varianza de la suma

$$VAR[X+Y] = VAR[X] + VAR[Y] + 2,E!\left[(X-\mu_X)(Y-\mu_Y)\right]$$

> Si $X$ e $Y$ son **independientes**: $;VAR[X+Y] = VAR[X] + VAR[Y]$

### Covarianza

$$COV[X,Y] = E!\left[(X - \mu_X)(Y - \mu_Y)\right]$$

### Fórmula alternativa (más práctica)

$$\boxed{COV[X,Y] = E[XY] - \mu_X,\mu_Y}$$

donde: $$E[XY] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} x,y; f_{X,Y}(x,y),dy,dx$$

---

## 11. COEFICIENTE DE CORRELACIÓN

$$\boxed{\rho_{X,Y} = \frac{COV[X,Y]}{\sqrt{VAR[X]\cdot VAR[Y]}}}$$

$$-1 \leq \rho_{X,Y} \leq 1$$

|Valor de $\rho$|Interpretación|
|---|---|
|$\rho = 1$|Correlación positiva perfecta|
|$\rho = -1$|Correlación negativa perfecta|
|$\rho = 0$|No correlacionadas (si independientes)|

---

## 12. DENSIDAD DE DISTRIBUCIÓN CONDICIONAL

### Dado un evento $B$ con $P[B] > 0$

$$\boxed{f_{X,Y/B}(x,y) = \frac{f_{X,Y}(x,y)}{P[B]}, \quad (x,y) \in B}$$

$$f_{X,Y/B}(x,y) = 0, \quad \text{en otro caso}$$

### Dado la observación de otra variable

$$f_{X/Y}!\left(\frac{x}{y}\right) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$

$$f_{Y/X}!\left(\frac{y}{x}\right) = \frac{f_{X,Y}(x,y)}{f_X(x)}$$

### Regla de la cadena (de ambas expresiones)

$$f_{X,Y}(x,y) = f_{X/Y}!\left(\frac{x}{y}\right) f_Y(y) = f_{Y/X}!\left(\frac{y}{x}\right) f_X(x)$$

---

## 13. RESUMEN — PASOS PARA RESOLVER EJERCICIOS

### Para hallar $k$

1. Plantear $\displaystyle\int!!\int f_{X,Y}(x,y),dx,dy = 1$
2. Integrar con los límites dados y despejar $k$

### Para hallar densidades marginales

1. $f_X(x)$: integrar $f_{X,Y}$ respecto a $y$ en su rango
2. $f_Y(y)$: integrar $f_{X,Y}$ respecto a $x$ en su rango

### Para verificar independencia

1. Calcular $f_X(x)$ y $f_Y(y)$
2. Verificar si $f_{X,Y}(x,y) \stackrel{?}{=} f_X(x)\cdot f_Y(y)$

### Para calcular $VAR[X+Y]$

1. Hallar $\mu_X = E[X]$ y $\mu_Y = E[Y]$
2. Hallar $E[X^2]$ y $E[Y^2]$
3. Calcular $VAR[X] = E[X^2] - \mu_X^2$ y $VAR[Y] = E[Y^2] - \mu_Y^2$
4. Calcular $COV[X,Y] = E[XY] - \mu_X\mu_Y$
5. Aplicar $VAR[X+Y] = VAR[X] + VAR[Y] + 2,COV[X,Y]$

### Para densidad condicional dado evento $B$

1. Calcular $P[B] = \displaystyle\iint_B f_{X,Y}(x,y),dx,dy$
2. Aplicar $f_{X,Y/B}(x,y) = \dfrac{f_{X,Y}(x,y)}{P[B]}$ para $(x,y)\in B$

---
---

# 📝 Enunciado del Ejercicio 1 (parcial)

>temas: [normalizacion-k, densidad-marginal, independencia-estadistica, probabilidad-region-curva]

Sean las variables aleatorias continuas $X$ e $Y$ cuya función de densidad de probabilidad (PDF) conjunta está definida por la siguiente expresión:

$$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 2; \quad x \le y \le 4-x \ 0 & \text{en otro caso} \end{cases}$$

**Se solicita desarrollar lo siguiente:**

- **a)** Determinar analíticamente el valor de la constante de normalización $k$.
- **b)** Obtener las funciones de densidad marginales $f_X(x)$ y $f_Y(y)$.
- **c)** Verificar si existe independencia estadística entre $X$ e $Y$.
- **d)** Calcular la probabilidad de que se cumpla el evento ${Y \le \sqrt{x}}$.

---

## 🟢 a) Determinación del valor de la constante $k$

### 1. Identificación de datos y concepto técnico

Para que una función sea considerada una PDF válida, debe cumplir con la **propiedad de normalización**, que establece que el volumen total bajo la superficie de la función en su región de soporte debe ser igual a **1**.

### 2. Planteamiento de la fórmula de integración

Planteamos la integral doble sobre la región de soporte: $$\int_{0}^{2} \int_{x}^{4-x} kx , dy , dx = 1$$

### 3. Desarrollo algebraico paso a paso

**Paso 3.1: Integración interna (respecto a $y$)** Mantenemos $x$ como una constante y aplicamos la regla fundamental del cálculo: $$\int_{x}^{4-x} kx , dy = kx \int_{x}^{4-x} dy = kx [y]_x^{4-x}$$ Sustituimos los límites superior e inferior: $$kx [ (4 - x) - (x) ] = kx (4 - 2x) = 4kx - 2kx^2$$

**Paso 3.2: Integración externa (respecto a $x$)** Integramos el resultado anterior en el rango definido para $x$ (de $0$ a $2$): $$\int_{0}^{2} (4kx - 2kx^2) , dx = k \int_{0}^{2} (4x - 2x^2) , dx$$ Aplicamos la regla de integración de potencias ($\int x^n dx = \frac{x^{n+1}}{n+1}$): $$k \left[ \frac{4x^2}{2} - \frac{2x^3}{3} \right]_0^2 = k \left[ 2x^2 - \frac{2}{3}x^3 \right]_0^2$$ Evaluamos los límites: $$k \left( 2(2)^2 - \frac{2}{3}(2)^3 \right) - k(0) = k \left( 8 - \frac{16}{3} \right)$$ Realizamos la operación fraccionaria ($8 = \frac{24}{3}$): $$k \left( \frac{24 - 16}{3} \right) = \frac{8k}{3}$$

### 4. Resultado final de $k$

Igualamos a la unidad para satisfacer la condición de normalización: $$\frac{8k}{3} = 1 \implies \mathbf{k = \frac{3}{8} = 0.375}$$

---

## 🔵 b) Funciones de densidad marginales

### 1. Densidad marginal de $X$ ($f_X(x)$)

**Fórmula:** Se obtiene integrando la función conjunta respecto a $y$ sobre su rango de soporte. $$f_X(x) = \int_{x}^{4-x} \frac{3}{8}x , dy$$ Aprovechando el cálculo del inciso anterior: $$f_X(x) = \frac{3}{8}x(4 - 2x) = \frac{3}{8}x \cdot 2(2 - x)$$ $$\mathbf{f_X(x) = \frac{3}{4}x(2 - x), \quad \text{para } 0 \le x \le 2}$$

### 2. Densidad marginal de $Y$ ($f_Y(y)$)

**Análisis del dominio:** La región de soporte es un triángulo con vértices en $(0,0)$, $(2,2)$ y $(0,4)$. El rango de $Y$ abarca desde $0$ hasta $4$. Debido a que la frontera derecha de $x$ cambia en $y = 2$, debemos dividir el cálculo:

- **Región 1 ($0 \le y \le 2$):** El límite superior de $x$ es la recta $y = x \implies x = y$. $$f_Y(y) = \int_{0}^{y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^y = \frac{3}{16}y^2$$
- **Región 2 ($2 \le y \le 4$):** El límite superior de $x$ es la recta $y = 4 - x \implies x = 4 - y$. $$f_Y(y) = \int_{0}^{4-y} \frac{3}{8}x , dx = \frac{3}{8} \left[ \frac{x^2}{2} \right]_0^{4-y} = \frac{3}{16}(4 - y)^2$$

**Resultado final:** $$\mathbf{f_Y(y) = \begin{cases} \frac{3}{16}y^2 & \text{si } 0 \le y \le 2 \ \frac{3}{16}(4-y)^2 & \text{si } 2 \le y \le 4 \ 0 & \text{en otro caso} \end{cases}}$$

---

## 🟡 c) Determinación de independencia estadística (Formulario)

 El formulario establece que $X$ e $Y$ son independientes si y solo si $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ para **todo** $(x,y)$ en el soporte.

 **Paso 1 — Expresiones obtenidas en el inciso b):**

 $f_X(x) = \frac{3}{4}x(2-x), \quad 0 \le x \le 2$

 $f_Y(y) = \begin{cases} \dfrac{3}{16}y^2 & 0 \le y \le 2 \\ \dfrac{3}{16}(4-y)^2 & 2 \le y \le 4 \end{cases}$

 **Paso 2 — Calcular el producto $f_X(x) \cdot f_Y(y)$ en la región $0 \le y \le 2$:**

 $f_X(x) \cdot f_Y(y) = \frac{3}{4}x(2-x) \cdot \frac{3}{16}y^2 = \frac{9}{64}x(2-x)y^2$

 **Paso 3 — Comparar con la PDF conjunta:**

 $f_{X,Y}(x,y) = \frac{3}{8}x$

 El producto depende de $(2-x)$ e $y^2$, mientras que la conjunta solo depende de $x$. Son expresiones distintas para cualquier punto general del soporte.

> **Conclusión:** $f_{X,Y}(x,y) \neq f_X(x) \cdot f_Y(y)$ — $X$ e $Y$ son **estadísticamente dependientes**.

---

## 🟠 d) Probabilidad $P(Y \le \sqrt{x})$

### 1. Análisis de límites e intersección

Debemos encontrar la región donde se intersectan el soporte original y la condición del evento.

- **Soporte:** $x \le y \le 4-x$.
- **Evento:** $y \le \sqrt{x}$.

Para que exista probabilidad no nula, debe cumplirse $x \le y \le \sqrt{x}$. Esta desigualdad es válida únicamente si $x \le \sqrt{x}$, lo cual ocurre en el intervalo **$0 \le x \le 1$**. En este rango, la curva $y = \sqrt{x}$ está por encima de la recta $y = x$.

### 2. Planteamiento de la integral

$$P(Y \le \sqrt{x}) = \int_{0}^{1} \int_{x}^{\sqrt{x}} \frac{3}{8}x , dy , dx$$

### 3. Desarrollo de la integración

**Paso 3.1: Integral interna** $$\int_{x}^{\sqrt{x}} \frac{3}{8}x , dy = \frac{3}{8}x [y]_x^{\sqrt{x}} = \frac{3}{8}x (\sqrt{x} - x) = \frac{3}{8}(x^{3/2} - x^2)$$

**Paso 3.2: Integral externa** $$\int_{0}^{1} \frac{3}{8}(x^{3/2} - x^2) , dx = \frac{3}{8} \left[ \frac{2}{5}x^{5/2} - \frac{x^3}{3} \right]_0^1$$ Sustituyendo el límite superior $x=1$: $$\frac{3}{8} \left( \frac{2}{5} - \frac{1}{3} \right) = \frac{3}{8} \left( \frac{6 - 5}{15} \right) = \frac{3}{8} \cdot \frac{1}{15}$$ $$\frac{3}{120} = \mathbf{\frac{1}{40} = 0.025}$$

**Resultado:** La probabilidad del evento es **0.025**.

---

## 📊 Gráfica en Desmos

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


---
---

# 📝 Enunciado del Ejercicio 2 (parcial)

>temas: [independencia-estadistica, varianza-suma, densidad-marginal, dominio-rectangular]

Determinar si las variables aleatorias $X$, $Y$ cuya densidad de distribución conjunta es:

$$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; \quad 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

**Se pide:**

- **a)** Determinar si son estadísticamente independientes.
- **b)** Calcular la varianza de $X + Y$.



Esta es la resolución detallada, paso a paso y pedagógica del segundo ejercicio del examen parcial, siguiendo los procedimientos técnicos establecidos para el análisis de variables aleatorias múltiples.

---

## 🟢 a) Determinación de la Independencia Estadística

### 1. Identificación de datos y concepto

Para verificar la **independencia estadística**, debemos comprobar si la función de densidad conjunta es igual al producto de sus funciones de densidad marginales para todo el dominio. La fórmula es: $$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

### 2. Cálculo de la función de densidad marginal de $X$ ($f_X(x)$)

La densidad marginal de una variable se obtiene integrando la función conjunta respecto a la otra variable sobre su rango de soporte.

- **Fórmula:** $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$
- **Sustitución de valores:** Para el rango $0 \le x \le 1$, integramos respecto a $y$ desde 0 hasta 1: $$f_X(x) = \int_{0}^{1} 4xy , dy$$
- **Desarrollo algebraico:** Extraemos $4x$ como constante fuera de la integral: $$f_X(x) = 4x \int_{0}^{1} y , dy$$ Aplicamos la regla de integración de potencias ($\int y^1 dy = \frac{y^2}{2}$): $$f_X(x) = 4x \left[ \frac{y^2}{2} \right]_0^1 = 4x \left( \frac{1^2}{2} - \frac{0^2}{2} \right) = 4x \left( \frac{1}{2} \right)$$
- **Resultado marginal X:** $\mathbf{f_X(x) = 2x, \quad \text{para } 0 \le x \le 1}$.

### 3. Cálculo de la función de densidad marginal de $Y$ ($f_Y(y)$)

Realizamos el mismo procedimiento, pero integrando respecto a $x$.

- **Fórmula:** $f_Y(y) = \int_{0}^{1} 4xy , dx$
- **Desarrollo:** $$f_Y(y) = 4y \int_{0}^{1} x , dx = 4y \left[ \frac{x^2}{2} \right]_0^1 = 4y \left( \frac{1}{2} \right)$$
- **Resultado marginal Y:** $\mathbf{f_Y(y) = 2y, \quad \text{para } 0 \le y \le 1}$.

### 4. Verificación de la condición de independencia

Multiplicamos las dos funciones marginales obtenidas: $$f_X(x) \cdot f_Y(y) = (2x) \cdot (2y) = \mathbf{4xy}$$ **Conclusión:** Dado que el producto de las marginales es idéntico a la función de densidad conjunta original ($4xy = 4xy$), se concluye que **las variables aleatorias $X$ e $Y$ son estadísticamente independientes**.

---

## 🔵 b) Cálculo de la varianza de $X + Y$

### 1. Identificación de la fórmula

La varianza de una suma de variables aleatorias se define generalmente como: $$VAR[X+Y] = VAR[X] + VAR[Y] + 2 \cdot COV[X,Y]$$ Sin embargo, dado que en el inciso anterior demostramos que $X$ e $Y$ son **independientes**, la covarianza es automáticamente **0** ($COV[X,Y] = 0$). Por lo tanto, la fórmula se simplifica a: $$VAR[X+Y] = VAR[X] + VAR[Y]$$

### 2. Cálculo de la varianza de $X$ ($VAR[X]$)

Utilizamos la fórmula práctica: $VAR[X] = E[X^2] - (E[X])^2$.

- **Esperanza $E[X]$:** $$E[X] = \int_{0}^{1} x \cdot f_X(x) , dx = \int_{0}^{1} x \cdot (2x) , dx = \int_{0}^{1} 2x^2 , dx$$ $$E[X] = \left[ \frac{2x^3}{3} \right]_0^1 = \mathbf{\frac{2}{3}}$$
- **Segundo momento $E[X^2]$:** $$E[X^2] = \int_{0}^{1} x^2 \cdot f_X(x) , dx = \int_{0}^{1} x^2 \cdot (2x) , dx = \int_{0}^{1} 2x^3 , dx$$ $$E[X^2] = \left[ \frac{2x^4}{4} \right]_0^1 = \frac{2}{4} = \mathbf{\frac{1}{2}}$$
- **Varianza de $X$:** $$VAR[X] = \frac{1}{2} - \left( \frac{2}{3} \right)^2 = \frac{1}{2} - \frac{4}{9} = \frac{9 - 8}{18} = \mathbf{\frac{1}{18}}$$.

### 3. Cálculo de la varianza de $Y$ ($VAR[Y]$)

Dada la simetría perfecta de la función conjunta y los límites de integración, el cálculo para $Y$ es idéntico al de $X$: $$VAR[Y] = \mathbf{\frac{1}{18}}$$.

### 4. Resultado final de la varianza de la suma

$$VAR[X+Y] = \frac{1}{18} + \frac{1}{18} = \frac{2}{18} = \mathbf{\frac{1}{9}}$$ En decimales, el resultado es aproximadamente **0.1111**.

---
---

# 📝 Enunciado del Ejercicio 3 (parcial)

>temas: [densidad-marginal, region-semicircular, limites-variables, distribucion-uniforme]

Las variables aleatorias $X, Y$ tienen la función de densidad de distribución de probabilidad conjunta que se indica:

$$f_{X,Y}(x,y) = \begin{cases} \frac{2}{\pi} & \text{si } x^2 + y^2 \le 1; \quad 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

Analice solo en los dos primeros cuadrantes.

**Se pide:**

- **a)** Encontrar la distribución marginal de $X$.
- **b)** Encontrar la distribución marginal de $Y$.

A continuación, se presenta la resolución detallada y pedagógica del ejercicio 3 del segundo parcial, siguiendo estrictamente el procedimiento técnico para el análisis de variables aleatorias continuas conjuntas.

---

## **1. Identificación de los datos del problema**

- **Función de densidad conjunta ($f_{X,Y}(x,y)$):** Es una constante $k = \frac{2}{\pi}$ dentro de una región específica. Esto indica una **distribución uniforme** sobre el área de soporte.
- **Región de soporte ($R$):** Definida por las inecuaciones:
    - $x^2 + y^2 \le 1$: El interior de un círculo unitario centrado en el origen.
    - $0 \le y \le 1$: La mitad superior del plano cartesiano.
- **Geometría:** La combinación de estas condiciones describe un **semicírculo unitario** situado en el semiplano superior (abarcando el primer y segundo cuadrante).
- **Límites de las variables:**
    - Para $y$: varía globalmente de $0$ a $1$.
    - Para $x$: varía globalmente de $-1$ a $1$.

---

## **2. Explicación de lo que se pide**

Se solicita encontrar las **funciones de densidad marginales** de las variables aleatorias $X$ e $Y$.

- La marginal de $X$ ($f_X(x)$) nos indica cómo se distribuye la probabilidad de $X$ individualmente, promediando (integrando) todos los posibles valores de $Y$ en cada punto $x$.
- La marginal de $Y$ ($f_Y(y)$) nos indica la distribución de probabilidad de $Y$ sola, integrando sobre todo el rango de $X$ para cada valor fijo de $y$.

---

## **3. Fórmulas utilizadas y justificación**

Según el **Formulario 806 II** y los textos de referencia:

1. **Densidad Marginal de $X$:** $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$$
2. **Densidad Marginal de $Y$:** $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx$$

**¿Por qué se usan estas fórmulas?** En variables continuas, la probabilidad conjunta se representa como un volumen bajo la superficie $f_{X,Y}(x,y)$. Para "proyectar" esta probabilidad sobre un solo eje (obtener la marginal), debemos acumular toda la masa de probabilidad existente en la dirección de la otra variable mediante una integral definida sobre la región de soporte.

---

## **4. Resolución Paso a Paso**

### **a) Encontrar la distribución marginal de $X$ ($f_X(x)$)**

**Paso 1: Identificar los límites de integración para $y$.** De la ecuación de la frontera $x^2 + y^2 = 1$, despejamos $y$: $$y^2 = 1 - x^2 \implies y = \pm \sqrt{1 - x^2}$$ Como el enunciado restringe $0 \le y \le 1$, el límite inferior de integración es $0$ y el límite superior es la semicircunferencia superior: $y = \sqrt{1 - x^2}$.

**Paso 2: Plantear y resolver la integral.** Holding $x$ fixed, $y$ ranges from $0$ to $\sqrt{1-x^2}$: $$f_X(x) = \int_{0}^{\sqrt{1 - x^2}} \frac{2}{\pi} , dy$$

**Paso 3: Realizar la integración.** $$f_X(x) = \frac{2}{\pi} \left[ y \right]_{0}^{\sqrt{1 - x^2}}$$ $$f_X(x) = \frac{2}{\pi} \left( \sqrt{1 - x^2} - 0 \right)$$

**Resultado final de $f_X(x)$:** $$f_X(x) = \begin{cases} \frac{2\sqrt{1 - x^2}}{\pi} & \text{si } -1 \le x \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

### **b) Encontrar la distribución marginal de $Y$ ($f_Y(y)$)**

**Paso 1: Identificar los límites de integración para $x$.** De la ecuación de la frontera $x^2 + y^2 = 1$, despejamos $x$: $$x^2 = 1 - y^2 \implies x = \pm \sqrt{1 - y^2}$$ Para un valor de $y$ fijo entre $0$ y $1$, la variable $x$ recorre el semicírculo desde el borde izquierdo (cuadrante II) hasta el derecho (cuadrante I). Por tanto, el límite inferior es $-\sqrt{1 - y^2}$ y el superior es $\sqrt{1 - y^2}$.

**Paso 2: Plantear y resolver la integral.** $$f_Y(y) = \int_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}} \frac{2}{\pi} , dx$$

**Paso 3: Realizar la integración.** $$f_Y(y) = \frac{2}{\pi} \left[ x \right]_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}}$$ $$f_Y(y) = \frac{2}{\pi} \left( \sqrt{1 - y^2} - (-\sqrt{1 - y^2}) \right)$$ $$f_Y(y) = \frac{2}{\pi} \left( 2\sqrt{1 - y^2} \right)$$

**Resultado final de $f_Y(y)$:** $$f_Y(y) = \begin{cases} \frac{4\sqrt{1 - y^2}}{\pi} & \text{si } 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

## **5. Verificación de los resultados**

Para que las marginales sean válidas, su integral sobre todo su dominio debe ser igual a 1.

- **Verificación para $f_X(x)$:** $\int_{-1}^{1} \frac{2}{\pi} \sqrt{1 - x^2} , dx$. Esta es la integral de una semicircunferencia multiplicada por una constante. Usando la sustitución trigonométrica $x = \sin\theta$: $\frac{2}{\pi} \int_{-\pi/2}^{\pi/2} \cos^2\theta , d\theta = \frac{2}{\pi} \left[ \frac{\theta}{2} + \frac{\sin 2\theta}{4} \right]_{-\pi/2}^{\pi/2} = \frac{2}{\pi} \left( \frac{\pi}{4} - (-\frac{\pi}{4}) \right) = \frac{2}{\pi} \cdot \frac{\pi}{2} = 1$. **Correcto.**
    
- **Verificación para $f_Y(y)$:** $\int_{0}^{1} \frac{4}{\pi} \sqrt{1 - y^2} , dy = \frac{4}{\pi} \left( \frac{\pi}{4} \right) = 1$. **Correcto.**
    

---

## **6. Gráfica en Desmos**

He generado el código para visualizar la región de soporte conjunta y las dos funciones marginales calculadas.

```desmos-graph
left=-1.5; right=1.5;
bottom=-0.5; top=1.5;
width=500; height=500;
---
x^2+y^2<=1|y>=0|#a5d8ff
f(x)=\frac{2\sqrt{1-x^2}}{\pi}|-1<=x<=1|RED
g(y)=\frac{4\sqrt{1-y^2}}{\pi}|0<=y<=1|GREEN
(0,0)|label:(0,0)|BLACK
(-1,0)|label:(-1,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

**Explicación de la gráfica:**

- **Área Azul:** Representa el soporte del semicírculo unitario definido en el enunciado.
- **Línea Roja ($f(x)$):** Representa la densidad marginal de $X$. Note que es máxima en el centro ($x=0$) porque es donde hay más "grosor" de semicírculo en el eje $y$, y cae hacia cero en los extremos $\pm 1$.
- **Línea Verde ($g(x)$):** Representa la forma de la densidad marginal de $Y$. Al ser un semicírculo, la mayor concentración de probabilidad para $Y$ está cerca de $y=0$ (la base es más ancha).

---
---

# **Enunciado del Ejercicio guia docente**

>temas: [normalizacion-k, densidad-marginal, independencia-estadistica, probabilidad-region-curva, probabilidad-complemento, densidad-condicional, esperanza, varianza]

Sean las variables aleatorias $X, Y$ con densidad de distribución conjunta: $$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 1; x \le y \le 2-x \\ 0 & \text{en otro caso} \end{cases}$$

---

## **a) Determinar el valor de $k$**

Para que sea una función de densidad válida, la integral doble sobre todo el rango debe ser igual a 1.

1. **Plantear la integral:** $\int_0^1 \int_x^{2-x} kx \, dy \, dx = 1$.
2. **Integrar respecto a $y$:** $$\int_0^1 kx [y]_x^{2-x} dx = \int_0^1 kx [(2-x) - x] dx = \int_0^1 kx (2-2x) dx = 2k \int_0^1 (x - x^2) dx$$
3. **Integrar respecto a $x$:** $$2k \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2k \left( \frac{1}{2} - \frac{1}{3} \right) = 2k \left( \frac{1}{6} \right) = \frac{k}{3}$$
4. **Despejar $k$:** $\frac{k}{3} = 1 \implies \mathbf{k = 3}$.

> **Gráfica — Región del dominio** (triángulo donde $f_{X,Y} \neq 0$):
> Vértices en $(0,0)$, $(1,1)$ y $(0,2)$. Frontera superior: $y=2-x$, frontera inferior: $y=x$, frontera izquierda: $x=0$.

```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=2-x|0<=x<=1|BLUE|SOLID
x=0|0<=y<=2|BLACK|DASHED
y<2-x|x>=0|y>x|x<=1|#a5d8ff
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(0,2)|label:(0,2)|BLUE
```

---

## **b) Funciones de densidad marginales**

Usamos las fórmulas para proyectar la densidad conjunta sobre cada eje.

- **Marginal de $X$ ($f_X(x)$):** $$f_X(x) = \int_x^{2-x} 3x \, dy = 3x [y]_x^{2-x} = 3x(2-2x) = \mathbf{6x(1-x), \quad 0 \le x \le 1}$$
- **Marginal de $Y$ ($f_Y(y)$):** La región es un triángulo con vértices en $(0,0)$, $(1,1)$ y $(0,2)$. Debemos dividir la integral:
    1. Si $0 \le y \le 1$, $x$ va de $0$ a $y$: $\int_0^y 3x \, dx = \frac{3}{2}y^2$.
    2. Si $1 \le y \le 2$, $x$ va de $0$ a $2-y$: $\int_0^{2-y} 3x \, dx = \frac{3}{2}(2-y)^2$.

$$\mathbf{f_Y(y) = \begin{cases} \frac{3}{2}y^2 & 0 \le y \le 1 \\ \frac{3}{2}(2-y)^2 & 1 \le y \le 2 \end{cases}}$$

> **Gráfica — Densidades marginales $f_X(x)$ y $f_Y(y)$:**

```desmos-graph
left=-0.2; right=2.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
g(y)=\frac{3}{2}y^2|0<=y<=1|RED|SOLID
h(y)=\frac{3}{2}(2-y)^2|1<=y<=2|RED|SOLID
```

---

## **c) Determinar si $X, Y$ son independientes**

Dos variables son independientes si $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$. Tomando un punto como $(0.5, 0.5)$:

- $f_{X,Y}(0.5, 0.5) = 3(0.5) = 1.5$.
- $f_X(0.5) \cdot f_Y(0.5) = [6(0.5)(1-0.5)] \cdot [\frac{3}{2}(0.5)^2] = 1.5 \cdot 0.375 = 0.5625$.

Como $1.5 \neq 0.5625$, concluye que **$X$ e $Y$ no son independientes**.

---

## **d) Probabilidad $P(Y \le \sqrt{x})$**

La región está acotada por $y=x$ (inferior) y $y=\sqrt{x}$ (superior) dentro del rango $0 \le x \le 1$:

$$P(Y \le \sqrt{x}) = \int_0^1 \int_x^{\sqrt{x}} 3x \, dy \, dx = \int_0^1 3x(\sqrt{x} - x) \, dx = \int_0^1 (3x^{3/2} - 3x^2) \, dx$$

$$= \left[ \frac{6}{5}x^{5/2} - x^3 \right]_0^1 = \frac{6}{5} - 1 = \mathbf{\frac{1}{5} = 0.2}$$

> **Gráfica — Región de integración inciso d):**
> Área sombreada entre $y=x$ (rojo) y $y=\sqrt{x}$ (verde) para $0 \le x \le 1$.

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=\sqrt{x}|0<=x<=1|GREEN|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|BLACK
```

---

## **e) Probabilidad $P(Y \le 2x)$**

Usamos el complemento: $P(Y \le 2x) = 1 - P(Y > 2x)$. El área donde $y > 2x$ ocurre de $x=0$ hasta el cruce de $y=2x$ con $y=2-x$ (en $x=2/3$).

1. $P(Y > 2x) = \int_0^{2/3} \int_{2x}^{2-x} 3x \, dy \, dx = \int_0^{2/3} 3x(2-3x) \, dx = \int_0^{2/3} (6x-9x^2) \, dx$
2. $[3x^2 - 3x^3]_0^{2/3} = 3\left(\frac{4}{9}\right) - 3\left(\frac{8}{27}\right) = \frac{4}{3} - \frac{8}{9} = \frac{4}{9}$.
3. $P(Y \le 2x) = 1 - \frac{4}{9} = \mathbf{\frac{5}{9}}$.

> **Gráfica — Región donde $y > 2x$ dentro del dominio** (complemento usado):
> Área sombreada en naranja es la región $y > 2x$, acotada por $y=2-x$ arriba y $y=2x$ abajo, hasta $x=2/3$.

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=2.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|DASHED
y=2-x|0<=x<=1|BLUE|SOLID
y=2x|0<=x<=1|ORANGE|SOLID
y<2-x|y>2x|x>=0|x<=0.667|#ffd8a8
(0.667,1.333)|label:(2/3, 4/3)|ORANGE
(1,1)|label:(1,1)|RED
(0,2)|label:(0,2)|BLUE
```

---

## **f) Probabilidad $P(Y \le 3x \mid Y \ge 2x)$**

Por definición de probabilidad condicional: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

1. $P(B) = P(Y \ge 2x) = 4/9$ (calculado en el inciso anterior).
2. $P(A \cap B) = P(2x \le Y \le 3x)$. Esta región se divide en $x \in [0, 1/2]$ y $x \in [1/2, 2/3]$ debido a las rectas de frontera.
3. La integral resulta en $7/36$.
4. Resultado: $\frac{7/36}{4/9} = \mathbf{\frac{7}{16} = 0.4375}$.

> **Gráfica — Región $2x \le y \le 3x$ dentro del dominio:**
> Área sombreada en morado es donde $2x \le y \le 3x$, acotada también por el dominio del triángulo.

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=2.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|DASHED
y=2-x|0<=x<=1|BLUE|SOLID
y=2x|0<=x<=0.667|ORANGE|SOLID
y=3x|0<=x<=0.5|PURPLE|SOLID
y<3x|y>2x|0<=x<=0.5|#d0bfff
y<2-x|y>2x|0.5<=x<=0.667|#d0bfff
(0,0)|label:(0,0)|BLACK
(0.5,1)|label:(1/2, 1)|PURPLE
(0.667,1.333)|label:(2/3, 4/3)|ORANGE
```

---

## **g) Hallar $E[X]$ y $VAR[X]$**

Usamos la densidad marginal $f_X(x) = 6x - 6x^2$ y las fórmulas del formulario:

- **Esperanza:** $E[X] = \int_0^1 x(6x - 6x^2) \, dx = \int_0^1 (6x^2 - 6x^3) \, dx = [2x^3 - 1.5x^4]_0^1 = \mathbf{0.5}$.
- **Segundo momento:** $E[X^2] = \int_0^1 x^2(6x - 6x^2) \, dx = \int_0^1 (6x^3 - 6x^4) \, dx = [1.5x^4 - 1.2x^5]_0^1 = 0.3$.
- **Varianza:** $VAR[X] = E[X^2] - (E[X])^2 = 0.3 - (0.5)^2 = \mathbf{0.05}$.

> **Gráfica — $f_X(x)$ con media $\mu_X = 0.5$ marcada:**

```desmos-graph
left=-0.1; right=1.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
x=0.5|0<=y<=1.5|GREEN|DASHED
(0.5,0)|label:mu=0.5|GREEN
```


---
---

# Enunciado del Ejercicio 1 (practica)

>temas: [normalización-k, densidad-marginal, integral-impropia, dominio-no-acotado]

Encontrar el valor de $k$ en la siguiente función $f_{X,Y}(x,y)$ y también la función de distribución marginal de $X$:
    $$f_{X,Y}(x,y) = \begin{cases} \frac{k(1+x+y)}{(1+x)^4 (1+y)^4} & \text{si } 0 \le x \le \infty; 0 \le y \le \infty \\ 0 & \text{en otro caso} \end{cases}$$

Para resolver este ejercicio, seguiremos los pasos metodológicos establecidos en las fuentes para funciones de densidad de probabilidad (PDF) conjunta y marginal.
## 1. Determinar el valor de $k$

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

## 2. Función de densidad marginal de $X$

La densidad marginal $f_X(x)$ se obtiene integrando la función conjunta respecto a $y$ sobre todo su rango. Aprovechando el cálculo de la integral interna realizado anteriormente con $k = 4.5$:

$$f_X(x) = \frac{4.5}{(1+x)^4} \cdot \left( \frac{2x+3}{6} \right)$$ Simplificando la expresión: $\mathbf{f_X(x) = \frac{3(2x+3)}{4(1+x)^4}, \quad \text{para } x \ge 0}$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. La integral interna $\frac{2x+3}{6}$ reutilizada del inciso anterior es correcta, y la simplificación $\frac{9/2}{(1+x)^4}\cdot\frac{2x+3}{6} = \frac{3(2x+3)}{4(1+x)^4}$ es correcta.

---

## Gráfica en Desmos

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

---
---

# # Enunciado del Ejercicio 2 (practica)

>temas: [independencia-estadistica, densidad-marginal, dominio-triangular]

Determinar si las variables aleatorias $U$ y $V$ son estadísticamente independientes sabiendo que su función de densidad de distribución conjunta está dada por:
    $$f_{U,V}(u,v) = \begin{cases} 24uv & \text{si } u \ge 0; v \ge 0; u+v \le 1 \\ 0 & \text{en otro caso} \end{cases}$$

## Paso 1: Definir la función y su región de soporte

La función de densidad conjunta es: $$f_{U,V}(u,v) = \begin{cases} 24uv & \text{si } u \ge 0; v \ge 0; u+v \le 1 \ 0 & \text{en otro caso} \end{cases}$$ La región donde la probabilidad es distinta de cero es un **triángulo** en el primer cuadrante delimitado por la recta $v = 1 - u$.

## Paso 2: Calcular la función de densidad marginal de $U$ ($f_U(u)$)

Para hallar la marginal de $U$, integramos la función conjunta respecto a $v$ sobre su rango de definición ($0 \le v \le 1-u$): $$f_U(u) = \int_{0}^{1-u} 24uv , dv$$ $f_U(u) = 24u \left[ \frac{v^2}{2} \right]_0^{1-u} = 12u(1-u)^2, \quad \text{para } 0 \le u \le 1.$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

## Paso 3: Calcular la función de densidad marginal de $V$ ($f_V(v)$)

Dada la simetría de la función conjunta y de la región de soporte, el cálculo para $V$ es análogo integrando respecto a $u$ ($0 \le u \le 1-v$): $f_V(v) = \int_{0}^{1-v} 24uv \, du = 12v(1-v)^2, \quad \text{para } 0 \le v \le 1.$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

## Paso 4: Verificar la condición de independencia

Dos variables son independientes si y solo si $f_{U,V}(u,v) = f_U(u) \cdot f_V(v)$ para todos los valores de su rango.

- Producto de las marginales: $[12u(1-u)^2] \cdot [12v(1-v)^2] = 144uv(1-u)^2(1-v)^2$.
- Función conjunta: $24uv$.

Claramente, **el producto de las marginales no es igual a la función conjunta** ($24uv \neq 144uv(1-u)^2(1-v)^2$).

**Conclusión:** Las variables aleatorias $U$ y $V$ **no son independientes**. Además, el hecho de que la región de soporte sea un triángulo (donde los límites de una variable dependen de la otra) es una prueba suficiente de que existe dependencia.

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. La comparación $24uv \neq 144uv(1-u)^2(1-v)^2$ es correcta. La alerta sobre el dominio triangular como condición suficiente de dependencia también es correcta.

---

## Gráfica en Desmos

La gráfica representa la región triangular de soporte y las curvas de las densidades marginales calculadas.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=2;
width=500; height=500;
---
x+y<=1|x>=0|y>=0|#a5d8ff
y=1-x|BLUE|0<=x<=1
f(x)=12x(1-x)^2|RED|0<=x<=1
(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Faltaban los parámetros de ventana (`left`, `right`, `bottom`, `top`) antes del `---`.
>
> **Corrección:** Se agregaron `left=-0.2; right=1.3; bottom=-0.2; top=1.3;` para encuadrar correctamente el triángulo de soporte.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el dominio del triángulo donde la densidad conjunta es $24uv$ ($u+v \le 1$).
- **Línea Roja ($f(x)$):** Representa la forma de las densidades marginales $12u(1-u)^2$ o $12v(1-v)^2$, mostrando que la probabilidad máxima no está en los extremos.
- **Puntos etiquetados:** Marcan los vértices de la región de soporte definida en el enunciado.

---
---

# Enunciado del Ejercicio 3 (practica)

>temas: [independencia-estadistica, varianza-suma, covarianza, densidad-marginal, dominio-rectangular]

Determinar si las variables aleatorias $X, Y$ cuya densidad de distribución conjunta:
$$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; 0 \le y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
  **a)** Son estadísticamente independientes.
   **b)** Calcular la varianza de $X+Y$.

Para resolver el ejercicio **E3** de la **Práctica 2**, seguiremos los procedimientos para verificar la independencia y calcular la varianza de una suma de variables aleatorias detallados en las fuentes.

## Resolución Paso a Paso

La función de densidad conjunta es: $$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

### a) Determinación de la Independencia Estadística

Para que $X$ e $Y$ sean independientes, debe cumplirse que $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ para todo su rango.

1. **Hallar la densidad marginal de $X$ ($f_X(x)$):** Integramos la función conjunta respecto a $y$ en su rango $$: $$$$f_X(x) = \int_{0}^{1} 4xy , dy = 4x \left[ \frac{y^2}{2} \right]_0^1 = 4x \left( \frac{1}{2} \right) = \mathbf{2x, \quad \text{para } 0 \le x \le 1}$$
    
2. **Hallar la densidad marginal de $Y$ ($f_Y(y)$):** Integramos la función conjunta respecto a $x$ en su rango $$:f_Y(y) = \int_{0}^{1} 4xy , dx = 4y \left[ \frac{x^2}{2} \right]_0^1 = 4y \left( \frac{1}{2} \right) = \mathbf{2y, \quad \text{para } 0 \le y \le 1}$$
    
3. **Verificar la condición de independencia:** Multiplicamos las marginales: $f_X(x) \cdot f_Y(y) = (2x) \cdot (2y) = 4xy$. Como el producto es igual a la función conjunta ($4xy = 4xy$), **las variables aleatorias $X$ e $Y$ son estadísticamente independientes**.

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. Marginales $f_X(x)=2x$ y $f_Y(y)=2y$ correctas. El dominio rectangular permite la factorización, condición necesaria y suficiente para independencia.
    

---

### b) Calcular la varianza de $X+Y$

Como $X$ e $Y$ son independientes, la varianza de la suma es igual a la suma de las varianzas: $VAR[X+Y] = VAR[X] + VAR[Y]$.

1. **Calcular la varianza de $X$ ($VAR[X]$):**
    
    - **Esperanza $E[X]$:** $\int_0^1 x(2x) , dx = [ \frac{2x^3}{3} ]_0^1 = \frac{2}{3}$.
    - **Segundo momento $E[X^2]$:** $\int_0^1 x^2(2x) , dx = [ \frac{2x^4}{4} ]_0^1 = \frac{1}{2}$.
    - **Varianza $VAR[X]$:** $E[X^2] - (E[X])^2 = \frac{1}{2} - (\frac{2}{3})^2 = \frac{1}{2} - \frac{4}{9} = \mathbf{\frac{1}{18}}$.
2. **Calcular la varianza de $Y$ ($VAR[Y]$):** Dada la simetría de la función y del rango, el cálculo es idéntico al de $X$: **$VAR[Y] = \frac{1}{18}$**.
    
3. **Varianza de la suma:** $VAR[X+Y] = \frac{1}{18} + \frac{1}{18} = \frac{2}{18} = \mathbf{\frac{1}{9} \approx 0.1111}$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. $E[X]=2/3$, $E[X^2]=1/2$, $VAR[X]=1/18$ correctos. Como $X$ e $Y$ son independientes $COV[X,Y]=0$, por lo que $VAR[X+Y]=VAR[X]+VAR[Y]=1/9$.
    

---

## Gráfica en Desmos

La región de soporte es un cuadrado unitario en el primer cuadrante. Se grafican también las funciones de densidad marginal.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x>=0|x<=1|y>=0|y<=1|#a5d8ff

f(x)=2x|RED|0<=x<=1
g(x)=2x|GREEN|0<=x<=1

(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
(1,1)|label:(1,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** La sintaxis `0<=x<=1{0<=y<=1}` no es válida en Desmos. Además faltaban los parámetros de ventana.
>
> **Corrección:** Se reemplazó por la desigualdad `y<=1|y>=0|x>=0|x<=1` (variables `x` e `y`) y se agregaron `left`, `right`, `bottom`, `top`. Las marginales $f_X$ y $f_Y$ son idénticas ($2x$) por simetría, se conserva solo la roja.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Soporte de la densidad conjunta ($0 \le x, y \le 1$).
- **Línea Roja ($f(x)$):** Función de densidad marginal de $X$, $f_X(x)=2x$.
- **Línea Verde ($g(x)$):** Función de densidad marginal de $Y$ (representada sobre el eje para visualización), $f_Y(y)=2y$.
- **Líneas Azules:** Límites de la región de probabilidad definida en el enunciado.

---
---

# Enunciado del Ejercicio 4 (practica)

>temas: [varianza-suma, covarianza, densidad-uniforme, dominio-triangular, esperanza]

Las funciones aleatorias $X, Y$ tiene la función de densidad de distribución conjunta que se indica calcular la varianza de $W = X+Y$:
$$f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } x \ge 0, y \ge 0, x+y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$

Para resolver el ejercicio **E4** de la **Práctica 2**, seguiremos el procedimiento para calcular la varianza de una suma de variables aleatorias continuas utilizando el método de la función de densidad de la nueva variable $W = X+Y$.

## Paso 1: Definir la región de soporte y la función conjunta

La función de densidad conjunta está dada por: $$f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } x \ge 0, y \ge 0, x+y \le 1 \ 0 & \text{en otro caso} \end{cases}$$ Esta región representa un **triángulo** en el primer cuadrante con vértices en $(0,0)$, $(1,0)$ y $(0,1)$.

## Paso 2: Hallar la función de densidad de $W = X+Y$

Para encontrar la densidad de la suma $f_W(w)$, integramos la función conjunta sobre la recta $x+y=w$ dentro de los límites de soporte. Para el rango $0 \le w \le 1$: $f_W(w) = \int_{0}^{w} f_{X,Y}(x, w-x) \, dx = \int_{0}^{w} 2 \, dx = \mathbf{2w, \quad \text{para } 0 \le w \le 1}$ Este resultado se obtiene considerando que para un valor fijo de $w$, $x$ varía desde $0$ hasta $w$.

> [!check] Correcto
> $f_W(w)=2w$ es válida: $\int_0^1 2w\,dw=1$ ✓.

## Paso 3: Calcular el valor esperado $E[W]$

Utilizando la densidad $f_W(w)$ encontrada: $$E[W] = \int_{0}^{1} w \cdot f_W(w) , dw = \int_{0}^{1} w(2w) , dw = \int_{0}^{1} 2w^2 , dw$$ $E[W] = \left[ \frac{2w^3}{3} \right]_0^1 = \mathbf{\frac{2}{3}}$

> [!check] Correcto

## Paso 4: Calcular el segundo momento $E[W^2]$

$$E[W^2] = \int_{0}^{1} w^2 \cdot f_W(w) , dw = \int_{0}^{1} w^2(2w) , dw = \int_{0}^{1} 2w^3 , dw$$ $E[W^2] = \left[ \frac{2w^4}{4} \right]_0^1 = \mathbf{\frac{1}{2}}$

> [!check] Correcto

## Paso 5: Calcular la varianza de $W$

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

## Gráfica en Desmos

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

---
---

# Enunciado del Ejercicio 5 (practica)

>temas: [pdf-multivariable, probabilidad-conjunta, densidad-marginal, factorizacion-integral]

Dada la función de densidad de distribución de probabilidad conjunta como se indica a continuación:
$$f_{W,X,Y,Z}(w,x,y,z) = \begin{cases} 16wxyz & \text{si } 0 \le w \le 1, 0 \le x \le 1, 0 \le y \le 1, 0 \le z \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
**a)** Hallar la probabilidad de $W \le 3$ y que $Y \le \frac{1}{2}$.
**b)** Encontrar la función de densidad marginal de $W$.


## 1. Análisis de la función conjunta

La función de densidad conjunta es: $$f_{W,X,Y,Z}(w,x,y,z) = \begin{cases} 16wxyz & \text{si } 0 \le w, x, y, z \le 1 \ 0 & \text{en otro caso} \end{cases}$$ Se observa que la función es **factorizable** en términos independientes: $f(w,x,y,z) = (2w)(2x)(2y)(2z)$. Esto indica que las variables $W, X, Y$ y $Z$ son **estadísticamente independientes** entre sí dentro del hipercubo unitario $^4$.

---

## a) Hallar la probabilidad de $W \le 3$ y que $Y \le \frac{1}{2}$

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

## b) Encontrar la función de densidad marginal de $W$

La densidad marginal de una variable se obtiene integrando la función conjunta respecto a todas las demás variables sobre sus respectivos rangos de definición:

$$f_W(w) = \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} 16wxyz , dx , dy , dz$$ $$f_W(w) = 16w \left( \int_{0}^{1} x , dx \right) \left( \int_{0}^{1} y , dy \right) \left( \int_{0}^{1} z , dz \right)$$

Calculando las integrales simples:

- $\int_0^1 x , dx = \frac{1}{2}$ (lo mismo para $y$ y $z$).

Sustituyendo: $$f_W(w) = 16w \cdot \left(\frac{1}{2}\right) \cdot \left(\frac{1}{2}\right) \cdot \left(\frac{1}{2}\right) = \frac{16w}{8}$$ $\mathbf{f_W(w) = 2w, \quad \text{para } 0 \le w \le 1}$

> [!check] Correcto
> La factorización de la integral triple es válida. Cada integral $\int_0^1 x\,dx = 1/2$, por lo que $16w \cdot (1/2)^3 = 2w$ ✓. Verificación: $\int_0^1 2w\,dw = 1$ ✓.

---

## Gráfica en Desmos

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

---
---

# Enunciado del Ejercicio 6 (practica)

>temas: [region-valor-absoluto, densidad-marginal, probabilidad-unilateral, esperanza-matematica]

Las variables aleatorias $X, Y$ tiene la función de densidad de distribución de probabilidad que se indica: $f_{X,Y}(x,y) = \begin{cases} \frac{1}{2} & \text{si } -1 \le x \le 1 \\ 0 & \text{en otro caso} \end{cases}$
**a)** Dibujar la región de probabilidad distinta de cero.
**b)** Determinar la función de densidad marginal de $X$.
**c)** Determine $P(X > 0)$.
**d)** Determinar el valor esperado de $X$.

> [!warning] Enunciado incompleto
> El enunciado original solo especifica $-1 \le x \le 1$ sin restricción sobre $y$. Con esa condición la integral doble diverge y $f$ no puede ser una PDF válida. La única región que normaliza a 1 con constante $1/2$ es $-1 \le x \le y \le 1$ (triángulo). El desarrollo usa esa región.

Para resolver este ejercicio, el cual corresponde a una variante del **Ejercicio 6** (identificado en las fuentes como el problema 4.5.1 de Yates & Goodman), asumiremos la región de soporte completa necesaria para que la función sea una densidad válida con la constante $1/2$.

## Enunciado del Ejercicio

Las variables aleatorias $X, Y$ tienen la siguiente función de densidad de distribución conjunta: $$f_{X,Y}(x,y) = \begin{cases} \frac{1}{2} & \text{si } -1 \le x \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

## Resolución Paso a Paso

### a) Dibujar la región de probabilidad distinta de cero

La región de soporte está definida por las desigualdades $-1 \le x \le 1$, $y \le 1$ y, fundamentalmente, **$x \le y$**. Esto describe un **triángulo** en el plano con los siguientes vértices:

- $(-1, -1)$
- $(-1, 1)$
- $(1, 1)$

Esta región ocupa la mitad superior izquierda del cuadrado delimitado por $x, y \in [-1, 1]$.

### b) Determinar la función de densidad marginal de $X$ ($f_X(x)$)

Para obtener la marginal de $X$, integramos la función conjunta respecto a $y$ sobre su rango de existencia. Para un valor fijo de $x$, $y$ varía desde $x$ hasta $1$: $$f_X(x) = \int_{x}^{1} \frac{1}{2} , dy = \frac{1}{2} [y]_x^1$$ $\mathbf{f_X(x) = \frac{1}{2}(1 - x), \quad \text{para } -1 \le x \le 1}$.

> [!check] Correcto
> Límites de integración correctos ($y$ de $x$ a $1$). Resultado $f_X(x)=\frac{1}{2}(1-x)$ verificado. Normalización: $\int_{-1}^1\frac{1}{2}(1-x)\,dx=1$ ✓.

### c) Determine $P(X > 0)$

Integramos la densidad marginal de $X$ calculada en el inciso anterior sobre el intervalo $(0, 1)$: $$P(X > 0) = \int_{0}^{1} \frac{1}{2}(1 - x) , dx = \frac{1}{2} \left[ x - \frac{x^2}{2} \right]_0^1$$ $P(X > 0) = \frac{1}{2} \left( 1 - \frac{1}{2} \right) = \mathbf{\frac{1}{4} = 0.25}$.

> [!check] Correcto
> Integración de $f_X(x)$ en $[0,1]$ correcta. Resultado $1/4$ ✓.

### d) Determinar el valor esperado de $X$ ($E[X]$)

Aplicamos la definición de esperanza para una variable aleatoria continua: $$E[X] = \int_{-1}^{1} x \cdot f_X(x) , dx = \int_{-1}^{1} x \cdot \frac{1}{2}(1 - x) , dx$$ $$E[X] = \frac{1}{2} \int_{-1}^{1} (x - x^2) , dx = \frac{1}{2} \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_{-1}^1$$ Evaluando en los límites: $E[X] = \frac{1}{2} \left[ \left( \frac{1}{2} - \frac{1}{3} \right) - \left( \frac{1}{2} + \frac{1}{3} \right) \right] = \frac{1}{2} \left[ -\frac{2}{3} \right] = \mathbf{-\frac{1}{3} \approx -0.3333}$.

> [!check] Correcto
> Desarrollo algebraico correcto. $\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_{-1}^{1} = \left(\frac{1}{2}-\frac{1}{3}\right)-\left(\frac{1}{2}+\frac{1}{3}\right)=-\frac{2}{3}$, por lo que $E[X]=-\frac{1}{3}$ ✓.

---

## Gráfica en Desmos

La gráfica muestra el soporte triangular donde la probabilidad es uniforme ($1/2$) y la curva de la densidad marginal de $X$.

```desmos-graph
left=-1.5; right=1.5; bottom=-1.5; top=1.5;
width=500; height=500;
---
y>=x|y<=1|x>=-1|x<=1|#a5d8ff
y=x|RED|-1<=x<=1
f(x)=0.5(1-x)|BLUE|-1<=x<=1
(-1,-1)|label:(-1,-1)|BLACK
(-1,1)|label:(-1,1)|BLACK
(1,1)|label:(1,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Faltaban parámetros de ventana. La restricción `x>=-1` sin `x<=1` dejaba la región abierta a la derecha.
>
> **Corrección:** Se agregaron `left=-1.5; right=1.5; bottom=-1.5; top=1.5;` y `x<=1` para cerrar correctamente el triángulo. Se eliminaron las líneas de borde redundantes (`y=1`, `x=-1`) ya que la región sombreada las cubre.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa la región de soporte conjunta $-1 \le x \le y \le 1$.
- **Línea Roja:** Delimita los bordes del triángulo de probabilidad.
- **Línea Azul ($f(x)$):** Representa la función de densidad marginal $f_X(x) = 0.5(1-x)$. Note que la probabilidad es mayor cuando $x$ es cercano a $-1$ y disminuye linealmente hasta llegar a cero en $x=1$.
- **Puntos etiquetados:** Indican los vértices del dominio de las variables aleatorias.

---
---

# Enunciado del Ejercicio 7 (practica)

>temas: [densidad-condicional, probabilidad-evento, region-triangular, exponencial-bivariada]

Las variables aleatorias $X, Y$ tienen la función de densidad de distribución de probabilidad conjunta que se indica:
$$f_{X,Y}(x,y) = \begin{cases} 6e^{-(2x+3y)} & \text{si } x \ge 0, y \ge 0 \\ 0 & \text{en otro caso} \end{cases}$$
Determine la función de densidad de distribución condicional $f_{X,Y|A}(x,y)$, sabiendo que $A$ es el evento dado por la expresión $x+y \le 1$ y que la densidad condicional es igual a la densidad conjunta dividida entre la probabilidad del evento $A$ para el rango $(x,y) \in A$.

Para resolver el **Ejercicio E7** de la **Práctica 2**, seguiremos el procedimiento para determinar una función de densidad condicional dado un evento específico $A$, utilizando las propiedades de las funciones de densidad conjunta y el cálculo de probabilidades en regiones del plano.

## 1. Definición de la región y la función

La función de densidad conjunta está dada por $f_{X,Y}(x,y) = 6e^{-(2x+3y)}$ para el primer cuadrante ($x, y \ge 0$). El evento $A$ corresponde a la región triangular delimitada por las desigualdades $x \ge 0, y \ge 0$ y $x+y \le 1$.

Para hallar la densidad condicional, la fórmula establecida es: $$f_{X,Y|A}(x,y) = \frac{f_{X,Y}(x,y)}{P[A]}, \quad \text{si } (x,y) \in A$$ Y es igual a $0$ en cualquier otro caso.

## 2. Cálculo de la probabilidad del evento $A$ ($P[A]$)

La probabilidad del evento $A$ se obtiene integrando la función de densidad conjunta sobre la región triangular descrita:

$$P[A] = \int_{0}^{1} \int_{0}^{1-x} 6e^{-(2x+3y)} , dy , dx$$

- **Integración interna (respecto a $y$):** Separamos los términos exponenciales: $6e^{-2x} \int_{0}^{1-x} e^{-3y} , dy$. La integral de $e^{-3y}$ es $\left[ \frac{e^{-3y}}{-3} \right]_0^{1-x} = -\frac{1}{3}(e^{-3(1-x)} - e^{0}) = \frac{1}{3}(1 - e^{3x-3})$. Multiplicando por la constante: $6e^{-2x} \cdot \frac{1}{3}(1 - e^{3x-3}) = 2e^{-2x} - 2e^{x-3}$.
    
- **Integración externa (respecto a $x$):** $\int_{0}^{1} (2e^{-2x} - 2e^{x-3}) , dx = \left[ -e^{-2x} - 2e^{x-3} \right]_0^1$. Evaluando en los límites: En $x=1$: $-e^{-2} - 2e^{-2} = -3e^{-2}$. En $x=0$: $-e^{0} - 2e^{-3} = -1 - 2e^{-3}$. Restando los valores: $(-3e^{-2}) - (-1 - 2e^{-3}) = \mathbf{1 - 3e^{-2} + 2e^{-3}}$.

> [!correction] Corrección — evaluación en $x=1$
> **Error identificado:** El archivo escribía $-e^{-2} - 2e^{0}$ en $x=1$, confundiendo $e^{x-3}\big|_{x=1} = e^{-2}$ con $e^{0}$.
>
> **Corrección:** $e^{x-3}\big|_{x=1} = e^{1-3} = e^{-2}$, por lo que el valor correcto es $-e^{-2} - 2e^{-2} = -3e^{-2}$. El resultado final $P[A]=1-3e^{-2}+2e^{-3}$ era correcto aunque el paso intermedio estaba mal.
    

## 3. Función de densidad condicional final

Sustituimos el valor de $P[A]$ en la definición de la densidad condicional para obtener el resultado:

$$\mathbf{f_{X,Y|A}(x,y) = \begin{cases} \frac{6e^{-(2x+3y)}}{1 - 3e^{-2} + 2e^{-3}} & \text{si } x \ge 0, y \ge 0, x+y \le 1 \ 0 & \text{en otro caso} \end{cases}}$$

_Nota: El valor numérico de la constante de normalización es aproximadamente $1/0.6936 \approx 1.442$._

> [!check] Correcto
> Fórmula del formulario aplicada correctamente: $f_{X,Y|A}=f_{X,Y}/P[A]$ para $(x,y)\in A$, cero fuera. $P[A]=1-3e^{-2}+2e^{-3}\approx 0.6936$ ✓.

---

## Gráfica en Desmos

La gráfica representa la región de soporte $A$ (el triángulo) donde la densidad condicional es distinta de cero.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x+y<=1|x>=0|y>=0|#a5d8ff
y=1-x|BLUE|0<=x<=1
(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Faltaban parámetros de ventana. Las líneas `x=0` e `y=0` usan variables distintas de $x$ e $y$ en Desmos y pueden causar error.
>
> **Corrección:** Se agregaron `left=-0.2; right=1.3; bottom=-0.2; top=1.3;` y se eliminaron `x=0|BLUE` e `y=0|BLUE` (los ejes de Desmos ya los muestran por defecto).

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el dominio del evento $A$ ($x+y \le 1$) donde la variable aleatoria condicionada tiene probabilidad definida.
- **Líneas Azules:** Son las fronteras que delimitan el triángulo de soporte en el primer cuadrante.
- **Puntos etiquetados:** Indican los vértices de la región de integración utilizada para calcular $P[A]$.
