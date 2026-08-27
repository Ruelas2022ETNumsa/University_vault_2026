---
title: AHPL — Guía unificada para ETN825
galaxy_body: beacon
scope: vault
tool: ahpl-notation
audience:
  - usuario
  - notebooklm
  - claude
tags:
  - beacon
  - ahpl
  - infraestructura
  - ETN825
date_created: 2026-08-27
date_updated: 2026-08-27
status: activo
---

# ⚡ GUÍA UNIFICADA DE NOTACIÓN AHPL (ETN825)

> Guía de escritura y lectura de módulos AHPL (A Hardware Programming Language) para Arquitectura de Computadores (ETN825). Basada en Hill & Peterson — Digital Systems 2ª ed. y material del docente. Este documento está organizado en tres bloques: **Reglas de notación (N1–N9)**, **Checklist (N10)**, y **Biblioteca de ejemplos por tipo (N11–N14)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM escriba, complete o explique código AHPL correctamente. Cuando el usuario pida un módulo o secuencia AHPL, responder con el bloque de código — no con pseudocódigo ni descripción textual.

### Defaults — cuando el usuario no especifica

- Formato de bloque: sección de declaraciones primero, luego pasos numerados.
- Registros: mayúsculas (`DR`, `CR`, `AC`, `PC`, `MR`). Escalares: minúsculas (`busy`, `ready`, `first`).
- Transferencia: `←` (asignación con reloj). Conexión de bus: `=` (sin reloj).
- Bifurcación fija: `→ (D)`. Bifurcación condicional: `→ (f)/(D)` o `→ (f, f̄)/(D1, D2)`.
- Condición negada: barra sobre la expresión (en texto plano usar `CSBUS_0̄` o indicar con `NOT(...)`).
- Paso nulo: `Null` — consume un ciclo de reloj sin operación.
- Fin de secuencia: `DEAD END` o `END SEQUENCE`.

### Reglas base — siempre obligatorias

Antes de escribir cualquier bloque AHPL, verificar en orden:

1. ¿Qué hace el módulo? (qué transfiere, qué controla, qué espera)
2. ¿Qué registros y buses necesita? (ver N2)
3. ¿Qué señales de entrada/salida? (ver N3)
4. ¿Qué tipo de secuencia? (lineal · bucle · bifurcación · subrutina) (ver N5)
5. ¿Hay operaciones simultáneas en un paso? (ver N6)
6. ¿El módulo termina o vuelve a otro paso? (ver N7)

---

## BLOQUE A — ESTRUCTURA Y DECLARACIONES

---

### N1. ESTRUCTURA OBLIGATORIA DE UN MÓDULO AHPL

Todo módulo AHPL tiene dos partes: **declaraciones** y **secuencia de control**. Sin declaraciones el módulo está incompleto.

```
MODULE: NOMBRE DEL MÓDULO
MEMORY: <registros internos con tamaño>
OUTPUTS: <señales y registros de salida>
INPUTS: <señales de entrada>
COMBUSES: <buses combinacionales con tamaño>

1. <paso 1>
2. <paso 2>
   ...
N. DEAD END   (o END SEQUENCE si retorna a otro módulo)

<expresiones combinacionales fuera de la secuencia>
END
```

Reglas:

- `MODULE:` — nombre del módulo en mayúsculas, descriptivo.
- `MEMORY:` — registros que retienen valor entre ciclos de reloj (flip-flops). Siempre con tamaño entre corchetes si son vectores: `DR[18]`, `CR[8]`. Escalares sin corchetes: `busy`, `first`.
- `OUTPUTS:` — señales o registros que salen del módulo. Si son buses de datos incluir tamaño: `CHAR[8]`. Señales booleanas sin corchetes: `print`, `feed`.
- `INPUTS:` — señales que entran al módulo desde otros módulos o dispositivos: `wait`, `csrdy`.
- `COMBUSES:` — buses combinacionales (sin reloj, conexión directa). Con tamaño y señales booleanas: `IOBUS[18]`, `CSBUS[12]`, `ready`, `datavalid`, `accept`.

❌ Incorrecto — falta tamaño en registro:
```
MEMORY: DR; CR; busy
```

✅ Correcto:
```
MEMORY: DR[18]; CR[8]; busy; first
```

---

### N2. DECLARACIÓN DE REGISTROS Y BUSES

#### Registros (MEMORY)

| Notación | Significado | Ejemplo |
|---|---|---|
| `REG[N]` | Registro de N bits | `DR[18]`, `CR[8]`, `IR[18]`, `AC[18]` |
| `REG` (sin corchetes) | Flip-flop de 1 bit (escalar) | `busy`, `first`, `ready` |
| Separador `;` | Separa elementos en la misma sección | `DR[18]; CR[8]; busy; first` |

#### Buses (COMBUSES)

| Notación | Significado | Ejemplo |
|---|---|---|
| `BUS[N]` | Bus de N bits, conexión combinacional | `IOBUS[18]`, `CSBUS[12]` |
| Señal booleana en COMBUSES | Bus de 1 bit (señal de handshake) | `ready`, `datavalid`, `accept` |

> **Diferencia clave:** `MEMORY` usa reloj — las transferencias `←` solo se efectúan al borde de reloj. `COMBUSES` es combinacional — las conexiones `=` son inmediatas y no retienen valor.

---

### N3. ENTRADAS Y SALIDAS

| Sección | Qué declara | Dirección |
|---|---|---|
| `INPUTS` | Señales que llegan de otros módulos o dispositivos | → hacia este módulo |
| `OUTPUTS` | Señales o registros que salen hacia otros módulos | ← desde este módulo |
| `COMBUSES` | Buses compartidos bidireccionales o señales de handshake | ↔ bidireccional |

**Ejemplo del módulo PRINTER INTERFACE:**

```
OUTPUTS: CHAR[8]; print; feed
INPUTS:  wait; csrdy
COMBUSES: IOBUS[18]; CSBUS[12]; ready; datavalid; accept
```

- `CHAR[8]` — los 8 bits del carácter enviado a la impresora (salida)
- `print`, `feed` — comandos booleanos a la impresora (salida)
- `wait` — señal de espera de la impresora (entrada)
- `csrdy` — canal CS listo, viene del sistema (entrada)
- `IOBUS[18]`, `CSBUS[12]` — buses compartidos del sistema
- `ready`, `datavalid`, `accept` — señales de handshake del protocolo de bus

---

## BLOQUE B — OPERADORES Y PASOS

---

### N4. OPERADORES AHPL

#### Transferencia y conexión

| Operador | Nombre | Uso | Reloj |
|---|---|---|---|
| `←` | Transferencia | `AC ← DR` — copia DR en AC al borde de reloj | Sí (sincrónico) |
| `=` | Conexión de bus | `IBUS = AC` — conecta AC al bus | No (combinacional) |
| `*` | Producto condicional | `CR ← (D₁₀:₁₇!) * (first, first̄)` | Sí |

#### Operadores lógicos

| Símbolo | Operación | Alternativa texto | Ejemplo |
|---|---|---|---|
| `∧` | AND | `AND`, `&` | `csrdy ∧ CSBUS₀` |
| `∨` | OR | `OR`, `+` | `busy ∨ first` |
| `⊕` | XOR | `XOR`, `@` | `AC ⊕ DR` |
| `¬` / barra | NOT | `NOT`, `!` al final del operando | `CSBUS̄₀`, `(accept)̄` |

#### Selección de bits

| Notación | Significado | Ejemplo |
|---|---|---|
| `REG[i]` | Bit i del registro | `IR[0]`, `CR[7]` |
| `REG[i:j]` | Bits i a j | `IR[8:17]`, `D[10:17]` |
| `REG[i:j]!` | Bits i a j, complementado | `D[10:17]!` — NOT de esa porción |

#### Operaciones aritméticas

| Notación | Operación | Ejemplo |
|---|---|---|
| `INC(REG)` | Incremento | `PC ← INC(PC)` |
| `ADD(A,B)` | Suma | `AC ← ADD(AC, DR)` |
| `RETURN(REG)` | Retorno/complemento lógico | `feed = RETURN(CR)` |

---

### N5. TIPOS DE PASO EN LA SECUENCIA

#### Paso de operación (transferencia o conexión)

Ejecuta una o más acciones en un ciclo de reloj.

```
4. CSBUS₀ = busy; datavalid = 1;
```

> El punto y coma `;` dentro de un paso separa **operaciones simultáneas** que ocurren en el mismo ciclo de reloj.

#### Paso de bifurcación fija

Va incondicionalmente al paso indicado. No ejecuta operación.

```
→ (CSBUS₃, CSBUS̄₃, CSBUS̄₂)/(1, 1A, 3)
```

Formato: `→ (condición₁, condición₂, ...)/(destino₁, destino₂, ...)`

- Las condiciones son mutuamente excluyentes.
- Los destinos pueden ser números de paso (`1`, `3`) o etiquetas (`1A`, `3`).

#### Paso de bifurcación condicional

Evalúa una condición y salta según el resultado.

```
→ (ready)/(3)
→ (datavalid)/(1A)
→ (first, first̄)/(3A, 8A)
```

- Si la condición es verdadera → va al destino indicado.
- Si es falsa → continúa al siguiente paso numerado.
- Con dos destinos: `→ (f, f̄)/(D_yes, D_no)` — el segundo destino es para la negación.

#### Paso nulo

Consume un ciclo sin operación. Útil para sincronización.

```
5A. Null
```

#### Fin de secuencia

```
DEAD END        ← el módulo se detiene, no retorna
END SEQUENCE    ← la secuencia termina y puede reiniciarse o llamarse desde otro módulo
```

---

### N6. OPERACIONES SIMULTÁNEAS EN UN PASO

Varias transferencias en el mismo paso se ejecutan **todas al mismo tiempo** en el mismo ciclo de reloj.

```
2A. DR ← IOBUS; busy ← 1; accept = 1; first ← 1
```

Esto significa:
- `DR ← IOBUS` — DR toma el valor de IOBUS
- `busy ← 1` — busy se pone en 1
- `accept = 1` — accept se activa (combinacional, inmediato)
- `first ← 1` — first se pone en 1

**Todos ocurren en el mismo borde de reloj.**

> Regla: si dos transferencias afectan el mismo registro en el mismo paso, es un error. Cada registro destino debe aparecer una sola vez por paso.

---

### N7. ETIQUETAS DE PASO Y SUBPASO

Los pasos se numeran con enteros. Los subpasos usan letra sufijo.

| Notación | Tipo | Uso |
|---|---|---|
| `1.` `2.` `3.` | Paso principal | Flujo principal de la secuencia |
| `1A.` `2A.` `3A.` | Subpaso A | Primera rama de bifurcación |
| `1B.` `2B.` | Subpaso B | Segunda rama (si hay) |
| `(1)` `(1A)` en bifurcación | Destino | A qué paso/subpaso ir |

**Ejemplo de uso de etiquetas del módulo PRINTER INTERFACE:**

```
→ (CSBUS₃, CSBUS̄₃, CSBUS̄₂)/(1, 1A, 3)
...
1A. ready = 1;
    → (datavalid)/(1A)
2A. DR ← IOBUS; busy ← 1; accept = 1; first ← 1
3A. CR ← (D₁₀:₁₇!) * (first, first̄)
```

---

### N8. EXPRESIONES COMBINACIONALES FUERA DE LA SECUENCIA

Algunas salidas se definen como expresiones combinacionales **después del END SEQUENCE**, antes del `END` del módulo. No son pasos — son definiciones permanentes.

```
END SEQUENCE
CHAR = CR
END
```

- `CHAR = CR` — la salida CHAR es siempre igual al contenido de CR (combinacional, no sincrónico).
- Se usan para salidas que deben reflejar el estado actual del registro en todo momento.

---

### N9. NOTACIÓN DE CONDICIÓN COMPUESTA Y SEÑALES NEGADAS

Las condiciones de bifurcación pueden combinar señales con AND (`∧`) o usar señales negadas (barra).

```
1. → (csrdy ∧ CSBUS̄₀ ∧ CSBUS₁ ∧ CSBUS̄₂)/(1)
```

Interpretación:
- `csrdy` — csrdy = 1
- `CSBUS̄₀` — bit 0 del CSBUS = 0 (negado)
- `CSBUS₁` — bit 1 del CSBUS = 1
- `CSBUS̄₂` — bit 2 del CSBUS = 0 (negado)
- Toda la condición: `csrdy AND (NOT CSBUS₀) AND CSBUS₁ AND (NOT CSBUS₂)`
- Si la condición es **falsa** → va al paso `(1)` (bucle de espera).
- Si es **verdadera** → continúa al paso 2.

> En el libro, las barras se escriben sobre los símbolos. En texto plano, se indica con subíndice negado o con notación `NOT(...)`.

---

## BLOQUE C — CHECKLIST

---

### N10. CHECKLIST ANTES DE ENTREGAR UN MÓDULO AHPL

Antes de escribir o completar un módulo, verificar:

- [ ] ¿El módulo tiene `MODULE:`, `MEMORY:`, `OUTPUTS:`, `INPUTS:`, `COMBUSES:`?
- [ ] ¿Los registros vectoriales tienen tamaño entre corchetes? (`DR[18]`, no `DR`)
- [ ] ¿Las transferencias usan `←` y las conexiones de bus usan `=`?
- [ ] ¿Las operaciones simultáneas están en el **mismo paso** separadas por `;`?
- [ ] ¿Ningún registro destino aparece dos veces en el mismo paso?
- [ ] ¿Las bifurcaciones tienen formato `→ (condición)/(destino)`?
- [ ] ¿Las condiciones negadas están correctamente indicadas con barra o `NOT`?
- [ ] ¿Los subpasos están etiquetados con letra sufijo (`1A`, `2A`)?
- [ ] ¿La secuencia termina con `DEAD END` o `END SEQUENCE`?
- [ ] ¿Las salidas combinacionales permanentes están después del `END SEQUENCE` y antes del `END`?
- [ ] ¿El módulo tiene `END` al final?

---

## BLOQUE D — BIBLIOTECA DE EJEMPLOS

---

### N11. MÓDULO COMPLETO — PRINTER INTERFACE

> Contexto para NotebookLM: módulo AHPL completo de la interface de impresora. Cubre el protocolo completo: espera de dirección en CSBUS, handshake con IOBUS (datavalid/accept), carga de DR, acumulación en CR con `first`, envío a impresora (feed/print), y espera de `wait`. Fuente: Hill & Peterson Digital Systems 2ª ed., material del docente ETN825.

```
MODULE: PRINTER INTERFACE
MEMORY: DR[18]; CR[8]; busy; first
OUTPUTS: CHAR[8]; print; feed
INPUTS: wait; csrdy
COMBUSES: IOBUS[18]; CSBUS[12]; ready; datavalid; accept

1.  → (csrdy ∧ CSBUS̄₀ ∧ CSBUS₁ ∧ CSBUS̄₂)/(1)
2.  accept = 1;
    → (CSBUS̄₃, CSBUS̄₃, CSBUS₃)/(1, 1A, 3)

3.  → (readȳ)/(3)
4.  CSBUS₀ = busy; datavalid = 1;
    → (accept̄, accept)/(4, 1)

1A. ready = 1;
    → (datavalid̄)/(1A)
2A. DR ← IOBUS; busy ← 1; accept = 1; first ← 1
3A. CR ← (D₁₀:₁₇!) * (first, first̄)
4A. feed = RETURN(CR); print = RETURN(CR);
5A. Null
6A. → (wait)/(6A)
7A. first ← 0; busy * first̄ ← 0
    → (first, first̄)/(3A, 8A)
8A. DEAD END

END SEQUENCE
CHAR = CR
END
```

#### Lectura paso a paso

| Paso | Qué hace |
|---|---|
| `1.` | Bucle de espera: permanece en 1 mientras la condición de dirección CSBUS no coincida con esta interface (código `010` negado). Sale cuando csrdy=1 y la dirección es correcta. |
| `2.` | Activa `accept=1` en el bus CS. Bifurca según bit 3 del CSBUS: si es 0 → vuelve a 1, si es 1 → va a 3 (Output) o 1A (Input). |
| `3.` | Bucle de espera: permanece mientras `ready` sea 0. |
| `4.` | Pone en CSBUS el estado `busy` y activa `datavalid=1`. Bucle hasta que `accept=1`. |
| `1A.` | Activa `ready=1` en el bus IO y espera hasta que `datavalid=1`. |
| `2A.` | Carga DR desde IOBUS, activa busy, accept, first — todo simultáneo. |
| `3A.` | Carga CR con bits 10:17 del bus de datos, condicionado por `first`/`first̄`. |
| `4A.` | Envía señales `feed` y `print` a la impresora (combinacional, basado en CR). |
| `5A.` | Paso nulo — sincronización de un ciclo. |
| `6A.` | Bucle de espera: permanece mientras la impresora indica `wait=1`. |
| `7A.` | Pone `first←0` y borra `busy*first̄`. Bifurca: si `first=1` vuelve a 3A, si no va a 8A. |
| `8A.` | DEAD END — módulo detenido hasta nuevo llamado. |
| `CHAR=CR` | Salida combinacional permanente: CHAR siempre refleja el contenido de CR. |

---

### N12. PATRÓN — BUCLE DE ESPERA CON SEÑAL

> Contexto para NotebookLM: patrón de polling. El módulo permanece en el mismo paso hasta que una señal cambia de estado. Se usa para esperar `ready`, `datavalid`, `accept`, `wait`, `csrdy`. El paso bifurca hacia sí mismo mientras la condición sea falsa (o verdadera, según el sentido).

```
% Espera mientras la señal es 0 (sale cuando es 1):
N.  → (señal̄)/(N)

% Espera mientras la señal es 1 (sale cuando es 0):
N.  → (señal)/(N)

% Ejemplo concreto — esperar que ready sea 1:
3.  → (readȳ)/(3)

% Ejemplo concreto — esperar que wait sea 0:
6A. → (wait)/(6A)
```

---

### N13. PATRÓN — BIFURCACIÓN MÚLTIPLE POR BITS DE BUS

> Contexto para NotebookLM: bifurcación a más de dos destinos según combinación de bits de un bus. Las condiciones son mutuamente excluyentes — exactamente una será verdadera. Se usa para decodificar campos de instrucción (IR), direcciones de dispositivo (CSBUS) o modos de operación.

```
% Formato general:
→ (cond₁, cond₂, cond₃)/(dest₁, dest₂, dest₃)

% Ejemplo — decodificación por bit 3 del CSBUS:
→ (CSBUS̄₃, CSBUS̄₃, CSBUS₃)/(1, 1A, 3)

% Ejemplo — decodificación de instrucción por IR[0]:
→ (IR̄[0], IR[0])/(fetch, execute)

% Ejemplo — bifurcación triple por IR[0:1]:
→ (IR[0] ∧ IR̄[1],   IR̄[0] ∧ IR[1],   IR[0] ∧ IR[1])/(paso_A, paso_B, paso_C)
```

> **Regla:** la suma lógica de todas las condiciones debe ser 1 (una siempre se cumple). Si ninguna se cumple, el comportamiento es indefinido.

---

### N14. PATRÓN — OPERACIÓN CONDICIONAL CON PRODUCTO *

> Contexto para NotebookLM: el operador `*` (producto condicional) permite cargar un registro con uno de dos valores según una condición booleana, en un único paso sincrónico.

```
% Formato:
REG ← (expresión!) * (cond, cond̄)

% Interpretación:
% Si cond = 1 → REG ← expresión
% Si cond = 0 → REG ← 0 (o retiene valor según contexto)

% Ejemplo del módulo PRINTER INTERFACE:
3A. CR ← (D₁₀:₁₇!) * (first, first̄)

% Interpretación:
% Si first = 1 → CR ← D[10:17] (NOT de los bits 10:17)
% Si first = 0 → CR ← 0
```

> El `!` después de la expresión indica complemento lógico bit a bit de ese rango. En este ejemplo, `D₁₀:₁₇!` es el NOT de los bits 10 a 17 del bus de datos.

---

### N15. PATRÓN — SALIDA COMBINACIONAL PERMANENTE (fuera de secuencia)

> Contexto para NotebookLM: las expresiones después de `END SEQUENCE` y antes de `END` son salidas combinacionales que el módulo mantiene en todo momento, sin reloj. Se usan cuando una salida debe reflejar en tiempo real el contenido de un registro o una operación lógica sobre él.

```
% Formato:
END SEQUENCE
SALIDA = expresión
END

% Ejemplo — CHAR siempre refleja CR:
END SEQUENCE
CHAR = CR
END

% Ejemplo con operación lógica — salida negada:
END SEQUENCE
CHAR = NOT(CR)
END

% Ejemplo con selección de bits:
END SEQUENCE
CHAR = CR[0:7]
END
```

> **Diferencia con transferencia en paso:** `CR ← valor` ocurre una vez al borde de reloj. `CHAR = CR` es continuo — si CR cambia, CHAR cambia en el mismo instante.

---

%%
# galaxy-links
[[_app/notebooklm/guides/ETN825/ETN825_tikz.md]]
[[_library_ETN825]]
%%
