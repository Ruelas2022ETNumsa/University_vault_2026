# Resumen 22 de noviembre de 2026: revisión y refinamiento de `informe.md`

**Hora de inicio de sesión:** 18:39 (sesión 1) y 20:06 (sesión 2; los tokens se reestablecen a las 01:06)
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
- Respaldos del informe: `informe 1.md` a `informe 7.md` (el 5 y el 6 son el estado al inicio de la sesión 2; el 7 es posterior al lote 1). Antes de otro cambio masivo: `informe 8.md`.
- Las preguntas pendientes para NotebookLM (A1 a A18), Perplexity (B1 a B10) y las tareas propias (C1 a C6) están en el contexto de sesión; se irán trayendo de a poco según la prioridad.

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

## 8. Decisión: arquitectura de la propuesta = opción A (PC + ESP32)

**Arquitectura única para el informe:** cámara USB/webcam en la PC → módulo de visión/IA en la PC (Python + OpenCV, luego detector profundo) → Wi-Fi (HTTP, rutas `/s` y `/go`) → ESP32 → BLE broadcast Pybricks → hub 51515 → motores. Se descarta la cámara del celular conectada al hub (*smart sensors*, `ha7.py`) como parte de la propuesta; queda solo como antecedente del proyecto. El celular queda como interfaz manual (la página web).

**Resumen del prototipo `ha9.py` (palabras del usuario):** Pybricks + hub + ESP32 + celular. Desde la página web, con un slider, se manda al ESP32 cuándo y cuánto mover un motor; se mueve un motor a la vez; funciona bien; el ESP32 recuerda el ángulo anterior de cada motor al volver a una articulación (es el ángulo *ordenado*, no el alcanzado).

### Antecedentes encontrados para la opción A (web, 22-nov) `[verificar contra el PDF]`

1. **Dang, Van, Nguyen, Nguyen, Tran, Huynh, Phi, Vo y Vo (2026)** (orden de nombres vietnamitas por confirmar; autor de correspondencia Vo Duy Cong). *Development of an educational robotic platform with dual control interfaces and intelligent computer vision-based interaction*. FME Transactions, 54(1), 93-106. DOI en el PDF: 10.5937/fme2601093P. Brazo de 4 GDL con ESP32, YOLOv12 corriendo en una laptop (solo CPU), ángulos enviados al controlador. Interfaz web (el resumen dice MQTT; la sección 2 dice Blynk: contradicción interna del artículo). PDF: https://scindeks-clanci.ceon.rs/data/pdf/1451-2092/2026/1451-20922601093T.pdf
2. **Shah y Arockia Doss (2026).** *Development of service robot manipulator for pick and place applications in domestic environment*. EPJ Web of Conferences, 355, 01001. DOI: 10.1051/epjconf/202635501001. ESP32 como punto de acceso Wi-Fi con página de sliders (igual que el prototipo), latencia menor a 150 ms, parada de emergencia en el navegador, YOLOv8-OBB y ROS/MoveIt **en simulación**. Tiene un video del modelo físico (Fig. 6, archivo .mp4 dentro del artículo). PDF: https://www.epj-conferences.org/articles/epjconf/pdf/2026/11/epjconf_staaar2026_01001.pdf
3. **Capaldi (2024).** *A low-cost wireless extension for object detection and data logging for educational robotics using the ESP-NOW protocol*. PeerJ Computer Science, 10, e1826. DOI: 10.7717/peerj-cs.1826. Robótica educativa (VEX V5) + ESP32 + PC con visión (YOLOv8); mide distancia, tiempo de ida y vuelta y detección; incluye ajuste de PID. Análogo directo de hub cerrado + ESP32 + PC. https://peerj.com/articles/cs-1826
4. **Bera (2026, 1 de octubre).** *Computer-vision-based robotic arm*. Electronics For You (revista, no revisada por pares; parte del texto es de acceso con registro). Laptop, Raspberry Pi 5 o servidor GPU hacen la visión; el ESP32 hace el control en tiempo real; comunicación por Wi-Fi, Ethernet o serial (y ESP-NOW). **Video de la prueba de concepto:** https://www.youtube.com/watch?v=PHznMxfTjuo. Página: https://www.electronicsforu.com/electronics-projects/computer-vision-based-robotic-arm
5. Por revisar (no verificados): *Development and experimental validation of an educational robotic platform with machine vision and web-based monitoring for automation teaching*, Future Internet, 18(6), 325 (https://www.mdpi.com/1999-5903/18/6/325); TeleopLab (arXiv 2509.05547), interfaz de celular para laboratorios remotos (posible apoyo de la afirmación de "aforo reducido" de 3.2).

### Cambios previstos en `informe.md` (HECHOS en la sesión 2, salvo las filas de Dang, Shah y Capaldi: se omitieron porque el usuario no tiene esas fuentes por ahora)

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

**Pendientes.** (1) Perplexity: A3 (PID), A4 (definiciones de IA), A5 con *Benitez et al. (2020), HardwareX 8*, A6 (meta-análisis), metadatos B y opcionales; los prompts están en `contexto22.md`, sección A.6. (2) Usuario: C1 a C5, mirar el video o la página de Pybricks, verificar los README de los cuatro proyectos abiertos. (3) Prioridad 3 sin hacer: letras de Pybricks por título, material interno, figuras, formato de tablas, acrónimos y la frase repetida de *smart sensors* en 1.1. (4) Dang, Shah y Capaldi (N22 a N24) omitidos por falta de fuentes.
