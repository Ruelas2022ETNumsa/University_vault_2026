## Ejemplo Simple de AHPL

### 1. Definición formal
Un diseño en **AHPL** (*A Hardware Programming Language*) se divide conceptualmente en dos partes: la **sección de datos** (registros, buses de comunicación y lógica de transferencias) y la **sección de control** (el circuito secuencial de control que genera las señales habilitadoras de reloj). Cada paso numerado dentro de la secuencia de control representa la actividad que ocurre durante exactamente un ciclo del reloj maestro síncrono del sistema.

---

### 2. Idea clave
El lenguaje utiliza el operador flecha \(\leftarrow\) para especificar **transferencias síncronas** entre registros (las cuales se efectúan en el flanco activo del reloj). En contraste, utiliza el signo de igualdad \(=\) para **conexiones combinacionales** directas a buses o líneas de salida, las cuales son inmediatas y no dependen de un pulso de reloj.

---

### 3. Caja negra del módulo

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}
\begin{document}
\begin{tikzpicture}[
    box/.style={draw=teal, fill=teal!5, minimum width=3.5cm, minimum height=4cm, align=center, thick, rounded corners=2pt},
    arrow/.style={-{Stealth}, thick},
    bus/.style={arrow, double, draw=violet, thick}
]
    % Module block
    \node[box] (mod) {SHIFT\_ROTATOR \\ (Módulo AHPL)};
    
    % Inputs (west)
    \draw[bus] ([xshift=-1.5cm, yshift=1cm]mod.west) -- node[above, midway, black] {\small $X$} ([yshift=1cm]mod.west);
    \draw[arrow, orange] ([xshift=-1.5cm, yshift=0.3cm]mod.west) -- node[above, midway, black] {\small $a$} ([yshift=0.3cm]mod.west);
    \draw[arrow, orange] ([xshift=-1.5cm, yshift=-0.3cm]mod.west) -- node[above, midway, black] {\small $b$} ([yshift=-0.3cm]mod.west);
    \draw[arrow, gray] ([xshift=-1.5cm, yshift=-1cm]mod.west) -- node[above, midway, black] {\small $clock$} ([yshift=-1cm]mod.west);
    
    % Outputs (east)
    \draw[bus] ([yshift=0.6cm]mod.east) -- +(1.5,0) node[right, black] {\small $Z$};
    \draw[arrow, orange] ([yshift=-0.6cm]mod.east) -- +(1.5,0) node[right, black] {\small $ready$};
    
    % Internal Registers (visual block inside)
    \node[draw=teal, fill=white, minimum width=2cm, minimum height=0.6cm, font=\small] at (mod.center) {$R$};
\end{tikzpicture}
\end{document}
```
*Fig. 4-15 · Caja negra del módulo rotador de registros de 3 bits.*
[[825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf#page=99]]
justificación: Representa la interfaz de hardware del sistema mostrando sus líneas de datos y de control síncronas.

---

### 4. Módulo AHPL completo — SHIFT_ROTATOR
Este sistema recibe un vector de datos de entrada \( X \) de 3 bits, lo almacena en el registro interno \( R \) y, condicionado por las señales de control \( a \) y \( b \), realiza una rotación circular a la derecha de cero, uno o dos lugares antes de entregar el resultado en el bus de salida \( Z \) activando la señal \( ready \).

```ahpl
MODULE: SHIFT_ROTATOR
MEMORY: R
INPUTS: X; a; b
OUTPUTS: Z; ready

1. R <- X
   -> (a & b, a, ~a & b) / (1, 2, 4)
2. R <- R, R[0:1]
   -> (b) / (4)
3. R <- R, R[0:1]
4. ready = 1
   Z = R
   -> (1)
END
```
[[825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf#page=99]]

*   **Paso 1**: Se realiza la carga en paralelo de datos \( R \leftarrow X \) en el flanco activo del reloj. Simultáneamente, se computa la bifurcación de control de tres vías en la que si \( a \land b = 1 \), el control permanece en el paso 1; si \( a = 1 \) pero \( b = 0 \), se salta al paso 2; y si \( \overline{a} \land b = 1 \), se salta directamente al paso 4 para no rotar.
*   **Paso 2**: Realiza la primera rotación circular a la derecha concatenando el último bit con los dos primeros (\( R \leftarrow R_2, R_{0:1} \)). Si \( b = 1 \), avanza al paso 3; si \( b = 0 \), salta al paso 4.
*   **Paso 3**: Efectúa la segunda rotación circular a la derecha de igual manera. El control pasa incondicionalmente al paso 4.
*   **Paso 4**: Es un paso puramente de conexión combinacional. El bus de salida \( Z \) se conecta al registro \( Z = R \) y se emite la señal de estado \( ready = 1 \) para indicar la finalización. El control retorna incondicionalmente al paso 1 para esperar un nuevo vector.

---

### 5. Ejercicio resuelto

##### Ej. Simulación del flujo de registros del módulo SHIFT_ROTATOR con entrada \( X = (1, 0, 1) \), señales de control \( a = 1 \), \( b = 0 \).

**Resolución**
El control iniciará en el paso 1 cargando \( X \), y debido a que \( a = 1 \) y \( b = 0 \), la bifurcación condicional dirigirá el flujo hacia el paso 2 para realizar una sola rotación a la derecha antes de emitir el resultado en el paso 4.

| Paso | Operación | Registros afectados | Resultado |
|---|---|---|---|
| **1** | \( R \leftarrow X \) | \( R \) | \( R = (1, 0, 1) \) |
| **2** | \( R \leftarrow R_2, R_{0:1} \) | \( R \) | \( R = (1, 1, 0) \) |
| **4** | \( ready = 1 \); \( Z = R \) | \( Z \), \( ready \) | \( Z = (1, 1, 0) \), \( ready = 1 \) |

---
