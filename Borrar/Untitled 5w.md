## Cycle stealing (Robo de ciclo)

1. Definición formal — de los libros fuente:
"Esta última técnica es la más común y se denomina robo de ciclo (*cycle stealing*), puesto que, en efecto, el módulo de DMA roba un ciclo de bus".

"An alternative technique called *cycle stealing* allows the DMA controller to transfer one data word at a time, after which it must return control of the buses to the CPU. The CPU merely delays its operation for one memory cycle to allow the direct memory I/O transfer to “steal” one memory cycle".

2. Propiedades y desarrollo:
- **Justificación de la prioridad del DMA sobre la CPU en el mismo ciclo de bus:**
  En la práctica totalidad de los sistemas de computación, el acceso de un módulo de DMA a la memoria principal posee una prioridad intrínsecamente superior a la del procesador. Esto se fundamenta en la naturaleza física y los requisitos de temporización de los dispositivos de E/S de alta velocidad (como controladores de discos o interfaces de red):
  - Los periféricos rápidos transmiten datos en tiempo real y sus flujos físicos de información no pueden detenerse ni ralentizarse una vez iniciados. Si el módulo de DMA es postergado en el uso del bus debido a que la CPU tiene prioridad, los búferes internos del periférico se desbordarán (*overrun* o *underrun*), resultando en una pérdida de datos crítica e irreversible o en fallos de transmisión.
  - Por el contrario, si a la CPU se le deniega temporalmente el acceso al bus de memoria, su hardware simplemente se detiene de forma segura durante un ciclo de reloj (se "congela") sin sufrir ninguna pérdida ni alteración de información.
- **Operación y repercusión en la CPU:**
  - El procesador es suspendido de manera asíncrona justo en el instante previo a que requiera utilizar el bus del sistema.
  - No constituye una interrupción por software estándar: la CPU no almacena su contexto de registros (programas en curso) ni ejecuta rutinas de servicio (ISR). En su lugar, el procesador se limita a pausar u ocluirse durante un único ciclo de bus, reanudando la ejecución inmediatamente después de que el DMA ha transferido la palabra de datos.
  - El efecto neto sobre la CPU es un decremento en su velocidad general de procesamiento debido a las recurrentes esperas de bus.
- **Diferenciación conceptual en el contexto de SIC (Single Instruction Computer) de Hill & Peterson:**
  Dentro de la arquitectura de E/S del computador SIC, es indispensable diferenciar el mecanismo de DMA de la **Secuencia Buffer** que implementa el hardware nativo:
  - **Secuencia Buffer en SIC:** Es una variante de interrupción por hardware especial en la que la CPU interviene activamente ejecutando una secuencia cableada de control (pasos 90 a 111 de la secuencia modificada). Utiliza la ALU y registros internos de la CPU (como el contador de palabras `BWC`, el contador de canal `CC` y el registro de comandos `BIOR`), y la transferencia física se canaliza a través de los registros y buses del procesador (`IOBUS` y `MD`). Adicionalmente, esta secuencia debe esperar de forma obligatoria a que la instrucción de la CPU que está en curso termine de ejecutarse para poder ser atendida.
  - **Mapeo de DMA en SIC:** A diferencia de la secuencia Buffer, el DMA opera como una **ruta alternativa a la memoria** que no compite por los registros ni la lógica de control que la CPU utiliza para sus instrucciones de programa. En SIC, la interacción simultánea con la RAM se maneja mediante puertos de memoria independientes (ej. memoria de puertos múltiples con un bloque de registros de banco dedicado `MA0`, `MD0`, `ST0`, `DS0`) que arbitran los accesos asíncronamente.

3. Figura o diagrama (si existe o aplica)

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[node distance=2cm, font=\sffamily\small]

% Timelines
\draw [thick, ->] (0,0) -- (10,0) node [right] {Tiempo};

% Grid lines
\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw [dashed, gray!50] (\x, -1) -- (\x, 4);
    \node [above] at (\x, 4) {T\x};
}

% Signals
\node [left] at (0, 3) {CPU Bus Access};
\draw [ultra thick, blue] (0, 3) -- (3, 3) node [midway, above] {Activo (Fetch/Exec)} 
                         -- (3, 2.2) -- (5, 2.2) node [midway, above, red] {Pausa (Ocioso)}
                         -- (5, 3) -- (9, 3) node [midway, above] {Activo};

\node [left] at (0, 1.5) {DMA Bus Request};
\draw [ultra thick, orange] (0, 1.2) -- (2.5, 1.2) -- (2.5, 1.8) node [above right] {BR} 
                           -- (5, 1.8) -- (5, 1.2) -- (9, 1.2);

\node [left] at (0, 0.5) {Bus Master};
\draw [ultra thick, green!60!black] (0, 0.5) -- (3, 0.5) node [midway, below] {CPU}
                                   -- (3, 0.5) -- (5, 0.5) node [midway, below, red] {DMA (Ciclo robado)}
                                   -- (5, 0.5) -- (9, 0.5) node [midway, below] {CPU};

\end{tikzpicture}
\end{document}
```