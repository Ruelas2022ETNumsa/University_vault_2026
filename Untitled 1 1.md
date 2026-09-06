## Cycle Stealing (Robo de Ciclo) — Prioridad del DMA sobre la CPU

### 1. Definición formal

> "El módulo de DMA es capaz de imitar al procesador y recibir el control del sistema cedido por él. Necesita dicho control para transferir datos a y desde memoria a través del bus del sistema. Para hacerlo, debe utilizarlo sólo cuando el procesador no lo necesita, o debe forzar al procesador a suspender temporalmente su funcionamiento. Esta última técnica es la más común y se denomina **robo de ciclo (*cycle stealing*)**, puesto que, en efecto, el módulo de DMA roba un ciclo de bus."

> "Una técnica alternativa denominada *robo de ciclo* permite al controlador de DMA transferir una palabra de datos a la vez, tras lo cual debe devolver el control de los buses a la CPU. La CPU simplemente retrasa su operación durante un ciclo de memoria para permitir que la transferencia directa de E/S a memoria 'robe' un ciclo de memoria."

---

### 2. Propiedades y desarrollo

**Justificación de la prioridad del DMA (Stallings)**

Cuando el DMA y la CPU solicitan el bus simultáneamente, el árbitro otorga prioridad al DMA para garantizar la transferencia en tiempo real. Los periféricos no pueden detenerse — si el DMA no accede al bus cuando el dato está listo, el buffer se desborda (*buffer overrun*) y el dato se pierde. La CPU puede ceder el bus temporalmente sin perder información. Como las transferencias DMA son infrecuentes, el impacto en el rendimiento es mínimo.

---

**Pasos de operación**

1. El periférico activa `DREQ` — dato listo.
2. El DMA solicita el bus con `HRQ` / `HOLD`.
3. La CPU termina el ciclo de bus actual y cede el control.
4. La CPU confirma con `HLDA` — bus liberado.
5. El DMA activa `DACK` — transferencia comienza.
6. El DMA transfiere un dato directamente entre periférico y RAM.
7. El DMA desactiva `HRQ`, actualiza dirección y contador, devuelve el bus.

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    node distance=2.5cm,
    block/.style={rectangle, draw, fill=blue!5, text width=3.2cm, align=center, minimum height=1.4cm, rounded corners, font=\sffamily\small},
    line/.style={draw, -{Stealth[scale=1.2]}, thick},
    bus/.style={draw, {Stealth[scale=1.2]}-{Stealth[scale=1.2]}, ultra thick, gray}
]
    \node [block] (cpu) {CPU\\(Procesador)};
    \node [block, right=5cm of cpu] (dma) {Controlador\\DMA};
    \node [block, below=3.5cm of cpu] (ram) {Memoria Principal\\(RAM)};
    \node [block, below=3.5cm of dma] (io) {Dispositivo E/S\\(Periférico)};

    \draw [line, transform canvas={yshift=0.2cm}] (dma) -- node[above, font=\sffamily\scriptsize] {P2: HRQ (HOLD Request)} (cpu);
    \draw [line, transform canvas={yshift=-0.2cm}] (cpu) -- node[below, font=\sffamily\scriptsize] {P4: HLDA (Hold Acknowledge)} (dma);
    \draw [line, transform canvas={xshift=-0.2cm}] (io) -- node[left, font=\sffamily\scriptsize] {P1: DREQ (Request)} (dma);
    \draw [line, transform canvas={xshift=0.2cm}] (dma) -- node[right, font=\sffamily\scriptsize] {P5: DACK (Acknowledge)} (io);
    \draw [bus] (cpu) -- (ram) node[midway, left, black, font=\sffamily\scriptsize] {P6: Acceso DMA};
    \draw [bus] (dma) -- (ram) node[midway, below left, black, font=\sffamily\scriptsize] {P6: Transferencia Directa};
    \draw [bus] (io) -- (ram);
\end{tikzpicture}
\end{document}
```

*Señales de arbitraje entre CPU, controlador DMA, memoria y periférico.*

---

**Diferencia con una interrupción**

| | Cycle Stealing (DMA) | Interrupción |
|---|---|---|
| Guarda contexto | No | Sí |
| Ejecuta ISR | No | Sí |
| Duración de la pausa | 1 ciclo de bus | Varios ciclos (save + ISR + restore) |
| Momento de atención | Entre ciclos de bus | Al finalizar la instrucción |
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
\node [left] at (0, 1.5) {DMA HRQ};
\draw [ultra thick, orange] (0, 1.2) -- (2.5, 1.2) -- (2.5, 1.8) node [above right] {HRQ}
                           -- (5, 1.8) -- (5, 1.2) -- (9, 1.2);
\node [left] at (0, 0.5) {Bus Master};
\draw [ultra thick, green!60!black] (0, 0.5) -- (3, 0.5) node [midway, below] {CPU}
                                   -- (5, 0.5) node [midway, below, red] {DMA (ciclo robado)}
                                   -- (9, 0.5) node [midway, below] {CPU};
\end{tikzpicture}
\end{document}
```

*El DMA ocupa el bus un ciclo por transferencia — la CPU reanuda inmediatamente.*

---

**Contexto SIC (Hill & Peterson) — T3.10**

El DMA es la tercera alternativa de E/S: ruta directa a memoria sin usar registros de la CPU.

- **Por Programa (T3.4):** CPU controla activamente cada transferencia — sin paralelismo.
- **Secuencia Buffer (T3.7–T3.9):** CPU ejecuta pasos 90–111 con `BWC`, `CC`, `BIOR`, `IOBUS`, `MD`. Espera a que finalice la instrucción en curso.
- **DMA (T3.10):** acceso asíncrono por puertos independientes (`MA0`, `MD0`, `ST0`, `DS0`) arbitrados por un **módulo de control de memoria** — sin intervención de la CPU.

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

---

![[pegar_imagen]]
*Fig. 7.12 · Puntos de ruptura para el DMA y las interrupciones en un ciclo de instrucción.*
[[Stallings - Organización y Arquitectura de Computadores - 7ed.pdf#page=]]
*Fig. 7.12*
justificación: Muestra en qué puntos del ciclo de instrucción el DMA puede tomar el bus (entre ciclos) versus dónde se atiende una interrupción (al finalizar la instrucción).
