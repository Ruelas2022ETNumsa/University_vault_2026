# T0 — Números Reales

## Axiomas de cuerpo de los nros. reales. $\mathbb{R}$

```cornell
::cue
Cuerpo conmutativo<br>
Axiomas · Clausura · Elementos neutros · Inversos · Distributividad<br>
¿Qué propiedades definen a los números reales como un cuerpo?<br>
¿Cómo se definen formalmente la resta y la división?<br>
¿Cuál es la diferencia conceptual entre una ecuación y una identidad?<br>
$a \cdot a^{-1} = 1, \quad a \neq 0$<br>
ver también: Axiomas de orden<br>
no confundir: elemento neutro con elemento inverso
::note
Si $a, b, c \in \mathbb{R}$

1. **Clausura**
	- $a+b \in \mathbb{R} \quad \text{y} \quad a \cdot b \in \mathbb{R}$

2. **Conmutatividad**
	- i) $a+b = b+a$
	- ii) $a \cdot b = b \cdot a$

3. **Asociatividad**
	- i) $(a+b)+c = a+(b+c)$
	- ii) $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

4. **Existencia de neutros**
	- i) $\exists \, 0 \in \mathbb{R} \ni a+0 = a \to 0$ es el neutro para la "$+$"
	- ii) $\exists \, 1 \in \mathbb{R} \ni a \cdot 1 = a \to 1$ es el neutro para la "$\cdot$"

5. **Existencia de negativos**
	- $\forall a \in \mathbb{R} \cdot \exists -a \in \mathbb{R} \ni a+(-a) = 0$
	- $-a$ = negativo de $a$ (u opuesto).

6. **Existencia de inversos**
	- $\forall a \in \mathbb{R} - \{0\} \cdot \exists a^{-1} \in \mathbb{R} \ni a \cdot a^{-1} = 1$
	- $a^{-1} = \frac{1}{a}$ es el inverso de $a$ (o recíproco).

7. **Distributividad**
	- $a(b+c) = ab + ac$

> [!note]
> La resta y la división son solo casos especiales de la "$+$" y la "$\cdot$".
> - **Resta:** $a-b = a + (-b)$
> - **División:** $\frac{a}{b} = a \cdot \frac{1}{b} = a \cdot b^{-1}, \quad b \neq 0$

$$\begin{array}{rcl}
\drac{1}{2} \ esto es una preigea \frac{1}{2}
\end{array}$$



**No confundir:**
- $2^3 = 8 \to$ **Igualdad** (verdad evidente).
- $x^2-4 = 0 \to$ **Ecuación** (verdad para algunas "$x$").
- $x^2-4 = (x-2)(x+2) \to$ **Identidad** (verdad para todo $x \in \mathbb{R}$).
```

> [!summary] Los números reales forman un cuerpo bajo los axiomas de clausura, conmutatividad, asociatividad, distributividad y la existencia de elementos neutros e inversos.

> [!note] Complemento (Nivel B/C)
> 
> Los axiomas presentados definen a los números reales como un **Cuerpo Conmutativo** (o Campo). De estos principios se derivan leyes fundamentales del álgebra elemental, tales como:
> 
> 1. **Unicidad del neutro:** El elemento $0$ (identidad aditiva) y el $1$ (identidad multiplicativa) son únicos en el sistema de los números reales.
> 2. **Unicidad del inverso:** Cada número real tiene un único negativo y, si no es cero, un único recíproco.
> 3. **Ley de simplificación:** Si $a + b = a + c$, entonces $b = c$. De igual forma, si $ab = ac$ con $a \neq 0$, entonces $b = c$.
> 4. **Propiedad del cero:** Para cualquier número real $a$, se cumple que $a \cdot 0 = 0$.