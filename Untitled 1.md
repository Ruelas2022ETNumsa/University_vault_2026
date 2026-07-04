# Cornell Marginalia — Ejemplos de sintaxis

%%  FEATURE 1 — Sintaxis básica inline  %%

Los números reales forman un cuerpo algebraico bajo suma y multiplicación. %%> Axiomas de cuerpo  ^mlq5wm %%

El neutro aditivo es $0$ y el neutro multiplicativo es $1$. %%> ! Distinción clave: $0 \neq 1$ %%

---

%%  FEATURE 2 — Semantic Highlighting (prefijos de color)  %%

Sea $a \in \mathbb{R}$, entonces $a + (-a) = 0$. %%> ? ¿Cuál es la diferencia entre negativo e inverso? %%

$\sqrt{x^2} = |x|$, no $\sqrt{x^2} = x$. %%> X- Error común: olvidar el valor absoluto %%

La desigualdad triangular: $|x+y| \leq |x|+|y|$. %%> V- Verificado con Apostol Cap. 0 %%

La distributividad vincula suma y producto: $a(b+c)=ab+ac$. %%> ! Único axioma que conecta ambas operaciones %%

---

%%  FEATURE 3 — Margen opuesto (solo Reading View)  %%

Existe $a^{-1}$ tal que $a \cdot a^{-1} = 1$ para todo $a \neq 0$. %%< Axioma 6 — Inverso multiplicativo %%

---

%%  FEATURE 4 — Agrupación Method A: Invisible Callout (Reading View)  %%

> [!cornell]
> %%> Axiomas 4–6: neutros, negativos, inversos %%
> **Existencia de elementos especiales:**
> - $\exists\; 0 : a + 0 = a$
> - $\exists\; 1 : a \cdot 1 = a$
> - $\exists\; {-a} : a + (-a) = 0$
> - $\exists\; a^{-1} : a \cdot a^{-1} = 1,\quad a \neq 0$

---

%%  FEATURE 5 — Agrupación Method B: Cornell Block (Reading View + PDF safe)  %%

```cornell
%%> CCANNID: Clausura · 
Conmuta
tiva · Asociativa · Neutros · 
Negativos · Inversos · Distributiva %%
Los **7 axiomas de cuerpo** de $\mathbb{R}$:


1. Clausura
2. Conmutatividad
3. Asociatividad
4. Existencia de neutros
5. Existencia de negativos
6. Existencia de inversos
7. Distributividad
```

---


























%%  FEATURE 6 — Active Recall con blur ;;  %%

El negativo de $a$ cumple $a + (-a) = 0$. %%> ? ¿Cómo se llama la propiedad que garantiza su existencia? ;; Existencia de negativos — Axioma 5 %%

El inverso de $a$ es $a^{-1} = \frac{1}{a}$. %%> ? ¿Para qué valores existe $a^{-1}$? ;; Para todo $a \neq 0$ %%

---

%%  FEATURE 7 — Imagen en margen  %%

La recta numérica representa geométricamente a $\mathbb{R}$. %%> img:[[comfor numbss - copia.png]] %%




asdsad%%< img:[[comfor numbss - copia.png]] %%



> [!cornell]
> %%> img:[[comfor numbss - copia.png]] %%
> La recta numérica representa geométricamente a $\mathbb{R}$.










# Números reales y desigualdades

--- start-multi-column: cornell-T0-001

```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

## Axiomas de cuerpo de los números reales (ℝ)

📝 **Desarrollo**

Si $a, b, c \in \mathbb{R}$:

1. **Clausura**
    - $a + b \in \mathbb{R}$ y $a \cdot b \in \mathbb{R}$
2. **Conmutatividad**
    - $a + b = b + a$
    - $a \cdot b = b \cdot a$
3. **Asociatividad**
    - $(a + b) + c = a + (b + c)$
    - $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
4. **Existencia de neutros**
    - i. $\exists \; 0 \in \mathbb{R} : a + 0 = a$
        - $0$ es el neutro para la suma "$+$".
    - ii. $\exists \; 1 \in \mathbb{R} : a \cdot 1 = a$
        - $1$ es el neutro para la multiplicación "$\times$".
5. **Existencia de negativos**
    - $\forall a \in \mathbb{R}, \exists -a \in \mathbb{R} : a + (-a) = 0$
    - $-a$ es el negativo de $a$.
6. **Existencia de inversos**
    - $\forall a \in \mathbb{R} - \{0\}, \exists \; a^{-1} \in \mathbb{R} : a \cdot a^{-1} = 1$
    - $a^{-1} = \frac{1}{a}$ es el inverso de $a$.
7. **Distributividad**
    - $a(b + c) = ab + ac$

--- end-column ---

🔑 **Claves**

Axiomas · Cuerpo · Reales · Neutros · Inversos

¿Cuáles son las reglas básicas que rigen la suma y multiplicación? ¿Qué elementos permiten la existencia de operaciones inversas? ¿Cómo se relacionan la suma y el producto aritmético?

$a + (-a) = 0$ $a \cdot a^{-1} = 1, a \neq 0$

ver también: Axiomas de orden

No confundir el neutro aditivo ($0$) con el neutro multiplicativo ($1$).

**C**lausura, **C**onmutativa, **A**sociativa, **N**eutros, **N**egativos, **I**nversos, **D**istributiva (**CCANNID**)

--- end-multi-column

> **Resumen:** Definición de los siete axiomas fundamentales que establecen a los números reales como un cuerpo algebraico bajo las operaciones de adición y multiplicación.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. 0, sección I 3.2)**, el sistema de los números reales se postula como un conjunto de elementos sobre los cuales se definen dos operaciones (adición y multiplicación) que cumplen unívocamente con las propiedades de cuerpo.
> 
> **Refuerzo de definiciones formales:**
> 
> 1. **Unicidad de resultados:** La suma $x+y$ y el producto $xy$ están unívocamente determinados por $x$ e $y$.
> 2. **Distinción de neutros:** El Axioma 4 de Apostol especifica explícitamente que existen dos números reales **distintos**, indicados por $0$ y $1$, tales que $0+x=x$ y $1 \cdot x = x$ para cada número real $x$.
> 3. **Existencia del recíproco:** Se enfatiza que para cada número real $x \neq 0$ existe un número real $y$ (denotado $x^{-1}$ o $1/x$) tal que $xy = 1$.
> 4. **Identidad de los elementos:** Apostol aclara en una nota que los números $0$ y $1$ utilizados para definir los negativos e inversos en los axiomas 5 y 6 son exactamente los mismos elementos neutros definidos en el axioma 4.

---


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