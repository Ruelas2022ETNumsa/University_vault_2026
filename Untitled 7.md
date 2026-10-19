## Comandos e instrucciones de E/S

**Idea central:** El procesador solicita operaciones de E/S emitiendo comandos específicos a los módulos de E/S mediante instrucciones que dependen del esquema de direccionamiento del sistema.

**Diapositivas (p.11, 13):**

p.11
* **Comandos de E/S (*I/O Commands*)**
  * Hay cuatro tipos de comandos de E/S que un módulo de E/S puede recibir cuando es direccionado por un procesador:
    1. **Control (*Control*)**
       * Se utiliza para activar un periférico y decirle qué hacer
    2. **Prueba (*Test*)**
       * Se utiliza para probar varias condiciones de estado asociadas con un módulo de E/S y sus periféricos
    3. **Lectura (*Read*)**
       * Hace que el módulo de E/S obtenga un elemento de datos del periférico y lo coloque en un buffer interno
    4. **Escritura (*Write*)**
       * Hace que el módulo de E/S tome un elemento de datos del bus de datos y posteriormente transmita ese elemento de datos al periférico

p.13
* **Instrucciones de E/S (*I/O Instructions*)**
  * Con la E/S programada existe una correspondencia estrecha entre las instrucciones relacionadas con E/S que el procesador obtiene de la memoria y los comandos de E/S que el procesador emite a un módulo de E/S para ejecutar esas instrucciones
  * La forma de la instrucción depende de la manera en que se direccionan los dispositivos externos
    * A cada dispositivo de E/S conectado a través de módulos de E/S se le asigna un identificador o dirección única
    * Cuando el procesador emite un comando de E/S, el comando contiene la dirección del dispositivo deseado
    * Por lo tanto, cada módulo de E/S debe interpretar las líneas de dirección para determinar si el comando es para él
  * **E/S mapeada en memoria (*Memory-mapped I/O*)**
    * Existe un único espacio de direcciones para las ubicaciones de memoria y los dispositivos de E/S
    * Se necesitan una sola línea de lectura y una sola línea de escritura en el bus

**Se completa con:** Stallings - Computer Organization and Architecture - 11ed.pdf
* **Secuencia de ejecución de los comandos en el módulo:**
  * En un comando de lectura (**Read**), el módulo de E/S interactúa con el periférico para depositar el dato en su registro de datos interno; posteriormente, el procesador solicita el dato y el módulo lo coloca en el bus de datos.
  * En un comando de control (**Control**), los parámetros transmitidos son específicos para cada periférico (por ejemplo, rebobinar una cinta magnética).
* **Aporte de Mano - Computer System Architecture:**
  * Clasifica las órdenes que recibe la interfaz en cuatro tipos: control, estado, salida de datos y entrada de datos (*control, status, data output, data input*), equivalentes a Control, Test, Write y Read de Stallings.

**Comparación con SIC:**

| Aspecto | Cap. 7 (Stallings) | SIC (Hill & Peterson) |
| - | - | - |
| Cómo se hace | La CPU ejecuta una instrucción de E/S que envía uno de cuatro comandos genéricos (Control, Test, Read, Write) al módulo de E/S a través del bus del sistema. | La CPU ejecuta la instrucción de transferencia `IOT` (código octal 75), la cual carga 12 bits en el registro `CSR` y los transmite por el bus `CSBUS` con la señal `csrdy = 1`. |
| Quién controla | La CPU emite la orden y controla la transferencia leyendo o escribiendo palabras en los registros del módulo de E/S. | La CPU controla la emisión del comando escribiendo en `CSR`/`CSBUS` y la transferencia mediante el bus de datos `IOBUS` o la prueba de bits con `TST`/`ISn`. |
| Ventaja | (No está en las láminas) Clasificación abstracta y universal aplicable tanto a esquemas de E/S aislada como a E/S mapeada en memoria. | Formato de instrucción `IOT` rígido pero estandarizado: los 6 bits superiores de `CSR` tienen significado uniforme (dispositivo, datos/estado, buffer) y los 6 inferiores dependen del periférico. |
| Limitación | (No está en las láminas) La codificación concreta de bits depende de la arquitectura específica del procesador y del fabricante del módulo de E/S. | La instrucción `IOT` está limitada a 8 dispositivos direccionables (bits `IR[6:8]`) y requiere lógica de decodificación individual en la interfaz de cada periférico. |

Conclusión: Stallings clasifica conceptualmente los comandos de E/S en cuatro tipos funcionales genéricos, mientras que el computador SIC define una estructura binaria de 18 bits para las instrucciones `IOT`/`TST` transmitidas mediante el registro `CSR` y los buses `CSBUS`/`IOBUS`.