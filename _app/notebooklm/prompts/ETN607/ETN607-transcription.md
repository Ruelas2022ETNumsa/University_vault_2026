TAREA:
Transcribir y complementar apuntes universitarios de Mecánica Aplicada (ETN607)
tomados en tablet (Samsung Notes, plantilla TABnote simple) a formato Markdown
listo para Obsidian. El output es una nota supernova lista para integrarse al vault.
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
PLANTILLA DE APUNTE — TABnote simple:
Los apuntes están tomados en Samsung Notes con plantilla TABnote en formato simple:
página A4 sin divisiones internas, flujo vertical de arriba hacia abajo.

ORDEN DE LECTURA:
Leer siempre de arriba hacia abajo, página completa, sin saltos laterales.
Pasar a la siguiente página al terminar.
Excepción: si un desarrollo, tabla o fórmula continúa visualmente en la misma
página de forma evidente, leerlo como unidad continua antes de seguir.

DETECCIÓN DE TÍTULOS:
- Título principal: texto centrado, color #BB3E03, con resaltador lateral simétrico
  y línea delgada debajo → ## en Markdown
- Subtítulo: texto con resaltador que llega hasta el borde derecho del área útil,
  color cálido variable, numerado (1., 2., 3...) → ## en Markdown
  (el número ancla el orden — preservarlo)
- Nunca usar ### salvo que haya un sub-subtítulo con desarrollo propio evidente

DETECCIÓN DE CALLOUTS:
- Caja de 4 lados con grosor notable, primera línea "> Título"
  → transcribir como callout Obsidian según catálogo:
  · "> Ejercicio" → ##### Ej. [enunciado] (formato de ejemplo resuelto)
  · "> Tarea"    → > [!important] Tarea: [contenido]
  · Otros títulos → > [!note] [Título]: [contenido]

DETECCIÓN DE IMÁGENES (IMA):
- Bloque delimitado por 2 líneas grises horizontales con texto "IMA · descripción"
  en gris → NO transcribir el contenido visual
  → incluir: > [!note] IMA · [descripción del pie] — pegar screenshot manualmente
  → si NLM puede inferir una descripción breve del diagrama, agregarla como pie

DETECCIÓN DE MARGINALIA:
Línea de resaltador que sobrepasa el borde del área útil hacia el margen externo.
El símbolo está escrito en el margen. Traducir según esta tabla:

| Símbolo | Tag marginalia         | Callout equivalente si no aplica margen |
|---------|------------------------|-----------------------------------------|
| !       | %%> ! texto %%         | > [!important] texto                    |
| ?       | %%> ?- texto %%        | > [!question] texto                     |
| X       | %%> X- texto %%        | > [!warning] Corrección: texto          |
| V       | %%> V- texto %%        | > [!check] texto                        |
| C       | %%> C- texto %%        | > [!note] texto                         |
| F       | %%> F- texto %%        | > [!note] Fórmula clave: texto          |
| R       | %%> R- texto %%        | > [!note] Relación: texto               |
| T       | %%> T- texto %%        | > [!important] Tarea: texto             |
| *       | %%> C- revisar %%      | > [!warning] Revisar                    |

REGLA: usar sintaxis %%> %% (marginalia inline) siempre que el símbolo esté
claramente al margen. Usar callout solo si la posición es ambigua.
T- es exclusivo de supernova — no heredar a notas derivadas.
_
CONVENCIONES DE ESCRITURA DEL APUNTE:
- valor[unidad] → preservar tal cual: 940[V], 470[Ω], 2[A]
- ∴ → preservar como símbolo de síntesis al cerrar desarrollos
- → ver Txx → preservar como referencia cruzada: → ver T03
- Flechas con texto anotado → incluir como nota al pie del elemento
- Flechas sin texto → ignorar
_
BLOQUES CORNELL:
Aplicar a subtítulos de teoría: definiciones, propiedades, procedimientos paso a paso.
NO aplicar a ejemplos resueltos ni a bloques IMA.

El ::note contiene la transcripción fiel del apunte.
El ::cue y el [!summary] los completa NLM usando los libros fuente.

ESTRUCTURA:

## [N. Subtítulo]

`````
cornell
::cue
[palabras clave separadas por · ]
[2-4 preguntas centrales que el subtítulo responde]
[fórmula o definición clave en inline $...$ — nunca display $$]
[conexiones: ver también: X — sin corchetes]
[errores comunes: no confundir X con Y — solo si aplica]

::note
[transcripción fiel del subtítulo: texto, fórmulas, convenciones y marginalia]
`````

>[!summary] [una línea del subtítulo — sin redundancia con otros subtítulos]

[ejemplos resueltos y bloques IMA van aquí, fuera del Cornell]

REGLAS:
- BUG NotebookLM: el identificador cornell va en línea separada de los backticks
  (primero `````  salto de línea, luego cornell) — obligatorio
- El título ## del subtítulo NO va dentro del bloque Cornell
- Marginalia dentro de ::note: usar %%> %% inline junto al elemento que acompaña
- Complemento y ejercicios de libros van SIEMPRE fuera del Cornell, después del [!summary]
- Gráficas TikZJax dentro de ::note: tamaño normal
_
NIVELES DE COMPLEMENTO:
Va DESPUÉS del Cornell (fuera del bloque), con este formato exacto:
> [!note] Complemento (Nivel B/C)
>
>   contenido...

NIVEL B — Solo definición reforzada:
- Agregar definición formal del libro si la del apunte es informal o incompleta.

NIVEL C — Complemento completo:
- Definición formal + propiedades omitidas + 1-2 ejercicios resueltos
  extraídos de los libros fuente + gráfica TikZJax si aporta claridad.

SIN EJERCICIOS aunque se pida C (aplicar B):
- Definiciones y axiomas fundamentales sin procedimiento asociado.
- Listas de propiedades puras.
- Notación y convenciones formales.

NIVEL C COMPLETO cuando:
- El subtítulo tiene procedimiento aplicable: deducción de ecuaciones, despeje de variables.
- El apunte ya tiene ejemplos → agregar uno de mayor dificultad de los libros.
- Coordenadas, restricciones, grados de libertad con casos concretos.

SIN REDUNDANCIA:
- Cada subtítulo es independiente. No adelantar el siguiente.
- No repetir definiciones previas — solo referenciarlas brevemente.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar qué no se entiende y su posición exacta en el PDF
(ej: "página 2, tercer renglón"). Esperar respuesta antes de continuar.
_
JERARQUÍA MARKDOWN:
# → Título principal del capítulo (uno por archivo).
## → Subtítulo numerado (detección por resaltador + número).
### → Sub-subtítulo solo si tiene desarrollo propio evidente.
Nunca ### para ítems de listas.
_
FORMATO MATEMÁTICO:
Preferir inline $...$. Usar display $$...$$ solo para:
- Desarrollo multilínea, sistemas, resultado principal de un procedimiento.

ESTRUCTURA ARRAY:
$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \\
                & = & \text{expr}_3
\end{array}$$

REGLAS:
- & separa columnas — siempre N-1 & para N columnas
- \\ termina cada fila — la última fila no lleva \\
- Texto dentro de math → \text{...}
- Nunca convertir símbolos a texto si el apunte los presenta simbólicamente
_
GRÁFICOS:
La estrategia principal para esta materia es IMA (recorte manual de screenshot).
TikZJax se usa solo cuando el diagrama es reproducible con código corto y limpio.

1. IMA (estrategia principal):
   Diagramas de sistemas físicos, cuerpos rígidos, trayectorias, péndulos,
   restricciones, ángulos de Euler, diagramas complejos en general.
   → > [!note] IMA · [descripción] — pegar screenshot manualmente

2. TIKZJAX (uso selectivo):
   Solo para: sistemas de coordenadas (cilíndricas, esféricas), diagramas de
   cuerpo libre simples, esquemas geométricos básicos, circuitos eléctricos
   simples (T7) con paquete circuitikz.

   REGLAS MÍNIMAS:
   · Identificador exacto: ```tikz — nunca latex, nunca tikzjax
   · \begin{document} y \end{document} siempre presentes
   · \documentclass NUNCA se incluye
   · Paquetes con \usepackage{} ANTES de \begin{document}
   · Si se usa \dfrac en nodos → cargar \usepackage{amsmath}
   · Para circuitos (T7) → \usepackage{circuitikz}
   · Color principal: teal / secundario: orange

3. NUNCA inventar gráficos. NUNCA mezclar herramientas.
   Si hay duda entre IMA y TikZJax → usar IMA.
_
EJEMPLOS RESUELTOS:
Van fuera del bloque Cornell, después del [!summary].
##### Ej. enunciado en la misma línea.
- Conservar numeración de partes del apunte.
- No agregar pasos que no estén en el apunte.
- Preservar valor[unidad] y ∴ tal cual aparecen.
- Al final: > [!note] solo si hay observación relevante — no por defecto.
_
NOTACIÓN LATEX: consultar ETN607_latex.md (fuente del notebook) si existe,
o MAT101_latex.md como referencia base, para cancelaciones, cajas de resultado
y desarrollos multilínea.
_
LIBROS PRIORITARIOS POR TEMA:
Consultar siempre _library_ETN607.md (fuente del notebook) según el tema activo.

— TEORÍA (transcripción + complemento) —
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
