De la fuente **apuntesTX** (apuntesT0.pdf), presento el primer subtítulo hasta antes de detectar el segundo ("Valor absoluto"), integrando el complemento nivel B y las gráficas solicitadas.

## La recta real e intervalos

`````cornell
::cue
````marginalia %%> %%
Correspondencia biunívoca · Recta real · Intervalos · Subconjuntos de $\mathbb{R}$<br>
¿Cómo se relacionan los números reales con la geometría?<br>
¿Qué diferencia un intervalo abierto de uno cerrado?<br>
¿Cómo se representan los intervalos infinitos?<br>
$[a, b] = \{x / a \leq x \leq b\}$<br>
ver también: Números reales<br>
no confundir: $(a, b)$ como punto con $(a, b)$ como intervalo abierto.

````
::note
````marginalia %%< %%
Existe correspondencia biunívoca "uno a uno" entre el conjunto $\mathbb{R}$ y una recta a escala llamada la **recta real**.

```desmos-graph
left=-5; right=5; bottom=-1; top=1;
width=320; height=120;
---
y=0 | #005F73
(0,0) | label:0 | #005F73
(1,0) | label:1 | #005F73
(1.41,0) | label:1.41 | #EE9B00
(2,0) | label:2 | #005F73
(2.71,0) | label:e | #EE9B00
(3.14,0) | label:\pi | #EE9B00
```

```tikz

\begin{tikzpicture}[scale=1.5, >=stealth]
    % Eje principal
    \draw[<->, thick] (-3.5,0) -- (4.5,0) node[right] {$x$};

    % Marcas enteras
    \foreach \x in {-2,-1,0,1,2,3}
        \draw (\x, 0.1) -- (\x, -0.1) node[below] {\small $\x$};

    % Puntos notables de los apuntes
    \fill[orange] (1.414, 0) circle (1.2pt) node[above] {\small $\sqrt{2}$};
    \fill[orange] (2.718, 0) circle (1.2pt) node[above] {\small $e$};
    \fill[orange] (3.141, 0) circle (1.2pt) node[above] {\small $\pi$};

    % Etiquetas de infinito
    \node at (-3.8, 0) {\small $-\infty$};
    \node at (4.8, 0) {\small $+\infty$};
\end{tikzpicture}

```

Un **intervalo** es un subconjunto de la recta real.

1. **Intervalo cerrado**
	- $[a, b] = \{x / a \leq x \leq b\}$
	- Incluye valores extremos.

2. **Intervalo abierto**
	- $]a, b[ \text{ o } (a, b) = \{x / a < x < b\}$
	- No incluye extremos.

3. **Intervalos semiabiertos**
	- $]a, b] = \{x / a < x \leq b\}$
	- $[a, b[ = \{x / a \leq x < b\}$

4. **Intervalos infinitos**
	- $]a, +\infty[ = \{x / x > a\}$
	- $]-\infty, b[ = \{x / x < b\}$

> [!note] Nota del manuscrito
> Los corchetes invertidos $]a, b[$ se utilizan indistintamente con los paréntesis $(a, b)$ para denotar apertura.

`````

> [!summary] La recta real establece una relación biyectiva entre puntos y números, permitiendo definir intervalos como subconjuntos acotados o no acotados de $\mathbb{R}$.

> [!note] Complemento (Nivel B)
> 
> Según **Apostol (Cap. I 3.7)**, la interpretación geométrica de los números reales se basa en la elección de un punto de origen (0) y un punto unidad (1), lo cual determina la escala de la recta. Por su parte, **Stewart (9na Ed.)** enfatiza que un conjunto de números reales es un intervalo si contiene al menos dos números y a todos los números reales comprendidos entre cualquier par de sus elementos.
> 
> Formalmente, la **Propiedad de Completitud** (Axioma del Extremo Superior) asegura que no existen "huecos" en esta recta, permitiendo que cada punto corresponda exactamente a un número real, ya sea racional o irracional.



```tikz

\begin{tikzpicture}[scale=1.5, >=stealth]
    % Eje principal
    \draw[<->, thick] (-3.5,0) -- (4.5,0) node[right] {$x$};

    % Marcas enteras
    \foreach \x in {-2,-1,0,1,2,3}
        \draw (\x, 0.1) -- (\x, -0.1) node[below] {\small $\x$};

    % Puntos notables de los apuntes
    \fill[orange] (1.414, 0) circle (1.2pt) node[above] {\small $\sqrt{2}$};
    \fill[orange] (2.718, 0) circle (1.2pt) node[above] {\small $e$};
    \fill[orange] (3.141, 0) circle (1.2pt) node[above] {\small $\pi$};

    % Etiquetas de infinito
    \node at (-3.8, 0) {\small $-\infty$};
    \node at (4.8, 0) {\small $+\infty$};
\end{tikzpicture}

```



Esta es una representación detallada de la recta real siguiendo las reglas de estilo de la guía de **TikZJax**, aplicando una escala de 1.5 para mayor legibilidad. Se han incluido puntos notables (irracionales y constantes) en color `orange` para ilustrar la correspondencia biunívoca entre los números reales y la recta geométrica.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
    % Eje principal con flechas y etiquetas de infinito
    \draw[<->, thick, teal] (-5,0) -- (5,0) node[right, black] {$x$};
    \node at (-5.4, 0) {\small $-\infty$};
    \node at (5.4, 0) {\small $+\infty$};

    % Marcas para los números enteros
    \foreach \x in {-4,-3,-2,-1,0,1,2,3,4}
        \draw (\x, 0.1) -- (\x, -0.1) node[below] {\small $\x$};

    % Puntos irracionales y constantes notables en color orange
    \fill[orange] (-3.141, 0) circle (1.5pt) node[above] {\small $-\pi$};
    \fill[orange] (-2.718, 0) circle (1.5pt) node[above] {\small $-e$};
    \fill[orange] (1.414, 0) circle (1.5pt) node[above] {\small $\sqrt{2}$};
    \fill[orange] (3.141, 0) circle (1.5pt) node[above] {\small $\pi$};

    % Resaltado del origen
    \draw[thick] (0, 0.2) -- (0, -0.2);
\end{tikzpicture}
\end{document}
```

> [!note] Detalles técnicos
> 
> - **Ejes**: Se utiliza el color `teal` para el eje principal y flechas `->` en los extremos de acuerdo a los valores predeterminados de la guía.
> - **Puntos**: Los puntos destacados se marcan con un radio de `1.5pt` y etiquetas en modo matemático para mantener la precisión técnica requerida.
> - **Escala**: Se ajustó a `scale=1.5` para asegurar que las etiquetas de puntos cercanos como $-3$, $-\pi$ y $-e$ no se traslapen visualmente.