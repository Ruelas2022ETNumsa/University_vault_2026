## Patrón AHPL de Bucle de Espera

1. **Definición formal** — Un bucle de espera (o *polling*) en AHPL mantiene al circuito de control en un paso determinado evaluando una señal de retroalimentación de manera cíclica. El paso de control bifurca hacia sí mismo mientras la condición de vuelta sea verdadera, y progresa al paso secuencial siguiente únicamente cuando la condición evaluada se vuelve falsa.

2. **Idea clave** — La expresión lógica dentro de una bifurcación condicional \( \rightarrow (cond)/(N) \) representa siempre la **condición de retorno**; el módulo continuará en ciclo mientras esta se evalúe como verdadera.

3. **Figura o diagrama**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[>=Stealth, node distance=2.5cm, font=\sffamily]
  % Estilos de nodos
  \tikzset{
    decision/.style={draw, diamond, aspect=2, fill=teal!10, minimum width=2.5cm, minimum height=1cm, align=center},
    block/.style={draw, rectangle, fill=orange!10, minimum width=2cm, minimum height=0.8cm, align=center}
  }
  
  % Nodos
  \node[decision] (cond) {ready = 0?};
  \node[block, below of=cond] (next) {Paso 2};
  
  % Flechas
  \draw[->, thick] (cond) -- node[right] {No (ready = 1)} (next);
  \draw[->, thick] (cond.west) -- ++(-1.2,0) node[above, near end] {Sí} |- (cond.north);
\end{tikzpicture}
\end{document}
```
*Fig. 1. Flujo de control de un bucle de espera en AHPL para la variante 1 (espera activa mientras `ready = 0`).*

### Código unificado en AHPL

A continuación se muestra la secuencia de control que contiene ambas variantes estructuradas dentro del mismo bloque de código:

```
MODULE: CONTROL_ESPERAS
INPUTS: ready; wait
SEQUENCE:
1. -> (~ready)/(1)
2. -> (wait)/(2)
3. DEAD END
END SEQUENCE
END
```

---

### Análisis detallado de las variantes

#### Variante 1: El módulo espera mientras `ready = 0` y sale cuando `ready = 1`

*   **Paso numerado exacto:**
    ```
    1. -> (~ready)/(1)
    ```
*   **Condición de retorno:** **\( \overline{ready} = 1 \)** (es decir, la señal `ready` es lógica `0`). Mientras esta condición se cumpla, el control vuelve permanentemente al paso `1.` retrasando el flujo en cada ciclo de reloj.
*   **Condición de salida:** **\( ready = 1 \)** (es decir, la condición de retorno \( \overline{ready} \) se vuelve falsa / lógica `0`). Al no cumplirse la bifurcación condicional, el control avanza inmediatamente al paso `2.`.

#### Variante 2: El módulo espera mientras `wait = 1` y sale cuando `wait = 0`

*   **Paso numerado exacto:**
    ```
    2. -> (wait)/(2)
    ```
*   **Condición de retorno:** **\( wait = 1 \)** (es decir, la señal `wait` se encuentra activa en nivel alto). El control se retroalimenta al mismo paso `2.`, deteniendo el avance de la secuencia.
*   **Condición de salida:** **\( wait = 0 \)** (es decir, la condición de retorno se evalúa como falsa). Una vez que el dispositivo periférico desactiva la señal `wait`, el secuenciador de control sale del bucle de espera y continúa al paso `3.` (`DEAD END`).

