

::cue
What is a window function?
::note
A calculation across related rows **without collapsing** them.

Unlike GROUP BY, all original rows stay visible.

::cue
What does PARTITION BY do?
::note
Splits rows into logical groups inside the window.

| PARTITION BY | GROUP BY       |
|--------------|----------------|
| keeps rows   | collapses rows |

---

%% ============================================================
   bytetiles/obsidian-cornell-notes — Ejemplos
   Sintaxis: ````cornell  ::cue  ::note
   Solo Reading View
   ============================================================ %%

# bytetiles · Cornell Notes — Ejemplos

%% EJEMPLO 1 — Texto plano %%

````cornell
::cue
¿Qué es el valor absoluto?
::note
Medida no negativa de un número real. Geométricamente es la distancia al origen.

$|x| = \left\{ \begin{array}{rcl} x & ; & x \geq 0 \\ -x & ; & x < 0 \end{array} \right.$

::cue
¿Cuándo $\sqrt{x^2} \neq x$?
::note
Cuando $x < 0$. La identidad general es $\sqrt{x^2} = |x|$, no $\sqrt{x^2} = x$.
````

---

%% EJEMPLO 2 — Listas en ambas columnas %%

````cornell
::cue
Propiedades básicas
::note
- $|-x| = |x|$
- $|x| \geq 0$
- $|x \cdot y| = |x| \cdot |y|$
- $|x|^2 = x^2$

::cue
Desigualdades
::note
- $|x| < a \Rightarrow -a < x < a$
- $|x| > a \Rightarrow x > a \vee x < -a$
- $|x+y| \leq |x|+|y|$ — Triangular
- $|x \cdot y| \geq x \cdot y$ — Schwarz
````

---

%% EJEMPLO 3 — Tabla en columna de notas %%

````cornell
::cue
Axiomas de cuerpo de $\mathbb{R}$
::note
| # | Axioma | Fórmula |
|---|--------|---------|
| 1 | Clausura | $a+b \in \mathbb{R}$ |
| 2 | Conmutatividad | $a+b = b+a$ |
| 3 | Asociatividad | $(a+b)+c = a+(b+c)$ |
| 4 | Neutros | $a+0=a,\quad a\cdot 1=a$ |
| 5 | Negativos | $a+(-a)=0$ |
| 6 | Inversos | $a \cdot a^{-1}=1$ |
| 7 | Distributividad | $a(b+c)=ab+ac$ |
````

---

%% EJEMPLO 4 — Callout y math %%

````cornell
::cue
> [!tip] Mnemotécnico
> **CCANNID**
::note
> [!note] Apostol Cap. 0
> Los neutros $0$ y $1$ son **distintos**. El axioma 4 lo especifica explícitamente.

$a \cdot a^{-1} = 1, \quad a \neq 0$

::cue
Cue sin nota (solo margen)
````

---

%% EJEMPLO 5 — Código dentro del bloque cornell %%

````cornell
::cue
Python
::note
```python
x = -3
abs_x = abs(x)  # equivale a |x|
print(abs_x)    # 3
```

::cue
LaTeX
::note
```latex
\left| x \right| = \sqrt{x^2}
```
````