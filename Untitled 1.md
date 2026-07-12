# Configuración Shell Commands

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
* **Campo:** \[input text\] (con ícono de lupa)

### Estado
* **Descripción:** No hay comandos de shell aún, haz clic en el botón 'New shell command' de abajo.
* **Acción:** >New shell command<

---

## Pestaña: Environments

### Directorio de trabajo (Working directory)
* **Descripción:** Un directorio donde se ejecutarán tus comandos. Si está vacío, por defecto será la ubicación de tu bóveda (vault). Puede ser relativo (= una carpeta en la bóveda) o absoluto (= completo desde la raíz del sistema de archivos de Windows). Si estás usando una shell que virtualiza otro sistema operativo diferente a Windows (por ejemplo, 'Windows Subsystem for Linux'), de igual manera deberías ingresar una ruta con formato de Windows. Tu shell hará la conversión si es necesario.
* **Campo:** \[input text (E:\repp)\]

### Shell por defecto de macOS (macOS default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual.
* **Campo:** \[Use system default/Bash/Dash/Z shell\] (menú de elección)

### Shell por defecto de Linux (Linux default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual.
* **Campo:** \[Use system default/Bash/Dash/Z shell\] (menú de elección)

### Shell por defecto de Windows (Windows default shell)
* **Descripción:** Puede ser anulado por cada comando de shell individual. Se recomienda Powershell sobre cmd.exe, porque este plugin no soporta el escape de variables en CMD.
* **Campo:** \[Use system default (cmd.exe)/PowerShell Core/PowerShell 5/cmd.exe\] (menú de elección)

---

### Shells personalizadas (Custom shells)
* **Descripción:** Define por ejemplo WSL (Windows Subsystem for Linux), MinGW-w64 (Git Bash) o Wine aquí.
* **Acción:** >New custom shell<

---

### Agregar directorios a la variable de entorno Path (Add directories to the Path environment variable)
* **Descripción:** Esto es a veces necesario para poder llamar a algunas aplicaciones instaladas por el usuario. Los directorios se añadirán DESPUÉS de los directorios por defecto en Path, a menos que se incluya {{!environment:Path}}. También se pueden usar otras {{variables}}, pero no afectan el orden de adición.

#### Adiciones de PATH para macOS (macOS PATH additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* **Campo:** [input text] (caja de texto multilínea vacía)

#### Adiciones de PATH para Linux (Linux PATH additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por dos puntos (:).
* **Campo:** [input text] (caja de texto multilínea vacía)

#### Adiciones de Path para Windows (Windows Path additions)
* **Descripción:** Define cada directorio en una línea separada, o múltiples directorios en una sola línea, separados por un punto y coma (;).
* **Campo:** [input text] (caja de texto multilínea vacía)

#### Nota informativa: Las adiciones de Path no funcionan en Shells personalizadas (The Path additions do not work in Custom shells)
* **Descripción:** Solo funcionan en shells que vienen predefinidas en este plugin. Para instrucciones sobre cómo hacer adiciones de Path para shells personalizadas, por favor haz clic en el enlace de documentación a la derecha.
