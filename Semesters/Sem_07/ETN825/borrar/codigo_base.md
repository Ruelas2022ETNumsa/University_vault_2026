| Identificador | Sección | Tamaño    | Rol                                                                              |
| ------------- | ------- | --------- | -------------------------------------------------------------------------------- |
| `DR`          | MEMORY  | `(18)`    | Registro de datos que almacena la palabra recibida desde `IOBUS`                 |
| `CR`          | MEMORY  | `(8)`     | Registro de carácter que almacena el código ASCII a imprimir                     |
| `busy`        | MEMORY  | `escalar` | Flip-flop de estado que indica si la interfaz está ocupada procesando            |
| `first`       | MEMORY  | `escalar` | Flip-flop de control que selecciona el primer $1$ o segundo $0$ carácter de `DR` |
| `CHAR`        | OUTPUTS | `(8)`     | Bus de salida combinacional conectado al registro `CR` hacia la impresora        |
| `print`       | OUTPUTS | `escalar` | Señal de salida que activa la impresión de un carácter                           |
| `feed`        | OUTPUTS | `escalar` | Señal de salida que activa el avance de papel o retorno de carro                 |
| `wait`        | INPUTS  | `escalar` | Señal de entrada desde la impresora que indica que la mecánica está ocupada      |
| `csrdy`       | INPUTS  | `escalar` | Señal de entrada que indica la presencia de un comando en `CSBUS`                |
| `IOBUS`       | COMBUS  | `(18)`    | Bus de datos bidireccional del sistema                                           |
| `CSBUS`       | COMBUS  | `(12)`    | Bus de control y selección de dispositivo                                        |
| `ready`       | COMBUS  | `escalar` | Línea de control que indica disponibilidad para recibir/enviar datos             |
| `datavalid`   | COMBUS  | `escalar` | Línea de control que valida la presencia de un dato en el bus                    |
| `accept`      | COMBUS  | `escalar` | Línea de control de handshake que confirma la recepción del dato/comando         |

```AHPL
MODULE: PRINTER INTERFACE
MEMORY: DR(18); CR(8); busy; first
OUTPUTS: CHAR(8); print; feed
INPUTS: wait; csrdy
COMBUS: IOBUS(18); CSBUS(12); ready; datavalid; accept

1. -> ~(csrdy /\ ~CSBUS(0) /\ CSBUS(1) /\ ~CSBUS(2)) / (1)
2. accept = 1;
   -> (~CSBUS(3), ~CSBUS(3), CSBUS(3)) / (1, 1A, 3)
3. -> (~ready) / (3)
4. CSBUS(0) = busy; datavalid = 1;
   -> (~accept, accept) / (4, 1)
1A. ready = 1
    -> (~datavalid) / (1A)
2A. DR <- IOBUS; busy <- 1; accept = 1; first <- 1
3A. CR <- (DR(10:17) ! DR(1:8)) * (first, ~first)
4A. feed = RETURN(CR); print = ~RETURN(CR);
5A. Null
6A. -> (wait) / (6A)
7A. first <- 0; busy * ~first <- 0
    -> (first, ~first) / (3A, 8A)
8A. DEAD END
END SEQUENCE
CHAR = CR
END
```

| Paso | Operación | Condición | Estado resultante |
|-|-|-|-|
| `1.` | — | $\rightarrow \overline{(csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}})} / (1)$ | Espera activa de selección. Permanece en `1.` mientras no se direccione la impresora (`010`) con $csrdy = 1$. |
| `2.` | $accept = 1$ | $\rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 1A, 3)$ | Confirma recepción de comando. Bifurca a `3.` si es solicitud de estatus ($CSBUS_{3} = 1$) o a `1.` y `1A.` si es orden de salida de datos ($CSBUS_{3} = 0$). |
| `3.` | — | $\rightarrow (\overline{ready}) / (3)$ | Espera activa de disponibilidad de la línea de control $ready$. |
| `4.` | $CSBUS_{0} = busy$ ; $datavalid = 1$ | $\rightarrow (\overline{accept}, accept) / (4, 1)$ | Coloca el flag $busy$ en $CSBUS_{0}$ y activa $datavalid = 1$. Retorna a `1.` tras recibir $accept = 1$. |
| `1A.` | $ready = 1$ | $\rightarrow (\overline{datavalid}) / (1A)$ | Asigna $ready = 1$ para indicar que la interfaz está lista para recibir. Espera en `1A.` mientras $datavalid = 0$. |
| `2A.` | $DR \leftarrow IOBUS$ ; $busy \leftarrow 1$ ; $accept = 1$ ; $first \leftarrow 1$ | — | Captura la palabra de 18 bits en $DR$, activa $busy \leftarrow 1$, emite el pulso $accept = 1$ e inicializa el indicador $first \leftarrow 1$. |
| `3A.` | $CR \leftarrow (DR_{10:17} ! DR_{1:8}) * (first, \overline{first})$ | — | Desempaqueta el carácter ASCII. Si $first = 1$, extrae $DR_{10:17}$; si $first = 0$, extrae $DR_{1:8}$. |
| `4A.` | $feed = RETURN(CR)$ ; $print = \overline{RETURN(CR)}$ | — | Genera impulsos hacia la impresora: activa $feed$ si $CR$ es retorno de carro, o $print$ si es carácter imprimible. |
| `5A.` | $Null$ | — | Paso nulo de sincronización. |
| `6A.` | — | $\rightarrow (wait) / (6A)$ | Espera activa mientras la mecánica de la impresora reporta ocupado ($wait = 1$). |
| `7A.` | $first \leftarrow 0$ ; $busy * \overline{first} \leftarrow 0$ | $\rightarrow (first, \overline{first}) / (3A, 8A)$ | Borra el flip-flop $first$. Si procesó el primer carácter ($first = 1$), vuelve a `3A.` para el segundo. Si procesó el segundo ($first = 0$), apaga $busy$ y avanza a `8A.`. |
| `8A.` | $DEAD\ END$ | — | Conclusión del proceso de impresión para la palabra actual. |
