---
galaxy_body: dropship
carrier: "[[_hangar/pdfpp_embed_nblm/pdfpp_embed_nblm.md]]"
scope: prueba
status: activo
date: 2026-08-16
---

## Proposito

Prompts de prueba para el carrier `pdfpp_embed_nblm`. El objetivo es probar si NotebookLM puede, dado un subtítulo de ETN607, entregar un complemento nivel B simple con referencias a figuras de los libros fuente en formato embed de PDF++ (`![[archivo.pdf#page=N]]`), listo para pegar en Obsidian.

Estas pruebas son independientes del notebook de transcripción — van en un notebook duplicado o separado con las fuentes ya cargadas.

**Fuentes en el vault** (`E:\University_vault_2026\_PDF\ETN-607`):
- `Alonso & Finn-Mecánica_Vol 1-1970-.pdf`
- `Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf`
- `Goldstein & Poole & Safko-Classical Mechanics-3th ed-Pearson.pdf`
- `H. Goldstein-Mecánica clásica-1994-ED REVERTE.pdf`
- `John R. Taylor-Classical mechanics-eng.pdf`
- `John R. Taylor-Instructor's Manual to accompany Classical Mechanics-2005.pdf`
- `John R. Taylor-Mecánica clásica-2005-ED REVERTÉ-esp.pdf`
- `LimYung-kuo-Problems and Solutions on Mechanics-1994.pdf`
- `Nelson & Best & McLean-schaums Statics and dynamics.pdf`

> ⚠️ **Restricción conocida:** NotebookLM entrega el número de página impreso en el libro, no el número que el visor PDF cuenta. El embed puede tener desfase según el PDF (portada, índice, etc.). Registrar en `chronicle.md` si el desfase es consistente o variable.

---

## Prompts

%%
Convención:
### v[N] — descripción breve
**Objetivo:** qué se quiere probar
**Uso:** cómo se usa en NotebookLM
**Resultado:** completar tras la prueba
**Notas:** observaciones
[bloque de código con el prompt]
%%

---

### v1 — complemento B con embed PDF++

**Objetivo:** probar si NotebookLM puede entregar un complemento nivel B de un subtítulo dado directamente en el chat, con referencias a figuras de los libros fuente en formato embed PDF++.

**Uso:** pegar el prompt en el notebook con las fuentes ETN607 cargadas. Luego en el chat escribir el subtítulo a desarrollar (ej: `"Coordenadas generalizadas"`).

**Resultado:** pendiente

**Notas:** si NotebookLM genera el número de página impreso, el embed puede no coincidir con la página del visor — registrar en `chronicle.md`.

```
TAREA:
Dado un subtítulo de ETN607 (Mecánica Aplicada), desarrollar un complemento breve nivel B.

FUENTES: usar solo los libros cargados en este notebook — no usar conocimiento general.

FORMATO DE RESPUESTA:

1. Definición formal
Extraer del libro fuente la definición más clara y directa del concepto.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura (si existe)
Si en las fuentes hay una figura que ilustre directamente el concepto, incluir exactamente este formato:
[[nombre_exacto_del_archivo.pdf#page=N]]
Etiqueta: [etiqueta de figura tal como aparece en el libro, ej: "Figure 4.3", "Fig. 7.1"]
Figura vista: [descripción breve de qué muestra la figura — 1 línea]
Donde N es el número de página impreso en el libro.
Si no hay figura relevante, omitir esta sección.

REGLAS:
- Solo citar si podés confirmar fuente + página + etiqueta de figura. Si no, omitir — no inventar.
- El enlace debe usar exactamente el formato [[archivo.pdf#page=N]] con doble corchete — no usar ! delante, no usar corchete simple.
- El nombre del archivo debe coincidir exactamente con el nombre del PDF cargado.
- La etiqueta de figura es obligatoria — si el libro no tiene etiqueta, usar el pie de figura textual.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.
```

---

### v3 — complemento B con embed PDF++ (prompt de producción)

**Objetivo:** dado un rango de subtítulos, buscar en los libros fuente el complemento nivel B y las figuras relevantes con embed PDF++ + bloque IMA-SRC de respaldo. Este es el prompt de producción que reemplaza IMA-SRC puro.

**Uso:** cargar en notebook separado con los 9 libros de ETN607 + _library_ETN607.md. Mandar el mismo rango que se usó en el notebook de transcripción: "desde subtítulo X hasta Y".

**Fuentes del notebook:**
- _library_ETN607.md
- Los 9 libros de ETN607 (ver lista en prompt)
- NO cargar el PDF de apuntes manuscritos

**Resultado:** pendiente

**Notas:** el embed usa `[[]]` sin `!` — no renderiza inline, evita que Obsidian se lentee. El bloque IMA-SRC queda como localizador de respaldo mientras el desfase de numeración no esté resuelto.

``````
TAREA:
Dado un rango de subtítulos o un concepto individual de ETN607 (Mecánica Aplicada),
buscar en los libros fuente el complemento nivel B o C y las figuras relevantes.

FUENTES: usar solo los libros cargados en este notebook y _library_ETN607.md.
No usar conocimiento general. Consultar _library_ETN607.md para criterio de selección
de libros y capítulos por tema.

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

NIVEL B: definición formal del libro + figura si existe.
NIVEL C: definición formal + propiedades omitidas + 1-2 ejercicios resueltos + figura si aplica.
  Si no hay figura en el libro → intentar TikZJax para el ejercicio (ver reglas abajo).
SIN ejercicios (aplicar B): axiomas, listas de propiedades puras, notación formal.
NIVEL C cuando: procedimiento aplicable, coordenadas/restricciones con casos concretos,
  el concepto tiene ejemplos canónicos en los libros → agregar uno de mayor dificultad.

FORMATO DE RESPUESTA POR SUBTÍTULO:

## [N. Subtítulo]

`````ad-note
title: Complemento (Nivel B/C)

1. Definición formal
Extraer del libro fuente la definición más clara y directa.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura o diagrama (si existe o aplica TikZJax)

CASO A — figura en el libro:
[[nombre_exacto_del_archivo.pdf#page=N]]
*[etiqueta de figura tal como aparece en el libro, ej: Fig. 2-4]*
*[descripción breve si existe — omitir si no hay]*
%%IMA-SRC | fuente: [nombre del archivo PDF] | página: [número impreso] | id: [etiqueta de figura] | posición: [dónde está en la página]
justificación: [por qué esta figura sirve — 1 oración, sin describir lo que se ve]%%

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
`````

REGLAS GENERALES:
- Solo citar si podés confirmar fuente + página + id. Si no, omitir — no inventar.
- El embed usa doble corchete sin ! → [[archivo.pdf#page=N]]
- El nombre del archivo debe coincidir exactamente con el nombre del PDF cargado.
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
Wells:   Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf
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

``````

---

### v2 — complemento B con embed + IMA-SRC (comparación)

**Objetivo:** probar la misma consulta que v1 pero pidiendo ambos formatos — embed PDF++ e IMA-SRC — para comparar cuál es más útil en la práctica y detectar diferencias en el número de página reportado.

**Uso:** igual que v1. Correr con el mismo subtítulo que v1 para comparar output.

**Resultado:** pendiente

**Notas:** comparar el número de página en IMA-SRC vs el del embed — si difieren, el problema de numeración es real y consistente.

```
TAREA:
Dado un subtítulo de ETN607 (Mecánica Aplicada), desarrollar un complemento breve nivel B.

FUENTES: usar solo los libros cargados en este notebook — no usar conocimiento general.

FORMATO DE RESPUESTA:

1. Definición formal
Extraer del libro fuente la definición más clara y directa del concepto.
Una sola definición — sin parafrasear, sin expandir.

2. Idea clave (opcional)
Solo si hay una propiedad o relación central que la definición no captura.
Máximo 2 líneas.

3. Figura (si existe)
Si en las fuentes hay una figura que ilustre directamente el concepto, incluir ambos formatos:

Embed PDF++:
![[nombre_exacto_del_archivo.pdf#page=N]]
*[pie de figura o etiqueta tal como aparece en el libro]*

Localizador IMA-SRC:
IMA-SRC | fuente: [nombre del archivo PDF] | página: [número impreso] | id: [etiqueta o pie de figura] | posición: [dónde está en la página]

Donde N es el número de página impreso en el libro.
Si no hay figura relevante, omitir esta sección.

REGLAS:
- Solo citar si podés confirmar fuente + página. Si no, omitir — no inventar.
- El nombre del archivo en el embed debe coincidir exactamente con el nombre del PDF cargado.
- Sin introducción, sin cierre, sin comentarios — solo el contenido estructurado.
- Respuesta compacta: no más de lo necesario para entender el concepto.
```
