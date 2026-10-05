# B) Explicación del programa SIC

**Idea:** la CPU envía los 1024 datos a la impresora (dispositivo #2) con **E/S programada**: antes de empezar pregunta si la interface está libre, envía las 1024 palabras con `OD2` y al final espera a que la interface termine de imprimir antes de detenerse.

**Datos del problema**

- $N = 1024_{10} = 2000_8$ palabras.
- El bloque de datos va de $00200_8$ a $02177_8$ (porque $00200_8 + 2000_8 - 1 = 02177_8$).
- En `00100` está el **puntero**, que apunta al dato actual. Empieza en `000200`.
- En `00101` está el **contador**, que empieza en $-1024_{10} = 776000_8$. Es negativo porque `ISZ` suma 1 y salta cuando llega a cero, así que tras 1024 incrementos se acaba solo, sin comparar.

---

## Consulta inicial de estatus

**`00000` `IS2 01`:** consulta el estatus de la impresora (#2). La máscara `01` selecciona el bit $busy$. Si $busy = 1$, salta la siguiente instrucción.

**`00001` `JMP 00003`:** solo se ejecuta si $busy = 0$ (si no, fue saltada). Va al bucle de envío.

**`00002` `JMP 00000`:** solo se ejecuta si $busy = 1$. Vuelve a consultar el estatus. Es una **espera activa**: la CPU repite la pregunta hasta que la interface esté libre.

## Bucle de envío

**`00003` `LAC I 00100`:** carga en $AC$ el dato al que apunta `00100` (direccionamiento indirecto). Primero lee el puntero y luego el dato que está en esa dirección.

**`00004` `OD2`:** envía $AC$ a la impresora. Aquí ocurre el handshake de la interface ($ready$, $datavalid$, $accept$), que sincroniza cada palabra.

**`00005` `ISZ 00100`:** suma 1 al puntero para que apunte al siguiente dato. Nunca llega a cero, así que no salta.

**`00006` `ISZ 00101`:** suma 1 al contador. Si llegó a cero, ya se enviaron las 1024 palabras y salta `00007`.

**`00007` `JMP 00003`:** se ejecuta mientras el contador no sea cero. Vuelve a `00003` para enviar la siguiente palabra, **sin consultar $busy$** (ver aclaraciones).

## Consulta final: esperar la impresión

**`00010` `IS2 01`:** consulta otra vez el estatus. Si $busy = 1$ (la interface sigue imprimiendo), salta la siguiente instrucción.

**`00011` `JMP 00013`:** solo se ejecuta si $busy = 0$: la impresión terminó y va a detener la CPU.

**`00012` `JMP 00010`:** solo se ejecuta si $busy = 1$. Repite la consulta (espera activa final).

**`00013` `HLT`:** fin del programa. Se llega aquí solo cuando el contador llegó a cero **y** la interface terminó de imprimir.

---

> **Resumen:** el programa es: *esperar interface libre → enviar 1024 palabras (cargar → `OD2` → avanzar puntero → contar) → esperar que termine de imprimir → `HLT`*. El puntero recorre los datos y el contador decide cuándo parar.

---

## Aclaraciones

**Por qué las direcciones están en octal**

El SIC trabaja con palabras de 18 bits, y cada dígito octal representa 3 bits, así que una dirección o dato se escribe con 6 dígitos octales. Por eso $1024_{10} = 2000_8$ y el contador negativo es $776000_8$.

**El truco de los dos `JMP` (inicial y final)**

Las líneas `00001`–`00002` y `00011`–`00012` parecen contradictorias, pero funcionan juntas con el salto de `IS2`:

- Si $busy = 0$, no hay salto, así que se ejecuta la primera `JMP` (avanzar).
- Si $busy = 1$, `IS2` salta esa instrucción, así que se ejecuta la segunda `JMP` y vuelve a consultar.

**Por qué $busy$ no se consulta en cada palabra**

En la interface modificada, $busy$ se pone en $1$ al recibir el comando y se mantiene en $1$ mientras se recibe el bloque. Si el programa consultara $busy$ antes de cada palabra, después de la primera vería $busy = 1$ y se quedaría esperando para siempre. Por eso se consulta una sola vez al inicio. Dentro del bucle, la sincronización palabra a palabra la hace el handshake de bus de `OD2`.

**Por qué hay una consulta final**

Sin ella, la CPU podría ejecutar `HLT` apenas enviada la última palabra, mientras la interface todavía imprime. Con la consulta final, el `HLT` solo se ejecuta cuando $busy = 0$.

**Puntero y contador son variables en memoria**

`00100` y `00101` son posiciones de memoria que el propio programa modifica con `ISZ`. Por eso, si se quiere ejecutar el programa **otra vez**, hay que volver a cargar `000200` y `776000` en ellas.

**Por qué el contador es negativo**

$776000_8 = 2^{18} - 1024$ es el $-1024$ en complemento a 2 de 18 bits. Sumando 1 en cada vuelta, llega a $0$ exactamente tras 1024 vueltas, y `ISZ` lo detecta sin necesitar una instrucción de comparación.

**Palabras y caracteres**

Cada palabra tiene 18 bits y guarda 2 caracteres ASCII, por eso 1024 palabras son 2048 caracteres. La impresión la hace la interface: separa los dos caracteres de cada palabra y los manda a la impresora con $print$ o $feed$ (es el trabajo de $first$ en el módulo base). El programa SIC solo entrega las palabras y espera a que termine.

**Qué supone el programa**

- El bloque de 1024 palabras ya está cargado en la memoria, desde $00200_8$.
- $busy$ baja a $0$ solo cuando la interface terminó de imprimir el bloque. Esto depende de que el inciso a) incluya la fase de impresión antes de apagar $busy$.
- No usa interrupciones ni DMA: la CPU está ocupada durante toda la impresión esperando y enviando. Eso es lo que significa "E/S programada".

**Relación con el inciso a)**

El inciso a) es el **hardware** (la interface que recibe 1K palabras) y el inciso b) es el **software** (el programa que se las envía). El bit $busy$ que consulta `IS2` es el mismo $busy$ del módulo AHPL.

**`IS2`, `ISZ` y `HLT`**

- **`IS2`:** lee el estatus del dispositivo y evalúa el bit de la máscara. Si vale $1$ salta la instrucción siguiente; si vale $0$ no salta.
- **`ISZ`:** incrementa en 1 la posición de memoria indicada. Si el resultado es cero salta la instrucción siguiente; si no, continúa en secuencia.
- **`HLT`:** detiene la CPU.
