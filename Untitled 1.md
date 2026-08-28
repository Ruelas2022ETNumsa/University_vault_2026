## Organización y Arquitectura del Computador SIC (24 pasos)

### 1. Definición formal
El computador **SIC (Small Instructional Computer)** es una máquina de dirección única con \( 2^{13} = 8192 \) localidades de memoria de **18 bits** cada una. Su arquitectura de direccionamiento básico se compone de un código de operación de 3 bits (`IR[0:2]`), un bit de indexación (`IR`), un bit de direccionamiento indirecto (`IR`) y un campo de dirección de 13 bits (`IR[5:17]`). La secuencia de control del procesador para las instrucciones de referencia a memoria se realiza en un total de **24 pasos de control** bajo la notación **AHPL**.

### 2. Idea clave
La optimización y compactación del ciclo de control de **24 pasos** radica en la compartición del paso de lectura de operando en memoria (Paso 14) para todas las instrucciones que requieren acceso de lectura (`ISZ`, `LAC`, `AND`, `TAD`), mientras que aquellas que solo escriben (`JMS`, `DAC`) o bifurcan (`JMP`) se desvían de manera combinacional antes de dicho acceso para ahorrar pasos de reloj.

### 3. Figura o diagrama (Caso B)
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=3cm, minimum height=0.8cm, text centered, draw=teal, fill=teal!10, text=teal!50!black, font=\bfseries]
\tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=0.8cm, text centered, draw=teal, fill=teal!5, text=teal!70!black]
\tikzstyle{decision} = [diamond, aspect=2, minimum width=2.5cm, minimum height=1cm, text centered, draw=orange, fill=orange!10, text=orange!80!black]
\tikzstyle{arrow} = [thick, ->, >=stealth, draw=gray]

\begin{tikzpicture}[node distance=1.6cm, scale=0.9, every node/.style={transform shape}]
  \node (start) [startstop] {Inicio (Paso 1)};
  \node (fetch) [process, below of=start] {Fetch (Pasos 2-4)};
  \node (dec) [decision, below of=fetch, yshift=-0.5cm] {¿Operativa (111)?};
  \node (addr) [decision, below of=dec, yshift=-1cm] {¿Direccionamiento?};
  \node (ind) [process, left of=addr, xshift=-2.5cm] {Indirecto (Pasos 6-8)};
  \node (idx) [process, right of=addr, xshift=2.5cm] {Indexado (Pasos 9-11)};
  \node (eff) [process, below of=addr, yshift=-1cm] {Cargar MA (Paso 12)};
  \node (exec) [startstop, below of=eff] {Ejecución MR (Pasos 13-24)};
  
  \draw [arrow] (start) -- (fetch);
  \draw [arrow] (fetch) -- (dec);
  \draw [arrow] (dec) -- node[anchor=south] {Sí (Paso 25)} ++(4.5,0) |- (exec);
  \draw [arrow] (dec) -- node[anchor=east] {No} (addr);
  \draw [arrow] (addr) -- node[anchor=south] {Indirecto} (ind);
  \draw [arrow] (addr) -- node[anchor=south] {Indexado} (idx);
  \draw [arrow] (addr) -- node[anchor=east] {Directo} (eff);
  \draw [arrow] (ind) |- (eff);
  \draw [arrow] (idx) |- (eff);
  \draw [arrow] (eff) -- (exec);
\end{tikzpicture}
\end{document}
```

### 4. Secuencia de Control en AHPL

```ahpl
MODULE: SIC
MEMORY: AC; MD; PC; IR; IA; IB; MA; lf; M
INPUTS: start
BUSES: ABUS; BBUS; OBUS

1. => (~start) / (1)
2. MA <- PC
3. MD <- M * DCD(MA)
4. IR <- MD; PC <- INC(PC)
5. => (IR & IR & IR, ~IR & ~IR, ~IR & IR, IR) / (25, 12, 6, 9)
6. MA <- IR[5:17]
7. MD <- M * DCD(MA)
8. IR[5:17] <- MD[5:17]; => (12)
9. => (IR) / (11)
10. IR[5:17] <- ADD(IA; IR[5:17]); => (12)
11. IR[5:17] <- ADD(IB; IR[5:17])
12. MA <- IR[5:17]
13. => (~IR, IR & ~IR & ~IR, IR & ~IR & IR, IR & IR & ~IR) / (14, 21, 23, 24)
14. MD <- M * DCD(MA)
15. => (DCD(IR[0:2])) / (16, 18, 19, 20)
16. MD <- INC(MD)
17. M * DCD(MA) <- MD; if (~(v/MD)) then (PC <- INC(PC)); => (2)
18. AC <- MD; => (2)
19. AC <- AC & MD; => (2)
20. OBUS = ADD(AC; MD); AC <- OBUS[1:18]; lf <- OBUS; => (2)
21. MD <- 5 T 0, PC
22. M * DCD(MA) <- MD; PC <- INC(MA); => (2)
23. M * DCD(MA) <- AC; => (2)
24. PC <- MA; => (2)
```