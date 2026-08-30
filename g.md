| Identificador | Sección | Tamaño | Rol |
|---|---|---|---|
| `DR` | MEMORY | `(18)` | Registro de datos de la interfaz — captura la palabra completa de 18 bits desde el `IOBUS` |
| `CR` | MEMORY | `(8)` | Registro de carácter — almacena temporalmente el carácter de 8 bits extraído de `DR` para ser impreso |
| `first` | MEMORY | `escalar` | Flip-flop de control (tipo JK) — indica si se procesa el primer byte (`1`) o el segundo byte (`0`) de la palabra |
| `CHAR` | OUTPUTS | `(8)` | Vector de salida — líneas de datos que transmiten el carácter de 8 bits (`CR`) hacia la impresora |
| `ready` | OUTPUTS | `escalar` | Señal de disponibilidad — se activa en el paso 1 indicando que la interfaz está lista para recibir una nueva palabra |
| `accept` | OUTPUTS | `escalar` | Señal de aceptación — pulso de sincronización enviado a la CPU en el paso 2 al recibir los datos |
| `print` | OUTPUTS | `escalar` | Comando de impresión — pulso que ordena imprimir el carácter en `CHAR` si este no es un retorno de carro |
| `feed` | OUTPUTS | `escalar` | Comando de avance — pulso que ordena el avance de línea y retorno si el carácter en `CHAR` es un retorno de carro |
| `datavalid` | INPUTS | `escalar` | Señal de datos válidos — entrada desde la CPU que indica que el dato en el bus es estable |
| `wait` | INPUTS | `escalar` | Señal de espera de la impresora — entrada que se pone en `1` mientras la impresora realiza el ciclo de impresión física |
| `IOBUS` | COMBUS | `(18)` | Bus de datos de entrada compartido — de donde la interfaz captura la palabra de datos de 18 bits |

```ahpl
MODULE: PRINTER INTERFACE
  MEMORY: DR(18); CR(8); first(JK)
  OUTPUTS: CHAR(8); ready; accept; print; feed
  INPUTS: datavalid; wait
  COMBUS: IOBUS(18)
  1. ready = 1
     -> (~datavalid)/(1)
  2. DR <- IOBUS; accept = 1; first <- 1
  3. CR <- (DR[10:17] & first) v (DR[1:8] & ~first)
  4. feed = RETURN(CR); print = ~RETURN(CR)
  5. Null
  6. -> (wait)/(6)
  7. first <- 0
     -> (first, ~first)/(3, 1)
END SEQUENCE
  CHAR = CR
END
```

| Paso        | Operación                                                                                               | Condición                                          | Estado resultante                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`        | \( ready = 1 \)                                                                                         | \( \rightarrow (\overline{datavalid})/(1) \)       | Espera activa. \( ready = 1 \) indica disponibilidad. Bucle de espera mientras \( datavalid = 0 \); sale al paso 2 cuando \( datavalid = 1 \).                      |
| `2.`        | \( DR \leftarrow IOBUS \); \( accept = 1 \); \( first \leftarrow 1 \)                                   | —                                                  | Captura simultánea de la palabra en \( DR(18) \) al flanco de reloj. La línea \( accept \) se activa por un ciclo y el control \( first \) se inicializa en 1.      |
| `3.`        | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \pmb{\text{ [sic]}} \) | —                                                  | Desempaquetado del carácter. Si \( first = 1 \) se extrae el byte alto de \( DR \); si \( first = 0 \) se extrae el byte bajo hacia \( CR(8) \).                    |
| `4.`        | \( feed = RETURN(CR) \); \( print = \overline{RETURN(CR)} \)                                            | —                                                  | Evaluación combinacional. La lógica de \( RETURN(CR) \) detecta si es retorno de carro para direccionar el pulso a \( feed \) o a \( print \).                      |
| `5.`        | \( Null \)                                                                                              | —                                                  | Paso nulo de sincronización. Otorga un ciclo de reloj extra para que la impresora reaccione y levante la línea de espera \( wait \).                                |
| `6.`        | —                                                                                                       | \( \rightarrow (wait)/(6) \)                       | Polling (espera activa). El control de la interfaz permanece en el paso 6 mientras la línea \( wait = 1 \).                                                         |
| `7.`        | \( first \leftarrow 0 \)                                                                                | \( \rightarrow (first, \overline{first})/(3, 1) \) | Control de flujo. Se borra \( first \). Si su estado previo era 1, bifurca al paso 3 para el segundo byte; si era 0, retorna al paso 1 a esperar una nueva palabra. |
| `CHAR = CR` | \( CHAR = CR \)                                                                                         | —                                                  | Salida combinacional permanente fuera de la secuencia. La salida \( CHAR(8) \) refleja continuamente el estado de \( CR(8) \).                                      |