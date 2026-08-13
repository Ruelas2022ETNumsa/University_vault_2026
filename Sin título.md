En el procesamiento digital de señales, el **tiempo real** se refiere a la capacidad de un sistema para procesar una señal **a medida que esta ocurre** en el mundo físico [1, 2]. No se trata simplemente de que el proceso sea "rápido", sino de que el sistema cumpla con restricciones temporales estrictas dictadas por la frecuencia de muestreo [3].

---

### MODO 1 · EXPLICACIÓN DE CONCEPTO

#### 1. Nivel Intuitivo
Imagina que estás hablando por un teléfono digital. Para que la comunicación sea fluida, el procesador del teléfono debe tomar tu voz, convertirla a números, procesarla y enviarla antes de que llegue el siguiente "pedacito" (muestra) de tu voz. Si el procesador tarda más tiempo en calcular que el tiempo que tarda la voz en llegar, las muestras empezarían a acumularse, generando un retraso (latencia) cada vez mayor hasta que el sistema falle. Procesar en **tiempo real** es como correr en una cinta de gimnasia: debes mantener el ritmo de la cinta o te caerás [4].

#### 2. Definición Formal y Restricción Computacional
Para un sistema que opera con un periodo de muestreo \\(T_s\\) (el tiempo entre una muestra y la siguiente), el tiempo total de procesamiento por muestra (\\(T_{proc}\\)) debe ser menor que dicho periodo [3, 5]:

\\[T_{proc} < T_s\\]

Donde \\(T_{proc}\\) incluye:
1. El tiempo para leer la entrada \\(x[n]\\) [3].
2. El tiempo para ejecutar el algoritmo (como un filtro FIR) [3].
3. El tiempo para entregar la salida \\(y[n]\\) [5].

Si la señal se muestrea a \\(8\text{ kHz}\\), el sistema tiene exactamente \\(1/8000 = 125\ \mu\text{s}\\) para hacer todos los cálculos antes de que llegue la siguiente muestra [5, 6].

#### 3. Conexión con los Libros Fuente
*   **Causalidad:** Según **Oppenheim**, los sistemas en tiempo real deben ser necesariamente **causales**, ya que "en tiempo real... nunca conocemos los valores futuros de una señal" [1, 2]. El sistema solo puede responder a lo que ya ha ocurrido o está ocurriendo [7, 8].
*   **Implementación:** **Hayes** destaca que en aplicaciones de tiempo real, el uso de chips **DSP** es crucial porque están optimizados para realizar operaciones de suma y multiplicación $MAC$ en un solo ciclo de reloj, maximizando el número de instrucciones posibles dentro de la ventana \\(T_s\\) [3, 9].

#### 4. Representación Visual
Un sistema de procesamiento en tiempo real se puede ver como un flujo continuo donde la restricción de tiempo es la clave:

```tikz
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.2, auto, >=stealth]
    % Nodos
    \node (input) at (0,0) {$x[n]$};
    \node [draw, rectangle, minimum height=1.2cm, minimum width=2.2cm, fill=teal!10, draw=teal, thick] (system) at (3,0) {Procesador DSP};
    \node (output) at (6,0) {$y[n]$};
    
    % Flechas
    \draw [->, thick, orange] (input) -- (system) node[midway, above] {\small Muestras};
    \draw [->, thick, teal] (system) -- (output);
    
    % Restricción
    \node [below of=system, node distance=1cm, text=red] {\textbf{Restricción: } $T_{proc} < T_s$};
    
    % Línea de tiempo
    \draw [->, gray, dashed] (-0.5,-1.5) -- (6.5,-1.5) node[right] {$t$};
    \foreach \x in {0,1,2,3,4,5,6}
        \draw (\x,-1.6) -- (\x,-1.4);
    \node at (0,-1.8) {\small $n$};
    \node at (1,-1.8) {\small $n+1$};
    \draw [<->, blue] (0,-2.1) -- (1,-2.1) node[midway, below] {$T_s$};
\end{tikzpicture}
\end{document}
```

---

### Preguntas de Comprensión Conceptual

1.  **¿Por qué un sistema no causal no puede operar en tiempo real?** *(Pista: Piensa en la disponibilidad de los datos en el momento del cálculo [1]).*
2.  **Si aumentamos la frecuencia de muestreo de un sistema, ¿se vuelve más fácil o más difícil procesar en tiempo real?** *(Considera qué pasa con el valor de \\(T_s\\) [5]).*
3.  **¿Qué sucede si un algoritmo de filtrado requiere más ciclos de reloj de los que el procesador puede ofrecer en un intervalo \\(T_s\\)?**

---

### Ejercicios de Refuerzo Resueltos

#### Ejercicio 1 (Restricción de Hardware - Hayes Cap. 8)
**Un chip DSP tiene un ciclo de instrucción de \\(100\text{ ns}\\). Para procesar una muestra, requiere 1 instrucción de lectura, 1 de salida, 8 de control y \\(N+1\\) instrucciones para un filtro FIR. Determine el ancho de banda máximo (frecuencia de muestreo \\(f_s\\)) que puede procesar si el filtro es de orden \\(N=255\\)** [3, 5].

**Desarrollo:**
1.  Calculamos el número total de instrucciones por muestra (\\(I\\)):
    \\[I = 1_{\text{read}} + 1_{\text{write}} + 8_{\text{ctrl}} + $255 + 1$_{\text{filter}} = 266 \text{ instrucciones}\\]
2.  Calculamos el tiempo total de procesamiento (\\(T_{proc}\\)):
    \\[T_{proc} = I \cdot \text{tiempo\_ciclo} = 266 \cdot 100\text{ ns} = 26.6\ \mu\text{s}\\]
3.  Para tiempo real, \\(T_s > T_{proc}\\). El límite crítico es \\(T_s = 26.6\ \mu\text{s}\\):
    \\[f_s = \dfrac{1}{T_s} = \dfrac{1}{26.6 \cdot 10^{-6}} \approx 37.59\text{ kHz}\\]

**Resultado:**
\\[\bbox[5px, border: 2px solid #005F73]{f_s \leq 37.59\text{ kHz}}\\]

---

#### Ejercicio 2 (Procesamiento de Voz - Hayes Cap. 7)
**Una señal de voz se muestrea a \\(10\text{ kHz}\\). El procesamiento consiste en bloques de \\(1024\\) valores. Si el sistema tarda \\(1\ \mu\text{s}\\) por cada multiplicación real y el algoritmo requiere realizar el equivalente a un producto de bloques que toma tiempo total \\(T_{alg} = 50\text{ ms}\\), determine si el sistema puede procesar la voz en tiempo real** [4].

**Desarrollo:**
1.  Calculamos el tiempo que tarda en "llenarse" un bloque de muestras (ventana de tiempo real):
    \\[T_{bloque} = \text{muestras} \cdot T_s = 1024 \cdot \dfrac{1}{10,000} = 102.4\text{ ms}\\]
2.  Comparamos con el tiempo de procesamiento:
    \\[T_{alg} = 50\text{ ms}\\]
3.  Como \\(50\text{ ms} < 102.4\text{ ms}\\), el procesador termina su tarea antes de que el siguiente bloque de datos esté listo.

**Resultado:**
\\[\bbox[5px, border: 2px solid #005F73]{\text{Sí, es tiempo real. Sobran } 52.4\text{ ms por bloque.}}\\]


