
##### Ej. Programa de software para el computador SIC que permita imprimir N planas de datos a través de la interfaz de impresora (dispositivo #2, módulo `PRINTER INTERFACE N-PLANAS` de `ahpl_fin.md`).

---

### 1. Planteamiento

Una plana equivale a **1024 palabras de 18 bits** ($\text{2000}_8$). La interfaz procesa e imprime cada plana llena de manera autónoma y retorna automáticamente a solicitar la siguiente plana mediante la línea de control `ready` sin requerir la emisión de un nuevo comando por parte de la CPU, manteniendo el flag **`busy = 1`** durante todo el trabajo.

Para indicarle a la interfaz que el trabajo de impresión ha concluido, la CPU debe enviar **4 palabras nulas consecutivas** (`000000` octal). Al detectar estas 4 palabras vacías, la interfaz activa la bandera interna `empty(0)`, detiene la recepción, imprime el texto remanente y apaga el flag `busy <- 0`.

**Fórmula general para $N$ planas:**
- **Total de palabras a enviar ($T$):**  
  
$$
T_{10} = 1024 \cdot N + 4 \quad \implies \quad T_8 = (2000_8 \cdot N) + 4_8
$$

- **Contador negativo (18 bits en complemento a 2):**  
  
$$
\text{Contador}_8 = 2^{18} - T = 777777_8 - T_8 + 1_8
$$

- **Dirección final del bloque en memoria:**  
  
$$
\text{Dirección final}_8 = 00200_8 + T_8 - 1_8
$$


**Resolución numérica en octal para $N = 3$ planas:**
- **Total de palabras ($T$):**  
  
$$
T = (3 \cdot 2000_8) + 4_8 = 6000_8 + 4_8 = \mathbf{6004_8} \quad (3076_{10} \text{ palabras})
$$

- **Contador negativo:**  
  
$$
\text{Contador}_8 = 777777_8 - 6004_8 + 1_8 = \mathbf{771774_8}
$$

- **Rango de direcciones:**  
  
$$
\text{Dirección inicial} = 00200_8 \quad \implies \quad \text{Dirección final} = 00200_8 + 6004_8 - 1_8 = \mathbf{06203_8}
$$


---

### 2. Manejo del flag `busy` (`IS2 01`)

- **Consulta inicial (`00000`–`00002`):** Se ejecuta `IS2 01` una sola vez antes de iniciar la transferencia para verificar que la interfaz esté libre (`busy = 0`). Si está ocupada (`busy = 1`), la CPU entra en espera activa.
- **Bucle de transferencia (`00003`–`00007`):** No se consulta `IS2 01` entre palabras ni entre planas. La instrucción `OD2` realiza el *handshake* por hardware de bus $`ready` / `datavalid` / `accept`$ para transferir de manera continua las $T$ palabras a velocidad de bus.
- **Consulta final (`00010`–`00012`):** Tras enviar el bloque total de palabras (incluidas las 4 de cierre), la CPU entra en un bucle de consulta `IS2 01`. La interfaz mantendrá `busy = 1` mientras se encuentra imprimiendo la última plana. Solo al terminar la impresión e indicar `busy = 0`, la CPU avanzará a la instrucción `HLT`, garantizando la impresión física completa de las $N$ planas en papel.

---

### 3. Restricciones del sistema

1. **Plana final con $1021 \le L \le 1023$ palabras de texto:** Si la última plana contiene $L$ palabras de texto útil dentro de dicho rango, no es posible colocar inmediatamente las 4 palabras de cierre porque sobrepasarían el tamaño máximo de la plana actual ($1024$). El software debe rellenar con palabras vacías (`000000`) hasta completar exactamente la palabra $1024$ de esa plana y, a continuación, agregar las 4 palabras `000000` de cierre (las cuales iniciarán y cortarán de inmediato una plana siguiente).
2. **Plana llena:** Una plana llena de 1024 palabras no puede contener internamente 4 palabras nulas consecutivas (`000000`), ya que esto provocaría el corte prematuro del trabajo de impresión.

---

### 4. Tabla de datos ($N = 3$)

| Dirección | Contenido | Descripción |
| :-: | :-: | - |
| `00100` | `000200` | Puntero a la dirección inicial del bloque de datos en memoria |
| `00101` | `771774` | Conteo negativo de palabras a transferir ($-3076_{10} = 771774_8$) |
| `00200` ... `02177` | Datos | **Plana 1:** 1024 palabras ($2000_8$ datos ASCII) |
| `02200` ... `04177` | Datos | **Plana 2:** 1024 palabras ($2000_8$ datos ASCII) |
| `04200` ... `06177` | Datos | **Plana 3:** 1024 palabras ($2000_8$ datos ASCII) |
| `06200` ... `06203` | `000000` | **Secuencia de cierre:** 4 palabras vacías para apagar la interfaz |

---

### 5. Programa de software (Tabla de instrucciones)

| Dirección | Instrucción | Explicación / Acción |
| :-: | :-: | - |
| `00000` | `IS2 01` | Consulta el estatus del dispositivo #2 (`busy`). Si $busy = 1$, salta a `00002` |
| `00001` | `JMP 00003` | Si $busy = 0$ (no saltó), avanza al bucle de envío de datos |
| `00002` | `JMP 00000` | Si $busy = 1$ (saltó), reintenta la consulta (espera activa inicial) |
| `00003` | `LAC I 00100` | Carga en `AC` la palabra apuntada indirectamente por la dirección `00100` |
| `00004` | `OD2` | Envía la palabra del `AC` al dispositivo #2 mediante *handshake* de bus |
| `00005` | `ISZ 00100` | Incrementa el puntero de memoria para acceder a la siguiente palabra |
| `00006` | `ISZ 00101` | Incrementa el contador negativo; si alcanza cero ($T$ palabras enviadas), salta a `00010` |
| `00007` | `JMP 00003` | Salta al inicio del bucle para transferir la siguiente palabra |
| `00010` | `IS2 01` | Consulta final de estatus. Si $busy = 1$ (imprimiendo), salta a `00012` |
| `00011` | `JMP 00013` | Si $busy = 0$ (impresión física total concluida), avanza a `HLT` |
| `00012` | `JMP 00010` | Si $busy = 1$ (saltó), reintenta la consulta final (espera activa de impresión) |
| `00013` | `HLT` | Detiene la CPU tras confirmar la finalización completa del trabajo de impresión |

---

### 6. Funcionamiento de las instrucciones

- **`IS2` (Input Status and Test):** Examina el registro de estatus `CSR` de la impresora (#2) probando el bit `CSBUS(0)` ($busy$) mediante la máscara octal `01`. Si el bit es `1`, la CPU salta la siguiente instrucción; si es `0`, continúa secuencialmente.
- **`OD2` (Output Data):** Coloca la palabra contenida en el acumulador `AC` sobre el `IOBUS` y ejecuta la secuencia de señales de interacción por hardware (*handshake*) con la interfaz de la impresora #2.
- **`LAC I` (Load Accumulator Indirect):** Carga en el registro `AC` el dato almacenado en la dirección contenida en la posición apuntada indirectamente.
- **`ISZ` (Increment and Skip if Zero):** Incrementa en 1 el contenido de la dirección especificada en memoria. Si el resultado es cero (`000000`), salta la instrucción siguiente. Se utiliza para actualizar los punteros de memoria y controlar el bucle con el contador negativo.
- **`JMP` (Jump):** Transfiere incondicionalmente el control del programa a la dirección indicada.
- **`HLT` (Halt):** Detiene la ejecución del procesador SIC.
