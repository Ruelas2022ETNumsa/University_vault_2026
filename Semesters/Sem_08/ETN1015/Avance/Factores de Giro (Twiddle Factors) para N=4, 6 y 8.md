## 2.2 Factores de Giro (Twiddle Factors) para N=4, 6 y 8

````ad-note
title: Complemento (Nivel C)

1. **Explicación intuitiva**
Los factores de giro, denotados como $W_N$, representan puntos distribuidos uniformemente sobre la circunferencia unitaria en el plano complejo [1]. El término $W_N^k$ puede verse como un vector de magnitud unidad que gira en sentido horario a medida que aumenta el índice $k$ [1]. Al calcular una DFT de $N$ puntos, dividimos el círculo completo ($2\pi$ radianes) en $N$ partes iguales [2]. Estos valores son constantes precalculadas que simplifican las operaciones de la DFT y FFT.

2. **Definición formal**
El factor de giro se define matemáticamente como [3]:

$$
W_N = e^{-j\dfrac{2\pi}{N}} = \cos\left(\dfrac{2\pi}{N}\right) - j\sin\left(\dfrac{2\pi}{N}\right)
$$

Para cualquier potencia $k$, el valor es [4]:

$$
W_N^k = e^{-j\dfrac{2\pi}{N}k}
$$


3. **Figura o diagrama**

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.8]
    \draw[->] (-1.3,0) -- (1.3,0) node[right] {$\text{Re}$};
    \draw[->] (0,-1.3) -- (0,1.3) node[above] {$\text{Im}$};
    \draw[dashed, teal] (0,0) circle (1);
    
    % Puntos N=8
    \foreach \a in {0,1,...,7} {
        \filldraw[orange] ({cos(-\a*45)}, {sin(-\a*45)}) circle (1.5pt);
        \node[anchor={-45-\a*45}] at ({1.15*cos(-\a*45)}, {1.15*sin(-\a*45)}) {\tiny $W_8^{\a}$};
    }
    
    \node[anchor=north] at (0,-1.4) {Distribución de factores de giro para $N=8$ ($45^\circ$ entre puntos)};
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: S. Palani, Principles of Digital Signal Processing | página: 88 | id: Fig. 2.3 | posición: centro de la página
justificación: La figura ilustra cómo los factores de giro dividen la circunferencia unitaria en partes iguales (en este caso 8).%%

4. **Valores específicos por Duración $N$**

*   **N = 4 (Intervalos de 90° o $\pi/2$)** [2, 5]:
    *   $W_4^0 = 1$
    *   $W_4^1 = -j$
    *   $W_4^2 = -1$
    *   $W_4^3 = j$
*   **N = 6 (Intervalos de 60° o $\pi/3$)** [6, 7]:
    *   $W_6^0 = 1$
    *   $W_6^1 = 0.5 - j0.866$
    *   $W_6^2 = -0.5 - j0.866$
    *   $W_6^3 = -1$
    *   $W_6^4 = -0.5 + j0.866$
    *   $W_6^5 = 0.5 + j0.866$
*   **N = 8 (Intervalos de 45° o $\pi/4$)** [8, 9]:
    *   $W_8^0 = 1$
    *   $W_8^1 = \dfrac{1}{\sqrt{2}} - j\dfrac{1}{\sqrt{2}} \approx 0.707 - j0.707$
    *   $W_8^2 = -j$
    *   $W_8^3 = -\dfrac{1}{\sqrt{2}} - j\dfrac{1}{\sqrt{2}}$
    *   $W_8^4 = -1$
    *   $W_8^5 = -\dfrac{1}{\sqrt{2}} + j\dfrac{1}{\sqrt{2}}$
    *   $W_8^6 = j$
    *   $W_8^7 = \dfrac{1}{\sqrt{2}} + j\dfrac{1}{\sqrt{2}}$

5. **Preguntas de comprensión**
*   ¿Qué propiedad del factor de giro permite que $W_8^2$ sea igual a $W_4^1$? [10]
*   ¿Por qué el valor de $W_N^N$ es siempre igual a 1? [1]
*   ¿En qué dirección se desplazan los puntos sobre el círculo unitario al aumentar el exponente $k$? [1]

6. **Ejercicios resueltos**

##### Ej. 2.2 — Simplificación de factores
Determine el valor decimal complejo de $W_8^3$ y $W_6^2$.

**Resolución:**
Para $W_8^3$ [8]:

$$
W_8^3 = e^{-j\dfrac{2\pi}{8} \cdot 3} = e^{-j\dfrac{3\pi}{4}} = \cos\left(\dfrac{3\pi}{4}\right) - j\sin\left(\dfrac{3\pi}{4}\right)
$$


$$
W_8^3 = \bbox[5px,border:1px solid \#005F73]{-0.707 - j0.707}
$$


Para $W_6^2$ [7]:

$$
W_6^2 = e^{-j\dfrac{2\pi}{6} \cdot 2} = e^{-j\dfrac{2\pi}{3}} = \cos\left(\dfrac{2\pi}{3}\right) - j\sin\left(\dfrac{2\pi}{3}\right)
$$


$$
W_6^2 = \bbox[5px,border:1px solid \#005F73]{-0.5 - j0.866}
$$

````
