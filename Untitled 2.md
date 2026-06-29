# Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a + b \in \mathbb{R}$ / $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a + b = b + a$ / $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - $(a + b) + c = a + (b + c)$ / $a \cdot (b \cdot c) = (a \cdot b) \cdot c$
4. **Existencia de neutros**
    
    - $\exists,0 \in \mathbb{R} \mid a + 0 = a$ (0 es el neutro para la suma "+")
    - $\exists,1 \in \mathbb{R} \mid a \cdot 1 = a$ (1 es el neutro para el producto "$\cdot$")
5. **Existencia de negativos**
    
    - $\forall,a \in \mathbb{R}, \exists,-a \in \mathbb{R} \mid a + (-a) = 0$ ($-a$ se denomina el negativo de $a$)
6. **Existencia de inversos**
    
    - $\forall,a \in \mathbb{R} - {0}, \exists,a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$ ($a^{-1} = \frac{1}{a}$ se denomina el inverso o recíproco de $a$)
7. **Distributividad**
    
    - $a(b + c) = ab + ac$

### Axiomas de igualdad

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    
    - $a = a$
2. **Simetría**
    
    - $a = b \Rightarrow b = a$
3. **Transitividad**
    
    - $(a = b \wedge b = c) \Rightarrow a = c$

> [!note] La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \text{ con } b \neq 0$

> [!important] **No confundir** $$ \begin{array}{rcl} 2^3 = 8 & \Rightarrow & \text{Igualdad (verdad evidente)} \ x^2 - 4 = 0 & \Rightarrow & \text{Ecuación (verdad para algunas } x) \ x^2 - 4 = (x - 2)(x + 2) & \Rightarrow & \text{Identidad (verdad para toda } x \in \mathbb{R}) \end{array} $$

--- end-column ---

🔑 **Claves**

Axiomas de cuerpo · Leyes fundamentales de $\mathbb{R}$ · Igualdad e Identidad.

¿Qué propiedades definen matemáticamente a los números reales como un cuerpo ordenado?

$$a(b+c) = ab + ac$$

--- end-multi-column

> **Resumen:** El sistema de los números reales se define a través de axiomas de cuerpo que rigen la suma, el producto y la igualdad, estableciendo las reglas para operar con neutros, inversos y distributividad.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con Apostol (Sección I 3.2), el sistema de los números reales se supone como un **cuerpo**, lo cual implica formalmente que la suma $x+y$ y el producto $xy$ están unívocamente determinados por el par $(x, y)$. Los axiomas de cuerpo garantizan que los elementos neutros ($0$ y $1$) son distintos entre sí y que el recíproco ($a^{-1}$) existe para todo elemento no nulo. Esta estructura axiomática permite deducir todas las leyes usuales del álgebra elemental como teoremas derivados de estas propiedades fundamentales. En términos de la teoría de conjuntos, el conjunto de los números reales $\mathbb{R}$ bajo estas operaciones constituye un ejemplo de un **campo ordenado completo**.



---



# T0 Números reales

## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-002

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Si $a, b, c \in \mathbb{R}$, se cumplen los siguientes axiomas:

1. **Clausura**
    - $a + b \in \mathbb{R} \wedge a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $i) \ a + b = b + a$
    - $ii) \ a \cdot b = b \cdot a$
3. **Asociatividad**
    - $i) \ (a + b) + c = a + (b + c)$
    - $ii) \ (a \cdot b)c = a(b \cdot c)$
4. **Existencia de neutros**
    - $i) \ \exists \ 0 \in \mathbb{R} \text{ tal que } a + 0 = a$ $\rightarrow 0 \text{ es el neutro para la suma } "+"$
    - $ii) \ \exists \ 1 \in \mathbb{R} \text{ tal que } a \cdot 1 = a$ $\rightarrow 1 \text{ es el neutro para el producto } "\times"$
5. **Existencia de negativos**
    - $\forall a \in \mathbb{R}, \exists \ -a \in \mathbb{R} \text{ tal que } a + (-a) = 0$ $-a \text{ es el negativo de } a$
6. **Existencia de inversos**
    - $\forall a \in \mathbb{R} - {0}, \exists \ a^{-1} \in \mathbb{R} \text{ tal que } a \cdot a^{-1} = 1$ $a^{-1} = \frac{1}{a} \text{ es el inverso de } a$
7. **Distributividad**
    - $a(b + c) = ab + ac$

### Axiomas de igualdad

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    - $a = a$
2. **Simetría**
    - $a = b \Rightarrow b = a$
3. **Transitividad**
    - $(a = b \wedge b = c) \Rightarrow a = c$

> [!note] Notas del manuscrito La **resta** y la **división** son solo casos especiales de la suma y el producto:
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \text{ con } b \neq 0$

**No confundir:**

- $2 + 3 = 5 \rightarrow$ **Igualdad:** es una verdad evidente.
- $x^2 - 4 = 0 \rightarrow$ **Ecuación:** verdad solo para algunos valores de $x$.
- $x^2 - 4 = (x - 2)(x + 2) \rightarrow$ **Identidad:** verdad para todo $x \in \mathbb{R}$.

--- end-column ---

🔑 **Claves** Axiomas de cuerpo · Neutros · Inversos · Clausura · Igualdad · Identidad

¿Cuáles son las reglas básicas que rigen las operaciones de suma y producto en el sistema de los números reales?

Fórmula clave (Distributividad): $a(b+c) = ab + ac$

--- end-multi-column

> **Resumen:** Los axiomas de cuerpo establecen las 7 propiedades fundamentales de la suma y el producto en $\mathbb{R}$, definiendo la existencia de elementos neutros e inversos.

> [!note] Complemento (Nivel B)
> 
> Según el texto de **Apostol (Vol. 1)**, el sistema de los números reales se define axiomáticamente como un **cuerpo ordenado**.
> 
> La definición formal refuerza que tanto la suma $x + y$ como el producto $xy$ están **unívocamente determinados** para cada par de números reales. Esto implica que los resultados de estas operaciones no solo pertenecen al conjunto (clausura), sino que son únicos para cada entrada.
> 
> Además, los axiomas de neutros (A4) especifican explícitamente que los números $0$ y $1$ deben ser **distintos** ($0 \neq 1$) para evitar que el sistema colapse en un conjunto con un solo elemento. Esta distinción es crucial para la estructura algebraica del cuerpo de los reales.