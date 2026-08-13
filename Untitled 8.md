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
