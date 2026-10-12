| Identificador | Sección | Tamaño       | Rol                                                                                               |
| ------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------- |
| `DR`          | MEMORY  | `(18)`       | Registro de datos que almacena la palabra recibida desde `IOBUS` o leída desde `BUFFER`           |
| `CR`          | MEMORY  | `(8)`        | Registro de carácter que almacena el código ASCII a enviar a la impresora                         |
| `BUFFER`      | MEMORY  | `(1024, 18)` | Memoria RAM interna de 1024 palabras de 18 bits para almacenar el bloque de datos                 |
| `cnt`         | MEMORY  | `(10)`       | Contador y puntero de dirección de 10 bits ($2^{10} = 1024$) para indexar `BUFFER`                |
| `limit`       | MEMORY  | `(10)`       | Registro de 10 bits que guarda la dirección siguiente a la última palabra no vacía recibida       |
| `empty`       | MEMORY  | `(3)`        | Contador de 3 bits para registrar hasta 4 palabras vacías consecutivas                            |
| `busy`        | MEMORY  | `escalar`    | Flip-flop de estado que indica si la interfaz está procesando la recepción o impresión del bloque |
| `first`       | MEMORY  | `escalar`    | Flip-flop de control que selecciona el primer ($1$) o segundo ($0$) carácter ASCII en `DR`        |
| `has_data`    | MEMORY  | `escalar`    | Flip-flop de estado que indica si se recibió al menos una palabra con texto útil no vacío         |
| `end_print`   | MEMORY  | `escalar`    | Flip-flop de estado que indica la llegada a la dirección límite de impresión                      |
| `CHAR`        | OUTPUTS | `(8)`        | Bus de salida combinacional conectado a `CR` hacia la impresora                                   |
| `print`       | OUTPUTS | `escalar`    | Señal de salida que activa la impresión de un carácter en la impresora                            |
| `feed`        | OUTPUTS | `escalar`    | Señal de salida que activa el avance de papel o retorno de carro                                  |
| `wait`        | INPUTS  | `escalar`    | Señal de entrada desde la impresora que indica que la mecánica está ocupada                       |
| `csrdy`       | INPUTS  | `escalar`    | Señal de entrada que indica la presencia de un comando válido en `CSBUS`                          |
| `IOBUS`       | COMBUS  | `(18)`       | Bus de datos bidireccional del sistema de 18 bits                                                 |
| `CSBUS`       | COMBUS  | `(12)`       | Bus de control y selección de dispositivo de 12 bits                                              |
| `ready`       | COMBUS  | `escalar`    | Línea de control que indica disponibilidad para recibir/enviar datos                              |
| `datavalid`   | COMBUS  | `escalar`    | Línea de control que valida la presencia de un dato en el bus                                     |
| `accept`      | COMBUS  | `escalar`    | Línea de control de handshake que confirma la recepción del dato/comando                          |

```AHPL
MODULE: PRINTER INTERFACE 1K
MEMORY: DR(18); CR(8); BUFFER(1024, 18); cnt(10); limit(10); empty(3); busy; first; has_data; end_print
OUTPUTS: CHAR(8); print; feed
INPUTS: wait; csrdy
COMBUS: IOBUS(18); CSBUS(12); ready; datavalid; accept

1. -> ~(csrdy /\ ~CSBUS(0) /\ CSBUS(1) /\ ~CSBUS(2)) / (1)
2. accept = 1
   -> (~CSBUS(3), ~CSBUS(3), CSBUS(3)) / (1, 1A, 3)
3. -> (~ready) / (3)
4. CSBUS(0) = busy; datavalid = 1
   -> (~accept, accept) / (4, 1)
1A. cnt <- \0,0,0,0,0,0,0,0,0,0\; empty <- \0,0,0\; limit <- \0,0,0,0,0,0,0,0,0,0\; has_data <- 0; busy <- 1
2A. ready = 1
    -> (~datavalid) / (2A)
3A. DR <- IOBUS; BUFFER * DCD(cnt) <- IOBUS; accept = 1
4A. accept = 1
    -> (datavalid) / (4A)
5A. -> (\/ / DR(10:17) \/ \/ / DR(1:8), ~ (\/ / DR(10:17) \/ \/ / DR(1:8))) / (6A, 7A)
6A. has_data <- 1; limit <- INC(cnt); empty <- \0,0,0\
    -> (8A)
7A. empty <- INC(empty)
    -> (8A)
8A. cnt <- INC(cnt)
    -> (empty(0) \/ (/\ / cnt), ~ (empty(0) \/ (/\ / cnt))) / (1B, 2A)
1B. cnt <- \0,0,0,0,0,0,0,0,0,0\
    -> (~has_data, has_data) / (11B, 2B)
2B. DR <- BUSFN(BUFFER; DCD(cnt)); first <- 1
3B. CR <- (DR(10:17) ! DR(1:8)) * (first, ~first)
4B. feed = RETURN(CR); print = ~RETURN(CR)
5B. Null
6B. -> (wait) / (6B)
7B. first <- 0
    -> (first, ~first) / (3B, 8B)
8B. cnt <- INC(cnt)
9B. end_print <- /\ / ~(cnt @ limit)
10B. -> (end_print, ~end_print) / (11B, 2B)
11B. busy <- 0
12B. DEAD END
END SEQUENCE
CHAR = CR
END
```

| Paso | Operación | Condición | Estado resultante |
|-|-|-|-|
| `1.` | — | $\rightarrow (\overline{csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}}}) / (1)$ | Espera activa de selección. Permanece en `1.` mientras no se direccione la impresora (`010`) con $csrdy = 1$. |
| `2.` | $accept = 1$ | $\rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 1A, 3)$ | Confirma recepción del comando. Bifurca a `3.` si es consulta de estatus ($CSBUS_{3} = 1$) o a `1.` y `1A.` si es orden de salida de datos ($CSBUS_{3} = 0$). |
| `3.` | — | $\rightarrow (\overline{ready}) / (3)$ | Espera activa de disponibilidad de la línea de control $ready$. |
| `4.` | $CSBUS_{0} = busy$ ; $datavalid = 1$ | $\rightarrow (\overline{accept}, accept) / (4, 1)$ | Coloca el flag $busy$ en $CSBUS_{0}$ y activa $datavalid = 1$. Retorna a `1.` tras recibir $accept = 1$. |
| `1A.` | $cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash$ ; $empty \leftarrow \backslash 0,0,0 \backslash$ ; $limit \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash$ ; $has\_data \leftarrow 0$ ; $busy \leftarrow 1$ | — | Inicialización de la fase de carga. Reinicia punteros, contadores y el indicador de datos útiles, y activa $busy \leftarrow 1$. |
| `2A.` | $ready = 1$ | $\rightarrow (\overline{datavalid}) / (2A)$ | Asigna $ready = 1$ para indicar disponibilidad para recibir una palabra desde la CPU. Espera activa en `2A.` mientras $datavalid = 0$. |
| `3A.` | $DR \leftarrow IOBUS$ ; $BUFFER * DCD(cnt) \leftarrow IOBUS$ ; $accept = 1$ | — | Captura la palabra de 18 bits en $DR$ y la almacena en la posición $cnt$ de $BUFFER$. Emite el pulso $accept = 1$. |
| `4A.` | $accept = 1$ | $\rightarrow (datavalid) / (4A)$ | Mantiene $accept = 1$ y realiza espera activa hasta que $datavalid$ baje a 0 antes de proceder con la evaluación y solicitar la siguiente palabra. |
| `5A.` | — | $\rightarrow (\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}, \overline{\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}}) / (6A, 7A)$ | Evalúa si la palabra contiene caracteres ASCII no nulos. Bifurca a `6A` si contiene texto útil o a `7A` si ambos caracteres son nulos (`00`). |
| `6A.` | $has\_data \leftarrow 1$ ; $limit \leftarrow INC(cnt)$ ; $empty \leftarrow \backslash 0,0,0 \backslash$ | $\rightarrow (8A)$ | Registra la presencia de texto útil, guarda la dirección límite siguiente $INC(cnt)$ en $limit$ y reinicia el contador de palabras vacías. |
| `7A.` | $empty \leftarrow INC(empty)$ | $\rightarrow (8A)$ | Incrementa en 1 el contador de palabras vacías consecutivas. |
| `8A.` | $cnt \leftarrow INC(cnt)$ | $\rightarrow (empty_{0} \lor \bigwedge / cnt, \overline{empty_{0} \lor \bigwedge / cnt}) / (1B, 2A)$ | Incrementa el puntero $cnt$. Pasa a la impresión (`1B`) si se acumularon 4 palabras vacías ($empty_{0} = 1$) o si se enviaron las 1024 palabras ($\bigwedge / cnt = 1$ en el valor previo a la transferencia); si no, retorna a `2A.`. |
| `1B.` | $cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash$ | $\rightarrow (\overline{has\_data}, has\_data) / (11B, 2B)$ | Reinicia $cnt$ a cero. Si no llegó texto útil ($has\_data = 0$), salta directamente a liberar la interfaz (`11B`); si llegó texto, inicia la impresión (`2B`). |
| `2B.` | $DR \leftarrow BUSFN(BUFFER; DCD(cnt))$ ; $first \leftarrow 1$ | — | Lee la palabra de `BUFFER` direccionada por $cnt$ mediante la función combinacional de bus hacia $DR$ e inicializa $first \leftarrow 1$. |
| `3B.` | $CR \leftarrow (DR_{10:17} ! DR_{1:8}) * (first, \overline{first})$ | — | Desempaqueta el carácter ASCII de 8 bits. Extrae $DR_{10:17}$ si $first = 1$ o $DR_{1:8}$ si $first = 0$. |
| `4B.` | $feed = RETURN(CR)$ ; $print = \overline{RETURN(CR)}$ | — | Genera los impulsos hacia la impresora: activa $feed$ si $CR$ es retorno de carro o $print$ si es carácter imprimible. |
| `5B.` | $Null$ | — | Paso nulo de sincronización para dar tiempo a la impresora física a levantar la señal $wait$. |
| `6B.` | — | $\rightarrow (wait) / (6B)$ | Espera activa mientras la impresora física reporte estado ocupado ($wait = 1$). |
| `7B.` | $first \leftarrow 0$ | $\rightarrow (first, \overline{first}) / (3B, 8B)$ | Limpia $first$. Si imprimió el primer carácter ($first = 1$), vuelve a `3B.` para el segundo. Si imprimió el segundo ($first = 0$), avanza a `8B.`. |
| `8B.` | $cnt \leftarrow INC(cnt)$ | — | Incrementa el puntero de palabra $cnt$. |
| `9B.` | $end\_print \leftarrow \bigwedge / \overline{cnt \oplus limit}$ | — | Evalúa la igualdad bit a bit entre el nuevo valor de $cnt$ e $limit$ usando lógica combinacional XNOR ($\sim (cnt @ limit)$) y reducción AND ($/\setminus$), almacenando el resultado en $end\_print$. |
| `10B.` | — | $\rightarrow (end\_print, \overline{end\_print}) / (11B, 2B)$ | Bifurca a `11B` para finalizar si se alcanzó el límite ($end\_print = 1$); de lo contrario, retorna a `2B` para leer la siguiente palabra. |
| `11B.` | $busy \leftarrow 0$ | — | Apaga el flag de estado $busy \leftarrow 0$ indicando la conclusión de la operación. |
| `12B.` | $DEAD\ END$ | — | Conclusión de la secuencia del módulo. |

---

### Lista de notaciones AHPL utilizadas y citas

1. **Escritura en arreglo RAM (`BUFFER * DCD(cnt) <- IOBUS`):**
   - Cita: *Hill & Peterson Digital Systems 2ª ed.* / *ahpl_diseno_sistemas_digitales.pdf*, Sección "Manejo de Arreglos de Memoria en AHPL", p. 28.

2. **Lectura de arreglo RAM (`DR <- BUSFN(BUFFER; DCD(cnt))`):**
   - Cita: *Hill & Peterson Digital Systems 2ª ed.* / *ahpl_diseno_sistemas_digitales.pdf*, Sección "Manejo de Arreglos de Memoria en AHPL", p. 29.

3. **Constantes vectoriales $`\0,0,0,0,0,0,0,0,0,0\`, `\0,0,0\`$:**
   - Cita: *AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales.pdf*, Diapositiva "AHPL SYNTAX".

4. **Operador de reducción OR (`\/ / DR(10:17)`):**
   - Cita: *AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales.pdf*, Diapositiva "OPERATORS".

5. **Operador de reducción AND $`/\ / cnt`, `/\ / ~(cnt @ limit)`$:**
   - Cita: *AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales.pdf*, Diapositiva "OPERATORS".

6. **Función estándar de incremento (`INC(cnt)`):**
   - Cita: *AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales.pdf*, Diapositiva "Standard Function in AHPL".

7. **Operador XOR bit a bit (`@`):**
   - Cita: No se encuentra explicitado el símbolo `@` en los archivos PDF/slides cargados (las fuentes emplean la notación `⊕` o la función `EXOR`). Se utiliza `@` por ser la representación estándar en texto plano/ASCII de la operación XOR en AHPL.
