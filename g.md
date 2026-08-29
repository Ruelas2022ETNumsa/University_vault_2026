## Módulo PRINTER INTERFACE (Example 9.3)

```ahpl
MODULE: PRINTER INTERFACE
MEMORY: DR; CR; first(JK)
OUTPUTS: CHAR; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS

1. ready = 1
   -> (~datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR[10:17] & first) | (DR[1:8] & ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
END SEQUENCE
CHAR = CR
END
```

| Paso        | Operación                                                                           | Condición                                          | Estado resultante                                                                                                                                                                                                                                  |
| :---------- | :---------------------------------------------------------------------------------- | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`        | \( ready = 1 \)                                                                     | \( \rightarrow (\overline{datavalid})/(1) \)       | **Espera activa de datos**. La interfaz anuncia disponibilidad mediante \( ready = 1 \). Se mantiene en bucle cerrado en el paso 1 mientras la línea de datos válidos permanezca desactivada (\( datavalid = 0 \)).                                |
| `2.`        | \( DR \leftarrow IOBUS \) <br> \( accept = 1 \) <br> \( first \leftarrow 1 \)       | —                                                  | **Captura y sincronización**. El registro de datos \( DR \) captura los 18 bits del bus. Se envía un pulso de confirmación (\( accept = 1 \)) a la CPU durante un periodo de reloj. El flip-flop JK \( first \) se inicializa en 1.                |
| `3.`        | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | —                                                  | **Desempaquetado**. Si \( first = 1 \), el registro \( CR \) se carga con el carácter superior (\( DR_{10:17} \)). Si \( first = 0 \), se carga con el carácter inferior (\( DR_{1:8} \)).                                                         |
| `4.`        | \( feed = RETURN(CR) \) <br> \( print = RETURN(CR) \)                               | —                                                  | **Activación del periférico**. La función combinacional \( RETURN(CR) \) evalúa si el carácter es un retorno de carro. Activa alternativamente \( feed \) o \( print \) según corresponda.                                                         |
| `5.`        | \( Null \)                                                                          | —                                                  | **Sincronización de hardware**. Paso nulo de un periodo de reloj que concede un margen de tiempo seguro a la impresora para levantar la señal de ocupado (\( wait = 1 \)).                                                                         |
| `6.`        | —                                                                                   | \( \rightarrow (wait)/(6) \)                       | **Polling de impresión**. El control queda en espera activa ciclando sobre el paso 6 mientras la línea \( wait \) esté en alto, indicando que la impresora está ejecutando la acción física.                                                       |
| `7.`        | \( first \leftarrow 0 \)                                                            | \( \rightarrow (first, \overline{first})/(3, 1) \) | **Control de flujo por carácter**. Se borra el indicador \( first \). Basándose en su estado antes del flanco de reloj, si era 1, bifurca al paso 3 para procesar el segundo carácter; si era 0, regresa al paso 1 para esperar una nueva palabra. |
| `CHAR = CR` | \( CHAR = CR \)                                                                     | —                                                  | **Salida combinacional permanente**. Expresión combinacional fuera de secuencia que asocia directamente la salida física \( CHAR \) al registro de caracteres \( CR \) de forma continua.                                                          |




---

copiar con el puntero:
Módulo PRINTER INTERFACE (Example 9.3)MODULE: PRINTER INTERFACE
MEMORY: DR[1]; CR[2]; first(JK)
OUTPUTS: CHAR[2]; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS[1]

1. ready = 1
   -> (~datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR[10:17] & first) | (DR[1:8] & ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
END SEQUENCE
CHAR = CR
END
PasoOperaciónCondiciónEstado resultante1.$ ready = 1 $$ \rightarrow (\overline{datavalid})/(1) $Espera activa de datos. La interfaz anuncia disponibilidad mediante $ ready = 1 $1. Se mantiene en bucle cerrado en el paso 1 mientras la línea de datos válidos permanezca desactivada ($ datavalid = 0 $)1.2.$ DR \leftarrow IOBUS $ <br> $ accept = 1 $ <br> $ first \leftarrow 1 $—Captura y sincronización. El registro de datos $ DR$2$ $ captura los 18 bits del bus1. Se envía un pulso de confirmación ($ accept = 1 $) a la CPU durante un periodo de reloj1. El flip-flop JK $ first $ se inicializa en 11.3.$ CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) $—Desempaquetado. Si $ first = 1 $, el registro $ CR$3$ $ se carga con el carácter superior ($ DR_{10:17} $)1. Si $ first = 0 $, se carga con el carácter inferior ($ DR_{1:8} $)1.4.$ feed = RETURN(CR) $ <br> $ print = RETURN(CR) $—Activación del periférico. La función combinacional $ RETURN(CR) $ evalúa si el carácter es un retorno de carro1. Activa alternativamente $ feed $ o $ print $ según corresponda1.5.$ Null $—Sincronización de hardware. Paso nulo de un periodo de reloj que concede un margen de tiempo seguro a la impresora para levantar la señal de ocupado ($ wait = 1 $)1.6.—$ \rightarrow (wait)/(6) $Polling de impresión. El control queda en espera activa ciclando sobre el paso 6 mientras la línea $ wait $ esté en alto, indicando que la impresora está ejecutando la acción física1.7.$ first \leftarrow 0 $$ \rightarrow (first, \overline{first})/(3, 1) $Control de flujo por carácter. Se borra el indicador $ first $1. Basándose en su estado antes del flanco de reloj, si era 1, bifurca al paso 3 para procesar el segundo carácter1; si era 0, regresa al paso 1 para esperar una nueva palabra1.CHAR = CR$ CHAR = CR $—Salida combinacional permanente. Expresión combinacional fuera de secuencia que asocia directamente la salida física $ CHAR$3$ $ al registro de caracteres $ CR$3$ $ de forma continua1.