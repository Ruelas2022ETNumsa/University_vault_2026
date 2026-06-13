# Resumen del Proyecto

## Enunciado

Desarrollar un sistema en **Assembler MASM 5.0 para Intel 8086 en modo real** que:

1. Solicite al usuario un número por teclado.
2. Acepte únicamente valores entre **1 y 9999**.
3. Convierta el número a su representación textual en español.
4. Muestre el resultado en pantalla.
5. Este problema debe ser implementado usando Assembler en línea extendido.
### Ejemplos

```text
1973 -> mil novecientos setenta y tres
28   -> veinte y ocho
9    -> nueve
1000 -> mil
9999 -> nueve mil novecientos noventa y nueve
```

---

# Plataforma

## Procesador

- Intel 8086
    

## Modo

- Modo Real
    

## Ensamblador

- MASM 5.0
    

## Sistema

- DOS (INT 21h)
    

---

# Entrada

La entrada será una cadena de caracteres.

Ejemplos:

```text
1978
25
9999
```

No se convertirá inicialmente a entero.

Se trabajará directamente con los caracteres ASCII.

Ejemplo:

```text
'1' '9' '7' '8'
```

---

# Rango permitido

```text
1 - 9999
```

El valor:

```text
0
```

queda excluido para simplificar la implementación.

---

# Mensaje inicial

Antes de solicitar el dato se mostrará algo similar a:

```text
Ingrese un valor entre 1 y 9999:
```

---

# Validación

Se aceptarán únicamente caracteres:

```text
'0'..'9'
```

y una longitud entre:

```text
1 y 4 caracteres
```

---

## Casos inválidos

### Letras

```text
12a4
```

### Símbolos

```text
12-4
```

### Más de 4 dígitos

```text
12345
```

### Cero

```text
0
```

### Vacío

---

## Mensaje de error

Para cualquier error se mostrará:

```text
Ingrese un valor correcto
```

Luego el programa volverá a pedir el dato.

---

# Bucle principal

El programa permanecerá en un ciclo:

```text
leer
validar

si inválido
    mostrar error
    volver a leer

si válido
    convertir
    mostrar resultado
```

---

# Salida

La posición exacta en pantalla no es importante.

Formato esperado:

```text
Ingrese un valor entre 1 y 9999:
1978

Resultado:
mil novecientos setenta y ocho
```

---

# Estrategia elegida

Se utilizarán tablas de palabras.

Esto simplifica el código y facilita la defensa del proyecto.

---

## Tabla de unidades

```text
uno
dos
tres
cuatro
cinco
seis
siete
ocho
nueve
```

---

## Tabla de decenas

```text
diez
veinte
treinta
cuarenta
cincuenta
sesenta
setenta
ochenta
noventa
```

---

## Tabla de centenas

```text
cien
doscientos
trescientos
cuatrocientos
quinientos
seiscientos
setecientos
ochocientos
novecientos
```

---

# Construcción del resultado

Se utilizará un buffer de salida.

Ejemplo:

```asm
resultado db 100 dup(?)
```

Las palabras se irán concatenando dentro del buffer.

Ejemplo:

```text
"mil "
"novecientos "
"setenta "
"y "
"ocho"
```

Resultado final:

```text
mil novecientos setenta y ocho
```

Posteriormente se imprimirá el buffer completo.

---

# Casos especiales confirmados

## Miles

```text
1000 -> mil
1001 -> mil uno
2000 -> dos mil
```

---

## Centenas

```text
100 -> cien
101 -> cien uno
115 -> cien quince
```

**Pendiente de confirmar** si el profesor exige el español formal:

```text
101 -> ciento uno
115 -> ciento quince
```

porque esto introduce lógica adicional.

---

## Decenas

Actualmente está decidido utilizar:

```text
21 -> veinte y uno
22 -> veinte y dos
23 -> veinte y tres
24 -> veinte y cuatro
25 -> veinte y cinco
```

en lugar de:

```text
21 -> veintiuno
22 -> veintidos
23 -> veintitres
24 -> veinticuatro
25 -> veinticinco
```

porque simplifica considerablemente el programa.

---

# Objetivo de diseño

Prioridades:

1. Que funcione correctamente para 1–9999.
    
2. Código corto.
    
3. Fácil de entender.
    
4. Fácil de modificar.
    
5. Fácil de defender ante el profesor.
    
6. Mantener compatibilidad con MASM 5.0 y 8086 real.
    

---

## Punto aún pendiente

Antes de escribir código conviene decidir una sola cosa:

### ¿Cómo representaremos los números del 101 al 199?

Opción A:

```text
101 -> cien uno
115 -> cien quince
199 -> cien noventa y nueve
```

Opción B (español correcto):

```text
101 -> ciento uno
115 -> ciento quince
199 -> ciento noventa y nueve
```

La opción A simplifica bastante el código. La opción B es lingüísticamente correcta. Esa es la única decisión importante que aún falta cerrar antes de definir la arquitectura final.