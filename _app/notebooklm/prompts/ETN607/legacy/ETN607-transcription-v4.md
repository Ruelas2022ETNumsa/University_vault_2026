%%
status: pendiente-prueba
version: v4
date: 2026-08-17
nota: separado del v3 — solo transcripción, sin complemento. Prueba pendiente: detección de figuras del apunte y bloque IMA.
%%

TAREA:
Transcribir apuntes universitarios de Mecánica Aplicada (ETN607) a formato Markdown.

FUENTES GUÍA (prioridad sobre conocimiento general):
- obsidian_notation.md → sintaxis Obsidian, Cornell, callouts, wikilinks
- ETN607_latex.md → notación LaTeX de la materia
- ETN607_TikzJax.md → reglas y ejemplos TikZJax para ETN607
Si hay conflicto entre estas fuentes y conocimiento general → prevalece el documento.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Dos mensajes posibles:

MENSAJE 1 — Transcripción:
"De apuntesTX, muéstrame subtítulo Y [HASTA subtítulo Z]"
→ transcribir TODO el contenido desde Y hasta detectar el título Z (no incluirlo)
→ si no se indica HASTA, detenerse al detectar cualquier nuevo subtítulo
→ NO adelantar el subtítulo siguiente
→ NO agregar complemento ni referencias a libros fuente

MENSAJE 2 — Ejercicios del cuaderno (solo si el usuario lo pide):
"De apuntesTX, muéstrame el ejercicio [enunciado/ec inicial] hasta [enunciado/ec final]"
→ buscar los ejercicios en el PDF por su enunciado o ecuación inicial (no por subtítulo)
→ transcribir resolución completa entre ambos puntos indicados
→ formato: ##### Ej., array LaTeX
→ NO agregar complemento ni referencias a libros fuente
→ NO repetir transcripción ya entregada
_
ESTILO DE TRANSCRIPCIÓN:
- Corregir ortografía y errores evidentes de notación matemática.
- El apunte es el esqueleto — mantener fidelidad al orden y contenido original.
- Corrección importante → nota breve al final de esa sección.
_
ORDEN DE LECTURA:
Leer de arriba hacia abajo. Al terminar cada página, pasar a la siguiente.
Excepción 1 — división en columnas: si la página tiene una línea vertical que divide
la página en dos, con los símbolos > | < pegados a la línea (> del lado izquierdo,
< del lado derecho), leer primero la columna izquierda completa de arriba hacia abajo,
luego la columna derecha completa de arriba hacia abajo.
Excepción 2 — desarrollo continuo: si una fórmula o tabla continúa visualmente
en la misma página de forma evidente, leerla como unidad antes de seguir.

DETECCIÓN DE TÍTULOS:
- Título principal: texto centrado, color #BB3E03, con resaltador lateral simétrico
  y línea delgada debajo → # en Markdown (uno por archivo)
- Subtítulo: texto con resaltador que llega hasta el borde derecho del área útil,
  color cálido variable, numerado (1., 2., 3...) → ## en Markdown
  (el número ancla el orden — preservarlo)
- Nunca usar ### salvo que haya un sub-subtítulo con desarrollo propio evidente

DETECCIÓN DE CALLOUTS:
- Caja de 4 lados con grosor notable, primera línea "> Título"
  · "> Ejercicio" → ##### Ej. [enunciado]
  · "> Tarea"    → > [!important] Tarea: [contenido]
  · Otros títulos → > [!note] [Título]: [contenido]

DETECCIÓN DE FIGURAS EN APUNTE:
Caja cerrada de 4 lados. Primera línea dentro de la caja: `Figura T.N` (ej: Figura 1.3).
Espacio central: dibujo o esquema a mano. Última línea: descripción breve opcional.
Fuente del apunte: ETN607_T0X.pdf donde X es el número de tema.
→ NO transcribir el contenido visual
→ incluir siempre:
    ![[pegar_imagen]]
    *Figura T.N · [descripción si existe — omitir si no hay]*
→ agregar al pie el bloque de localización:
    IMA | fuente: ETN607_T0X.pdf | página: [número impreso] | id: Figura T.N | posición: [dónde está en la página]
→ respetar la posición donde estaba en el apunte
→ la etiqueta `Figura T.N` es la señal identificadora — equivale al `>` del callout

DETECCIÓN DE MARGINALIA:
Línea de resaltador que sobrepasa el borde hacia el margen externo.
Símbolo escrito en el margen. Traducir:
! %%> ! texto %% · ? %%> ?- texto %% · X %%> X- texto %%
F %%> F- texto %% · * %%> C- revisar %%
V · C · R · T → transcribir el símbolo tal cual en ::note.
Usar callout solo si la posición es ambigua.
_
CONVENCIONES DEL APUNTE:
- valor[unidad] → notación del apunte, no convertir: 940[V], 470[Ω]
- ∴ → preservar como símbolo de síntesis
- → ver Txx → preservar como referencia cruzada
- Flechas con texto → nota al pie del elemento · Flechas sin texto → ignorar
_
BLOQUES CORNELL:
Aplicar a subtítulos de teoría: definiciones, propiedades, procedimientos.
NO aplicar a ejemplos resueltos ni bloques IMA.
El ::note contiene la transcripción. El ::cue y [!summary] los completa NLM.

ESTRUCTURA:

## [N. Subtítulo]

`````
cornell
::cue
[palabras clave · ]
[2-4 preguntas centrales]
[fórmula clave en inline LaTeX]
[ver también: X — errores comunes si aplica]

::note
[transcripción fiel: texto, fórmulas, convenciones, marginalia]
`````

>[!summary] [una línea — sin redundancia]

[ejemplos resueltos e IMA van aquí, fuera del Cornell]

REGLAS:
- identificador cornell en línea separada de los backticks — obligatorio
- Título ## NO va dentro del Cornell
- Marginalia en ::note: %%> %% inline junto al elemento
_
EJEMPLOS RESUELTOS:
##### Ej. enunciado en la misma línea — fuera del Cornell.
Preservar numeración, valor[unidad] y ∴. No agregar pasos que no estén en el apunte.
> [!note] solo si hay observación relevante — no por defecto.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar número de página. Esperar respuesta.
_
JERARQUÍA MARKDOWN:
# → Título principal (uno por archivo) · ## → Subtítulo numerado
### → Solo si hay sub-subtítulo con desarrollo propio evidente
_
FORMATO MATEMÁTICO:
Ecuaciones centrales: salto de línea antes y después.
Notación específica → ETN607_latex.md.
_
GRÁFICOS:
IMA es la estrategia principal — sistemas físicos, cuerpos rígidos, trayectorias,
péndulos, restricciones, Euler, diagramas complejos → ![[pegar_imagen]] + pie.
TikZJax solo para: coordenadas cilíndricas/esféricas, cuerpo libre simple,
esquemas geométricos básicos, circuitos T7 con circuitikz.
Si se usa TikZJax → consultar ETN607_TikzJax.md (fuente del notebook) para reglas y ejemplos.
REGLAS TIKZJAX: ```tikz exacto · \begin{document} y \end{document} siempre ·
\documentclass NUNCA · paquetes antes de \begin{document} ·
circuitikz para T7 · color principal teal / secundario orange.
Si hay duda → IMA. Nunca inventar. Nunca mezclar.
_
SALTOS DE LÍNEA: texto compacto, sin líneas vacías innecesarias. El apunte siempre tiene prioridad.
