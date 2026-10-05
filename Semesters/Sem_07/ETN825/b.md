# b) Escribir el programa de software que permita imprimir esa  cantidad de datos desde el computador SIC. 

##### Ej. Programa de software para el computador SIC que permita imprimir 1K $1024$ datos a través de la interfaz.

**Resolución**
Transferencia de un bloque de 1024 palabras desde memoria hacia el dispositivo de salida #0 mediante un bucle de E/S programada (polling de estatus e instrucción `OD0`), o mediante la activación del canal de Buffer (`OB0`).

---

### OPCIÓN 1: Transferencia por E/S Programada (Polling)

**Tabla de datos**

| Dirección | Contenido | Descripción |
|-|-|-|
| `00100` | `000200` | Puntero a la dirección inicial del bloque de datos en memoria |
| `00101` | `776000` | Conteo negativo de palabras a transferir ($-1024_{10} = 776000_8$) |
| `00200` ... `02177` | Datos | Bloque de 1024 palabras de 18 bits a imprimir |

**Tabla de instrucciones**

| Dirección | Instrucción | Explicación / Acción |
|-|-|-|
| `00000` | `LAC I 00100` | Carga en `AC` la palabra apuntada indirectamente por la dirección `00100` |
| `00001` | `IS0 01` | Consulta el estatus del dispositivo #0. Si $ready = 1$, salta la siguiente instrucción |
| `00002` | `JMP 00001` | Bucle de espera activa (polling) mientras la interfaz esté ocupada |
| `00003` | `OD0` | Emite la instrucción de salida de datos (`Output Data`) enviando `AC` al dispositivo #0 |
| `00004` | `ISZ 00100` | Incrementa el puntero de memoria para acceder al siguiente dato |
| `00005` | `ISZ 00101` | Incrementa el contador negativo; si alcanza cero ($1024$ palabras enviadas), salta `00006` |
| `00006` | `JMP 00000` | Salta al inicio del bucle para transferir la siguiente palabra |
| `00007` | `HLT` | Detiene la CPU tras completar la impresión de las 1024 palabras |

---

### OPCIÓN 2: Transferencia por Canal de Buffer (`OB0`)

**Tabla de datos (Reservados para Canal Buffer 0)**

| Dirección | Contenido | Descripción |
|-|-|-|
| `00040` | `776000` | Conteo negativo de palabras del Buffer ($-1024_{10}$) |
| `00041` | `02177` | Dirección final del área de Buffer en memoria ($00200_8 + 1023_{10} = 02177_8$) |

**Tabla de instrucciones**

| Dirección | Instrucción | Explicación / Acción |
|-|-|-|
| `00000` | `OB0` | Emite la orden de activación de Buffer de salida (`Output Buffer`) al dispositivo #0 |
| `00001` | `HLT` | Libera la CPU; el hardware de Buffer del SIC transfiere de forma autónoma los 1K datos |
