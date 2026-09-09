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

<br>

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit, backgrounds}
\begin{document}
\begin{tikzpicture}[
    font=\sffamily\small,
    box/.style={rectangle, draw, minimum width=2.2cm, minimum height=1.1cm, align=center, rounded corners=3pt},
    subbox/.style={rectangle, draw, minimum width=2.8cm, minimum height=0.9cm, align=center, rounded corners=2pt, font=\sffamily\scriptsize},
    arr/.style={draw, -{Stealth[scale=1.0]}, thick}
]

\node[box, fill=blue!15,   draw=blue!80]  (cpu) at (0,0)   {CPU};
\node[box, fill=green!25,  draw=green!80] (ram) at (4.5,0) {RAM};
\node[box, fill=orange!20, draw=orange!80](per) at (13,0)  {Periférico};

\draw[ultra thick, blue!70]   (cpu.south) -- ++(0,-8.2) coordinate (cpu_bot);
\draw[ultra thick, green!70]  (ram.south) -- ++(0,-8.2) coordinate (ram_bot);
\draw[ultra thick, orange!70] (per.south) -- ++(0,-8.2) coordinate (per_bot);

\node[subbox, fill=gray!10, draw=gray!60] (cnt) at (8.5,-1.2) {Contador\\de datos};
\node[subbox, fill=gray!10, draw=gray!60] (reg) at (8.5,-2.8) {Registro\\de datos};
\node[subbox, fill=gray!10, draw=gray!60] (dir) at (8.5,-4.4) {Registro de\\dirección};
\node[subbox, fill=gray!10, draw=gray!60, minimum height=1.8cm] (log) at (8.5,-6.8)
    {Lógica de control\\{\scriptsize(arbitraje de bus)}};

\begin{pgfonlayer}{background}
    \node[
        draw=gray!70, thick, dashed,
        fill=gray!5,
        rounded corners=6pt,
        fit=(cnt)(reg)(dir)(log),
        inner sep=10pt,
        label={[font=\sffamily\scriptsize\bfseries, gray!80]above:Controlador DMA}
    ] (dma) {};
\end{pgfonlayer}

\draw[arr, green!75]
    (cnt.west) -- (cnt.west -| ram.south)
    node[midway, above, font=\sffamily\scriptsize, green!80] {líneas de datos};

\draw[arr, orange!80]
    (per.south |- reg.east) -- (reg.east)
    node[midway, above, font=\sffamily\scriptsize, orange!90] {P6a: dato periférico};

\draw[arr, green!80]
    (reg.west) -- (reg.west -| ram.south)
    node[midway, below, font=\sffamily\scriptsize, green!90] {P6b: transf. directa};

\draw[arr, green!80]
    (dir.west) -- (dir.west -| ram.south)
    node[midway, above, font=\sffamily\scriptsize, green!90] {P6c: dir. memoria};

\coordinate (p1_y) at (0, -6.2);
\coordinate (p5_y) at (0, -7.4);

\draw[arr, orange!90]
    (per.south |- p1_y) -- (log.east |- p1_y)
    node[midway, above, font=\sffamily\scriptsize, orange!90] {P1: DREQ};

\draw[arr, orange!75]
    (log.east |- p5_y) -- (per.south |- p5_y)
    node[midway, below, font=\sffamily\scriptsize, orange!80] {P5: DACK};

\coordinate (p2_y) at (0, -6.4);
\coordinate (p4_y) at (0, -7.2);

\draw[arr, blue!80]
    (log.west |- p2_y) -- (cpu.south |- p2_y)
    node[midway, above, font=\sffamily\scriptsize, blue!80] {P2: HRQ};

\draw[arr, blue!65]
    (cpu.south |- p4_y) -- (log.west |- p4_y)
    node[midway, below, font=\sffamily\scriptsize, blue!70] {P4: HLDA};

\end{tikzpicture}
\end{document}
```

<br>

*Señales de arbitraje entre CPU, controlador DMA, memoria y periférico.*
<br>


---
<br>

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

**Contexto SIC (Hill & Peterson)**

Hill & Peterson presentan tres métodos de E/S en progresión de eficiencia:

| Método           | Intervención CPU             | Paralelismo |
| ---------------- | ---------------------------- | ----------- |
| Por programa     | Constante — sin paralelismo  | Ninguno     |
| Secuencia Buffer | Por bloque — overhead de ISR | Parcial     |
| DMA              | Solo inicio/fin              | Total       |

El DMA accede a memoria de forma autónoma mediante puertos propios (`MA0`, `MD0`, `ST0`, `DS0`), arbitrados por un **módulo de control de memoria** que resuelve conflictos cuando CPU y DMA acceden a la RAM simultáneamente — sin intervención de la CPU en cada dato transferido.

<br>
<br>
<br>
<br>
<br>
<br>

---

<br>
<br>

![[Untitled 1 1-06-09-2026_22-28-14.png|500]]

*Fig. 7.12 · Puntos de ruptura para el DMA y las interrupciones en un ciclo de instrucción.*

El DMA puede tomar el bus entre cualquier par de ciclos de bus (puntos de ruptura múltiples), mientras que una interrupción solo se atiende al finalizar la instrucción completa.

<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br>



---
