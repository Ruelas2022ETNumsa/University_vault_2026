### Módulo de Carga Sincrónica WAITER

1. **Definición formal**  
El lenguaje de descripción de hardware AHPL (*A Hardware Programming Language*) se basa en la premisa de que un sistema digital puede dividirse de manera óptima en una sección de control secuencial y otra sección que contiene los registros de datos y su lógica combinacional asociada. Cada instrucción o paso dentro de la secuencia de control representa un periodo de reloj maestro del sistema, en el cual se ejecutan transferencias sincrónicas hacia registros y conexiones a buses lógicos.

2. **Idea clave**  
La sincronización en AHPL está gobernada por reloj, lo que implica que las transferencias con el operador de asignación \( \leftarrow \) ocurren de forma síncrona en el flanco activo del reloj del sistema. Por el contrario, las conexiones representadas con el operador \( = \) son puramente combinacionales y no requieren el flanco del reloj para propagar su valor.

3. **Diagrama de caja negra**

```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\node[draw, rectangle, minimum width=3.5cm, minimum height=2.2cm, line width=1pt] (mod) at (0,0) {\textbf{MODULE: WAITER}};
\draw[<-] (mod.140) -- ++(-1.8,0) node[above, midway] {\( go \)};
\draw[<-] (mod.200) -- ++(-1.8,0) node[below, midway] {\( DBUS \)};
\draw[->] (mod.0) -- ++(1.8,0) node[above, midway] {\( ready \)};
\end{document}
```

---

##### Ej. Diseñar un módulo AHPL simple que espere una señal de inicio go, cargue un registro de almacenamiento AC con los datos de un bus de entrada DBUS, active una señal de salida ready y finalice su secuencia de control.

**Resolución**  
Se diseña una secuencia lineal que realiza un bucle de espera (*polling*) sobre la señal *go* y, tras su activación, transfiere los datos del bus de entrada al acumulador, finalizando en un estado de parada.

1) Tabla de declaraciones:

| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `AC` | MEMORY | `` | Registro acumulador de destino para almacenar el dato |
| `go` | INPUTS | escalar | Señal de habilitación de inicio para comenzar la carga |
| `DBUS` | INPUTS | `` | Líneas de datos de entrada desde las cuales se lee |
| `ready` | OUTPUTS | escalar | Línea de salida que indica la finalización del proceso |

2) Bloque de código:

```
MODULE: WAITER
INPUTS: go; DBUS
OUTPUTS: ready
MEMORY: AC

1. -> (~go) / (1)
2. AC <- DBUS
3. ready = 1
4. DEAD END
END SEQUENCE
END
```

3) Tabla de pasos:

| Paso | Operación | Condición | Estado resultante |
|---|---|---|---|
| `1.` | \( \rightarrow (1) \) | \( \overline{go} = 1 \) | Espera activa (*polling*) en el paso 1 mientras la señal sea baja. |
| `2.` | \( AC \leftarrow DBUS \) | — | Carga sincrónica del dato de \( DBUS \) en el acumulador al flanco de reloj. |
| `3.` | \( ready = 1 \) | — | Conexión combinacional directa que activa la señal \( ready \) durante este ciclo. |
| `4.` | DEAD END | — | Terminación del flujo de control y parada del módulo. |

---

⚡ ¿Te gustaría que modifiquemos este código para transformarlo en un sistema interactivo que implemente un protocolo de handshake completo de dos o tres líneas?