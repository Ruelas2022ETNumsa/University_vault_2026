## Cycle Stealing (Robo de Ciclo) — Prioridad del DMA sobre la CPU

### 1. Definición formal

> "Esta última técnica es la más común y se denomina **robo de ciclo (*cycle stealing*)**, puesto que, en efecto, el módulo de DMA roba un ciclo de bus."

> "Una técnica alternativa denominada *robo de ciclo* permite al controlador de DMA transferir una palabra de datos a la vez, tras lo cual debe devolver el control de los buses a la CPU. La CPU simplemente retrasa su operación durante un ciclo de memoria para permitir que la transferencia directa de E/S a memoria 'robe' un ciclo de memoria."

---

### 2. Propiedades y desarrollo

**Justificación de la prioridad del DMA (Stallings)**

Cuando el DMA y la CPU solicitan el bus simultáneamente, el árbitro de bus otorga prioridad al DMA para garantizar la transferencia en tiempo real. Esto se justifica porque los periféricos de alta velocidad no pueden detenerse — si el DMA no accede al bus cuando el dato está listo, el buffer del dispositivo se desborda (*buffer overrun*) y el dato se pierde. La CPU, en cambio, puede ceder el bus temporalmente sin perder información. Como las transferencias DMA son infrecuentes respecto a los accesos constantes de la CPU, el impacto en el rendimiento es mínimo.

---

**Pasos de operación**

1. El periférico activa `DREQ` indicando que tiene un dato listo.
2. El DMA solicita el bus con `BR` / `HOLD`.
3. La CPU termina el ciclo de bus actual y cede el control.
4. La CPU libera el bus y confirma con `BG` / `HLDA`.
5. El DMA activa `DACK` — la transferencia comienza.
6. El DMA transfiere un dato directamente entre periférico y RAM.
7. El DMA desactiva `BR`, actualiza su dirección y contador, y devuelve el bus a la CPU.

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

*Señales de arbitraje de bus entre CPU, controlador DMA, memoria y periférico.*

---

**Diferencia con una interrupción ordinaria**

El robo de ciclo no requiere cambio de contexto ni ISR — la CPU cede el bus entre ciclos y reanuda inmediatamente.

| | Cycle Stealing (DMA) | Interrupción |
|---|---|---|
| Guarda contexto (registros, PC) | No | Sí |
| Ejecuta ISR | No | Sí |
| Duración de la pausa | 1 ciclo de bus por transferencia | Varios ciclos (save + ISR + restore) |
| Momento de atención | Entre ciclos de bus | Al finalizar la instrucción en curso |
| Impacto en rendimiento | Mínimo | Mayor |

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
\draw [ultra thick, blue] (0, 3) -- (3, 3) node [midway, above] {Activo}
                         -- (3, 2.2) -- (5, 2.2) node [midway, above, red] {Cede el bus}
                         -- (5, 3) -- (9, 3) node [midway, above] {Activo};

\node [left] at (0, 1.5) {DMA Bus Request};
\draw [ultra thick, orange] (0, 1.2) -- (2.5, 1.2) -- (2.5, 1.8) node [above right] {BR}
                           -- (5, 1.8) -- (5, 1.2) -- (9, 1.2);

\node [left] at (0, 0.5) {Bus Master};
\draw [ultra thick, green!60!black] (0, 0.5) -- (3, 0.5) node [midway, below] {CPU}
                                   -- (5, 0.5) node [midway, below, red] {DMA (ciclo robado)}
                                   -- (9, 0.5) node [midway, below] {CPU};
\end{tikzpicture}
\end{document}
```

*El DMA ocupa el bus durante un ciclo por transferencia — la CPU reanuda inmediatamente después.*

---

**Contexto en el computador SIC (Hill & Peterson)**

El DMA es la tercera alternativa de E/S del SIC — ruta directa a memoria sin usar registros de la CPU:

- **Por Programa (T3.4):** la CPU controla activamente cada transferencia — sin paralelismo.
- **Secuencia Buffer (T3.7–T3.9):** la CPU ejecuta los pasos 90–111 usando `BWC`, `CC`, `BIOR`, `IOBUS` y `MD`. Debe esperar a que la instrucción en curso finalice.
- **DMA (T3.10):** acceso asíncrono mediante puertos independientes (`MA0`, `MD0`, `ST0`, `DS0`) arbitrados por un **módulo de control de memoria** — sin intervención de la CPU.

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

\node[lbl, fill=red!10, below=1cm of P2, xshift=0.9cm] (dma) {Puntos de atención DMA\\(entre ciclos de bus)};
\node[lbl, fill=orange!15, below=1.8cm of P5, xshift=0.5cm] (intr) {Punto de atención interrupción\\(al finalizar la instrucción)};

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

*El DMA atiende entre ciclos de bus — la interrupción solo al finalizar la instrucción.*
