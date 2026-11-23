# Control de un brazo robótico educativo mediante visión por computadora e inteligencia artificial: revisión de antecedentes y propuesta de integración con un prototipo LEGO

**Autores:** [pendiente]
**Asignatura / institución:** [pendiente]
**Docente:** [pendiente]
**Fecha:** [pendiente]

> **Estado del borrador (22-nov-2026):** segundo borrador completo (secciones 1 a 6), corregido con las respuestas de NotebookLM S0 a S8 y N22 a N24, las de Gemini A3 a A7 y N22b, y las búsquedas de Perplexity A1, A2 y A8. El informe sustenta de forma teórica cómo integrar visión por computadora e inteligencia artificial (IA) al control de un brazo robótico educativo de 4 articulaciones, y usa como base un prototipo LEGO cuyo control remoto con ESP32 ya funciona (esa parte se entrega en otra materia). No se presentan resultados de IA sobre el brazo, porque no son necesarios en esta materia. Falta pulir con consultas más detalladas y completar los datos marcados `[pendiente]`.
>
> **Citas y referencias (APA 7):** los datos salen del inventario y de las extracciones de NotebookLM, no de una lectura completa de cada PDF. Donde falta autor o año aparece `[pendiente]`, `[verificar]` o "s. f.". Antes de entregar hay que abrir cada fuente y confirmar autores, año, revista, cifras y ecuaciones. Copias anteriores de este archivo: `informe 1.md` a `informe 9.md`. Pendientes: abrir los PDF para confirmar autores, año, revista y páginas (C1); confirmar en el video del proyecto de Pybricks la alimentación y si los motores se mueven a la vez; verificar los README de los proyectos abiertos citados; datos de institución.

---

## 1. Introducción y antecedentes

### 1.1 Antecedentes

Los brazos robóticos que recogen un objeto y lo colocan en otro lugar (*pick and place*) son una de las aplicaciones más comunes de la robótica de manipulación. Para que el brazo sepa dónde está el objeto, un enfoque habitual es agregar una cámara y procesar la imagen. En proyectos de bajo costo, una solución frecuente es segmentar el color del objeto, obtener su centroide en la imagen y convertir esa posición en los ángulos de las articulaciones, ya sea con cinemática inversa o con calibraciones más simples (Autores [pendiente], 2026; Intisar et al., 2021).

**Robótica educativa con LEGO y brazos de bajo costo.** LEGO Mindstorms se usa en cursos universitarios desde hace más de una década. Fernández Panadero et al. (2010) reportaron que el 98 % de los estudiantes dijo haber aumentado sus conocimientos en robótica tras una actividad con kits LEGO. Wu et al. (2014) usaron un brazo con pinza en un laboratorio de sistemas de control, y Gunardi y Jumadri (2020) coordinaron por Bluetooth una cinta transportadora y un brazo NXT con un sensor de color para clasificar tres colores. Con un enfoque similar, Markvicka et al. (2023) diseñaron un brazo de bajo costo (menos de 200 USD) y lo evaluaron en un curso: con 36 estudiantes, las calificaciones no difirieron de forma significativa entre las tareas tradicionales y las tareas con el brazo, y se aplicó además una encuesta de percepción [verificar resultados y que esos datos correspondan a este trabajo]. Ninguno de estos trabajos usa una cámara ni el hub Inventor 51515 con Pybricks.

**Control remoto con ESP32 o desde el celular.** Tzompantzi Netzahual et al. (2019) controlaron un brazo didáctico de 4 GDL con un ESP32 y una aplicación Android, por Wi-Fi (servidor HTTP) y Bluetooth de bajo consumo (BLE), y reportan respuesta en tiempo real a menos de 40 m con ambas tecnologías, aunque solo midieron tiempos de respuesta para Wi-Fi. Suhaeb y Risal (2024) alojaron un servidor web en el ESP32 y midieron tiempos de respuesta de 85 a 92 ms para comandos directos. Yilmaz et al. (2025) construyeron un brazo IoT de 4 GDL con ESP32, interfaz web guardada en la memoria flash y parada de emergencia por hardware. Lim et al. (2021) manejaron un brazo de 6 GDL desde el celular con la aplicación Blynk y un sensor de color, con hasta 90 % de acierto. Shah y Arockia Doss (2026) controlan un brazo con ESP32 y servomotores MG996R desde una interfaz web con WebSockets, con una latencia menor a 150 ms entre la orden y la actuación (sin precisar cómo se midió) y una parada de emergencia en el navegador; su detección con YOLOv8-OBB y ROS/MoveIt se usó solo en simulación. Estos cinco trabajos controlan o clasifican **sin visión por cámara en el brazo físico**.

**Visión por computadora e IA para clasificar y tomar objetos.** Mada Sanjaya et al. (2018) combinaron una webcam, Python y OpenCV con una red neuronal para resolver la cinemática inversa de un brazo de 5 GDL. Intisar et al. (2021) lograron 94,6 % de acierto al clasificar por forma con un brazo de 4 GDL y segmentación HSV, y Mohammed et al. (2023) reportaron 93,83 % de precisión con luz entre 5 y 7000 lux usando una Raspberry Pi y un Arduino. Monroy Moya et al. (2026) clasificaron y apilaron objetos por forma y color con un brazo de 3 GDL (de 155 a 164 USD) cuya visión y control corren en una sola Raspberry Pi 4. Dos tesis ecuatorianas automatizan brazos didácticos: Aucapiña e Iza (2019) integraron un uArm Swift Pro de 4 GDL con dos cámaras, una red entrenada y retroiluminación, y reportaron 97,28 % de acierto en la identificación y 84,28 % en el ensamblado, la etapa más baja; Llerena y Salazar (2022) usaron un Hiwonder xArm 1S con Raspberry Pi 4, detección de color con HSV y una interfaz a la que se accede a distancia por VNC. Rangarajan y Bianchini (2026) usaron un detector basado en aprendizaje profundo y compensaron la falta de articulación de muñeca de un brazo de 4 GDL con barridos laterales de reorientación (89,8 % de éxito). Dos trabajos recientes ya separan la visión, que corre en una PC, del control, a cargo de un ESP32. Dang et al. (2026) construyeron un brazo de 4 GDL con ESP32, módulo PCA9685 y servos MG996R, cuya detección con YOLOv12 corre en una laptop solo con CPU; el artículo describe una validación cualitativa y no reporta precisión, tiempo de inferencia ni tasa de éxito. Capaldi (2024) conectó una PC con YOLOv8 a un hub educativo VEX V5 mediante dos ESP32 con el protocolo ESP-NOW, con pérdida de paquetes menor a 1 % hasta 40 m y 187 ms de ida y vuelta; su actuador es un brazo barredor de clasificación y no un brazo articulado.

Estos trabajos coinciden en tres limitaciones que también aplican a este proyecto: la **iluminación** altera la segmentación por color (Anusha et al., 2018; Intisar et al., 2021; Mohammed et al., 2023), la **calibración** entre cámara y brazo se desajusta con el tiempo (Rangarajan y Bianchini, 2026) y la **carga o alimentación** de los servos es limitada (Markvicka et al., 2023; Llerena y Salazar, 2022).

**Plataformas LEGO con cámara.** Existen proyectos de brazos con el hub LEGO Inventor 51515 que siguen una pelota roja con una cámara web (LEGO Ideas, s. f.), y un proyecto de Pybricks con un brazo LEGO SPIKE Prime que usa el celular como cámara (función *smart sensors*), busca un objeto rojo, gira la base hasta centrarlo y lo toma (Pybricks, s. f.-a). No se encontró un proyecto equivalente con el hub 51515 y cámara de celular. Otros trabajos con LEGO delegan la visión a una computadora externa, porque la cámara del propio robot no tiene la potencia necesaria (Autor [pendiente], s. f.). También hay proyectos abiertos que combinan partes de la arquitectura de este trabajo: un tren LEGO con hub Pybricks controlado por BLE desde un ESP32-S3 que sirve una página web y transmite video de una cámara, sin procesar la imagen (Johnson, 2026); un robot con hub 51515 que detecta y toma un objeto con visión TensorFlow y BLE, sin ESP32 confirmado (osullivp, 2021); un proyecto de la WRO 2026 con hub Inventor y Pybricks, un ESP32 y una cámara OpenMV que detecta bloques de color, sin que se documente la función del ESP32 (GC-TO, 2026); y un ESP32 como intermediario entre un módulo de visión (HuskyLens) y un hub SPIKE Prime (Anton's Mindstorms, 2025). Son repositorios y tutoriales, no literatura arbitrada, y se citan como antecedentes de implementación [verificar en cada README]. Pybricks, un firmware alternativo en MicroPython para los hubs LEGO, ofrece además una función en versión beta llamada *smart sensors*, que permite usar la cámara de un teléfono como sensor conectado al hub (Pybricks, s. f.-b).

**Brecha que atiende este trabajo.** Los trabajos con ESP32 controlan el brazo desde el celular o el navegador, casi siempre sin cámara; los de visión e IA procesan la imagen en una PC o en una Raspberry Pi y envían los ángulos a un microcontrolador; y los de LEGO con cámara la conectan al propio hub o a una computadora. Dang et al. (2026) y Capaldi (2024) ya combinan una PC con visión de aprendizaje profundo y un ESP32 en plataformas educativas; Pybricks y LEGO Ideas muestran que se puede dar visión a un hub LEGO; y hay proyectos abiertos con el ESP32 como puente Wi-Fi a BLE hacia un hub Pybricks. Por eso la novedad que se plantea no es la cámara, ni la PC con visión, ni el puente por separado. En la literatura académica revisada no aparece una combinación de brazo de 4 GDL con hub LEGO Inventor 51515 y Pybricks, control remoto desde una página web servida por un ESP32 y un módulo de visión o IA externo que le envíe las órdenes; los proyectos abiertos encontrados tienen solo partes de esa cadena (Tabla 1), y no se halló una tesis ni un artículo arbitrado que la documente completa. Este informe investiga cómo se puede lograr esa integración con equipo de bajo costo.

La Tabla 1 resume los antecedentes más cercanos y qué aporta cada uno.

**Tabla 1**

*Antecedentes más cercanos al proyecto*

| Antecedente | Cámara | Control o comunicación | Relación con este trabajo |
| ----------- | ------ | ---------------------- | ------------------------- |
| Tzompantzi Netzahual et al. (2019): brazo de 4 GDL | No | ESP32, app Android, Wi-Fi y BLE | Mismo número de articulaciones y ESP32; este proyecto usa una página web y envía al hub por BLE. |
| Suhaeb y Risal (2024): brazo con servidor web | No | ESP32 como servidor web (Wi-Fi) | Base de la idea de la página web en el ESP32. Reportan 85 a 92 ms de respuesta; aquí el retraso no se ha medido. |
| Yilmaz et al. (2025): brazo IoT de 4 GDL | No | ESP32, interfaz web, parada de emergencia | Referencia para el botón de parada, pendiente en este proyecto. |
| Intisar et al. (2021): brazo de 4 GDL | Webcam fija | PC con GUI, HSV y cinemática inversa | Mismo principio de segmentar por color; aquí se proponen tablas calibradas o una red neuronal en lugar de cinemática inversa. |
| Mada Sanjaya et al. (2018): brazo de 5 GDL | Webcam | PC, Python y red neuronal (ANN), Arduino | Antecedente directo del uso de IA para pasar de la imagen a los ángulos. |
| Llerena y Salazar (2022), tesis: xArm 1S | Webcam fija sobre una banda | Raspberry Pi 4, OpenCV (color HSV), GUI de escritorio con acceso remoto por VNC | Brazo didáctico con visión por color; visión y control corren en la misma Raspberry Pi y no en un celular. |
| Rangarajan y Bianchini (2026): brazo de 4 GDL | Cenital | Detector de aprendizaje profundo y HSV | Muestra cómo la IA y la planificación compensan un brazo sin muñeca. |
| Dang et al. (2026): brazo de 4 GDL | Cámara a la laptop [verificar modelo] | Laptop con YOLOv12 solo con CPU; ESP32 con PCA9685; USB en la ruta de visión [verificar] y MQTT en la interfaz web | Misma separación entre visión en PC y ESP32 como controlador; sin cifras de desempeño. Este proyecto agrega el hub LEGO y el enlace inalámbrico por BLE. |
| Capaldi (2024): hub VEX V5 con brazo barredor | Cámara OpenMV H7 por USB a una PC | PC con YOLOv8, dos ESP32 con ESP-NOW y RS-485 al VEX V5 | Análogo más cercano de la cadena PC con visión, ESP32 y hub educativo; usa ESP-NOW y no Wi-Fi más BLE. Reporta 187 ms de ida y vuelta y menos de 1 % de pérdida hasta 40 m. |
| Brazo de 3 GDL con una sola cámara (Autores [pendiente], 2026) | Cenital | HSV, centroide y cinemática inversa | Validado con luz controlada, cámara fija y pocas pruebas. |
| VISION (LEGO Ideas, s. f.) | Webcam en PC | Hub Inventor 51515 | Es el más parecido al hardware; aquí la cámara estaría en una PC y las órdenes llegarían al hub por el ESP32. |
| Brazo con visión de Pybricks (Pybricks, s. f.-a) | Celular | Hub SPIKE Prime, Pybricks | Referencia más cercana de visión en LEGO. En este proyecto solo se probó, de forma preliminar, la detección de color de la pelota roja sobre una base café; no se calibró ni se integró. |
| Wildlife Spotter Train (Johnson, 2026) | Cámara en el ESP32-S3 (video MJPEG) | Navegador, Wi-Fi, ESP32-S3, BLE [verificar GATT o difusión], City Hub con Pybricks | Muestra el ESP32 como puente de Wi-Fi a BLE hacia un hub Pybricks; es un tren y no procesa la imagen. |
| Lego51515 BLE Arduino TensorFlow (osullivp, 2021) | Cámara con TensorFlow | BLE, hub 51515 | Hub 51515 con visión y toma de objeto; no se confirmó ESP32 ni Pybricks. |

*Nota.* Elaboración propia a partir de las fuentes citadas. Verificar contra los trabajos completos.

### 1.2 Propósito general del trabajo

Investigar y sustentar con la literatura cómo integrar visión por computadora e IA al control de un brazo robótico educativo de cuatro articulaciones, tomando como base un prototipo con hub LEGO Inventor 51515 y firmware Pybricks que ya puede controlarse a distancia desde un celular mediante un ESP32, y proponer la arquitectura de esa integración.

---

## 2. Objetivo

### 2.1 Objetivo general

Analizar, a partir de la literatura, las técnicas de visión por computadora e IA que se usan para controlar brazos robóticos educativos de bajo costo, y proponer una arquitectura que las integre al prototipo de brazo LEGO con control remoto por ESP32.

### 2.2 Objetivos específicos

1. Identificar y comparar los antecedentes de brazos robóticos educativos o de bajo costo con visión por computadora, IA y control remoto.
2. Exponer los fundamentos teóricos necesarios: conceptos de manipuladores, cinemática, control de motores, detección de objetos por color, calibración entre cámara y brazo, y comunicación inalámbrica.
3. Comparar las técnicas de IA y visión que reportan las fuentes (segmentación HSV con tablas, cinemática inversa, redes neuronales y detección con aprendizaje profundo) según precisión, costo, requisitos y limitaciones.
4. Describir el prototipo LEGO con control remoto por ESP32 como base experimental sobre la que se integrará la IA.
5. Proponer una arquitectura de integración de la IA con el prototipo y un plan de pruebas para evaluarla. *[Las pruebas de la IA sobre el brazo quedan como trabajo futuro.]*

### 2.3 Alcance

El estudio es principalmente documental. Incluye:

- La revisión de 31 trabajos distintos (32 archivos; la tesis de Aucapiña e Iza está cargada dos veces, como tesis y como diapositivas) sobre brazos con visión, IA, control remoto y robótica educativa, más la documentación oficial de Pybricks y proyectos en línea.
- La descripción del prototipo ya implementado: un brazo de cuatro motores con hub LEGO, controlado desde el celular mediante una página web servida por un ESP32 con su propia red Wi-Fi. El ESP32 envía cada orden al hub por Bluetooth (mensajes de difusión de Pybricks) y el hub mueve una sola articulación por orden. Esta parte se probó con el brazo real y se documenta en otra materia.
- Una propuesta de arquitectura de IA que se apoya en ese prototipo, sin implementarla ni evaluarla sobre el brazo.

Quedan fuera del alcance:

- La validación experimental de la IA sobre el brazo (tasa de éxito, precisión y efecto de la luz).
- La alimentación con batería, que cambiaría la restricción de mover un motor a la vez.
- La comparación experimental entre métodos: las comparaciones se hacen con los datos que reportan las fuentes, que usan hardware y condiciones distintas.

### 2.4 Limitaciones

- **Naturaleza documental.** Las cifras de las fuentes (precisión, latencia, errores) no son comparables entre sí, porque cada trabajo usó brazos, cámaras y condiciones de luz diferentes.
- **Lectura parcial de las fuentes.** Los datos salen de consultas a NotebookLM y no de una lectura completa de cada PDF. Ya se contrastaron los datos de latencia, retroalimentación, agarre, separación entre visión y control, alimentación y diseños abiertos; faltan por confirmar autores, revista, año y páginas de varias fuentes.
- **Sin fuente específica de Pybricks.** Ninguna fuente académica revisada trata Pybricks ni el hub Inventor 51515; esa parte se apoya en la documentación oficial del firmware.
- **Prototipo sin IA integrada.** El prototipo funciona con control manual desde el celular; no se midió su retraso y no hay canal de vuelta del hub al ESP32 (la página muestra el último ángulo *ordenado*, no el alcanzado por el motor). La única prueba con visión fue preliminar: con la cámara del celular y Pybricks se detectó la pelota roja sobre una base café, sin calibración ni integración.
- **Alimentación limitada.** El brazo funciona solo con alimentación USB, sin batería, por lo que se mueve un motor a la vez y se vigila el voltaje del hub, con una pausa si baja de 5500 mV.
- **Precisión de los motores.** Según observaciones previas del proyecto, al soltar los motores aparecen desvíos de pocos grados y holguras en los engranajes.
- **Montaje en desarrollo.** Faltan ajustes de la posición inicial y recalibrar los ángulos de algunos motores, que necesitan valores negativos.

### 2.5 Método de la revisión

Las fuentes se buscaron con una herramienta de búsqueda asistida por IA con filtro académico (Perplexity), se reunieron como PDF en un cuaderno de NotebookLM (y de Gemini, con las mismas fuentes, cuando se agotó el límite de consultas; lo que salió de Gemini se atribuyó por inferencia y queda marcado) y se consultaron por tema (latencia, retroalimentación, sensores de agarre, separación entre visión y control, alimentación y diseños abiertos), pidiendo siempre autor, año y sección. Las afirmaciones críticas del informe se contrastaron con esas respuestas; lo que no se pudo confirmar queda marcado como `[verificar]`, `[pendiente]` o "s. f.". No se hizo una revisión sistemática con criterios formales de inclusión, y la verificación contra el texto completo de cada PDF está en curso.

---

## 3. Justificación del proyecto

> Esta sección responde: ¿por qué se quiere hacer el estudio y para qué servirá? Los argumentos salen de la literatura revisada; los datos de la institución siguen como `[pendiente]` porque no están en ninguna fuente.

### 3.1 Importancia para la institución

Los brazos robóticos de bajo costo se justifican en la literatura porque acercan la práctica con hardware real a quienes no pueden pagar equipo industrial. Un brazo industrial supera habitualmente los 30 000 USD y los kits comerciales de robótica educativa suelen costar más de 1000 USD, lo que limita cuántas unidades puede comprar una institución (Markvicka et al., 2023). Además, los modelos físicos reales enfrentan al estudiante con fenómenos que la teoría abstracta no muestra, como la holgura de las articulaciones (Ntambara et al., 2026) y la fricción entre eslabones (Intisar et al., 2021; Eiammanussakul y Sangveraphunsiri, 2018) [verificar]. Que el aprendizaje activo con estos modelos sea más efectivo que los métodos pasivos no se pudo respaldar con las fuentes cargadas [cita pendiente: meta-análisis]; los estudios con LEGO y con brazos que aparecen en ellas reportan percepciones favorables y calificaciones sin diferencia significativa frente a tareas tradicionales (Markvicka et al., 2023 [verificar]). Este estudio reúne, en un solo documento, las técnicas de visión e IA que otros trabajos usan con equipo de ese tipo y propone cómo aplicarlas a un brazo armado con un kit LEGO, un ESP32 y un celular.

[pendiente: nombre de la institución, carrera y asignatura, y por qué el tema es relevante para ellas.]

### 3.2 Escenario del proyecto

El informe se desarrolla en una materia de carácter investigativo que requiere sustentar la implementación de IA [pendiente: institución y asignatura]. Como base experimental se usa un brazo armado con el kit LEGO Inventor 51515 y firmware Pybricks, conectado por USB a un cargador de corriente limitada y sin batería. El brazo ya se controla desde un celular, sin instalar aplicaciones, mediante una página servida por un ESP32 con su propia red Wi-Fi; este avance corresponde a otra materia. Esto permite operarlo a distancia, una necesidad que reporta la literatura: en la Universidad Politécnica Salesiana el aforo limitado por la pandemia obliga a recibir las prácticas con brazos KUKA de forma virtual, sin experimentar el control en persona (Llerena y Salazar, 2022, p. 4), y en el laboratorio de Mecatrónica de la ESPE el número limitado de módulos dificulta el aprendizaje (Aucapiña e Iza, 2019, p. 2).

**Tarea de referencia.** La tarea de ejemplo del informe es de recoger y colocar: el brazo toma una pelota roja apoyada sobre una base de color café y la deposita en un cubo que marca el destino [verificar la descripción del cubo y de la base]. Con la cámara del celular y Pybricks ya se probó, de forma preliminar, que la pelota roja se detecta sobre esa base, sin calibración. Es el mismo enfoque del proyecto de Pybricks (s. f.-a), que busca un objeto rojo con el celular como *smart sensor*. La literatura advierte que el rojo y los tonos café pueden confundirse en la segmentación por color (Lim et al., 2021; Rangarajan y Bianchini, 2026).

### 3.3 Impacto esperado y utilidad

Lo que se busca lograr con el informe y para qué servirá. Cada fila se apoya en lo que reportan las fuentes.

| Tipo de impacto | Qué se busca lograr |
| --------------- | ------------------- |
| Educativo | Ofrecer una revisión ordenada de visión por computadora e IA aplicada a brazos de bajo costo, útil para aprender estos temas con equipo disponible (Fernández Panadero et al., 2010; Markvicka et al., 2023). |
| Tecnológico | Proponer una arquitectura en la que un módulo de visión o IA externo envíe órdenes a un hub LEGO con Pybricks por la vía ya probada del ESP32 (Suhaeb y Risal, 2024; Tzompantzi Netzahual et al., 2019). |
| Científico | Sistematizar una combinación que no aparece en las fuentes revisadas (hub LEGO con Pybricks, página web servida por un ESP32 y módulo de visión o IA externo) y dejar definido un plan de pruebas para evaluarla. |
| Económico | Aprovechar equipo de bajo costo y reutilizable en lugar de comprar un brazo comercial (Markvicka et al., 2023). Los montajes con visión reportan unos 80 USD (Intisar et al., 2021), de 155 a 164 USD (Monroy Moya et al., 2026) y 2075 USD con un uArm Swift Pro (Aucapiña e Iza, 2019). *[Pendiente: sumar el costo real del montaje.]* |
| Social | Permitir la práctica a distancia cuando hay aforo limitado (Llerena y Salazar, 2022). |
| Ambiental | No hay base en las fuentes. Omitir salvo que el docente lo pida. |

---

## 4. Desarrollo del proyecto

### 4.1 Marco teórico

#### 4.1.1 Conceptos básicos de manipuladores

Un **robot manipulador** es, según la definición de la IFR y de la norma ISO que recogen Aucapiña e Iza (2019), una máquina automática, reprogramable y multifuncional con tres o más ejes, capaz de posicionar y orientar piezas, herramientas o dispositivos especiales. Un **brazo robótico** es una cadena de eslabones rígidos unidos por articulaciones, que mueve un elemento terminal (Llerena y Salazar, 2022).

Los **grados de libertad (GDL)** son el número de parámetros independientes que hacen falta para fijar la posición y la orientación de ese elemento terminal (Llerena y Salazar, 2022). Cada **articulación** une dos eslabones consecutivos y permite su movimiento relativo; pueden ser revolutas, que giran y se miden en grados, o prismáticas, que se desplazan en línea recta (Llerena y Salazar, 2022). El **actuador** es el componente que genera el movimiento: en brazos de bajo costo suelen ser servomotores controlados por pulsos PWM (Tzompantzi Netzahual et al., 2019; Aucapiña e Iza, 2019) o servos de bus que reciben comandos digitales (Llerena y Salazar, 2022). El **efector final** es la herramienta acoplada al extremo del brazo que interactúa con el entorno; en las tareas de recoger y colocar es una garra o pinza (Aucapiña e Iza, 2019).

En este trabajo el brazo tiene cuatro articulaciones motorizadas: base, codo y muñeca mueven el brazo, y la garra funciona como efector final.

#### 4.1.2 Plataforma LEGO Inventor 51515 y firmware Pybricks

El hub LEGO Inventor 51515 puede funcionar con Pybricks, un firmware alternativo que se programa en MicroPython (Pybricks, s. f.-b). Cada motor del kit incluye un sensor de rotación, por lo que el programa puede pedir un ángulo absoluto con `run_target` o hacer que el motor siga un objetivo cambiante con `track_target` (Pybricks, s. f.-c).

Pybricks también permite que un hub reciba mensajes de otro dispositivo por Bluetooth sin establecer una conexión: el emisor difunde (*broadcast*) un mensaje con un canal, y el hub lo lee con `observe` (Pybricks, s. f.-d). Según una medición con sniffer hecha con un City Hub y el firmware 4.1.0b2 (no con el hub Inventor 51515), este modo permite del orden de 10 actualizaciones por segundo y observa peor cuando el hub está conectado a una computadora (Pybricks, s. f.-e). Esta es la vía que usa el prototipo para recibir las órdenes del ESP32. La función *smart sensors*, en versión beta, permite además usar la cámara de un celular como sensor del hub (Pybricks, s. f.-b).

#### 4.1.3 Cinemática del brazo

La cinemática estudia el movimiento del manipulador sin considerar las fuerzas que lo producen (Llerena y Salazar, 2022). La **cinemática directa** calcula la posición del efector final a partir de los ángulos de las articulaciones y las longitudes de los eslabones, usualmente con matrices de transformación homogénea. La **cinemática inversa** hace el camino contrario: dada la posición que se quiere alcanzar, determina los ángulos que debe tomar cada articulación (Llerena y Salazar, 2022; Markvicka et al., 2023).

El método más reportado para brazos de 3 a 5 GDL es el **geométrico** (Mohammed et al., 2023; Monroy Moya et al., 2024; Intisar et al., 2021). Para un objetivo en $(P_x, P_y)$ del plano de la mesa, el ángulo de la base se obtiene con:

$$\theta_1 = \arctan\left(\frac{P_y}{P_x}\right)$$

y el ángulo del codo, aplicando la ley de cosenos sobre el triángulo que forman los eslabones $a_2$ y $a_3$ y la distancia $N$ entre hombro y muñeca:

$$\theta_3 = \pm \cos^{-1}\left(\frac{N^2 - a_2^2 - a_3^2}{2\,a_2 a_3}\right)$$

(Mohammed et al., 2023). El doble signo corresponde a las dos configuraciones posibles, "codo arriba" y "codo abajo". Para trayectorias continuas se usa además el método diferencial con la matriz Jacobiana, que relaciona las velocidades articulares con las del efector final (Llerena y Salazar, 2022).

Una alternativa que reportan las fuentes es entrenar una red neuronal con datos de calibración para que prediga los ángulos directamente a partir de las coordenadas de la imagen, sin resolver ecuaciones (Mada Sanjaya et al., 2018). Esta idea se retoma en la sección 4.1.7.

#### 4.1.4 Control de posición de motores

En los servomotores económicos, el ángulo se fija con el ancho de un pulso PWM (Tzompantzi Netzahual et al., 2019; Llerena y Salazar, 2022). En un esquema de lazo cerrado, el controlador resta la posición medida de la deseada y corrige según ese error (Eiammanussakul y Sangveraphunsiri, 2018). Un controlador **PD** combina una corrección proporcional al error con otra proporcional a su velocidad de cambio (Yilmaz et al., 2025); el **PID** agrega un término integral que elimina el error que persiste [cita pendiente]. Capaldi (2024) usa el ajuste de las ganancias Kp, Ki y Kd de un brazo con peso, con una interfaz que grafica la respuesta, como actividad educativa para observar el tiempo de levantamiento, el sobreimpulso y el error en estado estacionario. En sistemas articulados más complejos se anidan varios lazos de posición, torque y velocidad (Eiammanussakul y Sangveraphunsiri, 2018). Cuando el encoder está en el eje del motor y hay una reductora, el ángulo de la articulación es la lectura del encoder dividida entre la relación de transmisión (Eiammanussakul y Sangveraphunsiri, 2018).

Las fuentes reportan problemas típicos y sus soluciones (Tabla 2). Con los motores del kit LEGO el control de posición lo resuelve el propio firmware (Pybricks, s. f.-c), por lo que la limitación relevante en el prototipo es de alimentación y no de lazo de control.

**Tabla 2**

*Problemas de control de posición en brazos de bajo costo y soluciones reportadas*

| Problema | Causa reportada | Solución reportada |
| -------- | --------------- | ------------------ |
| Vibración de los servos | Conflicto entre la librería de servos y la de comunicación serie en el microcontrolador (Lim et al., 2021). | Programar el movimiento por tiempo de pulso sin depender de interrupciones de software serie (Lim et al., 2021). |
| Deriva y descalibración | Errores de posición acumulados (Yilmaz et al., 2025). | Un giroscopio y acelerómetro en el extremo del brazo para detectar desviaciones y recalibrar el origen (Yilmaz et al., 2025). |
| Movimientos bruscos | Cambios repentinos entre posiciones (Llerena y Salazar, 2022; Monroy Moya et al., 2024). | Perfiles de velocidad trapezoidales con puntos intermedios (Monroy Moya et al., 2024). |
| Error por fricción y gravedad | La articulación no vuelve a cero exacto por la fricción y el peso del brazo (Eiammanussakul y Sangveraphunsiri, 2018). | Minimizar la fricción y compensar la gravedad en el controlador (Eiammanussakul y Sangveraphunsiri, 2018). |
| Inestabilidad eléctrica | Alimentar servos de alto consumo desde los pines de la tarjeta (Llerena y Salazar, 2022). | Un convertidor DC-DC regulable entre la fuente externa y los servos (Llerena y Salazar, 2022). |

*Nota.* Elaboración propia a partir de las fuentes citadas.

**Límites de alimentación.** Varias fuentes tratan la corriente disponible como una restricción de diseño. Ntambara et al. (2026) alimentaron un brazo con motores a pasos desde una fuente de 12 V y 2 A, limitaron la corriente de los controladores y activaron las articulaciones de forma secuencial, con un pico de 1,92 A y una caída de voltaje de 0,46 V. Yilmaz et al. (2025) aislaron la alimentación de los servos con relés y optoacopladores, midieron la corriente con un sensor ACS712, agregaron un fusible de 4,2 A y limitaron la velocidad por firmware. Lim et al. (2021) reportan caídas bruscas de voltaje y vibración al accionar varios servos con las librerías estándar. El prototipo de este trabajo aplica una idea parecida a la de Ntambara et al. (2026): un motor por orden y vigilancia del voltaje. Ninguna de las fuentes revisadas mide cuánto alarga el tiempo de ciclo el movimiento secuencial frente al simultáneo; Ntambara et al. (2026) no hicieron esa comparación.

#### 4.1.5 Detección de objetos por color

El flujo que describen las fuentes tiene cuatro pasos. Primero, la imagen se convierte de RGB a **HSV**, porque en RGB la luz afecta a los tres canales a la vez, mientras que HSV separa el tono (H), la pureza del color (S) y el brillo (V), lo que hace la selección de color menos sensible a las variaciones moderadas de luz (Anusha et al., 2018; Mohammed et al., 2023; Intisar et al., 2021). Segundo, la **umbralización** define un rango inferior y superior de H, S y V para cada color: los píxeles dentro del rango pasan a 1 y el resto a 0, y los umbrales pueden fijarse a mano con controles deslizantes o calcularse a partir de la luz medida (Llerena y Salazar, 2022; Mohammed et al., 2023). Tercero, la **segmentación** limpia la máscara con erosión, dilatación y filtros de suavizado, y descarta regiones menores que un tamaño mínimo (Mada Sanjaya et al., 2018; Mohammed et al., 2023; Anusha et al., 2018). Cuarto, se extraen los **contornos** y se calcula el **centroide** de cada región, con momentos de imagen o promediando los píxeles (Anusha et al., 2018; Mohammed et al., 2023; Medel et al., s. f.).

Las fuentes reportan cinco problemas frecuentes: la variación de la iluminación y las sombras, que descalibra los umbrales (Monroy Moya et al., 2024; Intisar et al., 2021; Llerena y Salazar, 2022); los brillos sobre superficies reflectantes, que blanquean los píxeles (Aucapiña e Iza, 2019; Rangarajan y Bianchini, 2026); la confusión entre colores cercanos, como rojo con naranja o con tonos café (Lim et al., 2021; Rangarajan y Bianchini, 2026); el bajo contraste con el fondo, que impide cerrar el contorno (Monroy Moya et al., 2024); y los objetos muy próximos, que se unen en un solo contorno y dan un centroide erróneo (Intisar et al., 2021).

#### 4.1.6 Calibración entre la cámara y el brazo

Un píxel de la imagen no basta para ubicar el objeto en el espacio: define un rayo desde la cámara. Cuando los objetos reposan en una mesa plana, se intersecta ese rayo con el plano de trabajo, que se define con un marcador de referencia (ArUco), y se transforma el resultado al sistema de coordenadas del robot (Rangarajan y Bianchini, 2026). Una forma más sencilla es la **homografía**, una matriz de 3×3 que relaciona directamente los puntos de la imagen con los del plano real y se calcula a partir de pares de puntos conocidos (Anusha et al., 2018; Aucapiña e Iza, 2019). Con una cámara cenital fija se puede usar incluso un factor de escala entre una medida real conocida y su tamaño en píxeles (Aucapiña e Iza, 2019; Intisar et al., 2021).

Cuando la cámara va montada sobre el brazo o se mueve respecto a él, se recurre a la **calibración ojo-mano**, que resuelve ecuaciones del tipo $AX = ZB$ entre las transformaciones que observa la cámara y la pose del efector final (Enebuse et al., 2021; Tabb y Ahmad Yousef, 2017). Otra opción es construir empíricamente una **tabla de calibración** que asocia coordenadas de la imagen con los ángulos medidos de los servos al alcanzar cada punto, y entrenar con ella una red neuronal (Mada Sanjaya et al., 2018). Un método de tablas con interpolación lineal, sin red neuronal ni modelo geométrico, es una de las opciones que se propone para este proyecto (sección 4.3); no se encontró tal cual en las fuentes revisadas, y el antecedente más cercano es la tabla de Mada Sanjaya et al. (2018). Una búsqueda adicional en la web tampoco halló un trabajo que use una tabla con interpolación lineal de píxeles a ángulos; los más cercanos mapean la imagen a un plano de trabajo calibrado y luego resuelven la cinemática inversa [cita pendiente: no se identificó una fuente verificable].

#### 4.1.7 Inteligencia artificial en el control de brazos

Aquí se entiende por **inteligencia artificial** el conjunto de técnicas que permiten a un programa hacer tareas que normalmente requieren criterio humano, como reconocer objetos; el **aprendizaje automático** es la parte de la IA en que el programa ajusta sus parámetros a partir de ejemplos, en lugar de seguir reglas escritas a mano; una **red neuronal** es un modelo de aprendizaje automático formado por capas de unidades que combinan sus entradas con pesos ajustables; y la **detección de objetos** es la tarea de ubicar en una imagen cada objeto de interés y asignarle una clase [cita pendiente: las fuentes cargadas traen definiciones parciales de aprendizaje automático, red neuronal y detección de objetos, pero sin autor identificado, y ninguna de IA; buscar una fuente externa].

Las fuentes muestran tres niveles de uso de la IA. **Visión clásica** (HSV, umbral y centroide), sin entrenamiento, que es la base de la mayoría de los trabajos (sección 4.1.5). **Redes neuronales para la cinemática inversa**: Mada Sanjaya et al. (2018) entrenaron una red con una capa oculta de 20 neuronas que recibe las coordenadas $(x, y)$ de la imagen y entrega los ángulos de cinco servos, con un error de 1,3 % entre los datos de calibración y la salida de la red. **Aprendizaje profundo para detectar y clasificar**: Aucapiña e Iza (2019) clasificaron piezas con un modelo MobileNet de TensorFlow (97,28 % en identificación y 38 a 50 ms de inferencia), y Rangarajan y Bianchini (2026) usaron YOLO11n-OBB para detectar la posición y el ángulo de un bolígrafo, con 89,8 % de éxito en la tarea completa. Dang et al. (2026) ejecutan YOLOv12 en una laptop solo con CPU, sin GPU, aunque no reportan el tiempo de inferencia; Capaldi (2024) midió la inferencia de YOLOv8 en tres equipos: 62,8 ms en una CPU AMD Ryzen 9 5950X, 52,1 ms en un Apple M2 y 8,41 ms en una GPU NVIDIA Quadro P2200 [verificar el tamaño del modelo YOLOv8 usado].

La Tabla 3 resume esas opciones.

**Tabla 3**

*Técnicas de visión e IA reportadas para guiar un brazo de bajo costo*

| Técnica | Qué necesita | Resultado reportado | Limitación reportada |
| ------- | ------------ | ------------------- | -------------------- |
| HSV, umbral y centroide, con cinemática inversa (Intisar et al., 2021; Mohammed et al., 2023) | Cámara, PC o Raspberry Pi, medidas del brazo | 94,6 % de acierto por forma; 93,83 % entre 5 y 7000 lux | Sensible a sombras y a colores parecidos |
| HSV con red neuronal para cinemática inversa (Mada Sanjaya et al., 2018) | Tabla de calibración y entrenamiento | 1,3 % de error entre calibración y salida | Hay que rehacer la tabla si cambia el montaje |
| Detección con aprendizaje profundo (Aucapiña e Iza, 2019; Rangarajan y Bianchini, 2026; Capaldi, 2024; Dang et al., 2026) | Conjunto de imágenes y entrenamiento; equipo con más capacidad (Dang et al. usan solo CPU) | 97,28 % de identificación (Aucapiña e Iza); 89,8 % de éxito total (Rangarajan y Bianchini); inferencia de YOLOv8 de 8,41 a 62,8 ms según el equipo (Capaldi) | Más datos y cómputo; sensible al deslumbramiento y a la deriva de calibración; Dang et al. no reportan métricas cuantitativas |

*Nota.* Los resultados provienen de montajes y condiciones distintas, por lo que no son comparables de forma directa.

#### 4.1.8 Comunicación inalámbrica con ESP32

El ESP32 es un sistema en chip de doble núcleo (160 a 240 MHz) que integra Wi-Fi 802.11 b/g/n y Bluetooth con BLE (Tzompantzi Netzahual et al., 2019). Puede crear su propia red Wi-Fi (modo punto de acceso), repartir direcciones en el rango 192.168.4.x y servir una interfaz web en el puerto 80 a la que el celular accede con un navegador, enviando peticiones HTTP que el ESP32 traduce en órdenes para el brazo (Tzompantzi Netzahual et al., 2019; Suhaeb y Risal, 2024). Suhaeb y Risal (2024) midieron entre 85 y 92 ms de respuesta para los botones de control y una reconexión automática en menos de 5 s. Tzompantzi Netzahual et al. (2019) midieron con Wireshark, desde un navegador, tiempos de respuesta HTTP de unos 50 a 60 ms a distancias de 1 a 40 m (sin indicar el número de repeticiones), y reportaron que si se envían instrucciones de forma simultánea la conexión se pierde unos 3 s y la aplicación muestra un aviso. Kumar et al. (2026), con un vehículo controlado por Wi-Fi, reportan una latencia de ida y vuelta de 38, 62 y unos 120 ms con señal fuerte, moderada y débil; es evidencia complementaria (revista de menor nivel y no es un brazo). Shah y Arockia Doss (2026) reportan menos de 150 ms entre la orden en la interfaz web y la actuación de los servos, con WebSockets sobre Wi-Fi, sin precisar cómo se midió. Capaldi (2024), con ESP-NOW (no Wi-Fi ni BLE) entre una PC y un hub VEX V5, midió 187 ms de ida y vuelta (desviación estándar de 57 ms), que incluye el tránsito por USB, los dos ESP32, la conversión a RS-485 y el procesamiento del hub, y una pérdida de paquetes menor a 1 % de 0 a 40 m y de 13,2 % a 60 m; recomienda 40 m o menos para control en lazo cerrado. Estas cifras usan métodos distintos y no son comparables entre sí.

El **BLE** fue diseñado para consumir menos energía que el Bluetooth clásico (Tzompantzi Netzahual et al., 2019). En su uso habitual, un dispositivo anuncia un servicio y otro se conecta a él; el modo de **difusión** (*broadcast*) no requiere conexión y es el que usa Pybricks para enviar mensajes al hub (Pybricks, s. f.-d). Tzompantzi Netzahual et al. (2019) evaluaron BLE solo con la intensidad de señal (RSSI) de las balizas del ESP32: promedio de -47,8 dBm a 1 m y de -88,7 dBm a unos 40 m. Afirman que ambas tecnologías responden en tiempo real a menos de 40 m, pero sin cifras de latencia para BLE; los tiempos de 50 a 60 ms corresponden solo a Wi-Fi. Ninguna de las fuentes revisadas mide la latencia de BLE, ni en modo de difusión ni con conexión, por lo que el retraso del enlace del prototipo debe medirse (sección 4.3). Fuera de las fuentes cargadas, la latencia de BLE sin conexión depende del intervalo de anuncio, del ciclo de escaneo del receptor y de un retardo aleatorio de 0 a 10 ms entre anuncios (Cho et al., 2014 [verificar]; [cita pendiente: documentación de Espressif]). La única cifra con ESP32 que se encontró (44 y 85 ms) corresponde a un ESP32 que recibe anuncios y los publica por un protocolo de mensajería (MQTT): es una latencia de sistema y en sentido contrario al de este prototipo, por lo que no se toma como referencia (Vieira y Rizzetti, 2025 [verificar]).

#### 4.1.9 Separación entre la visión y el control de los motores

En los trabajos revisados que usan una cámara, la imagen casi siempre se procesa en un equipo y los motores los mueve un microcontrolador distinto, al que se envían los ángulos (Tabla 4). Monroy Moya et al. (2024) son la excepción: concentran visión y control en una sola Raspberry Pi 4 para evitar latencias. En el resto el enlace es por cable (USB o serie), con tres excepciones inalámbricas: Aucapiña e Iza (2019) mencionan además Bluetooth para el uArm, Dang et al. (2026) ofrecen MQTT sobre Wi-Fi en su interfaz web (la ruta de visión sería por USB [verificar]) y Capaldi (2024) usa ESP-NOW entre la PC y el robot. Este proyecto mantendría la separación con un enlace inalámbrico, como Capaldi (2024), pero por Wi-Fi hasta el ESP32 y BLE de difusión hasta el hub: el módulo de visión enviaría las órdenes al ESP32 por Wi-Fi, que es la vía ya funcional del prototipo.

**Tabla 4**

*Separación entre el equipo de visión y el control de motores en trabajos con brazo*

| Trabajo | Equipo de visión | Control de motores | Enlace |
| ------- | ---------------- | ------------------ | ------ |
| Mohammed et al. (2023) | Raspberry Pi con webcam USB (OpenCV) | Arduino (cinemática inversa, 5 servos) | Serie UART |
| Intisar et al. (2021) | PC con webcam (OpenCV) | Arduino Uno (4 servos) | USB (serie) |
| Mada Sanjaya et al. (2018) | PC (Python y OpenCV) | Arduino (5 servos) | Puerto serie |
| Aucapiña e Iza (2019) | Computadora portátil (Qt, OpenCV, TensorFlow) | Placa del uArm Swift Pro (tipo Arduino Mega) y Arduino Uno para la pinza | Serie RS-232/USB y Bluetooth |
| Markvicka et al. (2023) | Laptop (MATLAB, Python o C++) | ATmega328 con servocontrolador PCA9685 | USB (serie) |
| Monroy Moya et al. (2024) | Raspberry Pi 4 | La misma Raspberry Pi 4 | Interno |
| Dang et al. (2026) | Laptop solo con CPU (YOLOv12) | ESP32 con PCA9685 y servos MG996R | USB en la ruta de visión [verificar]; MQTT por Wi-Fi en la interfaz web |
| Capaldi (2024) | PC (YOLOv8) con cámara OpenMV H7 por USB | ESP32 como puente y hub VEX V5 | USB serie a un ESP32, ESP-NOW al ESP32 del robot y RS-485 al VEX V5 |
| Este proyecto (propuesta) | PC con cámara USB (OpenCV) | ESP32 y hub LEGO 51515 | Wi-Fi (HTTP) al ESP32 y BLE de difusión al hub |

*Nota.* Elaboración propia a partir de las fuentes citadas. La última fila es una propuesta, no un trabajo implementado.

### 4.2 Prototipo base: control remoto con ESP32

El prototipo se compone de cuatro etapas (Figura 1): el celular se conecta por Wi-Fi a la red propia del ESP32; el ESP32 sirve una página con botones de articulación (ninguna, F base, D codo, A muñeca, B garra), un control deslizante de ángulo y un botón de accionar; el ESP32 emite cada orden por Bluetooth como la tupla `(articulación, ángulo, id_orden)` en el canal 1; y el hub, en modo remoto, mueve una sola articulación por cada orden nueva.

*Figura 1.* Arquitectura del prototipo base.

```
celular --Wi-Fi--> ESP32 (página web) --BLE broadcast--> hub 51515 --> motores
```

Para cuidar la alimentación USB limitada, el hub conserva las restricciones del programa original: un solo motor energizado a la vez, motor suelto al llegar, vigilancia del voltaje con pausa si baja de 5500 mV y límites de ángulo por articulación aplicados en el hub y no en la página. Las órdenes que llegan mientras el brazo se mueve se descartan, y sin señal del ESP32 no se mueve nada. El ESP32 recuerda el último ángulo ordenado de cada articulación y lo muestra en la página. El prototipo se probó con el brazo real: la interfaz y el botón de accionar funcionan desde el celular y el brazo se mueve. El retraso se describe como mínimo, pero no se midió con cifras.

### 4.3 Propuesta de integración de IA con el prototipo

**Idea central.** El hub no tiene capacidad para ejecutar visión por computadora ni redes neuronales (por eso otros proyectos con LEGO la delegan a un equipo externo, Autor [pendiente], s. f.). La propuesta es mantener el prototipo como está y añadir un módulo externo de visión e IA que haga el papel del operador humano: en lugar de que una persona elija la articulación y el ángulo en la página, un programa los calcula a partir de la imagen y los envía por la misma vía.

**Arquitectura propuesta (Figura 2).**

*Figura 2.* Arquitectura propuesta con IA.

```
cámara USB --> módulo de visión/IA (PC) --Wi-Fi (HTTP)--> ESP32 --BLE broadcast--> hub --> motores
```

1. **Cámara y módulo de IA.** Una cámara USB conectada a una PC captura la escena y un programa en Python con OpenCV detecta la pelota y el cubo (visión clásica HSV) y calcula su posición en la imagen. En una etapa posterior, un detector de aprendizaje profundo puede reemplazar o complementar la segmentación (Tabla 3). El celular se conserva como interfaz de control manual; no se propone usar su cámara ni la función *smart sensors*.
2. **De la imagen a los ángulos.** La posición se convierte en ángulos de articulación con una de tres opciones: tablas de calibración con interpolación lineal (la opción más simple; no hay un antecedente exacto en las fuentes), cinemática inversa geométrica (sección 4.1.3) o una red neuronal entrenada con la tabla de calibración (Mada Sanjaya et al., 2018).
3. **Envío de órdenes.** El módulo se conecta a la red Wi-Fi del ESP32 y usa las mismas rutas de la página (una para fijar el ángulo y otra para accionar), de modo que el hub no necesita cambios. A diferencia de la mayoría de los antecedentes de la Tabla 4, que unen la PC con el microcontrolador por cable, aquí el enlace es inalámbrico, como en Capaldi (2024).
4. **Secuencia de la tarea.** Como el hub mueve una articulación por orden y descarta las que llegan durante un movimiento, el módulo debe enviar las órdenes en secuencia y esperar a que cada movimiento termine (garra abre, base, codo, muñeca, garra cierra, retirada, traslado al cubo, garra abre, regreso a cero).

**Restricciones que impone el prototipo y que el diseño debe respetar.**

- No hay canal de vuelta del hub al ESP32: el módulo de IA no sabe cuándo terminó un movimiento ni dónde quedó el motor. Se propone esperar un tiempo fijo calculado con la velocidad del motor (200 °/s) o añadir un canal de vuelta como trabajo futuro. Otras fuentes sí lo implementan: Suhaeb y Risal (2024) consultan al ESP32 cada segundo y reciben el estado en JSON; Aucapiña e Iza (2019) reciben por serie las coordenadas y el estado de la pinza, con una respuesta de confirmación a cada orden; Yilmaz et al. (2025) usan un sensor inercial y finales de carrera; y Llerena y Salazar (2022) usan servos de bus que informan ángulo, voltaje y temperatura; Capaldi (2024) devuelve a la PC lecturas del ángulo del brazo, 20 por segundo, por el mismo enlace ESP-NOW. Ninguna de esas soluciones se aplica tal cual al hub, que solo recibe.
- En la medición con sniffer, hecha con un City Hub y no con el 51515, la emisión BLE permitió del orden de 10 mensajes por segundo (Pybricks, s. f.-e); se toma como referencia y debe medirse en el prototipo. Es suficiente para órdenes puntuales y no para seguir un objetivo en tiempo real.
- La alimentación USB limitada obliga a mover un motor a la vez, como en Ntambara et al. (2026), que activan las articulaciones de forma secuencial por el límite de su fuente de 12 V y 2 A. El movimiento será secuencial y probablemente más lento que con alimentación propia, aunque ninguna fuente revisada mide ese efecto sobre el tiempo de ciclo. [pendiente: confirmar en el video del proyecto de Pybricks (s. f.-a) si los motores se mueven a la vez y con qué alimentación; la página no lo indica].
- Ante la pérdida del enlace, el prototipo ya no mueve nada sin señal del ESP32; otros trabajos también fuerzan la parada de los motores cuando no llegan paquetes durante cierto tiempo (Zuiev et al., 2024).

**Plan de pruebas propuesto (trabajo futuro).** Medir el retraso entre la orden y el movimiento; medir la tasa de éxito de la toma y el depósito en un número fijo de repeticiones; y repetir bajo al menos dos condiciones de iluminación, ya que es la limitación más reportada (Monroy Moya et al., 2024; Mohammed et al., 2023).

### 4.4 Pruebas y resultados

El prototipo base funciona como se describe en la sección 4.2. La integración con IA está planteada como propuesta y no se evaluó sobre el brazo; sus pruebas quedan definidas en la sección 4.3. La única prueba con visión fue preliminar: con la cámara del celular y Pybricks se comprobó que la pelota roja se detecta sobre una base café; no se calibró ni se integró con el brazo. [pendiente: si se hace una prueba de concepto del módulo de visión, añadir aquí sus resultados.]

---

## 5. Conclusiones y recomendaciones

### 5.1 Conclusiones

1. **Antecedentes.** La literatura revisada muestra que los brazos de bajo costo con visión suelen segmentar por color en HSV y convertir la posición del objeto en ángulos con cinemática inversa, tablas o una red neuronal, con tasas de acierto reportadas de 84 % (confiabilidad global) a 97,28 % (identificación de piezas), según el trabajo y la métrica, que no son comparables entre sí (Aucapiña e Iza, 2019; Rangarajan y Bianchini, 2026; Mohammed et al., 2023; Intisar et al., 2021). El control remoto con ESP32 se ha hecho casi siempre sin cámara (Tzompantzi Netzahual et al., 2019; Suhaeb y Risal, 2024; Yilmaz et al., 2025), y solo Dang et al. (2026) y Capaldi (2024) lo combinan con visión de aprendizaje profundo en una PC en plataformas educativas. Ya existen proyectos LEGO con cámara y proyectos abiertos con un ESP32 como puente hacia un hub Pybricks (Pybricks, s. f.-a; LEGO Ideas, s. f.; Johnson, 2026), pero ni en la literatura académica revisada ni en esos proyectos aparece la combinación completa de brazo con hub LEGO y Pybricks, página web servida por un ESP32 y un módulo de visión externo; esa es la brecha que este trabajo atiende, con la cautela de que la búsqueda no fue sistemática.
2. **Fundamentos.** Integrar visión y brazo exige tres piezas teóricas que las fuentes cubren bien: detectar el objeto (HSV, umbral y centroide), pasar de la imagen a la posición del brazo (homografía, calibración ojo-mano, tablas o red neuronal) y resolver los ángulos (cinemática inversa geométrica o aprendida). El control de posición de los motores del kit LEGO lo resuelve el firmware, por lo que el límite del prototipo es la alimentación y no el lazo de control.
3. **Comparación de técnicas.** Para objetos de color definido y luz controlada, la visión clásica con HSV alcanza aciertos del orden de 94 % en los trabajos revisados (Intisar et al., 2021; Mohammed et al., 2023) y no necesita entrenamiento; esas cifras no son comparables de forma directa con las de las técnicas más pesadas (Tabla 3). La IA aporta robustez ante formas irregulares y permite resolver la orientación (Rangarajan y Bianchini, 2026), pero exige datos, entrenamiento y más cómputo, aunque Dang et al. (2026) la ejecutan solo con CPU y Capaldi (2024) midió de 52,1 a 62,8 ms de inferencia en CPU. Las fuentes coinciden en que la iluminación, la calibración y la carga útil son las limitaciones comunes.
4. **Prototipo base.** El control remoto desde el celular con ESP32 funciona con el brazo real y respeta las restricciones de alimentación. Sus límites son que no hay canal de vuelta del hub, que el retraso no se midió y que solo se mueve una articulación por orden.
5. **Propuesta.** Un módulo externo de visión e IA, ubicado en una PC con cámara USB, que envíe órdenes por las rutas web del ESP32 es una forma viable, por diseño, de integrar IA sin modificar el hub. Esta conclusión es de diseño: no se validó sobre el brazo, aunque la separación entre una PC con visión y un ESP32 inalámbrico tiene antecedentes con mediciones de enlace (Capaldi, 2024) y con validación cualitativa (Dang et al., 2026).

### 5.2 Limitaciones y trabajo futuro que reporta la literatura

La Tabla 5 resume lo que los trabajos revisados señalan como limitación y como línea futura, agrupado en las categorías que más se repiten.

**Tabla 5**

*Limitaciones y trabajo futuro reportados en la literatura*

| Categoría | Limitación frecuente | Trabajo futuro reportado |
| --------- | -------------------- | ------------------------ |
| Precisión | El detector de bordes falla con piezas irregulares o reflectantes (Monroy Moya et al., 2024); agarres que resbalan (Rangarajan y Bianchini, 2026); el brazo sigue la rutina aunque el objeto se caiga (Intisar et al., 2021 [verificar]). | Detectores de aprendizaje profundo (Monroy Moya et al., 2024); control visual continuo (Rangarajan y Bianchini, 2026); sensores de presencia o de fuerza en la pinza (Oliveira et al., 2021; Rangarajan y Bianchini, 2026). |
| Velocidad | Ciclo de 27 s por objeto, lento para producción (Mohammed et al., 2023). | Cámaras con mayor resolución y tasa de cuadros (Medel et al., s. f.); control adaptativo de velocidad (Yilmaz et al., 2025). |
| Costo | Los servos de bajo costo limitan la carga útil (Markvicka et al., 2023). | Diseños modulares y abiertos de bajo costo, como un brazo de 4 GDL con piezas cortadas con láser y controlador Arduino abierto (Narmadha et al., 2022) o un kit abierto de menos de 200 USD (Markvicka et al., 2023). |
| Iluminación | Sombras, parpadeo y brillos descalibran la segmentación (Intisar et al., 2021; Llerena y Salazar, 2022; Rangarajan y Bianchini, 2026). | Ajuste automático de umbrales (Medel et al., s. f.); redes convolucionales más robustas a la luz (Monroy Moya et al., 2024). |
| Calibración | Deriva de hasta 8 mm entre sesiones al mover cámara o base (Rangarajan y Bianchini, 2026); holgura y desgaste de engranajes (Mohammed et al., 2023). | Reestimar los marcadores cuadro a cuadro (Rangarajan y Bianchini, 2026); calibración continua en línea (Enebuse et al., 2021). |
| Uso educativo | Falta de programación previa en los estudiantes (Markvicka et al., 2023). | Módulos de aprendizaje asincrónico y coordinación entre teoría y taller (Markvicka et al., 2023; Fernández Panadero et al., 2010). |

*Nota.* Elaboración propia a partir de las fuentes citadas. Verificar contra los trabajos completos.

### 5.3 Recomendaciones

1. **Empezar por la visión clásica.** Implementar primero la detección HSV de la pelota y el cubo con un marcador de referencia para calibrar, y evaluar después un detector de aprendizaje profundo (Rangarajan y Bianchini, 2026; Monroy Moya et al., 2024).
2. **Controlar la luz y recalibrar.** Usar iluminación constante y repetir la calibración cuando se mueva la cámara o la base, porque son las fuentes de error más reportadas.
3. **Medir antes de afirmar.** Medir el retraso entre la orden y el movimiento, y la tasa de éxito en un número fijo de repeticiones, para tener cifras propias comparables con las de la literatura.
4. **Cerrar el lazo.** Añadir un canal de vuelta del hub al ESP32 para que el módulo de IA sepa cuándo terminó cada movimiento y dónde quedó el motor. Hay antecedentes con confirmaciones de estado por serie, por consulta periódica o por el mismo enlace inalámbrico (Aucapiña e Iza, 2019; Suhaeb y Risal, 2024; Capaldi, 2024).
5. **Seguridad.** Agregar un botón de parada en la página (como en Yilmaz et al., 2025) y definir qué hace el hub ante voltaje bajo cuando no hay computadora conectada.
6. **Verificar el agarre.** Considerar un sensor que confirme que la garra sujetó el objeto antes de continuar la secuencia, por ejemplo con un sensor infrarrojo de presencia en la pinza como el de Monroy Moya et al. (2024) o con los sensores de fuerza que revisan Oliveira et al. (2021).

---

## 6. Referencias bibliográficas e internet

> Formato APA 7. Los datos de revista, volumen, páginas y DOI vienen de la lista que generó NotebookLM y no se han verificado en los PDF; las entradas con [verificar] tienen dudas conocidas. Solo se listan las fuentes citadas. La definición de la IFR (2016) y de la ISO (2012) se cita a través de Aucapiña e Iza (2019), por lo que no se listan por separado.

Anton's Mindstorms. (2025). *HuskyLens + SPIKE Prime blocks* [Entrada de blog; verificar título y autor]. https://www.antonsmindstorms.com/2025/07/26/huskylens-spike-prime-blocks/

Anusha, G., Ganavi, D., Revathi, H., Sahana, P., Sreenivas Rao, M. V., y Basavanna, M. (2018). Robotic arm manipulation using shape and color based on visual servoing. *International Journal of Scientific Research in Computer Science, Engineering and Information Technology, 4*(6), 733-739.

Aucapiña Garnica, N. F., e Iza Guanochanga, B. I. (2019). *Diseño e implementación de un sistema de visión artificial para la manipulación, ensamblaje y control de calidad de piezas a través del uso de un brazo robótico para el laboratorio de mecatrónica* [Tesis de grado, Universidad de las Fuerzas Armadas ESPE]. [enlace pendiente]

[Autor pendiente]. (s. f.). *LEGO con Raspberry Pi y OpenCV* [Proyecto]. Tampere University. https://joedavid-tuni.github.io/MR3/

[Autores pendientes]. (2026). Low cost single camera robotic arm for vision guided pick and place. *Journal of Robotics and Control (JRC)*. https://journal.umy.ac.id/index.php/jrc/article/view/28524

Capaldi, E. I. (2024). A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol. *PeerJ Computer Science, 10*, Artículo e1826. https://doi.org/10.7717/peerj-cs.1826 [verificar revista, volumen y DOI: vienen de Perplexity]

Cho, K., [demás autores pendientes]. (2014). [título pendiente: análisis de la latencia de descubrimiento en BLE]. *Sensors, 15*(1). https://doi.org/10.3390/s150100059 [verificar]

Dang, P. T., Van, T. N. H., Nguyen, N. T., Nguyen, V. D. H., Tran, Q. T., Huynh, N. D., Phi, T. D., Vo, C. H., y Vo, D. C. (2026). Development of an educational robotic platform with dual control interfaces and intelligent computer vision-based interaction. *FME Transactions, 54*, 93-106. https://doi.org/10.5937/fme2601093P [verificar número y forma de los apellidos y nombres]

Eiammanussakul, T., y Sangveraphunsiri, V. (2018). A lower limb rehabilitation robot in sitting position with a review of training activities. *Journal of Healthcare Engineering, 2018*, 1-14.

Enebuse, I., Foo, M., Kader Ibrahim, B. K. S. M., Ahmed, H., Supmak, F., y Eyobu, O. S. (2021). A comparative review of hand-eye calibration techniques for vision guided robots. *IEEE Access, 9*, 113143-113154. https://doi.org/10.1109/ACCESS.2021.3104514

Fernández Panadero, C., Villena Román, J., y Delgado Kloos, C. (2010). Impact of learning experiences using LEGO Mindstorms in engineering courses. [revista o actas pendientes].

GC-TO. (2026). *WRO-2026-GC-FTO* [Código fuente]. GitHub. https://github.com/GC-TO/WRO-2026-GC-FTO

Gunardi, Y., y Jumadri, J. N. (2020). Design color sorting with conveyor and robot arm using Lego Mindstorm NXT. [revista pendiente: verificar nombre y volumen].

Intisar, M., Khan, M. M., Islam, M. R., y Masud, M. (2021). Computer vision based robotic arm controlled using interactive GUI. *Intelligent Automation & Soft Computing, 27*(2), 533-550. https://doi.org/10.32604/iasc.2021.015482

Johnson, K. (2026). *Wildlife spotter train* [Código fuente]. GitHub. https://github.com/keenanjohnson/wildlife-spotter-train

Kumar, A., Verma, A., Pal, V., Chaudhary, V., y Tripathi, A. (2026). Wireless robotic navigation via IoT-enabled Wi-Fi communication. *International Journal of Current Engineering and Technology, 16*(1). https://doi.org/10.14741/ijcet/v.16.1.4 [páginas pendientes]

LEGO Ideas. (s. f.). *VISION* [Propuesta de proyecto]. https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749

Lim, W. J., Teoh, P. S., Abdul Ghani, N. M., y Abas, M. F. (2021). Automatic control of color sorting and pick/place of a 6-DOF robot arm. *Journal Européen des Systèmes Automatisés, 54*(3), 435-443. https://doi.org/10.18280/jesa.540306

Llerena Buenaño, A. S., y Salazar Villamar, M. J. (2022). *Automatización de un sistema identificador y posicionador de objetos a través de un brazo robótico mediante visión artificial con lenguaje Python* [Tesis de grado, Universidad Politécnica Salesiana, sede Guayaquil]. [enlace pendiente]

Mada Sanjaya, W. S., Anggraeni, D., Munawwaroh, M., Nurasyidiek, M. Y. S., Rahayu, D. S., Samsudin, A., Santika, I. P., y Palupi, E. K. (2018). Colored object sorting using 5 DoF robot arm based artificial neural network (ANN) method. *Journal of Physics: Conference Series, 1090*, Artículo 012070. https://doi.org/10.1088/1742-6596/1090/1/012070

Markvicka, E., Finnegan, J. D., Moomau, K., Sommers, A. S., Peteranetz, M. S., y Daher, T. A. (2023). Designing learning experiences with a low-cost robotic arm. *2023 ASEE Annual Conference & Exposition*, Artículo 37271.

Medel, K. G. G., Sevilla, A. J., y Perez, M. P. (s. f.). Major color detection in robot vision. [revista pendiente], 78-82.

Mohammed, M. M., Al-Khafaji, M. M. H., y Abbas, T. F. (2023). Smart robot vision for a pick and place robotic system under different illumination conditions. *Engineering and Technology Journal, 41*(6). https://doi.org/10.30684/etj.2023.135966.1292

Monroy Moya, D. F., Barrera Prieto, F., y Rojas Sarmiento, D. A. (2024 [verificar: las extracciones dan 2024, 2025 y 2026]). Computer vision implementation on Raspberry Pi 4 for a 3 DOF robotic arm in object classification by shape and color. *Ingeniería e Investigación, 46*(2), Artículo e118562. https://doi.org/10.15446/ing.investig.118562

Narmadha, R., Anbarasi Jebaselvi, G. D., y Anitha, U. (2022). Composition of robotic arm control and color identification using machine learning algorithm. En J. C. Bansal, A. Engelbrecht, y P. K. Shukla (Eds.), *Computer vision and robotics: Proceedings of CVR 2021* (pp. 191-212). Springer. [DOI pendiente; verificar páginas]

Ntambara, [inicial pendiente], Furaha, [inicial pendiente], Masengo, [inicial pendiente], y Niyigaba, [inicial pendiente]. (2026). Design and prototyping of a smart powered lifting robotic arm (SPLRA). [revista, volumen y DOI pendientes: verificar; Perplexity indicó *Discover Robotics*, 2, artículo 17, https://doi.org/10.1007/s44430-026-00032-6]

Oliveira, F., Tinoco, V., Magalhães, S., Santos, F. N., y Silva, M. F. (2021 [verificar autores y año: NotebookLM no los identificó en la portada]). Research on end-effectors for harvesting manipulators. [actas o revista pendientes]

osullivp. (2021). *Lego51515BLEArduinoTensorFlow* [Código fuente]. GitHub. https://github.com/osullivp/Lego51515BLEArduinoTensorFlow

Pybricks. (s. f.-a). *Robotic arm with vision* [Proyecto; Perplexity lo atribuye a Laurens Valk y indica una actualización del 23 de marzo de 2026: verificar]. https://pybricks.com/project/robot-arm-camera-tracker/

Pybricks. (s. f.-b). *Use your phone as a smart sensor*. https://pybricks.com/learn/smart-sensors/getting-started/

Pybricks. (s. f.-c). *Motor, track_target* [Documentación]. https://docs.pybricks.com/en/stable/pupdevices/motor.html

Pybricks. (s. f.-d). *BLE broadcast/observe* [Registro de cambios del repositorio pybricks-api]. https://github.com/pybricks/pybricks-api/commit/3274cef849d91700905a56ec073cc2e3fb87f830

Pybricks. (s. f.-e). *Mediciones con sniffer de broadcast y observe* [Discusión #2822]. https://github.com/orgs/pybricks/discussions/2822

Rangarajan, A., y Bianchini, B. (2026). Vision-guided reorientation and color sorting of writing utensils using a low-cost 4-DoF arm. *American Journal of Student Research*. https://doi.org/10.70251/HYJR2348.467488

Shah, R., y Arockia Doss, A. S. (2026). Development of service robot manipulator for pick and place applications in domestic environment. *EPJ Web of Conferences, 355*, Artículo 01001. https://doi.org/10.1051/epjconf/202635501001 [verificar autores, revista y DOI: la revista y el DOI vienen de Perplexity]

Suhaeb, S., y Risal, A. (2024). Implementation of ESP32-based web host for control and monitoring of robotic arm. *Journal of Embedded System Security and Intelligent System, 5*(3), 249-254.

Tabb, A., y Ahmad Yousef, K. M. (2017). Solving the robot-world hand-eye(s) calibration problem with iterative methods. *Machine Vision and Applications, 28*(5-6), 569-590. https://doi.org/10.1007/s00138-017-0841-7

Tzompantzi Netzahual, J. E., Nava Bautista, H., y Sánchez Hernández, M. J. (2019). Real time control of robotic arm using Bluetooth Low Energy & Wi-Fi with the module board ESP32 and Android application. *International Journal of Science and Research, 8*(8). [páginas pendientes]

Vieira, E. de F., y Rizzetti, T. A. (2025). [título pendiente: ESP32 detectando anuncios BLE y publicándolos por MQTT]. *[Escola Regional de Redes de Computadores (ERRC): verificar]*. https://doi.org/10.5753/errc.2025.17688

Wu, Y., de Vries, C., Ford, M., y Herrera, A. (2014 [verificar autores: NotebookLM solo identifica a Penn State Erie]). *Project report: Using Mindstorms in a control systems lab to impact next generation engineers* [Informe de proyecto]. Penn State Erie, The Behrend College.

Yilmaz, S., Akay, C., y Kaysi, F. (2025). Design and implementation of a low-cost IoT-based robotic arm for product feeding and sorting in manufacturing lines. *Electronics, 14*(24), Artículo 4801. https://doi.org/10.3390/electronics14244801

Zuiev, A., Krylova, V., Hapon, A., y Honcharov, S. (2024). Research of microprocessor device and software for remote control of a robotic system. *Technology Audit and Production Reserves, 1*(2(75)), 31-37 [verificar revista y páginas]. https://doi.org/10.15587/2706-5448.2024.297339

---

## Guía resumen del manual de publicaciones con normas APA

> Resumen breve de las reglas APA 7 que se aplican en este informe. Preliminar: contrastar con el texto que envió el docente y confirmar con él cómo debe presentarse esta sección.

- **Cita en el texto:** autor y año entre paréntesis, por ejemplo (Pybricks, s. f.). Con dos autores se unen con "y"; con tres o más se usa "et al.".
- **Sin fecha:** se escribe "s. f.". Si hay varias obras del mismo autor sin fecha, se distinguen con letras: s. f.-a, s. f.-b.
- **Citado en otra fuente:** se indica el autor original y la fuente que lo recoge, por ejemplo (IFR, 2016, citado en Aucapiña e Iza, 2019).
- **Cita textual corta** (menos de 40 palabras): entre comillas, con autor, año y página.
- **Lista de referencias:** en orden alfabético, con sangría francesa. Cada fuente citada debe estar en la lista y viceversa.
- **Páginas web y documentos en línea:** autor, fecha, título en cursiva y enlace. Si hay DOI, se escribe como enlace (https://doi.org/...).
- **Tablas y figuras:** número en negrita, título en cursiva debajo del número, y una nota si hace falta ("*Nota.*").

---

## Anexo A. Lista de acrónimos

*(Actualizar a medida que se redacte el texto final.)*

| Acrónimo | Significado |
| -------- | ----------- |
| ANN | Red neuronal artificial (*Artificial Neural Network*) |
| ASEE | American Society for Engineering Education |
| BLE | Bluetooth de bajo consumo (*Bluetooth Low Energy*) |
| CPU | Unidad central de procesamiento (*Central Processing Unit*) |
| DC-DC | Convertidor de corriente continua a corriente continua |
| ESP-NOW | Protocolo inalámbrico sin conexión de Espressif |
| ESP32 | Microcontrolador con Wi-Fi y Bluetooth (fabricante Espressif) |
| GDL | Grados de libertad |
| GPU | Unidad de procesamiento gráfico (*Graphics Processing Unit*) |
| GUI | Interfaz gráfica de usuario (*Graphical User Interface*) |
| HSV | Tono, saturación y valor (*hue, saturation, value*) |
| HTTP | Protocolo de transferencia de hipertexto (*Hypertext Transfer Protocol*) |
| IA | Inteligencia artificial |
| IFR | Federación Internacional de Robótica (*International Federation of Robotics*) |
| IoT | Internet de las cosas (*Internet of Things*) |
| ISO | Organización Internacional de Normalización |
| JRC | Journal of Robotics and Control |
| MQTT | Protocolo de mensajería ligero (*Message Queuing Telemetry Transport*) |
| OpenCV | Open Source Computer Vision Library |
| PD / PID | Controlador proporcional-derivativo / proporcional-integral-derivativo |
| PWM | Modulación por ancho de pulso (*Pulse Width Modulation*) |
| RGB | Rojo, verde y azul (*red, green, blue*) |
| RS-485 | Estándar de comunicación serie diferencial |
| RSSI | Indicador de intensidad de la señal recibida (*Received Signal Strength Indicator*) |
| UART | Receptor-transmisor asíncrono universal (*Universal Asynchronous Receiver-Transmitter*) |
| USB | Bus serie universal (*Universal Serial Bus*) |
| YOLO | Detector de objetos en tiempo real (*You Only Look Once*) |
