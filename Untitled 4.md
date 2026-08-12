### 4. Considere la siguiente señal de tiempo continuo:

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

---

📊 Si te interesa, podemos escribir un script en Python para graficar la señal con distintos valores de $T$ y que así puedas comprobar visualmente estas simetrías par e impar.
