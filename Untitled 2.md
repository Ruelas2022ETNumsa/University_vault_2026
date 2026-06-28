## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo** Sean $a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a+b \in \mathbb{R}$
    - $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a+b = b+a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - $(a+b)+c = a+(b+c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    
    - $\exists 0 \in \mathbb{R} \ni a+0 = a$ (0 es el elemento neutro para la suma).
    - $\exists 1 \in \mathbb{R} \ni a \cdot 1 = a$ (1 es el elemento neutro para la multiplicación).
5. **Existencia de negativos**
    
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \ni a+(-a) = 0$ ($-a$ se denomina el negativo de $a$).
6. **Existencia de inversos**
    
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1} = 1$ ($a^{-1} = \frac{1}{a}$ es el inverso o recíproco de $a$, con $a \neq 0$).
7. **Distributividad**
    
    - $a(b+c) = ab + ac$

> [!note] Observaciones aclaratorias La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a-b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}$, con $b \neq 0$

--- end-column ---

🔑 **Claves**

--- end-multi-column

> **Resumen:** Los axiomas de cuerpo establecen las propiedades fundamentales de las operaciones de adición y multiplicación que rigen el sistema de los números reales.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con el texto de Apostol, el sistema de los números reales se toma como un concepto primitivo (no definido) que satisface este conjunto de axiomas.
> 
> Un detalle formal importante omitido en el manuscrito es que los elementos neutros $0$ y $1$ deben ser **distintos** ($0 \neq 1$) para que la estructura de cuerpo sea consistente. A partir de estos seis axiomas se pueden deducir por teorema todas las leyes usuales del álgebra elemental, tales como la ley de simplificación, la unicidad del neutro y las reglas de los signos.


A continuación se presentan ejercicios resueltos basados en los teoremas y propiedades derivados de los axiomas de cuerpo, extraídos de las fuentes bibliográficas.

**Ej. 1** Demostrar la **Ley de simplificación para la suma**: si $a + b = a + c$, entonces $b = c$. Solución: Sea $y$ el número real tal que $a + y = 0$ (el negativo de $a$, cuya existencia garantiza el Axioma 5). $\begin{array}{rcl} a + b & = & a + c \ (a + b) + y & = & (a + c) + y \ (b + a) + y & = & (c + a) + y \quad \text{(Axioma 2: Conmutatividad)} \ b + (a + y) & = & c + (a + y) \quad \text{(Axioma 3: Asociatividad)} \ b + 0 & = & c + 0 \quad \text{(Axioma 4: Existencia de neutros)} \ b & = & c \quad \text{(Axioma 4: Propiedad del neutro)} \end{array}$

**Ej. 2** Demostrar que para todo número real $a$, se cumple que **$a \cdot 0 = 0$**. Solución: $\begin{array}{rcl} a \cdot 0 + a \cdot 0 & = & a \cdot (0 + 0) \quad \text{(Axioma 7: Distributividad)} \ a \cdot 0 + a \cdot 0 & = & a \cdot 0 \quad \text{(Axioma 4: El 0 es neutro)} \ a \cdot 0 + a \cdot 0 & = & a \cdot 0 + 0 \quad \text{(Axioma 4: El 0 es neutro)} \end{array}$ Aplicando la ley de simplificación para la suma (demostrada en el Ej. 1), podemos cancelar $a \cdot 0$ de ambos miembros: $a \cdot 0 = 0$

**Ej. 3** Demostrar que si $a \cdot b = 0$, entonces **$a = 0$** o **$b = 0$**. Solución: Supongamos que $a \cdot b = 0$. Si $a = 0$, la proposición se cumple. Si $a \neq 0$, entonces existe el recíproco $a^{-1}$ tal que $a \cdot a^{-1} = 1$ (Axioma 6). Multiplicamos la ecuación original por $a^{-1}$: $\begin{array}{rcl} a^{-1} \cdot (a \cdot b) & = & a^{-1} \cdot 0 \ (a^{-1} \cdot a) \cdot b & = & 0 \quad \text{(Axioma 3: Asociatividad y Teorema } a \cdot 0 = 0) \ 1 \cdot b & = & 0 \quad \text{(Axioma 6: Existencia del recíproco)} \ b & = & 0 \quad \text{(Axioma 4: El 1 es neutro)} \end{array}$ Por lo tanto, al menos uno de los dos debe ser cero.

> [!note] Estas demostraciones ilustran cómo el sistema de los números reales se construye de forma puramente deductiva a partir de sus siete axiomas básicos, tal como se indica en la fuente Apostol.





A continuación se presentan ejercicios resueltos basados en los **Axiomas de cuerpo**, extrayendo las demostraciones formales de las leyes algebraicas fundamentales a partir de los axiomas postulados en el sistema de números reales de **Apostol**.

##### Ej. Demostrar la Ley de simplificación para la suma: si $a + b = a + c$, entonces $b = c$.

En virtud del **Axioma 5** (existencia de negativos), existe un número $y$ tal que $y + a = 0$. Partiendo de la igualdad dada: $$a + b = a + c$$ Sumamos $y$ a ambos miembros: $$y + (a + b) = y + (a + c)$$ Aplicando el **Axioma 2** (propiedad asociativa): $$(y + a) + b = (y + a) + c$$ Sustituyendo $y + a = 0$: $$0 + b = 0 + c$$ Finalmente, por el **Axioma 4** (elemento neutro), $0 + b = b$ y $0 + c = c$, por lo tanto: $$b = c$$

> [!note] Esta demostración prueba además que el elemento neutro $0$ es único.

##### Ej. Demostrar la posibilidad de la sustracción: Dados $a$ y $b$, existe uno y solo un $x$ tal que $a + x = b$.

Para demostrar la existencia, elegimos $y$ de manera que $a + y = 0$ (por Axioma 5) y definimos $x = y + b$. Comprobamos: $$a + x = a + (y + b)$$ Por **Axioma 2** (asociatividad): $$a + x = (a + y) + b = 0 + b = b$$ Para demostrar la unicidad, supongamos que existen dos soluciones $x$ y $z$ tales que $a + x = b$ y $a + z = b$. Entonces: $$a + x = a + z$$ Por la **Ley de simplificación** demostrada anteriormente, se concluye que $x = z$. Este valor único se designa por $b - a$.

##### Ej. Demostrar que el negativo de un negativo es el número original: $-(-a) = a$.

Por definición de elemento negativo (**Axioma 5**), se tiene que: $$a + (-a) = 0$$ Esta igualdad indica que $a$ es un número que, sumado a $(-a)$, da el neutro $0$. Sin embargo, el negativo de $(-a)$, denotado como $-(-a)$, es por definición el único número que sumado a $(-a)$ da $0$: $$-(-a) + (-a) = 0$$ Por la unicidad de los elementos opuestos (Teorema I.2 de Apostol), se concluye que: $$a = -(-a)$$

##### Ej. Demostrar que $b - a = b + (-a)$.

Sea $x = b - a$ y sea $y = b + (-a)$. Debemos probar que $x = y$. Por definición de sustracción, sabemos que $x + a = b$. Evaluamos ahora la suma de $y$ con $a$: $$y + a = [b + (-a)] + a$$ Aplicando el **Axioma 2** (asociatividad): $$y + a = b + [(-a) + a]$$ Por el **Axioma 5** (negativos), $(-a) + a = 0$: $$y + a = b + 0$$ Por el **Axioma 4** (neutros): $$y + a = b$$ Como $x + a = b$ y $y + a = b$, entonces $x + a = y + a$. Aplicando la **Ley de simplificación**, resulta $x = y$, es decir: $$b - a = b + (-a)$$