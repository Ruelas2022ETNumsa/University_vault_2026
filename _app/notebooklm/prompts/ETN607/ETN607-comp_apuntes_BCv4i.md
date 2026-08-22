TAREA:
Dado un rango de subtítulos o un concepto individual de ETN607 (Mecánica Aplicada),
buscar en los libros fuente el complemento nivel B o C y las figuras relevantes.

FUENTES: usar solo los libros cargados en este notebook y _library_ETN607.md.
No usar conocimiento general. Consultar _library_ETN607.md para criterio de selección de libros y capítulos por tema.

MENSAJES POSIBLES:

MENSAJE 1 — rango de subtítulos:
"De [fuente], desde subtítulo X hasta subtítulo Y, complemento nivel B/C"
→ buscar en los libros fuente según _library_ETN607.md
→ entregar complemento para cada subtítulo del rango
→ si un subtítulo no tiene complemento relevante → omitirlo sin avisar

MENSAJE 2 — concepto o subtítulo individual (para prueba o consulta puntual):
"Complemento nivel B/C: [nombre del concepto o subtítulo]"
→ buscar el concepto directamente en los libros fuente
→ entregar un solo bloque de complemento para ese concepto
→ misma estructura que Mensaje 1

NÚMERO DE PÁGINA (opcional en cualquier mensaje):
El usuario puede indicar el número de página del apunte como referencia de contexto.
Formato de ejemplo: "De apuntesTX, página X, desde subtítulo Y hasta subtítulo Z, complemento nivel B/C"
El número de página está impreso en la parte inferior derecha de cada hoja del apunte,
dentro de un recuadro, sobre el margen inferior.
Si el mensaje incluye número de página → localizar esa página primero antes de buscar el subtítulo.
Si no se indica → buscar por subtítulo normalmente.

NIVEL B: definición formal del libro + figura si existe.
NIVEL C: definición formal + propiedades omitidas + 1-2 ejercicios resueltos + figura si aplica.
  Si no hay figura en el libro → intentar TikZJax para el ejercicio (ver reglas abajo).
SIN ejercicios (aplicar B): axiomas, listas de propiedades puras, notación formal.
NIVEL C cuando: procedimiento aplicable, coordenadas/restricciones con casos concretos, el concepto tiene ejemplos canónicos en los libros → agregar uno de mayor dificultad.

FORMATO DE RESPUESTA POR SUBTÍTULO:

## [N. Subtítulo]

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
*[etiqueta de figura tal como aparece en el libro, ej: Fig. 2-4] · [descripción]*
→ descripción:
    · Si el libro tiene texto descriptivo → usarlo tal cual
    · Si no hay texto → generar una línea máximo basada en lo que se ve
      en la figura y el contexto del subtítulo. No inventar detalles técnicos.
      Si la figura es ambigua → omitir descripción.
→ agregar al pie el bloque de localización en este formato exacto (dos líneas):
[[nombre del archivo PDF#page=N]]
*Fig. X-X*
justificación: [por qué esta figura sirve — 1 oración, sin describir lo que se ve]
→ N es el número de página impreso en el libro (no el número del visor)
→ la etiqueta *Fig. X-X* debe coincidir exactamente con la del libro (con asteriscos de italics)
→ si hay más de una figura relevante → un bloque por figura

CASO B — no hay figura en el libro pero el concepto es geométrico o el ejercicio
tiene un diagrama representable → generar bloque TikZJax:
```tikz
\usepackage{tikz}
\begin{document}
% diagrama del concepto o ejercicio
\end{document}
```
Solo si el diagrama es simple: coordenadas, cuerpo libre, esquema geométrico básico.
Si hay duda sobre la complejidad → omitir y dejar espacio para IMA manual.

4. Ejercicios resueltos (solo nivel C)
##### Ej. [enunciado breve]
[resolución en LaTeX, array si corresponde]
Si el ejercicio involucra un diagrama y no hay figura en el libro → TikZJax (ver Caso B).

Si no hay figura ni diagrama aplicable → omitir sección 3.
``````

REGLAS GENERALES:
- Solo citar si podés confirmar fuente + página + id. Si no, omitir — no inventar.
- Figura: usar siempre ![[pegar_imagen]] + pie + bloque de localización ([[nombre.pdf#page=N]] + *Fig. X-X*). No usar embed de página completa.
- La etiqueta de figura es obligatoria como id (ej: Fig. 2-4). Si no hay etiqueta, usar el pie textual.
  Si tampoco hay pie, describir brevemente el visual como id.
- Podés citar más de una figura si son relevantes.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.

REGLAS TIKZJAX:
- Bloque exacto: ```tikz
- \begin{document} y \end{document} siempre presentes
- \documentclass NUNCA
- Paquetes antes de \begin{document}
- Color principal: teal · Color secundario: orange
- Solo para: coordenadas cilíndricas/esféricas, cuerpo libre simple, esquemas geométricos básicos
- Si hay duda sobre si el diagrama es representable → omitir, dejar espacio para IMA manual

LIBROS DISPONIBLES:
Taylor (dividido):
  caps.1-9   → John R. Taylor-Classical mechanics-eng-1to9.pdf
  caps.10-16 → John R. Taylor-Classical mechanics-eng-10to16.pdf
  (esp) caps.1-9   → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-1to9.pdf
  (esp) caps.10-16 → John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp-10to16.pdf
  soluciones → John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf
Goldstein (inglés): Goldstein & Poole & Safko-Classical Mechanics-3th ed-Pearson.pdf
Goldstein (esp):   H. Goldstein-Mecánica clásica-1994-ED REVERTE.pdf
Wells (ing):   Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf
Wells (esp):   Dare A. Wells-Dinamica de Lagrange-1972-McGraw-Hill-esp.pdf
Nelson:  Nelson & Best & McLean-schaums Statics and dynamics.pdf
Lim:     LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf
Alonso:  Alonso & Finn-Mecánica_Vol 1-1970-.pdf

TEORÍA POR TEMA (según _library_ETN607.md):
T1-T2 Taylor-1to9 Cap.1-2 · Alonso & Finn Vol.1
T3-T4 Taylor-1to9 Cap.7 · Goldstein Cap.1-2
T5 Taylor-1to9 Cap.7 y 4 · Goldstein Cap.1-2
T6 Taylor-1to9 Cap.7 · Goldstein Cap.1
T7 Wells Cap.7
T8 Goldstein Cap.4-5 · Taylor-10to16 Cap.10
