## Dispositivos externos

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

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf *(⚠ todo lo de abajo viene de NotebookLM: verificar página en el PDF)*
* **Función de cada bloque:**
  * Lógica de control: controla la operación del dispositivo según los comandos del módulo de E/S.
  * Transductor: convierte entre señales eléctricas y la forma de energía propia del entorno.
  * Buffer: guarda temporalmente los datos durante la transferencia.
* **Capacidad del buffer:** 8 a 16 bits en dispositivos en serie; mucho mayor en dispositivos orientados a bloques, como controladores de disco.
* **Enfoque funcional vs. estructural:** los discos y cintas son memoria en la jerarquía funcional, pero estructuralmente se comportan como dispositivos externos controlados por módulos de E/S.

**Comparación con SIC:** *(⚠ verificar cada celda del SIC contra Hill & Peterson. AHPL, `IOBUS` y `CSBUS` no son relevantes para la exposición.)*

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Clasificación de dispositivos | Tres categorías: legibles por humanos, legibles por máquina y de comunicación. | No aparece en las fuentes del SIC. |
| Interfaz del periférico | El periférico contiene lógica de control, buffer y transductor, conectándose al módulo de E/S por un enlace dedicado. | ⚠ Cada periférico dispone de un módulo de interfaz explícito que lo adapta al bus de E/S. |
| Temporización física | ⚠ (11ed, no de la lámina) La lógica de control y el buffer absorben las diferencias de velocidad del medio físico. | ⚠ Se diseñan generadores de pulso con tiempos explícitos (p. ej., 100 µs y 4 ms). |

Conclusión: ⚠ pendiente de verificar contra Hill & Peterson. Lo que sí se sostiene: el Cap. 7 presenta un modelo conceptual del dispositivo externo; la comparación con el SIC depende de lo que confirmen sus fuentes.

---

## Teclado/monitor e IRA

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

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf *(⚠ verificar página en el PDF)*
* **Normativa del código IRA:** definido en la Recomendación ITU-T T.50 (antes Alfabeto Internacional Nº 5, IA5). Su variante nacional en EE.UU. es ASCII (*American Standard Code for Information Interchange*).

**Comparación con SIC:** *(⚠ verificar contra Hill & Peterson)*

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Codificación de caracteres | IRA/ASCII de 7 bits (128 caracteres), con caracteres imprimibles y de control. | ⚠ Maneja caracteres como vectores (p. ej., ASCII o Hollerith de 12 bits) que pasan por el acumulador `AC` o por buffers. |

Conclusión: ⚠ pendiente de verificar contra Hill & Peterson.
