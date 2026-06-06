# Funciones reales

## Definición de función

$f$ es función si para cada $x$ de un conjunto $D$ (dominio) existe una ley, regla de correspondencia que le asigna un único $y$ de otro conjunto $R$ (imágenes) según:

$$
y=f(x)
$$

$\therefore$ " $y$ es función de $x$ según $f$ "

- En lenguaje matemático

$$
f \text{ es función}
\iff
(\forall x\in D)(\exists !\, y\in R)
/\; y=f(x)
$$

- De otro modo

$$f:D\to R$$
$$x\mapsto y$$
$$y=f(x)$$

- Notación conjuntista

$$
f=\{(x,y)\mid y=f(x),\;x\in D,\;y\in R\}
$$

Ej. de funciones
$$
f(x)=\frac{x^3-4x}{x^2+1}
$$
$$
f(x)=\ln(4x)+\arctan \!\left(
\frac{\sqrt{x-1}}{x}
\right)
$$
$$
y=\sqrt{x^3-x-1}+\cos(x^2)
$$
$$
y=e^{-2x}+\tanh (6x)+\operatorname{sech}(x)
$$
$$etc.$$

---

## Notación

En $y=f(x)$ se reemplaza en cualquier "$x$" en $f$.

### Ejemplo 1
$$
f(x)=2x^2-3x+1
$$

$$
\begin{array}{rcl}
f(3) & = & 2(3)^2-3(3)+1 \\
     & = & 2(9)-9+1 \\
     & = & 18-9+1 \\
     & = & 10
\end{array}
$$

$$
\begin{array}{rcl}
f(a) & = & 2a^2-3a+1
\end{array}
$$

$$
\begin{array}{rcl}
f(4x-5)
& = &
2(4x-5)^2-3(4x-5)+1
\\[4pt]
& = &
2(16x^2-40x+25)-12x+15+1
\\[4pt]
& = &
32x^2-80x+50-12x+16
\\[4pt]
& = &
32x^2-92x+66
\end{array}
$$

$$
\begin{array}{rcl}
f\!\left(\frac{2}{x^3}\right)
& = &
2\left(\frac{2}{x^3}\right)^2
-3\left(\frac{2}{x^3}\right)+1
\\[6pt]
& = &
2\left(\frac{4}{x^6}\right)
-\frac{6}{x^3}+1
\\[6pt]
& = &
\frac{8}{x^6}
-\frac{6}{x^3}
+1
\end{array}
$$
### Ejercicio 2

Analizar si $f$ es o no función.

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};
\node at (0,2.8) {$f$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, orange]
(a1) .. controls (-1,1.5) and (1,-1.5) .. (b6);

\draw[->, thick, blue!70!green]%teal]
(a2) -- (b5);

\draw[->, thick, color=olive]%green]
(a3) .. controls (-1,-1.5) and (1,1.5) .. (b4);

\end{tikzpicture}
\end{document}
```


$f$ sí es función.

$$  D_f=\{1,2,3\}  $$
$$R_f=\{4,5,6\}=rango,\ recorrido,\ codominio ,\text{ conjunto de imágenes}$$
  $$f={(1,6),(2,5),(3,4)}$$

- $\forall x$ del $D$ debe tener imagen.
- El $D$ debe ser único y no debe repetirse.
    

b)

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

\draw[->, thick, red]
(a1) .. controls (-1,1.2) and (1,0.6) .. (b5);

\draw[->, thick, blue]
(a2) -- (b5);

\draw[->, thick, green]
(a3) .. controls (-1,-1.2) and (1,-0.6) .. (b5);

\end{tikzpicture}
\end{document}
```

c)

```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 2);
\draw (4,0) ellipse (1 and 2);

\node at (-4,2.6) {$D$};
\node at (4,2.6) {$R$};

\node (a1) at (-4,1) {$1$};
\node (a2) at (-4,0) {$2$};
\node (a3) at (-4,-1) {$3$};

\node (b4) at (4,1) {$4$};
\node (b5) at (4,0) {$5$};
\node (b6) at (4,-1) {$6$};

% 1 -> 4
\draw[->, thick, red]
(a1) .. controls (-1,2) and (1,2) .. (b4);

% 1 -> 5
\draw[->, thick, blue]
(a1) .. controls (-1,0.8) and (1,0.4) .. (b5);

% 3 -> 5
\draw[->, thick, green]
(a3) .. controls (-1,-0.4) and (1,-0.2) .. (b5);

% 3 -> 6
\draw[->, thick, orange]
(a3) .. controls (-1,-2) and (1,-2) .. (b6);

\end{tikzpicture}
\end{document}
```








```tikz
\begin{document}
\begin{tikzpicture}

% Conjuntos
\draw (-3,0) ellipse (1 and 1.5);
\draw (3,0) ellipse (1 and 1.5);

% Nombres
\node at (-3,2) {$D$};
\node at (3,2) {$R$};

% Elementos
\node (x) at (-3,0) {$x$};
\node (y) at (3,0) {$y=f(x)$};

% Correspondencia
\draw[->, thick] (x) -- (y);
\node at (0,0.4) {$f$};

\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}

\draw (-4,0) ellipse (1 and 1.5);
\draw (0,0) ellipse (1 and 1.5);
\draw (4,0) ellipse (1 and 1.5);

\node at (-4,2) {$A$};
\node at (0,2) {$B$};
\node at (4,2) {$C$};

\node (x) at (-4,0) {$x$};
\node (gx) at (0,0) {$g(x)$};
\node (fgx) at (4,0) {$f(g(x))$};

\draw[->, thick] (x) -- (gx);
\node at (-2,0.4) {$g$};

\draw[->, thick] (gx) -- (fgx);
\node at (2,0.4) {$f$};

\draw[->, thick]
(-4,0.8) .. controls (0,2.5) .. (4,0.8);

\node at (0,2.9) {$f\circ g$};

\end{tikzpicture}
\end{document}
```


---
---
---

`red`rojo`green`verde`blue`azul`cyan`cian`magenta`magenta`yellow`amarillo`black`negro`white`blanco`gray` / `grey`gris`darkgray`gris oscuro`lightgray`gris claro`brown`marrón`lime`lima`olive`oliva`orange`naranja`pink`rosa`purple`púrpura`teal`turquesa`violet`violeta


---
---





            
        - Álgebra de funciones
            
        - Función par
            
        - Función impar
            
        - Función periódica
            
        - Función inversa
            

- Álgebra de funciones
    
    - Suma de funciones
        
    - Producto de funciones
        
    - Cociente de funciones
        
    - Dominio de una función
        
        - Funciones racionales
            
        - Funciones radicales
            
        - Funciones logarítmicas
            
        - Funciones exponenciales
            
        - Funciones trigonométricas inversas
            
