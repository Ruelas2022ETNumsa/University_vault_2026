---
title: AHPL — Guía unificada para ETN825 (LaTeX NotebookLM)
galaxy_body: beacon
scope: yyvaultyy
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
> **Nota de formato:** toda la notación AHPL usa KaTeX. Operadores, transferencias, señales y módulos completos se expresan en KaTeX inline \( \) o display \[ \]. No se usan bloques de código ni símbolos Unicode para notación matemática.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM escriba, complete o explique código AHPL correctamente. Cuando el usuario pida un módulo o secuencia AHPL, responder en KaTeX display — no con bloques de código, no con texto plano, no con símbolos Unicode.

### Defaults — cuando el usuario no especifica

- Formato: declaraciones primero, luego pasos numerados — todo en KaTeX display \[ \].
- Registros: mayúsculas (\( DR \), \( CR \), \( AC \), \( PC \), \( MR \)). Escalares: minúsculas (\( busy \), \( ready \), \( first \)).
- Transferencia: \( \leftarrow \) (asignación con reloj). Conexión de bus: \( = \) (sin reloj).
- Bifurcación fija: \( \rightarrow (D) \). Bifurcación condicional: \( \rightarrow (f)/(D) \) o \( \rightarrow (f,\, \overline{f})/(D_1, D_2) \).
- Condición negada: barra superior — \( \overline{X} \). Nunca barra pegada al símbolo ni Unicode.
- Paso nulo: \( \text{Null} \) — consume un ciclo de reloj sin operación.
- Fin de secuencia: \( \text{DEAD END} \) o \( \text{END SEQUENCE} \).

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

\[\textbf{MODULE: } \text{NOMBRE DEL MÓDULO}\]
\[\textbf{MEMORY: } \langle\text{registros internos con tamaño}\rangle\]
\[\textbf{OUTPUTS: } \langle\text{señales y registros de salida}\rangle\]
\[\textbf{INPUTS: } \langle\text{señales de entrada}\rangle\]
\[\textbf{COMBUSES: } \langle\text{buses combinacionales con tamaño}\rangle\]
\[1.\; \langle\text{paso 1}\rangle\]
\[2.\; \langle\text{paso 2}\rangle\]
\[\quad\vdots\]
\[N.\; \text{DEAD END} \quad (\text{o END SEQUENCE si retorna a otro módulo})\]
\[\langle\text{expresiones combinacionales fuera de la secuencia}\rangle\]
\[\textbf{END}\]

Reglas:

- \( \textbf{MODULE:} \) — nombre del módulo en mayúsculas, descriptivo.
- \( \textbf{MEMORY:} \) — registros que retienen valor entre ciclos de reloj (flip-flops). Vectores con tamaño: \( DR[18] \), \( CR[8] \). Escalares sin corchetes: \( busy \), \( first \).
- \( \textbf{OUTPUTS:} \) — señales o registros que salen del módulo. Con tamaño si son buses: \( CHAR[8] \). Booleanas sin corchetes: \( print \), \( feed \).
- \( \textbf{INPUTS:} \) — señales que entran desde otros módulos o dispositivos: \( wait \), \( csrdy \).
- \( \textbf{COMBUSES:} \) — buses combinacionales (sin reloj). Con tamaño y booleanas: \( IOBUS[18] \), \( CSBUS[12] \), \( ready \), \( datavalid \), \( accept \).

❌ Incorrecto — falta tamaño en registro:
\[ \textbf{MEMORY: } DR;\; CR;\; busy \]

✅ Correcto:
\[ \textbf{MEMORY: } DR[18];\; CR[8];\; busy;\; first \]

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

> **Diferencia clave:** `MEMORY` usa reloj — las transferencias \( \leftarrow \) solo se efectúan al borde de reloj. `COMBUSES` es combinacional — las conexiones \( = \) son inmediatas y no retienen valor.

---

### N3. ENTRADAS Y SALIDAS

| Sección | Qué declara | Dirección |
|---|---|---|
| `INPUTS` | Señales que llegan de otros módulos o dispositivos | \( \rightarrow \) hacia este módulo |
| `OUTPUTS` | Señales o registros que salen hacia otros módulos | \( \leftarrow \) desde este módulo |
| `COMBUSES` | Buses compartidos bidireccionales o señales de handshake | \( \leftrightarrow \) bidireccional |

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

| Operador | LaTeX | Nombre | Reloj |
|---|---|---|---|
| \( \leftarrow \) | `\leftarrow` | Transferencia — \( AC \leftarrow DR \) copia DR en AC al borde de reloj | Sí |
| \( = \) | `=` | Conexión de bus — \( IBUS = AC \) conecta AC al bus | No |
| \( * \) | `*` | Producto condicional — \( CR \leftarrow (D_{10:17}!) * (first,\, \overline{first}) \) | Sí |

#### Operadores lógicos

| Símbolo | LaTeX | Operación | Alternativa texto | Ejemplo |
|---|---|---|---|---|
| \( \land \) | `\land` | AND | `AND`, `&` | \( csrdy \land \overline{CSBUS_0} \) |
| \( \lor \) | `\lor` | OR | `OR`, `+` | \( busy \lor first \) |
| \( \oplus \) | `\oplus` | XOR | `XOR`, `@` | \( AC \oplus DR \) |
| \( \overline{X} \) | `\overline{X}` | NOT | `NOT`, `!` al final | \( \overline{CSBUS_0} \), \( \overline{accept} \) |

#### Selección de bits

| Notación | LaTeX | Significado | Ejemplo |
|---|---|---|---|
| \( REG_i \) | `REG_i` | Bit i del registro | \( IR_0 \), \( CR_7 \) |
| \( REG_{i:j} \) | `REG_{i:j}` | Bits i a j | \( IR_{8:17} \), \( D_{10:17} \) |
| \( REG_{i:j}! \) | `REG_{i:j}!` | Bits i a j, complementados | \( D_{10:17}! \) — NOT de esa porción |

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

\[ 4.\; CSBUS_0 = busy;\; datavalid = 1 \]

> El punto y coma \( ; \) dentro de un paso separa **operaciones simultáneas** que ocurren en el mismo ciclo de reloj.

#### Paso de bifurcación fija

Va incondicionalmente al paso indicado. No ejecuta operación.

\[ \rightarrow (\overline{CSBUS_3},\; CSBUS_3 \land \overline{CSBUS_3},\; CSBUS_3)/(1,\; 1A,\; 3) \]

Formato: \( \rightarrow (\text{cond}_1, \text{cond}_2, \ldots)/(\text{dest}_1, \text{dest}_2, \ldots) \)

- Las condiciones son mutuamente excluyentes.
- Los destinos pueden ser números de paso (\( 1 \), \( 3 \)) o etiquetas (\( 1A \), \( 3A \)).

#### Paso de bifurcación condicional

Evalúa una condición y salta según el resultado.

\[ \rightarrow (ready)/(3) \]
\[ \rightarrow (datavalid)/(1A) \]
\[ \rightarrow (first,\; \overline{first})/(3A,\; 8A) \]

- Si la condición es verdadera → va al destino indicado.
- Si es falsa → continúa al siguiente paso numerado.
- Con dos destinos: \( \rightarrow (f,\; \overline{f})/(D_{yes},\; D_{no}) \).

#### Paso nulo

Consume un ciclo sin operación. Útil para sincronización.

\[ 5A.\; \text{Null} \]

#### Fin de secuencia

\[ \text{DEAD END} \quad \leftarrow \text{el módulo se detiene, no retorna} \]
\[ \text{END SEQUENCE} \quad \leftarrow \text{la secuencia termina y puede reiniciarse} \]

---

### N6. OPERACIONES SIMULTÁNEAS EN UN PASO

Varias transferencias en el mismo paso se ejecutan **todas al mismo tiempo** en el mismo ciclo de reloj.

\[ 2A.\; DR \leftarrow IOBUS;\; busy \leftarrow 1;\; accept = 1;\; first \leftarrow 1 \]

Esto significa:
- \( DR \leftarrow IOBUS \) — DR toma el valor de IOBUS
- \( busy \leftarrow 1 \) — busy se pone en 1
- \( accept = 1 \) — accept se activa (combinacional, inmediato)
- \( first \leftarrow 1 \) — first se pone en 1

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

\[\rightarrow (\overline{CSBUS_3},\; CSBUS_3 \land \overline{CSBUS_3},\; CSBUS_3)/(1,\; 1A,\; 3)\]
\[\ldots\]
\[1A.\; ready = 1;\; \rightarrow (\overline{datavalid})/(1A)\]
\[2A.\; DR \leftarrow IOBUS;\; busy \leftarrow 1;\; accept = 1;\; first \leftarrow 1\]
\[3A.\; CR \leftarrow (D_{10:17}!) * (first,\; \overline{first})\]

---

### N8. EXPRESIONES COMBINACIONALES FUERA DE LA SECUENCIA

Algunas salidas se definen como expresiones combinacionales **después del END SEQUENCE**, antes del \( \textbf{END} \) del módulo. No son pasos — son definiciones permanentes.

\[\text{END SEQUENCE}\]
\[CHAR = CR\]
\[\textbf{END}\]

- \( CHAR = CR \) — la salida CHAR es siempre igual al contenido de CR (combinacional, no sincrónico).
- Se usan para salidas que deben reflejar el estado actual del registro en todo momento.

---

### N9. NOTACIÓN DE CONDICIÓN COMPUESTA Y SEÑALES NEGADAS

Las condiciones de bifurcación pueden combinar señales con AND \( (\land) \) o usar señales negadas con barra superior.

\[ 1.\; \rightarrow (csrdy \land \overline{CSBUS_0} \land CSBUS_1 \land \overline{CSBUS_2})/(1) \]

Interpretación:
- \( csrdy \) — csrdy = 1
- \( \overline{CSBUS_0} \) — bit 0 del CSBUS = 0 (negado)
- \( CSBUS_1 \) — bit 1 del CSBUS = 1
- \( \overline{CSBUS_2} \) — bit 2 del CSBUS = 0 (negado)
- Toda la condición: \( csrdy \land \overline{CSBUS_0} \land CSBUS_1 \land \overline{CSBUS_2} \)
- Si la condición es **falsa** → va al paso \( (1) \) (bucle de espera).
- Si es **verdadera** → continúa al paso 2.

> La barra superior \( \overline{X} \) es el único formato válido para el negado. No usar Unicode ni barra pegada al símbolo.

---

## BLOQUE C — CHECKLIST

---

### N10. CHECKLIST ANTES DE ENTREGAR UN MÓDULO AHPL

Antes de escribir o completar un módulo, verificar:

- [ ] ¿El módulo tiene \( \textbf{MODULE:} \), \( \textbf{MEMORY:} \), \( \textbf{OUTPUTS:} \), \( \textbf{INPUTS:} \), \( \textbf{COMBUSES:} \)?
- [ ] ¿Los registros vectoriales tienen tamaño entre corchetes? (\( DR[18] \), no \( DR \))
- [ ] ¿Las transferencias usan \( \leftarrow \) y las conexiones de bus usan \( = \)?
- [ ] ¿Las operaciones simultáneas están en el **mismo paso** separadas por \( ; \)?
- [ ] ¿Ningún registro destino aparece dos veces en el mismo paso?
- [ ] ¿Las bifurcaciones tienen formato \( \rightarrow (\text{condición})/(\text{destino}) \)?
- [ ] ¿Las condiciones negadas usan \( \overline{X} \)? (sin Unicode, sin barra pegada)
- [ ] ¿Los subpasos están etiquetados con letra sufijo (\( 1A \), \( 2A \))?
- [ ] ¿La secuencia termina con \( \text{DEAD END} \) o \( \text{END SEQUENCE} \)?
- [ ] ¿Las salidas combinacionales permanentes están después del \( \text{END SEQUENCE} \) y antes del \( \textbf{END} \)?
- [ ] ¿Toda la notación está en KaTeX? (sin bloques de código, sin Unicode, sin texto plano para operadores)

---

## BLOQUE D — BIBLIOTECA DE EJEMPLOS

---

### N11. MÓDULO COMPLETO — PRINTER INTERFACE

> Contexto para NotebookLM: módulo AHPL completo de la interface de impresora. Cubre el protocolo completo: espera de dirección en CSBUS, handshake con IOBUS (datavalid/accept), carga de DR, acumulación en CR con \( first \), envío a impresora (feed/print), y espera de \( wait \). Fuente: Hill & Peterson Digital Systems 2ª ed., material del docente ETN825.

\[\textbf{MODULE: PRINTER INTERFACE}\]
\[\textbf{MEMORY: } DR[18];\; CR[8];\; busy;\; first\]
\[\textbf{OUTPUTS: } CHAR[8];\; print;\; feed\]
\[\textbf{INPUTS: } wait;\; csrdy\]
\[\textbf{COMBUSES: } IOBUS[18];\; CSBUS[12];\; ready;\; datavalid;\; accept\]
\[1.\; \rightarrow (csrdy \land \overline{CSBUS_0} \land CSBUS_1 \land \overline{CSBUS_2})/(1)\]
\[2.\; accept = 1;\; \rightarrow (\overline{CSBUS_3},\; \overline{CSBUS_3},\; CSBUS_3)/(1,\; 1A,\; 3)\]
\[3.\; \rightarrow (\overline{ready})/(3)\]
\[4.\; CSBUS_0 = busy;\; datavalid = 1;\; \rightarrow (\overline{accept},\; accept)/(4,\; 1)\]
\[1A.\; ready = 1;\; \rightarrow (\overline{datavalid})/(1A)\]
\[2A.\; DR \leftarrow IOBUS;\; busy \leftarrow 1;\; accept = 1;\; first \leftarrow 1\]
\[3A.\; CR \leftarrow (D_{10:17}!) * (first,\; \overline{first})\]
\[4A.\; feed = RETURN(CR);\; print = RETURN(CR)\]
\[5A.\; \text{Null}\]
\[6A.\; \rightarrow (wait)/(6A)\]
\[7A.\; first \leftarrow 0;\; busy * \overline{first} \leftarrow 0;\; \rightarrow (first,\; \overline{first})/(3A,\; 8A)\]
\[8A.\; \text{DEAD END}\]
\[\text{END SEQUENCE}\]
\[CHAR = CR\]
\[\textbf{END}\]

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
| `7A.` | Pone \( first \leftarrow 0 \) y borra \( busy * \overline{first} \). Bifurca: si \( first = 1 \) vuelve a 3A, si no va a 8A. |
| `8A.` | DEAD END — módulo detenido hasta nuevo llamado. |
| `CHAR=CR` | Salida combinacional permanente: CHAR siempre refleja el contenido de CR. |

---

### N12. PATRÓN — BUCLE DE ESPERA CON SEÑAL

> Contexto para NotebookLM: patrón de polling. El módulo permanece en el mismo paso hasta que una señal cambia de estado.

\[\text{Espera mientras la señal es 0 (sale cuando es 1):}\]
\[N.\; \rightarrow (\overline{\text{señal}})/(N)\]
\[\text{Espera mientras la señal es 1 (sale cuando es 0):}\]
\[N.\; \rightarrow (\text{señal})/(N)\]
\[\text{Ejemplo — esperar que } ready = 1:\]
\[3.\; \rightarrow (\overline{ready})/(3)\]
\[\text{Ejemplo — esperar que } wait = 0:\]
\[6A.\; \rightarrow (wait)/(6A)\]

---

### N13. PATRÓN — BIFURCACIÓN MÚLTIPLE POR BITS DE BUS

> Contexto para NotebookLM: bifurcación a más de dos destinos según combinación de bits de un bus. Las condiciones son mutuamente excluyentes.

\[\text{Formato general:}\]
\[\rightarrow (\text{cond}_1,\; \text{cond}_2,\; \text{cond}_3)/(\text{dest}_1,\; \text{dest}_2,\; \text{dest}_3)\]
\[\text{Ejemplo — decodificación por } CSBUS_3:\]
\[\rightarrow (\overline{CSBUS_3},\; \overline{CSBUS_3},\; CSBUS_3)/(1,\; 1A,\; 3)\]
\[\text{Ejemplo — decodificación de instrucción por } IR_0:\]
\[\rightarrow (\overline{IR_0},\; IR_0)/(fetch,\; execute)\]
\[\text{Ejemplo — bifurcación triple por } IR_{0:1}:\]
\[\rightarrow (IR_0 \land \overline{IR_1},\; \overline{IR_0} \land IR_1,\; IR_0 \land IR_1)/(A,\; B,\; C)\]

> Regla: la suma lógica de todas las condiciones debe ser 1. Si ninguna se cumple, el comportamiento es indefinido.

---

### N14. PATRÓN — OPERACIÓN CONDICIONAL CON PRODUCTO *

> Contexto para NotebookLM: el operador \( * \) (producto condicional) permite cargar un registro con uno de dos valores según una condición booleana, en un único paso sincrónico.

\[\text{Formato:}\]
\[REG \leftarrow (\text{expresión}!) * (cond,\; \overline{cond})\]
\[\text{Interpretación:}\]
\[\text{Si } cond = 1 \Rightarrow REG \leftarrow \text{expresión}\]
\[\text{Si } cond = 0 \Rightarrow REG \leftarrow 0\]
\[\text{Ejemplo del módulo PRINTER INTERFACE:}\]
\[3A.\; CR \leftarrow (D_{10:17}!) * (first,\; \overline{first})\]
\[\text{Si } first = 1 \Rightarrow CR \leftarrow \overline{D_{10:17}}\]
\[\text{Si } first = 0 \Rightarrow CR \leftarrow 0\]

> El \( ! \) después de la expresión indica complemento lógico bit a bit de ese rango.

---

### N15. PATRÓN — SALIDA COMBINACIONAL PERMANENTE (fuera de secuencia)

> Contexto para NotebookLM: las expresiones después de \( \text{END SEQUENCE} \) y antes del \( \textbf{END} \) son salidas combinacionales que el módulo mantiene en todo momento, sin reloj.

\[\text{Formato:}\]
\[\text{END SEQUENCE}\]
\[SALIDA = \text{expresión}\]
\[\textbf{END}\]
\[\text{Ejemplo — CHAR siempre refleja CR:}\]
\[\text{END SEQUENCE}\]
\[CHAR = CR\]
\[\textbf{END}\]
\[\text{Ejemplo con salida negada: } CHAR = \overline{CR}\]
\[\text{Ejemplo con selección de bits: } CHAR = CR_{0:7}\]

> Diferencia con transferencia en paso: \( CR \leftarrow valor \) ocurre una vez al borde de reloj. \( CHAR = CR \) es continuo — si CR cambia, CHAR cambia en el mismo instante.

---

---

### N16. MÓDULO COMPLETO — CONTROLADOR DE MÁQUINAS-HERRAMIENTA

> Contexto para NotebookLM: módulo AHPL de un controlador de máquinas-herramienta con ROM de programa. Cubre: selección de secuencia desde SQR, direccionamiento de ROM con AR, carga de instrucción en PR, detección de fin de secuencia por reducción AND, control de flip-flop ss con producto condicional fuera de secuencia. Fuente: Hill & Peterson Digital Systems 2ª ed., material del docente ETN825.

\[\textbf{MODULE: CONTROLADOR DE MÁQUINAS-HERRAMIENTA}\]
\[\textbf{MEMORY: } ROM[1024,\,18];\; PR[18];\; AR[10];\; SQR[2];\; ss\]
\[\textbf{INPUTS: } SEQ[2];\; start;\; stop\]
\[\textbf{OUTPUTS: } OPR[18]\]
\[1.\; SQR \leftarrow SEQ\]
\[\quad\rightarrow (\overline{ss},\, ss)/(1,\,2)\]
\[2.\; AR \leftarrow SQR_0,\, SQR_1,\, 8T0\]
\[3.\; PR \leftarrow BUSFN(ROM;\, DCD(AR))\]
\[4.\; AR \leftarrow INC(AR)\]
\[\quad\rightarrow \bigl((\bigwedge\!/ AR_{2:9} \land ss),\;\overline{ss},\;\overline{(\bigwedge\!/ AR_{2:9} \land ss)}\bigr)/(5,\,6,\,3)\]
\[5.\; ss \leftarrow 0\]
\[6.\; PR \leftarrow 18T0\]
\[\quad\rightarrow (1)\]
\[\text{END SEQUENCE}\]
\[ss * (start \lor stop) \leftarrow (1{!}0) * (start,\, stop)\]
\[OPR = PR\]
\[\textbf{END}\]

#### Lectura paso a paso

| Paso | Qué hace |
|---|---|
| `1.` | Carga SQR con la secuencia seleccionada (SEQ). Bifurca: si ss=0 → vuelve a 1 (espera start), si ss=1 → va a 2. |
| `2.` | Carga AR con la dirección base: bits altos = SQR₀,SQR₁ (selecciona bloque de 256), bits bajos = 8 ceros. |
| `3.` | Lee ROM en la dirección AR y carga la instrucción en PR usando BUSFN con decodificador DCD. |
| `4.` | Incrementa AR. Bifurca: si reducción AND de AR₂₋₉ = 1 y ss=1 → fin de secuencia (5), si ss=0 → reset (6), si no → sigue leyendo (3). |
| `5.` | Pone ss=0 — fin del ciclo de ejecución. |
| `6.` | Resetea PR a cero y vuelve al inicio (1). |
| `ss*(start∨stop)` | Fuera de secuencia: producto condicional — si start=1 → ss←1 (activa máquina), si stop=1 → ss←0 (detiene). |
| `OPR=PR` | Salida combinacional permanente: OPR siempre refleja el contenido de PR. |

#### Patrones nuevos en este módulo

**`ROM[1024, 18]`** — memoria declarada en MEMORY con dos parámetros: cantidad de palabras y ancho en bits.

\[ \textbf{MEMORY: } ROM[1024,\,18] \]

**`8T0` / `18T0`** — constante de N bits todos en cero.

\[ AR \leftarrow SQR_0,\, SQR_1,\, 8T0 \quad \leftarrow \text{concatenación: 2 bits de SQR + 8 ceros} \]
\[ PR \leftarrow 18T0 \quad \leftarrow \text{reset: 18 bits en cero} \]

**`BUSFN(ROM; DCD(AR))`** — función de bus: selecciona la palabra de ROM apuntada por el decodificador de AR.

\[ PR \leftarrow BUSFN(ROM;\, DCD(AR)) \]

**`∧/REG_{i:j}`** — reducción AND: es 1 solo si todos los bits del rango son 1. Detecta fin de conteo.

\[ \bigwedge\!/ AR_{2:9} = 1 \quad \Leftrightarrow \quad AR_{2:9} = 11111111_2 \]

**Producto condicional fuera de secuencia** — permite actualizar un flip-flop desde señales externas de forma continua.

\[ ss * (start \lor stop) \leftarrow (1{!}0) * (start,\, stop) \]

> Si start=1 → ss←1 (arranca la máquina). Si stop=1 → ss←0 (detiene). El operador `!` indica complemento: `1!0` = NOT de `10` binario.

---

%%
# galaxy-links
[[_app/notebooklm/guides/ETN825/ETN825_tikz.md]]
[[_library_ETN825]]
%%
