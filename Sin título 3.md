## [3. Gráficas de los Filtros de Chebyshev Tipo 1 y Tipo 2]

title: Complemento (Nivel C)

1. Explicación intuitiva
Las gráficas de respuesta en frecuencia (magnitud) de los filtros de Chebyshev introducen un comportamiento oscilatorio de amplitud constante (**equirrizo**) en una de sus bandas con el objetivo de lograr una transición mucho más rápida hacia la banda de rechazo que la del filtro Butterworth del mismo orden. La diferencia fundamental en la apariencia y propiedades de sus gráficas radica en cuál de las bandas alberga estas oscilaciones:

- **Chebyshev Tipo 1 (Directo):**
  - **Banda de paso ($0 \le \Omega \le \Omega_p$):** Muestra un comportamiento **equirrizo**, oscilando entre el valor máximo $1$ y el valor mínimo $\frac{1}{\sqrt{1+\epsilon^2}}$.
  - **Comportamiento en la frecuencia cero ($\Omega = 0$):** Si el orden $N$ es **impar**, la gráfica inicia en $1$; si $N$ es **par**, inicia en el valor mínimo del rizo $\frac{1}{\sqrt{1+\epsilon^2}}$.
  - **Frecuencia límite ($\Omega = \Omega_p$):** La magnitud pasa exactamente por $\frac{1}{\sqrt{1+\epsilon^2}}$ para todo $N$.
  - **Banda de rechazo ($\Omega > \Omega_p$):** Cae de forma **estrictamente monótona** hacia cero sin volver a oscilar (filtro de polos puros).

- **Chebyshev Tipo 2 (Inverso):**
  - **Banda de paso ($0 \le \Omega \le \Omega_p$):** Muestra una respuesta **estrictamente monótona**, disminuyendo suavemente desde $1$ en $\Omega = 0$ hasta la frecuencia límite.
  - **Banda de rechazo ($\Omega \ge \Omega_s$):** Muestra un comportamiento **equirrizo**, oscilando entre cero y el nivel de atenuación máximo permitido.
  - **Presencia de nulos (ceros):** Toca exactamente el valor cero de magnitud en frecuencias discretas de la banda de rechazo debido a la presencia de ceros ubicados directamente sobre el eje imaginario $j\Omega$.

2. Definición formal
La respuesta en magnitud al cuadrado para cada prototipo analógico pasa-bajo de orden $N$ se expresa como:

**Tipo 1 (Rizo en banda de paso, polos puros):**

$$
|H_I(j\Omega)|^2 = \frac{1}{1 + \epsilon^2 T_N^2\left(\frac{\Omega}{\Omega_p}\right)}
$$

donde $\epsilon = \sqrt{10^{0.1 R_p} - 1}$ representa el parámetro de rizo en la banda de paso, y $T_N(x)$ es el **polinomio de Chebyshev de primer tipo**:

$$
T_N(x) = \begin{cases} \cos\left(N \cos^{-1}(x)\right), & |x| \le 1 \\ \cosh\left(N \cosh^{-1}(x)\right), & |x| > 1 \end{cases}
$$


**Tipo 2 (Monótono en banda de paso, equirrizo en banda de rechazo con ceros):**

$$
|H_{II}(j\Omega)|^2 = \frac{1}{1 + \left[ \epsilon_s^2 T_N^2\left(\frac{\Omega_s}{\Omega}\right) \right]^{-1}} = \frac{\epsilon_s^2 T_N^2\left(\frac{\Omega_s}{\Omega}\right)}{1 + \epsilon_s^2 T_N^2\left(\frac{\Omega_s}{\Omega}\right)}
$$

donde $\Omega_s$ es la frecuencia de inicio de la banda de rechazo y $\epsilon_s = \frac{1}{\sqrt{10^{0.1 A_s} - 1}}$. Las frecuencias de transmisión cero ($|H_{II}(j\Omega_k)| = 0$) ocurren en:

$$
\Omega_k = \frac{\Omega_s}{\cos\left(\frac{(2k-1)\pi}{2N}\right)}, \quad k = 1, 2, \dots, \left\lfloor \frac{N}{2} \right\rfloor
$$


3. Figura o diagrama

Curvas de respuesta en magnitud para **Chebyshev Tipo 1** (comparación entre orden impar $N=3$ y orden par $N=4$):

```desmos-graph
left=-0.2; right=2.5; bottom=-0.1; top=1.2;
width=300; height=200;
---
y = 1 / (1 + 0.25*(4*x^3 - 3*x)^2)^{1/2} |0<=x<=2.5|
y = 1 / (1 + 0.25*(8*x^4 - 8*x^2 + 1)^2)^{1/2} |0<=x<=2.5|
```

Curva de respuesta en magnitud para **Chebyshev Tipo 2** (respuesta monótona en banda de paso y rizo en banda de rechazo con puntos de nulo):

```desmos-graph
left=-0.2; right=3; bottom=-0.1; top=1.2;
width=300; height=200;
---
y = (0.2*(4*(1.2/x)^3 - 3*(1.2/x))^2 / (1 + 0.2*(4*(1.2/x)^3 - 3*(1.2/x))^2))^{1/2} |0.05<=x<=3|
```

4. Preguntas de comprensión
5. ¿Por qué en la gráfica del filtro Chebyshev Tipo 1 de orden par la magnitud en $\Omega = 0$ es igual al límite inferior del rizo $\frac{1}{\sqrt{1+\epsilon^2}}$, mientras que para orden impar la magnitud inicia exactamente en 1?
6. ¿Cuál es el origen algebraico de las muescas de transmisión nula ($|H(j\Omega)| = 0$) presentes en la gráfica de la banda de rechazo del filtro Chebyshev Tipo 2?
7. En términos de distorsión de fase y linealidad del retardo de grupo en la banda de paso, ¿por qué la gráfica del Chebyshev Tipo 2 presenta un comportamiento superior al del Chebyshev Tipo 1?

8. Ejercicios resueltos

##### Ej. 1: Determinación de máximos, mínimos y frecuencias de nulo en gráficas de magnitud
Para un filtro pasa-bajo analógico de **Chebyshev Tipo 1** y uno de **Chebyshev Tipo 2**, ambos de orden $N = 3$, con $\Omega_p = 100\text{ rad/s}$, $\Omega_s = 200\text{ rad/s}$, rizo en banda de paso de $1\text{ dB}$ ($\epsilon = 0.5088$) y atenuación en banda de rechazo de $30\text{ dB}$ ($\epsilon_s = 0.0316$):

a) Encontrar los puntos de máximo y mínimo de la gráfica de magnitud del Tipo 1 en la banda de paso.  
b) Encontrar las frecuencias de transmisión nula (magnitud cero) de la gráfica del Tipo 2 en la banda de rechazo.

**Resolución:**

**a) Puntos característicos de la gráfica Chebyshev Tipo 1 ($N = 3$):**
El polinomio de Chebyshev de orden 3 es $T_3(x) = 4x^3 - 3x$ para $x = \frac{\Omega}{\Omega_p}$.
Los máximos de magnitud suceden cuando $T_3(x) = 0$:

$$
4x^3 - 3x = 0 \implies x(4x^2 - 3) = 0 \implies x_1 = 0, \quad x_{2,3} = \pm \frac{\sqrt{3}}{2} \approx \pm 0.8660
$$

Convertimos a frecuencia angular continua:

$$
\Omega = 0 \text{ rad/s} \implies |H_I(j0)| = 1
$$


$$
\Omega = 0.8660 \times 100 = 86.60 \text{ rad/s} \implies |H_I(j 86.60)| = 1
$$


Los mínimos de la banda de paso suceden cuando $|T_3(x)| = 1$:

$$
4x^3 - 3x = \pm 1 \implies x = \pm 0.5, \quad x = \pm 1
$$

Evaluando para la región positiva ($\Omega \ge 0$):

$$
\Omega = 0.5 \times 100 = 50 \text{ rad/s} \implies |H_I(j 50)| = \frac{1}{\sqrt{1 + (0.5088)^2}} = \frac{1}{\sqrt{1.2589}} \approx 0.8913 \text{ (-1 dB)}
$$


$$
\Omega = 1.0 \times 100 = 100 \text{ rad/s} = \Omega_p \implies |H_I(j 100)| = 0.8913 \text{ (-1 dB)}
$$


**b) Frecuencias de nulo en la gráfica Chebyshev Tipo 2 ($N = 3$):**
Los ceros de la respuesta en magnitud suceden cuando $T_3\left(\frac{\Omega_s}{\Omega}\right) = 0$:

$$
\cos\left(3 \cos^{-1}\left(\frac{\Omega_s}{\Omega}\right)\right) = 0 \implies 3 \cos^{-1}\left(\frac{\Omega_s}{\Omega}\right) = \frac{(2k-1)\pi}{2}, \quad k = 1, 2
$$


$$
\cos^{-1}\left(\frac{\Omega_s}{\Omega}\right) = \frac{\pi}{6}, \frac{5\pi}{6} \implies \frac{\Omega_s}{\Omega} = \cos\left(\frac{\pi}{6}\right) = \frac{\sqrt{3}}{2} \approx 0.8660
$$

Despejando la frecuencia angular de la banda de rechazo con $\Omega_s = 200\text{ rad/s}$:

$$
\Omega_{z1} = \frac{\Omega_s}{\cos(\pi/6)} = \frac{200}{0.8660} \approx 230.94 \text{ rad/s}
$$

En $\Omega = 230.94\text{ rad/s}$, la gráfica de magnitud del filtro Chebyshev Tipo 2 cae exactamente a **cero** ($-\infty\text{ dB}$).

---

##### Ej. 2 (Mayor dificultad): Comparación directa de atenuación en la banda de transición
Considere dos filtros pasa-bajo de orden $N = 4$, uno Chebyshev Tipo 1 y otro Butterworth, ambos con frecuencia de corte/banda de paso $\Omega_p = 1000\text{ rad/s}$ y rizo de $1\text{ dB}$ ($\epsilon = 0.5088$). Calcular y comparar el valor de atenuación en decibelios en una frecuencia de la banda de transición $\Omega = 1200\text{ rad/s}$ a partir de sus curvas de respuesta.

**Resolución:**

**1. Evaluación del filtro Chebyshev Tipo 1:**
Para $N = 4$, el polinomio de Chebyshev es:

$$
T_4(x) = 8x^4 - 8x^2 + 1
$$

Evaluando en la frecuencia normalizada $x = \frac{1200}{1000} = 1.2$:

$$
T_4(1.2) = 8(1.2)^4 - 8(1.2)^2 + 1 = 8(2.0736) - 8(1.44) + 1 = 16.5888 - 11.52 + 1 = 6.0688
$$

Sustituyendo en la función de magnitud al cuadrado:

$$
|H_I(j1200)|^2 = \frac{1}{1 + \epsilon^2 T_4^2(1.2)} = \frac{1}{1 + (0.5088)^2 (6.0688)^2} = \frac{1}{1 + (0.25888)(36.8303)} = \frac{1}{1 + 9.5346} = \frac{1}{10.5346} \approx 0.09492
$$

Convertimos a atenuación en dB:

$$
\alpha_I(1200) = -10 \log_{10}(|H_I(j1200)|^2) = -10 \log_{10}(0.09492) \approx 10.23 \text{ dB}
$$


**2. Evaluación del filtro Butterworth de igual especificación ($1\text{ dB}$ en $\Omega_p$):**
La frecuencia de corte a $-3\text{ dB}$ $\Omega_c$ para el Butterworth se ajusta como:

$$
\Omega_c = \frac{\Omega_p}{\epsilon^{1/N}} = \frac{1000}{(0.5088)^{1/4}} = \frac{1000}{0.8444} \approx 1184.28 \text{ rad/s}
$$

Evaluando en $\Omega = 1200\text{ rad/s}$:

$$
|H_B(j1200)|^2 = \frac{1}{1 + \left(\frac{1200}{1184.28}\right)^8} = \frac{1}{1 + (1.01327)^8} = \frac{1}{1 + 1.1111} = \frac{1}{2.1111} \approx 0.47368
$$

Convertimos a atenuación en dB:

$$
\alpha_B(1200) = -10 \log_{10}(|H_B(j1200)|^2) = -10 \log_{10}(0.47368) \approx 3.25 \text{ dB}
$$


**Conclusión:**  
En la frecuencia $\Omega = 1200\text{ rad/s}$, apenas un $20\%$ por encima de la banda de paso, la curva del filtro Chebyshev Tipo 1 alcanza una atenuación de **$10.23\text{ dB}$** frente a solo **$3.25\text{ dB}$** del filtro Butterworth, demostrando la pendiente de caída sustancialmente mayor que caracteriza a las gráficas de Chebyshev.
