Explicá / definí Convolución Circular — Palani Cap. 2

Dado:
x1(n) = {2, 1, 2, 1} (origen en n=0)
x2(n) = {1, 2, 3, 4} (origen en n=0)
N = 4

Resolvé x3(m) = x1(n) ⊛ x2(n) paso a paso usando el método gráfico de círculos concéntricos (Palani Fig. 2.11) para cada valor de m = 0, 1, 2, 3.
Incluí el diagrama TikZJax para cada paso m.
Resultado esperado: x3(m) = {14, 16, 14, 16}

---


## Convolución Circular

### 1. Explicación intuitiva
La **convolución circular** es una operación matemática fundamental que combina dos secuencias discretas de longitud finita para producir una tercera secuencia de igual longitud. A diferencia de la convolución lineal, donde las señales se desplazan de manera infinita sobre un eje horizontal recto, en la convolución circular las secuencias se conciben como si estuvieran distribuidas sobre una estructura periódica o circular. 

Para visualizar el proceso mediante el **método gráfico de círculos concéntricos**, una de las señales permanece fija sobre un círculo exterior (en sentido antihorario), mientras que la otra señal se coloca en un círculo interior concéntrico, pero reflejada temporalmente (en sentido horario). Al multiplicar término a término los valores que coinciden radialmente y sumar dichos productos, se obtiene el resultado para el instante actual. Para calcular los instantes sucesivos, el círculo interior se hace rotar paso a paso en sentido antihorario, repitiendo el proceso de multiplicación y suma. Esta operación es de vital importancia en el procesamiento digital de señales, ya que modela de manera exacta la multiplicación de las señales en el dominio de la frecuencia mediante la **Transformada Discreta de Fourier $DFT$**.

### 2. Definición formal
Para dos secuencias periódicas o de longitud finita $x_1(n)$ y $x_2(n)$ de longitud $N$, la convolución circular $x_3(m)$ se define formalmente como:

$$
x_3(m) = x_1(n) \circledcirc_N x_2(n) = \sum_{n=0}^{N-1} x_1(n) x_2((m-n)_N)
$$

donde $(m-n)_N$ representa la operación de índice circular o módulo $N$. Esto garantiza que los índices de las señales siempre permanezcan dentro del rango de $0$ a $N-1$.

### 3. Figura o diagrama
A continuación se presentan los diagramas de **círculos concéntricos** correspondientes a cada uno de los pasos $m = 0, 1, 2, 3$ para calcular la convolución circular de las secuencias dadas:

#### Paso $m = 0$
En este estado inicial, la secuencia exterior $x_1(n)$ se distribuye en sentido antihorario $CCW$ a intervalos de $90^\circ$ comenzando desde $0^\circ$. La secuencia interior $x_2(n)$ se distribuye en sentido horario $CW$ comenzando también desde $0^\circ$ sin ninguna rotación.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.2cm);
  \draw[thick, orange] (0,0) circle (0.6cm);
  \draw[dashed, gray!50] (-1.6,0) -- (1.6,0);
  \draw[dashed, gray!50] (0,-1.6) -- (0,1.6);
  
  % Círculo exterior x1(n) - Fijo (CCW desde 0°)
  \node[teal, anchor=west] at (0:1.25cm) {\(x_1(0)=2\)};
  \node[teal, anchor=south] at (90:1.25cm) {\(x_1(1)=1\)};
  \node[teal, anchor=east] at (180:1.25cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north] at (270:1.25cm) {\(x_1(3)=1\)};
  
  % Puntos exterior (orange sobre teal)
  \fill[orange] ( 1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,    1.2) circle (0.05cm);
  \fill[orange] (-1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,   -1.2) circle (0.05cm);
  % Puntos interior (teal sobre orange)
  \fill[teal] ( 0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,   -0.6) circle (0.05cm);
  \fill[teal] (-0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,    0.6) circle (0.05cm);
  % Círculo interior x2(n) - m=0 (CW desde 0°)
  \node[orange, anchor=west]  at (0:0.65cm)   {\(x_2(0)=1\)};
  \node[orange, anchor=north] at (270:0.65cm) {\(x_2(1)=2\)};
  \node[orange, anchor=east]  at (180:0.65cm) {\(x_2(2)=3\)};
  \node[orange, anchor=south] at (90:0.65cm)  {\(x_2(3)=4\)};
  
  % Sentido de giro
  \draw[->, teal] (1.3,1.3) arc (45:75:1.5) node[midway, above right] {CCW};
  \draw[<-, orange] (0.5,-0.5) arc (-45:-75:0.7) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 1$
El círculo interior rota $90^\circ$ en sentido antihorario $CCW$, desplazando los valores de $x_2$ una posición en sentido antihorario.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.2cm);
  \draw[thick, orange] (0,0) circle (0.6cm);
  \draw[dashed, gray!50] (-1.6,0) -- (1.6,0);
  \draw[dashed, gray!50] (0,-1.6) -- (0,1.6);
  
  % Círculo exterior x1(n) - Fijo
  \node[teal, anchor=west] at (0:1.25cm) {\(x_1(0)=2\)};
  \node[teal, anchor=south] at (90:1.25cm) {\(x_1(1)=1\)};
  \node[teal, anchor=east] at (180:1.25cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north] at (270:1.25cm) {\(x_1(3)=1\)};
  
  % Puntos exterior
  \fill[orange] ( 1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,    1.2) circle (0.05cm);
  \fill[orange] (-1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,   -1.2) circle (0.05cm);
  % Puntos interior
  \fill[teal] ( 0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,   -0.6) circle (0.05cm);
  \fill[teal] (-0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,    0.6) circle (0.05cm);
  % Círculo interior x2(n) - m=1 (Rotado 90° CCW)
  \node[orange, anchor=west]  at (0:0.65cm)   {\(x_2(1)=2\)};
  \node[orange, anchor=north] at (270:0.65cm) {\(x_2(2)=3\)};
  \node[orange, anchor=east]  at (180:0.65cm) {\(x_2(3)=4\)};
  \node[orange, anchor=south] at (90:0.65cm)  {\(x_2(0)=1\)};
  
  % Sentido de giro
  \draw[->, teal] (1.3,1.3) arc (45:75:1.5) node[midway, above right] {CCW};
  \draw[<-, orange] (0.5,-0.5) arc (-45:-75:0.7) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 2$
El círculo interior se rota otros $90^\circ$ en sentido antihorario $CCW$, lo que equivale a un desplazamiento total de $180^\circ$ respecto al estado inicial.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.2cm);
  \draw[thick, orange] (0,0) circle (0.6cm);
  \draw[dashed, gray!50] (-1.6,0) -- (1.6,0);
  \draw[dashed, gray!50] (0,-1.6) -- (0,1.6);
  
  % Círculo exterior x1(n) - Fijo
  \node[teal, anchor=west] at (0:1.25cm) {\(x_1(0)=2\)};
  \node[teal, anchor=south] at (90:1.25cm) {\(x_1(1)=1\)};
  \node[teal, anchor=east] at (180:1.25cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north] at (270:1.25cm) {\(x_1(3)=1\)};
  
  % Puntos exterior
  \fill[orange] ( 1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,    1.2) circle (0.05cm);
  \fill[orange] (-1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,   -1.2) circle (0.05cm);
  % Puntos interior
  \fill[teal] ( 0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,   -0.6) circle (0.05cm);
  \fill[teal] (-0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,    0.6) circle (0.05cm);
  % Círculo interior x2(n) - m=2 (Rotado 180° CCW)
  \node[orange, anchor=west]  at (0:0.65cm)   {\(x_2(2)=3\)};
  \node[orange, anchor=north] at (270:0.65cm) {\(x_2(3)=4\)};
  \node[orange, anchor=east]  at (180:0.65cm) {\(x_2(0)=1\)};
  \node[orange, anchor=south] at (90:0.65cm)  {\(x_2(1)=2\)};
  
  % Sentido de giro
  \draw[->, teal] (1.3,1.3) arc (45:75:1.5) node[midway, above right] {CCW};
  \draw[<-, orange] (0.5,-0.5) arc (-45:-75:0.7) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 3$
El círculo interior se rota una vez más $90^\circ$ CCW, logrando un desplazamiento total de $270^\circ$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (1.2cm);
  \draw[thick, orange] (0,0) circle (0.6cm);
  \draw[dashed, gray!50] (-1.6,0) -- (1.6,0);
  \draw[dashed, gray!50] (0,-1.6) -- (0,1.6);
  
  % Círculo exterior x1(n) - Fijo
  \node[teal, anchor=west] at (0:1.25cm) {\(x_1(0)=2\)};
  \node[teal, anchor=south] at (90:1.25cm) {\(x_1(1)=1\)};
  \node[teal, anchor=east] at (180:1.25cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north] at (270:1.25cm) {\(x_1(3)=1\)};
  
  % Puntos exterior
  \fill[orange] ( 1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,    1.2) circle (0.05cm);
  \fill[orange] (-1.2,  0)   circle (0.05cm);
  \fill[orange] ( 0,   -1.2) circle (0.05cm);
  % Puntos interior
  \fill[teal] ( 0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,   -0.6) circle (0.05cm);
  \fill[teal] (-0.6,  0)   circle (0.05cm);
  \fill[teal] ( 0,    0.6) circle (0.05cm);
  % Círculo interior x2(n) - m=3 (Rotado 270° CCW)
  \node[orange, anchor=west]  at (0:0.65cm)   {\(x_2(3)=4\)};
  \node[orange, anchor=north] at (270:0.65cm) {\(x_2(0)=1\)};
  \node[orange, anchor=east]  at (180:0.65cm) {\(x_2(1)=2\)};
  \node[orange, anchor=south] at (90:0.65cm)  {\(x_2(2)=3\)};
  
  % Sentido de giro
  \draw[->, teal] (1.3,1.3) arc (45:75:1.5) node[midway, above right] {CCW};
  \draw[<-, orange] (0.5,-0.5) arc (-45:-75:0.7) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

### 4. Preguntas de comprensión
1. **¿Por qué la longitud de la secuencia resultante de una convolución circular de dos señales de longitud $N$ es igual a $N$ y no a $2N-1$?**
   *Respuesta:* Debido a que los índices de las señales involucradas se evalúan de manera periódica utilizando la operación módulo $N$. Esto provoca que cualquier muestra desplazada fuera del rango básico de $0$ a $N-1$ vuelva a aparecer de manera circular dentro de este intervalo, manteniendo la longitud constante.
2. **¿Qué técnica se debe implementar para obtener los mismos resultados que una convolución lineal utilizando la convolución circular?**
   *Respuesta:* Se debe aplicar **relleno de ceros (zero padding)** a ambas secuencias de modo que alcancen una longitud mínima común de $L \geq N_1 + N_2 - 1$ muestras antes de realizar la convolución circular.

---

### 5. Ejercicios resueltos

##### Ej. Convolución circular paso a paso
Dadas las secuencias discretas de período $N = 4$:

$$
x_1(n) = \{2, 1, 2, 1\}
$$


$$
x_2(n) = \{1, 2, 3, 4\}
$$

Determine la secuencia resultante de la convolución circular $x_3(m) = x_1(n) \circledcirc_4 x_2(n)$ para cada instante $m = 0, 1, 2, 3$ utilizando el método gráfico.

**Resolución:**

A partir de la definición formal y el análisis de la disposición de las muestras en los diagramas de círculos concéntricos presentados, realizamos los cálculos detallados para cada valor de $m$:

*   **Para $m = 0$:**
    Multiplicando las muestras radialmente correspondientes en el primer diagrama (sin rotar):
    
$$
x_3(0) = x_1(0)x_2(0) + x_1(1)x_2(3) + x_1(2)x_2(2) + x_1(3)x_2(1)
$$

    
$$
x_3(0) = (2 \cdot 1) + (1 \cdot 4) + (2 \cdot 3) + (1 \cdot 2)
$$

    
$$
x_3(0) = 2 + 4 + 6 + 2 = 14
$$


*   **Para $m = 1$:**
    Haciendo rotar el círculo interno $90^\circ$ CCW, se obtienen las nuevas alineaciones radiales:
    
$$
x_3(1) = x_1(0)x_2(1) + x_1(1)x_2(0) + x_1(2)x_2(3) + x_1(3)x_2(2)
$$

    
$$
x_3(1) = (2 \cdot 2) + (1 \cdot 1) + (2 \cdot 4) + (1 \cdot 3)
$$

    
$$
x_3(1) = 4 + 1 + 8 + 3 = 16
$$


*   **Para $m = 2$:**
    Rotando la secuencia interna otros $90^\circ$ CCW (desplazamiento de $180^\circ$ del estado original):
    
$$
x_3(2) = x_1(0)x_2(2) + x_1(1)x_2(1) + x_1(2)x_2(0) + x_1(3)x_2(3)
$$

    
$$
x_3(2) = (2 \cdot 3) + (1 \cdot 2) + (2 \cdot 1) + (1 \cdot 4)
$$

    
$$
x_3(2) = 6 + 2 + 2 + 4 = 14
$$


*   **Para $m = 3$:**
    Efectuando la última rotación de $90^\circ$ CCW en el círculo interno (desplazamiento de $270^\circ$):
    
$$
x_3(3) = x_1(0)x_2(3) + x_1(1)x_2(2) + x_1(2)x_2(1) + x_1(3)x_2(0)
$$

    
$$
x_3(3) = (2 \cdot 4) + (1 \cdot 3) + (2 \cdot 2) + (1 \cdot 1)
$$

    
$$
x_3(3) = 8 + 3 + 4 + 1 = 16
$$


**Resultado final:**
La secuencia resultante de la convolución circular es:

$$
\mathbf{x_3(m) = \{14, 16, 14, 16\}}
$$


---

##### Ej. Convolución circular de mayor dificultad (N = 4, con señales alternantes)
Determine la convolución circular $y(m) = x_1(n) \circledcirc_4 h(n)$ para las siguientes secuencias de longitud $N = 4$:

$$
x_1(n) = \{1, -1, 2, -2\}
$$


$$
h(n) = \{2, 1, 0, -1\}
$$


**Resolución:**
Para resolver este ejercicio mediante un procedimiento algebraico equivalente y riguroso, podemos formular la multiplicación utilizando la **representación matricial** de la convolución circular, donde la señal $h(n)$ se estructura como una **matriz circulante** y $x_1(n)$ como un vector columna:


$$
\begin{bmatrix} y(0) \\ y(1) \\ y(2) \\ y(3) \end{bmatrix} = \begin{bmatrix} h(0) & h(3) & h(2) & h(1) \\ h(1) & h(0) & h(3) & h(2) \\ h(2) & h(1) & h(0) & h(3) \\ h(3) & h(2) & h(1) & h(0) \end{bmatrix} \begin{bmatrix} x_1(0) \\ x_1(1) \\ x_1(2) \\ x_1(3) \end{bmatrix}
$$


Reemplazando los valores dados de $h(n)$ y $x_1(n)$:

$$
\begin{bmatrix} y(0) \\ y(1) \\ y(2) \\ y(3) \end{bmatrix} = \begin{bmatrix} 2 & -1 & 0 & 1 \\ 1 & 2 & -1 & 0 \\ 0 & 1 & 2 & -1 \\ -1 & 0 & 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \\ 2 \\ -2 \end{bmatrix}
$$


Realizando el producto fila por columna de manera detallada:
*   
$$
y(0) = (2 \cdot 1) + (-1 \cdot (-1)) + (0 \cdot 2) + (1 \cdot (-2)) = 2 + 1 + 0 - 2 = 1
$$

*   
$$
y(1) = (1 \cdot 1) + (2 \cdot (-1)) + (-1 \cdot 2) + (0 \cdot (-2)) = 1 - 2 - 2 + 0 = -3
$$

*   
$$
y(2) = (0 \cdot 1) + (1 \cdot (-1)) + (2 \cdot 2) + (-1 \cdot (-2)) = 0 - 1 + 4 + 2 = 5
$$

*   
$$
y(3) = (-1 \cdot 1) + (0 \cdot (-1)) + (1 \cdot 2) + (2 \cdot (-2)) = -1 + 0 + 2 - 4 = -3
$$


**Resultado final:**
La secuencia resultante de la convolución circular es:

$$
\mathbf{y(m) = \{1, -3, 5, -3\}}
$$

