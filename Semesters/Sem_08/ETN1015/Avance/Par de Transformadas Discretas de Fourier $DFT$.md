## 2. Par de Transformadas Discretas de Fourier $DFT$

`````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
El "par" de la Transformada Discreta de Fourier se refiere a las dos fórmulas matemáticas que nos permiten movernos entre el dominio del tiempo y el dominio de la frecuencia de forma reversible [1, 2]. La **DFT** (análisis) descompone una secuencia de muestras de tiempo en sus componentes de frecuencia, mientras que la **IDFT** (síntesis) reconstruye la señal original a partir de esos componentes [3, 4]. Es la representación ideal para computadoras porque ambas secuencias son finitas y discretas [2, 5].

2. **Definición formal**
Dada una secuencia de longitud $N$, el par de transformadas se define como [3, 4]:

**Ecuación de Análisis $DFT$:**

$$
X[k] = \sum_{n=0}^{N-1} x[n] W_N^{kn}, \quad k = 0, 1, \dots, N-1
$$


**Ecuación de Síntesis $IDFT$:**

$$
x[n] = \dfrac{1}{N} \sum_{k=0}^{N-1} X[k] W_N^{-kn}, \quad n = 0, 1, \dots, N-1
$$


Donde $W_N = e^{-j\dfrac{2\pi}{N}}$ es el **factor de giro** (*twiddle factor*) [3, 6].

3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.5]
    % Ejes
    \draw[->] (-1.2,0) -- (1.5,0) node[right] {$\text{Re}$};
    \draw[->] (0,-1.2) -- (0,1.5) node[above] {$\text{Im}$};
    % Circunferencia unitaria
    \draw[dashed, teal] (0,0) circle (1);
    % Factores para N=8
    \foreach \a in {0,1,...,7} {
        \filldraw[orange] ({cos(-\a*360/8)}, {sin(-\a*360/8)}) circle (1.5pt);
        \node[anchor={-45-\a*45}] at ({1.1*cos(-\a*360/8)}, {1.1*sin(-\a*360/8)}) {\tiny $W_8^{\a}$};
    }
    \node at (0.3,-1.6) {Distribución de los factores de giro ($N=8$)};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: S. Palani, Principles of Digital Signal Processing | página: 88 | id: Fig. 2.3 | posición: centro de la página
justificación: Muestra gráficamente los valores que toma el núcleo de la transformada $WN$ sobre el círculo unitario para una DFT de 8 puntos.%%

4. **Propiedades del par**:
- **Correspondencia uno a uno:** Existe una relación única entre una secuencia $x[n]$ y su transformada $X[k]$ [2, 4].
- **Periodicidad implícita:** Aunque trabajamos con secuencias finitas, las fórmulas de la DFT tratan a las señales como si fueran periódicas con periodo $N$ [7, 8].
- **Forma Matricial:** El par puede expresarse como un producto de matriz-vector: $\mathbf{X}_N = [W_N] \mathbf{x}_N$ y $\mathbf{x}_N = \dfrac{1}{N} [W_N^*] \mathbf{X}_N$ [6, 9].

5. **Preguntas de comprensión**
- ¿Por qué es necesaria la escala $1/N$ en la ecuación de síntesis $IDFT$? [3, 4]
- ¿Qué valor físico representan los índices $k$ en el dominio de la frecuencia? [10, 11]
- ¿Cómo se relaciona el factor de giro $W_N$ con las raíces de la unidad? [4, 6]

6. **Ejercicios resueltos**

##### Ej. 2.2 — IDFT de una secuencia de impulsos
Encontrar la IDFT de la secuencia de frecuencia $X[k] = \{1, 0, 1, 0\}$ para $N=4$.

**Resolución:**
Utilizamos la ecuación de síntesis para $N=4$:

$$
x[n] = \dfrac{1}{4} \sum_{k=0}^{3} X[k] W_4^{-kn}
$$

Sustituyendo los valores no nulos de $X[k]$ ($k=0$ y $k=2$):

$$
x[n] = \dfrac{1}{4} \left( XW_4^0 + X[12]W_4^{-2n} \right) = \dfrac{1}{4} \left( 1(1) + 1(e^{j\frac{2\pi}{4}2n}) \right)
$$

Simplificando el exponente:

$$
x[n] = \dfrac{1}{4} \left( 1 + e^{j\pi n} \right) = \dfrac{1}{4} \left( 1 + (-1)^n \right)
$$

Evaluando para cada $n$:

$$
\begin{array}{rcl} x & = & \dfrac{1}{4}(1 + 1) = \bbox[5px,border:1px solid \#005F73]{0.5} \\ x[13] & = & \dfrac{1}{4}(1 - 1) = \bbox[5px,border:1px solid \#005F73]{0} \\ x[12] & = & \dfrac{1}{4}(1 + 1) = \bbox[5px,border:1px solid \#005F73]{0.5} \\ x[14] & = & \dfrac{1}{4}(1 - 1) = \bbox[5px,border:1px solid \#005F73]{0} \end{array}
$$

Resultado final: $\bbox[5px,border:2px solid #005F73]{x[n] = \{0.5, 0, 0.5, 0\}}$. [15, 16]
`````

