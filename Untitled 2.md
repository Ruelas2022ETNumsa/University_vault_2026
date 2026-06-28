## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-T0-001

```
column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

$\forall a, b, c \in \mathbb{R}$:

1. **Clausura**
    
    - $a + b \in \mathbb{R}$ / $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    
    - i) $(a + b) + c = a + (b + c)$
    - ii) $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    
    - i) $\exists, 0 \in \mathbb{R} \mid a + 0 = a$
        - $0$ es el neutro para la suma "+"
    - ii) $\exists, 1 \in \mathbb{R} \mid a \cdot 1 = a$
        - $1$ es el neutro para la multiplicación "$\cdot$"
5. **Existencia de negativos**
    
    - $\forall a \in \mathbb{R}, \exists, -a \in \mathbb{R} \mid a + (-a) = 0$
    - $-a$ se denomina el negativo de $a$
6. **Existencia de inversos**
    
    - $\forall a \in \mathbb{R} - {0}, \exists, a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a}$ se denomina el inverso de $a$
7. **Distributividad**
    
    - $a(b + c) = ab + ac$

> [!note] Observaciones aclaratorias La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, b \neq 0$

> [!important] No confundir
> 
> - $2 + 3 = 5 \rightarrow$ Igualdad (verdad evidente).
> - $x^2 - 4 = 0 \rightarrow$ Ecuación (verdad para algunos valores de $x$).
> - $x^2 - 4 = (x - 2)(x + 2) \rightarrow$ Identidad (verdad para todo $x \in \mathbb{R}$).

### Teoremas sobre números reales

$\forall a, b, c, d, x \in \mathbb{R}$:

1. $a + b = a + c \Rightarrow b = c$
2. $(a \cdot b = a \cdot c) \wedge a \neq 0 \Rightarrow b = c$
3. $a + x = b \Rightarrow x = b - a$
4. $(a \cdot x = b \wedge a \neq 0) \Rightarrow x = b/a$
5. $a \cdot 0 = 0$
6. $a \cdot b = 0 \Rightarrow (a = 0 \vee b = 0)$
7. $a = b \Rightarrow -a = -b$
8. $a(-b) = -ab$
9. $(-a)(-b) = ab$
10. $\frac{a}{b} + \frac{c}{b} = \frac{a + c}{b}$
11. $\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$
12. $(\frac{a}{b})(\frac{c}{d}) = \frac{ac}{bd}$
13. $\frac{a/b}{c/d} = \frac{ad}{cb}$

#### Prueba de (1)

Hipótesis: $a + b = a + c \Rightarrow$ Tesis: $b = c$

Demostración: $$\begin{array}{rcl} b & = & b \ & = & b + 0 \ & = & b + [a + (-a)] \ & = & (b + a) + (-a) \ & = & (a + b) + (-a) \ & = & (a + c) + (-a) \ & = & c + [a + (-a)] \ & = & c + 0 \ b & = & c \end{array}$$

--- end-column ---

🔑 **Claves**

--- end-multi-column

> **Resumen:** Definición de los axiomas fundamentales (clausura, conmutatividad, asociatividad, elementos neutros, inversos y distributividad) y teoremas derivados que rigen las operaciones algebraicas en el sistema de números reales.

> [!note] Complemento (Nivel B)
> 
> De acuerdo con Apostol, el sistema de números reales se toma como un concepto primitivo que satisface estos axiomas de cuerpo, los cuales garantizan que las operaciones de adición y multiplicación están unívocamente determinadas para cada par de elementos.
> 
> Formalmente, un conjunto que satisface los axiomas del 1 al 6 (clausura, conmutatividad, asociatividad, distributividad y existencia de neutros e inversos) se denomina **cuerpo** (o _field_). Estos axiomas permiten deducir todas las leyes usuales del álgebra elemental, como la unicidad del elemento cero y del elemento unidad. El Cálculo se estructura sobre este sistema deductivo, definiendo nuevos conceptos como límite e integral a partir de estas propiedades algebraicas básicas.