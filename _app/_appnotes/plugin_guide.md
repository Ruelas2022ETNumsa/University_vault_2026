---
title: "Plugin Guide — Plugins simples del vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[obsidian_guide]]"
  - "[[_ToDo-system]]"
tags: [beacon, obsidian, plugins, infraestructura]
date_created: 2026-06-01
date_updated: 2026-06-01
status: activo
---

# Plugin Guide — Plugins simples del vault

> Plugins que no requieren archivo propio pero sí documentación de configuración y uso.
> Para plugins con sistema completo ver: [[desmos_guide]], [[tikzjax_guide]], [[obsidian_guide]], [[_pdf-system]], [[_excalidraw-system]].

---

## Índice

1. [Completr — Autocompletado de palabras y LaTeX](#1-completr--autocompletado-de-palabras-y-latex)
2. [Advanced Tables — Edición de tablas](#2-advanced-tables--edición-de-tablas)
3. [Multi-Column Markdown — Columnas en notas](#3-multi-column-markdown--columnas-en-notas)

---

## 1. Completr — Autocompletado de palabras y LaTeX

**Propósito:** Sugiere palabras mientras escribís, basándose en listas de términos propias y en los comandos LaTeX de MathJax. Evita reescribir términos técnicos repetitivos.

### Configuración recomendada

En Settings → Completr activar:
- **Word List** → activado
- **Word list folder** → `_app/completr-words`
- **LaTeX** → activado (incluye todos los comandos MathJax)
- **Scan vault** → opcional, escanea el vault para sugerir palabras ya usadas

### Estructura de archivos

```
_app/completr-words/
├── MAT101.txt       ← términos de Cálculo 1
├── general.txt      ← términos del vault, galaxy, infraestructura
└── ETNXXX.txt       ← un archivo por materia nueva
```

**Formato del archivo `.txt`:** una palabra o frase por línea, sin formato adicional.

```
clausura
conmutatividad
asociatividad
distributividad
axioma de cuerpo
número real
desigualdad
valor absoluto
```

### Reglas

- Un archivo `.txt` por materia — facilita agregar y archivar por semestre.
- El archivo `general.txt` contiene términos del sistema galaxy (`galaxy_body`, `orbiting`, `beacon`, etc.) y términos transversales a todas las materias.
- Para agregar palabras nuevas: editar el `.txt` correspondiente → `Ctrl+P` → **"Completr: Reload word lists"** — no hace falta reiniciar Obsidian.

### Flujo de uso

1. Escribís las primeras letras de un término → aparece sugerencia
2. `Tab` para aceptar, `Esc` para ignorar
3. Para LaTeX: escribís `\` y el inicio del comando → Completr filtra los comandos MathJax disponibles

---

## 2. Advanced Tables — Edición de tablas

**Propósito:** Facilita la creación y edición de tablas Markdown. Agrega navegación con `Tab` entre celdas, alineación automática de columnas y un toolbar opcional.

### Uso básico

| Acción | Cómo |
|--------|------|
| Avanzar a la siguiente celda | `Tab` |
| Retroceder a la celda anterior | `Shift+Tab` |
| Nueva fila | `Tab` en la última celda |
| Alinear la tabla | automático al tabular |

### Notas de uso en el vault

- La tabla se formatea automáticamente al usar `Tab` — no hace falta alinear los `|` a mano.
- Funciona sobre cualquier tabla Markdown existente: posicionarse en una celda y tabular activa el modo tabla.
- El toolbar aparece sobre la tabla en modo edición — permite insertar/eliminar filas y columnas sin escribir nada.
- Las tablas con LaTeX (`$...$`) en las celdas funcionan normalmente — Advanced Tables no interfiere con el renderizado de MathJax.

---

## 3. Multi-Column Markdown — Columnas en notas

**Propósito:** Permite dividir el cuerpo de una nota en columnas visibles en modo lectura y edición (Live Preview). Usado en el vault para el layout Cornell en notas `planet` y `comet`.

### Sintaxis actual (0.9.x)

```
--- start-multi-column: ID-unico
` ``column-settings
number of columns: 2
column size: [60%, 40%]
border: off
` ``

Contenido columna izquierda

--- end-column ---

Contenido columna derecha

--- end-multi-column
```

> El ID debe ser único dentro del mismo archivo. Si hay dos bloques en la misma nota usar `cornell-001`, `cornell-002`, etc.

### Layout Cornell para `planet` (teoría)

```
--- start-multi-column: cornell-001
` ``column-settings
number of columns: 2
column size: [60%, 40%]
border: off
` ``

## 📝 Desarrollo

Contenido principal del subtítulo —
definiciones, fórmulas, desarrollo.

--- end-column ---

## 🔑 Claves

- Concepto central
- Condición importante
- Palabra clave: **X**

--- end-multi-column

> **Resumen:** Idea central del subtítulo en una línea.
```

### Layout Cornell para `comet` (ejercicio)

```
--- start-multi-column: cornell-001
` ``column-settings
number of columns: 2
column size: [60%, 40%]
border: off
` ``

## 📋 Desarrollo

Paso a paso del ejercicio.

--- end-column ---

## ⚠️ Notas de método

- Justificación del paso clave
- Error común a evitar

--- end-multi-column

> **Patrón:** Tipo de ejercicio y estrategia de resolución.
```

### Reglas

- `border: off` siempre — el vault no usa bordes en columnas.
- El resumen `>` va **fuera** del bloque, después de `--- end-multi-column`.
- En modo edición (Live Preview) las columnas se renderizan correctamente. En modo lectura también.
- Si el bloque no renderiza: `Ctrl+P` → **"Fix Multi-Column Syntax in Current File"**.

%%
galaxy-links
[[_galaxy-system]]
[[obsidian_guide]]
[[desmos_guide]]
[[tikzjax_guide]]
[[_ToDo-system]]
%%
