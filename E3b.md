**Enunciado:** Las variables aleatorias X,Y tienen la función de densidad de distribución de probabilidad conjunta que se indica:

fX,Y​(x,y)={π2​0​si x2+y2≤1,0≤y≤1en otro caso​

**Instrucción adicional:** Analice solo en los dos primeros cuadrantes.

**Se pide:**

- **a)** Encontrar la distribución marginal de X (fX​(x)).
- **b)** Encontrar la distribución marginal de Y (fY​(y)).



A continuación, se presenta la resolución detallada y pedagógica del ejercicio 3 del segundo parcial, siguiendo estrictamente el procedimiento técnico para el análisis de variables aleatorias continuas conjuntas.

---

### **1. Identificación de los datos del problema**

- **Función de densidad conjunta ($f_{X,Y}(x,y)$):** Es una constante $k = \frac{2}{\pi}$ dentro de una región específica. Esto indica una **distribución uniforme** sobre el área de soporte.
- **Región de soporte ($R$):** Definida por las inecuaciones:
    - $x^2 + y^2 \le 1$: El interior de un círculo unitario centrado en el origen.
    - $0 \le y \le 1$: La mitad superior del plano cartesiano.
- **Geometría:** La combinación de estas condiciones describe un **semicírculo unitario** situado en el semiplano superior (abarcando el primer y segundo cuadrante).
- **Límites de las variables:**
    - Para $y$: varía globalmente de $0$ a $1$.
    - Para $x$: varía globalmente de $-1$ a $1$.

---

### **2. Explicación de lo que se pide**

Se solicita encontrar las **funciones de densidad marginales** de las variables aleatorias $X$ e $Y$.

- La marginal de $X$ ($f_X(x)$) nos indica cómo se distribuye la probabilidad de $X$ individualmente, promediando (integrando) todos los posibles valores de $Y$ en cada punto $x$.
- La marginal de $Y$ ($f_Y(y)$) nos indica la distribución de probabilidad de $Y$ sola, integrando sobre todo el rango de $X$ para cada valor fijo de $y$.

---

### **3. Fórmulas utilizadas y justificación**

Según el **Formulario 806 II** y los textos de referencia:

1. **Densidad Marginal de $X$:** $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dy$$
2. **Densidad Marginal de $Y$:** $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx$$

**¿Por qué se usan estas fórmulas?** En variables continuas, la probabilidad conjunta se representa como un volumen bajo la superficie $f_{X,Y}(x,y)$. Para "proyectar" esta probabilidad sobre un solo eje (obtener la marginal), debemos acumular toda la masa de probabilidad existente en la dirección de la otra variable mediante una integral definida sobre la región de soporte.

---

### **4. Resolución Paso a Paso**

#### **a) Encontrar la distribución marginal de $X$ ($f_X(x)$)**

**Paso 1: Identificar los límites de integración para $y$.** De la ecuación de la frontera $x^2 + y^2 = 1$, despejamos $y$: $$y^2 = 1 - x^2 \implies y = \pm \sqrt{1 - x^2}$$ Como el enunciado restringe $0 \le y \le 1$, el límite inferior de integración es $0$ y el límite superior es la semicircunferencia superior: $y = \sqrt{1 - x^2}$.

**Paso 2: Plantear y resolver la integral.** Holding $x$ fixed, $y$ ranges from $0$ to $\sqrt{1-x^2}$: $$f_X(x) = \int_{0}^{\sqrt{1 - x^2}} \frac{2}{\pi} , dy$$

**Paso 3: Realizar la integración.** $$f_X(x) = \frac{2}{\pi} \left[ y \right]_{0}^{\sqrt{1 - x^2}}$$ $$f_X(x) = \frac{2}{\pi} \left( \sqrt{1 - x^2} - 0 \right)$$

**Resultado final de $f_X(x)$:** $$f_X(x) = \begin{cases} \frac{2\sqrt{1 - x^2}}{\pi} & \text{si } -1 \le x \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

#### **b) Encontrar la distribución marginal de $Y$ ($f_Y(y)$)**

**Paso 1: Identificar los límites de integración para $x$.** De la ecuación de la frontera $x^2 + y^2 = 1$, despejamos $x$: $$x^2 = 1 - y^2 \implies x = \pm \sqrt{1 - y^2}$$ Para un valor de $y$ fijo entre $0$ y $1$, la variable $x$ recorre el semicírculo desde el borde izquierdo (cuadrante II) hasta el derecho (cuadrante I). Por tanto, el límite inferior es $-\sqrt{1 - y^2}$ y el superior es $\sqrt{1 - y^2}$.

**Paso 2: Plantear y resolver la integral.** $$f_Y(y) = \int_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}} \frac{2}{\pi} , dx$$

**Paso 3: Realizar la integración.** $$f_Y(y) = \frac{2}{\pi} \left[ x \right]_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}}$$ $$f_Y(y) = \frac{2}{\pi} \left( \sqrt{1 - y^2} - (-\sqrt{1 - y^2}) \right)$$ $$f_Y(y) = \frac{2}{\pi} \left( 2\sqrt{1 - y^2} \right)$$

**Resultado final de $f_Y(y)$:** $$f_Y(y) = \begin{cases} \frac{4\sqrt{1 - y^2}}{\pi} & \text{si } 0 \le y \le 1 \ 0 & \text{en otro caso} \end{cases}$$

---

### **5. Verificación de los resultados**

Para que las marginales sean válidas, su integral sobre todo su dominio debe ser igual a 1.

- **Verificación para $f_X(x)$:** $\int_{-1}^{1} \frac{2}{\pi} \sqrt{1 - x^2} , dx$. Esta es la integral de una semicircunferencia multiplicada por una constante. Usando la sustitución trigonométrica $x = \sin\theta$: $\frac{2}{\pi} \int_{-\pi/2}^{\pi/2} \cos^2\theta , d\theta = \frac{2}{\pi} \left[ \frac{\theta}{2} + \frac{\sin 2\theta}{4} \right]_{-\pi/2}^{\pi/2} = \frac{2}{\pi} \left( \frac{\pi}{4} - (-\frac{\pi}{4}) \right) = \frac{2}{\pi} \cdot \frac{\pi}{2} = 1$. **Correcto.**
    
- **Verificación para $f_Y(y)$:** $\int_{0}^{1} \frac{4}{\pi} \sqrt{1 - y^2} , dy = \frac{4}{\pi} \left( \frac{\pi}{4} \right) = 1$. **Correcto.**
    

---

### **6. Gráfica en Desmos**

He generado el código para visualizar la región de soporte conjunta y las dos funciones marginales calculadas.

```
left=-1.5; right=1.5;
bottom=-0.5; top=1.5;
---
x^2+y^2<=1|y>=0|#a5d8ff  // Región de soporte (Semicírculo)
f(x)= (2*sqrt(1-x^2))/pi |RED| -1<=x<=1 // Marginal f_X(x)
g(x)= (4*sqrt(1-x^2))/pi |GREEN| 0<=x<=1 // Marginal f_Y(y) (graficada en eje x para ver forma)
(0,0)|label:Origen
```

**Explicación de la gráfica:**

- **Área Azul:** Representa el soporte del semicírculo unitario definido en el enunciado.
- **Línea Roja ($f(x)$):** Representa la densidad marginal de $X$. Note que es máxima en el centro ($x=0$) porque es donde hay más "grosor" de semicírculo en el eje $y$, y cae hacia cero en los extremos $\pm 1$.
- **Línea Verde ($g(x)$):** Representa la forma de la densidad marginal de $Y$. Al ser un semicírculo, la mayor concentración de probabilidad para $Y$ está cerca de $y=0$ (la base es más ancha).