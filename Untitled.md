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



## Ejercicios resueltos (Axiomas de cuerpo)

A continuación se presentan demostraciones de leyes algebraicas fundamentales derivadas directamente de los axiomas de cuerpo, extraídas de **Apostol (Vol. 1)**. Estas pruebas ilustran el método deductivo a partir de las propiedades primitivas de los números reales.

**Ej. 1** Demostrar la **Ley de simplificación para la suma**: Si $a + b = a + c$, entonces $b = c$. Por el axioma 5, existe un número $y$ tal que $y + a = 0$. Sumamos $y$ a ambos miembros de la igualdad: $$y + (a + b) = y + (a + c)$$ Aplicando el axioma 2 (asociatividad): $$(y + a) + b = (y + a) + c$$ Sustituyendo el valor del opuesto ($0$) y aplicando el axioma 4 (neutro aditivo): $$\begin{array}{rcl} 0 + b & = & 0 + c \ b & = & c \end{array}$$

> [!note] Este resultado es crucial para demostrar formalmente que el elemento neutro $0$ es único.

**Ej. 2** Demostrar la **Unicidad de la sustracción**: Dados $a$ y $b$, existe uno y solo un $x$ tal que $a + x = b$. A este valor se le designa como $b - a$.

1. **Existencia**: Elegimos $y$ tal que $a + y = 0$ y definimos $x = y + b$. Al sustituir en la ecuación: $$a + x = a + (y + b) = (a + y) + b = 0 + b = b$$
2. **Unicidad**: Supongamos que existe otro valor $x'$ tal que $a + x' = b$. Entonces: $$a + x = a + x'$$ Por la ley de simplificación demostrada en el **Ej. 1**, concluimos que $x = x'$. Por tanto, el valor es único.

**Ej. 3** Demostrar la **Ley de simplificación para la multiplicación**: Si $ab = ac$ y $a \neq 0$, entonces $b = c$. Dado que $a \neq 0$, por el axioma 6 existe un recíproco $a^{-1}$ tal que $a^{-1}a = 1$. Multiplicamos ambos miembros por $a^{-1}$: $$a^{-1}(ab) = a^{-1}(ac)$$ Aplicando el axioma 2 para el producto (asociatividad): $$(a^{-1}a)b = (a^{-1}a)c$$ Sustituyendo por el neutro multiplicativo ($1$) y aplicando el axioma 4: $$\begin{array}{rcl} 1 \cdot b & = & 1 \cdot c \ b & = & c \end{array}$$

**Ej. 4** Demostrar que para cualquier número real $a$, se cumple $a \cdot 0 = 0$. Sabemos por el axioma 4 que $0 + 0 = 0$. Aplicando la propiedad distributiva (axioma 7): $$\begin{array}{rcl} a \cdot 0 + a \cdot 0 & = & a \cdot (0 + 0) \ a \cdot 0 + a \cdot 0 & = & a \cdot 0 \end{array}$$ Como el resultado $a \cdot 0$ es un número real, sumamos su opuesto $-(a \cdot 0)$ en ambos miembros: $$(a \cdot 0 + a \cdot 0) + [-(a \cdot 0)] = a \cdot 0 + [-(a \cdot 0)]$$ Usando la asociatividad y la definición de opuesto: $$\begin{array}{rcl} a \cdot 0 + (a \cdot 0 + [-(a \cdot 0)]) & = & 0 \ a \cdot 0 + 0 & = & 0 \ a \cdot 0 & = & 0 \end{array}$$




`> [!note] Complemento (Nivel B)
> 
> Según **Apostol**, el sistema de los `


`[!note] Complemento(Nivel B) **De`