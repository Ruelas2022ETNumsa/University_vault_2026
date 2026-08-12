A periodic signal $x_1(t)$ has a period $2$, and another periodic signal $x_2(t)$ has a period $3$. Find the fundamental frequency and period for the signal $y(t) = x_1(t) + x_2(t)$.

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

🧩 Si quieres, podemos proponer dos funciones senoidales concretas que cumplan con estos periodos (por ejemplo, con $T_1 = 2$ y $T_2 = 3$) para graficarlas y observar visualmente cómo se repite la señal resultante cada 6 segundos.
