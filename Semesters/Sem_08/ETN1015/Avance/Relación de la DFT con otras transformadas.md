## 2.3 Relación de la DFT con otras transformadas

`````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
La Transformada Discreta de Fourier $DFT$ no es un concepto aislado, sino una versión muestreada de representaciones de frecuencia continuas [1, 2]. Mientras que la DTFT y la Transformada Z operan sobre una variable continua $$\omega$ o $z$$, la DFT selecciona puntos específicos de estas funciones para que puedan ser procesados digitalmente [3-5]. Básicamente, la DFT actúa como un puente que permite representar señales finitas en el dominio de la frecuencia mediante un conjunto limitado de valores [1, 6, 7].

2. **Definición formal**
La relación de la DFT con las principales transformadas se define así:

- **Con la DTFT:** La DFT $X[k]$ consiste en $N$ muestras de la DTFT $X(e^{j\omega})$ tomadas en frecuencias equiespaciadas $\omega_k = \dfrac{2\pi k}{N}$ para $k = 0, 1, \dots, N-1$ [8-11].
- **Con la Transformada Z:** La DFT de $N$ puntos corresponde a evaluar $X(z)$ en $N$ puntos distribuidos uniformemente sobre el círculo unitario, donde $z_k = e^{j\frac{2\pi k}{N}}$ [10, 12-14].
- **Con la Serie de Fourier Discreta $DFS$:** Si se considera la extensión periódica de una secuencia finita, sus coeficientes $C_k$ se relacionan con la DFT mediante $X[k] = N C_k$ [8, 15, 16].

3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.8]
    % Ejes
    \draw[->] (-1.3,0) -- (1.5,0) node[right] {$\text{Re}(z)$};
    \draw[->] (0,-1.3) -- (0,1.5) node[above] {$\text{Im}(z)$};
    % Círculo unitario
    \draw[thick, teal] (0,0) circle (1);
    \node[teal, anchor=north east] at (-0.7,0.7) {Círculo Unitario};
    % Muestreo para N=8
    \foreach \k in {0,1,...,7} {
        \filldraw[orange] ({cos(\k*45)}, {sin(\k*45)}) circle (2pt);
        \draw[->, gray, thin] (0,0) -- ({0.95*cos(\k*45)}, {0.95*sin(\k*45)});
        \node[anchor=\k*45] at ({1.15*cos(\k*45)}, {1.15*sin(\k*45)}) {\small $X[k]$};
    }
    \node[anchor=north, align=center] at (0,-1.4) {La DFT como muestreo de $X(z)$ \\ sobre el círculo unitario ($N=8$)};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: Oppenheim & Willsky, Signals and Systems | página: 743 | id: Fig. 10.1 (adaptada) | posición: centro de la página
justificación: Ilustra cómo la DFT selecciona muestras específicas del plano Z sobre la circunferencia de radio unitario [17-19].%%

4. **Preguntas de comprensión**
- ¿Por qué se dice que la DFT es una versión "muestreada" de la DTFT? [1, 2]
- ¿Qué ocurre con la relación entre DFT y Transformada Z si la secuencia no es de duración finita? [20, 21]
- ¿Cómo afecta el aumento de puntos $N$ (Zero Padding) a las muestras tomadas de la DTFT? [22, 23]

5. **Ejercicios resueltos**

##### Ej. 2.20 — Obtención de secuencia desde muestras en Z
Dada la secuencia de longitud finita $x[n] = \{1, 2, 1, 1\}$, se sabe que su transformada Z es $X(z) = 1 + 2z^{-1} + z^{-2} + z^{-3}$ [24]. Si se muestrea $X(z)$ en $z = e^{j\frac{2\pi k}{4}}$ para $k = 0, 1, 2, 3$, determine la secuencia $x_1[n]$ resultante de la IDFT de esas muestras [24].

**Resolución:**
Al evaluar $X(z)$ en los puntos indicados:

$$
X_1[k] = X(z)\Big|_{z=e^{j\frac{2\pi k}{4}}} = 1 + 2e^{-j\frac{2\pi k}{4}} + e^{-j\frac{2\pi k \cdot 2}{4}} + e^{-j\frac{2\pi k \cdot 3}{4}}
$$
 [25]
Esta expresión coincide exactamente con la definición de la DFT de 4 puntos de la secuencia original [25]:

$$
X_1[k] = \sum_{n=0}^{3} x[n] e^{-j\frac{2\pi kn}{4}}
$$

Comparando término a término con $1 + 2e^{-j\frac{2\pi k \cdot 1}{4}} + 1e^{-j\frac{2\pi k \cdot 2}{4}} + 1e^{-j\frac{2\pi k \cdot 3}{4}}$, identificamos los valores de $x_1[n]$ [25]:

$$
\bbox[5px,border:2px solid \#005F73]{x_1[n] = \{1, 2, 1, 1\}}
$$
 [25]
`````
