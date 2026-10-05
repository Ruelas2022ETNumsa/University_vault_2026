##### Ej. Escribir el programa de software para el computador SIC que permita imprimir 1K $1024$ datos a través de la interfaz de impresora (módulo PRINTER INTERFACE de la fuente `codigo_base.md`). Respetá el protocolo de esa interfaz (consulta de estatus y transferencia de datos) y los tamaños estándar del SIC. Entregá tabla de datos y tabla de instrucciones con dirección, instrucción y explicación.

**Resolución**
Bucle de E/S programada con consulta de estatus (polling) mediante `IS2 01` (máscara del bit $busy$; la espera usa dos saltos: `JMP 00003` si la interfaz está libre y `JMP 00000` si está ocupada) y transferencia palabra a palabra mediante `OD2` para un bloque de 1024 palabras.


$$
N = 1024_{10} = 2000_8
$$


$$
\text{Contador negativo} = 2^{18} - 1024_{10} = 776000_8
$$


$$
\text{Dirección final} = 00200_8 + 2000_8 - 1 = 02177_8
$$


$$
\therefore\quad \color{orange}{\text{Bloque de } 1024 \text{ palabras desde } 00200_8 \text{ hasta } 02177_8}
$$


**Tabla de datos**

| Dirección | Contenido | Descripción |
|-|-|-|
| `00100` | `000200` | Puntero a la dirección inicial del bloque de datos en memoria |
| `00101` | `776000` | Conteo negativo de palabras a transferir ($-1024_{10} = 776000_8$) |
| `00200` ... `02177` | Datos | Bloque de 1024 palabras de 18 bits (2048 caracteres ASCII) a imprimir |

**Tabla de instrucciones**

| Dirección | Instrucción   | Explicación / Acción                                                                      |
| --------- | ------------- | ----------------------------------------------------------------------------------------- |
| `00000`   | `IS2 01`      | Consulta el estatus de la impresora (#2) con máscara `01` (bit $busy$). Si la interfaz está ocupada ($busy = 1$), salta `00001`   |
| `00001`   | `JMP 00003`   | Interfaz libre ($busy = 0$): salta a la carga y envío del dato |
| `00002`   | `JMP 00000`   | Bucle de espera activa (polling) mientras la interfaz esté ocupada       |
| `00003`   | `LAC I 00100` | Carga en `AC` la palabra apuntada indirectamente por la dirección `00100`                 |
| `00004`   | `OD2`         | Emite la instrucción de salida de datos (`Output Data`) enviando `AC` a la impresora (#2) |
| `00005`   | `ISZ 00100`   | Incrementa el puntero de memoria para acceder a la siguiente palabra                      |
| `00006`   | `ISZ 00101`   | Incrementa el contador negativo; si alcanza cero (1024 palabras enviadas), salta `00007`  |
| `00007`   | `JMP 00000`   | Salta al inicio del bucle para transferir la siguiente palabra                            |
| `00010`   | `HLT`         | Detiene la CPU tras completar la impresión de las 1024 palabras                           |
