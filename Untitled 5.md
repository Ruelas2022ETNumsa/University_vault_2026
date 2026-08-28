## Interface de Impresora Simplificada

Esta es la descripción formal en **AHPL** de una interface de impresora que utiliza líneas de control separadas y realiza la transferencia de datos de forma asíncrona mediante un **handshake de tres líneas**. La secuencia es iniciada por la propia interface cuando se encuentra lista para recibir datos.

### 1. Definición formal
La interface de la impresora tiene como entrada un vector de datos \( IOBUS_{0:17} \) que contiene **dos caracteres ASCII de 8 bits**. Utiliza señales de sincronización de bus (\( ready \), \( datavalid \), \( accept \)) y señales físicas de hardware conectadas directamente al mecanismo de la impresora (\( print \), \( feed \), \( wait \)).

### 2. Idea clave
La interface desempaqueta una palabra de 18 bits que contiene dos caracteres independientes colocados en \( IOBUS_{10:17} \) y \( IOBUS_{1:8} \). Para controlar qué carácter se está imprimiendo se utiliza el flip-flop de control \( first \) como bandera de estado.

### 3. Diagrama de Caja Negra
A continuación, se detalla la estructura física del módulo y sus conexiones combinacionales y sincrónicas:

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=1.2,>=Stealth]
  % Módulo principal
  \draw[draw=teal, ultra thick, fill=teal!5] (0,0) rectangle (4,5);
  \node[teal, font=\bfseries] at (2,4.5) {PRINTER INTERFACE};

  % Registros Internos (gray)
  \draw[draw=gray, thick, fill=gray!10] (0.5,2.5) rectangle (1.8,3.2);
  \node[gray, font=\small\bfseries] at (1.15,2.85) {DR};

  \draw[draw=gray, thick, fill=gray!10] (2.2,2.5) rectangle (3.5,3.2);
  \node[gray, font=\small\bfseries] at (2.85,2.85) {CR};

  \draw[draw=gray, thick, fill=gray!10] (1.5,1.2) rectangle (2.5,1.8);
  \node[gray, font=\small\bfseries] at (2,1.5) {first};

  % Entradas de bus y control (Left)
  \draw[<-] (-1.8,4) -- (0,4) node[midway, above, font=\small, orange] {datavalid};
  \draw[->, very thick, color=violet] (-1.8,3) -- (0,3) node[midway, above, font=\small] {IOBUS};
  \draw[->] (0,2) -- (-1.8,2) node[midway, above, font=\small, orange] {ready};
  \draw[->] (0,1) -- (-1.8,1) node[midway, above, font=\small, orange] {accept};

  % Salidas hacia el periférico (Right)
  \draw[->, very thick, color=violet] (4,3) -- (5.8,3) node[midway, above, font=\small] {CHAR};
  \draw[->] (4,2) -- (5.8,2) node[midway, above, font=\small, orange] {print};
  \draw[->] (4,1) -- (5.8,1) node[midway, above, font=\small, orange] {feed};
  \draw[<-] (4,4) -- (5.8,4) node[midway, above, font=\small, orange] {wait};

\end{tikzpicture}
\end{document}
```

---

### 4. Código AHPL de la Secuencia de Control

\[
\begin{aligned}
&\textbf{MODULE: PRINTER INTERFACE} \\
&\textbf{MEMORY: } DR;\; CR;\; first \\
&\textbf{OUTPUTS: } CHAR;\; ready;\; accept;\; print;\; feed \\
&\textbf{INPUTS: } datavalid;\; wait \\
&\textbf{COMBUSES: } IOBUS \\
&\\
&1.\; ready = 1 \\
&\quad \rightarrow (\overline{datavalid})/(1) \\
&2.\; DR \leftarrow IOBUS;\; accept = 1;\; first \leftarrow 1 \\
&3.\; CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \\
&4.\; feed = RETURN(CR);\; print = RETURN(CR) \\
&5.\; \text{Null} \\
&6.\; \rightarrow (wait)/(6) \\
&7.\; first \leftarrow 0 \\
&\quad \rightarrow (first,\; \overline{first})/(3,\; 1) \\
&\\
&\text{END SEQUENCE} \\
&CHAR = CR \\
&\textbf{END}
\end{aligned}
\]

---

### 5. Lectura paso a paso

| Paso | Operación y Análisis Técnico |
| :---: | :--- |
| **1** | **Bucle de espera (Polling)**: La interface activa la línea externa \( ready = 1 \) indicando que está desocupada. Se mantiene en un bucle cerrado en el paso 1 mientras \( datavalid \) sea \( 0 \). |
| **2** | **Captura y Acuse**: Una vez que el computador coloca el dato en el bus (\( datavalid = 1 \)), la palabra se almacena en el registro de datos \( DR \leftarrow IOBUS \), se activa la señal combinacional de confirmación \( accept = 1 \) por un ciclo de reloj y se inicializa la bandera \( first \leftarrow 1 \). |
| **3** | **Multiplexación de Carácter**: Se transfiere a \( CR \) la primera mitad de la palabra (\( DR_{10:17} \)) seleccionada mediante lógica condicional por \( first \). En la segunda vuelta, cuando \( first = 0 \), se transferirá la segunda mitad (\( DR_{1:8} \)). |
| **4** | **Activación del Comando**: Las líneas de salida física \( feed \) o \( print \) se activan de manera combinacional a partir del valor decodificado de \( CR \) a través de la función combinacional externa \( RETURN(CR) \). |
| **5** | **Ciclo de Estabilización**: Un paso nulo (\( \text{Null} \)) que no ejecuta ninguna transferencia, pero consume un ciclo de reloj para dar tiempo a que el periférico responda levantando la línea \( wait \). |
| **6** | **Espera de Ejecución**: Bucle de polling asíncrono. El control permanece en este paso mientras el mecanismo de la impresora esté realizando la acción física (\( wait = 1 \)). |
| **7** | **Control de Bucle Interno**: Al finalizar la impresión, se predispone el registro \( first \leftarrow 0 \). Como el cambio en el flip-flop ocurre al flanco de reloj de salida, la bifurcación condicional evalúa el valor *actual* de \( first \): si es \( 1 \), regresa al paso 3 para imprimir el segundo carácter; si es \( 0 \), vuelve al paso 1 para esperar una nueva transferencia. |
| **CHAR=CR** | **Salida Combinacional Permanente**: Fuera de la secuencia, la salida física de datos \( CHAR \) siempre refleja de manera directa e inmediata el contenido actual de \( CR \). |

🤠 ¿Te gustaría que modifiquemos este código para que trabaje bajo el control directo de la CPU utilizando el bus de control CSBUS del sistema SIC?