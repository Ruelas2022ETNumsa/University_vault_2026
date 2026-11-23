# Propuesta de imágenes para `informe.md`

**Qué es esto.** Lista de los lugares del informe donde conviene una imagen o figura, con el subtítulo, el párrafo anterior (donde iría la imagen justo después), qué imagen y de qué fuente. **No modifica `informe.md`.**

**Cómo leer cada ficha**
- **Subtítulo y párrafo anterior:** para ubicar el punto exacto. La imagen va debajo de ese párrafo.
- **Origen:** *Propia* (foto, captura o diagrama hecho por ti), *Fuente* (figura de un trabajo citado) o *Redibujo* (diagrama propio adaptado de una fuente, que evita reproducir la figura original).
- **Prioridad:** Alta (aporta evidencia propia o resuelve algo que hoy solo está en texto), Media (aclara un concepto con apoyo de la literatura), Opcional.
- **Pie sugerido (APA 7):** *Figura N* en negrita, título en cursiva y debajo la nota. Para figuras de fuentes: *Nota.* Adaptado de «título» (p. X), por A. Autor, año, revista (DOI). Licencia o permiso. Para figuras propias: *Nota.* Elaboración propia.

**Avisos importantes**
- **Números de figura sin confirmar.** Los números que cito (Fig. 1A y 4 de Capaldi, Figs. 9 y 10 de Tzompantzi, Figs. 21 y 22 de Dang) salen de las respuestas de NotebookLM y Gemini; el resto de las figuras de fuente las marco `[ubicar figura en el PDF]`. No he visto los PDF: **confirma que cada figura existe y es legible antes de usarla**.
- **Derechos.** PeerJ y EPJ Web of Conferences suelen publicar con CC BY (permite reproducir con atribución), pero hay que confirmarlo en la primera página de cada PDF. Para FME Transactions, la tesis ESPE, la tesis UPS, ASEE (Markvicka), Pybricks y LEGO Ideas hay que **verificar la licencia** o usar un **redibujo propio** con «Adaptado de». Las páginas web (Pybricks, LEGO Ideas, GitHub) se citan con enlace; evitar copiar sus imágenes si no hay licencia clara.
- **Numeración.** Hoy el informe solo tiene la Figura 1 y la Figura 2 (en texto ASCII). Las fichas 15 y 16 las reemplazan por diagramas reales. Al insertar las demás habrá que **renumerar todas las figuras** y citarlas en el texto («Figura 3», etc.), y agregar una lista de figuras si el docente la pide (tarea E-4 de la bitácora).

## Resumen

| N.º | Sección | Imagen propuesta | Origen | Prioridad |
| --- | ------- | ---------------- | ------ | --------- |
| 1 | 1.1 Plataformas LEGO con cámara | Brazo SPIKE Prime con celular y proyecto VISION | Fuente (Pybricks, LEGO Ideas) | Media |
| 2 | 1.1 Brecha | Cadena completa y qué cubre cada antecedente | Propia (diagrama) | Alta |
| 3 | 3.2 Tarea de referencia | Foto de la escena: pelota roja, base café y cubo | Propia | Alta |
| 4 | 4.1.1 | Brazo real con las 4 articulaciones rotuladas | Propia | Alta |
| 5 | 4.1.2 | Hub 51515 y flujo de difusión (broadcast y observe) | Propia, apoyada en Pybricks | Media |
| 6 | 4.1.3 | Esquema geométrico de la cinemática inversa | Redibujo de Mohammed et al. (2023) | Media |
| 7 | 4.1.4 | Curvas de ajuste de PID (Kp, Ki, Kd) | Fuente (Capaldi, 2024, Fig. 14) | Media |
| 8 | 4.1.4 | Corriente y caída de voltaje con movimiento secuencial | Fuente (Ntambara et al., 2026) | Opcional |
| 9 | 4.1.5 | Secuencia HSV, máscara, contorno y centroide | Propia, validada con Anusha y Mohammed | Alta |
| 10 | 4.1.6 | Plano de trabajo con marcador ArUco | Fuente (Rangarajan y Bianchini, 2026) | Media |
| 11 | 4.1.6 | Tabla de calibración píxeles a ángulos | Fuente (Mada Sanjaya et al., 2018) | Opcional |
| 12 | 4.1.7 | Arquitectura de la red neuronal y detección YOLO | Fuente (Mada Sanjaya; Capaldi o Dang) | Media |
| 13 | 4.1.8 | Tiempo de ida y vuelta de 11 segmentos y pérdida de paquetes | Fuente (Capaldi, 2024, Fig. 4 y Tabla 3) | Alta |
| 14 | 4.1.8 | RSSI de BLE frente a la distancia | Fuente (Tzompantzi et al., 2019, Figs. 9 y 10) | Media |
| 15 | 4.1.9 | Arquitecturas de Capaldi y Dang lado a lado | Fuente (Capaldi Fig. 1A; Dang, sección 2 o 3.2) | Alta |
| 16 | 4.2 | Figura 1 real y captura de la página web | Propia | Alta |
| 17 | 4.3 | Figura 2 real de la arquitectura propuesta | Propia | Alta |
| 18 | 4.3 | Diagrama de la secuencia de la tarea | Propia | Media |
| 19 | 4.4 | Captura de la prueba preliminar de detección | Propia | Alta |

---

## 1. Sección 1.1: Plataformas LEGO con cámara

**Subtítulo:** 1.1 Antecedentes → *Plataformas LEGO con cámara*

**Párrafo anterior:**
> **Plataformas LEGO con cámara.** Existen proyectos de brazos con el hub LEGO Inventor 51515 que siguen una pelota roja con una cámara web (LEGO Ideas, s. f.), y un proyecto de Pybricks con un brazo LEGO SPIKE Prime que usa el celular como cámara (función *smart sensors*), busca un objeto rojo, gira la base hasta centrarlo y lo toma (Pybricks, s. f.-a). No se encontró un proyecto equivalente con el hub 51515 y cámara de celular. Otros trabajos con LEGO delegan la visión a una computadora externa, porque la cámara del propio robot no tiene la potencia necesaria (Autor [pendiente], s. f.). También hay proyectos abiertos que combinan partes de la arquitectura de este trabajo: un tren LEGO con hub Pybricks controlado por BLE desde un ESP32-S3 que sirve una página web y transmite video de una cámara, sin procesar la imagen (Johnson, 2026); un robot con hub 51515 que detecta y toma un objeto con visión TensorFlow y BLE, sin ESP32 confirmado (osullivp, 2021); un proyecto de la WRO 2026 con hub Inventor y Pybricks, un ESP32 y una cámara OpenMV que detecta bloques de color, sin que se documente la función del ESP32 (GC-TO, 2026); y un ESP32 como intermediario entre un módulo de visión (HuskyLens) y un hub SPIKE Prime (Anton's Mindstorms, 2025). Son repositorios y tutoriales, no literatura arbitrada, y se citan como antecedentes de implementación [verificar en cada README]. Pybricks, un firmware alternativo en MicroPython para los hubs LEGO, ofrece además una función en versión beta llamada *smart sensors*, que permite usar la cámara de un teléfono como sensor conectado al hub (Pybricks, s. f.-b).

**Imagen propuesta:** una figura de dos paneles: (a) el brazo SPIKE Prime con el celular como cámara y (b) el proyecto VISION con webcam y hub 51515.
**Fuente:** (a) página del proyecto *Robotic arm with vision* de Pybricks (https://pybricks.com/project/robot-arm-camera-tracker/); (b) propuesta *VISION* de LEGO Ideas (enlace de la referencia). Alternativa: foto o captura del README de Johnson (2026) para mostrar el ESP32 como puente.
**Origen y derechos:** Fuente web. Verificar licencia; si no hay clara, **no reproducir** y dejar solo la cita con enlace.
**Prioridad:** Media.
**Pie sugerido:** *Figura N.* Antecedentes LEGO con cámara. *Nota.* (a) Adaptado de *Robotic arm with vision*, por Pybricks, s. f. (https://pybricks.com/project/robot-arm-camera-tracker/). (b) Adaptado de *VISION*, por LEGO Ideas, s. f.

---

## 2. Sección 1.1: Brecha que atiende este trabajo

**Subtítulo:** 1.1 Antecedentes → *Brecha que atiende este trabajo* (antes de «La Tabla 1 resume…»)

**Párrafo anterior:**
> **Brecha que atiende este trabajo.** Los trabajos con ESP32 controlan el brazo desde el celular o el navegador, casi siempre sin cámara; los de visión e IA procesan la imagen en una PC o en una Raspberry Pi y envían los ángulos a un microcontrolador; y los de LEGO con cámara la conectan al propio hub o a una computadora. Dang et al. (2026) y Capaldi (2024) ya combinan una PC con visión de aprendizaje profundo y un ESP32 en plataformas educativas; Pybricks y LEGO Ideas muestran que se puede dar visión a un hub LEGO; y hay proyectos abiertos con el ESP32 como puente Wi-Fi a BLE hacia un hub Pybricks. Por eso la novedad que se plantea no es la cámara, ni la PC con visión, ni el puente por separado. En la literatura académica revisada no aparece una combinación de brazo de 4 GDL con hub LEGO Inventor 51515 y Pybricks, control remoto desde una página web servida por un ESP32 y un módulo de visión o IA externo que le envíe las órdenes; los proyectos abiertos encontrados tienen solo partes de esa cadena (Tabla 1), y no se halló una tesis ni un artículo arbitrado que la documente completa. Este informe investiga cómo se puede lograr esa integración con equipo de bajo costo.

**Imagen propuesta:** diagrama de la cadena completa en eslabones (cámara → PC con visión e IA → Wi-Fi → ESP32 con página web → BLE de difusión → hub LEGO 51515 → motores) y, debajo, una fila por antecedente cercano (Dang, Capaldi, Pybricks con SPIKE Prime, Johnson, osullivp, GC-TO, Anton's Mindstorms, este trabajo) con los eslabones que cubre cada uno marcados. Es una versión visual de la Tabla 1 y hace evidente la brecha.
**Fuente:** propia, con los datos de la Tabla 1.
**Prioridad:** Alta (es la figura que más ayuda a defender la novedad).
**Pie sugerido:** *Figura N.* Eslabones de la cadena visión → ESP32 → hub LEGO que cubre cada antecedente. *Nota.* Elaboración propia a partir de las fuentes de la Tabla 1.

---

## 3. Sección 3.2: Tarea de referencia

**Subtítulo:** 3.2 Escenario del proyecto → *Tarea de referencia*

**Párrafo anterior:**
> **Tarea de referencia.** La tarea de ejemplo del informe es de recoger y colocar: el brazo toma una pelota roja apoyada sobre una base de color café y la deposita en un cubo que marca el destino [verificar la descripción del cubo y de la base]. Con la cámara del celular y Pybricks ya se probó, de forma preliminar, que la pelota roja se detecta sobre esa base, sin calibración. Es el mismo enfoque del proyecto de Pybricks (s. f.-a), que busca un objeto rojo con el celular como *smart sensor*. La literatura advierte que el rojo y los tonos café pueden confundirse en la segmentación por color (Lim et al., 2021; Rangarajan y Bianchini, 2026).

**Imagen propuesta:** foto cenital o en perspectiva de la escena real: brazo, pelota roja sobre la base café y el cubo de destino, con un rótulo en cada elemento. Ayuda a cerrar el `[verificar la descripción del cubo y de la base]`.
**Fuente:** propia.
**Prioridad:** Alta.
**Pie sugerido:** *Figura N.* Escena de la tarea de referencia. *Nota.* Elaboración propia.

---

## 4. Sección 4.1.1: Conceptos básicos de manipuladores

**Subtítulo:** 4.1.1 Conceptos básicos de manipuladores

**Párrafo anterior:**
> En este trabajo el brazo tiene cuatro articulaciones motorizadas: base, codo y muñeca mueven el brazo, y la garra funciona como efector final.

**Imagen propuesta:** foto del brazo LEGO real con las cuatro articulaciones rotuladas (F base, D codo, A muñeca, B garra, como en la página del prototipo), el efector final señalado y los ejes de giro. Opcional: un esquema con los tipos de articulación (revoluta y prismática) y el efector final como el de la tesis de Llerena y Salazar (2022) `[ubicar figura en el PDF; verificar licencia]`.
**Fuente:** propia (principal); Llerena y Salazar (2022) como apoyo conceptual si se quiere.
**Prioridad:** Alta (conecta la teoría con el brazo real).
**Pie sugerido:** *Figura N.* Articulaciones del brazo del prototipo. *Nota.* Elaboración propia.

---

## 5. Sección 4.1.2: Plataforma LEGO Inventor 51515 y firmware Pybricks

**Subtítulo:** 4.1.2 Plataforma LEGO Inventor 51515 y firmware Pybricks

**Párrafo anterior:**
> Pybricks también permite que un hub reciba mensajes de otro dispositivo por Bluetooth sin establecer una conexión: el emisor difunde (*broadcast*) un mensaje con un canal, y el hub lo lee con `observe` (Pybricks, s. f.-d). Según una medición con sniffer hecha con un City Hub y el firmware 4.1.0b2 (no con el hub Inventor 51515), este modo permite del orden de 10 actualizaciones por segundo y observa peor cuando el hub está conectado a una computadora (Pybricks, s. f.-e). Esta es la vía que usa el prototipo para recibir las órdenes del ESP32. La función *smart sensors*, en versión beta, permite además usar la cámara de un celular como sensor del hub (Pybricks, s. f.-b).

**Imagen propuesta:** esquema del modo difusión: el ESP32 emite en el canal 1 la tupla `(articulación, ángulo, id_orden)`, el hub la recibe con `observe` y mueve un motor. Opcional: foto del hub 51515 con los motores en sus puertos.
**Fuente:** propia, apoyada en la documentación de Pybricks (s. f.-d). Si se usa una imagen del hub de la documentación de Pybricks, verificar su licencia.
**Prioridad:** Media.
**Pie sugerido:** *Figura N.* Envío de órdenes por difusión BLE de Pybricks. *Nota.* Elaboración propia a partir de Pybricks (s. f.-d).

---

## 6. Sección 4.1.3: Cinemática del brazo

**Subtítulo:** 4.1.3 Cinemática del brazo

**Párrafo anterior** (texto y fórmulas):
> El método más reportado para brazos de 3 a 5 GDL es el **geométrico** (Mohammed et al., 2023; Monroy Moya et al., 2024; Intisar et al., 2021). Para un objetivo en $(P_x, P_y)$ del plano de la mesa, el ángulo de la base se obtiene con:
>
> $$\theta_1 = \arctan\left(\frac{P_y}{P_x}\right)$$
>
> y el ángulo del codo, aplicando la ley de cosenos sobre el triángulo que forman los eslabones $a_2$ y $a_3$ y la distancia $N$ entre hombro y muñeca:
>
> $$\theta_3 = \pm \cos^{-1}\left(\frac{N^2 - a_2^2 - a_3^2}{2\,a_2 a_3}\right)$$
>
> (Mohammed et al., 2023). El doble signo corresponde a las dos configuraciones posibles, "codo arriba" y "codo abajo". Para trayectorias continuas se usa además el método diferencial con la matriz Jacobiana, que relaciona las velocidades articulares con las del efector final (Llerena y Salazar, 2022).

**Imagen propuesta:** dos vistas del esquema geométrico: planta, con el ángulo de la base θ₁ al punto (Pₓ, P_y), y perfil, con el triángulo de lados a₂, a₃ y N, y las configuraciones «codo arriba» y «codo abajo».
**Fuente:** Mohammed et al. (2023), figuras del modelo geométrico (ecuaciones 3 a 11) `[ubicar figura en el PDF]`. **Recomendado: redibujo propio** «Adaptado de Mohammed et al. (2023)» con tus medidas del brazo; evita problemas de derechos.
**Prioridad:** Media. Resuelve de paso la duda de aplicar la fórmula a un brazo sin hombro (tarea E-9 de la bitácora): en tu redibujo puedes mostrar cuáles eslabones y ángulos corresponden a tu brazo.
**Pie sugerido:** *Figura N.* Esquema geométrico de la cinemática inversa. *Nota.* Adaptado de «Smart robot vision for a pick and place robotic system under different illumination conditions», por M. M. Mohammed et al., 2023, *Engineering and Technology Journal, 41*(6) (https://doi.org/10.30684/etj.2023.135966.1292).

---

## 7. Sección 4.1.4: Control de posición de motores (PID)

**Subtítulo:** 4.1.4 Control de posición de motores

**Párrafo anterior:**
> En los servomotores económicos, el ángulo se fija con el ancho de un pulso PWM (Tzompantzi Netzahual et al., 2019; Llerena y Salazar, 2022). En un esquema de lazo cerrado, el controlador resta la posición medida de la deseada y corrige según ese error (Eiammanussakul y Sangveraphunsiri, 2018). Un controlador **PD** combina una corrección proporcional al error con otra proporcional a su velocidad de cambio (Yilmaz et al., 2025); el **PID** agrega un término integral que elimina el error que persiste [cita pendiente]. Capaldi (2024) usa el ajuste de las ganancias Kp, Ki y Kd de un brazo con peso, con una interfaz que grafica la respuesta, como actividad educativa para observar el tiempo de levantamiento, el sobreimpulso y el error en estado estacionario. En sistemas articulados más complejos se anidan varios lazos de posición, torque y velocidad (Eiammanussakul y Sangveraphunsiri, 2018). Cuando el encoder está en el eje del motor y hay una reductora, el ángulo de la articulación es la lectura del encoder dividida entre la relación de transmisión (Eiammanussakul y Sangveraphunsiri, 2018).

**Imagen propuesta:** gráfica de la respuesta del brazo con tres curvas superpuestas: solo proporcional (Kp = 0,3), proporcional-integral (Kp = 0,3; Ki = 0,003) y PID completo (Kp = 0,3; Ki = 0,003; Kd = 2), con el ángulo objetivo de 45°.
**Fuente:** Capaldi (2024), Fig. 14, sección *Real time data logging → Tuning a PID controller* (págs. 21 y 22 según NotebookLM). PeerJ publica con CC BY; **confirmar la licencia en el PDF**.
**Prioridad:** Media (ilustra el único apoyo con cifras del PID en las fuentes).
**Pie sugerido:** *Figura N.* Respuesta del brazo con distintas ganancias de un controlador PID. *Nota.* Adaptado de «A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol» (Fig. 14), por E. I. Capaldi, 2024, *PeerJ Computer Science, 10*, e1826 (https://doi.org/10.7717/peerj-cs.1826). CC BY 4.0 `[verificar]`.

---

## 8. Sección 4.1.4: Límites de alimentación

**Subtítulo:** 4.1.4 Control de posición de motores → *Límites de alimentación*

**Párrafo anterior:**
> **Límites de alimentación.** Varias fuentes tratan la corriente disponible como una restricción de diseño. Ntambara et al. (2026) alimentaron un brazo con motores a pasos desde una fuente de 12 V y 2 A, limitaron la corriente de los controladores y activaron las articulaciones de forma secuencial, con un pico de 1,92 A y una caída de voltaje de 0,46 V. Yilmaz et al. (2025) aislaron la alimentación de los servos con relés y optoacopladores, midieron la corriente con un sensor ACS712, agregaron un fusible de 4,2 A y limitaron la velocidad por firmware. Lim et al. (2021) reportan caídas bruscas de voltaje y vibración al accionar varios servos con las librerías estándar. El prototipo de este trabajo aplica una idea parecida a la de Ntambara et al. (2026): un motor por orden y vigilancia del voltaje. Ninguna de las fuentes revisadas mide cuánto alarga el tiempo de ciclo el movimiento secuencial frente al simultáneo; Ntambara et al. (2026) no hicieron esa comparación.

**Imagen propuesta:** gráfica o diagrama de la corriente de pico de 1,92 A y de la caída de 0,46 V con activación secuencial, o el diagrama de alimentación (fuente de 12 V y 2 A, driver A4988, motores). Alternativa propia: una captura de tu registro del voltaje del hub (pausa bajo 5500 mV), que sí corresponde a tu prototipo.
**Fuente:** Ntambara et al. (2026), secciones 3.5 y 3.8 `[ubicar figura en el PDF]`; alternativa propia.
**Prioridad:** Opcional. Mejor si es propia: muestra tu restricción real de alimentación.
**Pie sugerido:** *Figura N.* Consumo de corriente con activación secuencial de los motores. *Nota.* Adaptado de «Design and prototyping of a smart powered lifting robotic arm (SPLRA)», por Ntambara et al., 2026 [verificar revista y DOI].

---

## 9. Sección 4.1.5: Detección de objetos por color

**Subtítulo:** 4.1.5 Detección de objetos por color

**Párrafo anterior** (el del flujo en cuatro pasos):
> El flujo que describen las fuentes tiene cuatro pasos. Primero, la imagen se convierte de RGB a **HSV**, porque en RGB la luz afecta a los tres canales a la vez, mientras que HSV separa el tono (H), la pureza del color (S) y el brillo (V), lo que hace la selección de color menos sensible a las variaciones moderadas de luz (Anusha et al., 2018; Mohammed et al., 2023; Intisar et al., 2021). Segundo, la **umbralización** define un rango inferior y superior de H, S y V para cada color: los píxeles dentro del rango pasan a 1 y el resto a 0, y los umbrales pueden fijarse a mano con controles deslizantes o calcularse a partir de la luz medida (Llerena y Salazar, 2022; Mohammed et al., 2023). Tercero, la **segmentación** limpia la máscara con erosión, dilatación y filtros de suavizado, y descarta regiones menores que un tamaño mínimo (Mada Sanjaya et al., 2018; Mohammed et al., 2023; Anusha et al., 2018). Cuarto, se extraen los **contornos** y se calcula el **centroide** de cada región, con momentos de imagen o promediando los píxeles (Anusha et al., 2018; Mohammed et al., 2023; Medel et al., s. f.).

**Imagen propuesta:** secuencia de cuatro paneles con tu propia escena (la pelota roja sobre la base café): imagen original → imagen en HSV → máscara binaria tras umbral y limpieza → contorno y centroide marcados. Si no tienes aún estas capturas, ver la tarea C-6 de la bitácora (prueba mínima con foto o video).
**Fuente:** propia. Como respaldo, el mismo flujo con ejemplos en Anusha et al. (2018), Mohammed et al. (2023) o Intisar et al. (2021) `[ubicar figura en el PDF]`.
**Prioridad:** Alta (es evidencia propia y refuerza el 4.4).
**Pie sugerido:** *Figura N.* Pasos de la detección de la pelota por color. *Nota.* Elaboración propia con OpenCV; flujo según Anusha et al. (2018) y Mohammed et al. (2023).

---

## 10. Sección 4.1.6: Calibración entre la cámara y el brazo (plano de trabajo)

**Subtítulo:** 4.1.6 Calibración entre la cámara y el brazo

**Párrafo anterior** (el primero del apartado):
> Un píxel de la imagen no basta para ubicar el objeto en el espacio: define un rayo desde la cámara. Cuando los objetos reposan en una mesa plana, se intersecta ese rayo con el plano de trabajo, que se define con un marcador de referencia (ArUco), y se transforma el resultado al sistema de coordenadas del robot (Rangarajan y Bianchini, 2026). Una forma más sencilla es la **homografía**, una matriz de 3×3 que relaciona directamente los puntos de la imagen con los del plano real y se calcula a partir de pares de puntos conocidos (Anusha et al., 2018; Aucapiña e Iza, 2019). Con una cámara cenital fija se puede usar incluso un factor de escala entre una medida real conocida y su tamaño en píxeles (Aucapiña e Iza, 2019; Intisar et al., 2021).

**Imagen propuesta:** montaje con cámara cenital, mesa plana y marcadores ArUco, con el plano de trabajo y el sistema de coordenadas del robot indicados.
**Fuente:** Rangarajan y Bianchini (2026) `[ubicar figura del montaje y los marcadores en el PDF; verificar licencia]`. Alternativa: figura del montaje con cámara cenital y factor de escala de Aucapiña e Iza (2019). **Recomendado:** redibujo propio de cómo quedaría tu montaje con la cámara USB sobre la mesa.
**Prioridad:** Media.
**Pie sugerido:** *Figura N.* Montaje de calibración con cámara cenital y marcadores ArUco. *Nota.* Adaptado de «Vision-guided reorientation and color sorting of writing utensils using a low-cost 4-DoF arm», por A. Rangarajan y B. Bianchini, 2026, *American Journal of Student Research* (https://doi.org/10.70251/HYJR2348.467488).

---

## 11. Sección 4.1.6: Tabla de calibración píxeles a ángulos

**Subtítulo:** 4.1.6 Calibración entre la cámara y el brazo (tabla de calibración)

**Párrafo anterior** (el segundo del apartado):
> Cuando la cámara va montada sobre el brazo o se mueve respecto a él, se recurre a la **calibración ojo-mano**, que resuelve ecuaciones del tipo $AX = ZB$ entre las transformaciones que observa la cámara y la pose del efector final (Enebuse et al., 2021; Tabb y Ahmad Yousef, 2017). Otra opción es construir empíricamente una **tabla de calibración** que asocia coordenadas de la imagen con los ángulos medidos de los servos al alcanzar cada punto, y entrenar con ella una red neuronal (Mada Sanjaya et al., 2018). Un método de tablas con interpolación lineal, sin red neuronal ni modelo geométrico, es una de las opciones que se propone para este proyecto (sección 4.3); no se encontró tal cual en las fuentes revisadas, y el antecedente más cercano es la tabla de Mada Sanjaya et al. (2018). Una búsqueda adicional en la web tampoco halló un trabajo que use una tabla con interpolación lineal de píxeles a ángulos; los más cercanos mapean la imagen a un plano de trabajo calibrado y luego resuelven la cinemática inversa [cita pendiente: no se identificó una fuente verificable].

**Imagen propuesta:** cuadrícula de puntos de calibración sobre la imagen (resolución de 467 × 624 px según NotebookLM) con la tabla de coordenadas y los ángulos de los cinco servos medidos en cada punto.
**Fuente:** Mada Sanjaya et al. (2018) `[ubicar figura o tabla en el PDF; verificar licencia]`. Alternativa: dibujar tu propia cuadrícula, que sería la base de la opción de interpolación lineal que propones.
**Prioridad:** Opcional.
**Pie sugerido:** *Figura N.* Tabla de calibración entre coordenadas de la imagen y ángulos de los servos. *Nota.* Adaptado de «Colored object sorting using 5 DoF robot arm based artificial neural network (ANN) method», por W. S. Mada Sanjaya et al., 2018, *Journal of Physics: Conference Series, 1090*, 012070 (https://doi.org/10.1088/1742-6596/1090/1/012070).

---

## 12. Sección 4.1.7: Inteligencia artificial en el control de brazos

**Subtítulo:** 4.1.7 Inteligencia artificial en el control de brazos

**Párrafo anterior:**
> Las fuentes muestran tres niveles de uso de la IA. **Visión clásica** (HSV, umbral y centroide), sin entrenamiento, que es la base de la mayoría de los trabajos (sección 4.1.5). **Redes neuronales para la cinemática inversa**: Mada Sanjaya et al. (2018) entrenaron una red con una capa oculta de 20 neuronas que recibe las coordenadas $(x, y)$ de la imagen y entrega los ángulos de cinco servos, con un error de 1,3 % entre los datos de calibración y la salida de la red. **Aprendizaje profundo para detectar y clasificar**: Aucapiña e Iza (2019) clasificaron piezas con un modelo MobileNet de TensorFlow (97,28 % en identificación y 38 a 50 ms de inferencia), y Rangarajan y Bianchini (2026) usaron YOLO11n-OBB para detectar la posición y el ángulo de un bolígrafo, con 89,8 % de éxito en la tarea completa. Dang et al. (2026) ejecutan YOLOv12 en una laptop solo con CPU, sin GPU, aunque no reportan el tiempo de inferencia; Capaldi (2024) midió la inferencia de YOLOv8 en tres equipos: 62,8 ms en una CPU AMD Ryzen 9 5950X, 52,1 ms en un Apple M2 y 8,41 ms en una GPU NVIDIA Quadro P2200 [verificar el tamaño del modelo YOLOv8 usado].

**Imagen propuesta:** figura de dos paneles: (a) la arquitectura de la red de Mada Sanjaya et al. (2): dos entradas (x, y), una capa oculta de 20 neuronas y cinco salidas (ángulos de los servos); (b) un ejemplo de detección con aprendizaje profundo sobre objetos reales.
**Fuente:** (a) Mada Sanjaya et al. (2018) `[ubicar la figura de la red en el PDF]`; (b) Capaldi (2024), imágenes de la aplicación de clasificación (Fig. 5 y sección de entrenamiento) o Dang et al. (2026), Figs. 21 y 22 (curvas de entrenamiento y matriz de confusión de YOLOv12) `[verificar licencia de FME Transactions]`. Capaldi (PeerJ, CC BY) es la opción más fácil en derechos.
**Prioridad:** Media.
**Pie sugerido:** *Figura N.* Ejemplos de IA en el control de brazos: (a) red neuronal para la cinemática inversa; (b) detección con YOLOv8. *Nota.* (a) Adaptado de Mada Sanjaya et al., 2018, *Journal of Physics: Conference Series, 1090*, 012070. (b) Adaptado de Capaldi, 2024, *PeerJ Computer Science, 10*, e1826.

---

## 13. Sección 4.1.8: Comunicación inalámbrica con ESP32 (latencia y alcance)

**Subtítulo:** 4.1.8 Comunicación inalámbrica con ESP32

**Párrafo anterior** (el primero del apartado):
> El ESP32 es un sistema en chip de doble núcleo (160 a 240 MHz) que integra Wi-Fi 802.11 b/g/n y Bluetooth con BLE (Tzompantzi Netzahual et al., 2019). Puede crear su propia red Wi-Fi (modo punto de acceso), repartir direcciones en el rango 192.168.4.x y servir una interfaz web en el puerto 80 a la que el celular accede con un navegador, enviando peticiones HTTP que el ESP32 traduce en órdenes para el brazo (Tzompantzi Netzahual et al., 2019; Suhaeb y Risal, 2024). Suhaeb y Risal (2024) midieron entre 85 y 92 ms de respuesta para los botones de control y una reconexión automática en menos de 5 s. Tzompantzi Netzahual et al. (2019) midieron con Wireshark, desde un navegador, tiempos de respuesta HTTP de unos 50 a 60 ms a distancias de 1 a 40 m (sin indicar el número de repeticiones), y reportaron que si se envían instrucciones de forma simultánea la conexión se pierde unos 3 s y la aplicación muestra un aviso. Kumar et al. (2026), con un vehículo controlado por Wi-Fi, reportan una latencia de ida y vuelta de 38, 62 y unos 120 ms con señal fuerte, moderada y débil; es evidencia complementaria (revista de menor nivel y no es un brazo). Shah y Arockia Doss (2026) reportan menos de 150 ms entre la orden en la interfaz web y la actuación de los servos, con WebSockets sobre Wi-Fi, sin precisar cómo se midió. Capaldi (2024), con ESP-NOW (no Wi-Fi ni BLE) entre una PC y un hub VEX V5, midió 187 ms de ida y vuelta (desviación estándar de 57 ms), que incluye el tránsito por USB, los dos ESP32, la conversión a RS-485 y el procesamiento del hub, y una pérdida de paquetes menor a 1 % de 0 a 40 m y de 13,2 % a 60 m; recomienda 40 m o menos para control en lazo cerrado. Estas cifras usan métodos distintos y no son comparables entre sí.

**Imagen propuesta:** (a) diagrama del tiempo de ida y vuelta de Capaldi dividido en 11 segmentos; (b) gráfica de la pérdida de paquetes frente a la distancia (0 a 60 m). Alternativa propia: una gráfica de barras que compare las latencias reportadas por Tzompantzi (50 a 60 ms), Suhaeb (85 a 92 ms), Kumar (38 a 120 ms), Shah (menos de 150 ms) y Capaldi (187 ms), con la advertencia de que no son comparables.
**Fuente:** Capaldi (2024), Fig. 4 y Tabla 2 (segmentos), y Tabla 3 (pérdida de paquetes; págs. 14, 15 y 22 según NotebookLM). Los segmentos 2 a 4 de la Tabla 2 no estaban en los fragmentos cargados; **leer la figura completa antes de reproducirla**. Confirmar CC BY.
**Prioridad:** Alta (son las cifras de enlace más completas de todas las fuentes).
**Pie sugerido:** *Figura N.* Tiempo de ida y vuelta y pérdida de paquetes de un enlace ESP-NOW entre una PC y un hub VEX V5. *Nota.* Adaptado de Capaldi, 2024, *PeerJ Computer Science, 10*, e1826 (Fig. 4 y Tabla 3). CC BY 4.0 `[verificar]`.

---

## 14. Sección 4.1.8: Comunicación inalámbrica con ESP32 (BLE)

**Subtítulo:** 4.1.8 Comunicación inalámbrica con ESP32 → *BLE*

**Párrafo anterior** (el segundo del apartado):
> El **BLE** fue diseñado para consumir menos energía que el Bluetooth clásico (Tzompantzi Netzahual et al., 2019). En su uso habitual, un dispositivo anuncia un servicio y otro se conecta a él; el modo de **difusión** (*broadcast*) no requiere conexión y es el que usa Pybricks para enviar mensajes al hub (Pybricks, s. f.-d). Tzompantzi Netzahual et al. (2019) evaluaron BLE solo con la intensidad de señal (RSSI) de las balizas del ESP32: promedio de -47,8 dBm a 1 m y de -88,7 dBm a unos 40 m. Afirman que ambas tecnologías responden en tiempo real a menos de 40 m, pero sin cifras de latencia para BLE; los tiempos de 50 a 60 ms corresponden solo a Wi-Fi. Ninguna de las fuentes revisadas mide la latencia de BLE, ni en modo de difusión ni con conexión, por lo que el retraso del enlace del prototipo debe medirse (sección 4.3). Fuera de las fuentes cargadas, la latencia de BLE sin conexión depende del intervalo de anuncio, del ciclo de escaneo del receptor y de un retardo aleatorio de 0 a 10 ms entre anuncios (Cho et al., 2014 [verificar]; [cita pendiente: documentación de Espressif]). La única cifra con ESP32 que se encontró (44 y 85 ms) corresponde a un ESP32 que recibe anuncios y los publica por un protocolo de mensajería (MQTT): es una latencia de sistema y en sentido contrario al de este prototipo, por lo que no se toma como referencia (Vieira y Rizzetti, 2025 [verificar]).

**Imagen propuesta:** gráfica de la intensidad de señal (RSSI) de las balizas BLE del ESP32 frente a la distancia, de 1 m (-47,8 dBm) a unos 40 m (-88,7 dBm).
**Fuente:** Tzompantzi Netzahual et al. (2019), sección 6, Figuras 9 y 10 (confirmadas por S1). Verificar la licencia de IJSR; si no es clara, **redibujar** la gráfica con los dos valores citados y los demás puntos del PDF.
**Prioridad:** Media. Respalda con un dato visual la frase «BLE solo se midió con RSSI».
**Pie sugerido:** *Figura N.* Intensidad de señal (RSSI) de BLE con el ESP32 según la distancia. *Nota.* Adaptado de «Real time control of robotic arm using Bluetooth Low Energy & Wi-Fi with the module board ESP32 and Android application» (Figs. 9 y 10), por J. E. Tzompantzi Netzahual et al., 2019, *International Journal of Science and Research, 8*(8).

---

## 15. Sección 4.1.9: Separación entre la visión y el control de los motores

**Subtítulo:** 4.1.9 Separación entre la visión y el control de los motores

**Párrafo anterior:**
> En los trabajos revisados que usan una cámara, la imagen casi siempre se procesa en un equipo y los motores los mueve un microcontrolador distinto, al que se envían los ángulos (Tabla 4). Monroy Moya et al. (2024) son la excepción: concentran visión y control en una sola Raspberry Pi 4 para evitar latencias. En el resto el enlace es por cable (USB o serie), con tres excepciones inalámbricas: Aucapiña e Iza (2019) mencionan además Bluetooth para el uArm, Dang et al. (2026) ofrecen MQTT sobre Wi-Fi en su interfaz web (la ruta de visión sería por USB [verificar]) y Capaldi (2024) usa ESP-NOW entre la PC y el robot. Este proyecto mantendría la separación con un enlace inalámbrico, como Capaldi (2024), pero por Wi-Fi hasta el ESP32 y BLE de difusión hasta el hub: el módulo de visión enviaría las órdenes al ESP32 por Wi-Fi, que es la vía ya funcional del prototipo.

**Imagen propuesta:** dos diagramas lado a lado de las arquitecturas más cercanas: (a) Capaldi (2024): PC con YOLOv8, ESP32 local, ESP-NOW, ESP32 del robot, RS-485, VEX V5; (b) Dang et al. (2026): laptop con YOLOv12, ESP32, PCA9685, servos MG996R y la interfaz web por MQTT. Debajo, tu arquitectura propuesta (la ficha 17) para compararla.
**Fuente:** (a) Capaldi (2024), Fig. 1A (*Connectivity*). (b) Dang et al. (2026), diagrama de arquitectura de la sección 2 o del hardware en la sección 3.2 `[ubicar figura en el PDF; verificar licencia]`. **Alternativa recomendada:** redibujo propio de ambos con el mismo estilo que tu Figura 2, para que se vea la comparación.
**Prioridad:** Alta.
**Pie sugerido:** *Figura N.* Arquitecturas con visión en una PC y ESP32 como enlace o controlador en dos plataformas educativas. *Nota.* Adaptado de Capaldi, 2024, *PeerJ Computer Science, 10*, e1826 (Fig. 1A), y de Dang et al., 2026, *FME Transactions, 54*, 93-106 (https://doi.org/10.5937/fme2601093P).

---

## 16. Sección 4.2: Prototipo base (Figura 1 real y captura de la página)

**Subtítulo:** 4.2 Prototipo base: control remoto con ESP32 (dos ubicaciones)

**(a) Reemplaza la Figura 1 actual en ASCII.** Párrafo anterior:
> El prototipo se compone de cuatro etapas (Figura 1): el celular se conecta por Wi-Fi a la red propia del ESP32; el ESP32 sirve una página con botones de articulación (ninguna, F base, D codo, A muñeca, B garra), un control deslizante de ángulo y un botón de accionar; el ESP32 emite cada orden por Bluetooth como la tupla `(articulación, ángulo, id_orden)` en el canal 1; y el hub, en modo remoto, mueve una sola articulación por cada orden nueva.

**(b) Captura y foto** (debajo del segundo párrafo). Párrafo anterior:
> Para cuidar la alimentación USB limitada, el hub conserva las restricciones del programa original: un solo motor energizado a la vez, motor suelto al llegar, vigilancia del voltaje con pausa si baja de 5500 mV y límites de ángulo por articulación aplicados en el hub y no en la página. Las órdenes que llegan mientras el brazo se mueve se descartan, y sin señal del ESP32 no se mueve nada. El ESP32 recuerda el último ángulo ordenado de cada articulación y lo muestra en la página. El prototipo se probó con el brazo real: la interfaz y el botón de accionar funcionan desde el celular y el brazo se mueve. El retraso se describe como mínimo, pero no se midió con cifras.

**Imágenes propuestas:** (a) diagrama real de bloques: celular → Wi-Fi (`BRAZO_LEGO`, `192.168.4.1`) → ESP32 con página web → BLE de difusión (canal 1) → hub 51515 → 4 motores, con el USB limitado. (b) Captura de la página en el celular (botones de articulación, slider y botón de accionar) y foto del montaje completo (celular, ESP32, hub y brazo).
**Fuente:** propia.
**Prioridad:** Alta.
**Pie sugerido:** *Figura 1.* Arquitectura del prototipo base. *Nota.* Elaboración propia. / *Figura N.* Interfaz web y montaje del prototipo. *Nota.* Elaboración propia.

---

## 17. Sección 4.3: Arquitectura propuesta (Figura 2 real)

**Subtítulo:** 4.3 Propuesta de integración de IA con el prototipo → *Arquitectura propuesta (Figura 2)*. Reemplaza la Figura 2 actual en ASCII.

**Párrafo anterior:**
> **Idea central.** El hub no tiene capacidad para ejecutar visión por computadora ni redes neuronales (por eso otros proyectos con LEGO la delegan a un equipo externo, Autor [pendiente], s. f.). La propuesta es mantener el prototipo como está y añadir un módulo externo de visión e IA que haga el papel del operador humano: en lugar de que una persona elija la articulación y el ángulo en la página, un programa los calcula a partir de la imagen y los envía por la misma vía.

**Imagen propuesta:** diagrama de bloques con el prototipo base en un color y el módulo nuevo (cámara USB, PC con OpenCV y detector profundo) en otro: cámara USB → módulo de visión e IA (PC) → Wi-Fi HTTP (rutas `/s` y `/go`) → ESP32 → BLE de difusión → hub 51515 → motores; el celular como interfaz manual alternativa. Mismo estilo que la Figura 1 para ver qué se agrega.
**Fuente:** propia.
**Prioridad:** Alta.
**Pie sugerido:** *Figura 2.* Arquitectura propuesta con visión e IA. *Nota.* Elaboración propia.

---

## 18. Sección 4.3: Secuencia de la tarea

**Subtítulo:** 4.3 Propuesta de integración de IA con el prototipo → *lista numerada, punto 4*

**Párrafo anterior:**
> 4. **Secuencia de la tarea.** Como el hub mueve una articulación por orden y descarta las que llegan durante un movimiento, el módulo debe enviar las órdenes en secuencia y esperar a que cada movimiento termine (garra abre, base, codo, muñeca, garra cierra, retirada, traslado al cubo, garra abre, regreso a cero).

**Imagen propuesta:** diagrama de flujo (o línea de tiempo) de los nueve pasos con la espera fija entre órdenes, indicando la limitación de un motor por orden y que no hay canal de vuelta.
**Fuente:** propia.
**Prioridad:** Media.
**Pie sugerido:** *Figura N.* Secuencia de órdenes de la tarea de recoger y colocar. *Nota.* Elaboración propia.

---

## 19. Sección 4.4: Pruebas y resultados

**Subtítulo:** 4.4 Pruebas y resultados

**Párrafo anterior:**
> El prototipo base funciona como se describe en la sección 4.2. La integración con IA está planteada como propuesta y no se evaluó sobre el brazo; sus pruebas quedan definidas en la sección 4.3. La única prueba con visión fue preliminar: con la cámara del celular y Pybricks se comprobó que la pelota roja se detecta sobre una base café; no se calibró ni se integró con el brazo. [pendiente: si se hace una prueba de concepto del módulo de visión, añadir aquí sus resultados.]

**Imagen propuesta:** captura de pantalla de la prueba preliminar (celular con Pybricks detectando la pelota roja sobre la base café), con el rectángulo o la marca de detección visible. Si haces la prueba mínima de HSV (tarea C-6), agregar el resultado de la ficha 9.
**Fuente:** propia.
**Prioridad:** Alta. Es la única evidencia propia con visión del informe.
**Pie sugerido:** *Figura N.* Detección preliminar de la pelota roja sobre la base café. *Nota.* Elaboración propia con la cámara del celular y Pybricks.

---

## Orden de trabajo sugerido

1. **Primero, las propias de prioridad Alta:** fichas 3, 4, 16, 17 y 19 (fotos, capturas y los dos diagramas que sustituyen a los ASCII).
2. **Después, los diagramas propios de apoyo:** fichas 2, 9 y 18.
3. **Figuras de fuente con mejor encaje y licencia más sencilla:** fichas 13, 15 y 7 (Capaldi, PeerJ CC BY), y luego 14 (Tzompantzi) y 6 (redibujo de Mohammed).
4. **Opcionales:** 1, 5, 8, 10, 11 y 12, según el espacio que permita el docente.

**Antes de insertar cualquier figura de fuente:** abrir el PDF, confirmar el número y la página, revisar la licencia, y decidir si se reproduce o se redibuja. Después de insertar, renumerar las figuras (E-4) y revisar la lista de acrónimos por si aparecen siglas nuevas en los rótulos.
