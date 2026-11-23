A continuación se presenta el análisis de las fuentes que proponen, implementan, evalúan o mencionan un canal de retorno (realimentación) desde el robot o sus componentes hacia el dispositivo o interfaz de control (como confirmación de posición, estado o fin de movimiento):

---

### **1. `T-ESPEL-MEC-0165.pdf` / `ESPEL-MEC-0165-P.pdf`**
* **Autor(es):** Marc Salazar y Anthony Llerena (Tutor: Ing. David Cortez).
* **Año:** 2022 (con cronograma de desarrollo en 2020–2022).
* **Qué proponen:** Proponen un sistema de automatización para la identificación, manipulación y ensamble de piezas por visión artificial utilizando un brazo robótico (uArm Swift Pro) y una interfaz gráfica bilateral desarrollada en QML, C++ y Python.
* **Canal de retorno (realimentación):** Implementan una comunicación serie RS-232 bilateral donde la placa del robot devuelve respuestas y estados a la interfaz:
  * Comando `P2220\n` para obtener y retornar las coordenadas actuales del robot (`ok X... Y... Z...`).
  * Comando `P2232\n` para verificar el estado del gripper (`ok V1`, donde 0 es desactivado, 1 trabajando y 2 activado).
  * Respuesta de confirmación `ok` tras enviar instrucciones de movimiento `G0`.
  * Despliegue visual en la interfaz de usuario con la señal de confirmación de fin de ciclo ("ESTADO DE LA MANIPULACIÓN: COMPLETADA").
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** de forma práctica mediante pruebas de manipulación de piezas y verificación de códigos de respuesta en la comunicación serie.

---

### **2. `electronics-14-04801.pdf`**
* **Autor(es):** No se indican los nombres de los autores en los extractos disponibles de la fuente.
* **Año:** 2025.
* **Qué proponen:** Un sistema industrial de alimentación y clasificación de productos basado en un brazo robótico de 4 GDL, una banda transportadora, lector RFID (RC522) y un controlador central ESP32 con servidor web/IoT.
* **Canal de retorno (realimentación):**
  * Un sensor inercial IMU MPU6050 (acelerómetro y giroscopio) en la muñeca del robot envía dinámicamente mediante \\(I^2C\\) los ángulos de rotación actuales al ESP32 para monitorear y corregir el error o deslizamiento de los servomotores.
  * Interruptores de límite (*limit switches*) envían notificaciones de eventos al controlador ESP32 para confirmar los límites de cada eje y la posición de *standby*.
  * La página de monitoreo del sistema en tiempo real (HMI web) recibe y muestra la ubicación de los eslabones, lecturas de sensores, estado de parada de emergencia y genera alertas sonoras/visuales al completar las cuotas de trabajo.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** experimentalmente, midiendo el error de posicionamiento de los servos (\\(\pm 1.2^\circ\\)), tiempo de ciclo (\\(4.8 \pm 0.3\text{ s}\\)), precisión RFID (\\(98.7\%\\)) y tiempo de respuesta ante paradas de emergencia (\\(45\text{ ms}\\)).

---

### **3. `118562-118562.pdf`**
* **Autor(es):** No se indican los nombres individuales de los autores en los extractos disponibles (figuran como *Authors* en tablas y figuras).
* **Año:** 2025.
* **Qué proponen:** Un sistema de clasificación de objetos geométricas por forma mediante visión artificial y un brazo robótico articulado de 3 GDL controlado por una Raspberry Pi 4 con interfaz GUI en Qt Designer/Python.
* **Canal de retorno (realimentación):**
  * Una pantalla OLED integrada en el espacio de trabajo del robot muestra en tiempo real los ángulos actuales de cada servomotor, los pasos de interpolación de la trayectoria y el estado del efector final (abierto o cerrado) para seguimiento continuo.
  * Sensores infrarrojos de presencia retroalimentan al sistema para detener o reducir la velocidad del robot si se detecta un objeto u obstáculo.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** de manera práctica en modos automático, semiautomático y manual, analizando métricas de precisión NRMSE, desviaciones estándar e intervalos de confianza.

---

### **4. `(249-254)+Implementation+of+ESP32-Based+Web+Host.pdf`**
* **Autor(es):** Sutarsi Suhaeb y Ahmad Risal.
* **Año:** 2024.
* **Qué proponen:** La implementación de un servidor web alojado en un microcontrolador ESP32 para el control y monitoreo en tiempo real de un brazo robótico a través de una interfaz web por Wi-Fi.
* **Canal de retorno (realimentación):** La interfaz web utiliza solicitudes AJAX con la función `fetch()` hacia el endpoint `/get_values` del ESP32 cada segundo, el cual responde retornando datos en formato JSON con los valores y estado de los parámetros/posiciones para actualizar en tiempo real la pantalla de monitoreo.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** físicamente, midiendo el tiempo de respuesta de los comandos (entre 85 y 110 ms), latencia y estabilidad bajo múltiples usuarios conectados (hasta 10 usuarios simultáneos).

---

### **5. `ART20196990.pdf`**
* **Autor(es):** No se indican los nombres de los autores en el extracto (desarrollado en colaboración con Microside S.A. de C.V.).
* **Año:** 2019.
* **Qué proponen:** Un prototipo de brazo robótico manipulador de 4 GDL basado en el módulo ESP32 controlado a través de una aplicación móvil nativa en Android comunicada mediante HTTP y Bluetooth.
* **Canal de retorno (realimentación):** El servidor Web alojado en el ESP32 escucha peticiones HTTP y envía de vuelta a la aplicación móvil mensajes de respuesta en texto plano (ejemplo: `"Abrir Pinza"`, `"Cerrar Pinza"`) que confirman la recepción e interpretación de la instrucción en la pantalla del dispositivo de control.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron**, analizando el tráfico Wi-Fi con Wireshark y midiendo los tiempos de respuesta del servidor en función de la distancia del dispositivo de control (de 1m a 40m).

---

### **6. `UPS-GT003848.pdf`**
* **Autor(es):** G. N. Montenegro Alcívar y M. L. Yaguachi Ríos (citados en marco de referencia) / Tesis de grado de la Universidad Politécnica Salesiana.
* **Año:** 2021.
* **Qué proponen:** Un sistema de control y visión artificial para la clasificación de objetos con un brazo robótico xARM1S.
* **Canal de retorno (realimentación):** Describe el uso de servomotores de bus inteligente (LX-15D / LX-225), los cuales incluyen un indicador RGB y transmiten hacia el controlador principal datos de retroalimentación de ángulo, voltaje y temperatura para protección.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** en las prácticas laboratorio de movimiento manual por ángulos y secuencias de posicionamiento.

---

### **7. `JHE2018-1927807.pdf`**
* **Autor(es):** No se indican los nombres individuales de los autores en los extractos disponibles (artículo de *Journal of Healthcare Engineering*).
* **Año:** 2018.
* **Qué proponen:** Un esquema y arquitectura de control para un robot de rehabilitación de miembros inferiores en ejercicios asistidos activos.
* **Canal de retorno (realimentación):** Diseña bucles de control en cascada que utilizan la realimentación continua de la posición articular actual (\\(\theta_j\\)) calculada mediante encóderes montados en el eje del motor, además de sensado de corriente (\\(i\\)) para realimentar el torque/fuerza de interacción entre el paciente y el robot.
* **¿Lo implementaron y evaluaron o solo lo mencionan?:** **Lo implementaron y evaluaron** mediante simulaciones y experimentos físicos aplicando perturbaciones de torque en la articulación del tobillo.

---

### **Otras fuentes que mencionan el tema o aplican lazo abierto:**
* **`s44430-026-00032-6.pdf` (2026):** Proproforma un brazo robótico de elevación (SPLRA) mediante motores a pasos y módulo Bluetooth. Esta fuente **menciona explícitamente que su sistema opera en lazo abierto (*open-loop*) y NO utiliza corrección por realimentación** ("Prevention of step loss was done via design and not feedback correction").
* **`CSEIT1846140.pdf` (2018):** **Menciona únicamente a nivel teórico/bibliográfico** que las tareas de manipulación robustas requieren verificación con realimentación de error de posición (*position error feedback*), comúnmente mediante servocontrol visual (*visual servoing*).
* **`Automatic_Control_of_Color_Sorting_and_P.pdf` (2021):** **Solo menciona** estudios previos de la literatura (ej. Högfeldt y Söderman, 2016) sobre realimentación háptica (*haptic feedback*), mientras que en su propio prototipo verifica la conexión con el servidor Blynk y reajusta los servos según comandos recibidos.

---

💡 Si deseas profundizar en la estructura de comandos serie o en los tiempos de respuesta de alguna de estas fuentes en particular, dímelo y lo revisamos a detalle.


==---==

A continuación se detallan las fuentes que abordan sensores o métodos de verificación del agarre en la pinza (fuerza, presencia, presión, táctil o vacío), indicando sus autores, año, página o sección, qué proponen y si lo implementaron o solo lo sugieren/mencionan:

---

### **1. `118562-118562.pdf`**
* **Autor(es):** David Fernando Monroy Moya, Fabián Barrera Prieto y Diego Alfonso Rojas Sarmiento.
* **Año:** 2025 (aceptado/publicado 2025–2026).
* **Página o Sección:** Abstract, Sección *"3 DOF robotic arm"*, *"Figure tracking and positioning"* y Conclusiones.
* **Qué proponen:** Proponen la integración de tres sensores infrarrojos de presencia en la celda de trabajo de un brazo robótico de 3 GDL. Uno de estos sensores está instalado específicamente en la parte superior del efector final (gripper) para detectar la presencia de objetos o la disponibilidad antes de manipularlos y evitar colisiones. Además, incorporan una pantalla OLED que muestra en tiempo real el estado del efector final (indicando si está abierto o cerrado).
* **¿Lo implementaron o solo lo sugieren?:** **Lo implementaron y evaluaron** físicamente en la celda de trabajo robótica.

---

### **2. `P-00W-KW7.pdf`**
* **Autor(es):** Francisco Oliveira, Vítor Tinoco, Sandro Magalhães, Filipe N. Santos y Manuel F. Silva.
* **Año:** 2021.
* **Página o Sección:** Sección III (*"Harvesting End-Effectors"*), Sección IV (*"Discussion"*), Sección V (*"Conclusion"*) y Tabla I.
* **Qué proponen:** Corresponde a una revisión del estado del arte de efectores finales para recolección agrícola, donde analizan las siguientes propuestas de verificación de agarre:
  * **Lehnert et al. (2017):** Incorporaron un **sensor de vacío** para detectar la sujeción a la ventosa y un micro-switch para verificar el desacople del fruto. *(**Implementado** en dicho estudio)*.
  * **Mu et al. (2020):** Utilizaron un efector final equipado con **sensor de fibra óptica** (para confirmar que envolvió exitosamente el fruto), **sensor de posición** y **sensor de presión**. *(**Implementado** en dicho estudio)*.
  * **Rong et al. (2021):** Evaluaron un gripper blando para hongos, pero notaron que la fuerza no controlada dañaba los frutos; por ello, concluyeron que el efector final debe equiparse con **sensores de realimentación de fuerza (*force feedback sensors*)** para regular la fuerza y confirmar si el objeto fue sujetado con éxito. *(**Sugerido como trabajo futuro** por dichos autores)*.
* **¿Lo implementaron o solo lo sugieren?:** Los autores del artículo realizan la revisión bibliográfica. En los trabajos revisados, Lehnert et al. y Mu et al. **lo implementaron**, mientras que Rong et al. **solo lo sugirieron como trabajo futuro**.

---

### **3. `ajsr2026_79gxSktt.pdf`**
* **Autor(es):** Anirudh Rangarajan y Bibit Bianchini.
* **Año:** 2026.
* **Página o Sección:** Secciones *"Hardware Setup - End-effector"*, *"Qualitative Performance and Failure Analysis"* y *"Discussion - Future Directions"*.
* **Qué proponen:** Utilizan un brazo de 4 GDL con una pinza provista de puntas de espuma blanda (*soft foam tips*) para sujetar bolígrafos suavemente. El proceso actual es en lazo abierto (*open-loop*), sin sensar la presencia o la fuerza durante el agarre o arrastre. Proponen para trabajos futuros desarrollar políticas de manipulación adaptativas que modulen el movimiento o la distancia de barrido en función de la **fuerza de contacto inferida o medida** (*inferred contact force*).
* **¿Lo implementaron o solo lo sugieren?:** **Solo lo sugieren como trabajo futuro** (su sistema actual funciona en lazo abierto sin sensores de fuerza o contacto).

---

### **4. `T-ESPEL-MEC-0165.pdf` / `ESPEL-MEC-0165-P.pdf`**
* **Autor(es):** Ney Fernando Aucapiña Garnica y Brayan Iván Iza Guanochanga (Tutor: Ing. Nathaly Rea) / Marc Salazar y Anthony Llerena (Tutor: Ing. David Cortez).
* **Año:** 2019 / 2022.
* **Página o Sección:** Sección 3.6 (*"Alternativas y selección del elemento de sujeción de piezas"*), Sección 3.12 y Referencias.
* **Qué proponen:** En la revisión de alternativas para el efector final citan el estudio de **Campos (2016)** (*Garras con sensores táctiles intrínsecos para manipular alimentos con robots*), donde se analiza la regulación de la fuerza mediante **sensores táctiles intrínsecos**. En su propio prototipo utilizan la pinza metálica *uArm Metallic Gripper* controlada por servomotor DC, sin instalar sensores de fuerza o táctiles directos en las pinzas.
* **¿Lo implementaron o solo lo sugieren?:** **Solo lo mencionan a nivel de revisión bibliográfica / marco teórico** (referenciando la investigación de Campos, 2016).

---

### **5. `electronics-14-04801.pdf`**
* **Autor(es):** No se indican los nombres de los autores en los extractos de la fuente.
* **Año:** 2025.
* **Página o Sección:** Sección 2.2.2 (*"Mechanical Design of ARM"*) y Sección 5 (*"Sensing and Identification"*).
* **Qué proponen:** Utilizan una pinza de mandíbulas paralelas con almohadillas adaptables (*compliant pads*) para sujetar objetos cúbicos. Para la verificación y control de movimiento del brazo y de la muñeca colocan un sensor inercial MPU6050 (acelerómetro y giroscopio) en la muñeca del robot, además de interruptores de límite (*limit switches*) en los ejes.
* **¿Lo implementaron o solo lo sugieren?:** **Lo implementaron y evaluaron** experimentalmente.

---

### **6. `Automatic_Control_of_Color_Sorting_and_P.pdf`**
* **Autor(es):** No se indican los nombres individuales de los autores en los extractos de la fuente.
* **Año:** 2021.
* **Página o Sección:** Sección de marco teórico / revisión de literatura.
* **Qué proponen:** Citan estudios previos de la literatura (Högfeldt y Söderman, 2016) sobre el uso de **realimentación háptica** (*haptic feedback*) en pinzas robóticas.
* **¿Lo implementaron o solo lo sugieren?:** **Solo lo mencionan a nivel bibliográfico**.

---

### **Otras fuentes del proyecto:**
En el resto de las fuentes de la libreta (`05942ac1a528769c3002f715f757989da7e8.pdf`, `872519a0fa329f8c0e976db1a5410809e3e4.pdf`, `s44430-026-00032-6.pdf`, `ART20196990.pdf`, `(249-254)+Implementation+of+ESP32-Based+Web+Host.pdf`, `UPS-GT003848.pdf`, `TSP_IASC_15482.pdf`, entre otras), la presencia o verificación directa del agarre mediante sensores de fuerza/táctiles en la pinza **no está en las fuentes** (varias operan en lazo abierto o basan la sujeción únicamente en el accionamiento del servomotor o temporización).

---

🔍 *Si deseas revisar los esquemas de circuito o los modelos exactos de alguno de estos sensores en particular, dime y lo profundizamos.*


===---===



A continuación se detallan las fuentes que separan el procesamiento de visión artificial (en una computadora, laptop o Raspberry Pi) del control de los motores o articulaciones del brazo robótico (delegado a un microcontrolador independiente como Arduino o controladores dedicados):

---

### **1. `Smart_Robot_Vision_for_a_Pick_and_Place.pdf`**
* **Autor(es):** No se indican los nombres individuales de los autores en los extractos de la fuente (*"no está en las fuentes"*).
* **Año:** No se indica el año de publicación en los extractos de la fuente (*"no está en las fuentes"*).
* **Página o Sección:** Sección 3.1 (*"Pick and Place Robotic System"*), Sección 4 (*"Image Processing and Feature Extraction Algorithm"*), Figuras 1, 5 y 11.
* **Equipo que hace la visión:** **Raspberry Pi (RPi)** con una cámara webcam conectada por puerto USB, ejecutando un programa en Python con la librería OpenCV para detectar forma, color y centroide.
* **Microcontrolador que mueve el brazo:** **Arduino** (configurado como microcontrolador esclavo para ejecutar la cinemática inversa y mover los 5 servomotores del brazo robótico de 5 GDL y la banda transportadora).
* **Cómo se comunican:** **Comunicación serie UART (RS232)** en configuración Maestro/Esclavo.

---

### **2. `TSP_IASC_15482.pdf`**
* **Autor(es):** Mohammad Monirujjaman Khan, M. Intisar, M. M. Khan, M. R. Islam y M. Masud.
* **Año:** 2021.
* **Página o Sección:** Sección 2.4 (*"Hardware Design"*), Sección 3 (*"Results and Analysis"*), Figuras 5 y 6, Tabla 7.
* **Equipo que hace la visión:** **Computadora (PC)** conectada a una webcam, ejecutando algoritmos de visión en OpenCV/Python para clasificación por color, forma y tamaño y cálculo de centroide.
* **Microcontrolador que mueve el brazo:** Microcontrolador **Arduino Uno** (recibe las coordenadas articulares y acciona los 4 servomotores MG90s del brazo robótico de 4 GDL).
* **Cómo se comunican:** Cable **USB** (comunicación serie sobre conexión USB entre la PC y la tarjeta Arduino Uno).

---

### **3. `Mada_Sanjaya_2018_J._Phys.__Conf._Ser._1090_012070.pdf`**
* **Autor(es):** Mada Sanjaya WS et al.
* **Año:** 2018.
* **Página o Sección:** Abstract, Sección 2 (*"General System Overview"*), Sección 3 (*"Color Detection"*), Sección 4 (*"Hardware of Robot Arm"*) y Figura 2.
* **Equipo que hace la visión:** **Computadora / PC** (procesamiento de imágenes con Python 2.7 y OpenCV para la detección de centroide y cálculo del modelo cinematizado mediante redes neuronales).
* **Microcontrolador que mueve el brazo:** Microcontrolador **Arduino** (recibe los ángulos predichos y genera las señales PWM para 5 servomotores en un brazo de 5 GDL).
* **Cómo se comunican:** **Puerto serie** (Serial Port / USB).

---

### **4. `T-ESPEL-MEC-0165.pdf` / `ESPEL-MEC-0165-P.pdf`**
* **Autor(es):** Marc Salazar y Anthony Llerena (Tutor: Ing. David Cortez)  / Ney Fernando Aucapiña Garnica y Brayan Iván Iza Guanochanga (Tutor: Ing. Nathaly Rea) .
* **Año:** 2022 / 2019.
* **Página o Sección:** Sección 3.5.1 (*"Selección del sistema de procesamiento"*), Sección 3.14.3 (*"Selección de la tarjeta de control"*), Sección 4.11.4 (*"Comunicación Interfaz-Brazo e Interfaz-Arduino"*), Tabla 28, Tabla 35 y Tabla 36.
* **Equipo que hace la visión:** **Computadora portátil / PC** (ejecutando una interfaz gráfica desarrollada en Qt Creator con C++, Python, OpenCV y TensorFlow).
* **Microcontrolador que mueve el brazo:** 
  * Tarjeta controladora del brazo **uArm Swift Pro** (placa basada internamente en **Arduino Mega**) para el movimiento de los ejes y servomotores.
  * Tarjeta **Arduino Uno** independiente para controlar el servomotor del elemento de sujeción (pinza) y el relé del sistema de iluminación.
* **Cómo se comunican:** **Puerto serie RS-232 / USB** (puertos COM3 y COM5 a 115200 baudios enviando cadenas de texto/códigos G como `G0 X... Y... Z...` y comandos como `c31\n`) y conexión inalámbrica **Bluetooth** para el módulo del uArm.

---

### **5. `Markvicka_et_al-2023-asee.pdf`**
* **Autor(es):** Markvicka et al.
* **Año:** 2023.
* **Página o Sección:** Sección 3.1 (*"Hardware architecture"*), Sección 3.2 (*"Software architecture"*), Tabla 1.
* **Equipo que hace la visión / procesamiento:** **Computadora portátil (Laptop / PC)** ejecutando programas en MATLAB, Python o C++ para el procesamiento de datos y la generación de trayectorias.
* **Microcontrolador que mueve el brazo:** Microcontrolador **ATmega328 (Adafruit METRO 328 / Arduino)** conectado a un servocontrolador de 16 canales (PCA9685 vía \\(I^2C\\)).
* **Cómo se comunican:** Cable **USB** (envío de comandos serie desde la laptop hacia el microcontrolador).

---

### **6. Estudios citados y comparados en `118562-118562.pdf`**
* **Autor(es) de la fuente principal:** David Fernando Monroy Moya, Fabián Barrera Prieto y Diego Alfonso Rojas Sarmiento.
* **Año de la fuente principal:** 2025.
* **Página o Sección:** Sección *"Introduction"* (págs. 2-3, Pasajes 17-18 y 24-25).
* **Aclaración:** Monroy, Barrera y Rojas (2025) señalan explícitamente que su propio desarrollo **no** separa el procesamiento, sino que **centraliza** la visión por computador y el control del brazo en una única placa Raspberry Pi 4B para evitar latencias. Sin embargo, en su marco teórico citan y describen las siguientes fuentes que sí separan ambos sistemas:
  * **Intisar et al. (2021) [ref. 24]:** Visión en **PC** mediante webcam USB (OpenCV) / Control del brazo de 4 GDL en **Arduino** / Comunicación por **USB**.
  * **Abdullah-Al-Noman et al. (2022) [ref. 25]:** Visión en **PC** (OpenCV) y sensor PixyMCU / Control del brazo de 5 GDL en **Arduino Mega 2560** / Comunicación por **USB / Serie**.
  * **Lahoti et al. (2021) [ref. 26]:** Visión en **Raspberry Pi 3B+** (red YOLO) / Control del brazo de 5 GDL en **Arduino Uno** / Comunicación **Serie UART**.
  * **Kumar et al. (2021) [ref. 27]:** Visión en **Raspberry Pi** (escaneo de píxeles RGB) / Control del brazo de 6 GDL en **Arduino Mega 2560** / Comunicación **Serie UART**.
  * **Cong et al. (2021) [ref. 28]:** Visión en **Raspberry Pi 4B** con cámara / Control de dos brazos de 3 GDL mediante **dos tarjetas Arduino Uno** (jerarquía Maestro-Esclavos) / Comunicación **Serie**.

---

🔍 *Si requieres conocer los parámetros específicos de configuración de baudios o los códigos de comandos utilizados en alguno de estos esquemas, con gusto los revisamos a detalle.*


===---===


A continuación se detallan las fuentes que abordan límites de alimentación o corriente en los actuadores (servos o motores) y sus soluciones, así como los datos reportados sobre el movimiento secuencial de las articulaciones y su efecto en el tiempo de ciclo o velocidad:

---

### **1. `s44430-026-00032-6.pdf`**
* **Autor(es):** No se indican los nombres de los autores en los extractos disponibles de la fuente (desarrollado para el prototipo de brazo de elevación SPLRA).
* **Año:** 2026.
* **Página o Sección:** Abstract, Sección 3.5 (*"Electrical power budget and stepper driver current limiting"*), Sección 3.8 (*"Open-loop stepper motion control"*), Sección 4.7 (*"Electrical power consumption and voltage-drop validation"*) y Tabla 4.
* **Límites de alimentación y corriente:** La fuente de alimentación en corriente continua está limitada a 12 V / 2 A (24 W). Sin embargo, cuatro motores a pasos NEMA 17 operando simultáneamente a sus especificaciones máximas de corriente de fase (1.5 A a 2 A) sobrepasarían dicha capacidad de 2 A.
* **Cómo lo resuelven:**
  1. **Limitación de corriente en controladores (*driver current limiting*):** Se ajusta el voltaje de referencia (\\(V_{ref}\\)) en los controladores de motor (tipo A4988/DRV8825) previo a los ensayos (\\(I_{limit} = V_{ref} / (8 R_s)\\)) para fijar una corriente de fase mínima suficiente para cargas ligeras.
  2. **Activación y movimiento secuencial de articulaciones (*sequential joint operation*):** Durante el procedimiento principal de elevación no mueven todos los motores al mismo tiempo a máxima corriente; activan primero el motor de elevación principal (hombro) y luego las articulaciones de soporte necesarias, manteniendo los demás motores en menor consumo o desactivados.
* **Efecto sobre el consumo y la estabilidad eléctrica:** La activación secuencial permitió mantener el consumo máximo en 1.92 A de pico (potencia máxima de 22.31 W y promedio de 1.45–1.73 A), reduciendo la caída de voltaje a \\(0.46\text{ V}\\) y evitando reinicios del microcontrolador Arduino o pérdida de pasos (*step loss*).
* **Efecto del movimiento secuencial sobre el tiempo de ciclo y la velocidad:** Reporta que el tiempo de ciclo por elevación (*cycle time per lift*) bajo esta operación secuencial varía según el ángulo de elevación: **4.0 s a 90°** y **2.6 s a 180°** (con un tiempo promedio de ciclo de ~3.3 s). Explica que a mayores ángulos de elevación se aprovecha una mayor ventaja mecánica, lo que reduce el tiempo de elevación. *Nota:* La fuente no realiza una prueba comparativa directa midiendo la velocidad/tiempo en movimiento paralelo simultáneo frente a secuencial, ya que el movimiento paralelo a plena carga excedería el límite eléctrico de 2 A de la fuente.

---

### **2. `Automatic_Control_of_Color_Sorting_and_P.pdf`**
* **Autor(es):** No se indican los nombres individuales de los autores en los extractos de la fuente.
* **Año:** 2021.
* **Página o Sección:** Sección 3 (*"Results and Analysis"*), Sección 4 (*"Conclusion"*) y Referencias.
* **Límites de alimentación y caídas de voltaje:** Mencionan que el accionamiento simultáneo de múltiples servomotores utilizando las librerías estándar `Servo.h` y `SoftwareSerial` genera conflictos de interrupción y fluctuaciones/caídas bruscas de voltaje (de 5 V a 0 V en intervalos muy cortos), provocando inestabilidad/vibración (*jittering*) y reiniciando los sensores de entrada.
* **Cómo lo resuelven:**
  1. **Control directo de registros PWM:** Modifican el código para controlar los servos mediante programación directa de los registros de temporizadores de PWM en Arduino (registros TIMER1 y TIMER2: `OCR1B`, `OCR1A`, `OCR2A`), lo que permite mantener la señal PWM activa sin apagar los servos al finalizar el ciclo y sostener el peso del brazo robótico sin necesidad de drivers externos.
  2. **Aumento de alimentación de entrada (Propuesta futura):** Recomiendan para trabajos futuros reemplazar la fuente de alimentación cableada por una batería de mayor potencia para mejorar la estabilidad ante cargas más pesadas.
* **Efecto de mover las articulaciones de forma secuencial sobre el tiempo de ciclo o la velocidad:** **no está en las fuentes**.

---

### **3. `electronics-14-04801.pdf`**
* **Autor(es):** No se indican los nombres de los autores en los extractos de la fuente.
* **Año:** 2025.
* **Página o Sección:** Sección 2.2.3 (*"Electronics and Power"*), Sección 6 (*"PCB Design of Control Board"*), Sección 2.3.6 y Tabla 1.
* **Límites de alimentación y corriente:** Identifican riesgos de sobrecorriente por la conmutación de los servomotores y el motor de la banda transportadora, así como interferencias electromagnéticas (EMI/back-EMF).
* **Cómo lo resuelven:**
  1. **Relés independientes y aislamiento por optoacopladores:** Aíslan las líneas de alimentación de los servomotores y de la banda mediante relés dedicados impulsados desde el ESP32 a través de optoacopladores PC817.
  2. **Sensor de corriente y fusible de protección:** Incorporan un sensor de corriente ACS712 para monitorear sobrecorriente y un fusible de cristal de 4.2 A para desconexión del circuito.
  3. **Líneas separadas de 5 V y 12 V DC y tierra en estrella (*star grounding*):** Utilizan líneas de alimentación separadas para lógica y potencia con topología de masa en estrella.
  4. **Limitación de velocidad por firmware:** Implementan restricciones de velocidad en los servomotores para prevenir movimientos repentinos y optimizar la eficiencia energética.
* **Efecto de mover las articulaciones de forma secuencial sobre el tiempo de ciclo o la velocidad:** **no está en las fuentes** (miden un tiempo de ciclo total promedio de \\(4.8 \pm 0.3\text{ s}\\) para el proceso Pick-and-Place automático, pero no evalúan el efecto del movimiento secuencial de cada articulación).

---

### **4. `ESPEL-MEC-0165-P.pdf` / `T-ESPEL-MEC-0165.pdf`**
* **Autor(es):** Ney Fernando Aucapiña Garnica y Brayan Iván Iza Guanochanga (2019) / Marc Salazar y Anthony Llerena (2022).
* **Año:** 2019 / 2022.
* **Página o Sección:** Sección 13 / Recomendaciones de `ESPEL-MEC-0165-P.pdf` (pág. 46) y Sección 3.14 de `T-ESPEL-MEC-0165.pdf`.
* **Límites de alimentación y regulación de voltaje:** Al alimentar el sistema desde una fuente principal de 12 V DC y requerir voltajes menores regulados para los servomotores de accionamiento (ej. 6 V para el servomotor Futaba S3003 o 5 V para relés).
* **Cómo lo resuelven:** Recomiendan e implementan el uso de un módulo convertidor de voltaje DC-DC regulable **LM2596** (convertidor Buck) para reducir la tensión de 12 V a los 6 V / 5 V requeridos, manteniendo constante el suministro y evitando daños por sobrevoltaje en los equipos electrónicos.
* **Efecto de mover las articulaciones de forma secuencial sobre el tiempo de ciclo o la velocidad:** **no está en las fuentes**.

---

### **5. `05942ac1a528769c3002f715f757989da7e8.pdf`**
* **Autor(es):** No se indican los nombres de los autores en los extractos disponibles de la fuente.
* **Año:** No se indica el año en los extractos disponibles de la fuente (*"no está en las fuentes"*).
* **Página o Sección:** Sección 7 (*"Circuit Design"*).
* **Límites de alimentación y regulación de voltaje:** Reducir la tensión de una batería LiPo de 7.4 V para alimentar la etapa de potencia del motor a 6 V y la etapa lógica a 5 V y 3.3 V.
* **Cómo lo resuelven:** Utilizan un regulador lineal 7805 o convertidor Buck para el riel de 5 V y un regulador AMS1117-3.3 para el SoC ESP, instalando condensadores de desacoplamiento (\\(100\ \mu\text{F}\\) electrolítico + \\(100\text{ nF}\\) cerámico) en las entradas de alimentación para suprimir el ruido de conmutación de los motores.
* **Efecto de mover las articulaciones de forma secuencial sobre el tiempo de ciclo o la velocidad:** **no está en las fuentes**.

---

💡 *Si deseas revisar las ecuaciones de par motor, la selección de fusibles o la configuración exacta de los convertidores Buck en alguna de las fuentes, avísame y lo profundizamos.*



===---===


En las fuentes cargadas se abordan propuestas de plataformas robóticas de bajo costo y código/diseño abierto (*open-source*) que buscan mantener la precisión de los servomotores minimizando los costos de manufactura y componentes:

---

### **1. Compilación de Bansal et al. (2022)**
* **Libro / Editores principales:** Jagdish Chand Bansal, Andries Engelbrecht y Praveen Kumar Shukla (Eds.), *Computer Vision and Robotics: Proceedings of CVR 2021* (publicado en 2022 por Springer).
* **Capítulo exacto:** **Capítulo 15** (*Chapter 15*): *"Composition of Robotic Arm Control and Color Identification Using Machine Learning Algorithm"*.
* **Autores del capítulo:** R. Narmadha, G. D. Anbarasi Jebaselvi y U. Anitha.
* **Páginas del capítulo:** Páginas **191 a 212**.
* **Sección(es):**
  * **Sección 1.1 (*Arm Control*) y Sección 2 (*Methodology*):** Proponen la fabricación de un brazo robótico de 4 GDL utilizando técnica de corte por láser para las piezas y un controlador abierto (*open-source*) basado en Arduino, lo que permite un ahorro masivo de costos y tiempo en manufactura sin sacrificar la exactitud dimensional, logrando reducir la tasa de error a menos del 1%.
  * **Sección 4 (*Conclusion*):** Analizan que el costo es la principal limitante en brazos robóticos y destacan que los servomotores de alto torque con alta precisión (*"High torque servos with excessive precision"*) son indispensables para lograr los movimientos del brazo pero constituyen el componente más costoso.

---

### **2. Markvicka (2023)**
* **Autor(es):** Eric Markvicka.
* **Año:** 2023.
* **Sección:** Sección 1 (*Introduction*), Sección 2 (*Related research*) y Sección 3 (*Low-Cost robotic arm platform / 3.1 Hardware architecture*).
* **Qué propone:** Propone un kit de brazo robótico de código y diseño abierto (*open-source*) de bajo costo (< \$200 USD) constituido por componentes comerciales ensamblables con herramientas básicas. Utiliza servomotores digitales de alto torque con engranajes metálicos (MG996R) controlados mediante un microcontrolador ATmega328 y un protector/driver de servos de 16 canales (PCA9685 vía \\(I^2C\\)) para lograr un control preciso de la posición articular sin requerir costosos equipos industriales.

---

### **3. Mada Sanjaya et al. (2018)**
* **Autor(es):** W. S. Mada Sanjaya et al..
* **Año:** 2018.
* **Sección:** *Abstract* y Sección 4 (*Hardware of Robot Arm*).
* **Qué propone:** Proponen la implementación de un sistema de clasificación y manipulación de objetos mediante un brazo robótico de 5 GDL de bajo costo y código abierto (*Open Source and Low Cost*) impulsado por servomotores controlados por Arduino y alimentados por batería de 5 V, utilizando redes neuronales artificiales (ANN) y Python/OpenCV para asegurar una alta tasa de precisión en el posicionamiento de los servos.

---

💡 *Si necesitas detalles adicionales sobre la arquitectura de control o los algoritmos utilizados en alguno de estos capítulos, dime y lo revisamos.*