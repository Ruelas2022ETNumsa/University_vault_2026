# Guía rápida de exposición (5 a 7 minutos)

## Orden de la exposición

1. **Enunciado (30 s):** es una interfaz de impresora con búfer de 1K palabras de 18 bits, con dos caracteres por palabra. Recibe un bloque, lo guarda y lo imprime solo hasta la última palabra con texto, sin los espacios vacíos del final.

2. **Variables (45 s):** no las leas todas, agrupalas:
   - `BUFFER` guarda el bloque y `cnt` es el puntero para recorrerlo.
   - `limit` guarda hasta dónde hay texto y `empty` cuenta las palabras vacías seguidas.
   - `has_data` indica si llegó algún texto, `first` elige el carácter alto o bajo, y `busy` indica si está ocupada.
   - `DR` guarda la palabra y `CR` el carácter que sale a la impresora.

3. **Etapa 1, pasos 1 a 4 (1 min):** espera ser seleccionada con `csrdy` y la dirección `010`. Si el comando es una consulta de estatus, responde `busy`. Si es una orden de datos, pasa a recibir.

4. **Etapa 2, pasos 1A a 8A (1,5 min):** reinicia contadores y pone `busy = 1`. Por cada palabra espera `datavalid`, la guarda en `BUFFER[cnt]` y confirma con `accept`. Si la palabra tiene texto, actualiza `limit` y `has_data`; si está vacía, suma a `empty`. Termina al llegar a 4 vacías seguidas o a 1024 palabras.

5. **Etapa 3, pasos 1B a 12B (2 min):** reinicia `cnt`. Si no hubo texto, salta a liberar la interfaz sin imprimir. Si hubo, lee la palabra y saca el carácter alto y luego el bajo. Un retorno de carro activa `feed` y cualquier otro carácter activa `print`. Antes de cada carácter espera a que `wait` baje. Al pasar `limit`, pone `busy = 0` y termina.

6. **Código y tabla (30 s):** el código es lo mismo que el diagrama en AHPL, y la tabla explica cada paso. Señalá un ejemplo, como `1B`: `cnt` a cero, y salto a `11B` si no hay texto.

---

## Guía del código (qué pasa en cada grupo de pasos)

**Pasos 1 a 4: atender el comando**
- **1:** espera a que la CPU seleccione la impresora (`csrdy = 1` y `CSBUS = 010`). Mientras no pase, se queda en 1.
- **2:** acepta el comando (`accept = 1`) y mira `CSBUS(3)`. Si vale 1 es una consulta de estatus y va a 3. Si vale 0 es una orden de datos: vuelve a 1 y arranca 1A a la vez.
- **3:** espera a que `ready` esté disponible para contestar.
- **4:** pone `busy` en `CSBUS(0)` con `datavalid = 1`, espera el `accept` de la CPU y vuelve a 1.

**Paso 1A: preparar la recepción**
- `cnt`, `empty` y `limit` quedan en 0, `has_data = 0` y `busy = 1`.

**Pasos 2A a 4A: recibir una palabra (handshake)**
- **2A:** pone `ready = 1` y espera a que llegue `datavalid`.
- **3A:** guarda la palabra en `DR` y en `BUFFER[cnt]`, y confirma con `accept = 1`.
- **4A:** mantiene `accept` hasta que `datavalid` baje a 0, y así queda lista para la siguiente palabra.

**Pasos 5A a 8A: clasificar y avanzar**
- **5A:** revisa si alguno de los dos caracteres de la palabra es distinto de 0.
- **6A (tiene texto):** `has_data = 1`, `limit = cnt + 1` y `empty = 0`.
- **7A (vacía):** `empty = empty + 1`.
- **8A:** `cnt = cnt + 1`. Si hay 4 vacías (`empty(0) = 1`) o el búfer se llenó, pasa a imprimir (1B). Si no, vuelve a 2A por otra palabra.

**Paso 1B: decidir si hay algo que imprimir**
- Pone `cnt = 0`. Si `has_data = 0`, salta a 11B sin imprimir. Si hay texto, sigue a 2B.

**Pasos 2B y 3B: leer y separar el carácter**
- **2B:** lee `BUFFER[cnt]` en `DR` y pone `first = 1`.
- **3B:** carga en `CR` el carácter alto (`DR(10:17)`) si `first = 1`, o el bajo (`DR(1:8)`) si `first = 0`.

**Pasos 4B a 6B: sacar el carácter a la impresora**
- **4B:** si `CR` es retorno de carro activa `feed`; si no, activa `print`.
- **5B:** paso nulo, da un ciclo para que la impresora levante `wait`.
- **6B:** espera mientras la impresora esté ocupada (`wait = 1`).

**Pasos 7B a 10B: siguiente carácter o siguiente palabra**
- **7B:** pone `first = 0`. Si el carácter que acaba de salir era el primero, vuelve a 3B por el segundo. Si era el segundo, sigue a 8B.
- **8B:** `cnt = cnt + 1`.
- **9B:** compara `cnt` con `limit` y guarda el resultado en `end_print`.
- **10B:** si llegó al límite, va a 11B. Si no, vuelve a 2B por la siguiente palabra.

**Pasos 11B y 12B: cerrar**
- **11B:** `busy = 0`.
- **12B:** fin de la secuencia.

---

## Ideas clave para repetir

- Guarda todo y luego imprime. `limit` evita imprimir los espacios vacíos del final.
- Una palabra con dos caracteres se imprime en dos vueltas gracias a `first`.
- `busy` está en 1 mientras recibe e imprime, y vuelve a 0 al final.

## Preguntas que pueden hacerte

- **¿Por qué 4 palabras vacías?** Es la condición de fin del bloque (`empty(0) = 1`, es decir, un valor de 4 o más).
- **¿Por qué `limit = cnt + 1`?** Apunta a la dirección siguiente a la última palabra con texto, y ahí se detiene la impresión.
- **¿Qué pasa si no llega texto?** `has_data = 0`, así que `1B` salta directo a `11B`.
- **¿Para qué sirve el paso 5B (Null)?** Da un ciclo para que la impresora levante `wait`.
