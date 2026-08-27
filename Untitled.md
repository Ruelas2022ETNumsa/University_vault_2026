```tikz
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=0.95]

% ---- MÓDULO INTERFACE (caja principal) ----
\draw[draw=teal, thick] (3,0) rectangle (8,7);
\node[font=\bfseries\small, teal] at (5.5,7.3) {INTERFACE};

% ---- REGISTROS INTERNOS ----
% DR(18)
\draw[draw=gray, thick] (3.4,5.6) rectangle (6.2,6.4);
\node[font=\small] at (4.8,6.0) {DR(18)};
% Triángulo (flip-flop D indicator)
\draw[gray] (3.4,5.85) -- (3.7,6.0) -- (3.4,6.15);

% CR(8)
\draw[draw=gray, thick] (3.4,3.8) rectangle (6.2,4.6);
\node[font=\small] at (4.8,4.2) {CR(8)};

% busy
\draw[draw=gray, thick] (3.4,2.4) rectangle (6.2,3.2);
\node[font=\small] at (4.8,2.8) {\textit{busy}};

% first
\draw[draw=gray, thick] (3.4,1.0) rectangle (6.2,1.8);
\node[font=\small] at (4.8,1.4) {\textit{first}};

% ---- BUS IOBUS (línea vertical) ----
\draw[very thick, black] (1.5,-0.5) -- (1.5,7.5);
\node[font=\small, below] at (1.5,-0.6) {IOBUS};

% ---- BUS CSBUS (línea vertical, más a la izquierda) ----
\draw[very thick, black] (0.2,-0.5) -- (0.2,7.5);
\node[font=\small, below] at (0.2,-0.6) {CSBUS};

% ---- LÍNEAS INDIVIDUALES HORIZONTALES (de izquierda hasta módulo) ----

% accept (entra al módulo hacia DR area) — flecha hacia la derecha
\draw[->, thick] (-1.2,6.0) -- (3.0,6.0);
\node[left, font=\small] at (-1.2,6.0) {\textit{accept}};

% datavalid (sale del módulo hacia la izquierda)
\draw[<-, thick] (-1.2,5.2) -- (3.0,5.2);
\node[left, font=\small] at (-1.2,5.2) {\textit{datavalid}};

% ready (sale del módulo hacia la izquierda)
\draw[<-, thick] (-1.2,4.4) -- (3.0,4.4);
\node[left, font=\small] at (-1.2,4.4) {\textit{ready}};

% csrdy (entra al módulo — desde abajo del CSBUS, línea vertical luego horizontal)
\draw[->, thick] (2.0,-1.2) -- (2.0,1.4) -- (3.0,1.4);
\node[below, font=\small] at (2.0,-1.2) {\textit{csrdy}};

% ---- SEÑALES SALIENTES (derecha del módulo → impresora) ----
% print
\draw[->, thick] (8,6.2) -- (9.5,6.2);
\node[right, font=\small] at (9.5,6.2) {\textit{print}};

% feed
\draw[->, thick] (8,5.5) -- (9.5,5.5);
\node[right, font=\small] at (9.5,5.5) {\textit{feed}};

% CHAR (desde CR — flecha gruesa)
\draw[->, very thick] (6.2,4.2) -- (9.5,4.2);
\node[right, font=\small] at (9.5,4.2) {\textit{CHAR}};

% ---- SEÑAL ENTRANTE (impresora → módulo) ----
% wait
\draw[->, thick] (9.5,2.8) -- (8,2.8);
\node[right, font=\small] at (9.5,2.8) {\textit{wait}};

% ---- ETIQUETA IMPRESORA ----
\draw[thick] (9.5,5.85) -- (10.5,6.4);
\draw[thick] (9.5,5.85) -- (10.5,5.3);
\node[font=\small\itshape] at (11.5,6.5) {IMPRESORA Dispositivo \#010};

% ---- CONEXIONES BIDIRECCIONALES IOBUS ↔ MÓDULO ----
% Las líneas horizontales individuales ya cubren accept/datavalid/ready
% Conexión IOBUS ↔ DR (bidireccional, doble flecha)
\draw[{Latex[length=3mm]}-{Latex[length=3mm]}, thick]
    (1.5,6.0) -- (3.4,6.0);
\draw[{Latex[length=3mm]}-{Latex[length=3mm]}, thick]
    (1.5,5.2) -- (3.4,5.2);
\draw[{Latex[length=3mm]}-{Latex[length=3mm]}, thick]
    (1.5,4.4) -- (3.4,4.4);

\end{tikzpicture}
\end{document}
```