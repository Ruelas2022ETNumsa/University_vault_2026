## 2. Transformada Discreta de Fourier $DFT$

`````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
La Transformada Discreta de Fourier $DFT$ es la herramienta que permite a las computadoras analizar el contenido de frecuencia de las señales [1]. Mientras que otras transformadas (como la DTFT) producen funciones continuas que no pueden almacenarse en una memoria digital, la DFT convierte una secuencia finita de muestras en el tiempo en otra secuencia finita de muestras en la frecuencia [2, 3]. Esencialmente, la DFT "muestrea" el espectro continuo de la DTFT en puntos equiespaciados para que los procesadores digitales puedan manipularlo [4, 5].

2. **Definición formal**
Dada una secuencia $x[n]$ de longitud $N$, su DFT de $N$ puntos se define como [6, 7]:

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\dfrac{2\pi}{N}kn} = \sum_{n=0}^{N-1} x[n] W_N^{kn}, \quad k = 0, 1, \dots, N-1
$$

Donde $W_N = e^{-j\dfrac{2\pi}{N}}$ es el **factor de giro** (*twiddle factor*) [6, 7].
Para recuperar la señal original, se utiliza la **Transformada Inversa $IDFT$** [6, 7]:

$$
x[n] = \dfrac{1}{N} \sum_{k=0}^{N-1} X[k] W_N^{-kn}, \quad n = 0, 1, \dots, N-1
$$


3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.5]
    % Ejes
    \draw[->] (-1.2,0) -- (1.5,0) node[right] {$\text{Re}\{W_N^{nk}\}$};
    \draw[->] (0,-1.2) -- (0,1.5) node[above] {$\text{Im}\{W_N^{nk}\}$};
    % Circunferencia unitaria
    \draw[dashed, teal] (0,0) circle (1);
    % Puntos para N=4 (sentido horario para exponentes positivos de WN)
    \filldraw[orange] (1,0) circle (2pt) node[anchor=north west] {$W_4^0=1$};
    \filldraw[orange] (0,-1) circle (2pt) node[anchor=north west] {$W_4^1=-j$};
    \filldraw[orange] (-1,0) circle (2pt) node[anchor=south east] {$W_4^2=-1$};
    \filldraw[orange] (0,1) circle (2pt) node[anchor=south east] {$W_4^3=j$};
    % Título
    \node at (0.3,-1.6) {Factores de giro $W_N^{nk}$ para $N=4$};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: S. Palani, Principles of Digital Signal Processing | página: 85 | id: Fig. 2.1 | posición: centro de la página
justificación: La figura muestra cómo el factor de giro distribuye los puntos uniformemente sobre la circunferencia unitaria en el plano complejo.%%

4. **Propiedades destacadas** [8, 9]:
- **Linealidad:** La DFT de una suma es la suma de las DFT [10, 11].
- **Periodicidad:** Tanto la señal $x[n]$ como su transformada $X[k]$ son periódicas con periodo $N$ [11, 12].
- **Simetría conjugada:** Para señales reales, $X[k] = X^*[N-k]$ [11, 13].
- **Convolución circular:** La multiplicación de dos DFT en frecuencia equivale a la convolución circular de las señales en el tiempo [14, 15].

5. **Preguntas de comprensión**
- ¿Cuál es la principal ventaja de la DFT sobre la DTFT para su implementación en hardware? [3]
- ¿Cómo se relaciona la DFT con el muestreo de la transformada de Fourier continua? [5]
- ¿Qué sucede con la resolución en frecuencia si se aumenta el número de puntos $N$ mediante *Zero Padding*? [16, 17]

6. **Ejercicios resueltos**

##### Ej. 2.1 — Cálculo de DFT de 4 puntos
Calcular la DFT de la secuencia $x[n] = \{1, j, -1, -j\}$ para $N=4$ [18].

**Resolución:**
Utilizando la matriz de factores de giro para $N=4$ [19]:

$$
W_4 = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix}
$$

Aplicamos la forma matricial $X_4 = [W_4]x_4$ [18, 20]:

$$
\begin{bmatrix} X \\ X[21] \\ X[22] \\ X[23] \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix} \begin{bmatrix} 1 \\ j \\ -1 \\ -j \end{bmatrix}
$$

Calculamos cada componente línea por línea [24]:

$$
\begin{array}{rcl} X & = & (1)(1) + (1)(j) + (1)(-1) + (1)(-j) = 1 + j - 1 - j = \bbox[5px,border:1px solid \#005F73]{0} \\ X[21] & = & (1)(1) + (-j)(j) + (-1)(-1) + (j)(-j) = 1 + 1 + 1 + 1 = \bbox[5px,border:1px solid \#005F73]{4} \\ X[22] & = & (1)(1) + (-1)(j) + (1)(-1) + (-1)(-j) = 1 - j - 1 + j = \bbox[5px,border:1px solid \#005F73]{0} \\ X[23] & = & (1)(1) + (j)(j) + (-1)(-1) + (-j)(-j) = 1 - 1 + 1 - 1 = \bbox[5px,border:1px solid \#005F73]{0} \end{array}
$$

Resultado final: $\bbox[5px,border:2px solid #005F73]{X[k] = \{0, 4, 0, 0\}}$.
`````
