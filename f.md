```ahpl
2. MEMADBUS = PC; read = 1
   → (~SYN(busy))/(2)
3. null
   → (SYN(busy))/(3)
4. NO DELAY
   OBUS = 0, DATAOUT;
   IR ← OBUS(1:18)
```


### Detalles de funcionamiento de la secuencia modificada

1. **Paso 2 (Petición de lectura):** Debido a la eliminación del registro `MA` en la CPU con memoria asíncrona, se conecta directamente el contador de programa al bus de direcciones de memoria (**`MEMADBUS = PC`**). Se levanta la señal de lectura (**`read = 1`**) y se realiza un bucle de espera activa (polling) hasta que la memoria responda activando su señal de ocupado (**`SYN(busy) = 1`**), lo que acusa recibo de la solicitud.
2. **Paso 3 (Espera de ciclo):** Es un paso de espera pasiva (**`null`**) en el que el secuenciador permanece retenido mientras la memoria realiza su ciclo interno (**`SYN(busy) = 1`**). Una vez concluido el ciclo de lectura, la memoria coloca el dato en las líneas de salida y desactiva su bandera de ocupado, permitiendo al CPU salir del bucle.
3. **Paso 4 (Captura directa sin retraso):** Se define como un paso de transferencia directa sin ciclo de reloj adicional (**`NO DELAY`**). Se conecta la línea de datos obtenida de la memoria al bus interno concatenando un cero de relleno (**`OBUS = 0, DATAOUT`**) y se captura directamente sobre el registro de instrucción (**`IR ← OBUS(1:18)`**) evitando el paso intermedio por el registro `MD`.

[[825 Hill Peterson Digital Systems Hardware Organization Design 7.pdf#page=230]]
*Fig. 7.8 · Instruction fetch control with asynchronous memory*
justificación: Muestra el diagrama de tiempos y el esquema de control para la secuencia de búsqueda modificada utilizando un protocolo de handshake de dos líneas.