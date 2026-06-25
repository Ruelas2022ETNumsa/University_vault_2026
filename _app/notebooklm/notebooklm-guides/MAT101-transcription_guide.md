---
title: "transcription-guide"
galaxy_body: beacon
scope: vault
audience: [usuario, chatgpt, claude]
related_notes:
  - "[[class-notes-guide]]"
  - "[[_note-system]]"
  - "[[desmos_guide]]"
  - "[[tikzjax_guide]]"
tags: [beacon, chatgpt, claude, transcripcion, infraestructura]
date_created: 2026-06-02
date_updated: 2026-06-05
status: activo
---

TAREA:
Transcribir apuntes manuscritos universitarios de Cálculo I a formato Markdown.

---

FLUJO DE TRABAJO:
1. El usuario proporcionará un PDF manuscrito.
2. Antes de transcribir, analizar todo el documento.
3. Identificar títulos y subtítulos principales.
4. Mostrar únicamente la estructura general detectada.
5. Esperar a que el usuario indique qué sección transcribir.
6. Transcribir sección por sección.

---

ORDEN DE LECTURA DEL PDF:
Cada página está dividida en dos mitades verticales.
Leer siempre:
1. Mitad izquierda completa (de arriba hacia abajo).
2. Mitad derecha completa (de arriba hacia abajo).
3. Pasar a la siguiente página.

Excepción: si un desarrollo, tabla o fórmula comienza en la mitad izquierda
y continúa en la derecha de forma evidente, leerlo como unidad continua.

---

DETECCIÓN DE TÍTULOS:
Los títulos están escritos en rojo.
El nivel jerárquico se determina por tamaño relativo dentro de la página:
- Texto rojo grande → ## (sección principal)
- Texto rojo mediano → ### (subsección)
Reportar ambos niveles al mostrar la estructura general.

---

ESTILO DE TRANSCRIPCIÓN:
- Corregir ortografía.
- Corregir errores evidentes de notación matemática.
- Mantener el contenido original del manuscrito.
- No agregar teoría externa.
- No expandir explicaciones.
- No agregar preguntas, ejercicios ni ejemplos que no estén en el manuscrito.
- Mantener estilo de apuntes universitarios.
- Si se realiza una corrección importante, informarla brevemente al final
  de esa sección como nota separada.

---

CUANDO ALGO NO SE ENTIENDE:
Si una palabra, símbolo o expresión no puede leerse con certeza:
- Detenerse antes de transcribir esa parte.
- Preguntar al usuario mostrando exactamente qué no se entiende
  y en qué posición de la página aparece (ej: "mitad derecha, tercer renglón").
- Esperar respuesta antes de continuar.

---

JERARQUÍA MARKDOWN:
# → Título principal de la nota (uno solo por archivo).
## → Sección principal (rojo grande).
### → Subsección (rojo mediano, solo si tiene desarrollo propio).
Nunca usar ### para ítems individuales de una lista de axiomas o propiedades.
Evitar niveles más profundos salvo necesidad real.

---

TEOREMAS, DEFINICIONES Y PROPIEDADES:
Nombre en negrita, fórmula en línea siguiente con tab:

1. **Nombre del axioma / teorema / propiedad**
	- $formula_1$
	- $formula_2$

Si tiene una sola fórmula:
1. **Nombre**
	$formula$

Si tiene explicación textual además de fórmula:
1. **Nombre**
	- $formula$
	- Explicación en español.

No usar — para separar nombre de fórmula en la misma línea.

---

FORMATO MATEMÁTICO:
Preferir fórmulas en línea: $a+b=c$

Usar bloque display ($$...$$) solo cuando:
- El desarrollo tiene más de una línea.
- Hay matrices o sistemas de ecuaciones.
- La fórmula es el resultado principal de una definición o teorema.

Para desarrollos algebraicos multilínea usar:
$$
\begin{array}{rcl}
f(n) & = & (n+1)^3 \\
     & = & n^3 + 3n^2 + 3n + 1
\end{array}
$$

Nunca convertir símbolos matemáticos a texto si el manuscrito los presenta
simbólicamente.

---

TABLAS:
Conservar estructura de tablas Markdown.
Dentro de tablas, nunca usar | directamente en expresiones matemáticas.
Usar $\vert x \vert$ para valor absoluto y $\Vert v \Vert$ para norma.

---

OBSERVACIONES Y NOTAS DEL MANUSCRITO:
Usar callouts de Obsidian:
> [!note]
> Texto de la observación.

> [!important]
> Texto.

---

GRÁFICOS:
Antes de generar cualquier gráfico, determinar la herramienta según este orden:

1. Funciones, curvas, rectas numéricas, intervalos, gráficas trigonométricas → Desmos
   Ver desmos_guide.md para sintaxis completa.

2. Diagramas de conjuntos con flechas, circunferencia trigonométrica,
   función inversa con espejo y=x, figuras geométricas estructuradas → TikZJax
   Ver tikzjax_guide.md para sintaxis completa.

3. No reproducible (sketch libre, diagrama conceptual sin estructura fija) →
   > [!note] Gráfico manuscrito
   > Descripción textual: tipo de gráfico, elementos visibles, etiquetas.

Nunca inventar gráficos que no existan en el manuscrito.
Nunca forzar en Desmos lo que corresponde a TikZJax ni viceversa.

TIPOS DE GRÁFICOS EN ESTE PDF (Cap. I — Funciones reales):
- Gráficas de funciones (parábola, exponencial, logarítmica, trigonométricas) → Desmos
- Diagrama de composición de funciones (óvalos con flechas A→B→C) → TikZJax
- Circunferencia trigonométrica con puntos etiquetados → TikZJax
- Función inversa con espejo y=x → TikZJax
- Rectas numéricas con intervalos → Desmos (ver reglas específicas abajo)
- Gráficas de seno, coseno, tangente → Desmos
- Función valor absoluto, escalón, distancia, signo → Desmos por tramos

---

GRAFICA DE RECTA NUMÉRICA E INTERVALOS:
Cuando el manuscrito muestra una recta numérica con intervalos,
reproducirla con desmos-graph siguiendo estas reglas.

NOTACIÓN DE INTERVALOS (usada en el manuscrito):
- [a,b]   → cerrado en ambos extremos (incluye a y b)
- ]a,b]   → abierto en a, cerrado en b
- [a,b[   → cerrado en a, abierto en b
- ]a,b[   → abierto en ambos extremos
- ]a,+∞[  → desde a sin incluirlo hasta infinito positivo
- ]-∞,b[  → desde menos infinito hasta b sin incluirlo
- [a,+∞[  → desde a incluido hasta infinito positivo
- ]-∞,b]  → desde menos infinito hasta b incluido

ORDEN DE DIBUJO EN DESMOS:
1. Primero todas las líneas horizontales (los intervalos).
2. Luego todos los puntos (extremos cerrados sin OPEN, abiertos con OPEN).

PUNTOS:
- Extremo incluido (corchete cerrado [ o ]) → punto sin OPEN
- Extremo no incluido (corchete abierto ] o [) → punto con OPEN

INTERVALOS HACIA EL INFINITO:
Extender la línea hasta el borde de la ventana visible y continuar
con DOTTED más allá para simular el infinito.
Los valores de corte (ej: -5, 5) son límites visuales solamente,
no son extremos matemáticos del intervalo.

MÚLTIPLES INTERVALOS EN LA MISMA RECTA:
Usar niveles verticales distintos para separarlos visualmente:
- Primer intervalo → y=0
- Segundo intervalo → y=1
- Tercer intervalo → y=2 (si fuera necesario)

OPERACIONES EN LOS VALORES:
Se pueden usar expresiones aritméticas directamente en el código.
Ejemplo: p+1 como extremo de un intervalo es válido en Desmos
y útil para relacionar extremos entre sí.

EJEMPLO — dos intervalos en la misma recta:
Azul: [-3, 3[
Rojo: ]-∞, -3[ ∪ [4, +∞[

```desmos-graph
left=-6.5; right=6.5; bottom=-1; top=3;
width=350; height=150;
---
y=0 \{-3<=x<3\}|#2d70b3
(-3,0)|label:-3|#2d70b3
(3,0)|OPEN|label:3|#2d70b3

y=1 \{x<-5\}|#ff7b7b|DOTTED
y=1 \{-5<x<-3\}|#ff7b7b
(-3,1)|OPEN|label:-3|#ff7b7b

y=1 \{4<=x<5\}|#ff7b7b
y=1 \{x>5\}|#ff7b7b|DOTTED
(4,1)|label:4|#ff7b7b
```

---

EJEMPLOS RESUELTOS:
Cuando el manuscrito presenta un ejercicio con desarrollo algebraico:
- Encabezar con **Ej.** seguido del enunciado en la misma línea.
- El desarrollo va en bloque display si es multilínea.
- Si el ejemplo tiene partes (a), b), c)...) conservar esa numeración.
- No agregar pasos intermedios que no estén en el manuscrito.

---

NOTAS AL MARGEN:
El manuscrito tiene anotaciones fuera del cuerpo principal. Tratarlas así:
- Notas aclaratorias relevantes → > [!note] con el texto de la anotación.
- Notas como "No para examen", "Tarea", advertencias → > [!important]
- El separador visual ∼o∼ que aparece entre temas → ignorar, no transcribir.
- Flechas o marcas de énfasis (★, ✶) sin texto propio → ignorar.

---

NOTACIÓN DE FUNCIONES ESPECIALES:
Usar siempre la notación del manuscrito sin convertirla:
- Si el manuscrito escribe sen x → transcribir $\text{sen}\, x$ (no $\sin x$)
- Si escribe tg x → transcribir $\text{tg}\, x$ (no $\tan x$)
- arc sen, arc cos, arc tg → $\text{arc sen}$, $\text{arc cos}$, $\text{arc tg}$
- senh, cosh, tgh → $\text{senh}\, x$, $\cosh x$, $\text{tgh}\, x$
- sech, cosec → $\text{sech}\, x$, $\text{cosec}\, x$
Nunca sustituir notación hispanohablante por notación anglosajona.

---

SALTOS DE LÍNEA:
Mantener el texto compacto.
Evitar líneas vacías innecesarias.

---
CORRECCIONES DEL USUARIO:
Si el usuario corrige una transcripción:
1. Revisar nuevamente el PDF en esa sección.
2. Verificar contra el manuscrito original.
3. Corregir la transcripción.
4. El manuscrito siempre tiene prioridad sobre interpretaciones previas.

---

OBJETIVO:
Transcripción Markdown fiel al manuscrito, matemáticamente correcta
y lista para usar en Obsidian.