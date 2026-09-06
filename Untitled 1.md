## Prioridad del DMA sobre el acceso al bus de la CPU

1. Definición formal — del libro fuente, sin parafrasear.

* "En casi todos los sistemas que tienen módulos de DMA, el acceso del módulo de DMA a memoria principal tiene más prioridad que el acceso de la CPU a memoria principal".
* "During DMA transfer, the CPU is idle and has no control of the memory buses. A DMA controller takes over the buses to manage the transfer directly between the I/O device and memory".
* "For some devices, a delay in gaining access to the bus may lead to an error. Such devices must be given high priority".

2. Idea clave — propiedad central no capturada por la definición.

La CPU es un dispositivo síncrono interno cuya marcha se puede pausar temporalmente sin perder información, mientras que los dispositivos de E/S rápidos operan en tiempo real y sufren pérdidas de datos irreversibles (*buffer overflow*) si el bus no se les concede de inmediato.

3. Figura o diagrama (si existe o aplica)

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[node distance=2cm, auto, >=Latex, thick,
    block/.style={rectangle, draw, fill=blue!5, text width=3.2cm, text centered, minimum height=1.2cm, rounded corners}]
    
    \node [block] (cpu) {CPU};
    \node [block, right=4cm of cpu] (dma) {Controlador DMA};
    \node [block, below=2.5cm of cpu, xshift=3.6cm] (ram) {Memoria Principal (RAM)};
    
    % Líneas de control handshake para arbitraje
    \draw [->, transform canvas={yshift=0.15cm}] (dma) -- node[above, scale=0.8] {BR (Bus Request)} (cpu);
    \draw [<-, transform canvas={yshift=-0.15cm}] (dma) -- node[below, scale=0.8] {BG (Bus Grant)} (cpu);
    
    % Buses de datos, direcciones y control
    \draw [double, <->] (cpu) -- node[left, scale=0.8, align=center] {Buses de Sistema\\(Alta Impedancia si BG=1)} (ram);
    \draw [double, <->] (dma) -- node[right, scale=0.8, align=center] {Buses de Sistema\\(Activos si BG=1)} (ram);
    
\end{tikzpicture}
\end{document}
```

4. Ejercicios resueltos (solo nivel C)

##### Ej. Ralentización del procesador por robo de ciclos de DMA

**Resolución**
Determinación del impacto cuantitativo sobre el rendimiento de la CPU debido al robo de ciclos de bus por transferencias síncronas de un dispositivo de E/S.

**Datos del enunciado:**
*   Velocidad de transmisión del periférico: $9600\text{ bps}$.
*   Tasa de captación/ejecución del procesador: $1\text{ MIPS}$ (un millón de instrucciones por segundo).
*   Se asume transmisión de caracteres estándar de $8\text{ bits}$ ($1\text{ byte}$ por transferencia) en modo robo de ciclo (*cycle stealing*).

**Paso 1:** Calcular la tasa de transferencias de caracteres por segundo hacia la memoria.

$$
\text{Tasa de caracteres} = \frac{\text{Velocidad de transmisión}}{\text{Bits por carácter}}
$$


$$
\text{Tasa de caracteres} = \frac{9600\text{ bps}}{8\text{ bits}} = 1200\text{ caracteres/s}
$$


**Paso 2:** Determinar la cantidad de ciclos de bus robados al procesador. Puesto que cada carácter transferido requiere un ciclo de bus exclusivo de memoria:

$$
\text{Ciclos robados por segundo} = 1200\text{ ciclos/s}
$$


**Paso 3:** Calcular la fracción de ralentización que experimenta el procesador respecto a su capacidad máxima de bus ($1,000,000\text{ ciclos/s}$):

$$
\text{Ralentización} = \frac{\text{Ciclos robados por segundo}}{\text{Frecuencia de bus de la CPU}}
$$


$$
\text{Ralentización} = \frac{1200}{1,000,000} = 0.0012
$$


$$
\therefore\quad \color{orange}{0.12\%}
$$

