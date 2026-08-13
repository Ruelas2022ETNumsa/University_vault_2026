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
