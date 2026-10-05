# b) Escribir el programa de software que permita imprimir esa  cantidad de datos desde el computador SIC. 

---

##### Ej. Programa SIC para imprimir 1K $1024$ datos a través de la interfaz de impresora (dispositivo #2).

**Resolución**
Bucle de E/S programada: consulta de estatus con `IS2 01` (bit $busy$) y envío palabra a palabra con `OD2`.

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
| `00100` | `000200` | Puntero al inicio del bloque de datos |
| `00101` | `776000` | Contador negativo ($-1024_{10} = 776000_8$) |
| `00200` ... `02177` | Datos | Bloque de 1024 palabras de 18 bits (2048 caracteres ASCII) a imprimir |

**Tabla de instrucciones**

| Dirección | Instrucción   | Explicación / Acción |
| --------- | ------------- | -------------------- |
| `00000`   | `IS2 01`      | Estatus de la impresora (#2), máscara `01` (bit $busy$): si $busy = 1$, salta `00001` |
| `00001`   | `JMP 00003`   | $busy = 0$: va a enviar el dato |
| `00002`   | `JMP 00000`   | $busy = 1$: repite la consulta |
| `00003`   | `LAC I 00100` | `AC` ← palabra apuntada indirectamente por `00100` |
| `00004`   | `OD2`         | Envía `AC` a la impresora (#2) |
| `00005`   | `ISZ 00100`   | Avanza el puntero al siguiente dato |
| `00006`   | `ISZ 00101`   | Incrementa el contador; si llega a cero (1024 palabras enviadas), salta `00007` |
| `00007`   | `JMP 00000`   | Vuelve a transferir la siguiente palabra |
| `00010`   | `HLT`         | Fin de la impresión de las 1024 palabras |
