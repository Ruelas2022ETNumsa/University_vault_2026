
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
\node[operation] (p0a) at (-3.8,-2.2) {Activar estado ocupado\\(busy = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p0a.west) {0A};

% Paso 1A
\node[operation] (p1a) at (0,-5.2) {Reiniciar cnt, limit, empty\\y banderas (has\_data = 0)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p1a.west) {1A};

% Paso 2A
\node[hs_operation] (p2a_op) at (0,-8.4) {Indicar listo\\(ready = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p2a_op.west) {2A};

\node[decision] (p2a_dec) at (0,-12.2) {¿Dato válido disponible\\(datavalid = 1)?};
\node[font=\scriptsize, gray, anchor=south east] at (p2a_dec.north west) {2A};

% Paso 3A
\node[operation] (p3a) at (0,-16.4) {Guardar palabra en BUFFER\\y DR; accept = 1};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p3a.west) {3A};

% Paso 4A
\node[hs_operation] (p4a_op) at (0,-19.8) {Sostener confirmación\\(accept = 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p4a_op.west) {4A};

\node[decision] (p4a_dec) at (0,-23.6) {¿CPU liberó bus\\(datavalid = 0)?};
\node[font=\scriptsize, gray, anchor=south east] at (p4a_dec.north west) {4A};

% Paso 5A
\node[decision] (p5a) at (0,-28.2) {¿Palabra contiene\\texto no nulo?};
\node[font=\scriptsize, gray, anchor=south east] at (p5a.north west) {5A};

% Paso 6A y 7A
\node[operation] (p6a) at (-4.4,-32.8) {has\_data = 1; limit = cnt + 1\\Reiniciar empty = 0};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p6a.west) {6A};

\node[operation] (p7a) at (4.4,-32.8) {Incrementar palabras\\vacías (empty + 1)};
\node[font=\scriptsize, gray, anchor=west] at ([xshift=0.2cm]p7a.east) {7A};

% Paso 8A
\node[operation] (p8a_op) at (0,-37.2) {Incrementar puntero\\(cnt = cnt + 1)};
\node[font=\scriptsize, gray, anchor=east] at ([xshift=-0.2cm]p8a_op.west) {8A};

\node[decision] (p8a_dec) at (0,-41.2) {¿4 vacías o buffer\\lleno (1024 palabras)?};
\node[font=\scriptsize, gray, anchor=south east] at (p8a_dec.north west) {8A};

% Saltos finales
\node[jump] (j1b) at (-4.6,-45.4) {1B};
\node[jump] (j2a) at (4.6,-45.4) {2A};

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
\node[operation] (p1b_op) at (0,-1.3) {Reiniciar puntero\\(cnt = 0)};
\node[font=\scriptsize, gray, left] at (-2.0,-1.3) {1B};

\node[decision] (p1b_dec) at (0,-2.8) {¿Se recibió texto útil\\(has\_data)?};
\node[font=\scriptsize, gray, left] at (-2.0,-2.8) {1B};

% Paso 2B
\node[operation] (p2b) at (0,-4.6) {Leer palabra de BUFFER\\a DR; first = 1};
\node[font=\scriptsize, gray, left] at (-2.4,-4.6) {2B};

% Paso 3B
\node[operation] (p3b) at (0,-6.1) {Extraer carácter ASCII\\de DR a CR};
\node[font=\scriptsize, gray, left] at (-2.4,-6.1) {3B};

% Paso 4B
\node[operation] (p4b) at (0,-7.6) {Enviar impulso\\print o feed (RETURN)};
\node[font=\scriptsize, gray, left] at (-2.2,-7.6) {4B};

% Paso 5B
\node[operation] (p5b) at (0,-8.9) {Sincronización\\(paso Null)};
\node[font=\scriptsize, gray, left] at (-1.8,-8.9) {5B};

% Paso 6B
\node[decision] (p6b) at (0,-10.3) {¿Impresora ocupada\\(wait = 1)?};
\node[font=\scriptsize, gray, left] at (-1.8,-10.3) {6B};

% Paso 7B
\node[operation] (p7b_op) at (0,-12.0) {Seleccionar segundo\\carácter (first = 0)};
\node[font=\scriptsize, gray, left] at (-1.8,-12.0) {7B};

\node[decision] (p7b_dec) at (0,-13.5) {¿Era 1er carácter?\\(valor previo de first)};
\node[font=\scriptsize, gray, left] at (-1.8,-13.5) {7B};

% Pasos 8B-10B
\node[operation] (p8b9b) at (0,-15.2) {Incrementar cnt y evaluar\\igualdad con limit};
\node[font=\scriptsize, gray, left] at (-2.2,-15.2) {8B-9B};

\node[decision] (p10b) at (0,-16.8) {¿Llegó al límite\\de texto (limit)?};
\node[font=\scriptsize, gray, left] at (-1.8,-16.8) {10B};

% Paso 11B
\node[decision] (p11b) at (0,-18.6) {¿Cortada por 4 vacías?\\(empty0)?};
\node[font=\scriptsize, gray, left] at (-1.8,-18.6) {11B};

% Pasos 12B y 13B
\node[operation] (p12b) at (0,-20.5) {Liberar interfaz\\(busy = 0)};
\node[font=\scriptsize, gray, left] at (-1.8,-20.5) {12B};

\node[operation, draw=orange] (p13b) at (0,-21.8) {Fin de secuencia\\(DEAD END)};
\node[font=\scriptsize, gray, left] at (-1.8,-21.8) {13B};

% Jump 12B si no hay datos en 1B
\node[jump] (j12b_p1b) at (3.2,-2.8) {12B};

% Jump 1A si empty0 = 0 en 11B
\node[jump] (j1a_p11b) at (3.2,-18.6) {1A};

% Conexiones
\draw[->, thick] (j1b) -- (p1b_op);
\draw[->, thick] (p1b_op) -- (p1b_dec);
\draw[->, thick] (p1b_dec) -- node[right, font=\small]{Sí} (p2b);
\draw[->, thick] (p1b_dec) -- node[above, font=\small]{No} (j12b_p1b);

\draw[->, thick] (p2b) -- (p3b);
\draw[->, thick] (p3b) -- (p4b);
\draw[->, thick] (p4b) -- (p5b);
\draw[->, thick] (p5b) -- (p6b);

\draw[->, thick] (p6b) -- node[right, font=\small]{No} (p7b_op);
\draw[thick, ->] (p6b.east) -- ++(1.5,0) node[above, font=\small]{Sí} -- ++(0,1.2) -- (p6b.east);

\draw[->, thick] (p7b_op) -- (p7b_dec);
\draw[->, thick] (p7b_dec) -- node[right, font=\small]{No (0)} (p8b9b);
\draw[thick, ->] (p7b_dec.west) -- ++(-2.8,0) node[above, font=\small]{Sí (1)} |- (p3b.west);

\draw[->, thick] (p8b9b) -- (p10b);

\draw[->, thick] (p10b) -- node[right, font=\small]{Sí} (p11b);
\draw[thick, ->] (p10b.east) -- ++(2.8,0) node[above, font=\small]{No} |- (p2b.east);

\draw[->, thick] (p11b) -- node[right, font=\small]{Sí (1)} (p12b);
\draw[->, thick] (p11b) -- node[above, font=\small]{No (0)} (j1a_p11b);

\draw[->, thick] (p12b) -- (p13b);

\end{tikzpicture}
\end{document}
```