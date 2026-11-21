# Resumen 21 de noviembre de 2026: esquema del informe, plan de fuentes y análisis del control con ESP32

**Objetivo del día:** dejar claro cómo se debe armar el informe del brazo LEGO y cómo se van a reunir las fuentes. El brazo aún no está terminado, así que el informe se avanza por partes. También se analizó agregar un ESP32 y una página en el celular para controlar el brazo (secciones 5 y 6). No se modificó `ha7.py`.

---

## 1. Decisiones de hoy

| Tema | Decisión |
| ---- | -------- |
| Torre de Hanói | **Fuera por ahora.** Primero se arma bien el brazo; hacia el final se decide si se agrega. |
| Hardware | LEGO Inventor **51515** con Pybricks. |
| Estilo de citas | **APA 7** en todo lo que se escriba. El texto del docente lo indica de forma implícita (la "Guía resumen del manual de publicaciones con normas APA"). Aún no es definitivo. |
| Formato del informe | El esquema de la sección 2 (lo entregó el usuario). |
| ESP32 + celular | Idea futura, no implementada. No entra como parte del sistema actual. Se analizó la viabilidad (sección 5). |
| ESP32 ↔ hub | La idea del usuario es por **Bluetooth**. Antes de seguir hay que comprobar cómo usar el Bluetooth del ESP32. |
| Celular ↔ ESP32 | **Wi-Fi** directo. Se acepta el retraso como costo de controlar con sliders desde el celular. |

## 2. Esquema del informe

Respetar este orden y estos títulos.

### 1. Introducción y antecedentes
Indicar brevemente los antecedentes y el propósito general del trabajo.

### 2. Objetivo
Indicar el alcance o la profundidad del estudio y sus limitaciones.

### 3. Justificación del proyecto
- Por qué el estudio es importante para la institución y cuál es el escenario del proyecto.
- La justificación dice **por qué** se quiere hacer la investigación y **qué impacto** se busca lograr cuando termine (científico, tecnológico, económico, social, ambiental u otro).
- Responde a la pregunta: **¿para qué servirá?**

### 4. Desarrollo del proyecto
Incluye los conceptos teóricos en los que se fundamenta (**marco teórico**).

### 5. Conclusiones y recomendaciones

### 6. Referencias bibliográficas e internet

### Al final
- Nota o sección titulada **"Guía resumen del manual de publicaciones con normas APA"**.
- **Anexo:** lista de acrónimos.

## 3. Qué hay ya y qué falta frente a este esquema

El borrador `informe.md` se **reorganizó el 21-nov** según este esquema (copia de la versión anterior en `informe 1.md`). Las secciones 1 y 2 tienen contenido; la 3, 4 y 5 están como estructura con marcas `[pendiente]`. Al final tiene una guía breve de APA y el anexo de acrónimos.

| Sección del esquema | Material disponible | Falta |
| ------------------- | ------------------- | ----- |
| 1. Introducción y antecedentes | Contexto y trabajos relacionados de `informe.md` | Ya reubicado; completar con las fuentes de Perplexity y NotebookLM |
| 2. Objetivo | Objetivo general, específicos, alcance y limitaciones de `informe.md` | Ya reubicado |
| 3. Justificación | Nada escrito | Definir institución, escenario e impacto esperado |
| 4. Desarrollo | `resumen_16.md` (montaje, calibración, ha7.py) y `propuesta.md` | Marco teórico; pruebas cuando el brazo esté terminado |
| 5. Conclusiones | Nada | Depende de terminar el brazo |
| 6. Referencias | Lista de `referencia.md` | Pasar a formato APA tras leer los trabajos completos |
| Anexo | Nada | Lista de acrónimos |

**Acrónimos candidatos** (a confirmar según lo que quede en el texto final): GDL, HSV, IMU, USB, BLE, ESP32, API.

## 4. Plan de fuentes

1. **Perplexity** (modo Pro / Deep Research, fuentes Académico): buscar tesis y papers. El prompt se entregó en el chat el 21-nov.
2. **Descargar o guardar** las fuentes relevantes.
3. **NotebookLM:** cargar las fuentes y pedir que extraiga de forma exhaustiva los puntos importantes por tema.
4. **Verificar** cada dato contra la fuente original antes de citarlo. Hasta hoy, las referencias de `referencia.md` solo se leyeron por extractos.
5. Pasar las referencias a **APA**.

## 5. Análisis del control con ESP32 y celular (solo análisis, nada implementado)

**Idea:** el celular se conecta por Wi-Fi al ESP32 y muestra sliders. Hay botones para elegir la articulación (base, codo, muñeca, garra); el slider mueve solo la articulación activa. El ESP32 empaqueta los datos en bytes y los envía al hub por Bluetooth. El hub muestra en la terminal de Pybricks qué articulación está activa y cuántos grados se moverá.

**Conclusión:** es viable. Lo que falta decidir y probar es el canal ESP32 → hub.

### 5.1 Qué se reutiliza de `ha7.py` (leído hoy)

- Ya se decodifican bytes con `unpack` (la cámara llega como 4 bytes). Un paquete de comando se leería igual.
- "Un botón activo a la vez" replica la regla actual de un solo motor energizado.
- Se reutilizan `ARTICULACIONES` (rangos y multiplicadores), `limitar()` y `muestrear()` (umbral de 5500 mV).
- `mover()` es bloqueante (`run_target` más un bucle). Para sliders haría falta un modo nuevo (por ejemplo "R = remoto" en el menú) con `track_target`, que sirve para cambiar el objetivo de forma continua.
- `track_target` va lo más rápido posible. Con USB sin batería conviene limitar velocidad o torque (`ACELERACION` y `TORQUE_MAX` hoy están en `None`) o limitar el cambio de objetivo por ciclo. *(Inferencia, sin probar.)*

### 5.2 Canales ESP32 → hub

| Opción | Cómo funciona | A favor | En contra |
| ------ | ------------- | ------- | --------- |
| Cable UART por puerto libre (C o E) | `UARTDevice` de Pybricks o la librería PUPRemote (el ESP32 se presenta como sensor LEGO). Pines 5 y 6 del puerto a 3,3 V. | No usa Bluetooth (ya ocupado por la compu y el celular de la cámara). Baja latencia. | Hay que hacer un cable Powered Up. El ESP32 se alimenta aparte. |
| **BLE broadcast** (la idea del usuario) | El ESP32 emite anuncios Bluetooth sin conexión en el formato de Pybricks (identificador de LEGO, canal, intervalo de 100 ms). El hub los lee con `observe`. | Sin cables. Alguien ya propuso un ESP32 con este formato. | Una prueba con sniffer (City Hub, firmware 4.1.0b2) indica que observar funciona mal con el hub conectado a una compu. Unas 10 actualizaciones por segundo como máximo. La API ahora está en `pybricks.messaging.BLERadio`. |
| Conexión BLE directa ESP32 ↔ hub | Pybricks no tiene BLE serial nativo para microcontroladores (solicitud abierta). | | No recomendado. |

Nada está verificado con el Inventor 51515: la documentación habla de hubs Powered Up en general.

**Sobre el Bluetooth del ESP32:** Pybricks necesita Bluetooth de bajo consumo (BLE). Hay que confirmar que el modelo de ESP32 lo tenga (algunos modelos no traen Bluetooth) y que pueda emitir anuncios BLE con el formato de Pybricks.

### 5.3 Celular → ESP32

- Lo más simple: el ESP32 crea su propia red Wi-Fi y sirve una página web con botones y sliders. No hace falta instalar una app.
- Así el Bluetooth del celular queda libre para la cámara. Falta probar que el celular sostenga ambas cosas a la vez.
- Alternativas: Blynk o MIT App Inventor.

### 5.4 Paquete de bytes (propuesta)

Marco corto: cabecera fija, número de articulación (0 a 3), ángulo en 2 bytes con signo y un byte de control. En el hub se leería con `unpack`.

### 5.5 Cuidado del voltaje y la corriente

El brazo funciona por USB desde un cargador con corriente limitada. `ha7.py` ya evita apagones (un motor a la vez, vigilancia de voltaje con umbral de 5500 mV, motores sueltos al llegar, descansos entre fases), pero el modo remoto debe mantener todo eso:

- Un solo motor energizado: el botón activo elige cuál; los demás quedan sueltos.
- Seguir llamando a `muestrear()`.
- Limitar velocidad, torque o el paso por ciclo.
- Los límites de ángulo se aplican en el hub, no en la app.
- Si no llega ningún paquete en cierto tiempo, soltar todos los motores. Botón de parada.
- Punto a resolver: la pausa actual por voltaje bajo (`pausar()`) usa `input()` del teclado de la compu. En el modo remoto hay que decidir qué hacer al bajar el voltaje (por ejemplo, soltar todo e ignorar comandos hasta reiniciar).

### 5.6 Botón de accionar o movimiento automático (decisión pendiente)

**Propuesta (a confirmar con el usuario):** empezar con **botón de accionar**. El slider fija el ángulo objetivo (el hub lo muestra, sin mover), y al apretar "accionar" se mueve una sola vez.

- Es más seguro con la corriente limitada.
- Evita ráfagas de órdenes con el retraso del Wi-Fi y el Bluetooth.
- Permite revisar en la terminal el valor que llegó antes de mover.

El movimiento automático (el motor sigue al slider) puede probarse después, con límite de velocidad.

## 6. Plan de pruebas propuesto

1. **Etapa 0:** comprobar el ESP32 solo: modelo, Bluetooth BLE y emisión de anuncios.
2. **Etapa 1:** el ESP32 envía articulación y ángulo; el hub **no mueve motores**, solo muestra en la terminal de Pybricks qué articulación está activa y cuántos grados se movería.
3. **Etapa 2:** un solo motor con botón de accionar, velocidad y torque limitados, vigilando el voltaje.
4. **Etapa 3:** las cuatro articulaciones con botones de selección.
5. **Etapa 4:** página Wi-Fi con sliders en el celular.
6. **Etapa 5:** evaluar el modo automático.

Si el Bluetooth no funciona bien en la etapa 1, probar el cable UART.

## 7. Pendientes

1. Completar autores y años de las referencias en `informe.md` (APA) tras leer los trabajos completos.
2. Definir la **justificación** (institución, escenario, impacto).
3. Confirmar con el docente cómo debe aparecer la "Guía resumen del manual de publicaciones con normas APA". Por ahora quedó una guía breve al final de `informe.md`.
4. Terminar el brazo (ver pendientes de `resumen_16.md`, sección 4).
5. ~~Comprobar el ESP32 con Bluetooth (etapa 0)~~ Hecho el 21-nov: ESP32-WROOM-32 con MicroPython v1.29.0 y Bluetooth activo (sección 8).
6. ~~Código ESP32 → hub (etapa 1)~~ Hecho el 21-nov (sección 8). Falta la etapa 2: mover un solo motor con botón de accionar, reutilizando `mover()` de `ha7.py` (ya vigila el voltaje y suelta el motor al llegar). Elegir primero la articulación de prueba.
7. Decidir: botón de accionar o movimiento automático (sección 5.6).
8. Decidir cómo se maneja el voltaje bajo en el modo remoto (sección 5.5).

## 8. Avances de la tarde del 21-nov (etapas 0 y 1)

- **Respaldo del firmware original** del ESP32 (4 MB) y documentación en `esp32/firmware_original.md`.
- **MicroPython v1.29.0** instalado con Thonny en el ESP32-WROOM-32 (chip ESP32-D0WD-V3, COM6). Bluetooth de bajo consumo comprobado.
- `bleradio.py` copiado en `/lib` del ESP32 (8146 bytes).
- **`ha8.py`** (base `ha7.py`, modo R: recibe y muestra, no mueve motores) y **`esp32/emisor_prueba.py`** (emite `(articulacion, angulo, id_orden)` cada 3 segundos).
- **Resultado de la etapa 1: la comunicación ESP32 → hub funciona.** Según el usuario, los mensajes llegan casi al instante y al parecer todos; la matriz de luces del hub muestra la letra del puerto (F, D, A, B) y el brazo no se mueve, que es lo esperado en el modo R.
- Revisado en la terminal de Pybricks (reporte del usuario): llegaron todos los mensajes y estaban correctos, y los valores fuera de rango (codo 200, garra 120) se recortaron a los límites de seguridad. **Etapa 1 cerrada.**
- **Estado al terminar la sesión:** se queda en el inicio de la etapa 2 (mover un motor con botón de accionar). Sin decidir: con qué articulación empezar (se propuso la garra) y si el código nuevo va en `ha9.py` desde `ha8.py`.

## 9. Fuentes del análisis

- [Pybricks BLE broadcast/observe (commit en pybricks-api)](https://github.com/pybricks/pybricks-api/commit/3274cef849d91700905a56ec073cc2e3fb87f830)
- [Formato de mensajes broadcast/observe](https://github.yxlr123.workers.dev/pybricks/technical-info/blob/master/pybricks-ble-broadcast-observe.md)
- [ESP32 con el formato de broadcast (support #800)](https://github.com/pybricks/support/issues/800)
- [Mediciones con sniffer de broadcast y observe (discusión #2822)](https://github.com/orgs/pybricks/discussions/2822)
- [Generic UART Device (docs de Pybricks)](https://docs.pybricks.com/en/latest/iodevices/uartdevice.html)
- [UART en puertos LEGO y pinout](https://lightofshadow.bearblog.dev/how-to-enable-uart-communication-on-lego-mindstormspike/)
- [PUPRemote](https://pypi.org/project/pupremote/)
- [Solicitud de BLE Serial (support #2281)](https://github.com/pybricks/support/issues/2281)
- [Notas de versión de Pybricks 4.0.0](https://github.com/pybricks/pybricks-micropython/releases/tag/v4.0.0)
- [Motor, `track_target` (docs de Pybricks)](https://docs.pybricks.com/en/stable/pupdevices/motor.html)
