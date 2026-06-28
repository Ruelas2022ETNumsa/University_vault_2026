Como se deriva de los axiomas de cuerpo, las leyes usuales del álgebra pueden demostrarse formalmente. A continuación se presentan ejercicios resueltos extraídos de **Apostol**, que muestran la aplicación de los axiomas para demostrar propiedades fundamentales.

##### **Ej. 1** Demostrar la unicidad del elemento neutro para la suma.

Si $0$ y $0'$ son elementos que satisfacen la propiedad del neutro aditivo ($a + 0 = a$ para todo $a$), entonces: $$\begin{array}{rcl} 0 + 0' & = & 0 \ 0' + 0 & = & 0' \end{array}$$ Por la propiedad conmutativa, $0 + 0' = 0' + 0$, por lo tanto $0 = 0'$. Esto prueba que el número $0$ es único.

##### **Ej. 2** Demostrar la Ley de simplificación para la suma: si $a + b = a + c$, entonces $b = c$.

1. Por el axioma de existencia de negativos, existe un número $y$ tal que $y + a = 0$.
2. Partiendo de la igualdad $a + b = a + c$, sumamos $y$ a ambos miembros:
    - $y + (a + b) = y + (a + c)$
3. Aplicando la propiedad asociativa:
    - $(y + a) + b = (y + a) + c$
4. Sustituyendo $y + a = 0$:
    - $0 + b = 0 + c$
5. Por la propiedad del elemento neutro:
    - $b = c$.

##### **Ej. 3** Demostrar la posibilidad de la sustracción: dados $a$ y $b$, existe un único $x$ tal que $a + x = b$.

Para demostrar existencia, elegimos $x = y + b$, donde $y$ es el negativo de $a$ ($y + a = 0$): $$\begin{array}{rcl} a + x & = & a + (y + b) \ & = & (a + y) + b \ & = & 0 + b \ & = & b \end{array}$$ Para demostrar la unicidad, supongamos que existe otro valor $x'$ tal que $a + x' = b$. Entonces $a + x = a + x'$, y por la ley de simplificación (Ej. 2), $x = x'$.

##### **Ej. 4** Demostrar que para cualquier número real $a$, $-(-a) = a$.

Por definición del negativo de un número, se cumple que:

- $a + (-a) = 0$ Esta igualdad indica que $a$ es el opuesto o negativo de $(-a)$. Simbólicamente, esto se expresa como $a = -(-a)$.