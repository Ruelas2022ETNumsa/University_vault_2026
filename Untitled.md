## La recta real intervalos

`````cornell
::cue

Correspondencia biunívoca<br>%%> izp1%%
recta real · intervalo · subconjunto · puntos extremos<br>
¿Cómo se define la correspondencia entre los números reales y la recta?<br>
¿Qué es un intervalo en el contexto de los números reales?<br>
¿Cuáles son las distintas formas de representar un intervalo?<br>
```marginalia

%%> pruba papuy $[a, b] = \{x \in \mathbb{R} \mid a \leq x \leq b\}$<br> %%
```

```marginalia
ver también: axiomas de orden<br>%%> izp2manolo%%
no confundir: corchete $[...]$ (incluye) con paréntesis o corchete invertido $]...[$ (excluye)
```






::note

````marginalia
Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.%%< prueba xxx%%
````
````marginalia

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

\filldraw (1.414,0) circle (1.5pt) node[above] {$\sqrt{2}$}; % COMENTAROOI
\filldraw (2.718,0) circle (1.5pt) node[above] {$e$};
\filldraw (3.141,0) circle (1.5pt) node[above] {$\pi$};

\node[right] at (4.5,0.3) {$+\infty$};
\node[left] at (-2.5,0.3) {$-\infty$};
\end{tikzpicture}
\end{document}
```


%%<! panamericana%%
````


````marginalia
- Un intervalo es un subconjunto de la recta real.

1. **Intervalo cerrado**%%< prueba 2pppppp%%
````   
   
   
   
	- $[a, b] = \{x / a \leq x \leq b\}$
	- Posee valores extremos.
	  
	  
	  
````marginalia
ACACAACAC%%< esto es una prueba%%
```desmos-graph
left=-1; right=5;
bottom=-1; top=1;
---
y=0 | #005F73
(1,0) | #005F73 | label: a
(4,0) | #005F73 | label: b
0 | 1 < x < 4 | #94D2BD
(4,0) | #005F73 | label HIDDEN: XXX |HIDDEN |
```
````	  
2. **Intervalo semiabierto (izquierda)**
	- $]a, b] = \{x / a < x \leq b\}$
```desmos-graph%%< prueba 3%%
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

5. **Intervalo infinito (izquierda)** %%<! prueba 5%%
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

> [!summary] Los intervalos son subconjuntos continuos de la recta real que representan segmentos (acotados) o  %%<! prueba 5%%
> semirrectas (infinitos) definidos por desigualdades.

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