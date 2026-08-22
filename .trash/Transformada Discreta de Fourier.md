## 2. Transformada Discreta de Fourier $DFT$

`````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
La DFT es una herramienta fundamental en el procesamiento digital que permite analizar el contenido de frecuencia de una secuencia de tiempo de duración finita [1, 2]. A diferencia de la Transformada de Fourier en Tiempo Discreto $DTFT$, que produce un espectro continuo, la DFT muestrea ese espectro en puntos equiespaciados, lo que la hace ideal para ser procesada por computadoras y hardware digital [2, 3]. Básicamente, convierte una secuencia discreta de tiempo en una secuencia discreta de frecuencia de la misma longitud [4, 5].

2. **Definición formal**
Dada una secuencia $x[n]$ de longitud $N$, la DFT de $N$ puntos se define como [4]:

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\dfrac{2\pi}{N}kn} = \sum_{n=0}^{N-1} x[n] W_N^{kn}, \quad k = 0, 1, \dots, N-1
$$

Donde $W_N = e^{-j\dfrac{2\pi}{N}}$ es el denominado **factor de giro** (*twiddle factor*) [4, 6].
La secuencia original se recupera mediante la IDFT [4]:

$$
x[n] = \dfrac{1}{N} \sum_{k=0}^{N-1} X[k] W_N^{-kn}, \quad n = 0, 1, \dots, N-1
$$


3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.5]
    % Ejes
    \draw[->] (-1.2,0) -- (1.2,0) node[right] {$\text{Re}$};
    \draw[->] (0,-1.2) -- (0,1.2) node[above] {$\text{Im}$};
    % Circunferencia unitaria
    \draw[dashed, teal] (0,0) circle (1);
    % Puntos para N=4
    \filldraw[orange] (1,0) circle (2pt) node[anchor=north west] {$W_4^0=1$};
    \filldraw[orange] (0,-1) circle (2pt) node[anchor=north west] {$W_4^1=-j$};
    \filldraw[orange] (-1,0) circle (2pt) node[anchor=south east] {$W_4^2=-1$};
    \filldraw[orange] (0,1) circle (2pt) node[anchor=south east] {$W_4^3=j$};
    % Título
    \node at (0,-1.5) {Representación de $W_4^{nk}$ en el plano complejo};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: S. Palani, Principles of Digital Signal Processing | página: 85 | id: Fig. 2.1 | posición: centro de la página
justificación: Representa cómo los factores de giro se distribuyen uniformemente sobre la circunferencia unitaria para N=4.%%

4. **Propiedades clave** [7]:
- **Periodicidad:** Tanto $x[n]$ como $X[k]$ son periódicas con periodo $N$ [8].
- **Linealidad:** La DFT de una combinación lineal de secuencias es la combinación lineal de sus DFT [9].
- **Desplazamiento circular:** Un desplazamiento en el tiempo $x((n-m))_N$ equivale a multiplicar por una fase $W_N^{km}X[k]$ [7, 10].
- **Convolución circular:** La multiplicación de dos DFT corresponde a la convolución circular de sus secuencias en el tiempo [7, 11].
- **Simetría conjugada:** Si $x[n]$ es real, $X[k] = X^*[N-k]$ [12].

5. **Preguntas de comprensión**
- ¿Cuál es la principal diferencia entre la DTFT y la DFT?
- ¿Por qué es necesario el "Zero Padding" antes de calcular una DFT?
- ¿Qué relación existe entre los coeficientes de una Serie de Fourier Discreta $DFS$ y la DFT?

6. **Ejercicios resueltos**

##### Ej. 2.1 — DFT de una secuencia básica
Calcular la DFT de la secuencia $x[n] = \{1, j, -1, -j\}$ para $N=4$ [13].

**Resolución:**
Para $N=4$, la matriz de factores de giro $W_4$ es [13, 14]:

$$
W_4 = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix}
$$

Aplicando la forma matricial $X_4 = [W_4]x_4$ [6, 13]:

$$
\begin{bmatrix} X \\ X[15] \\ X[16] \\ X[17] \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix} \begin{bmatrix} 1 \\ j \\ -1 \\ -j \end{bmatrix}
$$

Calculando cada componente:

$$
\begin{array}{rcl} X & = & 1(1) + 1(j) + 1(-1) + 1(-j) = 1 + j - 1 - j = \bbox[5px,border:1px solid \#005F73]{0} \\ X[15] & = & 1(1) + (-j)(j) + (-1)(-1) + (j)(-j) = 1 + 1 + 1 + 1 = \bbox[5px,border:1px solid \#005F73]{4} \\ X[16] & = & 1(1) + (-1)(j) + 1(-1) + (-1)(-j) = 1 - j - 1 + j = \bbox[5px,border:1px solid \#005F73]{0} \\ X[17] & = & 1(1) + (j)(j) + (-1)(-1) + (-j)(-j) = 1 - 1 + 1 - 1 = \bbox[5px,border:1px solid \#005F73]{0} \end{array}
$$

Resultado final: $\bbox[5px,border:2px solid #005F73]{X[k] = \{0, 4, 0, 0\}}$.
`````
