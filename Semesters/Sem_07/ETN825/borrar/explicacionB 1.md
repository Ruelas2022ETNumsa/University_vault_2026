# B) Explicación del programa SIC

**Idea:** la CPU envía los 1024 datos a la impresora (dispositivo #2) con **E/S programada**: antes de cada palabra pregunta si la interface está ocupada, la envía con `OD2` y repite 1024 veces.

**Datos del problema**

- $N = 1024_{10} = 2000_8$ palabras.
- El bloque de datos va de $00200_8$ a $02177_8$ (porque $00200_8 + 2000_8 - 1 = 02177_8$).
- En `00100` está el **puntero**, que apunta al dato actual. Empieza en `000200`.
- En `00101` está el **contador**, que empieza en $-1024_{10} = 776000_8$. Es negativo porque `ISZ` suma 1 y salta cuando llega a cero, así que tras 1024 incrementos se acaba solo, sin comparar.

---

**`00000` `IS2 01`:** consulta el estatus de la impresora (#2). La máscara `01` selecciona el bit $busy$. Si $busy = 1$, salta la siguiente instrucción.

**`00001` `JMP 00003`:** solo se ejecuta si $busy = 0$ (si no, fue saltada). Va a enviar el dato.

**`00002` `JMP 00000`:** solo se ejecuta si $busy = 1$. Vuelve a consultar el estatus. Es una **espera activa**: la CPU repite la pregunta hasta que la interface esté libre.

**`00003` `LAC I 00100`:** carga en $AC$ el dato al que apunta `00100` (direccionamiento indirecto). Primero lee el puntero y luego el dato que está en esa dirección.

**`00004` `OD2`:** envía $AC$ a la impresora. Aquí empieza el handshake de la interface.

**`00005` `ISZ 00100`:** suma 1 al puntero para que apunte al siguiente dato. Nunca llega a cero, así que no salta.

**`00006` `ISZ 00101`:** suma 1 al contador. Si llegó a cero, ya se enviaron las 1024 palabras y salta `00007`.

**`00007` `JMP 00000`:** se ejecuta mientras el contador no sea cero. Vuelve a consultar el estatus para enviar la siguiente palabra.

**`00010` `HLT`:** fin del programa. Se llega aquí solo cuando el contador llegó a cero.

---

> **Resumen:** el programa es un ciclo de *consultar → enviar → avanzar puntero → contar*. El puntero recorre los datos y el contador decide cuándo parar.

---

## Aclaraciones

**Por qué las direcciones están en octal**

El SIC trabaja con palabras de 18 bits, y cada dígito octal representa 3 bits, así que una dirección o dato se escribe con 6 dígitos octales. Por eso $1024_{10} = 2000_8$ y el contador negativo es $776000_8$.

**El truco de los dos `JMP`**

Las líneas `00001` y `00002` parecen contradictorias, pero funcionan juntas con el salto de `IS2`:

- Si $busy = 0$, no hay salto, así que se ejecuta `00001` y va a enviar.
- Si $busy = 1$, `IS2` salta `00001`, así que se ejecuta `00002` y vuelve a consultar.

**Puntero y contador son variables en memoria**

`00100` y `00101` son posiciones de memoria que el propio programa modifica con `ISZ`. Por eso, si se quiere ejecutar el programa **otra vez**, hay que volver a cargar `000200` y `776000` en ellas.

**Por qué el contador es negativo**

$776000_8 = 2^{18} - 1024$ es el $-1024$ en complemento a 2 de 18 bits. Sumando 1 en cada vuelta, llega a $0$ exactamente tras 1024 vueltas, y `ISZ` lo detecta sin necesitar una instrucción de comparación.

**Palabras y caracteres**

Cada palabra tiene 18 bits y guarda 2 caracteres ASCII, por eso 1024 palabras son 2048 caracteres. La interface de impresora separa los dos caracteres de cada palabra (es el trabajo de $first$ en el módulo base).

**Qué supone el programa**

- El bloque de 1024 palabras ya está cargado en la memoria, desde $00200_8$.
- No usa interrupciones ni DMA: la CPU está ocupada durante toda la impresión esperando y enviando. Eso es lo que significa "E/S programada".

**Relación con el inciso a)**

El inciso a) es el **hardware** (la interface que recibe 1K palabras) y el inciso b) es el **software** (el programa que se las envía). El bit $busy$ que consulta `IS2` es el mismo $busy$ del módulo AHPL.
