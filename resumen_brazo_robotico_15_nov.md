# Brazo robótico LEGO con visión: resumen y opciones

Fecha: 15 de noviembre de 2026

**Objetivo:** un brazo robótico con hub LEGO MINDSTORMS Inventor (51515) y 4 motores, corriendo Pybricks, que agarre una pelota quieta en cualquier punto de su alcance.

**Restricciones:**
- Solo se puede accionar **un motor a la vez** (límite de corriente).
- La pelota está estática en cada intento.

---

## 1. Qué se discutió, en orden

1. **Hub ↔ ESP32 por Bluetooth.** Se planteó que Pybricks puede difundir mensajes cortos por BLE (broadcast) y que un ESP32 podría recibirlos. Se propuso mandar un byte de 8 banderas (1/0), con un canal para cada dirección.
2. **ESP32 con cámara como "ojos".** La idea era ESP32-CAM detectando la pelota por color, convirtiendo su posición a ángulos de motor y mandándolos al hub.
3. **Cámara del celular con Pybricks.** Se encontró el proyecto "Robotic arm with vision", donde el celular hace de sensor de visión y manda `x, y, width, height` al hub. Se revisó la documentación y se concluyó que **esta ruta evita el ESP32 y la programación de visión**.
4. **Búsqueda de proyectos similares** para ambos caminos (sección 4 y 5).

---

## 2. Opción A: cámara del celular con Pybricks (recomendada para empezar)

**Qué es.** Pybricks permite usar el celular como "smart sensor": la app convierte la imagen de la cámara en números y los manda al hub por Bluetooth. El hub sigue corriendo tu programa.

**Datos del rastreador de color** (confirmado en la guía oficial):
- Entrega 4 valores: `x`, `y`, `width`, `height`.
- Son **porcentajes (0 a 100) del lado más largo de la imagen**, no píxeles.
- Si no ve el color, todo es 0. Si hay varios objetos, entrega solo el más grande.
- El color a buscar se configura enviando un byte con la mitad del tono (hue): `app.configure(0, 0, bytes([Color.X.h // 2]))`.

**Cómo se conecta** (según la guía, descrito para SPIKE Prime):
1. Conectar el hub desde la compu con Pybricks, sin abrir la cámara.
2. Apretar el botón Bluetooth del hub para que vuelva a parpadear.
3. Abrir Pybricks en el celular y conectarse al mismo hub, sin cargar programa.
4. Tocar el ícono del teléfono para encender la cámara.
5. Iniciar el programa (desde la compu o con el botón del hub).

**Celular:**
- Android: funciona bien con Chrome.
- iPhone: Safari y Chrome no tienen Bluetooth web, hay que usar un navegador como Bluefy.
- Opcional: conexión USB con adaptador OTG (solo Android), más rápida y estable.

**Estado de la función.** La guía la presenta como **función nueva en beta** y recomienda probar con [Pybricks Beta](https://beta.pybricks.com/). No verifiqué si ya salió de beta.

**Cómo funciona el proyecto del brazo** (archivo `spike_arm_camera.py`):
- Dos tareas en paralelo: una lee y desempaqueta los 4 valores, la otra mueve el brazo.
- La base gira hasta ver un objeto grande (`width > 8`) y centrado (`70 <= x <= 80`).
- Luego baja, cierra la pinza hasta que se atasque (`run_until_stalled`), sube, gira 360° y suelta.
- Para evitar falsos positivos con piezas magenta, usan un tono de referencia más anaranjado (`hue=8`).

**Qué hay que cambiar para tu brazo:**
- `PrimeHub` por `InventorHub` (hub 51515).
- Puertos, nombres de motores y ángulos (hay que calibrarlos a mano).
- El color de referencia, según tu pelota.
- **El arranque con `multitask`** mueve 3 motores a la vez y va contra tu límite de corriente. Hay que pasarlo a movimientos secuenciales.
- **Limitación del proyecto original:** solo agarra objetos a un radio fijo (baja siempre la misma distancia). Para "cualquier parte" hay que usar `y` y/o `height` para decidir cuánto extender hombro y muñeca, con una tabla calibrada.

**Pendiente de verificar con el 51515:**
- La guía dice que la técnica funciona con cualquier hub que corra Pybricks, pero **no menciona el Inventor** en la parte de la segunda conexión Bluetooth. Como tiene la misma electrónica que el SPIKE Prime debería tener botón Bluetooth y aceptar dos conexiones, pero eso es una deducción, no algo confirmado.
- La guía muestra `AppData` importado desde `pybricks.messaging` en el código, pero el texto dice `pybricks.tools`. Usar la que traiga tu archivo y probar la otra si da error.

---

## 3. Opción B: ESP32 (con cámara) como cerebro de visión

**Idea inicial.** ESP32-CAM o ESP32-S3 con cámara fija sobre la zona de trabajo. Detecta la pelota por color (umbral, sin IA), calcula (x, y) y la convierte en ángulos con una tabla de calibración. Manda los ángulos al hub.

**Comunicación con el hub:**
- **BLE broadcast de Pybricks** (`hub.ble.broadcast` / `hub.ble.observe`): sirve para mensajes cortos, sin conexión. *No verifiqué en la documentación la codificación exacta del paquete ni el ID de fabricante; hay que mirarla antes de implementar.*
- **Cable (alternativa):** la placa **LMS-ESP32** de Anton's Mindstorms conecta un ESP32 a un puerto del hub con la librería PUPRemote, y el hub llama funciones del ESP32. El ejemplo que revisé es con SPIKE y una cámara Pixy2. *No verifiqué disponibilidad, precio ni compatibilidad con el Inventor.*

**Lo que mostraron los proyectos encontrados (sección 5):**
- El ESP32-CAM es limitado. Varios proyectos le mandan la imagen por Wi-Fi a una PC que la procesa con OpenCV, y solo devuelven (x, y) al microcontrolador.
- Para detección simple de una mancha de color existen cámaras que ya entregan x, y sin programar visión (Pixy2, OpenMV, WonderCam). Un foro de Arduino lo recomienda justamente para este caso.
- Pixy2 consume 240 mA de forma permanente según el ejemplo de LMS-ESP32, algo a tener en cuenta con tu límite de corriente.
- La propia cámara del celular, por lo anterior, resulta más simple.

---

## 4. De (x, y) a una posición del brazo (el "z")

Con una cámara fija y una pelota siempre apoyada en la mesa, no necesitás medir z: está dado por la altura de la mesa. Lo que hay que resolver es la relación entre la imagen y los ángulos del brazo:

- **Calibración por puntos (lo más práctico con LEGO):** poner la pelota en 6 a 10 posiciones conocidas, anotar los ángulos de motor que funcionan, y armar una tabla o fórmula que los relacione con (x, y) de la imagen.
- **Transformación calibrada cámara→mundo:** un proyecto universitario (sección 5) usa una matriz de transformación calibrada ("eye-to-hand") que convierte los centroides 2D de la imagen en coordenadas (X, Y, Z) del espacio de trabajo, y luego cinemática para llegar ahí.
- **Verificar el alcance:** ese mismo proyecto comprueba que el punto objetivo esté dentro del área alcanzable del brazo antes de moverlo (para un brazo de 2 segmentos, la distancia al punto debe estar entre |L1 − L2| y L1 + L2).
- **Profundidad con una sola cámara:** si la cámara va montada en el brazo, el tamaño aparente (`width`/`height`) o la posición vertical `y` sirven de indicador de distancia.

---

## 5. Proyectos y fuentes encontrados

### Cámara del celular con Pybricks
- [Robotic arm with vision (proyecto oficial)](https://pybricks.com/project/robot-arm-camera-tracker/): el que se quiere replicar.
- [Use your phone as a smart sensor (guía)](https://pybricks.com/learn/smart-sensors/getting-started/): conexión, valores, Python, otros hubs.
- [Line following con cámara](https://pybricks.com/learn/smart-sensors/line-camera/) y [Image classification](https://pybricks.com/learn/smart-sensors/machine-learning/): otros sensores del celular (línea y clasificación por machine learning).
- [Groceries with machine learning](https://pybricks.com/project/machine-learning-groceries/): otro proyecto con SPIKE Prime y visión.
- [Pybricks Beta](https://beta.pybricks.com/): donde probar la función nueva.
- [Discusión en GitHub sobre las páginas antiguas de visión](https://github.gg22.workers.dev/orgs/pybricks/discussions/2706): indica que las funciones antiguas ya están integradas en Pybricks.

### ESP32 con cámara y detección de objetos
- [ESP32-CAM ball detector (ElectronicWings)](https://www.electronicwings.com/users/AliceBrown/projects/5336/esp32-cam-based-ball-detector): detecta pelotas con Python y OpenCV a partir del video de la ESP32-CAM.
- [Ball detection on ESP32-CAM and transfer to ESP32 (UCLA LEMUR)](https://uclalemur.com/blog/foray-ball-detection-on-esp-32-cam-and-transfer-back-to-esp-32-board): detecta una pelota verde en una PC y manda su (x, y) a otro ESP32, o (-1, -1) si no la ve. Comenta que se podría enviar también el área o la distancia.
- [Foro Arduino: ESP32-CAM calcula (x, y) y manda a otro ESP32](https://forum.arduino.cc/t/advice-on-using-esp32-cam-to-capture-image-and-send-data-to-esp32/1454348): plantea justo la arquitectura de la Opción B y sugiere la Pixy2 como alternativa sin programación.
- [Quargi: color tracking con ESP32-CAM y robot con brazo](https://github.com/lily-osp/Quargi): ESP32-CAM detecta un color y manda datos por serie a un Arduino.
- [Shell Game: brazo con ESP32 y visión en PC](https://github.com/roboSobia/Shell-Game): cámara IP más OpenCV en la PC, comandos al ESP32 que mueve el brazo; destaca que calibrar los ángulos de los servos es lo más crítico.
- [Proyecto ECE445 (Illinois): clasificación con brazo, ESP32 y mapeo imagen→(X, Y, Z)](https://courses.grainger.illinois.edu/ece445zjui/getfile.asp?id=25989): segmentación por color y YOLOv8-nano, transformación calibrada a coordenadas 3D.
- [MaxArm de Hiwonder (ESP32): clasificación por color con cinemática inversa](https://hackster.io/HiwonderRobot/maxarm-arduino-robot-arm-conduct-color-sorting-in-two-ways-8b4dc1): brazo basado en ESP32 que detecta color y manda (x, y) a la cinemática inversa.
- [Foosball con OpenMV: seguimiento de bola a QVGA](https://forums.openmv.io/t/automated-foosball-goalkeeper/11663): recomienda QVGA (320×240) para seguimiento de manchas y comunicación a un ESP32.
- [Brazo pick-and-place con ESP32-CAM y TinyML (artículo)](https://annals.fih.upt.ro/pdf-full/2025/ANNALS-2025-2-15.pdf).

### ESP32 junto a Pybricks
- [LMS-ESP32 con Pybricks y Pixy2](https://kai-morich.github.io/lms-esp32-pybricks-info/pixy2): ESP32 conectado a un puerto del hub con PUPRemote.

---

## 6. Recomendación y próximos pasos

1. **Empezar con la Opción A (cámara del celular).** Es lo más rápido y no requiere programar visión. Primero replicar la demo con tu pelota y tu hub 51515.
2. Confirmar que el Inventor acepta la segunda conexión Bluetooth (celular + compu) y que tu firmware es el de la beta.
3. Adaptar el código: puertos, ángulos, color, y **reemplazar el `multitask` inicial por movimientos de un motor a la vez**.
4. Calibrar una tabla (x, y, tamaño) → ángulos de hombro y muñeca para agarrar a distintas distancias, no solo a un radio fijo.
5. **Dejar el ESP32 como plan B**, para el caso de querer una cámara fija independiente del brazo o una conexión cableada (LMS-ESP32 + PUPRemote).

**Datos que faltan para adaptar el código:** qué hace cada uno de los 4 motores, en qué puerto está cada uno, y dónde irá montada la cámara (en el brazo o fija).


https://www.youtube.com/watch?v=5z3mEdhCSug

https://courses.ece.cornell.edu/ece5990/ECE5725_Fall2018_Projects/yf92_yw2226_M/index.html


