## IIR and FIR Filters

title: Complemento (Nivel C)

### 1. Explicación intuitiva

En el procesamiento digital de señales, los filtros se clasifican según la duración de su respuesta al impulso:

*   **FIR (Finite Impulse Response):** Son filtros de "respuesta finita". Imagina que golpeas una campana y el sonido se detiene abruptamente tras un tiempo determinado. En estos sistemas, la salida actual depende únicamente de los valores presentes y pasados de la **entrada**. No tienen realimentación (feedback), lo que los hace intrínsecamente estables y capaces de ofrecer una respuesta de fase perfectamente lineal [1], [2], [3].
*   **IIR (Infinite Impulse Response):** Son filtros de "respuesta infinita". Es como una campana cuya vibración, en teoría, nunca se detiene por completo porque la energía se realimenta. La salida actual depende no solo de las entradas, sino también de los valores pasados de la **salida**. Esto permite obtener filtros muy selectivos con pocos cálculos, pero introduce el riesgo de inestabilidad y distorsión de fase [4], [5], [6].

### 2. Definición formal

#### Filtros FIR
Un filtro FIR se describe mediante una ecuación de diferencia no recursiva de orden $N-1$:

$$
y(n) = \sum_{k=0}^{N-1} h(k)x(n-k)
$$

Donde $h(k)$ son los coeficientes de la respuesta al impulso de longitud finita $N$. Su función de transferencia en el dominio $z$ es un polinomio [2], [7]:

$$
H(z) = \sum_{k=0}^{N-1} h(k)z^{-k}
$$


#### Filtros IIR
Un filtro IIR se describe mediante una ecuación de diferencia recursiva:

$$
y(n) = \sum_{k=0}^{M} b_k x(n-k) - \sum_{k=1}^{N} a_k y(n-k)
$$

Donde la salida $y(n)$ se calcula recursivamente a partir de valores de salida anteriores. Su función de transferencia es una función racional [8], [6], [7]:

$$
H(z) = \frac{\sum_{k=0}^{M} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}
$$


### 3. Diagrama de bloques

La principal diferencia estructural es la presencia de la red de retroalimentación en el modelo IIR.

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, every node/.style={transform shape}]
    % FIR Diagram
    \node at (0,1.5) {\textbf{Estructura FIR (No recursiva)}};
    \draw[->] (-1,0) node[left] {\(x(n)\)} -- (0,0);
    \draw (0,0) circle (0.2) node {\(+\)};
    \draw[->] (0,0) -- (1.5,0) node[right] {\(y(n)\)};
    \draw[->] (-0.5,0) -- (-0.5,-0.8) -- (0,-0.8);
    \node[draw, rectangle] at (0.3,-0.8) {\(z^{-1}\)};
    \draw[->] (0.6,-0.8) -- (1,-0.8) -- (1,-0.2) -- (0.15,-0.15);
    \node at (1.2,-0.5) {\(b_k\)};

    % IIR Diagram
    \begin{scope}[yshift=-3cm]
    \node at (0,1.5) {\textbf{Estructura IIR (Recursiva)}};
    \draw[->] (-1,0) node[left] {\(x(n)\)} -- (0,0);
    \draw (0,0) circle (0.2) node {\(+\)};
    \draw[->] (0,0) -- (2,0) node[right] {\(y(n)\)};
    % Feedback path
    \draw[->] (1.5,0) -- (1.5,-1) -- (0.5,-1);
    \node[draw, rectangle] at (0,-1) {\(z^{-1}\)};
    \draw[->] (-0.5,-1) -- (-1,-1) -- (-1,-0.2) -- (-0.15,-0.15);
    \node at (-1.3,-0.6) {\(-a_k\)};
    \node at (1.7,-0.6) {Realimentación};
    \end{scope}
\end{tikzpicture}
\end{document}
```

### 4. Preguntas de comprensión

1.  ¿Por qué los filtros FIR son siempre estables a diferencia de los IIR?
2.  Si necesitas un filtro con fase lineal para procesar audio sin distorsionar el tiempo de llegada de las frecuencias, ¿qué tipo elegirías?
3.  ¿Qué ventaja computacional ofrece un filtro IIR frente a un FIR para cumplir una misma especificación de magnitud?

### 5. Ejercicios resueltos

##### Ej. 1: Identificación de sistema (Palani Ex. 3.9 modificado)
Dado el sistema $y(n) = 0.5 y(n-1) + x(n)$, determine si es FIR o IIR y halle su respuesta al impulso [9], [10].

**Resolución:**
1.  **Tipo:** Es un sistema **IIR** porque la salida depende de un valor pasado de la salida ($y(n-1)$), lo que implica recursividad [4], [11].
2.  **Respuesta al impulso $h(n)$:** Asumimos reposo inicial ($y(-1)=0$) y $x(n) = \delta(n)$ [12]:
    *   $n=0: h(0) = 0.5(0) + 1 = 1$
    *   $n=1: h(1) = 0.5(1) + 0 = 0.5$
    *   $n=2: h(2) = 0.5(0.5) + 0 = 0.25$
    *   En general: $h(n) = (0.5)^n u(n)$
Como el número de términos es infinito, se confirma que es IIR [9].

##### Ej. 2: Diseño de Filtro FIR (Hayes Schaum 8.3)
Dibuje la realización en forma directa de un filtro FIR cuya respuesta al impulso es $h(n) = \{1, 2, 3, 2, 1\}$ [13].

**Resolución:**
La ecuación de diferencia es:

$$
y(n) = x(n) + 2x(n-1) + 3x(n-2) + 2x(n-3) + x(n-4)
$$

Este es un filtro FIR de orden 4 (longitud $M=5$). La estructura utiliza una línea de retardo con tomas (tapped delay line) donde cada coeficiente $h(n)$ multiplica a la señal de entrada retardada [14], [15].

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[node distance=1.5cm, auto, >=stealth]
    \node (x) {\(x(n)\)};
    \node[draw, rectangle, right of=x] (z1) {\(z^{-1}\)};
    \node[draw, rectangle, right of=z1] (z2) {\(z^{-1}\)};
    \node[draw, rectangle, right of=z2] (z3) {\(z^{-1}\)};
    \node[draw, rectangle, right of=z3] (z4) {\(z^{-1}\)};
    
    \node[below of=x, node distance=1cm] (m0) {\(\times 1\)};
    \node[below of=z1, node distance=1cm] (m1) {\(\times 2\)};
    \node[below of=z2, node distance=1cm] (m2) {\(\times 3\)};
    \node[below of=z3, node distance=1cm] (m3) {\(\times 2\)};
    \node[below of=z4, node distance=1cm] (m4) {\(\times 1\)};
    
    \draw[->] (x) -- (z1); \draw[->] (z1) -- (z2); \draw[->] (z2) -- (z3); \draw[->] (z3) -- (z4);
    \draw[->] (x) -- (m0); \draw[->] (z1) -- (m1); \draw[->] (z2) -- (m2); \draw[->] (z3) -- (m3); \draw[->] (z4) -- (m4);
    
    \node[circle, draw, below of=m2, node distance=1cm] (sum) {\(+\)};
    \draw[->] (m0) |- (sum); \draw[->] (m1) |- (sum); \draw[->] (m2) -- (sum); 
    \draw[->] (m3) |- (sum); \draw[->] (m4) |- (sum);
    \draw[->] (sum) -- ++(1.5,0) node[right] {\(y(n)\)};
\end{tikzpicture}
\end{document}
```
