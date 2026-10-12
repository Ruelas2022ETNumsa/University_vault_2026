# a) Modificar la interface para que reciba 1K de datos cada vez e imprima lo cargado

---

## Identificadores

| Identificador | Sección | Tamaño       | Rol                                                                                               |
| ------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------- |
| `DR`          | MEMORY  | `(18)`       | Registro de datos que almacena la palabra recibida desde `IOBUS` o leída desde `BUFFER`           |
| `CR`          | MEMORY  | `(8)`        | Registro de carácter que almacena el código ASCII a enviar a la impresora                         |
| `BUFFER`      | MEMORY  | `(1024, 18)` | Memoria RAM interna de 1024 palabras de 18 bits para almacenar el bloque de datos                 |
| `cnt`         | MEMORY  | `(10)`       | Contador y puntero de dirección de 10 bits ($2^{10} = 1024$) para indexar `BUFFER`                |
| `limit`       | MEMORY  | `(10)`       | Dirección siguiente a la última palabra no vacía recibida (tope de impresión)                     |
| `empty`       | MEMORY  | `(3)`        | Contador de palabras vacías consecutivas; `empty(0) = 1` al llegar a 4                            |
| `busy`        | MEMORY  | `escalar`    | Flip-flop de estado: 1 desde que inicia la carga hasta terminar de imprimir todo el bloque        |
| `first`       | MEMORY  | `escalar`    | Selecciona el primer ($1$) o segundo ($0$) carácter ASCII de `DR`                                 |
| `has_data`    | MEMORY  | `escalar`    | Indica si se recibió al menos una palabra con texto no vacío                                      |
| `CHAR`        | OUTPUTS | `(8)`        | Bus de salida combinacional conectado a `CR` hacia la impresora                                   |
| `print`       | OUTPUTS | `escalar`    | Señal que activa la impresión de un carácter                                                      |
| `feed`        | OUTPUTS | `escalar`    | Señal que activa el avance de papel o retorno de carro                                            |
| `wait`        | INPUTS  | `escalar`    | Entrada de la impresora: la mecánica está ocupada                                                 |
| `csrdy`       | INPUTS  | `escalar`    | Entrada que indica un comando válido en `CSBUS`                                                   |
| `IOBUS`       | COMBUS  | `(18)`       | Bus de datos bidireccional del sistema                                                            |
| `CSBUS`       | COMBUS  | `(12)`       | Bus de control y selección de dispositivo                                                         |
| `ready`       | COMBUS  | `escalar`    | Línea que indica disponibilidad para recibir/enviar datos                                         |
| `datavalid`   | COMBUS  | `escalar`    | Línea que valida la presencia de un dato en el bus                                                |
| `accept`      | COMBUS  | `escalar`    | Línea de handshake que confirma la recepción del dato/comando                                     |

Palabra vacía: sus dos caracteres son NUL (`00h`), es decir `\/ / DR(10:17) \/ \/ / DR(1:8) = 0`. Umbral: 4 palabras vacías consecutivas encienden la bandera de "no más caracteres".

---

## Módulo AHPL

```AHPL
MODULE: PRINTER INTERFACE 1K
MEMORY: DR(18); CR(8); BUFFER(1024, 18); cnt(10); limit(10); empty(3); busy; first; has_data
OUTPUTS: CHAR(8); print; feed
INPUTS: wait; csrdy
COMBUS: IOBUS(18); CSBUS(12); ready; datavalid; accept

1. -> ~(csrdy /\ ~CSBUS(0) /\ CSBUS(1) /\ ~CSBUS(2)) / (1)
2. accept = 1
   -> (~CSBUS(3), ~CSBUS(3), CSBUS(3)) / (1, 1A, 3)
3. -> (~ready) / (3)
4. CSBUS(0) = busy; datavalid = 1
   -> (~accept, accept) / (4, 1)
1A. cnt <- 0,0,0,0,0,0,0,0,0,0; limit <- 0,0,0,0,0,0,0,0,0,0; empty <- 0,0,0; has_data <- 0; busy <- 1
2A. ready = 1
    -> (~datavalid) / (2A)
3A. DR <- IOBUS; BUFFER * DCD(cnt) <- IOBUS; accept = 1
4A. -> (datavalid) / (4A)
5A. has_data * (\/ / DR(10:17) \/ \/ / DR(1:8)) <- 1
    limit * (\/ / DR(10:17) \/ \/ / DR(1:8)) <- INC(cnt)
    empty * (\/ / DR(10:17) \/ \/ / DR(1:8)) <- 0,0,0
    empty * (~ (\/ / DR(10:17) \/ \/ / DR(1:8))) <- INC(empty)
6A. cnt <- INC(cnt)
    -> (empty(0) \/ (/\ / cnt), ~ (empty(0) \/ (/\ / cnt))) / (1B, 2A)
1B. cnt <- 0,0,0,0,0,0,0,0,0,0
    -> (~has_data, has_data) / (10B, 2B)
2B. DR <- BUSFN(BUFFER; DCD(cnt)); first <- 1
3B. CR <- (DR(10:17) ! DR(1:8)) * (first, ~first)
4B. feed = RETURN(CR); print = ~RETURN(CR)
5B. Null
6B. -> (wait) / (6B)
7B. first <- 0
    -> (first, ~first) / (3B, 8B)
8B. cnt <- INC(cnt)
9B. -> (cnt EQ limit, ~ (cnt EQ limit)) / (10B, 2B)
10B. busy <- 0
11B. DEAD END
END SEQUENCE
CHAR = CR
END
```

---

## Pasos

| Paso   | Operación                                                                                                                                                                                                                                                                                | Condición                                                                                  | Estado resultante                                                                                                                                                                                                   |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1.`   | —                                                                                                                                                                                                                                                                                        | $\rightarrow (\overline{csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}}}) / (1)$ | Espera de selección. Permanece en `1.` mientras no se direccione la impresora (`010`) con $csrdy = 1$.                                                                                                              |
| `2.`   | $accept = 1$                                                                                                                                                                                                                                                                             | $\rightarrow (\overline{CSBUS_{3}}, \overline{CSBUS_{3}}, CSBUS_{3}) / (1, 1A, 3)$        | Confirma el comando. Va a `3.` si es consulta de estatus ($CSBUS_{3} = 1$) o a `1.` y `1A.` si es orden de salida de datos ($CSBUS_{3} = 0$).                                                                       |
| `3.`   | —                                                                                                                                                                                                                                                                                        | $\rightarrow (\overline{ready}) / (3)$                                                     | Espera de $ready$ para responder el estatus.                                                                                                                                                                        |
| `4.`   | $CSBUS_{0} = busy$ ; $datavalid = 1$                                                                                                                                                                                                                                                     | $\rightarrow (\overline{accept}, accept) / (4, 1)$                                         | Entrega $busy$ en $CSBUS_{0}$ con $datavalid = 1$. Vuelve a `1.` al recibir $accept$.                                                                                                                               |
| `1A.`  | $cnt \leftarrow 0$ ; $limit \leftarrow 0$ ; $empty \leftarrow 0$ ; $has\_data \leftarrow 0$ ; $busy \leftarrow 1$                                                                                                                                                                        | —                                                                                          | Inicializa la fase de carga y activa $busy$.                                                                                                                                                                        |
| `2A.`  | $ready = 1$                                                                                                                                                                                                                                                                              | $\rightarrow (\overline{datavalid}) / (2A)$                                                | Indica disponibilidad para recibir una palabra. Espera mientras $datavalid = 0$.                                                                                                                                    |
| `3A.`  | $DR \leftarrow IOBUS$ ; $BUFFER * DCD(cnt) \leftarrow IOBUS$ ; $accept = 1$                                                                                                                                                                                                              | —                                                                                          | Captura la palabra en $DR$, la guarda en $BUFFER[cnt]$ y emite $accept$.                                                                                                                                            |
| `4A.`  | —                                                                                                                                                                                                                                                                                        | $\rightarrow (datavalid) / (4A)$                                                           | Cierre del handshake: espera mientras la CPU sostiene $datavalid = 1$.                                                                                                                                              |
| `5A.`  | Si $DR \neq 0$: $has\_data \leftarrow 1$ ; $limit \leftarrow INC(cnt)$ ; $empty \leftarrow 0$. Si $DR = 0$: $empty \leftarrow INC(empty)$                                                                                                                                                | —                                                                                          | Clasifica la palabra. Con texto, actualiza el tope de impresión y reinicia la cuenta de vacías. Vacía, la cuenta.                                                                                                   |
| `6A.`  | $cnt \leftarrow INC(cnt)$                                                                                                                                                                                                                                                                | $\rightarrow (empty_{0} \lor \bigwedge / cnt, \overline{empty_{0} \lor \bigwedge / cnt}) / (1B, 2A)$ | Pasa a imprimir si hay 4 vacías consecutivas (bandera de no más caracteres, $empty_{0} = 1$) o si se llenó el buffer ($\bigwedge / cnt = 1$ con el valor anterior). Si no, recibe la siguiente palabra en `2A.`. |
| `1B.`  | $cnt \leftarrow 0$                                                                                                                                                                                                                                                                       | $\rightarrow (\overline{has\_data}, has\_data) / (10B, 2B)$                                | Reinicia el puntero. Sin texto útil salta a `10B.` (no imprime nada); con texto va a `2B.`.                                                                                                                         |
| `2B.`  | $DR \leftarrow BUSFN(BUFFER; DCD(cnt))$ ; $first \leftarrow 1$                                                                                                                                                                                                                           | —                                                                                          | Lee la palabra $BUFFER[cnt]$ en $DR$ e inicia por el primer carácter.                                                                                                                                               |
| `3B.`  | $CR \leftarrow (DR_{10:17} ! DR_{1:8}) * (first, \overline{first})$                                                                                                                                                                                                                      | —                                                                                          | Desempaqueta: $DR_{10:17}$ si $first = 1$, $DR_{1:8}$ si $first = 0$.                                                                                                                                               |
| `4B.`  | $feed = RETURN(CR)$ ; $print = \overline{RETURN(CR)}$                                                                                                                                                                                                                                    | —                                                                                          | Activa $feed$ si $CR$ es retorno de carro, o $print$ si es imprimible.                                                                                                                                              |
| `5B.`  | $Null$                                                                                                                                                                                                                                                                                   | —                                                                                          | Paso nulo de sincronización para que la impresora active $wait$.                                                                                                                                                    |
| `6B.`  | —                                                                                                                                                                                                                                                                                        | $\rightarrow (wait) / (6B)$                                                                | Espera mientras la mecánica está ocupada.                                                                                                                                                           |
| `7B.`  | $first \leftarrow 0$                                                                                                                                                                                                                                                                     | $\rightarrow (first, \overline{first}) / (3B, 8B)$                                         | Si acaba de imprimir el primer carácter vuelve a `3B.` por el segundo; si fue el segundo avanza a `8B.`.                                                                                                            |
| `8B.`  | $cnt \leftarrow INC(cnt)$                                                                                                                                                                                                                                                                | —                                                                                          | Apunta a la siguiente palabra del buffer.                                                                                                                                                           |
| `9B.`  | —                                                                                                                                                                                                                                                                                        | $\rightarrow (cnt\ EQ\ limit, \overline{cnt\ EQ\ limit}) / (10B, 2B)$                     | Compara el puntero ya incrementado con $limit$. Si lo alcanzó, termina; si no, vuelve a `2B.`. Funciona también si $limit$ dio la vuelta a 0 (buffer lleno de texto).                                                |
| `10B.` | $busy \leftarrow 0$                                                                                                                                                                                                                                                                      | —                                                                                          | Libera la interface: $busy = 0$ solo cuando terminó de imprimir todo el bloque.                                                                                                                                     |
| `11B.` | $DEAD\ END$                                                                                                                                                                                                                                                                              | —                                                                                          | Fin de la secuencia del bloque.                                                                                                                                                                                     |

---

## Correcciones respecto a la respuesta de NotebookLM

- Fin de impresión: comparaba `cnt EQ limit` en el mismo paso del `INC`, con el valor viejo de `cnt`. Imprimía una palabra de más, o repetía la palabra 0 si `limit` daba la vuelta a 0. Ahora `8B.` incrementa y `9B.` compara.
- Constantes: `\0,0,0\` pasó a `0,0,0`, igual que en el AHPL base.
- Renumeración: `9B.` pasó a ser `10B.` (`busy <- 0`) y el `DEAD END` quedó en `11B.`. Los saltos de `1B.` y `9B.` apuntan a `10B.`.
- A verificar: la lectura `BUSFN(BUFFER; DCD(cnt))` contra `ahpl_diseno_sistemas_digitales.pdf`.
