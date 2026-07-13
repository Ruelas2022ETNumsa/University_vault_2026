---
title: Shell Commands — Guía de Scripting
galaxy_body: beacon
scope: vault
author:
  - usuario
  - claude
audience:
  - usuario
  - claude
related_notes:
  - "[[shellcmd_config_gral]]"
  - "[[shellcmd_config_script]]"
  - "[[shellcommands_guide(scripts)]]"
tags:
  - beacon
  - obsidian
  - shell-commands
  - infraestructura
  - automatizacion
date_created: 2026-07-12
date_updated: 2026-07-12
status: borrador
---

# Shell Commands — Guía de Scripting

> Hoja de referencia rápida para construir scripts. No duplica las transcripciones — las complementa.
> Para opciones detalladas del plugin: [[shellcmd_config_gral]] y [[shellcmd_config_script]].

---

## 1. Estructura mental de un script

Todo script tiene 4 decisiones:

| # | Decisión | Pregunta clave |
|---|---|---|
| 1 | **Trigger** | ¿Cómo se dispara? Manual, hotkey, evento automático |
| 2 | **Variables** | ¿Qué datos del vault necesito? Archivo activo, selección, fecha, input del usuario |
| 3 | **Comando** | ¿Qué ejecuto? PowerShell, Python, batch, etc. |
| 4 | **Output** | ¿Dónde va el resultado? Nota, portapapeles, notificación, ignorar |

---

## 2. Triggers disponibles

### Manual
- Paleta de comandos (`Ctrl+P`)
- Hotkey asignada en Obsidian
- Botón en ribbon (via plugin Commander)
- URI de Obsidian

### Automático (Eventos)
| Evento | Cuándo se dispara | Variables extra disponibles |
|---|---|---|
| Obsidian inicia | Al abrir Obsidian | ninguna |
| Obsidian cierra | Al cerrar Obsidian | ninguna |
| Archivo creado | Al crear cualquier archivo | `{{event_file_path}}`, `{{event_file_name}}`, `{{event_title}}` |
| Archivo modificado | Al cambiar contenido | `{{event_file_path}}`, `{{event_file_content}}` |
| Archivo eliminado | Al borrar un archivo | `{{event_file_path}}`, `{{event_file_name}}` |
| Archivo movido | Al mover un archivo | `{{event_file_path}}`, `{{event_old_file_path}}`, `{{event_old_folder_path}}` |
| Archivo renombrado | Al renombrar | `{{event_file_name}}`, `{{event_old_file_name}}`, `{{event_old_title}}` |
| Carpeta creada/eliminada/movida/renombrada | Eventos de carpeta | `{{event_folder_path}}`, `{{event_folder_name}}` |
| Menú de archivo 🚫 | Clic derecho sobre un archivo | `{{event_file_path}}`, `{{event_file_name}}` |
| Menú de carpeta 🚫 | Clic derecho sobre una carpeta | `{{event_folder_path}}`, `{{event_folder_name}}` |
| Cada N segundos | Periódico | ninguna |
| Panel activo cambia | Al cambiar de nota | ninguna |
| Cursor se mueve | Al mover el cursor en editor | `{{caret_position}}` |

> 🚫 = no soporta debouncing

---

## 3. Variables — tabla de referencia rápida

### Archivo activo
| Variable | Qué devuelve | Disponibilidad |
|---|---|---|
| `{{title}}` | Nombre del archivo sin extensión | Solo si hay archivo activo |
| `{{file_name}}` | Nombre del archivo con extensión | Solo si hay archivo activo |
| `{{file_path:relative}}` | Ruta relativa desde la raíz del vault | Solo si hay archivo activo |
| `{{file_path:absolute}}` | Ruta absoluta desde el sistema de archivos | Solo si hay archivo activo |
| `{{file_extension:with-dot}}` | Extensión con punto (ej. `.md`) | Solo si hay archivo activo |
| `{{file_extension:no-dot}}` | Extensión sin punto (ej. `md`) | Solo si hay archivo activo |
| `{{file_uri}}` | URI de Obsidian que abre el archivo | Solo si hay archivo activo |
| `{{file_content}}` | Contenido completo incluyendo YAML | Solo si hay archivo activo |
| `{{note_content}}` | Contenido sin YAML | Solo si hay archivo activo |
| `{{folder_name}}` | Nombre de la carpeta contenedora | Solo si hay archivo activo |
| `{{folder_path:relative}}` | Ruta relativa de la carpeta contenedora | Solo si hay archivo activo |
| `{{folder_path:absolute}}` | Ruta absoluta de la carpeta contenedora | Solo si hay archivo activo |
| `{{tags}}` | Etiquetas de la nota (definir separador) | Solo si hay archivo activo |
| `{{selection}}` | Texto seleccionado actualmente | Solo en modo edición con texto seleccionado |
| `{{caret_paragraph}}` | Línea donde está el cursor | Solo en modo edición |
| `{{caret_position}}` | Línea:columna del cursor | Solo en modo edición |

### YAML / Frontmatter
| Variable | Qué devuelve | Disponibilidad |
|---|---|---|
| `{{yaml_content:with-dashes}}` | Frontmatter completo con `---` | Solo si hay YAML en el archivo |
| `{{yaml_content:no-dashes}}` | Frontmatter sin `---` | Solo si hay YAML en el archivo |
| `{{yaml_value:propiedad}}` | Valor único de una propiedad YAML | Solo si la propiedad existe |
| `{{yaml_values:propiedad:separador}}` | Lista de valores de una propiedad YAML | Solo si la propiedad existe |

### Siempre disponibles
| Variable | Qué devuelve |
|---|---|
| `{{vault_path}}` | Ruta absoluta del vault |
| `{{clipboard}}` | Contenido del portapapeles |
| `{{date:formato}}` | Fecha/hora con formato custom ([momentjs](https://momentjs.com/docs/#/displaying/format/)) |
| `{{new_note_folder_name}}` | Nombre de la carpeta para nuevas notas (config Obsidian) |
| `{{new_note_folder_path:relative}}` | Ruta relativa de la carpeta para nuevas notas |
| `{{new_note_folder_path:absolute}}` | Ruta absoluta de la carpeta para nuevas notas |
| `{{workspace}}` | Nombre del workspace activo (requiere plugin Workspaces) |
| `{{obsidian_api_version}}` | Versión de la API de Obsidian |
| `{{shell_commands_plugin_version:plugin}}` | Versión del plugin Shell Commands |
| `{{environment:NOMBRE}}` | Valor de una variable de entorno del sistema |

### Variables de eventos (solo disponibles cuando el trigger es un evento)
| Variable | Qué devuelve |
|---|---|
| `{{event_file_name}}` | Nombre del archivo del evento (con extensión) |
| `{{event_title}}` | Nombre del archivo del evento (sin extensión) |
| `{{event_file_path:relative}}` | Ruta relativa del archivo del evento |
| `{{event_file_path:absolute}}` | Ruta absoluta del archivo del evento |
| `{{event_file_content}}` | Contenido completo del archivo del evento |
| `{{event_note_content}}` | Contenido sin YAML del archivo del evento |
| `{{event_file_extension:with-dot}}` | Extensión con punto del archivo del evento |
| `{{event_folder_name}}` | Carpeta contenedora del archivo/carpeta del evento |
| `{{event_folder_path:relative}}` | Ruta relativa de la carpeta del evento |
| `{{event_folder_path:absolute}}` | Ruta absoluta de la carpeta del evento |
| `{{event_old_file_name}}` | Nombre anterior (renombrado) |
| `{{event_old_title}}` | Nombre anterior sin extensión (renombrado) |
| `{{event_old_file_path:relative}}` | Ruta anterior del archivo (movido/renombrado) |
| `{{event_old_folder_name}}` | Carpeta anterior (movido/renombrado) |
| `{{event_old_folder_path:relative}}` | Ruta anterior de la carpeta (movido/renombrado) |
| `{{event_tags}}` | Etiquetas del archivo del evento |
| `{{event_type}}` | Nombre del evento disparado |
| `{{event_yaml_value:propiedad}}` | Valor YAML del archivo del evento |

### Variables personalizadas (Custom variables)
Se crean en `Pestaña: Variables → Custom variables`. Se acceden como `{{_nombre}}`.
Útiles para recibir input del usuario via Prompts o para pasar valores entre scripts.

---

## 4. Output — dónde va el resultado

| Canal | Comportamiento |
|---|---|
| `Ignore` | Descarta la salida |
| `Notification balloon` | Muestra notificación flotante |
| `Status bar` | Muestra en la barra inferior de Obsidian |
| `Clipboard` | Copia al portapapeles |
| `Current file: Caret position` | Inserta en la posición del cursor |
| `Current file: Top` | Inserta al inicio del archivo activo |
| `Current file: Bottom` | Inserta al final del archivo activo |
| `Open files` | Abre o crea un archivo con la salida |
| `Assign custom variables` | Guarda la salida en una variable personalizada |
| `Ask execution` | Pregunta al usuario qué hacer con la salida |

> stdout y stderr se configuran por separado. Si usan el mismo canal se combinan.

---

## 5. Patrones comunes

### Script Python con argumentos del vault
```
"C:\ruta\python.exe" "{{vault_path}}\.obsidian\scripts\python\mi_script\main.py" "{{file_path:relative}}" "{{vault_path}}"
```

### Git commit automático al modificar un archivo
```powershell
cd "{{vault_path}}" && git add "{{event_file_path:relative}}" && git commit -m "update: {{event_title}}"
```
*Trigger: Archivo modificado*

### Backup de la nota activa con fecha
```powershell
Copy-Item "{{file_path:absolute}}" "{{file_path:absolute}}.{{date:YYYY-MM-DD}}.bak"
```

### Pasar contenido largo via stdin (evita límite de línea de comandos)
Usar el campo **stdin** en Pestaña General con `{{note_content}}` y en el comando recibir desde stdin:
```python
import sys
content = sys.stdin.read()
```

### Encadenar comandos en Windows (PowerShell)
```powershell
comando1 ; comando2 ; comando3
```
Con condición de éxito:
```powershell
comando1 -and comando2
```

---

## 6. Escape de caracteres especiales

- Por defecto el plugin **escapa automáticamente** los caracteres especiales en los valores de variables.
- Para usar el valor **sin escapar** (peligroso): `{{!nombre_variable}}`
- **CMD.exe** no soporta escape de variables — usar PowerShell siempre que sea posible.

---

## 7. Checklist para crear un script nuevo

- [ ] Definir el trigger (manual / evento)
- [ ] Identificar qué variables necesito y verificar su disponibilidad según el trigger
- [ ] Si necesito input del usuario → configurar un Prompt en Preactions con Custom variables
- [ ] Si el comando es largo → usar stdin para pasar contenido
- [ ] Configurar stdout y stderr en Output
- [ ] Probar con `Ctrl+clic` en el botón de ejecución para ver el output antes de automatizar
- [ ] Asignar alias descriptivo en Pestaña General
