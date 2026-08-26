---
title: "Biblioteca ETN825 — Guía de libros"
galaxy_body: beacon
scope: vault
audience: usuario
related_notes:
  - "[[_config/_library-system]]"
tags: [beacon, library, ETN825, infraestructura]
date_created: 2026-07-29
date_updated: 2026-08-26
_last_edit: 2026-08-26 — Temario oficial incorporado; T8/T9/T10 movidos a complementarios; Temario 2021 eliminado; 5 libros nuevos agregados al stack (Perez VHDL, Stallings OS, Silberschatz OS, Tanenbaum Distributed, Hauck Reconfigurable)
status: desarollo
---

# 📚 Biblioteca ETN825 — Guía de libros

## Propósito

Este archivo es tu referencia personal para saber qué libro usar en cada tema de ETN825.

---

## Temario 2026_1 — Semestre más reciente

> ✅ Temario oficial recibido del docente — 2026-08-26.

### T1 — LENGUAJE DE PROGRAMACIÓN EN HARDWARE (HDL)
- 1.1 Organización y Arquitectura del Computador SIC. (24 pasos).

### T2 — COMUNICACIÓN ENTRE SISTEMAS
- 2.1 Operaciones en Paralelo.
- 2.2 Módulos Interactuantes.
- 2.3 Sincronización.
- 2.4 Interconexión de Sistemas.
- 2.5 Interface de Impresora, Secuencia Iniciada por la Impresora.
- 2.6 Comunicación Intersistemas, Respondiente y No-Respondiente.
- 2.7 Comunicación entre un Módulo Master y Otro Arbitrario.
- 2.8 Interface de Impresora, Secuencia Iniciada por la CPU.

### T3 — INTERRUPCIONES Y SISTEMA I/O
- 3.1 Interrupciones.
- 3.2 Secuencia de Interrupción.
- 3.3 Operaciones Para Transferencia de Datos.
- 3.4 Transferencia de Datos Mediante Programa.
- 3.5 Flujograma Secuencia I/O.
- 3.6 Descripción Secuencia AHPL por Programa.
- 3.7 Transferencia de Datos Mediante Buffer.
- 3.8 Flujograma Secuencia Buffer.
- 3.9 Descripción Secuencia AHPL Buffer.
- 3.10 Introducción Secuencia DMA.

### T4 — INTERFACES Y PERIFÉRICOS
- 4.1 Interface Genérica de Periféricos que se Conectan al Computador.
- 4.2 Interface Simplificada.
- 4.3 Interface de Unidad de Cinta.

### T5 — ADMINISTRACIÓN DE MEMORIA PARA GRANDES SISTEMAS
- 5.1 Introducción.
- 5.2 Memoria Stack.
- 5.3 Memoria Asociativa.
- 5.4 Memoria Buffer (Caché).
- 5.5 Memoria Virtual.
- 5.6 Bancos de Memoria Múltiple.
- 5.7 Bancos de Memoria Múltiple con Accesos Múltiples.

### T6 — AVANCES EN LA TECNOLOGÍA DE LAS COMPUTADORAS
- 6.1 Introducción.
- 6.2 Desempeño.
- 6.3 El Límite de la Potencia Disipada.
- 6.4 De los Monoprocesadores a los Multiprocesadores.

### SEGUNDA PARTE — PROCESADORES AVANZADOS
- Investigación bibliográfica sobre últimos avances en organización y arquitectura.
- Utilización de lenguajes de descripción de Hardware cuando sea necesario.
- Exposición y debate en clases.

### SEGUNDA PARTE — COMPUTACIÓN RECONFIGURABLE
- Estructura Computacional.
- Arreglo de Interconexiones.
- Configuración.
- Arquitecturas de Computación Reconfigurable.
- Integración a Sistemas de Computación Tradicionales.

### SEGUNDA PARTE — ENTRADA SALIDA EN COMPUTADORES COMERCIALES (Stallings)
- Dispositivos externos.
- Módulos de E/S.
- E/S programada.
- E/S mediante interrupciones.
- Acceso directo a memoria.
- Canales y procesadores de E/S.

---

## Temas complementarios (no evaluados)

> Temas inferidos en sesión anterior — no forman parte del temario oficial 2026_1 ni entran al examen. Se mantienen como referencia de contexto y profundización opcional.

### T8 — Diseño de sistemas de memoria
- Memoria virtual y paginación
- Diseño de memoria caché: políticas de reemplazo, políticas de escritura
- Diseño de memoria virtual: traducción de direcciones, administración de páginas, tamaño de página

### T9 — Diseño de sistemas de entrada/salida
- Interface de entrada/salida: registros de control, buffers de datos
- Métodos de transferencia de datos: programada, interrupciones, DMA, interfaz serie y paralelo
- Controladores de dispositivos: tarjetas de expansión, buses de expansión
- Protocolo de comunicaciones: RS-232, USB, Ethernet, PCI

### T10 — Diseño de sistemas multiprocesador
- Sistemas multiprocesador: definición, tipos y características
- Arquitectura de sistemas multiprocesador: simétrica, asimétrica y numérica
- Interconexión de sistemas multiprocesador: topologías, enrutamiento y latencia
- Sincronización y coordinación en sistemas multiprocesador
- Sistemas de memoria compartida y distribuida

---

## Stack completo

| Libro | Rol | Idioma |
|---|---|---|
| Hill, F.J. & Peterson, G.R. — Digital Systems: Hardware Organization and Design — 2ª ed. (1978) | AHPL principal — fuente primaria de T1, T2, T3, T4 | Inglés |
| Hill, F.J. & Peterson, G.R. — Introduction to Switching Theory and Logical Design — 3ª ed. (1981) | Base previa a AHPL — fundamentos RTL | Inglés |
| Stallings, W. — Computer Organization and Architecture: Designing for Performance — 11ª ed. (2019) | Teoría principal Bloque A — T1, T3, T4, T5, T6 | Inglés |
| Stallings, W. — Organización y Arquitectura de Computadores — 7ª ed. (2007) | Puente lingüístico Bloque A | Español |
| Hamacher, V.C. et al. — Computer Organization and Embedded Systems — 6ª ed. (2012) | Segunda opinión Bloque A — fuerte en T2, T3 | Inglés |
| Hennessy, J.L. & Patterson, D.A. — Computer Architecture: A Quantitative Approach — 6ª ed. (2017) | Teoría rigurosa — T5, T6 | Inglés |
| Patterson, D.A. & Hennessy, J.L. — Computer Organization and Design: The Hardware/Software Interface — 5ª ed. (2014) | Puente didáctico entre Stallings y Quantitative | Inglés |
| Carter, N. — Schaum's Outline of Computer Architecture — 1ª ed. (2002) | Problemas resueltos — T1, T3, T5 | Inglés |
| Mano, M.M. — Computer System Architecture — 3ª ed. (1993) — Adaptación india Dorling Kindersley 2007 (ISBN: 0131755633) | Segunda opinión — T3/T4 (Cap. 11: I/O, interrupciones, DMA, serial), T5 (Cap. 12: memoria, caché, virtual), T6 (Cap. 13: multiprocesadores) — PDF completo 539 pp. ✅ | Inglés |
| Stallings, W. — Data and Computer Communications — 10ª ed. (2013) | Teoría principal Bloque B — T2 paralelo/serie | Inglés |
| Stallings, W. — Comunicaciones y Redes de Computadores — 6ª ed. | Puente lingüístico Bloque B | Español |
| Forouzan, B.A. — Data Communications and Networking — 5ª ed. (2013) | Segunda opinión Bloque B — más didáctico | Inglés |
| Stevens, W.R. & Fall, K.R. — TCP/IP Illustrated, Vol. 1: The Protocols — 2ª ed. (2011) | Complemento TCP/IP — consulta puntual | Inglés |
| Tanenbaum, A.S. & Wetherall, D.J. — Computer Networks — 5ª ed. (2010) | Complemento redes — T6 multiprocesadores/dist. | Inglés |
| Langdon, G.G. Jr. — Computer Design — 1ª ed. (1982) | Complemento AHPL — segunda opinión RTL | Inglés |
| Hill, F.J. & Peterson, G.R. — Digital Systems: Hardware Organization and Design — 1ª ed. (1973) | Apoyo AHPL — primera formulación del lenguaje | Inglés |
| Perez, Soto, Fernandez — Diseño de sistemas digitales con VHDL — 1ª ed. (2002) — Thomson | VHDL — Segunda Parte: contexto HDL moderno vs AHPL | Español |
| Stallings, W. — Operating Systems Internals and Design Principles — 8ª ed. (2015) — Pearson | Contexto SO — interrupciones y DMA desde perspectiva de SO | Inglés |
| Silberschatz, A. et al. — Operating System Concepts — 10ª ed. (2018) — Wiley | Consulta puntual SO — complemento a Stallings OS | Inglés |
| Tanenbaum, A.S. & Van Steen, M. — Distributed Systems Principles and Paradigms — 2ª ed. (2007) — Pearson | Contexto sistemas distribuidos — T6 multiprocesadores | Inglés |
| Hauck, S. & DeHon, A. — Reconfigurable Computing The Theory and Practice — 1ª ed. (2008) — Elsevier | Segunda Parte: Computación Reconfigurable | Inglés |

---

## Complementos (PDFs / resúmenes)

Archivos adicionales que no son libros completos pero aportan valor puntual a NotebookLM.

| Archivo                                                        | Contenido                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Temas      |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `ETN825-Hill-Peterson-Resumen-Docente-ESP` | Resumen elaborado por el docente basado en Hill & Peterson Digital Systems 2ª ed. En español. Cubre comunicación entre sistemas, operaciones en paralelo, módulos interactuantes, sincronización, interconexión (IOBUS/CSBUS), handshake respondiente/no-respondiente, interfaces de impresora con módulo AHPL completo, interrupciones (flags, MR, vectorial/no-vectorial, PSR/PSW), transferencia de datos (programada, Buffer, DMA) con flujogramas y secuencias AHPL, interfaces y periféricos (interface SIC genérica, simplificada, lectora de cinta), administración de memoria (Stack, Asociativa, Buffer/Caché, Virtual, Bancos múltiples). ⚠️ Sin numeración de página ni etiquetas en imágenes — afecta extracción por referencia específica pero no consultas conceptuales. Sirve como puente al español y refleja el criterio del docente sobre qué es relevante. | T1, T2, T3, T4, T5 |
| `AHPL-Resumen-Garcia-Vargas-basado-Hill-Peterson-3ed`          | Resumen completo de AHPL basado en Hill & Peterson 3ª ed. Cubre convención de operandos (escalares, vectores, matrices), operadores booleanos y de reducción, declaraciones con reloj, estructura de módulos (NAME, MEMORY, INPUTS, OUTPUTS, BUSES, CLUNITS), secuencia de control con pasos numerados y saltos, descripción de unidades lógicas combinatorias (CLUNIT). Incluye ejemplos resueltos: fetch routine, DATA SELECTOR, FULLADD.                                                                                   | T1, T2, T3 |
| `AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales` | Diapositivas académicas. Complementa el resumen anterior con sintaxis alternativa de operadores (`&` AND, `+` OR, `@` XOR), operadores relacionales (NE, EQ, GT, GE, LT, LE), transferencias condicionales con múltiples registros fuente/destino, manejo de arreglos RAM con DCD(AR), y mapeo AHPL → VHDL. Útil para comparar con VHDL si el docente lo menciona.                                                                                                                                                            | T1, T2     |
| `AHPL-Teoria-Base-Rocasalvo-ETN821`                            | Teoría base de AHPL elaborada por el auxiliar Rocasalvo para ETN-821. Cubre la arquitectura de dos secciones (circuito secuencial de control + registro de datos y lógica), diferencia entre conexiones (`=`) y transferencias (`←`), operaciones lógicas (AND, OR, XOR, NOT), reducción, concatenación, rotaciones, suma, resta, incremento, codificación, operaciones condicionadas por derecha e izquierda, condiciones de bifurcación y diagramas de tiempo. Incluye diagramas de circuito real (flip-flops, compuertas). | T1, T2     |
| `SIC-ModuloAHPL-47Pasos-Original-y-Explicado`                  | El módulo SIC completo escrito en AHPL en dos versiones: código original con los 47 pasos y versión comentada con explicación de cada bloque (fetch, decodificación, modos de direccionamiento, ALU, instrucciones operativas, rotaciones, saltos). Incluye la tabla de nemónicos IR0-IR2 y flujograma de flujo de control. Fuente primaria para entender cómo se construye el SIC en AHPL.                                                                                                                                   | T1         |
| `SIC-Ejercicios-Resueltos-Rocasalvo-ETN821`                    | Guía de ejercicios resueltos del SIC elaborada por el auxiliar Rocasalvo para ETN-821. Cubre programación paso a paso con tablas de registros y direcciones usando las instrucciones LAC, DAC, CMA, AND, TAD, RAL, RAR, ISZ, JMP, JMS, SKZ, SKP, SZL, CLL, CLA, HLT. Incluye ejercicios con direccionamiento directo, indexado, indirecto y subrutinas.                                                                                                                                                                       | T1, T2     |
| `SIC-Ejercicios-Resueltos-y-ModificacionesAHPL-ETN821`         | Colección de ejercicios resueltos con dos bloques: (1) programación SIC con direccionamiento indexado, indirecto, subrutinas, rotaciones, paridad, inversión de bits, máximo, sumatoria y multiplicación; (2) modificaciones del AHPL de 24 pasos incluyendo cambios en ISZ, incorporación de XOR/OREX, nueva instrucción JMPAC y reconfiguración completa de la tabla de nemónicos IR0-IR2.                                                                                                                                  | T1, T2     |


### Chatgpt
| Archivo                                                        | Contenido                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Temas      |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `introduccion_ahpl_transferencia_registros`                    | Presentación de diapositivas académicas (23 slides, EMI — Ing. Arturo Marín Thames). Cubre: concepto de transferencia de registros (notación ←, letras mayúsculas), sincronización por reloj maestro (combinación AND CLK+SCN → CSP/SCI), implementación hardware de transferencia AR→BR con flip-flops D, transferencias múltiples a un registro (SCN1/SCN2/SCN3 → DR con compuertas AND/OR), operaciones set/clear (AC←0,0,0,0 / AC←1,1,1,1), operaciones simultáneas, selección de bits individuales con subíndices (DR[2:3], CR[0]←AR[3:5]), operaciones lógicas (complemento, OR, AND) con diagramas de circuito, bus de registros (problema costo AND/OR directas, solución IBUS, dos pasos IBUS=AR / DR←IBUS), diagrama de tiempos de transferencia por bus, notación simplificada de red de bus, y secuenciación de control (formato →(f1,f2,...,fk)/(D1,...,Dn) con ejemplos IR[0] y FF s). ✅ Descripción de GPT verificada contra PDF — correcta en lo sustancial. ⚠️ Corregido: el PDF no menciona el computador SIC en ninguna slide — es base de AHPL general, no del SIC específicamente. | T1         |

| `ahpl_diseno_sistemas_digitales`                               | Documento teórico (31 pp.) que introduce AHPL para describir y diseñar sistemas digitales. Cubre: transferencia de registros (notación ←, flip-flops D, sincronización), buses internos (IBUS, símbolo =) y buses de interconexión entre sistemas, secuenciamiento de control (bifurcaciones fijas y condicionales →(D)/→(F)/(S)), transferencias condicionales con asterisco (\*), convención de operandos (escalares, vectores, matrices), operadores AHPL (NOT/AND/OR/XOR, encadenar, reducción, compresión, codificación binaria), lógica combinacional (CLUNIT/LOGIC, FULLADD, ADD, COMP), estructura de módulos (MEMORY, INPUTS, OUTPUTS, BUSES, LABELS, ONE SHOTS), sentencias completas (DV←OCLV, BUS=OCLV, DEAD END, NO DELAY), subsistemas asincrónicos (SYN), reducción por estudio de tiempos, y manejo de RAM/ROM con DCD(AR) y BUSFN. Incluye ejemplos completos: sistema retransmisor, DATA SELECTOR, controlador ROM de máquinas-herramienta. ✅ Descripción de GPT verificada contra PDF — sustancialmente correcta. ⚠️ T5 corregido: el PDF cubre acceso a RAM/ROM en AHPL (DCD, BUSFN) pero NO memoria virtual, caché ni paginación — no reemplaza a Stallings para T5 del temario 2026. | T1, T2 |

---

## Archivos divididos

| Libro | PDF | Capítulos | Contenido | Temas |
|---|---|---|---|---|
| Hill & Peterson — Digital Systems 2ª ed. | PDF 1 | 2, 4, 5, 6 | Registros, transferencias, AHPL básico, secuencia de control | T1 |
| Hill & Peterson — Digital Systems 2ª ed. | PDF 2 | 7 | Computador SIC completo — los 24 pasos | T1 |
| Hill & Peterson — Digital Systems 2ª ed. | PDF 3 | 9, 10, 11, 13 | Comunicación entre módulos, interfaces, I/O, interrupciones | T2, T3, T4 |

### Capítulos faltantes

| Capítulo | Contenido | Relevancia | Cobertura alternativa |
|---|---|---|---|
| 1 | Introducción y fundamentos digitales | Baja | Complementos AHPL ya cubren la base |
| 3 | Lógica combinacional en AHPL | Media | Cubierto parcialmente por los resúmenes de complementos |
| 8 | Memoria | Alta — T5 | Stallings COA 11ª ed. |
| 12 | Multiprocesadores / sistemas avanzados | Media — T6 | Stallings COA 11ª ed. + Hennessy & Patterson |

---

## Qué usar por tema

### Parcial 1 — AHPL y Comunicación (T1, T2)

| Tema | Primera opción | Segunda opción | Consulta puntual | Español |
|---|---|---|---|---|
| T1 — HDL / SIC / AHPL | Hill & Peterson Digital Systems 2ª ed. | Hill & Peterson Digital Systems 1ª ed. (1973) | Langdon Computer Design | — |
| T2 — Comunicación entre sistemas | Hill & Peterson Digital Systems 2ª ed. | Hamacher 6ª ed. | Stallings COA 11ª ed. | Stallings español 7ª ed. |

### Parcial 2 — Interrupciones, I/O, Interfaces (T3, T4)

| Tema | Primera opción | Segunda opción | Consulta puntual | Español |
|---|---|---|---|---|
| T3 — Interrupciones y sistema I/O | Hill & Peterson Digital Systems 2ª ed. | Stallings COA 11ª ed. | Mano CSA 3ª ed. | Stallings español 7ª ed. |
| T4 — Interfaces y periféricos | Hill & Peterson Digital Systems 2ª ed. | Hamacher 6ª ed. | Mano CSA 3ª ed. | Stallings español 7ª ed. |

### Parcial 3 — Memoria, Multiprocesadores, Avances (T5, T6)

| Tema | Primera opción | Segunda opción | Consulta puntual | Español |
|---|---|---|---|---|
| T5 — Administración de memoria | Stallings COA 11ª ed. | Hennessy & Patterson Quantitative 6ª ed. | Mano CSA 3ª ed. | Stallings español 7ª ed. |
| T6 — Avances / Multiprocesadores | Hennessy & Patterson Quantitative 6ª ed. | Stallings COA 11ª ed. | Tanenbaum Computer Networks 5ª ed. | Stallings español 7ª ed. |

### Complemento Bloque B (T2 paralelo/serie — según avance del docente)

| Tema | Primera opción | Segunda opción | Consulta puntual | Español |
|---|---|---|---|---|
| Comunicaciones paralelo/serie | Stallings DCC 10ª ed. | Forouzan 5ª ed. | — | Stallings Comunicaciones 6ª ed. |
| TCP/IP (si el docente profundiza) | Stevens TCP/IP Illustrated Vol.1 2ª ed. | Tanenbaum Computer Networks 5ª ed. | — | — |

---

## Flujo de uso

```
Tema AHPL / SIC / HDL      → Hill & Peterson Digital Systems 2ª ed.
No entiendo la notación    → Langdon Computer Design (segunda opinión RTL)
Base lógica previa         → Hill & Peterson Switching Theory 3ª ed.

Tema nuevo (arq. general)  → Stallings COA 11ª ed.
No entiendo en inglés      → Stallings español 7ª ed.
Segunda opinión arq.       → Hamacher 6ª ed.
Quiero el fondo teórico    → Hennessy & Patterson Quantitative 6ª ed.
Necesito paso a paso       → Patterson & Hennessy COD 5ª ed.
Ejercicios resueltos       → Schaum's Computer Architecture

Tema comunicaciones        → Stallings DCC 10ª ed. o Forouzan 5ª ed.
No entiendo en inglés (B)  → Stallings Comunicaciones 6ª ed. español
Solo TCP/IP                → Stevens Vol.1 (consulta puntual)
```

---

## Diapositivas de clase (uso en sesión — no NotebookLM)

Archivos convertidos a PDF desde formato de diapositivas. No se suben a NotebookLM. Se usan directamente en sesión como material de repaso rápido.

### Stallings COA 10ª ed. (2016) — 21 capítulos en PDF

Fuente: https://github.com/mguludag/Stallings-Computer-Org-and-Arch-Slides — pasadas por el docente, convertidas a PDF.

| Tema | Título                                                    | Temas ETN825 | Útil                            |
| ---- | --------------------------------------------------------- | ------------ | ------------------------------- |
| 1    | Basic Concepts and Computer Evolution                     | T1           | ✅                               |
| 2    | Performance Issues                                        | —            | ⚪️ Contextual                   |
| 3    | A Top-Level View of Computer Function and Interconnection | T1, T2       | ✅                               |
| 4    | Cache Memory                                              | T5, T8       | ✅                               |
| 5    | Internal Memory                                           | T5, T8       | ✅                               |
| 6    | External Memory                                           | —            | ⚪️ Secundario                   |
| 7    | Input/Output                                              | T3, T4, T9   | ✅                               |
| 8    | Operating System Support                                  | —            | ⚪️ SO — no directo              |
| 9    | Number Systems                                            | —            | ⚪️ Base matemática              |
| 10   | Computer Arithmetic                                       | —            | ⚪️ Base matemática              |
| 11   | Digital Logic                                             | —            | ⚪️ Cubierto por Hill & Peterson |
| 12   | Instruction Sets: Characteristics and Functions           | T1           | ✅                               |
| 13   | Instruction Sets: Addressing Modes and Formats            | T1           | ✅                               |
| 14   | Processor Structure and Function                          | T1           | ✅                               |
| 15   | Reduced Instruction Set Computers (RISC)                  | T1           | ✅                               |
| 16   | Instruction-Level Parallelism and Superscalar             | T2, T6       | ✅                               |
| 17   | Parallel Processing                                       | T6, T10      | ✅                               |
| 18   | Multicore Computers                                       | T6, T10      | ✅                               |
| 19   | Control Unit Operation                                    | T1           | ✅                               |
| 20   | Microprogrammed Control                                   | T1           | ✅                               |
| 21   | Microinstruction Examples                                 | T1           | ✅                               |

> ⚠️ Caps. ✅ directamente útiles: 1, 3, 4, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 (15 de 21). Caps. ⚪️ se consultan solo si el docente los menciona explícitamente.

---

## Libros descartados

| Libro | Razón |
|---|---|
| Hennessy & Patterson — Quantitative Approach 5ª ed. | Redundante con la 6ª ed. que ya está en el stack |
| Patterson & Hennessy — COD 3ª ed. | Redundante con la 5ª ed. |
| Patterson & Hennessy — COD 4ª ed. | Redundante con la 5ª ed. |
| Patterson & Hennessy — COD MIPS 6ª ed. | Usa MIPS — ejemplos no alineados con temario Intel |
| Hill & Peterson — Switching Theory 2ª ed. | Redundante con la 3ª ed. |
| Eijkhout — Introduction to High Performance Scientific Computing | HPC / computación científica — fuera del scope |
| Hauck & DeHon — Reconfigurable Computing | FPGAs — fuera del scope del temario |
| Deisenroth & Faisal — Mathematics for Machine Learning | Machine learning — fuera del scope |
| Stallings — Solutions Manual Operating Systems 5ª ed. (2004) | SO puro — misma razón que OSTEP |
| Stallings — Solutions Manual Data and Computer Communications 10ª ed. caps. 1–13 (2014) | Redes/telecomunicaciones puro — Protocol Architecture, LAN, WAN, Ethernet. Sin contacto real con ETN825 |
| Arpaci-Dusseau, R.H. & Arpaci-Dusseau, A.C. — Operating Systems: Three Easy Pieces (OSTEP) | SO puro — los temas de contacto (memoria virtual, DMA) están mejor cubiertos desde hardware por Stallings y Mano. Genera ruido en NotebookLM sin aportar valor diferencial para ETN825 |
| Swanson, R.E. — Extensions of AHPL and Optimization of the AHPL Compiler for MSI/LSI Design (tesis doctoral, U. of Arizona) | Investigación de posgrado sobre construcción del compilador AHPL y extensiones para síntesis en chips MSI/LSI — excede completamente el nivel del temario. ETN825 trabaja AHPL como herramienta de descripción, no como objeto de investigación |

---

%%
# galaxy-links
[[_app/_config/_library-system.md]]
%%
