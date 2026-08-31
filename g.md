### **Tabla de declaraciones**

| Identificador | Sección | Tamaño | Rol |
| :--- | :--- | :--- | :--- |
| `DR` | MEMORY | `(18)` | Registro de datos de 18 bits que captura la palabra desde el bus de E/S |
| `CR` | MEMORY | `(8)` | Registro de 8 bits que almacena el carácter ASCII individual que se va a procesar |
| `first` | MEMORY | escalar | Flip-flop tipo JK de control que indica si se procesa el primer (1) o el segundo (0) carácter |
| `CHAR` | OUTPUTS | `(8)` | Vector de salida que contiene el carácter ASCII actual enviado a la impresora |
| `ready` | OUTPUTS | escalar | Señal de salida que indica que la interfaz está lista para recibir una nueva palabra |
| `accept` | OUTPUTS | escalar | Señal de aceptación (handshake) activa por un ciclo de reloj para notificar la recepción |
| `print` | OUTPUTS | escalar | Comando de salida que indica a la impresora que debe imprimir el carácter en `CHAR` |
| `feed` | OUTPUTS | escalar | Comando de salida que indica a la impresora que debe avanzar papel |
| `datavalid` | INPUTS | escalar | Señal de entrada que indica que el CPU ha colocado un dato válido en el bus |
| `wait` | INPUTS | escalar | Señal de entrada que indica que la impresora está ocupada procesando una operación |
| `IOBUS` | COMBUS | `(18)` | Bus de comunicación combinacional de entrada/salida de 18 bits |

---

### **Módulo AHPL: PRINTER INTERFACE**

```ahpl
MODULE: PRINTER_INTERFACE
MEMORY: DR(18); CR(8); first
INPUTS: datavalid; wait
OUTPUTS: CHAR(8); ready; accept; print; feed
COMBUS: IOBUS(18)

1. ready = 1
   -> (~datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR(10:17) /\ first) \/ (DR(1:8) /\ ~first)
4. feed = RETURN(CR); print = ~RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
END SEQUENCE
CHAR = CR
END
```

---

### **Lectura paso a paso de la secuencia**

| Paso | Operación | Condición | Estado resultante |
| :--- | :--- | :--- | :--- |
| `1.` | \( \text{ready} = 1 \) | \( \rightarrow (\overline{\text{datavalid}})/(1) \) | **Espera activa (Polling).** La interfaz notifica al CPU que está lista para recibir datos levantando la línea \( \text{ready} \). El secuenciador permanece en el paso 1 en un bucle cerrado mientras \( \text{datavalid} = 0 \), y avanza al paso 2 en el flanco de reloj cuando la CPU activa \( \text{datavalid} = 1 \). |
| `2.` | \( DR \leftarrow \text{IOBUS} \); \( \text{accept} = 1 \); \( \text{first} \leftarrow 1 \) | — | **Carga inicial y handshake.** En el flanco de subida de reloj, el registro \( DR(18) \) captura la palabra completa del bus \( \text{IOBUS}(18) \). Simultáneamente, el flip-flop \( \text{first} \) se inicializa en \( 1 \) y se genera un pulso combinacional de un ciclo en \( \text{accept} = 1 \) para confirmar la recepción del dato al CPU. |
| `3.` | \( CR \leftarrow (DR_{10:17} \land \text{first}) \lor (DR_{1:8} \land \overline{\text{first}}) \) | — | **Desempaquetado del carácter.** Se extrae un carácter ASCII de 8 bits de la palabra de datos de 18 bits. Si \( \text{first} = 1 \), el registro \( CR(8) \) se carga con el primer carácter de los bits \( DR_{10:17} \). Si \( \text{first} = 0 \), se carga el segundo carácter desde \( DR_{1:8} \). |
| `4.` | \( \text{feed} = \text{RETURN}(CR) \); \( \text{print} = \overline{\text{RETURN}(CR)} \) | — | **Decodificación de comandos.** La función combinacional \( \text{RETURN}(CR) \) evalúa el carácter en \( CR \). Si detecta que es un retorno de carro, activa la línea de salida \( \text{feed} = 1 \); en caso contrario, activa \( \text{print} = 1 \) para ordenar la impresión del carácter estándar. |
| `5.` | \( \text{Null} \) | — | **Paso nulo de sincronización.** Se consume un ciclo de reloj completo sin alterar registros para dar tiempo físico de propagación a la impresora y permitirle levantar la señal de ocupado \( \text{wait} \). |
| `6.` | — | \( \rightarrow (\text{wait})/(6) \) | **Espera de dispositivo (Polling).** El secuenciador permanece retenido en un bucle de espera en el paso 6 mientras la impresora realice la operación de impresión o avance físico y mantenga \( \text{wait} = 1 \). Avanza al paso 7 cuando \( \text{wait} = 0 \). |
| `7.` | \( \text{first} \leftarrow 0 \) | \( \rightarrow (\text{first}, \overline{\text{first}})/(3, 1) \) | **Control de flujo.** El flip-flop \( \text{first} \) se borra síncronamente en \( 0 \). La bifurcación evalúa el estado previo de \( \text{first} \): si era \( 1 \) (primer carácter impreso), salta al paso 3 para procesar el segundo carácter; si era \( 0 \) (ambos caracteres impresos), retorna al paso 1 para esperar una nueva transmisión del CPU. |
| `CHAR = CR` | \( \text{CHAR} = CR \) | — | **Salida combinacional permanente.** Definida fuera de la secuencia de control. La salida \( \text{CHAR}(8) \) refleja de manera continua y en tiempo real el contenido de \( CR(8) \), asegurando que el carácter esté disponible para la impresora durante todo el ciclo de impresión. |

---
¿Te gustaría que analicemos cómo se modifica este módulo para que la secuencia de control sea completamente iniciada y controlada por la CPU mediante líneas del bus de control `CSBUS`?