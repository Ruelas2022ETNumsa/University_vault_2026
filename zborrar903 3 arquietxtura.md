# Arquitectura del programa P3A.asm

## Descripción general

El programa lee una cadena de caracteres ingresada por el usuario y muestra en pantalla únicamente los caracteres ubicados en posiciones de índice impar (1, 3, 5, …). Todo el acceso a hardware se realiza sin interrupciones: la entrada se obtiene del buffer de teclado del BIOS leyendo directamente memoria, y la salida se escribe directamente en la memoria de video.

---

## Organización en memoria

El programa ocupa tres segmentos físicos en memoria real:

```
[ pila  ]  segmento de pila     — 128 bytes (64 words)
[ datos ]  segmento de datos    — variables, buffers y etiquetas de texto
[ codigo]  segmento de código   — procedimientos ejecutables
```

El registro `DS` apunta a `datos` durante toda la ejecución. El registro `ES` apunta a `0B800h` (video) durante toda la ejecución, con la única excepción del interior de `LeerCadena`, donde se redirige temporalmente a `0040h` (BDA) para leer el teclado y se restaura a video antes de escribir el eco.

---

## Segmento de datos

### Constantes (EQU — no ocupan memoria)

|Nombre|Valor|Uso|
|---|---|---|
|`MAX_CADENA`|80|Límite máximo de caracteres que puede ingresar el usuario. Define el tamaño de ambos buffers.|
|`COLS`|80|Columnas de la pantalla. Se usa para calcular el offset de cada fila en video.|
|`ATRI`|07h|Atributo de video: texto gris claro sobre fondo negro. Se aplica a cada celda escrita en B800h.|
|`POS_LBL1`|0|Offset en B800h de la fila 0. Aquí se imprime la etiqueta "Cadena original:".|
|`POS_IN`|160|Offset en B800h de la fila 1. Aquí se muestra el eco del teclado mientras el usuario escribe.|
|`POS_LBL2`|480|Offset en B800h de la fila 3. Aquí se imprime la etiqueta "Resultado:".|
|`POS_OUT`|640|Offset en B800h de la fila 4. Aquí se imprime `cadena_salida`.|
|`LEN_LBL1`|calculado|Longitud en bytes de `label1`, calculada en tiempo de ensamblado con `$ - label1`.|
|`LEN_LBL2`|calculado|Longitud en bytes de `label2`, calculada en tiempo de ensamblado con `$ - label2`.|

### Variables (DB/DW — ocupan memoria en el segmento datos)

|Nombre|Tipo|Uso|
|---|---|---|
|`cadena_entrada`|DB 80 DUP|Buffer donde `LeerCadena` almacena cada carácter leído del teclado. Se llena byte a byte.|
|`cadena_salida`|DB 80 DUP|Buffer donde `ProcesarCadena` escribe el resultado. Contiene solo los caracteres de índice impar.|
|`tam_in`|DW|Cantidad real de caracteres ingresados por el usuario. La escribe `LeerCadena` al detectar ENTER. La lee `ProcesarCadena` para saber hasta dónde recorrer `cadena_entrada`.|
|`tam_out`|DW|Cantidad de caracteres copiados a `cadena_salida`. La escribe `ProcesarCadena`. La lee `program` para pasarla a `ImprimirTexto`.|
|`label1`|DB|Texto fijo `'Cadena original:'` impreso en fila 0 antes de que el usuario escriba.|
|`label2`|DB|Texto fijo `'Resultado:'` impreso en fila 3 antes de mostrar la salida.|

---

## Segmento de código — procedimientos

### `program`

Procedimiento principal `FAR`. Inicializa los segmentos, establece el orden de ejecución y termina el programa. No implementa lógica propia: delega todo en los cuatro procedimientos auxiliares. Consultar diagrama de flujo `program`.

Registros que establece y mantienen su valor durante toda la ejecución:

- `DS` → segmento `datos`
- `ES` → `0B800h` (video), salvo durante el interior de `LeerCadena`

---

### `LimpiarPantalla`

Escribe el carácter espacio con atributo `07h` en las 2000 celdas de la pantalla (80 × 25). Usa `REP STOSW` para escribir un word por celda en una sola pasada. No recibe parámetros; depende de que `ES` ya apunte a `0B800h`. Consultar diagrama de flujo `LimpiarPantalla`.

---

### `ImprimirTexto`

Procedimiento genérico de escritura en video. Recibe una cadena en `DS:SI`, su longitud en `CX`, y la posición destino en video en `DI`. Por cada carácter carga el byte con `LODSB` y lo escribe junto al atributo `ATRI` con `STOSW`. Es invocado cuatro veces desde `program`: para `label1`, para el eco de `cadena_entrada` (indirectamente via `LeerCadena`), para `label2` y para `cadena_salida`. Consultar diagrama de flujo `ImprimirTexto`.

---

### `LeerCadena`

Captura la entrada del usuario sin usar interrupciones. Accede al buffer circular de teclado que el BIOS mantiene en el segmento `0040h` de la BIOS Data Area (BDA). El mecanismo es el siguiente: el BIOS escribe cada tecla presionada como un word `(scancode | ASCII)` en el buffer y avanza el puntero `TAIL`; el programa lee ese word desde `HEAD` y avanza `HEAD` para indicar que el dato fue consumido. Mientras `HEAD == TAIL` el buffer está vacío y el procedimiento espera.

Para acceder al BDA sin alterar `DS` (que debe permanecer en `datos`), se redirige `ES` temporalmente a `0040h`. Una vez leído el carácter, `ES` se restaura a `0B800h` antes de escribir el eco en video.

El procedimiento termina cuando detecta ENTER (`AL = 0Dh`) y almacena el conteo final en `tam_in`. Consultar diagrama de flujo `LeerCadena`.

Registros usados internamente:

- `BX` — puntero de escritura en `cadena_entrada`
- `CX` — contador de caracteres leídos
- `BP` — posición actual del eco en video (offset dentro de B800h)
- `SI` — puntero al slot del buffer circular al leer del BDA
- `ES` — alterna entre `0040h` (BDA) y `0B800h` (video)

---

### `ProcesarCadena`

Recorre `cadena_entrada` y copia a `cadena_salida` únicamente los caracteres de índice impar. La estrategia es posicionar `SI` en `cadena_entrada + 1` (índice 1) y avanzar de dos en dos: `LODSB` carga el carácter impar y avanza `SI` en 1; el `INC SI` siguiente salta el carácter par. El número de iteraciones se calcula como `tam_in / 2` (con `SHR CX, 1`); el `ADC CX, 0` posterior suma el carry para no perder el último índice impar cuando `tam_in` es impar.

La escritura en `cadena_salida` se hace con `MOV [DI], AL` en lugar de `STOSB` porque `ES` apunta a video y `STOSB` usaría `ES:DI`, sobreescribiendo B800h en lugar de los datos. Al finalizar escribe el conteo en `tam_out`. Consultar diagrama de flujo `ProcesarCadena`.

---

## Mapa de uso de ES durante la ejecución

`ES` es el registro con más movimiento en el programa. Este es su estado en cada etapa:

```
program inicio          ES = 0B800h  (video)
LimpiarPantalla         ES = 0B800h
ImprimirTexto (label1)  ES = 0B800h
LeerCadena
  bucle espera teclado  ES = 0040h   (BDA, temporal)
  tras leer cada char   ES = 0B800h  (restaurado)
  eco en video          ES = 0B800h
ProcesarCadena          ES = 0B800h  (no se usa)
ImprimirTexto (label2)  ES = 0B800h
ImprimirTexto (salida)  ES = 0B800h
```

---

## Restricciones de diseño aplicadas

- Sin `INT 10h`: el video se maneja escribiendo directamente en `0B800h`.
- Sin `INT 16h`: el teclado se lee directamente del buffer circular del BDA en `0040h`.
- Sin terminadores en cadenas: la longitud siempre se maneja explícitamente via `tam_in` y `tam_out` o mediante constantes calculadas en tiempo de ensamblado (`LEN_LBL1`, `LEN_LBL2`).
- `STOSB` no se usa en `ProcesarCadena` porque `ES` no apunta a `datos` sino a video.