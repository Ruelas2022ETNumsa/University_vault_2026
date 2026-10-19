CONTEXTO — Exposición Cap. 7 (Input/Output) — ETN825

SESIÓN
- Worker: alx-rul · Skill usado: plan (lectura del vault, escritura solo con confirmación)
- Inicio de sesión: leer E:\University_vault_2026\_skills\_start.md y seguir su flujo
- Regla del skill plan: antes de sobrescribir un archivo avisar "cambios masivos, bk necesario" y esperar confirmación. Agregar contenido sin tocar lo existente (edit_file) no necesita bk.

OBJETIVO
Exponer en clases el Capítulo 7 "Input/Output" (Stallings COA). Las diapositivas son la BASE de lo que se expone y las otras fuentes completan lo necesario. También se compara el capítulo con el SIC del curso.
SIC = el computador de Hill & Peterson (Digital Systems 2ª ed.), NO el de Beck. Si algo del SIC no está en las fuentes, decir "No aparece en las fuentes del SIC". AHPL ya no es relevante.

FUENTE BASE
- CH07-COA10e.pdf — 52 láminas, Stallings COA 10ª ed. Citar con páginas reales del PDF.
- Puntos conocidos: el resumen (p.52) menciona "disk drive" y "characteristics of I/O channels" pero esas láminas no existen en el PDF. En el texto de la Fig. 7.19 los caracteres se ven corruptos en la imagen.

LIBROS DEL NOTEBOOK (nombres exactos)
Principales:
1. CH07-COA10e.pdf
2. Stallings - Computer Organization and Architecture - 11ed.pdf (libro del docente, complemento principal)
Apoyo:
3. Stallings - Organización y Arquitectura de Computadores - 7ed.pdf (español)
4. Stallings - Operating Systems - 8ed.pdf (solo rol del SO)
5. Mano - Computer System Architecture.pdf (consulta puntual)
6. Hamacher - Computer Organization and Embedded Systems - 6ed.pdf (interfaces y buses)
Para el SIC:
7. 825 Hill Peterson Digital Systems Hardware Organization Design 9-10-11-13.pdf
8. 825-Hill-Peterson-Resumen-Docente-ESP (sin paginación ni etiquetas de figura)
Opcionales: 825 Hill Peterson ... Design 7.pdf (SIC completo) y SIC-ModuloAHPL-47Pasos-Original-y-Explicado.
Descartado: Tanenbaum Distributed Systems (no trata hardware de E/S). Beck no hace falta.

PROMPT DE NOTEBOOKLM
- Archivo: E:\University_vault_2026\_app\notebooklm\prompts\ETN825\ETN825-expo-cap7.md (~7 000 bytes, límite 10 000 caracteres)
- Basado en ETN825-P1.md (estructura) y ETN1015-study.md (citado de figuras)
- Tres mensajes: "Subtítulo: X" · "Concepto: X" · "Subtítulo SIC: X" (o "Concepto SIC: X")
- Cada respuesta separa lo que dicen las diapositivas (con página) de lo que se completa con otra fuente (nombrada)
- Figuras: [[CH07-COA10e.pdf#page=N]] + etiqueta Fig. 7.x + bloque %%IMA-SRC | fuente | página | id | posición%% + justificación. Máximo 2 por respuesta; si no se confirma fuente + página + id, se omite.
- TikZJax y AHPL solo si se piden explícitamente
- Estado: prompt escrito y aún sin probar en NotebookLM. No sé si ya fue cargado en el notebook.

ARCHIVO DE TRABAJO
E:\University_vault_2026\Semesters\Sem_07\ETN825\expo825cap7.md
- Tabla de los 16 subtítulos con páginas y figuras
- Una sección por subtítulo con 3 snippets separados (Subtítulo · Concepto · Subtítulo + SIC) listos para copiar a NotebookLM

SUBTÍTULOS (página del PDF)
1 Dispositivos externos 4–6 · 2 Teclado/monitor e IRA 6 · 3 Módulo de E/S 3,7–8 · 4 E/S programada 9–12 · 5 Comandos e instrucciones de E/S 11,13 · 6 Mapeo de E/S 14–15 · 7 E/S por interrupciones 16–18 · 8 Diseño e identificación del dispositivo 19–20 · 9 Controladores 82C59A/8255A/82C55A 21–24 · 10 DMA 25–29 · 11 Controlador 8237A 30–31 · 12 Direct Cache Access y DDIO 32–38 · 13 Evolución de la E/S y canales 39–40 · 14 Interfaces y buses externos 41–48 · 15 Caso IBM zEC12 49–51 · 16 Resumen 52

PENDIENTE / SIGUIENTE PASO
- Probar en NotebookLM el subtítulo 1 con sus 3 mensajes y revisar: que no invente datos del SIC, que cite bien las páginas y que las figuras salgan con el formato correcto
- Ajustar el prompt si falla algo, luego seguir con los subtítulos 2, 3 y 4 y después el resto
- Dividir la exposición en clases
- Preferencias del usuario: respuestas ultra cortas, sin explicaciones largas