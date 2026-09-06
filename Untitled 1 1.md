## Cycle Stealing (Robo de Ciclo) — Prioridad del DMA sobre la CPU

### 1. Definición formal

> "Esta última técnica es la más común y se denomina **robo de ciclo (*cycle stealing*)**, puesto que, en efecto, el módulo de DMA roba un ciclo de bus."

> "Una técnica alternativa denominada *robo de ciclo* permite al controlador de DMA transferir una palabra de datos a la vez, tras lo cual debe devolver el control de los buses a la CPU. La CPU simplemente retrasa su operación durante un ciclo de memoria para permitir que la transferencia directa de E/S a memoria 'robe' un ciclo de memoria."

---

### 2. Propiedades y desarrollo

**Justificación de la prioridad del DMA sobre la CPU (Stallings)**

La prioridad absoluta del DMA sobre la CPU en el acceso a la memoria se fundamenta en la naturaleza física y temporal de los dispositivos periféricos:

- Los periféricos de alta velocidad (discos magnéticos, controladores de red) transmiten datos en flujos continuos en tiempo real. Si el controlador de DMA no obtiene acceso inmediato al bus de memoria en el instante en que el dato está listo, el flujo entrante sobrescribirá el buffer del dispositivo, resultando en una **pérdida inevitable de datos** (*buffer overrun*).
- La CPU es un dispositivo puramente interno controlado por reloj que retiene de forma segura todo su estado interno al detenerse. Postergar su acceso al bus por un ciclo no genera ninguna pérdida de datos ni fallo operativo — únicamente un retraso de rendimiento menor.
- Las transferencias DMA a memoria son relativamente infrecuentes comparadas con los accesos constantes de la CPU, por lo que el impacto en el rendimiento global es mínimo.

Por consiguiente, el acceso del módulo de DMA a la memoria principal siempre recibe **prioridad superior** al de la CPU.

---

**Pasos de operación del robo de ciclo**

1. El periférico activa `DREQ` (*DMA Request*) hacia el controlador de DMA indicando que tiene un dato listo.
2. El controlador de DMA solicita el bus al procesador activando `BR` (*Bus Request* / `HOLD`).
3. El procesador suspende su ejecución en su siguiente **punto de ruptura** — justo antes de necesitar el bus del sistema (puede ocurrir entre captación de instrucción, decodificación, captación de operando o ejecución).
4. La CPU coloca sus líneas de dirección, datos y control en **alta impedancia**, desconectándose eléctricamente del bus, y responde con `BG` (*Bus Grant* / `HLDA`).
5. El controlador de DMA activa `DACK` (*DMA Acknowledge*) hacia el periférico indicando que la transferencia comienza.
6. El DMA coloca la dirección destino en el bus de direcciones, habilita `RD`/`WR` y transfiere **un único dato** (palabra o byte) directamente entre el periférico y la memoria principal.
7. El DMA incrementa su registro de dirección, decrementa el contador de palabras, desactiva `BR`/`HOLD` y devuelve el control del bus al procesador inmediatamente.

**Diagrama de bloques — señales de arbitraje**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    node distance=1.5cm,
    block/.style={rectangle, draw, fill=blue!5, text width=2.2cm, align=center, minimum height=1cm, rounded corners, font=\sffamily\scriptsize},
    line/.style={draw, -{Stealth[scale=0.8]}, thick},
    bus/.style={draw, {Stealth[scale=0.8]}-{Stealth[scale=0.8]}, ultra thick, gray}
]
    \node [block] (cpu) {CPU\\(Procesador)};
    \node [block, right=3cm of cpu] (dma) {Controlador\\DMA};
    \node [block, below=2cm of cpu] (ram) {Memoria Principal\\(RAM)};
    \node [block, below=2cm of dma] (io) {Dispositivo E/S\\(Periférico)};

    \draw [line, transform canvas={yshift=0.15cm}] (dma) -- node[above, font=\sffamily\tiny] {BR (Bus Request / HOLD)} (cpu);
    \draw [line, transform canvas={yshift=-0.15cm}] (cpu) -- node[below, font=\sffamily\tiny] {BG (Bus Grant / HLDA)} (dma);

    \draw [line, transform canvas={xshift=-0.15cm}] (io) -- node[left, font=\sffamily\tiny] {DREQ (Request)} (dma);
    \draw [line, transform canvas={xshift=0.15cm}] (dma) -- node[right, font=\sffamily\tiny] {DACK (Acknowledge)} (io);

    \draw [bus] (cpu) -- (ram) node[midway, left, black, font=\sffamily\tiny] {Buses de Sistema};
    \draw [bus] (dma) -- (ram) node[midway, below left, black, font=\sffamily\tiny] {Acceso Directo};
    \draw [bus] (io) -- (ram);
\end{tikzpicture}
\end{document}
```

*Señales de control y arbitraje de bus entre CPU, controlador DMA, memoria y periférico.*

---

**Diferencia clave con una interrupción ordinaria**

A diferencia de una interrupción, el robo de ciclo **no requiere cambio de contexto, no guarda registros en la pila ni ejecuta una ISR**. El procesador simplemente se pausa durante exactamente un ciclo de bus y reanuda la instrucción en curso. El único efecto es una ligera ralentización en la velocidad de ejecución global.

| | Cycle Stealing (DMA) | Interrupción |
|---|---|---|
| Guarda contexto (registros, PC) | No | Sí |
| Ejecuta rutina de servicio (ISR) | No | Sí |
| Duración de la pausa | 1 ciclo de bus | Varios ciclos (save + ISR + restore) |
| Punto de ruptura | En cualquier acceso al bus | Solo al finalizar la instrucción en curso |
| Impacto en rendimiento | Mínimo (ralentización leve) | Mayor (overhead de cambio de contexto) |

**Diagrama de tiempo — ciclo robado**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[node distance=2cm, font=\sffamily\small]

\draw [thick, ->] (0,0) -- (10,0) node [right] {Tiempo};

\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw [dashed, gray!50] (\x, -1) -- (\x, 4);
    \node [above] at (\x, 4) {T\x};
}

\node [left] at (0, 3) {CPU Bus Access};
\draw [ultra thick, blue] (0, 3) -- (3, 3) node [midway, above] {Activo (Fetch/Exec)}
                         -- (3, 2.2) -- (5, 2.2) node [midway, above, red] {Pausa (Alta Impedancia)}
                         -- (5, 3) -- (9, 3) node [midway, above] {Activo};

\node [left] at (0, 1.5) {DMA Bus Request};
\draw [ultra thick, orange] (0, 1.2) -- (2.5, 1.2) -- (2.5, 1.8) node [above right] {BR}
                           -- (5, 1.8) -- (5, 1.2) -- (9, 1.2);

\node [left] at (0, 0.5) {Bus Master};
\draw [ultra thick, green!60!black] (0, 0.5) -- (3, 0.5) node [midway, below] {CPU}
                                   -- (5, 0.5) node [midway, below, red] {DMA (1 ciclo robado)}
                                   -- (9, 0.5) node [midway, below] {CPU};
\end{tikzpicture}
\end{document}
```

*El DMA toma control del bus por exactamente un ciclo — la CPU reanuda inmediatamente después.*

---

**Contexto en el computador SIC (Hill & Peterson)**

El DMA se define como la tercera gran alternativa de E/S en el SIC — una **ruta alternativa a la memoria que no utiliza los registros que la CPU usa para sus instrucciones regulares**. Esto lo diferencia radicalmente de las dos alternativas previas:

- **Transferencia por Programa (T3.4):** la CPU ejecuta instrucciones de E/S activamente — no hay paralelismo.
- **Secuencia Buffer (T3.7–T3.9):** variante de interrupción por hardware en la que la CPU interviene ejecutando los pasos 90–111 de la secuencia modificada, usando registros internos (`BWC`, `CC`, `BIOR`) y canalizando la transferencia a través de `IOBUS` y `MD`. Debe esperar a que la instrucción en curso termine antes de atenderse.
- **DMA (T3.10):** opera de forma asíncrona mediante puertos de memoria independientes (`MA0`, `MD0`, `ST0`, `DS0`). Las solicitudes concurrentes se arbitran mediante un **módulo de control de memoria** (*Memory Control Module*) que gestiona el acceso a la RAM sin involucrar registros ni lógica de control de la CPU.

**Puntos de ruptura DMA vs Interrupción**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    phase/.style={rectangle, draw=black, fill=blue!5, minimum width=2.1cm, minimum height=1.1cm, align=center, font=\tiny\sffamily},
    lbl/.style={draw, rectangle, rounded corners, font=\tiny\sffamily, align=center}
]

\node[phase] (P1) {Captación\\instrucción};
\node[phase, right=0.15cm of P1] (P2) {Decodificación\\instrucción};
\node[phase, right=0.15cm of P2] (P3) {Captación\\operando};
\node[phase, right=0.15cm of P3] (P4) {Ejecución\\instrucción};
\node[phase, right=0.15cm of P4] (P5) {Almacenar\\resultado};
\node[phase, right=0.15cm of P5] (P6) {Procesar\\interrupción};

\node[lbl, fill=red!10, below=1cm of P2, xshift=0.9cm] (dma) {Puntos de ruptura DMA\\(antes de cualquier acceso al bus)};
\node[lbl, fill=orange!15, below=1.8cm of P5, xshift=0.5cm] (intr) {Punto de ruptura interrupción\\(solo al finalizar la instrucción)};

\path (P1.east) -- node(b1) {} (P2.west);
\path (P2.east) -- node(b2) {} (P3.west);
\path (P3.east) -- node(b3) {} (P4.west);
\path (P4.east) -- node(b4) {} (P5.west);
\path (P5.east) -- node(b5) {} (P6.west);

\draw[-Stealth, red, thick] (dma.north) -- (b1.center);
\draw[-Stealth, red, thick] (dma.north) -- (b2.center);
\draw[-Stealth, red, thick] (dma.north) -- (b3.center);
\draw[-Stealth, red, thick] (dma.north) -- (b4.center);
\draw[-Stealth, orange!80!black, thick] (intr.north) -- (b5.center);

\draw[thick, ->] ([yshift=-2.5cm]P1.west) -- ([yshift=-2.5cm]P6.east) node[right, font=\tiny\sffamily] {Tiempo};
\end{tikzpicture}
\end{document}
```

*El DMA puede interrumpir el ciclo de instrucción en múltiples puntos — la interrupción solo al finalizar.*
