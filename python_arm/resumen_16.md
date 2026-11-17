# Resumen 16 de noviembre de 2026: brazo con camara (ha7.py)

**Objetivo:** que el brazo (hub LEGO Inventor 51515 con Pybricks, 4 motores) busque una pelota roja con la camara del celular, la agarre y la deje en un cubo cafe, usando la compu solo para dar comandos por teclado.

**Restriccion de potencia:** trabajamos sin bateria, solo con USB. Por eso se mueve **un motor a la vez** y el umbral de voltaje es 5500 mV (pausa con g/x).

---

## 1. Lo que se hizo hoy

1. **Revision de viabilidad.** Se leyo `spike_arm_camera.py` (proyecto oficial "Robotic arm with vision") y se concluyo que se puede replicar, cambiando hub, puertos, color y el arranque con `multitask`, que mueve 3 motores a la vez.
2. **Nombres corregidos en el codigo.** En `ha6.py` los puertos y multiplicadores estaban bien, pero los nombres no:

   | Puerto | Nombre correcto | Multiplicador | Rango (articulacion) |
   | ------ | --------------- | ------------- | -------------------- |
   | F | base | x3 | 0 a 360 |
   | D | codo (en ha6 decia "hombro") | x3 | -120 a 180 |
   | A | muneca | x1 | 0 a 190 |
   | B | garra | - | 0 cerrada, 90 abierta |

   C y E quedan libres. Velocidad 200 y umbral 5500 mV sin cambios.
3. **Se creo `ha7.py`** (archivo nuevo, `ha6.py` no se toco) = `ha6.py` + camara + calibracion manual:
   - **Menu:** `C` calibracion manual, `A` automatico, `X` salir.
   - **Calibracion manual:** motores sueltos, se mueve el brazo a mano y el programa imprime motores (`motor>articulacion`, ya divididos por el multiplicador), IMU del hub (cabeceo, balanceo, rumbo), lo que ve la camara para pelota y cubo (`x, y, width, height`), voltaje y corriente. Boton izquierdo del hub = guardar VISTA (camara), derecho = guardar POSE (motores), ambos = salir. Cada POSE imprime lineas listas para pegar en `TABLA_TOMAR` / `TABLA_SOLTAR`.
   - **Automatico:** barre la base buscando primero el cubo y luego la pelota, calcula codo y muneca interpolando las tablas (o los pide por teclado si hay menos de 2 filas), toma la pelota, la deja en el cubo y vuelve a 0.
4. **Primera prueba en el brazo real:** en general funciona (reportado por el usuario).

## 2. Observaciones de la prueba

- **Posicion inicial:** en el primer giro (barrido de la camara) el brazo barre con todo. Hace falta una posicion inicial distinta, con el brazo recogido para que no choque.
- **Cambio de montaje:** se agrego un soporte trasero detras del brazo. Ahora la camara gira junto con el brazo, sobre el eje horizontal. *(Inferencia mia, a confirmar:)* si la camara sube y baja con el codo, `y` y `height` cambian con el angulo del codo, no solo con la distancia a la pelota. Las VISTAS de la calibracion deben tomarse siempre con el codo en la misma posicion.
- **Demasiada salida en pantalla:** se imprimen demasiadas lineas y cuesta ver que es que.
- **Pregunta abierta:** se puede usar la laptop para los comandos por teclado y el celular solo para la camara (ver seccion 3).

## 3. Se pueden usar 2 Pybricks? Hay otra manera?

**Respuesta corta: no hace falta un segundo hub. Lo que preguntas es justamente la configuracion que ya usa `ha7.py`.**

Como funciona hoy:
- La **compu** tiene Pybricks Code conectado al hub. Ahi corre el programa y ahi se escriben los comandos (`input()`).
- El **celular** se conecta al **mismo hub** como segunda conexion y solo hace de sensor. No abre ningun programa; convierte la imagen en `x, y, width, height`.
- El hub sigue ejecutando el programa y decide que hacer.

Segun la guia oficial de smart sensors:
- Para la segunda conexion se aprieta el boton Bluetooth del hub hasta que vuelve a parpadear, se abre Pybricks en el celular, se conecta y se toca el icono del telefono.
- Hay una opcion USB (adaptador OTG, solo Android) que da mas velocidad y confiabilidad, y la compu sigue conectada por Bluetooth.
- La guia describe estos pasos para SPIKE Prime. El Inventor 51515 no aparece nombrado, pero la prueba de hoy indica que funciona igual.
- La funcion esta en beta (hay que usar Pybricks Beta y firmware actualizado).

**Opciones si algun dia hiciera falta otra cosa:**

| Opcion | Sirve? | Nota |
| ------ | ------ | ---- |
| **Un hub, compu + celular** (actual) | Si | Es lo que ya hace ha7.py. |
| **Celular por USB (OTG)**, compu por Bluetooth | Si, solo Android | Mas estable que Bluetooth para la camara. |
| **Segundo hub con la camara** y mandar datos al hub del brazo por BLE broadcast (`BLERadio`) | Posible, pero no recomendado | El broadcast no necesita conexion, pero la documentacion avisa que es lento mientras el hub esta conectado a una compu. Agrega un hub, su programa y mas cosas que fallen. Solo conviene si el hub del brazo no pudiera tener las 2 conexiones. |
| **Teclado desde la compu con `stdin`** (tutorial "Control your hub with your keyboard") | Si, pero cambia el estilo | Lee 1 caracter a la vez con `poll`; hay que hacer clic en la terminal de Pybricks Code. `input()` de ha7.py ya hace algo equivalente con Enter. |
| **pybricksdev por USB** en la compu | Si | Segun el mantenedor, con firmware beta se reconecta solo aunque el hub ya este conectado al celular por Bluetooth. Ojo: no conviene abrir en la misma compu la conexion del navegador y la de pybricksdev por Bluetooth a la vez (fallo reportado). |

**Recomendacion:** quedarse con 1 hub + compu (teclado) + celular (camara). Si la conexion de la camara se corta o va lenta, probar el celular por USB OTG antes de pensar en un segundo hub.

## 4. Pendientes para ha7.py (propuestas, nada hecho todavia)

1. **Nueva posicion inicial** distinta de "todo en 0", pensada para que el barrido no choque (brazo recogido, codo y muneca en una pose que despeje la camara).
2. **Menos texto en pantalla**, por ejemplo:
   - una linea corta por etapa, con el resto detras de un modo detallado (`DEBUG = True/False`);
   - en calibracion, una sola linea compacta que se actualice, y las lineas largas solo al guardar VISTA o POSE.
3. **Recalibrar la camara** con el nuevo montaje (soporte trasero): ventana `x` (70 a 80), `width` minimo (8), tonos de pelota (8) y cubo (25).
4. **Verificar el cambio de color en caliente:** el programa alterna el tono con `app.configure()` entre pelota y cubo. Si las filas PELOTA y CUBO salen iguales en calibracion, no funciona y hay que buscar otra via.
5. **Llenar `TABLA_TOMAR` y `TABLA_SOLTAR`** con varias POSES (6 a 10 posiciones) y decidir si la clave de distancia es `y` o `height` (`CLAVE_DISTANCIA`).

## 5. Fuentes

- [Use your phone as a smart sensor (guia oficial)](https://pybricks.com/learn/smart-sensors/getting-started/)
- [Robotic arm with vision (proyecto oficial)](https://pybricks.com/project/robot-arm-camera-tracker/)
- [Control your hub with your keyboard](https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/)
- [Hub to hub communication using data broadcasting](https://pybricks.com/projects/tutorials/wireless/hub-to-hub/broadcast)
- [Documentacion de `messaging` (AppData, BLERadio)](https://docs.pybricks.com/en/stable/messaging/index.html)
- [Discusion sobre pybricksdev + celular + 2 conexiones](https://github.gg22.workers.dev/orgs/pybricks/discussions/2730)
