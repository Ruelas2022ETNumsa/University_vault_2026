Explicá / definí Convolución Circular — Palani Cap. 2

Dado:
x1(n) = {2, 1, 2, 1} (origen en n=0)
x2(n) = {1, 2, 3, 4} (origen en n=0)
N = 4

Resolvé x3(m) = x1(n) ⊛ x2(n) paso a paso usando el método gráfico de círculos concéntricos (Palani Fig. 2.11) para cada valor de m = 0, 1, 2, 3.
Incluí el diagrama TikZJax para cada paso m.
Resultado esperado: x3(m) = {14, 16, 14, 16}

---



## [2. Convolución Circular]

````ad-note
title: Complemento (Nivel C)

1. Explicación intuitiva
La convolución circular es una operación fundamental en el procesamiento digital de señales discretas que permite combinar dos secuencias de igual longitud mediante un proceso de traslape y suma periódica. A diferencia de la convolución lineal ordinaria, donde las señales se desplazan infinitamente a lo largo de una línea de tiempo recta, en la convolución circular imaginamos que ambas secuencias están dispuestas sobre círculos concéntricos. Al mantener una secuencia fija en el círculo exterior y rotar la otra secuencia en el círculo interior, los valores alineados radialmente se multiplican y se suman para cada muestra de salida. El resultado tiene siempre la misma longitud fija que las señales de entrada. Este método describe exactamente lo que ocurre en el dominio del tiempo discreto cuando multiplicamos término a terminos las DFT de dos señales en el dominio de la frecuencia.

2. Definición formal
Según el libro de texto base (Palani, Cap. 2), la convolución circular de dos secuencias de $N$ puntos, $x_1(n)$ y $x_2(n)$, se define matemáticamente como:

$$
x_3(m) = x_1(n) \circledast_N x_2(n) = \sum_{n=0}^{N-1} x_1(n) x_2((m - n)_N), \quad m = 0, 1, \dots, N-1
$$

donde el término $(m - n)_N$ denota el índice temporal evaluado módulo $N$, es decir, el residuo de $(m-n) \pmod N$.

3. Figura o diagrama (si existe o aplica visualización)

[[S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf#page=139]]
*Fig. 2.11*
*Circular convolution of Example 2.22.*
%%IMA-SRC | fuente: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf | página: 139 | id: Fig. 2.11 | posición: centro de la página%%
justificación: Esta figura ilustra el método gráfico de círculos concéntricos para resolver la convolución circular de dos señales paso a paso.

4. Preguntas de comprensión (solo nivel B/C conceptual)
5. ¿Cuál es la principal diferencia entre la convolución lineal y la convolución circular en términos de la longitud del vector resultante?
6. ¿Por qué es necesario aplicar relleno de ceros (zero-padding) si se desea que el resultado de una convolución circular sea idéntico al de una convolución lineal?
7. Si rotamos la secuencia interna en sentido antihorario para calcular $x_3(m)$, ¿qué operación de desplazamiento temporal discreto se está implementando físicamente?

8. Ejercicios resueltos (solo nivel C)

##### Ej. 1: Convolución circular por método gráfico de círculos concéntricos
Dadas las secuencias discretas de $N = 4$ puntos:

$$
x_1(n) = \{2, 1, 2, 1\} \quad \text{con origen en } n = 0
$$


$$
x_2(n) = \{1, 2, 3, 4\} \quad \text{con origen en } n = 0
$$

Calcular $x_3(m) = x_1(n) \circledast x_2(n)$ paso a paso empleando el método gráfico de círculos concéntricos para $m = 0, 1, 2, 3$.

###### Paso para $m = 0$:
1. Graficamos los $N=4$ valores de $x_1(n)$ espaciados uniformemente en el círculo exterior en sentido antihorario $CCW$, comenzando con $x_1(0) = 2$ a las 12 en punto.
2. Graficamos los $N=4$ valores de $x_2(0-n)_N = x_2((-n))_N$ en el círculo interior en sentido horario $CW$, comenzando con $x_2(0) = 1$ a las 12 en punto. Esto ubica a $x_2(3)=4$ a las 9 en punto, $x_2(2)=3$ a las 6 en punto y $x_2(1)=2$ a las 3 en punto.
3. Multiplicamos las muestras radialmente coincidentes y sumamos los productos:

$$
x_3(0) = (2 \cdot 1) + (1 \cdot 4) + (2 \cdot 3) + (1 \cdot 2) = 2 + 4 + 6 + 2 = 14
$$


```tikz
\usepackage{tikz}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.8cm);
  \draw[thick, orange] (0,0) circle (1.1cm);
  
  % Ejes de referencia
  \draw[gray, dashed] (-2.2,0) -- (2.2,0);
  \draw[gray, dashed] (0,-2.2) -- (0,2.2);
  
  % Indicadores de dirección
  \draw[->, teal, thick] (40:1.8) arc (40:65:1.8);
  \node[teal, right] at (52:1.8) {\scriptsize CCW};
  \draw[<-, orange, thick] (115:1.1) arc (115:140:1.1);
  \node[orange, left] at (127:1.1) {\scriptsize CW};
  
  % Valores círculo exterior (x1) - Fijo en CCW
  \node[teal] at (0, 2.05) {\scriptsize $x_1(0)=2$};
  \node[teal] at (-2.1, 0) {\scriptsize $x_1(1)=1$};
  \node[teal] at (0, -2.05) {\scriptsize $x_1(2)=2$};
  \node[teal] at (2.1, 0) {\scriptsize $x_1(3)=1$};
  
  % Valores círculo interior (x2) - Clockwise m=0
  \node[orange] at (0, 0.75) {\scriptsize $x_2(0)=1$};
  \node[orange] at (-0.65, 0) {\scriptsize $x_2(3)=4$};
  \node[orange] at (0, -0.75) {\scriptsize $x_2(2)=3$};
  \node[orange] at (0.65, 0) {\scriptsize $x_2(1)=2$};
  
  % Centro
  \node[draw, fill=white, inner sep=2pt] at (0,0) {\small $m=0$};
\end{tikzpicture}
\end{document}
```

###### Paso para $m = 1$:
1. Rotamos el círculo interior una posición en sentido antihorario $CCW$. El valor $x_2(1)=2$ se mueve a las 12 en punto, $x_2(0)=1$ a las 9 en punto, $x_2(3)=4$ a las 6 en punto y $x_2(2)=3$ a las 3 en punto.
2. Multiplicamos y sumamos los productos correspondientes:

$$
x_3(1) = (2 \cdot 2) + (1 \cdot 1) + (2 \cdot 4) + (1 \cdot 3) = 4 + 1 + 8 + 3 = 16
$$


```tikz
\usepackage{tikz}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.8cm);
  \draw[thick, orange] (0,0) circle (1.1cm);
  
  % Ejes de referencia
  \draw[gray, dashed] (-2.2,0) -- (2.2,0);
  \draw[gray, dashed] (0,-2.2) -- (0,2.2);
  
  % Indicadores de dirección
  \draw[->, teal, thick] (40:1.8) arc (40:65:1.8);
  \node[teal, right] at (52:1.8) {\scriptsize CCW};
  \draw[<-, orange, thick] (115:1.1) arc (115:140:1.1);
  \node[orange, left] at (127:1.1) {\scriptsize CW};
  
  % Valores círculo exterior (x1) - Fijo en CCW
  \node[teal] at (0, 2.05) {\scriptsize $x_1(0)=2$};
  \node[teal] at (-2.1, 0) {\scriptsize $x_1(1)=1$};
  \node[teal] at (0, -2.05) {\scriptsize $x_1(2)=2$};
  \node[teal] at (2.1, 0) {\scriptsize $x_1(3)=1$};
  
  % Valores círculo interior (x2) - Rotado 1 CCW
  \node[orange] at (0, 0.75) {\scriptsize $x_2(1)=2$};
  \node[orange] at (-0.65, 0) {\scriptsize $x_2(0)=1$};
  \node[orange] at (0, -0.75) {\scriptsize $x_2(3)=4$};
  \node[orange] at (0.65, 0) {\scriptsize $x_2(2)=3$};
  
  % Centro
  \node[draw, fill=white, inner sep=2pt] at (0,0) {\small $m=1$};
\end{tikzpicture}
\end{document}
```

###### Paso para $m = 2$:
1. Rotamos el círculo interior una segunda posición en sentido antihorario $CCW$. El valor $x_2(2)=3$ se mueve a las 12 en punto, $x_2(1)=2$ a las 9 en punto, $x_2(0)=1$ a las 6 en punto y $x_2(3)=4$ a las 3 en punto.
2. Multiplicamos y sumamos los productos correspondientes:

$$
x_3(2) = (2 \cdot 3) + (1 \cdot 2) + (2 \cdot 1) + (1 \cdot 4) = 6 + 2 + 2 + 4 = 14
$$


```tikz
\usepackage{tikz}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.8cm);
  \draw[thick, orange] (0,0) circle (1.1cm);
  
  % Ejes de referencia
  \draw[gray, dashed] (-2.2,0) -- (2.2,0);
  \draw[gray, dashed] (0,-2.2) -- (0,2.2);
  
  % Indicadores de dirección
  \draw[->, teal, thick] (40:1.8) arc (40:65:1.8);
  \node[teal, right] at (52:1.8) {\scriptsize CCW};
  \draw[<-, orange, thick] (115:1.1) arc (115:140:1.1);
  \node[orange, left] at (127:1.1) {\scriptsize CW};
  
  % Valores círculo exterior (x1) - Fijo en CCW
  \node[teal] at (0, 2.05) {\scriptsize $x_1(0)=2$};
  \node[teal] at (-2.1, 0) {\scriptsize $x_1(1)=1$};
  \node[teal] at (0, -2.05) {\scriptsize $x_1(2)=2$};
  \node[teal] at (2.1, 0) {\scriptsize $x_1(3)=1$};
  
  % Valores círculo interior (x2) - Rotado 2 CCW
  \node[orange] at (0, 0.75) {\scriptsize $x_2(2)=3$};
  \node[orange] at (-0.65, 0) {\scriptsize $x_2(1)=2$};
  \node[orange] at (0, -0.75) {\scriptsize $x_2(0)=1$};
  \node[orange] at (0.65, 0) {\scriptsize $x_2(3)=4$};
  
  % Centro
  \node[draw, fill=white, inner sep=2pt] at (0,0) {\small $m=2$};
\end{tikzpicture}
\end{document}
```

###### Paso para $m = 3$:
1. Rotamos el círculo interior una tercera posición en sentido antihorario $CCW$. El valor $x_2(3)=4$ se mueve a las 12 en punto, $x_2(2)=3$ a las 9 en punto, $x_2(1)=2$ a las 6 en punto y $x_2(0)=1$ a las 3 en punto.
2. Multiplicamos y sumamos los productos correspondientes:

$$
x_3(3) = (2 \cdot 4) + (1 \cdot 3) + (2 \cdot 2) + (1 \cdot 1) = 8 + 3 + 4 + 1 = 16
$$


```tikz
\usepackage{tikz}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, >=latex]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.8cm);
  \draw[thick, orange] (0,0) circle (1.1cm);
  
  % Ejes de referencia
  \draw[gray, dashed] (-2.2,0) -- (2.2,0);
  \draw[gray, dashed] (0,-2.2) -- (0,2.2);
  
  % Indicadores de dirección
  \draw[->, teal, thick] (40:1.8) arc (40:65:1.8);
  \node[teal, right] at (52:1.8) {\scriptsize CCW};
  \draw[<-, orange, thick] (115:1.1) arc (115:140:1.1);
  \node[orange, left] at (127:1.1) {\scriptsize CW};
  
  % Valores círculo exterior (x1) - Fijo en CCW
  \node[teal] at (0, 2.05) {\scriptsize $x_1(0)=2$};
  \node[teal] at (-2.1, 0) {\scriptsize $x_1(1)=1$};
  \node[teal] at (0, -2.05) {\scriptsize $x_1(2)=2$};
  \node[teal] at (2.1, 0) {\scriptsize $x_1(3)=1$};
  
  % Valores círculo interior (x2) - Rotado 3 CCW
  \node[orange] at (0, 0.75) {\scriptsize $x_2(3)=4$};
  \node[orange] at (-0.65, 0) {\scriptsize $x_2(2)=3$};
  \node[orange] at (0, -0.75) {\scriptsize $x_2(1)=2$};
  \node[orange] at (0.65, 0) {\scriptsize $x_2(0)=1$};
  
  % Centro
  \node[draw, fill=white, inner sep=2pt] at (0,0) {\small $m=3$};
\end{tikzpicture}
\end{document}
```

###### Resultado Final de la Convolución Circular:
Uniendo todos los términos discretos obtenidos:

$$
\boxed{x_3(m) = \{14, 16, 14, 16\}, \quad m = 0, 1, 2, 3}
$$

````
