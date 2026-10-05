## 10. Relación entre Polos de Filtros Analógicos y Digitales

title: Complemento (Nivel C)

### 1. Explicación intuitiva
El diseño de filtros digitales IIR (Respuesta Infinita al Impulso) se basa generalmente en la transformación de filtros analógicos ya conocidos (como Butterworth o Chebyshev) [1, 2]. Para que esta conversión sea efectiva, los polos del sistema en el plano $s$ (dominio continuo) deben trasladarse al plano $z$ (dominio discreto) de manera que se preserve la estabilidad y la respuesta en frecuencia [3, 4]. 

La regla fundamental de estabilidad dicta que un polo en el semiplano izquierdo del plano $s$ ($\text{Re}\{s\} < 0$) debe mapearse forzosamente al interior del círculo unitario en el plano $z$ ($|z| < 1$) [5, 6]. Si un polo analógico está en el eje imaginario ($j\Omega$), su equivalente digital debe ubicarse exactamente sobre la circunferencia unitaria [7, 8].

### 2. Definición formal
La relación específica entre los polos depende de la técnica de transformación empleada:

*   **Invarianza al impulso:** Utiliza un mapeo exponencial directo donde cada polo analógico $p_k$ se transforma en un polo digital $z_k$ mediante la relación:
    
$$
z_k = e^{p_k T}
$$

    donde $T$ es el período de muestreo [9-11]. Este mapeo es de "muchos a uno", lo que puede generar aliasing si el filtro no está limitado en banda [12, 13].

*   **Transformación Bilineal:** Utiliza una aproximación algebraica basada en la regla trapezoidal de integración. La relación que define la ubicación de los polos es:
    
$$
s = \frac{2}{T} \frac{z-1}{z+1} \implies z = \frac{1 + (sT/2)}{1 - (sT/2)}
$$

    A diferencia de la invarianza al impulso, este es un mapeo "uno a uno" que comprime todo el eje $j\Omega$ analógico dentro del círculo unitario, eliminando el aliasing pero introduciendo una distorsión no lineal en la frecuencia conocida como *warping* [14-16].

### 3. Diagrama de mapeo (Plano s a Plano z)

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Plano s
    \draw[->] (-2.5,0) -- (0.5,0) node[right] {$\text{Re}(s)$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$j\Omega$};
    \fill[teal!20] (-2.3,-1.4) rectangle (0,1.4);
    \node at (-1.2, 1) {\small LHP};
    \node[teal] at (-0.5, 0.5) {$\times$};
    \node at (-1.2,-1.8) {Plano $s$ (Continuo)};

    % Flecha de transformación
    \draw[->, thick] (0.8,0) -- (1.8,0) node[midway, above] {\small Mapeo};

    % Plano z
    \begin{scope}[xshift=4cm]
        \draw[->] (-1.5,0) -- (1.5,0) node[right] {$\text{Re}(z)$};
        \draw[->] (0,-1.5) -- (0,1.5) node[above] {$\text{Im}(z)$};
        \draw[dashed, gray] (0,0) circle [radius=1cm];
        \fill[teal!20] (0,0) circle [radius=1cm];
        \node at (0, 0.4) {\small $|z|<1$};
        \node[teal] at (0.3, 0.3) {$\times$};
        \node at (0,-1.8) {Plano $z$ (Digital)};
    \end{scope}
\end{tikzpicture}
\end{document}
```
%%IMA-SRC | fuente: propio basado en Palani Fig 3.3 y 3.4 | justificación: Ilustra visualmente la condición de estabilidad donde el semiplano izquierdo se mapea al interior del círculo unitario.%%

### 4. Preguntas de comprensión
1. ¿Por qué la transformación bilineal es preferible para filtros que no están limitados en banda en comparación con la invarianza al impulso? [14, 17]
2. Si un filtro analógico es estable, ¿qué garantiza que el filtro digital resultante también lo sea tras una transformación bilineal? [8, 18]
3. En el mapeo $z = e^{sT}$, ¿qué sucede con los polos analógicos que tienen la misma parte real pero partes imaginarias que difieren en múltiplos de $2\pi/T$? [12, 19]

### 5. Ejercicios resueltos

##### Ej. 1: Mapeo por Invarianza al Impulso
**Enunciado:** Un filtro analógico tiene un polo en $s = -2$ y se utiliza un período de muestreo $T = 0.1 \text{ s}$. Determine la ubicación del polo digital usando invarianza al impulso y verifique su estabilidad [20].

**Resolución:**
Utilizando la fórmula de mapeo directo para polos distintos [21]:

$$
z_k = e^{p_k T}
$$

Sustituyendo los valores:

$$
z_1 = e^{(-2)(0.1)} = e^{-0.2}
$$


$$
z_1 \approx 0.8187
$$

Como $|z_1| = 0.8187 < 1$, el polo se encuentra dentro del círculo unitario y el sistema digital es estable [7].

##### Ej. 2: Mapeo por Transformación Bilineal
**Enunciado:** Para el mismo polo analógico $s = -2$ y $T = 0.1 \text{ s}$, determine la ubicación del polo digital empleando la transformación bilineal [22].

**Resolución:**
Partimos de la relación de despeje para $z$ en la bilineal [22]:

$$
z = \frac{1 + sT/2}{1 - sT/2}
$$

Sustituyendo $s = -2$ y $T = 0.1$:

$$
z = \frac{1 + (-2)(0.1)/2}{1 - (-2)(0.1)/2} = \frac{1 - 0.1}{1 + 0.1}
$$


$$
z = \frac{0.9}{1.1} \approx 0.8182
$$

Aunque el valor es cercano al del ejercicio anterior, el método bilineal asegura que no habrá aliasing de los componentes frecuenciales asociados [15]. El sistema es estable pues $|0.8182| < 1$ [8].
