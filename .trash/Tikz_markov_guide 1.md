# Guía para dibujar Cadenas de Markov en TikZ

Esta guía explica el **patrón** detrás de los ejemplos de este archivo, para que un modelo (NotebookLM u otro) pueda generar diagramas nuevos con cualquier número de estados y cualquier matriz de transición, no solo copiar los ejemplos existentes.

## 1. Estructura base de todo diagrama

Todo diagrama sigue el mismo esqueleto:

```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA (opcional, solo de referencia/depuración)
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};
\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=COLOR1] (A) at (X1,Y1) {$A$};
% ... un \node por cada estado ...
% =====================================================
% TRANSICIONES (un bloque de comentario por estado)
% =====================================================
% Bucle (self-loop) primero, luego una flecha hacia cada otro estado
\draw[->,ultra thick,COLOR1] (A) .. controls (cx1,cy1) and (cx2,cy2) ..node[pos] {$p_{AA}$}(A);
\draw[->,very thick,COLOR1]  (A) to[bend left=N] node[pos=0.2] {$p_{AB}$} (B);
\end{tikzpicture}
\end{document}
```

La grilla con números rojos es solo una ayuda visual para ubicar coordenadas a mano; **puede omitirse** en el diagrama final si se quiere un resultado más limpio.

## 1.1 Reglas de formato obligatorias

- **El bloque de código siempre debe ir envuelto exactamente así, sin excepción:**

```tikz
\begin{document}

\end{document}
```

  Es decir: todo el contenido (grilla, nodos, flechas, `tikzpicture`) va dentro de un único code fence etiquetado `tikz` cuyo contenido empieza con `\begin{document}` y termina con `\end{document}`. Nunca se debe entregar solo el `tikzpicture` suelto, sin este envoltorio.
- **Nunca usar `fill=` en los nodos.** Los nodos se dibujan solo con `draw,circle,thick,color=...` — el color pinta el borde y la letra del estado, no el interior del círculo. Si el nodo se rellena de color, la letra queda difícil de leer sobre el fondo, así que el relleno (`fill`) queda prohibido en estos diagramas.

## 2. Cómo ubicar los N estados (posicionamiento)

Los estados se reparten en un **círculo imaginario centrado en (6,6)** (el centro de la grilla de 12×12), en sentido horario empezando arriba.

Fórmula angular para el estado número `i` (con `i = 0, 1, 2, ... N-1`):

```
ángulo_i = 90° - i × (360° / N)
x_i = 6 + R × cos(ángulo_i)
y_i = 6 + R × sin(ángulo_i)
```

Redondea `x_i`, `y_i` al entero más cercano para que las coordenadas calcen con la grilla.

Radio `R` sugerido según N (para que ningún nodo quede pegado al borde 0 o 12):

| N estados | R sugerido | Caso especial                                                                                        |
| --------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| 2         | —          | No usar círculo: colocar en línea horizontal, p. ej. (2,6) y (10,6)                                  |
| 3         | 4.5        |                                                                                                      |
| 4         | 4          | Da un cuadrado perfecto: arriba, derecha, abajo, izquierda                                           |
| 5–6       | 5          |                                                                                                      |
| 7 u más   | 5.5        | Si los nodos quedan muy juntos, ampliar la grilla a 14×14 o 16×16 manteniendo el centro proporcional |

Ejemplo: para N=4, ángulos = 90°, 0°, -90°, -180° → posiciones (6,10), (10,6), (6,2), (2,6). Esto coincide exactamente con el ejemplo de 4 estados más abajo.

## 3. Cómo dibujar el bucle (self-loop) de cada estado

El bucle representa la probabilidad de quedarse en el mismo estado ($p_{ii}$). Debe sobresalir **hacia afuera del círculo** (lejos del centro), nunca hacia adentro, para no cruzar las flechas hacia otros estados.

Regla práctica: usa la dirección cardinal (arriba/abajo/izquierda/derecha) más cercana a la posición del nodo respecto al centro:

- Nodo en la mitad superior → bucle hacia **arriba**: `.. controls (x-1,y+1) and (x+1,y+1) ..` con etiqueta `node[above]`
- Nodo en la mitad derecha → bucle hacia **la derecha**: `.. controls (x+1,y+1) and (x+1,y-1) ..` con etiqueta `node[right]`
- Nodo en la mitad inferior → bucle hacia **abajo**: `.. controls (x+1,y-1) and (x-1,y-1) ..` con etiqueta `node[below]`
- Nodo en la mitad izquierda → bucle hacia **la izquierda**: `.. controls (x-1,y-1) and (x-1,y+1) ..` con etiqueta `node[left]`

Es una heurística, no una fórmula exacta: si dos bucles quedan demasiado cerca o se cruzan con una flecha, ajusta la dirección o el desplazamiento (±1, ±1.5) a ojo.

## 4. Cómo dibujar las flechas entre estados distintos

Cada flecha de un estado a otro se dibuja con una curva (`bend left=N`) para poder distinguir visualmente la flecha de ida de la flecha de vuelta entre el mismo par de nodos (A→B y B→A no deben superponerse).

- Color de la flecha = color del nodo de **origen**.
- Grosor: `very thick` para flechas entre estados, `ultra thick` para el bucle (así el bucle resalta).
- Ángulo de curvatura (`bend left=N`) sugerido por estado en orden alfabético: A=10, B=20, C=30, D=40, E=50... (súmale 10 por cada letra). Si con muchos estados (N>6) las curvas se ven demasiado pronunciadas o se cruzan, reduce la progresión (por ejemplo, +5 en vez de +10).
- Posición de la etiqueta sobre la curva (`pos=...`): repártelas entre 0.2 y 0.4 para que las etiquetas de varias flechas saliendo del mismo nodo no se amontonen en un punto.
- Dibuja una flecha por cada transición con probabilidad mayor a 0 (si $p_{ij}=0$, simplemente no se traza esa flecha, para no saturar el dibujo).

## 5. Reglas sobre las probabilidades

- Las probabilidades que salen de un mismo estado (incluyendo el bucle) **deben sumar 1**: $p_{ii} + \sum_{j \neq i} p_{ij} = 1$.
- Usa siempre el valor numérico real (p. ej. `$0.35$`), nunca un placeholder como `$0.X$` — los ejemplos más abajo tienen ese placeholder de muestra y hay que reemplazarlo por un número real al generar un diagrama nuevo.
- Si el usuario da una matriz de transición, cada fila de la matriz corresponde a las flechas que salen de un estado.

## 6. Paleta de colores

Usa un color distinto por estado, cíclicamente, en este orden (evita `red` porque ya se usa para los números de la grilla, y `gray` porque es el color de la grilla):

```
orange, pink, lime, purple, teal, magenta, cyan, brown, olive, violet, blue, black
```

Si N > 12, repite la paleta o defina colores personalizados con `\definecolor`.

## 7. Plantilla genérica reutilizable

Para generar un diagrama nuevo, sigue este algoritmo:

1. Pide o define: número de estados N, sus nombres, y la matriz/lista de transiciones $p_{ij}$.
2. Calcula las posiciones $(x_i, y_i)$ con la fórmula angular de la sección 2.
3. Asigna un color de la paleta a cada estado en orden.
4. Para cada estado, en un bloque comentado `% ESTADO_i`:
   - Dibuja el `\node` circular en su posición y color.
5. Para cada estado, en otro bloque:
   - Dibuja primero el bucle con $p_{ii}$ (sección 3).
   - Dibuja una flecha hacia cada otro estado con $p_{ij} > 0$ (sección 4).
6. Verifica que cada fila de probabilidades suma 1 y que no quedan placeholders.
7. Envuelve todo en `\begin{tikzpicture}...\end{tikzpicture}` dentro de `\begin{document}...\end{document}` (o solo el `tikzpicture` si se va a insertar dentro de un documento LaTeX más grande).

## 8. Prompt sugerido para pedirle esto a NotebookLM

> "Genera un diagrama de cadena de Markov en TikZ con N estados llamados [...], usando el patrón de posicionamiento circular (centro 6,6, ángulo = 90° − i·360°/N), un self-loop por estado con su probabilidad de quedarse, y una flecha curva (`bend left`) hacia cada estado con probabilidad de transición > 0. La matriz de transición es: [...]. Verifica que cada fila sume 1 antes de entregar el código."

## 9. Checklist final antes de compilar

- [ ] Cada estado tiene un `\node` con color único.
- [ ] Cada estado tiene exactamente un bucle (self-loop).
- [ ] Solo hay flechas para probabilidades > 0.
- [ ] Ninguna etiqueta es un placeholder (`0.X`, `p`, etc.).
- [ ] Las probabilidades de cada estado suman 1.
- [ ] Las flechas A→B y B→A (si existen ambas) están curvadas en direcciones que no se superponen.
- [ ] Compilado de prueba en Overleaf o quicklatex.com antes de usarlo en el documento final.

---

## 10. Ejemplos de referencia (2 a 6 estados)

Los siguientes bloques son los ejemplos originales que ilustran el patrón descrito arriba. **Nota:** usan probabilidades de muestra que no necesariamente suman 1, y el ejemplo contiene un placeholder `$0.X$` sin reemplazar — son solo referencia visual del patrón, no copiar los números literalmente.

```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (2,6) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,6) {$B$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (1,7) and (3,7) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.5,above] {$0.4$} (B);

% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (9,7) and (11,7) ..node[above] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.5,below] {$0.4$} (A);

\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,10) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,4) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (2,4) {$C$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,11) and (7,11) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,5) and (11,3) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (1,3) and (1,5) ..node[left] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,10) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,6) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (6,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (2,6) {$D$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,11) and (7,11) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);

% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,7) and (11,5) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (7,1) and (5,1) ..node[below] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (1,5) and (1,7) ..node[left] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,11) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,7) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (9,2) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (3,2) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (2,7) {$E$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,12) and (7,12) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.3,right] {$0.2$} (E);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,8) and (11,6) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.3,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (10,3) and (10,1) ..node[right] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);

% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (4,1) and (2,1) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=40] node[pos=0.3,right] {$0.4$} (E);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (1,6) and (1,8) ..node[left] {$0.8$}(E);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,teal] (E) to[bend left=50] node[pos=0.3,right] {$0.4$} (D);

\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
% =====================================================
% GRILLA
% =====================================================
\draw[gray!100] (0,0) grid (12,12);
\foreach \x in {1,2,...,12}
    \node[below,red] at (\x,0) {\x};

\foreach \y in {1,2,...,12}
    \node[left,red] at (0,\y) {\y};
% =====================================================
% ESTADOS
% =====================================================
\node[draw,circle,thick,color=orange]  (A) at (6,11) {$A$};
\node[draw,circle,thick,color=pink]    (B) at (10,8) {$B$};
\node[draw,circle,thick,color=lime]    (C) at (10,4) {$C$};
\node[draw,circle,thick,color=purple]  (D) at (6,1) {$D$};
\node[draw,circle,thick,color=teal]    (E) at (2,4) {$E$};
\node[draw,circle,thick,color=magenta]    (F) at (2,8) {$F$};
% =====================================================
% A
% =====================================================
\draw[->,ultra thick,orange] (A) .. controls (5,12) and (7,12) ..node[above] {$0.4$}(A);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.X$} (C);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (D);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.2,right] {$0.2$} (E);
\draw[->,very thick,orange]  (A) to[bend left=10] node[pos=0.4,right] {$0.2$} (F);
% =====================================================
% B
% =====================================================
\draw[->,ultra thick,pink] (B) .. controls (11,9) and (11,7) ..node[right] {$0.4$}(B);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.2,right] {$0.4$} (F);
\draw[->,very thick,pink] (B) to[bend left=20] node[pos=0.4,right] {$0.4$} (A);
% =====================================================
% C
% =====================================================
\draw[->,ultra thick,lime] (C) .. controls (11,5) and (11,3) ..node[right] {$0.2$}(C);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (F);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,lime] (C) to[bend left=30] node[pos=0.3,right] {$0.4$} (B);
% =====================================================
% D
% =====================================================
\draw[->,ultra thick,purple] (D) .. controls (7,0) and (5,0) ..node[below] {$0.7$}(D);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.2,right] {$0.4$} (E);
\draw[->,very thick,purple] (D) to[bend left=30] node[pos=0.3,right] {$0.4$} (F);
% =====================================================
% E
% =====================================================
\draw[->,ultra thick,teal] (E) .. controls (1,3) and (1,5) ..node[left] {$0.8$}(E);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,teal] (E) to[bend left=20] node[pos=0.3,right] {$0.4$} (F);
% =====================================================
% F
% =====================================================
\draw[->,ultra thick,magenta] (F) .. controls (1,7) and (1,9) ..node[left] {$0.8$}(F);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (A);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (B);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (C);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.2,right] {$0.4$} (D);
\draw[->,very thick,magenta] (F) to[bend left=20] node[pos=0.3,right] {$0.4$} (E);

\end{tikzpicture}
\end{document}
```
