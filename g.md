```ahpl
MODULE: PRINTER INTERFACE
  MEMORY: DR; CR; first(JK)
  OUTPUTS: CHAR; ready; accept; print; feed
  INPUTS: datavalid; wait
  COMBUS: IOBUS
1. ready = 1
   -> (~datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR[10:17] & first) \/ (DR[1:8] & ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
8. DEAD END
END SEQUENCE
  CHAR = CR
END
```

| Paso        | Operación                                                                           | Condición                                          | Estado resultante                                                                                                                                                                                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`        | \( ready = 1 \)                                                                     | \( \rightarrow (\overline{datavalid})/(1) \)       | Espera activa. \( ready = 1 \) indica disponibilidad de la interfaz. Bucle de espera mientras \( datavalid = 0 \); salta al paso 2 en el flanco de reloj cuando \( datavalid = 1 \).                                                                                                                |
| `2.`        | \( DR \leftarrow IOBUS \); \( accept = 1 \); \( first \leftarrow 1 \)               | —                                                  | Captura simultánea de datos. El registro de datos de la interfaz \( DR \) se carga desde \( IOBUS \). Se afirma la línea de control \( accept = 1 \) para indicar la recepción. El flag \( first \) se inicializa en 1 para indicar que se procesa el primer carácter.                              |
| `3.`        | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | —                                                  | Desempaquetado del carácter. Si \( first = 1 \), el registro de caracteres de la impresora \( CR \) se carga con el primer carácter de los bits más significativos \( DR[10:17] \). Si \( first = 0 \), se carga con el segundo carácter \( DR[1:8] \).                                             |
| `4.`        | \( feed = RETURN(CR) \); \( print = RETURN(CR) \)                                   | —                                                  | Evaluación lógica combinacional mediante la unidad combinacional externa \( RETURN(CR) \). Activa los comandos físicos \( feed \) (alimentar papel) o \( print \) (imprimir) según el código de carácter ASCII cargado en \( CR \).                                                                 |
| `5.`        | \( Null \)                                                                          | —                                                  | Paso nulo de retardo. Introduce un ciclo de reloj de espera requerido para dar tiempo a que el periférico de impresión reaccione y levante su señal de ocupado \( wait = 1 \).                                                                                                                      |
| `6.`        | —                                                                                   | \( \rightarrow (wait)/(6) \)                       | Bucle de espera (polling). El control permanece en espera en el paso 6 mientras la impresora esté ocupada ejecutando la impresión física y mantenga \( wait = 1 \). Continúa al paso 7 una vez completada la acción (\( wait = 0 \)).                                                               |
| `7.`        | \( first \leftarrow 0 \)                                                            | \( \rightarrow (first, \overline{first})/(3, 1) \) | Control de secuencia. Se limpia el flip-flop \( first \leftarrow 0 \). Si \( first \) era originalmente 1, la bifurcación condicional regresa al paso 3 para procesar y desempaquetar el segundo carácter almacenado en \( DR[1:8] \). Si era 0, regresa al paso 1 para esperar un nuevo handshake. |
| `8.`        | \( DEAD\ END \)                                                                     | —                                                  | Fin de secuencia que detiene el flujo de control del módulo hasta el siguiente inicio asíncrono.                                                                                                                                                                                                    |
| `CHAR = CR` | \( CHAR = CR \)                                                                     | —                                                  | Expresión combinacional permanente fuera de la secuencia. La salida física de datos \( CHAR \) a la impresora refleja de manera continua el contenido del registro \( CR \) en todo momento.                                                                                                        |


---

copia con cursor:

MODULE: PRINTER INTERFACE
  MEMORY: DR[1]; CR[2]; first(JK)
  OUTPUTS: CHAR[2]; ready; accept; print; feed
  INPUTS: datavalid; wait
  COMBUS: IOBUS[1]
1. ready = 1
   -> (~datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR[10:17] & first) \/ (DR[1:8] & ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
8. DEAD END
END SEQUENCE
  CHAR = CR
END