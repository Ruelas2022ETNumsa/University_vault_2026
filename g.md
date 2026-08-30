
## PRINTER INTERFACE

| Identificador | Sección | Tamaño | Rol |
| ------ | ------ | ------ | ------ |
| `DR` | MEMORY | `(18)` | Registro de datos — captura el valor de `IOBUS(18)` en el paso 2 |
| `CR` | MEMORY | `(8)` | Registro de carácter — acumula el byte extraído de `DR` |
| `first` | MEMORY | `escalar (JK)` | Flip-flop de control — indica primera (1) o segunda (0) pasada |
| `CHAR` | OUTPUTS | `(8)` | Salida de carácter a la impresora — refleja `CR` en todo momento |
| `ready` | OUTPUTS | `escalar` | Señal de disponibilidad — activa en paso 1 mientras espera dato |
| `accept` | OUTPUTS | `escalar` | Señal de aceptación — pulso de 1 ciclo en paso 2 |
| `print` | OUTPUTS | `escalar` | Comando de impresión — activo si `CR` no es retorno de carro |
| `feed` | OUTPUTS | `escalar` | Comando de avance — activo si `CR` es retorno de carro |
| `datavalid` | INPUTS | `escalar` | Indica dato válido en `IOBUS` — habilita salida del bucle en paso 1 |
| `wait` | INPUTS | `escalar` | Señal de espera de la impresora — mantiene el bucle en paso 6 |
| `IOBUS` | COMBUS | `(18)` | Bus de datos del sistema — fuente del dato capturado en `DR` |

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

| Paso        | Operación                                                                           | Condición                                          | Estado resultante                                                                                                                                                    |
| ----------- | ----------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`        | \( ready = 1 \)                                                                     | \( \rightarrow (\overline{datavalid})/(1) \)       | Espera activa. \( ready = 1 \) indica disponibilidad. Bucle mientras \( datavalid = 0 \); sale cuando \( datavalid = 1 \).                                           |
| `2.`        | \( DR \leftarrow IOBUS \); \( accept = 1 \); \( first \leftarrow 1 \)               | —                                                  | Captura simultánea al flanco de reloj. \( DR(18) \) toma el valor de \( IOBUS(18) \). \( accept = 1 \) por un ciclo. \( first \) se inicializa en 1.                 |
| `3.`        | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | —                                                  | Desempaquetado. Si \( first = 1 \): \( CR \leftarrow DR_{10:17} \). Si \( first = 0 \): \( CR \leftarrow DR_{1:8} \).                                                |
| `4.`        | \( feed = RETURN(CR) \); \( print = \overline{RETURN(CR)} \)                        | —                                                  | Evaluación combinacional. \( RETURN(CR) \) detecta si \( CR \) es retorno de carro — activa \( feed \) o \( print \) según corresponda.                              |
| `5.`        | \( Null \)                                                                          | —                                                  | Paso nulo. Sincronización — da tiempo a la impresora para levantar \( wait \).                                                                                       |
| `6.`        | —                                                                                   | \( \rightarrow (wait)/(6) \)                       | Polling. Espera mientras \( wait = 1 \); sale cuando \( wait = 0 \).                                                                                                 |
| `7.`        | \( first \leftarrow 0 \)                                                            | \( \rightarrow (first, \overline{first})/(3, 1) \) | Control de flujo. \( first \) se borra. Si \( first \) era 1 \( \rightarrow \) paso 3 (segundo carácter). Si era 0 \( \rightarrow \) paso 1 (esperar nueva palabra). |
| `CHAR = CR` | \( CHAR = CR \)                                                                     | —                                                  | Salida combinacional permanente. \( CHAR(8) \) refleja \( CR(8) \) en todo momento, fuera de la secuencia.                                                           |



---

copiar con el puntero:

PRINTER INTERFACEIdentificadorSecciónTamañoRolDRMEMORY(18)Registro de datos — captura el valor de IOBUS(18) en el paso 21CRMEMORY(8)Registro de carácter — acumula el byte extraído de DR1firstMEMORYescalar (JK)Flip-flop de control — indica primera (1) o segunda (0) pasada1CHAROUTPUTS(8)Salida de carácter a la impresora — refleja CR en todo momento1readyOUTPUTSescalarSeñal de disponibilidad — activa en paso 1 mientras espera dato1acceptOUTPUTSescalarSeñal de aceptación — pulso de 1 ciclo en paso 21printOUTPUTSescalarComando de impresión — activo si CR no es retorno de carro1feedOUTPUTSescalarComando de avance — activo si CR es retorno de carro1datavalidINPUTSescalarIndica dato válido en IOBUS — habilita salida del bucle en paso 11waitINPUTSescalarSeñal de espera de la impresora — mantiene el bucle en paso 61IOBUSCOMBUS(18)Bus de datos del sistema — fuente del dato capturado en DR1MODULE: PRINTER INTERFACE
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
PasoOperaciónCondiciónEstado resultante1.$ ready = 1 $$ \rightarrow (\overline{datavalid})/(1) $Espera activa. $ ready = 1 $ indica disponibilidad. Bucle mientras $ datavalid = 0 $; sale cuando $ datavalid = 1 $2.2.$ DR \leftarrow IOBUS $; $ accept = 1 $; $ first \leftarrow 1 $—Captura simultánea al flanco de reloj. $ DR(18) $ toma el valor de $ IOBUS(18) $. $ accept = 1 $ por un ciclo. $ first $ se inicializa en 12.3.$ CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) $—Desempaquetado. Si $ first = 1 $: $ CR \leftarrow DR_{10:17} $. Si $ first = 0 $: $ CR \leftarrow DR_{1:8} $2.4.$ feed = RETURN(CR) $; $ print = \overline{RETURN(CR)} $—Evaluación combinacional. $ RETURN(CR) $ detecta si $ CR $ es retorno de carro — activa $ feed $ o $ print $ según corresponda2.5.$ Null $—Paso nulo. Sincronización — da tiempo a la impresora para levantar $ wait $2.6.—$ \rightarrow (wait)/(6) $Polling. Espera mientras $ wait = 1 $; sale cuando $ wait = 0 $2.7.$ first \leftarrow 0 $$ \rightarrow (first, \overline{first})/(3, 1) $Control de flujo. $ first $ se borra. Si $ first $ era 1 $ \rightarrow $ paso 3 (segundo carácter). Si era 0 $ \rightarrow $ paso 1 (esperar nueva palabra)2.CHAR = CR$ CHAR = CR $—Salida combinacional permanente. $ CHAR(8) $ refleja $ CR(8) $ en todo momento, fuera de la secuencia2.