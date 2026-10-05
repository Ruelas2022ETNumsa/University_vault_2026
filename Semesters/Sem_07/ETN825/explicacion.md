# Explicación del módulo INTERFACE 1K

---

## Idea general

El módulo base `PRINTER INTERFACE` recibía **una sola palabra** de 18 bits por `IOBUS` y la entregaba a la impresora. El inciso a) pide que la interface reciba **1K (1024) palabras** cada vez que la CPU lo ordena.

Para lograrlo se agregan dos elementos al módulo base:

- Una memoria interna $BUFFER[1024,\,18]$, que guarda las 1024 palabras recibidas.
- Un contador $cnt[10]$, que indica en qué posición de $BUFFER$ se guarda la siguiente palabra. Tiene 10 bits porque $2^{10} = 1024$, justo la cantidad de posiciones.

El módulo ya no tiene salidas hacia la impresora, porque su trabajo es solo **recibir y almacenar** el bloque.

La secuencia tiene tres partes:

1. **Pasos 1 a 4:** atender los comandos de la CPU (selección y consulta de estado).
2. **Pasos 1A a 5A:** recibir las 1024 palabras, una por una.
3. **Pasos 6A y 7A:** cerrar la recepción.

---

## Declaraciones

- $DR[18]$: registro de datos de 18 bits. Es el tamaño de una palabra, igual que $IOBUS$.
- $BUFFER[1024,\,18]$: memoria de 1024 palabras de 18 bits, donde queda el bloque completo.
- $cnt[10]$: contador que apunta a la posición actual de $BUFFER$.
- $busy$: flip-flop que indica si la interface está ocupada recibiendo un bloque.
- $csrdy$ (entrada): indica que hay un comando válido en $CSBUS$.
- $IOBUS[18]$: bus por donde llegan los datos.
- $CSBUS[12]$: bus de control, por donde la CPU selecciona el dispositivo y envía comandos.
- $ready$, $datavalid$, $accept$: señales del protocolo de **handshake** (el "diálogo" entre emisor y receptor para transferir cada palabra sin perder datos).

---

## Parte 1: atender comandos (pasos 1 a 4)

Esta parte viene del módulo base y no cambia.

**Paso 1: espera de selección.**
La interface se queda en este paso, repitiéndolo, hasta que se cumplan dos cosas: $csrdy = 1$ (hay un comando en $CSBUS$) y los bits 0, 1 y 2 de $CSBUS$ valen $0,\ 1,\ 0$ (el código $010$, que es la dirección de esta interface). La barra sobre toda la expresión significa que mientras la condición **no** se cumpla, el módulo vuelve al paso 1. Esto sirve para que la interface ignore los comandos dirigidos a otros dispositivos.

**Paso 2: aceptar el comando y decidir qué hacer.**
Con $accept = 1$ se le confirma a la CPU que el comando fue recibido. Después, según el bit 3 de $CSBUS$, el módulo se bifurca hacia tres caminos posibles: volver al paso 1, ir al paso 1A (orden de transferir datos) o ir al paso 3 (consulta de estado).

**Paso 3: esperar a que la CPU esté lista.**
Si la CPU pidió el estado, la interface espera hasta que $ready = 1$. Se hace así para no responder antes de que la CPU pueda leer la respuesta.

**Paso 4: responder el estado.**
Se coloca $busy$ en $CSBUS_0$ y se activa $datavalid = 1$, es decir: "este dato es válido, léelo". El módulo se queda en este paso hasta que la CPU responde con $accept = 1$, y entonces vuelve al paso 1. La utilidad de esta consulta es que la CPU puede **preguntar si la interface está ocupada antes de enviar datos**, y así no interrumpe una recepción en curso.

---

## Parte 2: recibir el bloque de 1K (pasos 1A a 5A)

Esta parte es la que se modificó respecto al módulo base.

**Paso 1A: inicializar la recepción.**
Se hacen dos cosas a la vez, en el mismo ciclo de reloj:

- $cnt \leftarrow 0,0,0,0,0,0,0,0,0,0$ pone el contador en cero. Así la primera palabra se guarda en la posición 0 de $BUFFER$.
- $busy \leftarrow 1$ avisa que la interface está ocupada. Si la CPU consulta el estado durante la recepción, recibirá $busy = 1$.

**Paso 2A: avisar que se puede enviar.**
Con $ready = 1$ la interface le dice a la CPU: "estoy lista para recibir una palabra". Se queda en este paso mientras $datavalid = 0$, es decir, mientras la CPU todavía no coloca el dato en el bus.

**Paso 3A: capturar y guardar la palabra.**
Cuando $datavalid = 1$, el dato en $IOBUS$ es válido. En un solo paso:

- $DR \leftarrow IOBUS$ captura la palabra en el registro de datos.
- $BUFFER * DCD(cnt) \leftarrow IOBUS$ la guarda en $BUFFER$. El decodificador $DCD(cnt)$ convierte el valor de $cnt$ (10 bits) en una sola línea activa entre 1024, y así selecciona exactamente **una posición** de memoria donde escribir.
- $accept = 1$ le confirma a la CPU que la palabra fue recibida.

Todo va en el mismo paso porque el dato en $IOBUS$ solo está garantizado mientras $datavalid = 1$.

**Paso 4A: cerrar el handshake de esa palabra.**
La interface espera a que la CPU baje $datavalid$ a 0. Este paso es necesario: si se volviera directo a 2A, $datavalid$ seguiría en 1 por la palabra anterior y la interface guardaría **la misma palabra otra vez**. Esperar a que baje asegura que la siguiente vez que $datavalid$ valga 1 sea por una palabra nueva.

**Paso 5A: avanzar y decidir si terminó.**
Se hacen dos cosas en el mismo paso:

- $cnt \leftarrow INC(cnt)$ incrementa el contador para apuntar a la siguiente posición.
- La bifurcación usa $\bigwedge / cnt$, que es el AND de los 10 bits de $cnt$. Esa reducción vale 1 solo cuando todos los bits son 1, o sea $cnt = 1023$, la última posición.

Como la bifurcación evalúa $cnt$ **antes** del incremento, cuando vale 1023 significa que la palabra recién guardada fue la número 1024. Entonces el módulo salta a 6A. En cualquier otro caso vuelve a 2A para recibir la siguiente palabra. Al incrementarse desde 1023, el contador vuelve a 0 y queda listo para el siguiente bloque.

---

## Parte 3: cierre (pasos 6A y 7A)

**Paso 6A: liberar la interface.**
$busy \leftarrow 0$ indica que la recepción terminó y la interface ya no está ocupada. Si la CPU consulta el estado ahora, sabrá que el bloque completo ya está almacenado.

**Paso 7A: fin.**
`DEAD END` detiene la secuencia. El módulo queda esperando un nuevo reinicio. Después de `END SEQUENCE` el módulo cierra con `END`.

---

## Resumen para la exposición

El módulo trabaja como un ciclo de tres fases: **escuchar** al sistema (1 a 4), **recibir** 1024 palabras repitiendo el ciclo *esperar dato, guardar, confirmar, esperar que termine, avanzar* (2A a 5A), y **cerrar** liberando $busy$ (6A y 7A). El contador $cnt$ cumple dos funciones a la vez: es la dirección de escritura en $BUFFER$ y es el criterio de parada, porque su AND de reducción detecta la posición 1023.

> **Nota:** la bifurcación del paso 2, $(\overline{CSBUS_3},\ \overline{CSBUS_3},\ CSBUS_3)/(1,\ 1A,\ 3)$, se mantiene tal como aparece en el módulo original del libro. Si preguntan por ella, lo importante es que representa tres caminos: ignorar el comando, iniciar una transferencia o responder el estado.
