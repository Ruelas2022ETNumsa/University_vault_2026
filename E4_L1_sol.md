### **Señal a: $x(n) = \sum_{k=0}^{4} \delta(n-k)$**

#### **1. Desarrollo paso a paso**
A partir de la definición de la Transformada de Fourier en Tiempo Discreto $DTFT$:

$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x(n) e^{-j\omega n}
$$


Sustituyendo la secuencia de impulsos, la sumatoria se reduce al intervalo de soporte $n \in$:

$$
X(e^{j\omega}) = \sum_{n=0}^{4} e^{-j\omega n}
$$


Esta expresión representa una serie geométrica finita de 5 términos con razón $e^{-j\omega}$. Aplicando la fórmula de la suma geométrica finita $\sum_{k=0}^{N-1} q^k = \frac{1-q^N}{1-q}$:

$$
X(e^{j\omega}) = \frac{1 - e^{-j5\omega}}{1 - e^{-j\omega}}
$$


Para simplificar a su forma cerrada, factorizamos la fase mitad tanto en el numerador como en el denominador:

$$
X(e^{j\omega}) = \frac{e^{-j5\omega/2} \left( e^{j5\omega/2} - e^{-j5\omega/2} \right)}{e^{-j\omega/2} \left( e^{j\omega/2} - e^{-j\omega/2} \right)}
$$


Aplicando la identidad de Euler $e^{j\theta} - e^{-j\theta} = 2j\sin(\theta)$:

$$
X(e^{j\omega}) = e^{-j2\omega} \frac{2j \sin\left(\frac{5\omega}{2}\right)}{2j \sin\left(\frac{\omega}{2}\right)}
$$


La expresión analítica simplificada en **forma cerrada** es:

$$
\mathbf{X(e^{j\omega}) = e^{-j2\omega} \frac{\sin\left(\frac{5\omega}{2}\right)}{\sin\left(\frac{\omega}{2}\right)}}
$$


#### **2. Magnitud y Fase**
*   **Magnitud:**
    
$$
\mathbf{|X(e^{j\omega})| = \left| \frac{\sin\left(\frac{5\omega}{2}\right)}{\sin\left(\frac{\omega}{2}\right)} \right|}
$$

*   **Fase:**
    
$$
\mathbf{\angle X(e^{j\omega}) = -2\omega + \angle \left( \frac{\sin\left(\frac{5\omega}{2}\right)}{\sin\left(\frac{\omega}{2}\right)} \right)}
$$

    *Nota: El término angular adicional aporta saltos de $\pi$ (o $-\pi$) radianes en las frecuencias donde el cociente de senos cambia de signo.*

---

### **Señal b: $x(n) = (0.5)^{|n|}$**

#### **1. Desarrollo paso a paso**
Por tratarse de una secuencia bilateral, dividimos la sumatoria en sus componentes anticausal ($n < 0$) y causal ($n \ge 0$):

$$
X(e^{j\omega}) = \sum_{n=-\infty}^{-1} (0.5)^{-n} e^{-j\omega n} + \sum_{n=0}^{\infty} (0.5)^n e^{-j\omega n}
$$


*   **Componente anticausal ($n < 0$):**
    Realizando el cambio de variable $m = -n$:
    
$$
\sum_{m=1}^{\infty} (0.5)^m e^{j\omega m} = \sum_{m=1}^{\infty} \left(0.5 e^{j\omega}\right)^m
$$

    Esta serie geométrica infinita converge porque el módulo de la razón es $\left|0.5 e^{j\omega}\right| = 0.5 < 1$:
    
$$
\sum_{m=1}^{\infty} \left(0.5 e^{j\omega}\right)^m = \frac{0.5 e^{j\omega}}{1 - 0.5 e^{j\omega}}
$$


*   **Componente causal ($n \ge 0$):**
    Aplicando directamente la fórmula de la serie geométrica infinita para $|a| < 1$:
    
$$
\sum_{n=0}^{\infty} \left(0.5 e^{-j\omega}\right)^n = \frac{1}{1 - 0.5 e^{-j\omega}}
$$


Sumando ambas contribuciones bajo un mismo denominador común:

$$
X(e^{j\omega}) = \frac{0.5 e^{j\omega}}{1 - 0.5 e^{j\omega}} + \frac{1}{1 - 0.5 e^{-j\omega}}
$$


$$
X(e^{j\omega}) = \frac{0.5 e^{j\omega}\left(1 - 0.5 e^{-j\omega}\right) + \left(1 - 0.5 e^{j\omega}\right)}{\left(1 - 0.5 e^{j\omega}\right)\left(1 - 0.5 e^{-j\omega}\right)}
$$


Desarrollando el numerador:

$$
N = 0.5 e^{j\omega} - 0.25 + 1 - 0.5 e^{j\omega} = 0.75
$$


Desarrollando el denominador:

$$
D = 1 - 0.5 e^{-j\omega} - 0.5 e^{j\omega} + 0.25 = 1.25 - \cos(\omega)
$$


Obtenemos la forma cerrada preliminar:

$$
X(e^{j\omega}) = \frac{0.75}{1.25 - \cos(\omega)}
$$


Multiplicando numerador y denominador por 4, la expresión analítica simplificada en **forma cerrada** es:

$$
\mathbf{X(e^{j\omega}) = \frac{3}{5 - 4\cos(\omega)}}
$$


#### **2. Magnitud y Fase**
Al ser $x(n)$ una señal real y par, su DTFT resultante es puramente real, par y estrictamente positiva, dado que el denominador $5 - 4\cos(\omega) \ge 1 > 0$ para todo $\omega$.
*   **Magnitud:**
    
$$
\mathbf{|X(e^{j\omega})| = \frac{3}{5 - 4\cos(\omega)}}
$$

*   **Fase:**
    
$$
\mathbf{\angle X(e^{j\omega}) = 0}
$$


---

### **Visualización de los Espectros de Magnitud**

```desmos-graph
left=-6.28; right=6.28; bottom=-1; top=6;
width=300; height=200;
---
y = \abs(\sin(2.5x)/\sin(0.5x))
y = 3/(5-4\cos(x))
```
