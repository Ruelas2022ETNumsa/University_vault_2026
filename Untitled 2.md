# Configuración Shell Commands

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

---

## Pestaña: Shell commands

### Buscar comandos de shell (Search shell commands)
* **Descripción:** Busca alias de comandos de shell, comandos, IDs e íconos.
* **Campo:** \[input text\]

### Estado
* **Descripción:** No hay comandos de shell aún, haz clic en el botón 'New shell command' de abajo.
* **Acción:** >New shell command<

---

## Pestaña: Environments

### Directorio de trabajo (Working directory)
* **Descripción:** Un directorio donde se ejecutarán tus comandos. Si está vacío, por defecto será la ubicación de tu bóveda (vault). Puede ser relativo (= una carpeta en la bóveda) o absoluto (= completo desde la raíz del sistema de archivos de Windows). Si estás usando una shell que virtualiza otro sistema operativo diferente a Windows (por ejemplo, 'Windows Subsystem for Linux'), de igual manera deberías ingresar una ruta con formato de Windows. Tu shell hará la conversión si es necesario.
* **Campo:** \[E:\repp\]

### Shell por defecto de macOS (macOS default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual.
* **Campo:** \[Use system default\]

### Shell por defecto de Linux (Linux default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual.
* **Campo:** \[Use system default\]

### Shell por defecto de Windows (Windows default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual. Se recomienda Powershell sobre cmd.exe, porque este plugin no soporta el escape de variables in CMD.
* **Campo:** \[Use system default (cmd.exe)\]

---

### Shells personalizadas (Custom shells)
* **Descripción:** Define por ejemplo WSL (Windows Subsystem for Linux), MinGW-w64 (Git Bash) o Wine aquí.
* **Acción:** >New custom shell<

---

### Agregar directorios a la variable de entorno Path (Add directories to the Path environment variable)
* **Descripción:** Esto es a veces necesario para poder llamar a algunas aplicaciones instaladas por el usuario. Los directorios se añadirán DESPUÉS de los directorios por defecto en Path, a menos que se incluya {{environment:Path}}. También se pueden usar otras {{variables}}, pero no afectan el orden de adición.

#### Adiciones de PATH para macOS (macOS PATH additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* **Campo:** \[input text\]

#### Adiciones de PATH para Linux (Linux PATH additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* **Campo:** \[input text\]

#### Adiciones de Path para Windows (Windows Path additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por un punto y coma (;).
* **Campo:** \[input text\]

#### Nota informativa: Las adiciones de Path no funcionan en Shells personalizadas (The Path additions do not work in Custom shells)
* **Descripción:** Solo funcionan en shells que vienen predefinidas in este plugin. Para instrucciones sobre cómo hacer adiciones de Path para shells personalizadas, por favor haz clic en el enlace de documentación a la derecha.

---

## Pestaña: Preactions

### Prompts
* **Acción:** >New prompt<

---

## Pestaña: Output

### Envolturas de salida (Output wrappers)
* **Acción:** >New output wrapper<

---

### Duración del mensaje de error (Error message duration)
* **Descripción:** Se refiere a los mensajes sobre comandos de shell fallidos. En segundos, entre 1 y 180.
* **Campo:** \[20\]

---

### Duración del mensaje de notificación (Notification message duration)
* **Descripción:** Se refiere a mensajes informativos, no fatales, por ejemplo, salida dirigida al 'Globo de notificación'. En segundos, entre 1 y 180.
* **Campo:** \[10\]

---

### Mostrar una notificación al ejecutar comandos de shell (Show a notification when executing shell commands)
* **Campo:** \[Do not show/Show for 10 seconds/Show until the process is finished/show only if executing takes long\]

---

### Enviar la salida al Portapapeles también muestra un mensaje de notificación (Outputting to Clipboard displays a notification message, too)
* **Descripción:** Si la salida de un comando de shell se dirige al portapapeles, también muestra la salida en una caja emergente en la esquina superior derecha. Esto ayuda a notar qué se insertó en el portapapeles.
* **Campo:** (1/0) = 1

---

### Enviar la salida al Globo de notificación/error usa formato monoespaciado (Outputting to Notification/error balloon uses monospace formatting)
* **Descripción:** (description:)
* **Campo:** \[For stdout and stderr\]
* **Acción:** >T< (manage obsidian's monospace font)

---

## Pestaña: Events

* **Descripción General:** Los eventos introducen una forma de ejecutar comandos de shell automáticamente en ciertas situaciones, por ejemplo, cuando Obsidian se inicia. Se configuran para cada comando de shell por separado, pero esta pestaña contiene opciones generales para ellos.

---

### Habilitar eventos (Enable events)
* **Descripción:** Esta es una forma rápida de apagar inmediatamente todos los eventos, si lo deseas.
* **Campo:** (1/0) =1

---

### Vista general de eventos
* **Descripción:** Lo siguiente ofrece solo un vistazo rápido sobre qué eventos están habilitados en qué comandos de shell. Para habilitar/deshabilitar eventos para un comando de shell, ve a la configuración del comando de shell en particular a través de la pestaña 'Shell commands'. La lista solo se actualiza cuando vuelves a abrir todo el panel de configuración.
* **Estado:** No hay eventos habilitados para ningún comando de shell (No events are enabled for any shell commands).

---

---
---
---



## Pestaña: Variables

### Previsualizar variables en la paleta de comandos y menús (Preview variables in command palette and menus)
* **Descripción:** Si está activado, los nombres de las variables se sustituyen por sus valores en tiempo real cuando ves tus comandos en la paleta de comandos y en los menús contextuales de clic derecho (si se usan). Una buena manera de asegurar que tus comandos usarán los valores correctos.
* **Campo:** (1/0) = 1

---

### Mostrar menú de autocompletado (Show autocomplete menu)
* **Descripción:** Si está activado, aparece un menú desplegable cuando comienzas a escribir nombres de \{\{variable\}\}, mostrando las variables que coinciden y sus instrucciones. También permite definir sugerencias personalizadas en el archivo autocomplete.yaml - consulta la documentación.
* **Campo:** (1/0) = 1

---

### Variables personalizadas (Custom variables)
* **Descripción:** (description:)
* **Acción:** >open a pane that displays all custom varialbles and their values<
* **Campo:** \[Via URI: Notify/Via URI: Don't Notify\] \[Via output assignment: Notify/Via output assignment: Don't Notify\]
* **Acción:** >New custom variable<

---

### Variables integradas (Built-in variables)

#### \{\{caret_paragraph\}\}
* **Descripción:** Da una línea de texto en la posición actual del cursor. Solo disponible cuando un panel de notas está abierto, no en la vista de gráfico, ni al ver archivos que no sean de texto. No disponible en modo de vista previa.
* **Default value for \{\{caret_paragraph\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors/Cancel execution silently/execute whit value\]

#### \{\{caret_position\}\}, \{\{caret_position:line\}\} or \{\{caret_position:column\}\}
* **Descripción:** Da el número de línea y la posición de columna de la posición actual del cursor como 'línea:columna'. Obtén solo el número de línea usando \{\{caret_position:line\}\}, y solo la columna con \{\{caret_position:column\}\}. Los números de línea y columna están indexados en 1. Solo disponible cuando un panel de notas está abierto, no en la vista de gráfico, ni al ver archivos que no sean de texto. No disponible en modo de vista previa.
* **Default value for \{\{caret_position\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{clipboard\}\}
* **Descripción:** Da el contenido que copiaste por última vez en tu portapapeles.
* **Default value for \{\{clipboard\}\}**
	* **Descripción:** \{\{clipboard\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{date\}\}
* **Descripción:** Da una marca de fecha/hora según tu gusto. La parte "format" se puede personalizar y es obligatoria. Opciones de formato: https://momentjs.com/docs/#/displaying/format/
* **Default value for \{\{date\}\}**
	* **Descripción:** \{\{date\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{environment:variable\}\}
* **Descripción:** Da el valor de una variable de entorno. Es un valor original recibido cuando se inició Obsidian. Solo disponible si el nombre de la variable de entorno pasada existe.
* **Default value for \{\{environment\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{file_content\}\}
* **Descripción:** Da el contenido del archivo actual, incluyendo el frontmatter YAML. Si necesitas excluir el YAML, usa \{\{note_content\}\} en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{file_content\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{file_extension:with-dot\}\} or \{\{file_extension:no-dot\}\}
* **Descripción:** Da la terminación del nombre del archivo actual. Usa \{\{file_extension:with-dot\}\} para incluir un punto precedente. Si la extensión está vacía, no se añade ningún punto. \{\{file_extension:no-dot\}\} nunca incluye un punto. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{file_extension\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{file_name\}\}
* **Descripción:** Da el nombre del archivo actual con una extensión de archivo. Si lo necesitas sin la extensión, usa \{\{title\}\} en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{file_name\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{file_path:relative\}\} or \{\{file_path:absolute\}\}
* **Descripción:** Da la ruta al archivo actual, ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{file_path\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{file_uri\}\}
* **Descripción:** Da un URI de Obsidian que abre el archivo actual. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{file_uri\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{folder_name\}\}
* **Descripción:** Da el nombre de la carpeta contenedora del archivo actual, o un punto si la carpeta es la raíz de la bóveda. No se incluyen carpetas ancestros. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{folder_name\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{folder_path:relative\}\} or \{\{folder_path:absolute\}\}
* **Descripción:** Da la ruta a la carpeta contenedora del archivo actual, ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{folder_path\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{new_note_folder_name\}\}
* **Descripción:** Da el nombre de la carpeta para "Ubicación predeterminada para nuevas notas" (una configuración en Obsidian). No se incluyen carpetas ancestros.
* **Default value for \{\{new_note_folder_name\}\}**
	* **Descripción:** \{\{new_note_folder_name\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{folder_path:relative\}\} or \{\{folder_path:absolute\}\}
* **Descripción:** Da la ruta a la carpeta "Ubicación predeterminada para nuevas notas" (una configuración en Obsidian), ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian.
* **Default value for \{\{new_note_folder_path\}\}**
	* **Descripción:** \{\{new_note_folder_path\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{note_content\}\}
* **Descripción:** Da el contenido de la nota actual sin el frontmatter YAML. Si necesitas incluir el YAML, usa \{\{file_content\}\} en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{note_content\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{obsidian_api_version\}\} or \{\{obsidian_api_version:major|minor|patch\}\}
* **Descripción:** Da la versión de la API de Obsidian, la cual sigue el ciclo de lanzamiento de la aplicación de escritorio.
* **Default value for \{\{obsidian_api_version\}\}**
	* **Descripción:** \{\{obsidian_api_version\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{selection\}\}
* **Descripción:** Da el texto seleccionado actualmente. Solo disponible cuando hay algo seleccionado en el modo de Edición/Vista previa en vivo, no en el modo de Lectura.
* **Default value for \{\{selection\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{shell_commands_plugin_version:plugin\}\}, \{\{shell_commands_plugin_version:plugin:major|minor|patch\}\}, \{\{shell_commands_plugin_version:settings\}\} or \{\{shell_commands_plugin_version:settings:major|minor|patch\}\}
* **Descripción:** Da la versión del plugin o la versión de la estructura de configuración.
* **Default value for \{\{shell_commands_plugin_version\}\}**
	* **Descripción:** \{\{shell_commands_plugin_version\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{tags\}\}
* **Descripción:** Da todas las etiquetas definidas en la nota actual. Reemplaza la parte "separator" con una coma, espacio o los caracteres que desees usar como separador entre etiquetas. Siempre se necesita definir un separador. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{tags\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{title\}\}
* **Descripción:** Da el nombre del archivo actual sin una extensión de archivo. Si lo necesitas con la extensión, usa \{\{file_name\}\} en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
* **Default value for \{\{title\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]

#### \{\{vault_path\}\}
* **Descripción:** Da la ruta absoluta de la bóveda de Obsidian desde la raíz del sistema de archivos. Esta es la misma que se usa como directorio de trabajo por defecto si no defines uno manualmente. Si defines un directorio de trabajo manualmente, esta variable no te dará tu directorio definido manualmente, siempre da el directorio raíz de la bóveda.
* **Default value for \{\{vault_path\}\}**
	* **Descripción:** \{\{vault_path\}\} siempre está disponible, por lo que no puede tener un valor por defecto.

#### \{\{workspace\}\}
* **Descripción:** Da el nombre del espacio de trabajo actual. Solo disponible cuando el plugin principal Workspaces está activado.
* **Default value for \{\{workspace\}\}**
	* **Descripción:** Si no está disponible, entonces:
	* **Campo:** \[Cancel execution and show errors\]