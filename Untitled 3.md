## Organización y Arquitectura del Computador SIC (24 pasos)

### 1. Definición formal
El computador instruccional pequeño (SIC) posee un espacio de memoria direccionable de \( 2^{13} = 8192 \) palabras de \( 18 \) bits cada una, con direcciones que van desde \( 0 \) hasta \( 8191 \) (\( 0 \) a \( 17777 \) en octal) [1#page=19]. Su arquitectura se organiza en torno a una sección de control cableada (secuenciador de pasos AHPL) y una sección de datos que contiene registros de alta velocidad interconectados por buses comunes de \( 18 \) bits (\( ABUS \) y \( BBUS \)) y una unidad aritmético-lógica (ALU) [1#page=19, 1#page=164].

### 2. Idea clave
La arquitectura del SIC destaca por su simplicidad: implementa un protocolo de direccionamiento que soporta direccionamiento directo, indirecto e indexado (usando dos registros de índice, \( IA \) y \( IB \)) [1#page=19, 1#page=170]. El direccionamiento y la ejecución de sus 7 instrucciones direccionadas se realizan secuencialmente en un ciclo de control básico de 24 pasos [1#page=170, 20#page=3].

### 3. Figuras y diagramas

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily, scale=0.95]
% IR Fields
\draw[thick, fill=teal!10] (0,0) rectangle (2,0.8);
\node at (1,0.4) {\small\textbf{OP CODE}};

\draw[thick, fill=orange!10] (2,0) rectangle (3.2,0.8);
\node at (2.6,0.4) {\small\textbf{IA/IB}};

\draw[thick, fill=orange!10] (3.2,0) rectangle (4.4,0.8);
\node at (3.8,0.4) {\small\textbf{I}};

\draw[thick, fill=violet!10] (4.4,0) rectangle (9,0.8);
\node at (6.7,0.4) {\small\textbf{ADDRESS}};

% Bit indices
\node[above] at (0,0.8) {\tiny 0};
\node[above] at (2,0.8) {\tiny 2};
\node[above] at (3.2,0.8) {\tiny 3};
\node[above] at (4.4,0.8) {\tiny 4};
\node[above] at (9,0.8) {\tiny 17};

% Labels below
\node[below, align=center] at (1,-0.1) {\tiny Bits 0--2\\ \tiny Código de Op.};
\node[below, align=center] at (2.6,-0.1) {\tiny Bit 3\\ \tiny Indexación};
\node[below, align=center] at (3.8,-0.1) {\tiny Bit 4\\ \tiny Indirecto};
\node[below, align=center] at (6.7,-0.1) {\tiny Bits 5--17\\ \tiny Dirección de Memoria};
\end{tikzpicture}
\end{document}
```
*Fig. 2.2 · Formato y distribución de campos de una instrucción de SIC de 18 bits [1#page=21].*

---

### 4. Estructura y Declaración de Recursos del Módulo SIC
El hardware básico que constituye al procesador SIC para la ejecución de sus instrucciones direccionadas se declara formalmente en el módulo AHPL de la siguiente manera [1#page=170]:

```ahpl
MODULE: SIC
MEMORY: AC; MD; PC; IR; IA; IB; MA; lf; M
INPUTS: start
BUSES: ABUS; BBUS
```

#### Descripción de Registros y Buses (Sección de Datos) [1#page=19, 1#page=21, 1#page=164]:
*   `AC`: Acumulador de 18 bits. Almacena temporalmente los operandos y resultados de las operaciones aritméticas y lógicas de la ALU.
*   `MD`: Registro de datos de memoria de 18 bits. Actúa como buffer intermedio en los accesos de lectura y escritura a la memoria principal.
*   `PC`: Contador de programa de 13 bits. Almacena la dirección de la siguiente instrucción a ser captada de la memoria.
*   `IR`: Registro de instrucción de 18 bits. Almacena la instrucción binaria que se encuentra actualmente en ejecución.
*   `IA` e `IB`: Registros de índice de 13 bits cada uno, utilizados para el direccionamiento indexado.
*   `MA`: Registro de dirección de memoria de 13 bits. Retiene la dirección física del dato que se desea leer o escribir en la memoria.
*   `lf`: Flag de enlace (*Link Flag*) de 1 bit. Almacena el acarreo saliente de la suma de TAD y se utiliza en instrucciones de rotación.
*   `M`: Matriz de memoria RAM de 8192 palabras de 18 bits.
*   `ABUS` y `BBUS`: Buses comunes de datos de 18 bits que alimentan los operandos hacia las entradas de la unidad de suma de la ALU.

---

### 5. Secuencia de Control del SIC (24 pasos)
A continuación se presenta la secuencia de control original en AHPL para el ciclo de búsqueda, decodificación, modificación de direcciones y ejecución de las instrucciones direccionadas del SIC [1#page=170, 20#page=3]:

```ahpl
1. -> (~start)/(1)
2. MA <- PC
3. MD <- M * DCD(MA); PC <- INC(PC)
4. IR <- MD
5. -> (&/IR[0:2])/(24)
6. -> (IR, ~IR & IR, ~IR & ~IR)/(7, 10, 11)
7. -> (IR)/(9)
8. MA <- ADD(IR[5:17]; IA); -> (11)
9. MA <- ADD(IR[5:17]; IB); -> (11)
10. MA <- IR[5:17]
11. MD <- M * DCD(MA)
12. MA <- MD[5:17]
13. -> (IR)/(21)
14. MD <- M * DCD(MA)
15. -> (~IR & ~IR, ~IR & IR, IR & ~IR, IR & IR)/(16, 18, 19, 20)
16. MD <- INC(MD)
17. M * DCD(MA) <- MD; PC <- INC(PC) * (~(&/MD)); -> (2)
18. AC <- MD; -> (2)
19. AC <- AC & MD; -> (2)
20. AC, lf <- ADD(AC; MD); -> (2)
21. -> (~IR & ~IR, ~IR & IR, IR & ~IR)/(22, 24, 26)
22. MD <- 0, 0, 0, 0, 0, PC
23. M * DCD(MA) <- MD; PC <- INC(MA); -> (2)
24. MD <- AC
25. M * DCD(MA) <- MD; -> (2)
26. PC <- MA; -> (2)
```

---

### 6. Análisis Detallado de las Fases del Ciclo

#### Fase de Búsqueda (*Fetch*) [1#page=170]:
*   **Paso 1**: Bucle de espera síncrona. El control permanece en este paso hasta que se activa la señal externa de inicio (\( start = 1 \)).
*   **Paso 2**: Transferencia de la dirección de la instrucción actual desde el contador de programa (\( PC \)) hacia el registro de dirección de memoria (\( MA \)).
*   **Paso 3**: Operación combinada simultánea. Se solicita una lectura de memoria en la dirección apuntada por \( MA \) hacia el registro \( MD \), y de manera paralela se incrementa el contenido de \( PC \) para apuntar a la siguiente dirección física.
*   **Paso 4**: El contenido binario de la instrucción leída se transfiere de \( MD \) a \( IR \).

#### Fase de Decodificación y Bifurcación Operativa [1#page=170]:
*   **Paso 5**: Prueba de exclusión. Si los bits de código de operación \( IR_{0:2} \) son todos \( 1 \) (instrucciones operativas o de E/S, código octal \( 7 \)), se salta incondicionalmente a la secuencia operativa que inicia a partir del paso \( 24 \) (en la secuencia general de la máquina).

#### Fase de Modificación de Dirección (Direccionamiento) [1#page=170, 20#page=3]:
*   **Paso 6**: Análisis de las banderas de direccionamiento. Si se requiere indexación (\( IR_3 = 1 \)), bifurca a \( 7 \). Si no hay indexación pero sí direccionamiento indirecto (\( \overline{IR_3} \land IR_4 = 1 \)), salta a \( 10 \). Si no hay ninguna modificación (direccionamiento directo), salta a \( 11 \).
*   **Paso 7**: Selección del registro de índice. Si \( IR_4 = 1 \) se selecciona el registro \( IB \) (pasando al paso \( 9 \)), de lo contrario se selecciona el registro \( IA \) (pasando al paso \( 8 \)).
*   **Pasos 8 y 9**: Se realiza la suma de la base de la dirección (\( IR_{5:17} \)) con el registro de índice correspondiente (\( IA \) o \( IB \)), cargando el resultado en \( MA \). Posteriormente, se bifurca incondicionalmente al paso \( 11 \).
*   **Paso 10**: En caso de direccionamiento indirecto exclusivo, se copia la dirección del puntero desde \( IR_{5:17} \) hacia \( MA \).
*   **Pasos 11 y 12**: Se realiza una lectura intermedia de memoria para extraer el puntero de dirección real hacia \( MD \) y, en el paso siguiente, se extrae la dirección modificada \( MD_{5:17} \) cargándola finalmente en \( MA \).

#### Fase de Bifurcación de Ejecución [1#page=170, 20#page=3]:
*   **Paso 13**: Bifurcación por lectura o escritura. Si \( IR_0 = 1 \), la instrucción corresponde a una operación de escritura o salto (JMS, DAC, JMP), bifurcando a \( 21 \). Si \( IR_0 = 0 \), corresponde a una operación de lectura (ISZ, LAC, AND, TAD), procediendo secuencialmente al paso \( 14 \).

#### Fases de Ejecución Individual de Instrucciones direccionadas:

##### A. Operaciones de Lectura de Memoria (\( IR_0 = 0 \)) [1#page=170, 20#page=3]:
*   **Paso 14**: Lectura del operando final de la dirección física cargada en \( MA \), transfiriéndolo a \( MD \).
*   **Paso 15**: Decodificador de operación ALU. Se examinan los bits \( IR_{1:2} \) para bifurcar a la sub-secuencia de la operación correspondiente:
    *   \( 00 \): **ISZ** (paso \( 16 \))
    *   \( 01 \): **LAC** (paso \( 18 \))
    *   \( 10 \): **AND** (paso \( 19 \))
    *   \( 11 \): **TAD** (paso \( 20 \))
*   **Pasos 16--17 (ISZ - Increment and Skip if Zero)**: Se incrementa el operando en \( MD \) (paso \( 16 \)) y se guarda de vuelta en la memoria principal. Si el operando resultante es igual a cero (\( \overline{\bigvee / MD} = 1 \)), se incrementa el contador de programa \( PC \) nuevamente para saltar la siguiente instrucción; de cualquier forma, retorna al paso \( 2 \).
*   **Paso 18 (LAC - Load Accumulator)**: Copia el contenido del operando de \( MD \) al acumulador \( AC \) y retorna a \( 2 \).
*   **Paso 19 (AND - Logical AND)**: Realiza la operación AND bit a bit entre \( AC \) y \( MD \), guardando el resultado en \( AC \) y retorna a \( 2 \).
*   **Paso 20 (TAD - Two's-Complement Add)**: Suma el acumulador con el operando de memoria utilizando el sumador binario de la ALU. El resultado se guarda en \( AC \) y el bit de acarreo de la posición más significativa actualiza el registro \( lf \), retornando a \( 2 \).

##### B. Operaciones de Escritura o Salto de Memoria (\( IR_0 = 1 \)) [1#page=170, 20#page=3]:
*   **Paso 21**: Decodificador de escritura y salto. Se analizan \( IR_{1:2} \) para bifurcar a:
    *   \( 00 \): **JMS** (paso \( 22 \))
    *   \( 01 \): **DAC** (paso \( 24 \))
    *   \( 10 \): **JMP** (paso \( 26 \))
*   **Pasos 22--23 (JMS - Jump to Subroutine)**: Carga en \( MD \) la dirección de retorno (rellenando con 5 ceros y concatenando con \( PC \)), la escribe en la primera posición de la subrutina apuntada por \( MA \) y salta cargando \( PC \) con el valor incrementado de \( MA \), retornando al inicio en \( 2 \).
*   **Pasos 24--25 (DAC - Deposit Accumulator)**: Transfiere el contenido de \( AC \) a \( MD \) (paso \( 24 \)) y realiza el almacenamiento físico en la memoria principal en la dirección apuntada por \( MA \) (paso \( 25 \)), retornando a \( 2 \).
*   **Paso 26 (JMP - Jump)**: Almacena incondicionalmente la dirección de destino \( MA \) en el contador de programa \( PC \), alterando el flujo secuencial del programa, y retorna a \( 2 \).

---
🧩 **Si lo deseas, podemos diseñar un ejercicio tipo examen (nivel C) que requiera modificar algunos de estos 24 pasos para agregar una nueva instrucción direccionada al computador SIC.**