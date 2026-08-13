---
title: "Shell Commands — notebooklm_fix"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_scripting_guide]]"
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
tags: [beacon, obsidian, shell-commands, notebooklm, infraestructura, automatizacion]
date_created: 2026-08-13
date_updated: 2026-08-13
status: activo
---

# Shell Commands — notebooklm_fix

> Script de corrección automática sobre archivos `.md` generados desde NotebookLM.
> Normaliza bloques Cornell, notación matemática y bloques de código antes de usar el archivo en Obsidian.

---

## 1. Propósito

NotebookLM entrega el output con varios problemas de formato que impiden el renderizado correcto en Obsidian. Este script los corrige en un solo paso directamente sobre el archivo `.md` activo.

---

## 2. Archivo del script

```
.obsidian/scripts/python/notebooklm_fix/src/main.py
```

---

## 3. Correcciones que aplica

### 3.1 Bloques Cornell mal formados

NotebookLM a veces separa el identificador `cornell` del bloque de backticks con un salto de línea. Obsidian no lo reconoce así.

**Antes:**
```
`````
cornell
::cue
...
```

**Después:**
```
`````cornell
::cue
...
```

También corrige bloques con 3 o 4 backticks en lugar de 5, y cierres con menos de 5 backticks.

---

### 3.2 `\frac` → `\dfrac`

Reemplaza todas las ocurrencias de `\frac` por `\dfrac` para forzar el tamaño de fracción display, más legible en apuntes.

**Antes:**
```
\(\dfrac{d}{dx} f(x)\)  →  se ve pequeño inline
\frac{1}{2}
```

**Después:**
```
\dfrac{1}{2}
```

> No afecta `\dfrac` ni `\tfrac` ya existentes.

---

### 3.3 Bloques desmos sin etiqueta

Si NotebookLM genera un bloque de código con contenido desmos pero sin la etiqueta del lenguaje, el script la agrega.

**Antes:**
````
```
left=...
```
````

**Después:**
````
```desmos-graph
left=...
```
````

---

### 3.4 Arrays en una línea

Cuando un array `$$\begin{array}...\end{array}$$` llega todo en una línea con ` \ ` como separador de filas, el script lo expande correctamente con saltos de línea reales.

**Antes:**
```
$$\begin{array}{rcl} a & = & b \ c & = & d \end{array}$$
```

**Después:**
```
$$\begin{array}{rcl}
a & = & b \\
c & = & d
\end{array}$$
```

---

### 3.5 Bloques marginalia en Cornell

Inserta automáticamente los bloques `marginalia` dentro de cada bloque Cornell si aún no los tiene. Es idempotente — no duplica si ya están presentes.

**Antes:**
```
`````cornell
::cue
palabras clave

::note
contenido
`````
```

**Después:**
```
`````cornell
::cue
````marginalia %%> %%
palabras clave

````
::note
````marginalia %%< %%
contenido
`````
```

---

## 4. Qué no toca

- No modifica bloques de código inline ni triple backtick con contenido propio
- No toca el YAML frontmatter
- No modifica archivos sin cambios (idempotente — si corre dos veces, el resultado es el mismo)
