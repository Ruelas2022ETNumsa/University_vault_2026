A continuación se presenta la transcripción fiel y completa del módulo **PRINTER INTERFACE** correspondiente al **Ejemplo 9.3** de Hill & Peterson (*Digital Systems: Hardware Organization and Design*, 2ª edición, pp. 349-350), seguido de su análisis detallado paso a paso en formato de tabla con KaTeX inline.

### Módulo AHPL: PRINTER INTERFACE

```ahpl
MODULE: PRINTER INTERFACE
MEMORY: DR; CR; first(JK)
OUTPUTS: CHAR; ready; accept; print; feed
INPUTS: datavalid; wait
COMBUS: IOBUS

1. ready = 1
   -> (datavalid)/(1)
2. DR <- IOBUS; accept = 1; first <- 1
3. CR <- (DR[10:17] & first) | (DR[1:8] & ~first)
4. feed = RETURN(CR); print = ~RETURN(CR)
5. Null
6. -> (wait)/(6)
7. first <- 0
   -> (first, ~first)/(3, 1)
END SEQUENCE

CHAR = CR
END
```

---

### Lectura paso a paso de la secuencia de control

Esta tabla detalla el funcionamiento de cada paso de la secuencia de control e interacciones de señales:

| Paso | Operación | Condición | Estado resultante |
| :--- | :--- | :--- | :--- |
| `1.` | \( ready = 1 \) | — | **Espera activa**: La interfaz de la impresora inicia la secuencia activando la señal \( ready = 1 \) en el bus para indicar que está lista para recibir una nueva palabra de datos. |
| `1A.` | — | \( \overline{datavalid} \) | **Bucle de polling**: El control se bifurca recursivamente al Paso 1 mientras la señal de la CPU \( datavalid \) sea \( 0 \) (no hay dato en el bus). |
| `2.` | \( DR \leftarrow IOBUS \)<br>\( accept = 1 \)<br>\( first \leftarrow 1 \) | — | **Handshake y captura**: Al detectarse \( datavalid = 1 \), se carga la palabra de 18 bits en el registro intermedio \( DR \). Al mismo tiempo, se envía un pulso de un ciclo en \( accept = 1 \) como acuse de recibo para la CPU y se inicializa el flip-flop JK \( first \leftarrow 1 \) para procesar el primer carácter (carácter de la izquierda). |
| `3.` | \( CR \leftarrow (DR_{10:17} \land first) \lor (DR_{1:8} \land \overline{first}) \) | — | **Selección de carácter**: Se transfiere al registro de caracteres \( CR \) de 8 bits el carácter correspondiente. Si \( first = 1 \), se extraen los bits \( DR_{10:17} \); si \( first = 0 \), se extraen los bits \( DR_{1:8} \). |
| `4.` | \( feed = RETURN(CR) \)<br>\( print = \overline{RETURN(CR)} \) | — | **Comandos a la impresora**: La unidad lógica combinacional \( RETURN(CR) \) evalúa el carácter actual. Si es un retorno de carro (*Carriage Return*), se activa la línea \( feed = 1 \) para avanzar papel. Si no lo es, se activa \( print = 1 \) para imprimir el carácter normal en papel. |
| `5.` | Null | — | **Paso nulo de sincronización**: No se realizan transferencias físicas; se consume un ciclo de reloj para dar tiempo a que la impresora física reaccione y active su línea \( wait \). |
| `6.` | — | \( wait \) | **Bucle de espera de impresión**: El control permanece retenido en el Paso 6 mientras la impresora esté ocupada ejecutando la impresión o el avance de línea (\( wait = 1 \)). |
| `7.` | \( first \leftarrow 0 \) | — | **Actualización de carácter**: Se borra el flip-flop \( first \leftarrow 0 \) para indicar que el primer carácter ya ha sido procesado. |
| `7A.` | — | \( \rightarrow (first, \overline{first})/(3, 1) \) | **Bifurcación de control**: Si el estado previo de \( first \) antes del flanco de reloj era 1, la secuencia vuelve al Paso 3 para procesar el segundo carácter (\( DR_{1:8} \)). Si ya era 0, la palabra de 18 bits ha sido impresa por completo y se retorna al Paso 1 a esperar una nueva transmisión de la CPU. |
| `CHAR` | \( CHAR = CR \) | — | **Salida combinacional permanente**: Expresión fuera de la secuencia que conecta de forma continua la salida física \( CHAR \) con los bits del registro \( CR \). |

---
[[825 Hill Peterson Digital Systems Hardware Organization Design 9-10-11-13.pdf#page=350]]
*Example 9.3*
La interfaz permite deserializar una palabra de datos del sistema para imprimir dos caracteres consecutivos ASCII asincrónicamente mediante un protocolo de enlace asíncrono interactivo de tres líneas (*handshaking*).

¿Te gustaría generar un diagrama de tiempos TikZ con las transiciones de las señales de control durante este proceso de impresión? 🕒