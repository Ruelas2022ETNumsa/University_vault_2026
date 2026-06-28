## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

$a, b, c \in \mathbb{R}$

1. **Clausura**
    
    - $a+b \in \mathbb{R}$ / $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a+b = b+a$ / $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - $(a+b)+c = a+(b+c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **$\exists$ de neutros**
    
    - $\exists,0 \in \mathbb{R} \ni a+0 = a$ ($0$ neutro para "$+$")
    - $\exists,1 \in \mathbb{R} \ni a \cdot 1 = a$ ($1$ neutro para "$\cdot$")
5. **$\exists$ de negativos**
    
    - $\forall a \in \mathbb{R} ;\exists -a \in \mathbb{R} \ni a+(-a)=0$
    - $-a$ se denomina el negativo de $a$.
6. **$\exists$ de inversos**
    
    - $\forall a \in \mathbb{R} - {0} ;\exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1}=1$
    - $a^{-1} = \frac{1}{a}$ se denomina el inverso de $a$.
7. **Distributividad**
    
    - $a(b+c) = ab+ac$

--- end-column ---

🔑 **Claves**

--- end-multi-column

> **Resumen:** Definición de las reglas fundamentales que rigen las operaciones de adición y multiplicación en el conjunto de los números reales.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con Apostol, el sistema de los números reales se define formalmente como un **cuerpo** bajo las operaciones de adición ($+$) y multiplicación ($\cdot$), las cuales asignan a cada par de números reales $x$ e $y$ un número real único ($x+y$ y $xy$ respectivamente).
> 
> Un aspecto fundamental del **Axioma 4 (Existencia de elementos neutros)** es que los números $0$ y $1$ deben ser distintos entre sí. Asimismo, se establece que a partir de estos axiomas se pueden deducir todas las leyes usuales del álgebra elemental, como la unicidad del neutro y la posibilidad de la sustracción y división.

## Ejercicios resueltos: Axiomas de cuerpo de los números reales

Los siguientes ejercicios muestran cómo utilizar los axiomas de cuerpo para demostrar las propiedades fundamentales del álgebra.

1. **Ej.** Demostrar la ley de simplificación para la suma: Si $a+b=a+c$, entonces $b=c$.
    
    - **Solución:** $\begin{array}{rcl} a+b & = & a+c \ \exists, y \in \mathbb{R} \ni y+a & = & 0 \quad (\text{Axioma 5}) \ y+(a+b) & = & y+(a+c) \ (y+a)+b & = & (y+a)+c \quad (\text{Asociatividad}) \ 0+b & = & 0+c \ b & = & c \quad (\text{Neutro aditivo}) \end{array}$ Este teorema también prueba que el elemento neutro $0$ es único.
2. **Ej.** Demostrar que para todo número real $a$, se cumple que $0 \cdot a = 0$.
    
    - **Solución:** Sea $z = 0 \cdot a$. $\begin{array}{rcl} z+z & = & 0 \cdot a + 0 \cdot a \ z+z & = & (0+0) \cdot a \quad (\text{Distributividad}) \ z+z & = & 0 \cdot a \ z+z & = & z \end{array}$ Sumando el opuesto $-z$ a ambos miembros: $\begin{array}{rcl} (z+z)+(-z) & = & z+(-z) \ z+(z+(-z)) & = & 0 \ z+0 & = & 0 \ z & = & 0 \end{array}$ Por lo tanto, $0 \cdot a = 0$.
3. **Ej.** Demostrar la regla de los signos para el producto: $(-a)b = -(ab)$.
    
    - **Solución:** Sea $z = (-a)b$. Para demostrar que es el negativo de $ab$, sumamos $z$ con $ab$: $\begin{array}{rcl} z + ab & = & (-a)b + ab \ z + ab & = & (-a + a)b \quad (\text{Distributividad}) \ z + ab & = & 0 \cdot b \quad (\text{Axioma 5}) \ z + ab & = & 0 \quad (\text{Teorema anterior}) \end{array}$ Como la suma da el neutro $0$, $z$ es por definición el negativo de $ab$, es decir, $(-a)b = -(ab)$.
4. **Ej.** Demostrar que el negativo de la suma es la suma de los negativos: $-(a+b) = -a-b$.
    
    - **Solución:** Debemos verificar que $(a+b) + [(-a)+(-b)] = 0$. $\begin{array}{rcl} (a+b) + [(-a)+(-b)] & = & a + [b + ((-a)+(-b))] \quad (\text{Asociatividad}) \ & = & a + [(-a) + (b + (-b))] \quad (\text{Conmutatividad}) \ & = & (a + (-a)) + (b + (-b)) \quad (\text{Asociatividad}) \ & = & 0 + 0 \quad (\text{Axioma 5}) \ & = & 0 \end{array}$ Debido a la unicidad del elemento negativo, se concluye que $-(a+b) = -a-b$.