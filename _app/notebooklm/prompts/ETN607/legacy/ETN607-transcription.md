TAREA:
Transcribir y complementar apuntes universitarios de Mecánica Aplicada (ETN607)
a formato Markdown.
_
FUENTES GUÍA (prioridad sobre conocimiento general):
- obsidian_notation.md  → sintaxis Obsidian, Cornell, callouts, wikilinks
- _library_ETN607.md    → criterio de selección de libros y capítulos por tema
- ETN607_latex.md       → notación LaTeX de la materia
- ETN607_TikzJax.md     → reglas y ejemplos TikZJax para ETN607
Si hay conflicto entre estas fuentes y conocimiento general → prevalece el documento.
_
FUENTES DE REFERENCIA: consultar _library_ETN607.md para
criterio de selección, capítulos y páginas exactas de cada libro por tema.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Tres mensajes posibles:

MENSAJE 1 — Transcripción + complemento:
"De apuntesTX, muéstrame subtítulo Y [HASTA subtítulo Z] con complemento nivel B/C"
→ transcribir TODO el contenido desde Y hasta detectar el título Z (no incluirlo)
→ si no se indica HASTA, detenerse al detectar cualquier nuevo subtítulo
→ NO adelantar el subtítulo siguiente

MENSAJE 2 — Ejercicios de libros (solo si el usuario lo pide):
  "De apuntesTX, subtítulo Y, muéstrame ejercicios resueltos"
  → ejercicios de los libros fuente según tema
  → si hay gráfica relevante: citá libro, capítulo y página (ej: "Fig. X, Wells Cap.3 p.47")
  → si NLM no puede localizar la figura con certeza: omitir — no inventar
  → NO repetir transcripción ni complemento ya entregado

MENSAJE 3 — Ejercicios del cuaderno (solo si el usuario lo pide):
  "De apuntesTX, muéstrame el ejercicio [enunciado/ec inicial] hasta [enunciado/ec final]"
  → buscar los ejercicios en el PDF por su enunciado o ecuación inicial (no por subtítulo)
  → transcribir resolución completa entre ambos puntos indicados
  → si hay gráfica en el apunte: citá figura equivalente del libro fuente
    (libro, capítulo, página) — si no existe con certeza, omitir
  → formato idéntico al Mensaje 2: ##### Ej., array LaTeX
  → complemento nivel B/C va después si el usuario lo pide
  → NO repetir transcripción ni complemento ya entregado
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

DETECCIÓN DE IMÁGENES (IMA):
Bloque delimitado por 2 líneas grises con texto "IMA · descripción" en gris.
→ NO transcribir el contenido visual
→ incluir: ![[pegar_imagen]]
            *IMA · [descripción del pie]*
→ respetar la posición donde estaba en el apunte

DETECCIÓN DE MARGINALIA:
Línea de resaltador que sobrepasa el borde hacia el margen externo.
Símbolo escrito en el margen. Traducir:
! %%> ! texto %% · ? %%> ?- texto %% · X %%> X- texto %% · V %%> V- texto %%
C %%> C- texto %% · F %%> F- texto %% · R %%> R- texto %% · T %%> T- texto %% · * %%> C- revisar %%
Usar callout solo si la posición es ambigua.
_
CONVENCIONES DEL APUNTE:
- valor[unidad] → preservar: 940[V], 470[Ω], 2[A]
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
[fórmula clave en inline $...$ — nunca display $$]
[ver también: X — errores comunes si aplica]

::note
[transcripción fiel: texto, fórmulas, convenciones, marginalia]
`````

>[!summary] [una línea — sin redundancia]

[ejemplos resueltos e IMA van aquí, fuera del Cornell]

REGLAS:
- BUG: identificador cornell en línea separada de los backticks — obligatorio
- Título ## NO va dentro del Cornell
- Marginalia en ::note: %%> %% inline junto al elemento
- Complemento y ejercicios SIEMPRE fuera del Cornell, después del [!summary]
_
COMPLEMENTO:
> [!note] Complemento (Nivel B/C)
>
>   contenido...

NIVEL B: definición formal del libro si la del apunte es informal.
NIVEL C: definición formal + propiedades omitidas + 1-2 ejercicios resueltos + gráfica si aplica.
SIN ejercicios (aplicar B): axiomas, listas de propiedades puras, notación formal.
NIVEL C cuando: procedimiento aplicable, coordenadas/restricciones con casos concretos,
  apunte ya tiene ejemplos → agregar uno de mayor dificultad.
→ extraer siempre de los libros fuente según _library_ETN607.md, no del conocimiento general.
Sin redundancia — cada subtítulo es independiente.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar posición exacta en el PDF. Esperar respuesta.
_
JERARQUÍA MARKDOWN:
# → Título principal (uno por archivo) · ## → Subtítulo numerado
### → Solo si hay sub-subtítulo con desarrollo propio evidente
_
FORMATO MATEMÁTICO:
Inline $...$ preferido. Display $$...$$ solo para multilínea:
$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \\
                & = & \text{expr}_3
\end{array}$$
Reglas: & separa cols · \\ termina fila (última sin \\) · \text{} para texto en math
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
EJEMPLOS RESUELTOS:
##### Ej. enunciado en la misma línea — fuera del Cornell.
Preservar numeración, valor[unidad] y ∴. No agregar pasos que no estén en el apunte.
> [!note] solo si hay observación relevante — no por defecto.

_
NOTACIÓN LATEX: consultar ETN607_latex.md como base.
_
FUENTES Y LIBROS POR TEMA:
apuntesTX · obsidian_notation.md · _library_ETN607.md
Taylor (dividido):
  caps.1-9   → John R. Taylor-Classical mechanics-eng-1to9.pdf
  caps.10-16 → John R. Taylor-Classical mechanics-eng-10to16.pdf
  (esp) caps.1-9   → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-1to9.pdf
  (esp) caps.10-16 → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-10to16.pdf
  soluciones → John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf
Goldstein (inglés): Goldstein & Poole & Safko-Classical Mechanics-3th ed-Pearson.pdf
Goldstein (esp):   H. Goldstein-Mecánica clásica-1994-ED REVERTE.pdf
Wells:   Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf
Nelson:  Nelson & Best & McLean-schaums Statics and dynamics.pdf
Lim:     LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf
Alonso:  Alonso & Finn-Mecánica_Vol 1-1970-.pdf

TEORÍA:
T1-T2  Taylor-1to9 Cap.1-2 · Alonso & Finn Vol.1
T3-T4  Taylor-1to9 Cap.7 · Goldstein Cap.1-2
T5     Taylor-1to9 Cap.7 y 4 · Goldstein Cap.1-2
T6     Taylor-1to9 Cap.7 · Goldstein Cap.1
T7     Wells Cap.7
T8     Goldstein Cap.4-5 · Taylor-10to16 Cap.10

EJERCICIOS:
T1-T2  Nelson Cap.11-13 · Wells Cap.1-2
T3-T4  Wells Cap.2-5 · Lim Mechanics of a Particle/System
T5     Wells Cap.5-6 · Lim Conservative Systems
T6     Wells Cap.6 · Lim Dissipative Systems
T7     Wells Cap.7
T8     Wells Cap.8-9 · Lim Rigid Bodies
_
SALTOS DE LÍNEA: texto compacto, sin líneas vacías innecesarias. El apunte siempre tiene prioridad.
