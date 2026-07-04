# Guía de notación Obsidian para NotebookLM

Esta guía explica cómo leer archivos Markdown generados en Obsidian
con el sistema Galaxy. Su propósito es evitar errores de interpretación
al usarlos como fuentes en NotebookLM.

---

## 1. Metadatos — ignorar completamente

**Bloque YAML** — aparece al inicio de cada archivo entre `---`:
```
---
title: Nombre del archivo
tags: [beacon, mat101]
date_created: 2026-01-01
---
```
No contiene contenido matemático. Ignorar por completo.

**Bloques de comentario** — aparecen al final del archivo entre `%%`:
```
%%
galaxy-links
[[nota_relacionada]]
%%
```
Son metadatos internos del vault. Ignorar por completo.

**Wikilinks** — referencias internas con doble corchete:
```
[[nombre-de-nota]]  →  ignorar
[[nota|texto visible]]  →  ignorar
```
No son fuentes externas. No intentar resolver el enlace.

---

## 2. Estructura Cornell

Las notas de teoría usan un bloque de dos columnas generado por
el plugin Cornell Notes (bytetiles/obsidian-cornell-notes). El bloque
completo tiene esta forma:


````cornell
::cue

🔑 Claves
[palabras clave, preguntas, fórmula central, conexiones]

::note

📝 Desarrollo
[contenido principal: definiciones, fórmulas, desarrollo]

````

**Marcadores** — son infraestructura del plugin, no contenido:
- ` ````cornell ` → marca inicio del bloque
- `::cue` → delimita la columna izquierda (Claves)
- `::note` → delimita la columna derecha (Desarrollo)
- ` ```` ` de cierre → marca fin del bloque

**Orden de lectura del contenido:**
1. Claves (`::cue`, columna izquierda) → síntesis y conexiones
2. Desarrollo (`::note`, columna derecha) → contenido principal
3. Callouts debajo del bloque (`> [!summary]`) → resumen de cierre

---

## 3. Callouts

Son bloques de aviso con esta sintaxis:
```
> [!note] Título opcional
> Contenido del callout.

> [!important] Título opcional
> Contenido importante.
```

- `[!note]` → observación aclaratoria o complemento de contenido
- `[!important]` → advertencia relevante (ej: "no entra al examen", tarea)

Leer el contenido normalmente. El tipo de callout indica su peso,
no es sintaxis especial que deba ignorarse.

---

## 4. Ejemplos resueltos

Los ejemplos resueltos usan encabezado de nivel 5:
```
##### Ej. 3 — Calcular el dominio de f(x) = √(x−1)
```
El enunciado va en la misma línea que el `#####`.
El desarrollo va en las líneas siguientes, sin bloque Cornell.

---

## 5. Notación hispanohablante

Las notas usan notación matemática en español. Nunca sustituir
por equivalentes en inglés:

| Notación en el archivo | Significado     | No reemplazar por |
|------------------------|-----------------|-------------------|
| `\text{sen}\,x`        | seno            | sin               |
| `\text{tg}\,x`         | tangente        | tan               |
| `\text{arc\,sen}\,x`   | arcoseno        | arcsin            |
| `\text{arc\,cos}\,x`   | arcocoseno      | arccos            |
| `\text{arc\,tg}\,x`    | arcotangente    | arctan            |
| `\text{senh}\,x`       | seno hiperbólico| sinh              |
| `\text{cosec}\,x`      | cosecante       | csc               |

---

## 6. Tablas — valor absoluto y norma

Dentro de tablas Markdown, el carácter `|` es el separador de columnas y no puede usarse dentro de expresiones matemáticas. Por eso:

- Valor absoluto → `$\vert x \vert$` (nunca `|x|` dentro de tablas)
- Norma vectorial → `$\Vert v \Vert$` (nunca `||v||` dentro de tablas)

Fuera de tablas, `|x|` y `||v||` son válidos si el contexto lo permite.

---

## 7. Bloques de visualización

Las notas pueden contener bloques de código para gráficas.
NotebookLM no renderiza estas visualizaciones, pero debe leer
el contenido matemático que contienen.

**Bloques Desmos:**
````
```desmos-graph
y = x^2
---
bounds: {left: -5, right: 5, bottom: -2, top: 10}
```
````
Leer las expresiones matemáticas (líneas antes del `---`).
Ignorar los parámetros de configuración (líneas después del `---`).

**Bloques TikZJax:**
````
```tikz
\begin{tikzpicture}
  \draw (0,0) -- (1,1);
\end{tikzpicture}
```
````
Leer el contenido matemático del entorno `tikzpicture`.
Ignorar comandos de formato visual (colores, grosores, posición de texto).

**Bloque comentado en Claves:**
Dentro de la columna de Claves puede aparecer:
````
%```desmos-graph
%```
````
Es un marcador técnico obligatorio para el render en Obsidian.
Ignorar completamente — no contiene contenido matemático.
