# A) Explicación del módulo INTERFACE 1K

**Idea:** el módulo base recibía una palabra de 18 bits. Este recibe **1024 palabras** y las guarda en $BUFFER[1024,\,18]$, usando un contador $cnt[10]$ como dirección ($2^{10} = 1024$).

---

**1.** Espera hasta que $csrdy = 1$ y el código en $CSBUS_{0:2}$ sea $010$, la dirección de esta interface. Así ignora los comandos de otros dispositivos.

**2.** Con $accept = 1$ confirma que recibió el comando. Según $CSBUS_3$ decide qué hacer: ir a recibir datos (1A) o responder el estado (3).

**3.** Espera a que $ready = 1$ para poder responder a la CPU.

**4.** Pone $busy$ en $CSBUS_0$ con $datavalid = 1$ y espera el $accept$ de la CPU. Sirve para que la CPU sepa si la interface está ocupada antes de enviar datos.

**1A.** Inicia la recepción: $cnt \leftarrow 0$ para empezar en la posición 0 de $BUFFER$ y $busy \leftarrow 1$ para avisar que está ocupada.

**2A.** Con $ready = 1$ avisa que puede recibir. Espera mientras $datavalid = 0$, o sea, hasta que la CPU ponga el dato en el bus.

**3A.** Con el dato válido, lo captura ($DR \leftarrow IOBUS$) y lo guarda en $BUFFER$ en la posición que indica $cnt$ (el decodificador $DCD(cnt)$ elige una de las 1024). Con $accept = 1$ confirma la recepción.

**4A.** Espera a que $datavalid$ baje a 0. Sin esto, volvería a 2A con el $datavalid$ anterior todavía en 1 y guardaría la misma palabra dos veces.

**5A.** Incrementa $cnt$ y revisa $\bigwedge / cnt$ (AND de sus 10 bits), que vale 1 solo si $cnt = 1023$. Como se evalúa antes del incremento, eso significa que la palabra recién guardada fue la 1024: va a 6A. Si no, vuelve a 2A por la siguiente.

**6A.** $busy \leftarrow 0$: la recepción terminó y el bloque está completo.

**7A.** `DEAD END`: fin de la secuencia.

---

> **Nota:** la bifurcación del paso 2 se mantiene igual que en el libro. Representa tres caminos: ignorar, transferir o responder estado.

---
## Aclaraciones

**Cómo leer una línea del código**

- $\leftarrow$ es una **transferencia con reloj**: el valor se guarda en el registro cuando llega el pulso de reloj. Ejemplo: $cnt \leftarrow INC(cnt)$.
- $=$ es una **conexión de bus sin reloj**: la señal vale eso mientras el módulo esté en ese paso, y vuelve a 0 al salir. Ejemplo: $accept = 1$.
- El `;` separa acciones **simultáneas**: todas ocurren en el mismo ciclo de reloj. Por eso en 3A se captura, se guarda y se confirma "a la vez".
- $\rightarrow (condición)/(destino)$ significa: si la condición es verdadera, salta al destino. Si es falsa, sigue con el paso siguiente.
- Un paso que salta **a sí mismo** es una espera. Ejemplo: $\rightarrow (\overline{ready})/(3)$ se queda en 3 mientras $ready = 0$ y sale cuando $ready = 1$.
- La barra sobre una señal ($\overline{ready}$) es su negación: vale 1 cuando la señal vale 0.
- Con varias condiciones, $(c_1, c_2)/(d_1, d_2)$ se lee: si se cumple $c_1$ va a $d_1$, si se cumple $c_2$ va a $d_2$.

**Las tres señales del handshake**

Sirven para que dos dispositivos se pasen un dato sin perderlo, aunque tengan velocidades distintas:

- $ready$: la pone quien **recibe**. Dice "estoy listo".
- $datavalid$: la pone quien **envía**. Dice "el dato en el bus es válido".
- $accept$: la pone quien **recibe**. Dice "ya lo tomé".

Los roles se invierten según la fase. En los pasos 1A a 5A la interface **recibe** datos de la CPU, así que ella pone $ready$ y $accept$. En el paso 4 la interface **envía** su estado, así que ella pone $datavalid$ y la CPU pone $accept$.

**Dos ramas, un solo módulo**

Después del paso 2 el módulo sigue una de dos ramas:

- La rama **sin letra** (3 y 4) responde la consulta de estado y vuelve a 1.
- La rama **con letra A** (1A a 7A) recibe el bloque y termina en `DEAD END`.

Las letras solo distinguen los pasos de la segunda rama. No indican un orden distinto de ejecución.

**Detalles de notación**

- $cnt \leftarrow 0,0,0,0,0,0,0,0,0,0$ es una constante vectorial: 10 bits, uno por cada bit de $cnt$.
- $BUFFER[1024,\,18]$ significa 1024 posiciones de 18 bits. Para escribir en una sola posición se usa $BUFFER * DCD(cnt)$. El decodificador $DCD$ convierte el número de 10 bits en una única línea activa entre 1024, y esa línea habilita la escritura solo en esa posición.
- $\bigwedge / cnt$ es una reducción AND: junta los 10 bits con AND y da un solo bit. Vale 1 solo si los 10 bits son 1, es decir, $cnt = 1111111111_2 = 1023$.
- $INC(cnt)$ suma 1. Desde 1023 vuelve a 0, así que el contador queda listo para un nuevo bloque.

**Cosas que conviene tener claras**

- **La interface solo recibe y guarda.** No imprime ni procesa los datos. Si luego hay que imprimirlos, eso lo hace otro módulo o el programa SIC del inciso b).
- **5A usa el valor antiguo de $cnt$.** En un mismo paso, la bifurcación lee los registros como estaban **antes** del reloj, y el incremento se guarda al final. Por eso se compara con 1023 y no con 0.
- **$DR$ viene del módulo base.** Captura la palabra, pero $BUFFER$ la toma directo de $IOBUS$, así que $DR$ no se vuelve a leer. No afecta el funcionamiento.
- **Cada registro destino aparece una sola vez por paso.** Por eso en 3A $DR$ y $BUFFER$ se cargan a la vez sin conflicto: son destinos distintos.
- **Paso 2:** las dos primeras condiciones iguales son del libro. Si no las puedes explicar, di que se mantienen como en el módulo original y que representan tres caminos.
 
