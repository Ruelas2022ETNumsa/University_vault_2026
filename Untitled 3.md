## Clasificación de señales de tiempo continuo

Clasifique las siguientes señales de tiempo continuo como **señales pares, impares o ninguna de las dos**. Determine la **potencia** y la **energía** para cada caso de señal de potencia o de energía.

1. $$x(t)=(1+t^2)\cos^2(5t)$$
    
2. $$x(t)=u(t)$$
    
3. $$x(t)=tu(t)$$
    
4. $$x(t)=t\sin(2t)$$
    
5. $$x(t)=t+\cos(2t)$$
    
6. $$x(t)=e^{-2t}\sin(2t)$$


----
respuesta e notebooklm

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

📊 Si lo deseas, podemos proponer un script en Python para graficar alguna de estas señales y que de este modo puedas visualizar de manera intuitiva su comportamiento y su falta o presencia de simetría.
