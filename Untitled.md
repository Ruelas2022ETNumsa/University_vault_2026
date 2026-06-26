# Números reales y desigualdades

## Axiomas de cuerpo de los números reales

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    - $a + b \in \mathbb{R}$ ; $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    - $(a + b) + c = a + (b + c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    - $\exists 0 \in \mathbb{R} \text{ tal que } a + 0 = a \rightarrow 0 \text{ es el neutro para la suma } "+"$
    - $\exists 1 \in \mathbb{R} \text{ tal que } a \cdot 1 = a \rightarrow 1 \text{ es el neutro para el producto } "\cdot"$
5. **Existencia de negativos**
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} \text{ tal que } a + (-a) = 0$
    - $-a = \text{negativo de } a$
6. **Existencia de inversos**
    - $\forall a \in \mathbb{R} - {0}, \exists a^{-1} \in \mathbb{R} \text{ tal que } a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a} \text{ es el inverso de } a$
7. **Distributividad**
    - $a \cdot (b + c) = ab + ac$

## Axiomas de igualdad

Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
    - $a = a$
2. **Simetría**
    - $a = b \Rightarrow b = a$
3. **Transitividad**
    - $(a = b \land b = c) \Rightarrow a = c$

> [!note] La resta y la división son solo casos especiales de la suma ($+$) y el producto ($\cdot$):
> 
> - **Resta:** $a - b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, b \neq 0$

> [!important] **No confundir:**
> 
> - $2^3 = 8 \rightarrow \text{Igualdad (verdad evidente).}$
> - $x^2 - 4 = 0 \rightarrow \text{Ecuación (verdad para algunas } x\text{).}$
> - $x^2 - 4 = (x - 2)(x + 2) \rightarrow \text{Identidad (verdad para toda } x \in \mathbb{R}\text{).}$

> [!note] Complemento (Nivel B)
> 
> De acuerdo con Apostol, el sistema de los números reales se puede estructurar de forma deductiva tomando estos axiomas como leyes primitivas. A partir de ellos se pueden demostrar las siguientes propiedades fundamentales de unicidad:
> 
> 1. **Unicidad del elemento neutro:** Si un número $0'$ tiene la propiedad de que $a + 0' = a$ para todo $a$, entonces $0' = 0$. Lo mismo ocurre para el neutro multiplicativo $1$.
> 2. **Unicidad de opuestos e inversos:** Para cada número real $a$, existe un único negativo $-a$ y, si $a \neq 0$, un único recíproco $a^{-1}$.
> 
> Estos axiomas definen a los números reales como un **cuerpo**. Al combinarse con los axiomas de orden (que garantizan que se pueden comparar magnitudes), $\mathbb{R}$ se define formalmente como un **cuerpo ordenado**.


## Ejercicios resueltos (Axiomas de cuerpo)

A continuación se presentan aplicaciones de los axiomas de cuerpo para demostrar leyes fundamentales del álgebra, extraídas de **Apostol (Vol. 1)**.

**Ej. 1** Demostrar la **Ley de simplificación para la suma**: Si $a + b = a + c$, entonces $b = c$. En virtud del axioma 5 (existencia de negativos), se puede elegir un número $y$ tal que $y + a = 0$. Al sumar $y$ en ambos miembros: $$y + (a + b) = y + (a + c)$$ Aplicando el axioma 2 (asociatividad): $$(y + a) + b = (y + a) + c$$ Sustituyendo por el neutro (axioma 5) y aplicando el axioma 4 (existencia de neutros): $$\begin{array}{rcl} 0 + b & = & 0 + c \ b & = & c \end{array}$$

> [!note] Este resultado es fundamental porque permite demostrar que el elemento neutro $0$ es único.

**Ej. 2** Demostrar la **Posibilidad de la sustracción**: Dados $a$ y $b$, existe uno y sólo un $x$ tal que $a + x = b$. Para demostrar la existencia, elegimos un $y$ tal que $a + y = 0$ y definimos $x = y + b$. Comprobamos la igualdad: $$a + x = a + (y + b) = (a + y) + b = 0 + b = b$$ Para demostrar la unicidad, supongamos que existe otro valor $x'$ tal que $a + x' = b$. Entonces: $$a + x = a + x'$$ Por la ley de simplificación demostrada en el **Ej. 1**, concluimos que $x = x'$. Por tanto, el valor $x$ es único y se designa como $b - a$.

**Ej. 3** Demostrar que $b - a = b + (-a)$. Sea $x = b - a$ y sea $y = b + (-a)$. Por la definición de resta en el ejercicio anterior, sabemos que $x + a = b$. Ahora probamos que $y + a$ también es igual a $b$: $$\begin{array}{rcl} y + a & = & [b + (-a)] + a \ & = & b + [(-a) + a] \ & = & b + 0 \ & = & b \end{array}$$ Puesto que $x + a = y + a$, por la ley de simplificación, $x = y$, es decir, $b - a = b + (-a)$.

**Ej. 4** Demostrar la ley del doble signo: $-(-a) = a$. Por definición del axioma 5, el negativo de un número es aquel que sumado al original da cero. Tenemos que $a + (-a) = 0$. Esta misma igualdad nos indica que $a$ cumple la condición de ser el negativo del número $(-a)$. Simbólicamente: $$a = -(-a)$$ como se quería demostrar.