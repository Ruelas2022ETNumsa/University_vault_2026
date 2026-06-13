## Resumen consolidado del proyecto

### Enunciado

Desarrollar un programa para **8086 en modo real**, usando **MASM 5.0**, que:

1. Lea una cadena desde teclado.
    
2. Obtenga únicamente los caracteres ubicados en posiciones impares.
    
3. Muestre el resultado en pantalla de texto 80x25.
    
4. No utilice interrupciones para entrada, salida o video.
    

Única excepción permitida:

```asm
mov ax,4C00h
int 21h
```

para finalizar el programa.

---

# Plataforma

- Intel 8086
    
- Modo Real
    
- MASM 5.0
    
- DOSBox
    
- Un único archivo ASM
    
- Memoria de video directa
    
- Sin INT 10h
    
- Sin INT 16h
    
- Sin INT 21h (excepto salida al DOS)
    

---

# Entrada

El usuario verá un mensaje similar a:

```text
Ingrese texto y presione ENTER para confirmar:
```

Luego escribirá una cadena de longitud variable.

La captura termina cuando se detecta:

```text
ENTER
```

El ENTER:
- no se almacena
- no forma parte de la cadena

---

# Método de lectura elegido

Se utilizará el método más simple:

### Buffer de teclado BIOS

Área:

```text
0040:001E
```

No se utilizarán:

### Método alternativo 1

Acceso directo al controlador de teclado:

```text
Puerto 60h
Puerto 64h
```

### Método alternativo 2

Interrupciones BIOS:

```asm
int 16h
```

(prohibidas)

---

# Tamaño máximo

Se adopta:

```asm
MAX_CADENA equ 255
```

Razones:

- simplifica la reserva de memoria
- permite entradas relativamente largas
- evita complicaciones innecesarias

Si el usuario intenta ingresar más de 255 caracteres:

```text
No se garantiza el comportamiento.
```

Esta limitación se documentará explícitamente.

---

# Almacenamiento

## Entrada

```asm
cadena_entrada db MAX_CADENA dup(?)
tam_in         dw ?
```

---

## Salida

Se corrige la definición previa y queda:

```asm
cadena_salida db MAX_CADENA dup(?)
tam_out       dw ?
```

La salida siempre tendrá espacio suficiente.

---

# Fin de cadena

No se utilizarán terminadores:

```text
0
$
CR
LF
```

Todo el procesamiento dependerá de:

```asm
tam_in
```

---

# Posiciones impares

El enunciado original ya define que el conteo comienza en:

```text
0
```

Por tanto:

```text
0 -> ignorar
1 -> copiar
2 -> ignorar
3 -> copiar
...
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

---

# Espacios

Los espacios son caracteres normales.

Participan en el conteo igual que letras, números y símbolos.

---

# Estrategia de detección

Se utilizará el bit menos significativo de la posición.

Conceptualmente:

```text
LSB = 0 -> posición par
LSB = 1 -> posición impar
```

---

# Construcción de la salida

Se utilizará una segunda cadena.

```text
cadena_entrada
      ↓
ProcesarCadena
      ↓
cadena_salida
```

No se imprimirá directamente desde la cadena original.

---

# Pantalla

Acceso directo a:

```asm
B800h
```

Modo texto:

```text
80 columnas
25 filas
```

Cada celda:

```text
1 byte carácter
1 byte atributo
```

Atributo:

```asm
07h
```

(gris claro sobre negro)

---

# Limpieza de pantalla

Se utilizará el método clásico de escritura directa sobre memoria de video.

La idea es llenar toda la pantalla con espacios.

Conceptualmente:

```asm
mov ax,0720h
mov cx,2000
rep stosw
```

Ventajas:

- rápido
    
- simple
    
- clásico en 8086
    
- da la apariencia de pantalla completamente limpia
    

---

# Impresión

La impresión será genérica.

Un único procedimiento servirá para mostrar:

- mensajes
    
- cadena original
    
- resultado
    

Se intentará aprovechar instrucciones de cadena siempre que simplifiquen el código.

---

# Uso de instrucciones de cadena

Se consideran válidas y deseables.

Posibles instrucciones:

```asm
LODSB
STOSB
STOSW
MOVSB
REP
```

Porque simplifican el código y muestran conceptos clásicos del 8086.

---

# Carácter "¿"

Caso especial:

```text
¿
```

Dependiendo de:

- DOSBox
    
- página de códigos
    
- configuración del entorno
    

podría mostrarse correctamente o no.

Propuesta:

- permitirlo si funciona durante las pruebas
    
- si aparecen problemas, documentar que debe evitarse
    

---

# Estructura prevista

```text
MAIN
│
├─ LimpiarPantalla
├─ LeerCadena
├─ ProcesarCadena
├─ ImprimirCadena
└─ Finalizar
```

Todo dentro de un único archivo ASM.

---

# Filosofía final

La prioridad no es producir el programa más corto.

La prioridad es:

- cumplir el enunciado
    
- respetar la restricción de no usar interrupciones
    
- utilizar conceptos clásicos de 8086
    
- ser fácil de explicar en una defensa oral
    
- mantener una estructura clara y modular
    

---

## Mi única duda importante antes de diseñar el flujo detallado

El buffer de teclado BIOS (`0040:001E`) normalmente contiene las teclas que BIOS va almacenando, pero **sin usar INT 16h hay que gestionar cuidadosamente los punteros de cabeza y cola del buffer**.

¿Tu profesor ya explicó el uso del buffer BIOS para lectura sin interrupciones o simplemente dijo "no usen interrupciones" y dejó que ustedes investiguen la implementación? Esa respuesta cambia bastante el diseño de `LeerCadena`.