
## Subtítulos de las diapositivas (52 láminas, páginas reales del PDF)

| #   | Subtítulo                                            | Págs.    | Figuras / tablas                                                     |
| --- | ---------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| 1   | Dispositivos externos                                | 4–5      | Fig. 7.2 (p.5)                                                       |
| 2   | Teclado/monitor e IRA                                | 6        | —                                                                    |
| 3   | Módulo de E/S                                        | 3, 7–8   | Fig. 7.1 (p.3), Fig. 7.3 (p.8)                                       |
| 4   | E/S programada                                       | 9–10, 12 | Tabla 7.1 (p.10), Fig. 7.4 (p.12)                                    |
| 5   | Comandos e instrucciones de E/S                      | 11, 13   | —                                                                    |
| 6   | Mapeo de E/S (mapeada vs aislada)                    | 14–15    | Fig. 7.5 (p.15)                                                      |
| 7   | E/S por interrupciones                               | 16–18    | Fig. 7.6 (p.17), Fig. 7.7 (p.18)                                     |
| 8   | Problemas de diseño e identificación del dispositivo | 19–20    | —                                                                    |
| 9   | Controladores 82C59A, 8255A y 82C55A                 | 21–24    | Fig. 7.8 (p.21), Fig. 7.9 (p.22), Fig. 7.10 (p.23), Fig. 7.11 (p.24) |
| 10  | DMA: limitaciones y funcionamiento                   | 25–29    | Fig. 7.12 a 7.15 (p.26–29)                                           |
| 11  | Controlador 8237A (fly-by)                           | 30–31    | Tabla 7.2 (p.31)                                                     |
| 12  | Direct Cache Access y DDIO                           | 32–38    | Fig. 7.16 (p.33), Fig. 7.17 (p.38)                                   |
| 13  | Evolución de la E/S y canales                        | 39–40    | Fig. 7.18 (p.40)                                                     |
| 14  | Interfaces y buses externos                          | 41–48    | —                                                                    |
| 15  | Caso IBM zEC12                                       | 49–51    | Fig. 7.19 a 7.21                                                     |
| 16  | Resumen                                              | 52       | —                                                                    |

La sección 14 incluye USB, FireWire, SCSI, Thunderbolt, InfiniBand, PCIe y SATA (p.46), Ethernet y Wi-Fi.

---

### 1. Dispositivos externos (p.4–5)

**Mensaje 1**
```
Subtítulo: Dispositivos externos
```
**Mensaje 2**
```
Concepto: Dispositivo periférico
```
**Mensaje 3**
```
Concepto SIC: Dispositivo periférico
```
**Mensaje 4**
```
"Figure 7.2 Block Diagram of an External Device" completa la explicación con las fuentes cargadas para el tema 7
```

#### Respuesta

**Idea central:** Los dispositivos externos (periféricos) permiten el intercambio de datos entre el entorno exterior y el computador mediante enlaces conectados a un módulo de E/S.

**Diapositivas (p.4–5):**

p.4
* **Dispositivos externos**
  * Proporcionan un medio para intercambiar datos entre el entorno externo y el computador
  * Se conectan al computador mediante un enlace hacia un módulo de E/S
    * El enlace se utiliza para intercambiar control, estado y datos entre el módulo de E/S y el dispositivo externo
  * *Dispositivo periférico*
    * Un dispositivo externo conectado a un módulo de E/S
* **Tres categorías:**
  * **Legibles por humanos (*Human readable*)**
    * Adecuados para comunicarse con el usuario del computador
    * Terminales de pantalla de video (*VDTs*), impresoras
  * **Legibles por máquina (*Machine readable*)**
    * Adecuados para comunicarse con equipos
    * Sistemas de disco y cinta magnética, sensores y actuadores
  * **Comunicación (*Communication*)**
    * Adecuados para comunicarse con dispositivos remotos como una terminal, un dispositivo legible por máquina u otro computador

p.5

![[CH07-COA10e.pdf#page=5&rect=124,47,623,531|CH07-COA10e, p.5]]

*Fig. 7.2 · Diagrama de bloques de un dispositivo externo*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 5 | id: Fig. 7.2 | posición: centro de la diapositiva
justificación: Ilustra la estructura interna general de un periférico externo y sus señales de interfaz con el módulo de E/S y el entorno.%%

* **Qué muestra (la lámina p.5 solo trae la figura, sin texto):**
  * **Señales de control desde el módulo de E/S (*Control signals from I/O module*):** entran a la lógica de control.
  * **Señales de estado hacia el módulo de E/S (*Status signals to I/O module*):** salen de la lógica de control.
  * **Bits de datos hacia y desde el módulo de E/S (*Data bits to and from I/O module*):** flecha en ambos sentidos con el buffer.
  * **Tres bloques internos:** lógica de control (*Control logic*), buffer (*Buffer*) y transductor (*Transducer*). El buffer aparece como la parte superior del bloque del transductor.
  * **Datos (propios del dispositivo) hacia y desde el entorno (*Data (device-unique) to and from environment*):** flecha en ambos sentidos con el transductor.
* **Cómo se lee (solo lo que dibuja la figura):**
  * El módulo de E/S envía control a la lógica de control y recibe de ella el estado.
  * La lógica de control tiene una flecha hacia el buffer.
  * Los bits de datos van y vienen entre el módulo de E/S y el buffer.
  * El transductor es el bloque que se conecta con el entorno.

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
* **Función de cada bloque:**
  * Lógica de control: controla la operación del dispositivo según los comandos del módulo de E/S.
  * Transductor: convierte entre señales eléctricas y la forma de energía propia del entorno.
  * Buffer: guarda temporalmente los datos durante la transferencia.
* **Capacidad del buffer:** 8 a 16 bits en dispositivos en serie; mucho mayor en dispositivos orientados a bloques, como controladores de disco.
* **Enfoque funcional vs. estructural:** los discos y cintas son memoria en la jerarquía funcional, pero estructuralmente se comportan como dispositivos externos controlados por módulos de E/S.

**Comparación con SIC:**

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Clasificación de dispositivos | Tres categorías: legibles por humanos, legibles por máquina y de comunicación. | No aparece en las fuentes del SIC. |
| Interfaz del periférico | El periférico contiene lógica de control, buffer y transductor, conectándose al módulo de E/S por un enlace dedicado. | Cada periférico dispone de un módulo de interfaz explícito que lo adapta al bus de E/S. |
| Temporización física | (11ed, no de la lámina) La lógica de control y el buffer absorben las diferencias de velocidad del medio físico. | Se diseñan generadores de pulso con tiempos explícitos (p. ej., 100 µs y 4 ms). |

Conclusión: el Cap. 7 presenta un modelo conceptual del dispositivo externo (lógica de control, buffer y transductor).

---

### 2. Teclado/monitor e IRA (p.6)

**Mensaje 1**
```
Subtítulo: Teclado/monitor e IRA
```
**Mensaje 2**
```
Concepto: International Reference Alphabet (IRA)
```
**Mensaje 3**
```
Concepto SIC: International Reference Alphabet (IRA)
```

#### Respuesta

**Idea central:** El teclado y el monitor son la forma más común de interacción usuario-computador, y el intercambio se hace carácter por carácter con el código IRA de 7 bits.

**Diapositivas (p.6):**

p.6
* **Teclado/Monitor (*Keyboard/Monitor*)**
  * La forma más común de interacción computador/usuario
    * El usuario proporciona la entrada a través del teclado
    * El monitor muestra los datos proporcionados por el computador
  * **Alfabeto de Referencia Internacional (*International Reference Alphabet - IRA*)**
    * La unidad básica de intercambio es el carácter
      * Asociado a cada carácter hay un código
      * Cada carácter en este código está representado por un código binario único de 7 bits
        * Se pueden representar 128 caracteres diferentes
    * Los caracteres son de dos tipos:
      * **Imprimibles (*Printable*)**
        * Caracteres alfabéticos, numéricos y especiales que se pueden imprimir en papel o mostrar en una pantalla
      * **Control (*Control*)**
        * Tienen que ver con el control de la impresión o visualización de caracteres
          * Un ejemplo es el retorno de carro (*carriage return*)
        * Otros caracteres de control están relacionados con procedimientos de comunicación
  * **Códigos de teclado (*Keyboard Codes*)**
    * Cuando el usuario presiona una tecla, genera una señal electrónica que es interpretada por el transductor en el teclado y traducida al patrón de bits del código IRA correspondiente
    * Este patrón de bits se transmite al módulo de E/S en el computador
    * En la salida, los caracteres en código IRA se transmiten al dispositivo externo desde el módulo de E/S
    * El transductor interpreta el código y envía las señales electrónicas requeridas al dispositivo de salida, ya sea para mostrar el carácter indicado o realizar la función de control solicitada

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
* **Normativa del código IRA:** definido en la Recomendación ITU-T T.50 (antes Alfabeto Internacional Nº 5, IA5). Su variante nacional en EE.UU. es ASCII (*American Standard Code for Information Interchange*).

**Comparación con SIC:**

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Codificación de caracteres | IRA/ASCII de 7 bits (128 caracteres), con caracteres imprimibles y de control. | Maneja caracteres como vectores (p. ej., ASCII o Hollerith de 12 bits) que pasan por el acumulador `AC` o por buffers. |

---

### 3. Módulo de E/S (p.3, 7–8)

**Mensaje 1**
```
Subtítulo: Módulo de E/S
```
**Mensaje 2**
```
Concepto: Data buffering
```
**Mensaje 3**
```
Concepto SIC: Data buffering
```
**Mensaje 4**
```
"Figure 7.1 Generic Model of an I/O Module" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.3 Block Diagram of an I/O Module" completa la explicación con las fuentes cargadas para el tema 7
```

#### Respuesta

**Idea central:** El módulo de E/S es la interfaz intermedia entre el bus del sistema y los dispositivos externos; gestiona la transferencia de datos, el control, la temporización y el estado.

**Diapositivas (p.3, 7–8):**

p.3
* **Módulo de E/S (*I/O Module*)**

![[CH07-COA10e.pdf#page=3&rect=124,35,585,529|CH07-COA10e, p.3]]

*Fig. 7.1 · Modelo genérico de un módulo de E/S*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 3 | id: Fig. 7.1 | posición: centro de la diapositiva
justificación: Muestra el módulo de E/S entre las tres líneas del bus del sistema y los enlaces a los dispositivos periféricos.%%

* **Qué muestra (la lámina p.3 solo trae la figura, sin texto):**
  * **Bus del sistema (*System Bus*):** arriba, con líneas de dirección (*Address Lines*), de datos (*Data Lines*) y de control (*Control Lines*).
  * **Módulo de E/S (*I/O Module*):** bloque central, conectado a las tres líneas del bus.
  * **Enlaces a dispositivos periféricos (*Links to peripheral devices*):** cuatro líneas que salen del módulo hacia abajo.
* **Cómo se lee (solo lo que dibuja la figura):** las tres líneas del bus bajan y entran al módulo; del lado opuesto, el módulo se conecta a los periféricos mediante varios enlaces. El módulo queda entre el bus del sistema y los dispositivos externos.

p.7
* **Las funciones principales de un módulo de E/S se dividen en las siguientes categorías:**
  * **Control y temporización (*Control and timing*)**
    * Coordina el flujo de tráfico entre los recursos internos y los dispositivos externos
  * **Comunicación con el procesador (*Processor communication*)**
    * Involucra decodificación de comandos, datos, reporte de estado, reconocimiento de direcciones
  * **Comunicación con el dispositivo (*Device communication*)**
    * Involucra comandos, información de estado y datos
  * **Almacenamiento temporal de datos (*Data buffering*)**
    * Realiza la operación de almacenamiento temporal necesaria para equilibrar las velocidades del dispositivo y la memoria
  * **Detección de errores (*Error detection*)**
    * Detecta y reporta errores de transmisión

p.8

![[CH07-COA10e.pdf#page=8&rect=37,48,679,515|CH07-COA10e, p.8]]

*Fig. 7.3 · Diagrama de bloques de un módulo de E/S*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 8 | id: Fig. 7.3 | posición: centro de la diapositiva
justificación: Muestra la estructura interna del módulo de E/S y separa la interfaz con el bus del sistema de la interfaz con el dispositivo externo.%%

* **Qué muestra (la lámina p.8 solo trae la figura, sin texto):**
  * **Interfaz hacia el bus del sistema (*Interface to System Bus*):**
    * Líneas de datos (*Data Lines*): conectadas a los registros de datos (*Data Registers*) y a los registros de estado/control (*Status/Control Registers*).
    * Líneas de dirección (*Address Lines*) y de control (*Control Lines*): conectadas a la lógica de E/S (*I/O Logic*).
  * **Dentro del módulo:** registros de datos, registros de estado/control y lógica de E/S. La lógica de E/S se conecta con ambos registros y con cada bloque de lógica de interfaz del dispositivo externo.
  * **Interfaz hacia el dispositivo externo (*Interface to External Device*):** dos bloques *External Device Interface Logic* con puntos suspensivos entre ellos (hay más). Cada uno tiene tres líneas: datos (*Data*), estado (*Status*) y control (*Control*).
* **Cómo se lee (solo lo que dibuja la figura):**
  * Por las líneas de datos del bus se llega a los dos registros.
  * Las líneas de dirección y de control del bus llegan a la lógica de E/S.
  * La lógica de E/S conecta los registros con los bloques de interfaz de cada dispositivo.
  * Cada bloque de interfaz sale hacia su dispositivo con datos, estado y control.

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
* **Numeración en el 11ed:** Sección 8.2 (*I/O Modules*). Las figuras son **Figure 8.1 Generic Model of an I/O Module** y **Figure 8.3 Block Diagram of an I/O Module**.
* **Por qué existe el módulo:** los periféricos no se conectan directo al bus por tres razones:
  1. Variedad de periféricos, con modos de operación distintos.
  2. Diferencia de velocidad entre periféricos y CPU/memoria, que exige almacenamiento temporal (*data buffering*).
  3. Formatos de datos y tamaños de palabra distintos.
* **Nombres según la complejidad del módulo:** si es primitivo y la CPU lo controla en detalle → controlador de dispositivo (*device controller*) o controlador de E/S. Si ejecuta sus propias instrucciones de E/S → canal de E/S (*I/O channel*) o procesador de E/S (*I/O processor*).
* **Función de las líneas del bus (Fig. 7.1):** dirección → direcciones enviadas por el procesador; datos → transferencia de datos; control → órdenes y señales de control.
* **Función de los bloques internos (Fig. 7.3):**
  * Registros de datos: almacenan temporalmente los datos transferidos desde o hacia el procesador.
  * Registros de estado/control: contienen la condición del módulo o del periférico y aceptan comandos de control de la CPU.
  * Lógica de E/S: interpreta las líneas de dirección y control y gobierna la operación interna.
  * Lógica de interfaz del dispositivo: convierte las órdenes del bus en las señales específicas de cada enlace.
* **Secuencia paso a paso de control y temporización:**
  1. El procesador solicita al módulo de E/S verificar el estado del dispositivo adjunto.
  2. El módulo de E/S retorna el estado del dispositivo.
  3. Si el dispositivo está listo para transferir, el procesador emite la orden de transferencia al módulo.
  4. El módulo de E/S obtiene el dato del dispositivo periférico.
  5. El módulo transfiere el dato al procesador mediante el bus de datos.
* **Detalle de la comunicación con el procesador:**
  * **Decodificación de comandos (*Command decoding*):** el módulo acepta e interpreta mandatos del bus (READ, WRITE, CONTROL, TEST).
  * **Reconocimiento de direcciones (*Address recognition*):** cada dispositivo conectado posee una dirección única que el módulo debe identificar en las líneas de dirección.
* **Tipos de errores detectados:**
  * Mal funcionamiento mecánico o eléctrico del periférico (p. ej., atascamiento de papel, sector defectuoso).
  * Alteración no intencionada de bits durante la transmisión (comprobada mediante bits de paridad par o impar).

**Comparación con SIC:**

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Estructura del módulo | Módulo genérico con registros de datos, registros de estado/control, lógica de E/S e interfaz hacia el bus del sistema. | Se diseña un módulo de interfaz explícito en AHPL independiente para cada periférico (p. ej., `PRINTER INTERFACE`, `DISPLAY INTERFACE`). |
| Conexión con los buses | Se conecta a las líneas de dirección, datos y control del bus del sistema (`System Bus`). | Se conecta al bus de datos de 18 bits (`IOBUS`), al bus de estado/control de 12 bits (`CSBUS`) y a líneas de control de handshake. |
| Control y registros internos | Los registros de datos y de estado/control se conectan a las líneas de datos; la lógica de E/S recibe dirección y control. | El registro `CSR` en la CPU almacena el código de comando/dispositivo transmitido por el `CSBUS`, y la transferencia utiliza `MD` o `AC` a través del `IOBUS`. |
| Temporización y sincronización | Maneja internamente la temporización y el *data buffering* para amortiguar las diferencias de velocidad. | Sincronización mediante un protocolo de handshaking de 3 líneas (`ready`, `datavalid`, `accept`) y temporizadores por hardware (*one-shots*). |

Conclusión: Stallings presenta una arquitectura genérica e integrada de módulo de E/S con registros y lógica interna, mientras que el SIC implementa en hardware módulos de interfaz individuales adaptados a los buses `IOBUS` y `CSBUS`.

---

### 4. E/S programada (p.9–10, 12)

## E/S programada

**Idea central:** En la E/S programada, el procesador tiene el control directo de la operación de E/S y debe esperar hasta que la operación se complete.

**Diapositivas (p.9–10, 12):**

p.9
* **Tres técnicas son posibles para las operaciones de E/S:**
  * **E/S programada (*Programmed I/O*)**
    * Los datos se intercambian entre el procesador y el módulo de E/S
    * El procesador ejecuta un programa que le da control directo de la operación de E/S
    * Cuando el procesador emite un comando debe esperar hasta que la operación de E/S esté completa
    * Si el procesador es más rápido que el módulo de E/S, esto es un desperdicio del tiempo del procesador
  * **E/S mediante interrupciones (*Interrupt-driven I/O*)**
    * El procesador emite un comando de E/S, continúa ejecutando otras instrucciones, y es interrumpido por el módulo de E/S cuando este último ha completado su trabajo
  * **Acceso directo a memoria (*Direct memory access - DMA*)**
    * El módulo de E/S y la memoria principal intercambian datos directamente sin la intervención del procesador

p.10
[[CH07-COA10e.pdf#page=10]]
*Tabla 7.1 · Técnicas de E/S*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 10 | id: Tabla 7.1 | posición: centro de la diapositiva
justificación: Clasifica las tres técnicas de E/S según si emplean interrupciones y si la transferencia hacia la memoria atraviesa el procesador.%%

* **Qué muestra (la lámina p.10 solo trae la tabla):** una tabla de 2 filas por 2 columnas:
  * **Filas:** transferencia de E/S a memoria a través del procesador (*I/O-to-memory transfer through processor*) y transferencia directa de E/S a memoria (*Direct I/O-to-memory transfer*).
  * **Columnas:** sin interrupciones (*No Interrupts*) y con uso de interrupciones (*Use of Interrupts*).
  * **Celdas:**
    * A través del procesador, sin interrupciones → E/S programada (*Programmed I/O*).
    * A través del procesador, con interrupciones → E/S mediante interrupciones (*Interrupt-driven I/O*).
    * Transferencia directa, con interrupciones → acceso directo a memoria (*DMA*).
    * Transferencia directa, sin interrupciones → celda vacía.
* **Cómo se lee (solo lo que dibuja la tabla):** las filas indican si los datos pasan por el procesador; las columnas indican si se usan interrupciones.

p.12
[[CH07-COA10e.pdf#page=12]]
*Fig. 7.4 · Tres técnicas para la entrada de un bloque de datos: (a) E/S programada, (b) E/S mediante interrupciones, (c) acceso directo a memoria*
%%IMA-SRC | fuente: CH07-COA10e.pdf | página: 12 | id: Fig. 7.4 | posición: centro de la diapositiva
justificación: Compara en tres diagramas de flujo cómo se lee un bloque de datos con E/S programada, con interrupciones y con DMA.%%

* **Qué muestra (la lámina p.12 solo trae la figura, con tres diagramas):**
  * **(a) E/S programada (*Programmed I/O*):**
    1. Emitir comando de lectura al módulo de E/S (*Issue Read command to I/O module*) · CPU→I/O.
    2. Leer estado del módulo de E/S (*Read status of I/O module*) · I/O→CPU.
    3. Comprobar estado (*Check status*): sale hacia condición de error (*Error condition*), vuelve a leer el estado si no está listo (*Not ready*) o sigue si está listo (*Ready*).
    4. Leer palabra del módulo de E/S (*Read word from I/O Module*) · I/O→CPU.
    5. Escribir palabra en memoria (*Write word into memory*) · CPU→memory.
    6. ¿Completado? (*Done?*): si no, vuelve a emitir el comando de lectura; si sí, siguiente instrucción (*Next instruction*).
  * **(b) E/S mediante interrupciones (*Interrupt-driven I/O*):**
    1. Emitir comando de lectura al módulo de E/S · CPU→I/O. Una flecha punteada sale hacia "Hacer otra cosa" (*Do something else*).
    2. Leer estado del módulo de E/S · I/O→CPU. Una flecha punteada de interrupción (*Interrupt*) llega a este paso.
    3. Comprobar estado (error o listo), leer palabra del módulo de E/S · I/O→CPU y escribir palabra en memoria · CPU→memory.
    4. ¿Completado?: si no, vuelve a emitir el comando; si sí, siguiente instrucción.
  * **(c) Acceso directo a memoria (*Direct memory access*):**
    1. Emitir comando de lectura de bloque al módulo de E/S (*Issue Read block command to I/O module*) · CPU→DMA. Una flecha punteada sale hacia "Hacer otra cosa".
    2. Leer estado del módulo DMA (*Read status of DMA module*) · DMA→CPU. Una flecha punteada de interrupción llega a este paso.
    3. Siguiente instrucción.
* **Cómo se lee (solo lo que dibujan los diagramas):**
  * En (a) hay un bucle entre "Comprobar estado" y "Leer estado" cuando el módulo no está listo, y otro bucle externo desde "¿Completado?" hacia el comando de lectura.
  * En (b) después del comando la CPU sigue con otra cosa y la interrupción lleva al paso de leer estado; el bucle "¿Completado?" se repite por cada palabra.
  * En (c) se emite un solo comando para el bloque, la CPU hace otra cosa, y la interrupción lleva a leer el estado del módulo DMA y a la siguiente instrucción; no hay bucle por palabra.

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
* **Numeración en el 11ed:** Sección 8.3 (*Programmed I/O*). La tabla es **Table 8.1 I/O Techniques** y la figura es **Figure 8.4 Three Techniques for Input of a Block of Data**.
* **Visión general de la E/S programada (texto del libro, no está en las láminas):**
  * Cuando el procesador encuentra una instrucción relacionada con E/S, la ejecuta emitiendo un comando al módulo de E/S correspondiente.
  * El módulo realiza la acción y establece los bits apropiados en el registro de estado de E/S.
  * El módulo no hace nada más para alertar al procesador; en particular, no lo interrumpe.
  * Por eso el procesador debe comprobar periódicamente el estado del módulo hasta encontrar que la operación se completó.
* **Impacto en el rendimiento:** los dispositivos de E/S operan a velocidades muy inferiores a las de la CPU y la memoria. La espera activa (*polling*) mantiene al procesador ejecutando instrucciones de prueba de estado y degrada el cómputo útil del sistema.

**Comparación con SIC:**

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Cómo se hace | La CPU emite el comando de E/S al módulo y ejecuta un bucle de software leyendo el registro de estado hasta detectar que el dato está listo. | La CPU ejecuta instrucciones de la clase `IOT` (como `ISn` o `TST`), leyendo el registro `CSR` mediante el bus `CSBUS` en un bucle hasta verificar la condición. |
| Quién controla | La CPU controla cada paso de la transferencia; lee el dato desde el módulo de E/S a un registro de la CPU y luego lo escribe en la memoria. | La CPU controla la transferencia completa ejecutando secuencias en AHPL que mueven el dato desde el bus `IOBUS` al acumulador `AC` o registro `MD`. |
| Ventaja | (No está en las láminas) Hardware simple en el módulo de E/S y en la CPU; no necesita circuitos de interrupción ni de DMA. | Hardware de interfaz básico; no requiere controladores de interrupción priorizados ni lógica de concesión de bus DMA. |
| Limitación | Desperdicio de tiempo del procesador cuando es más rápido que el módulo de E/S (lámina p.9); la CPU gasta ciclos comprobando el estado mientras el periférico responde. | Bloquea la secuencia de control de la CPU esperando la respuesta de las señales de *handshake* (`ready`, `datavalid`, `accept`) y el cambio de bits en `CSR`. |

Conclusión: Stallings presenta la E/S programada como consulta del registro de estado por parte de la CPU, mientras que el SIC la implementa con instrucciones `IOT`/`TST` que prueban el registro `CSR` sobre los buses `IOBUS` y `CSBUS`.




**Mensaje 1**
```
Subtítulo: E/S programada
```
**Mensaje 2**
```
Concepto: Técnicas de E/S
```
**Mensaje 3**
```
Concepto SIC: Técnicas de E/S
```
**Mensaje 4**
```
"Table 7.1 I/O Techniques" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.4 Three Techniques for Input of a Block of Data" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 5. Comandos e instrucciones de E/S (p.11, 13)

**Mensaje 1**
```
Subtítulo: Comandos e instrucciones de E/S
```
**Mensaje 2**
```
Concepto: Comandos de E/S
```
**Mensaje 3**
```
Concepto SIC: Comandos de E/S
```

---

### 6. Mapeo de E/S (p.14–15)

**Mensaje 1**
```
Subtítulo: Mapeo de E/S
```
**Mensaje 2**
```
Concepto: Memory-mapped I/O
```
**Mensaje 3**
```
Concepto SIC: Memory-mapped I/O
```
**Mensaje 4**
```
"Figure 7.5 Memory-Mapped and Isolated I/O" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 7. E/S por interrupciones (p.16–18)

**Mensaje 1**
```
Subtítulo: E/S por interrupciones
```
**Mensaje 2**
```
Concepto: Procesamiento de una interrupción
```
**Mensaje 3**
```
Concepto SIC: Procesamiento de una interrupción
```
**Mensaje 4**
```
"Figure 7.6 Simple Interrupt Processing" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.7 Changes in Memory and Registers for an Interrupt" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 8. Diseño e identificación del dispositivo (p.19–20)

**Mensaje 1**
```
Subtítulo: Diseño e identificación del dispositivo
```
**Mensaje 2**
```
Concepto: Vectored interrupt
```
**Mensaje 3**
```
Concepto SIC: Vectored interrupt
```

---

### 9. Controladores 82C59A, 8255A, 82C55A (p.21–24)

**Mensaje 1**
```
Subtítulo: Controladores 82C59A, 8255A, 82C55A
```
**Mensaje 2**
```
Concepto: Controlador de interrupciones 82C59A
```
**Mensaje 3**
```
Concepto SIC: Controlador de interrupciones 82C59A
```
**Mensaje 4**
```
"Figure 7.8 Use of the 82C59A Interrupt Controller" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.9 The Intel 8255A Programmable Peripheral Interface" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.10 The Intel 8255A Control Word" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.11 Keyboard/Display Interface to 82C55A" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 10. DMA (p.25–29)

**Mensaje 1**
```
Subtítulo: DMA
```
**Mensaje 2**
```
Concepto: DMA (Direct Memory Access)
```
**Mensaje 3**
```
Concepto SIC: DMA (Direct Memory Access)
```
**Mensaje 4**
```
"Figure 7.12 Typical DMA Block Diagram" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.13 DMA and Interrupt Breakpoints During an Instruction Cycle" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.14 Alternative DMA Configurations" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.15 8237 DMA Usage of System Bus" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 11. Controlador 8237A (p.30–31)

**Mensaje 1**
```
Subtítulo: Controlador 8237A
```
**Mensaje 2**
```
Concepto: Fly-by DMA
```
**Mensaje 3**
```
Concepto SIC: Fly-by DMA
```
**Mensaje 4**
```
"Table 7.2 Intel 8237A Registers" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 12. Direct Cache Access y DDIO (p.32–38)

**Mensaje 1**
```
Subtítulo: Direct Cache Access y DDIO
```
**Mensaje 2**
```
Concepto: Direct Data I/O (DDIO)
```
**Mensaje 3**
```
Concepto SIC: Direct Data I/O (DDIO)
```
**Mensaje 4**
```
"Figure 7.16 Xeon E5-2600/4600 Chip Architecture" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.17 Comparison of DMA and DDIO" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 13. Evolución de la E/S y canales (p.39–40)

**Mensaje 1**
```
Subtítulo: Evolución de la E/S y canales
```
**Mensaje 2**
```
Concepto: Canal de E/S (I/O channel)
```
**Mensaje 3**
```
Concepto SIC: Canal de E/S (I/O channel)
```
**Mensaje 4**
```
"Figure 7.18 I/O Channel Architecture" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 14. Interfaces y buses externos (p.41–48)

**Mensaje 1**
```
Subtítulo: Interfaces y buses externos
```
**Mensaje 2**
```
Concepto: Universal Serial Bus (USB)
```
**Mensaje 3**
```
Concepto SIC: Universal Serial Bus (USB)
```

---

### 15. Caso IBM zEC12 (p.49–51)

**Mensaje 1**
```
Subtítulo: Caso IBM zEC12
```
**Mensaje 2**
```
Concepto: Subsistema de canales (channel subsystem)
```
**Mensaje 3**
```
Concepto SIC: Subsistema de canales (channel subsystem)
```
**Mensaje 4**
```
"Figure 7.19 IBM EC12 I/O Channel Subsystem Structure" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.20 IBM zEC12 I/O Frames-Front View" completa la explicación con las fuentes cargadas para el tema 7
```
```
"Figure 7.21 IBM EC12 I/O System Structure" completa la explicación con las fuentes cargadas para el tema 7
```

---

### 16. Resumen (p.52)

*Nota: la lámina menciona "Disk drive" y "Characteristics of I/O channels", pero esas láminas no existen en el PDF.*

**Mensaje 1**
```
Subtítulo: Resumen
```
