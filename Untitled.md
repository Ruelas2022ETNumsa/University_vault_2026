# Números reales y desigualdades

--- start-multi-column: cornell-T0-001
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

### Axiomas de cuerpo de los números reales

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    - $a + b \in \mathbb{R}$ ; $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    - i) $(a + b) + c = a + (b + c)$
    - ii) $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    - i) $\exists 0 \in \mathbb{R} \text{ tal que } a + 0 = a$ $\rightarrow 0 \text{ es el neutro para la suma } "+"$
    - ii) $\exists 1 \in \mathbb{R} \text{ tal que } a \cdot 1 = a$ $\rightarrow 1 \text{ es el neutro para el producto } "\cdot"$
5. **Existencia de negativos**
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \text{ tal que } a + (-a) = 0$
    - $-a = \text{negativo de } a$
6. **Existencia de inversos**
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \text{ tal que } a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a} \text{ es el inverso de } a$
7. **Distributividad**
    - $a \cdot (b + c) = ab + ac$

--- end-column ---

🔑 **Claves**

--- end-multi-column









> **Resumen:** El conjunto $\mathbb{R}$ con las operaciones de adición y multiplicación que satisfacen estos siete axiomas constituye un sistema algebraico denominado cuerpo.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol**, el sistema de los números reales se introduce asumiendo la existencia de un conjunto $\mathbb{R}$ con dos operaciones binarias que cumplen estas leyes fundamentales. De estos axiomas se derivan propiedades de unicidad esenciales para el cálculo:
> 
> 1. **Unicidad del elemento neutro:** El número $0$ (identidad aditiva) y el número $1$ (identidad multiplicativa) son únicos en $\mathbb{R}$.
> 2. **Unicidad de opuestos e inversos:** Para cada $a$, su negativo $-a$ es único; asimismo, para todo $a \neq 0$, su recíproco $a^{-1}$ es único.
> 
> El cumplimiento de estos axiomas permite tratar a los números reales como un **cuerpo**, sobre el cual se construirán posteriormente las estructuras de orden y completitud necesarias para definir límites e integrales.