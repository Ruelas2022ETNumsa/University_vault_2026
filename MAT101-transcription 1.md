TAREA:%%> transcription 2 [[MAT101-study 1#^n9jesu]] {stitch: otra prueba para stitch}%%
Transcribir y complementar apuntes manuscritos universitarios de Cálculo I
a formato Markdown listo para Obsidian.
_
NOTACIÓN OBSIDIAN: consultar obsidian_notation.md (fuente del notebook) para interpretar YAML, wikilinks, Cornell, callouts y bloques de visualización.
_
FUENTES DE REFERENCIA: consultar MAT101_library.md (fuente del notebook) para criterio de selección, capítulos y páginas exactas de cada libro por tema.
-
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Dos mensajes por subtítulo:

MENSAJE 1 — Transcripción + complemento:
"De apuntesTX, muéstrame subtítulo Y [HASTA subtítulo Z] con complemento nivel B/C"
→ transcribir TODO el contenido desde Y hasta detectar el título Z (no incluirlo)
→ si no se indica HASTA, detenerse al detectar cualquier nuevo título rojo
→ NO adelantar el subtítulo siguiente

MENSAJE 2 — Ejercicios (solo si el usuario lo pide):
  "De apuntesTX, subtítulo Y, muéstrame ejercicios resueltos"
  → ejercicios de los libros fuente, con gráficas si aplica
  → NO repetir transcripción ni complemento ya entregado

MENSAJE 3 — Ejercicios del cuaderno:
  "De apuntesTX, muéstrame el ejercicio [a) $ec$] hasta [b) $ec$] con complemento nivel B/C"
  → buscar en el PDF los ejercicios indicados por su enunciado (no por subtítulo)
  → los incisos a) b) c)... están escritos en rojo en el cuaderno
  → transcribir resolución completa con gráficas si aplica
  → usar mismo formato que Mensaje 2: ##### Ej., array LaTeX, Desmos/TikZJax
  → complemento nivel B/C va después, igual que en Mensaje 2
  → NO repetir transcripción ni complemento ya entregado
_
ORDEN DE LECTURA DEL PDF:
Cada página está dividida en dos mitades verticales.
Leer siempre:
1. Mitad izquierda completa (de arriba hacia abajo).
2. Mitad derecha completa (de arriba hacia abajo).
3. Pasar a la siguiente página.

Excepción: si un desarrollo, tabla o fórmula comienza en la mitad izquierda
y continúa en la derecha de forma evidente, leerlo como unidad continua.
_
DETECCIÓN DE TÍTULOS:
Títulos en rojo. Tamaño determina jerarquía:
- Rojo grande → ## | Rojo mediano → ###
_
ESTILO DE TRANSCRIPCIÓN:
- Corregir ortografía y errores evidentes de notación matemática.
- Manuscrito como esqueleto principal. Estilo apuntes universitarios.
- Corrección importante → nota breve al final de esa sección.
_
BLOQUES CORNELL:
Aplicar a subtítulos de teoría: definiciones, axiomas, teoremas, propiedades, procedimientos
paso a paso. NO aplicar a ejemplos resueltos, ej , demostraciones.

ESTRUCTURA:

## [SUBTITULO Y]

````
cornell
::cue

[contenido de las claves]<br>
[palabras clave separadas por · ]<br>
[2-4 preguntas centrales que el subtítulo responde, según su complejidad]<br>
[fórmula o definición clave en inline $...$ — nunca display $$]<br>
[conexiones: "ver también: X" — solo si hay un subtítulo relacionado evidente jamas usar corchetes solo palabras ]<br>
[errores comunes: "no confundir X con Y" — solo si aplica]<br>
[mnemónico — solo si el subtítulo tiene una lista de 5 o más ítems]

::note

[transcripción fiel del subtítulo: texto, fórmulas y gráficas]

ESTRUCTURA GRAFICA (si hay graficas en los apuntes):
DESMOS:
```
left= ;right= ;bottom= ;top= ;
width= ;height= ;
---
[ecuaciones con modificadores][color defalut #005F73]
```
TIKZJAX:
```tikz
\begin{document}
\begin{tikzpicture}

\end{tikzpicture}
\end{document}
```

````

>[!summary]( resumen una línea del subtítulo sin redundancia de otros subtítulos)

##### [aca vienen los ejemplos, demostraciones y ejerccicios resueltos]

REGLAS:
- usar la etiqueta de `[!summary]` y no resumen en el bloque de resumen
- en la esctructura de cornell debe colocarse `cornell`antes de ::cue de forma obligatoria
- El subtítulo Y del archivo NO va dentro del bloque Cornell.
- Gráficas Desmos width máximo 320px.
- Graficas desmos el uso de label es por ejemplo : (2, 0) | label:(d-b)/(a-c)
- en la esctructura de los bloques desmos debe colocarse `desmos-graph`antes de left= ... de forma obligatoria
- TikZJax tamaño normal.
- Complemento, ejercicios y demostraciones van siempre FUERA del Cornell, después del Resumen.
_
NIVELES DE COMPLEMENTO:
Va DESPUÉS del Cornell (fuera del bloque), con este formato exacto:
> [!note] Complemento (Nivel B/C)
>  
>   contenido...

NIVEL B — Solo definición reforzada (sin ejercicios):
- Agregar definición formal del libro si la del manuscrito es informal.

NIVEL C — Complemento completo:
- Definición formal + propiedades omitidas + 1-2 ejercicios resueltos
  extraídos de los libros fuente + gráfica si aporta claridad.

SIN EJERCICIOS aunque se pida C (aplicar B):
- Axiomas y propiedades fundamentales (cuerpo, orden, igualdad).
- Listas de propiedades puras sin aplicación procedimental.
- Notación y definiciones formales sin desarrollo algorítmico.

NIVEL C COMPLETO cuando:
- Aplicación directa: dominio, valor absoluto, inecuaciones.
- Métodos procedimentales: método de signos, completar cuadrados.
- Funciones con dominio/rango no trivial: trigonométricas inversas, compuestas.
- El manuscrito ya tiene ejemplos → agregar uno de mayor dificultad.

SIN REDUNDANCIA:
- Cada subtítulo es independiente. No adelantar el siguiente.
- No repetir definiciones previas — solo referenciarlas brevemente.
_
CUANDO ALGO NO SE ENTIENDE:
Detenerse, indicar qué no se entiende y su posición (ej: "mitad derecha,
tercer renglón"). Esperar respuesta antes de continuar.
_
JERARQUÍA MARKDOWN:
# → Título principal (uno por archivo).
## → Sección principal (rojo grande).
### → Subsección (rojo mediano, solo si tiene desarrollo propio).
Nunca ### para ítems de listas. Sin niveles más profundos.
_
TEOREMAS, DEFINICIONES Y PROPIEDADES:
Nombre en negrita, fórmula en línea siguiente con tab:
1. **Nombre**
	- $formula_1$ / $formula_2$
	- Explicación si aplica.
No usar — para separar nombre de fórmula en la misma línea.
_
FORMATO MATEMÁTICO:
Preferir inline $...$. Usar display $$...$$ solo para:
ESTRUCTURA DE LATEX ARRAY
$$\begin{array}{rcll}
  \text{expr}_1 & = & \text{expr}_2 & (\text{justificación}) \
                & = & \text{expr}_3 & (\text{justificación}) \
  \text{expr}_1 & = & \text{expr}_n & (\text{LQQD})
\end{array}$$
O
$$\begin{array}{rcl}
  \text{expr}_1 & = & \text{expr}_2 \
                & = & \text{expr}_3 \
  \text{expr}_1 & = & \text{expr}_n
\end{array}$$
REGLAS DE LATEX ARRAY
- Nunca convertir símbolos a texto si el manuscrito los presenta simbólicamente.
- `&` separa columnas — siempre N-1 `&` para N columnas
- `\\` termina cada fila — la última fila **no** lleva `\\`
- Celdas vacías → dejar en blanco entre `&&`
- Texto dentro de math → `\text{...}`
- El `$$..$$` envuelve todo el bloque
- INICIO `$$\begin{array}{rcl}` O `$$\begin{array}{rcll}`
- FIN `\end{array}$$`
_
NOTAS AL MARGEN Y DEL MANUSCRITO:
Las notas van dentro del Cornell.
> [!note] observaciones aclaratorias
> [!important] advertencias, "No para examen", tareas
Separador ∼o∼ entre temas → ignorar. Flechas y marcas sin texto → ignorar.
_
GRÁFICOS — elegir en orden:
1. Desmos: funciones, curvas, rectas numéricas, intervalos, trigonométricas,
   parábolas, exponencial, logarítmica. Múltiples intervalos: y=0, y=1, y=2...
   Sintaxis completa: sección NOTEBOOKLM de
   MAT101_desmos.md — obligatoria sin excepción.
   Mínimos: "---" siempre · sin llaves en restricciones
2. TikZJax: conjuntos, composición (óvalos A→B→C), circunferencia trigonométrica,
   función inversa con espejo y=x, figuras geométricas. Sintaxis: MAT101_TikzJax.md
3. No reproducible → > [!note] Gráfico manuscrito + descripción textual.
Nunca inventar gráficos ni mezclar herramientas.
_
EJEMPLOS RESUELTOS:
##### Ej. enunciado en la misma línea. Display si multilínea (debajo del bloque de resumen).
Conservar numeración de partes. No agregar pasos que no estén en el manuscrito.
Al final de un ejercicio, agregar > [!note] solo si hay una observación
relevante o conexión importante — no por defecto.
_
SALTOS DE LÍNEA: texto compacto, sin líneas vacías innecesarias. El manuscrito siempre tiene prioridad — revisar el PDF en la sección indicada y corregir.
_
NOTACIÓN LATEX: consultar MAT101_latex.md (fuente del notebook) para cancelaciones,
colores, cajas de resultado, fracciones y desarrollos multilínea.
_
LIBROS PRIORITARIOS POR TEMA:
Consultar siempre las fuentes cargadas en el notebook según el tema.
Para ejercicios, Schaum's, Maron y Demidovich son válidos en cualquier tema.
El Stewart 7ma en español es el puente lingüístico — usarlo para confirmar terminología en español.

LIBROS POR TEMA (ARCHIVOS DIVIDIDOS):
Apostol: 1to7|8to16 · Thomas: 1to6|7to12|13to17 · Stewart 7ma: 1to4|5to8|9to11

— P1 —
T0 Números reales:        Apostol(1to7) · Stewart 9na · Stewart 7ma(1to4)
T1 Funciones reales:      Stewart 9na · Piskunov · Stewart 7ma(1to4)
T2 Límites y continuidad: Stewart 9na · Piskunov · Stewart 7ma(1to4)

— P2 —
T3 Derivación:            Stewart 9na · Piskunov · Stewart 7ma(1to4)
T4 Aplic. derivación:     Stewart 9na · Piskunov · Thomas(1to6) · Stewart 7ma(1to4)

— P3 —
T5 Integración:           Stewart 9na · Piskunov · Stewart 7ma(5to8)
T6 Aplic. integración:    Piskunov · Stewart 9na · Thomas(1to6) · Stewart 7ma(5to8)

— EXTRA —
T7 Series reales:         Apostol(8to16) · Stewart 9na · Stewart 7ma(9to11)

Apostol primera fuente en T0 (axiomas) y T7 (series).
Stewart 9na columna vertebral en T1–T5. Piskunov segunda fuente clave en T1–T6.
Thomas consulta puntual en T4 y T6.