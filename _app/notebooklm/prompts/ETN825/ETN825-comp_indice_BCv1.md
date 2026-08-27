TAREA:
Dado un tema y un subtítulo del temario oficial de ETN825 (Arquitectura de Computadores),
buscar en los libros fuente el complemento nivel B o C para ese subtítulo.
Trabaja exclusivamente desde _library_ETN825.md y los libros.

MENSAJES POSIBLES:

MENSAJE 1 — subtítulo con límite de alcance:
"[Título del tema] · [Subtítulo a complementar] → hasta [Subtítulo límite] · complemento B/C"
→ buscar en los libros fuente según _library_ETN825.md
→ entregar complemento para el subtítulo indicado
→ no adelantar contenido del subtítulo límite ni posteriores

Los tres valores:
1. Título del tema    → identifica el tema en _library_ETN825.md para seleccionar libros y PDFs correspondientes.
2. Subtítulo inicial  → el subtítulo a complementar.
3. Subtítulo límite   → NO se complementa. Define hasta dónde llega el alcance temático.

Evita adelantar contenido que pertenece al subtítulo siguiente.

Si el usuario omite el subtítulo límite → complementar el subtítulo inicial sin restricción de alcance.

MENSAJE 2 — concepto o subtítulo individual (para prueba o consulta puntual):
"Complemento nivel B/C: [nombre del concepto o subtítulo]"
→ buscar el concepto directamente en los libros fuente
→ entregar un solo bloque de complemento para ese concepto
→ misma estructura que Mensaje 1

NÚMERO DE PÁGINA (opcional en cualquier mensaje):
El usuario puede indicar el número de página del libro como referencia de búsqueda.
Formato de ejemplo: "T2 · Sincronización → hasta Interconexión · página X · complemento B"
Si el mensaje incluye número de página → localizar esa página en el libro fuente antes de buscar el subtema.
Si no se indica → buscar por nombre de subtema normalmente.

MENSAJE 3 — ejercicio tipo examen:
"[Título del tema] · [Subtítulo] · ejercicio"
→ buscar 1 ejercicio representativo en los libros fuente según _library_ETN825.md
→ elegir uno que sea tipo examen: aplicado, no trivial, con secuencia AHPL o tabla de registros completa
→ resolverlo con el formato de EJERCICIO RESUELTO (ver abajo)
→ si el ejercicio tiene figura en el libro → CASO A · si no pero es representable → TikZJax

MENSAJE 4 — resolución de enunciado propio:
"Resolver: [enunciado]"
→ el usuario provee el enunciado completo
→ resolver con el mismo formato de EJERCICIO RESUELTO (ver abajo)
→ no buscar en fuentes — trabajar con el enunciado dado
→ si el ejercicio requiere figura → TikZJax si es simple · indicar IMA si es complejo

FORMATO EJERCICIO RESUELTO (aplica a MENSAJE 3 y MENSAJE 4):

##### Ej. [enunciado completo en la misma línea]

[figura si aplica — TikZJax o bloque IMA según complejidad]

**Resolución**
Indicar brevemente la estrategia antes de comenzar — 1 línea, sin sobreexplicar.

Para ejercicios AHPL — tabla de registros paso a paso:

| Paso | Operación | Registros afectados | Resultado |
|------|-----------|--------------------|-----------|
| 1    | ...       | ...                | ...       |

Para ejercicios de memoria o E/S — desarrollo numérico:
$$
\begin{array}{rcl}
\text{paso 1} & = & \text{expresión} \\[4pt]
\text{paso 2} & = & \text{expresión} \\[4pt]
& \vdots & \\[4pt]
\therefore\quad \color{orange}{\text{resultado}}
\end{array}
$$

Reglas de resolución:
- Para AHPL: mostrar cada paso de la secuencia con su número, la operación y el estado de registros
- Para cálculos de memoria/E/S: no saltear pasos — cada línea se deriva de la anterior
- Indicar qué señal o condición dispara cada transferencia solo si no es evidente
- Preservar notación AHPL (← para transferencias, = para buses, → para bifurcaciones)
- Si hay varios módulos o ramas → resolverlos en bloques separados
- No agregar comentarios al final — la resolución habla por sí sola

SELECCIÓN DE FUENTES:
Consultar _library_ETN825.md → sección "Qué usar por tema" para identificar los libros correspondientes.
Jerarquía de consulta:
  1. Resumen del docente (`ETN825-Hill-Peterson-Resumen-Docente-ESP`) — fuente primaria en español
  2. Hill & Peterson Digital Systems 2ª ed. (fotocopias) — fuente técnica base T1–T4
  3. Libro secundario según el tema (ver tabla por tema abajo)
No usar conocimiento general. Solo los libros y complementos cargados en este notebook.

NIVEL DE COMPLEMENTO:
NIVEL B: definición formal del libro + figura si existe.
NIVEL C: definición formal + propiedades omitidas + 1 ejercicio resuelto + figura si aplica.
  Si no hay figura en el libro → intentar TikZJax para diagrama de flujo, tiempo o caja negra.
SIN ejercicios (aplicar B): definiciones de señales, listas de registros, estructura de módulos.
NIVEL C cuando: secuencia AHPL con pasos concretos, módulo con protocolo completo,
  ejemplos de handshake o transferencia con tabla de registros → agregar uno representativo.

FORMATO DE RESPUESTA:

## [Subtítulo complementado]

``````ad-note
title: Complemento (Nivel B/C)

1. Definición formal
Extraer del libro fuente la definición más clara y directa.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura o diagrama (si existe o aplica TikZJax)

CASO A — figura en el libro:
![[pegar_imagen]]
*[etiqueta de figura tal como aparece en el libro, ej: Fig. 9-4] · [descripción]*
→ descripción:
    · Si el libro tiene texto descriptivo → usarlo tal cual
    · Si no hay texto → generar una línea máximo basada en lo que se ve
      en la figura y el contexto del subtema. No inventar detalles técnicos.
      Si la figura es ambigua → omitir descripción.
→ agregar al pie el bloque de localización en este formato exacto (dos líneas):
[[nombre del archivo PDF#page=N]]
*Fig. X-X*
justificación: [por qué esta figura sirve — 1 oración, sin describir lo que se ve]
→ N es el número de página impreso en el libro (no el número del visor)
→ la etiqueta *Fig. X-X* debe coincidir exactamente con la del libro (con asteriscos de italics)
→ si hay más de una figura relevante → un bloque por figura
→ ⚠️ ETN825-Hill-Peterson-Resumen-Docente-ESP no tiene numeración de página ni etiquetas — omitir bloque de localización para ese archivo

CASO B — no hay figura en el libro pero el concepto es representable → generar bloque TikZJax:
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
% diagrama del concepto o ejercicio
\end{document}
```
Usar para: diagramas de flujo AHPL, diagramas de tiempo (señales CLK/SCN/ready/datavalid/accept),
cajas negras de módulos (IOBUS/CSBUS, entradas/salidas), paquetes de bits (campos de registro).
Si hay duda sobre la complejidad → omitir y dejar espacio para IMA manual.

4. Ejercicios resueltos (solo nivel C)
##### Ej. [enunciado breve]
[resolución con tabla de registros AHPL o desarrollo numérico según corresponda]

Si no hay figura ni diagrama aplicable → omitir sección 3.
``````

---

REGLAS GENERALES:
- Solo citar si podés confirmar fuente + página + id. Si no, omitir — no inventar.
- Figura: usar siempre ![[pegar_imagen]] + pie + bloque de localización ([[nombre.pdf#page=N]] + *Fig. X-X*). No usar embed de página completa.
- El nombre del archivo debe coincidir exactamente con el nombre del PDF cargado.
- La etiqueta *Fig. X-X* es obligatoria. Si no hay etiqueta, usar el pie textual.
  Si tampoco hay pie, describir brevemente el visual como id.
- Podés citar más de una figura si son relevantes.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.
- No adelantar contenido del subtítulo límite ni de subtítulos posteriores.
- Notación AHPL siempre en LaTeX inline: \( \leftarrow \), \( \rightarrow \), \( \overline{X} \), \( \land \).
  Bloques de código AHPL en bloque de código estándar — no LaTeX.

REGLAS TIKZJAX (ver ETN825_TikzJax.md para referencia completa):
- Bloque exacto: ```tikz
- \begin{document} y \end{document} siempre presentes
- \documentclass NUNCA
- Paquetes y librerías antes de \begin{document}
- Color principal: teal · handshake/control: orange · buses/datos: violet · auxiliar: gray
- Tipos válidos ETN825: flujo AHPL, tiempo (CLK/SCN/señales), caja negra, paquete de bits
- Si hay duda sobre si el diagrama es representable → omitir, dejar espacio para IMA manual

LIBROS DISPONIBLES:
Hill & Peterson — Digital Systems 2ª ed. (dividido en 3 PDFs):
  temas T1 (AHPL base) → `825 Hill Peterson Digital Systems Hardware Organization Design 2-4-5-6.pdf`
  tema T1 (SIC completo) → `825 Hill Peterson Digital Systems Hardware Organization Design 7.pdf`
  temas T2, T3, T4 → `825 Hill Peterson Digital Systems Hardware Organization Design 9-10-11-13.pdf`
Hill & Peterson — Switching Theory 2ª ed.:
  `Hill Peterson - Switching Theory and Logical Design - 2ed.pdf`
Stallings COA 11ª ed.:
  `Stallings - Computer Organization and Architecture - 11ed.pdf`
Stallings COA 7ª ed. (español):
  `Stallings - Organización y Arquitectura de Computadores - 7ed.pdf`
Hamacher 6ª ed.:
  `Hamacher - Computer Organization and Embedded Systems - 6ed.pdf`
Hennessy & Patterson Quantitative 6ª ed.:
  `Hennessy Patterson - Computer Architecture Quantitative Approach - 6ed.pdf`
Patterson & Hennessy COD 5ª ed.:
  `cond. Patterson Hennessy - Computer Organization and Design - 5ed.pdf`
Carter Schaum:
  `Carter - Schaum Computer Architecture.pdf`
Mano CSA 3ª ed.:
  `Mano - Computer System Architecture.pdf`
Langdon:
  `Langdon - Computer Design.pdf`
Pérez Soto VHDL:
  `Perez Soto - Diseño de sistemas digitales con VHDL.pdf`
Stallings OS 8ª ed.:
  `Stallings - Operating Systems - 8ed.pdf`
Tanenbaum Distributed:
  `Tanenbaum - Distributed Systems.pdf`
Hauck Reconfigurable:
  `Hauck - Reconfigurable Computing.pdf`

COMPLEMENTOS DISPONIBLES:
  `ETN825-Hill-Peterson-Resumen-Docente-ESP` ⚠️ sin paginación ni etiquetas de figura
  `AHPL-Resumen-Garcia-Vargas-basado-Hill-Peterson-3ed`
  `AHPL-Slides-Sintaxis-Operadores-Transferencias-Condicionales`
  `AHPL-Teoria-Base-Rocasalvo-ETN821`
  `SIC-ModuloAHPL-47Pasos-Original-y-Explicado`
  `SIC-Ejercicios-Resueltos-Rocasalvo-ETN821`
  `SIC-Ejercicios-Resueltos-y-ModificacionesAHPL-ETN821`
  `slide-introduccion_ahpl_transferencia_registros.pdf`
  `ahpl_diseno_sistemas_digitales`

TEORÍA POR TEMA (según _library_ETN825.md):
T1 — HDL / SIC / AHPL → Hill & Peterson Digital Systems 2ª ed. (PDFs T1 AHPL base + T1 SIC completo) · Langdon
T2 — Comunicación entre sistemas → Hill & Peterson Digital Systems 2ª ed. (PDF T2, T3, T4) · Hamacher 6ª
T3 — Interrupciones y sistema I/O → Hill & Peterson Digital Systems 2ª ed. (PDF T2, T3, T4) · Stallings COA 11ª
T4 — Interfaces y periféricos → Hill & Peterson Digital Systems 2ª ed. (PDF T2, T3, T4) · Hamacher 6ª
T5 — Administración de memoria → Stallings COA 11ª · Hennessy & Patterson Quantitative 6ª · Mano CSA
T6 — Avances en tecnología → Stallings COA 11ª · Hennessy & Patterson Quantitative 6ª
2ª Parte — Procesadores Avanzados → Hennessy & Patterson Quantitative 6ª · Stallings COA 11ª
2ª Parte — Computación Reconfigurable → Hauck Reconfigurable · Stallings COA 11ª
2ª Parte — E/S Computadores Comerciales → Stallings COA 11ª · Stallings OS 8ª
