# Señales de tiempo continuo periódicas y no periódicas

# 1. Señales de tiempo continuo periódicas y no periódicas

Graficar las siguientes señales de tiempo continuo usando, por ejemplo, MATLAB o Python. Determinar qué señal es periódica y seleccionar un rango de tiempo que cubra al menos tres períodos, presentándola en una gráfica separada.

$$
x(t)=5\cos\left[2\pi(15)t+0.25\pi\right]
$$

$$
x(t)=5\cos\left[2\pi(15)t+0.25\pi\right]
+5\cos\left[2\pi(10)t+0.3\pi\right]
$$

# 2. Determinar la convolución lineal

Determinar la convolución lineal de las siguientes secuencias, donde $x(n)$ es la entrada y $h(n)$ representa la respuesta al impulso de un sistema de tiempo discreto.

$$
x(n)=[1\quad 1\quad 1\quad 1]
$$

$$
h(n)=[1\quad 2\quad 3]
$$

Graficar la salida en todos los instantes en los que la respuesta del sistema sea diferente de cero.

# 3. Sistema de tiempo discreto recursivo

Considere un sistema de tiempo discreto recursivo con entrada $x(n)$ y salida $y(n)$, el cual está descrito por la siguiente ecuación de diferencias:

$$
y(n)=2y(n-1)+x(n)
$$

Si la entrada es:

$$
x(n)=\delta(n)
$$

determinar la salida $y(n)$ en el rango de tiempo $0\leq n\leq5$, dada la condición inicial:

$$
y(-1)=0
$$

y graficar la respuesta.

# 4. Transformada de Fourier de Tiempo Discreto (DTFT)

Determinar la Transformada de Fourier de Tiempo Discreto (DTFT) de las siguientes funciones del tiempo:

$$
x(n)=\sum_{k=0}^{4}\delta(n-k)
$$

$$
x(n)=(0.5)^{|n|}
$$

Graficar su magnitud y fase.

# 5. Transformada Discreta de Fourier (DFT)

Seleccionar 5 puntos de cada una de las señales del ejercicio 4 y calcular y graficar la magnitud y fase de la DFT (Transformada Discreta de Fourier) de:

- a) 5 puntos
- b) 10 puntos
- c) 50 puntos

Comparar cada gráfica con las gráficas de la DTFT obtenida en el ejercicio 4.

---

# Mensajes NotebookLM

## Ejercicio 1

```
Rápido con MATLAB: Graficar las siguientes señales de tiempo continuo y determinar cuál es periódica. Para la señal periódica, seleccionar un rango de tiempo que cubra al menos tres períodos y presentarla en una gráfica separada.

Señal 1: x(t) = 5·cos[2π(15)t + 0.25π]
Señal 2: x(t) = 5·cos[2π(15)t + 0.25π] + 5·cos[2π(10)t + 0.3π]

Indicar el período de cada señal periódica encontrada. Graficar ambas señales. Usar t con resolución suficiente para visualización limpia.
Resolución analítica: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf Cap. 1 — K. Deergha Rao-Signals and Systems.pdf Cap. 1 — Oppenheim & Willsky-Signals and Systems-2th ed-1to5.pdf Cap. 1.
Código: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf Cap. 1.
```

## Ejercicio 2

```
Resolvé con MATLAB: Determinar la convolución lineal de las siguientes secuencias, donde x(n) es la entrada y h(n) es la respuesta al impulso de un sistema LTI de tiempo discreto.

x(n) = [1  1  1  1]
h(n) = [1  2  3]

Desarrollar analíticamente la convolución paso a paso (suma de convolución). Indicar el soporte de la salida y(n) — longitud esperada, índices donde y(n) ≠ 0. Graficar y(n) con stem en todos los instantes donde la respuesta sea diferente de cero. Verificar el resultado con la función conv() de MATLAB.
Resolución analítica: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf Cap. 1 — Oppenheim & Willsky-Signals and Systems-2th ed-6to11.pdf Cap. 6 — SCHAUM-HWEI P. HSU-SIGNALS AND SYSTEMS-1995.pdf Cap. 3–4.
Código: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf Cap. 2.
Verificación: SCHAUM-HWEI P. HSU-SIGNALS AND SYSTEMS-1995.pdf Cap. 3–4 — Mani, Oppenheim, Willsky, Nawab-Signals and Systems Solutions Manual.pdf.
```

## Ejercicio 3

```
Resolvé con MATLAB: Analizar el siguiente sistema de tiempo discreto recursivo con entrada x(n) y salida y(n).

Ecuación en diferencias: y(n) = 2·y(n-1) + x(n)
Entrada: x(n) = δ(n)  (impulso unitario)
Condición inicial: y(-1) = 0
Rango de evaluación: 0 ≤ n ≤ 5

Desarrollar analíticamente la respuesta muestra a muestra para n = 0, 1, 2, 3, 4, 5 usando la condición inicial dada. Identificar si el sistema es estable (analizar el polo). Implementar en MATLAB usando un bucle for que respete la condición inicial. Graficar y(n) con stem.
Resolución analítica: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf Cap. 1 — Oppenheim & Willsky-Signals and Systems-2th ed-6to11.pdf Cap. 6 — SCHAUM-HWEI P. HSU-SIGNALS AND SYSTEMS-1995.pdf Cap. 4.
Código: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf Cap. 2.
Verificación: SCHAUM-HWEI P. HSU-SIGNALS AND SYSTEMS-1995.pdf Cap. 4 — Mani, Oppenheim, Willsky, Nawab-Signals and Systems Solutions Manual.pdf.
```

## Ejercicio 4

```
Resolvé con MATLAB: Determinar la Transformada de Fourier de Tiempo Discreto (DTFT) de las siguientes secuencias y graficar magnitud y fase.

Señal a: x(n) = sum_{k=0}^{4} δ(n-k)   [suma de 5 impulsos desplazados, n = 0,1,2,3,4]
Señal b: x(n) = (0.5)^|n|               [secuencia bilateral de longitud infinita]

Para cada señal:
- Obtener la expresión analítica de X(e^jω)
- Simplificar hasta forma cerrada si es posible
- Graficar |X(e^jω)| y ∠X(e^jω) en el rango ω ∈ [-π, π]
- En MATLAB: usar un vector denso de ω (N = 512 o más) y evaluar la DTFT directamente desde la definición o usando freqz según corresponda
- Señal b requiere truncamiento: justificar el largo elegido
Resolución analítica: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf Cap. 2 — Oppenheim & Willsky-Signals and Systems-2th ed-6to11.pdf Cap. 7 — Proakis & Manolakis — Digital Signal Processing Principles Algorithms Applications — 4th ed-1to5.pdf Cap. 3 — SCHAUM-MONSON H. HAYES-DIGITAL SIGNAL PROCESSING-1999.pdf Cap. 3.
Código: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf Cap. 3.
Verificación: SCHAUM-MONSON H. HAYES-DIGITAL SIGNAL PROCESSING-1999.pdf Cap. 3 — Proakis & Manolakis — Digital Signal Processing Solutions Manual — 4th ed.pdf.
```

## Ejercicio 5

```
Código MATLAB para: Calcular y graficar la DFT de las dos señales del ejercicio 4, usando las primeras 5 muestras de cada una (n = 0,1,2,3,4). Para cada señal calcular la DFT con N = 5, N = 10 y N = 50 puntos (zero-padding). Graficar magnitud y fase de cada caso. Superponer o comparar visualmente cada gráfica con la DTFT obtenida en el ejercicio 4 (incluir la DTFT como referencia en las mismas figuras).

Señal a: x(n) = [1 1 1 1 1]  (5 muestras de sum δ(n-k))
Señal b: x(n) = (0.5)^|n| evaluada en n = 0,1,2,3,4 → [1, 0.5, 0.25, 0.125, 0.0625]

Usar fft() con el argumento de longitud para zero-padding. Escalar el eje de frecuencia a ω ∈ [0, 2π] o [-π, π]. Un subplot por valor de N. Incluir la DTFT de referencia (del ejercicio 4) en cada subplot.
Resolución analítica: S. Palani, D. Kalaiyarasi-Principles of Digital Signal Processing - 2nd Ed.pdf Cap. 2 — Oppenheim & Willsky-Signals and Systems-2th ed-6to11.pdf Cap. 8 — SCHAUM-MONSON H. HAYES-DIGITAL SIGNAL PROCESSING-1999.pdf Cap. 5–6.
Código: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf Cap. 5.
Verificación: SCHAUM-MONSON H. HAYES-DIGITAL SIGNAL PROCESSING-1999.pdf Cap. 5–6 — Proakis & Manolakis — Digital Signal Processing Solutions Manual — 4th ed.pdf.
```

---

## Mensajes NotebookLM — Resolución analítica

## Ejercicio 1 — Analítico

```
Resolvé rápido / sin ejercicio adicional: Determinar analíticamente si las siguientes señales de tiempo continuo son periódicas. Para cada señal periódica, calcular el período fundamental T0.

Señal 1: x(t) = 5·cos[2π(15)t + 0.25π]
Señal 2: x(t) = 5·cos[2π(15)t + 0.25π] + 5·cos[2π(10)t + 0.3π]

Para la señal 2: aplicar el criterio de periodicidad de suma de sinusoides — verificar si el cociente de frecuencias es racional y calcular el período de la suma como mínimo común múltiplo de los períodos individuales. Mostrar cada paso.
Referencia: Palani Cap. 1 — Rao Cap. 1 — Oppenheim EN (1to5) Cap. 1.
```

## Ejercicio 2 — Analítico

```
Resolvé rápido / sin ejercicio adicional: Calcular analíticamente la convolución lineal y(n) = x(n) * h(n) de las siguientes secuencias mediante la suma de convolución.

x(n) = [1  1  1  1]   (n = 0, 1, 2, 3)
h(n) = [1  2  3]       (n = 0, 1, 2)

Desarrollar la suma de convolución y(n) = Σ x(k)·h(n-k) término a término para cada n. Indicar el soporte de y(n) (longitud = 6, índices n = 0…5). Mostrar la tabla de productos desplazados si es necesario.
Referencia: Palani Cap. 1 — Oppenheim EN (6to11) Cap. 6 — Hsu Schaum Cap. 3–4.
```

## Ejercicio 3 — Analítico

```
Resolvé rápido / sin ejercicio adicional: Resolver analíticamente el sistema recursivo de tiempo discreto muestra a muestra para n = 0, 1, 2, 3, 4, 5.

Ecuación en diferencias: y(n) = 2·y(n-1) + x(n)
Entrada: x(n) = δ(n)
Condición inicial: y(-1) = 0

Sustituir directamente en la ecuación para cada n y obtener y(0), y(1), …, y(5). Luego analizar la estabilidad identificando el polo del sistema (denominador de H(z)) y verificar si cae dentro o fuera del círculo unitario.
Referencia: Palani Cap. 1 — Oppenheim EN (6to11) Cap. 6 — Hsu Schaum Cap. 4.
```

## Ejercicio 4 — Analítico

```
Resolvé rápido / sin ejercicio adicional: Obtener la expresión analítica de la DTFT X(e^jω) para las siguientes secuencias y simplificar hasta forma cerrada.

Señal a: x(n) = Σ_{k=0}^{4} δ(n-k)   (suma de 5 impulsos desplazados)
Señal b: x(n) = (0.5)^|n|             (secuencia bilateral)

Señal a: aplicar linealidad y la propiedad de desplazamiento de la DTFT — X(e^jω) = Σ e^{-jωk} para k = 0…4 — simplificar usando suma de progresión geométrica.
Señal b: separar en parte causal y anticausal, aplicar la fórmula de serie geométrica a cada parte y sumar — obtener forma cerrada en función de cos(ω).
Indicar magnitud |X(e^jω)| y fase ∠X(e^jω) resultantes.
Referencia: Palani Cap. 2 — Oppenheim EN (6to11) Cap. 7 — Hayes Schaum DSP Cap. 3 — Proakis & Manolakis (1to5) Cap. 3.
```

## Ejercicio 5 — Analítico

```
Resolvé rápido / sin ejercicio adicional: Calcular analíticamente la DFT de N puntos de las siguientes secuencias para N = 5, N = 10 y N = 50.

Señal a: x(n) = [1 1 1 1 1]  (n = 0…4)
Señal b: x(n) = [(0.5)^|n|]  evaluada en n = 0…4 → [1, 0.5, 0.25, 0.125, 0.0625]

Para cada caso aplicar la definición X[k] = Σ_{n=0}^{N-1} x(n)·e^{-j2πkn/N}. Para N > 5 el zero-padding extiende la secuencia — aclarar qué muestras se agregan. Señal a con N = 5: simplificar usando suma geométrica en función de k. Indicar los N valores de X[k] para k = 0…N-1 en cada caso y explicar cómo el zero-padding aumenta la resolución de la DTFT muestreada.
Referencia: Palani Cap. 2 — Oppenheim EN (6to11) Cap. 8 — Hayes Schaum DSP Cap. 5–6.
```