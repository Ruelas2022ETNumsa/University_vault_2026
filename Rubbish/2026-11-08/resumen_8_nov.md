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

- `ha.py`: **programa base de referencia** para el movimiento (ver sección 4).
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

## 5. Pendientes

- Actualizar `ha.py` con el nuevo mapa de puertos: hombro A, muñeca C, codo D, garra E.
- Decidir si se agrega `stop()` tras cada articulación en `ha.py` o si se mantiene el hold, ya que el brazo podría caer por gravedad al soltar.
- Definir el uso del sensor de color (puerto F).
