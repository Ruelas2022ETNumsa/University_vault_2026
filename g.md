## Módulo PRINTER INTERFACE (Example 9.3)

| Identificador | Sección | Tamaño | Rol |
| :--- | :--- | :--- | :--- |
| `DR` | MEMORY | `(18)` | Registro de datos — captura el valor de `IOBUS(18)` en el paso 2. |
| `CR` | MEMORY | `(8)` | Registro de carácter — acumula el byte extraído de `DR`. |
| `first` | MEMORY | escalar | Flip-flop de control (tipo JK) — indica primera (1) o segunda (0) pasada. |
| `CHAR` | OUTPUTS | `(8)` | Salida de carácter a la impresora — refleja `CR` en todo momento. |
| `ready` | OUTPUTS | escalar | Señal de disponibilidad — activa en paso 1 mientras espera dato. |
| `accept` | OUTPUTS | escalar | Señal de aceptación — pulso de 1 ciclo en paso 2. |
| `print` | OUTPUTS | escalar | Comando de impresión — activo si `CR` no es retorno de carro. |
| `feed` | OUTPUTS | escalar | Comando de avance — activo si `CR` es retorno de carro. |
| `datavalid` | INPUTS | escalar | Indica dato válido en `IOBUS` — habilita salida del bucle en paso 1. |
| `wait` | INPUTS | escalar | Señal de espera de la impresora — mantiene el bucle en paso 6. |
| `IOBUS` | COMBUS | `(18)` | Bus de datos del sistema — fuente del dato capturado en `DR`. |

```ahpl
MODULE: PRINTER INTERFACE
MEMORY: DR(18); CR(8); first
OUTPUTS: CHAR(8); ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS(18)

1. ready = 1
   → (~datavalid)/(1)
2. DR ← IOBUS; accept = 1; first ← 1
3. CR ← (DR(10:17) & first) | (DR(1:8) & ~first)
4. feed = RETURN(CR); print = ~RETURN(CR)
5. Null
6. → (wait)/(6)
7. first ← 0
   → (first, ~first)/(3, 1)
8. DEAD END
END SEQUENCE
CHAR = CR
END
```

| Paso        | Operación                                                                           | Condición                                          | Estado resultante / Explicación                                                                                                                                                                                                                                      |
| :---------- | :---------------------------------------------------------------------------------- | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`        | \( ready = 1 \)                                                                     | \( \rightarrow (\overline{datavalid})/(1) \)       | **Espera activa (Polling)**. Se mantiene la señal \( ready = 1 \) para indicar disponibilidad al CPU. Mientras \( datavalid = 0 \), el control permanece en este paso; al recibir \( datavalid = 1 \), avanza al paso 2.                                             |
| `2.`        | \( DR \leftarrow IOBUS \); \( accept = 1 \); \( first \leftarrow 1 \)               | —                                                  | **Captura de datos e inicialización**. Al flanco de reloj, se carga la palabra completa de 18 bits de \( IOBUS \) en \( DR \), se genera un pulso de un ciclo en \( accept = 1 \) para confirmar la recepción al CPU, y se inicializa el flip-flop \( first \) en 1. |
| `3.`        | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | —                                                  | **Desempaquetado (Demultiplexación)**. Si \( first = 1 \), se transfiere el primer carácter \( DR_{10:17} \) a \( CR \). Si \( first = 0 \), se transfiere el segundo carácter \( DR_{1:8} \) a \( CR \).                                                            |
| `4.`        | \( feed = RETURN(CR) \); \( print = \overline{RETURN(CR)} \)                        | —                                                  | **Activación de comandos**. La unidad combinacional \( RETURN(CR) \) evalúa el carácter en \( CR \). Si es retorno de carro, activa \( feed = 1 \). De lo contrario, activa la señal de impresión \( print = 1 \).                                                   |
| `5.`        | \( Null \)                                                                          | —                                                  | **Retardo de sincronización**. Paso nulo de un ciclo de reloj para dar tiempo a que la impresora responda y establezca la señal \( wait \).                                                                                                                          |
| `6.`        | —                                                                                   | \( \rightarrow (wait)/(6) \)                       | **Espera de finalización (Polling)**. Bucle de espera activa sobre la línea \( wait \). El control permanece retenido en este paso hasta que la impresora termine la operación física (\( wait = 0 \)).                                                              |
| `7.`        | \( first \leftarrow 0 \)                                                            | \( \rightarrow (first, \overline{first})/(3, 1) \) | **Control de bucle**. Se borra el flip-flop \( first \). El estado del flip-flop se evalúa antes de la transición de reloj: si era 1, bifurca al paso 3 para procesar el segundo carácter; si era 0, retorna al paso 1 para esperar una nueva palabra de datos.      |
| `8.`        | \( DEAD\ END \)                                                                     | —                                                  | **Fin de secuencia**. Detiene el secuenciador de control en un estado de parada.                                                                                                                                                                                     |
| `CHAR = CR` | \( CHAR = CR \)                                                                     | —                                                  | **Salida combinacional permanente**. Conexión directa fuera de la secuencia de control: la salida \( CHAR(8) \) refleja continuamente el valor del registro \( CR(8) \) sin depender del reloj.                                                                      |