## Organización y Arquitectura del Computador SIC (24 pasos)

1. Definición formal
El computador **SIC (Small Instructional Computer)** es un procesador de palabra de 18 bits con direccionamiento de una sola dirección, un espacio de direccionamiento de 8192 palabras de memoria y dos registros de índice (\(IA, IB\)), cuya unidad de control ejecuta de forma cableada una secuencia síncrona de 24 pasos para realizar las fases de búsqueda, direccionamiento y ejecución de sus instrucciones direccionadas a memoria.

2. Idea clave
La secuencia de control de 24 pasos simplifica la decodificación compartiendo el direccionamiento indexado e indirecto mediante un bus común de salida (\(OBUS\)), permitiendo que la ALU resuelva tanto las sumas de direcciones como las operaciones aritméticas en las mismas etapas.

3. Figura o diagrama (si existe o aplica TikZJax)
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    node distance=1.4cm and 2.2cm,
    block/.style={draw=teal, fill=teal!10, rectangle, minimum width=3.2cm, minimum height=0.75cm, align=center, rounded corners=2pt},
    decision/.style={draw=orange, fill=orange!10, diamond, minimum width=1.6cm, minimum height=1.6cm, align=center},
    side/.style={draw=violet, fill=violet!10, rectangle, minimum width=2.8cm, minimum height=0.75cm, align=center, rounded corners=2pt},
    arr/.style={draw=gray, -{Stealth}, thick}
]
\node[block] (fetch) {Fetch (1--4)};
\node[decision, below=of fetch] (dec1) {\small Operativa?};
\node[block, below=of dec1] (addr) {Resolver direcci\'on (6--12)};
\node[decision, below=of addr] (dec2) {\small Modo?};
\node[side, right=of dec2] (idx) {Indexado\\$MA\!\leftarrow\!ADD(I,IR)$};
\node[side, left=of dec2] (ind) {Indirecto\\$MA\!\leftarrow\!MD[5\!:\!17]$};
\node[block, below=2.2cm of dec2] (exec) {Ejecuci\'on (13--23)};
\node[block, below=of exec] (inc) {$PC\leftarrow INC(PC)$ (24)};

\draw[arr] (fetch) -- (dec1);
\draw[arr] (dec1) -- node[right, font=\small]{No} (addr);
\draw[arr] (dec1.east) -- ++(1.2,0) |- node[right, font=\small, near start]{S\'i (111)} (exec.east);
\draw[arr] (addr) -- (dec2);
\draw[arr] (dec2) -- node[above, font=\small]{Idx} (idx);
\draw[arr] (dec2) -- node[above, font=\small]{Ind} (ind);
\draw[arr] (idx.south) |- (exec.east);
\draw[arr] (ind.south) |- (exec.west);
\draw[arr] (dec2) -- node[right, font=\small]{Dir} (exec);
\draw[arr] (exec) -- (inc);
\draw[arr] (inc.west) -- ++(-2.2,0) |- (fetch.west);
\end{tikzpicture}
\end{document}
```
*Fig. 6.3* · Diagrama de flujo simplificado del ciclo de instrucción del computador SIC.
[[825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf#page=170]]
*Fig. 6.3*
justificación: Este diagrama ilustra las transiciones de control de las fases de búsqueda y resolución de direcciones (directo, indexado e indirecto) hacia la fase de ejecución y retorno de la secuencia de 24 pasos de SIC.

Propiedades omitidas en el nivel B:
* **Restricción de Indexación e Indirección:** El hardware de SIC limita la indexación indirecta de tal modo que la combinación \(10\) en los bits 3 y 4 del IR representa indexación directa con el registro de índice \(IA\) (sin indirección), mientras que la combinación \(11\) representa indexación con el registro \(IB\) seguida obligatoriamente de direccionamiento indirecto.
* **Compartición del bus OBUS:** Para evitar duplicación de lógica, el bus \(OBUS\) se utiliza tanto para transferencias de datos hacia el acumulador (\(AC\)) como para alimentar los resultados del sumador en el cálculo de direcciones indexadas.
* **Optimización de PC y MD:** Los registros \(PC\), \(MD\), \(IA\) e \(IB\) comparten la misma unidad lógica de incremento (\(INC\)) para ahorrar compuertas en el silicio.

4. Ejercicios resueltos (solo nivel C)
##### Ej. Modificar la secuencia de control de 24 pasos del Computador SIC para que la instrucción ISZ (Increment and Skip if Zero) incremente el contenido de la dirección de memoria MA y, si el resultado es cero, salte 15 instrucciones hacia adelante (es decir, sume 15 a PC en lugar de omitir solo una instrucción).

**Resolución**
Sustituir el incremento simple de la instrucción de salto por una suma de constante en el paso \(23-1\) para lograr el desplazamiento neto deseado.

Para la modificación de la secuencia AHPL de ejecución de ISZ:

```ahpl
22.  MD <- INC(MD)                                         // Incrementa el operando leído en MD
23.  M * DCD(MA) <- MD                                     // Almacena el operando modificado en memoria
     -> (\/MD) / (24)                                      // Si no es cero, va directamente al paso 24 (incremento normal)
23-1. PC <- ADD(PC; 14\top13)                              // Si es cero, suma 14 en formato de 13 bits a PC
24.  PC <- INC(PC)                                         // Incremento final común (PC <- PC + 14 + 1 = PC + 15)
     -> (1)                                                // Retorna al ciclo de búsqueda
```
