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
4. [Cornell Marginalia — Notas al margen en el editor](#4-cornell-marginalia--notas-al-margen-en-el-editor)
5. [Commander — Botones personalizados en el ribbon](#5-commander--botones-personalizados-en-el-ribbon)
6. [File Hider — Ocultar archivos del explorador](#6-file-hider--ocultar-archivos-del-explorador)
7. [Attachment Management — Renombrar y organizar imágenes pegadas](#7-attachment-management--renombrar-y-organizar-imágenes-pegadas)
8. [Python Scripter — Scripts Python como comandos](#8-python-scripter--scripts-python-como-comandos)

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

## 4. Cornell Marginalia — Notas al margen en el editor

**Plugin:** [latazadehomero/cornell-marginalia](https://github.com/latazadehomero/cornell-marginalia) — instalado vía BRAT

**Propósito:** Agrega notas al margen (marginalia) directamente en el editor, fuera del área de texto principal. Complementa a Cornell Notes: mientras Cornell Notes maneja el layout de dos columnas para el contenido de la nota, Marginalia permite anotar al margen — comentarios, aclaraciones, referencias — sin interrumpir el flujo del texto.

> **Estado:** plugin recién integrado al vault. Uso aún en exploración — esta sección se irá actualizando.

### Coexistencia con Cornell Notes — parche aplicado

Ambos plugins registraban el mismo bloque ` ```cornell `, lo que impedía activarlos simultáneamente (Obsidian desactivaba uno automáticamente al activar el otro).

**Parche aplicado** en `.obsidian/plugins/cornell-marginalia/main.js`, línea 14017:

```
// Antes:
this.registerMarkdownCodeBlockProcessor("cornell", ...)

// Después:
this.registerMarkdownCodeBlockProcessor("cornell-m", ...)
```

Cambio de una sola línea: el bloque de Marginalia pasó de `cornell` a `cornell-m`. Cornell Notes sigue usando `````cornell` (4 backticks) sin modificación. Los dos plugins ahora coexisten sin conflicto.

> **Nota de mantenimiento:** si Cornell Marginalia se actualiza vía BRAT, el `main.js` se sobreescribe y el parche se pierde. Volver a aplicar el cambio en la línea `registerMarkdownCodeBlockProcessor` después de cada actualización.

### Sintaxis

Marginalia tiene dos modos de uso:

**Modo inline** (método principal — funciona en cualquier parte del documento):

```
%%> Nota al margen derecha %%
%%< Nota al margen izquierda %%
```

**Modo bloque** (método secundario — para alineación precisa en Reading View, usa el nuevo nombre tras el parche):

````
```cornell-m
Texto principal de la sección.
%%> Aclaración al margen sobre este párrafo. %%
Más texto que continúa normalmente.
```
````

### Ejemplo de uso

En una nota planet o comet, dentro o fuera de un bloque Cornell Notes:

```
La transformada de Laplace se define como:

$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$

%%> Ver demostración en ETN806-T03. %%

La condición de convergencia requiere que $\text{Re}(s) > \sigma_0$.
```

La nota `%%> Ver demostración... %%` aparece al margen derecho sin ocupar espacio en el flujo del texto.

### Notas de configuración

- La posición del margen (izquierda/derecha por defecto) se configura en **Settings → Cornell Marginalia → Alignment**.
- El ancho del margen y el estilo visual son ajustables desde el mismo panel.
- Las marginalia son visibles en **Live Preview** y en **Reading View** — no en Source Mode.

---

## 5. Commander — Botones personalizados en el ribbon

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

## 6. Flexplorer — Explorador de archivos mejorado

**Plugin:** [kh4f/flexplorer](https://github.com/kh4f/flexplorer) — disponible en Community Plugins

**Propósito:** Mejora el explorador de archivos nativo de Obsidian. Permite ocultar archivos y carpetas del explorador, anclarlos (pin) al tope de la lista, reordenarlos manualmente con drag-and-drop, y configurar el orden de cada carpeta de forma independiente.

### Por qué reemplaza a File Hider

> **File Hider fue descartado.** No cumplía con el propósito principal — ocultar tipos de archivo del explorador — sin importar la configuración que se le hiciera. Por más pruebas que se le hicieran, el plugin sencillamente no hacía lo que prometía. Ningún cambio en los patrones ni en las opciones tuvo efecto. Flexplorer sí lo hace, y además ofrece funcionalidades adicionales útiles para el vault.

### Funcionalidades usadas en el vault

| Función | Descripción |
|---|---|
| **Ocultar archivos** | Clic derecho sobre cualquier archivo o carpeta → *Hide* — desaparece del explorador sin eliminarse del disco |
| **Pin** | Clic derecho → *Pin* — ancla el archivo al tope de su carpeta, útil para notas de referencia frecuente |
| **Orden por carpeta** | Cada carpeta puede tener su propio modo de orden independientemente del resto |
| **Reorden manual** | Drag-and-drop para organizar archivos dentro de una carpeta en el orden que se quiera |

### Cómo ocultar un archivo o carpeta

1. Clic derecho sobre el archivo o carpeta en el explorador
2. Seleccionar **Hide**
3. El elemento desaparece del explorador — sigue existiendo en disco
4. Para volver a mostrarlo: **Settings → Flexplorer** → lista de elementos ocultos → quitar de la lista

---

## 7. Attachment Management — Renombrar y organizar imágenes pegadas

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

## 8. Python Scripter — Scripts Python como comandos

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
| 1 | `\dfrac` sin `d` | `\dfrac` |
| 2 | Bloque desmos sin etiqueta (` ``` ` + `left=`) | Agrega `desmos-graph` |
| 3 | Arrays LaTeX en una sola línea (` \ ` como separador) | `\\` + salto de línea |

**El script recibe:** `sys.argv[1]` = file path relativo · `sys.argv[2]` = vault path absoluto.

**Ejecución:** botón en el ribbon (configurado en Commander) → Notice con resultado.

---

### Guía de configuración por script

Cada script tiene su propia configuración en Settings → Python Scripter → [nombre del script].

| Campo | Descripción | Notas |
|---|---|---|
| **Run Directory** | Carpeta relativa al vault desde donde se ejecuta el script | Dejar vacío = raíz del vault |
| **Interpreter** | Ruta al ejecutable de Python | Usar ruta completa: `C:\...\python.exe` |
| **Include Current File Path** | Pasa la ruta relativa del archivo activo como argumento | Llega en `sys.argv[1]` |
| **Include Vault Path** | Pasa la ruta absoluta del vault como argumento | Llega en `sys.argv[2]` |
| **Include Clipboard Contents** | Pasa el contenido del portapapeles como argumento | Llega en `sys.argv[3]` |
| **Include Highlighted Contents** | Pasa el texto seleccionado en la nota como argumento | Llega en `sys.argv[4]` |
| **Predefined Arguments** | Argumentos fijos adicionales definidos de antemano | Se agregan después de los anteriores |
| **Number of Arguments to Prompt For** | Cantidad de argumentos que el plugin pide al usuario antes de ejecutar | Abre un modal por cada uno |
| **Run Type** | `Ribbon Icon` = botón en el ribbon · `Command` = solo Command Palette | |
| **Output Type** | `Notice` = notificación flotante · `Insert into File` = inserta en la nota activa | Usar `Notice` para scripts de corrección |
| **Output Location** | Solo aplica si Output Type es `Insert into File` | `End of File` o `Cursor Location` |

> **Orden fijo de argumentos:** el plugin siempre pasa los argumentos en este orden:
> `sys.argv[0]` ruta del script · `sys.argv[1]` file path · `sys.argv[2]` vault path · `sys.argv[3]` clipboard · `sys.argv[4]` highlighted
>
> Si algún toggle está OFF ese argumento no se pasa — los índices se desplazan. Activar siempre los mismos toggles para mantener el orden predecible.

---

### Guía para escribir scripts

#### Estructura base

Todo script debe comenzar con esta estructura. Ajustar según los toggles activados.

```python
import sys
import os

# --- Argumentos del plugin ---
file_path  = sys.argv[1]  # ruta relativa del archivo activo
vault_path = sys.argv[2]  # ruta absoluta del vault
# sys.argv[3] → clipboard (si Include Clipboard Contents = ON)
# sys.argv[4] → highlighted (si Include Highlighted Contents = ON)

# --- Validar que hay archivo activo ---
if not file_path or file_path == 'void.md':
    print("No hay archivo activo.")
    sys.exit(0)

# --- Construir ruta absoluta ---
abs_path = os.path.join(vault_path, file_path)

if not os.path.exists(abs_path):
    print(f"Archivo no encontrado: {abs_path}")
    sys.exit(0)

# --- Leer el archivo ---
with open(abs_path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# --- operaciones sobre content ---

# --- Guardar si hubo cambios ---
if content != original:
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Correcciones realizadas.")
else:
    print("Sin cambios.")
```

> **`void.md`** es el fallback que pasa el plugin cuando no hay nota activa. Siempre validar contra este valor para evitar operar sobre un archivo inexistente.

#### Regex en Python — reglas de escape

El error más común al escribir regex para LaTeX en Python es el escape de `\`. Regla simple:

| Lo que querés buscar | En el string Python | En raw string `r""` |
|---|---|---|
| `\dfrac` | `"\\dfrac"` | `r"\dfrac"` |
| `\\` (doble backslash) | `"\\\\"` | `r"\\"` |
| `\ ` (backslash + espacio) | `"\\ "` | `r"\ "` |

> Usar siempre **raw strings** `r"..."` en `re.sub()` — evita confusión y errores de escape.

#### Cómo probar desde terminal

Antes de conectar el script a Obsidian, probarlo desde PowerShell:

```powershell
& "C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" `
  ".obsidian\scripts\python\notebooklm_fix\src\main.py" `
  "Semesters\Sem_01\MAT101\Partial_1\void.md" `
  "E:\University_vault_2026"
```

Si devuelve `Sin cambios.` o `Correcciones realizadas.` — el script funciona. Si lanza excepción — hay un error antes de conectarlo a Obsidian.




%%
galaxy-links
[[_galaxy-system]]
[[obsidian_guide]]
[[desmos_guide]]
[[tikzjax_guide-legacy]]
[[better-export-pdf]]
[[_ToDo-system]]
%%
