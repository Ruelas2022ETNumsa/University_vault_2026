---
title: MAT101 — Guía de uso NotebookLM
galaxy_body: beacon
scope: vault
audience:
  - usuario
related_notes:
  - "[[_config/_notebooklm-system]]"
  - "[[prompts/MAT101/MAT101-study]]"
  - "[[prompts/MAT101/MAT101-transcription]]"
tags:
  - beacon
  - notebooklm
  - MAT101
  - infraestructura
date_created: 2026-06-03
date_updated: 2026-07-02
status: activo
---

# MAT101 — Guía de uso NotebookLM

> MAT101 tiene dos notebooks con prompts distintos: uno para **transcribir apuntes manuscritos** y otro para **estudiar y resolver ejercicios**. Esta guía explica cómo usar cada uno.

---

## Prompt de transcripción — `MAT101-transcription`

Convierte apuntes manuscritos (PDF escaneado o exportado desde tablet) en `.md` listo para Obsidian. Genera bloques Cornell, complemento de los libros y gráficas Desmos/TikZJax según corresponda.

**Cuándo usarlo:** cuando tenés un PDF de apuntes de un tema completo y querés transcribirlo subtítulo por subtítulo.

**Fuente del PDF en el notebook:** se sube con el nombre `apuntesTX` donde `X` es el código del tema (T0, T1, T2, etc.).

---

### Mensaje 1 — Transcripción + complemento

Este es el mensaje principal. Transcribe el contenido del subtítulo indicado y agrega complemento del nivel pedido.

**Sintaxis:**
```
De apuntesTX, muéstrame el subtítulo "[nombre exacto]" con complemento nivel [B/C]
```

**Con rango (de un subtítulo hasta otro):**
```
De apuntesTX, muéstrame el subtítulo "[nombre exacto]" HASTA "[nombre del siguiente]" con complemento nivel [B/C]
```

> Si no se indica HASTA, el notebook se detiene al detectar cualquier nuevo título. Si se indica HASTA, transcribe todo lo que hay entre ambos sin incluir el segundo.

**Niveles de complemento:**

| Nivel | Qué agrega |
|---|---|
| B | Solo definición formal del libro si la del manuscrito es informal |
| C | Definición formal + propiedades omitidas + 1-2 ejercicios resueltos + gráfica si aporta |

> Nivel C sin ejercicios (aplica B automáticamente) en: axiomas, propiedades puras, notación formal.

**Ejemplos:**

```
De apuntesT0, muéstrame el subtítulo "Axiomas de cuerpo de los números reales"
HASTA "Teoremas sobre números reales" con complemento nivel B
```

```
De apuntesT1, muéstrame el subtítulo "Dominio y rango de una función" con complemento nivel C
```

```
De apuntesT2, muéstrame el subtítulo "Definición de límite" HASTA "Propiedades de límites" con complemento nivel C
```

---

### Mensaje 2 — Ejercicios resueltos

Opcional. Se usa después del Mensaje 1 si querés ejercicios adicionales del mismo subtítulo, extraídos de los libros fuente.

**Sintaxis:**
```
De apuntesTX, subtítulo "[nombre exacto]", muéstrame ejercicios resueltos
```

> No repite la transcripción ni el complemento ya entregado — solo agrega los ejercicios.

**Ejemplos:**

```
De apuntesT1, subtítulo "Dominio y rango de una función", muéstrame ejercicios resueltos
```

```
De apuntesT3, subtítulo "Regla de la cadena", muéstrame ejercicios resueltos
```

---

## Prompt de estudio — `MAT101-study`

Actúa como tutor de Cálculo 1 orientado a ingeniería. Infiere el modo según lo que pedís — no hace falta activarlo explícitamente. Si hay ambigüedad, pregunta.

**Cuándo usarlo:** para entender conceptos, resolver ejercicios o practicar antes de un examen.

---

### Modo 1 · Explicación de concepto

Para entender un tema desde cero o en profundidad. El notebook explica intuitivamente, agrega rigor formal si aporta, conecta con los libros, incluye visualización si corresponde, y cierra con preguntas de comprensión y ejercicios resueltos de los libros.

**Lo activa:** pedir que expliquen un concepto, definición o tema.

**Qué devuelve:**
- Explicación intuitiva
- Definición formal (solo si aporta comprensión real)
- Referencia a libros del stack (reformulada, nunca copiada)
- Visualización Desmos o TikZJax si el concepto lo requiere
- 2-3 preguntas de comprensión
- 1-2 ejercicios resueltos de los libros

**Ejemplos:**

```
Explicame qué es la continuidad de una función en un punto
```

```
No entiendo la regla de la cadena, explicame desde el principio con un ejemplo
```

```
Explicame el teorema del valor medio según Piskunov
```

---

### Modo 2 · Ejercicio resuelto

Para resolver un ejercicio con desarrollo completo paso a paso. Incluye un ejercicio similar de mayor dificultad al final, extraído de los libros.

**Lo activa:** entregar un ejercicio para resolver.

**Qué devuelve:**
- Enunciado claro
- Desarrollo paso a paso sin saltear pasos algebraicos
- Visualización si aporta claridad
- Resultado final destacado con caja
- Ejercicio de mayor dificultad resuelto al final

**Ejemplos:**

```
Resolvé: encontrá el dominio de f(x) = sqrt(x^2 - 4) / (x - 1)
```

```
Resolvé paso a paso: lim(x→2) (x^2 - 4) / (x - 2)
```

```
Resolvé: derivá f(x) = sin(x^2) * e^(3x) usando regla de la cadena y producto
```

---

### Modo 3 · Ejercicio rápido

Para resolver sin explicación extra ni ejercicio adicional al final. Solo enunciado, desarrollo y resultado.

**Lo activa:** pedir que resuelvan sin extras, o aclarar que no querés ejercicio adicional.

**Qué devuelve:**
- Enunciado
- Desarrollo paso a paso
- Visualización si aplica
- Resultado final — sin ejercicio extra, sin preguntas

**Ejemplos:**

```
Solo resolvé, sin ejercicio extra: derivá f(x) = ln(cos(x))
```

```
Rápido: calculá la integral de x * e^x dx
```

```
Solo el resultado con desarrollo: lim(x→0) sin(3x) / x
```

---

## Fuentes del notebook

Ambos notebooks comparten el mismo stack de PDFs. Las guías `.md` varían según el notebook.

### PDFs (libros)

| Fuente | Rol |
|---|---|
| Stewart — *Calculus ET* 9na ed. | Teoría principal — columna vertebral |
| Apostol — *Calculus* Vol.1 2da ed. | Teoría rigurosa — axiomas y series |
| Piskunov — *Differential and Integral Calculus* Vol.1 | Teoría soviética — clara para ingeniería |
| Thomas — *Calculus* 14va ed. | Consulta puntual — aplicaciones geométricas |
| Stewart — *Cálculo ET* 7ma ed. (1to4 / 5to8 / 9to11) | Puente lingüístico español |
| Apostol (1to7 / 8to16) | Dividido por rango de capítulos |
| Thomas (1to6 / 7to12) | Dividido por rango de capítulos |
| Mendelson — *Schaum's 3000 Solved Problems* | Ejercicios de inicio |
| Maron — *Problems in Calculus of One Variable* | Ejercicios de práctica |
| Demidovich — *Problems in Mathematical Analysis* | Ejercicios nivel examen |

### Guías `.md` (fuentes de referencia técnica)

| Archivo | Contenido | Notebook |
|---|---|---|
| `MAT101_library.md` | Criterio de fuentes por tema, caps y páginas | ambos |
| `obsidian_notation.md` | Interpretación de YAML, Cornell, callouts, Desmos | ambos |
| `MAT101_desmos.md` | Sintaxis Desmos para Obsidian | ambos |
| `MAT101_TikzJax.md` | Sintaxis TikZJax para Obsidian | ambos |
| `MAT101_latex.md` | Notación LaTeX: cajas, cancelaciones, fracciones | ambos |

%%
galaxy-links
[[_config/_notebooklm-system]]
[[prompts/MAT101/MAT101-study]]
[[prompts/MAT101/MAT101-transcription]]
%%
