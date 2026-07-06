# Cornell Marginalia — Ejemplos de sintaxis


Mitochondria 
are 
membrane-bound
cell organelles that 
generate most of the chemical energy. %%> "Powerhouse" of the cell (ATP) %%

> [!cornell]
> %%> Your margin note here %%
> This is my introductory paragraph:%%> Your margin note here %%
> - List item 1 %%> Your margin note here %%
> - List item 2 %%> Your margin note here %%
```cornell-m
%%>  ese preuese%%
srserserse
serser
eRTpert
ert
ert
ert
etre
tet
ert

```

```cornell-m
%%> Your perfectly aligned note here %%
The main text that requires strict alignment goes here.
- It can contain lists
- Images, and more!
```

eeEr%%> uuui %%




Select any text (or just place your cursor on an empty line).

Right-click and select "Insert Cornell Block" (or use the Command Palette).

The plugin will wrap your text, auto-inject the %%>  %% syntax, and place your cursor magically in the center—ready for you to start typing your margin note instantly.


%%  FEATURE 1 — Sintaxis básica inline  %%

Los números reales forman un cuerpo algebraico bajo suma y multiplicación. %%> Axiomas de cuerpo  ^mlq5wm%%

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

```cornell-m
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

La recta numérica representa geométricamente a $\mathbb{R}$. %%> img:[[Cornell Marginalia — Ejemplos de sintaxis-11-06-2026_19-01-03.png]] %%




asdsad%%< img:[[Cornell Marginalia — Ejemplos de sintaxis-11-06-2026_19-01-03.png]] %%



> [!cornell]
> %%> img:[[Cornell Marginalia — Ejemplos de sintaxis-11-06-2026_19-01-03.png]] %%
> La recta numérica representa geométricamente a $\mathbb{R}$.



```cornell-m
Texto principal de la sección.%%> Aclaración al margen sobre este párrafo. %%
Más texto que continúa normalmente.
```




---
---
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





```cornell-m
Texto principal de la sección.%%> Aclaración al margen sobre este párrafo. %%
Más texto que continúa normalmente.
```

[^1]: nota de pued en marjanalia
