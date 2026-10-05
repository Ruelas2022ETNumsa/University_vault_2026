## [3. Filtro Analógico Chebyshev]

title: Complemento (Nivel C)

1. Explicación intuitiva
El **filtro analógico de Chebyshev** es un prototipo de filtro diseñado para lograr una transición más abrupta entre la banda de paso y la banda de rechazo que la del filtro Butterworth de igual orden [1]. Para conseguir esta mayor pendiente de caída (*rolloff*), el filtro de Chebyshev introduce variaciones periódicas de amplitud o **rizos (*ripples*) de igual magnitud** (comportamiento equirrizo) en una de las bandas de frecuencia [1].

Existen dos tipos principales de filtros de Chebyshev [1]:
- **Tipo I (Chebyshev directo):** Presenta rizo constante en la banda de paso y una caída estrictamente monótona en la banda de rechazo [1, 2]. Es un filtro de polos puros (sin ceros finitos) [2, 3].
- **Tipo II (Chebyshev inverso):** Presenta un comportamiento estrictamente monótono en la banda de paso y rizo constante en la banda de rechazo [2, 4]. Su función de transferencia posee tanto polos como ceros sobre el eje imaginario $j\Omega$ [2, 4].

A diferencia del filtro Butterworth —cuyos polos se ubican sobre una circunferencia en el plano $s$—, los polos de un filtro de Chebyshev Tipo I se distribuyen sobre una **elipse** en el semiplano izquierdo del plano complejo [5, 6]. Esto comprime la ubicación de los polos hacia el eje imaginario, incrementando la selectividad del filtro a costa de introducir una respuesta de fase no lineal más acentuada en la banda de paso [4, 7].

2. Definición formal
La respuesta en magnitud al cuadrado de un filtro analógico Chebyshev Tipo I de orden $N$ está dada por [1]:

$$
|H_a(j\Omega)|^2 = \frac{1}{1 + \epsilon^2 C_N^2\left(\frac{\Omega}{\Omega_p}\right)}
$$

donde $\Omega_p$ es la frecuencia límite de la banda de paso, $\epsilon$ es el parámetro de rizo en la banda de paso [1], y $C_N(x)$ es el **polinomio de Chebyshev de primer tipo y orden $N$** [1, 8], definido por:

$$
C_N(x) = \begin{cases} \cos\left(N \cos^{-1}(x)\right), & |x| \le 1 \\ \cosh\left(N \cosh^{-1}(x)\right), & |x| > 1 \end{cases}
$$

donde $x = \frac{\Omega}{\Omega_p}$ [1]. Los polinomios de Chebyshev satisfacen la relación recursiva [9, 10]:

$$
C_0(x) = 1, \quad C_1(x) = x, \quad C_{N+1}(x) = 2x C_N(x) - C_{N-1}(x)
$$


El parámetro de rizo $\epsilon$ se relaciona con la atenuación máxima en la banda de paso $R_p$ (en dB) mediante [11, 12]:

$$
\epsilon = \sqrt{10^{0.1 R_p} - 1}
$$

El orden mínimo $N$ requerido para satisfacer las especificaciones de atenuación $A_s$ en la banda de rechazo $\Omega_s$ se determina por [5, 13]:

$$
N \ge \frac{\cosh^{-1}\left(\sqrt{\frac{10^{0.1 A_s} - 1}{10^{0.1 R_p} - 1}}\right)}{\cosh^{-1}\left(\frac{\Omega_s}{\Omega_p}\right)} = \frac{\ln\left(g + \sqrt{g^2 - 1}\right)}{\ln\left(\frac{\Omega_s}{\Omega_p} + \sqrt{\left(\frac{\Omega_s}{\Omega_p}\right)^2 - 1}\right)}, \quad g = \frac{\sqrt{10^{0.1 A_s} - 1}}{\epsilon}
$$


Los polos del filtro estables (semiplano izquierdo $\text{LHP}$) se ubican sobre una elipse con semieje menor $a \Omega_p$ y semieje mayor $b \Omega_p$ [6, 14]:

$$
s_k = x_k + j y_k = -a \Omega_p \sin(\phi_k) + j b \Omega_p \cos(\phi_k), \quad k = 1, 2, \dots, N
$$

donde los ángulos $\phi_k$ coinciden con las posiciones de un filtro Butterworth equivalente [6]:

$$
\phi_k = \frac{(2k-1)\pi}{2N}, \quad k = 1, 2, \dots, N
$$

y los parámetros de la elipse $a$ y $b$ se calculan como [14]:

$$
a = \frac{1}{2} \left( \alpha^{1/N} - \alpha^{-1/N} \right), \quad b = \frac{1}{2} \left( \alpha^{1/N} + \alpha^{-1/N} \right), \quad \alpha = \frac{1}{\epsilon} + \sqrt{1 + \frac{1}{\epsilon^2}}
$$


3. Figura o diagrama
Distribución de los polos estables de un filtro Chebyshev Tipo I de orden $N=4$ sobre una elipse en el plano complejo $s$:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.3, >=latex]
    % Ejes cartesianos
    \draw[->] (-2.2,0) -- (1.5,0) node[right] {$\sigma = \mathrm{Re}\{s\}$};
    \draw[->] (0,-2.2) -- (0,2.2) node[above] {$j\Omega = \mathrm{Im}\{s\}$};

    % Circunferencia de referencia Butterworth y Elipse Chebyshev
    \draw[dashed, color=gray!60] (0,0) circle (1.5cm);
    \draw[thick, teal] (0,0) ellipse (0.6cm and 1.5cm);

    % Polos LHP (estables) N=4
    \node[teal, mark size=4pt] at (-0.23, 1.39) {\textbf{$\times$}};
    \node[teal, mark size=4pt] at (-0.23, -1.39) {\textbf{$\times$}};
    \node[teal, mark size=4pt] at (-0.55, 0.57) {\textbf{$\times$}};
    \node[teal, mark size=4pt] at (-0.55, -0.57) {\textbf{$\times$}};

    % Acotaciones de semiejes
    \draw[<->, orange!90!black, thick] (0, -1.8) -- (-0.6, -1.8) node[midway, below] {$a\Omega_p$};
    \draw[<->, teal, thick] (1.8, 0) -- (1.8, 1.5) node[midway, right] {$b\Omega_p$};

    \node[above left] at (-0.23, 1.39) {$s_1$};
    \node[below left] at (-0.55, 0.57) {$s_2$};

\end{tikzpicture}
\end{document}
```

4. Preguntas de comprensión
5. ¿Cuál es la diferencia fundamental en el comportamiento de magnitud entre un filtro Chebyshev Tipo I y un filtro Chebyshev Tipo II tanto en la banda de paso como en la de rechazo? [1, 4]
6. ¿Cómo se relaciona la distribución elíptica de los polos en el plano $s$ con el hecho de que el filtro Chebyshev logre una banda de transición más angosta que el filtro Butterworth del mismo orden? [6, 14, 15]
7. ¿Por qué el valor de la ganancia en $\Omega = 0$ ($|H_a(j0)|^2$) difiere entre un filtro Chebyshev Tipo I de orden par y uno de orden impar? [9, 14, 16]

8. Ejercicios resueltos

##### Ej. 1: Cálculo de parámetros, orden y función de transferencia
Diseñar un filtro pasa-bajo analógico Chebyshev Tipo I que satisfaga las siguientes especificaciones:
- Banda de paso: Rizo máximo de $1\text{ dB}$ hasta $\Omega_p = 1000\text{ rad/s}$.
- Banda de rechazo: Atenuación mínima de $30\text{ dB}$ para $\Omega_s = 2000\text{ rad/s}$.

Obtener el factor de rizo $\epsilon$, el orden $N$, la ubicación de los polos en el plano $s$ y la función de transferencia $H_a(s)$.

**Resolución:**

**Paso 1: Cálculo del factor de rizo $\epsilon$ y parámetro de atenuación $g$**

$$
\epsilon = \sqrt{10^{0.1 R_p} - 1} = \sqrt{10^{0.1} - 1} = \sqrt{1.258925 - 1} = \sqrt{0.258925} \approx 0.50884
$$


$$
g = \frac{\sqrt{10^{0.1 A_s} - 1}}{\epsilon} = \frac{\sqrt{10^{3} - 1}}{0.50884} = \frac{\sqrt{999}}{0.50884} = \frac{31.60696}{0.50884} \approx 62.1143
$$


**Paso 2: Determinación del orden $N$**
La relación de frecuencias de la banda de transición es $\frac{\Omega_s}{\Omega_p} = \frac{2000}{1000} = 2$.

$$
N \ge \frac{\ln\left(g + \sqrt{g^2 - 1}\right)}{\ln\left(\frac{\Omega_s}{\Omega_p} + \sqrt{\left(\frac{\Omega_s}{\Omega_p}\right)^2 - 1}\right)} = \frac{\ln\left(62.1143 + \sqrt{62.1143^2 - 1}\right)}{\ln\left(2 + \sqrt{2^2 - 1}\right)}
$$


$$
N \ge \frac{\ln(62.1143 + 62.1062)}{\ln(2 + 1.73205)} = \frac{\ln(124.2205)}{\ln(3.73205)} = \frac{4.82208}{1.31696} \approx 3.6616
$$

Se adopta el orden entero superior:

$$
N = 4
$$


**Paso 3: Cálculo de los semiejes de la elipse $a$ y $b$**

$$
\alpha = \frac{1}{\epsilon} + \sqrt{1 + \frac{1}{\epsilon^2}} = \frac{1}{0.50884} + \sqrt{1 + \left(\frac{1}{0.50884}\right)^2} = 1.96525 + 2.20504 = 4.17029
$$


$$
\alpha^{1/4} = (4.17029)^{0.25} \approx 1.42886, \quad \alpha^{-1/4} = \frac{1}{1.42886} \approx 0.69986
$$


$$
a = \frac{1}{2}(1.42886 - 0.69986) = 0.36450
$$


$$
b = \frac{1}{2}(1.42886 + 0.69986) = 1.06436
$$


**Paso 4: Determinación de las coordenadas de los polos estables $s_k$**
Para $N = 4$, los ángulos de los polos son $\phi_k = \frac{(2k-1)\pi}{8}$ para $k = 1, 2, 3, 4$:
- $\phi_1 = 22.5^\circ \implies \sin(22.5^\circ) = 0.38268, \quad \cos(22.5^\circ) = 0.92388$
- $\phi_2 = 67.5^\circ \implies \sin(67.5^\circ) = 0.92388, \quad \cos(67.5^\circ) = 0.38268$

Multiplicando por los semiejes escalados por $\Omega_p = 1000\text{ rad/s}$:
- $x_1 = -0.36450 \times 1000 \times 0.38268 = -139.49\text{ rad/s}$
- $y_1 = 1.06436 \times 1000 \times 0.92388 = 983.34\text{ rad/s}$
- $x_2 = -0.36450 \times 1000 \times 0.92388 = -336.75\text{ rad/s}$
- $y_2 = 1.06436 \times 1000 \times 0.38268 = 407.31\text{ rad/s}$

Los polos conjugados resultan:

$$
s_1, s_4 = -139.49 \pm j 983.34, \quad s_2, s_3 = -336.75 \pm j 407.31
$$


**Paso 5: Construcción de la función de transferencia $H_a(s)$**
Formando las secciones cuadráticas del denominador:

$$
(s - s_1)(s - s_1^*) = s^2 + 2(139.49)s + (139.49^2 + 983.34^2) = s^2 + 278.98 s + 986427
$$


$$
(s - s_2)(s - s_2^*) = s^2 + 2(336.75)s + (336.75^2 + 407.31^2) = s^2 + 673.50 s + 279302
$$


Dado que $N = 4$ es par, la ganancia en DC es $H_a(0) = \frac{1}{\sqrt{1 + \epsilon^2}} = \frac{1}{\sqrt{1.258925}} \approx 0.89125$ [14, 17]. El término constante del numerador $K$ es:

$$
K = 0.89125 \times (986427 \times 279302) = 0.89125 \times (2.7551 \times 10^{11}) \approx 2.4555 \times 10^{11}
$$


Sustituyendo en la expresión final:

$$
H_a(s) = \frac{2.4555 \times 10^{11}}{\left(s^2 + 278.98 s + 986427\right)\left(s^2 + 673.50 s + 279302\right)}
$$


---

##### Ej. 2 (Mayor dificultad): Obtención de la ecuación polinomial de Chebyshev
Demostrar mediante la relación de recurrencia que el polinomio de Chebyshev de orden $N = 3$ es $C_3(x) = 4x^3 - 3x$ y utilizarlo para expresar la función de respuesta en magnitud al cuadrado $|H_a(j\Omega)|^2$ de un filtro pasa-bajo de orden 3 con $\Omega_p = 100\text{ rad/s}$ y rizo de $0.5\text{ dB}$.

**Resolución:**

**Paso 1: Deducción del polinomio $C_3(x)$**
Partiendo de las condiciones iniciales $C_0(x) = 1$ y $C_1(x) = x$ [3]:
1. Para $N = 1$:

$$
C_2(x) = 2x C_1(x) - C_0(x) = 2x(x) - 1 = 2x^2 - 1
$$

2. Para $N = 2$:

$$
C_3(x) = 2x C_2(x) - C_1(x) = 2x(2x^2 - 1) - x = 4x^3 - 2x - x = 4x^3 - 3x
$$


**Paso 2: Cálculo del factor de rizo $\epsilon$**
Para $R_p = 0.5\text{ dB}$:

$$
\epsilon^2 = 10^{0.1(0.5)} - 1 = 10^{0.05} - 1 \approx 1.12202 - 1 = 0.12202
$$


**Paso 3: Expresión analítica de $|H_a(j\Omega)|^2$**
Sustituyendo $x = \frac{\Omega}{\Omega_p} = \frac{\Omega}{100}$ en la definición de magnitud al cuadrado:

$$
C_3^2\left(\frac{\Omega}{100}\right) = \left[ 4\left(\frac{\Omega}{100}\right)^3 - 3\left(\frac{\Omega}{100}\right) \right]^2 = \left( 4 \times 10^{-6} \Omega^3 - 3 \times 10^{-2} \Omega \right)^2
$$


$$
|H_a(j\Omega)|^2 = \frac{1}{1 + 0.12202 \left( 4 \times 10^{-6} \Omega^3 - 3 \times 10^{-2} \Omega \right)^2}
$$

