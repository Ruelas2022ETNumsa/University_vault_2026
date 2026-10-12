
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.85,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.4cm, minimum height=0.85cm, font=\small, align=center},
    hs_operation/.style={draw=orange, thick, minimum width=3.4cm, minimum height=0.85cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% ===== Columna izquierda =====
\node[jump] (j1) at (0,0) {1};

\node[decision] (p1) at (0,-2.6) {¿Dispositivo impresor\\seleccionado (csrdy)?};
\node[font=\scriptsize, gray, anchor=south east] at (p1.north west) {1};

\node[hs_operation] (p2_op) at (0,-6.0) {Aceptar comando\\(accept = 1)};
\node[font=\scriptsize, gray, anchor=south east] at (p2_op.north west) {2};

\node[decision] (p2_dec) at (0,-9.2) {¿Tipo de comando\\(CSBUS3)?};

\node[jump] (j1_p2)  at (-5.0,-12.4) {1};
\node[jump] (j1a_p2) at (0,-12.4) {1A};
\node[jump] (j3_p2)  at (5.2,-9.2) {3};

% ===== Columna derecha =====
\node[jump] (j3_in) at (10,0) {3};

\node[decision] (p3) at (10,-2.6) {¿Línea control\\ready disponible?};
\node[font=\scriptsize, gray, anchor=south east] at (p3.north west) {3};

\node[hs_operation] (p4_op) at (10,-6.0) {Enviar estatus busy\\(datavalid = 1)};
\node[font=\scriptsize, gray, anchor=south east] at (p4_op.north west) {4};

\node[decision] (p4_dec) at (10,-9.2) {¿CPU confirmó\\recepción (accept)?};

\node[jump] (j1_p4) at (10,-12.4) {1};

% ===== Conexiones izquierda =====
\draw[->, thick] (j1) -- (p1);
\draw[->, thick] (p1) -- node[right, font=\small, pos=0.45]{Sí} (p2_op);
\draw[->, thick] (p1.west) -- node[above, font=\small, midway]{No} ++(-1.6,0) |- (j1.west);

\draw[->, thick] (p2_op) -- (p2_dec);
\draw[->, thick] (p2_dec.east) -- node[above, font=\small, midway]{Estatus (1)} (j3_p2.west);
\draw[->, thick] (p2_dec.south) -- node[right, font=\small, pos=0.45]{Datos (0)} (j1a_p2.north);
\draw[->, thick] (p2_dec.west) -| node[above, font=\small, pos=0.24]{Datos (0)} (j1_p2.north);

% ===== Conexiones derecha =====
\draw[->, thick] (j3_in) -- (p3);
\draw[->, thick] (p3) -- node[right, font=\small, pos=0.45]{Sí} (p4_op);
\draw[->, thick] (p3.east) -- node[above, font=\small, midway]{No} ++(1.6,0) |- (j3_in.east);

\draw[->, thick] (p4_op) -- (p4_dec);
\draw[->, thick] (p4_dec) -- node[right, font=\small, pos=0.45]{Sí} (j1_p4);
\draw[->, thick] (p4_dec.east) -- node[above, font=\small, midway]{No} ++(1.6,0) |- (p4_op.east);

\end{tikzpicture}
\end{document}
```


```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.85,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.4cm, minimum height=0.85cm, font=\small, align=center},
    hs_operation/.style={draw=orange, thick, minimum width=3.4cm, minimum height=0.85cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entrada 1A
\node[jump] (j1a) at (0,0) {1A};

% Paso 1A
\node[operation] (p1a) at (0,-2.0) {Reiniciar cnt, limit, empty\\y banderas; busy = 1};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p1a.west) {1A};

% Paso 2A
\node[hs_operation] (p2a_op) at (0,-4.4) {Indicar listo\\(ready = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p2a_op.west) {2A};

\node[decision] (p2a_dec) at (0,-8.0) {¿Dato válido disponible\\(datavalid = 1)?};

% Paso 3A
\node[operation] (p3a) at (0,-11.8) {Guardar palabra en BUFFER\\y DR; accept = 1};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p3a.west) {3A};

% Paso 4A
\node[hs_operation] (p4a_op) at (0,-14.4) {Sostener confirmación\\(accept = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p4a_op.west) {4A};

\node[decision] (p4a_dec) at (0,-18.0) {¿CPU liberó bus\\(datavalid = 0)?};

% Paso 5A
\node[decision] (p5a) at (0,-22.4) {¿Palabra contiene\\texto no nulo?};
\node[font=\scriptsize, gray, anchor=south east] at (p5a.north west) {5A};

% Paso 6A y 7A
\node[operation] (p6a) at (-3.6,-26.4) {has\_data = 1; limit = cnt + 1\\Reiniciar empty = 0};
\node[font=\scriptsize, gray, anchor=south east] at (p6a.north west) {6A};

\node[operation] (p7a) at (3.6,-26.4) {Incrementar palabras\\vacías (empty + 1)};
\node[font=\scriptsize, gray, anchor=south west] at (p7a.north east) {7A};

% Paso 8A
\node[operation] (p8a_op) at (0,-29.6) {Incrementar puntero\\(cnt = cnt + 1)};
\node[font=\scriptsize, gray, anchor=south east] at (p8a_op.north west) {8A};

\node[decision] (p8a_dec) at (0,-33.4) {¿4 vacías o buffer\\lleno (1024 palabras)?};

% Saltos finales
\node[jump] (j1b) at (-3.4,-37.4) {1B};
\node[jump] (j2a) at (3.4,-37.4) {2A};

% Conexiones
\draw[->, thick] (j1a) -- (p1a);
\draw[->, thick] (p1a) -- (p2a_op);
\draw[->, thick] (p2a_op) -- (p2a_dec);
\draw[->, thick] (p2a_dec) -- node[right, font=\small, pos=0.5]{Sí} (p3a);
\draw[->, thick] (p2a_dec.east) -- node[above, font=\small, midway]{No} ++(2.0,0) |- (p2a_op.east);

\draw[->, thick] (p3a) -- (p4a_op);
\draw[->, thick] (p4a_op) -- (p4a_dec);
\draw[->, thick] (p4a_dec) -- node[right, font=\small, pos=0.5]{Sí} (p5a);
\draw[->, thick] (p4a_dec.east) -- node[above, font=\small, midway]{No} ++(2.0,0) |- (p4a_op.east);

\draw[->, thick] (p5a.south) -- ++(0,-0.8) -| node[above, font=\small, pos=0.2]{Sí} (p6a.north);
\draw[->, thick] (p5a.south) -- ++(0,-0.8) -| node[above, font=\small, pos=0.2]{No} (p7a.north);

\draw[->, thick] (p6a.south) |- (p8a_op.west);
\draw[->, thick] (p7a.south) |- (p8a_op.east);

\draw[->, thick] (p8a_op) -- (p8a_dec);
\draw[->, thick] (p8a_dec.south) -- ++(0,-0.8) -| node[above, font=\small, pos=0.2]{Sí} (j1b.north);
\draw[->, thick] (p8a_dec.south) -- ++(0,-0.8) -| node[above, font=\small, pos=0.2]{No} (j2a.north);

\end{tikzpicture}
\end{document}
```

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\begin{document}
\begin{tikzpicture}[
    scale=0.8,
    decision/.style={diamond, draw=gray, thick, aspect=2.0, inner sep=1pt, font=\small, align=center},
    operation/.style={draw=teal, thick, minimum width=3.4cm, minimum height=0.85cm, font=\small, align=center},
    jump/.style={circle, draw=gray, thick, inner sep=2pt, font=\small}
]

% Entrada 1B
\node[jump] (j1b) at (0,0) {1B};

% Paso 1B
\node[operation] (p1b_op) at (0,-1.6) {Reiniciar puntero\\(cnt = 0)};
\node[font=\scriptsize, gray, anchor=south east] at (p1b_op.north west) {1B};

\node[decision] (p1b_dec) at (0,-4.4) {¿Se recibió texto útil\\(has\_data)?};

% Paso 2B
\node[operation] (p2b) at (0,-7.5) {Leer palabra de BUFFER\\a DR; first = 1};
\node[font=\scriptsize, gray, anchor=south east] at (p2b.north west) {2B};

% Paso 3B
\node[operation] (p3b) at (0,-9.7) {Extraer carácter ASCII\\de DR a CR};
\node[font=\scriptsize, gray, anchor=south east] at (p3b.north west) {3B};

% Paso 4B
\node[operation] (p4b) at (0,-11.9) {Enviar impulso\\print o feed (RETURN)};
\node[font=\scriptsize, gray, anchor=south east] at (p4b.north west) {4B};

% Paso 5B
\node[operation] (p5b) at (0,-14.1) {Sincronización\\(paso Null)};
\node[font=\scriptsize, gray, anchor=south east] at (p5b.north west) {5B};

% Paso 6B
\node[decision] (p6b) at (0,-17.5) {¿Impresora ocupada\\(wait = 1)?};
\node[font=\scriptsize, gray, anchor=south east] at ([xshift=-0.3cm]p6b.north west) {6B};

% Paso 7B
\node[operation] (p7b_op) at (0,-20.6) {Seleccionar segundo\\carácter (first = 0)};
\node[font=\scriptsize, gray, anchor=south east] at (p7b_op.north west) {7B};

\node[decision] (p7b_dec) at (0,-23.7) {¿Era 1er carácter?\\(valor previo de first)};

% Pasos 8B-9B y 10B
\node[operation] (p8b9b) at (0,-26.8) {Incrementar cnt y evaluar\\igualdad con limit};
\node[font=\scriptsize, gray, anchor=south east] at (p8b9b.north west) {8B-9B};

\node[decision] (p10b) at (0,-29.7) {¿Llegó al límite\\de texto (limit)?};
\node[font=\scriptsize, gray, anchor=south east] at ([xshift=-0.3cm]p10b.north west) {10B};

% Pasos 11B y 12B
\node[operation] (p11b) at (0,-32.6) {Liberar interfaz\\(busy = 0)};
\node[font=\scriptsize, gray, anchor=south east] at (p11b.north west) {11B};

\node[operation, draw=orange] (p12b) at (0,-34.6) {Fin de secuencia\\(DEAD END)};
\node[font=\scriptsize, gray, anchor=south east] at (p12b.north west) {12B};

% Conexiones principales
\draw[->, thick] (j1b) -- (p1b_op);
\draw[->, thick] (p1b_op) -- (p1b_dec);
\draw[->, thick] (p1b_dec) -- node[right, font=\small, pos=0.5]{Sí} (p2b);
\draw[->, thick] (p1b_dec.east) -- node[above, font=\small, midway]{No} ++(6.5,0) |- (p11b.east);

\draw[->, thick] (p2b) -- (p3b);
\draw[->, thick] (p3b) -- (p4b);
\draw[->, thick] (p4b) -- (p5b);
\draw[->, thick] (p5b) -- (p6b);

% Espera de impresora (wait)
\draw[->, thick] (p6b) -- node[right, font=\small, pos=0.5]{No} (p7b_op);
\draw[->, thick] (p6b.east) -- node[above, font=\small, midway]{Sí} ++(1.8,0) -- ++(0,1.8) -| (p6b.north);

\draw[->, thick] (p7b_op) -- (p7b_dec);
\draw[->, thick] (p7b_dec) -- node[right, font=\small, pos=0.5]{No (0)} (p8b9b);
\draw[->, thick] (p7b_dec.west) -- node[above, font=\small, midway]{Sí (1)} ++(-3.2,0) |- (p3b.west);

\draw[->, thick] (p8b9b) -- (p10b);

\draw[->, thick] (p10b) -- node[right, font=\small, pos=0.5]{Sí} (p11b);
\draw[->, thick] (p10b.east) -- node[above, font=\small, midway]{No} ++(4.2,0) |- (p2b.east);

\draw[->, thick] (p11b) -- (p12b);

\end{tikzpicture}
\end{document}
```
