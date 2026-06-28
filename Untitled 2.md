--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

## Números reales y desigualdades

### Axiomas de cuerpo de los números $\mathbb{R}$

Si $a, b, c \in \mathbb{R}$:

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
    
    - $\exists , 0 \in \mathbb{R} \mid a+0 = a$ (0 es el neutro para la suma "$+$")
    - $\exists , 1 \in \mathbb{R} \mid a \cdot 1 = a$ (1 es el neutro para la multiplicación "$\times$")
5. **Existencia de negativos**
    
    - $\forall a \in \mathbb{R}, \exists , -a \in \mathbb{R} \mid a+(-a) = 0$ ($-a$ se denomina negativo de $a$)
6. **Existencia de inversos**
    
    - $\forall a \in \mathbb{R} - {0}, \exists , a^{-1} \in \mathbb{R} \mid a \cdot a^{-1} = 1$ ($a^{-1} = \frac{1}{a}$ se denomina inverso de $a$)
7. **Distributividad**
    
    - $a(b+c) = ab+ac$

> [!note] Notas del manuscrito La resta y la división son solo casos especiales de la suma y la multiplicación:
> 
> - **Resta:** $a-b = a+(-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \text{ con } b \neq 0$

--- end-column ---

🔑 **Claves**

--- end-multi-column

> **Resumen:** Los números reales forman un cuerpo bajo las operaciones de adición y multiplicación, cumpliendo propiedades de clausura, conmutatividad, asociatividad, distributividad y existencia de elementos neutros e inversos.

> [!note] Complemento(Nivel B) **Definición formal de Cuerpo (Apostol):** Se supone la existencia de un conjunto $\mathbb{R}$ de elementos llamados números reales y dos operaciones llamadas adición y multiplicación, tales que para cada par de números reales $x$ e $y$ se puede formar la suma $x+y$ y el producto $xy$, los cuales están unívocamente determinados por $x$ e $y$. El sistema satisface los seis axiomas de cuerpo mencionados anteriormente, lo que garantiza que las operaciones de sustracción y división (excepto por cero) sean siempre posibles y produzcan resultados únicos dentro del mismo conjunto.



A continuación, se presentan ejercicios resueltos sobre la aplicación y demostración de los axiomas de cuerpo, extraídos de los teoremas fundamentales del sistema de números reales (Apostol, Vol. 1).

**Ej. 1** Demostrar que el elemento neutro para la suma ($0$) es único. Solución: Supongamos que existen dos números, $0$ y $0'$, que cumplen la propiedad del elemento neutro. Entonces:

1. $0 + 0' = 0$ (considerando a $0'$ como neutro).
2. $0 + 0' = 0'$ (considerando a $0$ como neutro). Por la propiedad transitiva de la igualdad, se concluye que $0 = 0'$.

**Ej. 2** Probar la Ley de Simplificación: si $a + b = a + c$, entonces $b = c$. Solución:

1. Por el Axioma 5, existe un número $y$ (el negativo de $a$) tal que $y + a = 0$.
2. Partiendo de la hipótesis $a + b = a + c$, sumamos $y$ a ambos miembros: $$y + (a + b) = y + (a + c)$$
3. Aplicamos la propiedad asociativa (Axioma 3): $$(y + a) + b = (y + a) + c$$
4. Sustituimos $y + a$ por $0$: $$0 + b = 0 + c$$
5. Por el Axioma 4 (elemento neutro), obtenemos el resultado: $$b = c$$

**Ej. 3** Demostrar que para todo número real $a$, se cumple que $a \cdot 0 = 0$. Solución:

1. Sabemos que $0 + 0 = 0$ por el axioma del elemento neutro.
2. Multiplicamos ambos lados por $a$: $$a(0 + 0) = a \cdot 0$$
3. Aplicamos la propiedad distributiva (Axioma 7): $$a \cdot 0 + a \cdot 0 = a \cdot 0$$
4. Por el Axioma 4, podemos escribir $a \cdot 0$ como $a \cdot 0 + 0$: $$a \cdot 0 + a \cdot 0 = a \cdot 0 + 0$$
5. Aplicando la ley de simplificación (demostrada en el Ej. 2), eliminamos $a \cdot 0$ de ambos miembros: $$a \cdot 0 = 0$$

**Ej. 4** Demostrar que el negativo de una suma es la suma de los negativos: $-(a + b) = -a - b$. Solución: Para probar que $-(a + b) = (-a) + (-b)$, debemos verificar que su suma con $(a + b)$ da como resultado el neutro $0$: $$\begin{array}{rcl} (a + b) + [(-a) + (-b)] & = & a + {b + [(-a) + (-b)]} \quad \text{(Asociatividad)} \ & = & a + {b + [(-b) + (-a)]} \quad \text{(Conmutatividad)} \ & = & a + {[b + (-b)] + (-a)} \quad \text{(Asociatividad)} \ & = & a + {0 + (-a)} \quad \text{(Existencia de negativos)} \ & = & a + (-a) \quad \text{(Elemento neutro)} \ & = & 0 \quad \text{(Existencia de negativos)} \end{array}$$ Dado que la suma es $0$, por la unicidad del negativo se cumple la igualdad.

