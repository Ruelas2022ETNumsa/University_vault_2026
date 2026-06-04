---
title: "NotebookLM — Guía de modos y triggers"
galaxy_body: beacon
scope: vault
audience: [usuario]
related_notes:
  - "[[desmos_guide]]"
  - "[[tikzjax_guide]]"
tags: [beacon, notebooklm, infraestructura]
date_created: 2026-06-03
status: activo
---

# NotebookLM — Guía de modos y triggers

> Referencia de uso del notebook de Cálculo 1. Describe cada modo del prompt de configuración, cómo activarlo y qué esperar como respuesta.

---

## Stack de fuentes del notebook

| Fuente | Uso principal |
|--------|--------------|
| Stewart — *Early Transcendentals* 9na ed. | Explicaciones, ejemplos visuales, límites, derivadas, integrales |
| Apostol — *Cálculo* Vol. 1 | Rigor formal, demostraciones, definiciones precisas |
| Piskunov — *Differential and Integral Calculus* Vol. 1 | Desarrollo clásico, teoría aplicada |
| Mendelson — *Schaum's 3,000 Solved Problems* | Ejercicios resueltos paso a paso, variedad de tipos |
| Maron — *Problems in Calculus of One Variable* | Ejercicios progresivos, estilo examen |
| Demidovich — *Course of Mathematical Analysis (Problems)* | Ejercicios de dificultad creciente, ingeniería |
| Thomas — *Calculus* 14va ed. | Explicaciones aplicadas, contexto de ingeniería |
| `desmos_guide.md` | Sintaxis Desmos para el plugin de Obsidian |
| `tikzjax_guide.md` | Sintaxis TikZJax para diagramas técnicos |
| Nota del alumno (`.md`) | Base de contexto — apuntes propios como referencia |

---

## Modos de respuesta

---

### MODO 1 · Explicación de concepto

**Para qué sirve:** entender un tema desde cero o en profundidad. NotebookLM explica de forma intuitiva primero, agrega rigor formal si aporta, conecta con los libros, incluye visualización Desmos si corresponde, y cierra con preguntas de comprensión más ejercicios resueltos de los libros.

**Triggers:**
```
"Explicame [concepto]"
"No entiendo [tema], explicame desde el principio"
"Modo 1 — [tema]"
"¿Qué es [definición]?"
```

**Ejemplo de trigger completo:**
```
Explicame el concepto de valor absoluto para ingeniería,
conectalo con inecuaciones y mostrá una visualización.
```

**Qué esperar como respuesta:**
- Explicación intuitiva en prosa
- Definición formal o demostración (si aporta comprensión real)
- Referencia a uno o más libros del stack (reformulada, no copiada)
- Bloque Desmos si el concepto es graficable
- 2-3 preguntas de comprensión al final
- 1-2 ejercicios resueltos extraídos de los libros

---

### MODO 2 · Ejercicio resuelto

**Para qué sirve:** resolver un ejercicio con desarrollo completo paso a paso, justificando cada paso. Incluye un ejercicio similar de mayor dificultad al final.

**Triggers:**
```
"Resolvé [ejercicio]"
"Modo 2 — [ejercicio]"
"Paso a paso: [problema]"
"¿Cómo se resuelve [tipo de ejercicio]?"
```

**Ejemplo de trigger completo:**
```
Resolvé la inecuación |2x - 3| > 5 paso a paso
y al final dame un ejercicio similar más difícil.
```

**Qué esperar como respuesta:**
- Enunciado claro
- Desarrollo numerado con justificación de cada paso
- Visualización Desmos si aporta (a criterio de NotebookLM)
- Resultado final destacado
- Ejercicio de mayor dificultad resuelto, extraído de los libros

---

### MODO 3 · Ejercicio rápido

**Para qué sirve:** resolver sin explicación adicional ni ejercicio extra al final. Solo los 4 pasos esenciales: enunciado, desarrollo, visualización si aplica, resultado.

**Triggers:**
```
"Solo resolvé [ejercicio]"
"Ejercicio rápido: [problema]"
"Modo 2.5 — [ejercicio]"
"Resolvé sin extras: [problema]"
```

**Ejemplo de trigger completo:**
```
Solo resolvé: encontrá los valores de x para los que
(x-1)(x+3) > 0
```

**Qué esperar como respuesta:**
- Enunciado
- Desarrollo paso a paso con justificación
- Visualización si aplica
- Resultado final — sin ejercicio extra, sin preguntas

---

### MODO 4 · Dictado para Obsidian

**Para qué sirve:** generar contenido listo para pegar directamente en una nota de Obsidian. Responde en texto plano sin introducción ni cierre — solo el bloque de contenido con título, desarrollo, código si aplica y resumen.

**Triggers:**
```
"Completá mi nota sobre [tema]"
"Dictame [concepto] para Obsidian"
"Modo 3 — [tema]"
"Dame el contenido para pegar en mi nota de [tema]"
```

**Ejemplo de trigger completo:**
```
Dictame el contenido de la propiedad triangular
del valor absoluto para pegar en mi nota.
```

**Qué esperar como respuesta:**
```markdown
## Título

[desarrollo en prosa con LaTeX]
[bloque Desmos si aplica]

> **Resumen en una línea.**
```
Sin texto antes ni después del bloque — directo al contenido.

---

### MODO 5 · Revisión de nota

**Para qué sirve:** revisar si el contenido matemático de una nota es correcto. NotebookLM identifica errores matemáticos (definición incorrecta, notación mal usada, paso inválido, omisión importante), señala imprecisiones de notación y sugiere qué agregar indicando de qué libro lo tomaría. Aplica a cualquier nota, no solo MAT101.

**Triggers:**
```
"Modo 4 — revisá la sección [nombre] de mi nota [nombre]"
"Revisá si esto es correcto: [pega la sección]"
"¿Hay errores en esta sección? [pega el contenido]"
"Corregí y mejorá: [pega el contenido]"
```

**Ejemplo de trigger completo:**
```
Modo 4 — revisá la sección "Axiomas de orden"
de mi nota MAT101. La tenés como fuente en el notebook.
```

**Qué esperar como respuesta:**
- Lista de errores encontrados (o confirmación de que no hay)
- Por cada error: fragmento original → explicación → versión corregida
- Imprecisiones de notación señaladas con versión mejorada
- Sugerencias de contenido complementario con referencia al libro y sección

---

## Triggers para tareas especiales

Estas no son modos formales — son pedidos directos que el prompt maneja bien.

---

### Resumen para examen

```
Generá un resumen de [sección/tema] de mi nota MAT101
estilo hoja de fórmulas para examen de ingeniería,
con las propiedades más importantes y condiciones de cada una.
```

**Qué esperar:** tabla o lista compacta con propiedades, fórmulas clave, condiciones de aplicación y casos especiales. Cruza tu nota con los libros para no omitir nada relevante.

---

### Guía de ejercicios tipo examen

```
Del tema [tema], generá una guía de 5 ejercicios progresivos
estilo examen de ingeniería, resueltos,
extraídos de los libros disponibles.
```

**Qué esperar:** 5 ejercicios de dificultad creciente, cada uno con enunciado y resolución paso a paso. NotebookLM prioriza Schaum's, Maron y Demidovich para este tipo de pedido.

---

### Profundizar con un libro específico

```
Explicame [tema] según Apostol.
¿Qué dice Stewart sobre [concepto]?
Buscá ejercicios de [tema] en Demidovich.
```

**Qué esperar:** respuesta anclada en el libro indicado, reformulada, sin copiar párrafos.

---

### Mejorar una sección específica de la nota

```
Tengo esto en mi nota sobre [tema]: [pega la sección].
¿Cómo lo mejorarías con los libros disponibles?
Agregá definiciones más precisas, ejemplos y
propiedades que falten.
```

**Qué esperar:** versión enriquecida de la sección con definiciones más completas, propiedades faltantes y ejemplos adicionales de los libros.

---

## Nota sobre el formato .md como fuente

Cuando subís una nota `.md` al notebook, NotebookLM la interpreta así gracias al prompt de configuración:

- Los separadores `--- start-multi-column` / `--- end-column ---` / `--- end-multi-column` son infraestructura visual — los ignora para el análisis matemático
- Columna izquierda (60%) = desarrollo → definiciones y fórmulas principales
- Columna derecha (40%) = claves → conceptos clave y condiciones
- `> Resumen:` = síntesis del subtema
- Bloques ` ```desmos-graph ``` ` = código de gráfica — los lee como referencia de sintaxis y como contexto del tema

%%
galaxy-links
[[desmos_guide]]
[[tikzjax_guide]]
%%
