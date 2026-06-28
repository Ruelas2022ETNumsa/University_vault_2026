

A continuación se presentan ejercicios resueltos extraídos de las fuentes bibliográficas sobre la aplicación y demostración de los **Axiomas de cuerpo**, los cuales fundamentan las operaciones de adición y multiplicación en los números reales.

##### **Ej. 1** Demostrar la Ley de simplificación para la suma: Si $a + b = a + c$, entonces $b = c$.

**Demostración:** $$ \begin{array}{rcl} a + b & = & a + c \ (-a) + (a + b) & = & (-a) + (a + c) \ [(-a) + a] + b & = & [(-a) + a] + c \ 0 + b & = & 0 + c \ b & = & c \end{array} $$

> [!note] Esta demostración utiliza el **Axioma 5** (existencia de negativos), el **Axioma 2** (propiedad asociativa) y el **Axioma 4** (existencia de elementos neutros).

---

##### **Ej. 2** Demostrar que para cualquier número real $a$, se cumple que $a \cdot 0 = 0$.

**Demostración:** Partimos de la propiedad del elemento neutro para la suma: $0 + 0 = 0$. Multiplicando ambos miembros por $a$: $$ \begin{array}{rcl} a \cdot (0 + 0) & = & a \cdot 0 \ a \cdot 0 + a \cdot 0 & = & a \cdot 0 \end{array} $$ Sumando el opuesto de $(a \cdot 0)$, denotado como $-(a \cdot 0)$, en ambos lados: $$ \begin{array}{rcl} (a \cdot 0 + a \cdot 0) + [-(a \cdot 0)] & = & a \cdot 0 + [-(a \cdot 0)] \ a \cdot 0 + {a \cdot 0 + [-(a \cdot 0)]} & = & 0 \ a \cdot 0 + 0 & = & 0 \ a \cdot 0 & = & 0 \end{array} $$

> [!note] Este resultado muestra que el producto de cualquier número por el neutro aditivo es siempre el neutro aditivo, propiedad derivada directamente de la **Propiedad distributiva** (Axioma 3).

---

##### **Ej. 3** Probar que el elemento neutro de la suma ($0$) es único.

**Demostración:** Supongamos que existen dos números, $0$ y $0'$, que cumplen la propiedad del neutro aditivo.

1. Si usamos la propiedad para $0'$, tenemos: $0 + 0' = 0$.
2. Si usamos la propiedad para $0$, tenemos: $0' + 0 = 0'$.
3. Por la **Propiedad conmutativa** (Axioma 1): $0 + 0' = 0' + 0$.
4. Por lo tanto: $0 = 0'$.

---

##### **Ej. 4** Demostrar que $(-a)(-b) = ab$.

**Demostración:** Primero se demuestra que $(-a)b = -(ab)$. Para ello, notamos que: $$ ab + (-a)b = [a + (-a)]b = 0 \cdot b = 0 $$ Esto indica que $(-a)b$ es el opuesto de $ab$. Ahora, para el caso de dos negativos: $$ (-a)(-b) = -[a(-b)] = -[(-b)a] = -[-(ba)] = ba = ab $$

> [!note] Se utiliza el **Teorema I.4** de Apostol, que establece que $-(-a) = a$, es decir, el opuesto del opuesto de un número es el número original.