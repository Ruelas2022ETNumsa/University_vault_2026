## Diagrama de flujo del DMA

1. Definición formal — El acceso directo a memoria $DMA$ es una técnica en la que un módulo de E/S específico toma el control de las operaciones de transferencia para mover bloques de datos directamente entre la memoria principal y el periférico, sin intervención continua del procesador [1, 2].

2. Idea clave — El procesador solo interviene al inicio (para cargar parámetros como dirección inicial y cuenta de palabras) y al final de la transferencia (recibiendo una interrupción de fin de bloque), permitiendo que ejecute otras tareas mientras el controlador de DMA "roba" ciclos de bus para el movimiento de datos [3-5].

3. Figura o diagrama

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    node distance=1.2cm,
    every node/.style={font=\footnotesize},
    block/.style={rectangle, draw, fill=teal!10, text width=3cm, align=center, minimum height=0.8cm},
    decision/.style={diamond, draw, fill=orange!10, text width=2cm, align=center, inner sep=0pt},
    step/.style={circle, draw, fill=gray!20, inner sep=2pt},
    arrow/.style={-Stealth, thick}
]

% Flujo principal SIC (Pasos 90-111)
\node (start) [step] {2};
\node (scan) [decision, below=0.5cm of start] {90. scan: 1? \\ \tiny{$\lor/(DCD(CC) \land BCR)$}};
\node (inc_cc) [block, right=1.5cm of scan] {91. $CC \leftarrow INC(CC)$};
\node (fetch) [block, below=0.8cm of scan] {92-95. Cargar cuenta de palabras a $BWC$};
\node (addr) [block, below=0.5cm of fetch] {95-98. Formar dirección actual de memoria};
\node (type) [decision, below=0.8cm of addr] {99. ¿Tipo? \\ \tiny{$1=In / 0=Out$}};

% Ramas
\node (output) [block, below left=1.2cm and 0.5cm of type] {100-102. Leer de Memoria y enviar por $IOBUS$};
\node (input) [block, below right=1.2cm and 0.5cm of type] {103-106. Obtener de $IOBUS$ y guardar en Memoria};

% Unión y fin
\node (done) [decision, below=3.5cm of type] {107. ¿Bloque \\ terminado?};
\node (bufend) [block, left=1.5cm of done] {108. $bufend = 1$};
\node (store) [block, below=0.8cm of done] {109-111. $BUFRDY = 1$ y guardar nuevo $BWC$};

% Conexiones
\draw [arrow] (start) -- (scan);
\draw [arrow] (scan) -- node[anchor=south] {No} (inc_cc);
\draw [arrow] (inc_cc) |- (scan);
\draw [arrow] (scan) -- node[anchor=left] {Yes} (fetch);
\draw [arrow] (fetch) -- (addr);
\draw [arrow] (addr) -- (type);
\draw [arrow] (type) -| node[anchor=south east, pos=0.2] {Output (0)} (output);
\draw [arrow] (type) -| node[anchor=south west, pos=0.2] {Input (1)} (input);
\draw [arrow] (output) |- (done);
\draw [arrow] (input) |- (done);
\draw [arrow] (done) -- node[anchor=south] {Yes} (bufend);
\draw [arrow] (done) -- node[anchor=left] {No} (store);
\draw [arrow] (bufend) |- (start);
\draw [arrow] (store) -- ++(4,0) |- (start);

\end{tikzpicture}
\end{document}
```
*Fig. 11-13 · Flujograma de la secuencia Buffer/DMA en el computador SIC: describe el proceso de barrido de canales (scan), obtención de parámetros y transferencia bidireccional.* [6, 7]

4. Ejercicios resueltos

##### Ej. Describir la secuencia AHPL de control para la transferencia de bloque (Buffer) del SIC.

**Resolución**
Se implementa una secuencia de 22 pasos $90-111$ que gestiona el barrido de canales listos y la transferencia directa a memoria [8-16].

1) Tabla de declaraciones

| Identificador | Sección | Tamaño  | Rol                                                         |
| ------------- | ------- | ------- | ----------------------------------------------------------- |
| `BCR`         | MEMORY  | `(4)`   | Buffer Control Register: indica qué canal requiere servicio |
| `CC`          | MEMORY  | `(2)`   | Channel Counter: puntero para el barrido de canales         |
| `BWC`         | MEMORY  | `(13)`  | Buffer Word Count: cuenta (negativa) de palabras restantes  |
| `BIOR`        | MEMORY  | `(4)`   | Buffer Input/Output Register: define dirección (In/Out)     |
| `BUFRDY`      | OUTPUTS | `(4)`   | Indica al periférico que la CPU está lista para el dato     |
| `bufend`      | OUTPUTS | escalar | Señal de fin de bloque                                      |
| `IOBUS`       | COMBUS  | `(18)`  | Bus de datos para comunicación con periféricos              |

2) Bloque de código
```ahpl
90. -> (\/(DCD(CC) /\ BCR))/(92)
91. CC <- INC(CC)
    -> (90)
92. IR(5:17) <- BADDR(CC); BCR * DCD(CC) <- 4 T 0
93. MA <- IR(5:17)
94. MD <- BUSFN(M; DCD(MA)); IR(5:17) <- INC(IR(5:17))
95. MA <- IR(5:17); BWC <- MD
96. MD <- BUSFN(M; DCD(MA))
97. MA <- ADD(MD; BWC)
98. BWC <- INC(BWC); BUFRDY = DCD(CC)
99. NO DELAY
    -> (\/(DCD(CC) /\ BIOR))/(103)
100. MD <- BUSFN(M; DCD(MA))
101. -> (ready)/(101)
102. IOBUS = MD; datavalid = 1
     -> (accept, ~accept)/(107, 102)
103. ready = 1
     -> (datavalid)/(103)
104. MD <- IOBUS
105. M * DCD(MA) <- MD
106. accept = 1
     -> (datavalid)/(106)
107. NO DELAY
     -> (\/BWC)/(109)
108. bufend = 1
     -> (2)
109. BUFRDY = DCD(CC)
110. MA <- BADDR(CC); MD <- BWC
111. M * DCD(MA) <- MD
     -> (2)
```

3) Tabla de pasos (Resumen de la lógica)

| Paso   | Operación                    | Condición        | Estado resultante                                                         |
| ------ | ---------------------------- | ---------------- | ------------------------------------------------------------------------- |
| `90.`  | $\rightarrow (92)$       | $BCR_i = 1$  | Salta si el canal actual tiene una petición activa.                       |
| `91.`  | $CC \leftarrow INC(CC)$  | —                | Incrementa puntero para probar el siguiente canal.                        |
| `97.`  | $MA \leftarrow MD + BWC$ | —                | Calcula la dirección real: $\text{DirFinal} + \text{CuentaNegativa}$. |
| `99.`  | $\rightarrow (103)$      | $BIOR_i = 1$ | Bifurca a secuencia de Entrada si el bit de dirección es 1.               |
| `107.` | $\rightarrow (109)$      | $BWC \neq 0$ | Si la cuenta no es cero, guarda el progreso; si es cero, termina bloque.  |

