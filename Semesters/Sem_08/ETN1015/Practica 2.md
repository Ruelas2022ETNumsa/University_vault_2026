# E8
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

---

# E9

### **Enunciado**

Demostrar que la energía total de la señal combinada $z(t) = x(t) \pm y(t)$ es igual a la suma de sus energías individuales, es decir:

$$E_{x \pm y} = E_x + E_y$$

siempre que $x(t)$ e $y(t)$ sean señales ortogonales.

---

### **Desarrollo paso a paso**

#### **1. Definiciones fundamentales**

Para una señal compleja general de tiempo continuo $f(t)$, la **energía total** en el intervalo infinito se define como:

$$E_f = \int_{-\infty}^{\infty} |f(t)|^2 dt = \int_{-\infty}^{\infty} f(t) f^*(t) dt$$

Donde $f^*(t)$ denota el conjugado complejo de $f(t)$.

Por definición, dos señales $x(t)$ e $y(t)$ son **ortogonales** en el intervalo $(-\infty, \infty)$ si y solo si su producto interno es nulo:

$$\int_{-\infty}^{\infty} x(t) y^*(t) dt = 0$$

De igual manera, aplicando la propiedad del conjugado en ambos lados, se cumple que:

$$\left( \int_{-\infty}^{\infty} x(t) y^*(t) dt \right)^* = 0^* \implies \int_{-\infty}^{\infty} x^*(t) y(t) dt = 0$$

---

#### **2. Análisis de la energía de la suma/resta**

Definimos la señal resultante de la combinación lineal:

$$z(t) = x(t) \pm y(t)$$

La energía total de la señal combinada $E_z$ es:

$$E_z = \int_{-\infty}^{\infty} |z(t)|^2 dt = \int_{-\infty}^{\infty} z(t) z^*(t) dt$$

Sustituyendo $z(t) = x(t) \pm y(t)$ y su conjugado $z^*(t) = x^*(t) \pm y^*(t)$ en la integral:

$$E_z = \int_{-\infty}^{\infty} [x(t) \pm y(t)] [x^*(t) \pm y^*(t)] dt$$

Aplicando la propiedad distributiva para expandir el producto del integrando:

$$[x(t) \pm y(t)] [x^*(t) \pm y^*(t)] = x(t)x^*(t) \pm x(t)y^*(t) \pm y(t)x^*(t) + y(t)y^*(t)$$

_Nota que, independientemente de si elegimos el signo superior $(+)$ o el inferior $(-)$, el producto del último término siempre conserva el signo positivo, ya que $(+) \cdot (+) = +$ y $(-) \cdot (-) = +$._

Sustituimos esta expansión dentro de la integral:

$$E_z = \int_{-\infty}^{\infty} \left[ x(t)x^*(t) \pm x(t)y^*(t) \pm y(t)x^*(t) + y(t)y^*(t) \right] dt$$

Por la propiedad de linealidad de la integral, podemos separar los términos en integrales independientes:

$$\begin{array}{rcl} E_z & = & \int_{-\infty}^{\infty} x(t)x^*(t) dt \pm \int_{-\infty}^{\infty} x(t)y^*(t) dt \pm \int_{-\infty}^{\infty} y(t)x^*(t) dt + \int_{-\infty}^{\infty} y(t)y^*(t) dt \end{array}$$

Expresando los productos de la forma $f(t)f^*(t)$ como magnitudes al cuadrado $|f(t)|^2$:

$$\begin{array}{rcl} E_z & = & \int_{-\infty}^{\infty} |x(t)|^2 dt \pm \int_{-\infty}^{\infty} x(t)y^*(t) dt \pm \int_{-\infty}^{\infty} x^*(t)y(t) dt + \int_{-\infty}^{\infty} |y(t)|^2 dt \end{array}$$

---

#### **3. Aplicación de la hipótesis de ortogonalidad**

Dado que las señales $x(t)$ e $y(t)$ son **ortogonales** por hipótesis, sus integrales cruzadas se anulan de la siguiente manera:

$$\int_{-\infty}^{\infty} x(t)y^*(t) dt = 0 \quad \text{y} \quad \int_{-\infty}^{\infty} x^*(t)y(t) dt = 0$$

Sustituyendo estas condiciones en nuestra ecuación:

$$\begin{array}{rcl} E_z & = & \int_{-\infty}^{\infty} |x(t)|^2 dt \pm \bcancel{\int_{-\infty}^{\infty} x(t)y^*(t) dt}^{0} \pm \bcancel{\int_{-\infty}^{\infty} x^*(t)y(t) dt}^{0} + \int_{-\infty}^{\infty} |y(t)|^2 dt \\ E_z & = & \int_{-\infty}^{\infty} |x(t)|^2 dt + \int_{-\infty}^{\infty} |y(t)|^2 dt \end{array}$$

Reconociendo que las integrales restantes representan exactamente las energías de cada una de las señales individuales:

$$E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

$$E_y = \int_{-\infty}^{\infty} |y(t)|^2 dt$$

Sustituimos y obtenemos el resultado final demostrado:

$$E_z = E_x + E_y$$

---

### **Resultado Destacado**

$$\bbox[border: 2px solid #005F73, 12px]{ E_{x \pm y} = E_x + E_y }$$

¡Demostración completada de forma totalmente rigurosa para el caso general complejo!

---
---

# E10

### **Enunciado**

Derivar una expresión para la **potencia promedio** de la siguiente señal de tiempo continuo:

$$x(t) = A_1\cos(\Omega_1 t + \theta_1) + A_2\cos(\Omega_2 t + \theta_2)$$

para la condición de frecuencias idénticas:

$$\Omega_1 = \Omega_2 = \Omega$$

---

### **Desarrollo paso a paso**

#### **1. Expresión de la señal bajo la condición dada**

Al aplicar la igualdad de frecuencias $\Omega_1 = \Omega_2 = \Omega$, la señal se reduce a:

$$x(t) = A_1\cos(\Omega t + \theta_1) + A_2\cos(\Omega t + \theta_2)$$

Esta señal resultante es periódica con un período fundamental común $T_0 = \dfrac{2\pi}{\Omega}$.

#### **2. Definición de la potencia promedio**

La potencia promedio temporal $P_x$ de una señal periódica en tiempo continuo sobre un período completo $T_0$ está dada por la integral:

$$P_x = \dfrac{1}{T_0} \int_{0}^{T_0} x^2(t) dt$$

#### **3. Expansión cuadrática del integrando $x^2(t)$**

Elevamos la expresión de $x(t)$ al cuadrado aplicando el trinomio cuadrado perfecto:

$$x^2(t) = \left[ A_1\cos(\Omega t + \theta_1) + A_2\cos(\Omega t + \theta_2) \right]^2$$

$$x^2(t) = A_1^2\cos^2(\Omega t + \theta_1) + A_2^2\cos^2(\Omega t + \theta_2) + 2A_1 A_2\cos(\Omega t + \theta_1)\cos(\Omega t + \theta_2)$$

Sustituimos esto dentro de la integral de potencia:

$$P_x = \dfrac{1}{T_0} \int_{0}^{T_0} \left[ A_1^2\cos^2(\Omega t + \theta_1) + A_2^2\cos^2(\Omega t + \theta_2) + 2A_1 A_2\cos(\Omega t + \theta_1)\cos(\Omega t + \theta_2) \right] dt$$

Por linealidad de la integración, podemos segmentar la expresión en tres términos individuales:

$$P_x = I_1 + I_2 + I_3$$

Donde:

$$\begin{array}{rcl} I_1 & = & \dfrac{A_1^2}{T_0} \int_{0}^{T_0} \cos^2(\Omega t + \theta_1) dt \\ I_2 & = & \dfrac{A_2^2}{T_0} \int_{0}^{T_0} \cos^2(\Omega t + \theta_2) dt \\ I_3 & = & \dfrac{2 A_1 A_2}{T_0} \int_{0}^{T_0} \cos(\Omega t + \theta_1)\cos(\Omega t + \theta_2) dt \end{array}$$

---

#### **4. Evaluación de las integrales individuales**

- **Términos de potencia individuales ($I_1$ e $I_2$):** Utilizamos la identidad trigonométrica del ángulo medio, $\cos^2(\alpha) = \dfrac{1 + \cos(2\alpha)}{2}$:

$$\begin{array}{rcl} I_1 & = & \dfrac{A_1^2}{T_0} \int_{0}^{T_0} \left[ \dfrac{1 + \cos(2\Omega t + 2\theta_1)}{2} \right] dt \\ & = & \dfrac{A_1^2}{2T_0} \left[ \int_{0}^{T_0} 1 \cdot dt + \int_{0}^{T_0} \cos(2\Omega t + 2\theta_1) dt \right] \end{array}$$

    Dado que la integral de cualquier sinusoide armónica pura $\cos(2\Omega t + 2\theta_1)$ evaluada sobre un número entero de sus períodos (en este caso, dos ciclos completos de frecuencia $2\Omega$ dentro de $T_0$) es **idénticamente nula**:

$$\int_{0}^{T_0} \cos(2\Omega t + 2\theta_1) dt = 0$$

    Por lo tanto, el término se reduce a:

$$I_1 = \dfrac{A_1^2}{2\bcancel{T_0}} [\bcancel{T_0} + 0] = \dfrac{A_1^2}{2}$$

    Siguiendo un análisis idéntico para $I_2$:

$$I_2 = \dfrac{A_2^2}{2}$$

- **Término de acoplamiento de fase ($I_3$):** Utilizamos la identidad trigonométrica del producto de cosenos, $\cos(\alpha)\cos(\beta) = \dfrac{1}{2}\left[\cos(\alpha - \beta) + \cos(\alpha + \beta)\right]$:

$$\cos(\Omega t + \theta_1)\cos(\Omega t + \theta_2) = \dfrac{1}{2}\left[\cos(\theta_1 - \theta_2) + \cos(2\Omega t + \theta_1 + \theta_2)\right]$$

    Sustituimos esta equivalencia en la integral para $I_3$:

$$\begin{array}{rcl} I_3 & = & \dfrac{\bcancel{2} A_1 A_2}{T_0} \int_{0}^{T_0} \dfrac{1}{\bcancel{2}} \left[ \cos(\theta_1 - \theta_2) + \cos(2\Omega t + \theta_1 + \theta_2) \right] dt \\ & = & \dfrac{A_1 A_2}{T_0} \left[ \int_{0}^{T_0} \cos(\theta_1 - \theta_2) dt + \int_{0}^{T_0} \cos(2\Omega t + \theta_1 + \theta_2) dt \right] \end{array}$$

    Nuevamente, el término oscilatorio con frecuencia doble se anula al integrarse en el período fundamental:

$$\int_{0}^{T_0} \cos(2\Omega t + \theta_1 + \theta_2) dt = 0$$

    Por otro lado, la expresión **$\cos(\theta_1 - \theta_2)$ es una constante independiente del tiempo $t$**. Su integral sobre el período es simplemente la constante multiplicada por la duración del intervalo $T_0$:

$$\int_{0}^{T_0} \cos(\theta_1 - \theta_2) dt = T_0 \cos(\theta_1 - \theta_2)$$

    Reemplazando esto en la ecuación de $I_3$:

$$I_3 = \dfrac{A_1 A_2}{\bcancel{T_0}} \left[ \bcancel{T_0} \cos(\theta_1 - \theta_2) \right] = A_1 A_2 \cos(\theta_1 - \theta_2)$$

---

#### **5. Suma de componentes y resultado final**

Reuniendo los resultados parciales de cada una de las integrales, obtenemos la potencia promedio de la señal combinada:

$$\bbox[border: 2px solid #005F73, 12px]{ P_x = \dfrac{A_1^2}{2} + \dfrac{A_2^2}{2} + A_1 A_2 \cos(\theta_1 - \theta_2) }$$

---

### **Análisis Físico y Visualización**

Este resultado es sumamente interesante porque demuestra que cuando dos señales tienen la misma frecuencia, **su potencia total no es simplemente la suma de las potencias individuales**, sino que está fuertemente influenciada por la **interferencia de fase**:

1. **Constructiva pura** (Fases iguales, $\theta_1 - \theta_2 = 0$): $P_x = \dfrac{(A_1+A_2)^2}{2}$.
2. **Destructiva pura** (Fases opuestas, $\theta_1 - \theta_2 = \pi$): $P_x = \dfrac{(A_1-A_2)^2}{2}$.

Grafiquemos en Desmos las señales componentes y la resultante para amplitudes $A_1 = 3$, $A_2 = 2$ y un desfase parcial de $\theta_1 - \theta_2 = \dfrac{\pi}{3}$:

```desmos-graph
left=-2; right=8; bottom=-6; top=6;
width=500; height=250;
---
y=3*\cos(x) | -2<=x<=8 | #005F73
y=2*\cos(x - \pi/3) | -2<=x<=8 | #EE9B00
y=3*\cos(x) + 2*\cos(x - \pi/3) | -2<=x<=8 | #0A9396
```

- _Curva azul petróleo (`#005F73`): componente $x_1(t) = 3\cos(t)$._
- _Curva ámbar (`#EE9B00`): componente desfasada $x_2(t) = 2\cos(t - \pi/3)$._
- _Curva verde azulado (`#0A9396`): señal resultante $x(t) = x_1(t) + x_2(t)$ cuya amplitud refleja la potencia final calculada._

---
---

# E11

### **Enunciado**

Determinar la potencia promedio temporal ($P_x$) de la señal exponencial compleja de tiempo continuo:

$$x(t) = Ae^{j\Omega t}$$

donde $A$ es, en general, una amplitud compleja.

---

### **Desarrollo paso a paso**

#### **1. Magnitud al cuadrado de la señal compleja**

Para calcular la potencia de una señal compleja, primero debemos hallar su magnitud o valor absoluto al cuadrado, $|x(t)|^2$.

Representando la amplitud $A$ en su forma polar como $A = |A|e^{j\theta}$ (donde $|A|$ es su magnitud real y $\theta$ su fase inicial):

$$x(t) = |A|e^{j\theta} e^{j\Omega t} = |A|e^{j(\Omega t + \theta)}$$

Ahora, calculamos la magnitud al cuadrado de la señal, recordando que la magnitud de cualquier exponencial compleja con exponente puramente imaginario es siempre igual a la unidad ($|e^{j\alpha}| = 1$):

$$\begin{array}{rcl} |x(t)|^2 & = & \left| |A| e^{j(\Omega t + \theta)} \right|^2 \\ & = & |A|^2 \cdot \underbrace{\left| e^{j(\Omega t + \theta)} \right|^2}_{1} \\ & = & |A|^2 \end{array}$$

_Nota de comprensión:_ A diferencia de los cosenos reales que oscilan entre $-A$ y $A$, la exponencial compleja representa un fasor giratorio en el plano complejo cuyo radio es constante e igual a $|A|$. Por lo tanto, su magnitud al cuadrado no varía con el tiempo.

---

### **Visualización de la señal**

Para visualizar intuitivamente este comportamiento, grafiquemos en Desmos la parte real de la señal $\text{Re}\{x(t)\} = |A|\cos(\Omega t)$ (que sí oscila) junto a su magnitud absoluta constante $|x(t)| = |A|$ (para valores ilustrativos de $|A| = 3$ y $\Omega = 2$):

```desmos-graph
left=-5; right=5; bottom=-4; top=4;
width=500; height=250;
---
y=3 | -5<=x<=5 | #EE9B00
y=3*\cos(2*x) | -5<=x<=5 | #005F73
```

- _Curva azul petróleo (`#005F73`): parte real oscilatoria de la señal, $\text{Re}\{x(t)\} = 3\cos(2t)$._
- _Línea ámbar (`#EE9B00`): magnitud constante de la envolvente, $|x(t)| = 3$._

---

#### **2. Cálculo de la potencia promedio**

Podemos realizar el cálculo por dos caminos formales que conducen exactamente al mismo resultado:

##### **Método A: Definición por límite de intervalo infinito**

La definición general de la potencia promedio para cualquier señal en tiempo continuo es:

$$P_x = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt$$

Sustituyendo nuestra magnitud al cuadrado $|x(t)|^2 = |A|^2$:

$$P_x = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |A|^2 dt$$

Dado que $|A|^2$ es una constante respecto al tiempo $t$, sale de la integral:

$$\begin{array}{rcl} P_x & = & \lim_{T \to \infty} \dfrac{|A|^2}{T} \int_{-T/2}^{T/2} 1 \cdot dt \\ & = & \lim_{T \to \infty} \dfrac{|A|^2}{T} \Big[ t \Big]_{-T/2}^{T/2} \\ & = & \lim_{T \to \infty} \dfrac{|A|^2}{T} \left[ \dfrac{T}{2} - \left( -\dfrac{T}{2} \right) \right] \\ & = & \lim_{T \to \infty} \dfrac{|A|^2}{\bcancel{T}} \left( \bcancel{T} \right) \\ & = & |A|^2 \end{array}$$

---

##### **Método B: Integración sobre su período fundamental**

Como la señal $x(t) = Ae^{j\Omega t}$ es periódica con un período fundamental $T_0 = \dfrac{2\pi}{\Omega}$ (asumiendo $\Omega \neq 0$), su potencia promedio se simplifica calculando la energía media en un solo período completo:

$$P_x = \dfrac{1}{T_0} \int_{0}^{T_0} |x(t)|^2 dt$$

Sustituyendo $|x(t)|^2 = |A|^2$:

$$\begin{array}{rcl} P_x & = & \dfrac{1}{T_0} \int_{0}^{T_0} |A|^2 dt \\ & = & \dfrac{|A|^2}{T_0} \int_{0}^{T_0} 1 \cdot dt \\ & = & \dfrac{|A|^2}{\bcancel{T_0}} \Big( \bcancel{T_0} \Big) \\ & = & |A|^2 \end{array}$$

---

### **Resultado Destacado**

$$\bbox[border: 2px solid #005F73, 12px]{ P_x = |A|^2 }$$

_(Nota: Si asumimos que la amplitud $A$ es un parámetro real, el resultado se simplifica directamente a $P_x = A^2$)._
