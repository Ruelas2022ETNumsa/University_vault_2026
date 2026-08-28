## Organización y Arquitectura del Computador SIC (24 pasos)

### 1. Definición formal
El computador **SIC (Small Instructional Computer)** es un sistema digital de dirección única que posee una memoria principal de \( 2^{13} = 8192 \) localidades direccionables, donde cada dato o instrucción almacenada tiene la forma de una **palabra binaria de 18 bits**. Su arquitectura de control ejecuta las instrucciones de referencia a memoria a través de una secuencia de **24 pasos de control** escritos en el lenguaje de transferencia de registros **AHPL**, los cuales integran el ciclo de búsqueda (*fetch*), la decodificación del direccionamiento y la ejecución de operaciones elementales.

### 2. Idea clave
La eficiencia del ciclo de control de **24 pasos** radica en el uso de pasos de control de tipo **NO DELAY** que permiten realizar la decodificación del direccionamiento de manera combinacional en el mismo ciclo de reloj. Esto evita retardos innecesarios antes de decidir si se requiere indexación, direccionamiento indirecto o bifurcaciones de salto inmediato.

### 3. Figuras y diagramas

#### CASO A — Figuras en el libro fuente

![[pegar_imagen]]
*Fig. 2-2 · Basic SIC instruction codes and format*
[[825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf#page=21]]
*Fig. 2-2*
justificación: Muestra la distribución y el formato de los 18 bits de una instrucción en el computador SIC, detallando los campos de código de operación (bits 0 a 2), indexación (bit 3), indirección (bit 4) y el campo de dirección de memoria (bits 5 a 17).

![[pegar_imagen]]
*Fig. 6-5 · Alternate approach to address modification*
[[825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf#page=173]]
*Fig. 6-5*
justificación: Detalla el diagrama de bloques para la decodificación lógica y bifurcación combinacional de los modos de direccionamiento directo, indirecto e indexado en el ciclo de control del SIC.

---

#### CASO B — Flujo general de control del SIC (Pasos 1 al 24)

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=2.5cm, minimum height=0.6cm, text centered, draw=teal, fill=teal!10, text=teal!50!black, font=\bfseries]
\tikzstyle{process} = [rectangle, minimum width=2.5cm, minimum height=0.6cm, text centered, draw=teal, fill=teal!5, text=teal!70!black]
\tikzstyle{decision} = [diamond, aspect=2, minimum width=2.2cm, minimum height=0.8cm, text centered, draw=orange, fill=orange!10, text=orange!80!black]
\tikzstyle{arrow} = [thick, ->, >=stealth, draw=gray]

\begin{tikzpicture}[node distance=1.3cm, scale=0.85, every node/.style={transform shape}]
  \node (start) [startstop] {Espera start (P1)};
  \node (fetch) [process, below of=start] {Fetch (P2 - P4)};
  \node (dec_op) [decision, below of=fetch, yshift=-0.2cm] {¿Operativa (111)?};
  
  \node (addr_mod) [process, below of=dec_op, yshift=-0.4cm] {Modif. Dirección (P6 - P11)};
  \node (dec_jmp) [decision, below of=addr_mod, yshift=-0.2cm] {¿JMP (110)?};
  
  \node (jmp_exec) [process, left of=dec_jmp, xshift=-2.2cm] {PC <- MA (P13)};
  \node (type_dec) [decision, below of=dec_jmp, yshift=-0.4cm] {¿Tipo de Instrucción?};
  
  \node (read_path) [process, left of=type_dec, xshift=-2.2cm] {Lectura (ISZ, LAC, AND, TAD)};
  \node (write_path) [process, right of=type_dec, xshift=2.2cm] {Escritura (JMS, DAC)};
  
  \node (op_exec) [process, right of=dec_op, xshift=3.2cm] {Inst. Operativas (P25 - P47)};
  
  \draw [arrow] (start) -- (fetch);
  \draw [arrow] (fetch) -- (dec_op);
  \draw [arrow] (dec_op) -- node[anchor=south] {Sí} (op_exec);
  \draw [arrow] (dec_op) -- node[anchor=east] {No} (addr_mod);
  \draw [arrow] (addr_mod) -- (dec_jmp);
  \draw [arrow] (dec_jmp) -- node[anchor=south] {Sí} (jmp_exec);
  \draw [arrow] (dec_jmp) -- node[anchor=east] {No} (type_dec);
  \draw [arrow] (type_dec) -- node[anchor=south] {Lectura} (read_path);
  \draw [arrow] (type_dec) -- node[anchor=south] {Escritura} (write_path);
  
  % Feedback loops to Fetch (P2)
  \draw [arrow] (op_exec) |- (fetch);
  \draw [arrow] (jmp_exec) |- (fetch);
  \draw [arrow] (read_path) |- (fetch);
  \draw [arrow] (write_path) |- (fetch);
\end{tikzpicture}
\end{document}
```

---

### 4. Secuencia de Control en AHPL (Pasos 1 al 24)
Esta es la secuencia AHPL formal para el ciclo de búsqueda y ejecución de instrucciones de referencia a memoria en el procesador SIC:

```ahpl
MODULE: SIC
MEMORY: AC; MD; PC; IR; IA; IB; MA; lf; M
INPUTS: start
BUSES: ABUS; BBUS

1. => (~SYN(start)) / (1)
2. MA <- PC
3. MD <- BUSFN(M; DCD(MA))
4. IR <- MD
5. => (IR & IR & IR) / (25)
6. NO DELAY
   => (~IR & ~IR, ~IR & IR, IR) / (13, 7, 10)
7. MA <- IR[5:17]
8. MD <- BUSFN(M; DCD(MA))
9. NO DELAY
   IR[5:17] <- MD[5:17]; => (12)
10. MA <- ADD(IR[5:17]; IA); => (12)
11. MA <- ADD(IR[5:17]; IB)
12. NO DELAY
    => (IR & IR, ~(IR & IR)) / (13, 14)
13. PC <- MA; => (2)
14. NO DELAY
    => (~IR, IR & ~IR & ~IR, IR & ~IR & IR, IR & IR & ~IR) / (15, 21, 23, 24)
15. MD <- BUSFN(M; DCD(MA))
16. => (DCD(IR[0:2])) / (17, 18, 19, 20)
17. MD <- INC(MD)
18. M * DCD(MA) <- MD; => (~(v/MD)) / (2)
19. PC <- INC(PC); => (2)
20. AC <- MD; => (2)
21. AC <- AC & MD; => (2)
22. OBUS = ADD(AC; MD); AC <- OBUS[1:18]; lf <- OBUS; => (2)
23. MD <- (AC ! (5 T 0, INC(PC))) * (IR, ~IR)
24. M * DCD(MA) <- MD; => (~IR) / (2)
```

---

### 5. El Ciclo de Instrucciones Operativas (Pasos 25 al 47) - Fin de T1
Cuando el código de operación decodificado en el **Paso 5** corresponde a `111` (instrucción operativa o de registro), el control se desvía hacia el **Paso 25** para dar inicio a la secuencia de ejecución de instrucciones internas de CPU. Esta fase representa la culminación del procesador SIC y el cierre temático de la unidad **T1**:

*   **Decodificación de Evento Primario (Pasos 25-29)**: Se analizan los bits correspondientes del `IR` de manera simultánea para ejecutar las operaciones que modifican el acumulador (`AC`) y el indicador de acarreo (`lf`). Aquí se procesan de manera asíncrona o bajo reloj instrucciones como `CLA` (limpiar acumulador), `CMA` (complementar acumulador), `CLL` (limpiar acarreo) y `STL` (fijar acarreo).
*   **Rotaciones del Acumulador (Pasos 30-34)**: Si se activa el bit de rotación, el acumulador y la bandera de enlace rotan a la izquierda (`RAL`) o a la derecha (`RAR`), empleando transferencias sincronizadas de registros que conectan el bit de mayor o menor peso con la bandera `lf`.
*   **Evento Secundario y Saltos Condicionales (Pasos 35-47)**: Se realiza el test condicional de los registros. Dependiendo de los bits de prueba, la máquina ejecuta saltos condicionales incrementando directamente el Contador de Programa (`PC <- INC(PC)`) si se cumplen condiciones lógicas como `SZA` (salto si acumulador es cero), `SZL` (salto si acarreo es cero) o `SPA`/`SNA` (salto por signo del acumulador). Al finalizar estas pruebas, la secuencia retorna incondicionalmente al **Paso 2** para buscar la siguiente instrucción.