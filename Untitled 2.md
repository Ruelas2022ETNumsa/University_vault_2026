# Números reales y desigualdades

--- start-multi-column: cornell-T0-010

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

### Axiomas de cuerpo de los nros. $\mathbb{R}$

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a+b \in \mathbb{R}$ / $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a+b = b+a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - $i)\ (a+b)+c = a+(b+c)$
    - $ii)\ (a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    
    - $i.\ \exists 0 \in \mathbb{R} \mid a+0 = a$
        - $0$ es el neutro para la suma.
    - $ii.\ \exists 1 \in \mathbb{R} \mid a \cdot 1 = a$
        - $1$ es el neutro para la multiplicación.
5. **Existencia de negativos**
    
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \mid a + (-a) = 0$
    - $-a$ se denomina el negativo de $a$.
6. **Existencia de inversos**
    
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a}$ se denomina el recíproco o inverso de $a$.
7. **Distributividad**
    
    - $a(b+c) = ab + ac$

> [!note] Observaciones aclaratorias La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a-b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \text{ con } b \neq 0$

### Axiomas de igualdad

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    
    - $a = a$
2. **Simetría**
    
    - $a = b \implies b = a$
3. **Transitividad**
    
    - $(a = b \land b = c) \implies a = c$

> [!important] Notas del manuscrito No confundir los siguientes conceptos:
> 
> - $2^3 = 8$ : **Igualdad** (verdad evidente).
> - $x^2 - 4 = 0$ : **Ecuación** (verdad solo para algunos valores de $x$).
> - $x^2 - 4 = (x-2)(x+2)$ : **Identidad** (verdad para todo $x \in \mathbb{R}$).

--- end-column ---

🔑 **Claves**

Axioma · Cuerpo · Neutro · Inverso · Recíproco · Igualdad

¿Qué reglas rigen las operaciones básicas en el sistema de números reales? ¿Cómo se definen formalmente la resta y la división a partir de los axiomas de cuerpo? ¿Cuál es la diferencia fundamental entre una ecuación y una identidad matemática?

$\forall a \in \mathbb{R}, a+0=a$ $\forall a \in \mathbb{R}-{0}, a \cdot a^{-1}=1$

--- end-multi-column

> **Resumen:** Definición de las reglas operativas fundamentales (cuerpo) y de relación (igualdad) que estructuran el sistema de los números reales.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Sección I 3.2)**, el sistema de los números reales se postula como un **cuerpo ordenado con el axioma del extremo superior**. Los axiomas de cuerpo establecen que la suma y el producto están unívocamente determinados para cada par de números reales.
> 
> Un detalle formal importante omitido en el manuscrito es la **unicidad de los elementos neutros y opuestos**, la cual se deduce como teorema a partir de estos axiomas:
> 
> 1. **Unicidad del cero:** Si $a+b=a+c$, entonces $b=c$ (Ley de simplificación). Esto prueba que el número 0 es único.
> 2. **Unicidad del inverso:** Para cada $a \neq 0$, el recíproco $a^{-1}$ es único.
> 3. **Propiedad del producto nulo:** El teorema I.11 de Apostol establece que $ab=0$ si y solo si $a=0$ o $b=0$, propiedad fundamental para la resolución de ecuaciones.



--- start-multi-column: cornell-T0-002

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Axiomas de cuerpo de los números reales ($\mathbb{R}$)

Sea $a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a + b \in \mathbb{R}$ / $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - $(a + b) + c = a + (b + c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    
    - $\exists 0 \in \mathbb{R} \mid a + 0 = a$
    - $0$ es el neutro para la suma "+".
    - $\exists 1 \in \mathbb{R} \mid a \cdot 1 = a$
    - $1$ es el neutro para la multiplicación "$\cdot$".
5. **Existencia de negativos (opuestos)**
    
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \mid a + (-a) = 0$.
    - $-a$ se denomina el negativo de $a$.
6. **Existencia de inversos (recíprocos)**
    
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$.
    - $a^{-1} = \frac{1}{a}$ es el inverso de $a$.
7. **Distributividad**
    
    - $a(b + c) = ab + ac$.

### Axiomas de igualdad

Sea $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    
    - $a = a$
2. **Simetría**
    
    - $a = b \implies b = a$
3. **Transitividad**
    
    - $(a = b \land b = c) \implies a = c$

> [!note] Resta y división La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, b \neq 0$

> [!important] No confundir
> 
> - $2^3 = 8$ → Igualdad: es una verdad evidente.
> - $x^4 - 4 = 0$ → Ecuación: verdad para algunas "$x$".
> - $x^2 - 4 = (x - 2)(x + 2)$ → Identidad: verdad para toda $x \in \mathbb{R}$.

--- end-column ---

🔑 **Claves**

Cuerpo · Clausura · Neutro · Inverso · Identidad

¿Qué propiedades definen a los números reales como un "cuerpo"?

¿Cómo se definen formalmente la resta y la división a partir de los axiomas?

¿Cuál es la diferencia entre una ecuación y una identidad matemática?

$a(b+c) = ab+ac$

ver también: Teoremas de los números reales

no confundir elemento neutro con elemento inverso.

--- end-multi-column ---

> **Resumen:** Los axiomas de cuerpo establecen las reglas fundamentales de suma y multiplicación que permiten operar con los números reales bajo una estructura algebraica cerrada y consistente..

> [!note] Complemento (Nivel B)
> 
> Formalmente, el sistema de los números reales se define como un **cuerpo ordenado con el axioma del extremo superior**. Los axiomas de cuerpo (del 1 al 7) garantizan que para cada par de números reales $x$ e $y$, la suma $x+y$ y el producto $xy$ están unívocamente determinados.
> 
> Es fundamental notar que los axiomas de la existencia de neutros (A4) especifican que $0$ y $1$ son números reales **distintos**. Además, el axioma de existencia de inverso recíproco (A6) es el único que impone una restricción de dominio, pues el número $0$ no posee recíproco dentro del sistema de los números reales. De estos axiomas se derivan todas las leyes usuales del álgebra elemental, como la unicidad del cero y del uno, así como la regla de los signos.





A continuación se presentan ejercicios resueltos basados en los **Axiomas de Cuerpo**, extraídos y adaptados del libro **Apostol (Calculus, Vol. 1)**, los cuales demuestran cómo las leyes algebraicas fundamentales se derivan rigurosamente de los axiomas.

##### Ej. 1 Demostrar la Ley de simplificación para la suma: Si $a + b = a + c$, entonces $b = c$.

En virtud del **Axioma 5** (existencia de negativos), existe un número $y$ tal que $y + a = 0$. Sumando $y$ a ambos miembros de la igualdad original: $$\begin{array}{rcl} y + (a + b) & = & y + (a + c) \ (y + a) + b & = & (y + a) + c \quad \text{(por Axioma 2: Asociatividad)} \ 0 + b & = & 0 + c \quad \text{(por Axioma 5)} \ b & = & c \quad \text{(por Axioma 4: Neutro)} \end{array}$$

> [!note] Este ejercicio demuestra que el elemento neutro $0$ es único. Si existieran dos neutros $0$ y $0'$, se cumpliría $0 + 0' = 0$ y $0 + 0 = 0$, lo que por simplificación implica $0 = 0'$.

##### Ej. 2 Demostrar la propiedad del producto por cero: $a \cdot 0 = 0$ para cualquier número real $a$.

Partimos de la propiedad del neutro aditivo $0 + 0 = 0$. Aplicando el **Axioma 7** (distributividad): $$\begin{array}{rcl} a \cdot (0 + 0) & = & a \cdot 0 \ a \cdot 0 + a \cdot 0 & = & a \cdot 0 \end{array}$$ Por el **Axioma 4**, sabemos que $a \cdot 0 + 0 = a \cdot 0$, por lo tanto: $$\begin{array}{rcl} a \cdot 0 + a \cdot 0 & = & a \cdot 0 + 0 \end{array}$$ Aplicando la **Ley de simplificación** (Ej. 1), cancelamos $a \cdot 0$ en ambos lados, resultando: $$\begin{array}{rcl} a \cdot 0 & = & 0 \end{array}$$.

##### Ej. 3 Demostrar la regla de los signos para el producto de negativos: $(-a)(-b) = ab$.

Para demostrar esto, primero es útil establecer que $(-a)b = -(ab)$. Consideramos la suma $ab + (-a)b$. Por distributividad: $$\begin{array}{rcl} ab + (-a)b & = & [a + (-a)]b \ ab + (-a)b & = & 0 \cdot b \quad \text{(por Axioma 5)} \ ab + (-a)b & = & 0 \quad \text{(por Ej. 2)} \end{array}$$ Esto indica que $(-a)b$ es el opuesto de $ab$. Ahora, para $(-a)(-b)$: $$\begin{array}{rcl} (-a)(-b) & = & -[a(-b)] \ (-a)(-b) & = & -[-(ab)] \quad \text{(aplicando la misma lógica al segundo factor)} \end{array}$$ Finalmente, por el teorema de la doble negación $-(-x) = x$, concluimos: $$\begin{array}{rcl} (-a)(-b) & = & ab \end{array}$$.

##### Ej. 4 Demostrar la unicidad del recíproco: Si $a \neq 0$ y $ab = 1$, entonces $b = a^{-1}$.

Supongamos que $b$ y $a^{-1}$ son ambos recíprocos de $a$. Por definición del **Axioma 6**: $$\begin{array}{rcl} a \cdot b & = & 1 \ a \cdot a^{-1} & = & 1 \end{array}$$ Igualando ambas expresiones: $$\begin{array}{rcl} a \cdot b & = & a \cdot a^{-1} \end{array}$$ Dado que $a \neq 0$, multiplicamos por $a^{-1}$ en ambos lados: $$\begin{array}{rcl} a^{-1} \cdot (a \cdot b) & = & a^{-1} \cdot (a \cdot a^{-1}) \ (a^{-1} \cdot a) \cdot b & = & (a^{-1} \cdot a) \cdot a^{-1} \quad \text{(Asociatividad)} \ 1 \cdot b & = & 1 \cdot a^{-1} \ b & = & a^{-1} \end{array}$$.











