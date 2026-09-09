## Cycle stealing (Robo de ciclo)

### 1. Definición formal
> "Esta última técnica es la más común y se denomina **robo de ciclo (*cycle stealing*)**, puesto que, en efecto, el módulo de DMA roba un ciclo de bus."

---

### 2. Propiedades y desarrollo

*   **Mecanismo de prioridad y justificación de Stallings/Mano**: 
    La prioridad absoluta del DMA sobre la CPU en el acceso a la memoria se justifica por la naturaleza física y temporal de los dispositivos periféricos. Los periféricos de alta velocidad (como discos magnéticos o controladores de red) transmiten datos en flujos continuos en tiempo real; **si el controlador de DMA no obtiene acceso inmediato al bus de memoria al estar listo el dato, este se perderá irremediablemente por desbordamiento de buffer (*buffer overrun*)**. En contraste, **la CPU es un dispositivo puramente interno que puede detener su ejecución temporalmente (*stall*) sin sufrir ninguna pérdida de información**, reanudando sus operaciones de manera transparente una vez que el DMA libera los buses. Además, las transferencias de E/S a memoria son relativamente infrecuentes en comparación con los constantes accesos de la CPU, por lo que el impacto en el rendimiento es mínimo.

*   **Diferencia clave con una interrupción ordinaria**: 
    A diferencia de una interrupción, el robo de ciclo **no requiere que la CPU realice un cambio de contexto, guarde el estado de sus registros en la pila o ejecute una rutina de servicio de interrupción (ISR)**. El procesador simplemente se pone en un estado de pausa de bus o alta impedancia durante **exactamente un ciclo de bus** (el tiempo necesario para transferir una sola palabra) y luego continúa inmediatamente con la instrucción en curso. El único efecto real es que la CPU se ralentiza ligeramente en su velocidad de ejecución global, pero se ahorra el enorme *overhead* de procesamiento que imponen las interrupciones normales.

*   **Puntos de ruptura (*Breakpoints*) de operación**: 
    La CPU puede suspenderse temporalmente en diversos puntos dentro del ciclo de instrucción (captación de instrucción, decodificación, captación de operando, ejecución, etc.), pero **siempre se detiene justo antes del instante en que necesita realizar un acceso al bus del sistema**. El controlador de DMA solicita el bus activando la línea `BR` (*Bus Request* o `HOLD`), la CPU finaliza su ciclo de bus actual, coloca sus líneas en alta impedancia y responde con `BG` (*Bus Grant* o `HLDA`), permitiendo que el DMA "robe" el ciclo de acceso a la RAM.

*   **Contexto en el computador SIC (Hill & Peterson)**: 
    En el computador SIC de Hill & Peterson, el DMA se define como la tercera gran alternativa de E/S: una **"ruta alternativa a la memoria que no utiliza los registros que la CPU usa para sus instrucciones regulares"**, de manera que la CPU y el DMA comparten la memoria de igual manera de forma asíncrona. Esto difiere radicalmente de las transferencias por programa o por Buffer (pasos 90-111), las cuales se ejecutan secuencialmente bajo el control directo de la CPU mediante el barrido de líneas `BCR` y el uso del registro contador de palabras `BWC`. Para evitar colisiones en sistemas multipuerto, el acceso de DMA a la RAM se coordina asincrónicamente mediante un **módulo de control de memoria (*Memory Control Module*)**, el cual arbitra las solicitudes concurrentes gestionando registros específicos de puerto como el estado del banco (`ST0`), dirección del banco (`MA0`) y registro de datos (`MD0`).

---

### 3. Figura o diagrama

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    node distance=1.5cm,
    block/.style={rectangle, draw, fill=blue!5, text width=2.2cm, align=center, minimum height=1cm, rounded corners, font=\sffamily\scriptsize},
    line/.style={draw, -{Stealth[scale=0.8]}, thick},
    bus/.style={draw, {Stealth[scale=0.8]}-{Stealth[scale=0.8]}, ultra thick, gray}
]
    % Nodes
    \node [block] (cpu) {CPU\\(Procesador)};
    \node [block, right=3cm of cpu] (dma) {Controlador\\DMA};
    \node [block, below=2cm of cpu] (ram) {Memoria Principal\\(RAM)};
    \node [block, below=2cm of dma] (io) {Dispositivo E/S\\(Periférico)};

    % Handshake CPU - DMA
    \draw [line, transform canvas={yshift=0.15cm}] (dma) -- node[above, font=\sffamily\tiny] {BR (Bus Request / HOLD)} (cpu);
    \draw [line, transform canvas={yshift=-0.15cm}] (cpu) -- node[below, font=\sffamily\tiny] {BG (Bus Grant / HLDA)} (dma);

    % Handshake DMA - Periferico
    \draw [line, transform canvas={xshift=-0.15cm}] (io) -- node[left, font=\sffamily\tiny] {DREQ (Request)} (dma);
    \draw [line, transform canvas={xshift=0.15cm}] (dma) -- node[right, font=\sffamily\tiny] {DACK (Acknowledge)} (io);

    % Buses lines representing the shared interconnect
    \draw [bus] (cpu) -- (ram) node[midway, left, black, font=\sffamily\tiny] {Buses de Sistema};
    \draw [bus] (dma) -- (ram) node[midway, below left, black, font=\sffamily\tiny] {Acceso Directo};
    \draw [bus] (io) -- (ram);

\end{tikzpicture}
\end{document}
```

*Fig. 8-15*  
justificación: Diagrama de bloques que ilustra las señales de control y arbitraje (`BR`/`BG`) para el robo de ciclo de bus y la transferencia directa entre periférico y memoria.

---

💡 **Siguiente paso sugerido**: ¿Te gustaría complementar este análisis con el cálculo exacto de la penalización de velocidad de la CPU ante una tasa de transferencia de datos dada en cycle stealing, utilizando los problemas prácticos del capítulo de Stallings o Mano?