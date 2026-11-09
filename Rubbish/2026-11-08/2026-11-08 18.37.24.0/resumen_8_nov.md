# Resumen 8 noviembre 2026

Contexto del brazo robótico con Pybricks y el hub LEGO Inventor 51515, alimentado por USB desde la PC.

## 1. Estado del cableado (recableado el 8-nov-2026)

El brazo se recableó, así que los puertos de `ha.py` ya no coinciden con el hardware real.

| Puerto | Dispositivo | Rol confirmado (visualmente) |
| ------ | ----------- | ---------------------------- |
| A | Motor mediano Technic | **hombro** |
| B | vacío | sin uso |
| C | Motor mediano Technic | **muñeca** |
| D | Motor mediano Technic | **codo** |
| E | Motor mediano Technic | **garra** |
| F | **Sensor de color** | sensor (nuevo) |

- Total: 4 motores (A, C, D, E) y 1 sensor de color (**puerto F**).
- Los roles se determinaron con `detect_motor.py`, probando un motor a la vez de forma visual.

## 2. Comparación con `ha.py` (pendiente de actualizar)

| Rol | Puerto en `ha.py` (viejo) | Puerto real (nuevo) |
| --- | ------------------------- | ------------------- |
| hombro | A | A (igual) |
| codo | C | **D** |
| muñeca | B | **C** |
| garra | F | **E** |

- El puerto F, que en `ha.py` era la garra, ahora tiene el sensor de color. `ha.py` fallaría tal cual al crear `Motor(Port.F)`.
- Los multiplicadores y rangos por articulación de `ha.py` (A ×3, C ×1, B ×3) están ligados a los nombres de articulación, no al puerto. Hay que revisar que sigan correspondiendo a cada articulación tras el cambio.

## 3. Programas en esta carpeta

- `ha.py`: **programa base de referencia** para el movimiento (ver sección 4). Quedó con el mapa de puertos viejo.
- `ha2.py`: versión con el mapa nuevo (A hombro, D codo, C muñeca, E garra) que **suelta cada motor al llegar a su destino**. **Probado: funciona sin complicaciones** (ver sección 5).
- `ha3.py`: `ha2.py` + reinicio automático al terminar la secuencia + monitoreo de la inclinación del hub (ver sección 6).
- `ha4.py`: `ha3.py` + estado inicial a 0 en paralelo con la entrada de ángulos + muñeca a 0 tras agarrar (ver sección 7). Reemplazado por `ha5.py`.
- **`ha5.py`: programa de trabajo actual** (ver sección 8).
- `puertos.py`: detecta qué hay en cada puerto A-F y lo imprime en la consola de Pybricks.
- `detect_motor.py`: prueba los motores detectados uno por uno, en orden alfabético.
  - Pide `y`/`Y` por puerto, gira 270° a 200°/s, vuelve a 0 y frena el motor antes de pasar al siguiente.

## 4. Por qué `ha.py` es la referencia base

`ha.py` mueve **un motor a la vez**, esperando a que termine antes de pasar al siguiente (A → C → B, y la garra aparte). Esto limita la corriente en un hub alimentado por USB/PC.

Detalle de cómo funciona realmente:
- Cada movimiento usa `run_target(200, objetivo, wait=False)` y espera a que termine, vigilando voltaje y corriente.
- Al terminar, el motor queda en **hold**, sosteniendo su posición. **No se apaga después de cada movimiento.**
- Los motores se sueltan (`detener_todo()`) solo en el descanso entre fases (TAKE → LEFT → INICIO) y al final del programa.
- Si el voltaje baja de 5000 mV durante 3 muestras seguidas, pausa y espera `g` + Enter (continuar) o `x` (abortar).

Conclusión: `ha.py` garantiza un solo motor **moviéndose** a la vez, pero los motores ya movidos siguen consumiendo corriente de hold hasta el siguiente descanso. `detect_motor.py` sí hace `stop()` a cada motor al terminar su prueba, de modo que solo hay uno energizado en todo momento.

## 5. Resultado de `ha2.py`: funciona sin complicaciones

Se probó la secuencia completa (TAKE: 45°/45°/45°, LEFT: 0°/0°/0°, INICIO) con el hub conectado por USB. Terminó sin apagarse y sin pausas por voltaje.

- Cada motor se suelta (`stop()`) al llegar a su destino, así que solo hay un motor energizado a la vez.
- Batería en reposo: 8410 mV.
- Voltaje mínimo: **6637 mV** (hombro), muy por encima del umbral de pausa de 5500 mV. Pausas: 0.
- Corriente máxima: **502 mA** (hombro).
- Al soltar los motores hay pequeños desvíos de pocos grados (hombro 47.7° pedido 45°, muñeca 43.3° pedido 45°; en LEFT hombro -1° y codo -4° pedidos 0°).
- Sentido de giro: con `Direction.CLOCKWISE` un ángulo positivo gira a favor del reloj mirando el motor de frente. En el brazo puede verse al revés por los engranajes.

Conclusión: soltar cada motor al llegar es viable en este brazo y es el comportamiento que se mantiene en `ha3.py`.

## 6. `ha3.py`: diferencias respecto a `ha2.py`

- **Reinicio automático:** al terminar la secuencia (toma, traslado, suelta e inicio) vuelve a pedir los ángulos de TAKE y LEFT, como si se reiniciara el programa. Se hace `reset_angle(0)` en cada ciclo porque el brazo vuelve a inicio.
- **Aborto:** si la secuencia se aborta (`x` tras voltaje bajo), no se hace reset, porque el brazo puede no estar en inicio.
- **Salida:** `x` + Enter en cualquier pregunta de ángulos o menú cierra el programa.
- **Inclinación del hub** (`hub.imu.tilt()`, cabeceo y balanceo): se imprime al inicio y al final de cada ciclo. Con `MOSTRAR_INCLINACION_POR_MOVIMIENTO = True` también se imprime tras cada cambio de posición. Por defecto está en `False`.
- Los ángulos de los motores se siguen mostrando en la consola como antes.

## 7. `ha4.py`: primera corrección del flujo (reemplazado por `ha5.py`)

- **Estado inicial:** al arrancar, los motores van a 0 de a uno (muñeca → codo → hombro → garra), sin pedir nada, mientras el usuario escribe los ángulos. Para eso se leía el teclado sin bloquear.
- **TAKE:** tras cerrar la garra, la muñeca vuelve a 0 para no arrastrar el objeto.
- **Problema encontrado en la prueba:** el hombro también debía volver a 0 (el brazo seguía pareciendo arrastrar el objeto), y la lectura de teclado en paralelo hacía que no apareciera el mensaje para ingresar ángulos y que el primer Enter se tomara como ángulo erróneo.

## 8. `ha5.py`: programa de trabajo actual

Usa el mapa de puertos nuevo (A hombro, D codo, C muñeca, E garra) y suelta cada motor al llegar a su destino, con un solo motor energizado a la vez.

**Flujos**
- **TAKE:** garra abre → hombro → codo → muñeca → garra cierra → **muñeca a 0 → hombro a 0** (movimiento más limpio, sin arrastrar el objeto).
- **LEFT:** hombro → codo → muñeca → garra abre (suelta el objeto).
- **INICIO:** muñeca → codo → hombro → garra, todos a 0.

**Arranque**
- Calibra todos los motores a 0 de a uno, y al terminar pide un **Enter** antes de mostrar la entrada de ángulos. Se quitó la lectura de teclado en paralelo de `ha4.py`.
- Hace `reset_angle(0)` tras calibrar y al final de cada secuencia completa, así los pequeños desvíos no se acumulan.
- Al terminar la secuencia vuelve a pedir valores, como si se reiniciara. Tras una secuencia abortada (`x` por voltaje bajo) vuelve a calibrar a 0 en el siguiente ciclo.

**Monitoreo**
- Pausa si el voltaje baja de 5500 mV durante 3 muestras seguidas (`g` + Enter continúa, `x` aborta) y avisa por debajo de 6000 mV.
- Inclinación del hub (cabeceo y balanceo) al inicio y al final de cada ciclo. `MOSTRAR_INCLINACION_POR_MOVIMIENTO = True` la imprime tras cada movimiento.
- Resumen de voltaje mínimo, corriente máxima y pausas al final de cada ciclo.

## 9. Ideas discutidas, aún sin implementar

- **Usar la IMU del hub para medir el ngulo real de hombro y codo.** Sirve como medición absoluta independiente del encoder, pero solo ve giros en un plano vertical, mide la suma de ambos giros si el hub está en un eslabón común y debe leerse con el brazo quieto. No consume corriente de los motores. Antes de integrarlo conviene un experimento que lea `tilt()` con el brazo en posiciones conocidas.
- **Otras lecturas disponibles:** `motor.load()`, `motor.speed()`, `motor.stalled()`, y en el hub `up()`, `acceleration()`, `angular_velocity()`, `heading()`, `rotation()`.

## 10. Pendientes

- Probar `ha5.py` completo: hombro a 0 tras tomar el objeto, Enter tras la calibración y reinicio entre ciclos.
- Revisar si el codo también debe volver a 0 tras tomar el objeto.
- Probar ángulos más grandes y vigilar el voltaje mínimo.
- Vigilar si los desvíos al soltar los motores crecen con más movimientos.
- Revisar si la garra deja caer el objeto con `SOLTAR_GARRA_CERRADA = True` (si pasa, ponerlo en `False`).
- Definir el uso del sensor de color (puerto F).
- Decidir si se usa la IMU del hub para hombro y codo (primero el experimento de `tilt()`).
- `ha.py` queda solo como referencia histórica con el mapa de puertos viejo.
