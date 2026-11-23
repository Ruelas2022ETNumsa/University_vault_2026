# Bitácora de pendientes: `informe.md` (22-nov-2026)

**Estado:** `informe.md` ya incluye los lotes 1 a 4 (lote 4 = Dang, Capaldi y Shah). Respaldo previo al lote 4: `informe 9.md`. Antes de otro cambio masivo: pedir `informe 10.md`.
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
- [~] A-11 **Dang et al. (2026):** autores, volumen, páginas y DOI confirmados. Falta el número, la forma APA de los apellidos y si la ruta de visión va por USB (inferencia de Gemini, `[verificar]` en el informe).
- [~] A-12 **Capaldi (2024):** resultados confirmados. Falta revista, volumen y DOI en el PDF, la tabla 2 completa (segmentos 2 a 4 del tiempo de ida y vuelta) y el tamaño del modelo YOLOv8.
- [~] A-13 **Shah y Arockia Doss (2026):** datos confirmados. Falta el orden y la forma APA de los autores, revista, DOI, y si el punto de acceso Wi-Fi y los sliders aparecen en el PDF.
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
- [ ] E-4 Figuras 1 y 2 como diagramas reales; formato APA 7 de tablas y figuras.
- [ ] E-5 Sumar Dang y Capaldi a la Tabla 5 si aportan limitaciones o trabajo futuro; revisar 3.3 (Tecnológico) con Capaldi.
- [ ] E-6 Compactar 1.1 (hoy repite la Tabla 1) y quitar la frase repetida de *smart sensors*.
- [ ] E-7 «Autor pendiente» de Tampere y JRC: título en la posición del autor cuando no haya autor.
- [ ] E-8 Acrónimos: revisar los que sobran (p. ej. ASEE, JRC, MQTT si ya no se citan).
- [ ] E-9 4.1.3: aclarar cómo aplica la fórmula de cinemática inversa (a₂, a₃) a un brazo sin hombro (base, codo, muñeca, garra).
- [ ] E-10 2.3: aclarar cuántos de los 31 trabajos son PDF revisados y cuántos son proyectos web frente a las referencias listadas.
- [ ] E-11 4.4: si se hace C-5 o C-6, añadir sus resultados; si no, renombrarlo «Estado del prototipo y plan de validación».
- [ ] E-12 Revisión final de coherencia (años, conteos, citas cruzadas entre tablas, texto y referencias).
- [ ] E-13 Actualizar `resumen_22.md` al cerrar cada lote.

## F. Hecho hasta ahora (referencia rápida)

- [x] Sesión 2: lotes 1 a 3 (respuestas S0 a S8, Perplexity A1, A2, A8, Gemini A3 a A7).
- [x] Lote 4: Dang, Capaldi y Shah integrados (1.1, brecha, Tablas 1, 3 y 4, 4.1.4, 4.1.7, 4.1.8, 4.1.9, 4.3, conclusiones 1, 3 y 5, recomendación 4, referencias, acrónimos, 2.3 y 2.5).
- [x] Opinión general del borrador y lista de pendientes (esta bitácora).
