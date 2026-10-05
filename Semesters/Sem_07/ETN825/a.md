# a) Modificar la interface para que reciba 1K de datos cada vez

---

| Identificador | Sección | Tamaño | Rol |
|-|-|-|-|
| `DR` | MEMORY | `(18)` | Registro de datos que captura la palabra transferida desde `IOBUS` |
| `BUFFER` | MEMORY | `(1024, 18)` | Memoria RAM interna de 1K palabras (1024 palabras de 18 bits) para almacenar el bloque |
| `cnt` | MEMORY | `(10)` | Contador y puntero de dirección de 10 bits ($2^{10} = 1024$) para indexar `BUFFER` |
| `busy` | MEMORY | `escalar` | Flip-flop de estado que indica si la interfaz está procesando la recepción del bloque de datos |
| `ready` | COMBUSES | `escalar` | Línea de control que indica disponibilidad para recibir la siguiente palabra |
| `accept` | COMBUSES | `escalar` | Línea de control de handshake que confirma la recepción de cada palabra |
| `csrdy` | INPUTS | `escalar` | Señal de entrada de habilitación de comando en el bus de control `CSBUS` |
| `datavalid` | COMBUSES | `escalar` | Línea de control que indica la presencia de un dato válido en `IOBUS` |
| `IOBUS` | COMBUSES | `(18)` | Bus de datos del sistema de 18 bits |
| `CSBUS` | COMBUSES | `(12)` | Bus de control y selección de 12 bits |

```AHPL
MODULE: INTERFACE 1K
MEMORY: DR(18); BUFFER(1024, 18); cnt(10); busy
INPUTS: csrdy
COMBUSES: IOBUS(18); CSBUS(12); ready; datavalid; accept

1. -> ~(csrdy /\ ~CSBUS(0) /\ CSBUS(1) /\ ~CSBUS(2)) / (1)
2. accept = 1;
   -> (~CSBUS(3), ~CSBUS(3), CSBUS(3)) / (1, 1A, 3)
3. -> (~ready) / (3)
4. CSBUS(0) = busy; datavalid = 1
   -> (~accept, accept) / (4, 1)
1A. cnt <- \0,0,0,0,0,0,0,0,0,0\; busy <- 1
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

| Paso  | Operación                                                                                     | Condición                                                                                                          | Estado resultante                                                                                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`  | —                                                                                             | $\rightarrow \overline{(csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}})} / (1)$ | Espera activa de selección. Retorna a `1.` mientras no se direccione el dispositivo (`010`) con $csrdy = 1$.                                                                                |
| `2.`  | $accept = 1$                                                                            | $\rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 1A, 3)$                           | Confirma recepción del comando. Bifurca a `3.` si es solicitud de estatus ($CSBUS_{3} = 1$) o a `1.` y `1A.` si es comando de transferencia de datos ($CSBUS_{3} = 0$).               |
| `3.`  | —                                                                                             | $\rightarrow (\overline{ready}) / (3)$                                                                                  | Polling interno de disponibilidad antes de entregar estatus a la CPU.                                                                                                                             |
| `4.`  | $CSBUS_{0} = busy$ ; $datavalid = 1$                                              | $\rightarrow (\overline{accept}, accept) / (4, 1)$                                                           | Coloca el bit de estatus $busy$ en $CSBUS_{0}$ y activa $datavalid = 1$. Retorna a `1.` tras recibir la confirmación $accept = 1$.                                        |
| `1A.` | $cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash$ ; $busy \leftarrow 1$  | —                                                                                                                  | Inicialización del bloque de 1K datos. Borra el contador de dirección $cnt(10)$ a cero y activa el flag $busy \leftarrow 1$.                                                          |
| `2A.` | $ready = 1$                                                                             | $\rightarrow (\overline{datavalid}) / (2A)$                                                                  | Asigna $ready = 1$ para indicar disponibilidad de recepción. Espera activa en `2A.` mientras $datavalid = 0$.                                                                         |
| `3A.` | $DR \leftarrow IOBUS$ ; $BUFFER * DCD(cnt) \leftarrow IOBUS$ ; $accept = 1$ | —                                                                                                                  | Almacena la palabra de 18 bits de $IOBUS$ en $DR$ y en la posición direccionada por $cnt$ dentro de $BUFFER(1024, 18)$. Emite la señal de conformidad $accept = 1$. |
| `4A.` | —                                                                                             | $\rightarrow (datavalid) / (4A)$                                                                             | Finalización de Handshake. Mantiene la espera mientras la CPU/origen sostiene la señal $datavalid = 1$.                                                                                     |
| `5A.` | $cnt \leftarrow INC(cnt)$                                                               | $\rightarrow (\bigwedge / cnt, \overline{\bigwedge / cnt}) / (6A, 2A)$                                       | Incrementa el puntero de dirección. Si se completaron las 1024 palabras ($\bigwedge / cnt = 1$), avanza a `6A.`; en caso contrario, vuelve a `2A.` para recibir la siguiente palabra.       |
| `6A.` | $busy \leftarrow 0$                                                                     | —                                                                                                                  | Libera la interfaz actualizando el flag de estado $busy \leftarrow 0$.                                                                                                                      |
| `7A.` | $DEAD\ END$                                                                             | —                                                                                                                  | Conclusión de la secuencia de recepción del bloque de 1K datos.                                                                                                                                   |

