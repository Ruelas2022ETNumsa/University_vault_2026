### Análisis de Periodicidad en Tiempo Continuo

---

#### **Señal 1:** $x(t) = 5\cos[2\pi(15)t + 0.25\pi]$

##### **1. Análisis de periodicidad**
Una señal senoidal en tiempo continuo de la forma estándar:

$$
x(t) = A\cos(\omega_0 t + \phi)
$$

es **siempre periódica** para cualquier frecuencia angular $\omega_0 \neq 0$. 

##### **2. Cálculo del período fundamental $T_0$**
Identificamos los parámetros de la señal:
*   Amplitud: $A = 5$
*   Frecuencia angular: $\omega_0 = 2\pi(15) = 30\pi \text{ rad/s}$
*   Fase: $\phi = 0.25\pi \text{ rad}$

El período fundamental $T_0$ de una sinusoide continua es el menor intervalo temporal positivo en el que la señal se repite, definido por:

$$
T_0 = \frac{2\pi}{\omega_0}
$$


Sustituyendo $\omega_0$:

$$
T_0 = \frac{2\pi}{30\pi} = \frac{1}{15} \text{ s} \approx 0.0667 \text{ s}
$$


*   **Resultado 1:** La señal es **periódica** con un período fundamental **$T_0 = \frac{1}{15} \text{ s}$**.

---

#### **Señal 2:** $x(t) = 5\cos[2\pi(15)t + 0.25\pi] + 5\cos[2\pi(10)t + 0.3\pi]$

##### **1. Análisis de los componentes individuales**
La señal se compone de la suma de dos señales senoidales:

$$
x(t) = y_1(t) + y_2(t)
$$


*   **Primer componente:** $y_1(t) = 5\cos[2\pi(15)t + 0.25\pi]$
    *   Frecuencia angular: $\omega_1 = 30\pi \text{ rad/s}$
    *   Período fundamental individual: $T_1 = \frac{2\pi}{30\pi} = \frac{1}{15} \text{ s}$

*   **Segundo componente:** $y_2(t) = 5\cos[2\pi(10)t + 0.3\pi]$
    *   Frecuencia angular: $\omega_2 = 2\pi(10) = 20\pi \text{ rad/s}$
    *   Período fundamental individual: $T_2 = \frac{2\pi}{20\pi} = \frac{1}{10} \text{ s}$

##### **2. Aplicación del criterio de periodicidad para suma de sinusoides**
La combinación lineal de dos señales continuas periódicas es periódica si y solo si el cociente de sus períodos fundamentales individuales es un número racional:

$$
\frac{T_1}{T_2} \in \mathbb{Q}
$$


Evaluamos la relación de períodos:

$$
\frac{T_1}{T_2} = \frac{\frac{1}{15}}{\frac{1}{10}} = \frac{10}{15} = \frac{2}{3}
$$


Como $\frac{2}{3}$ es un número racional (expresado como la relación de dos números enteros), la señal compuesta $x(t)$ **es periódica**.

##### **3. Cálculo del período fundamental de la suma $T_0$**
La relación de los períodos se expresa de forma simplificada en términos de enteros primos entre sí ($\gcd(k_1, k_2) = 1$):

$$
\frac{T_1}{T_2} = \frac{k_2}{k_1} = \frac{2}{3} \implies k_1 = 3, \quad k_2 = 2
$$


El período fundamental $T_0$ de la señal suma es el mínimo común múltiplo $MCM$ de los períodos individuales, el cual se calcula multiplicando de forma cruzada por los coeficientes enteros determinados:

$$
T_0 = k_1 T_1 = k_2 T_2
$$


Sustituyendo los valores:

$$
T_0 = 3 \cdot \left(\frac{1}{15} \text{ s}\right) = \frac{3}{15} \text{ s} = \frac{1}{5} \text{ s} = 0.2 \text{ s}
$$


$$
T_0 = 2 \cdot \left(\frac{1}{10} \text{ s}\right) = \frac{2}{10} \text{ s} = \frac{1}{5} \text{ s} = 0.2 \text{ s}
$$


Ambos caminos confirman de manera consistente el período fundamental del sistema compuesto.

*   **Resultado 2:** La señal es **periódica** con un período fundamental **$T_0 = \frac{1}{5} \text{ s} = 0.2 \text{ s}$**.

---

#### **Visualización temporal (Señal 2)**

```desmos-graph
left=-0.1; right=0.5; bottom=-11; top=11;
width=600; height=200;
---
y = 5\cos(30\pi x + 0.25\pi) + 5\cos(20\pi x + 0.3\pi)
```


