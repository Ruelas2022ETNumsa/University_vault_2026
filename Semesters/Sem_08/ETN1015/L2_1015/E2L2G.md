Explicá / definí Convolución Circular (x2 modificada) — Palani Cap. 2

Dado:
x1(n) = {2, 1, 2, 1, 0} (zero-pad a N=5)
x2(n) = {1, 2, 3, 4, 5} (origen en n=0)
N = 5

Resolvé x3(m) = x1(n) ⊛ x2(n) paso a paso usando el método gráfico de círculos concéntricos (Palani Fig. 2.11) para cada valor de m = 0, 1, 2, 3, 4.
Incluí el diagrama TikZJax para cada paso m.

---
## Convolución Circular con Secuencia Modificada

title: Complemento (Nivel C)

### 1. Explicación intuitiva
La **convolución circular** es una operación de filtrado digital que opera sobre secuencias periódicas o de duración finita en un espacio de indexación cerrado. A diferencia de la convolución lineal convencional, en la que las secuencias se deslizan indefinidamente sobre una recta temporal infinita, en la convolución circular el desplazamiento se efectúa dentro de un anillo periódico de longitud fija $N$.

Mediante el **método de círculos concéntricos** de Palani, representamos las señales espacialmente en dos anillos concéntricos. El círculo exterior se configura de manera estática situando los valores de la secuencia $x_1(n)$ distribuidos uniformemente en sentido antihorario a intervalos angulares constantes de $\Delta\theta = 360^\circ/N$. El círculo interior aloja los valores de la segunda secuencia $x_2(n)$ dispuestos en sentido horario, lo que emula la inversión temporal requerida por la definición de la convolución. Cada muestra del resultado $x_3(m)$ se determina multiplicando par a par los elementos alineados radialmente y sumando estos productos. Para progresar en el tiempo discreto, el círculo interior rota paso a paso en sentido antihorario, alineando periódicamente nuevos pares de muestras sin desbordar jamás el límite espacial impuesto por $N$.

### 2. Definición formal
Dadas dos secuencias discretas $x_1(n)$ y $x_2(n)$ de longitud finita $N$, su convolución circular de $N$ puntos se define matemáticamente como la suma ponderada periódica:

$$
x_3(m) = x_1(n) \circledcirc_N x_2(n) = \sum_{n=0}^{N-1} x_1(n) x_2((m-n)_N)
$$

donde $(m-n)_N$ indica la operación de índice módulo $N$. Esta indexación cíclica restringe la evaluación temporal estrictamente al intervalo finito:

$$
0 \le m \le N-1
$$


---

### 3. Figuras y diagramas de círculos concéntricos ($N=5$)
Para una longitud $N = 5$, el espaciado angular uniforme entre muestras es de $\Delta\theta = 72^\circ$. 

*   La secuencia exterior **$x_1(n)$** permanece fija en sentido antihorario $CCW$ en las posiciones angulares: $0^\circ$, $72^\circ$, $144^\circ$, $216^\circ$ y $288^\circ$.
*   La secuencia interior **$x_2(n)$** se refleja inicialmente en sentido horario $CW$ para $m=0$, y en cada incremento temporal rota $72^\circ$ en sentido antihorario.

#### Paso $m = 0$
En el estado inicial, la secuencia $x_2(n)$ se dispone en sentido horario desde $0^\circ$ sin rotación, alineando radialmente $x_1(n)$ con la secuencia temporalmente invertida.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  
  % Líneas radiales discontinuas de alineación
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  
  % Puntos exterior (orange sobre teal)
  \foreach \angle in {0, 72, 144, 216, 288} {
    \fill[orange] (\angle:2.2cm) circle (0.06cm);
  }
  % Etiquetas exterior x1(n)
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  % Puntos interior (teal sobre orange)
  \foreach \angle in {0, 288, 216, 144, 72} {
    \fill[teal] (\angle:1.2cm) circle (0.06cm);
  }
  % Etiquetas interior x2(n) — CW desde 0°, m=0 sin rotar
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(0)=1\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(4)=5\)};

  % Sentidos de giro de referencia
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 1$
Se aplica una rotación de el círculo interno de $72^\circ$ en sentido antihorario. Esto desplaza circularmente la secuencia interna un paso, alineando el valor $x_2(1)$ con el origen estático $x_1(0)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  
  % Líneas radiales discontinuas de alineación
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  
  % Puntos exterior
  \foreach \angle in {0, 72, 144, 216, 288} {
    \fill[orange] (\angle:2.2cm) circle (0.06cm);
  }
  % Etiquetas exterior x1(n)
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  % Puntos interior
  \foreach \angle in {0, 288, 216, 144, 72} {
    \fill[teal] (\angle:1.2cm) circle (0.06cm);
  }
  % Etiquetas interior x2(n) — m=1, rotado 72° CCW
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(1)=2\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(0)=1\)};

  % Sentidos de giro de referencia
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 2$
El anillo interior gira un segundo incremento angular de $72^\circ$ CCW (desplazamiento acumulado de $144^\circ$), emparejando la muestra de entrada $x_1(0)$ con la ponderación $x_2(2)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  
  % Líneas radiales discontinuas de alineación
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  
  % Puntos exterior
  \foreach \angle in {0, 72, 144, 216, 288} {
    \fill[orange] (\angle:2.2cm) circle (0.06cm);
  }
  % Etiquetas exterior x1(n)
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  % Puntos interior
  \foreach \angle in {0, 288, 216, 144, 72} {
    \fill[teal] (\angle:1.2cm) circle (0.06cm);
  }
  % Etiquetas interior x2(n) — m=2, rotado 144° CCW
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(2)=3\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(3)=4\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(1)=2\)};

  % Sentidos de giro de referencia
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 3$
Se rota el círculo interno una tercera posición angular de $72^\circ$ CCW (desplazamiento acumulado de $216^\circ$). Esto sincroniza radialmente la muestra inicial con el coeficiente $x_2(3)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  
  % Líneas radiales discontinuas de alineación
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  
  % Puntos exterior
  \foreach \angle in {0, 72, 144, 216, 288} {
    \fill[orange] (\angle:2.2cm) circle (0.06cm);
  }
  % Etiquetas exterior x1(n)
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  % Puntos interior
  \foreach \angle in {0, 288, 216, 144, 72} {
    \fill[teal] (\angle:1.2cm) circle (0.06cm);
  }
  % Etiquetas interior x2(n) — m=3, rotado 216° CCW
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(3)=4\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(4)=5\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(2)=3\)};

  % Sentidos de giro de referencia
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

#### Paso $m = 4$
Se ejecuta el último desplazamiento de $72^\circ$ CCW (desplazamiento acumulado de $288^\circ$), completando la convolución cíclica antes de que un nuevo paso devuelva el sistema a su estado inicial $m=0$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2, >=stealth, every node/.style={font=\small}]
  % Círculos concéntricos
  \draw[thick, teal] (0,0) circle (2.2cm);
  \draw[thick, orange] (0,0) circle (1.2cm);
  
  % Líneas radiales discontinuas de alineación
  \foreach \angle in {0, 72, 144, 216, 288} {
    \draw[dashed, gray!40] (\angle:1.2cm) -- (\angle:2.2cm);
  }
  
  % Puntos exterior
  \foreach \angle in {0, 72, 144, 216, 288} {
    \fill[orange] (\angle:2.2cm) circle (0.06cm);
  }
  % Etiquetas exterior x1(n)
  \node[teal, anchor=west]       at (0:2.4cm)   {\(x_1(0)=2\)};
  \node[teal, anchor=south west] at (72:2.4cm)  {\(x_1(1)=1\)};
  \node[teal, anchor=south east] at (144:2.4cm) {\(x_1(2)=2\)};
  \node[teal, anchor=north east] at (216:2.4cm) {\(x_1(3)=1\)};
  \node[teal, anchor=north west] at (288:2.4cm) {\(x_1(4)=0\)};
  % Puntos interior
  \foreach \angle in {0, 288, 216, 144, 72} {
    \fill[teal] (\angle:1.2cm) circle (0.06cm);
  }
  % Etiquetas interior x2(n) — m=4, rotado 288° CCW
  \node[orange, anchor=west]       at (0:1.35cm)   {\(x_2(4)=5\)};
  \node[orange, anchor=north west] at (288:1.35cm) {\(x_2(0)=1\)};
  \node[orange, anchor=north east] at (216:1.35cm) {\(x_2(1)=2\)};
  \node[orange, anchor=south east] at (144:1.35cm) {\(x_2(2)=3\)};
  \node[orange, anchor=south west] at (72:1.35cm)  {\(x_2(3)=4\)};

  % Sentidos de giro de referencia
  \draw[->, teal] (2.4,2.4) arc (45:65:2.9) node[midway, above right] {CCW};
  \draw[<-, orange] (0.9,-0.9) arc (-45:-65:1.3) node[midway, below left] {CW};
\end{tikzpicture}
\end{document}
```

---

### 4. Preguntas de comprensión
1. **¿Qué propiedad física de los sistemas LTI justifica geométricamente la inversión del sentido de giro (de CCW a CW) al disponer la secuencia $x_2(n)$ en el círculo interior?**
   *Respuesta:* Corresponde a la inversión temporal o reflexión de la señal en el tiempo ($x_2(-n)$), requerida por la suma de convolución para garantizar la propiedad de invarianza temporal en la respuesta al impulso del sistema.
2. **Si la secuencia exterior $x_1(n)$ tuviera longitud $N_1 = 3$ y se deseara realizar una convolución circular de $N=5$ puntos sin alterar la naturaleza del cálculo, ¿cómo debe prepararse la secuencia?**
   *Respuesta:* Se debe realizar la técnica de relleno de ceros (*zero-padding*), completando la secuencia original con $N - N_1 = 2$ ceros al final para cumplir con la longitud obligatoria del buffer circular.

---

### 5. Ejercicios resueltos

##### Ej. Convolución circular paso a paso ($N = 5$)
Dadas las secuencias discretas de período $N = 5$:

$$
x_1(n) = \{2, 1, 2, 1, 0\}
$$


$$
x_2(n) = \{1, 2, 3, 4, 5\}
$$

Determine la secuencia resultante $x_3(m) = x_1(n) \circledcirc_5 x_2(n)$ para cada instante $m = 0, 1, 2, 3, 4$ utilizando el método gráfico de círculos concéntricos.

**Resolución:**

Multiplicando par a par las muestras radialmente coincidentes indicadas en los diagramas de círculos concéntricos y sumando de manera explícita:

*   **Para $m = 0$:**
    
$$
x_3(0) = x_1(0)x_2(0) + x_1(1)x_2(4) + x_1(2)x_2(3) + x_1(3)x_2(2) + x_1(4)x_2(1)
$$

    
$$
x_3(0) = (2 \cdot 1) + (1 \cdot 5) + (2 \cdot 4) + (1 \cdot 3) + (0 \cdot 2)
$$

    
$$
x_3(0) = 2 + 5 + 8 + 3 + 0 = 18
$$


*   **Para $m = 1$:**
    
$$
x_3(1) = x_1(0)x_2(1) + x_1(1)x_2(0) + x_1(2)x_2(4) + x_1(3)x_2(3) + x_1(4)x_2(2)
$$

    
$$
x_3(1) = (2 \cdot 2) + (1 \cdot 1) + (2 \cdot 5) + (1 \cdot 4) + (0 \cdot 3)
$$

    
$$
x_3(1) = 4 + 1 + 10 + 4 + 0 = 19
$$


*   **Para $m = 2$:**
    
$$
x_3(2) = x_1(0)x_2(2) + x_1(1)x_2(1) + x_1(2)x_2(0) + x_1(3)x_2(4) + x_1(4)x_2(3)
$$

    
$$
x_3(2) = (2 \cdot 3) + (1 \cdot 2) + (2 \cdot 1) + (1 \cdot 5) + (0 \cdot 4)
$$

    
$$
x_3(2) = 6 + 2 + 2 + 5 + 0 = 15
$$


*   **Para $m = 3$:**
    
$$
x_3(3) = x_1(0)x_2(3) + x_1(1)x_2(2) + x_1(2)x_2(1) + x_1(3)x_2(0) + x_1(4)x_2(4)
$$

    
$$
x_3(3) = (2 \cdot 4) + (1 \cdot 3) + (2 \cdot 2) + (1 \cdot 1) + (0 \cdot 5)
$$

    
$$
x_3(3) = 8 + 3 + 4 + 1 + 0 = 16
$$


*   **Para $m = 4$:**
    
$$
x_3(4) = x_1(0)x_2(4) + x_1(1)x_2(3) + x_1(2)x_2(2) + x_1(3)x_2(1) + x_1(4)x_2(0)
$$

    
$$
x_3(4) = (2 \cdot 5) + (1 \cdot 4) + (2 \cdot 3) + (1 \cdot 2) + (0 \cdot 1)
$$

    
$$
x_3(4) = 10 + 4 + 6 + 2 + 0 = 22
$$


**Resultado final:**
La secuencia resultante de la convolución circular es:

$$
\mathbf{x_3(m) = \{18, 19, 15, 16, 22\}}
$$


---

##### Ej. Convolución circular de mayor dificultad (N = 5, con impulsos alternantes)
Determine de manera exacta la convolución circular $y(m) = x_1(n) \circledcirc_5 x_2(n)$ de las siguientes señales de período $N=5$ extraídas de Palani Ej. 2.27(b):

$$
x_1(n) = \delta(n) + \delta(n-1) - \delta(n-2) + \delta(n-3) \implies x_1(n) = \{1, 1, -1, 1, 0\}
$$


$$
x_2(n) = \delta(n) - \delta(n-2) + \delta(n-4) \implies x_2(n) = \{1, 0, -1, 0, 1\}
$$


**Resolución:**

Podemos plantear la convolución circular rigurosamente estructurando una representación matricial, donde la secuencia estática $x_2(n)$ se dispone en forma de una **matriz circulante** y $x_1(n)$ como un vector columna:


$$
\begin{bmatrix} y(0) \\ y(1) \\ y(2) \\ y(3) \\ y(4) \end{bmatrix} = \begin{bmatrix} x_2(0) & x_2(4) & x_2(3) & x_2(2) & x_2(1) \\ x_2(1) & x_2(0) & x_2(4) & x_2(3) & x_2(2) \\ x_2(2) & x_2(1) & x_2(0) & x_2(4) & x_2(3) \\ x_2(3) & x_2(2) & x_2(1) & x_2(0) & x_2(4) \\ x_2(4) & x_2(3) & x_2(2) & x_2(1) & x_2(0) \end{bmatrix} \begin{bmatrix} x_1(0) \\ x_1(1) \\ x_1(2) \\ x_1(3) \\ x_1(4) \end{bmatrix}
$$


Reemplazando los valores correspondientes de las secuencias:

$$
\begin{bmatrix} y(0) \\ y(1) \\ y(2) \\ y(3) \\ y(4) \end{bmatrix} = \begin{bmatrix} 1 & 1 & 0 & -1 & 0 \\ 0 & 1 & 1 & 0 & -1 \\ -1 & 0 & 1 & 1 & 0 \\ 0 & -1 & 0 & 1 & 1 \\ 1 & 0 & -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -1 \\ 1 \\ 0 \end{bmatrix}
$$


Realizamos detalladamente el producto algebraico de filas por columnas:
*   
$$
y(0) = (1 \cdot 1) + (1 \cdot 1) + (0 \cdot (-1)) + (-1 \cdot 1) + (0 \cdot 0) = 1 + 1 + 0 - 1 + 0 = 1
$$

*   
$$
y(1) = (0 \cdot 1) + (1 \cdot 1) + (1 \cdot (-1)) + (0 \cdot 1) + (-1 \cdot 0) = 0 + 1 - 1 + 0 - 0 = 0
$$

*   
$$
y(2) = (-1 \cdot 1) + (0 \cdot 1) + (1 \cdot (-1)) + (1 \cdot 1) + (0 \cdot 0) = -1 + 0 - 1 + 1 + 0 = -1
$$

*   
$$
y(3) = (0 \cdot 1) + (-1 \cdot 1) + (0 \cdot (-1)) + (1 \cdot 1) + (1 \cdot 0) = 0 - 1 + 0 + 1 + 0 = 0
$$

*   
$$
y(4) = (1 \cdot 1) + (0 \cdot 1) + (-1 \cdot (-1)) + (0 \cdot 1) + (1 \cdot 0) = 1 + 0 + 1 + 0 + 0 = 2
$$


**Resultado final:**
La secuencia resultante de la convolución circular es:

$$
\mathbf{y(m) = \{1, 0, -1, 0, 2\}}
$$


*(Nota teórica: Se observa que el resultado analítico corregido corrige una errata tipográfica existente en el texto original de Palani en la página 149, donde se imprimió erróneamente un 3 en lugar de un 1 en la primera muestra del vector).*




