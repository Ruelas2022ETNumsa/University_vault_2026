%%
# tpl_prompt_transcription
Prototipo de prompt de transcripción TABnote para cualquier materia.
Derivado de ETN607-transcription.md y ETN607-transcription-divisions.md.

Al crear el prompt de una materia nueva:
1. Copiar el bloque de la variante correspondiente (A o B)
2. Reemplazar todos los campos [MATERIA] y [NOMBRE_MATERIA] con los datos reales
3. Completar la sección FUENTES Y LIBROS POR TEMA con el stack de _library_MATERIA.md
4. Guardar en _app/notebooklm/prompts/[MATERIA]/[MATERIA]-transcription.md
   y/o [MATERIA]-transcription-divisions.md según las plantillas TABnote que use la materia

Referencia visual del sistema TABnote: _TABnote-ref.md (este carrier)
Referencia de libros y stack: _library-system.md
Instancia completa de referencia: ETN607-transcription.md y ETN607-transcription-divisions.md
%%

---
---

# VARIANTE A — TABnote simple
%%
Usar cuando los apuntes están en plantilla TABnote sin divisiones (flujo vertical puro).
Equivalente a ETN607-transcription.md.
%%

TAREA:
Transcribir y complementar apuntes universitarios de [NOMBRE_MATERIA] ([MATERIA])
tomados en tablet (Samsung Notes, plantilla TABnote simple) a formato Markdown
listo para Obsidian. El output es una nota supernova lista para integrarse al vault.
_
NOTACION OBSIDIAN: consultar obsidian_notation.md (fuente del notebook) para
interpretar YAML, wikilinks, Cornell, callouts y bloques de visualizacion.
_
FUENTES DE REFERENCIA: consultar _library_[MATERIA].md (fuente del notebook) para
criterio de seleccion, capitulos y paginas exactas de cada libro por tema.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Tres mensajes posibles:

MENSAJE 1 — Transcripcion + complemento:
"De apuntesTX, muestrame subtitulo Y [HASTA subtitulo Z] con complemento nivel B/C"
-> transcribir TODO el contenido desde Y hasta detectar el titulo Z (no incluirlo)
-> si no se indica HASTA, detenerse al detectar cualquier nuevo subtitulo
-> NO adelantar el subtitulo siguiente

MENSAJE 2 — Ejercicios de libros (solo si el usuario lo pide):
  "De apuntesTX, subtitulo Y, muestrame ejercicios resueltos"
  -> ejercicios de los libros fuente segun tema
  -> si hay grafica relevante: cita libro, capitulo y pagina (ej: "Fig. X, Autor Cap.3 p.47")
  -> si NLM no puede localizar la figura con certeza: omitir — no inventar
  -> NO repetir transcripcion ni complemento ya entregado

MENSAJE 3 — Ejercicios del cuaderno (solo si el usuario lo pide):
  "De apuntesTX, muestrame el ejercicio [enunciado/ec inicial] hasta [enunciado/ec final]"
  -> buscar los ejercicios en el PDF por su enunciado o ecuacion inicial (no por subtitulo)
  -> transcribir resolucion completa entre ambos puntos indicados
  -> si hay grafica en el apunte: cita figura equivalente del libro fuente
    (libro, capitulo, pagina) — si no existe con certeza, omitir
  -> formato identico al Mensaje 2: ##### Ej., array LaTeX
  -> complemento nivel B/C va despues si el usuario lo pide
  -> NO repetir transcripcion ni complemento ya entregado
_
ESTILO DE TRANSCRIPCION:
- Corregir ortografia y errores evidentes de notacion matematica.
- El apunte es el esqueleto — mantener fidelidad al orden y contenido original.
- Correccion importante -> nota breve al final de esa seccion.
_
PLANTILLA DE APUNTE — TABnote simple:
Los apuntes estan tomados en Samsung Notes con plantilla TABnote en formato simple:
pagina A4 sin divisiones internas, flujo vertical de arriba hacia abajo.

ORDEN DE LECTURA:
Leer siempre de arriba hacia abajo, pagina completa, sin saltos laterales.
Pasar a la siguiente pagina al terminar.
Excepcion: si un desarrollo, tabla o formula continua visualmente en la misma
pagina de forma evidente, leerlo como unidad continua antes de seguir.

DETECCION DE TITULOS:
- Titulo principal: texto centrado, color #BB3E03, con resaltador lateral simetrico
  y linea delgada debajo -> # en Markdown (uno por archivo)
- Subtitulo: texto con resaltador que llega hasta el borde derecho del area util,
  color calido variable, numerado (1., 2., 3...) -> ## en Markdown
  (el numero ancla el orden — preservarlo)
- Nunca usar ### salvo que haya un sub-subtitulo con desarrollo propio evidente

DETECCION DE CALLOUTS:
- Caja de 4 lados con grosor notable, primera linea "> Titulo"
  . "> Ejercicio" -> ##### Ej. [enunciado]
  . "> Tarea"    -> > [!important] Tarea: [contenido]
  . Otros titulos -> > [!note] [Titulo]: [contenido]

DETECCION DE IMAGENES (IMA):
Bloque delimitado por 2 lineas grises con texto "IMA . descripcion" en gris.
-> NO transcribir el contenido visual
-> incluir: ![[pegar_imagen]]
            *IMA . [descripcion del pie]*
-> respetar la posicion donde estaba en el apunte

DETECCION DE MARGINALIA:
Linea de resaltador que sobrepasa el borde hacia el margen externo.
Simbolo escrito en el margen. Traducir:
! %%> ! texto %% . ? %%> ?- texto %% . X %%> X- texto %% . V %%> V- texto %%
C %%> C- texto %% . F %%> F- texto %% . R %%> R- texto %% . T %%> T- texto %% . * %%> C- revisar %%
Usar callout solo si la posicion es ambigua.
_
CONVENCIONES DEL APUNTE:
- valor[unidad] -> preservar: 940[V], 470[ohm], 2[A]
- por tanto -> preservar como simbolo de sintesis
- -> ver Txx -> preservar como referencia cruzada
- Flechas con texto -> nota al pie del elemento . Flechas sin texto -> ignorar
_
BLOQUES CORNELL:
Aplicar a subtitulos de teoria: definiciones, propiedades, procedimientos.
NO aplicar a ejemplos resueltos ni bloques IMA.
El ::note contiene la transcripcion. El ::cue y [!summary] los completa NLM.

ESTRUCTURA:

## [N. Subtitulo]

`````
cornell
::cue
[palabras clave . ]
[2-4 preguntas centrales]
[formula clave en inline $...$ — nunca display $$]
[ver tambien: X — errores comunes si aplica]

::note
[transcripcion fiel: texto, formulas, convenciones, marginalia]
`````

>[!summary] [una linea — sin redundancia]

[ejemplos resueltos e IMA van aqui, fuera del Cornell]

REGLAS:
- BUG: identificador cornell en linea separada de los backticks — obligatorio
- Titulo ## NO va dentro del Cornell
- Marginalia en ::note: %%> %% inline junto al elemento
- Complemento y ejercicios SIEMPRE fuera del Cornell, despues del [!summary]
_
COMPLEMENTO:
> [!note] Complemento (Nivel B/C)
>
>   contenido...

NIVEL B: definicion formal del libro si la del apunte es informal.
NIVEL C: definicion formal + propiedades omitidas + 1-2 ejercicios resueltos + grafica si aplica.
SIN ejercicios (aplicar B): axiomas, listas de propiedades puras, notacion formal.
NIVEL C cuando: procedimiento aplicable, coordenadas/restricciones con casos concretos,
  apunte ya tiene ejemplos -> agregar uno de mayor dificultad.
Sin redundancia — cada subtitulo es independiente.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar posicion exacta en el PDF. Esperar respuesta.
_
JERARQUIA MARKDOWN:
# -> Titulo principal (uno por archivo) . ## -> Subtitulo numerado
### -> Solo si hay sub-subtitulo con desarrollo propio evidente
_
FORMATO MATEMATICO:
Inline $...$ preferido. Display $$...$$ solo para multilinea:
$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \\
                & = & \text{expr}_3
\end{array}$$
Reglas: & separa cols . \\ termina fila (ultima sin \\) . \text{} para texto en math
_
GRAFICOS:
IMA es la estrategia principal -> ![[pegar_imagen]] + pie.
TikZJax solo para: coordenadas, cuerpo libre simple, esquemas geometricos basicos.
REGLAS TIKZJAX: ```tikz exacto . \begin{document} y \end{document} siempre .
\documentclass NUNCA . paquetes antes de \begin{document} .
color principal teal / secundario orange.
Si hay duda -> IMA. Nunca inventar. Nunca mezclar.
_
EJEMPLOS RESUELTOS:
##### Ej. enunciado en la misma linea — fuera del Cornell.
Preservar numeracion, valor[unidad]. No agregar pasos que no esten en el apunte.
> [!note] solo si hay observacion relevante — no por defecto.
_
NOTACION LATEX: consultar [MATERIA]_latex.md o MAT101_latex.md como base.
_
FUENTES Y LIBROS POR TEMA:
%%
Completar con el stack de _library_[MATERIA].md al crear el prompt de la materia.
Modelo: ver ETN607-transcription.md seccion FUENTES Y LIBROS POR TEMA.

apuntesTX . obsidian_notation.md . _library_[MATERIA].md
[Libro principal (eng)]: nombre-exacto-archivo.pdf
[Libro puente esp]:      nombre-exacto-archivo-esp.pdf
[Libro ejercicios]:      nombre-exacto-archivo.pdf

TEORIA:
T1  [libro] Cap.X
...

EJERCICIOS:
T1  [libro] Cap.X
...
%%
_
SALTOS DE LINEA: texto compacto, sin lineas vacias innecesarias. El apunte siempre tiene prioridad.

---
---

# VARIANTE B — TABnote con divisiones
%%
Usar cuando los apuntes estan en plantilla TABnote Cornell o Aurea (con lineas divisorias).
Equivalente a ETN607-transcription-divisions.md.
%%

TAREA:
Transcribir y complementar apuntes universitarios de [NOMBRE_MATERIA] ([MATERIA])
tomados en tablet (Samsung Notes, plantillas TABnote con divisiones) a formato
Markdown listo para Obsidian. El output es una nota supernova lista para integrarse al vault.
_
NOTACION OBSIDIAN: consultar obsidian_notation.md (fuente del notebook) para
interpretar YAML, wikilinks, Cornell, callouts y bloques de visualizacion.
_
FUENTES DE REFERENCIA: consultar _library_[MATERIA].md (fuente del notebook) para
criterio de seleccion, capitulos y paginas exactas de cada libro por tema.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Tres mensajes posibles:

MENSAJE 1 — Transcripcion + complemento:
"De apuntesTX, muestrame subtitulo Y [HASTA subtitulo Z] con complemento nivel B/C"
-> transcribir TODO el contenido desde Y hasta detectar el titulo Z (no incluirlo)
-> si no se indica HASTA, detenerse al detectar cualquier nuevo subtitulo
-> NO adelantar el subtitulo siguiente

MENSAJE 2 — Ejercicios de libros (solo si el usuario lo pide):
  "De apuntesTX, subtitulo Y, muestrame ejercicios resueltos"
  -> ejercicios de los libros fuente segun tema
  -> si hay grafica relevante: cita libro, capitulo y pagina
  -> si NLM no puede localizar la figura con certeza: omitir — no inventar
  -> NO repetir transcripcion ni complemento ya entregado

MENSAJE 3 — Ejercicios del cuaderno (solo si el usuario lo pide):
  "De apuntesTX, muestrame el ejercicio [enunciado/ec inicial] hasta [enunciado/ec final]"
  -> buscar los ejercicios en el PDF por su enunciado o ecuacion inicial (no por subtitulo)
  -> transcribir resolucion completa entre ambos puntos indicados
  -> si hay grafica en el apunte: cita figura equivalente del libro fuente — si no existe, omitir
  -> formato identico al Mensaje 2: ##### Ej., array LaTeX
  -> complemento nivel B/C va despues si el usuario lo pide
  -> NO repetir transcripcion ni complemento ya entregado
_
ESTILO DE TRANSCRIPCION:
- Corregir ortografia y errores evidentes de notacion matematica.
- El apunte es el esqueleto — mantener fidelidad al orden y contenido original.
- Correccion importante -> nota breve al final de esa seccion.
_
DETECCION DE PLANTILLA:
Antes de transcribir cualquier subtitulo, detectar que plantilla esta activa
inspeccionando la estructura visual de la pagina.

Las plantillas con divisiones tienen lineas separadoras notorias y gruesas
(cualquier color) que delimitan 4 zonas:

  +-----------------------------+
  |         TITULO              |  <- zona titulo (franja superior)
  +--------------+--------------+
  |              |              |  <- zona corta + zona desarrollo
  |              |              |
  +--------------+--------------+
  |         RESUMEN             |  <- zona resumen (franja inferior)
  +-----------------------------+

PLANTILLA CORNELL — zona corta a la IZQUIERDA:
  . Izquierda angosta: preguntas, dudas, palabras clave escritas por el alumno
  . Derecha amplia: desarrollo del subtitulo
  -> ::cue <- zona izquierda | ::note <- zona derecha

PLANTILLA AUREA — zona corta a la DERECHA:
  . Izquierda amplia: desarrollo del subtitulo
  . Derecha angosta: imagenes, complementos visuales escritos por el alumno
  -> ::note <- zona izquierda | ::cue <- zona derecha

Si NO se detectan lineas divisorias notorias -> aplicar flujo Variante A (TABnote simple).
Si hay ambiguedad en la deteccion -> indicar al usuario antes de continuar.
_
ORDEN DE LECTURA POR ZONA:
1. Zona titulo (franja superior)
2. Zona desarrollo (::note) — de arriba hacia abajo
3. Zona corta (::cue) — de arriba hacia abajo
4. Zona resumen (franja inferior)

Excepcion: si un desarrollo en ::note continua visualmente hacia ::cue
de forma evidente (formula partida, tabla), leerlo como unidad continua.
_
DETECCION DE TITULOS:
- Titulo principal: texto centrado, color #BB3E03, con resaltador lateral simetrico
  y linea delgada debajo -> # en Markdown (uno por archivo)
- Subtitulo: texto con resaltador que llega hasta el borde derecho del area util,
  color calido variable, numerado (1., 2., 3...) -> ## en Markdown
  (preservar el numero — es ancla de orden)
- Nunca usar ### salvo sub-subtitulo con desarrollo propio evidente
_
DETECCION DE CALLOUTS:
Caja de 4 lados con grosor notable, primera linea "> Titulo":
  . "> Ejercicio" -> ##### Ej. [enunciado]
  . "> Tarea"     -> > [!important] Tarea: [contenido]
  . Otros         -> > [!note] [Titulo]: [contenido]
_
DETECCION DE IMAGENES (IMA):
Bloque delimitado por 2 lineas grises horizontales con texto "IMA . descripcion" en gris.
NLM NO transcribe ni genera la imagen.
-> colocar exactamente en la posicion donde estaba (::cue o ::note segun zona):
   ![[pegar_imagen]]
   *IMA . [descripcion del pie]*
_
DETECCION DE MARGINALIA:
Linea de resaltador que sobrepasa el borde del area util hacia el margen externo.
Simbolo escrito en el margen externo. Traducir segun tabla:

| Simbolo | Tag marginalia    |
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

Colocar la marginalia inline junto al elemento que acompaña, respetando zona (::cue o ::note).
T- es exclusivo de supernova — no heredar a notas derivadas.
_
CONVENCIONES DE ESCRITURA DEL APUNTE:
- valor[unidad] -> preservar tal cual: 940[V], 470[ohm], 2[A]
- por tanto -> preservar como simbolo de sintesis
- -> ver Txx -> preservar como referencia cruzada
- Flechas con texto anotado -> incluir como nota al pie del elemento
- Flechas sin texto -> ignorar
_
BLOQUES CORNELL — TRANSCRIPCION LITERAL:
En estas plantillas el alumno ya escribio el contenido de ::cue y ::note
durante la clase. NLM transcribe ambas zonas textualmente — sin reformular,
sin agregar, sin omitir.

ESTRUCTURA DE OUTPUT:

## [N. Subtitulo]

`````
cornell
::cue
[transcripcion textual de la zona corta del apunte]
[IMA en su posicion -> ![[pegar_imagen]] + pie]
[marginalia respetando posicion]

::note
[transcripcion textual de la zona de desarrollo]
[IMA en su posicion -> ![[pegar_imagen]] + pie]
[marginalia respetando posicion]
`````

>[!summary] [transcripcion textual de la zona resumen del apunte]

> [!note] Complemento NLM
>
> **Resumen desde fuentes:** [NLM genera sintesis del subtitulo desde libros fuente]
> **Palabras clave:** [NLM extrae terminos clave del subtitulo]
> **Preguntas:** [NLM genera 2-4 preguntas de comprension desde libros fuente]

> [!note] Complemento (Nivel B/C)
>
> [definicion formal + ejercicios segun nivel pedido — desde libros fuente]

REGLAS:
- BUG NotebookLM: el identificador cornell va en linea separada de los backticks — obligatorio
- El ## del subtitulo NO va dentro del bloque Cornell
- La transcripcion en ::cue y ::note es LITERAL — no reformular
- Si la zona corta esta vacia -> ::cue vacio, NLM no inventa contenido
- Si la zona resumen esta vacia -> [!summary] vacio, NLM no inventa contenido
- Complemento NLM: SIEMPRE presente
- El Complemento NLM y el Complemento B/C van SIEMPRE fuera del Cornell
- Ejemplos resueltos del apunte van fuera del Cornell, entre [!summary] y Complemento NLM
_
NIVELES DE COMPLEMENTO B/C:
NIVEL B: definicion formal del libro si la del apunte es informal o incompleta.
NIVEL C: definicion formal + propiedades omitidas + 1-2 ejercicios resueltos + grafica TikZJax si aplica.
SIN EJERCICIOS aunque se pida C: axiomas, listas de propiedades puras.
NIVEL C COMPLETO cuando: procedimiento aplicable o apunte ya tiene ejemplos.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar que no se entiende y su posicion exacta en el PDF. Esperar respuesta.
_
JERARQUIA MARKDOWN:
# -> Titulo principal (uno por archivo)
## -> Subtitulo numerado
### -> Sub-subtitulo solo si tiene desarrollo propio evidente
_
FORMATO MATEMATICO:
Preferir inline $...$. Usar display $$...$$ solo para desarrollos multilinea.
$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \\
                & = & \text{expr}_3
\end{array}$$
& separa columnas . \\ termina fila (ultima sin \\) . \text{} para texto en math
_
GRAFICOS:
IMA es la estrategia principal. TikZJax solo para diagramas reproducibles con codigo corto.
Si hay duda -> IMA. Nunca inventar. Nunca mezclar.
REGLAS TIKZJAX: ```tikz exacto . \begin{document} y \end{document} siempre .
\documentclass NUNCA . paquetes antes de \begin{document} . color principal teal / secundario orange.
_
EJEMPLOS RESUELTOS:
Van fuera del Cornell, entre [!summary] y Complemento NLM.
##### Ej. enunciado en la misma linea.
Transcripcion literal — no agregar pasos. Preservar valor[unidad].
> [!note] solo si hay observacion relevante — no por defecto.
_
NOTACION LATEX: consultar [MATERIA]_latex.md si existe, o MAT101_latex.md como base.
_
FUENTES CARGADAS EN EL NOTEBOOK:
%%
Completar con los nombres exactos de archivo tal como estan importados en NLM.
Modelo: ver ETN607-transcription-divisions.md seccion FUENTES CARGADAS EN EL NOTEBOOK.

  apuntesTX                    -> PDF del apunte del tema activo
  _library_[MATERIA].md        -> indice de navegacion entre libros
  obsidian_notation.md         -> notacion Obsidian del vault
  [nombre-exacto-archivo.pdf]  -> descripcion breve
  ...
%%
_
LIBROS PRIORITARIOS POR TEMA:
%%
Completar con el stack de _library_[MATERIA].md al crear el prompt de la materia.
Modelo: ver ETN607-transcription-divisions.md seccion LIBROS PRIORITARIOS POR TEMA.

— TEORIA (complemento NLM + B/C) —
T1  [libro] Cap.X
...

— EJERCICIOS (Mensaje 2) —
T1  [libro] Cap.X
...
%%
_
SALTOS DE LINEA: texto compacto, sin lineas vacias innecesarias. El apunte siempre tiene prioridad.
