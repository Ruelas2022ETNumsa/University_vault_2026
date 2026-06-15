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

## 🟡 c) Determinación de independencia estadística

### 1. Criterio técnico

Dos variables aleatorias son independientes si y solo si su PDF conjunta es igual al producto de sus PDFs marginales para todo punto en el plano: $$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

### 2. Verificación por punto de prueba

Seleccionamos un punto dentro del soporte, por ejemplo $x = 1, y = 2$:

- **PDF Conjunta:** $f_{X,Y}(1,2) = \frac{3}{8}(1) = \mathbf{0.375}$.
- **Marginal de $X$:** $f_X(1) = \frac{3}{4}(1)(2-1) = 0.75$.
- **Marginal de $Y$:** $f_Y(2) = \frac{3}{16}(2)^2 = 0.75$.

Multiplicamos las marginales: $0.75 \times 0.75 = \mathbf{0.5625}$.

### 3. Conclusión

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













