# Bitácora de pendientes: `informe.md` (22-nov-2026)

**Estado:** `informe.md` ya incluye los lotes 1 a 4 (lote 4 = Dang, Capaldi y Shah). Respaldo previo al lote 4: `informe 9.md`. Antes de otro cambio masivo: pedir `informe 10.md`. **Sesión 4 (23-nov, worker `alx_hot`):** el usuario insertó imágenes provisionales en `informe.md` (varias sin pie ni número) y decidió no aplicar por ahora los cambios hallados; todo lo pendiente de esa sesión está en la sección G y en las líneas marcadas «S4» de A y E. Detalle en `resumen_22.md`, sección 11.
**Reglas:** no inventar datos; lo no verificado queda `[verificar]`, `[pendiente]` o "s. f."; avisar "cambios masivos, bk necesario" antes de editar.
**Cierre común para consultas a NotebookLM, Gemini o Perplexity:** *Responde solo con lo que está en las fuentes. Indica archivo PDF exacto (no «Fuente N»), autor, año y página o sección. Si no está, escribe 'no está en las fuentes'. No inventes.* Para Perplexity: *Para cada fuente dame autor(es), año, título, revista o editorial, DOI o URL, y página o sección. No inventes; si no puedes confirmar un dato, escribe no confirmado.*

Leyenda: `[ ]` pendiente, `[x]` hecho, `[~]` en curso o parcial.

---

## A. Verificación contra los PDF (NotebookLM o Gemini con el cuaderno `iaarm`)

- [ ] A-1 **Suhaeb y Risal (2024):** ¿85 a 92 ms o 85 a 110 ms con hasta 10 usuarios? Revista, volumen, número y páginas.
- [ ] A-2 **Monroy Moya et al.:** año real (2024, 2025 o 2026), revista, volumen, número, DOI. Unificar el año en todo el informe (hoy 1.1 dice 2026, el resto 2024).
- [ ] A-3 **`T-ESPEL-MEC-0165.pdf` (Aucapiña e Iza):** confirmar que es la tesis ESPE con el uArm. Página del «número limitado de módulos», 97,28 %, 84,28 %, 2075 USD, año.
- [ ] A-4 **Tesis UPS (Llerena y Salazar):** confirmar xArm 1S, aforo por pandemia con KUKA y la página (p. 4 está por inferencia).
- [ ] A-5 **Intisar et al. (2021):** pasaje de «sigue la rutina aunque el objeto se caiga»; costo de unos 80 USD; que no mencione fuerza de agarre.
- [ ] A-6 **Markvicka et al. (2023):** 36 estudiantes, sin diferencia significativa, encuesta (n = 35, 78 %), 30 000 USD de un brazo industrial, 1000 USD de los kits.
- [ ] A-7 **Archivos sin metadatos:** `2010S03C01.pdf`, `2402.17243v1.pdf`, `30-100-1-SP.pdf`, `978-3-642-32527-4_17.pdf`, `P-00W-KW7.pdf` (autores, año, título, revista o editorial, DOI).
- [ ] A-8 **`s44430-026-00032-6.pdf` (Ntambara):** revista, volumen, artículo, DOI, iniciales de los cuatro autores.
- [ ] A-9 **Zuiev, Kumar, Wu (Penn State Erie), Medel, Gunardi, Fernández Panadero:** revista o editorial, páginas, año, autores faltantes.
- [ ] A-10 **Narmadha et al. (2022):** páginas exactas del cap. 15 y DOI.
- [~] A-11 **Dang et al. (2026):** autores (orden), volumen, número (1), páginas y DOI confirmados (S4). La ruta de visión quedó respaldada: portátil con webcam integrada o cámara USB externa, interfaz local por USB y web por MQTT; el modelo de cámara no se indica. Falta decidir la forma APA del primer autor: la portada dice «Dang Phuoc Thinh» pero el encabezado del PDF dice «D.P. Thinh et al.» (S4).
- [x] A-12 **Capaldi (2024):** confirmado en la página de PeerJ (S4): *PeerJ Computer Science* 10:e1826, DOI 10.7717/peerj-cs.1826, CC BY 4.0. Tabla 2 completa (segmentos 2, 3 y 4 = 20,0, 2,01 y 1,56 ms). El artículo no indica el tamaño del modelo YOLOv8 (116 imágenes, 50 épocas): dejarlo como «no indicado». Quitar los `[verificar]` de la referencia y de 4.1.7.
- [x] A-13 **Shah y Arockia Doss (2026):** confirmado (S4): Ronit Shah y Arockia Selvakumar Arockia Doss, *EPJ Web of Conferences* 355, 01001, 3-mar-2026, DOI 10.1051/epjconf/202635501001, CC BY 4.0; el punto de acceso Wi-Fi, los sliders, los WebSockets, la latencia menor a 150 ms y la parada de emergencia aparecen en el PDF. Quitar el `[verificar]` de la referencia.
- [ ] A-15 **(S4) Tzompantzi et al. (2019):** abrir el PDF en IJSR (https://www.ijsr.net/getabstract.php?paperid=ART20196990) y confirmar las Figs. 9 y 10 (RSSI) y el número de repeticiones del Wireshark. Datos de la referencia ya confirmados: *IJSR* 8(4), abril de 2019, pp. 775-780, DOI 10.21275/ART20196990.
- [ ] A-16 **(S4) Mohammed et al. (2023):** confirmar en la primera página el título exacto (la revista imprime *Smart Robot Vision for a Pick and Place Robotic System*; el informe agrega «under different illumination conditions») y ubicar el número de las figuras del esquema geométrico y de los pasos HSV.
- [ ] A-17 **(S4) Mada Sanjaya et al. (2018):** ubicar el número de las figuras de la tabla de calibración y de la red neuronal (20 neuronas) y de la figura con las coordenadas por color; la Fig. 3 (pasos de detección) ya está usada en 4.1.5.
- [ ] A-18 **(S4) Rangarajan y Bianchini (2026):** completar la referencia con volumen, número y páginas (4(6), 74-88). Tomar la cita de la versión publicada, no la de arXiv.
- [ ] A-14 Tabla 5 (limitaciones): revisar si Dang y Capaldi agregan filas (ver E-5).

## B. Perplexity (fuentes externas y metadatos)

- [ ] B-1 **A3 (PID):** libros, apuntes o revisiones que definan PID y el término integral (efecto sobre el error en estado estacionario), de preferencia con servomotores o brazos educativos y acceso abierto. Cierra el `[cita pendiente]` de 4.1.4.
- [ ] B-2 **A4 (definiciones):** libro, survey u organismo reconocido que defina inteligencia artificial, aprendizaje automático, red neuronal artificial y detección de objetos. Cierra el `[cita pendiente]` de 4.1.7.
- [ ] B-3 **A5 (aforo y práctica remota):** laboratorios remotos con brazos o robots educativos que mencionen aforo o equipos limitados; buscar *Benitez et al. (2020), Design of an affordable IoT open-source robot arm for online teaching of robotics courses during the pandemic contingency, HardwareX 8*.
- [ ] B-4 **A6 (aprendizaje activo):** meta-análisis o estudios con cifras de aprendizaje activo frente a pasivo en ingeniería, y estudios de que los modelos físicos enseñan fricción u holgura.
- [ ] B-5 **Metadatos:** autores del JRC 2026 y del proyecto de Tampere; revista de Fernández Panadero 2010, Gunardi y Jumadri 2020 y Medel; autores de Wu et al. 2014 y de Oliveira et al. 2021; revista, volumen y DOI de Capaldi y de Shah; títulos de Cho et al. (2014) y de Vieira y Rizzetti (2025).
- [ ] B-6 **Opcionales:** detectores livianos (YOLO nano, MobileNet), rojo contra café en HSV, comunicación de un solo sentido.
- [ ] B-7 **Por revisar:** Future Internet 18(6), 325 (https://www.mdpi.com/1999-5903/18/6/325) y TeleopLab (arXiv 2509.05547). Bera (2026, Electronics For You) no se cita; decidir si se incluye como referencia de implementación.

## C. Tareas del usuario

- [ ] C-1 Abrir los PDF y confirmar autores, año, revista y páginas (cierra la mayoría de los `[verificar]`; empezar por A-1 a A-6).
- [ ] C-2 Institución, carrera, asignatura, docente y fecha (cabecera, 3.1 y 3.2).
- [ ] C-3 Costo real del montaje (3.3, fila Económico).
- [ ] C-4 Confirmar con el docente el formato de la guía APA y si APA 7 es definitivo.
- [ ] C-5 Medir el retraso orden-movimiento del prototipo (opcional, recomendado para el 4.4).
- [ ] C-6 Prueba mínima de HSV de la pelota roja sobre la base café desde foto o video, con ángulos predichos por la tabla de calibración (opcional, recomendado: 4.4 hoy no tiene cifras propias).
- [ ] C-7 Ver el video o la página del proyecto de Pybricks (*Robotic arm with vision*) y anotar si los motores se mueven a la vez y con qué alimentación (cierra el `[pendiente]` de 4.3).
- [ ] C-8 Verificar los README de los cuatro proyectos abiertos: Johnson (GATT o difusión), osullivp (placa y firmware), GC-TO (función del ESP32), Anton's Mindstorms (título y autor).
- [ ] C-9 Confirmar con el docente cómo entender «sustentar la implementación de IA» (teórico-documental o con prueba de concepto) y si hace falta adjuntar enlaces de video.

## D. Discrepancias abiertas (resolver con los PDF, C-1)

- [ ] Suhaeb: 85 a 92 ms (informe) frente a 85 a 110 ms (S4).
- [ ] Monroy Moya: 2024 (referencia y 4.x), 2025 (S4 y S5), 2026 (S0 y 1.1).
- [ ] Las dos tesis (ESPE con uArm; UPS con xArm 1S) se mezclaron en NotebookLM y Gemini; se usó la atribución del informe.
- [ ] Dang: MQTT en el Abstract y en 3.3, Blynk en la sección 2.
- [ ] Atribuciones por inferencia de Gemini: aforo de la UPS (Llerena y Salazar) y 36 participantes (Markvicka).

## E. Edición de `informe.md` (míos, con `edit_file`, previo bk `informe 10.md`)

- [ ] E-1 Aplicar los resultados de A-1 a A-13 y B-1 a B-5 (quitar `[verificar]` y `[cita pendiente]` según corresponda).
- [ ] E-2 **Prioridad 3, referencias:** reordenar las letras de Pybricks por título (a = BLE broadcast, b = Mediciones, c = Motor, d = Robotic arm, e = Use your phone; hoy *Robotic arm* es s. f.-a) y actualizar todas las citas del texto.
- [ ] E-3 Quitar material interno: bloque «Estado del borrador», notas «Verificar contra los trabajos completos», línea meta de 3.3 y fila «Ambiental».
- [ ] E-4 Figuras 1 y 2 como diagramas reales; formato APA 7 de tablas y figuras (ver sección G para el detalle de las imágenes).
- [ ] E-5 Sumar Dang y Capaldi a la Tabla 5 si aportan limitaciones o trabajo futuro; revisar 3.3 (Tecnológico) con Capaldi.
- [ ] E-6 Compactar 1.1 (hoy repite la Tabla 1) y quitar la frase repetida de *smart sensors*.
- [ ] E-7 «Autor pendiente» de Tampere y JRC: título en la posición del autor cuando no haya autor.
- [ ] E-8 Acrónimos: revisar los que sobran (p. ej. ASEE, JRC, MQTT si ya no se citan).
- [ ] E-9 4.1.3: aclarar cómo aplica la fórmula de cinemática inversa (a₂, a₃) a un brazo sin hombro (base, codo, muñeca, garra).
- [ ] E-10 2.3: aclarar cuántos de los 31 trabajos son PDF revisados y cuántos son proyectos web frente a las referencias listadas.
- [ ] E-11 4.4: si se hace C-5 o C-6, añadir sus resultados; si no, renombrarlo «Estado del prototipo y plan de validación».
- [ ] E-12 Revisión final de coherencia (años, conteos, citas cruzadas entre tablas, texto y referencias).
- [ ] E-13 Actualizar `resumen_22.md` al cerrar cada lote.
- [ ] E-14 **(S4) Referencias que corregir con lo ya verificado:** Tzompantzi 8(8) → 8(4), pp. 775-780, DOI 10.21275/ART20196990; Rangarajan y Bianchini → agregar 4(6), 74-88; Pybricks (s. f.-a) → quitar el `[verificar]` (autor Laurens Valk, 23-mar-2026); Capaldi y Shah → quitar los `[verificar]` (A-12 y A-13); Dang → decidir «Dang» o «Thinh» y quitar el `[verificar]` del número; Mohammed → ver A-16.
- [ ] E-15 **(S4) Capaldi y el Wi-Fi:** el artículo dice que el Wi-Fi tiene demasiado retraso para control en tiempo real cuando la PC maneja el robot, y la propuesta del informe usa Wi-Fi (HTTP) hasta el ESP32. Reconocerlo en 4.1.8 o en las limitaciones de 4.3.
- [ ] E-16 **(S4) Datos nuevos para el texto:** Rangarajan y Bianchini (YOLO11n-OBB con 540 imágenes, precisión 0,968, recall 0,985, mAP50 0,981, 46,4 ms por cuadro en CPU de 2 núcleos sin GPU, división por imagen y no por utensilio) y Shah y Arockia Doss (YOLOv8-OBB con 9086 imágenes, precisión 94,6 %, recall 92,1 %, mAP@0,5 de 95,3 %) para 4.1.7 y la Tabla 3; Dang (gestos con latencia típica menor a 200 ms) para 4.1.8. Decidir si se agregan. Rangarajan es de una revista de estudiantes: mencionarlo en 2.5 o en las limitaciones.
- [ ] E-17 **(S4) Nota de Shah:** sus objetivos hablan de asistencia a pacientes y hospitales aunque el título dice «domestic»; revisar que 1.1 no describa el trabajo con más alcance del que tiene.

## F. Hecho hasta ahora (referencia rápida)

- [x] Sesión 2: lotes 1 a 3 (respuestas S0 a S8, Perplexity A1, A2, A8, Gemini A3 a A7).
- [x] Lote 4: Dang, Capaldi y Shah integrados (1.1, brecha, Tablas 1, 3 y 4, 4.1.4, 4.1.7, 4.1.8, 4.1.9, 4.3, conclusiones 1, 3 y 5, recomendación 4, referencias, acrónimos, 2.3 y 2.5).
- [x] Opinión general del borrador y lista de pendientes (esta bitácora).

---

## G. Imágenes del informe (sesión 4, 23-nov; el usuario no aplicó cambios, queda todo pendiente)

Refs: `informe_img.md` (19 fichas; todas las anclas coinciden con el texto vigente) y `resumen_22.md` sección 11 (fuentes, licencias y estado). Las imágenes provisionales ya están en `informe.md` como embeds de Obsidian; no se vio su contenido.

**G-1. Pies y formato (imágenes ya insertadas)**
- [ ] G-1.1 Poner pie a las cinco imágenes que no lo tienen: dos en 1.1 (`Pasted image 20261122233113.png`, `informe-23-11-2026_00-10-13.png`), una en 4.1.6 (`…_00-07-42.png`) y dos en 4.1.9 (`…_00-12-18.png`, `informe-22-11-2026_23-53-06.png`).
- [ ] G-1.2 Dar formato APA 7 a todos los pies (como las tablas): arriba, `**Figura N**` en negrita y `*Título*` en cursiva; abajo, `*Nota.*`. Hoy los cuatro pies existentes son texto plano y dicen «Figura N».
- [ ] G-1.3 Borrar la línea suelta con la URL de `camera-arm.jpg` en 1.1 (no es una imagen), o descargar la foto y embeberla; la licencia de Pybricks no es clara, así que mejor solo la cita con enlace.
- [ ] G-1.4 Citar cada figura en el texto («Figura 5», etc.) en el párrafo anterior; hoy solo se citan «Figura 1» (4.2) y «Figura 2» (4.3).
- [ ] G-1.5 Revisar la imagen sin pie de 4.1.6: si es la tabla de calibración de Mada Sanjaya, moverla después del segundo párrafo (el de la calibración ojo-mano y la tabla); si es la Fig. 3 de Rangarajan, dejarla junto a la Fig. 1.
- [ ] G-1.6 Unir las dos imágenes de 4.1.9 en una figura con paneles (a) y (b) y pie único: (a) Capaldi, Fig. 1, configuración A (recorte del panel rotulado «c» de la imagen, sin letra); (b) Dang, redibujo propio (derechos reservados). Nota del pie: «Redibujo propio a partir de Dang et al., 2026, Fig. 1».
- [ ] G-1.7 Pies sugeridos ya redactados (ver `resumen_22.md` 11.2 y la conversación): Mada Sanjaya (Fig. 3, CC BY 3.0), Rangarajan (Fig. 1, CC BY 4.0), Shah (Fig. 7, CC BY 4.0), Capaldi (Fig. 1 configuración A, CC BY 4.0).
- [ ] G-1.8 Si el informe se exporta con otra herramienta, convertir `![[archivo.png]]` en `![](ruta)`; en Obsidian se puede fijar el ancho con `![[archivo.png|500]]`.

**G-2. Figuras que faltan (de `informe_img.md`)**
- [ ] G-2.1 **Propias de prioridad alta:** ficha 3 (foto de la escena: pelota roja, base café y cubo), ficha 4 (brazo real con F base, D codo, A muñeca, B garra rotulados), ficha 16 (diagrama del prototipo en lugar de la Figura 1 en ASCII, más captura de la página y foto del montaje), ficha 17 (diagrama de la arquitectura propuesta en lugar de la Figura 2 en ASCII) y ficha 19 (captura de la prueba preliminar de detección).
- [ ] G-2.2 **Propias de apoyo:** ficha 2 (cadena visión → ESP32 → hub y qué cubre cada antecedente), ficha 9 (secuencia HSV propia; depende de C-6) y ficha 18 (secuencia de los nueve pasos).
- [ ] G-2.3 **De fuente:** ficha 13 (Capaldi, Fig. 4 y Tabla 2 o 3; CC BY 4.0). Opcionales: fichas 6, 7, 14, 10, 12 y 5. Ficha 14 (Tzompantzi): primero abrir el PDF (A-15).
- [ ] G-2.4 **Idea nueva:** ficha 20, diagrama de flujo del método de la revisión para 2.5 (Perplexity → NotebookLM y Gemini → 31 trabajos en 32 archivos).
- [ ] G-2.5 Corregir `informe_img.md`: pie de la ficha 14 (IJSR 8(4), pp. 775-780, no 8(8)); cambiar el título de Mohammed según A-16; marcar como confirmados Capaldi (Figs. 1A, 4, 7B, 14B y Tablas 2 y 3, CC BY 4.0) y Dang (Figs. 1, 10, 20, 21, 22 y 23; derechos reservados, solo redibujo); quitar el `[verificar]` de la ficha 13 sobre los segmentos 2 a 4; leer en la Fig. 14B los valores de Kp, Ki y Kd de la ficha 7.
- [ ] G-2.6 Para la ficha 1(b), LEGO Ideas: la URL que pasó el usuario es `/entries/…` y la referencia usa `/application/…`; decidir cuál abre bien y dejar una sola. El sitio bloquea mi acceso. Sin licencia clara: solo cita con enlace.

**G-3. Numeración final (cuando estén todas)**
- [ ] G-3.1 Renumerar por orden de aparición: 1.1 (1 y 2), 3.2 (3), 4.1.1 (4), 4.1.5 (5), 4.1.6 (6 y 7), 4.1.8 (8 y 9), 4.1.9 (10), 4.2 (11 y 12), 4.3 (13 y 14), 4.4 (15), y cambiar las citas de texto «Figura 1» y «Figura 2» por los números nuevos.
- [ ] G-3.2 Agregar una lista de figuras si el docente la pide (ver E-4) y revisar el anexo de acrónimos por si aparecen siglas nuevas en los rótulos.
- [ ] G-3.3 Antes de insertar cualquier figura de fuente: abrir el PDF, confirmar número y página, revisar la licencia y decidir si se reproduce o se redibuja.
