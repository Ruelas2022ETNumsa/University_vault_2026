# a) Modificar la interface para que reciba 1K de datos cada vez

---

| Identificador | Sección | Tamaño       | Rol                                                                                   |
| ------------- | ------- | ------------ | ------------------------------------------------------------------------------------- |
| `DR`          | MEMORY  | `(18)`       | Registro de datos que captura la palabra transferida desde `IOBUS`                    |
| `BUFFER`      | MEMORY  | `(1024, 18)` | Memoria RAM interna de 1024 palabras de 18 bits para almacenar el bloque de datos     |
| `cnt`         | MEMORY  | `(10)`       | Contador y puntero de dirección de 10 bits ($2^{10} = 1024$) para indexar `BUFFER`    |
| `busy`        | MEMORY  | `escalar`    | Flip-flop de estado que indica si la interfaz está procesando la recepción del bloque |
| `csrdy`       | INPUTS  | `escalar`    | Señal de entrada que indica la presencia de un comando válido en `CSBUS`              |
| `IOBUS`       | COMBUS  | `(18)`       | Bus de datos bidireccional del sistema de 18 bits                                     |
| `CSBUS`       | COMBUS  | `(12)`       | Bus de control y selección de dispositivo de 12 bits                                  |
| `ready`       | COMBUS  | `escalar`    | Línea de control que indica disponibilidad para recibir/enviar datos                  |
| `datavalid`   | COMBUS  | `escalar`    | Línea de control que valida la presencia de un dato en el bus                         |
| `accept`      | COMBUS  | `escalar`    | Línea de control de handshake que confirma la recepción del dato/comando              |

```AHPL
MODULE: INTERFACE 1K
MEMORY: DR(18); BUFFER(1024, 18); cnt(10); busy
INPUTS: csrdy
COMBUS: IOBUS(18); CSBUS(12); ready; datavalid; accept

1. -> (~ (csrdy /\ ~CSBUS(0) /\ CSBUS(1) /\ ~CSBUS(2))) / (1)
2. accept = 1
   -> (~CSBUS(3), ~CSBUS(3), CSBUS(3)) / (1, 1A, 3)
3. -> (~ready) / (3)
4. CSBUS(0) = busy; datavalid = 1
   -> (~accept, accept) / (4, 1)
1A. cnt <- 0,0,0,0,0,0,0,0,0,0; busy <- 1
2A. ready = 1
    -> (~datavalid) / (2A)
3A. DR <- IOBUS; BUFFER * DCD(cnt) <- IOBUS; accept = 1
4A. -> (datavalid) / (4A)
5A. cnt <- INC(cnt)
    -> (/\ / cnt, ~ (/\ / cnt)) / (6A, 2A)
6A. busy <- 0
7A. DEAD END
END SEQUENCE
END
```

| Paso  | Operación                                                                        | Condición                                                                                                    | Estado resultante                                                                                                                                                              |
| ----- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `1.`  | —                                                                                | $\rightarrow (\overline{csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}}}) / (1)$ | Espera activa de selección. Permanece en `1.` mientras no se direccione la interfaz (`010`) con $csrdy = 1$.                                                                   |
| `2.`  | $accept = 1$                                                                     | $\rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 1A, 3)$                           | Confirma recepción del comando. Bifurca a `3.` si es solicitud de estatus ($CSBUS_{3} = 1$) o a `1.` y `1A.` si es comando de transferencia ($CSBUS_{3} = 0$).                 |
| `3.`  | —                                                                                | $\rightarrow (\overline{ready}) / (3)$                                                                       | Espera activa de disponibilidad de la línea de control $ready$.                                                                                                                |
| `4.`  | $CSBUS_{0} = busy$ ; $datavalid = 1$                                             | $\rightarrow (\overline{accept}, accept) / (4, 1)$                                                           | Coloca el flag $busy$ en $CSBUS_{0}$ y activa $datavalid = 1$. Retorna a `1.` tras recibir $accept = 1$.                                                                       |
| `1A.` | $cnt \leftarrow 0,0,0,0,0,0,0,0,0,0$ ; $busy \leftarrow 1$ | —                                                                                                            | Inicialización de la recepción del bloque. Borra el contador $cnt$ a cero y activa el flag $busy \leftarrow 1$.                                                                |
| `2A.` | $ready = 1$                                                                      | $\rightarrow (\overline{datavalid}) / (2A)$                                                                  | Asigna $ready = 1$ para indicar disponibilidad para recibir una palabra. Bucle en `2A.` mientras $datavalid = 0$.                                                              |
| `3A.` | $DR \leftarrow IOBUS$ ; $BUFFER * DCD(cnt) \leftarrow IOBUS$ ; $accept = 1$      | —                                                                                                            | Captura la palabra de 18 bits de $IOBUS$ en $DR$ y la almacena en la posición $cnt$ de $BUFFER(1024, 18)$. Emite $accept = 1$.                                                 |
| `4A.` | —                                                                                | $\rightarrow (datavalid) / (4A)$                                                                             | Finalización del Handshake de la palabra. Espera activa mientras la CPU sostiene $datavalid = 1$.                                                                              |
| `5A.` | $cnt \leftarrow INC(cnt)$                                                        | $\rightarrow (\bigwedge / cnt, \overline{\bigwedge / cnt}) / (6A, 2A)$                                       | Incrementa el puntero de dirección. Si se completaron las 1024 palabras ($\bigwedge / cnt = 1$), avanza a `6A.`; en caso contrario, retorna a `2A.` para la siguiente palabra. |
| `6A.` | $busy \leftarrow 0$                                                              | —                                                                                                            | Finaliza la recepción del bloque actualizando el flag de estado $busy \leftarrow 0$.                                                                                           |
| `7A.` | $DEAD\ END$                                                                      | —                                                                                                            | Conclusión de la secuencia de recepción del bloque de 1K datos.                                                                                                                |
