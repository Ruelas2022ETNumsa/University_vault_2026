### **Desarrollo Muestra a Muestra**

Dada la ecuación en diferencias recursiva:

$$
y(n) = 2y(n-1) + x(n)
$$


Con la entrada $x(n) = \delta(n)$, sabemos que:

$$
x(n) = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}
$$


Sustituyendo paso a paso para cada índice $n$ con la condición inicial $y(-1) = 0$:

*   **Para $n = 0$:**
    
$$
y(0) = 2y(-1) + x(0) = 2(0) + 1 = 1
$$


*   **Para $n = 1$:**
    
$$
y(1) = 2y(0) + x(1) = 2(1) + 0 = 2
$$


*   **Para $n = 2$:**
    
$$
y(2) = 2y(1) + x(2) = 2(2) + 0 = 4
$$


*   **Para $n = 3$:**
    
$$
y(3) = 2y(2) + x(3) = 2(4) + 0 = 8
$$


*   **Para $n = 4$:**
    
$$
y(4) = 2y(3) + x(4) = 2(8) + 0 = 16
$$


*   **Para $n = 5$:**
    
$$
y(5) = 2y(4) + x(5) = 2(16) + 0 = 32
$$


La secuencia resultante de salida en este intervalo es:

$$
y(n) = \{1, \quad 2, \quad 4, \quad 8, \quad 16, \quad 32\} \quad \text{para } n = 0, 1, 2, 3, 4, 5
$$


La forma general de la respuesta (que corresponde a la respuesta al impulso $h(n)$ por ser $x(n) = \delta(n)$) es:

$$
y(n) = 2^n u(n)
$$


---

### **Análisis de Estabilidad en el Dominio Z**

Para obtener la función de transferencia $H(z)$, aplicamos la transformada Z a ambos lados de la ecuación en diferencias bajo condiciones de reposo inicial:

$$
Y(z) = 2z^{-1}Y(z) + X(z)
$$


Agrupamos los términos de la salida $Y(z)$:

$$
Y(z)(1 - 2z^{-1}) = X(z)
$$


Despejamos la relación de transferencia $H(z) = \frac{Y(z)}{X(z)}$:

$$
H(z) = \frac{1}{1 - 2z^{-1}} = \frac{z}{z - 2}
$$


#### **1. Identificación del Polo**
El polo del sistema se obtiene al igualar el denominador de $H(z)$ a cero:

$$
z - 2 = 0 \implies z_p = 2
$$


El sistema posee un único polo real en **$z_p = 2$**.

#### **2. Criterio de Estabilidad**
*   Un sistema LTI discreto y causal es estable en el sentido BIBO si y solo si todos los polos de su función de transferencia se ubican estrictamente dentro del círculo unitario en el plano Z, es decir, sus magnitudes deben ser menores que la unidad ($|z_i| < 1$).
*   Evaluando el módulo de nuestro polo:
    
$$
|z_p| = |2| = 2 > 1
$$


Dado que el polo cae **fuera del círculo unitario**, la región de convergencia del sistema causal ($\text{ROC: } |z| > 2$) no incluye la circunferencia de radio unitario ($|z| = 1$).

---

### **Resultado Final**

*   **Valores calculados:** 
    
$$
y(0)=1, \quad y(1)=2, \quad y(2)=4, \quad y(3)=8, \quad y(4)=16, \quad y(5)=32
$$

*   **Polo del sistema:** 
    
$$
z_p = 2
$$

*   **Estabilidad:** El sistema es **inestable** porque su polo está fuera del círculo unitario ($|z_p| > 1$).
