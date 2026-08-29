## Código AHPL: Interface de Impresora

### 1. Definición formal
La **interface de impresora** (*Printer Interface*) es un módulo AHPL de control y transferencia de datos que sirve para coordinar la comunicación asíncrona y estructurada entre una unidad central de procesamiento (CPU) y un periférico de impresión física.

### 2. Idea clave
La interface utiliza un protocolo de transferencia bidireccional (*handshake*) mediante buses combinacionales, alternando el almacenamiento de los bytes alto y bajo en un registro intermedio para realizar la transferencia completa bajo el control de una señal indicadora de fase.

### 3. Caja negra del módulo
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[node distance=2cm, auto, >=Latex,
  module/.style={rectangle, draw=teal, fill=teal!5, thick, minimum width=4cm, minimum height=6cm, align=center},
  signal/.style={->, thick, >=stealth, color=gray!80!black},
  bus/.style={<->, double, thick, >=stealth, color=orange}
]
  % Módulo Principal
  \node (mod) [module] at (0,0) {\textbf{PRINTER INTERFACE}\\[1em] \textit{Memory:}\\[0.2em] DR, CR, first};

  % Señales de entrada (izquierda)
  \draw [signal, <-] (mod.150) -- ++(-2,0) node[above, pos=0.1] {datavalid};
  \draw [signal, <-] (mod.170) -- ++(-2,0) node[above, pos=0.1] {wait};
  
  % Buses (izquierda inferior)
  \draw [bus] (mod.210) -- ++(-2,0) node[above, pos=0.1, color=black] {IOBUS};

  % Señales de salida (derecha)
  \draw [signal] (mod.30) -- ++(2,0) node[above, pos=0.9] {ready};
  \draw [signal] (mod.10) -- ++(2,0) node[above, pos=0.9] {accept};
  \draw [signal] (mod.-10) -- ++(2,0) node[above, pos=0.9] {print};
  \draw [signal] (mod.-30) -- ++(2,0) node[above, pos=0.9] {feed};
  \draw [signal] (mod.-50) -- ++(2,0) node[above, pos=0.9] {CHAR};

\end{tikzpicture}
\end{document}
```

### 4. Código AHPL completo

```ahpl
MODULE: PRINTER INTERFACE
MEMORY: DR; CR; first(JK)
OUTPUTS: CHAR; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS
1. ready = 1
   -> (datavalid)/(1)
2. DR ← IOBUS; accept = 1; first ← 1
3. CR ← (DR10:17 ∧ first) ∨ (DR1:8 ∧ ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first ← 0; busy * ~first ← 0
   -> (first, ~first)/(3, 8)
8. DEAD END
END SEQUENCE
CHAR = CR
END
```