

### **Enunciado**

Calcular analíticamente la DFT de $N$ puntos de las siguientes secuencias para $N = 5$, $N = 10$ y $N = 50$:

*   **Señal a:** $x(n) = [1, \quad 1, \quad 1, \quad 1, \quad 1]$ para $n = 0 \dots 4$
*   **Señal b:** $x(n) = (0.5)^n$ para $n = 0 \dots 4$ (es decir, $x(n) = [1, \quad 0.5, \quad 0.25, \quad 0.125, \quad 0.0625]$)

Para cada caso, aplicar la definición de la DFT y describir el efecto del zero-padding en el muestreo de la DTFT.

---

### **Desarrollo Analítico de la Señal a**

La señal $x(n)$ tiene una longitud de soporte real de $L = 5$. Al aplicar un zero-padding para un tamaño $N \ge 5$, extendemos la secuencia agregando muestras nulas:
*   Para $N = 5$: No se agregan ceros.
*   Para $N = 10$: Se agregan $10 - 5 = 5$ ceros en el intervalo $n = 5 \dots 9$.
*   Para $N = 50$: Se agregan $50 - 5 = 45$ ceros en el intervalo $n = 5 \dots 49$.

La definición de la DFT de $N$ puntos para esta secuencia con soporte en $0 \le n \le 4$ es:

$$
X[k] = \sum_{n=0}^{N-1} x(n) e^{-j\frac{2\pi}{N}kn} = \sum_{n=0}^{4} (1) \cdot e^{-j\frac{2\pi}{N}kn}
$$


Esta expresión corresponde a una serie geométrica finita de 5 términos con razón $q = e^{-j\frac{2\pi}{N}k}$. 

*   Para el componente de DC ($k = 0$):
    
$$
X = \sum_{n=0}^{4} 1 = 5
$$

*   Para $k \neq 0$ (donde $q \neq 1$), aplicamos la suma de una serie geométrica finita $\sum_{n=0}^{M-1} q^n = \frac{1-q^M}{1-q}$:
    
$$
X[k] = \frac{1 - e^{-j\frac{10\pi}{N}k}}{1 - e^{-j\frac{2\pi}{N}k}}
$$


Para simplificar a su forma trigonométrica cerrada, factorizamos los términos de fase media tanto en el numerador como en el denominador:

$$
X[k] = \frac{e^{-j\frac{5\pi}{N}k} \left(e^{j\frac{5\pi}{N}k} - e^{-j\frac{5\pi}{N}k}\right)}{e^{-j\frac{\pi}{N}k} \left(e^{j\frac{\pi}{N}k} - e^{-j\frac{\pi}{N}k}\right)}
$$


Aplicando la relación de Euler, la **forma cerrada general** es:

$$
\mathbf{X[k] = e^{-j\frac{4\pi}{N}k} \frac{\sin\left(\frac{5\pi k}{N}\right)}{\sin\left(\frac{\pi k}{N}\right)}}
$$


---

#### **1. Caso $N = 5$**
Sustituyendo $N = 5$ en la forma cerrada para $k = 1, 2, 3, 4$:

$$
X[k] = e^{-j\frac{4\pi}{5}k} \frac{\sin(\pi k)}{\sin\left(\frac{\pi k}{5}\right)}
$$

Dado que $\sin(\pi k) = 0$ para cualquier entero $k$ y el denominador $\sin\left(\frac{\pi k}{5}\right) \neq 0$ en este rango:

$$
X[k] = 0 \quad \text{para } k = 1, 2, 3, 4
$$


*   **Resultado $N = 5$:**
    
$$
\mathbf{X[k] = [5, \quad 0, \quad 0, \quad 0, \quad 0]}
$$


---

#### **2. Caso $N = 10$**
Sustituyendo $N = 10$ en la forma cerrada para $k = 0 \dots 9$:

$$
X[k] = e^{-j\frac{2\pi}{5}k} \frac{\sin\left(\frac{\pi k}{2}\right)}{\sin\left(\frac{\pi k}{10}\right)}
$$

*   Para valores pares de $k$ ($k = 2, 4, 6, 8$), el numerador se anula: $\sin(\pi, 2\pi, 3\pi, 4\pi) = 0$, por lo que $X[k] = 0$.
*   Para valores impares de $k$:
    *   $k = 1$: $X = e^{-j72^\circ} \frac{\sin(90^\circ)}{\sin(18^\circ)} = \frac{1}{0.3090} e^{-j72^\circ} \approx 3.2361 e^{-j72^\circ} = 1 - j3.0777$
    *   $k = 3$: $X = e^{-j216^\circ} \frac{\sin(270^\circ)}{\sin(54^\circ)} = \frac{-1}{0.8090} e^{-j216^\circ} = 1.2361 e^{-j36^\circ} = 1 - j0.7265$
    *   $k = 5$: $X = e^{-j360^\circ} \frac{\sin(450^\circ)}{\sin(90^\circ)} = 1 \cdot \frac{1}{1} = 1$
    *   $k = 7$: Por simetría conjugada de secuencias reales, $X = X^* \approx 1 + j0.7265$.
    *   $k = 9$: Por simetría conjugada de secuencias reales, $X = X^* \approx 1 + j3.0777$.

*   **Resultado $N = 10$:**
    
$$
\mathbf{X[k] = [5, \quad 1-j3.0777, \quad 0, \quad 1-j0.7265, \quad 0, \quad 1, \quad 0, \quad 1+j0.7265, \quad 0, \quad 1+j3.0777]}
$$


---

#### **3. Caso $N = 50$**
Sustituyendo $N = 50$ en la expresión de forma cerrada:

$$
X[k] = e^{-j\frac{2\pi}{25}k} \frac{\sin\left(\frac{\pi k}{10}\right)}{\sin\left(\frac{\pi k}{50}\right)}
$$

Los $N = 50$ valores discretos corresponden a muestras espaciadas a intervalos de $\Delta\omega = \frac{2\pi}{50}$ rad. Los primeros coeficientes son:
*   $X = 5$
*   $X \approx 4.7668 - j1.2239$
*   $X \approx 4.1097 - j2.2593$
*   $X \approx 3.1473 - j2.9555$
*   $X \approx 2.0491 - j3.2289$
*   $X \approx 1 - j3.0777$ (coincide con $X$ del caso $N=10$ debido al submuestreo de la malla)

---

### **Desarrollo Analítico de la Señal b**

La secuencia dada es $x(n) = [1, \quad 0.5, \quad 0.25, \quad 0.125, \quad 0.0625]$ para $n = 0 \dots 4$. Al aplicar definición de la DFT para $N \ge 5$:

$$
X[k] = \sum_{n=0}^{4} (0.5)^n e^{-j\frac{2\pi}{N}kn} = \sum_{n=0}^{4} \left(0.5 e^{-j\frac{2\pi}{N}k}\right)^n
$$


Esta expresión representa una serie geométrica finita de 5 términos con razón $q = 0.5 e^{-j\frac{2\pi}{N}k}$. Aplicando la fórmula de suma geométrica:

$$
\mathbf{X[k] = \frac{1 - \left(0.5 e^{-j\frac{2\pi}{N}k}\right)^5}{1 - 0.5 e^{-j\frac{2\pi}{N}k}} = \frac{1 - \frac{1}{32}e^{-j\frac{10\pi}{N}k}}{1 - 0.5 e^{-j\frac{2\pi}{N}k}}}
$$


---

#### **1. Caso $N = 5$**
Sustituyendo $N = 5$ en la forma cerrada general:

$$
X[k] = \frac{1 - \frac{1}{32}e^{-j2\pi k}}{1 - 0.5 e^{-j\frac{2\pi}{5}k}} = \frac{\frac{31}{32}}{1 - 0.5 e^{-j\frac{2\pi}{5}k}} = \frac{31}{32 - 16 e^{-j\frac{2\pi}{5}k}}
$$

Evaluamos numéricamente para cada índice $k = 0 \dots 4$:
*   $k = 0$: $X = \frac{31}{32 - 16} = \frac{31}{16} = 1.9375$
*   $k = 1$: $X = \frac{31}{32 - 16 e^{-j72^\circ}} \approx 0.8704 - j0.4896$
*   $k = 2$: $X = \frac{31}{32 - 16 e^{-j144^\circ}} \approx 0.6608 - j0.1383$
*   $k = 3$: Por simetría conjugada, $X = X^* \approx 0.6608 + j0.1383$.
*   $k = 4$: Por simetría conjugada, $X = X^* \approx 0.8704 + j0.4896$.

*   **Resultado $N = 5$:**
    
$$
\mathbf{X[k] = [1.9375, \quad 0.8704 - j0.4896, \quad 0.6608 - j0.1383, \quad 0.6608 + j0.1383, \quad 0.8704 + j0.4896]}
$$


---

#### **2. Caso $N = 10$**
Sustituyendo $N = 10$ en la forma cerrada general:

$$
X[k] = \frac{1 - \frac{1}{32}e^{-j\pi k}}{1 - 0.5 e^{-j\frac{\pi}{5}k}}
$$

El numerador depende de la paridad de $k$ debido a que $e^{-j\pi k} = (-1)^k$:

$$
X[k] = \begin{cases} \frac{31}{32 - 16 e^{-j\frac{\pi}{5}k}}, & k \text{ par} \\ \frac{33}{32 - 16 e^{-j\frac{\pi}{5}k}}, & k \text{ impar} \end{cases}
$$

Evaluamos analíticamente para cada componente:
*   $k = 0$ (par): $X = 1.9375$
*   $k = 1$ (impar): $X = \frac{33}{32 - 16 e^{-j36^\circ}} \approx 1.3926 - j0.6873$
*   $k = 2$ (par): $X = \frac{31}{32 - 16 e^{-j72^\circ}} \approx 0.8704 - j0.4896$ (coincide con $X$ de $N=5$)
*   $k = 3$ (impar): $X = \frac{33}{32 - 16 e^{-j108^\circ}} \approx 0.7637 - j0.3145$
*   $k = 4$ (par): $X = \frac{31}{32 - 16 e^{-j144^\circ}} \approx 0.6608 - j0.1383$ (coincide con $X$ de $N=5$)
*   $k = 5$ (impar): $X = \frac{33}{32 - 16 e^{-j180^\circ}} = \frac{33}{48} = 0.6875$
*   Muestras de $k = 6 \dots 9$: Obtenidas mediante simetría conjugada $X[N-k] = X^*[k]$.

*   **Resultado $N = 10$:**
    
$$
\mathbf{X[k] = [1.9375, \, 1.3926-j0.6873, \, 0.8704-j0.4896, \, 0.7637-j0.3145, \, 0.6608-j0.1383, \, 0.6875, \, \text{simétricos}]}
$$


---

#### **3. Caso $N = 50$**
Sustituyendo $N = 50$ en la forma cerrada general:

$$
X[k] = \frac{1 - \frac{1}{32}e^{-j\frac{\pi}{5}k}}{1 - 0.5 e^{-j\frac{\pi}{25}k}}
$$

Los primeros valores para $k = 0 \dots 5$ son:
*   $X = 1.9375$
*   $X \approx 1.9092 - j0.2010$
*   $X \approx 1.8280 - j0.3831$
*   $X \approx 1.7043 - j0.5307$
*   $X \approx 1.5533 - j0.6333$
*   $X \approx 1.3926 - j0.6873$ (coincide con $X$ del caso $N=10$)

---

### **Visualización del Espectro Continuo $DTFT$**

La envolvente espectral continua de magnitud para ambas señales de tiempo finito se grafica a continuación en el rango $[-\pi, \pi]$:

```desmos-graph
left=-3.14; right=3.14; bottom=-1; top=6;
width=550; height=200;
---
y = \abs(\sin(2.5x)/\sin(0.5x))
y = (1 + 1/1024 - (1/16)\cos(5x))^{1/2} / (1.25 - \cos(x))^{1/2}
```

---

### **Efecto del Zero-Padding en la Resolución**

1.  **Resolución Espectral Física (Invariable):** La resolución espectral real del sistema está estrictamente limitada por la ventana temporal de los datos originales ($L = 5$). Realizar zero-padding agregando muestras nulas **no añade información física nueva** ni permite separar físicamente dos componentes senoidales adyacentes que no fuesen ya separables con las 5 muestras iniciales.
2.  **Densidad de Muestreo Espectral (Mejorada):** Al incrementar el número de puntos de $N = 5$ a $N = 10$ y $N = 50$, la rejilla de muestreo en frecuencia se vuelve más densa, reduciendo el espaciamiento a $\Delta\omega = \frac{2\pi}{N}$. Esto actúa como una **interpolación ideal en el dominio de la frecuencia** (reconstrucción mediante núcleo de Dirichlet), permitiendo visualizar con gran precisión la envolvente continua de la DTFT y revelando picos o valles que de otro modo quedarían ocultos en una rejilla gruesa.
