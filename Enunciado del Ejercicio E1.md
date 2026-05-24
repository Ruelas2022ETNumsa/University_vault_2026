Para resolver este ejercicio paso a paso, utilizaremos las fórmulas de variables aleatorias continuas múltiples detalladas en el **Formulario 806 II**.

### **Enunciado del Ejercicio E1**

Sean las variables aleatorias $X, Y$ con densidad de distribución conjunta: $$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 1; x \le y \le 2-x \ 0 & \text{en otro caso} \end{cases}$$

---

### **a) Determinar el valor de $k$**

Para que sea una función de densidad válida, la integral doble sobre todo el rango debe ser igual a 1.

1. **Plantear la integral:** $\int_0^1 \int_x^{2-x} kx , dy dx = 1$.
2. **Integrar respecto a $y$:** $$\int_0^1 kx [y]_x^{2-x} dx = \int_0^1 kx [(2-x) - x] dx = \int_0^1 kx (2-2x) dx = 2k \int_0^1 (x - x^2) dx$$
3. **Integrar respecto a $x$:** $$2k \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2k \left( \frac{1}{2} - \frac{1}{3} \right) = 2k \left( \frac{1}{6} \right) = \frac{k}{3}$$
4. **Despejar $k$:** $\frac{k}{3} = 1 \implies \mathbf{k = 3}$.

---

### **b) Funciones de densidad marginales**

Usamos las fórmulas para proyectar la densidad conjunta sobre cada eje.

- **Marginal de $X$ ($f_X(x)$):** $$f_X(x) = \int_x^{2-x} 3x , dy = 3x [y]_x^{2-x} = 3x(2-2x) = \mathbf{6x(1-x), \quad 0 \le x \le 1}$$.
- **Marginal de $Y$ ($f_Y(y)$):** La región es un triángulo con vértices en (0,0), (1,1) y (0,2). Debemos dividir la integral:
    1. Si $0 \le y \le 1$, $x$ va de $0$ a $y$: $\int_0^y 3x , dx = \frac{3}{2}y^2$.
    2. Si $1 \le y \le 2$, $x$ va de $0$ a $2-y$: $\int_0^{2-y} 3x , dx = \frac{3}{2}(2-y)^2$. $$\mathbf{f_Y(y) = \begin{cases} \frac{3}{2}y^2 & 0 \le y \le 1 \ \frac{3}{2}(2-y)^2 & 1 \le y \le 2 \end{cases}}$$.

---

### **c) Determinar si $X, Y$ son independientes**

Dos variables son independientes si $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$. Tomando un punto como (0.5, 0.5):

- $f_{X,Y}(0.5, 0.5) = 3(0.5) = 1.5$.
- $f_X(0.5) \cdot f_Y(0.5) = [6(0.5)(1-0.5)] \cdot [\frac{3}{2}(0.5)^2] = 1.5 \cdot 0.375 = 0.5625$. Como $1.5 \neq 0.5625$, concluye que **$X$ e $Y$ no son independientes**.

---

### **d) Probabilidad $P(Y \le \sqrt{x})$**

La región está acotada por $y=x$ (inferior) y $y=\sqrt{x}$ (superior) dentro del rango $0 \le x \le 1$: $$P(Y \le \sqrt{x}) = \int_0^1 \int_x^{\sqrt{x}} 3x , dy dx = \int_0^1 3x(\sqrt{x} - x) dx = \int_0^1 (3x^{3/2} - 3x^2) dx$$ $$= \left[ \frac{6}{5}x^{5/2} - x^3 \right]_0^1 = \frac{6}{5} - 1 = \mathbf{\frac{1}{5} = 0.2}$$.

---

### **e) Probabilidad $P(Y \le 2x)$**

Usamos el complemento: $P(Y \le 2x) = 1 - P(Y > 2x)$. El área donde $y > 2x$ ocurre de $x=0$ hasta el cruce de $y=2x$ con $y=2-x$ (en $x=2/3$).

1. $P(Y > 2x) = \int_0^{2/3} \int_{2x}^{2-x} 3x , dy dx = \int_0^{2/3} 3x(2-3x) dx = \int_0^{2/3} (6x-9x^2) dx$
2. $[3x^2 - 3x^3]_0^{2/3} = 3(\frac{4}{9}) - 3(\frac{8}{27}) = \frac{4}{3} - \frac{8}{9} = \frac{4}{9}$.
3. $P(Y \le 2x) = 1 - \frac{4}{9} = \mathbf{\frac{5}{9}}$.

---

### **f) Probabilidad $P(Y \le 3x \mid Y \ge 2x)$**

Por definición de probabilidad condicional: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

1. $P(B) = P(Y \ge 2x) = 4/9$ (calculado en el inciso anterior).
2. $P(A \cap B) = P(2x \le Y \le 3x)$. Esta región se divide en $x \in [0, 1/2]$ y $x \in [1/2, 2/3]$ debido a las rectas de frontera.
3. La integral resulta en $7/36$.
4. Resultado: $\frac{7/36}{4/9} = \mathbf{\frac{7}{16} = 0.4375}$.

---

### **g) Hallar $E[X]$ y $VAR[X]$**

Usamos la densidad marginal $f_X(x) = 6x - 6x^2$ y las fórmulas del formulario:

- **Esperanza:** $E[X] = \int_0^1 x(6x - 6x^2) dx = \int_0^1 (6x^2 - 6x^3) dx = [2x^3 - 1.5x^4]_0^1 = \mathbf{0.5}$.
- **Segundo momento:** $E[X^2] = \int_0^1 x^2(6x - 6x^2) dx = \int_0^1 (6x^3 - 6x^4) dx = [1.5x^4 - 1.2x^5]_0^1 = 0.3$.
- **Varianza:** $VAR[X] = E[X^2] - (E[X])^2 = 0.3 - (0.5)^2 = \mathbf{0.05}$.