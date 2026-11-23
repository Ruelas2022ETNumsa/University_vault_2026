# Contexto 22: traspaso para continuar en un chat nuevo (22-nov-2026)

**Cómo usar este archivo:** pedir que se lea al iniciar el chat nuevo, junto con `resumen_22.md` (registro de avance y decisiones) y `bitacora_22.md` (lista viva de pendientes). Este archivo es el traspaso: cómo retomar, el estado real de `informe.md`, los datos de las fuentes que no deben perderse, las discrepancias abiertas y los prompts listos para pegar. Actualizado al cierre de la sesión 3 (la 1 fue a las 18:39; la 2, 20:06 con tokens a las 01:06; la 3, 21:43 con tokens a las 02:43).

---

## 1. Cómo retomar

1. Leer `E:\University_vault_2026\_skills\_start.md` con el MCP Filesystem, hacer la verificación MCP (`write_file` y `edit_file` sobre `E:\University_vault_2026\Rubbish\section.md`) y elegir la **skill 2 (plan)**. El operator se ignora. Tras listar `_hangar`, responder solo `ok`. El worker es el que indique el mensaje de apertura.
2. Leer este archivo, `resumen_22.md` y `bitacora_22.md`.
3. Preguntar al usuario qué trae: respuestas de la sección 7 (verificación en PDF y Perplexity) o resultados de sus tareas.
4. Cada cambio masivo a `informe.md`: avisar **"cambios masivos, bk necesario"** y esperar el respaldo (siguiente: `informe 10.md`). Aplicar con `edit_file` por lotes, no reescribiendo el archivo. Una pregunta por mensaje, en español y directo.
5. Al cerrar cada lote, actualizar `resumen_22.md` y marcar la bitácora.

**Herramientas.**
- NotebookLM se quedó sin consultas el 22-nov. Alternativa: **Gemini** con el cuaderno `iaarm` (https://gemini.google.com/notebook/df4a68df-58fe-4c26-9070-2cfa24b4f409), con las mismas fuentes, pero con menos metadatos (suele responder «no está en las fuentes» para autor y año, y numera «Fuente N»). Cierre extra para Gemini: *«Identifica cada fuente por el nombre exacto del archivo PDF, no por Fuente N; si no ves autor o año, dilo»*. Lo que salga de Gemini se atribuye por inferencia y se marca `[verificar]`.
- Perplexity (Deep Research, foco Académico) sigue siendo la vía para fuentes externas y metadatos.
- Si `edit_file` falla con `EPERM` al renombrar un archivo temporal, otro programa (Obsidian, sincronización) tiene el archivo abierto: avisar con el mensaje de `_start.md` y reintentar tras cerrarlo.

**Respaldos del informe.** `informe 1.md` a `informe 9.md` (el 5 y el 6 son el estado al inicio de la sesión 2; el 7 es posterior al lote 1; el 9 es el estado justo antes del lote 4). `resumen_22 1.md` es el respaldo del resumen. `informe.md` es el vigente (lotes 1 a 4).

## 2. El proyecto

Informe universitario (materia investigativa), **puramente teórico y documental**: *Control de un brazo robótico educativo mediante visión por computadora e inteligencia artificial: revisión de antecedentes y propuesta de integración con un prototipo LEGO*. Archivo: `E:\University_vault_2026\python_arm\informe.md`.

- **Prototipo real (otra materia, funciona):** celular → Wi-Fi (página web servida por el ESP32, red `BRAZO_LEGO`, `192.168.4.1`) → ESP32 (`esp32/web_control.py`, guardado como `main.py`) → BLE de difusión de Pybricks, canal 1, tupla `(articulación, ángulo, id_orden)` → hub LEGO Inventor 51515 (`ha9.py`) → motores. Un motor a la vez (solo USB de corriente limitada, sin batería); vigila el voltaje (pausa bajo 5500 mV); límites de ángulo en el hub; descarta órdenes durante un movimiento. El ESP32 recuerda el último ángulo *ordenado*. Rutas web: `/s`, `/go`, `/pos`, `/cero`. **No tiene visión.** Sin canal de vuelta hub → ESP32, retraso no medido, falta recalibrar ángulos negativos.
- **Propuesta (no implementada):** cámara USB en la PC → módulo de visión e IA en la PC (Python y OpenCV; luego un detector profundo) → Wi-Fi (HTTP, rutas `/s` y `/go`) → ESP32 → BLE de difusión → hub 51515 → motores. El celular queda como interfaz manual; se descarta la cámara del celular con *smart sensors*.
- **Prueba preliminar propia:** con la cámara del celular y Pybricks se detectó la pelota roja sobre una base café; sin calibrar ni integrar.
- **Tarea de referencia:** tomar la pelota roja sobre la base café y depositarla en un cubo.
- "Sustentar la implementación de IA" se interpreta como sustento teórico-documental (**a confirmar con el docente**); si el docente pide algo implementado, la prueba mínima sería detección HSV de la pelota y el cubo desde foto o video, con ángulos predichos por la tabla de calibración.

**Esquema del docente (respetar orden y títulos).** 1. Introducción y antecedentes (antecedentes y propósito general). 2. Objetivo (alcance o profundidad y limitaciones). 3. Justificación del proyecto (importancia para la institución, escenario, impacto científico, tecnológico, económico, social, ambiental; ¿para qué servirá?). 4. Desarrollo del proyecto (incluye el marco teórico). 5. Conclusiones y recomendaciones. 6. Referencias bibliográficas e internet. Al final: «Guía resumen del manual de publicaciones con normas APA» y anexo con lista de acrónimos. Citas APA 7, `(Autor, año)`; sin dato = «s. f.».

**Reglas.** No inventar datos; lo no verificado se marca `[verificar]`, `[pendiente]`, `[cita pendiente]` o «s. f.». Verificar cada dato contra el PDF antes de entregar.

## 3. Estado de `informe.md` (con los lotes 1 a 4)

Estructura: 1 Introducción y antecedentes (1.1, 1.2; Tabla 1), 2 Objetivo (2.1 a 2.5), 3 Justificación (3.1 a 3.3), 4 Desarrollo (4.1.1 a 4.1.9 con Tablas 2, 3 y 4; 4.2 prototipo; 4.3 propuesta con Figura 2; 4.4 pruebas), 5 Conclusiones y recomendaciones (Tabla 5), 6 Referencias, guía APA y anexo de acrónimos.

- **Lote 1 (S0 a S8):** arquitectura única (PC con visión); BLE medido solo con RSSI y los 50 a 60 ms de Tzompantzi son solo Wi-Fi; conclusión 1 con 84 % (confiabilidad global) a 97,28 % (identificación), métricas no comparables; sniffer con City Hub 4.1.0b2; brecha suavizada; tarea descrita en 3.2; nuevos 2.3, 2.5, 4.1.9 y Tabla 4; límites de alimentación (Ntambara, Yilmaz, Lim); Kumar; canales de retorno, alimentación secuencial y parada por pérdida de enlace en 4.3; 5.3 con agarre y cerrar el lazo.
- **Lote 2 (Perplexity A1, A2, A8):** solo la página de Pybricks *Robotic arm with vision* (SPIKE Prime; no confirma batería ni motores simultáneos); cuatro proyectos abiertos (Johnson 2026, osullivp 2021, GC-TO 2026, Anton's Mindstorms 2025) a verificar en sus README; sin medición publicada de latencia BLE de difusión con ESP32 (Cho 2014 modelo; Vieira y Rizzetti 2025 con 44 y 85 ms, sentido contrario).
- **Lote 3 (Gemini A3 a A7):** PID y IA sin definición en las fuentes (`[cita pendiente]`); aforo (UPS Guayaquil y ESPE Latacunga); sin meta-análisis de aprendizaje activo (3.1 reescrito); Markvicka con 36 estudiantes y sin diferencia significativa; sin antecedente de tabla píxeles a ángulos con interpolación lineal.
- **Lote 4 (N22 a N24, N24b, Gemini N22b; bk `informe 9.md`):** Dang, Capaldi y Shah integrados en 1.1, la brecha, las Tablas 1, 3 y 4, 4.1.4, 4.1.7, 4.1.8, 4.1.9, 4.3, las conclusiones 1, 3 y 5, la recomendación 4, 2.3 (31 trabajos en 32 archivos), 2.5, referencias y acrónimos (CPU, GPU, ESP-NOW, RS-485).
- **Brecha vigente:** la novedad no es la cámara, ni la PC con visión, ni el puente por separado. Es la combinación hub LEGO 51515 con Pybricks + página web servida por un ESP32 + módulo de visión externo, que no se halló completa en la literatura revisada (búsqueda no sistemática).

## 4. Datos de las fuentes que no deben perderse

**Corpus.** 32 archivos = 31 trabajos distintos (la tesis de Aucapiña e Iza está como `ESPEL-MEC-0165-P.pdf` diapositivas y `T-ESPEL-MEC-0165.pdf` tesis). Sin metadatos: `2010S03C01.pdf`, `2402.17243v1.pdf`, `30-100-1-SP.pdf` (IJATEC-IRIS 2020, sin autores), `978-3-642-32527-4_17.pdf` (LEGO Mindstorms en ingeniería, sin autor), `P-00W-KW7.pdf` (efectores para cosecha), `s44430-026-00032-6.pdf` (Ntambara). Medel sin año; Penn State Erie 2014 sin autor personal. Siempre empezar una consulta nueva con la lista de fuentes cargadas (S0), porque las respuestas valen solo para lo cargado.

**Dang et al. (2026)** (`1451-20922601093T.pdf`). Nueve autores en el orden de la portada: Dang Phuoc Thinh, Van Thi Ngoc Han, Nguyen Nghiep Thinh, Nguyen Vu Duc Huy, Tran Quang Thuan, Huynh Nhat Duy, Phi Thanh Dat, Vo Cong Hieu, Vo Duy Cong (correspondencia). *Development of an Educational Robotic Platform with Dual Control Interfaces and Intelligent Computer Vision-Based Interaction*. FME Transactions 54, 93-106, DOI 10.5937/fme2601093P; el número no aparece en el PDF. Abstract y 3.3: la interfaz web usa MQTT (órdenes publicadas al ESP32); sección 2 menciona Blynk (contradicción interna). YOLOv12 corre en una laptop solo con CPU (entrenamiento en Colab con GPU). Flujo: caja delimitadora, transformación calibrada 2D al robot, cinemática inversa, ESP32, PCA9685, servos MG996R. Según Gemini (inferencia): sin mAP, sin tiempo de inferencia, sin éxito ni ciclo (validación cualitativa), calibración solo mencionada, ruta de visión por USB. PDF: https://scindeks-clanci.ceon.rs/data/pdf/1451-2092/2026/1451-20922601093T.pdf

**Capaldi (2024)** (`peerj-cs-10-1826.pdf`). Emma I. Capaldi. *A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol*. PeerJ Computer Science, 10, e1826, DOI 10.7717/peerj-cs.1826 (revista y DOI vienen de Perplexity). VEX V5 + dos ESP32 (ESP-NOW) + RS-485; cámara OpenMV H7 por USB a una PC con YOLOv8 en Python. Pérdida de paquetes: 0 % a 0 m, 0,197 % a 10 m, 0,571 % a 20 m, 0,861 % a 30 m, 0,126 % a 40 m, 13,2 % a 60 m (recomienda 40 m o menos para lazo cerrado). Ida y vuelta 187 ms (DE 57 ms); la Tabla 2 tiene 11 segmentos y los segmentos 2 a 4 no estaban en los fragmentos cargados (los 1 y 11 son calculados, 29,8 ms cada uno). 30 pruebas de clasificación (10 por condición). Inferencia de YOLOv8: 62,8 ms (Ryzen 9 5950X), 52,1 ms (Apple M2), 8,41 ms (Quadro P2200). Experimento de PID con Kp, Ki, Kd y retorno del ángulo a 20 lecturas por segundo. https://peerj.com/articles/cs-1826

**Shah y Arockia Doss (2026)** (`epjconf_staaar2026_01001.pdf`). *Development of Service Robot Manipulator for Pick and Place applications in Domestic Environment*. EPJ Web of Conferences, 355, 01001, DOI 10.1051/epjconf/202635501001 (de Perplexity). WebSockets con ESP32 (ESPAsyncWebServer), latencia menor a 150 ms sin método de medición (4.1 y 5.2.2), parada de emergencia en el navegador (5.2.3), YOLOv8-OBB y ROS/MoveIt solo en simulación (Gazebo y RViz); el brazo físico (MG996R) es manual. Video del modelo físico en la Fig. 6. https://www.epj-conferences.org/articles/epjconf/pdf/2026/11/epjconf_staaar2026_01001.pdf

**Tzompantzi Netzahual et al. (2019).** Tabla 1 «Sending instructions in real time through Wi-Fi» (sección 6): 50 a 60 ms (0,0499 a 0,0595 s) a 1, 10, 20, 30 y 40 m, ESP32 como punto de acceso; solo Wi-Fi. BLE solo con RSSI (Figuras 9 y 10). Latencias Wi-Fi reunidas (métodos distintos, no comparables): Tzompantzi 50-60 ms; Suhaeb 85-92 ms; Kumar 38 a unos 120 ms (ida y vuelta); Shah menos de 150 ms; Capaldi 187 ms (ESP-NOW, ida y vuelta). Ninguna fuente mide latencia de BLE.

**Retorno (S4).** Suhaeb consulta `/get_values` cada segundo y recibe JSON; Aucapiña e Iza (uArm): serie bilateral, comandos `P2220` (coordenadas) y `P2232` (estado de pinza), `ok` tras cada `G0`; Yilmaz: IMU MPU6050 y finales de carrera; Llerena y Salazar: servos de bus LX-15D/LX-225 con ángulo, voltaje y temperatura; Monroy Moya: OLED e infrarrojos; Ntambara: lazo abierto; Capaldi: ángulo a 20 lecturas por segundo por ESP-NOW.

**Agarre (S5).** Monroy Moya (infrarrojo en la pinza, implementado); Oliveira et al. 2021 (vacío, fibra óptica, fuerza; Lehnert 2017, Mu 2020, Rong 2021); Rangarajan y Bianchini (lazo abierto; fuerza de contacto como trabajo futuro); Aucapiña e Iza (cita a Campos 2016, táctil). Intisar no aparece.

**Visión y control separados (S6).** Ver Tabla 4. Monroy Moya cita además a Intisar 2021, Abdullah-Al-Noman 2022, Lahoti 2021, Kumar 2021 y Cong 2021.

**Alimentación (S7).** Ntambara 12 V y 2 A, pico 1,92 A, caída 0,46 V, secuencial (holgura: repetibilidad angular 0,41 ± 0,23° y posicional 2,47 ± 0,58 mm, 10 ciclos, 0,8 kg); Lim (caídas de 5 a 0 V con `Servo.h`); Yilmaz (relés, PC817, ACS712, fusible 4,2 A, tierra en estrella); Aucapiña e Iza (LM2596); Kumar (LiPo 7,4 V a 6 / 5 / 3,3 V). Ninguna mide el efecto del movimiento secuencial en el tiempo de ciclo.

**Diseños abiertos (S8).** Bansal et al. (2022), cap. 15, Narmadha, Anbarasi Jebaselvi y Anitha, pp. 191-212 (brazo de 4 GDL, corte láser y Arduino abierto, error menor a 1 %); Markvicka: kit abierto menor a 200 USD (MG996R, ATmega328, PCA9685).

**Zuiev et al. (2024).** DOI 10.15587/2706-5448.2024.297339; revista *Technology Audit and Production Reserves*, 1(2(75)), 31-37 (sin verificar). Vehículo 4WD. Usable: parada forzada si no llegan paquetes (3.4), S.BUS de un solo sentido (3.1), retardos internos del ESP32 de microsegundos. **No usar** los «60-80 ms frente a 10-20 ms» como latencia inalámbrica (es conversión del receptor). No mide BLE.

**Kumar et al. (2026).** DOI 10.14741/ijcet/v.16.1.4; páginas sin verificar (Perplexity dijo 16-19). Revista de nivel bajo; vehículo, no brazo. Latencia de ida y vuelta 38 / 62 / unos 120 ms con señal fuerte / moderada / débil; éxito 99,6 / 97,2 / 96,1 %. 30 m × 20 m medido; los «30-100 m» son un rango estimado. Solo Bluetooth clásico (HC-05 y HC-06).

**Ntambara et al. (2026).** El primer autor es Ntambara (no Furaha). Revista, volumen y DOI sin verificar (Perplexity: *Discover Robotics*, 2, artículo 17, DOI 10.1007/s44430-026-00032-6). No afirma que el movimiento secuencial alargue el tiempo de ciclo.

**No citadas.** Bera (2026, Electronics For You; video https://www.youtube.com/watch?v=PHznMxfTjuo), Future Internet 18(6), 325 y TeleopLab (arXiv 2509.05547).

## 5. Discrepancias abiertas (resolver con los PDF)

- Suhaeb: el informe dice 85 a 92 ms; S4 dice 85 a 110 ms con hasta 10 usuarios.
- Monroy Moya: 2024 (referencia y casi todo el informe), 2025 (S4 y S5) o 2026 (1.1 y S0). Unificar.
- Las dos tesis (ESPE con uArm, Aucapiña e Iza; UPS con xArm 1S, Llerena y Salazar) se mezclaron en NotebookLM y Gemini; el informe usa la atribución propia; confirmar.
- Intisar: «sigue la rutina aunque el objeto se caiga» quedó `[verificar]` en la Tabla 5.
- Atribuciones por inferencia (Gemini): aforo de la UPS (Llerena y Salazar, p. 4) y 36 participantes (Markvicka).
- Dang: MQTT o Blynk; ruta de visión por USB (inferencia) y número del volumen; modelo de cámara.
- Metadatos sin verificar: Ntambara, Zuiev, Oliveira (autores y año), Wu (autores), Cho y Vieira (títulos), Kumar (páginas), Gunardi, Fernández Panadero, Medel (revista), Capaldi y Shah (revista y DOI), orden de autores de Shah.

## 6. Pendientes

Lista completa y viva en `bitacora_22.md` (bloques A a F). Orden recomendado:

1. **Verificar en los PDF** (prompts V1 a V11, sección 7) y aplicar el resultado al informe con `informe 10.md`.
2. **Perplexity** (A3 PID, A4 definiciones de IA, A5 aforo, A6 aprendizaje activo, metadatos B).
3. **Tareas del usuario:** institución, carrera, asignatura, docente y fecha; costo real del montaje; confirmar con el docente el formato APA y qué significa «sustentar»; ver el video o la página de Pybricks (motores simultáneos y alimentación); verificar los README de los cuatro proyectos abiertos; opcional pero recomendado, medir el retraso orden-movimiento o hacer la prueba mínima de HSV para dar cifras propias al 4.4.
4. **Prioridad 3 (formato y limpieza):** reordenar las letras de Pybricks por título (a = BLE broadcast, b = Mediciones, c = Motor, d = Robotic arm, e = Use your phone; hoy *Robotic arm* es s. f.-a); quitar material interno (bloque «Estado del borrador», notas «Verificar contra los trabajos completos», línea meta de 3.3 y fila «Ambiental»); figuras 1 y 2 como diagramas reales; formato APA 7 de tablas y figuras; acrónimos que sobran; frase repetida de *smart sensors* en 1.1; «Autor pendiente» de Tampere y JRC; compactar 1.1; aclarar cómo aplica la fórmula de 4.1.3 a un brazo sin hombro; aclarar en 2.3 cuántos de los 31 trabajos son PDF y cuántos proyectos web; sumar Dang y Capaldi a la Tabla 5 si aportan.

## 7. Prompts listos para pegar

**Cierre común (NotebookLM o Gemini), al final de cada pregunta:** *Responde solo con lo que está en las fuentes. Indica archivo PDF exacto (no «Fuente N»), autor, año y página o sección. Si no está, escribe 'no está en las fuentes'. No inventes.* No nombrar secciones del informe (el cuaderno no las ve).

**V1 (Suhaeb).** Sobre Suhaeb y Risal (2024): ¿el tiempo de respuesta de los botones es de 85 a 92 ms o de 85 a 110 ms con hasta 10 usuarios? Copia el pasaje y la tabla, y dame revista, volumen, número, páginas y año.

**V2 (Monroy Moya).** Sobre el trabajo de Monroy Moya et al. (visión con Raspberry Pi 4 y brazo de 3 GDL): año, revista, volumen, número, fechas de recepción y publicación, y DOI.

**V3 (tesis ESPE).** Sobre `T-ESPEL-MEC-0165.pdf` y `ESPEL-MEC-0165-P.pdf`: ¿son la misma tesis? Año y sede; brazo usado; página donde dice que el número limitado de módulos dificulta el aprendizaje; datos de 97,28 %, 84,28 %, 38 a 50 ms y el costo de 2075 USD, con página de cada uno.

**V4 (tesis UPS).** Sobre la tesis con el Hiwonder xArm 1S (Llerena y Salazar): universidad, sede, año; copia el pasaje del aforo limitado por la pandemia y las prácticas virtuales con brazos KUKA, con su página.

**V5 (Intisar).** Sobre Intisar et al. (2021): título exacto, autores, revista, volumen, número, páginas y DOI; copia el pasaje donde dice que el brazo sigue la rutina aunque el objeto se caiga, si existe; confirma el costo de unos 80 USD y si menciona sensores de agarre.

**V6 (Markvicka).** Sobre Markvicka et al. (2023): confirma los 36 estudiantes, que las calificaciones no difirieron de forma significativa entre tareas tradicionales y con el brazo, la encuesta (n = 35, 78 %), los 30 000 USD de un brazo industrial y los 1000 USD de los kits, con sección de cada dato.

**V7 (sin metadatos).** Para `2010S03C01.pdf`, `2402.17243v1.pdf`, `30-100-1-SP.pdf`, `978-3-642-32527-4_17.pdf` y `P-00W-KW7.pdf`: autores, año, título, revista o editorial y DOI, según la primera página.

**V8 (Ntambara).** Sobre `s44430-026-00032-6.pdf`: revista, volumen, número o artículo, DOI, y nombres e iniciales de los cuatro autores en el orden de la portada.

**V9 (varios).** Revista o editorial, páginas, año y autores que falten de: Zuiev et al., Kumar et al., Wu y colaboradores (Penn State Erie), Medel, Gunardi y Jumadri, y Fernández Panadero et al.

**V10 (Narmadha).** Capítulo 15 de Bansal et al. (2022): autores, título del capítulo, páginas exactas y DOI.

**V11 (residuales de las tres fuentes nuevas).** (a) `1451-20922601093T.pdf` (Dang): número del volumen, modelo de la cámara y, si el texto lo dice, cómo llegan los ángulos al ESP32 en la tarea de visión. (b) `peerj-cs-10-1826.pdf` (Capaldi): revista, volumen y DOI; valores de los segmentos 2 a 4 de la Tabla 2; tamaño del modelo YOLOv8 usado. (c) `epjconf_staaar2026_01001.pdf` (Shah): autores en el orden de la portada, revista, DOI, y si el ESP32 actúa como punto de acceso Wi-Fi con una página de sliders.

**Cierre común (Perplexity):** *Para cada fuente dame autor(es), año, título, revista o editorial, DOI o URL, y página o sección. No inventes; si no puedes confirmar un dato, escribe no confirmado.*

**P-A3 (PID).** Libros, apuntes universitarios o revisiones que definan el control PID y el término integral y su efecto sobre el error en estado estacionario, de preferencia con servomotores o brazos educativos y acceso abierto.

**P-A4 (definiciones).** Libro, survey u organismo reconocido que defina inteligencia artificial, aprendizaje automático, red neuronal artificial y detección de objetos en visión por computadora.

**P-A5 (aforo y práctica a distancia).** Laboratorios remotos con brazos o robots educativos que mencionen el aforo o los equipos limitados; buscar en especial *Benitez et al. (2020), Design of an affordable IoT open-source robot arm for online teaching of robotics courses during the pandemic contingency, HardwareX 8*.

**P-A6 (aprendizaje activo).** Meta-análisis o estudios con cifras de aprendizaje activo frente a pasivo en ingeniería o ciencias, y estudios de que los modelos físicos enseñan fricción u holgura.

**P-B (metadatos).** Autores del JRC 2026 («Low cost single camera robotic arm for vision guided pick and place») y del proyecto de Tampere («LEGO con Raspberry Pi y OpenCV»); revista de Fernández Panadero 2010, Gunardi y Jumadri 2020 y Medel; autores de Wu et al. 2014 y de Oliveira et al. 2021; revista, volumen y DOI de Capaldi (2024) y de Shah y Arockia Doss (2026); títulos de Cho et al. (2014, DOI 10.3390/s150100059) y de Vieira y Rizzetti (2025, DOI 10.5753/errc.2025.17688).

**P-Opcionales.** Detectores livianos (YOLO nano, MobileNet), rojo contra café en HSV, comunicación de un solo sentido.
