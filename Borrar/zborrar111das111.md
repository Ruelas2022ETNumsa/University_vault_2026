# Arquitectura — P1.asm · Clasificador de IP por clase

**Plataforma:** MASM 5.0 / Intel 8086 / Modo real / DOSBox  
**Entrada:** IP escrita por el usuario en teclado  
**Salida:** Clase A, Clase B, Clase C o Sub-red por consola DOS

---

## 1. Estructura de segmentos

El programa sigue el modelo clásico de tres segmentos explícitos de MASM:

|Segmento|Atributos|Registro|Contenido|
|---|---|---|---|
|`pila`|`PARA STACK 'STACK'`|SS|64 palabras (128 bytes) reservadas para la pila de llamadas|
|`datos`|`PARA 'DATA'`|DS|Buffer de entrada + todos los mensajes de texto|
|`codigo`|`PUBLIC 'CODE'`|CS|Único procedimiento `program PROC FAR`|

> `ASSUME SS:pila, DS:datos, CS:codigo` informa al ensamblador qué segmento usa cada registro, pero **DS hay que cargarlo a mano** en el prólogo porque el CPU no lo inicializa solo. SS y CS los configura el loader del DOS.

---

## 2. Variables del segmento `datos`

### 2.1 Buffer de entrada — estructura para INT 21h/0Ah

Los tres campos forman una **estructura posicional contigua**. INT 21h función 0Ah recibe un único puntero y navega los campos por posición fija: byte 0 = límite, byte 1 = conteo, byte 2 en adelante = datos. Si hubiera cualquier hueco entre ellos la función leería basura.

|Variable|Tipo|Offset|Propósito|
|---|---|---|---|
|`buf_max`|`DB 15`|0000h|Máximo de caracteres que leerá DOS. Vale 15 porque la IP más larga posible es `255.255.255.255` (15 chars).|
|`buf_len`|`DB 0`|0001h|DOS escribe aquí cuántos caracteres leyó realmente. El programa no la usa directamente; el parser se detiene solo al encontrar los centinelas.|
|`buf_dat`|`DB 15 DUP(0)`|0002h|Zona donde DOS deposita los caracteres tecleados. El último byte que escribe DOS es siempre un `CR` (0Dh), de ahí que el parser lo chequee como centinela de fin.|

### 2.2 Mensajes de salida

Todos terminan en `'$'`, que es el terminador requerido por INT 21h función 09h. Si terminaran en `0` como cadenas C, la función 09h imprimiría basura hasta encontrar un `$` por casualidad.

|Variable|Contenido|Bytes|Cuándo se usa|
|---|---|---|---|
|`msg_prompt`|`'Ingrese una direccion IP: $'`|26|Antes de leer el teclado|
|`msg_newline`|`0Dh, 0Ah, '$'`|3|CR+LF que separa el prompt del resultado|
|`msg_a`|`'Clase A$'`|8|Primer octeto 1–127|
|`msg_b`|`'Clase B$'`|8|Primer octeto 128–191|
|`msg_c`|`'Clase C$'`|8|Primer octeto 192–223|
|`msg_s`|`'Sub-red$'`|8|Primer octeto 224–255|

---

## 3. Registros utilizados

|Registro|Rol durante la ejecución|
|---|---|
|`AX`|Triple uso: (1) carga del segmento `datos` en el prólogo, (2) acumulador del octeto durante el parser (`AX = AX×10 + dígito`), (3) operando de los `CMP` en la clasificación. En la salida, `AH = 09h` es la función de INT 21h.|
|`BX`|Doble uso: durante el parser `BL` recibe el byte leído de `buf_dat` y se le resta `'0'`; durante la clasificación `BX` recibe la dirección del mensaje elegido (`LEA BX, msg_x`) y la transfiere a `DX` en la salida.|
|`CX`|Constante `10` para `MUL CX` dentro del bucle del parser.|
|`DX`|Puntero a string para INT 21h/09h y puntero a buffer para INT 21h/0Ah. En la salida recibe el valor de `BX` (`MOV DX, BX`).|
|`SI`|Puntero de lectura sobre `buf_dat`. Se inicializa con `LEA SI, buf_dat` y avanza con `INC SI` en cada iteración del bucle.|
|`DS`|Segmento base para todos los accesos a `datos`. Se carga una vez en el prólogo y no cambia.|

---

## 4. Algoritmo A — parser ASCII a número binario

**Propósito:** convertir los dígitos del primer octeto de la IP (que llegan como caracteres ASCII desde el teclado) en un número entero de 8086 que pueda compararse directamente.

**Por qué no se usa `AAM`:** `AAM` divide `AX` por 10 y es útil para el sentido inverso (número → BCD). Para construir el número desde texto se necesita multiplicar, no dividir.

```
acumulador = 0
para cada byte en buf_dat:
    si byte == '.' o CR o 0  → salir
    acumulador = acumulador × 10
    acumulador = acumulador + (byte − '0')
```

**Traza con `'1','9','2','.'`:**

|Iteración|byte|byte − '0'|AX antes ×10|AX final|
|---|---|---|---|---|
|1|'1'|1|0|1|
|2|'9'|9|10|19|
|3|'2'|2|190|192|
|4|'.'|—|sale del bucle|**192**|

**Por qué tres centinelas (`'.'`, `0Dh`, `0`):**  
Una IP de un solo octeto como `'10'` no tiene punto; el único terminador que DOS pone al final del buffer es `CR` (0Dh). Sin ese chequeo el parser seguiría leyendo bytes fuera del buffer. El `0` es un centinela de seguridad adicional.

**Efecto colateral de `MUL CX`:** la instrucción produce un resultado de 32 bits en `DX:AX`. Como el valor máximo posible es `255 × 10 + 9 = 2559`, que cabe en 16 bits, `DX` siempre queda en cero y no contamina la clasificación.

---

## 5. Algoritmo B — clasificación por rangos sin signo

**Propósito:** determinar la clase de red a partir del valor numérico del primer octeto, usando el modelo clásico de clases IPv4.

**Modelo de clases IPv4 (RFC 791):**

|Rango primer octeto|Clase|Bits iniciales|
|---|---|---|
|1 – 127|Clase A|`0xxxxxxx`|
|128 – 191|Clase B|`10xxxxxx`|
|192 – 223|Clase C|`110xxxxx`|
|224 – 255|Sub-red / multicast|`111xxxxx`|

**Implementación en tres `CMP` en cascada:**

```asm
CMP AX, 127  →  JBE es_clase_a   ; si AX ≤ 127 → Clase A
CMP AX, 191  →  JBE es_clase_b   ; si 128 ≤ AX ≤ 191 → Clase B
CMP AX, 223  →  JBE es_clase_c   ; si 192 ≤ AX ≤ 223 → Clase C
                                  ; si llegó aquí: 224–255 → Sub-red
```

Cada `CMP` solo lo ejecutan los valores que fallaron todos los anteriores, por lo que las condiciones son mutuamente excluyentes sin necesidad de rangos explícitos.

**Por qué `JBE` y no `JLE`:**  
`JBE` (Jump if Below or Equal) opera sin signo usando los flags `CF` y `ZF`. `JLE` opera con signo, donde el byte `128` se interpreta como `−128` en complemento a dos. Usando `JLE`, el rango 128–255 saltaría siempre a Clase A porque todos los valores son "negativos" respecto a 127. `JBE` trata el registro como un entero sin signo de 0 a 255, que es el dominio correcto.

---

## 6. Algoritmo C — salida por consola

**Propósito:** imprimir el mensaje correspondiente a la clase detectada usando el servicio de DOS.

```
BX = dirección del mensaje elegido   (viene de la clasificación)
DX = BX
AH = 09h
INT 21h                              → DOS imprime hasta encontrar '$'
```

El puente `BX → DX` existe porque las cuatro ramas de la clasificación necesitan un punto de convergencia único. `BX` actúa como "parámetro de retorno" implícito entre la clasificación y la salida.

---

## 7. Prólogo y epílogo estándar `.EXE`

```asm
PUSH DS        ; guarda el segmento del PSP que DOS puso en DS
SUB  AX, AX   ; AX = 0
PUSH AX        ; apila 0000h → al hacer RET salta a DS:0000 = INT 20h
MOV  AX, datos
MOV  DS, AX   ; ahora DS apunta al segmento datos del programa
...
RET            ; DOS retoma el control vía la dirección apilada en el prólogo
```

Este mecanismo es obligatorio en programas `.EXE` para modo real. El `RET` final no retorna a ninguna función; retorna al DOS usando la dirección `DS:0000` (que apunta a INT 20h) que el prólogo dejó en la pila.

---

## 8. Flujo completo de ejecución

```
Inicio
  │
  ├─ Prólogo: cargar DS, preparar retorno DOS
  │
  ├─ Entrada
  │    ├─ INT 21h/09h → mostrar prompt
  │    ├─ INT 21h/0Ah → leer IP en buf_dat
  │    └─ INT 21h/09h → CR+LF
  │
  ├─ Parser (bucle leer_digito)
  │    └─ AX = acumular dígitos hasta '.' o CR o 0
  │
  ├─ Clasificación (tres CMP/JBE en cascada)
  │    └─ BX = dirección del mensaje correcto
  │
  ├─ Salida
  │    └─ INT 21h/09h → imprimir mensaje en BX
  │
  └─ RET → DOS
```

---

_Generado a partir de `P1.asm` · MASM 5.0 / 8086 modo real_