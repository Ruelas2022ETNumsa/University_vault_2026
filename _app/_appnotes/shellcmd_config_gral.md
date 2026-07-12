---
title: "Shell Commands — Configuración Global"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_config_script]]"
  - "[[shellcommands_guide]]"
tags: [beacon, obsidian, shell-commands, infraestructura, automatizacion]
date_created: 2026-07-12
date_updated: 2026-07-12
status: borrador
---

# Configuración Shell Commands (Global)

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
Busca alias de comandos de shell, comandos, IDs e íconos.
* Campo: \[input text\]

### Estado
No hay comandos de shell aún, haz clic en el botón 'New shell command' de abajo.
* Acción: >New shell command<

> [!info] Configuración por script
> Al crear un nuevo comando con *New shell command*, se habilitan opciones de configuración individuales para ese comando (alias, shell, output, eventos, variables, etc.).
> → Ver también: [[shellcmd_config_script]]

---

## Pestaña: Environments

### Directorio de trabajo (Working directory)
Un directorio donde se ejecutarán tus comandos. Si está vacío, por defecto será la ubicación de tu bóveda (vault). Puede ser relativo (= una carpeta en la bóveda) o absoluto (= completo desde la raíz del sistema de archivos de Windows). Si estás usando una shell que virtualiza otro sistema operativo diferente a Windows (por ejemplo, 'Windows Subsystem for Linux'), de igual manera deberías ingresar una ruta con formato de Windows. Tu shell hará la conversión si es necesario.
* Campo: \[E:\repp\]

### Shell por defecto de macOS (macOS default shell)
Puede ser anulado por cada comando de shell individual.
* Campo: \[Use system default\]

### Shell por defecto de Linux (Linux default shell)
Puede ser anulado por cada comando de shell individual.
* Campo: \[Use system default\]

### Shell por defecto de Windows (Windows default shell)
Puede ser anulado por cada comando de shell individual. Se recomienda Powershell sobre cmd.exe, porque este plugin no soporta el escape de variables in CMD.
* Campo: \[Use system default (cmd.exe)\]

### Shells personalizadas (Custom shells)
Define por ejemplo WSL (Windows Subsystem for Linux), MinGW-w64 (Git Bash) o Wine aquí.
* Acción: >New custom shell<

### Agregar directorios a la variable de entorno Path (Add directories to the Path environment variable)
Esto es a veces necesario para poder llamar a algunas aplicaciones instaladas por el usuario. Los directorios se añadirán DESPUÉS de los directorios por defecto en Path, a menos que se incluya {{environment:Path}}. También se pueden usar otras {{variables}}, pero no afectan el orden de adición.

### Adiciones de PATH para macOS (macOS PATH additions)
Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* Campo: \[input text\]

### Adiciones de PATH para Linux (Linux PATH additions)
Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* Campo: \[input text\]

### Adiciones de Path para Windows (Windows Path additions)
Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por un punto y coma (;).
* Campo: \[input text\]

> [!warning] Nota informativa: Las adiciones de Path no funcionan en Shells personalizadas (The Path additions do not work in Custom shells)
Solo funcionan en shells que vienen predefinidas in este plugin. Para instrucciones sobre cómo hacer adiciones de Path para shells personalizadas, por favor haz clic en el enlace de documentación a la derecha.

---

## Pestaña: Preactions

### Prompts
* Acción: >New prompt<

---

## Pestaña: Output

### Envolturas de salida (Output wrappers)
* Acción: >New output wrapper<

### Duración del mensaje de error (Error message duration)
Se refiere a los mensajes sobre comandos de shell fallidos. En segundos, entre 1 y 180.
* Campo: \[20\]

### Duración del mensaje de notificación (Notification message duration)
Se refiere a mensajes informativos, no fatales, por ejemplo, salida dirigida al 'Globo de notificación'. En segundos, entre 1 y 180.
* Campo: \[10\]

### Mostrar una notificación al ejecutar comandos de shell (Show a notification when executing shell commands)
* Campo: \[Do not show/Show for 10 seconds/Show until the process is finished/show only if executing takes long\]

### Enviar la salida al Portapapeles también muestra un mensaje de notificación (Outputting to Clipboard displays a notification message, too)
Si la salida de un comando de shell se dirige al portapapeles, también muestra la salida en una caja emergente en la esquina superior derecha. Esto ayuda a notar qué se insertó en el portapapeles.
* Campo: (1/0) = 1

### Enviar la salida al Globo de notificación/error usa formato monoespaciado (Outputting to Notification/error balloon uses monospace formatting)
* Campo: \[For stdout and stderr\]
* Acción: >T< (manage obsidian's monospace font)

---

## Pestaña: Events

* Descripción General: Los eventos introducen una forma de ejecutar comandos de shell automáticamente en ciertas situaciones, por ejemplo, cuando Obsidian se inicia. Se configuran para cada comando de shell por separado, pero esta pestaña contiene opciones generales para ellos.

---

### Habilitar eventos (Enable events)
Esta es una forma rápida de apagar inmediatamente todos los eventos, si lo deseas.
* Campo: (1/0) =1

---

### Vista general de eventos
Lo siguiente ofrece solo un vistazo rápido sobre qué eventos están habilitados en qué comandos de shell. Para habilitar/deshabilitar eventos para un comando de shell, ve a la configuración del comando de shell en particular a través de la pestaña 'Shell commands'. La lista solo se actualiza cuando vuelves a abrir todo el panel de configuración.
* Estado: No hay eventos habilitados para ningún comando de shell (No events are enabled for any shell commands).

---

## Pestaña: Variables

> [!note] Comportamiento por defecto de las variables
> La mayoría de las variables solo están disponibles cuando hay un archivo activo en el panel. Para todas ellas, si no están disponibles se puede configurar:
> `[Cancel execution and show errors / Cancel execution silently / Execute with value]`
> Las variables siempre disponibles ({{clipboard}}, {{date}}, {{vault_path}}, {{new_note_folder_name}}, {{new_note_folder_path}}, {{obsidian_api_version}}, {{shell_commands_plugin_version}}) no tienen valor por defecto.

### Previsualizar variables en la paleta de comandos y menús (Preview variables in command palette and menus)
Si está activado, los nombres de las variables se sustituyen por sus valores en tiempo real cuando ves tus comandos en la paleta de comandos y en los menús contextuales de clic derecho (si se usan). Una buena manera de asegurar que tus comandos usarán los valores correctos.
* Campo: (1/0) = 1

### Mostrar menú de autocompletado (Show autocomplete menu)
Si está activado, aparece un menú desplegable cuando comienzas a escribir nombres de `{{variable}}`, mostrando las variables que coinciden y sus instrucciones. También permite definir sugerencias personalizadas en el archivo autocomplete.yaml - consulta la documentación.
* Campo: (1/0) = 1

### Variables personalizadas (Custom variables)
 * Acción: >open a pane that displays all custom varialbles and their values<
* Campo: \[Via URI: Notify/Via URI: Don't Notify\] \[Via output assignment: Notify/Via output assignment: Don't Notify\]
* Acción: >New custom variable<

### Variables integradas (Built-in variables)

#### `{{caret_paragraph}}`
 Da una línea de texto en la posición actual del cursor. Solo disponible cuando un panel de notas está abierto, no en la vista de gráfico, ni al ver archivos que no sean de texto. No disponible en modo de vista previa.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{caret_position}}`, `{{caret_position:line}}` or `{{caret_position:column}}`
 Da el número de línea y la posición de columna de la posición actual del cursor como 'línea:columna'. Obtén solo el número de línea usando `{{caret_position:line}}`, y solo la columna con `{{caret_position:column}}`. Los números de línea y columna están indexados en 1. Solo disponible cuando un panel de notas está abierto, no en la vista de gráfico, ni al ver archivos que no sean de texto. No disponible en modo de vista previa.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{clipboard}}`
Da el contenido que copiaste por última vez en tu portapapeles.
##### Default value
* `{{clipboard}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{date}}`
 Da una marca de fecha/hora según tu gusto. La parte "format" se puede personalizar y es obligatoria. Opciones de formato: https://momentjs.com/docs/#/displaying/format/
##### Default value
* `{{date}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{environment:variable}}`
Da el valor de una variable de entorno. Es un valor original recibido cuando se inició Obsidian. Solo disponible si el nombre de la variable de entorno pasada existe.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{file_content}}`
Da el contenido del archivo actual, incluyendo el frontmatter YAML. Si necesitas excluir el YAML, usa `{{note_content}}` en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{file_extension:with-dot}}` or `{{file_extension:no-dot}}`
Da la terminación del nombre del archivo actual. Usa `{{file_extension:with-dot}}` para incluir un punto precedente. Si la extensión está vacía, no se añade ningún punto. `{{file_extension:no-dot}}` nunca incluye un punto. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{file_name}}`
Da el nombre del archivo actual con una extensión de archivo. Si lo necesitas sin la extensión, usa `{{title}}` en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{file_path:relative}}` or `{{file_path:absolute}}`
Da la ruta al archivo actual, ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{file_uri}}`
Da un URI de Obsidian que abre el archivo actual. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{folder_name}}`
Da el nombre de la carpeta contenedora del archivo actual, o un punto si la carpeta es la raíz de la bóveda. No se incluyen carpetas ancestros. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{folder_path:relative}}` or `{{folder_path:absolute}}` — carpeta del archivo activo
Da la ruta a la carpeta contenedora del archivo actual, ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{new_note_folder_name}}`
Da el nombre de la carpeta para "Ubicación predeterminada para nuevas notas" (una configuración en Obsidian). No se incluyen carpetas ancestros.
##### Default value
* `{{new_note_folder_name}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{folder_path:relative}}` or `{{folder_path:absolute}}` — carpeta de nuevas notas (`new_note_folder_path`)
Da la ruta a la carpeta "Ubicación predeterminada para nuevas notas" (una configuración en Obsidian), ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian.
##### Default value
* `{{new_note_folder_path}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{note_content}}`
Da el contenido de la nota actual sin el frontmatter YAML. Si necesitas incluir el YAML, usa `{{file_content}}` en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{obsidian_api_version}}` or `{{obsidian_api_version:major|minor|patch}}`
Da la versión de la API de Obsidian, la cual sigue el ciclo de lanzamiento de la aplicación de escritorio.
##### Default value
* `{{obsidian_api_version}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{selection}}`
Da el texto seleccionado actualmente. Solo disponible cuando hay algo seleccionado en el modo de Edición/Vista previa en vivo, no en el modo de Lectura.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{shell_commands_plugin_version:plugin}}`, `{{shell_commands_plugin_version:plugin:major|minor|patch}}`, `{{shell_commands_plugin_version:settings}}` or `{{shell_commands_plugin_version:settings:major|minor|patch}}`
Da la versión del plugin o la versión de la estructura de configuración.
##### Default value
* `{{shell_commands_plugin_version}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{tags}}`
Da todas las etiquetas definidas en la nota actual. Reemplaza la parte "separator" con una coma, espacio o los caracteres que desees usar como separador entre etiquetas. Siempre se necesita definir un separador. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{title}}`
Da el nombre del archivo actual sin una extensión de archivo. Si lo necesitas con la extensión, usa `{{file_name}}` en su lugar. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{vault_path}}`
Da la ruta absoluta de la bóveda de Obsidian desde la raíz del sistema de archivos. Esta es la misma que se usa como directorio de trabajo por defecto si no defines uno manualmente. Si defines un directorio de trabajo manualmente, esta variable no te dará tu directorio definido manualmente, siempre da el directorio raíz de la bóveda.
##### Default value
* `{{vault_path}}` siempre está disponible, por lo que no puede tener un valor por defecto.

#### `{{workspace}}`
Da el nombre del espacio de trabajo actual. Solo disponible cuando el plugin principal Workspaces está activado.
##### Default value
* → Ver nota al inicio de la sección.

#### `{{yaml_content:with-dashes}}` or `{{yaml_content:no-dashes}}`
Entrega el frontmatter YAML de la nota actual. Los guiones --- pueden ser incluidos o excluidos. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, debe estar presente una sección de frontmatter YAML.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{yaml_value:property}}`
Lee un único valor del frontmatter del archivo actual. Toma el nombre de una propiedad como argumento. Puedes acceder a propiedades anidadas con la notación de punto: `property1.property2`. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{yaml_values:property:separator}}`
Lee una lista de valores del frontmatter del archivo actual. Toma el nombre de una propiedad y un separador como argumentos. Puedes acceder a propiedades anidadas con la notación de punto: `property1.property2`. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_content}}`
Entrega el contenido del archivo relacionado con el evento, incluyendo el frontmatter YAML. Si necesitas excluir el YAML, usa `{{event_note_content}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_extension:with-dot}}` or `{{event_file_extension:no-dot}}`
Entrega la extensión del nombre del archivo relacionado con el evento. Usa `{{event_file_extension:with-dot}}` para incluir un punto precedente. Si la extensión está vacía, no se añade ningún punto. `{{event_file_extension:no-dot}}` nunca incluye un punto. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_name}}`
Entrega el nombre del archivo relacionado con el evento junto con su extensión de archivo. Si lo necesitas sin la extensión, usa `{{event_title}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_path:relative}}` or `{{event_file_path:absolute}}` — ruta del archivo del evento
Entrega la ruta del archivo relacionado con el evento, ya sea absoluta desde la raíz del sistema de archivos, o relativa desde la raíz del vault de Obsidian. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_uri}}`
Entrega un URI de Obsidian que abre el archivo relacionado con el evento. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_folder_name}}`
Eventos de archivo: Entrega el nombre de la carpeta contenedora del archivo relacionado con el evento. Eventos de carpeta: Entrega el nombre de la carpeta seleccionada. Entrega un punto si la carpeta es la raíz del vault. No se incluyen carpetas ancestros. Solo disponible en los eventos: Menú de archivo, Menú de carpeta, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado, Carpeta creada, Carpeta eliminada, Carpeta movida, Carpeta renombrada.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_folder_path:relative}}` or `{{event_folder_path:absolute}}`
Eventos de archivo: Entrega la ruta de la carpeta contenedora del archivo relacionado con el evento. Eventos de carpeta: Entrega la ruta de la carpeta relacionada con el evento. La ruta es absoluta desde la raíz del sistema de archivos, o relativa desde la raíz del vault de Obsidian. Solo disponible en los eventos: Menú de archivo, Menú de carpeta, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado, Carpeta creada, Carpeta eliminada, Carpeta movida, Carpeta renombrada.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_note_content}}`
Entrega el contenido del archivo relacionado con el evento sin el frontmatter YAML. Si necesitas incluir el YAML, usa `{{event_file_content}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_old_file_name}}`
Entrega el nombre antiguo del archivo renombrado con su extensión de archivo. Si lo necesitas sin la extensión, usa `{{event_old_title}}` en su lugar. Solo disponible en los eventos: Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_path:relative}}` or `{{event_file_path:absolute}}` — ruta antigua del archivo (`event_old_file_path`)
Entrega la ruta antigua del archivo renombrado/movido, ya sea absoluta desde la raíz del sistema de archivos, o relativa desde la raíz del vault de Obsidian. Solo disponible en los eventos: Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_old_folder_name}}`
Eventos de archivo: Entrega el nombre de la carpeta contenedora antigua del archivo movido. Eventos de carpeta: Entrega el nombre antiguo de la carpeta renombrada. Solo disponible en los eventos: Archivo movido, Folder renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_file_path:relative}}` or `{{event_file_path:absolute}}` — ruta antigua de la carpeta (`event_old_folder_path`)
Eventos de archivo: Entrega la ruta de la carpeta contenedora antigua del archivo movido. Eventos de carpeta: Entrega la ruta antigua de la carpeta renombrada/movida. La ruta es absoluta desde la raíz del sistema de archivos, o relativa desde la raíz del vault de Obsidian. Solo disponible en los eventos: Archivo movido, Folder movido, Folder renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_old_title}}`
Entrega el nombre antiguo del archivo renombrado sin la extensión de archivo. Si lo necesitas con la extensión, usa `{{event_old_file_name}}` en su lugar. Solo disponible en los eventos: Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_tags}}`
Entrega todas las etiquetas definidas en la nota relacionada con el evento. Reemplaza la sección "separator" con una coma, espacio o los caracteres que desees utilizar como separador entre etiquetas. Siempre es necesario definir un separador. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_title}}`
Entrega el nombre del archivo relacionado con el evento sin su extensión de archivo. Si lo necesitas con la extensión, usa `{{event_file_name}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_type}}` or `{{event_type:category}}`
Indica qué evento fue activado. Solo disponible en cualquier evento.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_yaml_content:with-dashes}}` or `{{event_yaml_content:no-dashes}}`
Entrega el frontmatter YAML de la nota relacionada con el evento. Los guiones --- pueden ser incluidos o excluidos. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado. Además, debe estar presente una sección de frontmatter YAML.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_yaml_value:property}}`
Lee un único valor del frontmatter del archivo relacionado con el evento. Toma el nombre de una propiedad como argumento. Puedes acceder a propiedades anidadas con la notación de punto: `property1.property2`. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
##### Default value
- → Ver nota al inicio de la sección.

#### `{{event_yaml_values:property:separator}}`
Lee una lista de valores del frontmatter del archivo relacionado con el evento. Toma el nombre de una propiedad y un separador como argumentos. Puedes acceder a propiedades anidadas con la notación de punto: `property1.property2`. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
##### Default value
- → Ver nota al inicio de la sección.

---

Cuando escribes variables dentro de los comandos, aparece un texto de vista previa debajo del campo del comando para mostrar cómo se verá el comando cuando se ejecute con las variables sustituidas por sus valores reales.

Se intenta escapar los caracteres especiales en los valores de las variables (excepto si usas CMD como la terminal en Windows). Esto es para mejorar la seguridad, de modo que una variable no cause accidentalmente que sucedan cosas malas. Si deseas usar un valor bruto sin escapar, añade un signo de exclamación antes del nombre de la variable, por ejemplo, `{{!title}}`, ¡pero ten cuidado, es peligroso!

No hay forma de evitar el procesamiento de variables. Si necesitas caracteres `{{}}` en tu comando, no se procesarán como variables siempre y cuando no contengan ninguno de los nombres de variables listados anteriormente. Si necesitas pasar por ejemplo `{{title}}` literalmente a tu comando, no hay forma de hacerlo en este momento, por favor crea una discusión en GitHub.

Todas las variables que acceden al archivo actual pueden hacer que la vista previa del comando falle si no tenías un panel de archivo activo al abrir la ventana de configuración - por ejemplo, si tenías el foco en la vista de gráfico en lugar de en una nota = ningún archivo está activo actualmente. Pero esto no rompe ninguna otra cosa más que la vista previa.