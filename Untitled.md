## Código AHPL de un Módulo Simple

1. **Definición formal** — Un módulo en AHPL es una descripción estructural de hardware que se compone de una sección de declaraciones (donde se especifican de forma precisa los registros, buses y líneas de entrada/salida) y una secuencia de control constituida por transferencias sincronizadas por reloj y conexiones lógicas combinacionales en ciclos de tiempo individuales.

2. **Idea clave** — La descripción procedimental de un módulo requiere que el diseñador posea un esquema mental claro del hardware antes de escribir la secuencia, puesto que cada asignación o conexión especifica directamente conexiones físicas reales de circuitos y registros.

3. **Figura o diagrama**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\tikzset{
    block/.style={draw, rectangle, minimum width=3cm, minimum height=1.5cm, text centered, draw=teal, fill=teal!10, line width=1pt},
    line/.style={draw, -Latex, line width=1pt, draw=gray}
}
\begin{tikzpicture}[node distance = 2cm, auto]
    % Módulo
    \node [block] (module) {RECEPTOR\_SIMPLE};
    
    % Entradas
    \path [line] (-3.5, 0.4) -- node[above, near start] {start} (module.west |- 0, 0.4);
    \draw [line, double, double distance=2pt] (-3.5, -0.4) -- node[above, near start] {DATOS\_IN(8)} (module.west |- 0, -0.4);
    
    % Salidas
    \path [line] (module.east |- 0, 0.4) -- node[above, near end] {ready} (3.5, 0.4);
    \draw [line, double, double distance=2pt] (module.east |- 0, -0.4) -- node[above, near end] {AC(8)} (3.5, -0.4);
\end{tikzpicture}
\end{document}
```
*Fig. 1-1 · Diagrama de caja negra del módulo receptor simple.*

4. **Desarrollo del módulo**

##### Declaraciones

| Identificador | Sección | Tamaño    | Rol                                                             |
| ------------- | ------- | --------- | --------------------------------------------------------------- |
| `AC`          | MEMORY  | `(8)`     | Registro acumulador para almacenar el dato entrante             |
| `busy`        | MEMORY  | `escalar` | Registro de 1 bit que indica si el módulo está procesando datos |
| `DATOS_IN`    | INPUTS  | `(8)`     | Líneas de entrada de datos de 8 bits                            |
| `start`       | INPUTS  | `escalar` | Señal de inicio de recepción                                    |
| `AC`          | OUTPUTS | `(8)`     | Salida paralela del registro acumulador                         |
| `ready`       | OUTPUTS | `escalar` | Señal de salida que indica que el dato ha sido almacenado       |
| `DBUS`        | COMBUS  | `(8)`     | Bus de datos de interconexión interna                           |

##### Bloque de código

```
MODULE: RECEPTOR_SIMPLE
MEMORY: AC(8); busy
INPUTS: DATOS_IN(8); start
OUTPUTS: AC(8); ready
COMBUS: DBUS(8)

1. DBUS = DATOS_IN; ready = 0; busy = 0
   -> (~start)/(1)
2. DBUS = DATOS_IN; busy = 1; AC <- DBUS
3. ready = 1; busy = 0
   -> (1)
END SEQUENCE
END
```

##### Tabla de pasos

| Paso | Operación                                                                | Condición                  | Estado resultante                                                                               |
| ---- | ------------------------------------------------------------------------ | -------------------------- | ----------------------------------------------------------------------------------------------- |
| `1.` | \( DBUS = DATOS\_IN \) <br> \( ready = 0 \) <br> \( busy = 0 \)          | \( \overline{start} = 1 \) | El módulo permanece en estado de reposo esperando la señal \( start = 1 \).                     |
| `2.` | \( DBUS = DATOS\_IN \) <br> \( busy = 1 \) <br> \( AC \leftarrow DBUS \) | —                          | El dato en el bus se transfiere al acumulador \( AC \) en el flanco de reloj.                   |
| `3.` | \( ready = 1 \) <br> \( busy = 0 \)                                      | —                          | Se activa la bandera \( ready \) y se retorna incondicionalmente al paso 1 para un nuevo ciclo. |