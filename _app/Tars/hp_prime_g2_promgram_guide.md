---
title: HP Prime G2 — Guía de programación PPL
galaxy_body: beacon
scope: vault
project: tars-hpprgm-conversion
date_created: 2026-09-05
date_updated: 2026-09-05
status: activo
tags:
  - beacon
  - hp-prime
  - ppl
  - programacion
  - referencia
---

# HP Prime G2 — Guía de programación PPL

> Guía de referencia para generación de código HP PPL con IA.
> Basada en documentación oficial, tutoriales de Edward Shore, hpprime.club, hpmuseum.org y experiencia directa de pruebas en CASE.

---

## 1. Estructura obligatoria de todo programa

```
EXPORT NOMBRE_PROG()
BEGIN
  // código acá
END;
```

- El nombre solo puede tener letras, números y `_`, y debe empezar con letra.
- Cada línea de comando termina en `;`
- Comentarios con `//`
- El nombre en `EXPORT` debe coincidir exactamente con el nombre del archivo `.hpprgm`

---

## 2. Variables — reglas críticas

### LOCAL — límite de 7 por declaración

`LOCAL` tiene un límite no documentado de **7 variables por declaración**. Con más de 7 devuelve error de sintaxis. Siempre partir en varias líneas:

```
// MAL — 9 variables en una línea → error de sintaxis
LOCAL op, r1, x1, r2, x2, mag1, ang1, mag2, ang2;

// BIEN — partido en bloques de máximo 7
LOCAL op, r1, x1, r2, x2, mag1, ang1;
LOCAL mag2, ang2, resultado;
```

### Tipos de variables

| Tipo | Descripción |
|------|-------------|
| `LOCAL var;` | Local al programa — se crea al entrar y se elimina al salir |
| `EXPORT var;` | Global — persiste en memoria, nunca se puede eliminar salvo borrándola del fuente |
| `A` – `Z`, `θ` | Variables globales del sistema, siempre disponibles, valor inicial 0 |
| `Z0`–`Z9` | Variables de números complejos |
| `L0`–`L9` | Variables de listas |
| `M0`–`M9` | Variables de matrices/vectores |
| `G0`–`G9` | Objetos gráficos (G0 = pantalla actual) |

### Asignación e inicialización

```
LOCAL k := 1;        // declarar e inicializar en la misma línea
LOCAL a, b, c;       // valor por defecto: 0
a := 5;              // asignación
```

> ⚠️ Las variables `EXPORT` globales, una vez compiladas, **nunca se pueden eliminar** excepto borrándolas del archivo fuente y recompilando.

### Nombres de variables

Mantener nombres **cortos** — los nombres se codifican en UTF-16 LE en el binario, así que nombres largos aumentan el tamaño del archivo `.hpprgm` innecesariamente.

---

## 3. Funciones matemáticas — siempre en MAYÚSCULAS

PPL requiere las funciones matemáticas en mayúsculas. Minúsculas generan error de sintaxis.

| Correcto | Incorrecto | Descripción |
|----------|------------|-------------|
| `SQRT(x)` | `sqrt(x)` | Raíz cuadrada |
| `SIN(x)` | `sin(x)` | Seno |
| `COS(x)` | `cos(x)` | Coseno |
| `TAN(x)` | `tan(x)` | Tangente |
| `ATAN(x)` | `atan(x)` | Arcotangente |
| `ASIN(x)` | `asin(x)` | Arcoseno |
| `ACOS(x)` | `acos(x)` | Arcocoseno |
| `ABS(x)` | `abs(x)` | Valor absoluto |
| `LOG(x)` | `log(x)` | Logaritmo base 10 |
| `LN(x)` | `ln(x)` | Logaritmo natural |
| `EXP(x)` | `exp(x)` | Exponencial |
| `SIGN(x)` | `sign(x)` | Signo (+1, -1, 0) |
| `FLOOR(x)` | `floor(x)` | Piso |
| `π` | `pi` / `PI` | Número π |

### atan2 no existe en PPL

`atan2(y, x)` no existe. Reemplazar con `ATAN(y/x)` y manejar el caso `x == 0` manualmente:

```
IF x == 0 THEN
  angulo := 90 * SIGN(y);
ELSE
  angulo := ATAN(y / x) * 180 / π;
END;
```

---

## 4. I/O — entrada y salida

### CHOOSE — menú de opciones

```
CHOOSE(var, "Titulo",
  "1. Opcion A",
  "2. Opcion B",
  "3. Opcion C"
);
// var toma valor 1, 2 o 3 según la selección
```

### INPUT — pedir valor al usuario

```
// Forma simple
INPUT(var, "Titulo", "etiqueta:", "descripcion:", valor_default);

// Forma multi-campo
INPUT(
  {var1, var2, var3},
  "Titulo",
  {"label1", "label2", "label3"},
  {"desc1", "desc2", "desc3"},
  {default1, default2, default3}
);
```

### MSGBOX — mensaje emergente

```
MSGBOX("Texto: " + variable);
// Detiene ejecución hasta que el usuario presiona una tecla
// Solo acepta strings — concatenar con +
```

### PRINT — salida a consola/terminal

```
PRINT("texto");
PRINT(variable);
```

### RETURN — devolver resultado

```
RETURN valor;       // devuelve al stack de Home
RETURN "texto" + variable;  // puede devolver strings
```

---

## 5. Estructuras de control

### IF / THEN / ELSE

```
IF condicion THEN
  // ...
END;

IF condicion THEN
  // si verdadero
ELSE
  // si falso
END;
```

### CASE — equivalente a switch

```
CASE
  IF op == 1 THEN
    // ...
  END;
  IF op == 2 THEN
    // ...
  END;
  DEFAULT
    // si ninguna condición es verdadera
END;
```

> Preferir `CASE` sobre cadenas de `IF/ELSE` cuando se evalúa la misma variable.

### FOR

```
FOR i FROM 1 TO 10 DO
  // ...
END;

FOR i FROM 10 TO 1 STEP -1 DO
  // ...
END;
```

### WHILE

```
WHILE condicion DO
  // ...
END;
```

### REPEAT / UNTIL

```
REPEAT
  // se ejecuta al menos una vez
UNTIL condicion;
```

### Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `==` | Igual (comparación) |
| `≠` | Distinto |
| `<`, `≤`, `>`, `≥` | Menor, menor-igual, mayor, mayor-igual |
| `:=` | Asignación |
| `AND`, `OR`, `NOT` | Lógicos |

> ⚠️ `=` es comparación en CAS, `:=` es asignación en PPL. No mezclar.

---

## 6. Gráficos — pantalla 320×240

La pantalla de la HP Prime G2 es de **320 × 240 píxeles**. Origen (0,0) en esquina superior izquierda.

```
RECT();                          // limpiar pantalla (blanco)
RECT(RGB(0,0,0));               // limpiar con color
PIXON(x, y);                    // encender píxel
PIXON(x, y, color);
LINE(x1, y1, x2, y2);          // línea
LINE(x1, y1, x2, y2, color);
TEXTOUT_P("texto", x, y);      // texto en pantalla
TEXTOUT_P("texto", x, y, fuente, tamaño, color, fondo);
FREEZE;                          // congelar pantalla hasta toque
WAIT(0);                         // congelar hasta cualquier tecla
```

Objetos gráficos disponibles: `G0` (pantalla activa) hasta `G9` (buffers).

```
DIMGROB_P(G1, 320, 240);       // inicializar buffer G1
BLIT_P(G0, 0, 0, 320, 240, G1, 0, 0, 320, 240);  // copiar buffer a pantalla
```

---

## 7. Subrutinas y múltiples funciones

Las subrutinas deben declararse **antes** del programa principal que las llama:

```
// Subrutina — va ANTES del programa principal
helper(x)
BEGIN
  RETURN x * 2;
END;

// Programa principal
EXPORT MI_PROG()
BEGIN
  LOCAL resultado;
  resultado := helper(5);
  MSGBOX("Resultado: " + resultado);
END;
```

> ⚠️ Si `MiProg2` llama a `MiProg1`, el fuente de `MiProg1` debe compilarse primero.

---

## 8. Limitaciones conocidas — checklist para IA

Antes de subir un programa generado por IA, verificar:

- [ ] `LOCAL` máximo 7 variables por línea — partir si hay más
- [ ] Funciones math en MAYÚSCULAS (`SQRT`, `SIN`, `COS`, `ATAN`, `ABS`, `LOG`, `LN`)
- [ ] Usar `π` en lugar de `pi` o `PI`
- [ ] `atan2` no existe — reemplazar con `ATAN(y/x)` + manejo de `x == 0`
- [ ] Comparación con `==`, asignación con `:=`
- [ ] Todo comando termina en `;`
- [ ] Nombre del `EXPORT` coincide con nombre del archivo `.hpprgm`
- [ ] Nombres de variables cortos (eficiencia en binario UTF-16 LE)
- [ ] Subrutinas declaradas antes del programa principal que las llama
- [ ] Si hay múltiples `EXPORT`, el script Python de conversión necesita actualización (actualmente asume 1 función exportada)

---

## 9. Categorías de programas probadas

| Categoría | Estado | Notas |
|-----------|--------|-------|
| Funciones simples (1 `EXPORT`, sin vars globales) | ✅ Probado | KMH_CONV — exitoso 2026-09-04 |
| CHOOSE + INPUT + MSGBOX (sin gráficos) | ✅ Probado | VOL_CALC, FASOR_CALC — exitosos 2026-09-05 |
| Múltiples funciones `EXPORT` | ⬜ Pendiente | Requiere actualizar script Python |
| Gráficos (RECT, PIXON, TEXTOUT_P) | ⬜ Pendiente | |
| Python embebido (`#PYTHON ... #END`) | ⬜ Pendiente | Solo G2 |

---

## 10. Recursos de referencia

| Recurso | URL |
|---------|-----|
| Referencia completa de comandos PPL | https://en.hpprime.club/docs/commands-list |
| Tutorial Edward Shore (PDF) | https://literature.hpcalc.org/community/hpprime-prog-tutorial.pdf |
| Formato `.hpprgm` (Omnimaga) | https://www.omnimaga.org/hp-prime/the-hpprgm-format/ |
| Foro HP Museum | https://hpmuseum.org/forum |
| TI-Planet Wiki — formato de archivo | https://wiki.tiplanet.org/HP_Prime/File_Format |
| hpprime.club — intro a programación | https://en.hpprime.club/articles/hans-hp-prime-programming-introduction/ |
