Una **señal de potencia** es aquella que se mantiene activa de forma permanente a lo largo del tiempo sin decaer a cero, por lo que su **energía total acumulada es infinita**. Como no podemos medir su energía de forma directa porque no converge, los ingenieros analizamos su **potencia promedio**, que representa el ritmo con el que la señal consume o entrega energía por unidad de tiempo.

Formalmente, una señal es de potencia si su potencia promedio normalizada $P$ es **finita y distinta de cero** $$0 < P < \infty$$.

---

### Definición Matemática

Para una señal continua $x(t)$, la **potencia promedio normalizada** $calculada sobre una resistencia hipotética de $1\ \Omega$$ se define como:

$$
P = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt
$$

#### El Caso de las Señales Periódicas

Si la señal es periódica con un período fundamental $T_0$ (es decir, cumple que $x(t) = x(t + T_0)$), la potencia promedio a lo largo de toda su historia infinita es idéntica a la potencia promedio calculada **en un único período**. Esto simplifica enormemente el análisis matemático:

$$
P = \dfrac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x(t)|^2 dt
$$

---

### Ejemplo Clásico: La Onda Senoidal

Consideremos la señal de voltaje dada por:

$$
x(t) = 2 \cos(2t)
$$

Esta es una señal continua y periódica, con amplitud $A = 2\text{ V}$ y frecuencia angular $\omega_0 = 2\text{ rad/s}$. Su período fundamental es:

$$
T_0 = \dfrac{2\pi}{\omega_0} = \dfrac{2\pi}{2} = \pi\text{ segundos}
$$

Grafiquemos esta señal senoidal para visualizar su comportamiento continuo y oscilatorio a lo largo del tiempo:

```
left=-5; right=5; bottom=-3; top=3; width=550; height=200;
---
y=2\cos(2x)|#005F73
```

Como la señal no se apaga nunca, su energía total integrada es infinita. Calculemos su potencia promedio evaluando un solo período $$T_0 = \pi$$:

$$
P = \dfrac{1}{\pi} \int_{-\pi/2}^{\pi/2} |2\cos(2t)|^2 dt
$$

$$
P = \dfrac{4}{\pi} \int_{-\pi/2}^{\pi/2} \cos^2(2t) dt
$$

Aplicamos la identidad trigonométrica del ángulo doble $\cos^2(u) = \dfrac{1 + \cos(2u)}{2}$:

$$
P = \dfrac{4}{\pi} \int_{-\pi/2}^{\pi/2} \left( \dfrac{1 + \cos(4t)}{2} \right) dt
$$

$$
P = \dfrac{2}{\pi} \int_{-\pi/2}^{\pi/2} (1 + \cos(4t)) dt
$$

$$
P = \dfrac{2}{\pi} \left[ t + \dfrac{\sin(4t)}{4} \right]_{-\pi/2}^{\pi/2}
$$

Evaluando los límites de integración obtenemos:

$$
P = \dfrac{2}{\pi} \left[ \left( \dfrac{\pi}{2} + \dfrac{\sin(2\pi)}{4} \right) - \left( -\dfrac{\pi}{2} + \dfrac{\sin(-2\pi)}{4} \right) \right]
$$

Dado que $\sin(2\pi) = 0$ y $\sin(-2\pi) = 0$:

$$
P = \dfrac{2}{\pi} \left( \dfrac{\pi}{2} - \left( -\dfrac{\pi}{2} \right) \right) = \dfrac{2}{\pi} (\pi) = 2\text{ W}
$$

Destacamos nuestro resultado bajo la jerarquía de examen:

$$
\bbox[5px, border: 2px solid \#005F73]{P = 2\text{ W}}
$$

Dado que $0 < P < \infty$, **la señal $x(t) = 2\cos(2t)$ es rigurosamente una señal de potencia**. En general, cualquier senoidal pura de la forma $A \cos(\omega_0 t + \theta)$ tiene una potencia constante de $\dfrac{A^2}{2}$, independientemente de su frecuencia y fase.

---

### Preguntas de Comprensión Conceptual

1. **¿Por qué una señal periódica no nula siempre tiene energía total infinita?** _(Pista: Piensa en qué ocurre al sumar o integrar áreas positivas idénticas de forma infinita)._
2. **Si una señal física tiene energía total finita $$E < \infty$$, ¿cuál es necesariamente su potencia promedio en el intervalo de $-\infty$ a $\infty$?**.
3. **¿Puede un dispositivo real y físico generar una señal de potencia pura en la práctica?** _(Pista: Considera las restricciones de almacenamiento de energía y el tiempo de vida útil de los componentes físicos)._

---

### Ejercicios de Refuerzo Resueltos

#### Ejercicio 1 (Señal Continua Compleja - Rao Cap. 1)

**Determine si la señal exponencial compleja $x(t) = e^{j\left(2t + \dfrac{\pi}{4}\right)}$ es de energía o de potencia, y calcule sus valores correspondientes**.

**Desarrollo:**

1. Analizamos la magnitud cuadrática de la señal compleja. Recordamos que para cualquier exponente complejo puro $|e^{j\theta}| = 1$: $$
|x(t)|^2 = \left| e^{j\left(2t + \dfrac{\pi}{4}\right)} \right|^2 = (1)^2 = 1
$$
    
2. Calculamos la energía total $E$: $$
E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} 1 \cdot dt = \infty
$$ Dado que $E = \infty$, la señal no es de energía.
    
3. Calculamos la potencia promedio infinita $P$: 
$$
P = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt = \lim_{T \to \infty} \dfrac{1}{T} \int_{-T/2}^{T/2} 1 \cdot dt
$$
$$
P = \lim_{T \to \infty} \dfrac{1}{T} [t]_{-T/2}^{T/2} = \lim_{T \to \infty} \dfrac{1}{T} \left( \dfrac{T}{2} - \left(-\dfrac{T}{2}\right) \right) = \lim_{T \to \infty} \dfrac{\cancel{T}}{\cancel{T}} = 1\text{ W}
$$
    

**Resultado:** La potencia promedio es finita y no nula $$1\text{ W}$$. Por lo tanto: 
$$
\bbox[5px, border: 2px solid \#005F73]{P = 1\text{ W} \quad (\text{Señal de Potencia})}
$$

---

#### Ejercicio 2 (Secuencia Discreta - Rao Cap. 6 / Hsu Schaum Cap. 1)

**Determine si la señal en tiempo discreto $x[n] = (0.5)^n u[n]$ es de energía, de potencia o ninguna, y calcule sus valores**.

**Desarrollo:**

1. Planteamos la ecuación de energía para señales discretas. Debido al escalón unitario discreto $u[n]$, los límites de la sumatoria se reducen de $0$ a $\infty$: 
$$
E = \sum_{n=-\infty}^{\infty} |x[n]|^2 = \sum_{n=0}^{\infty} |(0.5)^n|^2 = \sum_{n=0}^{\infty} (0.25)^n
$$
    
2. Aplicamos la fórmula de sumatoria para series geométricas infinitas $\sum_{n=0}^{\infty} a^n = \dfrac{1}{1-a}$ para $|a| < 1$: 

$$
E = \dfrac{1}{1 - 0.25} = \dfrac{1}{0.75} = \dfrac{4}{3}\text{ J}
$$
    
3. Dado que la energía total es finita $$E = \dfrac{4}{3}\text{ J}$$, la señal se clasifica como una **señal de energía**. Su potencia promedio debe ser, por definición, igual a cero. Comprobémoslo aplicando el límite: 
$$
P = \lim_{N \to \infty} \dfrac{1}{2N + 1} \sum_{n=0}^{N} (0.25)^n
$$
$$
P = \lim_{N \to \infty} \dfrac{1}{2N + 1} \left( \dfrac{1 - (0.25)^{N+1}}{1 - 0.25} \right) = \lim_{N \to \infty} \dfrac{4}{3(2N + 1)} \left(1 - \cancelto{0}{(0.25)^{N+1}}\right) = 0\text{ W}
$$
    

**Resultado:** 
$$
\bbox[5px, border: 2px solid \#005F73]{E = \dfrac{4}{3}\text{ J} \quad (\text{Señal de Energía})}
$$

---

📊 ¿Te gustaría que analicemos la potencia de otras señales periódicas de mayor complejidad en ingeniería, como un tren de pulsos rectangulares u ondas dientes de sierra?

