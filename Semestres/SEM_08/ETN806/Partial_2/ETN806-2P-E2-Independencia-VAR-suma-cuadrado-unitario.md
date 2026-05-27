---
title: "ETN806 — 2do Parcial — E2: Independencia Estadística y VAR(X+Y) en cuadrado unitario"
aliases: [E2b, 2P-E2]
tags: [ETN806, 2do-parcial, examen, variables-aleatorias-multiples, independencia-estadistica, varianza, cuadrado-unitario]
materia: Procesos Estocásticos (ETN806)
parcial: 2do Parcial
tipo: ejercicio-examen
fuente: 2do Parcial
fecha: 2026-05-25
estado: revisado
temas: [independencia-estadistica, varianza-suma, densidad-marginal, dominio-rectangular]
---

A continuación se presenta el enunciado del **Ejercicio 2** extraído de la fuente **SEGUNDO PARCIAL.pdf**:

### 📝 Enunciado del Ejercicio 2

**2.- (20%)** Determinar si las variables aleatorias $X$, $Y$ cuya densidad de distribución conjunta es:

$$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; \quad 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

**Se pide:**

- **a)** Determinar si son estadísticamente independientes.
- **b)** Calcular la varianza de $X + Y$.



Esta es la resolución detallada, paso a paso y pedagógica del segundo ejercicio del examen parcial, siguiendo los procedimientos técnicos establecidos para el análisis de variables aleatorias múltiples.

---

### 📝 Enunciado del Ejercicio 2

Determinar si las variables aleatorias $X$ e $Y$, cuya densidad de distribución conjunta está dada por la siguiente expresión, son independientes y calcular la varianza de su suma:

$$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; \quad 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

**Se pide:**

- **a)** Determinar si son estadísticamente independientes.
- **b)** Calcular la varianza de la variable aleatoria $W = X + Y$.

---

### 🟢 a) Determinación de la Independencia Estadística

#### 1. Identificación de datos y concepto

Para verificar la **independencia estadística**, debemos comprobar si la función de densidad conjunta es igual al producto de sus funciones de densidad marginales para todo el dominio. La fórmula es: $$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

#### 2. Cálculo de la función de densidad marginal de $X$ ($f_X(x)$)

La densidad marginal de una variable se obtiene integrando la función conjunta respecto a la otra variable sobre su rango de soporte.

- **Fórmula:** $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$
- **Sustitución de valores:** Para el rango $0 \le x \le 1$, integramos respecto a $y$ desde 0 hasta 1: $$f_X(x) = \int_{0}^{1} 4xy , dy$$
- **Desarrollo algebraico:** Extraemos $4x$ como constante fuera de la integral: $$f_X(x) = 4x \int_{0}^{1} y , dy$$ Aplicamos la regla de integración de potencias ($\int y^1 dy = \frac{y^2}{2}$): $$f_X(x) = 4x \left[ \frac{y^2}{2} \right]_0^1 = 4x \left( \frac{1^2}{2} - \frac{0^2}{2} \right) = 4x \left( \frac{1}{2} \right)$$
- **Resultado marginal X:** $\mathbf{f_X(x) = 2x, \quad \text{para } 0 \le x \le 1}$.

#### 3. Cálculo de la función de densidad marginal de $Y$ ($f_Y(y)$)

Realizamos el mismo procedimiento, pero integrando respecto a $x$.

- **Fórmula:** $f_Y(y) = \int_{0}^{1} 4xy , dx$
- **Desarrollo:** $$f_Y(y) = 4y \int_{0}^{1} x , dx = 4y \left[ \frac{x^2}{2} \right]_0^1 = 4y \left( \frac{1}{2} \right)$$
- **Resultado marginal Y:** $\mathbf{f_Y(y) = 2y, \quad \text{para } 0 \le y \le 1}$.

#### 4. Verificación de la condición de independencia

Multiplicamos las dos funciones marginales obtenidas: $$f_X(x) \cdot f_Y(y) = (2x) \cdot (2y) = \mathbf{4xy}$$ **Conclusión:** Dado que el producto de las marginales es idéntico a la función de densidad conjunta original ($4xy = 4xy$), se concluye que **las variables aleatorias $X$ e $Y$ son estadísticamente independientes**.

---

### 🔵 b) Cálculo de la varianza de $X + Y$

#### 1. Identificación de la fórmula

La varianza de una suma de variables aleatorias se define generalmente como: $$VAR[X+Y] = VAR[X] + VAR[Y] + 2 \cdot COV[X,Y]$$ Sin embargo, dado que en el inciso anterior demostramos que $X$ e $Y$ son **independientes**, la covarianza es automáticamente **0** ($COV[X,Y] = 0$). Por lo tanto, la fórmula se simplifica a: $$VAR[X+Y] = VAR[X] + VAR[Y]$$

#### 2. Cálculo de la varianza de $X$ ($VAR[X]$)

Utilizamos la fórmula práctica: $VAR[X] = E[X^2] - (E[X])^2$.

- **Esperanza $E[X]$:** $$E[X] = \int_{0}^{1} x \cdot f_X(x) , dx = \int_{0}^{1} x \cdot (2x) , dx = \int_{0}^{1} 2x^2 , dx$$ $$E[X] = \left[ \frac{2x^3}{3} \right]_0^1 = \mathbf{\frac{2}{3}}$$
- **Segundo momento $E[X^2]$:** $$E[X^2] = \int_{0}^{1} x^2 \cdot f_X(x) , dx = \int_{0}^{1} x^2 \cdot (2x) , dx = \int_{0}^{1} 2x^3 , dx$$ $$E[X^2] = \left[ \frac{2x^4}{4} \right]_0^1 = \frac{2}{4} = \mathbf{\frac{1}{2}}$$
- **Varianza de $X$:** $$VAR[X] = \frac{1}{2} - \left( \frac{2}{3} \right)^2 = \frac{1}{2} - \frac{4}{9} = \frac{9 - 8}{18} = \mathbf{\frac{1}{18}}$$.

#### 3. Cálculo de la varianza de $Y$ ($VAR[Y]$)

Dada la simetría perfecta de la función conjunta y los límites de integración, el cálculo para $Y$ es idéntico al de $X$: $$VAR[Y] = \mathbf{\frac{1}{18}}$$.

#### 4. Resultado final de la varianza de la suma

$$VAR[X+Y] = \frac{1}{18} + \frac{1}{18} = \frac{2}{18} = \mathbf{\frac{1}{9}}$$ En decimales, el resultado es aproximadamente **0.1111**.

---