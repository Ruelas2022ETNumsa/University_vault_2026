## Prioridad de DMA sobre el acceso de la CPU al bus

1. Definición formal — del libro fuente, sin parafrasear.

> "el procesador cede a un módulo de E/S la autoridad para leer de o escribir en memoria, para que así la transferencia E/S-memoria pueda producirse sin la intervención del procesador. Durante esas transferencias, el módulo de E/S proporciona a la memoria las órdenes de lectura o escritura, liberando al procesador de cualquier responsabilidad en el intercambio. Esta operación se conoce con el nombre de acceso directo a memoria (DMA, Direct Memory Access)".

2. Idea clave — El DMA tiene prioridad absoluta porque los dispositivos de E/S operan en tiempo real; si se retrasan pueden perderse datos por desbordamiento, mientras que si la CPU se retrasa, solo se pausa temporalmente.

3. Figura o diagrama (si existe o aplica)

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    box/.style={draw, rectangle, minimum width=2.5cm, minimum height=1.2cm, align=center, font=\sffamily\small, thick},
    arrow/.style={-{Stealth[scale=1.0]}, thick, font=\sffamily\scriptsize}
]
    % Nodes
    \node[box] (cpu) {CPU};
    \node[box, right=3.5cm of cpu] (dma) {Controlador\\DMA};
    \node[box, below=2.5cm of cpu] (mem) {Memoria\\Principal};
    \node[box, right=3.2cm of dma] (io) {Dispositivo E/S\\(Periférico)};

    % Lines and labels
    \draw[arrow] (io.west) -- node[above] {Petición DMA} node[below] {(DREQ)} (dma.east);
    \draw[arrow] (dma.165) -- node[above] {Bus Request} node[below] {(BR / HOLD)} (cpu.15);
    \draw[arrow] (cpu.345) -- node[above] {Bus Grant} node[below] {(BG / HLDA)} (dma.195);
    \draw[arrow] (dma.south) -- node[below right, align=center] {Control de Bus\\(Direcciones, Datos, RD, WR)} (mem.east);
    \draw[arrow] (cpu.south) -- node[left, align=center] {Acceso síncrono\\(Buses de CPU)} (mem.north);
\end{tikzpicture}
\end{document}
```

4. Ejercicios resueltos (solo nivel C)

##### Ej. Ralentización de la CPU por transferencia DMA en modo de robo de ciclo

**Resolución**
Calcular el número de ciclos de bus robados por segundo por el controlador de DMA y compararlo con la tasa de procesamiento de la CPU.

1. Identificar la velocidad de transmisión del periférico: el dispositivo transmite caracteres a una tasa de \\(2400 \text{ caracteres/s}\\).
2. Determinar el tamaño de palabra de la memoria: cada transferencia DMA maneja palabras de \\(16\text{-bits}\\).
3. Dado que un carácter estándar equivale a \\(8 \text{ bits}\\) (\\(1\text{ byte}\\)), cada palabra de \\(16\text{-bits}\\) se compone de \\(2\text{ caracteres}\\):
\\[\text{Tasa de palabras} = \frac{2400 \text{ caracteres/s}}{2 \text{ caracteres/palabra}} = 1200 \text{ palabras/s}\\]
4. Como la transferencia se realiza mediante robo de ciclo (cycle stealing), cada palabra transferida roba exactamente un ciclo de bus a la CPU:
\\[\text{Ciclos robados} = 1200 \text{ ciclos/s}\\]
5. Determinar la tasa de captación y ejecución de la CPU: el procesador funciona a una tasa promedio de 1 MIPS (\\(1,000,000 \text{ instrucciones/s}\\)).
6. Asumiendo que el procesador utiliza un ciclo de bus para captar/ejecutar cada instrucción, calculamos la fracción de ralentización del procesador:
\\[\text{Ralentización} = \frac{1200 \text{ ciclos robados/s}}{1,000,000 \text{ ciclos totales/s}}\\]
\\[\text{Ralentización} = 0.0012 \times 100\% = 0.12\%\\]
\\[\therefore\quad \color{orange}{0.12\%}\\]