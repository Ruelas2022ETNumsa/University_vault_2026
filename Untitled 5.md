### **Enunciado**

Verificar si la señal de tiempo continuo $x(t) = e^{-ct}$ es una señal de energía, de potencia, o ninguna de las anteriores, para un valor complejo $c$ con parte real no nula ($\text{Re}\{c\} \neq 0$).

---

### **Desarrollo paso a paso**

#### **1. Definición y preparación de la señal**

Para analizar un exponente complejo $c$, lo representamos en su forma cartesiana estándar:

$$c = \sigma + j\omega$$

Donde:

- $\sigma = \text{Re}\{c\} \neq 0$ (parte real no nula, según la condición del problema).
- $\omega = \text{Im}\{c\}$ (parte imaginaria).

Sustituyendo esto en la expresión de nuestra señal $x(t)$:

$$x(t) = e^{-(\sigma + j\omega)t} = e^{-\sigma t} e^{-j\omega t}$$

Para realizar los análisis de energía y potencia, requerimos la magnitud al cuadrado de la señal, $|x(t)|^2$. Recordando que la magnitud de cualquier exponencial compleja pura de la forma $e^{-j\omega t}$ es siempre igual a la unidad ($|e^{-j\omega t}| = 1$), obtenemos:

$$|x(t)|^2 = \left|e^{-\sigma t} e^{-j\omega t}\right|^2 = \left(e^{-\sigma t}\right)^2 \cdot \underbrace{\left|e^{-j\omega t}\right|^2}_{1} = e^{-2\sigma t}$$

Fijate que el comportamiento de $|x(t)|^2$ queda gobernado de forma exclusiva por la parte real $\sigma$. Visualicemos ambas situaciones posibles según el signo de $\sigma$:

```desmos-graph
left=-4; right=4; bottom=-1; top=5;
width=500; height=250;
---
y=e^{-2*x} | -4<=x<=4 | #005F73
y=e^{2*x} | -4<=x<=4 | #EE9B00
```

_En azul petróleo (`#005F73`), se muestra $|x(t)|^2$ para $\sigma > 0$ (decae hacia el infinito pero diverge hacia el pasado). En ámbar (`#EE9B00`), se representa el caso para $\sigma < 0$ (crece exponencialmente hacia el futuro)._

---

#### **2. Análisis de Energía Total ($E_\infty$)**

Por definición, la energía total de una señal compleja en tiempo continuo es:

$$E_\infty = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

Sustituyendo $|x(t)|^2 = e^{-2\sigma t}$:

$$E_\infty = \int_{-\infty}^{\infty} e^{-2\sigma t} dt$$

Dado que es una integral impropia de límites infinitos y $\sigma \neq 0$, planteamos el límite simétrico para evaluar su convergencia:

$$\begin{array}{rcl} E_\infty & = & \lim_{T \to \infty} \int_{-T}^{T} e^{-2\sigma t} dt \\ & = & \lim_{T \to \infty} \left[ \dfrac{e^{-2\sigma t}}{-2\sigma} \right]_{-T}^{T} \\ & = & \lim_{T \to \infty} \left( \dfrac{e^{-2\sigma T}}{-2\sigma} - \dfrac{e^{2\sigma T}}{-2\sigma} \right) \\ & = & \lim_{T \to \infty} \dfrac{e^{2\sigma T} - e^{-2\sigma T}}{2\sigma} \end{array}$$

Evaluamos el comportamiento de este límite según el signo de $\sigma$:

- **Si $\sigma > 0$:** Al tender $T \to \infty$, el término $e^{2\sigma T} \to \infty$ y el término $e^{-2\sigma T} \to 0$. $$E_\infty = \lim_{T \to \infty} \dfrac{\infty - 0}{2\sigma} = \infty$$
- **Si $\sigma < 0$:** Al tender $T \to \infty$, el término $e^{2\sigma T} \to 0$ y el término $e^{-2\sigma T} \to \infty$ (puesto que $-2\sigma T > 0$). $$E_\infty = \lim_{T \to \infty} \dfrac{0 - \infty}{2\sigma} = \infty \quad (\text{dado que } \sigma < 0, \text{ el cociente resulta positivo})$$

Como la energía total diverge ($E_\infty = \infty$), la señal **no es una señal de energía**.

---

#### **3. Análisis de Potencia Promedio ($P_\infty$)**

Por definición, la potencia promedio de una señal continua sobre un intervalo de tiempo infinito es:

$$P_\infty = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt$$

Sustituyendo $|x(t)|^2 = e^{-2\sigma t}$:

$$\begin{array}{rcl} P_\infty & = & \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} e^{-2\sigma t} dt \\ & = & \lim_{T \to \infty} \dfrac{1}{T} \left[ \dfrac{e^{-2\sigma t}}{-2\sigma} \right]_{-T/2}^{T/2} \\ & = & \lim_{T \to \infty} \dfrac{1}{T} \left( \dfrac{e^{-\sigma T}}{-2\sigma} - \dfrac{e^{\sigma T}}{-2\sigma} \right) \\ & = & \lim_{T \to \infty} \dfrac{e^{\sigma T} - e^{-\sigma T}}{2\sigma T} \end{array}$$

Evaluamos los límites correspondientes:

- **Si $\sigma > 0$:** Puesto que $e^{-\sigma T} \to 0$, el límite se reduce a una indeterminación del tipo $\dfrac{\infty}{\infty}$: $$P_\infty = \lim_{T \to \infty} \dfrac{e^{\sigma T}}{2\sigma T}$$ Aplicando la regla de L'Hôpital respecto de $T$: $$P_\infty = \lim_{T \to \infty} \dfrac{\dfrac{d}{dT}\left(e^{\sigma T}\right)}{\dfrac{d}{dT}(2\sigma T)} = \lim_{T \to \infty} \dfrac{\sigma e^{\sigma T}}{2\sigma} = \lim_{T \to \infty} \dfrac{e^{\sigma T}}{2} = \infty$$
    
- **Si $\sigma < 0$:** Puesto que $e^{\sigma T} \to 0$, definimos $\sigma' = -\sigma > 0$ y reescribimos el límite: $$P_\infty = \lim_{T \to \infty} \dfrac{-e^{-\sigma T}}{2\sigma T} = \lim_{T \to \infty} \dfrac{e^{\sigma' T}}{2\sigma' T}$$ Aplicando de nuevo la regla de L'Hôpital: $$P_\infty = \lim_{T \to \infty} \dfrac{\sigma' e^{\sigma' T}}{2\sigma'} = \lim_{T \to \infty} \dfrac{e^{\sigma' T}}{2} = \infty$$
    

Como la potencia promedio temporal también diverge ($P_\infty = \infty$), la señal **no es una señal de potencia**.

---

### **Conclusión**

Al comprobar que tanto la energía total $E_\infty$ como la potencia promedio $P_\infty$ tienden a infinito bajo la condición de parte real no nula, podemos concluir con total rigurosidad:

$$\bbox[border: 2px solid #005F73, 10px]{ \begin{array}{c} \mathbf{x(t) = e^{-ct} \text{ es una señal de tipo "ni de energía ni de potencia"}} \\ \text{para cualquier valor complejo } c \in \mathbb{C} \text{ con } \text{Re}\{c\} \neq 0. \end{array} }$$
