Para resolver el **Ejercicio E1** de forma completa, utilizaremos las definiciones y procedimientos establecidos en el **Formulario 806 II** y los pasos de resolución detallados en la fuente **ejercicio_var.pdf**.

### **Enunciado del Ejercicio E1**

Sean las variables aleatorias $X, Y$ con función de densidad de probabilidad conjunta: $$f_{X,Y}(x,y) = \begin{cases} kx & \text{si } 0 \le x \le 1; x \le y \le 2-x \ 0 & \text{en otro caso} \end{cases}$$

---

### **a) Determinar el valor de $K$**

Según el formulario, para que una función sea de densidad válida, su integral sobre todo el rango debe ser igual a 1.

1. **Planteamiento:** $\int_0^1 \int_x^{2-x} kx , dy dx = 1$.
2. **Integración respecto a $y$:** $$\int_0^1 kx [y]_x^{2-x} dx = \int_0^1 kx [(2-x) - x] dx = \int_0^1 kx (2-2x) dx = 2k \int_0^1 (x - x^2) dx$$.
3. **Integración respecto a $x$:** $$2k \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2k \left( \frac{1}{2} - \frac{1}{3} \right) = 2k \left( \frac{1}{6} \right) = \frac{k}{3}$$.
4. **Resultado:** $\frac{k}{3} = 1 \implies \mathbf{k = 3}$.

---

### **b) Funciones de densidad marginales**

Usamos las fórmulas del formulario para proyectar la densidad sobre cada eje.

- **Marginal de $X$ ($f_X(x)$):** Integramos la conjunta respecto a $y$. $$f_X(x) = \int_x^{2-x} 3x , dy = 3x [y]_x^{2-x} = 3x(2-2x) = \mathbf{6x(1-x), \quad 0 \le x \le 1}$$.
- **Marginal de $Y$ ($f_Y(y)$):** La región es un triángulo. Debemos dividir la integral según el valor de $y$:
    1. Para $0 \le y \le 1$: $x$ varía de $0$ a $y \implies \int_0^y 3x , dx = \frac{3}{2}y^2$.
    2. Para $1 \le y \le 2$: $x$ varía de $0$ a $2-y \implies \int_0^{2-y} 3x , dx = \frac{3}{2}(2-y)^2$. $$\mathbf{f_Y(y) = \begin{cases} \frac{3}{2}y^2 & 0 \le y \le 1 \ \frac{3}{2}(2-y)^2 & 1 \le y \le 2 \end{cases}}$$.

---

### **c) Determinar si $X, Y$ son independientes**

Dos variables son independientes si y solo si $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$.

- Si tomamos el punto $(0.5, 0.5)$:
    - $f_{X,Y}(0.5, 0.5) = 3(0.5) = 1.5$.
    - $f_X(0.5) \cdot f_Y(0.5) = [6(0.5)(1-0.5)] \cdot [\frac{3}{2}(0.5)^2] = 1.5 \cdot 0.375 = 0.5625$.
- Como $1.5 \neq 0.5625$, se concluye que **$X$ e $Y$ no son independientes**.

---

### **d) Probabilidad $P(y \le \sqrt{x})$**

La región está acotada inferiormente por $y=x$ y superiormente por $y=\sqrt{x}$ dentro del rango de $X$. $$P(y \le \sqrt{x}) = \int_0^1 \int_x^{\sqrt{x}} 3x , dy dx = \int_0^1 3x(\sqrt{x} - x) dx = \int_0^1 (3x^{3/2} - 3x^2) dx$$ $$= \left[ \frac{6}{5}x^{5/2} - x^3 \right]_0^1 = \frac{6}{5} - 1 = \mathbf{0.2}$$.

---

### **e) Probabilidad $P(y \le 2x)$**

Es más sencillo usar el complemento: $P(y \le 2x) = 1 - P(y > 2x)$. La recta $y=2x$ corta a la frontera superior $y=2-x$ en $x=2/3$.

1. $P(y > 2x) = \int_0^{2/3} \int_{2x}^{2-x} 3x , dy dx = \int_0^{2/3} 3x(2-3x) dx = \int_0^{2/3} (6x-9x^2) dx$.
2. $[3x^2 - 3x^3]_0^{2/3} = 3(\frac{4}{9}) - 3(\frac{8}{27}) = \frac{4}{3} - \frac{8}{9} = \frac{4}{9}$.
3. **Resultado:** $1 - \frac{4}{9} = \mathbf{\frac{5}{9} \approx 0.5556}$.

---

### **f) Probabilidad de $P(y \le 3x / y \ge 2x)$**

Usamos la definición de probabilidad condicional: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

1. **Denominador:** $P(B) = P(y \ge 2x) = 4/9$ (calculado en el inciso anterior).
2. **Numerador:** $P(2x \le y \le 3x)$. Se divide en dos regiones: $x \in [0, 0.5]$ y $x \in [0.5, 2/3]$ debido a las fronteras $y=3x$ y $y=2-x$.
    - La integral total del numerador resulta en $7/36$.
3. **Resultado:** $\frac{7/36}{4/9} = \mathbf{\frac{7}{16} = 0.4375}$.

---

### **g) Hallar $E[X]$ y $VAR[X]$**

Usamos las fórmulas para una sola variable aplicadas a la marginal $f_X(x) = 6x - 6x^2$.

- **Esperanza:** $E[X] = \int_0^1 x(6x - 6x^2) dx = \int_0^1 (6x^2 - 6x^3) dx = [2x^3 - 1.5x^4]_0^1 = \mathbf{0.5}$.
- **Segundo momento:** $E[X^2] = \int_0^1 x^2(6x - 6x^2) dx = \int_0^1 (6x^3 - 6x^4) dx = [1.5x^4 - 1.2x^5]_0^1 = 0.3$.
- **Varianza:** $VAR[X] = 0.3 - (0.5)^2 = 0.3 - 0.25 = \mathbf{0.05}$.

---

### **Gráfica de la región de soporte y límites**

Para visualizar la región de integración y las rectas que definen las probabilidades solicitadas:

```desmos-graph
width=500; height=500
y=x|ORANGE|0<=x<=1
y=2-x|ORANGE|0<=x<=1
x=0|ORANGE|0<=y<=2
y>x|y<2-x|x>=0|#ffd700
y=\sqrt{x}|BLUE|DASHED|0<=x<=1|label:y=\sqrt{x}
y=2x|RED|DASHED|0<=x<=0.66|label:y=2x
y=3x|PURPLE|DASHED|0<=x<=0.5|label:y=3x
(1,1)|label:(1,1)
(0,2)|label:(0,2)
(0,0)|label:(0,0)
```

- **Área Amarilla:** Región donde la densidad es distinta de cero ($f_{X,Y} > 0$).
- **Línea Azul:** Límite para el inciso (d).
- **Línea Roja:** Límite para el inciso (e) y parte del (f).
- **Línea Morada:** Límite superior para el numerador del inciso (f).