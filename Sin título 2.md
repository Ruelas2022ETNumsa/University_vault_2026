Un **sistema variante en el tiempo** (o variable en el tiempo) es aquel cuyas propiedades, comportamiento o características físicas cambian activamente a lo largo del tiempo [1-3]. En estos sistemas, la respuesta ante una señal de entrada específica depende directamente del instante de tiempo en el cual se aplica dicha entrada [1].

En contraste, un sistema es **invariante en el tiempo** si un desplazamiento temporal en la señal de entrada produce únicamente el mismo desplazamiento temporal en la salida [2, 4, 5]. Si un sistema no cumple con esta propiedad de constancia, se clasifica como **variante en el tiempo** [6, 7].

---

### **Prueba Analítica de Variación Temporal**
Para determinar analíticamente si un sistema es variante en el tiempo, se realiza una prueba matemática comparando dos señales de salida obtenidas por diferentes caminos [2, 7-9]:

1. **Desplazamiento en la salida:** Se evalúa la respuesta del sistema, \\(y(t)\\) o \\(y[n]\\), ante una entrada genérica \\(x(t)\\) o \\(x[n]\\), y luego se le aplica un retraso temporal directo de \\(t_0\\) (o \\(n_0\\) muestras en tiempo discreto), resultando en \\(y(t-t_0)\\) o \\(y[n-n_0]\\) [2, 7, 8].
2. **Respuesta a la entrada desplazada:** Se calcula la salida del sistema, \\(y_d(t)\\) o \\(y_d[n]\\), cuando la señal de entrada se desplaza *antes* de ingresar al sistema, es decir, introduciendo \\(x(t-t_0)\\) o \\(x[n-n_0]\\) en el operador de transformación [2, 7, 8].

Si el sistema es **variante en el tiempo**, estas señales **no coinciden** para alguna entrada o retraso [6, 7, 10]:
\\[y(t-t_0) \neq T[x(t-t_0)] \quad \text{o bien} \quad y[n-n_0] \neq T[x[n-n_0]]\\]

---

### **Ejemplos Comunes de Sistemas Variantes en el Tiempo**

*   **Sistemas con ganancia variable (Multiplicadores de tiempo):**
    Sistemas descritos por \\(y(t) = t \cdot x(t)\\) o \\(y[n] = n \cdot x[n]\\) varían con el tiempo debido a que su factor de ganancia se modifica en cada instante de tiempo [11, 12].
    *   *Ejemplo en tiempo discreto:* Si ingresamos \\(x_1[n] = \delta[n]\\), la salida es \\(y_1[n] = n\delta[n] = 0\\) [12, 13]. Si retrasamos la entrada por una muestra, \\(x_2[n] = \delta[n-1]\\), la salida resultante es \\(y_2[n] = n\delta[n-1] = \delta[n-1]\\) [13]. Como la salida original desplazada una muestra es \\(y_1[n-1] = 0\\), y esto no coincide con la salida real \\(y_2[n]\\), el sistema es variante en el tiempo [12, 13].
    *   Otros casos análogos continuos con ganancias exponenciales o senoidales variables son \\(y(t) = e^{-t}x(t)\\) o \\(y(t) = \sin(2t)x(t)\\) [6, 14].

*   **Escalamiento de tiempo (Time Scaling):**
    Sistemas de compresión de tiempo o submuestreo descritos por \\(y(t) = x(2t)\\) o \\(y[n] = x[2n]\\) son variantes en el tiempo [15, 16]. Cualquier retraso temporal en la entrada se comprime por un factor de dos en la escala de tiempo de la salida, impidiendo que se mantenga la invariancia temporal directa [16, 17].

*   **Inversión temporal (Time Reversal):**
    Sistemas que realizan una reflexión del tiempo, como \\(y(t) = x(-t)\\) o \\(y[n] = x[-n]\\), varían con el tiempo [18, 19]. Esto se debe a que un desplazamiento hacia la derecha en la entrada (retraso antes de procesar) se traduce en un desplazamiento hacia la izquierda (adelanto) en la salida tras aplicar la inversión de signo al tiempo [20].

*   **Ejemplo físico: El cohete impulsor de la NASA**
    El transbordador espacial responde a la segunda ley de Newton: \\(f_z(t) = M(t)\frac{d^2 z(t)}{dt^2}\\) [1]. Dado que la masa del cohete \\(M(t)\\) disminuye de manera continua y drástica a medida que se quema y consume el combustible, el modelo dinámico que lo describe cambia sus parámetros con el tiempo, convirtiéndolo en un ejemplo físico clásico de variación temporal [1, 3].

---

IMA-SRC | fuente: Oppenheim & Willsky-Signals and Systems-2th ed-1to5.pdf | página: 52 | id: Figure 1.47 | posición: parte central e inferior de la página
justificación: Esta figura ilustra un contraejemplo de escalamiento temporal donde la respuesta del sistema ante una entrada desplazada no es igual a la salida original desplazada, demostrando la variación temporal del sistema.

IMA-SRC | fuente: Charles L. Phillips John Parr Eve Riskin-Signals, Systems, and Transforms-4th ED.pdf | página: 74 | id: Figure 2.45 | posición: parte central de la página
justificación: Esta figura muestra la prueba gráfica de variación en el tiempo para un sistema que realiza inversión temporal sobre una señal escalón unitario.

---

📊 ¿Te gustaría que analicemos algún ejemplo o ejercicio en particular de tus fuentes para verificar paso a paso si es variante en el tiempo?
