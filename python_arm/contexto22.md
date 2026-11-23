# Contexto 22: continuar la sesión de refinamiento del informe (22-nov-2026)

**Cómo usar este archivo:** pegarlo o pedir que se lea al iniciar una sesión nueva, junto con `resumen_22.md` (registro de avance y decisiones). Este archivo es el traspaso: dónde estamos, qué se decidió, qué falta y qué preguntas hay que correr en NotebookLM.

---

## A. ESTADO ACTUALIZADO (sesión 2 del 22-nov-2026). LEER ESTO PRIMERO; las secciones 0 a 10 de abajo son el traspaso original y quedan como histórico

### A.1 Sesión y herramientas

- Hora de inicio de la sesión 2: 20:06 (los tokens se reestablecen a las 01:06). Worker `alx-rul`. Skill 2 (plan); el operator se ignora. MCP verificado (write y edit sobre `Rubbish\section.md`) y `_hangar` listado.
- NotebookLM se quedó sin tokens. Se usa **Gemini** con el cuaderno `iaarm` (https://gemini.google.com/notebook/df4a68df-58fe-4c26-9070-2cfa24b4f409), que tiene las mismas fuentes. Gemini da menos metadatos: casi siempre responde «autor y año: no está en las fuentes» y numera «Fuente 1, 2...». Cierre a agregar en cada prompt: «Identifica cada fuente por el nombre exacto del archivo PDF, no por Fuente N; si no ves autor o año, dilo». Lo que salga de Gemini se atribuye por inferencia y se marca `[verificar]`.
- Perplexity sigue siendo la vía para fuentes externas.
- `informe.md` se editó con `edit_file` por lotes (no se reescribió entero), siempre después de que el usuario creara el respaldo.

### A.2 Respaldos del informe

- `informe 5.md` y `informe 6.md`: estado al inicio de la sesión 2 (46,96 KB).
- `informe 7.md` (58,40 KB): después del lote 1 y antes de los lotes 2 y 3.
- `informe.md`: vigente (ya con los tres lotes). Antes de otro cambio masivo: pedir `informe 8.md`.

### A.3 Lo hecho en `informe.md` (tres lotes)

**Lote 1 (respuestas S0 a S8; bk 6).** Prioridad 1, puntos 1 a 7 aplicados:
1. Arquitectura única = opción A. Tabla 1: fila de Pybricks pasa a ser referencia con prueba preliminar (pelota roja sobre base café, sin calibrar ni integrar) y fila VISION con la cámara en PC. 4.1.6: la tabla con interpolación lineal es una opción propuesta, no del proyecto. 4.3: cámara USB en PC, Figura 2 corregida, celular solo como interfaz manual, *smart sensors* descartado.
2. 4.1.8: BLE solo se midió con RSSI (-47,8 dBm a 1 m; -88,7 dBm a unos 40 m); los 50 a 60 ms de Tzompantzi son solo Wi-Fi (Wireshark, desde un navegador, repeticiones no indicadas); ninguna fuente mide latencia de BLE.
3. Conclusión 1: rango 84 % (confiabilidad global) a 97,28 % (identificación), no comparables.
4. Conclusión 3: sin «comparable».
5. Sniffer de Pybricks: City Hub, firmware 4.1.0b2, no el 51515 (4.1.2 y 4.3).
6. «Brecha» suavizada en 1.1.
7. La tarea (pelota roja sobre base café que se deposita en un cubo) se describe en 3.2.
Contenido nuevo: 2.3 (28 trabajos distintos en 29 archivos) y 2.5 (método de la revisión); párrafo de límites de alimentación en 4.1.4 (Ntambara, Yilmaz, Lim); definiciones de IA en 4.1.7 (con `[cita pendiente]`); Kumar en 4.1.8 (38 / 62 / unos 120 ms de ida y vuelta); **4.1.9 nueva con la Tabla 4** (separación entre visión y control: Mohammed, Intisar, Mada Sanjaya, Aucapiña e Iza, Markvicka, Monroy Moya y la propuesta); la tabla de limitaciones pasó a **Tabla 5**; en 4.3 se agregaron canales de retorno (Suhaeb, Aucapiña e Iza, Yilmaz, Llerena y Salazar), alimentación secuencial (Ntambara; ninguna fuente mide el efecto en el tiempo de ciclo) y parada ante pérdida de enlace (Zuiev); 4.4 con la prueba preliminar; 5.3 con agarre (Monroy Moya, Oliveira) y cerrar el lazo; Tabla 5 con diseños abiertos (Narmadha et al., 2022, cap. 15 de Bansal et al., pp. 191-212; Markvicka). Referencias nuevas: Kumar, Narmadha, Ntambara, Oliveira, Zuiev. Acrónimos nuevos: DC-DC, RGB, RSSI, UART, MQTT.

**Lote 2 (Perplexity A1, A2, A8; bk 7).**
- A1: solo se halló la página del proyecto de Pybricks *Robotic arm with vision* (SPIKE Prime, celular como *smart sensor*, objeto rojo, la base gira hasta width > 8 y 70 < x < 80, actualizado el 23-mar-2026; autor Laurens Valk sin confirmar). No confirma batería ni motores simultáneos y no hay video equivalente con el 51515. Se quitó del informe la frase de videos con batería; queda `[pendiente: confirmar en el video]`. La referencia mantiene la letra s. f.-a.
- A2: no hay tesis ni artículo arbitrado con la cadena completa. Proyectos abiertos: Wildlife Spotter Train (Johnson, 2026: ESP32-S3 como puente Wi-Fi a BLE hacia un City Hub con Pybricks y cámara MJPEG, sin visión), Lego51515BLEArduinoTensorFlow (osullivp, 2021), WRO-2026-GC-FTO (GC-TO, 2026) y HuskyLens con LMS-ESP32 (Anton's Mindstorms, 2025). Agregados en 1.1, Tabla 1 (dos filas), brecha, conclusión 1 y referencias. **Falta verificar los README** (GATT o difusión en Wildlife, función del ESP32 en WRO, placa y firmware en osullivp).
- A8: no hay medición publicada de latencia de un paquete BLE en broadcast de ESP32 a otro dispositivo. Cho et al. (2014, *Sensors*, 15(1), DOI 10.3390/s150100059) es modelo de latencia de descubrimiento. Vieira y Rizzetti (2025, ERRC, DOI 10.5753/errc.2025.17688) dan 44 y 85 ms, pero con el ESP32 como receptor que publica por MQTT (latencia de sistema, sentido contrario). Souboura (2026) y Shih (2022) no se citaron. Agregado en 4.1.8 y referencias (títulos pendientes).

**Lote 3 (Gemini A3 a A7).**
- A3: la definición de PID y del término integral no está en las fuentes (solo PI y PD dentro de lazos en cascada). El `[cita pendiente]` de 4.1.4 sigue.
- A4: hay definiciones parciales de aprendizaje automático, red neuronal y detección de objetos, sin autor identificado; la de IA no. Marca de 4.1.7 actualizada.
- A5: UPS Guayaquil (atribuido a Llerena y Salazar, 2022): el aforo limitado por la pandemia obligó a dar prácticas en línea con brazos KUKA KR AGILUS; Aucapiña e Iza (2019): número limitado de módulos en la ESPE Latacunga. Corregidos 3.2 y 3.3 (se quitó a Tzompantzi, que no habla de aforo).
- A6: no hay meta-análisis. 3.1 reescrito (se quitó «aprendizaje activo más efectivo»; holgura con Ntambara y Mohammed, fricción con Eiammanussakul). 1.1: Markvicka (36 estudiantes, calificaciones sin diferencia significativa entre tareas tradicionales y con brazo; encuesta n = 35, 78 %) en vez de «efecto favorable». Dato de holgura de Ntambara: repetibilidad angular 0,41 ± 0,23° y posicional 2,47 ± 0,58 mm (10 ciclos, 0,8 kg).
- A7: ningún antecedente de tabla píxeles a ángulos con interpolación lineal; frase añadida en 4.1.6 con `[cita pendiente]`.

### A.4 Datos de S0 a S8 que no deben perderse

- S0: 29 archivos = 28 trabajos (la tesis de Aucapiña e Iza está como `ESPEL-MEC-0165-P.pdf` diapositivas y `T-ESPEL-MEC-0165.pdf` tesis). Sin metadatos: `2010S03C01.pdf`, `2402.17243v1.pdf`, `30-100-1-SP.pdf` (IJATEC-IRIS 2020, sin autores), `978-3-642-32527-4_17.pdf` (LEGO Mindstorms en ingeniería, sin autor), `P-00W-KW7.pdf` (efectores para cosecha), `s44430-026-00032-6.pdf` (Ntambara). Medel sin año. Penn State Erie 2014 sin autor personal. Dang, Shah y Capaldi no están cargados.
- S4 (retorno): Suhaeb consulta `/get_values` cada segundo y recibe JSON; Aucapiña e Iza (uArm): serie bilateral, comandos `P2220` (coordenadas) y `P2232` (estado de pinza), `ok` tras cada `G0`; Yilmaz: IMU MPU6050 y finales de carrera; Llerena y Salazar: servos de bus LX-15D/LX-225 con ángulo, voltaje y temperatura; Monroy Moya: OLED e infrarrojos; Ntambara: lazo abierto.
- S5 (agarre): Monroy Moya (infrarrojo en la pinza, implementado), Oliveira et al. 2021 (vacío, fibra óptica, fuerza; Lehnert 2017, Mu 2020, Rong 2021), Rangarajan y Bianchini (lazo abierto; fuerza de contacto como trabajo futuro), Aucapiña e Iza (cita a Campos 2016, táctil). Intisar no aparece.
- S6 (visión y control separados): ver Tabla 4 del informe. Monroy Moya (2025 según S6) cita además a Intisar 2021, Abdullah-Al-Noman 2022, Lahoti 2021, Kumar 2021 y Cong 2021.
- S7 (alimentación): Ntambara 12 V y 2 A, pico 1,92 A, caída 0,46 V, secuencial; Lim (caídas de 5 a 0 V con `Servo.h`, registros PWM); Yilmaz (relés, optoacopladores PC817, ACS712, fusible 4,2 A, tierra en estrella); Aucapiña e Iza (convertidor LM2596); Kumar (LiPo 7,4 V a 6 / 5 / 3,3 V). Ninguna mide el efecto del movimiento secuencial en el tiempo de ciclo.
- S8: Bansal et al. (2022), cap. 15, Narmadha, Anbarasi Jebaselvi y Anitha, pp. 191-212, brazo de 4 GDL con corte láser y Arduino abierto, error menor a 1 %; Markvicka: kit abierto menor a 200 USD con MG996R, ATmega328 y PCA9685.

### A.5 Discrepancias abiertas (resolver con los PDF, tarea C1)

- Suhaeb: el informe dice 85 a 92 ms; S4 dice 85 a 110 ms con hasta 10 usuarios.
- Monroy Moya: año 2024 (informe), 2025 (S4 y S5) o 2026 (S0).
- NotebookLM y Gemini mezclaron las dos tesis (ESPE, uArm, Aucapiña e Iza; UPS, xArm 1S, Llerena y Salazar). Se usó la atribución del informe; confirmar.
- Intisar: la limitación «sigue la rutina aunque el objeto se caiga» quedó `[verificar]` en la Tabla 5.
- Atribuciones por inferencia (Gemini): «Fuente 1 = Llerena y Salazar» (aforo) y «Fuente 3 = Markvicka» (36 participantes).
- Metadatos sin verificar: Ntambara (revista, volumen, DOI, iniciales), Zuiev (revista y páginas), Oliveira (autores y año), Wu (autores), Cho y Vieira (títulos), Kumar (páginas), Gunardi, Fernández Panadero y Medel (revista).

### A.6 Pendientes

**Prompts para Perplexity (aun no corridos).** Cierre común: «Para cada fuente dame autor(es), año, título, revista o editorial, DOI o URL, y página o sección. No inventes; si no puedes confirmar un dato, escribe no confirmado».
- A3 (PID): libros, apuntes universitarios o revisiones que definan el control PID y el término integral y su efecto sobre el error en estado estacionario, de preferencia con servomotores o brazos educativos y acceso abierto.
- A4 (definiciones): libro, survey u organismo reconocido que defina inteligencia artificial, aprendizaje automático, red neuronal artificial y detección de objetos en visión por computadora.
- A5 (aforo y práctica a distancia): laboratorios remotos con brazos o robots educativos que mencionen el aforo o los equipos limitados, y buscar en especial *Benitez et al. (2020), Design of an affordable IoT open-source robot arm for online teaching of robotics courses during the pandemic contingency, HardwareX 8* (aparece citado dentro de una de las fuentes).
- A6 (aprendizaje activo): meta-análisis o estudios con cifras de aprendizaje activo frente a pasivo en ingeniería o ciencias, y estudios de que los modelos físicos enseñan fricción u holgura.
- B (metadatos): autores del JRC 2026 y del proyecto de Tampere; revista de Fernández Panadero 2010, Gunardi y Jumadri 2020 y Medel; autores de Wu et al. 2014 y de Oliveira et al. 2021; datos de Ntambara, Zuiev, Kumar y del año de Monroy Moya.
- Opcionales: detectores livianos (YOLO nano, MobileNet), rojo contra café en HSV, comunicación de un solo sentido.

**Tareas del usuario.** C1 (abrir los PDF y confirmar autores, año, revista, páginas); C2 (institución, carrera, asignatura); C3 (costo real del montaje); C4 (confirmar con el docente el formato de la guía APA); C5 (medir el retraso orden-movimiento, opcional); ver el video o la página del proyecto de Pybricks y anotar si los motores se mueven a la vez y con qué alimentación; verificar los README de los cuatro proyectos abiertos; completar títulos de Cho y Vieira.

**Prioridad 3 (sin hacer).** Reordenar las letras de Pybricks por título (a = BLE broadcast, b = Mediciones, c = Motor, d = Robotic arm, e = Use your phone; hoy Robotic arm es s. f.-a); quitar material interno (bloque de estado, notas Verificar contra los trabajos completos, línea meta de 3.3 y fila Ambiental); figuras 1 y 2 como diagramas reales; formato APA 7 de tablas y figuras; acrónimos que sobran; la frase repetida de *smart sensors* en 1.1; «Autor pendiente» de Tampere y JRC.

**Omitido por ahora.** N22 a N24 (Dang, Shah y Capaldi): el usuario no tiene esas fuentes, así que no se citan ni están en la Tabla 1.

### A.7 Cómo retomar

1. Leer `_start.md`, activar skill 2 (plan) y leer este archivo y `resumen_22.md`. Responder `ok` tras listar `_hangar`.
2. Pedir al usuario las respuestas de A3 a A6, B, y lo que haya verificado en los PDF y README.
3. Aplicar los cambios con `edit_file`, previo aviso «cambios masivos, bk necesario» y un respaldo `informe 8.md`.
4. Luego prioridad 3 y actualizar el registro de `resumen_22.md`.

---

## 0. Arranque de sesión (reglas del vault)

- Leer `E:\University_vault_2026\_skills\_start.md` con el MCP Filesystem y seguir su flujo (verificación MCP con `write_file` y `edit_file` sobre `Rubbish\section.md`, selección de skill).
- Skill usado: **2 = plan** (`_claude-plan.md`). El operator ya no importa: se ignora.
- Hora de inicio de la sesión anterior: 18:39 (los tokens se reestablecen 5 horas después).
- Antes de **reescribir archivos grandes** (como `informe.md`): avisar **"cambios masivos, bk necesario"** y esperar la copia de respaldo del usuario. Respaldos: `informe 1.md` a `informe 4.md`.
- [Histórico, ya superado: `informe.md` se modificó en la sesión 2, ver sección A.] El usuario pidió expresamente no hacer cambios hasta tener todo cruzado.
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

## 5. Revisión del borrador: lista de pendientes por prioridad (HISTÓRICO: el estado actual de cada punto está en A.3 y A.6)

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

## 9. Preguntas pendientes para NotebookLM (cuaderno con las 29 fuentes) (HISTÓRICO: S0 a S8 ya corridas y aplicadas; N22 a N24 omitidas; ver A.3 a A.6)

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

## 10. Próximos pasos (HISTÓRICO: ver A.7)

1. Correr **S0 a S3** en el cuaderno con las 29 fuentes y traer las respuestas (cierra el punto 2 de la prioridad 1).
2. Correr S4 a S8 (y N22 a N24 si se cargan Dang, Shah y Capaldi).
3. Pedir a Perplexity los videos de brazos LEGO con Pybricks (o que el usuario pase los enlaces).
4. Cruzar todo con `informe.md` y proponer los cambios de la prioridad 1, uno por uno, sin escribir todavía.
5. Cuando haya acuerdo: avisar **"cambios masivos, bk necesario"**, esperar la copia de respaldo y recién entonces escribir.
6. Seguir con las prioridades 2, 3 y 4; actualizar el registro de avance de `resumen_22.md`.
