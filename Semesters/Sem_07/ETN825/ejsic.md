# Ejercicio SIC: imprimir la palabra SALUDO (impresora, interface versión 2)

## Enunciado

Escribir el programa de software para imprimir, desde el computador SIC, la palabra: SALUDO.

Se debe considerar la segunda versión de la Interface de la impresora (controlada por la CPU). Se adjunta el respectivo código ASCII. La palabra a imprimirse se encuentra grabada en las siguientes direcciones de la memoria del computador: 300; 301; 302 (especificar en detalle, el contenido de estas 3 posiciones). Utilizar la notación octal para todos los números.

Datos del código ASCII necesarios (mayúsculas):

| Letra | ASCII decimal | Binario |
|---|---|---|
| S | 083 | 01010011 |
| A | 065 | 01000001 |
| L | 076 | 01001100 |
| U | 085 | 01010101 |
| D | 068 | 01000100 |
| O | 079 | 01001111 |

## Resolución

### 1. Conversión ASCII a octal

| Letra | Decimal | Octal |
|---|---|---|
| S | 83 | 123 |
| A | 65 | 101 |
| L | 76 | 114 |
| U | 85 | 125 |
| D | 68 | 104 |
| O | 79 | 117 |

Ejemplo: 83 = 1x64 + 2x8 + 3, entonces 83 decimal = 123 octal.

### 2. Contenido de las posiciones 300, 301 y 302

Cada palabra del SIC tiene 18 bits y empaqueta dos caracteres ASCII de 8 bits. Formato de la palabra: `0 | 2a letra (bits 1:8) | 0 | 1a letra (bits 10:17)`. Los bits 0 y 9 quedan en 0. El peso de la mitad alta es 2^9 = 1000 octal.

Palabra = (2a letra) x 1000 + (1a letra), todo en octal.

| Dirección | Letras (1a, 2a) | Cálculo | Contenido | Bits 0 a 17 |
|---|---|---|---|---|
| 300 | S, A | 101 x 1000 + 123 | **101123** | 0 01000001 0 01010011 |
| 301 | L, U | 125 x 1000 + 114 | **125114** | 0 01010101 0 01001100 |
| 302 | D, O | 117 x 1000 + 104 | **117104** | 0 01001111 0 01000100 |

### 3. Contador negativo

Para 3 palabras: 2^18 - 3 = 777777 - 3 + 1 = **777775** (octal).

### 4. Programa (todo en octal; impresora = dispositivo 2)

| Dir | Código | Instrucción | Comentario |
|---|---|---|---|
| 100 | 100312 | LAC 312 | AC <- 000300 |
| 101 | 500310 | DAC 310 | puntero <- 300 |
| 102 | 100313 | LAC 313 | AC <- 777775 (-3) |
| 103 | 500311 | DAC 311 | contador <- -3 |
| 104 | 752300 | IS2 00 | trae el estado de la impresora |
| 105 | 744000 | TST 4000 | salta si busy = 1 |
| 106 | 600110 | JMP 110 | impresora libre, ir a imprimir |
| 107 | 600104 | JMP 104 | impresora ocupada, volver a preguntar |
| 110 | 120310 | LAC* 310 | AC <- palabra apuntada por el puntero |
| 111 | 752000 | OD2 | envía 2 letras a la impresora |
| 112 | 000310 | ISZ 310 | puntero + 1 |
| 113 | 000311 | ISZ 311 | contador + 1; si llega a 0 salta el JMP siguiente |
| 114 | 600104 | JMP 104 | siguiente palabra |
| 115 | 600115 | JMP 115 | fin (o HLT si la tabla del curso da su código) |

Variables y constantes:

| Dir | Contenido | Descripción |
|---|---|---|
| 310 | (variable) | puntero |
| 311 | (variable) | contador |
| 312 | 000300 | constante: dirección inicial del texto |
| 313 | 777775 | constante: -3 |

Datos: 300 = 101123, 301 = 125114, 302 = 117104.

### 5. Traza de ejecución

| Vuelta | Palabra enviada | Contador tras ISZ | Sale impreso |
|---|---|---|---|
| 1 | 101123 | 777776 | S A |
| 2 | 125114 | 777777 | L U |
| 3 | 117104 | 000000 (salta) | D O |

Resultado impreso: **SALUDO**.

## Aclaración para escribir en el examen

- La impresora es el dispositivo 2.
- En la interface versión 2 el bit busy llega por CSBUS0, por eso se usa TST además de IS2 (ISn solo prueba CSR6:11).
- TST salta cuando el bit probado vale 1 (busy = 1).
- El puntero y el contador se inicializan dentro del programa, porque el enunciado solo garantiza el contenido de 300 a 302.
