
## Subtítulos de las diapositivas (52 láminas, páginas reales del PDF)

| # | Subtítulo | Págs. | Figuras / tablas |
|---|---|---|---|
| 1 | Dispositivos externos | 3–6 | Fig. 7.1 (p.3), Fig. 7.2 (p.5) |
| 2 | Teclado/monitor e IRA | 6 | — |
| 3 | Módulo de E/S: funciones y estructura | 3, 7–8 | Fig. 7.1 (p.3), Fig. 7.3 (p.8) |
| 4 | E/S programada | 9–12 | Tabla 7.1 (p.10), Fig. 7.4 (p.12) |
| 5 | Comandos e instrucciones de E/S | 11, 13 | — |
| 6 | Mapeo de E/S (mapeada vs aislada) | 14–15 | Fig. 7.5 (p.15) |
| 7 | E/S por interrupciones | 16–18 | Fig. 7.6 (p.17), Fig. 7.7 (p.18) |
| 8 | Problemas de diseño e identificación del dispositivo | 19–20 | — |
| 9 | Controladores 82C59A, 8255A y 82C55A | 21–24 | Fig. 7.8 (p.21), Fig. 7.9 (p.22), Fig. 7.10 (p.23), Fig. 7.11 (p.24) |
| 10 | DMA: limitaciones y funcionamiento | 25–29 | Fig. 7.12 a 7.15 (p.26–29) |
| 11 | Controlador 8237A (fly-by) | 30–31 | Tabla 7.2 (p.31) |
| 12 | Direct Cache Access y DDIO | 32–38 | Fig. 7.16 (p.33), Fig. 7.17 (p.38) |
| 13 | Evolución de la E/S y canales | 39–40 | Fig. 7.18 (p.40) |
| 14 | Interfaces y buses externos | 41–48 | — |
| 15 | Caso IBM zEC12 | 49–51 | Fig. 7.19 a 7.21 |
| 16 | Resumen | 52 | — |

La sección 14 incluye USB, FireWire, SCSI, Thunderbolt, InfiniBand, PCIe y SATA (p.46), Ethernet y Wi-Fi.

---
### intro
## Figure 7.1 — Generic Model of an I/O Module

![[CH07-COA10e.pdf#page=3&rect=124,35,585,529|CH07-COA10e, p.3]]
*Fig. 7.1 · Modelo genérico de un módulo de E/S*

justificación: Muestra la estructura conceptual de bloques y las interfaces de conexión del módulo de E/S con el bus del sistema y los periféricos externos.

**Qué muestra:**
- El **módulo de E/S** (*I/O Module*) como bloque intermedio central de la arquitectura.
- La interfaz hacia el **bus del sistema** (*System Bus*), compuesta por tres conjuntos de líneas de bus:
  - **Líneas de dirección** (*Address Lines*).
  - **Líneas de datos** (*Data Lines*).
  - **Líneas de control** (*Control Lines*).
- La interfaz hacia los **dispositivos periféricos**: enlaces específicos o dedicados (*Links to peripheral devices*).

**Cómo se lee:**
- **Desde la CPU y Memoria:** El procesador coloca la dirección del dispositivo en las líneas de dirección para seleccionar el módulo/puerto de E/S, emite comandos mediante las líneas de control (lectura, escritura, prueba) y transfiere datos a través de las líneas de datos.
- **A través del módulo de E/S:** El módulo intercepta las señales del bus del sistema, las decodifica, aplica la lógica de control interna, gestiona la temporización y efectúa el búfering de datos.
- **Hacia/desde los periféricos:** El módulo transmite estas órdenes e intercambia datos y señales de estado con los periféricos externos mediante sus enlaces dedicados (*links*).

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
- **Cambio de numeración:** En la 11ª edición del libro, esta figura pasa a llamarse **Figure 8.1 Generic Model of an I/O Module** dentro del Capítulo 8 (*Input/Output*).
- **Razones para no conectar periféricos directamente al bus del sistema:**
  1. *Diversidad operativa:* Existe una gran variedad de periféricos con métodos de operación distintos; integrar la lógica de cada uno en la CPU sería impracticable.
  2. *Disparidad de velocidad:* La velocidad de transferencia de los periféricos suele ser mucho más lenta (o en ciertos casos más rápida) que la de la memoria y la CPU, degradando la eficiencia del bus del sistema.
  3. *Incompatibilidad de formatos:* Los periféricos utilizan formatos de datos y longitudes de palabra diferentes a los del computador.
- **Niveles de complejidad del módulo:** La fuente aclara que este modelo abarca desde un controlador simple de dispositivo (*I/O controller* o *device controller*, común en microcomputadores) hasta un canal o procesador de E/S (*I/O channel* o *I/O processor*, común en mainframes) que ejecuta sus propios programas de E/S autonomamente.
- **Apoyo complementario (Mano - Computer System Architecture.pdf):** En la obra de Mano, este esquema corresponde a la conexión del bus de E/S con módulos de interfaz (Fig. 11-1 p.388), donde cada interfaz decodifica la dirección enviada por el bus y supervisa al controlador del periférico.
![[expo825cap7-18-10-2026_22-24-14.png]]
---
### 1. Dispositivos externos (p.3–6)

**Subtítulo**
```
Subtítulo: Dispositivos externos
```

## Dispositivos externos

**Idea central:** Los dispositivos externos o periféricos permiten el intercambio de datos entre el entorno exterior y el computador a través de un enlace dedicado con un módulo de entrada/salida (E/S).

**Según las diapositivas (p.4–6):**
- **Definición y enlace de conexión:** Se conectan al computador mediante un enlace hacia el módulo de E/S, el cual sirve para intercambiar datos, señales de control y estado.
- **Clasificación en tres categorías:**
  - **Legibles por humanos (*human readable*):** Diseñados para interactuar con el usuario (ej. monitores/terminales VDT e impresoras).
  - **Legibles por máquina (*machine readable*):** Diseñados para comunicarse con equipos o almacenamiento (ej. discos magnéticos, cintas, sensores y actuadores).
  - **De comunicación (*communication*):** Orientados a comunicarse con dispositivos remotos, como una terminal, un dispositivo legible por máquina u otro computador.
- **Estructura interna genérica (Fig. 7.2):** Se compone de una lógica de control (*control logic*), un búfer (*buffer*) para almacenamiento temporal de datos y un transductor (*transducer*).

![[CH07-COA10e.pdf#page=5&rect=110,50,628,535|CH07-COA10e, p.5]]

- **Ejemplo Teclado/Monitor:**
  - La unidad básica de intercambio es el carácter mediante el código IRA (*International Reference Alphabet*), compuesto por 7 bits (128 caracteres).
  - Los caracteres se clasifican en imprimibles (alfanuméricos y símbolos) y de control (como el retorno de carro).
  - Al pulsar una tecla, el transductor del teclado convierte la señal eléctrica en el patrón de bits IRA enviado al módulo de E/S; en la salida, el módulo retransmite el código al monitor para su representación física.

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
- **Rol del transductor:** Transforma la energía eléctrica en otras formas de energía (magnética, óptica, mecánica) durante la salida, y viceversa durante la entrada.
- **Tamaño del búfer:** Varía según el tipo de dispositivo; es de 8 a 16 bits en dispositivos seriales (como el teclado), mientras que en dispositivos orientados a bloques (como controladores de disco) el búfer es significativamente mayor.
- **Mecanismo en unidades de disco (*disk drive*):** Contiene la electrónica para el brazo de lectura/escritura; en discos de cabeza fija el transductor convierte patrones magnéticos directamente a bits en el búfer, mientras que en discos de cabeza móvil la lógica de control gestiona además el desplazamiento radial del brazo.

**Figuras de apoyo:**
[[CH07-COA10e.pdf#page=5]]
*Fig. 7.2 · Diagrama de bloques de un dispositivo externo*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 5 | id: Fig. 7.2 | posición: centro
justificación: Permite visualizar la división interna del periférico entre lógica de control, búfer y transductor, así como la interfaz de señales con el módulo de E/S.%%

**Dato para el docente:** El código IRA (*International Reference Alphabet*), anteriormente denominado IA5 y conocido en su versión estadounidense como ASCII, utiliza exactamente 7 bits de codificación para representar 128 caracteres (divididos en imprimibles y de control).

---

**Concepto**
```
Concepto: Dispositivo periférico
```

## Dispositivo periférico

Según la diapositiva (p.4), un **dispositivo periférico** (*peripheral device*) es un dispositivo externo conectado a un módulo de E/S que proporciona un medio para intercambiar datos, señales de control y estado entre el computador y el entorno exterior.

Se complementa con:
- **Stallings - Computer Organization and Architecture - 11ed.pdf (Sección 8.1):** Explica que los periféricos no se conectan directamente al bus del sistema debido a la amplia variedad de métodos de operación, las severas diferencias de velocidad respecto a la CPU y memoria, y los distintos formatos o tamaños de palabra que emplean, haciendo necesaria la presencia del módulo de E/S como intermediario.
- **Mano - Computer System Architecture.pdf (p.383):** Los define como dispositivos *on-line* (bajo control directo del sistema) capaces de transferir información a la memoria, y los clasifica en tres tipos: de entrada, de salida y de almacenamiento auxiliar.

[[CH07-COA10e.pdf#page=5]]
*Fig. 7.2 · Diagrama de bloques de un dispositivo externo*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 5 | id: Fig. 7.2 | posición: centro
justificación: Muestra los bloques internos de un periférico (lógica de control, búfer y transductor) y sus líneas de conexión con el módulo de E/S.%%

---

**Subtítulo + SIC**
```
Subtítulo SIC: Dispositivos externos
```

## Dispositivos externos

**Idea central:** Los dispositivos externos o periféricos permiten el intercambio de datos, señales de control y estado entre el entorno exterior y el computador a través de un módulo de entrada/salida (E/S).

**Según las diapositivas (p.4–6):**
- **Conexión e interfaz:** Se conectan al computador mediante un enlace hacia el módulo de E/S para transmitir información de control, datos y estado.
- **Clasificación en tres categorías:**
  - **Legibles por humanos (*human readable*):** Diseñados para interactuar con el usuario (ej. monitores VDT, impresoras).
  - **Legibles por máquina (*machine readable*):** Diseñados para comunicarse con equipos o medios de almacenamiento (ej. discos magnéticos, cintas, sensores y actuadores).
  - **De comunicación (*communication*):** Orientados a comunicarse con dispositivos remotos, como una terminal, un dispositivo legible por máquina u otro computador.
- **Estructura interna (Fig. 7.2):** Integrada por la lógica de control (*control logic*), búfer de almacenamiento temporal (*buffer*) y transductor (*transducer*).
- **Ejemplo Teclado/Monitor:**
  - La unidad básica de intercambio es el carácter mediante el código IRA (*International Reference Alphabet*), compuesto por 7 bits (128 caracteres).
  - Los caracteres se dividen en imprimibles (alfanuméricos y símbolos) y de control (como el retorno de carro).
  - Al pulsar una tecla, el transductor del teclado convierte la acción en el patrón binario IRA enviado al módulo de E/S; en la salida, el módulo retransmite el código al monitor para su representación física.

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
- **Rol del transductor:** Transforma la energía eléctrica en otras formas de energía (magnética, óptica, mecánica) durante la salida, y realiza la conversión inversa durante la entrada.
- **Tamaño del búfer:** Varía según el dispositivo, siendo de pocos bits (8 a 16 bits) en periféricos orientados a caracteres y de mayor capacidad (sectores completos) en unidades de almacenamiento masivo.

**Figuras de apoyo:**
[[CH07-COA10e.pdf#page=5]]
*Fig. 7.2 · Diagrama de bloques de un dispositivo externo*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 5 | id: Fig. 7.2 | posición: centro
justificación: Muestra la división interna del periférico entre lógica de control, búfer y transductor, así como la interfaz de señales con el módulo de E/S.%%

**Dato para el docente:** El código IRA (*International Reference Alphabet*), equivalente a ASCII o IA5, utiliza exactamente 7 bits de codificación para representar 128 caracteres (divididos en imprimibles y de control).

---

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
|-|-|-|
| Cómo se hace | Conexión al módulo de E/S mediante un enlace dedicado de datos, control y estado. | Conexión directa a los buses del sistema (`IOBUS` de 18 bits y `CSBUS` de 12 bits) mediante un módulo de interfaz específico. |
| Quién controla | El módulo de E/S intermedio asume la interfaz con el bus del sistema, la temporización y el búfering. | La CPU controla la transferencia enviando comandos por el `CSBUS` y coordinando mediante un protocolo de *handshake* de 3 líneas (`ready`, `datavalid`, `accept`). |

**Conclusión:** En el Cap. 7 un módulo de E/S intermedio conecta el bus del sistema con los periféricos; en el SIC la CPU coordina la transferencia con el periférico mediante señales de handshake sobre `IOBUS` y `CSBUS`.

### 2. Teclado/monitor e IRA (p.6)

**Subtítulo**
```
Subtítulo: Teclado/monitor e IRA
```
**Concepto**
```
Concepto: Código IRA
```
**Subtítulo + SIC**
```
Subtítulo SIC: Teclado/monitor e IRA
```

### 3. Módulo de E/S: funciones y estructura (p.3, 7–8)

**Subtítulo**
```
Subtítulo: Módulo de E/S: funciones y estructura
```
**Concepto**
```
Concepto: Buffering de datos en el módulo de E/S
```
**Subtítulo + SIC**
```
Subtítulo SIC: Módulo de E/S: funciones y estructura
```

### 4. E/S programada (p.9–12)

**Subtítulo**
```
Subtítulo: E/S programada
```
**Concepto**
```
Concepto: Las tres técnicas de E/S (Tabla 7.1)
```
**Subtítulo + SIC**
```
Subtítulo SIC: E/S programada
```

### 5. Comandos e instrucciones de E/S (p.11, 13)

**Subtítulo**
```
Subtítulo: Comandos e instrucciones de E/S
```
**Concepto**
```
Concepto: Comando de E/S Test
```
**Subtítulo + SIC**
```
Subtítulo SIC: Comandos e instrucciones de E/S
```

### 6. Mapeo de E/S (p.14–15)

**Subtítulo**
```
Subtítulo: Mapeo de E/S (mapeada vs aislada)
```
**Concepto**
```
Concepto: E/S mapeada en memoria vs E/S aislada
```
**Subtítulo + SIC**
```
Subtítulo SIC: Mapeo de E/S (mapeada vs aislada)
```

### 7. E/S por interrupciones (p.16–18)

**Subtítulo**
```
Subtítulo: E/S por interrupciones
```
**Concepto**
```
Concepto: Procesamiento simple de una interrupción
```
**Subtítulo + SIC**
```
Subtítulo SIC: E/S por interrupciones
```

### 8. Problemas de diseño e identificación del dispositivo (p.19–20)

**Subtítulo**
```
Subtítulo: Problemas de diseño e identificación del dispositivo
```
**Concepto**
```
Concepto: Interrupción vectorizada
```
**Subtítulo + SIC**
```
Subtítulo SIC: Problemas de diseño e identificación del dispositivo
```

### 9. Controladores 82C59A, 8255A y 82C55A (p.21–24)

**Subtítulo**
```
Subtítulo: Controladores 82C59A, 8255A y 82C55A
```
**Concepto**
```
Concepto: Controlador de interrupciones 82C59A
```
**Subtítulo + SIC**
```
Subtítulo SIC: Controladores 82C59A, 8255A y 82C55A
```

### 10. DMA: limitaciones y funcionamiento (p.25–29)

**Subtítulo**
```
Subtítulo: DMA: limitaciones y funcionamiento
```
**Concepto**
```
Concepto: Puntos de ruptura de DMA en el ciclo de instrucción
```
**Subtítulo + SIC**
```
Subtítulo SIC: DMA: limitaciones y funcionamiento
```

### 11. Controlador 8237A (p.30–31)

**Subtítulo**
```
Subtítulo: Controlador 8237A (fly-by)
```
**Concepto**
```
Concepto: DMA fly-by
```
**Subtítulo + SIC**
```
Subtítulo SIC: Controlador 8237A (fly-by)
```

### 12. Direct Cache Access y DDIO (p.32–38)

**Subtítulo**
```
Subtítulo: Direct Cache Access y DDIO
```
**Concepto**
```
Concepto: Direct Data I/O (DDIO)
```
**Subtítulo + SIC**
```
Subtítulo SIC: Direct Cache Access y DDIO
```

### 13. Evolución de la E/S y canales (p.39–40)

**Subtítulo**
```
Subtítulo: Evolución de la E/S y canales
```
**Concepto**
```
Concepto: Canal de E/S selector y multiplexor
```
**Subtítulo + SIC**
```
Subtítulo SIC: Evolución de la E/S y canales
```

### 14. Interfaces y buses externos (p.41–48)

**Subtítulo**
```
Subtítulo: Interfaces y buses externos
```
**Concepto**
```
Concepto: USB SuperSpeed
```
**Subtítulo + SIC**
```
Subtítulo SIC: Interfaces y buses externos
```

### 15. Caso IBM zEC12 (p.49–51)

**Subtítulo**
```
Subtítulo: Caso IBM zEC12
```
**Concepto**
```
Concepto: Subsistema de canales del IBM zEC12
```
**Subtítulo + SIC**
```
Subtítulo SIC: Caso IBM zEC12
```

### 16. Resumen (p.52)

**Subtítulo**
```
Subtítulo: Resumen
```
**Concepto**
```
Concepto: Evolución de la función de E/S
```
**Subtítulo + SIC**
```
Subtítulo SIC: Resumen
```

---
