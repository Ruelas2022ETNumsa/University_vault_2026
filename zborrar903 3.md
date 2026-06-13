# Enunciado Original

> Sin utilizar interrupciones, desarrollar un sistema de computación que lea una cadena de caracteres desde teclado e imprima en pantalla 80x25 solo los caracteres de las posiciones impares de la misma.

Ejemplo dado:
```text
entrada =la libertad es hacer lo que tienes que hacer, no lo que quieres hacer ¿Que opinas?
```
contantodo:
l=0 no se copia
a=1

Salida esperada (según el enunciado):
```text
a l b r a   s h c r l   u   i n s q e h c r,  o l   u   u e e   a e   Q e o i a ?
```

Interpretación adoptada para el proyecto:
```text
salida = albra shcrl  u insqehcr ol u uee ae Qeoia?
```

Los espacios también son caracteres válidos y participan en el conteo.

---

# Plataforma y Restricciones
## Entorno
- MASM 5.0
- Arquitectura 8086
- Modo Real
- DOSBox
- Un único archivo fuente ASM
- Pantalla texto 80x25

## Restricción principal

No se utilizarán interrupciones para:

- lectura
- escritura
- manejo de video

Por tanto NO se usará:
```asm
INT 10h
INT 16h
INT 21h
```
durante la resolución del problema.

Excepción aceptada temporalmente:
```asm
mov ax,4C00h
int 21h
```
para finalizar el programa.

---

# Adaptación del Problema
El programa deberá cumplir completamente con el enunciado original.
La cadena será ingresada por el usuario desde el teclado durante la ejecución del programa.
Debido a que la longitud de la cadena no se conoce en tiempo de ensamblado, se reservará un área de memoria suficientemente grande para almacenar la entrada.

Ejemplo:
```
MAX_CADENA equ 80cadena_entrada db MAX_CADENA dup(?)cadena_salida  db MAX_CADENA dup(?)tam_in  dw ?tam_out dw ?
```
El usuario escribirá caracteres hasta pulsar la tecla ENTER.

Durante la lectura:
- los caracteres se almacenarán en `cadena_entrada`
- se contabilizará la cantidad de caracteres ingresados
- el valor se guardará en `tam_in`

Posteriormente la cadena será procesada para generar `cadena_salida`, la cual contendrá únicamente los caracteres ubicados en posiciones impares.

---
# Manejo de la Cadena de Entrada
La cadena de entrada será dinámica.
Se reservará memoria para una cantidad máxima de caracteres definida por una constante.

Ejemplo:
```
MAX_CADENA equ 80cadena_entrada db MAX_CADENA dup(?)
```
La longitud real dependerá de lo que escriba el usuario.

Por este motivo no se utilizará:
```
tam_in equ $-cadena_entrada
```
ya que dicho mecanismo solo funciona cuando el contenido de la cadena es conocido durante el ensamblado.

La longitud real se calculará durante la ejecución y se almacenará en:
```
tam_in dw ?
```

---
# Finalización de la Lectura
La lectura finalizará cuando el usuario pulse la tecla ENTER.
Conceptualmente:
```
usuario escribe caracteres            ↓se almacenan en memoria            ↓ENTER            ↓fin de lectura
```
El carácter ENTER no formará parte de la cadena almacenada.

---

# Detección del Fin de la Cadena
El programa no buscará terminadores especiales dentro de la cadena.
No se utilizarán:
```
0$
```
como marcadores de finalización.

La longitud válida de la cadena estará determinada exclusivamente por el valor almacenado en:
```
tam_in
```
Por tanto, el procesamiento de la cadena se realizará utilizando dicha longitud.

Ejemplo conceptual:
```
mov cx,tam_in
```
De esta manera solo se recorrerán los caracteres realmente ingresados por el usuario.

---

# Criterio para Posiciones Impares
La numeración comienza en:
```text
0
```
como en el ejemplo del enunciado.

Por tanto:
```text
posición 0 → NO copiar
posición 1 → copiar
posición 2 → NO copiar
posición 3 → copiar
```

Ejemplo:
```text
Hola
0123
```

Resultado:
```text
oa
```

## observación a considerar

Hay una consecuencia importante de este cambio:

**ya no podremos usar la solución que propusiste inicialmente para detectar posiciones impares mediante el bit menos significativo de un índice implícito, a menos que tengamos algún contador de posición.**

Necesitaremos decidir entre:

1. Llevar un contador de posición (`0,1,2,3...`) y comprobar su bit 0.
2. Empezar directamente desde el segundo carácter (`posición 1`) y avanzar de dos en dos.

Esa decisión sí afecta al diseño de `ProcesarCadena`, por lo que conviene fijarla antes de escribir el algoritmo. Yo me inclinaría por la segunda porque es más simple y más cercana al objetivo del ejercicio.

---

# Tratamiento de Espacios
Los espacios cuentan como caracteres normales.

Ejemplo:
```text
AB CD
01234
```
Se procesan exactamente igual que cualquier otro carácter.

Si una posición impar contiene:
```text
' '
```
el espacio se copia a la salida.

---

# Estrategia para Detectar Paridad
No se usará una variable "índice" solo para mostrar números.
La idea seleccionada es verificar el bit menos significativo del contador de posición.

Conceptualmente:
```text
LSB = 0 → posición par
LSB = 1 → posición impar
```

Entonces:
```text
impar → copiar
par → ignorar
```

---

# Cadena de Salida
Se construirá una segunda cadena.
Esquema:
```text
cadena_entrada
        ↓
procesamiento
        ↓
cadena_salida
```
No se imprimirá directamente desde la cadena original.

---

# Reserva de Memoria para la Salida
Se eligió la solución más simple.
```asm
cadena_salida db tam_in dup(?)
```

Ventajas:
- siempre existe espacio suficiente
- diseño sencillo
- fácil de explicar
Aunque sobren posiciones, no representa ningún problema.

---

# Longitud de la Salida
Se almacenará en una variable independiente.
Ejemplo conceptual:
```asm
tam_out dw ?
```
Esto permitirá conocer exactamente cuántos caracteres fueron copiados.

---

# Pantalla de Video
Se utilizará acceso directo a memoria de video.
Segmento:
```asm
B800h
```

Modo texto:
```text
80 columnas
25 filas
```

Cada celda ocupará:
```text
1 byte carácter
1 byte atributo
```

Ejemplo:
```text
'A' 07h
```

---

# Atributo de Color
Se utilizará:
```asm
07h
```

que corresponde a:
```text
gris claro sobre negro
```
para toda la salida.

---

# Limpieza de Pantalla
Antes de mostrar resultados se limpiará la pantalla.
Se implementará un procedimiento específico.
La limpieza se realizará escribiendo espacios directamente sobre:
```text
B800:0000
```
Probablemente utilizando instrucciones de cadena para simplificar el código.

---

# Presentación en Pantalla
Se mostrarán textos descriptivos.
Ejemplo:
```text
Cadena original:
la libertad es hacer lo que tienes que hacer, no lo que quieres hacer ¿Que opinas?

Resultado:
albra shcrl  u insqehcr ol u uee ae Qeoia?
```

---

# Manejo de Líneas
Si una cadena supera las 80 columnas:
```text
columna 79 → última posición visible
```
la impresión continuará automáticamente en la siguiente fila.
El salto de línea es un comportamiento de visualización.
No forma parte de la cadena.

---

# Modularización

Se prefiere un diseño didáctico.
Todo estará en un único archivo ASM.
No habrá módulos externos.
Posible estructura:

```text
MAIN
│
├─ LimpiarPantalla
├─ ProcesarCadena
├─ ImprimirCadena
└─ Finalizar
```

---

# Procedimientos
Se utilizarán procedimientos (`PROC/ENDP`) para favorecer:
- claridad
- reutilización
- defensa oral
- mantenimiento

---

# Procedimiento de Impresión

Se acordó que sea genérico.
Conceptualmente:

```text
ImprimirCadena(
    dirección,
    longitud
)
```

De esta forma podrá utilizarse para:
```text
Cadena original
```
y
```text
Resultado
```
sin duplicar código.

---

# Instrucciones de Cadena
Están permitidas.
Pueden utilizarse cuando simplifiquen el programa.
Ejemplos:

```asm
LODSB
STOSB
MOVSB
STOSW
REP
REPNE
```
No existe restricción en este aspecto.

---

# Filosofía del Desarrollo
El objetivo principal no es minimizar líneas de código.
El objetivo es:
- que funcione
- que respete el enunciado
- que sea fácil de entender
- que sea fácil de corregir
- que sea defendible académicamente
- que aproveche conceptos clásicos de 8086 y MASM 5.0

Con estas definiciones ya es posible pasar al diseño detallado (variables, procedimientos, flujo general y registros utilizados) antes de escribir el código.