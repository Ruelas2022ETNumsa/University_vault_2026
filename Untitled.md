La prioridad de los módulos de **DMA (Direct Memory Access / Acceso Directo a Memoria)** sobre la **CPU** para acceder al bus del sistema y a la memoria principal es una regla de diseño fundamental en la arquitectura de computadores, y se justifica principalmente por tres razones basadas en el hardware y la naturaleza de las transferencias de datos:

### 1. Prevención de pérdida de datos (*Buffer Overflow*)
Los dispositivos periféricos rápidos que utilizan DMA (como discos magnéticos, unidades de cinta o controladores de red) operan transfiriendo grandes bloques de datos en tiempo real. Los procesos físicos y mecánicos de estos dispositivos (como un disco girando bajo el cabezal de lectura) **no se pueden detener ni ralentizar** una vez que se inicia la transferencia de un bloque. 
Como estos periféricos disponen de búferes de almacenamiento interno muy pequeños, si el controlador de DMA no obtiene acceso inmediato al bus para depositar (o extraer) el dato en la memoria RAM, el búfer interno del periférico se desbordará, lo que provocará una **pérdida irrecuperable de datos o un error de transmisión crítico**.

### 2. La CPU puede pausarse de forma segura
A diferencia de los dispositivos de E/S en tiempo real, **la CPU es un dispositivo síncrono controlado internamente** por el reloj del sistema, lo que significa que su ejecución puede pausarse o demorarse sin ninguna consecuencia negativa para los datos. 
Cuando el controlador de DMA solicita el bus activando la línea de petición de bus (*Bus Request* o HOLD), la CPU termina el ciclo de bus actual, coloca sus líneas de dirección, datos y control en un estado de alta impedancia (desconectándose eléctricamente del bus) y concede el control mediante la señal de concesión de bus (*Bus Grant* o HLDA). 
Durante este tiempo (habitualmente un solo ciclo de bus en la técnica de **robo de ciclo** o *cycle stealing*), la CPU simplemente se detiene o ralentiza su marcha temporalmente. **No se produce una pérdida de información** ni es necesario realizar un costoso proceso de salvar y restaurar el contexto del procesador como ocurriría en una interrupción de software. Una vez que el DMA libera el bus, la CPU continúa inmediatamente con su operación normal.

### 3. Frecuencia relativa de accesos al bus
Aunque la velocidad de transferencia de datos de los periféricos de alta velocidad es crítica en el instante de la transmisión, los accesos del DMA al bus de memoria siguen siendo **infrecuentes en comparación con el flujo constante de accesos que realiza la CPU** para captar instrucciones y operandos. 
Dar prioridad absoluta al DMA cuando este lo requiere asegura que las transferencias de E/S finalicen con éxito, mientras que el impacto de penalización sobre el rendimiento de la CPU es sumamente bajo, ralentizándola solo de forma marginal.

---

¿Te gustaría que elaboremos una comparación detallada entre el funcionamiento del **robo de ciclo** (*cycle stealing*) y el **modo ráfaga** (*burst transfer*) en las transferencias de DMA?