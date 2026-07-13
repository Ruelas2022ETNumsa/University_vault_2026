---
title: Shell Commands — Configuración por Script
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

# Configuración Shell Commands (individual por script)

> [!info] Referencia
> Este archivo documenta solo la configuración individual por script. Para opciones globales del plugin (environments, output global, variables built-in, etc.) ver: [[shellcmd_config_gral]]

## Leyenda de Componentes
* `\[input text\]` o `\[input text (ejemplo)\]`: Caja de texto para escribir.
* `\[opción1/opción2\]`: Menú de elección de opciones.
* `>Texto<`: Botón de acción.
* `(1/0)`: Elección entre encendido y apagado (Toggle).

---

## Pestañas Principales

* [x] Shell commands
* [ ] Environments
* [ ] Preactions
* [ ] Output
* [ ] Events
* [ ] Variables

> [!info] Todo lo documentado en este archivo corresponde a la configuración individual accesible dentro de la pestaña Shell commands.

> **Tip:** Presiona `Ctrl + arriba/abajo` para navegar entre comandos de shell. Acción rápida: `>_ <` ejecuta inmediatamente; `Ctrl+clic` ejecuta y pregunta qué hacer con la salida. *Aplica en todas las pestañas de configuración.*

---

### Comando de shell creado (Shell command)
Muestra la estructura de un comando de shell creado en la lista. A la derecha de su alias o nombre cuenta con botones de acción rápida para configurar y ejecutar la tarea dentro de Obsidian utilizando el plugin Shell commands.

- Alias / Nombre del comando: \[Mi Script de Sincronización\]

### Botones de acción rápida
- _ < Ejecutar ahora: `Clic` normal: ejecuta inmediatamente. `Ctrl+clic`: ejecuta y pregunta qué hacer con la salida (output).
- ⚙️ Configuración general: Configura el alias, ícono, configuraciones generales y la entrada estándar (stdin).
- 📄 Preacciones (Preactions): Solicita valores o confirmaciones al usuario antes de proceder con la ejecución.
- ≡ Manejo de salida: Configura el comportamiento de la salida estándar (stdout), salida de errores (stderr) e ignorar errores.
- 🗀 Selección de Shell: Permite elegir la shell y configurar comandos específicos para diferentes sistemas operativos.
- ⚄ Eventos (Events): Configura disparadores o eventos automáticos para el comando.
- \</\> Variables: Define los valores por defecto para las variables utilizadas en el script.
- 🗑️ Eliminar: Borra permanentemente este comando de shell.

### Configuración del comando
- Comando principal: \[enter your command\]
- Preview / Ejecutable: \[copia del comando principal\]
- Shell / Terminal: \[cmd.exe\]

### Acciones adicionales
- 🔗 Copiar URI de Obsidian: Copia la URI de Obsidian de este comando al portapapeles; al visitar dicha URI se ejecutará el comando. `Ctrl+clic`: copia como un enlace en formato Markdown.
- $\bigoplus$ Configurar Hotkey: Redirige directamente a los ajustes de teclas de acceso rápido (hotkeys) de Obsidian para asignarle un atajo al comando.

---

## Pestaña: Configuración del comando / General
### Alias / Alias
Si no está vacío, el alias se mostrará en la paleta de comandos en lugar del comando real. Un alias nunca se ejecuta como un comando. Puedes usar variables estilo `{{}}`. Comenzar una variable con `{{!` evitará el escape de caracteres especiales.

- Campo: \[input text\]

### Ícono / Icon
Si se define, el ícono se mostrará en el menú de archivos, carpetas y del editor delante del texto del alias. Ayuda a distinguir visualmente los comandos.

- Opción: \[No icon / Lista de íconos disponibles\]

### Pedir confirmación antes de la ejecución / Ask confirmation before execution
- Control: (1/0)

### Pasar variables a la entrada estándar (stdin) (experimental) / Pass variables to standard input (stdin) (experimental)
Se usa para pasar textos largos como entrada al comando de shell si exceden el límite de longitud de la línea de comandos (ej. `{{note_content}}`). También sirve para programas interactivos que piden múltiples valores (poner en líneas separadas). Puede contener `{{variables}}` o texto estático.

- Campo: \[input text\]
- Acción: >❓< (Ir a la documentación)

### Identificadores y Atajos / IDs & Shortcuts
- **Shell command id:** `xxxpwtaxxx` 
  - Acciones: >🗐< (Copiar valor)
- **Obsidian command palette id:** `obsidian-shellcommands:shell-command-xxxpwtaxxx`
  - Acciones: >🗐< (Copiar valor)

---

## Pestaña: Configuración del comando / Preactions
Las preacciones se realizan antes de que se ejecute el comando de shell real, con el fin de hacer ciertos preparativos.

### Mensaje emergente / Prompt
Se utilizan para solicitar valores al usuario justo antes de la ejecución del comando. Se accede a los valores mediante variables personalizadas. Puedes administrarlos en la pestaña 'Preactions' de la configuración principal del plugin.

- Opción: \[No prompt / Create new prompt\]

---

### Ventana Emergente: Crear nuevo mensaje / Create prompt
#### Título del prompt / Prompt title
- Campo: \[input text\]
- Acción rápida: >>_ < (Ejecutar ahora)

#### Descripción / Description
Se muestra entre el título del prompt y los campos. Admite el uso de `{{variables}}`.

- Campo: \[input text\]

#### Vista previa del comando de shell en el prompt / Preview shell command in prompt
Si está activo, el prompt mostrará el comando de shell ejecutable con los nombres de las variables y resaltará las variables afectadas por los valores ingresados.

- Control: (1/0)

#### Campos / Fields
Permite añadir campos al formulario. Se pueden usar `{{variables}}` en las etiquetas, valores por defecto, descripciones, etc.

- Acción: >New prompt field<

#### Texto del botón de ejecución / Execute button text
- Campo: \[input text\] (by default : Execute)

- Acción final: >Create prompt<

> **Tip:** Puedes personalizar el estilo visual del modal del prompt con CSS usando la clase `.SC-prompt-modal-fyquadt617` o `.SC-prompt-modal` (para todos los modals).

---

## Pestaña: Configuración del comando / Output
### Canal de salida para stdout / Output channel for stdout
- Opción: \[Ignore/Notification balloon/Current file:(Caret position/Top/Bottom)/Open files/Status bar/Clipboard/Assign custom variables/Ask execution\]

### Canal de salida para stderr / Output channel for stderr
Si tanto stdout como stderr usan el mismo canal, se combinarán en el mismo mensaje con stdout.

- Opción: \[Ignore/Notification balloon/Current file:(Caret position/Top/Bottom)/Status bar/Clipboard/Ask execution\]

### Envoltorio de salida para stdout / Output wrapper for stdout
Se usa para rodear la salida con texto predefinido (ej. poner la salida en un bloque de código).

- Opción: \[No stdout wrapper/Create a new output wrapper\]

### Envoltorio de salida para stderr / Output wrapper for stderr
- Opción: \[No stderr wrapper/Create a new output wrapper\]

### Detectar colores, estilos de fuente, etc. en la salida (Código ANSI) / Detect colors, font styles etc. in output (ANSI code)
Los programas de shell pueden generar código ANSI para aplicar colores y formato. Si está activado, las ocurrencias de ANSI se convierten a elementos HTML. De lo contrario, se muestra como texto plano.

- Controles: \[stdout: Enable/Disable\] \[stderr: Enable/Disable\]
- Acción: >❓<

### Modo de manejo de salida / Output handling mode
Establece en 'Realtime' si el comando tarda mucho y deseas que la salida se procese a medida que esté disponible. 'Wait until finished' pospone el manejo hasta recibir toda la salida.

- Opción: \[Wait until finished/Realtime (experimental)\]
- Acción: >❓<

### Orden de salida stdout/stderr / Order of stdout/stderr output
Cuando la salida contiene tanto errores como salida normal, define cuál debe presentarse primero (solo importa si el modo es 'Wait until finished').

- Opción: \[Stdout first, then stderr./Stderr first, then stdout.\]

### Ignorar códigos de error / Ignore error codes
Lista de números separados por comas. Si la ejecución falla con uno de estos códigos de salida, no se mostrará ningún mensaje de error y se ignorará el canal stderr.

- Campo: \[input text\]

### Mostrar una notificación al ejecutar / Show a notification when executing
- Opción: \[Default (Do not show)/Do not show/Show for 10 seconds/Show until process is finished/Show only if executing takes long\]

---

## Pestaña: Configuración del comando / Environments
### Comando de shell por defecto / Default shell command
Se usa en sistemas operativos que no definen su propio comando de shell.

- Campo: \[Enter your command\]
- Preview de terminal: `cmd.exe`

### Comando de shell en macOS / Shell command on macOS
Si está vacío, se utilizará el comando de shell por defecto en macOS.

- Campo: \[input text\]
- Preview de terminal: `Unknown shell`

### Comando de shell en Linux / Shell command on Linux
Si está vacío, se utilizará el comando de shell por defecto en Linux.

- Campo: \[input text\]
- Preview de terminal: `Unknown shell`

### Comando de shell en Windows / Shell command on Windows
Si está vacío, se utilizará el comando de shell por defecto en Windows.

- Campo: \[input text\]
- Preview de terminal: `cmd.exe`

### Terminal de macOS / macOS shell
- Opción: \[Use default (system default)/Bash/Dash/Zsh (Z shell)\]

### Terminal de Linux / Linux shell
- Opción: \[Use default (system default)/Bash/Dash/Zsh (Z shell)\]

### Terminal de Windows / Windows shell
Se recomienda PowerShell sobre cmd.exe, ya que este plugin no admite el escape de variables en CMD.

- Opción: \[Use default (cmd.exe)/PowerShell Core/PowerShell 5/cmd.exe\]

---

## Pestaña: Configuración del comando / Events
### Disponibilidad en la paleta de comandos de Obsidian / Availability in Obsidian's command palette
- Opción: \[Command palette & hotkeys/hotkeys only/excluded\]

### Debouncing (experimental) / Debouncing (experimental)
Si está activado, los eventos no pueden realizar múltiples ejecuciones concurrentes o muy continuas de este comando de shell. No afecta a los eventos marcados con un ícono de prohibido.
- Acción: >❓<

- **Execute before cooldown:** (1/0)
- **Execute after cooldown:** (1/0)

### Ejecutar este comando de shell automáticamente cuando: / Execute this shell command automatically when:

> [!note] Todos los eventos siguientes tienen el mismo control: toggle (1/0) y un botón >❓< de documentación.

* Obsidian inicia / Obsidian starts
* Obsidian cierra / Obsidian quits
* Cambiar el panel activo / Switching the active pane
* El cursor se mueve en el editor / Caret moved in editor
* Cada n segundos / Every n seconds
* Menú de archivo / File menu 🚫
* Menú de carpeta / Folder menu 🚫
* Menú del editor / Editor menu 🚫
* Contenido del archivo modificado / File content modified
* Archivo creado / File created
* Archivo eliminado / File deleted
* Archivo movido / File moved
* Archivo renombrado / File renamed
* Carpeta creada / Folder created
* Carpeta eliminada / Folder deleted
* Carpeta movida / Folder moved
* Carpeta renombrada / Folder renamed

> *Nota general del sistema:* Cada uno de estos eventos proporciona variables adicionales específicas (como `{{event_type}}`, `{{event_file_path}}`, `{{event_file_content}}`, etc.) que pueden ser utilizadas por el script al dispararse de manera automática.

---

## Pestaña: Configuración del comando / Variables
### Valores por defecto para variables / Default values for variables
Ciertas variables pueden no estar disponibles en algunas situaciones (por ejemplo, `{{file_name}}` no está disponible si no hay ningún panel de archivo activo). Puedes definir valores por defecto que se utilizarán cuando una variable no esté disponible de otro modo.

---

### Configuración por Variable
Cada una de las siguientes variables cuenta con su propia caja selectora para definir la acción en caso de no estar disponible:

#### Lista de Variables del Editor y Archivo
* `{{caret_paragraph}}`
* `{{caret_position}}`
* `{{environment}}`
* `{{file_content}}`
* `{{file_extension}}`
* `{{file_name}}`
* `{{file_path}}`
* `{{file_uri}}`
* `{{folder_name}}`
* `{{folder_path}}`
* `{{note_content}}`
* `{{selection}}`
* `{{tags}}`
* `{{title}}`
* `{{workspace}}`
* `{{yaml_content}}`
* `{{yaml_value}}`
* `{{yaml_values}}`

#### Lista de Variables de Eventos (Disparadores)
* `{{event_file_content}}`
* `{{event_file_extension}}`
* `{{event_file_name}}`
* `{{event_file_path}}`
* `{{event_file_uri}}`
* `{{event_folder_name}}`
* `{{event_folder_path}}`
* `{{event_note_content}}`
* `{{event_old_file_name}}`
* `{{event_old_file_path}}`
* `{{event_old_folder_name}}`
* `{{event_old_folder_path}}`
* `{{event_old_title}}`
* `{{event_tags}}`
* `{{event_title}}`
* `{{event_type}}`
* `{{event_yaml_content}}`
* `{{event_yaml_value}}`
* `{{event_yaml_values}}`

#### Opciones de comportamiento (para todas las variables anteriores):
Si no está disponible, entonces:
- Opción: [Inherit: cancel execution and show errors/Cancel execution and show errors/Cancel execution silently/Execute with value:]
- Acción: >❓<

---