# Contexto 22: continuar la sesión de refinamiento del informe (22-nov-2026)

**Cómo usar este archivo:** pegarlo o pedir que se lea al iniciar una sesión nueva, junto con `resumen_22.md` (registro de avance y decisiones). Este archivo es el traspaso: dónde estamos, qué se decidió, qué falta y qué preguntas hay que correr en NotebookLM.

---

## 0. Arranque de sesión (reglas del vault)

- Leer `E:\University_vault_2026\_skills\_start.md` con el MCP Filesystem y seguir su flujo (verificación MCP con `write_file` y `edit_file` sobre `Rubbish\section.md`, selección de skill).
- Skill usado: **2 = plan** (`_claude-plan.md`). El operator ya no importa: se ignora.
- Hora de inicio de la sesión anterior: 18:39 (los tokens se reestablecen 5 horas después).
- Antes de **reescribir archivos grandes** (como `informe.md`): avisar **"cambios masivos, bk necesario"** y esperar la copia de respaldo del usuario. Respaldos: `informe 1.md` a `informe 4.md`.
- **No se ha modificado `informe.md` en esta sesión.** El usuario pidió expresamente no hacer cambios hasta tener todo cruzado.
- Idioma: español, directo. Si hay dudas, preguntar antes de escribir. Una pregunta por mensaje.

## 1. El proyecto en una frase

Informe universitario (materia investigativa), **puramente teórico/documental**: "Control de un brazo robótico educativo mediante visión por computadora e IA: revisión de antecedentes y propuesta de integración con un prototipo LEGO". Archivo: `E:\University_vault_2026\python_arm\informe.md` (primer borrador completo, secciones 1 a 6, más guía APA y anexo de acrónimos).

- El **prototipo real NO tiene visión**: es control manual (`ha9.py`): celular → Wi-Fi (página web servida por el ESP32, red `BRAZO_LEGO`, `192.168.4.1`) → ESP32 → BLE broadcast de Pybricks → hub LEGO Inventor 51515 → motores. Funciona bien, un motor a la vez, y el ESP32 recuerda el último ángulo *ordenado* de cada articulación.
- Limitaciones del prototipo: sin batería (solo USB de corriente limitada), por eso un motor por orden; sin canal de vuelta hub → ESP32; retraso "mínimo" pero no medido; falta recalibrar ángulos negativos.
- La **IA y la visión son una PROPUESTA bien fundamentada**, no implementada. No se necesita parte práctica.
- Prueba preliminar propia (no continuada por falta de tiempo): con la cámara del celular y Pybricks se probó que detecta la pelota roja sobre una base café; no se calibró ni se integró.
- Los videos de brazos LEGO con Pybricks parecen mostrar seguimiento simultáneo de la pelota con todos los motores (con batería). El prototipo no puede hacerlo por la alimentación USB. **Falta el enlace del video para poder citarlo** (APA).
- "Sustentar la implementación de IA" se interpreta (a confirmar con el docente) como sustento teórico: nombrar los trabajos (papers y tesis) en que se basa la propuesta y adjuntar los enlaces de sus videos.

## 2. Esquema del docente (respetar orden y títulos)

1. Introducción y antecedentes (antecedentes y propósito general). 2. Objetivo (alcance o profundidad y limitaciones). 3. Justificación del proyecto (por qué es importante para la institución, escenario, impacto: científico, tecnológico, económico, social, ambiental; ¿para qué servirá?). 4. Desarrollo del proyecto (incluye el marco teórico). 5. Conclusiones y recomendaciones. 6. Referencias bibliográficas e internet. Al final: "Guía resumen del manual de publicaciones con normas APA" y anexo con lista de acrónimos. Citas: APA 7, `(Autor, año)`; sin dato = "s. f.".

## 3. Cómo trabajamos las fuentes

Perplexity (Deep Research, foco Académico) dio fuentes → se cargaron en NotebookLM (26 PDF) → NotebookLM extrajo datos por tema → se escribió el borrador. Ahora se **verifica cada dato contra el PDF** y se refina por prioridades. Regla: **no inventar datos**; lo no verificado se marca `[verificar]`, `[pendiente]` o "s. f.".

**Aviso de NotebookLM:** las respuestas valen solo para las fuentes que el cuaderno tiene cargadas. En una consulta se vio que el cuaderno solo tenía las 3 fuentes nuevas (Zuiev, Kumar, Ntambara) y no las 26 originales, por lo que sus "no está en las fuentes" no sirven para el corpus completo. **Siempre empezar con la pregunta S0 (lista de fuentes cargadas).**

## 4. Decisión tomada: arquitectura de la propuesta = opción A

Cámara USB/webcam en la **PC** → módulo de visión/IA en la PC (Python + OpenCV; luego un detector profundo) → Wi-Fi (HTTP, rutas `/s` y `/go` del ESP32) → ESP32 → BLE broadcast Pybricks → hub 51515 → motores. El celular queda como interfaz manual. Se descarta la cámara del celular conectada al hub (*smart sensors*) como parte de la propuesta.

## 5. Revisión del borrador: lista de pendientes por prioridad

### Prioridad 1 (errores de fondo; se corrigen de a uno)

1. **Cámara/módulo de IA: "tres versiones".** Eran tres frases que afirman de más que el proyecto usa visión: (a) Tabla 1, fila Pybricks: "Base del proyecto: se adaptó el hub, los puertos, el color y el arranque"; (b) 4.1.6: "el que usa este proyecto en su versión con cámara de celular"; (c) 4.3: "tablas de calibración con interpolación (la del proyecto)". Corrección acordada: estado real = implementado (control manual) / prueba preliminar (detección roja sobre café, sin calibrar) / propuesta (visión en PC). Pendiente decidir y escribir. Borrador de la fila de Pybricks (solo en el chat, no escrito): "Referencia más cercana de visión en LEGO. En este proyecto solo se probó, de forma preliminar, la detección de color de la pelota roja sobre una base café; no se calibró ni se integró". El contraste de los videos (seguimiento simultáneo frente a un motor a la vez por alimentación) va en 1.1 ("Plataformas LEGO con cámara") y en las restricciones de 4.3, no en 4.1.6.
2. **4.1.8 dice que no hay mediciones de latencia BLE en las fuentes.** Verificar con S1 a S3. Ya se sabe: la Tabla 1 de Tzompantzi es solo Wi-Fi; BLE se evaluó con RSSI (Figuras 9 y 10).
3. **Conclusión 1:** rango de acierto "84 % a 94,6 %" contradice el 97,28 % de 4.1.7 y la Tabla 3; el 84 % es "confiabilidad global" (otra métrica).
4. **Conclusión 3:** dice que la visión clásica es "comparable" a técnicas más pesadas, pero la Tabla 3 dice que las cifras no son comparables. Suavizar o quitar.
5. **Sniffer (Pybricks, s. f.-e):** fue con un City Hub, firmware 4.1.0b2, no con el 51515; 4.3 lo generaliza a "unos 10 mensajes por segundo". Aclarar.
6. **"Brecha" de 1.1 demasiado fuerte:** el proyecto de Pybricks con SPIKE Prime y cámara de celular, y *smart sensors*, ya usan el celular como cámara de un hub LEGO. La novedad real es la página web del ESP32 más un módulo de IA externo.
7. **"La pelota y el cubo" aparecen en 4.3 y 5.3 sin presentar la tarea.** Describirla en 3.2 o 4.2.
8. **Verificar contra los PDF (C1, A1 a A14).**

### Prioridad 2: rigor investigativo y esquema

Datos de institución, carrera y asignatura (cabecera, 3.1, 3.2); subsección de metodología de la revisión y conciliar "26 fuentes" con las 28 referencias listadas (las dos tesis ESPE pueden ser un mismo archivo duplicado); definir IA, aprendizaje automático, red neuronal y detección de objetos en 4.1.7; apoyos débiles (el PID de 4.1.4 se apoya en un robot de rehabilitación y falta cita para el término integral; Pybricks s. f.-b para decir que el 51515 corre Pybricks; "aprendizaje activo más efectivo" y "aforo reducido" de 3.1 y 3.2); costo real del montaje (C3) y fuente de "diseños modulares abiertos" (A18).

### Prioridad 3: formato APA y limpieza

Letras de Pybricks (s. f.-a a s. f.-e) según el orden alfabético del título (BLE broadcast, Mediciones, Motor, Robotic arm, Use your phone); fuentes sin autor con el título en la posición del autor (Tampere, JRC; ver B10); quitar material interno (bloque "Estado del borrador", notas "Verificar contra los trabajos completos", líneas meta de 3.3 y la fila "Ambiental: omitir"); figuras 1 y 2 como diagramas reales y formato APA 7 de tablas y figuras; confirmar con el docente el formato de la guía APA (C4); anexo de acrónimos (agregar RGB, DC-DC; revisar los que sobran).

### Prioridad 4 (opcional)

Medir el retraso orden-movimiento (C5); fuentes extra B4 a B9 (LEGO y BLE, comunicación de un solo sentido, detectores livianos, HSV con rojo y café).

## 6. Fuentes nuevas encontradas para la opción A

Verificadas leyendo el texto completo (Dang y Shah) o parcialmente (Capaldi, Bera). Confirmar volumen, páginas y orden de nombres en el PDF.

- **Dang et al. (2026)**: Dang Phuoc Thinh, Van Thi Ngoc Han, Nguyen Nghiep Thinh, Nguyen Vu Duc Huy, Tran Quang Thuan, Huynh Nhat Duy, Phi Thanh Dat, Vo Cong Hieu, Vo Duy Cong (autor de correspondencia). *Development of an Educational Robotic Platform with Dual Control Interfaces and Intelligent Computer Vision-Based Interaction*. FME Transactions, 54(1), 93-106. DOI en el PDF: 10.5937/fme2601093P. Brazo de 4 GDL con ESP32; YOLOv12 en una laptop solo con CPU; ángulos enviados al controlador. La interfaz web aparece como MQTT en el resumen y como Blynk en la sección 2 (contradicción interna). PDF: https://scindeks-clanci.ceon.rs/data/pdf/1451-2092/2026/1451-20922601093T.pdf
- **Shah y Arockia Doss (2026)**: *Development of Service Robot Manipulator for Pick and Place applications in Domestic Environment*. EPJ Web of Conferences, 355, 01001. DOI: 10.1051/epjconf/202635501001. ESP32 como punto de acceso con página de sliders, latencia menor a 150 ms, parada de emergencia en el navegador; YOLOv8-OBB y ROS/MoveIt **solo en simulación**. Video del modelo físico en la Fig. 6 (.mp4 dentro del artículo). PDF: https://www.epj-conferences.org/articles/epjconf/pdf/2026/11/epjconf_staaar2026_01001.pdf
- **Capaldi (2024)**: Emma I. Capaldi. *A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol*. PeerJ Computer Science, 10, e1826. DOI: 10.7717/peerj-cs.1826. Hub educativo VEX V5 + ESP32 + PC con visión (YOLOv8); mide distancia, tiempo de ida y vuelta y detección; incluye ajuste de PID. Es el análogo más cercano de la arquitectura; **conviene cargarlo en NotebookLM** (https://peerj.com/articles/cs-1826.pdf). Solo se vio el resumen.
- **Bera (2026, 1 de octubre)**: *Computer-vision-based robotic arm*, Electronics For You (revista, no revisada por pares; parte del texto exige registro gratuito). Visión en laptop, Raspberry Pi 5 o servidor GPU y control en el ESP32 por Wi-Fi, Ethernet, serial o ESP-NOW. **Video de la prueba de concepto:** https://www.youtube.com/watch?v=PHznMxfTjuo
- Por revisar (no verificados): Future Internet 18(6), 325 (https://www.mdpi.com/1999-5903/18/6/325); TeleopLab (arXiv 2509.05547).

## 7. Tres fuentes de la segunda ronda de Perplexity (ya cargadas en NotebookLM)

- **Zuiev, Krylova, Hapon y Honcharov (2024)**: *Research of microprocessor device and software for remote control of a robotic system*. DOI 10.15587/2706-5448.2024.297339. Perplexity dio la revista *Technology Audit and Production Reserves*, 1(2(75)), 31-37: **no verificado** (NotebookLM no lo encontró). Es un vehículo 4WD, no un brazo. Usable como apoyo: (a) parada forzada de motores si no llegan paquetes durante cierto tiempo, sin cifra del intervalo (Sec. 3.4); (b) S.BUS es de un solo sentido y se nombran protocolos con telemetría de retorno (CRSF, IBUS, FPort, MAVLink, DShot) (Sec. 3.1); (c) retardos internos del ESP32 de microsegundos (Tablas 2 y 3, a 160 MHz). **NO usar** los "60-80 ms frente a 10-20 ms" como latencia inalámbrica: es el retardo de conversión del receptor entre protocolos de radiocontrol. Las menciones a Wi-Fi y Bluetooth son cualitativas; no mide BLE.
- **Kumar, Verma, Pal, Chaudhary y Tripathi (2026)**: *Wireless Robotic Navigation via IoT-Enabled Wi-Fi Communication*. International Journal of Current Engineering and Technology, 16(1). DOI 10.14741/ijcet/v.16.1.4. Páginas sin verificar (Perplexity dijo 16-19). Revista de nivel bajo: usar solo como evidencia complementaria. Vehículo, no brazo. Tabla 2: latencia de ida y vuelta 38 / 62 / unos 120 ms con señal fuerte / moderada / débil, y éxito de 99,6 / 97,2 / 96,1 %. Hardware: "ESP8266 o ESP32" (no precisan). Las "200 secuencias" son para la precisión direccional, no para la latencia. 30 m × 20 m fue medido; los "30-100 m" son un rango típico estimado. Solo menciona Bluetooth clásico (HC-05 y HC-06) con alcance menor a 10-15 m, sin BLE. STOP retira la corriente a los motores; no hay confirmación de vuelta.
- **Ntambara, Furaha, Masengo y Niyigaba (2026)**: *Design and prototyping of a smart powered lifting robotic arm (SPLRA)*. **El primer autor es Ntambara, no Furaha** (Perplexity se equivocó). Identificador s44430-026-00032-6. Revista, volumen y DOI **sin verificar**: Perplexity dio *Discover Robotics*, 2, artículo 17, DOI 10.1007/s44430-026-00032-6, y NotebookLM no lo leyó (lo dedujo). Respalda la limitación de corriente: no opera los cuatro motores a la vez con su corriente máxima (Sec. 3); activa dos articulaciones durante el levantamiento; fuente de 12 V y 2 A; límite del driver A4988 con Vref; baja velocidad y activación secuencial (Sec. 3.5 y 3.8); corriente pico de 1,92 A y caída de 0,46 V. Comunicación celular + HC-06 (Bluetooth clásico) + UART en lazo abierto, sin retorno ni latencia medida. **No afirma** que el movimiento secuencial alargue el tiempo de ciclo; los 10 ensayos están a 135° (Tabla 5) y los tiempos de 2,6 a 4,0 s corresponden a otros ángulos.

## 8. Resultados de NotebookLM hasta ahora sobre Tzompantzi (2019)

La Tabla 1 se titula "Sending instructions in real time through Wi-Fi" (Sección 6): tiempos de respuesta HTTP de unos 50 a 60 ms (0,0499 a 0,0595 s) a 1, 10, 20, 30 y 40 m, con el ESP32 en modo punto de acceso (`192.168.4.1`). **Es solo Wi-Fi.** BLE se evaluó con RSSI (Figuras 9 y 10), no con latencia. Rango de latencia Wi-Fi reunido (métodos distintos, no comparables): Tzompantzi 50-60 ms; Suhaeb 85-92 ms; Kumar 38 a ~120 ms (ida y vuelta); Shah menos de 150 ms. Falta confirmar con S1 a S3 que ninguna de las fuentes mide latencia de BLE.

## 9. Preguntas pendientes para NotebookLM (cuaderno con las 29 fuentes)

Estado: el usuario junta las 26 + las 3 nuevas en un cuaderno. Orden: **S0 a S3 primero** (cierran el punto 2 de la prioridad 1). Al final de **cada** pregunta va este cierre (ya incluido abajo): *"Responde solo con lo que está en las fuentes. Indica fuente (autor, año) y página o sección. Si no está, escribe 'no está en las fuentes'. No inventes."* No nombrar secciones del informe (NotebookLM no las ve).

**S0.** Lista todas las fuentes cargadas con autor(es), año y título, y dime cuántas son en total. Marca cuáles aparecen repetidas (por ejemplo, dos archivos de la misma tesis).

**S1.** En Tzompantzi Netzahual et al. (2019), sección 6, Figuras 9 y 10: describe qué se midió con BLE (RSSI u otra cosa), a qué distancias, con qué valores y con qué dispositivo. Dime la distancia máxima probada para BLE y la distancia máxima probada para Wi-Fi.

**S2.** En Tzompantzi Netzahual et al. (2019): (a) copia el pasaje donde afirma que la respuesta es en tiempo real hasta unos 40 m y dime para qué tecnología (Wi-Fi, BLE o ambas); (b) copia el pasaje sobre una interrupción de unos 3 segundos al enviar instrucciones por Wi-Fi de forma simultánea, con las condiciones; (c) explica cómo se midió el 'Response time' de la Tabla 1 (quién lo midió, desde qué dispositivo, cuántas repeticiones).

**S3 (A15).** ¿Alguna fuente cargada mide la latencia (tiempo de respuesta o retardo) de BLE, ya sea en modo broadcast (sin conexión) o con conexión? Si una fuente mide solo RSSI o alcance, dilo aparte. Si ninguna mide latencia de BLE, escribe 'no está en las fuentes'.

**S4 (A16).** ¿Qué fuentes proponen, implementan o evalúan un canal de retorno (realimentación) desde el robot hacia el dispositivo de control, como confirmación de posición o de fin de movimiento? Para cada fuente dime: autor, año, qué proponen, y si lo implementaron y evaluaron o solo lo mencionan.

**S5 (A17).** ¿Qué fuentes mencionan sensores o verificación del agarre en la pinza (fuerza, presencia, táctil)? Para cada una dime qué proponen y si lo implementaron o solo lo sugieren como trabajo futuro.

**S6.** ¿Qué fuentes separan el procesamiento de visión (en PC, Raspberry Pi u otro equipo) del control de los motores, que queda a cargo de un microcontrolador distinto (Arduino, ESP32 u otro)? Para cada una dime: autor, año, qué equipo hace la visión, qué microcontrolador mueve el brazo, y cómo se comunican (USB, serie, Wi-Fi, Bluetooth).

**S7.** ¿Qué fuentes mencionan límites de alimentación o de corriente de los servos o motores, y cómo los resuelven (fuente externa, convertidor, limitar corriente, mover un motor a la vez)? Dime además si alguna reporta el efecto de mover las articulaciones de forma secuencial sobre el tiempo de ciclo o la velocidad.

**S8 (A18).** ¿Alguna fuente propone diseños modulares abiertos para reducir costo sin perder precisión de los servos? Dime autor, año y sección. Si la fuente es Bansal et al. (2022), indica el capítulo exacto, sus autores y sus páginas.

**Si se cargan Dang, Shah y Capaldi (N22 a N24):** (N22) Dang et al. (2026): lista completa de autores en el orden de la portada, volumen, número, páginas y DOI; ¿la interfaz web usa MQTT o Blynk? (copia los dos pasajes); confirma que YOLOv12 corre en una laptop solo con CPU y cómo llegan los ángulos al controlador. (N23) Shah y Arockia Doss (2026): confirma la latencia menor a 150 ms (cómo se midió), la parada de emergencia en el navegador y que YOLOv8-OBB y ROS/MoveIt se usaron solo en simulación; sección de cada dato. (N24) Capaldi (2024): copia los resultados de distancia y tiempo de ida y vuelta con unidades, el hub educativo usado y qué hace el experimento de ajuste de PID; sección de cada dato.

**Preguntas originales aún no corridas** (están en el contexto de la sesión anterior; el usuario las trae de a poco): A1 (TSP_IASC_15482: título exacto, autores, revista, volumen, número, páginas, año y DOI; ¿"Computer Vision Based Robotic Arm Controlled Using Interactive GUI" o "Design and Implementation of a Robotic Vision System Operated Using an Interactive GUI Application"?), A2 (tesis ESPE: año y sede; ¿son la misma tesis?), A3 (Monroy Moya: año, revista, volumen, número, fechas, DOI), A5 (Gunardi y Jumadri: revista, volumen, número, páginas, año), A6 (Fernández Panadero: congreso o revista, páginas, año), A7 (Medel: año, revista, volumen, páginas), A8 (Eiammanussakul: ¿robot de rehabilitación?; control en cascada y fórmula del ángulo), A9 (Mohammed: 93,83 %, 97,11 %, 27 s y ecuaciones 3 a 11), A10 (Intisar: 94,6 % y limitaciones), A11 (Rangarajan y Bianchini: 89,8 %, deriva de 8 mm, 2,65 px, YOLO11n-OBB, 19 de 20 fallos), A12 (Markvicka: costos), A13 (tesis ESPE: 84 %, 97,28 %, 38 a 50 ms, MobileNet_0.5_224, 0,2 mm), A14 (Mada Sanjaya: 20 neuronas, 1,3 %, 5 servos, 467 × 624 px). Cada una con el cierre "Responde solo con lo que está en las fuentes...".

**Perplexity pendiente:** B1 (autores reales del JRC 2026, del kit ASEE y de "LEGO con Raspberry Pi y OpenCV" de Tampere); B2 (PID en brazos educativos); B3 (LEGO SPIKE/51515/Pybricks en educación o investigación); B4 a B10 según prioridad. Se pidió una segunda ronda de 3 fuentes (ya hecha, ver sección 7). Falta un prompt para los **videos** de brazos LEGO con Pybricks (título, canal, año, enlace, hub, alimentación y si los motores se mueven a la vez o por turnos).

**Tareas del usuario (C1 a C6):** abrir los PDF y confirmar autores, año, revista y páginas (C1); datos de institución, carrera y asignatura (C2); costo real del montaje (C3); confirmar con el docente el formato de la guía APA y si APA 7 es definitivo (C4); medir el retraso orden-movimiento (C5, opcional); decidir si hace falta prueba de concepto (C6: se asume que no; si el docente la pide, la prueba mínima sería detección HSV de la pelota y el cubo desde foto o video con ángulos predichos por la tabla de calibración).

**Ítems a abrir en los PDF (C1) de las fuentes nuevas:** Zuiev (revista, volumen, número, páginas), Kumar (páginas), Ntambara (revista, volumen, DOI), Dang (volumen, páginas, orden de nombres).

## 10. Próximos pasos

1. Correr **S0 a S3** en el cuaderno con las 29 fuentes y traer las respuestas (cierra el punto 2 de la prioridad 1).
2. Correr S4 a S8 (y N22 a N24 si se cargan Dang, Shah y Capaldi).
3. Pedir a Perplexity los videos de brazos LEGO con Pybricks (o que el usuario pase los enlaces).
4. Cruzar todo con `informe.md` y proponer los cambios de la prioridad 1, uno por uno, sin escribir todavía.
5. Cuando haya acuerdo: avisar **"cambios masivos, bk necesario"**, esperar la copia de respaldo y recién entonces escribir.
6. Seguir con las prioridades 2, 3 y 4; actualizar el registro de avance de `resumen_22.md`.
