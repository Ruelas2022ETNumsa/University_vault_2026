
# 1.

Se seleccionan al azar 2 repuestos para un dispositivo de una caja que contiene 3 repuestos marca HUAWEI, 2 marca TECNO y 3 marca INFINIX.

Si (X) es el número de repuestos marca HUAWEI y sea (Y) el número de repuestos marca TECNO que se seleccionan, calcule la tabla de distribución y el coeficiente de correlación.

## solucion

Para resolver este ejercicio sobre variables aleatorias discretas múltiples, seguiremos un procedimiento técnico y pedagógico detallado, fundamentado en la teoría de la **distribución hipergeométrica multivariada**.

---

## 1. IDENTIFICACIÓN DE LOS DATOS DEL PROBLEMA

El experimento consiste en extraer una muestra de una caja sin reemplazo. Los datos son:

- **Contenido total de la caja ($N$):** 8 repuestos en total.
    - Repuestos marca **HUAWEI** ($a_1$): 3 unidades.
    - Repuestos marca **TECNO** ($a_2$): 2 unidades.
    - Repuestos marca **INFINIX** ($a_3$): 3 unidades.
- **Tamaño de la muestra ($n$):** Se seleccionan 2 repuestos al azar.
- **Variables aleatorias definidas:**
    - $X$: Número de repuestos marca HUAWEI seleccionados.
    - $Y$: Número de repuestos marca TECNO seleccionados.

---

## 2. EXPLICACIÓN DE LO QUE SE PIDE

Se solicita:

1. **La tabla de distribución de probabilidad conjunta $P_{X,Y}(x, y)$:** Una matriz que muestre las probabilidades de todas las combinaciones posibles de $X$ y $Y$.
2. **El coeficiente de correlación ($\rho_{XY}$):** Un índice adimensional que mide la fuerza y dirección de la relación lineal entre el número de repuestos HUAWEI y TECNO obtenidos.
## solucion

---

### 3. FÓRMULAS UTILIZADAS Y JUSTIFICACIÓN

#### A. Probabilidad Hipergeométrica Multivariada

Se utiliza porque seleccionamos elementos de diferentes categorías sin reemplazo de un conjunto finito: $$P(X=x, Y=y) = \frac{\binom{a_1}{x} \binom{a_2}{y} \binom{a_3}{n-x-y}}{\binom{N}{n}}$$ Donde:

- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ es el coeficiente binomial (combinaciones).

#### B. Esperanza Matemática y Varianza

Para obtener la correlación, necesitamos los momentos estadísticos de cada variable:

- **Esperanza ($E[X]$):** $\mu_x = \sum x P_x(x)$
- **Varianza ($VAR[X]$):** $E[X^2] - (E[X])^2$

#### C. Covarianza y Coeficiente de Correlación

- **Covarianza ($COV[X,Y]$):** $E[XY] - E[X]E[Y]$.
- **Coeficiente de Correlación ($\rho_{XY}$):** $\frac{COV[X,Y]}{\sigma_X \sigma_Y}$.

---

### 4. RESOLUCIÓN PASO A PASO

#### Paso 1: Determinar el número total de formas de selección

Calculamos el denominador de nuestra función de probabilidad (combinaciones de 8 tomadas de 2 en 2): $$\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = \mathbf{28}$$

#### Paso 2: Calcular las probabilidades conjuntas $f(x, y)$

Los valores posibles para $(x, y)$ deben cumplir que $0 \leq x+y \leq 2$.

- **$f(0,0)$:** 0 Huawei, 0 Tecno (implica 2 Infinix). $$P(X=0, Y=0) = \frac{\binom{3}{0}\binom{2}{0}\binom{3}{2}}{28} = \frac{1 \cdot 1 \cdot 3}{28} = \frac{3}{28}$$
- **$f(1,0)$:** 1 Huawei, 0 Tecno (implica 1 Infinix). $$P(X=1, Y=0) = \frac{\binom{3}{1}\binom{2}{0}\binom{3}{1}}{28} = \frac{3 \cdot 1 \cdot 3}{28} = \frac{9}{28}$$
- **$f(2,0)$:** 2 Huawei, 0 Tecno (implica 0 Infinix). $$P(X=2, Y=0) = \frac{\binom{3}{2}\binom{2}{0}\binom{3}{0}}{28} = \frac{3 \cdot 1 \cdot 1}{28} = \frac{3}{28}$$
- **$f(0,1)$:** 0 Huawei, 1 Tecno (implica 1 Infinix). $$P(X=0, Y=1) = \frac{\binom{3}{0}\binom{2}{1}\binom{3}{1}}{28} = \frac{1 \cdot 2 \cdot 3}{28} = \frac{6}{28}$$
- **$f(1,1)$:** 1 Huawei, 1 Tecno (implica 0 Infinix). $$P(X=1, Y=1) = \frac{\binom{3}{1}\binom{2}{1}\binom{3}{0}}{28} = \frac{3 \cdot 2 \cdot 1}{28} = \frac{6}{28}$$
- **$f(0,2)$:** 0 Huawei, 2 Tecno (implica 0 Infinix). $$P(X=0, Y=2) = \frac{\binom{3}{0}\binom{2}{2}\binom{3}{0}}{28} = \frac{1 \cdot 1 \cdot 1}{28} = \frac{1}{28}$$

#### Paso 3: Construcción de la Tabla de Distribución

Sumamos filas y columnas para obtener las **probabilidades marginales**:

|$Y \setminus X$|0|1|2|**Marginal $P_Y(y)$**|
|:-:|:-:|:-:|:-:|:-:|
|**0**|$3/28$|$9/28$|$3/28$|**$15/28$**|
|**1**|$6/28$|$6/28$|$0$|**$12/28$**|
|**2**|$1/28$|$0$|$0$|**$1/28$**|
|**Marginal $P_X(x)$**|**$10/28$**|**$15/28$**|**$3/28$**|**$1$**|

---

### 5. CÁLCULO DEL COEFICIENTE DE CORRELACIÓN

#### A. Cálculo de las Esperanzas ($E[X]$ y $E[Y]$)

- **$E[X]$:** $(0 \cdot \frac{10}{28}) + (1 \cdot \frac{15}{28}) + (2 \cdot \frac{3}{28}) = \frac{15+6}{28} = \frac{21}{28} = \mathbf{\frac{3}{4}}$
- **$E[Y]$:** $(0 \cdot \frac{15}{28}) + (1 \cdot \frac{12}{28}) + (2 \cdot \frac{1}{28}) = \frac{12+2}{28} = \frac{14}{28} = \mathbf{\frac{1}{2}}$

#### B. Cálculo de la Correlación ($E[XY]$)

Solo el término donde $x=1$ y $y=1$ es distinto de cero:

- **$E[XY]$:** $(1 \cdot 1 \cdot \frac{6}{28}) = \frac{6}{28} = \mathbf{\frac{3}{14}}$

#### C. Cálculo de la Covarianza ($COV[X,Y]$)

$$COV[X,Y] = E[XY] - E[X] \cdot E[Y]$$ $$COV[X,Y] = \frac{3}{14} - (\frac{3}{4} \cdot \frac{1}{2}) = \frac{3}{14} - \frac{3}{8}$$ _Mínimo común múltiplo (56):_ $$COV[X,Y] = \frac{12 - 21}{56} = \mathbf{-\frac{9}{56}}$$

#### D. Cálculo de las Varianzas ($VAR[X]$ y $VAR[Y]$)

- **$E[X^2]$:** $(1^2 \cdot \frac{15}{28}) + (2^2 \cdot \frac{3}{28}) = \frac{15 + 12}{28} = \frac{27}{28}$
    - $VAR[X] = \frac{27}{28} - (\frac{3}{4})^2 = \frac{27}{28} - \frac{9}{16} = \frac{108 - 63}{112} = \mathbf{\frac{45}{112}}$
- **$E[Y^2]$:** $(1^2 \cdot \frac{12}{28}) + (2^2 \cdot \frac{1}{28}) = \frac{12 + 4}{28} = \frac{16}{28}$
    - $VAR[Y] = \frac{16}{28} - (\frac{1}{2})^2 = \frac{4}{7} - \frac{1}{4} = \frac{16 - 7}{28} = \mathbf{\frac{9}{28}}$

#### E. Cálculo Final del Coeficiente ($\rho_{XY}$)

$$\rho_{XY} = \frac{-9/56}{\sqrt{(\frac{45}{112})(\frac{9}{28})}} = \frac{-9/56}{\sqrt{\frac{405}{3136}}} = \frac{-9/56}{9\sqrt{5}/56} = -\frac{1}{\sqrt{5}}$$ $$\rho_{XY} \approx \mathbf{-0.4472}$$

---

### 6. RESULTADO FINAL

1. **La tabla de distribución conjunta** es la presentada en el Paso 3.
2. **El coeficiente de correlación** es: $$\boxed{\rho_{XY} = -\frac{1}{\sqrt{5}} \approx -0.4472}$$

**Interpretación:** Existe una **correlación negativa moderada**. Esto tiene sentido físico: al seleccionar más repuestos de una marca (Huawei), quedan menos espacios disponibles en la muestra de 2 para la otra marca (Tecno).

---

# 2. (25%)

Las variables aleatorias (X) y (Y) tienen la función de densidad de distribución de probabilidad conjunta que se indica:

$$  
f_{X,Y}(x,y)=  
\begin{cases}  
\dfrac{2}{\pi}, & \text{si } x^2+y^2 \le 1,; 0 \le y \le 1,\ \\ 
0, & \text{en otro caso.}  
\end{cases}  
$$

Analice solo en los dos primeros cuadrantes.

a)Encontrar la distribución marginal de (X).
 b)Encontrar la distribución marginal de (Y).

## sol.

Para resolver este ejercicio sobre variables aleatorias continuas múltiples, seguiremos un procedimiento técnico y pedagógico exhaustivo, fundamentado en la teoría de las **distribuciones marginales** para funciones de densidad de probabilidad (PDF) conjunta.

---

## 1. IDENTIFICACIÓN DE LOS DATOS DEL PROBLEMA

- **Función de densidad conjunta ($f_{X,Y}(x,y)$):** Es una constante $k = \frac{2}{\pi}$ dentro de una región específica.
- **Región de soporte ($R$):** Está delimitada por las inecuaciones:
    1. $x^2 + y^2 \le 1$: El interior de un círculo unitario centrado en el origen.
    2. $0 \le y \le 1$: La mitad superior del plano cartesiano (primer y segundo cuadrante).
- **Geometría:** La combinación de estas condiciones describe un **semicírculo unitario** situado en el semiplano superior.
- **Límites globales de las variables:**
    - Para $y$: Varía de $0$ a $1$.
    - Para $x$: Varía de $-1$ a $1$.

---

## 2. EXPLICACIÓN DE LO QUE SE PIDE

Se solicita encontrar las **funciones de densidad marginales** de las variables aleatorias $X$ e $Y$.

- **La marginal de $X$ ($f_X(x)$):** Describe cómo se distribuye la probabilidad de $X$ individualmente, promediando (integrando) todos los posibles valores de $Y$ existentes para cada punto del eje $x$.
- **La marginal de $Y$ ($f_Y(y)$):** Indica la distribución de probabilidad de $Y$ sola, integrando sobre todo el rango de valores de $X$ para cada valor fijo de $y$.

---

## 3. FÓRMULAS UTILIZADAS Y JUSTIFICACIÓN

De acuerdo con el formulario de la materia y los textos de referencia, las fórmulas son:

1. **Densidad Marginal de $X$:** $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$$
2. **Densidad Marginal de $Y$:** $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx$$

**Justificación:** En variables continuas, la probabilidad conjunta representa un volumen bajo la superficie de la función $f_{X,Y}(x,y)$. Para "proyectar" esta probabilidad sobre un solo eje (obtener la marginal), debemos acumular (integrar) toda la masa de probabilidad existente en la dirección de la otra variable sobre la región de soporte.

---

## 4. RESOLUCIÓN PASO A PASO

#### a) Encontrar la distribución marginal de $X$ ($f_X(x)$)

**Paso 1: Identificar los límites de integración para $y$.** Partimos de la ecuación de la frontera del soporte $x^2 + y^2 = 1$. Despejamos la variable $y$ para conocer sus límites en función de $x$: $$y^2 = 1 - x^2 \implies y = \pm \sqrt{1 - x^2}$$ Dado que el enunciado restringe la región a $0 \le y \le 1$, el límite inferior de integración es $0$ y el límite superior es la semicircunferencia superior $y = \sqrt{1 - x^2}$.

**Paso 2: Plantear la integral.** Para un valor de $x$ fijo dentro del intervalo $[-1, 1]$, la variable $y$ recorre desde el eje de las abscisas ($0$) hasta el borde del círculo: $$f_X(x) = \int_{0}^{\sqrt{1 - x^2}} \frac{2}{\pi} , dy$$

**Paso 3: Realizar el desarrollo algebraico de la integración.** Extraemos la constante $\frac{2}{\pi}$ de la integral y evaluamos: $$f_X(x) = \frac{2}{\pi} \left[ y \right]_{0}^{\sqrt{1 - x^2}}$$ $$f_X(x) = \frac{2}{\pi} \left( \sqrt{1 - x^2} - 0 \right)$$

**Resultado final de $f_X(x)$:** $$\boxed{f_X(x) = \begin{cases} \frac{2\sqrt{1 - x^2}}{\pi}, & \text{si } -1 \le x \le 1 \ \\
 0, & \text{en otro caso} \end{cases}}$$

---

#### b) Encontrar la distribución marginal de $Y$ ($f_Y(y)$)

**Paso 1: Identificar los límites de integración para $x$.** Nuevamente usamos la ecuación de la frontera $x^2 + y^2 = 1$, pero esta vez despejamos $x$: $$x^2 = 1 - y^2 \implies x = \pm \sqrt{1 - y^2}$$ Para un valor de $y$ fijo entre $0$ y $1$, la variable $x$ recorre el semicírculo desde el borde izquierdo (cuadrante II) hasta el borde derecho (cuadrante I). Por tanto, el límite inferior es $-\sqrt{1 - y^2}$ y el superior es $\sqrt{1 - y^2}$.

**Paso 2: Plantear la integral.** $$f_Y(y) = \int_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}} \frac{2}{\pi} , dx$$

**Paso 3: Realizar el desarrollo algebraico de la integración.** $$f_Y(y) = \frac{2}{\pi} \left[ x \right]_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}}$$ Sustituimos los límites: $$f_Y(y) = \frac{2}{\pi} \left( \sqrt{1 - y^2} - (-\sqrt{1 - y^2}) \right)$$ $$f_Y(y) = \frac{2}{\pi} \left( \sqrt{1 - y^2} + \sqrt{1 - y^2} \right)$$ $$f_Y(y) = \frac{2}{\pi} \left( 2\sqrt{1 - y^2} \right)$$

**Resultado final de $f_Y(y)$:** $$\boxed{f_Y(y) = \begin{cases} \frac{4\sqrt{1 - y^2}}{\pi}, & \text{si } 0 \le y \le 1  \\
\ 0, & \text{en otro caso} \end{cases}}$$

---

## 5. VERIFICACIÓN DE LOS RESULTADOS

Para que las marginales calculadas sean válidas, su integral sobre todo su dominio debe ser igual a 1.

- **Verificación para $f_X(x)$:** $\int_{-1}^{1} \frac{2}{\pi} \sqrt{1 - x^2} , dx$ Utilizando la sustitución trigonométrica $x = \sin\theta \implies dx = \cos\theta , d\theta$: $\frac{2}{\pi} \int_{-\pi/2}^{\pi/2} \cos^2\theta , d\theta = \frac{2}{\pi} \left[ \frac{\theta}{2} + \frac{\sin 2\theta}{4} \right]_{-\pi/2}^{\pi/2} = \frac{2}{\pi} \left( \frac{\pi}{4} - (-\frac{\pi}{4}) \right) = \frac{2}{\pi} \cdot \frac{\pi}{2} = \mathbf{1}$. **Correcto.**
    
- **Verificación para $f_Y(y)$:** $\int_{0}^{1} \frac{4}{\pi} \sqrt{1 - y^2} , dy$ Aplicando el mismo método de integración, el resultado es $\frac{4}{\pi} \cdot (\frac{\pi}{4}) = \mathbf{1}$. **Correcto.**

---

# 3. (25%)

Un experimento aleatorio consiste en el lanzamiento de una moneda 3 veces.

Si se define la variable aleatoria (X) como el número total de sellos obtenidos y la variable aleatoria (Y) como el número de caras obtenidas en el último lanzamiento, encontrar la función de distribución de probabilidad conjunta y las distribuciones marginales.

## sol


Para resolver este ejercicio sobre variables aleatorias discretas múltiples, realizaremos un análisis técnico y pedagógico exhaustivo, desglosando el experimento desde su espacio muestral hasta la obtención de las funciones de probabilidad marginales, basándonos en los fundamentos de la teoría de probabilidad para variables discretas.

---

## 1. IDENTIFICACIÓN DE LOS DATOS DEL PROBLEMA

- **Experimento:** Lanzamiento de una moneda 3 veces.
- **Variable Aleatoria $X$:** Número total de sellos (S) obtenidos en los tres lanzamientos.
- **Variable Aleatoria $Y$:** Número de caras (C) obtenidas en el último lanzamiento (el tercer lanzamiento).
- **Resultados de la moneda:** Suponemos una moneda legal donde la probabilidad de cara $P(C) = 1/2$ y la de sello $P(S) = 1/2$.

---

## 2. EXPLICACIÓN DE LO QUE SE PIDE

Se solicita:

1. **Función de distribución de probabilidad conjunta $P_{X,Y}(x, y)$:** Una representación (usualmente una tabla) que asigne una probabilidad a cada par posible de valores $(x, y)$.
2. **Distribuciones marginales:** Las funciones de probabilidad individuales para $X$ ($P_X(x)$) y para $Y$ ($P_Y(y)$), obtenidas a partir de la conjunta.

---

## 3. FÓRMULAS UTILIZADAS Y JUSTIFICACIÓN

#### A. Definición de Probabilidad en Espacios Equiprobables

Dado que cada lanzamiento es independiente y la moneda es justa, todos los resultados del espacio muestral tienen la misma probabilidad: $$P(\text{resultado}) = \frac{1}{2^n} = \frac{1}{2^3} = \frac{1}{8}$$

#### B. Función de Probabilidad Conjunta (PMF Conjunta)

Para variables discretas, se define como la probabilidad de que $X$ tome un valor $x$ **y** $Y$ tome un valor $y$ simultáneamente: $$P_{X,Y}(x, y) = P(X = x \cap Y = y)$$

#### C. Distribuciones Marginales

Se obtienen sumando las probabilidades conjuntas sobre todos los valores de la otra variable:

- **Marginal de $X$:** $P_X(x) = \sum_{y \in S_y} P_{X,Y}(x, y)$
- **Marginal de $Y$:** $P_Y(y) = \sum_{x \in S_x} P_{X,Y}(x, y)$

---

## 4. RESOLUCIÓN PASO A PASO

#### Paso 1: Construcción del Espacio Muestral ($S$) y Mapeo de Variables

El espacio muestral $S$ contiene $2^3 = 8$ resultados posibles. Evaluamos cada resultado para determinar los valores de $X$ (total de sellos) e $Y$ (caras en el 3er lanzamiento, donde $C=1$ y $S=0$).

|Resultado ($s$)|$X(s)$ (Total de Sellos)|$Y(s)$ (Cara en 3er tiro)|Par $(x, y)$|Probabilidad|
|:--|:-:|:-:|:-:|:-:|
|**CCC**|0|1|(0, 1)|$1/8$|
|**CCS**|1|0|(1, 0)|$1/8$|
|**CSC**|1|1|(1, 1)|$1/8$|
|**CSS**|2|0|(2, 0)|$1/8$|
|**SCC**|1|1|(1, 1)|$1/8$|
|**SCS**|2|0|(2, 0)|$1/8$|
|**SSC**|2|1|(2, 1)|$1/8$|
|**SSS**|3|0|(3, 0)|$1/8$|

#### Paso 2: Cálculo de Probabilidades Conjuntas $P_{X,Y}(x, y)$

Contamos cuántas veces aparece cada par $(x, y)$ en la tabla anterior y multiplicamos por su probabilidad individual ($1/8$):

- **Para $X=0$:**
    - $P(0, 0) = 0$ (No hay resultados con 0 sellos que terminen en S).
    - $P(0, 1) = 1/8$ (Resultado: CCC).
- **Para $X=1$:**
    - $P(1, 0) = 1/8$ (Resultado: CCS).
    - $P(1, 1) = 2/8$ (Resultados: CSC, SCC).
- **Para $X=2$:**
    - $P(2, 0) = 2/8$ (Resultados: CSS, SCS).
    - $P(2, 1) = 1/8$ (Resultado: SSC).
- **Para $X=3$:**
    - $P(3, 0) = 1/8$ (Resultado: SSS).
    - $P(3, 1) = 0$ (No hay resultados con 3 sellos que terminen en C).

#### Paso 3: Construcción de la Tabla de Distribución Conjunta y Marginales

Sumamos las filas para obtener la marginal de $Y$ y las columnas para la marginal de $X$.

|$Y \setminus X$|**0**|**1**|**2**|**3**|**Marginal $P_Y(y)$**|
|:--|:-:|:-:|:-:|:-:|:-:|
|**0 (Sello)**|0|$1/8$|$2/8$|$1/8$|**$4/8 = 1/2$**|
|**1 (Cara)**|$1/8$|$2/8$|$1/8$|0|**$4/8 = 1/2$**|
|**Marginal $P_X(x)$**|**$1/8$**|**$3/8$**|**$3/8$**|**$1/8$**|**1**|

---

## 5. RESULTADO FINAL

#### A. Función de Distribución Conjunta

La tabla presentada en el Paso 3 constituye la función de probabilidad conjunta. Matemáticamente se expresa como: 

$$P_{X,Y}(x, y) = \begin{cases} 1/8, & (x,y) \in {(0,1), (1,0), (2,1), (3,0)} \ \\
 \\
 2/8, & (x,y) \in {(1,1), (2,0)} \ \\
 \\
 0, & \text{en otro caso} \end{cases}$$



#### B. Distribuciones Marginales

**Distribución de $X$ (Número total de sellos):** Sigue una **distribución Binomial** con $n=3$ y $p=0.5$:

$$P_X(x) = \begin{cases} 1/8, & x=0  \\
\ 3/8, & x=1 \ \\
 3/8, & x=2  \\
\ 1/8, & x=3  \\
\ 0, & \text{otro caso} \end{cases}$$

**Distribución de $Y$ (Cara en el último lanzamiento):** Sigue una **distribución de Bernoulli** con $p=0.5$: 

$$P_Y(y) = \begin{cases} 1/2, & y=0  \\
\ 1/2, & y=1 \ \\
 0, & \text{otro caso} \end{cases}$$

---

## 6. VERIFICACIÓN

- **Suma de probabilidades conjuntas:** $\frac{0+1+2+1+1+2+1+0}{8} = \frac{8}{8} = \mathbf{1}$. **Correcto.**
- **Suma de marginal $P_X(x)$:** $\frac{1}{8} + \frac{3}{8} + \frac{3}{8} + \frac{1}{8} = \frac{8}{8} = \mathbf{1}$. **Correcto.**
- **Suma de marginal $P_Y(y)$:** $\frac{4}{8} + \frac{4}{8} = \mathbf{1}$. **Correcto.**

**Nota sobre independencia:** Al observar que $P(X=3, Y=1) = 0$, mientras que el producto de sus marginales es $P_X(3)P_Y(1) = (1/8)(1/2) = 1/16$, se concluye que **las variables $X$ e $Y$ no son independientes**.






---

# 4. (25%)

Las variables aleatorias (X) y (Y) tienen la función de probabilidad conjunta que se indica:

$$  
f_{X,Y}(x,y)=  
\begin{cases}  
e^{-y}, & \text{para } x>0,; y>x,\ \\ 
0, & \text{en otro caso.}  
\end{cases}  
$$

Encontrar las distribuciones marginales y evaluar:

$$  
P!\left(X>2/ Y<4\right).  
$$

# sol

Para resolver este ejercicio sobre variables aleatorias continuas múltiples, seguiremos un procedimiento técnico y pedagógico exhaustivo, fundamentado en el cálculo integral y la teoría de probabilidades condicionales para funciones de densidad de probabilidad (PDF) conjunta.

---

### 1. IDENTIFICACIÓN DE LOS DATOS DEL PROBLEMA

- **Función de densidad conjunta ($f_{X,Y}(x,y)$):** Está definida como $e^{-y}$ dentro de una región específica.
- **Región de soporte ($S$):** Definida por las inecuaciones:
    1. $x > 0$: La variable $X$ es estrictamente positiva.
    2. $y > x$: La variable $Y$ siempre es mayor que $X$.
- **Geometría del soporte:** Estas condiciones describen una región infinita en el primer cuadrante, situada por encima de la recta de identidad $y = x$, extendiéndose desde el eje de las ordenadas hasta el infinito.
    - Para un valor fijo de $x$, la variable $y$ varía de $x$ a $\infty$.
    - Para un valor fijo de $y$, la variable $x$ varía de $0$ a $y$.

---

### 2. EXPLICACIÓN DE LO QUE SE PIDE

Se solicita realizar lo siguiente:

1. **Encontrar la distribución marginal de $X$ ($f_X(x)$):** La proyección de la masa de probabilidad sobre el eje horizontal.
2. **Encontrar la distribución marginal de $Y$ ($f_Y(y)$):** La proyección sobre el eje vertical.
3. **Evaluar la probabilidad condicional $P(X > 2 \mid Y < 4)$:** La probabilidad de que $X$ supere 2, dado que ya sabemos que el valor de $Y$ es menor a 4.

---

### 3. FÓRMULAS UTILIZADAS Y JUSTIFICACIÓN

#### A. Densidades Marginales

Se utilizan para "eliminar" la dependencia de una de las variables mediante la integración sobre todo su rango de existencia:

- $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$
- $f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx$

#### B. Probabilidad Condicional para Eventos

Se basa en la definición fundamental de probabilidad condicional:

- $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ Donde $A = {X > 2}$ y $B = {Y < 4}$.

---

### 4. RESOLUCIÓN PASO A PASO

#### Paso 1: Obtener la distribución marginal de $X$ ($f_X(x)$)

Fijamos $x$ y recorremos todos los valores posibles de $y$. Según el soporte, si conocemos $x$, entonces $y$ debe comenzar en $x$ y puede llegar hasta $\infty$.

**Desarrollo integral:** $$f_X(x) = \int_{x}^{\infty} e^{-y} , dy$$ Aplicamos la regla fundamental del cálculo (integral de una exponencial): $$f_X(x) = \left[ -e^{-y} \right]_{x}^{\infty}$$ Evaluamos en los límites: $$f_X(x) = \lim_{y \to \infty} (-e^{-y}) - (-e^{-x}) = 0 + e^{-x}$$ **Resultado marginal $X$:** $$\boxed{f_X(x) = e^{-x}, \quad x > 0}$$ _(Nota: $X$ sigue una distribución Exponencial con parámetro $\lambda = 1$)_.

#### Paso 2: Obtener la distribución marginal de $Y$ ($f_Y(y)$)

Fijamos $y$ y recorremos los valores de $x$. Según el soporte ($0 < x < y$), la variable $x$ está acotada inferiormente por 0 y superiormente por el valor actual de $y$.

**Desarrollo integral:** $$f_Y(y) = \int_{0}^{y} e^{-y} , dx$$ Como el integrando $e^{-y}$ no depende de $x$, se extrae de la integral: $$f_Y(y) = e^{-y} \int_{0}^{y} 1 , dx$$ $$f_Y(y) = e^{-y} [x]_{0}^{y} = e^{-y} (y - 0)$$ **Resultado marginal $Y$:** $$\boxed{f_Y(y) = y e^{-y}, \quad y > 0}$$ _(Nota: $Y$ sigue una distribución Gamma con $\alpha = 2$ y $\beta = 1$ o Erlang-2)_.

---

### 5. CÁLCULO DE LA PROBABILIDAD CONDICIONAL $P(X > 2 \mid Y < 4)$

#### Subpaso 5.1: Calcular el denominador $P(Y < 4)$

Utilizamos la marginal de $Y$ calculada en el paso anterior. $$P(Y < 4) = \int_{0}^{4} y e^{-y} , dy$$ Integramos por partes ($u = y, dv = e^{-y}dy \implies du = dy, v = -e^{-y}$): $$\int y e^{-y} dy = -y e^{-y} - \int -e^{-y} dy = -y e^{-y} - e^{-y} = -e^{-y}(y+1)$$ Evaluamos de 0 a 4: $$P(Y < 4) = [-e^{-4}(4+1)] - [-e^{0}(0+1)]$$ $$P(Y < 4) = -5e^{-4} + 1 \approx \mathbf{0.9084}$$

#### Subpaso 5.2: Calcular el numerador $P(X > 2 \cap Y < 4)$

Debemos integrar la conjunta sobre la región donde se cumplen tres condiciones simultáneamente: $x > 2$, $y < 4$ y el soporte original $y > x$. La región resultante es un triángulo con vértices en $(2,2)$, $(4,4)$ y $(2,4)$. Los límites son: $2 < x < 4$ y, para cada $x$, $x < y < 4$.

**Planteamiento de la integral doble:** $$P(X > 2, Y < 4) = \int_{2}^{4} \left( \int_{x}^{4} e^{-y} , dy \right) dx$$ _Integral interna (sobre $y$):_ $$\int_{x}^{4} e^{-y} , dy = [-e^{-y}]_{x}^{4} = e^{-x} - e^{-4}$$ _Integral externa (sobre $x$):_ $$P(X > 2, Y < 4) = \int_{2}^{4} (e^{-x} - e^{-4}) , dx$$ $$P(X > 2, Y < 4) = \left[ -e^{-x} - x e^{-4} \right]_{2}^{4}$$ Sustitución de valores: $$= (-e^{-4} - 4e^{-4}) - (-e^{-2} - 2e^{-4})$$ $$= -5e^{-4} + e^{-2} + 2e^{-4}$$ $$= e^{-2} - 3e^{-4} \approx \mathbf{0.0804}$$

#### Subpaso 5.3: Aplicación de la fórmula condicional

$$P(X > 2 \mid Y < 4) = \frac{e^{-2} - 3e^{-4}}{1 - 5e^{-4}}$$

---

### 6. RESULTADO FINAL

Evaluando numéricamente con $e \approx 2.71828$:

1. **Distribuciones Marginales:**
    - $f_X(x) = e^{-x}$ para $x > 0$.
    - $f_Y(y) = y e^{-y}$ para $y > 0$.
2. **Probabilidad Condicional:** $$P(X > 2 \mid Y < 4) = \frac{0.1353 - 0.0549}{1 - 0.0916} = \frac{0.0804}{0.9084}$$ $$\boxed{P(X > 2 \mid Y < 4) \approx 0.0885}$$

**Razonamiento:** La probabilidad es baja porque la condición $y > x$ restringe fuertemente el espacio para $x$ cuando limitamos $y$ a valores pequeños (menores a 4).