---
title: "transcription-guide"
galaxy_body: beacon
scope: vault
audience: [usuario, notebooklm]
related_notes:
  - "[[class-notes-guide]]"
  - "[[_note-system]]"
  - "[[desmos_guide]]"
  - "[[tikzjax_guide]]"
tags: [beacon, notebooklm, transcripcion, infraestructura]
date_created: 2026-06-02
date_updated: 2026-06-25
status: activo
---

TAREA:
Transcribir y complementar apuntes manuscritos universitarios de Cálculo I
a formato Markdown listo para Obsidian.
_
FLUJO DE TRABAJO:
PDF del tema completo cargado como fuente apuntesTX. Dos mensajes por subtítulo:

MENSAJE 1 — Transcripción + complemento:
  "De apuntesTX, muéstrame subtítulo Y con complemento nivel B/C"
  → transcripción fiel + complemento según nivel
  → NO adelantar el subtítulo siguiente

MENSAJE 2 — Ejercicios (solo si el usuario lo pide):
  "De apuntesTX, subtítulo Y, muéstrame ejercicios resueltos"
  → ejercicios de los libros fuente, con gráficas si aplica
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
- Transcribir TODO el contenido del subtítulo hasta que inicie el siguiente título rojo.
  No omitir texto, notas al margen ni observaciones dentro del subtítulo.
- Corregir ortografía y errores evidentes de notación matemática.
- Manuscrito como esqueleto principal. Estilo apuntes universitarios.
- Corrección importante → nota breve al final de esa sección.
_
BLOQUES CORNELL:
Aplicar a subtítulos de teoría: definiciones, axiomas, teoremas, propiedades
y procedimientos paso a paso. NO aplicar a ejemplos resueltos.

ESTRUCTURA:
--- start-multi-column: cornell-TX-00N
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**
[transcripción fiel del subtítulo: texto, fórmulas y gráficas]

--- end-column ---

🔑 **Claves**
[dejar vacío]
%```desmos-graph
%```

--- end-multi-column

> **Resumen:** [una línea del subtítulo sin redundancia de otros subtítulos]

REGLAS:
- ID secuencial por tema: cornell-T0-001, cornell-T0-002, cornell-T1-001...
- Gráficas Desmos dentro de Desarrollo: width máximo 320px.
- TikZJax dentro de Desarrollo: tamaño normal.
- El bloque comentado %```desmos-graph / %``` en Claves es OBLIGATORIO
  siempre que haya un bloque Desmos en Desarrollo — sin él Desmos no renderiza.
- Si no hay Desmos en Desarrollo, omitir el bloque comentado en Claves.
- Complemento y ejercicios van siempre FUERA del Cornell, después del Resumen.
- El título principal del archivo NO va dentro del bloque Cornell.
_
NIVELES DE COMPLEMENTO:
Va DESPUÉS del Cornell (fuera del bloque), con este formato exacto:
> [!note] Complemento (Nivel B/C)
>
> contenido...

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
Preferir inline $...$. Usar display $...$ solo para:
- Desarrollo multilínea, matrices, sistemas, resultado principal de teorema.
Multilínea con \begin{array}{rcl}..\end{array}.
Nunca convertir símbolos a texto si el manuscrito los presenta simbólicamente.
_
TABLAS:
En tablas: $\vert x \vert$ para valor absoluto, $\Vert v \Vert$ para norma.
Nunca | dentro de expresiones matemáticas en tablas.
_
NOTAS DEL MANUSCRITO:
> [!note] observaciones aclaratorias
> [!important] advertencias, "No para examen", tareas
_
GRÁFICOS — elegir en orden:
1. Desmos: funciones, curvas, rectas numéricas, intervalos, trigonométricas,
   parábolas, exponencial, logarítmica. Múltiples intervalos: y=0, y=1, y=2...
   Sintaxis completa: sección NOTEBOOKLM de
   desmos_notebook_lm.md — obligatoria sin excepción.
   Mínimos: ```desmos-graph exacto · "---" siempre · sin llaves en restricciones
2. TikZJax: conjuntos, composición (óvalos A→B→C), circunferencia trigonométrica,
   función inversa con espejo y=x, figuras geométricas. Sintaxis: tikzjax_guide.md
3. No reproducible → > [!note] Gráfico manuscrito + descripción textual.
Nunca inventar gráficos ni mezclar herramientas.
_
EJEMPLOS RESUELTOS:
**Ej.** enunciado en la misma línea. Display si multilínea.
Conservar numeración de partes. No agregar pasos que no estén en el manuscrito.
Al final de un ejercicio, agregar > [!note] solo si hay una observación
relevante o conexión importante — no por defecto.
_
NOTAS AL MARGEN:
> [!note] notas aclaratorias · > [!important] advertencias y tareas.
Separador ∼o∼ entre temas → ignorar. Flechas y marcas sin texto → ignorar.
_
NOTACIÓN HISPANOHABLANTE (respetar siempre):
sen x → $\text{sen}\,x$ · tg x → $\text{tg}\,x$ · arc sen/cos/tg → igual.
senh, tgh, sech, cosec → con \text{}. Nunca sustituir por sin/tan/etc.
_
SALTOS DE LÍNEA: texto compacto, sin líneas vacías innecesarias. El manuscrito siempre tiene prioridad — revisar el PDF en la sección indicada y corregir.
_
LIBROS PRIORITARIOS POR TEMA — P1 (Parcial 1):
Consultar siempre las fuentes cargadas en el notebook según el tema.
Para ejercicios, Schaum's, Maron y Demidovich son válidos en cualquier tema.
El Stewart 7ma en español es el puente lingüístico — usarlo para confirmar
terminología en español.

LIBROS POR TEMA(ARCHIVOS DIVIDIDOS):
Apostol: 1to7|8to16 · Thomas: 1to6|7to12|13to17 · Stewart 7ma: 1to4|5to8|9to11

T0 Números reales: Apostol(1to7) · Stewart 9na · Stewart 7ma(1to4)
T1 Funciones reales: Stewart 9na · Thomas(1to6) · Stewart 7ma(1to4)
T2 Límites y continuidad: Stewart 9na · Apostol(1to7) · Stewart 7ma(1to4)

Apostol como primera fuente para T0 porque cubre axiomas y orden con
rigor formal. Para funciones y límites, Stewart 9na es primera opción.
