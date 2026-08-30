| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `DR` | MEMORY | `(18)` | Registro de datos que carga la palabra de 18 bits desde el bus `IOBUS` |
| `CR` | MEMORY | `(8)` | Registro de caracteres que almacena el byte actual en proceso de impresión |
| `first` | MEMORY | escalar (JK) | Flip-flop de control que indica si se está procesando el primer (1) o el segundo (0) carácter |
| `CHAR` | OUTPUTS | `(8)` | Vector de salida que entrega el carácter ASCII directamente a la impresora |
| `ready` | OUTPUTS | escalar | Señal de salida que indica al computador que la interfaz está lista para recibir datos |
| `accept` | OUTPUTS | escalar | Señal de salida que indica al computador que el dato fue capturado en `DR` |
| `print` | OUTPUTS | escalar | Comando síncrono que ordena a la impresora imprimir el carácter en `CHAR` |
| `feed` | OUTPUTS | escalar | Comando síncrono que ordena a la impresora realizar un avance de línea |
| `datavalid` | INPUTS | escalar | Señal de entrada que indica que el computador ha colocado un dato válido en el bus |
| `wait` | INPUTS | escalar | Señal de entrada que indica que la impresora está ocupada procesando una operación |
| `IOBUS` | COMBUS | `(18)` | Bus de comunicaciones del sistema digital, fuente de datos para `DR` |

```ahpl
MODULE: PRINTER INTERFACE
  MEMORY: DR(18); CR(8); first(JK)
  OUTPUTS: CHAR(8); ready; accept; print; feed
  INPUTS: datavalid; wait
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

| Paso | Operación | Condición | Estado resultante / Explicación |
|---|---|---|---|
| `1.` | \( ready = 1 \) | \( \rightarrow (\overline{datavalid})/(1) \) | **Espera activa de datos**. La interfaz establece su señal \( ready = 1 \) para indicar disponibilidad. Permanece en bucle en el paso 1 mientras la CPU mantenga \( datavalid = 0 \) (\( \overline{datavalid} \)); cuando se detecta un \( 1 \) lógico en dicha línea, el control avanza al paso 2. |
| `2.` | \( DR \leftarrow IOBUS \) ; \( accept = 1 \) ; \( first \leftarrow 1 \) | — | **Captura y reconocimiento**. Al flanco de reloj positivo, el registro \( DR \) carga los 18 bits presentes en \( IOBUS \), se activa la salida combinacional \( accept = 1 \) durante un ciclo de reloj para notificar la recepción y se inicializa el flip-flop \( first \) en \( 1 \). |
| `3.` | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | — | **Desempaquetado de caracteres**. Si \( first = 1 \), el registro de caracteres \( CR \) toma la porción alta de la palabra (\( DR_{10:17} \)). Si \( first = 0 \), toma el byte inferior (\( DR_{1:8} \)). |
| `4.` | \( feed = RETURN(CR) \) ; \( print = \overline{RETURN(CR)} \) | — | **Decodificación y comando combinacional**. La unidad combinacional \( RETURN(CR) \) evalúa el byte en \( CR \). Si es un retorno de carro, activa el avance \( feed = 1 \) y desactiva la impresión (\( print = 0 \)); si es un carácter ordinario, activa la impresión \( print = 1 \) y desactiva el avance. |
| `5.` | \( Null \) | — | **Paso nulo de sincronización**. No altera registros durante este ciclo de reloj, otorgándole el tiempo necesario a la impresora para reaccionar al comando físico y levantar la señal de ocupado \( wait \). |
| `6.` | — | \( \rightarrow (wait)/(6) \) | **Espera por procesamiento periférico**. El control de la secuencia se bloquea en un bucle cerrado en el paso 6 mientras la impresora mantenga la línea \( wait = 1 \). Sale al paso 7 una vez completada la impresión o el avance (\( wait = 0 \)). |
| `7.` | \( first \leftarrow 0 \) | \( \rightarrow (first, \overline{first})/(3, 1) \) | **Control del bucle interno**. El flip-flop \( first \) se limpia en el borde de reloj. Al bifurcar, se evalúa su estado inmediatamente previo: si era \( 1 \), retorna al paso 3 para transferir el segundo carácter de \( DR \); si era \( 0 \), retorna al paso 1 para esperar una nueva palabra de datos. |

🤖 ¿Te gustaría que analicemos cómo se modificaría esta secuencia de control si utilizáramos el protocolo de handshake asíncrono completamente respondiente descrito en el Example 9.4 del mismo libro?