## 4.4.1 Características de Filtros FIR de Fase Lineal

title: Complemento (Nivel C)

### 1. Explicación intuitiva
En el procesamiento digital de señales, una respuesta en fase lineal garantiza que todas las componentes espectrales de una señal de entrada sufran exactamente el mismo retardo temporal al atravesar el filtro [1, 2]. Esto evita la distorsión de fase (o dispersión), conservando intacta la forma de onda de la señal en el dominio del tiempo, lo cual es fundamental en aplicaciones de transmisión de datos, procesamiento de imágenes y audio de alta fidelidad [3, 4]. En sistemas FIR causales de coeficientes reales, esta propiedad no requiere polos fuera del origen (garantizando siempre la estabilidad absoluta) y se logra imponiendo condiciones de simetría o antisimetría en la respuesta al impulso $h(n)$ respecto a su centro temporal $\alpha = \frac{N-1}{2}$ [2, 3, 5].

---

### 2. Definición formal
Un filtro FIR causal de longitud $N$ (orden $N-1$) con respuesta al impulso real $h(n)$ definida en $0 \le n \le N-1$ posee **fase lineal exacta** si su respuesta en frecuencia $H(\omega)$ se expresa de la forma [6, 7]:

$$
H(\omega) = \pm |H(\omega)| e^{j \theta(\omega)}
$$

donde la función de fase $\theta(\omega)$ satisface una de las dos condiciones siguientes [8-10]:

1. **Fase lineal estricta (retardo de fase y de grupo constantes)** [1, 2, 11]:
   
$$
\theta(\omega) = -\alpha \omega, \quad -\pi \le \omega \le \pi
$$

   con retardo de fase $\tau_p = \alpha$ y retardo de grupo $\tau_g = \alpha$, donde $\alpha = \frac{N-1}{2}$ [1, 12]. Esto requiere que la respuesta al impulso posea **simetría positiva** [2, 13]:
   
$$
h(n) = h(N-1-n), \quad 0 \le n \le N-1
$$


2. **Fase lineal en sentido amplio (retardo de grupo constante)** [2, 7, 14]:
   
$$
\theta(\omega) = \beta - \alpha \omega, \quad -\pi \le \omega \le \pi, \quad \beta = \pm \frac{\pi}{2}
$$

   con retardo de grupo $\tau_g = \alpha = \frac{N-1}{2}$ [1, 14]. Esto requiere que la respuesta al impulso posea **antisimetría (simetría negativa)** [9, 11]:
   
$$
h(n) = -h(N-1-n), \quad 0 \le n \le N-1
$$

   con la condición adicional $h\left(\frac{N-1}{2}\right) = 0$ cuando $N$ es impar [9, 15, 16].

#### Clasificación en cuatro tipos de filtros FIR de fase lineal [15, 17, 18]:
- **Tipo I ($h(n)$ simétrico, $N$ impar)**: $\alpha$ es un entero. No presenta ceros obligatorios en $\omega = 0$ ni $\omega = \pi$; es apto para filtros Pasa-Bajos $LP$, Pasa-Altos $HP$, Pasa-Banda $BP$ y Rechaza-Banda $BS$ [19-21].
- **Tipo II ($h(n)$ simétrico, $N$ par)**: $\alpha$ es un semi-entero. Posee un cero obligatorio en $z = -1$ ($\omega = \pi$), de modo que $H(\pi) = 0$; no puede emplearse para filtros Pasa-Altos ni Rechaza-Banda [15, 21-23].
- **Tipo III ($h(n)$ antisimétrico, $N$ impar)**: $\alpha$ es un entero. Posee ceros obligatorios en $z = 1$ ($\omega = 0$) y en $z = -1$ ($\omega = \pi$); no es adecuado para LP, HP ni BS, pero es óptimo para diferenciadores y transformadores de Hilbert [15, 21, 23, 24].
- **Tipo IV ($h(n)$ antisimétrico, $N$ par)**: $\alpha$ es un semi-entero. Posee un cero obligatorio en $z = 1$ ($\omega = 0$), de modo que $H(0) = 0$; no puede utilizarse para filtros Pasa-Bajos ni Rechaza-Banda [21, 22, 25].

#### Ubicación de ceros en el plano $z$ [18, 26, 27]:
Si $z_1 = r e^{j\theta}$ es un cero de la función de transferencia $H(z)$, la condición de fase lineal con coeficientes reales obliga a que sus ceros aparezcan en cuadrupletes: $z_1$, su complejo conjugado $z_1^* = r e^{-j\theta}$, su recíproco $\frac{1}{z_1} = \frac{1}{r} e^{-j\theta}$ y el conjugado de su recíproco $\frac{1}{z_1^*} = \frac{1}{r} e^{j\theta}$ [26-28]. Si el cero se ubica sobre la circunferencia unitaria ($r = 1$) o sobre el eje real ($\theta = 0, \pi$), este patrón se reduce a pares [26, 27].

---

### 3. Diagrama (Constelación de Ceros en el Plano $z$)

```tikz
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{amsmath}
\pgfplotsset{compat=1.18}
\begin{document}
\begin{tikzpicture}
  \begin{axis}[
    axis lines=middle,
    xlabel={$\text{Re}$},
    ylabel={$\text{Im}$},
    xmin=-1.8, xmax=1.8,
    ymin=-1.8, ymax=1.8,
    grid=both,
    grid style={line width=.1pt, draw=gray!20},
    axis equal image,
    ticks=none
  ]
    \draw[dashed, teal!80, line width=0.8pt] (axis cs:0,0) circle [radius=1cm];
    \node[teal, anchor=north west] at (axis cs:0.707,-0.707) {\small $|z|=1$};

    \node[orange, font=\bfseries] at (axis cs:0.5, 0.5) {$\circ$};
    \node[anchor=south east] at (axis cs:0.5, 0.5) {\tiny $z_1$};

    \node[orange, font=\bfseries] at (axis cs:0.5, -0.5) {$\circ$};
    \node[anchor=north east] at (axis cs:0.5, -0.5) {\tiny $z_1^*$};

    \node[orange, font=\bfseries] at (axis cs:1.2, 1.2) {$\circ$};
    \node[anchor=south west] at (axis cs:1.2, 1.2) {\tiny $\frac{1}{z_1^*}$};

    \node[orange, font=\bfseries] at (axis cs:1.2, -1.2) {$\circ$};
    \node[anchor=north west] at (axis cs:1.2, -1.2) {\tiny $\frac{1}{z_1}$};

    \node[teal, font=\Large\bfseries] at (axis cs:0,0) {$\times$};
    \node[anchor=north east] at (axis cs:0,0) {\tiny $N-1$ polos};
  \end{axis}
\end{tikzpicture}
\end{document}
```

---

### 4. Preguntas de comprensión
1. ¿Por qué un filtro FIR con simetría positiva y longitud par $N$ (Tipo II) no puede utilizarse para diseñar un filtro pasa-altos? [15, 22, 23]
2. ¿Cuál es la diferencia física fundamental entre requerir $\theta(\omega) = -\alpha \omega$ y requerir $\theta(\omega) = \beta - \alpha \omega$? [1, 2, 14]
3. Si un filtro FIR de fase lineal tiene un cero complejo en $z_1 = 0.5 e^{j \pi/3}$, ¿cuáles son los otros tres ceros obligatorios asociados en el plano $z$? [26, 27, 29]

---

### 5. Ejercicios resueltos

##### Ej. 1 Demostración de respuesta en frecuencia y retardo para simetría positiva con $N$ impar (Tipo I)
Obtener la expresión compacta de la respuesta en frecuencia $H(\omega)$ y verificar la linealidad de la fase para un filtro FIR causal de longitud $N = 5$ con coeficientes reales simétricos $h(n) = \{b_0, b_1, b_2, b_1, b_0\}$ [11, 30, 31].

**Resolución:**
La Transformada de Fourier de Tiempo Discreto $DTFT$ de la secuencia de longitud $N = 5$ viene dada por [6, 30]:

$$
H(\omega) = \sum_{n=0}^{4} h(n) e^{-j \omega n} = b_0 + b_1 e^{-j \omega} + b_2 e^{-j 2\omega} + b_1 e^{-j 3\omega} + b_0 e^{-j 4\omega}
$$

Factorizando el término de retardo del centro de simetría $\alpha = \frac{N-1}{2} = \frac{5-1}{2} = 2$ [2, 31]:

$$
H(\omega) = e^{-j 2\omega} \left[ b_0 e^{j 2\omega} + b_1 e^{j \omega} + b_2 + b_1 e^{-j \omega} + b_0 e^{-j 2\omega} \right]
$$

Agrupando las exponenciales complejas conjugadas utilizando la identidad de Euler $e^{j k \omega} + e^{-j k \omega} = 2 \cos(k \omega)$ [8, 31]:

$$
H(\omega) = e^{-j 2\omega} \left[ b_2 + 2 b_1 \cos(\omega) + 2 b_0 \cos(2\omega) \right]
$$

Definiendo la respuesta en amplitud real $H_r(\omega)$ como [19, 31]:

$$
H_r(\omega) = b_2 + 2 b_1 \cos(\omega) + 2 b_0 \cos(2\omega)
$$

La respuesta en frecuencia adopta la forma estándar [6, 31]:

$$
H(\omega) = H_r(\omega) e^{-j 2\omega}
$$

Por lo tanto:
- **Respuesta de magnitud:** $|H(\omega)| = |H_r(\omega)|$ [6, 31].
- **Respuesta de fase:** $\theta(\omega) = -2\omega$ (para $H_r(\omega) \ge 0$) o $\theta(\omega) = -2\omega + \pi$ (para $H_r(\omega) < 0$) [16, 19].
- **Retardo de fase y retardo de grupo:** $\tau_p = -\frac{\theta(\omega)}{\omega} = 2$ muestras, $\tau_g = -\frac{d\theta(\omega)}{d\omega} = 2$ muestras [1, 17].

---

##### Ej. 2 Análisis, clasificación y realización con estructura de fase lineal
Dado el filtro FIR determinado por la ecuación de diferencias [32, 33]:

$$
y(n) = x(n) + \frac{1}{2}x(n-1) - \frac{1}{4}x(n-2) + \frac{1}{2}x(n-3) + x(n-4)
$$

$a$ Verificar si cumple la condición de fase lineal y determinar su tipo (Tipo I-IV) [11, 33].
$b$ Obtener la función de transferencia $H(z)$ e implementar la estructura de realización de fase lineal que minimice el número de multiplicadores [13, 33].

**Resolución:**

**(a) Verificación de la fase lineal y clasificación:**
La respuesta al impulso del filtro se extrae directamente de los coeficientes de la entrada [34, 35]:

$$
h(n) = \left\{ 1, \; \frac{1}{2}, \; -\frac{1}{4}, \; \frac{1}{2}, \; 1 \right\}, \quad 0 \le n \le 4
$$

La longitud del filtro es $N = 5$ (impar) [11, 35]. Verificando la condición de simetría respecto al centro $\alpha = \frac{5-1}{2} = 2$ [2, 36]:

$$
h(0) = h(4) = 1, \quad h(1) = h(3) = \frac{1}{2}, \quad h(2) = -\frac{1}{4}
$$

Puesto que $h(n) = h(4-n)$ para todo $n \in \{0, 1, 2, 3, 4\}$, la respuesta al impulso presenta **simetría positiva** con longitud impar $N = 5$, lo que clasifica al sistema como un **Filtro FIR de Fase Lineal Tipo I** [11, 17, 37].

**(b) Función de transferencia y realización óptima:**
Aplicando la Transformada Z a la respuesta al impulso [35, 38]:

$$
H(z) = \sum_{n=0}^{4} h(n) z^{-n} = 1 + \frac{1}{2} z^{-1} - \frac{1}{4} z^{-2} + \frac{1}{2} z^{-3} + z^{-4}
$$

Agrupando las potencias de $z^{-1}$ asociadas a coeficientes simétricos [13, 35]:

$$
H(z) = \left( 1 + z^{-4} \right) + \frac{1}{2} \left( z^{-1} + z^{-3} \right) - \frac{1}{4} z^{-2}
$$

Expresando la relación en el dominio $z$ para la salida $Y(z)$ [39, 40]:

$$
Y(z) = \left[ X(z) + z^{-4} X(z) \right] + \frac{1}{2} \left[ z^{-1} X(z) + z^{-3} X(z) \right] - \frac{1}{4} z^{-2} X(z)
$$

Esta agrupación reduce las multiplicaciones necesarias de 5 (en forma directa) a solo 3 multiplicadores ($1$, $\frac{1}{2}$ y $-\frac{1}{4}$), cumpliendo con el mínimo teórico de $\frac{N+1}{2} = 3$ multiplicaciones [22, 33, 41].
