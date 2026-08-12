Classify the following continuous-time signals as periodic or aperiodic. If periodic, determine the period. 

i) $x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)$
ii) $x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)$
iii) $x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)$
iv) $x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)$
v) $x(t) = e^{j(4t+\tfrac{\pi}{5})}$
vi) $x(t) = \cos\left(2t + \frac{\pi}{4}\right)$
vii) $x(t) = \cos(2\pi t)u(t)$
viii) $x(t) = \cos^2(t)$




Para determinar si una señal continua \(x(t)\) es periódica, debemos verificar si existe un valor positivo \(T > 0\) tal que se cumpla la relación: \[x(t + T) = x(t) \quad \text{para todo } t \in \mathbb{R} \text{}\]

El menor valor positivo de \(T\) que satisface esta condición es el **periodo fundamental** (\(T_0\)). Para señales sinusoidales de la forma \(A\cos(\omega_0 t + \theta)\) o exponenciales complejas \(e^{j(\omega_0 t + \theta)}\), la señal siempre es periódica con un periodo fundamental de: \[T_0 = \frac{2\pi}{|\omega_0|} \text{}\]

Cuando tenemos una **suma de señales periódicas** con periodos fundamentales \(T_1, T_2, \dots\), la señal resultante será periódica si y solo si la relación entre cualquiera de sus periodos es un **número racional**: \[\frac{T_i}{T_j} \in \mathbb{Q} \text{}\]

Si esta condición se cumple, el periodo fundamental \(T_0\) de la suma es el **mínimo común múltiplo (MCM)** de los periodos individuales. Además, la adición de una constante (componente de cd) no altera la periodicidad ni el periodo fundamental de la señal.

A continuación se clasifica y resuelve detalladamente cada uno de los casos planteados:

---

### **i) \(x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)\)**

Esta señal es la suma de dos componentes periódicas:

1. \(x_1(t) = \cos\left(\frac{2\pi}{3}t\right)\), con frecuencia angular \(\omega_1 = \frac{2\pi}{3}\) rad/s. Su periodo fundamental es: \[T_1 = \frac{2\pi}{\omega_1} = \frac{2\pi}{2\pi/3} = 3 \text{ s}\]
2. \(x_2(t) = 2\sin\left(\frac{\pi}{2}t\right)\), con frecuencia angular \(\omega_2 = \frac{\pi}{2}\) rad/s. Su periodo fundamental es: \[T_2 = \frac{2\pi}{\omega_2} = \frac{2\pi}{\pi/2} = 4 \text; s}\]

Evaluamos la relación de los periodos: \[\frac{T_1}{T_2} = \frac{3}{4}\]

Como el resultado (\(\frac{3}{4}\)) es un **número racional**, la señal resultante es **periódica**. Su periodo fundamental \(T_0\) es el mínimo común múltiplo de \(T_1 = 3\) y \(T_2 = 4\): \[T_0 = \text{MCM}(3, 4) = 12 \text{ s}\]

- **Clasificación:** **Periódica**
- **Periodo fundamental (\(T_0\)):** **\(12\) s**

---

### **ii) \(x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)\)**

Analizamos las dos componentes de la suma:

1. \(x_1(t) = \cos(2\pi t)\), con frecuencia \(\omega_1 = 2\pi\) rad/s y periodo fundamental: \[T_1 = \frac{2\pi}{2\pi} = 1 \text{ s}\]
2. \(x_2(t) = \sin\left(\sqrt{2}\pi t\right)\), con frecuencia \(\omega_2 = \sqrt{2}\pi\) rad/s y periodo fundamental: \[T_2 = \frac{2\pi}{\sqrt{2}\pi} = \sqrt{2} \text{ s}\]

Evaluamos la relación de los periodos: \[\frac{T_1}{T_2} = \frac{1}{\sqrt{2}}\]

Dado que \(\frac{1}{\sqrt{2}}\) es un **número irracional**, las señales no comparten un periodo común en el tiempo.

- **Clasificación:** **Aperiódica** (No periódica)

---

### **iii) \(x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)\)**

Esta señal es una constante sumada a una función sinusoidal periódica.

- La constante \(\frac{1}{2}\) no afecta la periodicidad ni el periodo de la componente variable.
    
- La componente variable es \(x_2(t) = -\frac{1}{2}\cos(2t)\), cuya frecuencia angular es \(\omega = 2\) rad/s. Su periodo fundamental es: \[T_0 = \frac{2\pi}{|\omega|} = \frac{2\pi}{2} = \pi \text{ s}\]
    
- **Clasificación:** **Periódica**
    
- **Periodo fundamental (\(T_0\)):** **\(\pi\) s** (aproximadamente \(3.1416\) s)
    

---

### **iv) \(x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)\)**

La constante \(1\) no altera el periodo de la señal. Analizamos los dos términos sinusoidales periódicos:

1. \(x_1(t) = \sin(4t)\), con frecuencia angular \(\omega_1 = 4\) rad/s y periodo: \[T_1 = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s}\]
2. \(x_2(t) = \cos\left(6t + \frac{\pi}{3}\right)\), con frecuencia angular \(\omega_2 = 6\) rad/s y periodo: \[T_2 = \frac{2\pi}{6} = \frac{\pi}{3} \text{ s}\]

Relación de periodos: \[\frac{T_1}{T_2} = \frac{\pi/2}{\pi/3} = \frac{3}{2}\]

Como la relación es un **número racional** (\(\frac{3}{2}\)), la señal combinada es **periódica**. Buscamos el menor periodo común \(T_0\) de modo que sea un múltiplo entero de ambos periodos: \[T_0 = 2 T_1 = 3 T_2 \implies T_0 = 2\left(\frac{\pi}{2}\right) = 3\left(\frac{\pi}{3}\right) = \pi \text{ s}\]

- **Clasificación:** **Periódica**
- **Periodo fundamental (\(T_0\)):** **\(\pi\) s**

---

### **v) \(x(t) = e^{j(4t+\tfrac{\pi}{5})}\)**

Esta es una señal exponencial compleja de la forma \(e^{j(\omega_0 t + \theta)}\) con frecuencia angular \(\omega_0 = 4\) rad/s. Las exponenciales complejas en tiempo continuo siempre son periódicas, y su periodo fundamental es: \[T_0 = \frac{2\pi}{|\omega_0|} = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s}\]

- **Clasificación:** **Periódica**
- **Periodo fundamental (\(T_0\)):** **\(\frac{\pi}{2}\) s**

---

### **vi) \(x(t) = \cos\left(2t + \frac{\pi}{4}\right)\)**

Es una señal senoidal simple con frecuencia angular \(\omega_0 = 2\) rad/s. Al ser una sinusoide básica continua, siempre es periódica, y su periodo fundamental es: \[T_0 = \frac{2\pi}{|\omega_0|} = \frac{2\pi}{2} = \pi \text{ s}\]

- **Clasificación:** **Periódica**
- **Periodo fundamental (\(T_0\)):** **\(\pi\) s**

---

### **vii) \(x(t) = \cos(2\pi t)u(t)\)**

La señal está multiplicada por la función escalón unitario \(u(t)\), lo que significa que: \[x(t) = \begin{cases} \cos(2\pi t) & \text{si } t \ge 0 \ 0 & \text{si } t < 0 \end{cases} \text{}\]

Para que una señal sea periódica, la repetición del patrón debe ocurrir de manera idéntica a lo largo de todo el eje del tiempo, desde \(-\infty\) hasta \(+\infty\). Al estar truncada (vale \(0\) para todo el tiempo negativo y oscila para el tiempo positivo), cualquier desplazamiento en el tiempo \(T > 0\) romperá la simetría en la zona de transición alrededor del origen \(t = 0\). Por lo tanto, no existe ningún valor \(T > 0\) que cumpla la propiedad \(x(t + T) = x(t)\) para todo \(t\).

- **Clasificación:** **Aperiódica** (No periódica)

---

### **viii) \(x(t) = \cos^2(t)\)**

Utilizando la identidad trigonométrica del ángulo doble para reducir el exponente de la función: \[\cos^2(t) = \frac{1}{2} + \frac{1}{2}\cos(2t) \text{}\]

Esto nos deja con una constante más un término senoidal cuya frecuencia angular es \(\omega_0 = 2\) rad/s. El periodo fundamental de la señal combinada está definido únicamente por este término variable: \[T_0 = \frac{2\pi}{|\omega_0|} = \frac{2\pi}{2} = \pi \text{ s}\]

- **Clasificación:** **Periódica**
- **Periodo fundamental (\(T_0\)):** **\(\pi\) s**

---

🧩 Si quieres, podemos calcular los coeficientes de la serie de Fourier para alguna de estas señales periódicas, como por ejemplo para \(x(t) = \cos^2(t)\).
