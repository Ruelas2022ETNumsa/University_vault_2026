## Enunciado

Diseñá en AHPL una interfaz de impresora que reciba de la CPU un trabajo de una o varias planas, donde cada plana es un bloque de hasta 1K palabras de 18 bits (dos caracteres ASCII por palabra). La interfaz debe:

1. Recibir y guardar cada plana, hasta completar 1K palabras o hasta recibir 4 palabras vacías seguidas.
2. Imprimir cada plana carácter por carácter, solo hasta la última palabra con texto, sin imprimir los espacios vacíos del final.
3. Enviar el retorno de carro como avance de papel y esperar a que la impresora esté libre antes de cada carácter.
4. Si la plana se llenó, imprimirla y recibir otra; si se cortó por 4 palabras vacías, imprimirla y dar por terminado el trabajo.
5. No imprimir nada si la plana no trae texto.
6. Informar a la CPU, cuando lo consulte, si la interfaz está ocupada mientras dura todo el trabajo.

<div class="break-page"></div>

### Declaración de variables

Registros, salidas, entradas y líneas de bus que usa la interfaz.

| Identificador | Sección | Tamaño       | Rol                                                                                                     |
| ------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| `DR`          | MEMORY  | `[18]`       | Registro de datos que almacena la palabra recibida desde `IOBUS` o leída desde `BUFFER`                 |
| `CR`          | MEMORY  | `[8]`        | Registro de carácter que almacena el código ASCII a enviar a la impresora                               |
| `BUFFER`      | MEMORY  | `[1024, 18]` | Memoria RAM interna de 1024 palabras de 18 bits para almacenar el bloque de datos de la plana           |
| `cnt`         | MEMORY  | `[10]`       | Contador y puntero de dirección de 10 bits ($2^{10} = 1024$) para indexar `BUFFER`                      |
| `limit`       | MEMORY  | `[10]`       | Registro de 10 bits que guarda la dirección siguiente a la última palabra no vacía recibida en la plana |
| `empty`       | MEMORY  | `[3]`        | Contador de 3 bits para registrar hasta 4 palabras vacías consecutivas en la plana                      |
| `busy`        | MEMORY  | `escalar`    | Flip-flop de estado que indica si la interfaz está procesando la recepción o impresión de la secuencia  |
| `first`       | MEMORY  | `escalar`    | Flip-flop de control que selecciona el primer ($1$) o segundo ($0$) carácter ASCII en `DR`              |
| `has_data`    | MEMORY  | `escalar`    | Flip-flop de estado que indica si la plana actual contiene texto útil no vacío                          |
| `end_print`   | MEMORY  | `escalar`    | Flip-flop de estado que indica la llegada a la dirección límite de impresión de la plana                |
| `CHAR`        | OUTPUTS | `[8]`        | Bus de salida combinacional conectado a `CR` hacia la impresora                                         |
| `print`       | OUTPUTS | `escalar`    | Señal de salida que activa la impresión de un carácter en la impresora                                  |
| `feed`        | OUTPUTS | `escalar`    | Señal de salida que activa el avance de papel o retorno de carro                                        |
| `wait`        | INPUTS  | `escalar`    | Señal de entrada desde la impresora que indica que la mecánica está ocupada                             |
| `csrdy`       | INPUTS  | `escalar`    | Señal de entrada que indica la presencia de un comando válido en `CSBUS`                                |
| `IOBUS`       | COMBUS  | `[18]`       | Bus de datos bidireccional del sistema de 18 bits                                                       |
| `CSBUS`       | COMBUS  | `[12]`       | Bus de control y selección de dispositivo de 12 bits                                                    |
| `ready`       | COMBUS  | `escalar`    | Línea de control que indica disponibilidad para recibir/enviar datos                                    |
| `datavalid`   | COMBUS  | `escalar`    | Línea de control que valida la presencia de un dato en el bus                                           |
| `accept`      | COMBUS  | `escalar`    | Línea de control de handshake que confirma la recepción del dato/comando                                |

### Diagrama de flujo


```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.9,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.2cm, minimum height=0.65cm, font=\small, align=center},
    hs_operation/.style={draw=orange, thick, minimum width=3.2cm, minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Nodo de inicio
\node[jump] (j1) at (0,0) {1};

% Paso 1
\node[decision] (p1) at (0,-3.2) {¿Dispositivo impresor\\seleccionado (csrdy)?};
\node[font=\scriptsize, gray, anchor=south east] at (p1.north west) {1};

% Paso 2
\node[hs_operation] (p2_op) at (0,-7.4) {Aceptar comando\\(accept = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p2_op.west) {2};

\node[decision] (p2_dec) at (0,-11.4) {¿Tipo de comando\\(CSBUS3)?};
\node[font=\scriptsize, gray, anchor=south east] at (p2_dec.north west) {2};

\node[jump] (j1_p2) at (-5.0,-15.4) {1};
\node[jump] (j0a_p2) at (0,-15.4) {0A};
\node[jump] (j3_p2) at (5.4,-11.4) {3};

% Paso 3
\node[jump] (j3_in) at (11,0) {3};
\node[decision] (p3) at (11,-3.2) {¿Línea control\\ready disponible?};
\node[font=\scriptsize, gray, anchor=south east] at (p3.north west) {3};

% Paso 4
\node[hs_operation] (p4_op) at (11,-7.4) {Enviar estatus busy\\(datavalid = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p4_op.west) {4};

\node[decision] (p4_dec) at (11,-11.4) {¿CPU confirmó\\recepción (accept)?};
\node[font=\scriptsize, gray, anchor=south east] at (p4_dec.north west) {4};

\node[jump] (j1_p4) at (11,-15.4) {1};

% Conexiones izquierda
\draw[->, thick] (j1) -- (p1);
\draw[->, thick] (p1) -- node[right, font=\small, pos=0.45]{Sí} (p2_op);
\draw[->, thick] (p1.west) -- node[above, font=\small, midway]{No} ++(-1.8,0) |- (j1.west);

\draw[->, thick] (p2_op) -- (p2_dec);
\draw[->, thick] (p2_dec.east) -- node[above, font=\small, midway]{Estatus (1)} (j3_p2.west);
\draw[->, thick] (p2_dec.south) -- node[right, font=\small, pos=0.45]{Datos (0)} (j0a_p2.north);
\draw[->, thick] (p2_dec.west) -| node[above, font=\small, pos=0.2]{Datos (0)} (j1_p2.north);

% Conexiones derecha
\draw[->, thick] (j3_in) -- (p3);
\draw[->, thick] (p3) -- node[right, font=\small, pos=0.45]{Sí} (p4_op);
\draw[->, thick] (p3.east) -- node[above, font=\small, midway]{No} ++(1.8,0) |- (j3_in.east);

\draw[->, thick] (p4_op) -- (p4_dec);
\draw[->, thick] (p4_dec) -- node[right, font=\small, pos=0.45]{Sí} (j1_p4);
\draw[->, thick] (p4_dec.east) -- node[above, font=\small, midway]{No} ++(1.8,0) |- (p4_op.east);

\end{tikzpicture}
\end{document}
```

---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.88,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.4cm, minimum height=0.65cm, font=\small, align=center},
    hs_operation/.style={draw=orange, thick, minimum width=3.4cm, minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entradas 0A y 1A
\node[jump] (j0a) at (-3.8,0) {0A};
\node[jump] (j1a) at (3.8,0) {1A};

% Paso 0A
\node[operation] (p0a) at (-3.8,-2.3) {Activar estado ocupado\\(busy = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p0a.west) {0A};

% Paso 1A
\node[operation] (p1a) at (0,-4.9) {Reiniciar cnt, limit, empty\\y banderas (has\_data = 0)};
\node[font=\scriptsize, gray, anchor=south east] at (p1a.north west) {1A};

% Paso 2A
\node[hs_operation] (p2a_op) at (0,-6.7) {Indicar listo\\(ready = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p2a_op.west) {2A};

\node[decision] (p2a_dec) at (0,-9.5) {¿Dato válido disponible\\(datavalid = 1)?};
\node[font=\scriptsize, gray, anchor=south east] at (p2a_dec.north west) {2A};

% Paso 3A
\node[operation] (p3a) at (0,-12.5) {Guardar palabra en BUFFER\\y DR; accept = 1};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p3a.west) {3A};

% Paso 4A
\node[hs_operation] (p4a_op) at (0,-14.6) {Sostener confirmación\\(accept = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p4a_op.west) {4A};

\node[decision] (p4a_dec) at (0,-17.4) {¿CPU liberó bus\\(datavalid = 0)?};
\node[font=\scriptsize, gray, anchor=south east] at (p4a_dec.north west) {4A};

% Paso 5A
\node[decision] (p5a) at (0,-21.2) {¿Palabra contiene\\texto no nulo?};
\node[font=\scriptsize, gray, anchor=south east] at (p5a.north west) {5A};

% Paso 6A y 7A
\node[operation] (p6a) at (-4.4,-24.5) {has\_data = 1; limit = cnt + 1\\Reiniciar empty = 0};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p6a.west) {6A};

\node[operation] (p7a) at (4.4,-24.5) {Incrementar palabras\\vacías (empty + 1)};
\node[font=\scriptsize, gray, anchor=west] at ([xshift=0.2cm]p7a.east) {7A};

% Paso 8A
\node[operation] (p8a_op) at (0,-26.7) {Incrementar puntero\\(cnt = cnt + 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p8a_op.west) {8A};

\node[decision] (p8a_dec) at (0,-29.8) {¿4 vacías o buffer\\lleno (1024 palabras)?};
\node[font=\scriptsize, gray, anchor=south east] at (p8a_dec.north west) {8A};

% Saltos finales
\node[jump] (j1b) at (-4.6,-33.0) {1B};
\node[jump] (j2a) at (4.6,-33.0) {2A};

% Conexiones
\draw[->, thick] (j0a) -- (p0a);
\draw[->, thick] (p0a.south) |- (p1a.west);
\draw[->, thick] (j1a.south) |- (p1a.east);
\draw[->, thick] (p1a) -- (p2a_op);
\draw[->, thick] (p2a_op) -- (p2a_dec);
\draw[->, thick] (p2a_dec) -- node[right, font=\small, pos=0.45]{Sí} (p3a);
\draw[->, thick] (p2a_dec.east) -- node[above, font=\small, midway]{No} ++(1.8,0) |- (p2a_op.east);

\draw[->, thick] (p3a) -- (p4a_op);
\draw[->, thick] (p4a_op) -- (p4a_dec);
\draw[->, thick] (p4a_dec) -- node[right, font=\small, pos=0.45]{Sí} (p5a);
\draw[->, thick] (p4a_dec.east) -- node[above, font=\small, midway]{No} ++(1.8,0) |- (p4a_op.east);

\draw[->, thick] (p5a.west) -| node[above, font=\small, pos=0.2]{Sí} (p6a.north);
\draw[->, thick] (p5a.east) -| node[above, font=\small, pos=0.2]{No} (p7a.north);

\draw[->, thick] (p6a.south) |- (p8a_op.west);
\draw[->, thick] (p7a.south) |- (p8a_op.east);

\draw[->, thick] (p8a_op) -- (p8a_dec);
\draw[->, thick] (p8a_dec.west) -| node[above, font=\small, pos=0.2]{Sí} (j1b.north);
\draw[->, thick] (p8a_dec.east) -| node[above, font=\small, pos=0.2]{No} (j2a.north);

\end{tikzpicture}
\end{document}
```

---

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.88,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.4cm, minimum height=0.65cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entrada 1B
\node[jump] (j1b) at (0,0) {1B};

% Paso 1B
\node[operation] (p1b_op) at (0,-1.6) {Reiniciar puntero\\(cnt = 0)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p1b_op.west) {1B};

\node[decision, aspect=2.5] (p1b_dec) at (0,-4.2) {¿Se recibió texto útil\\(has\_data)?};
\node[font=\scriptsize, gray, anchor=south east] at (p1b_dec.north west) {1B};

% Paso 2B
\node[operation] (p2b) at (0,-7.0) {Leer palabra de BUFFER\\a DR; first = 1};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p2b.west) {2B};

% Paso 3B
\node[operation] (p3b) at (0,-8.8) {Extraer carácter ASCII\\de DR a CR};
\node[font=\scriptsize, gray, anchor=west] at ([xshift=0.2cm]p3b.east) {3B};

% Paso 4B
\node[operation] (p4b) at (0,-10.6) {Enviar impulso\\print o feed (RETURN)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p4b.west) {4B};

% Paso 5B
\node[operation] (p5b) at (0,-12.4) {Sincronización\\(paso Null)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p5b.west) {5B};

% Paso 6B
\node[decision, aspect=2.5] (p6b) at (0,-15.0) {¿Impresora ocupada\\(wait = 1)?};
\node[font=\scriptsize, gray, anchor=south east] at (p6b.north west) {6B};

% Paso 7B
\node[operation] (p7b_op) at (0,-17.8) {Seleccionar segundo\\carácter (first = 0)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p7b_op.west) {7B};

\node[decision, aspect=2.5] (p7b_dec) at (0,-20.4) {¿Era 1er carácter?\\(valor previo de first)};
\node[font=\scriptsize, gray, anchor=south east] at (p7b_dec.north west) {7B};

% Pasos 8B-10B
\node[operation] (p8b9b) at (0,-23.2) {Incrementar cnt y evaluar\\igualdad con limit};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p8b9b.west) {8B-9B};

\node[decision, aspect=2.5] (p10b) at (0,-25.8) {¿Llegó al límite\\de texto (limit)?};
\node[font=\scriptsize, gray, anchor=south east] at (p10b.north west) {10B};

% Paso 11B
\node[decision, aspect=2.5] (p11b) at (0,-29.2) {¿Cortada por 4 vacías?\\(empty0)?};
\node[font=\scriptsize, gray, anchor=south east] at (p11b.north west) {11B};

% Pasos 12B y 13B
\node[operation] (p12b) at (0,-32.0) {Liberar interfaz\\(busy = 0)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p12b.west) {12B};

\node[operation, draw=orange] (p13b) at (0,-33.8) {Fin de secuencia\\(DEAD END)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p13b.west) {13B};

% Jump 12B si no hay datos en 1B
\node[jump] (j12b_p1b) at (5.4,-4.2) {12B};

% Jump 1A si empty0 = 0 en 11B
\node[jump] (j1a_p11b) at (5.4,-29.2) {1A};

% Conexiones
\draw[->, thick] (j1b) -- (p1b_op);
\draw[->, thick] (p1b_op) -- (p1b_dec);
\draw[->, thick] (p1b_dec) -- node[right, font=\small, pos=0.45]{Sí} (p2b);
\draw[->, thick] (p1b_dec.east) -- node[above, font=\small, midway]{No} (j12b_p1b.west);

\draw[->, thick] (p2b) -- (p3b);
\draw[->, thick] (p3b) -- (p4b);
\draw[->, thick] (p4b) -- (p5b);
\draw[->, thick] (p5b) -- (p6b);

\draw[->, thick] (p6b) -- node[right, font=\small, pos=0.45]{No} (p7b_op);
\draw[->, thick] (p6b.east) -- node[above, font=\small, pos=0.5]{Sí} ++(2.8,0) |- (p6b.north);

\draw[->, thick] (p7b_op) -- (p7b_dec);
\draw[->, thick] (p7b_dec) -- node[right, font=\small, pos=0.45]{No (0)} (p8b9b);
\draw[->, thick] (p7b_dec.west) -- node[above, font=\small, midway]{Sí (1)} ++(-3.6,0) |- (p3b.west);

\draw[->, thick] (p8b9b) -- (p10b);

\draw[->, thick] (p10b) -- node[right, font=\small, pos=0.45]{Sí} (p11b);
\draw[->, thick] (p10b.east) -- node[above, font=\small, midway]{No} ++(5.4,0) |- (p2b.east);

\draw[->, thick] (p11b) -- node[right, font=\small, pos=0.45]{Sí (1)} (p12b);
\draw[->, thick] (p11b.east) -- node[above, font=\small, midway]{No (0)} (j1a_p11b.west);

\draw[->, thick] (p12b) -- (p13b);

\end{tikzpicture}
\end{document}
```

### Código AHPL

Descripción en AHPL de la interfaz, paso a paso.

$\text{MODULE: PRINTER INTERFACE N-PLANAS}$
$\text{MEMORY: } DR[18];\ CR[8];\ BUFFER[1024, 18];\ cnt[10];\ limit[10];$
$\qquad empty[3];\ busy;\ first;\ has\_data;\ end\_print$
$\text{OUTPUTS: } CHAR[8];\ print;\ feed$
$\text{INPUTS: } wait;\ csrdy$
$\text{COMBUS: } IOBUS[18];\ CSBUS[12];\ ready;\ datavalid;\ accept$

$1.\ \rightarrow (\overline{csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}}}) / (1)$
$2.\ accept = 1$
$\qquad \rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 0A, 3)$
$3.\ \rightarrow (\overline{ready}) / (3)$
$4.\ CSBUS_{0} = busy;\ datavalid = 1$
$\qquad \rightarrow (\overline{accept}, accept) / (4, 1)$

$0A.\ busy \leftarrow 1$
$\qquad \rightarrow (1A)$
$1A.\ cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash;\ empty \leftarrow \backslash 0,0,0 \backslash;$
$\qquad limit \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash;\ has\_data \leftarrow 0$
$2A.\ ready = 1$
$\qquad \rightarrow (\overline{datavalid}) / (2A)$
$3A.\ DR \leftarrow IOBUS;\ BUFFER * DCD(cnt) \leftarrow IOBUS;\ accept = 1$
$4A.\ accept = 1$
$\qquad \rightarrow (datavalid) / (4A)$
$5A.\ \rightarrow (\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}, \overline{\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}}) / (6A, 7A)$
$6A.\ has\_data \leftarrow 1;\ limit \leftarrow INC(cnt);\ empty \leftarrow \backslash 0,0,0 \backslash$
$\qquad \rightarrow (8A)$
$7A.\ empty \leftarrow INC(empty)$
$\qquad \rightarrow (8A)$
$8A.\ cnt \leftarrow INC(cnt)$
$\qquad \rightarrow (empty_{0} \lor \bigwedge / cnt, \overline{empty_{0} \lor \bigwedge / cnt}) / (1B, 2A)$

$1B.\ cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash$
$\qquad \rightarrow (\overline{has\_data}, has\_data) / (12B, 2B)$
$2B.\ DR \leftarrow BUSFN(BUFFER; DCD(cnt));\ first \leftarrow 1$
$3B.\ CR \leftarrow (DR_{10:17} ! DR_{1:8}) * (first, \overline{first})$
$4B.\ feed = RETURN(CR);\ print = \overline{RETURN(CR)}$
$5B.\ Null$
$6B.\ \rightarrow (wait) / (6B)$
$7B.\ first \leftarrow 0$
$\qquad \rightarrow (first, \overline{first}) / (3B, 8B)$
$8B.\ cnt \leftarrow INC(cnt)$
$9B.\ end\_print \leftarrow \bigwedge / \overline{cnt \oplus limit}$
$10B.\ \rightarrow (end\_print, \overline{end\_print}) / (11B, 2B)$
$11B.\ \rightarrow (empty_{0}, \overline{empty_{0}}) / (12B, 1A)$
$12B.\ busy \leftarrow 0$
$13B.\ DEAD\ END$
$\text{END SEQUENCE}$
$CHAR = CR$
$\text{END}$

### Descripción de los pasos

Qué hace cada paso del código y a dónde salta.

- `1.` Espera activa de selección. Permanece en `1.` mientras no se direccione la impresora (`010`) con $csrdy = 1$.
- `2.` Confirma recepción del comando. Bifurca a `3.` si es consulta de estatus ($CSBUS_{3} = 1$) o a `1.` y `0A.` si es orden de salida de datos ($CSBUS_{3} = 0$).
- `3.` Espera activa de disponibilidad de la línea de control $ready$.
- `4.` Coloca el flag $busy$ en $CSBUS_{0}$ y activa $datavalid = 1$. Retorna a `1.` tras recibir $accept = 1$.
- `0A.` Inicialización única del trabajo de impresión. Activa el flag $busy \leftarrow 1$ antes de iniciar el lazo de recepción de planas.
- `1A.` Inicio de una plana. Reinicia punteros, contadores de vacías y el indicador de texto útil. Mantiene $busy = 1$.
- `2A.` Asigna $ready = 1$ para indicar disponibilidad para recibir una palabra desde la CPU. Espera activa en `2A.` mientras $datavalid = 0$.
- `3A.` Captura la palabra de 18 bits en $DR$ y la almacena en la posición $cnt$ de $BUFFER$. Emite el pulso $accept = 1$.
- `4A.` Mantiene $accept = 1$ y realiza espera activa hasta que $datavalid$ baje a 0 antes de proceder con la evaluación y solicitar la siguiente palabra.
- `5A.` Evalúa si la palabra contiene caracteres ASCII no nulos. Bifurca a `6A` si contiene texto útil o a `7A` si ambos caracteres son nulos (`00`).
- `6A.` Registra la presencia de texto útil en la plana, guarda la dirección límite siguiente $INC(cnt)$ en $limit$ y reinicia el contador de palabras vacías.
- `7A.` Incrementa en 1 el contador de palabras vacías consecutivas en la plana.
- `8A.` Incrementa el puntero $cnt$. Pasa a la impresión de la plana (`1B`) si se acumularon 4 palabras vacías ($empty_{0} = 1$) o si se enviaron las 1024 palabras ($\bigwedge / cnt = 1$ en el valor previo); si no, retorna a `2A.`.
- `1B.` Reinicia $cnt$ a cero. Si no llegó texto útil en la plana ($has\_data = 0$), salta directamente a terminar todo el trabajo (`12B`); si llegó texto, inicia la impresión de la plana (`2B`).
- `2B.` Lee la palabra de `BUFFER` direccionada por $cnt$ mediante la función combinacional de bus hacia $DR$ e inicializa $first \leftarrow 1$.
- `3B.` Desempaqueta el carácter ASCII de 8 bits. Extrae $DR_{10:17}$ si $first = 1$ o $DR_{1:8}$ si $first = 0$.
- `4B.` Genera los impulsos hacia la impresora: activa $feed$ si $CR$ es retorno de carro o $print$ si es carácter imprimible.
- `5B.` Paso nulo de sincronización para dar tiempo a la impresora física a levantar la señal $wait$.
- `6B.` Espera activa mientras la impresora física reporte estado ocupado ($wait = 1$).
- `7B.` Limpia $first$. Si imprimió el primer carácter ($first = 1$), vuelve a `3B.` para el segundo. Si imprimió el segundo ($first = 0$), avanza a `8B.`.
- `8B.` Incrementa el puntero de palabra $cnt$.
- `9B.` Evalúa la igualdad bit a bit entre el nuevo valor de $cnt$ y $limit$ con lógica combinacional XNOR ($\overline{cnt \oplus limit}$) y reducción AND ($\bigwedge /$), almacenando el resultado en $end\_print$.
- `10B.` Bifurca a `11B` si concluyó la impresión del texto de la plana actual; de lo contrario, retorna a `2B` para leer la siguiente palabra.
- `11B.` Evalúa la causa de fin de la plana: si fue cortada por 4 vacías ($empty_{0} = 1$), avanza a finalizar todo el trabajo (`12B`); si fue plana llena ($empty_{0} = 0$), retorna a `1A` para recibir la siguiente plana sin apagar `busy`.
- `12B.` Apaga el flag de estado $busy \leftarrow 0$ indicando la conclusión de todo el trabajo de impresión.
- `13B.` Conclusión de la secuencia del módulo.
