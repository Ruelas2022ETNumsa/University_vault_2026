--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

**Axiomas de cuerpo de los números reales $\mathbb{R}$**

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a + b \in \mathbb{R}$
    - $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - i) $(a + b) + c = a + (b + c)$
    - ii) $a(b \cdot c) = (a \cdot b)c$
4. **Existencia de elementos neutros**
    
    - i) $\exists 0 \in \mathbb{R} \text{ tal que } a + 0 = a$
        - $0$ es el neutro para la suma "+".
    - ii) $\exists 1 \in \mathbb{R} \text{ tal que } a \cdot 1 = a$
        - $1$ es el neutro para el producto "$\cdot$".
5. **Existencia de negativos (Opuestos)**
    
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \text{ tal que } a + (-a) = 0$
    - $-a$ se denomina el negativo de $a$.
6. **Existencia de inversos (Recíprocos)**
    
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \text{ tal que } a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a}$ es el inverso de $a$.
7. **Distributividad**
    
    - $a(b + c) = ab + ac$

### Axiomas de igualdad

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    
    - $a = a$
2. **Simetria**
    
    - $a = b \Rightarrow b = a$
3. **Transitividad**
    
    - $(a = b \wedge b = c) \Rightarrow a = c$

> [!note] Observaciones aclaratorias La resta y la división son solo casos especiales de la suma y el producto:
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}; \quad b \neq 0$

> [!important] No confundir
> 
> - $2^3 = 8 \rightarrow$ **Igualdad:** Verdad evidente.
> - $x^2 - 4 = 0 \rightarrow$ **Ecuación:** Verdad para algunos valores de $x$.
> - $x^2 - 4 = (x - 2)(x + 2) \rightarrow$ **Identidad:** Verdad para todo $x \in \mathbb{R}$.

--- end-column ---

🔑 **Claves**

Axiomas de cuerpo · Elementos neutros · Opuestos · Recíprocos · Identidad

¿Qué propiedades garantizan que $\mathbb{R}$ sea un sistema algebraico cerrado? ¿Cuál es la distinción formal entre una ecuación y una identidad?

$(a = b \wedge b = c) \Rightarrow a = c$

ver también: Axiomas de orden

No confundir la resta como operación primitiva; es la suma con el elemento opuesto.

--- end-multi-column ---

> **Resumen:** El sistema de los números reales se define algebraicamente como un cuerpo donde la suma y el producto cumplen propiedades de clausura, conmutatividad, asociatividad, existencia de neutros, inversos y distributividad.

> [!note] Complemento (Nivel B)
> 
> Formalmente, el sistema de los números reales se postula como un **cuerpo ordenado con la propiedad del extremo superior** (axioma de completitud). Según Apostol, los axiomas de cuerpo establecen que la suma y el producto están unívocamente determinados para cada par de números reales. Un detalle técnico omitido en el manuscrito, pero fundamental en la definición formal, es que los elementos neutros $0$ y $1$ deben ser distintos ($0 \neq 1$) para evitar que el cuerpo sea trivial. A partir de estos axiomas se deducen todas las leyes del Álgebra elemental como teoremas, incluyendo la unicidad del cero y del uno, así como la ley de simplificación ($a + b = a + c \Rightarrow b = c$).




##### Ej. 1 Demostrar que $0 \cdot a = 0$ para cualquier número real $a$.

Para la demostración se utilizan los axiomas de elemento neutro, distributividad y la ley de simplificación: $$\begin{array}{rcl} a \cdot 1 & = & a \cdot (1 + 0) \ a & = & a \cdot 1 + a \cdot 0 \ a + 0 & = & a + a \cdot 0 \ 0 & = & a \cdot 0 \end{array}$$

> [!note] Este resultado es fundamental para asegurar que el producto por cero anula cualquier cantidad en el cuerpo de los reales.

##### Ej. 2 Demostrar la Ley de Simplificación para la suma: si $a + b = a + c$, entonces $b = c$.

A partir de la existencia del opuesto (axioma 5) y la asociatividad (axioma 3): $$\begin{array}{rcl} a + b & = & a + c \ \text{Sea } y \text{ tal que } y + a & = & 0 \ y + (a + b) & = & y + (a + c) \ (y + a) + b & = & (y + a) + c \ 0 + b & = & 0 + c \ b & = & c \end{array}$$

> [!note] De forma análoga se puede demostrar la ley de simplificación para la multiplicación siempre que el factor común sea distinto de cero.

##### Ej. 3 Determinar si la afirmación $(p + q)^2 = p^2 + q^2$ es una identidad basándose en los axiomas de cuerpo.

Falsa. Aplicando la propiedad distributiva (Axioma 7) de forma iterada: $$\begin{array}{rcl} (p + q)^2 & = & (p + q)(p + q) \ & = & p(p + q) + q(p + q) \ & = & p^2 + pq + qp + q^2 \end{array}$$ Por la propiedad conmutativa (Axioma 2), $pq = qp$, por lo tanto: $$(p + q)^2 = p^2 + 2pq + q^2$$ La igualdad solo es verdadera si $2pq = 0$, por lo que no se cumple para todo $p, q \in \mathbb{R}$.