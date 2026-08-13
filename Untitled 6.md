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
