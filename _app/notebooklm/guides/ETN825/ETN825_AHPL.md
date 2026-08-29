---
title: AHPL — Guía unificada para ETN825 (LaTeX NotebookLM)
galaxy_body: beacon
scope: devault
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

> Guía de escritura y lectura de módulos AHPL (A Hardware Programming Language) para Arquitectura de Computadores (ETN825). Basada en Hill & Peterson — Digital Systems 2ª ed. y material del docente. Este documento está organizado en tres bloques: **Reglas de notación (N1–N9)**, **Checklist (N10)**, y **Biblioteca de ejemplos por tipo (N11–N15)**.
>
> **Nota de formato:** las expresiones AHPL usan LaTeX con `\( \)` para inline y `\[ \]` para display. Los bloques de código del módulo usan bloques de código estándar — LaTeX solo aplica a la notación matemática, no al código fuente AHPL.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM escriba, complete o explique código AHPL correctamente. Cuando el usuario pida un módulo o secuencia AHPL, responder con el bloque de código — no con pseudocódigo ni descripción textual.

### Defaults — cuando el usuario no especifica

- Formato de bloque: sección de declaraciones primero, luego pasos numerados.
- Registros: mayúsculas (`DR`, `CR`, `AC`, `PC`, `MR`). Escalares: minúsculas (`busy`, `ready`, `first`).
- Transferencia: \( \leftarrow \) (asignación con reloj). Conexión de bus: \( = \) (sin reloj).
- Bifurcación fija: \( \rightarrow (D) \). Bifurcación condicional: \( \rightarrow (f)/(D) \) o \( \rightarrow (f,\, \bar{f})/(D_1, D_2) \).
- Condición negada: barra sobre la expresión — \( \overline{X} \).
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
COMBUS: <buses combinacionales con tamaño>

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
- `COMBUS:` — buses combinacionales (sin reloj, conexión directa). Con tamaño y señales booleanas: `IOBUS[18]`, `CSBUS[12]`, `ready`, `datavalid`, `accept`.

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

#### Buses (COMBUS)

| Notación | Significado | Ejemplo |
|---|---|---|
| `BUS[N]` | Bus de N bits, conexión combinacional | `IOBUS[18]`, `CSBUS[12]` |
| Señal booleana en COMBUS | Bus de 1 bit (señal de handshake) | `ready`, `datavalid`, `accept` |

> **Diferencia clave:** `MEMORY` usa reloj — las transferencias \( \leftarrow \) solo se efectúan al borde de reloj. `COMBUS` es combinacional — las conexiones \( = \) son inmediatas y no retienen valor.

---

### N3. ENTRADAS Y SALIDAS

| Sección | Qué declara | Dirección |
|---|---|---|
| `INPUTS` | Señales que llegan de otros módulos o dispositivos | \( \rightarrow \) hacia este módulo |
| `OUTPUTS` | Señales o registros que salen hacia otros módulos | \( \leftarrow \) desde este módulo |
| `COMBUS` | Buses compartidos bidireccionales o señales de handshake | \( \leftrightarrow \) bidireccional |

**Ejemplo del módulo PRINTER INTERFACE:**

```
OUTPUTS: CHAR[8]; ready; accept; print; feed
INPUTS:  datavalid; wait
COMBUS: IOBUS[18]
```

- `CHAR[8]` — los 8 bits del carácter enviado a la impresora (salida)
- `ready`, `accept` — señales de handshake hacia el bus (salida)
- `print`, `feed` — comandos booleanos a la impresora (salida)
- `datavalid` — indica que hay dato válido en el bus (entrada)
- `wait` — señal de espera de la impresora (entrada)
- `IOBUS[18]` — bus de datos compartido del sistema

---

## BLOQUE B — OPERADORES Y PASOS

---

### N4. OPERADORES AHPL

#### Transferencia y conexión

| Operador | LaTeX | Nombre | Reloj |
|---|---|---|---|
| \( \leftarrow \) | `\leftarrow` | Transferencia — \( AC \leftarrow DR \) copia DR en AC al borde de reloj | Sí |
| \( = \) | `=` | Conexión de bus — \( IBUS = AC \) conecta AC al bus | No |
| \( * \) | `*` | Transferencia condicional — \( A * \overline{a} \leftarrow B \) (si \( a=0 \), transfiere B a A); \( D \leftarrow (A \mathop{!} B \mathop{!} C) * (f,\, g,\, h) \) (selecciona origen según control) | Sí |

#### Operadores lógicos

| Símbolo | LaTeX | Operación | Alternativa texto | Ejemplo |
|---|---|---|---|---|
| \( \land \) | `\land` | AND | `AND`, `&` | \( csrdy \land \overline{CSBUS_0} \) |
| \( \lor \) | `\lor` | OR | `OR`, `+` | \( busy \lor first \) |
| \( \oplus \) | `\oplus` | XOR | `XOR`, `@` | \( AC \oplus DR \) |
| \( \overline{X} \) | `\overline{X}` | NOT | `NOT`, `~` prefijo | \( \overline{CSBUS_0} \), \( \overline{accept} \) |

#### Selección de bits

| Notación | LaTeX | Significado | Ejemplo |
|---|---|---|---|
| \( REG_i \) | `REG_i` | Bit i del registro | \( IR_0 \), \( CR_7 \) |
| \( REG_{i:j} \) | `REG_{i:j}` | Bits i a j | \( IR_{8:17} \), \( D_{10:17} \) |

#### Operaciones aritméticas

| Notación | LaTeX | Operación | Ejemplo |
|---|---|---|---|
| \( INC(REG) \) | `INC(REG)` | Incremento | \( PC \leftarrow INC(PC) \) |
| \( ADD(A,B) \) | `ADD(A,B)` | Suma | \( AC \leftarrow ADD(AC, DR) \) |
| \( RETURN(REG) \) | `RETURN(REG)` | Complemento lógico | \( feed = RETURN(CR) \) |

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
→ (CSBUS₃, ~CSBUS₃, ~CSBUS₂)/(1, 1A, 3)
```

Formato: `→ (condición₁, condición₂, ...)/(destino₁, destino₂, ...)`

- Las condiciones son mutuamente excluyentes.
- Los destinos pueden ser números de paso (`1`, `3`) o etiquetas (`1A`, `3`).

#### Paso de bifurcación condicional

Evalúa una condición y salta según el resultado.

```
→ (ready)/(3)
→ (datavalid)/(1A)
→ (first, ~first)/(3A, 8A)
```

- Si la condición es verdadera → va al destino indicado.
- Si es falsa → continúa al siguiente paso numerado.
- Con dos destinos: `→ (f, ~f)/(D_yes, D_no)` — el segundo destino es para la negación.

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
2. DR ← IOBUS; accept = 1; first ← 1
```

Esto significa:
- `DR ← IOBUS` — DR toma el valor de IOBUS
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

**Ejemplo de uso de etiquetas — patrón genérico con bifurcación:**

```
3.  → (modo, ~modo)/(3A, 3B)

3A. REG ← IOBUS; flag ← 1
    → (5)

3B. REG ← 0; flag ← 0

4.  ...
5.  DEAD END
```

- `3.` — paso principal que bifurca según `modo`
- `3A.` — subpaso A (rama cuando `modo = 1`) — salta al paso 5 al terminar
- `3B.` — subpaso B (rama cuando `modo = 0`) — continúa al paso 4
- `(5)` en bifurcación — destino numérico; `(3A)` sería destino con letra sufijo

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

> En el libro, las barras se escriben tipográficamente sobre los símbolos (barra superior). En los bloques de código de esta guía se usa `~` como prefijo — por ejemplo `~CSBUS₀` — como sustitución tipográfica aceptada. En tablas KaTeX se usa `\overline{X}`.

---

## BLOQUE C — CHECKLIST

---

### N10. CHECKLIST ANTES DE ENTREGAR UN MÓDULO AHPL

Antes de escribir o completar un módulo, verificar:

- [ ] ¿El módulo tiene `MODULE:`, `MEMORY:`, `OUTPUTS:`, `INPUTS:`, `COMBUS:`?
- [ ] ¿Los registros vectoriales tienen tamaño entre corchetes? (`DR[18]`, no `DR`)
- [ ] ¿Las transferencias usan `←` y las conexiones de bus usan `=`?
- [ ] ¿Las operaciones simultáneas están en el **mismo paso** separadas por `;`?
- [ ] ¿Ningún registro destino aparece dos veces en el mismo paso?
- [ ] ¿Las bifurcaciones tienen formato `→ (condición)/(destino)`?
- [ ] ¿Las condiciones negadas usan `~` en bloques de código o `\overline{X}` en tablas KaTeX?
- [ ] ¿Los subpasos están etiquetados con letra sufijo (`1A`, `2A`)?
- [ ] ¿La secuencia termina con `DEAD END` o `END SEQUENCE`?
- [ ] ¿Las salidas combinacionales permanentes están después del `END SEQUENCE` y antes del `END`?
- [ ] ¿El módulo tiene `END` al final?

---

## BLOQUE D — BIBLIOTECA DE EJEMPLOS

---

### N11. MÓDULO COMPLETO — PRINTER INTERFACE

> Contexto para NotebookLM: módulo AHPL completo de la interface de impresora. Cubre el protocolo completo: handshake con IOBUS (datavalid/accept), carga de DR, acumulación en CR con `first`, envío a impresora (feed/print), y espera de `wait`. Fuente: Hill & Peterson Digital Systems 2ª ed., Example 9.3, p. 349-350.

```
MODULE: PRINTER INTERFACE
MEMORY: DR[18]; CR[8]; first(JK)
OUTPUTS: CHAR[8]; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS[18]
1. ready = 1
   → (~datavalid)/(1)
2. DR ← IOBUS; accept = 1; first ← 1
3. CR ← (DR₁₀:₁₇ ∧ first) ∨ (DR₁:₈ ∧ ~first)
4. feed = RETURN(CR); print = RETURN(CR)
5. Null
6. → (wait)/(6)
7. first ← 0
   → (first, ~first)/(3, 8)
8. DEAD END
END SEQUENCE
CHAR = CR
END
```

#### Lectura paso a paso

| Paso | Qué hace |
|---|---|
| `1.` | `ready = 1`. Bucle de espera mientras `datavalid = 0` — sale cuando `datavalid = 1`. |
| `2.` | \( DR \leftarrow IOBUS;\; accept = 1;\; first \leftarrow 1 \) — todo simultáneo. |
| `3.` | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) — acumula carácter en CR. |
| `4.` | \( feed = RETURN(CR);\; print = RETURN(CR) \) — envía señales a impresora. |
| `5.` | Paso nulo — sincronización. |
| `6.` | Bucle de espera mientras \( wait = 1 \) — sale cuando \( wait = 0 \). |
| `7.` | \( first \leftarrow 0 \). Bifurca: \( first = 1 \rightarrow 3 \), \( first = 0 \rightarrow 8 \). |
| `8.` | DEAD END. |
| `CHAR = CR` | Salida combinacional permanente: \( CHAR = CR \) en todo momento. |

---

### N12. PATRÓN — BUCLE DE ESPERA CON SEÑAL

> Contexto para NotebookLM: patrón de polling. El módulo permanece en el mismo paso hasta que una señal cambia de estado. Se usa para esperar `datavalid`, `wait`, `ready`, `accept`. El paso bifurca hacia sí mismo mientras la condición sea falsa (o verdadera, según el sentido).

```
% Espera mientras la señal es 0 (sale cuando es 1):
N.  → (~señal)/(N)

% Espera mientras la señal es 1 (sale cuando es 0):
N.  → (señal)/(N)

% Ejemplo concreto — esperar que datavalid sea 1:
1.  → (~datavalid)/(1)

% Ejemplo concreto — esperar que wait sea 0:
6.  → (wait)/(6)
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

### N14. PATRÓN — TRANSFERENCIA CONDICIONAL CON OPERADOR *

> Contexto para NotebookLM: el operador `*` indica transferencia condicional — la operación solo se ejecuta si la señal de control asociada vale 1. Puede aparecer en el lado izquierdo (destino condicionado) o en el lado derecho (selección de origen). Fuente: Hill & Peterson Digital Systems 2ª ed., sección 4.7, p. 105.

```
% Formato — condición en lado izquierdo:
A * ~a ← B

% Interpretación:
% Si a = 0 (~a = 1) → A ← B
% Si a = 1 (~a = 0) → no ocurre transferencia

% Dos transferencias condicionales simultáneas (p. 105):
2. A * ~a ← B ; D * a ← C

% Interpretación:
% Si a = 0 → A ← B
% Si a = 1 → D ← C

% Formato — selección de origen en lado derecho (row catenation):
D ← (A ! B ! C) * (f, g, h)

% Interpretación:
% Si f = 1 → D ← A
% Si g = 1 → D ← B
% Si h = 1 → D ← C
% Las condiciones f, g, h son mutuamente excluyentes
```

> El operador `!` en `(A ! B ! C)` es row catenation — concatena registros para formar un vector compuesto. No es complemento lógico. El operador `*` relaciona ese vector con el vector de control `(f, g, h)` para seleccionar cuál transferir.

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
