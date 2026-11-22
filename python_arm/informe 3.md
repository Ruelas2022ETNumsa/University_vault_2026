# Brazo robótico LEGO con visión por cámara para recoger y depositar objetos

**Autores:** [pendiente]
**Asignatura / institución:** [pendiente]
**Docente:** [pendiente]
**Fecha:** [pendiente]

> **Estado del borrador (21-nov-2026):** reorganizado según el esquema del docente (ver `resumen_21.md`). Tienen contenido las secciones 1 y 2 (la 1.1 se amplió con las fuentes de NotebookLM). Las secciones 3, 4 y 5 son estructura con marcas `[pendiente]`. El brazo se controla a mano desde el celular (ESP32 + página web), pero el modo automático con visión aún no está terminado, por lo que no hay resultados finales ni conclusiones.
>
> **Citas y referencias (APA 7):** los datos de los antecedentes salen del inventario y de la extracción de NotebookLM, no de una lectura completa de cada PDF. Donde falta autor o año aparece `[pendiente]` o "s. f.". Antes de entregar hay que abrir cada fuente, confirmar autores, año, revista y cifras. Copias anteriores de este archivo: `informe 1.md` y `informe 2.md`.

---

## 1. Introducción y antecedentes

### 1.1 Antecedentes

Los brazos robóticos que recogen un objeto y lo colocan en otro lugar (*pick and place*) son una de las aplicaciones más comunes de la robótica de manipulación. Para que el brazo sepa dónde está el objeto, un enfoque habitual es agregar una cámara y procesar la imagen. En proyectos de bajo costo, una solución frecuente es segmentar el color del objeto, obtener su centroide en la imagen y convertir esa posición en los ángulos de las articulaciones, ya sea con cinemática inversa o con calibraciones más simples (Autores [pendiente], 2026; Monirujjaman Khan et al., 2021).

**Robótica educativa con LEGO y brazos de bajo costo.** LEGO Mindstorms se usa en cursos universitarios desde hace más de una década. Fernández Panadero et al. (2010) reportaron que el 98 % de los estudiantes dijo haber aumentado sus conocimientos en robótica tras una actividad con kits LEGO. Wu et al. (2014) usaron un brazo con pinza en un laboratorio de sistemas de control, y Gunardi y Jumadri (2020) coordinaron por Bluetooth una cinta transportadora y un brazo NXT con un sensor de color para clasificar tres colores. Con un enfoque similar, Markvicka et al. (2023) diseñaron un brazo de bajo costo (menos de 200 USD) y observaron un efecto favorable en el aprendizaje de cinemática y control. Ninguno de estos trabajos usa una cámara ni el hub Inventor 51515 con Pybricks.

**Control remoto con ESP32 o desde el celular.** Tzompantzi Netzahual et al. (2019) controlaron un brazo didáctico de 4 GDL con un ESP32 y una aplicación Android, por Wi-Fi (servidor HTTP) y Bluetooth de bajo consumo (BLE), con respuesta en tiempo real hasta unos 40 m. Suhaeb y Risal (2024) alojaron un servidor web en el ESP32 y midieron tiempos de respuesta de 85 a 92 ms para comandos directos. Yilmaz et al. (2025) construyeron un brazo IoT de 4 GDL con ESP32, interfaz web guardada en la memoria flash y parada de emergencia por hardware. Lim et al. (2021) manejaron un brazo de 6 GDL desde el celular con la aplicación Blynk y un sensor de color, con hasta 90 % de acierto. Estos cuatro trabajos controlan o clasifican **sin visión por cámara**.

**Visión por computadora para clasificar y tomar objetos.** Mada Sanjaya et al. (2018) combinaron una webcam, Python y OpenCV con una red neuronal para resolver la cinemática inversa de un brazo de 5 GDL. Monirujjaman Khan et al. (2021) lograron 94,6 % de acierto al clasificar por forma con un brazo de 4 GDL y segmentación HSV, y Mohammed et al. (2023) reportaron 93,83 % de precisión con luz entre 5 y 7000 lux usando una Raspberry Pi y un Arduino. Monroy Moya et al. (2024) hicieron lo mismo con un brazo de 3 GDL (unos 155 USD) controlado solo por una Raspberry Pi 4. Dos tesis ecuatorianas automatizan brazos didácticos de 4 GDL: Aucapiña e Iza (2021) integraron un uArm Swift Pro con visión y reportaron 84 % de confiabilidad global, y Llerena y Salazar (2022) usaron un Hiwonder xArm 1S con Raspberry Pi 4 y una interfaz operada a distancia por red. Rangarajan y Bianchini (2026) compensaron la falta de articulación de muñeca de un brazo de 4 GDL con barridos laterales de reorientación (89,8 % de éxito).

Estos trabajos coinciden en tres limitaciones que también aplican a este proyecto: la **iluminación** altera la segmentación por color (Anusha et al., 2018; Monirujjaman Khan et al., 2021; Llerena y Salazar, 2022), la **calibración** entre cámara y brazo se desajusta con el tiempo (Rangarajan y Bianchini, 2026) y la **carga o alimentación** de los servos es limitada (Markvicka et al., 2023; Llerena y Salazar, 2022).

**Plataformas LEGO con cámara.** Existen proyectos de brazos con el hub LEGO Inventor 51515 que siguen una pelota roja con una cámara web (LEGO Ideas, s. f.), y un proyecto oficial de Pybricks con un brazo LEGO SPIKE Prime y cámara que detecta objetos de colores para tomarlos (Pybricks, s. f.-a). Otros trabajos con LEGO delegan la visión a una computadora externa, porque la cámara del propio robot no tiene la potencia necesaria (Autor [pendiente], s. f.). Pybricks, un firmware alternativo en MicroPython para los hubs LEGO, ofrece además una función en versión beta llamada *smart sensors*, que permite usar la cámara de un teléfono como sensor conectado al hub (Pybricks, s. f.-b).

**Brecha que atiende este trabajo.** Los trabajos con ESP32 controlan el brazo desde el celular pero sin cámara; los de visión procesan la imagen en una PC o en una Raspberry Pi; y los de LEGO con cámara no se controlan desde el celular. En las fuentes revisadas no aparece una combinación de hub LEGO Inventor 51515 con Pybricks, cámara de celular y control remoto desde una página web servida por un ESP32. Este proyecto reúne esas piezas con equipo de bajo costo.

La Tabla 1 resume los antecedentes más cercanos y qué aporta cada uno.

**Tabla 1**

*Antecedentes más cercanos al proyecto*

| Antecedente | Cámara | Control o comunicación | Relación con este trabajo |
| ----------- | ------ | ---------------------- | ------------------------- |
| Tzompantzi Netzahual et al. (2019): brazo de 4 GDL | No | ESP32, app Android, Wi-Fi y BLE | Mismo número de articulaciones y ESP32; este proyecto usa una página web y envía al hub por BLE. |
| Suhaeb y Risal (2024): brazo con servidor web | No | ESP32 como servidor web (Wi-Fi) | Base de la idea de la página web en el ESP32. Reportan 85 a 92 ms de respuesta; aquí el retraso no se ha medido. |
| Yilmaz et al. (2025): brazo IoT de 4 GDL | No | ESP32, interfaz web, parada de emergencia | Referencia para el botón de parada, pendiente en este proyecto. |
| Monirujjaman Khan et al. (2021): brazo de 4 GDL | Webcam fija | PC con GUI, HSV y cinemática inversa | Mismo principio de segmentar por color; este proyecto usa tablas calibradas en lugar de cinemática inversa. |
| Llerena y Salazar (2022), tesis: xArm 1S de 4 GDL | Webcam | Raspberry Pi 4, OpenCV, GUI remota por red | Brazo didáctico de 4 GDL con visión; la visión corre en una Raspberry Pi y no en un celular. |
| Mohammed et al. (2023): brazo de 5 GDL | Webcam | Raspberry Pi y Arduino | Muestra el efecto de la iluminación sobre HSV, útil para las pruebas. |
| Brazo de 3 GDL con una sola cámara (Autores [pendiente], 2026) | Cenital | HSV, centroide y cinemática inversa | Validado con luz controlada, cámara fija y pocas pruebas. |
| VISION (LEGO Ideas, s. f.) | Webcam en PC | Hub Inventor 51515 | Es el más parecido al hardware; aquí la cámara es un celular conectado al hub. |
| Brazo con visión de Pybricks (Pybricks, s. f.-a) | Celular | Hub SPIKE Prime, Pybricks | Base del proyecto: se adaptó el hub, los puertos, el color y el arranque. |
| LEGO con Raspberry Pi y OpenCV (Autor [pendiente], s. f.) | Raspberry Pi | Bluetooth | Alternativa descartada por ahora para no agregar equipos. |

*Nota.* Elaboración propia a partir de las fuentes citadas. Verificar contra los trabajos completos.

### 1.2 Propósito general del trabajo

Construir y documentar un brazo robótico con motores y hub LEGO Inventor 51515 con firmware Pybricks que pueda controlarse a distancia desde el celular (página web servida por un ESP32) y que use la cámara del celular para encontrar una pelota roja, tomarla y dejarla en un cubo café, con la computadora usada solo para dar comandos por teclado.

---

## 2. Objetivo

### 2.1 Objetivo general

Desarrollar un brazo robótico LEGO controlado con Pybricks que pueda manejarse a distancia desde el celular y que, con la cámara del celular, localice una pelota roja, la tome y la deposite en un cubo café.

### 2.2 Objetivos específicos

1. Definir y programar las cuatro articulaciones del brazo (base, codo, muñeca y garra) con sus multiplicadores y rangos de movimiento.
2. Implementar el control remoto manual: un ESP32 que sirva una página web por Wi-Fi y envíe las órdenes al hub por Bluetooth, de modo que cada orden mueva una articulación.
3. Integrar la cámara del celular como *smart sensor* del hub, de modo que el programa reciba la posición y el tamaño de la pelota y del cubo.
4. Diseñar un procedimiento de calibración manual que registre, para varias posiciones, la lectura de la cámara junto con los ángulos del brazo, y que genere las tablas de toma y de depósito.
5. Implementar una rutina automática que busque el cubo y la pelota, calcule la pose del brazo interpolando las tablas, tome la pelota, la deje en el cubo y regrese a la posición inicial.
6. Garantizar un funcionamiento seguro con alimentación USB limitada: un solo motor energizado a la vez, vigilancia del voltaje y límites de ángulo aplicados en el hub.
7. Evaluar el desempeño del sistema: retraso del control remoto, tasa de éxito de la toma e influencia de la iluminación. *[Pendiente: depende de terminar el montaje y de definir las pruebas.]*

### 2.3 Alcance

El estudio incluye:

- El brazo de cuatro motores y un único hub LEGO, conectado a la computadora (programa y comandos por teclado) y al celular (cámara).
- El control manual desde el celular: un ESP32 crea su propia red Wi-Fi y sirve una página con botones para elegir la articulación, un control deslizante de ángulo y un botón de accionar. El ESP32 envía cada orden al hub por Bluetooth (mensajes de difusión de Pybricks) y el hub mueve una sola articulación por orden. Esta parte se probó con el brazo real.

La pelota y el cubo permanecen quietos durante cada ejecución. El sistema opera en interior, con iluminación constante, sobre una superficie plana, con objetos livianos de color definido (pelota roja y cubo café) dentro del radio de alcance del brazo, y con operación local o remota inalámbrica (Monroy Moya et al., 2024; Llerena y Salazar, 2022).

Quedan fuera del alcance de esta etapa:

- La integración del modo automático con visión y el control remoto en un solo flujo, que sigue en desarrollo y se plantea como trabajo futuro apoyado en los antecedentes de la sección 1.
- La alimentación con batería, que cambiaría la restricción de mover un motor a la vez.

### 2.4 Limitaciones

- **Alimentación limitada.** El brazo funciona solo con alimentación USB, sin batería. Por eso se mueve un motor a la vez y se vigila el voltaje del hub, con una pausa si baja de 5500 mV.
- **Precisión limitada.** Los motores no tienen la precisión de un brazo industrial y, según observaciones previas del proyecto, al soltarlos aparecen desvíos de pocos grados y holguras en los engranajes.
- **Colores y luz.** El rojo y el café pueden confundirse al segmentar en HSV, y los cambios de luz, las sombras o el brillo degradan la detección (Monroy Moya et al., 2024; Monirujjaman Khan et al., 2021).
- **Carga útil.** Los motores y el montaje solo permiten manipular objetos ligeros, como en otros brazos de bajo costo (Aucapiña e Iza, 2021; Markvicka et al., 2023).
- **Sin verificación del agarre.** La garra no tiene sensor que confirme que sujetó el objeto, por lo que el brazo completa la secuencia aunque este se caiga (Monirujjaman Khan et al., 2021).
- **Cámara montada sobre el brazo.** Tras agregar un soporte trasero, la cámara gira junto con el brazo, por lo que las calibraciones deben tomarse siempre con el brazo en la misma posición de referencia. *[Por confirmar con pruebas.]*
- **Función en beta.** La función *smart sensors* de Pybricks exige la versión beta de la aplicación y un firmware actualizado (Pybricks, s. f.-b). La guía oficial describe los pasos para SPIKE Prime; con el Inventor 51515 la prueba del proyecto indica que funciona igual, pero la documentación no lo nombra.
- **Sin canal de vuelta del hub al ESP32.** La página muestra el último ángulo *ordenado*, no el alcanzado por el motor; si se aborta un movimiento, el valor guardado difiere de la posición real.
- **Retraso no medido.** El retraso entre accionar y mover es mínimo según la observación del usuario, pero no se midió con cifras.
- **Montaje en desarrollo.** El brazo todavía no está terminado. En una primera prueba real el programa funcionó en general, pero faltan ajustes de posición inicial, de salida en pantalla, de recalibración de la cámara con el nuevo montaje y de los ángulos de algunos motores, que necesitan valores negativos.

---

## 3. Justificación del proyecto

> Esta sección responde: ¿por qué se quiere hacer el estudio y para qué servirá? Los argumentos salen de la literatura revisada; los datos de la institución siguen como `[pendiente]` porque no están en ninguna fuente.

### 3.1 Importancia para la institución

Los brazos robóticos de bajo costo se justifican en la literatura porque acercan la práctica con hardware real a quienes no pueden pagar equipo industrial. Un brazo industrial supera habitualmente los 30 000 USD y los kits comerciales de robótica educativa suelen costar más de 1000 USD, lo que limita cuántas unidades puede comprar una institución (Markvicka et al., 2023). Además, el aprendizaje activo con modelos físicos es más efectivo que los métodos pasivos y enfrenta al estudiante con fenómenos que la teoría abstracta no muestra, como la holgura de las articulaciones y la fricción (Fernández Panadero et al., 2010; Markvicka et al., 2023). Este proyecto aprovecha un kit LEGO Inventor 51515, un ESP32 y un celular, equipos de bajo costo y de uso común, para construir un brazo con control remoto y visión por cámara.

[pendiente: nombre de la institución, carrera y asignatura, y por qué el tema es relevante para ellas.]

### 3.2 Escenario del proyecto

El proyecto se desarrolla como informe universitario [pendiente: institución y asignatura]. Se trabaja con un brazo armado con el kit LEGO Inventor 51515 y firmware Pybricks, conectado por USB a un cargador de corriente limitada y sin batería; ese límite obliga a mover un motor a la vez y a vigilar el voltaje. El control se hace desde un celular, sin instalar aplicaciones, mediante una página servida por un ESP32 con su propia red Wi-Fi. Esto permite operar el brazo a distancia, como plantearon otros trabajos para mantener las prácticas de laboratorio con aforo reducido (Tzompantzi Netzahual et al., 2019; Llerena y Salazar, 2022). El modo automático con cámara sigue en desarrollo.

### 3.3 Impacto esperado y utilidad

Lo que se busca lograr al terminar el proyecto y para qué servirá. Cada fila se apoya en lo que reportan las fuentes; los resultados propios quedan por confirmar con las pruebas.

| Tipo de impacto | Qué se busca lograr |
| --------------- | ------------------- |
| Educativo | Contar con un brazo práctico para aprender programación en Python, comunicación inalámbrica y visión por color, reproducible con equipo ya disponible (Fernández Panadero et al., 2010; Markvicka et al., 2023). |
| Tecnológico | Demostrar que un hub LEGO con Pybricks puede controlarse desde el celular con un ESP32 por Wi-Fi y Bluetooth, y dejar la base para integrar la visión por computadora (Suhaeb y Risal, 2024; Tzompantzi Netzahual et al., 2019). |
| Científico | Documentar una arquitectura que no aparece en las fuentes revisadas (hub LEGO, celular y ESP32) y medir su retraso, su tasa de éxito y el efecto de la luz. *[Pendiente: depende de hacer las pruebas.]* |
| Económico | Reutilizar equipo de bajo costo en lugar de comprar un brazo comercial (Markvicka et al., 2023). *[Pendiente: sumar el costo real del montaje.]* |
| Social | Permitir la práctica a distancia cuando hay aforo limitado (Tzompantzi Netzahual et al., 2019; Llerena y Salazar, 2022). |
| Ambiental | No hay base en las fuentes. Omitir salvo que el docente lo pida. |

---

## 4. Desarrollo del proyecto

### 4.1 Marco teórico

[pendiente: se redactará con las fuentes de Perplexity y NotebookLM. Temas previstos:]

- Brazos robóticos y tareas de *pick and place*
- Plataforma LEGO Inventor 51515 y firmware Pybricks
- *Smart sensors* de Pybricks: celular como cámara del hub
- Segmentación de color (HSV) y detección de objetos
- Calibración entre la cámara y el brazo: tablas e interpolación
- Cinemática del brazo (como contraste con el método de tablas)
- Control remoto: Wi-Fi, Bluetooth de bajo consumo y ESP32
- Imprecisión de motores sin encoders de alta precisión

### 4.2 Diseño del sistema

[pendiente: montaje mecánico, articulaciones (puertos, multiplicadores y rangos), alimentación y comunicación (celular, Wi-Fi, ESP32, Bluetooth, hub). Material de partida en `resumen_16.md` y `resumen_21.md`, secciones 8 y 9.]

### 4.3 Implementación

[pendiente: calibración manual, tablas de toma y depósito, rutina automática (`ha7.py`) y modo remoto (`ha9.py` y `web_control.py`).]

### 4.4 Pruebas y resultados

[pendiente: hasta terminar el brazo.]

---

## 5. Conclusiones y recomendaciones

### 5.1 Conclusiones

[pendiente: dependen de terminar el brazo y de las pruebas.]

### 5.2 Recomendaciones

[pendiente: incluye unir el modo automático con visión al control remoto, medir el retraso, agregar un botón de parada en la página (como en Yilmaz et al., 2025) y definir qué hace el hub ante voltaje bajo sin la computadora.]

---

## 6. Referencias bibliográficas e internet

> Formato APA 7. Completar autores y años al leer los trabajos completos, y ordenar la lista alfabéticamente al terminar. Solo se listan las fuentes citadas en el texto. Las entradas marcadas [pendiente] vienen del inventario de NotebookLM y no se han verificado en el PDF.

Anusha, G., Ganavi, D., Revathi, H., Sahana, P., Sreenivas Rao, M. V., y Basavanna, M. (2018). *Robotic arm manipulation using shape and color based on visual servoing*. [revista pendiente].

Aucapiña Garnica, N. F., e Iza Guanochanga, B. I. (2021). *Diseño e implementación de un sistema de visión artificial para la manipulación, ensamblaje y control de calidad de piezas...* [Tesis de grado, Universidad de las Fuerzas Armadas ESPE]. [enlace pendiente]

[Autor pendiente]. (s. f.). *LEGO con Raspberry Pi y OpenCV* [Proyecto]. Tampere University. https://joedavid-tuni.github.io/MR3/

[Autores pendientes]. (2026). Low cost single camera robotic arm for vision guided pick and place. *Journal of Robotics and Control (JRC)*. https://journal.umy.ac.id/index.php/jrc/article/view/28524

[Autores pendientes]. ([año pendiente]). *Kit educativo de visión con brazo robótico de 3 GDL* [Artículo de conferencia]. American Society for Engineering Education (ASEE). https://peer.asee.org/45199.pdf

Fernández Panadero, C., Villena Román, J., y Delgado Kloos, C. (2010). Impact of learning experiences using LEGO Mindstorms in engineering courses. [Actas de conferencia pendientes].

Gunardi, Y., y Jumadri, J. N. (2020). Design color sorting with conveyor and robot arm using Lego Mindstorm NXT. [revista pendiente].

LEGO Ideas. (s. f.). *VISION* [Propuesta de proyecto]. https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749

Lim, W. J., Teoh, P. S., Abdul Ghani, N. M., y Abas, M. F. (2021). Automatic control of color sorting and pick/place of a 6-DOF robot arm. [revista pendiente].

Llerena Buenaño, A. S., y Salazar Villamar, M. J. (2022). *Automatización de un sistema identificador y posicionador de objetos a través de un brazo robótico mediante visión artificial con lenguaje Python* [Tesis de grado, Universidad Politécnica Salesiana, sede Guayaquil]. [enlace pendiente]

Mada Sanjaya, W. S., Anggraeni, D., Nurasyidiek, M. Y. S., et al. (2018). Colored object sorting using 5 DoF robot arm based artificial neural network (ANN) method. *Journal of Physics: Conference Series, 1090*, 012070.

Markvicka, E., Finnegan, J. D., Moomau, K., Sommers, A. S., Peteranetz, M. S., y Daher, T. A. (2023). Designing learning experiences with a low-cost robotic arm. [Actas ASEE pendientes].

Mohammed, M. M., Al-Khafaji, M. M. H., y Abbas, T. F. (2023). Smart robot vision for a pick and place robotic system under different illumination conditions. [revista pendiente].

Monirujjaman Khan, M., Intisar, M., Islam, M. R., Nizamuddin, A. S., et al. (2021). Design and implementation of a robotic vision system operated using an interactive graphical user interface (GUI) application. [revista pendiente].

Monroy Moya, D. F., Barrera Prieto, F., y Rojas Sarmiento, D. A. (2024). Computer vision implementation on Raspberry Pi 4 for a 3 DOF robotic arm in object classification by shape and color. [revista pendiente].

Pybricks. (s. f.-a). *Robotic arm with vision*. https://pybricks.com/project/robot-arm-camera-tracker/

Pybricks. (s. f.-b). *Use your phone as a smart sensor*. https://pybricks.com/learn/smart-sensors/getting-started/

Rangarajan, A., y Bianchini, B. (2026). Vision-guided reorientation and color sorting of writing utensils using a low-cost 4-DoF arm. [revista pendiente].

Suhaeb, S., y Risal, A. (2024). Implementation of ESP32-based web host for control and monitoring of robotic arm. [revista pendiente].

Tzompantzi Netzahual, J. E., Nava Bautista, H., y Sánchez Hernández, M. J. (2019). Real time control of robotic arm using Bluetooth Low Energy & Wi-Fi with the module board ESP32 and Android application. [revista pendiente].

Wu, Y., de Vries, C., Ford, M., y Herrera, A. (2014). *Project report: Using Mindstorms in a control systems lab to impact next generation engineers* [Informe de proyecto]. [institución pendiente].

Yilmaz, S., Akay, C., y Kaysi, F. (2025). Design and implementation of a low-cost IoT-based robotic arm for product feeding and sorting in manufacturing lines. *Electronics, 14*, 4801.

---

## Guía resumen del manual de publicaciones con normas APA

> Resumen breve de las reglas APA 7 que se aplican en este informe. Preliminar: contrastar con el texto que envió el docente y confirmar con él cómo debe presentarse esta sección.

- **Cita en el texto:** autor y año entre paréntesis, por ejemplo (Pybricks, s. f.). Con dos autores se unen con "y"; con tres o más se usa "et al.".
- **Sin fecha:** se escribe "s. f.". Si hay varias obras del mismo autor sin fecha, se distinguen con letras: s. f.-a, s. f.-b.
- **Cita textual corta** (menos de 40 palabras): entre comillas, con autor, año y página.
- **Lista de referencias:** en orden alfabético, con sangría francesa. Cada fuente citada debe estar en la lista y viceversa.
- **Páginas web y documentos en línea:** autor, fecha, título en cursiva y enlace. Si hay DOI, se escribe como enlace (https://doi.org/...).
- **Tablas y figuras:** número en negrita, título en cursiva debajo del número, y una nota si hace falta ("*Nota.*").

---

## Anexo A. Lista de acrónimos

*(Actualizar a medida que se redacte el texto final.)*

| Acrónimo | Significado |
| -------- | ----------- |
| ASEE | American Society for Engineering Education |
| BLE | Bluetooth de bajo consumo (*Bluetooth Low Energy*) |
| ESP32 | Microcontrolador con Wi-Fi y Bluetooth (fabricante Espressif) |
| GDL | Grados de libertad |
| GUI | Interfaz gráfica de usuario (*Graphical User Interface*) |
| HSV | Tono, saturación y valor (*hue, saturation, value*) |
| HTTP | Protocolo de transferencia de hipertexto (*Hypertext Transfer Protocol*) |
| IoT | Internet de las cosas (*Internet of Things*) |
| JRC | Journal of Robotics and Control |
| OpenCV | Open Source Computer Vision Library |
| USB | Bus serie universal (*Universal Serial Bus*) |
