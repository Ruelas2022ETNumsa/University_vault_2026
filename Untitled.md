## AXIOMAS DE IGUALDAD

````cornell
::cue
```cornell-m
%%> %%
```cornell-m
%%> %%
Propiedades de la igualdad<br>Igualdad · Identidad · Ecuación<br>¿Cuáles son los tres axiomas fundamentales que rigen la relación de igualdad en los números reales?<br>¿En qué se diferencia una ecuación de una identidad matemática?<br>$a = b \land b = c \Rightarrow a = c$<br>ver también: Axiomas de cuerpo

```
```
::note
```cornell-m
%%< %%
```cornell-m
%%< %%
Si $a, b, c \in \mathbb{R}$:

1. **Reflexividad**
	- $a = a$

2. **Simetría**
	- $a = b \Rightarrow b = a$

3. **Transitividad**
	- $(a = b \land b = c) \Rightarrow a = c$

> [!note] Resta y división son solo casos especiales de $+$ y $\cdot$
> - **Resta**: $a - b = a + (-b)$
> - **División**: $\dfrac{a}{b} = a \cdot \dfrac{1}{b} = a \cdot b^{-1}, b \neq 0$

**No confundir:**
- $2^3 = 8 \Rightarrow$ Igualdad $\rightarrow$ Verdad evidente.
- $x^2 - 4 = 0 \Rightarrow$ Ecuación $\rightarrow$ Verdad para algunas "$x$".
- $x^2 - 4 = (x - 2)(x + 2) \Rightarrow$ Identidad $\rightarrow$ Verdad para toda $x \in \mathbb{R}$.
  \dfrac
  $$\begin{array}{ccc}\dfrac{1}{2}\\
esto\end{array}$$
sdfsd  
```desmos-graph
left=dfgg
```
````

> [!summary] La igualdad en $\mathbb{R}$ es una relación de equivalencia (reflexiva, simétrica y transitiva) que permite distinguir entre igualdades numéricas, ecuaciones condicionales e identidades universales.

> [!note] Complemento (Nivel C)
> 
> **Definición formal de Igualdad de Conjuntos** Según Apostol, se dice que dos conjuntos $A$ y $B$ son iguales (o idénticos) si constan exactamente de los mismos elementos, lo cual se denota como $A = B$. Un teorema fundamental derivado de esto es que $A = B$ si y solo si $A \subseteq B$ y $B \subseteq A$.
> 
> **Identidad en Polinomios** En el contexto de funciones reales, dos polinomios son idénticamente iguales si los coeficientes de un polinomio son iguales a los coeficientes correspondientes del otro. Esto implica que la diferencia entre ambos es un polinomio nulo para todo valor de la variable.
> 
> ##### Ej. Identificación de Identidades vs. Ecuaciones
> 
> Determine si las siguientes afirmaciones son verdaderas (identidades) o falsas (ecuaciones condicionales o falsedades):
> 
> a) $\sqrt{a^2 + b^2} = a + b$ $$\begin{array}{rcll} \sqrt{3^2 + 4^2} & = & 3 + 4 & (\text{Valores de prueba: } a=3, b=4)\\
\sqrt{9 + 16} & = & 7 &\\
5 & \neq & 7 & (\text{Falso. No es una identidad}) \end{array}$$
> 
> b) $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{x+y}$ $$\begin{array}{rcll} \dfrac{1}{1} + \dfrac{1}{1} & = & \dfrac{1}{1+1} & (\text{Valores de prueba: } x=1, y=1)\\
2 & \neq & 0.5 & (\text{Falso. Es una falacia algebraica común}) \end{array}$$
> 
> c) $(p - q)^2 = p^2 - q^2$ $$\begin{array}{rcll} (p - q)^2 & = & p^2 - 2pq + q^2 & (\text{Desarrollo correcto})\\
p^2 - 2pq + q^2 & \neq & p^2 - q^2 & (\text{Falso. Solo es cierto si } q=0 \text{ o } p=q) \end{array}$$ _(Fuente: Stewart 7ed, Examen de diagnóstico de álgebra, pág. A2)_.




## La recta real intervalos

`````cornell
::cue
```cornell-m
%%> %%
Correspondencia biunívoca<br>
recta real · intervalo · subconjunto · puntos extremos<br>
¿Cómo se define la correspondencia entre los números reales y la recta?<br>
¿Qué es un intervalo en el contexto de los números reales?<br>
¿Cuáles son las distintas formas de representar un intervalo?<br>
$[a, b] = \{x \in \mathbb{R} \mid a \leq x \leq b\}$<br>
ver también: axiomas de orden<br>
no confundir: corchete $[...]$ (incluye) con paréntesis o corchete invertido $]...[$ (excluye)

```
::note
```cornell-m
%%< %%
Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```tikz
\begin{document}
\begin{tikzpicture}[x=1.5cm]
\draw[latex-latex] (-2.5,0) -- (4.5,0);
\foreach \x in {-2,-1,0,1,2,3,4}
  \draw (\x,0.1) -- (\x,-0.1);
\node[below] at (-2,-0.1) {$-2$};
\node[below] at (-1,-0.1) {$-1$};
\node[below] at (0,-0.1) {$0$};
\node[below] at (1,-0.1) {$1$};
\node[below] at (2,-0.1) {$2$};
\node[below] at (3,-0.1) {$3$};
\node[below] at (4,-0.1) {$4$};

\filldraw (1.414,0) circle (1.5pt) node[above] {$\sqrt{2}$};
\filldraw (2.718,0) circle (1.5pt) node[above] {$e$};
\filldraw (3.141,0) circle (1.5pt) node[above] {$\pi$};

\node[right] at (4.5,0.3) {$+\infty$};
\node[left] at (-2.5,0.3) {$-\infty$};
\end{tikzpicture}
\end{document}
```

- Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**
	- $[a, b] = \{x / a \leq x \leq b\}$
	- Posee valores extremos.
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(1,0) | #005F73 | label: a
(4,0) | #005F73 | label: b
0 | 1 < x < 4 | #94D2BD
```

2. **Intervalo semiabierto (izquierda)**
	- $]a, b] = \{x / a < x \leq b\}$
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(1,0) | open | #005F73 | label: a
(4,0) | #005F73 | label: b
0 | 1 < x < 4 | #94D2BD
```

3. **Intervalo abierto**
	- $]a, b[ = \{x / a < x < b\}$
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(1,0) | open | #005F73 | label: a
(4,0) | open | #005F73 | label: b
0 | 1 < x < 4 | #94D2BD
```

4. **Intervalo infinito (derecha)**
	- $]a, +\infty[ = \{x / x > a\}$
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(1,0) | open | #005F73 | label: a
0 | x > 1 | #94D2BD
```

5. **Intervalo infinito (izquierda)**
	- $]-\infty, b[ = \{x / x < b\}$
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(4,0) | open | #005F73 | label: b
0 | x < 4 | #94D2BD
```
`````

> [!summary] Los intervalos son subconjuntos continuos de la recta real que representan segmentos (acotados) o semirrectas (infinitos) definidos por desigualdades.

> [!note] Complemento (Nivel C)
> 
> **Definición Formal** Un intervalo es un conjunto de números reales que contiene al menos dos números y todos los números reales comprendidos entre cualesquiera dos de sus elementos. Geométricamente, corresponden a rayos (intervalos infinitos) y segmentos de recta (intervalos finitos).
> 
> **Tipos de Intervalos Adicionales** Según Stewart, existen variaciones en la notación y tipos que complementan lo visto:
> 
> | Notación de Conjunto | Notación de Intervalo | Tipo | | :--- | :--- | :--- | | ${x \mid a < x < b}$ | $(a, b)$ | Abierto | | ${x \mid a \leq x \leq b}$ | $[a, b]$ | Cerrado | | ${x \mid a \leq x < b}$ | $[a, b)$ | Semiabierto | | ${x \mid a < x \leq b}$ | $(a, b]$ | Semiabierto | | ${x \mid x \geq a}$ | $[a, \infty)$ | Infinito cerrado | | ${x \mid x \leq b}$ | $(-\infty, b]$ | Infinito cerrado | | $\mathbb{R}$ | $(-\infty, \infty)$ | Recta real completa |
> 
> **Operaciones con Intervalos** Es común expresar soluciones de desigualdades como la **unión** ($\cup$) o **intersección** ($\cap$) de intervalos. Por ejemplo, el conjunto de puntos que no pertenecen a un intervalo abierto $(a, b)$ se puede expresar como $(-\infty, a] \cup [b, \infty)$.
> 
> ##### Ej. Expresar la solución de la desigualdad $4 \leq 3x - 2 < 13$ en notación de intervalos.
> 
> $$\begin{array}{rcll} 4 \leq 3x - 2 < 13 & & & (\text{Desigualdad original})\\
6 \leq 3x < 15 & & & (\text{Sumar 2 en todos los miembros})\\
2 \leq x < 5 & & & (\text{Dividir entre 3}) \end{array}$$ **Solución:** $[2, 5)$ o $[2, 5[$ en notación de los apuntes.



```tikz
\begin{document}
\begin{tikzpicture}[x=1.5cm]
\draw[latex-latex] (-2.5,0) -- (4.5,0);
\foreach \x in {-2,-1,0,1,2,3,4}
  \draw (\x,0.1) -- (\x,-0.1);
\node[below] at (-2,-0.1) {$-2$};
\node[below] at (-1,-0.1) {$-1$};
\node[below] at (0,-0.1) {$0$};
\node[below] at (1,-0.1) {$1$};
\node[below] at (2,-0.1) {$2$};
\node[below] at (3,-0.1) {$3$};
\node[below] at (4,-0.1) {$4$};

\filldraw (1.414,0) circle (1.5pt) node[above] {$\sqrt{2}$};
\filldraw (2.718,0) circle (1.5pt) node[above] {$e$};
\filldraw (3.141,0) circle (1.5pt) node[above] {$\pi$};

\node[right] at (4.5,0.3) {$+\infty$};
\node[left] at (-2.5,0.3) {$-\infty$};
\end{tikzpicture}
\end{document}
```