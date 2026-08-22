## 2.3 Relleno de Ceros (Zero Padding)

`````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
El relleno de ceros consiste en añadir muestras de valor cero al final de una secuencia de tiempo de duración finita [1, 2]. Aunque esto no añade información nueva a la señal original, permite que la computadora calcule la DFT con un mayor número de puntos. Esto tiene dos propósitos principales: alcanzar una longitud que sea potencia de 2 para usar algoritmos rápidos $FFT$ y obtener una representación visual más suave del espectro, ya que al aumentar $N$ estamos "muestreando" la DTFT con mayor densidad [1, 3].

2. **Definición formal**
Dada una secuencia $x[n]$ de longitud $L$, la secuencia extendida $x_p[n]$ de longitud $N$ (donde $N > L$) se define como:

$$
x_p[n] = \begin{cases} x[n], & 0 \le n \le L-1 \\ 0, & L \le n \le N-1 \end{cases}
$$

La DFT de $N$ puntos resultante se obtiene evaluando la transformada $Z$ de la secuencia original en $N$ puntos equiespaciados sobre el círculo unitario [4, 5].

3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    % Ejes
    \draw[->] (-0.5,0) -- (6.5,0) node[right] {$n$};
    \draw[->] (0,-0.5) -- (0,2.5) node[above] {$x_p[n]$};
    
    % Muestras originales (L=3)
    \foreach \n/\y in {0/1, 1/2, 2/1.5} {
        \draw[thick, teal] (\n,0) -- (\n,\y);
        \filldraw[teal] (\n,\y) circle (2pt);
    }
    
    % Muestras de Zero Padding (N=6)
    \foreach \n in {3,4,5} {
        \draw[thick, orange] (\n,0) -- (\n,0);
        \filldraw[orange] (\n,0) circle (2pt);
        \node[above, orange, scale=0.7] at (\n,0.1) {0};
    }
    
    \node[anchor=west, teal] at (0,2.2) {\small Muestras originales ($L=3$)};
    \node[anchor=west, orange] at (3,1.2) {\small Zero padding ($N-L=3$)};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: S. Palani, Principles of Digital Signal Processing | página: 92 | id: Fig. 2.3 (inferido) | posición: descripción de concepto
justificación: Ilustra visualmente cómo se agregan muestras nulas al final de una secuencia de datos finita.%%

4. **Preguntas de comprensión**
- ¿El relleno de ceros mejora la resolución para distinguir dos frecuencias muy cercanas entre sí? [3]
- ¿Qué relación debe cumplir $N$ respecto a las longitudes de dos señales para que su convolución circular equivalga a la convolución lineal? [6, 7]
- ¿Por qué se prefiere que la longitud total $N$ sea una potencia de 2? [2]

5. **Ejercicios resueltos**

##### Ej. 2.3 — DFT de 4 puntos con Zero Padding
Calcular la DFT de la secuencia $x[n] = \{1, 1, 1\}$ utilizando un relleno de ceros para $N=4$ [8].

**Resolución:**
Primero, extendemos la secuencia añadiendo un cero al final para alcanzar $N=4$:

$$
x_p[n] = \{1, 1, 1, 0\}
$$

Utilizamos la matriz de factores de giro $W_4$:

$$
X_4 = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \\ 0 \end{bmatrix}
$$

Calculamos cada componente:

$$
\begin{array}{rcl} X & = & 1(1) + 1(1) + 1(1) + 1(0) = \bbox[5px,border:1px solid \#005F73]{3} \\ X[9] & = & 1(1) + (-j)(1) + (-1)(1) + (j)(0) = 1 - j - 1 = \bbox[5px,border:1px solid \#005F73]{-j} \\ X[10] & = & 1(1) + (-1)(1) + 1(1) + (-1)(0) = 1 - 1 + 1 = \bbox[5px,border:1px solid \#005F73]{1} \\ X[11] & = & 1(1) + (j)(1) + (-1)(1) + (-j)(0) = 1 + j - 1 = \bbox[5px,border:1px solid \#005F73]{j} \end{array}
$$

Resultado final: $\bbox[5px,border:2px solid #005F73]{X[k] = \{3, -j, 1, j\}}$.
`````
