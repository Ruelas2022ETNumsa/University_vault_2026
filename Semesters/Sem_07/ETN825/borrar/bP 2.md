# b) Escribir el programa de software que permita imprimir esa cantidad de datos desde el computador SIC

---

## Planteamiento

Bucle de E/S programada sobre la interfaz de impresora (dispositivo #2) modificada para recibir 1K datos. Se consulta el estatus con $IS2\ 01$ (bit $busy$) **una vez antes** de iniciar el bloque, se envía palabra a palabra con $OD2$, y se consulta el estatus **una vez al final** para asegurar que la impresión terminó antes de $HLT$.

$$
N = 1024_{10} = 2000_{8}
$$

$$
\text{Contador negativo} = 2^{18} - 1024_{10} = 777777_{8} - 1777_{8} = 776000_{8}
$$

$$
\text{Dirección final} = 00200_{8} + 2000_{8} - 1 = 02177_{8}
$$

$$
\therefore\quad \text{Bloque de } 1024 \text{ palabras desde } 00200_{8} \text{ hasta } 02177_{8} \text{ con contador } 776000_{8}
$$

---

## Manejo del flag $busy$ ($IS2\ 01$)

En la interfaz modificada, $busy$ se activa al recibir el comando de transferencia y permanece en $1$ durante la recepción del bloque de 1024 palabras. Por eso no se puede consultar antes de cada palabra: tras la primera, $busy = 1$ y el programa quedaría esperando para siempre.

- **Consulta inicial (`00000`–`00002`):** se verifica $busy = 0$ una sola vez antes de iniciar el bloque. Si $busy = 1$, espera activa.
- **Bucle de envío (`00003`–`00007`):** no consulta $busy$. La sincronización palabra a palabra la hace el *handshake* de bus de $OD2$ ($ready$ / $datavalid$ / $accept$).
- **Consulta final (`00010`–`00012`):** al terminar de enviar las 1024 palabras, espera activa hasta $busy = 0$, es decir, hasta que la interfaz termine de imprimir el bloque. Recién entonces ejecuta $HLT$.

---

## Tabla de datos

| Dirección | Contenido | Descripción |
|-|-|-|
| `00100` | `000200` | Puntero al inicio del bloque de datos |
| `00101` | `776000` | Contador negativo ($-1024_{10} = 776000_{8}$) |
| `00200` ... `02177` | Datos | Bloque de 1024 palabras de 18 bits (2048 caracteres ASCII) a imprimir |

---

## Programa

| Dirección | Instrucción | Operación | Explicación |
|-|-|-|-|
| `00000` | `IS2 01` | $busy = 1 \Rightarrow$ salta `00001` | Estatus de la impresora (#2), máscara `01` (bit $busy$). Consulta inicial |
| `00001` | `JMP 00003` | $PC \leftarrow 00003$ | $busy = 0$: va al bucle de envío |
| `00002` | `JMP 00000` | $PC \leftarrow 00000$ | $busy = 1$: repite la consulta (espera activa inicial) |
| `00003` | `LAC I 00100` | $AC \leftarrow M[M[00100]]$ | $AC \leftarrow$ palabra apuntada indirectamente por `00100` |
| `00004` | `OD2` | $\text{Impresora} \leftarrow AC$ | Envía $AC$ a la impresora (#2) con *handshake* de bus |
| `00005` | `ISZ 00100` | $M[00100] \leftarrow M[00100] + 1$ | Avanza el puntero al siguiente dato |
| `00006` | `ISZ 00101` | $M[00101] \leftarrow M[00101] + 1$; si $= 0$ salta `00007` | Incrementa el contador; si llega a cero (1024 palabras enviadas) salta `00007` |
| `00007` | `JMP 00003` | $PC \leftarrow 00003$ | Vuelve al bucle para enviar la siguiente palabra (sin consultar $busy$) |
| `00010` | `IS2 01` | $busy = 1 \Rightarrow$ salta `00011` | Consulta final: ¿la interfaz terminó de imprimir el bloque? |
| `00011` | `JMP 00013` | $PC \leftarrow 00013$ | $busy = 0$: impresión completa, va a detener la CPU |
| `00012` | `JMP 00010` | $PC \leftarrow 00010$ | $busy = 1$: repite la consulta (espera activa final) |
| `00013` | `HLT` | — | Fin: las 1024 palabras ya fueron enviadas e impresas |

---

## Funcionamiento de las instrucciones

- **`IS2`:** lee el estatus del dispositivo #2 y evalúa el bit indicado por la máscara (`01` prueba $CSBUS_{0} = busy$). Si el bit vale $1$ salta la instrucción siguiente; si vale $0$ no salta.
- **`ISZ`:** incrementa en 1 la posición de memoria indicada. Si el resultado es cero, salta la instrucción siguiente; si no, continúa en secuencia.
- **`HLT`:** detiene la CPU. La consulta final con `IS2 01` evita que se detenga mientras la interfaz aún está imprimiendo.
