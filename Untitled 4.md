## Cycle stealing (robo de ciclo) — Prioridad del DMA

### 1. Definición formal
"Para hacerlo, el módulo de DMA debe utilizar sólo cuando el procesador no lo necesita, o debe forzar al procesador a que suspenda temporalmente su funcionamiento. Esta última técnica es la más común y se denomina robo de ciclo (cycle stealing), puesto que, en efecto, el módulo de DMA roba un ciclo de bus".

### 2. Propiedades y desarrollo
* **Pasos de operación del robo de ciclo**:
  1. Un dispositivo periférico de alta velocidad solicita una transferencia activando la señal de solicitud de DMA (`DREQ` o `DMA request`) hacia el controlador de DMA.
  2. El controlador de DMA solicita el control de los buses del sistema al procesador activando la línea de solicitud de bus (`HOLD` o `BR`).
  3. El procesador suspende su ejecución en su siguiente punto de ruptura (justo antes de que necesite utilizar los buses en su ciclo de instrucción).
  4. La CPU desconecta sus buffers colocando las líneas de dirección, datos y control en estado de alta impedancia y otorga el control de los buses mediante la señal de concesión (`HLDA` o `BG`).
  5. El controlador de DMA activa la señal de reconocimiento (`DACK` o `DMA acknowledge`) para indicar al periférico que la transferencia va a comenzar.
  6. El controlador de DMA coloca la dirección destino en el bus de direcciones y habilita las líneas de lectura/escritura en memoria (`RD`/`WR`), transfiriendo **un único dato** (palabra o byte) directamente entre el periférico y la memoria principal.
  7. El DMA incrementa su registro de dirección, decrementa el contador de palabras, desactiva la señal `HOLD`/`BR` y devuelve de forma inmediata el control del bus al procesador.

* **Diferencia clave con las interrupciones ordinarias**: A diferencia de una interrupción tradicional, en el robo de ciclo el procesador no tiene que guardar su contexto (como registros o el contador de programa) ni ejecutar una rutina de servicio de interrupción (ISR). Simplemente se "pausa" durante un único ciclo de bus. El único impacto es una ligera ralentización en la velocidad de ejecución de la CPU.

* **Justificación de la prioridad del DMA sobre la CPU (según Stallings)**:
  * **Integridad de datos en periféricos de tiempo real**: Los dispositivos de E/S rápidos (como discos magnéticos o tarjetas de red) operan a una velocidad constante que viene dictada por el medio físico o de transmisión. Si el controlador de DMA no obtiene acceso inmediato al bus de memoria en el instante en que el dato está listo, el flujo continuo de datos entrantes sobrescribirá el buffer del dispositivo antes de que pueda ser procesado, resultando en una **pérdida inevitable de datos** (data overrun).
  * **Inocuidad de la suspensión de la CPU**: La CPU es un elemento puramente electrónico controlado por reloj que retiene de manera completamente segura todo su estado interno por hardware al detenerse. Postergar el acceso al bus por parte de la CPU por uno o varios ciclos no genera ninguna pérdida de datos ni fallo operativo, limitándose únicamente a un retraso de rendimiento menor.
  * Por consiguiente, el acceso de los módulos de DMA a la memoria principal siempre recibe una **prioridad superior** que el acceso de la CPU.

### 3. Figura o diagrama

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    phase/.style={rectangle, draw=black, fill=blue!5, minimum width=2.1cm, minimum height=1.1cm, align=center, font=\tiny\sffamily},
    lbl/.style={draw, rectangle, rounded corners, font=\tiny\sffamily, align=center}
]

% Nodes for instruction cycle phases (Stallings Fig 7.12 / 8.13)
\node[phase] (P1) {Captación\\instrucción};
\node[phase, right=0.15cm of P1] (P2) {Decodificación\\instrucción};
\node[phase, right=0.15cm of P2] (P3) {Captación\\operando};
\node[phase, right=0.15cm of P3] (P4) {Ejecución\\instrucción};
\node[phase, right=0.15cm of P4] (P5) {Almacenar\\resultado};
\node[phase, right=0.15cm of P5] (P6) {Procesar\\interrupción};

% Labels for Breakpoints
\node[lbl, fill=red!10, below=1cm of P2, xshift=0.9cm] (dma) {Puntos de ruptura para el DMA\\(Justo antes de necesitar el bus de sistema)};
\node[lbl, fill=orange!15, below=1.8cm of P5, xshift=0.5cm] (intr) {Punto de ruptura para interrupción\\(Solo al finalizar el ciclo de instrucción)};

% Coordinates for boundaries
\path (P1.east) -- node(b1) {} (P2.west);
\path (P2.east) -- node(b2) {} (P3.west);
\path (P3.east) -- node(b3) {} (P4.west);
\path (P4.east) -- node(b4) {} (P5.west);
\path (P5.east) -- node(b5) {} (P6.west);

% Arrows for DMA breakpoints
\draw[-Stealth, red, thick] (dma.north) -- (b1.center);
\draw[-Stealth, red, thick] (dma.north) -- (b2.center);
\draw[-Stealth, red, thick] (dma.north) -- (b3.center);
\draw[-Stealth, red, thick] (dma.north) -- (b4.center);

% Arrow for Interrupt breakpoint
\draw[-Stealth, orange!80!black, thick] (intr.north) -- (b5.center);

% Timeline arrow at the bottom
\draw[thick, ->] ([yshift=-2.5cm]P1.west) -- ([yshift=-2.5cm]P6.east) node[right, font=\tiny\sffamily] {Tiempo};

\end{tikzpicture}
\end{document}
```