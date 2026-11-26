# Resumen 22 de noviembre de 2026: revisión y refinamiento de `informe.md`

**Hora de inicio de sesión:** 18:39 (sesión 1), 20:06 (sesión 2; los tokens se reestablecen a las 01:06) y 21:43 (sesión 3, worker `alx_gml`; los tokens se reestablecen a las 02:43) y 23:25 (sesión 4, skill 2 plan, worker `alx_hot`; los tokens se reestablecen a las 04:25)
**Bitácora de pendientes:** `bitacora_22.md` (estado vigente de lo que falta)
**Objetivo del día:** refinar el primer borrador completo del informe (`informe.md`, secciones 1 a 6) y dejarlo listo como trabajo investigativo. Se corrige por una lista de pendientes ordenada por prioridad, de a uno.

---

## 1. Qué es este trabajo

Informe universitario de una materia investigativa:
**"Control de un brazo robótico educativo mediante visión por computadora e IA: revisión de antecedentes y propuesta de integración con un prototipo LEGO"**.

- Es un informe **puramente teórico / documental**. No presenta resultados de IA sobre el brazo.
- Se basa en otros papers y tesis del tema. El sustento del trabajo son esos antecedentes.
- El prototipo base (LEGO Inventor 51515 + Pybricks + ESP32 con página web servida por el propio ESP32) ya funciona y se entrega en otra materia. Es la base sobre la que se **propone** la arquitectura de IA: un módulo externo de visión que envía órdenes a las rutas web del ESP32.
- Idioma: español, directo. Si hay dudas, preguntar antes de escribir.

## 2. Esquema del docente (respetar orden y títulos)

1. **Introducción y antecedentes:** indicar brevemente los antecedentes y el propósito general del trabajo.
2. **Objetivo:** indicar el alcance o la profundidad del estudio y sus limitaciones.
3. **Justificación del proyecto:**
   - Por qué el estudio es importante para la institución y cuál es el escenario del proyecto.
   - Dice **por qué** se quiere hacer la investigación y **qué impacto** se busca lograr cuando termine (científico, tecnológico, económico, social, ambiental u otro).
   - Responde: **¿para qué servirá?**
4. **Desarrollo del proyecto:** incluye los conceptos teóricos en los que se fundamenta (**marco teórico**).
5. **Conclusiones y recomendaciones.**
6. **Referencias bibliográficas e internet.**
- **Al final:** nota o sección titulada **"Guía resumen del manual de publicaciones con normas APA"** y un **anexo** con la lista de acrónimos.

## 3. Cómo estamos trabajando (flujo de fuentes)

1. **Perplexity** (Deep Research, foco Académico) entregó las fuentes: tesis y papers.
2. Las fuentes se descargaron y se cargaron en **NotebookLM** (26 PDF), que es la base del informe. NotebookLM extrajo los puntos por tema y se hizo un inventario.
3. Con esas extracciones y el esquema del docente se escribió el **primer borrador completo** (`informe.md`).
4. Ahora se refina: revisión del borrador, lista de pendientes por prioridad y corrección uno por uno.
5. Antes de entregar hay que **verificar cada dato contra el PDF original** (hasta hoy las citas salen de extracciones de NotebookLM, no de una lectura completa).

**Reglas de trabajo**

- **No inventar datos.** Lo no verificado se marca `[verificar]`, `[pendiente]` o "s. f.".
- Estilo de citas: **APA 7**, `(Autor, año)`. Aún no es definitivo; confirmar con el docente.
- Antes de reescribir archivos grandes: avisar **"cambios masivos, bk necesario"** y esperar la copia de respaldo.
- Respaldos del informe: `informe 1.md` a `informe 9.md` (el 5 y el 6 son el estado al inicio de la sesión 2; el 7 es posterior al lote 1; el 9 es el estado justo antes del lote 4). Antes de otro cambio masivo: `informe 10.md`.
- Las preguntas pendientes para NotebookLM (A1 a A18), Perplexity (B1 a B10) y las tareas propias (C1 a C6) están en el contexto de sesión; se irán trayendo de a poco según la prioridad. El estado vigente de lo que falta está en `bitacora_22.md`.

## 4. Decisión sobre "sustentar la implementación de IA"

La sección 3.2 dice que la materia "requiere sustentar la implementación de IA". Criterio actual (**a confirmar con el docente**): el sustento puede ser **teórico-documental**, nombrando los trabajos (papers y tesis) en los que se basa la propuesta, y adjuntando los **enlaces de los videos** de esos trabajos cuando existan. Por eso la sección 4.4 se renombraría a algo como "Estado del prototipo y plan de validación" y no se hace prueba de concepto, salvo que el docente la pida.

- Pendiente: encontrar y verificar los enlaces de video de los trabajos citados `[verificar]`.
- Opción de respaldo si el docente pide algo implementado: detección HSV de la pelota y el cubo desde foto o video, centroide y ángulos predichos por la tabla de calibración, sin mover el brazo.

## 5. Revisión del borrador (22-nov)

**Veredicto:** cumple el esquema (secciones 1 a 6 en orden, guía APA y anexo al final). Sólido en antecedentes y marco teórico. Flojo en: coherencia de la propuesta (4.3), metodología de la revisión, fundamentos de IA y datos sin verificar.

### Prioridad 1: errores de fondo o contradicciones (se corrigen primero, de a uno)

1. **Cámara y módulo de IA: tres versiones distintas.** Tabla 1 (cámara = celular conectado al hub), sección 4.1.6 (versión con cámara de celular, tablas con interpolación) y sección 4.3 (cámara con PC o Raspberry Pi hacia el ESP32). Fijar una sola arquitectura y explicar cómo convive el Bluetooth del hub (emisión del ESP32 frente a la cámara del celular).
2. **Sección 4.1.8 dice que no hay mediciones de latencia BLE en las fuentes,** pero Tzompantzi et al. (2019) tiene una tabla de tiempos de respuesta (A4). Verificar. También aclarar si los 40 m son de Wi-Fi, BLE o ambos.
3. **Conclusión 1: rango de acierto 84 % a 94,6 %,** pero 4.1.7 y la Tabla 3 reportan 97,28 %; además el 84 % es "confiabilidad global" (otra métrica).
4. **Conclusión 3: dice "comparable"** a técnicas más pesadas, pero la Tabla 3 y las limitaciones dicen que las cifras no son comparables. Suavizar o quitar.
5. **Medición con sniffer (Pybricks, s. f.-e):** fue con un City Hub, firmware 4.1.0b2, no con el 51515. 4.3 la generaliza a "unos 10 mensajes por segundo". Aclarar.
6. **"Brecha" (1.1) demasiado fuerte:** el proyecto de Pybricks con SPIKE Prime y cámara de celular, y *smart sensors*, ya usan el celular como cámara de un hub LEGO. La novedad real es la página web del ESP32 más un módulo de IA externo.
7. **"La pelota y el cubo" aparecen en 4.3 y 5.3 sin haber presentado la tarea.** Describirla en 3.2 o 4.2.
8. **Verificar contra los PDF (C1, A1 a A14):** autores del JRC (B1), título y autores de Intisar, año de Aucapiña y Monroy Moya, revista de Gunardi, Fernández y Medel, páginas de Tzompantzi.

### Prioridad 2: rigor investigativo y esquema

- Datos de institución, carrera y asignatura (cabecera, 3.1 y 3.2) (C2).
- Subsección corta de **metodología de la revisión** (cómo se buscaron las fuentes y criterios). Conciliar "26 fuentes" con las 28 referencias (las dos tesis ESPE pueden contar como dos archivos, A2).
- **4.1.7:** definir IA, aprendizaje automático, red neuronal y detección de objetos (MobileNet, YOLO).
- Apoyos débiles: el PID y el control de posición (4.1.4) se apoyan en un robot de rehabilitación (Eiammanussakul) y falta cita para el término integral (usar B2); verificar que Pybricks (s. f.-b) respalde que el 51515 corre Pybricks (4.1.2); verificar "aprendizaje activo más efectivo" y "aforo reducido" (3.1 y 3.2).
- Costo real del montaje (C3) y fuente de "diseños modulares abiertos" (A18).

### Prioridad 3: formato APA y limpieza

- Letras de Pybricks (s. f.-a a s. f.-e) según el orden alfabético del título: BLE broadcast, Mediciones, Motor, Robotic arm, Use your phone.
- Fuentes sin autor (Tampere, JRC): título en la posición del autor; sin "[Autor pendiente]" (B10).
- Quitar material interno: bloque "Estado del borrador", notas "Verificar contra los trabajos completos", líneas meta de 3.3 (fila "Ambiental: omitir").
- Figuras 1 y 2 como diagramas reales; formato APA 7 de tablas y figuras.
- Confirmar con el docente el formato de la guía APA (C4).
- Anexo de acrónimos: agregar RGB, DC-DC; revisar los que sobran.

### Prioridad 4: opcional

- Medir el retraso orden-movimiento del prototipo (C5).
- Fuentes extra de Perplexity (B4 a B9): LEGO y BLE, comunicación de un solo sentido, detectores livianos, HSV con rojo y café.

## 6. Estado del prototipo (referencia, de `resumen_21.md`)

- Arquitectura: celular → Wi-Fi (red propia `BRAZO_LEGO`, página en `192.168.4.1`) → ESP32 (`esp32/web_control.py`, guardado como `main.py`) → BLE broadcast de Pybricks, canal 1, tupla `(articulacion, angulo, id_orden)` → hub (`ha9.py`, modo R) → motores.
- Un motor a la vez; vigilancia de voltaje (pausa bajo 5500 mV); límites de ángulo en el hub; órdenes durante un movimiento se descartan.
- Rutas web del ESP32: `/s` (slider), `/go` (accionar), `/pos`, `/cero`.
- Sin canal de vuelta hub → ESP32; retraso "mínimo" pero no medido; falta recalibrar ángulos negativos.

## 7. Registro de avance de la sesión

- [x] Lectura de `informe.md` y `resumen_21.md`.
- [x] Revisión contra el esquema y lista de prioridades (sección 5).
- [x] Decisión provisional sobre "sustentar" (sección 4).
- [x] Prioridad 1, punto 1: cámara y módulo de IA. **Decidido: opción A (PC + ESP32)**; Tabla 1, 4.1.6 y 4.3 reescritas (sección 9).
- [x] Prioridad 1, puntos 2 a 7 aplicados al informe (sección 9). El punto 8 (verificar contra los PDF, C1) sigue abierto.
- [~] Prioridad 2 parcial (conciliación de fuentes, método de la revisión, definiciones de IA con cita pendiente, aforo y aprendizaje activo corregidos); quedan datos de institución, costo real y citas de PID e IA. Prioridad 3 y 4 sin hacer (sección 9).
- [x] Lote 4: Dang, Capaldi y Shah integrados al informe, con la brecha reformulada (sección 9).
- [x] Bitácora de pendientes creada: `bitacora_22.md`.
- [ ] Verificación contra los PDF (C1), Perplexity A3 a A6 y B, prioridades 3 y 4, y prueba mínima para 4.4: ver `bitacora_22.md`.

## 8. Decisión: arquitectura de la propuesta = opción A (PC + ESP32)

**Arquitectura única para el informe:** cámara USB/webcam en la PC → módulo de visión/IA en la PC (Python + OpenCV, luego detector profundo) → Wi-Fi (HTTP, rutas `/s` y `/go`) → ESP32 → BLE broadcast Pybricks → hub 51515 → motores. Se descarta la cámara del celular conectada al hub (*smart sensors*, `ha7.py`) como parte de la propuesta; queda solo como antecedente del proyecto. El celular queda como interfaz manual (la página web).

**Resumen del prototipo `ha9.py` (palabras del usuario):** Pybricks + hub + ESP32 + celular. Desde la página web, con un slider, se manda al ESP32 cuándo y cuánto mover un motor; se mueve un motor a la vez; funciona bien; el ESP32 recuerda el ángulo anterior de cada motor al volver a una articulación (es el ángulo *ordenado*, no el alcanzado).

### Antecedentes encontrados para la opción A (web, 22-nov) `[verificar contra el PDF]`

**Estado (sesión 3):** Dang, Shah y Capaldi ya están cargados en NotebookLM, verificados en parte (N22 a N24) y citados en el informe (sección 9, lote 4). Bera y las dos fuentes "por revisar" no se citan.

1. **Dang, Van, Nguyen, Nguyen, Tran, Huynh, Phi, Vo y Vo (2026)** (orden de nombres vietnamitas por confirmar; autor de correspondencia Vo Duy Cong). *Development of an educational robotic platform with dual control interfaces and intelligent computer vision-based interaction*. FME Transactions, 54(1), 93-106. DOI en el PDF: 10.5937/fme2601093P. Brazo de 4 GDL con ESP32, YOLOv12 corriendo en una laptop (solo CPU), ángulos enviados al controlador. Interfaz web (el resumen dice MQTT; la sección 2 dice Blynk: contradicción interna del artículo). PDF: https://scindeks-clanci.ceon.rs/data/pdf/1451-2092/2026/1451-20922601093T.pdf
2. **Shah y Arockia Doss (2026).** *Development of service robot manipulator for pick and place applications in domestic environment*. EPJ Web of Conferences, 355, 01001. DOI: 10.1051/epjconf/202635501001. ESP32 como punto de acceso Wi-Fi con página de sliders (igual que el prototipo), latencia menor a 150 ms, parada de emergencia en el navegador, YOLOv8-OBB y ROS/MoveIt **en simulación**. Tiene un video del modelo físico (Fig. 6, archivo .mp4 dentro del artículo). PDF: https://www.epj-conferences.org/articles/epjconf/pdf/2026/11/epjconf_staaar2026_01001.pdf
3. **Capaldi (2024).** *A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol*. PeerJ Computer Science, 10, e1826. DOI: 10.7717/peerj-cs.1826. Robótica educativa (VEX V5) + ESP32 + PC con visión (YOLOv8); mide distancia, tiempo de ida y vuelta y detección; incluye ajuste de PID. Análogo directo de hub cerrado + ESP32 + PC. https://peerj.com/articles/cs-1826
4. **Bera (2026, 1 de octubre).** *Computer-vision-based robotic arm*. Electronics For You (revista, no revisada por pares; parte del texto es de acceso con registro). Laptop, Raspberry Pi 5 o servidor GPU hacen la visión; el ESP32 hace el control en tiempo real; comunicación por Wi-Fi, Ethernet o serial (y ESP-NOW). **Video de la prueba de concepto:** https://www.youtube.com/watch?v=PHznMxfTjuo. Página: https://www.electronicsforu.com/electronics-projects/computer-vision-based-robotic-arm
5. Por revisar (no verificados): *Development and experimental validation of an educational robotic platform with machine vision and web-based monitoring for automation teaching*, Future Internet, 18(6), 325 (https://www.mdpi.com/1999-5903/18/6/325); TeleopLab (arXiv 2509.05547), interfaz de celular para laboratorios remotos (posible apoyo de la afirmación de "aforo reducido" de 3.2).

### Cambios previstos en `informe.md` (HECHOS: Tabla 1, 4.1.6 y 4.3 en la sesión 2; las filas de Dang, Shah y Capaldi en el lote 4 de la sesión 3, una vez cargadas las fuentes)

- **Tabla 1:** fila de LEGO Ideas y Pybricks sin "aquí la cámara es un celular"; agregar filas de Dang et al. (2026), Shah y Arockia Doss (2026) y Capaldi (2024).
- **4.1.6:** quitar el párrafo de "versión con cámara de celular" o pasarlo a una nota; el método de tablas con interpolación pasa a ser una opción de la PC.
- **4.3:** una sola arquitectura (cámara en PC); aclarar la convivencia del Bluetooth del hub (solo emisión del ESP32; el hub conectado a la PC degrada `observe` según Pybricks, s. f.-e) `[pregunta abierta]`.
- Referencias: agregar las fuentes nuevas en APA 7 una vez verificadas.

## 9. Registro de la sesión 2 (20:06; skill 2 plan, worker `alx-rul`)

**Herramientas.** NotebookLM se quedó sin tokens: se usa Gemini con el cuaderno `iaarm` (https://gemini.google.com/notebook/df4a68df-58fe-4c26-9070-2cfa24b4f409), que da menos metadatos (casi siempre sin autor ni año y con «Fuente N»). Pedirle siempre que identifique cada fuente por el nombre del archivo PDF; lo que salga de ahí se atribuye por inferencia y se marca `[verificar]`. Perplexity sigue para fuentes externas. Los cambios se hicieron con `edit_file` por lotes, cada uno tras un respaldo del usuario.

**Lote 1 (respuestas S0 a S8 de NotebookLM; bk `informe 6.md`).**
- Prioridad 1, puntos 1 a 7: arquitectura única (cámara USB en PC, Wi-Fi al ESP32, BLE de difusión al hub; celular solo manual); BLE medido solo con RSSI y 50 a 60 ms solo de Wi-Fi; conclusión 1 con 84 % a 97,28 % como métricas distintas; conclusión 3 sin «comparable»; sniffer con City Hub 4.1.0b2; brecha suavizada; tarea de pelota roja, base café y cubo descrita en 3.2.
- Nuevo: 2.5 método de la revisión; 28 trabajos distintos en 29 archivos; límites de alimentación en 4.1.4; definiciones de IA en 4.1.7 (cita pendiente); Kumar en 4.1.8; 4.1.9 con la Tabla 4 (visión separada del control); limitaciones pasan a Tabla 5; retorno, alimentación secuencial y parada por pérdida de enlace en 4.3; prueba preliminar en 2.4 y 4.4; agarre y cerrar el lazo en 5.3; diseños abiertos (Narmadha y Markvicka) en la Tabla 5; cinco referencias nuevas (Kumar, Narmadha, Ntambara, Oliveira, Zuiev) y acrónimos DC-DC, RGB, RSSI, UART, MQTT.

**Lote 2 (Perplexity A1, A2, A8; bk `informe 7.md`).**
- A1: solo la página del proyecto de Pybricks *Robotic arm with vision* (SPIKE Prime, celular como *smart sensor*, objeto rojo; autor Laurens Valk sin confirmar). No confirma batería ni motores simultáneos. Se quitó la frase de los videos con batería de 1.1 y 4.3 (queda `[pendiente]`).
- A2: sin tesis ni artículo arbitrado con la cadena completa. Cuatro proyectos abiertos con partes (Johnson 2026, osullivp 2021, GC-TO 2026, Anton's Mindstorms 2025) agregados a 1.1, Tabla 1, brecha, conclusión 1 y referencias. Verificar los README.
- A8: sin medición publicada de latencia de un paquete BLE en broadcast de ESP32; Cho et al. (2014) como modelo y Vieira y Rizzetti (2025, 44 y 85 ms, sistema en sentido contrario) agregados a 4.1.8 con títulos pendientes.

**Lote 3 (Gemini A3 a A7).**
- A3 y A4: no hay definición de PID ni de IA en las fuentes; solo definiciones parciales de aprendizaje automático, red neuronal y detección de objetos sin autor. Quedan como `[cita pendiente]`.
- A5: aforo limitado por pandemia en la UPS Guayaquil (Llerena y Salazar, 2022, por inferencia) y módulos limitados en la ESPE (Aucapiña e Iza, 2019). 3.2 y 3.3 corregidos; se quitó a Tzompantzi de esa afirmación.
- A6: sin meta-análisis. 3.1 reescrito y 1.1 corregido (Markvicka: 36 estudiantes, sin diferencia significativa en notas).
- A7: sin antecedente de tabla píxeles a ángulos con interpolación lineal; frase añadida en 4.1.6.

**Discrepancias abiertas (C1).** Suhaeb 85 a 92 ms frente a 85 a 110 ms; año de Monroy Moya (2024, 2025 o 2026); las dos tesis se mezclaron en NotebookLM y Gemini; Intisar sin sensores de agarre en las fuentes; metadatos sin verificar de Ntambara, Zuiev, Oliveira, Wu, Cho, Vieira, Kumar, Gunardi, Fernández Panadero y Medel.

**Pendientes.** (1) Perplexity: A3 (PID), A4 (definiciones de IA), A5 con *Benitez et al. (2020), HardwareX 8*, A6 (meta-análisis), metadatos B y opcionales; los prompts están en `contexto22.md`, sección A.6. (2) Usuario: C1 a C5, mirar el video o la página de Pybricks, verificar los README de los cuatro proyectos abiertos. (3) Prioridad 3 sin hacer: letras de Pybricks por título, material interno, figuras, formato de tablas, acrónimos y la frase repetida de *smart sensors* en 1.1. (4) Dang, Shah y Capaldi: resuelto en el lote 4 (más abajo).

**Lote 4 (sesión 3, worker `alx_gml`, inicio 21:43; NotebookLM N22 a N24 y N24b, Gemini N22b; bk `informe 9.md`).** NotebookLM llegó a su límite de consultas; N22b se corrió en Gemini (atribución por inferencia, `[verificar]`).
- **Dang et al. (2026)** (`1451-20922601093T.pdf`): nueve autores en el orden de la portada; FME Transactions 54, pp. 93-106, DOI 10.5937/fme2601093P; el número no aparece en el PDF. MQTT en el Abstract y en 3.3 (las órdenes de la web llegan al ESP32 como mensajes MQTT); Blynk solo en la sección 2. YOLOv12 corre en una laptop solo con CPU (el entrenamiento fue en Colab con GPU). Flujo: caja delimitadora, transformación calibrada de 2D al espacio del robot, cinemática inversa, ESP32, PCA9685 y servos MG996R. Gemini: sin mAP, sin tiempo de inferencia, sin tasa de éxito ni tiempo de ciclo (validación cualitativa), calibración solo mencionada como "transformación calibrada"; ruta de visión por USB (inferencia, `[verificar]`).
- **Capaldi (2024)** (`peerj-cs-10-1826.pdf`): VEX V5 con dos ESP32 (ESP-NOW) y RS-485; cámara OpenMV H7 por USB a una PC con YOLOv8 en Python. Pérdida de paquetes menor a 1 % de 0 a 40 m y 13,2 % a 60 m (recomienda 40 m o menos para lazo cerrado). Ida y vuelta de 187 ms (DE 57 ms); los segmentos 2 a 4 de la Tabla 2 no estaban en los fragmentos cargados, pero lo faltante cuadra con el total. 30 pruebas de clasificación (10 por condición). Inferencia de YOLOv8: 62,8 ms (Ryzen 9 5950X), 52,1 ms (Apple M2) y 8,41 ms (Quadro P2200). PID: interfaz con Kp, Ki y Kd y retorno del ángulo a 20 lecturas por segundo.
- **Shah y Arockia Doss (2026)** (`epjconf_staaar2026_01001.pdf`): WebSockets con ESP32 (ESPAsyncWebServer), latencia menor a 150 ms sin método de medición, parada de emergencia en el navegador (5.2.3); YOLOv8-OBB y ROS/MoveIt solo en simulación (Gazebo y RViz); el brazo físico (MG996R) es manual.
- **Cambios en `informe.md`:** 1.1 (visión con ESP32 y control remoto); brecha reformulada (la novedad no es la cámara, ni la PC con visión, ni el puente por separado, sino la combinación con el hub 51515 y Pybricks, la página del ESP32 y el módulo externo); Tablas 1, 3 y 4; 4.1.4 (PID de Capaldi), 4.1.7 (inferencia), 4.1.8 (187 ms, pérdida de paquetes, 150 ms) y 4.1.9; 4.3 (enlace inalámbrico y canal de vuelta); conclusiones 1, 3 y 5; recomendación 4; 2.3 (31 trabajos en 32 archivos) y 2.5 (Gemini); tres referencias y acrónimos CPU, GPU, ESP-NOW y RS-485.
- **Siguen `[verificar]`:** número y apellidos de Dang, ruta de visión por USB, revista y DOI de Capaldi y Shah, orden de autores de Shah, tamaño del modelo YOLOv8 y modelo de cámara de Dang.

## 10. Lo logrado hasta ahora (cierre parcial de la sesión 3)

- `informe.md` incorpora los lotes 1 a 4: arquitectura única (PC con visión, Wi-Fi al ESP32, BLE de difusión al hub), correcciones de fondo de la prioridad 1, método de la revisión, límites de alimentación, separación entre visión y control (Tabla 4), antecedentes de proyectos abiertos y los tres trabajos nuevos (Dang, Capaldi, Shah).
- La brecha se reformuló con cautela: ya existen PC con visión y ESP32 en plataformas educativas, hubs LEGO con cámara y ESP32 como puente hacia Pybricks; no se halló la cadena completa.
- Respaldos `informe 1.md` a `informe 9.md` y `resumen_22 1.md`; siguiente respaldo: `informe 10.md`.
- Bitácora de pendientes en `bitacora_22.md` (verificación en los PDF, Perplexity, tareas del usuario, discrepancias y ediciones).
- Lo más importante que falta: verificar los datos clave contra los PDF (C1: Suhaeb, Monroy Moya, las dos tesis, Intisar, Markvicka), cerrar los metadatos, datos de institución y costo, la prioridad 3 (formato y limpieza) y, si se puede, una prueba mínima o la medición del retraso para dar cifras propias al 4.4.

---

## 11. Registro de la sesión 4 (23-nov-2026; inicio 23:25; skill 2 plan; worker `alx_hot`): imágenes del informe

**Alcance.** Solo se trabajó la parte de imágenes. Claude no editó `informe.md` en esta sesión: el usuario insertó a mano las imágenes provisionales. No se creó `informe 10.md`. Se leyó `informe_img.md` (propuesta de 19 fichas con ubicación, fuente y pie APA) y no se modificó. Se comprobó que los 19 párrafos de anclaje de `informe_img.md` siguen siendo texto vigente de `informe.md`.

**Decisión del usuario al cierre:** por ahora no se aplica ninguno de los cambios señalados abajo; quedan como pendientes en `bitacora_22.md` (sección G y ediciones nuevas en A y E). Las imágenes quedan como provisionales: varias sin pie ni número.

### 11.1 Núcleo de figuras propuesto (de `informe_img.md`)

- **Núcleo (11):** fichas 2 (brecha), 3 (escena de la tarea), 4 (brazo rotulado), 9 (secuencia HSV), 13 (Capaldi, ida y vuelta y pérdida de paquetes), 15 (arquitecturas de Capaldi y Dang), 16a y 16b (prototipo base: diagrama y captura o foto), 17 (arquitectura propuesta), 18 (secuencia de la tarea) y 19 (prueba preliminar).
- **Opcionales:** 6 (cinemática, redibujo de Mohammed), 7 (PID de Capaldi), 14 (RSSI de Tzompantzi), 10 (montaje ArUco), 12 (red neuronal y YOLO), 5 (modo difusión de Pybricks). **Descartar:** 1, 8 y 11 (dependen de páginas web o PDF con licencia poco clara o aportan poco). **Idea nueva (no está en el archivo):** una ficha 20 con un diagrama de flujo del método de la revisión en 2.5.
- Las propias (3, 4, 16b, 19) salen de dos sesiones: una de fotos del montaje y una de capturas. Las fichas 9 y 19 dependen de la prueba mínima C-6.

### 11.2 Fuentes de figuras verificadas en la web (23-nov)

| Fuente | Figuras útiles | Licencia | Enlace |
| ------ | -------------- | -------- | ------ |
| Capaldi (2024), PeerJ CS 10:e1826 | Fig. 1A (cámara por USB a la PC y PC a VEX por ESP-NOW), Fig. 4A/B (camino del mensaje y osciloscopio), Tablas 2 y 3, Fig. 7B (detección YOLOv8), Fig. 14B (PID, objetivo de 45°) | CC BY 4.0 (PDF) | https://peerj.com/articles/cs-1826 ; copia: https://pmc.ncbi.nlm.nih.gov/articles/PMC10909231 |
| Mada Sanjaya et al. (2018), JPCS 1090, 012070 | Fig. 3 (captura, HSV, binaria y objeto marcado); otra figura con coordenadas por color; tabla de calibración y red de 20 neuronas (números de figura sin verificar) | CC BY 3.0 | https://iopscience.iop.org/article/10.1088/1742-6596/1090/1/012070 |
| Rangarajan y Bianchini (2026), AJSR 4(6), 74-88 | Fig. 1 (montaje con cámara cenital, ArUco y contenedores), Fig. 3 (pose del ArUco) | CC BY 4.0 (versión publicada; arXiv es el manuscrito aceptado) | https://arxiv.org/pdf/2608.15968 |
| Shah y Arockia Doss (2026), EPJ Web Conf. 355, 01001 | Fig. 7 (interfaz web con sliders); Fig. 3 (flujo, solo simulación); Fig. 6 es un video `Physical Model.mp4` | CC BY 4.0 | https://www.epj-conferences.org/articles/epjconf/pdf/2026/11/epjconf_staaar2026_01001.pdf |
| Mohammed et al. (2023), ETJ 41(6), 756-770 | Esquema geométrico y pasos HSV (números de figura sin verificar) | CC BY 4.0 | https://etj.uotechnology.edu.iq/article_176897_49464698aa46aa702ac4e4cd8207145d.pdf |
| Dang et al. (2026), FME Transactions 54(1), 93-106 | Fig. 1 (arquitectura), 10 (web MQTT), 16, 20 (montaje), 21 y 22 (YOLOv12), 23 (detección) | **«All rights reserved»: no copiar; redibujar** | https://scindeks-clanci.ceon.rs/data/pdf/1451-2092/2026/1451-20922601093T.pdf |
| Pybricks, *Robotic arm with vision* | Foto del brazo SPIKE con celular | Sin licencia clara; mejor solo cita con enlace | https://pybricks.com/project/robot-arm-camera-tracker/ ; imagen: https://pybricks.com/project/spike-prime/arm/camera-arm.jpg |
| LEGO Ideas, *VISION* | Brazo con PC y webcam que sigue una pelota roja en 3D | Sin licencia clara; solo cita con enlace. El sitio bloquea mi acceso (no se pudo abrir) | https://ideas.lego.com/challenges/339f0029-37b3-4dad-9dd2-6bcec3b93349/application/1099c817-11f6-4d42-8224-381674d1c749 (el usuario pasó la variante `/entries/…`) |
| Tzompantzi et al. (2019), IJSR 8(4) | Figs. 9 y 10 (RSSI frente a la distancia) | Sin verificar | https://www.ijsr.net/getabstract.php?paperid=ART20196990 (el PDF no se pudo abrir) |

**Figuras elegidas con el usuario:** Capaldi Fig. 1A recortada (en la imagen del usuario la configuración A del pie está en el panel rotulado «c»; se recorta solo ese panel, sin letra); Mada Sanjaya Fig. 3 en 4.1.5; Rangarajan Fig. 1 en 4.1.6 (la Fig. 3 de Rangarajan es opcional junto a ella); Shah Fig. 7 en 4.1.8 (alternativa: 4.2 junto a la captura propia); Dang solo como redibujo propio en 4.1.9; VISION solo con enlace. De Mada Sanjaya se vio también una segunda figura (rojo, verde, azul con coordenadas), posible apoyo de 4.1.6.

### 11.3 Hallazgos de la sesión que corrigen el informe (sin aplicar)

- **Tzompantzi (2019):** es *IJSR* 8(4), abril de 2019, pp. 775-780, DOI 10.21275/ART20196990. El informe y la ficha 14 dicen `8(8)`.
- **Capaldi (2024):** PeerJ Computer Science 10:e1826, DOI correcto, CC BY 4.0. La Tabla 2 completa: segmentos 2, 3 y 4 = 20,0, 2,01 y 1,56 ms; el resto cuadra con los 187 ms (n = 10, DE 57 ms; segmentos con n = 12; segmentos 1 y 11 calculados, 29,8 ms). El artículo no indica el tamaño del modelo YOLOv8 (116 imágenes, 50 épocas). Rango de inferencia en sus conclusiones: 10,8 a 64,4 ms. **Advertencia propia del artículo:** el Wi-Fi tiene demasiado retraso para control en tiempo real cuando la PC maneja el robot; la propuesta del informe usa Wi-Fi (HTTP) hasta el ESP32, así que conviene reconocerlo en 4.1.8 o en las limitaciones. Los valores de Kp, Ki y Kd de la ficha 7 no están en el texto: leerlos en la leyenda de la Fig. 14B.
- **Dang et al. (2026):** los nueve autores y su orden coinciden con la referencia; número 1 confirmado (VOL. 54, No 1). La portada trae «Dang Phuoc Thinh» primero, pero el encabezado del PDF dice «D.P. Thinh et al.» y el resumen en serbio usa «Тин»: **decidir si se cita «Dang» o «Thinh»**. La visión corre en un portátil con webcam integrada o cámara USB externa; la interfaz de escritorio va por USB y la web por MQTT (resumen y 3.3; la sección 2 dice Blynk). Dato nuevo: reconocimiento de gestos con latencia típica menor a 200 ms. El modelo de la cámara no se indica.
- **Shah y Arockia Doss (2026):** autores Ronit Shah y Arockia Selvakumar Arockia Doss, publicado el 3 de marzo de 2026, CC BY 4.0. Confirmados: punto de acceso «RobotArm», sliders, WebSockets, latencia menor a 150 ms sin método, parada de emergencia en el navegador y ROS/MoveIt solo en simulación. Dato nuevo para 4.1.7 o la Tabla 3: YOLOv8-OBB con 9086 imágenes anotadas, precisión 94,6 %, recall 92,1 % y mAP@0,5 de 95,3 %. Nota: los objetivos del artículo hablan de asistencia a pacientes y entornos hospitalarios aunque el título dice «domestic».
- **Rangarajan y Bianchini (2026):** *American Journal of Student Research* 4(6), 74-88. Es una revista de estudiantes (primer autor de un colegio secundario). YOLO11n-OBB con 540 imágenes: precisión 0,968, recall 0,985, mAP50 0,981; inferencia de 46,4 ms por cuadro en una CPU Xeon de 2 núcleos sin GPU; 176 de 196 pruebas (89,8 %). Los autores advierten que la división de datos fue por imagen y no por utensilio, así que no se mide cómo detecta utensilios nuevos.
- **Mohammed et al. (2023):** ETJ 41(6), 756-770, CC BY 4.0, 354 imágenes, 5 a 7000 lux, 93,83 %. La revista imprime el título corto *Smart Robot Vision for a Pick and Place Robotic System*; la referencia del informe agrega «under different illumination conditions»: revisar la primera página del PDF.
- **Pybricks, *Robotic arm with vision*:** autor Laurens Valk, publicado el 23 de marzo de 2026 (resuelve el `[verificar]` de la referencia).

### 11.4 Imágenes provisionales en `informe.md` (estado al revisar)

Embeds de Obsidian (`![[…]]`); no pude ver su contenido, se asumió que son las correspondientes.

| Sección | Imagen | Pie |
| ------- | ------ | --- |
| 1.1, tras «Plataformas LEGO con cámara» | `Pasted image 20261122233113.png` | No tiene |
| 1.1 | Línea suelta con la URL de `camera-arm.jpg` (no es una imagen embebida) | No aplica: borrarla o descargar la foto y embeberla |
| 1.1 | `informe-23-11-2026_00-10-13.png` | No tiene |
| 4.1.5 | `informe-23-11-2026_00-00-28.png` (Mada Sanjaya, Fig. 3) | Sí, sin número ni formato APA |
| 4.1.6 | `informe-23-11-2026_00-06-38.png` (Rangarajan, Fig. 1) | Sí, sin número ni formato APA |
| 4.1.6 | `informe-23-11-2026_00-07-42.png` (entre los dos párrafos) | No tiene |
| 4.1.8 | `informe-23-11-2026_00-03-52.png` (Shah, Fig. 7) | Sí, sin número ni formato APA |
| 4.1.9 | `informe-23-11-2026_00-12-18.png` e `informe-22-11-2026_23-53-06.png`, seguidas | No tienen |

**Problemas detectados:** cinco imágenes sin pie; los pies existentes son texto plano (el número debería ir en negrita y el título en cursiva, arriba de la figura, como las tablas) y dicen «Figura N»; ninguna figura nueva se cita en el texto (solo «Figura 1» en 4.2 y «Figura 2» en 4.3); la imagen sin pie de 4.1.6 debería ir después del segundo párrafo si es la tabla de calibración de Mada Sanjaya (o quedarse junto a la otra si es la Fig. 3 de Rangarajan); las dos de 4.1.9 conviene unirlas en una sola figura con paneles (a) y (b); la nota de Dang debe decir «redibujo propio». Las Figuras 1 y 2 de 4.2 y 4.3 siguen en ASCII. No aparecen aún las fichas 2, 3, 4, 16b, 18, 19 ni la 13 (Capaldi, Fig. 4 y Tabla 2).

**Numeración sugerida cuando estén todas (por orden de aparición):** 1.1 (1 y 2), 3.2 (3), 4.1.1 (4), 4.1.5 (5), 4.1.6 (6 y 7), 4.1.8 (8 y 9), 4.1.9 (10), 4.2 (11 y 12), 4.3 (13 y 14), 4.4 (15). Hay que cambiar las citas del texto «Figura 1» y «Figura 2» por sus números nuevos. Si el informe se exporta con otra herramienta, convertir los embeds a `![](ruta)`; en Obsidian se puede fijar el tamaño con `![[archivo.png|500]]`.

**Cierre de la sesión:** el usuario no hará ninguno de los cambios mencionados por ahora; todo quedó anotado en `bitacora_22.md`. Siguiente respaldo si se retoman las ediciones: `informe 10.md`.
