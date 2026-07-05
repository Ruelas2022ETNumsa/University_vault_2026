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
date_updated: 2026-07-04
status: activo
---

# Plugin Guide — Plugins simples del vault

> Plugins que no requieren archivo propio pero sí documentación de configuración y uso.
> Para plugins con sistema completo ver: [[desmos_guide]], [[tikzjax_guide-legacy]], [[obsidian_guide]], [[_pdf-system]], [[_excalidraw-system]], [[better-export-pdf]].

---

## Índice

1. [Completr — Autocompletado de palabras y LaTeX](#1-completr--autocompletado-de-palabras-y-latex)
2. [Advanced Tables — Edición de tablas](#2-advanced-tables--edición-de-tablas)
3. [Cornell Notes — Layout Cornell en notas](#3-cornell-notes--layout-cornell-en-notas)
4. [Commander — Botones personalizados en el ribbon](#4-commander--botones-personalizados-en-el-ribbon)
5. [File Hider — Ocultar archivos del explorador](#5-file-hider--ocultar-archivos-del-explorador)
6. [Attachment Management — Renombrar y organizar imágenes pegadas](#6-attachment-management--renombrar-y-organizar-imágenes-pegadas)
7. [Python Scripter — Scripts Python como comandos](#7-python-scripter--scripts-python-como-comandos)

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

## 3. Cornell Notes — Layout Cornell en notas

**Plugin:** [bytetiles/obsidian-cornell-notes](https://github.com/bytetiles/obsidian-cornell-notes) — v1.0.2

**Propósito:** Renderiza el layout Cornell de dos columnas en notas `planet` y `comet`. Reemplaza a Multi-Column Markdown.

**Razón del cambio:** Multi-Column causaba carga lenta en modo lectura y tenía bugs de renderizado frecuentes. Cornell Notes es más liviano, sin bugs conocidos, y soporta nativamente bloques Desmos y TikZJax dentro del layout.

### Sintaxis

La sintaxis es idéntica a la ya usada en todo el vault — sin migración de notas existentes.

````cornell
::cue

Contenido de la columna izquierda — claves, preguntas, mnemónicos.

::note

Contenido de la columna derecha — desarrollo, definiciones, fórmulas.

````

> 4 backticks para el fence exterior. Si hay bloques de código adentro, usar 3 backticks internos normalmente.

### Títulos de columnas

Configurables desde **Settings → Cornell Notes**. En el vault están configurados como:

- Columna izquierda: `🔑 Claves`
- Columna derecha: `📝 Desarrollo`

No se declaran dentro del bloque de código — se aplican globalmente desde la configuración.

### Modos de renderizado

Funciona correctamente en los tres modos (probado):

| Modo | Resultado |
|---|---|
| Lectura | ✓ Dos columnas |
| Escritura (Live Preview) | ✓ Dos columnas |
| Escritura con vista previa | ✓ Dos columnas |

### Soporte de bloques dentro del layout

A diferencia de Multi-Column, este plugin soporta nativamente:
- Bloques `desmos-graph`
- Bloques `tikz`
- Callouts (`> [!note]`, `> [!summary]`)
- LaTeX (`$...$`)
- Wikilinks y todo Markdown estándar

---

## 4. Commander — Botones personalizados en el ribbon

**Propósito:** Agrega comandos de Obsidian como botones en el ribbon (barra lateral izquierda), el menú de archivo, o el menú contextual. Evita abrir el Command Palette para acciones frecuentes.

### Botones configurados en el vault

| Botón | Comando | Uso |
|-------|---------|-----|
| Crear nota desde plantilla | `Templater: Create new note from template` | Abre el selector de plantillas galaxy para crear cualquier tipo de nota |
| Recargar Obsidian | `Reload app without saving` | Fuerza el re-render de bloques TikZJax que no renderizan en el primer arranque |

### Cómo agregar un botón nuevo

1. Settings → Commander → sección **Ribbon**
2. Clic en **+** → buscar el comando por nombre
3. Elegir ícono y nombre visible → confirmar
4. El botón aparece en el ribbon inmediatamente

### Nota sobre "Reload app without saving"

Este botón existe exclusivamente como workaround para el bug de TikZJax: los bloques `tikz` a veces no renderizan al primer arranque del vault. Recargar Obsidian sin guardar fuerza el re-render sin perder cambios no guardados (Obsidian guarda automáticamente). Ver [[tikzjax_guide-legacy]] sección U7.

---

## 5. File Hider — Ocultar archivos del explorador

**Propósito:** Oculta archivos y extensiones del explorador de Obsidian sin eliminarlos del disco. Mantiene el explorador limpio mostrando solo archivos relevantes para el trabajo en el vault.

### Archivos ocultos en el vault

| Patrón | Tipo | Razón |
|--------|------|-------|
| `*.tmp` | Extensión | Archivos temporales generados por plugins |
| `*.bat` | Extensión | Scripts de sistema — no son notas del vault |
| `*.ps1` | Extensión | Scripts PowerShell — no son notas del vault |

### Cómo agregar un patrón

Settings → File Hider → agregar el patrón (nombre exacto, extensión con `*`, o carpeta).

### Bug conocido

File Hider no aplica los patrones de ocultamiento al arrancar Obsidian — los archivos ocultos vuelven a ser visibles hasta que se abre la configuración del plugin y se reinicia la app. No hay workaround conocido por el momento; es un bug del plugin.

---

## 6. Attachment Management — Renombrar y organizar imágenes pegadas

**Propósito:** Renombra automáticamente cualquier imagen pegada o arrastrada a una nota, heredando el nombre de la nota host y guardándola en `_assets/`. Elimina los nombres genéricos tipo `Pasted image 20260602.png` y mantiene la convención Galaxy sin intervención manual.

### Por qué existe en el vault

Cuando pegás una imagen en una nota `comet` o `planet`, Obsidian la guarda con un nombre genérico en la carpeta por defecto. Eso rompe dos reglas del sistema Galaxy: el nombre no sigue el patrón `ETNXXX-TNN-nombre-descriptivo` y el archivo no va a `_assets/`. Este plugin corrige ambas cosas automáticamente al momento de pegar.

### Configuración aplicada

| Campo | Valor | Por qué |
|---|---|---|
| Root path | *(vacío)* | Raíz del vault — dejar vacío para que `_assets` se resuelva desde la raíz |
| Attachment path | `_assets` | Carpeta destino única para todas las imágenes del vault |
| Attachment format | `${notename}-${date}` | Hereda el nombre Galaxy de la nota host + timestamp para evitar colisiones |
| Date format | `YYYYMMDDHHmmss` | Fecha + hora hasta segundos — suficiente para unicidad, sin milisegundos innecesarios |
| Automatically rename | `ON` | Renombrado automático al pegar — sin intervención manual |
| Extension override | *(vacío)* | No se fuerza ninguna extensión — se conserva la original |
| Exclude extension | `pdf\|docx?\|xlsx?\|zip\|rar` | PDFs y documentos los maneja PDF++ con su propio sistema en `_pdf/` |
| Exclude paths | `_app;_pdf;_templates;borrar` | Protege toda la infraestructura del vault de renombrados accidentales |
| Exclude subpaths | `ON` | La exclusión aplica también a todas las subcarpetas de las rutas listadas |

> **Nota sobre Root path vacío:** dejar el campo vacío (no elegir ninguna de las tres opciones del dropdown) es lo que hace que `_assets` en Attachment path se resuelva correctamente desde la raíz del vault. Si se elige `In folder specified below` y se escribe `_assets` en ese campo, el plugin crea una carpeta anidada `_assets/_assets/`.

### Resultado en el vault

Al pegar una imagen en `ETN806-T01-joint-pdf-definition.md`:

```
Antes:   Pasted image 20260602143000.png  →  carpeta aleatoria
Después: ETN806-T01-joint-pdf-definition-20260602143000.png  →  _assets/
```

### Lo que el plugin NO hace

El plugin solo renombra y reubica el archivo de imagen. El tipo `photon` del sistema Galaxy requiere además:

1. Crear la nota `photon` con su YAML y el campo `attached_to` apuntando a la nota host.
2. Agregar el wikilink en el bloque `%%` de la nota host.

Esos dos pasos siguen siendo manuales o via plantilla `tpl-photon.md`. Ver [[_galaxy-system]] sección `photon`.

### Flujo de trabajo completo con el plugin

```
1. Abrís la nota host (ej. ETN806-T01-joint-pdf-definition.md)
        ↓
2. Pegás la imagen (Ctrl+V) o la arrastrás al editor
        ↓
3. Attachment Management la renombra y mueve a _assets/ automáticamente
   → ETN806-T01-joint-pdf-definition-20260602143000.png
        ↓
4. (Manual) Creás la nota photon con tpl-photon.md
   → YAML con attached_to: "[[ETN806-T01-joint-pdf-definition]]"
        ↓
5. (Manual) Agregás el wikilink en el bloque %% de la nota host
```

---

## 7. Python Scripter — Scripts Python como comandos

**Plugin:** `nickrallison/obsidian-python-scripter` (instalado vía BRAT)

**Propósito:** Registra scripts Python como comandos de Obsidian ejecutables desde el ribbon o el Command Palette. Permite automatizar correcciones y tareas sobre las notas del vault sin salir de Obsidian.

### Configuración aplicada

| Campo | Valor |
|---|---|
| Interpreter | `C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe` |
| Include Current File Path | ON |
| Include Vault Path | ON |
| Output Type | Notice |

### Estructura de scripts

Cada script vive en su propia carpeta bajo `.obsidian/scripts/python/`. El plugin detecta cualquier carpeta con `src/main.py` y la registra como comando.

```
.obsidian/scripts/python/
└── notebooklm_fix/
    └── src/
        └── main.py
```

### Script: notebooklm_fix

Corrige errores frecuentes que NotebookLM comete al generar notas `.md`. Opera sobre el archivo activo al momento de ejecutarse.

**Correcciones que aplica:**

| # | Error | Correción |
|---|---|---|
| 1 | `\frac` sin `d` | `\dfrac` |
| 2 | Bloque desmos sin etiqueta (` ``` ` + `left=`) | Agrega `desmos-graph` |
| 3 | Arrays LaTeX en una sola línea (` \ ` como separador) | `\\` + salto de línea |

**El script recibe:** `sys.argv[1]` = file path relativo · `sys.argv[2]` = vault path absoluto.

**Ejecución:** botón en el ribbon (configurado en Commander) → Notice con resultado.




%%
galaxy-links
[[_galaxy-system]]
[[obsidian_guide]]
[[desmos_guide]]
[[tikzjax_guide-legacy]]
[[better-export-pdf]]
[[_ToDo-system]]
%%
