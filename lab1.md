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