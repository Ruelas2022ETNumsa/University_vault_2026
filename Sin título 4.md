## Robo de Ciclo (Cycle Stealing)

1. **Definición formal** — Es una técnica de acceso directo a memoria $DMA$ en la que el módulo de DMA fuerza al procesador a suspender su operación temporalmente para tomar el control del bus del sistema y transferir una sola palabra de datos [1], [2]. Se denomina "robo" porque el controlador de DMA utiliza un ciclo de bus que, de otro modo, habría sido utilizado por la CPU, reintegrando el control al procesador inmediatamente después de la transferencia de dicha palabra [3], [2].

2. **Idea clave** — El procesador no se detiene mediante una interrupción (no salva contexto), sino que simplemente se pausa durante un ciclo de bus justo antes de que necesite utilizarlo, lo que causa que el programa se ejecute más lentamente pero con una eficiencia global mucho mayor que la E/S programada [4], [5].

3. **Diagrama de tiempo del Robo de Ciclo**
```tikz
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[node distance=0.5cm, font=\small]
    % Reloj
    \draw[gray, thin] (0,2) -- (10,2) node[right] {CLK};
    \foreach \x in {0,1,2,3,4,5,6,7,8,9} {
        \draw[gray, thin] (\x,2.1) -- (\x,1.9);
    }

    % CPU Bus Control
    \node at (-1.5,1.5) {CPU Bus};
    \draw[thick, teal] (0,1.5) -- (3,1.5) node[midway, above] {Instrucción} -- (3,1.1) -- (4,1.1) node[midway, below] {PAUSA} -- (4,1.5) -- (7,1.5) node[midway, above] {Instrucción};

    % DMA Bus Control
    \node at (-1.5,0.5) {DMA Bus};
    \draw[thick, orange] (0,0.5) -- (3,0.5) -- (3,0.9) -- (4,0.9) node[midway, above] {ROBO} -- (4,0.5) -- (7,0.5);

    % Marcadores de ciclo
    \draw[<->, >=Stealth] (3,0) -- (4,0) node[midway, below] {1 Ciclo de Bus};
\end{tikzpicture}
\end{document}
```
*Fig. 8-13 · Puntos de ruptura para el DMA: el procesador se suspende justo antes de necesitar el bus [6], [7].*

4. **Comparación de Modos de Transferencia**

| Característica | Robo de Ciclo (Cycle Stealing) | Transferencia en Ráfaga (Burst Mode) |
| :--- | :--- | :--- |
| **Unidad de transferencia** | Una palabra por cada "robo" [3]. | Un bloque completo de datos [3]. |
| **Control del bus** | Se alterna entre DMA y CPU ciclo a ciclo [8]. | El DMA es maestro hasta terminar el bloque [3]. |
| **Impacto en CPU** | Ralentización ligera del procesamiento [4]. | El procesador queda ocioso por un tiempo prolongado [3]. |
| **Uso típico** | Dispositivos de velocidad media/baja [3]. | Dispositivos rápidos (ej. discos magnéticos) [3]. |

5. **Ejercicio de Aplicación (Nivel C)**

##### Ej. Un módulo de DMA transfiere caracteres a memoria mediante robo de ciclo desde un dispositivo que transmite a 9600 bps. El procesador capta instrucciones a un ritmo de 1 MIPS. ¿Cuánto disminuye la velocidad del procesador? [9]

**Resolución**
Para determinar la penalización, calculamos cuántos ciclos de bus "roba" el DMA por segundo en relación a la capacidad de procesamiento de la CPU.


$$
\text{Velocidad de transferencia (caracteres/s)} = \frac{9600 \text{ bps}}{8 \text{ bits/char}} = 1200 \text{ char/s}
$$


$$
\text{Ciclos robados por segundo} = 1200 \text{ ciclos/s}
$$


$$
\text{Ralentización} = \frac{\text{Ciclos robados}}{\text{Instrucciones por segundo (MIPS)}} = \frac{1200}{1,000,000}
$$


$$
\therefore\quad \color{orange}{0.12 \%}
$$


La velocidad del procesador disminuye en un **0.12%**, lo cual es una penalización despreciable comparada con el tiempo que perdería la CPU gestionando la transferencia mediante E/S programada [10].
