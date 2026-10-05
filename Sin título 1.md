## [3. Filtro Analógico Butterworth]

title: Complemento (Nivel C)

1. Explicación intuitiva
El filtro analógico Butterworth es un prototipo fundamental de filtro pasa-bajo caracterizado por presentar una respuesta en frecuencia suave y monótona, sin oscilaciones ni rizos, tanto en la banda de paso como en la banda de rechazo [1-4]. Por esta razón, se le conoce como un filtro de **máxima planitud** (*maximally flat*) en el origen de frecuencias ($\Omega = 0$) [2, 4, 5].

A diferencia de otros filtros prototipo (como los filtros Chebyshev o Elípticos, que introducen rizos para acelerar la caída en la banda de transición) [6-8], el filtro Butterworth sacrifica la pendiente de atenuación a cambio de una respuesta de magnitud lisa y una respuesta de fase más lineal en la banda de paso [9-11]. Su comportamiento queda completamente determinado por dos parámetros principales: el orden del filtro $N$ y la frecuencia de corte a $-3\text{ dB}$ $\Omega_c$ [2, 4, 12]. A medida que el orden $N$ aumenta, la banda de transición se vuelve más angosta y la respuesta se aproxima progresivamente a la de un filtro pasa-bajo ideal [1, 4, 12, 13].

En el diseño de filtros digitales IIR, el filtro Butterworth analógico cumple la función de **prototipo continuo**, el cual posteriormente se transforma al dominio discreto mediante técnicas como la Transformación Bilineal o la Invariancia al Impulso [14-17].

2. Definición formal
El filtro analógico Butterworth pasa-bajo de orden $N$ se define mediante la función de respuesta en magnitud al cuadrado [1, 2, 4, 5]:

$$
|H_a(j\Omega)|^2 = \frac{1}{1 + \left(\frac{\Omega}{\Omega_c}\right)^{2N}}
$$

donde $\Omega$ es la frecuencia analógica continua en $\text{rad/s}$, $\Omega_c$ es la frecuencia de corte a $-3\text{ dB}$ y $N$ es el orden del sistema [1, 2, 4].

Expandiendo a la variable compleja de Laplace $s = j\Omega$, se obtiene la relación polinomial [5, 18-20]:

$$
H_a(s) H_a(-s) = \frac{1}{1 + \left(\frac{s}{j\Omega_c}\right)^{2N}} = \frac{1}{1 + (-1)^N \left(\frac{s}{\Omega_c}\right)^{2N}}
$$

Los polos de la función compuesta $H_a(s)H_a(-s)$ son las $2N$ raíces del denominador, las cuales se distribuyen de manera simétrica sobre una circunferencia de radio $\Omega_c$ en el plano complejo $s$, con posiciones angulares dadas por [18-22]:

$$
\varphi_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2N}, \quad k = 1, 2, \dots, 2N
$$

Para garantizar un filtro causal y estable, se seleccionan únicamente los $N$ polos ubicados en el semiplano izquierdo de Laplace ($\text{Re}\{s\} < 0$) [17, 18, 20, 21, 23]:

$$
s_k = \Omega_c \exp\left(j \left[\frac{\pi}{2} + \frac{(2k-1)\pi}{2N}\right]\right), \quad k = 1, 2, \dots, N
$$


3. Figura o diagrama
Visualización de la distribución de polos en el plano complejo $s$ para un filtro Butterworth de orden $N=3$ con frecuencia de corte normalizada $\Omega_c = 1$ [18, 21, 23]:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.3, >=latex]
    % Ejes cartesianos
    \draw[->] (-2.2,0) -- (1.8,0) node[right] {$\sigma = \mathrm{Re}\{s\}$};
    \draw[->] (0,-2.2) -- (0,2.2) node[above] {$j\Omega = \mathrm{Im}\{s\}$};

    % Circunferencia de radio Omega_c = 1.5
    \draw[dashed, color=gray!80, thick] (0,0) circle (1.5cm);
    \node[below right, color=gray!90] at (1.1, -1.1) {$\Omega_c$};

    % Polos LHP (estables) - N=3 -> angulos: 120°, 180°, 240°
    \node[teal, mark size=4pt] at (-0.75, 1.299) {\textbf{$\times$}};
    \node[above left] at (-0.75, 1.299) {$s_1 = e^{j 120^\circ}$};

    \node[teal, mark size=4pt] at (-1.5, 0) {\textbf{$\times$}};
    \node[below left] at (-1.5, 0) {$s_2 = e^{j 180^\circ}$};

    \node[teal, mark size=4pt] at (-0.75, -1.299) {\textbf{$\times$}};
    \node[below left] at (-0.75, -1.299) {$s_3 = e^{j 240^\circ}$};

    % Polos RHP (descartados) - angulos: 0°, 60°, 300°
    \node[orange!80!black, opacity=0.4] at (1.5, 0) {$\times$};
    \node[orange!80!black, opacity=0.4] at (0.75, 1.299) {$\times$};
    \node[orange!80!black, opacity=0.4] at (0.75, -1.299) {$\times$};

    % Linea de radio e indicacion
    \draw[->, gray] (0,0) -- (-0.75, 1.299);
    \node[midway, left] at (-0.3, 0.6) {$\Omega_c$};
\end{tikzpicture}
\end{document}
```

4. Preguntas de comprensión
5. ¿Por qué la respuesta en magnitud del filtro Butterworth se denomina de "máxima planitud" en el origen ($\Omega = 0$) y qué relación matemática guardan las primeras $2N-1$ derivadas de $|H_a(j\Omega)|^2$ con esta propiedad? [2]
6. ¿Cuál es el procedimiento matemático para seleccionar los polos de $H_a(s)$ a partir de las $2N$ raíces de $H_a(s)H_a(-s)=0$ y por qué razón física y de estabilidad se descartan los polos del semiplano derecho? [17, 18, 21]
7. Si se compara un filtro Butterworth con un filtro Chebyshev tipo I del mismo orden y bajo las mismas especificaciones de atenación, ¿cuál de los dos presenta una banda de transición más angosta y cuál exhibe un comportamiento de fase más regular en la banda de paso? [3, 6, 9, 10, 24]

8. Ejercicios resueltos

##### Ej. 1: Determinación de orden, polos y función de transferencia analógica
Diseñar un filtro pasa-bajo analógico Butterworth que satisfaga las siguientes especificaciones [22]:
- Atenuación máxima en la banda de paso: $3\text{ dB}$ a $f_p = 500\text{ Hz}$.
- Atenuación mínima en la banda de rechazo: $40\text{ dB}$ a $f_s = 1000\text{ Hz}$.

Obtener el orden $N$, la frecuencia de corte $\Omega_c$, las posiciones de los polos estables en el plano $s$ y la función de transferencia analógica $H_a(s)$ [22].

**Resolución:**

**Paso 1: Conversión a frecuencias angulares y factores de especificación**
Las frecuencias analógicas en $\text{rad/s}$ son [22]:

$$
\Omega_p = 2\pi f_p = 2\pi (500) = 1000\pi \text{ rad/s}
$$


$$
\Omega_s = 2\pi f_s = 2\pi (1000) = 2000\pi \text{ rad/s}
$$

Dado que en $\Omega_p = 1000\pi\text{ rad/s}$ la atenuación es de $3\text{ dB}$ ($A_p = 1/\sqrt{2} \approx 0.7071$), la frecuencia de corte a $-3\text{ dB}$ coincide con la frecuencia de la banda de paso [22]:

$$
\Omega_c = \Omega_p = 1000\pi \text{ rad/s}
$$

Para la banda de rechazo ($A_s = 40\text{ dB} \implies A_s = 0.01$) [22]:

$$
\frac{1}{A_s^2} - 1 = 10^4 - 1 = 9999
$$


**Paso 2: Cálculo del orden del filtro $N$**
Aplicando la ecuación para la determinación del orden [12, 22, 25, 26]:

$$
N \ge \frac{\log_{10}\left(\frac{1/A_s^2 - 1}{1/A_p^2 - 1}\right)}{2 \log_{10}\left(\frac{\Omega_s}{\Omega_p}\right)} = \frac{\log_{10}(9999)}{2 \log_{10}\left(\frac{2000\pi}{1000\pi}\right)} = \frac{3.99996}{2 \log_{10}(2)} = \frac{3.99996}{0.60206} \approx 6.643
$$

Tomando el entero superior inmediato [22, 25, 26]:

$$
N = 7
$$


**Paso 3: Ubicación de los polos estables en el semiplano izquierdo ($\text{LHP}$)**
Los $N = 7$ polos del semiplano izquierdo sobre la circunferencia de radio $\Omega_c = 1000\pi$ tienen fases dadas por [17, 22]:

$$
\varphi_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{14}, \quad k = 1, 2, \dots, 7
$$

Calculando las componentes rectangulares de cada polo $s_k = \Omega_c e^{j\varphi_k}$ [22, 27]:
- $k=1: \varphi_1 = 102.86^\circ \implies s_1 = 1000\pi (-0.2225 + j0.9749)$
- $k=2: \varphi_2 = 128.57^\circ \implies s_2 = 1000\pi (-0.6235 + j0.7818)$
- $k=3: \varphi_3 = 154.29^\circ \implies s_3 = 1000\pi (-0.8987 + j0.4384)$
- $k=4: \varphi_4 = 180.00^\circ \implies s_4 = -1000\pi$
- $k=5: \varphi_5 = 205.71^\circ \implies s_5 = s_3^*$
- $k=6: \varphi_6 = 231.43^\circ \implies s_6 = s_2^*$
- $k=7: \varphi_7 = 257.14^\circ \implies s_7 = s_1^*$

**Paso 4: Construcción de la función de transferencia $H_a(s)$**
El polinomio denominador normalizado ($\Omega_c = 1$) para $N=7$ factorizado en secciones cuadráticas y lineales es [28-30]:

$$
D_n(s) = (s + 1)(s^2 + 1.8019 s + 1)(s^2 + 1.2470 s + 1)(s^2 + 0.4450 s + 1)
$$

Sustituyendo el escalamiento en frecuencia $s \leftarrow \frac{s}{\Omega_c} = \frac{s}{1000\pi}$, se obtiene la función de transferencia desnormalizada [29, 30]:

$$
H_a(s) = \frac{(1000\pi)^7}{(s + 1000\pi)\left(s^2 + 1.8019(1000\pi)s + (1000\pi)^2\right)\left(s^2 + 1.2470(1000\pi)s + (1000\pi)^2\right)\left(s^2 + 0.4450(1000\pi)s + (1000\pi)^2\right)}
$$


---

##### Ej. 2 (Mayor dificultad): Diseño con atenuación en dB y ajuste exacto de la frecuencia de corte
Diseñar un filtro analógico pasa-bajo Butterworth que cumpla con las siguientes especificaciones en dB [25]:
- Banda de paso: Atenuación máxima de $1\text{ dB}$ a $\Omega_p = 200\text{ rad/s}$.
- Banda de rechazo: Atenuación mínima de $30\text{ dB}$ a $\Omega_s = 600\text{ rad/s}$.

Determinar el orden exacto $N$, la frecuencia de corte $\Omega_c$ ajustada para satisfacer la banda de paso exactamente, y la función de transferencia desnormalizada $H_a(s)$ [25, 31].

**Resolución:**

**Paso 1: Conversión de especificaciones en dB a factores de magnitud**
Las pérdidas en dB se convierten mediante [25, 32, 33]:

$$
\frac{1}{A_p^2} - 1 = 10^{R_p/10} - 1 = 10^{0.1} - 1 \approx 0.25893
$$


$$
\frac{1}{A_s^2} - 1 = 10^{A_s/10} - 1 = 10^{3.0} - 1 = 999
$$


**Paso 2: Determinación del orden $N$**
Sustituyendo en la expresión general del orden del filtro [12, 25, 26]:

$$
N \ge \frac{\log_{10}\left(\frac{10^{A_s/10} - 1}{10^{R_p/10} - 1}\right)}{2 \log_{10}\left(\frac{\Omega_s}{\Omega_p}\right)} = \frac{\log_{10}\left(\frac{999}{0.25893}\right)}{2 \log_{10}\left(\frac{600}{200}\right)} = \frac{\log_{10}(3858.18)}{2 \log_{10}(3)} = \frac{3.58638}{2 (0.47712)} \approx 3.758
$$

Como el orden debe ser un número entero, se adopta [25, 34]:

$$
N = 4
$$


**Paso 3: Ajuste de la frecuencia de corte $\Omega_c$**
Puesto que se eligió $N = 4 > 3.758$, el filtro superará las exigencias. Ajustando $\Omega_c$ para cumplir de forma exacta la especificación en la banda de paso $\Omega_p = 200\text{ rad/s}$ [25]:

$$
\Omega_c = \frac{\Omega_p}{\left(10^{R_p/10} - 1\right)^{\frac{1}{2N}}} = \frac{200}{(0.25893)^{\frac{1}{8}}} = \frac{200}{0.84439} \approx 236.86\text{ rad/s}
$$


**Paso 4: Polinomio de Butterworth normalizado para $N = 4$**
Para un orden par $N = 4$, los coeficientes de las secciones cuadráticas del denominador vienen dados por [31, 35]:

$$
b_k = 2 \sin\left(\frac{(2k-1)\pi}{2N}\right), \quad k = 1, 2
$$

- $k=1: b_1 = 2 \sin\left(\frac{\pi}{8}\right) = 0.76537$
- $k=2: b_2 = 2 \sin\left(\frac{3\pi}{8}\right) = 1.84776$

La función de transferencia normalizada ($\Omega_c = 1$) es [28, 29, 31]:

$$
H_n(s) = \frac{1}{(s^2 + 0.7654 s + 1)(s^2 + 1.8478 s + 1)}
$$


**Paso 5: Desnormalización de la función de transferencia $H_a(s)$**
Sustituyendo $s \leftarrow \frac{s}{\Omega_c} = \frac{s}{236.86}$ se obtiene la respuesta del sistema desnormalizado [29, 31]:

$$
H_a(s) = \frac{\Omega_c^4}{\left(s^2 + 0.7654 \Omega_c s + \Omega_c^2\right)\left(s^2 + 1.8478 \Omega_c s + \Omega_c^2\right)}
$$

Evaluando los términos numéricos con $\Omega_c = 236.86\text{ rad/s}$ ($\Omega_c^2 \approx 56102.5$ y $\Omega_c^4 \approx 3.1475 \times 10^9$):
- $0.7654 \Omega_c = 181.29$
- $1.8478 \Omega_c = 437.67$

Sustituyendo directamente en la expresión final:

$$
H_a(s) = \frac{3.1475 \times 10^9}{(s^2 + 181.29 s + 56102.5)(s^2 + 437.67 s + 56102.5)}
$$

