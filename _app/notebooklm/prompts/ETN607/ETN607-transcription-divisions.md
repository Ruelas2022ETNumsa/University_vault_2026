TAREA:
Transcribir y complementar apuntes universitarios de Mecánica Aplicada (ETN607)
tomados en tablet (Samsung Notes, plantillas TABnote con divisiones) a formato
Markdown listo para Obsidian. El output es una nota supernova lista para integrarse al vault.
_
NOTACIÓN OBSIDIAN: consultar obsidian_notation.md (fuente del notebook) para
interpretar YAML, wikilinks, Cornell, callouts y bloques de visualización.
_
FUENTES DE REFERENCIA: consultar _library_ETN607.md (fuente del notebook) para
criterio de selección, capítulos y páginas exactas de cada libro por tema.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Dos mensajes por subtítulo:

MENSAJE 1 — Transcripción + complemento:
"De apuntesTX, muéstrame subtítulo Y [HASTA subtítulo Z] con complemento nivel B/C"
→ transcribir TODO el contenido desde Y hasta detectar el título Z (no incluirlo)
→ si no se indica HASTA, detenerse al detectar cualquier nuevo subtítulo
→ NO adelantar el subtítulo siguiente

MENSAJE 2 — Ejercicios (solo si el usuario lo pide):
  "De apuntesTX, subtítulo Y, muéstrame ejercicios resueltos"
  → ejercicios de los libros fuente según tema, con gráficas si aplica
  → NO repetir transcripción ni complemento ya entregado
_
DETECCIÓN DE PLANTILLA:
Antes de transcribir cualquier subtítulo, detectar qué plantilla está activa
inspeccionando la estructura visual de la página.

Las plantillas con divisiones tienen líneas separadoras notorias y gruesas
(cualquier color) que delimitan 4 zonas:

  ┌─────────────────────────────┐
  │         TÍTULO              │  ← zona título (franja superior)
  ├──────────────┬──────────────┤
  │              │              │  ← zona corta + zona desarrollo
  │              │              │
  ├──────────────┴──────────────┤
  │         RESUMEN             │  ← zona resumen (franja inferior)
  └─────────────────────────────┘

PLANTILLA CORNELL — zona corta a la IZQUIERDA:
  · Izquierda angosta: preguntas, dudas, palabras clave escritas por el alumno
  · Derecha amplia: desarrollo del subtítulo
  → ::cue ← zona izquierda | ::note ← zona derecha

PLANTILLA ÁUREA — zona corta a la DERECHA:
  · Izquierda amplia: desarrollo del subtítulo
  · Derecha angosta: imágenes, complementos visuales escritos por el alumno
  → ::note ← zona izquierda | ::cue ← zona derecha

Si NO se detectan líneas divisorias notorias → aplicar flujo de plantilla simple
(ver ETN607-transcription.md).

Si hay ambigüedad en la detección → indicar al usuario antes de continuar.
_
ORDEN DE LECTURA POR ZONA:
Independiente de la plantilla detectada, leer siempre en este orden:
1. Zona título (franja superior)
2. Zona desarrollo (::note) — de arriba hacia abajo
3. Zona corta (::cue) — de arriba hacia abajo
4. Zona resumen (franja inferior)

Excepción: si un desarrollo en ::note continúa visualmente hacia ::cue
de forma evidente (fórmula partida, tabla), leerlo como unidad continua.
_
DETECCIÓN DE TÍTULOS:
- Título principal: texto centrado, color #BB3E03, con resaltador lateral simétrico
  y línea delgada debajo → # en Markdown (uno por archivo)
- Subtítulo: texto con resaltador que llega hasta el borde derecho del área útil,
  color cálido variable, numerado (1., 2., 3...) → ## en Markdown
  (preservar el número — es ancla de orden)
- Nunca usar ### salvo sub-subtítulo con desarrollo propio evidente
_
DETECCIÓN DE CALLOUTS:
Caja de 4 lados con grosor notable, primera línea "> Título":
  · "> Ejercicio" → ##### Ej. [enunciado]
  · "> Tarea"     → > [!important] Tarea: [contenido]
  · Otros         → > [!note] [Título]: [contenido]
_
DETECCIÓN DE IMÁGENES (IMA):
Bloque delimitado por 2 líneas grises horizontales con texto "IMA · descripción" en gris.
NLM NO transcribe ni genera la imagen.
→ colocar exactamente en la posición donde estaba (::cue o ::note según zona):
   ![[pegar_imagen]]
   *IMA · [descripción del pie]*
_
DETECCIÓN DE MARGINALIA:
Línea de resaltador que sobrepasa el borde del área útil hacia el margen externo.
Símbolo escrito en el margen externo. Traducir según tabla:

| Símbolo | Tag marginalia    |
|---------|-------------------|
| !       | %%> ! texto %%    |
| ?       | %%> ?- texto %%   |
| X       | %%> X- texto %%   |
| V       | %%> V- texto %%   |
| C       | %%> C- texto %%   |
| F       | %%> F- texto %%   |
| R       | %%> R- texto %%   |
| T       | %%> T- texto %%   |
| *       | %%> C- revisar %% |

Colocar la marginalia inline junto al elemento que acompaña, respetando
en qué zona estaba (::cue o ::note).
T- es exclusivo de supernova — no heredar a notas derivadas.
_
CONVENCIONES DE ESCRITURA DEL APUNTE:
- valor[unidad] → preservar tal cual: 940[V], 470[Ω], 2[A]
- ∴ → preservar como símbolo de síntesis
- → ver Txx → preservar como referencia cruzada
- Flechas con texto anotado → incluir como nota al pie del elemento
- Flechas sin texto → ignorar
_
BLOQUES CORNELL — TRANSCRIPCIÓN LITERAL:
En estas plantillas el alumno ya escribió el contenido de ::cue y ::note
durante la clase. NLM transcribe ambas zonas textualmente — sin reformular,
sin agregar, sin omitir.

ESTRUCTURA DE OUTPUT:

## [N. Subtítulo]

`````
cornell
::cue
[transcripción textual de la zona corta del apunte]
[IMA en su posición → ![[pegar_imagen]] + pie]
[marginalia respetando posición]

::note
[transcripción textual de la zona de desarrollo]
[IMA en su posición → ![[pegar_imagen]] + pie]
[marginalia respetando posición]
`````

>[!summary] [transcripción textual de la zona resumen del apunte]

> [!note] Complemento NLM
>
> **Resumen desde fuentes:** [NLM genera síntesis del subtítulo desde libros fuente]
> **Palabras clave:** [NLM extrae términos clave del subtítulo]
> **Preguntas:** [NLM genera 2-4 preguntas de comprensión desde libros fuente]

> [!note] Complemento (Nivel B/C)
>
> [definición formal + ejercicios según nivel pedido — desde libros fuente]

REGLAS:
- BUG NotebookLM: el identificador cornell va en línea separada de los backticks
  (primero `````  salto de línea, luego cornell) — obligatorio
- El ## del subtítulo NO va dentro del bloque Cornell
- La transcripción en ::cue y ::note es LITERAL — no reformular
- Si la zona corta está vacía → ::cue vacío, NLM no inventa contenido
- Si la zona resumen está vacía → [!summary] vacío, NLM no inventa contenido
- El Complemento NLM y el Complemento B/C van SIEMPRE fuera del Cornell
- Ejemplos resueltos del apunte van fuera del Cornell, entre [!summary] y Complemento NLM
_
NIVELES DE COMPLEMENTO B/C:
NIVEL B — Solo definición reforzada:
- Definición formal del libro si la del apunte es informal o incompleta.

NIVEL C — Complemento completo:
- Definición formal + propiedades omitidas + 1-2 ejercicios resueltos
  de los libros fuente + gráfica TikZJax si aporta claridad.

SIN EJERCICIOS aunque se pida C (aplicar B):
- Definiciones y axiomas fundamentales sin procedimiento asociado.
- Listas de propiedades puras.

NIVEL C COMPLETO cuando:
- El subtítulo tiene procedimiento aplicable.
- El apunte ya tiene ejemplos → agregar uno de mayor dificultad.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar qué no se entiende y su posición exacta en el PDF
(ej: "página 2, zona desarrollo, tercer renglón"). Esperar respuesta.
_
JERARQUÍA MARKDOWN:
# → Título principal (uno por archivo)
## → Subtítulo numerado
### → Sub-subtítulo solo si tiene desarrollo propio evidente
_
FORMATO MATEMÁTICO:
Preferir inline $...$. Usar display $$...$$ solo para desarrollos multilínea.

$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \\
                & = & \text{expr}_3
\end{array}$$

REGLAS ARRAY:
- & separa columnas — N-1 & para N columnas
- \\ termina cada fila — última fila sin \\
- \text{...} para texto dentro de math
- Nunca convertir símbolos a texto si el apunte los presenta simbólicamente
_
GRÁFICOS:
Estrategia principal: IMA (placeholder manual).
TikZJax: solo para diagramas reproducibles con código corto y limpio.

IMA (principal): sistemas físicos, cuerpos rígidos, trayectorias, ángulos de Euler,
diagramas complejos → ![[pegar_imagen]] + pie descriptivo en su posición exacta.

TIKZJAX (selectivo): coordenadas cilíndricas/esféricas, cuerpo libre simple,
esquemas geométricos básicos, circuitos T7 con circuitikz.

REGLAS MÍNIMAS TIKZJAX:
· Identificador exacto: ```tikz
· \begin{document} y \end{document} siempre presentes
· \documentclass NUNCA se incluye
· Paquetes con \usepackage{} ANTES de \begin{document}
· Para circuitos (T7) → \usepackage{circuitikz}
· Color principal: teal / secundario: orange

Si hay duda entre IMA y TikZJax → usar IMA.
Nunca inventar gráficos. Nunca mezclar herramientas.
_
EJEMPLOS RESUELTOS:
Van fuera del Cornell, entre [!summary] y Complemento NLM.
##### Ej. enunciado en la misma línea.
- Transcripción literal del apunte — no agregar pasos.
- Preservar valor[unidad] y ∴ tal cual aparecen.
- > [!note] solo si hay observación relevante — no por defecto.
_
NOTACIÓN LATEX: consultar ETN607_latex.md (fuente del notebook) si existe,
o MAT101_latex.md como referencia base.
_
LIBROS PRIORITARIOS POR TEMA:
Consultar _library_ETN607.md (fuente del notebook) según el tema activo.

— TEORÍA (complemento NLM + B/C) —
T1–T2  Conceptos básicos:        Taylor Cap.1–2 · Alonso & Finn Vol.1
T3–T4  Lagrange partícula/sist.: Taylor Cap.7 · Goldstein Cap.1–2
T5     Sistemas conservativos:   Taylor Cap.7 · Goldstein Cap.1–2
T6     Sistemas disipativos:     Taylor Cap.7 · Goldstein Cap.1
T7     Circuitos eléctricos:     Wells Cap.7
T8     Cuerpos rígidos:          Goldstein Cap.4–5 · Taylor Cap.10

— EJERCICIOS (Mensaje 2) —
T1–T2  Nelson Schaum's Dynamics Cap.11–13 · Wells Cap.1–2
T3–T4  Wells Cap.2–5 · Lim — Mechanics of a Particle/System
T5     Wells Cap.5–6 · Lim — Conservative Systems
T6     Wells Cap.6  · Lim — Dissipative Systems
T7     Wells Cap.7
T8     Wells Cap.8–9 · Lim — Rigid Bodies
