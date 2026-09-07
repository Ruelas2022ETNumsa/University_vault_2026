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
\begin{tikzpicture}[font=\sffamily\small]

% --- Eje de tiempo ---
\draw[thick, ->] (0,0) -- (13,0) node[right] {Tiempo};
\foreach \x/\lbl in {0/T0, 2/T1, 4/T2, 6/T3, 8/T4, 10/T5} {
    \draw[dashed, gray!40] (\x, 0.2) -- (\x, 5.5);
    \node[above, font=\sffamily\scriptsize] at (\x, 5.5) {\lbl};
}

% --- Etiquetas de filas ---
\node[left, align=right, font=\sffamily\scriptsize] at (0, 4.4) {CPU\\Bus};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 2.8) {DMA\\HRQ};
\node[left, align=right, font=\sffamily\scriptsize] at (0, 1.4) {Bus\\Master};

% === Fila 1: CPU Bus ===
\draw[ultra thick, blue] (0, 4.2) -- (5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (2.4, 4.2) {Activo};
\draw[ultra thick, blue] (5, 4.2) -- (5, 3.7);
\draw[ultra thick, blue] (5, 3.7) -- (8.6, 3.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (6.8, 3.7) {Cede el bus};
\draw[ultra thick, blue] (8.6, 3.7) -- (8.6, 4.2);
\draw[ultra thick, blue] (8.6, 4.2) -- (12.5, 4.2);
\node[above, font=\sffamily\scriptsize, blue] at (10.5, 4.2) {Activo};

% === Fila 2: DMA HRQ ===
\draw[ultra thick, orange!80!black] (0, 2.6) -- (2, 2.6);
\draw[ultra thick, orange!80!black] (2, 2.6) -- (2, 3.1);
\node[above, font=\sffamily\scriptsize, orange!80!black] at (4.5, 3.1) {HRQ activo};
\draw[ultra thick, orange!80!black] (2, 3.1) -- (8.0, 3.1);
\draw[ultra thick, orange!80!black] (8.0, 3.1) -- (8.0, 2.6);
\draw[ultra thick, orange!80!black] (8.0, 2.6) -- (12.5, 2.6);

% === Fila 3: Bus Master ===
\draw[ultra thick, green!50!black] (0, 1.2) -- (5.4, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (2.4, 1.2) {CPU};
\draw[ultra thick, green!50!black] (5.4, 1.2) -- (5.4, 1.7);
\draw[ultra thick, red!70!black] (5.4, 1.7) -- (8.0, 1.7);
\node[above, font=\sffamily\scriptsize, red!70!black] at (6.7, 1.7) {DMA (ciclo robado)};
\draw[ultra thick, green!50!black] (8.0, 1.7) -- (8.0, 1.2);
\draw[ultra thick, green!50!black] (8.0, 1.2) -- (12.5, 1.2);
\node[below, font=\sffamily\scriptsize, green!50!black] at (10.5, 1.2) {CPU};

% --- Pasos escalonados: P1 más bajo (-4.2), P7 sube a (-0.6) ---
% Cada paso en su x, la guía solo llega hasta la y del texto

% P1 en x=0, y=-4.2
\draw[densely dashed, red!50, line width=0.6pt] (0, 0) -- (0, -4.2);
\node[right, font=\sffamily\scriptsize, red!60!black] at (0, -4.2) {P1: DREQ activo (periférico listo)};

% P2 en x=2, y=-3.6
\draw[densely dashed, violet!60, line width=0.6pt] (2, 0) -- (2, -3.6);
\node[right, font=\sffamily\scriptsize, violet] at (2, -3.6) {P2: HRQ activo — DMA solicita bus};

% P3 en x=5, y=-3.0
\draw[densely dashed, gray!50, line width=0.6pt] (5, 0) -- (5, -3.0);
\node[right, font=\sffamily\scriptsize, gray!70!black] at (5, -3.0) {P3: CPU termina ciclo actual};

% P4 en x=5.4, y=-2.4
\draw[densely dashed, green!50!black, line width=0.6pt] (5.4, 0) -- (5.4, -2.4);
\node[right, font=\sffamily\scriptsize, green!60!black] at (5.4, -2.4) {P4: HLDA — CPU cede, bus libre};

% P5 en x=6.0, y=-1.8
\draw[densely dashed, green!40!black, line width=0.6pt] (6.0, 0) -- (6.0, -1.8);
\node[right, font=\sffamily\scriptsize, green!40!black] at (6.0, -1.8) {P5: DACK — DMA toma el bus};

% P6 en x=7.0, y=-1.2
\draw[densely dashed, blue!50, line width=0.6pt] (7.0, 0) -- (7.0, -1.2);
\node[right, font=\sffamily\scriptsize, blue!70!black] at (7.0, -1.2) {P6: Transferencia directa E/S $\to$ RAM};

% P7 en x=8.0, y=-0.6
\draw[densely dashed, orange!70, line width=0.6pt] (8.0, 0) -- (8.0, -0.6);
\node[right, font=\sffamily\scriptsize, orange!80!black] at (8.0, -0.6) {P7: HRQ baja — bus devuelto a CPU};

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
