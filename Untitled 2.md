# T0 Números reales

## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Junto con el conjunto de los números reales $\mathbb{R}$, se supone la existencia de dos operaciones llamadas adición y multiplicación.

Sean $a, b, c \in \mathbb{R}$:

1. **Clausura**
    - $a + b \in \mathbb{R}$
    - $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    - $(a + b) + c = a + (b + c)$
    - $(a \cdot b)c = a(b \cdot c)$
4. **Existencia de elementos neutros**
    - $\exists 0 \in \mathbb{R} \mid a + 0 = a$ (0 es el neutro aditivo).
    - $\exists 1 \in \mathbb{R} \mid a \cdot 1 = a$ (1 es el neutro multiplicativo).
5. **Existencia de negativos (opuestos)**
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \mid a + (-a) = 0$
    - $-a$ se denomina el negativo de $a$.
6. **Existencia de inversos (recíprocos)**
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a}$ se denomina el recíproco o inverso de $a$.
7. **Distributividad**
    - $a(b + c) = ab + ac$

**Axiomas de igualdad** Sean $a, b, c \in \mathbb{R}$:

1. **Reflexividad**: $a = a$.
2. **Simetría**: $a = b \implies b = a$.
3. **Transitividad**: $(a = b \land b = c) \implies a = c$.

> [!note] La resta y la división son casos especiales de la suma y la multiplicación:
> 
> - **Resta**: $a - b = a + (-b)$
> - **División**: $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \quad b \neq 0$

**No confundir:**

- $2^3 = 8 \rightarrow$ **Igualdad**: verdad evidente.
- $x^2 - 4 = 0 \rightarrow$ **Ecuación**: verdad para algunos $x$.
- $x^2 - 4 = (x - 2)(x + 2) \rightarrow$ **Identidad**: verdad para todo $x \in \mathbb{R}$.

--- end-column ---

🔑 **Claves**

--- end-multi-column

> **Resumen:** Los axiomas de cuerpo definen las propiedades fundamentales de la suma y la multiplicación, estableciendo a $\mathbb{R}$ como una estructura algebraica cerrada y ordenada.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Sección I 3.2)**, los axiomas de cuerpo garantizan que la suma $x+y$ y el producto $xy$ están unívocamente determinados para cada par de números reales. Además, el sistema de axiomas permite deducir todas las leyes usuales del Álgebra elemental, como la unicidad del elemento neutro (0 y 1) y la ley de simplificación para la suma y multiplicación. Un conjunto que satisface estos axiomas de clausura, conmutatividad, asociatividad, existencia de neutros, opuestos, recíprocos y distributividad se denomina, en álgebra abstracta, un **Cuerpo**.