
---

**Contexto técnico**

- MASM 5.0, Intel 8086, modo real
- Assembler en línea extendido: código `__asm { }` dentro de un programa C/C++
- Compilador: Code::Blocks con compilador que soporte inline ASM para 8086
- Salida en pantalla 80x25 (puede ser `printf` del lado C o video directo, a definir)

Estructura base:

```c
#include <stdio.h>
void main() {
    __asm {
        // lógica aquí
    }
}
```

---

**Enunciado**

Desarrollar un sistema que lea desde teclado un número de hasta 4 dígitos y muestre en pantalla su equivalente en texto en español.

```
entrada: 1973  →  mil novecientos setenta y tres
entrada: 28    →  veintiocho
entrada: 9     →  nueve
```

---

**Reglas definidas**

- Rango válido: 0 – 9999
- Se rechaza: ceros a la izquierda (`0013`), más de 4 dígitos, letras (`a123`), vacío
- Sin tildes en los textos
- El programa corre en ciclo permanente: leer → validar → convertir o error → volver a leer

---

**Prioridades de diseño en orden**

1. Correcto para todo el rango 1–9999
2. Código corto
3. Fácil de entender
4. Fácil de modificar
5. Fácil de defender ante el profesor
6. Compatible con MASM 5.0 y 8086 real

---

**Planteamiento**

El número se lee como string desde teclado. La conversión se divide en cuatro capas independientes que se resuelven de mayor a menor:

```
[ millares ]  →  "mil"  (solo si digito_millares >= 1)
[ centenas ]  →  "cien" / "ciento" / "doscientos" ... "novecientos"
[ decenas  ]  →  "diez"..."diecinueve" / "veinte"..."noventa"
[ unidades ]  →  "uno"..."nueve"
```

Cada capa consulta una tabla de strings fijos en C (o en el segmento de datos). El `__asm` se encarga de descomponer el número en sus cuatro dígitos mediante divisiones sucesivas por 1000, 100 y 10, y de indexar las tablas. El lado C hace el `printf` del resultado.

**Casos especiales a resolver explícitamente:**

- `0` → `"cero"`
- `11–19` → nombres irregulares (`"once"` … `"diecinueve"`)
- `21–29` → `"veinti"` + unidad fusionado (`"veintidos"`)
- `30–99` → decena + `" y "` + unidad cuando unidad != 0
- `100` → `"cien"` exacto, `101–199` → `"ciento "` + resto
- `1000` → `"mil"` solo, `1001–1999` → `"mil "` + resto

**Flujo del ciclo principal:**

```
1. Leer string desde teclado (C: gets o fgets)
2. Validar en __asm:
     - longitud 1–4
     - todos los chars entre '0'–'9'
     - si longitud > 1, primer char != '0'
3. Si inválido: mostrar mensaje de error, volver a 1
4. Convertir string a número binario (resta '0' + MUL por potencia)
5. Descomponer en millares / centenas / decenas / unidades
6. Armar string resultado consultando tablas
7. Mostrar resultado
```

---

**Decisión pendiente para arrancar**

¿La salida y las tablas de texto van en el lado C (más simple) o todo en `__asm` puro? Eso define cuánto del programa vive en C y cuánto en ensamblador.