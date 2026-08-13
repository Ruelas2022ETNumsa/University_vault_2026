# E1. Classify the following continuous-time signals as periodic or aperiodic. If periodic, determine the period. 

i) $x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)$
ii) $x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)$
iii) $x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)$
iv) $x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)$
v) $x(t) = e^{j(4t+\tfrac{\pi}{5})}$
vi) $x(t) = \cos\left(2t + \frac{\pi}{4}\right)$
vii) $x(t) = \cos(2\pi t)u(t)$
viii) $x(t) = \cos^2(t)$

---

### i) $x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)$

$$T_1 = \frac{2\pi}{2\pi/3} = 3 \text{ s}, \quad T_2 = \frac{2\pi}{\pi/2} = 4 \text{ s}$$

$$\frac{T_1}{T_2} = \frac{3}{4} \in \mathbb{Q} \implies \text{Periódica}$$

$$T_0 = \text{MCM}(3,4) = 12 \text{ s}$$

---

### ii) $x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)$

$$T_1 = \frac{2\pi}{2\pi} = 1 \text{ s}, \quad T_2 = \frac{2\pi}{\sqrt{2}\pi} = \sqrt{2} \text{ s}$$

$$\frac{T_1}{T_2} = \frac{1}{\sqrt{2}} \notin \mathbb{Q} \implies \textbf{Aperiódica}$$

---

### iii) $x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)$

La constante no afecta la periodicidad. Para $-\frac{1}{2}\cos(2t)$ con $\omega = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$

---

### iv) $x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)$

La constante no afecta la periodicidad.

$$T_1 = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s}, \quad T_2 = \frac{2\pi}{6} = \frac{\pi}{3} \text{ s}$$

$$\frac{T_1}{T_2} = \frac{3}{2} \in \mathbb{Q} \implies \text{Periódica}$$

$$T_0 = 2T_1 = 3T_2 = \pi \text{ s}$$

---

### v) $x(t) = e^{j\left(4t + \frac{\pi}{5}\right)}$

Exponencial compleja con $\omega_0 = 4$ rad/s, siempre periódica:

$$T_0 = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s} \implies \text{Periódica}$$

---

### vi) $x(t) = \cos\left(2t + \frac{\pi}{4}\right)$

$\omega_0 = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$

---

### vii) $x(t) = \cos(2\pi t)u(t)$

$$x(t) = \begin{cases} \cos(2\pi t) & t \ge 0 \\ 0 & t < 0 \end{cases}$$

La señal vale $0$ para $t < 0$, por lo que no existe $T > 0$ tal que $x(t+T) = x(t)$ para todo $t$.

$$\implies \textbf{Aperiódica}$$

---

### viii) $x(t) = \cos^2(t)$

Por identidad trigonométrica:

$$\cos^2(t) = \frac{1}{2} + \frac{1}{2}\cos(2t)$$

$\omega_0 = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$




---
---


# E2. A periodic signal $x_1(t)$ has a period $2$, and another periodic signal $x_2(t)$ has a period $3$. Find the fundamental frequency and period for the signal $y(t) = x_1(t) + x_2(t)$.

---

Para determinar el periodo fundamental y la frecuencia fundamental de la señal combinada $y(t) = x_1(t) + x_2(t)$, se sigue un procedimiento matemático estándar para la suma de señales periódicas:

### **1. Verificación de la periodicidad**

La suma de dos señales periódicas continuas es periódica si y solo si la relación de sus periodos individuales es un número racional. A partir de los datos del problema, tenemos:

- Periodo de $x_1(t)$: $T_1 = 2$
- Periodo de $x_2(t)$: $T_2 = 3$

Evaluamos la relación de ambos periodos:

$$\frac{T_1}{T_2} = \frac{2}{3}$$

Como el resultado ($\frac{2}{3}$) es un **número racional**, confirmamos que la señal combinada $y(t)$ es **periódica**.

---

### **2. Cálculo del periodo fundamental ($T_0$)**

De acuerdo con la propiedad de combinación de señales, la relación de los periodos se puede expresar como:

$$\frac{T_1}{T_2} = \frac{k}{m} = \frac{2}{3}$$

Donde elegimos los enteros $k = 2$ y $m = 3$ de modo que no tengan factores comunes (su máximo común divisor es 1). El periodo fundamental ($T_0$) de la suma de las señales se calcula como:

$$T_0 = m T_1 = k T_2 = 3(2) = 2(3) = 6\text{ s}$$

Por lo tanto, el **periodo fundamental** de la señal es **$T_0 = 6$ segundos**.

---

### **3. Cálculo de la frecuencia fundamental**

En el análisis de señales, la frecuencia fundamental suele expresarse en dos unidades distintas:

- **Frecuencia fundamental cíclica ($f_0$) en Hertz (Hz):**

$$f_0 = \frac{1}{T_0} = \frac{1}{6}\text{ Hz} \approx 0.167\text{ Hz}$$

- **Frecuencia angular fundamental ($\omega_0$) en radianes por segundo (rad/s):**

$$\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{6} = \frac{\pi}{3}\text{ rad/s} \approx 1.047\text{ rad/s}$$

---

### **Resumen de Resultados:**

- **Periodo fundamental ($T_0$):** **$6$ s**
- **Frecuencia fundamental ($f_0$):** **$\frac{1}{6}$ Hz**
- **Frecuencia angular fundamental ($\omega_0$):** **$\frac{\pi}{3}$ rad/s**

---
---

# E3.  Clasificación de señales de tiempo continuo

Clasifique las siguientes señales de tiempo continuo como **señales pares, impares o ninguna de las dos**. Determine la **potencia** y la **energía** para cada caso de señal de potencia o de energía.

1. $x(t)=(1+t^2)\cos^2(5t)$
    
2. $x(t)=u(t)$
    
3. $x(t)=tu(t)$
    
4. $x(t)=t\sin(2t)$
    
5. $x(t)=t+\cos(2t)$
    
6. $x(t)=e^{-2t}\sin(2t)$

---

Para clasificar estas señales de tiempo continuo en **pares, impares o ninguna de las dos**, y determinar su **energía ($E$)** y **potencia ($P$)**, utilizaremos las definiciones matemáticas fundamentales:

- **Señal Par:** Cumple con la propiedad de simetría respecto al eje vertical, es decir, $x(-t) = x(t)$ para todo $t$.
- **Señal Impar:** Cumple con la propiedad de simetría respecto al origen, es decir, $x(-t) = -x(t)$ para todo $t$.
- **Energía Total ($E$):** Se define como:

$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

- **Potencia Promedio ($P$):** Se define como:

$$P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt$$

- **Clasificación de energía o potencia:**
    - Una **señal de energía** tiene energía finita y potencia promedio igual a cero ($0 < E < \infty$ y $P = 0$).
    - Una **señal de potencia** tiene potencia promedio finita y energía infinita ($0 < P < \infty$ y $E = \infty$).
    - Si tanto $E$ como $P$ resultan infinitos, la señal se clasifica como **ninguna de las dos** (ni de energía ni de potencia).

A continuación, se detalla la resolución para cada una de las señales presentadas:

---

### **1. $x(t) = (1+t^2)\cos^2(5t)$**

- **Clasificación de simetría:** **Señal Par**
    
    - **Demostración:** Evaluamos $x(-t)$ sustituyendo $t$ por $-t$:

$$x(-t) = (1 + (-t)^2)\cos^2(5(-t))$$

Dado que $(-t)^2 = t^2$ y que el coseno es una función par ($\cos(-\theta) = \cos(\theta)$), obtenemos:

$$x(-t) = (1+t^2)\cos^2(5t) = x(t)$$

Por lo tanto, la señal es simétrica y es **par**.

- **Energía y Potencia:**
    
    - A medida que $t \to \pm\infty$, el término polinómico $(1+t^2)$ crece de forma ilimitada, lo que causa que la amplitud de la señal tienda al infinito.
    - La integral de la energía diverge debido a este crecimiento: **$E = \infty$**.
    - De igual forma, el valor cuadrático medio en el tiempo no se estabiliza en un valor finito y crece continuamente hacia el infinito: **$P = \infty$**.
    - **Clasificación:** **Ninguna de las dos** (no es señal de energía ni de potencia).

---

### **2. $x(t) = u(t)$ (Escalón unitario)**

- **Clasificación de simetría:** **Ninguna de las dos**
    
    - **Demostración:** La función escalón unitario vale $1$ para $t > 0$ y $0$ para $t < 0$. Su versión invertida en el tiempo, $x(-t) = u(-t)$, vale $1$ para $t < 0$ y $0$ para $t > 0$.
    - Dado que $u(-t) \neq u(t)$ y $u(-t) \neq -u(t)$, la señal no tiene simetría par ni impar.

- **Energía y Potencia:**
    
    - **Energía ($E$):**

$$E = \int_{-\infty}^{\infty} |u(t)|^2 dt = \int_{0}^{\infty} (1)^2 dt = [t]_0^{\infty} = \infty$$

Por lo tanto, la energía es infinita: **$E = \infty$**.

- **Potencia ($P$):**

$$P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |u(t)|^2 dt = \lim_{T \to \infty} \frac{1}{2T} \int_{0}^{T} (1)^2 dt = \lim_{T \to \infty} \frac{T}{2T} = \frac{1}{2} = 0.5 \text{ W}$$

Por lo tanto, la potencia promedio es finita: **$P = 0.5 \text{ W}$**.

- **Clasificación:** Es una **señal de potencia** (potencia finita y energía infinita).

---

### **3. $x(t) = tu(t)$ (Función rampa unitaria)**

- **Clasificación de simetría:** **Ninguna de las dos**
    
    - **Demostración:** La función rampa unitaria $r(t) = tu(t)$ vale $t$ para $t > 0$ y $0$ para $t < 0$. Su versión invertida $x(-t) = -t u(-t)$ vale $-t$ para $t < 0$ y $0$ para $t > 0$.
    - Como no se cumple la igualdad con $x(t)$ ni con $-x(t)$, no posee simetría.

- **Energía y Potencia:**
    
    - **Energía ($E$):**

$$E = \int_{0}^{\infty} t^2 dt = \left[ \frac{t^3}{3} \right]_0^{\infty} = \infty$$

Por lo tanto, la energía es infinita: **$E = \infty$**.

- **Potencia ($P$):**

$$P = \lim_{T \to \infty} \frac{1}{2T} \int_{0}^{T} t^2 dt = \lim_{T \to \infty} \frac{T^2}{6} = \infty$$

Por lo tanto, la potencia promedio es infinita: **$P = \infty$**.

- **Clasificación:** **Ninguna de las dos** (no es señal de energía ni de potencia).

---

### **4. $x(t) = t\sin(2t)$**

- **Clasificación de simetría:** **Señal Par**
    
    - **Demostración:** Reemplazamos $t$ por $-t$:

$$x(-t) = (-t)\sin(2(-t))$$

Sabiendo que el seno es una función impar ($\sin(-\theta) = -\sin(\theta)$):

$$x(-t) = (-t)(-\sin(2t)) = t\sin(2t) = x(t)$$

Dado que $x(-t) = x(t)$, la señal es **par**.

- **Energía y Potencia:**
    
    - La oscilación sinusoidal de la señal se multiplica por un factor $t$ que crece indefinidamente a medida que $t \to \pm\infty$.
    - Esto causa que tanto la integral para calcular la energía total como el límite para calcular la potencia promedio diverjan hacia el infinito.
    - **Resultados:** **$E = \infty$** y **$P = \infty$**.
    - **Clasificación:** **Ninguna de las dos**.

---

### **5. $x(t) = t+\cos(2t)$**

- **Clasificación de simetría:** **Ninguna de las dos**
    
    - **Demostración:** La señal está compuesta por la suma de un término impar ($t$) y un término par ($\cos(2t)$). La suma de una función par y una impar no posee simetría par ni impar.

$$x(-t) = -t + \cos(-2t) = -t + \cos(2t) \neq x(t) \text{ y } \neq -x(t)$$

- **Energía y Potencia:**
    
    - Al igual que en los casos de crecimiento lineal, la presencia del término $t$ provoca que la amplitud de la señal tienda al infinito a medida que el tiempo avanza.
    - Por consiguiente, la energía y la potencia promedio son infinitas.
    - **Resultados:** **$E = \infty$** y **$P = \infty$**.
    - **Clasificación:** **Ninguna de las dos**.

---

### **6. $x(t) = e^{-2t}\sin(2t)$**

- **Clasificación de simetría:** **Ninguna de las dos**
    
    - **Demostración:** Sustituimos $t$ por $-t$:

$$x(-t) = e^{-2(-t)}\sin(2(-t)) = -e^{2t}\sin(2t)$$

Como este resultado no es idéntico a $x(t)$ ni a $-x(t)$, no posee simetría par ni impar.

- **Energía y Potencia:**
    
    - Dado que la señal está definida para todo el eje temporal ($-\infty < t < \infty$), cuando evaluamos el límite en los tiempos negativos ($t \to -\infty$), el término exponencial $e^{-2t}$ crece exponencialmente hacia el infinito.
    - Debido a este crecimiento exponencial desmedido en el lado izquierdo del eje del tiempo, tanto la energía total como la potencia integrada divergen.
    - **Resultados:** **$E = \infty$** y **$P = \infty$**.
    - **Clasificación:** **Ninguna de las dos**.
    - _(Nota: Si esta señal hubiera estado multiplicada por un escalón unitario, $u(t)$, para limitar su dominio a los tiempos positivos, habría decaído a cero y se habría clasificado como una señal de energía con valores finitos; sin embargo, al ser una señal bilateral de extensión infinita, diverge)._

---
---

# E4. Considere la siguiente señal de tiempo continuo:

$$
x(t) = 2\sin\left(\frac{2\pi(t-T)}{10}\right)
$$

Determine los valores de $T$ para los cuales la señal es:

1. Una función **par**.
2. Una función **impar**.

---

Para resolver este problema, analizamos la señal de tiempo continuo dada:

$$x(t) = 2\sin\left(\frac{2\pi(t-T)}{10}\right) = 2\sin\left(\frac{\pi}{5}(t-T)\right) = 2\sin\left(\frac{\pi}{5}t - \frac{\pi}{5}T\right)$$

Por definición, las propiedades de simetría temporal para señales continuas son las siguientes:

1. Una señal es **par** si cumple con: $x(-t) = x(t)$.
2. Una señal es **impar** si cumple con: $x(-t) = -x(t)$.

Evaluemos primero la señal invertida en el tiempo, $x(-t)$:

$$x(-t) = 2\sin\left(\frac{\pi}{5}(-t) - \frac{\pi}{5}T\right) = 2\sin\left(-\left[\frac{\pi}{5}t + \frac{\pi}{5}T\right]\right)$$

Dado que la función seno es una función impar por naturaleza ($\sin(-\theta) = -\sin(\theta)$), tenemos:

$$x(-t) = -2\sin\left(\frac{\pi}{5}t + \frac{\pi}{5}T\right)$$

---

### **1. Condición para que sea una función par**

Para que $x(t)$ sea una función par, se debe cumplir la igualdad para todo $t$:

$$x(-t) = x(t) \implies -2\sin\left(\frac{\pi}{5}t + \frac{\pi}{5}T\right) = 2\sin\left(\frac{\pi}{5}t - \frac{\pi}{5}T\right)$$

Dividiendo entre $2$ y reordenando la ecuación:

$$\sin\left(\frac{\pi}{5}t - \frac{\pi}{5}T\right) + \sin\left(\frac{\pi}{5}t + \frac{\pi}{5}T\right) = 0$$

Utilizando la identidad trigonométrica de la suma de senos ($\sin(A+B) + \sin(A-B) = 2\sin(A)\cos(B)$), donde $A = \frac{\pi}{5}t$ y $B = \frac{\pi}{5}T$:

$$2\sin\left(\frac{\pi}{5}t\right)\cos\left(\frac{\pi}{5}T\right) = 0$$

Para que esta ecuación se cumpla para cualquier valor de $t$, el término constante debe ser cero:

$$\cos\left(\frac{\pi}{5}T\right) = 0$$

La función coseno se anula en los múltiplos impares de $\pi/2$:

$$\frac{\pi}{5}T = (2k + 1)\frac{\pi}{2} \quad \text{para cualquier entero } k \in \mathbb{Z}$$

Despejando $T$:

$$T = \frac{5}{2}(2k + 1) = 5k + 2.5 \quad \text{para } k \in \mathbb{Z}$$

- **Respuesta (Par):** La señal es una función **par** para todos los valores de $T = 5k + 2.5$ con $k \in \mathbb{Z}$ (es decir, $T = \pm 2.5, \pm 7.5, \pm 12.5, \dots$).
- _Verificación:_ Si elegimos $T = 2.5$, la señal se convierte en $2\sin\left(\frac{\pi}{5}t - \frac{\pi}{2}\right) = -2\cos\left(\frac{\pi}{5}t\right)$, la cual es claramente una función par.

---

### **2. Condición para que sea una función impar**

Para que $x(t)$ sea una función impar, se debe cumplir la igualdad para todo $t$:

$$x(-t) = -x(t) \implies -2\sin\left(\frac{\pi}{5}t + \frac{\pi}{5}T\right) = -2\sin\left(\frac{\pi}{5}t - \frac{\pi}{5}T\right)$$

Dividiendo entre $-2$ y reordenando la ecuación:

$$\sin\left(\frac{\pi}{5}t + \frac{\pi}{5}T\right) - \sin\left(\frac{\pi}{5}t - \frac{\pi}{5}T\right) = 0$$

Utilizando la identidad trigonométrica de la diferencia de senos ($\sin(A+B) - \sin(A-B) = 2\cos(A)\sin(B)$), donde $A = \frac{\pi}{5}t$ y $B = \frac{\pi}{5}T$:

$$2\cos\left(\frac{\pi}{5}t\right)\sin\left(\frac{\pi}{5}T\right) = 0$$

Para que esta ecuación se cumpla para cualquier valor de $t$, el término constante debe ser cero:

$$\sin\left(\frac{\pi}{5}T\right) = 0$$

La función seno se anula en los múltiplos enteros de $\pi$:

$$\frac{\pi}{5}T = k\pi \quad \text{para cualquier entero } k \in \mathbb{Z}$$

Despejando $T$:

$$T = 5k \quad \text{para } k \in \mathbb{Z}$$

- **Respuesta (Impar):** La señal es una función **impar** para todos los valores de $T = 5k$ con $k \in \mathbb{Z}$ (es decir, $T = 0, \pm 5, \pm 10, \dots$).
- _Verificación:_ Si elegimos $T = 5$, la señal se convierte en $2\sin\left(\frac{\pi}{5}t - \pi\right) = -2\sin\left(\frac{\pi}{5}t\right)$, la cual es claramente una función impar.
