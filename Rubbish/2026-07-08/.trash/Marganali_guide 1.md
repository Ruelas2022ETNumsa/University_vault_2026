---
title: "Cornell Marginalia — Guía completa"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[plugin_guide]]"
  - "[[obsidian_guide]]"
  - "[[latex_guide]]"
tags: [beacon, obsidian, plugins, infraestructura, marginalia]
date_created: 2026-07-06
date_updated: 2026-07-06
status: activo
---

# Cornell Marginalia — Guía completa

> Plugin: [latazadehomero/cornell-marginalia](https://github.com/latazadehomero/cornell-marginalia) — instalado vía Community Plugins
> Versión actual: v4.9.0

---

## Índice

- [[#§0. Instalación y parche]]
- [[#§1. Sintaxis core]]
- [[#§2. Semantic Highlighting]]
- [[#§3. Grouping — Method A vs B]]
- [[#§4. Imágenes en el margen]]
- [[#§5. Marginalia Explorer]]
- [[#§6. Reading View]]
- [[#§7. Active Recall — Blur]]
- [[#§8. Flashcard Generator]]
- [[#§9. Margin Threads]]
- [[#§10. Doodle Engine]]
- [[#§11. Omni-Capture]]
- [[#§12. PDF Export]]
- [[#§13. Shortcuts completos]]

---

## §0. Instalación y parche

### Instalación

El plugin está disponible en **Community Plugins** de Obsidian.

1. Settings → Community plugins → Browse → buscar **Cornell Marginalia**
2. Instalar y activar

### Parche obligatorio — coexistencia con Cornell Notes

Cornell Notes (`bytetiles/obsidian-cornell-notes`) y Cornell Marginalia registran el mismo bloque ` ```cornell `. Obsidian desactiva uno si los dos están activos simultáneamente.

**Parche:** editar `.obsidian/plugins/cornell-marginalia/main.js`, línea donde aparece:

```
this.registerMarkdownCodeBlockProcessor("cornell", ...)
```

Cambiar `"cornell"` por `"cornell-m"`:

```
this.registerMarkdownCodeBlockProcessor("cornell-m", ...)
```

Esto hace que Marginalia use ` ```cornell-m ` como bloque propio. Cornell Notes sigue usando ` ````cornell ` (4 backticks) sin modificación. Ambos plugins coexisten sin conflicto.

> ⚠️ **Mantenimiento:** si el plugin se actualiza desde Community Plugins, el `main.js` se sobreescribe y el parche se pierde. Reaplicar el cambio después de cada actualización.

---

## §1. Sintaxis core

### Inline — método principal

```
%%> Nota al margen derecha %%
%%< Nota al margen izquierda %%
```

Las marginalia se escriben directamente en el flujo del texto, en cualquier parte del documento. El plugin las extrae y las renderiza al margen sin ocupar espacio en el área principal.

**Ejemplo:**

```
La transformada de Laplace se define como:

$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$

%%> Ver demostración en ETN806-T03. %%

La condición de convergencia requiere que $\text{Re}(s) > \sigma_0$.
```

### Comportamiento por modo

| Modo | Visibilidad |
|---|---|
| Live Preview | ✓ Renderiza al margen |
| Reading View | ✓ Renderiza al margen (requiere toggle ON en settings) |
| Source Mode | Visible como texto plano `%%> ... %%` |

### Bidireccional

`%%>` fuerza margen derecho. `%%<` fuerza margen izquierdo. Útil para workflows de doble margen. La dirección por defecto se configura en Settings → Margin Alignment.

---

## §2. Semantic Highlighting

Añadir un prefijo al inicio del texto de la marginalia activa un color automático. Permite categorizar el tipo de anotación de un vistazo.

| Prefijo | Significado | Color por defecto |
|---|---|---|
| `?` | Pregunta / duda | 🟠 Naranja |
| `!` | Importante / examen | 🟡 Amarillo |
| `X-` | Corrección / error | 🔴 Rojo |
| `V-` | Verificado / confirmado | 🟢 Verde |

**Ejemplos:**

```
%%> ? ¿Por qué se usa Re(s) > σ₀ como condición? %%
%%> ! Definición de examen %%
%%> X- La fórmula del libro tiene un error de signo %%
%%> V- Verificado con Kreyszig p.218 %%
```

Los prefijos y colores son completamente personalizables desde **Settings → Color Tags**.

---

## §3. Grouping — Method A vs B

Por defecto, Obsidian trata párrafos, listas e imágenes como bloques separados. Esto puede causar desalineación visual entre la marginalia y el contenido al que pertenece en Reading View.

> ⚠️ Los métodos A y B **solo renderizan en Reading View**. En Live Preview se ven como texto plano o callout normal.

### Method A — Callout invisible `[!cornell]`

Para agrupar contenido mixto (párrafo + lista, párrafo + imagen) de forma liviana y sin romper el Markdown estándar.

```markdown
> [!cornell]
> %%> Nota que cubre todo el grupo %%
> Párrafo introductorio del concepto.
> - Ítem 1
> - Ítem 2
> - Ítem 3
```

El plugin oculta automáticamente el fondo, borde y título del callout. Se ve como texto normal pero la marginalia queda alineada con todo el grupo.

### Method B — Bloque `cornell-m`

Para composiciones complejas que requieren alineación exacta o exportación a PDF.

````markdown
```cornell-m
%%> Nota perfectamente alineada %%
Texto principal con alineación estricta.
- Puede contener listas
- Imágenes
- Múltiples párrafos
```
````

Crea un entorno Flexbox aislado que garantiza que texto y marginalia queden bloqueados entre sí sin importar la cantidad de contenido. Es el método recomendado para exportar a PDF.

> ⚡ **Atajo:** seleccionar texto → clic derecho → **"Insert Cornell Block"** (o Command Palette). El plugin envuelve el texto, inyecta `%%>  %%` y posiciona el cursor listo para escribir la nota.

### Cuándo usar cada método

| Situación | Método |
|---|---|
| Texto simple con lista o imagen | A — callout `[!cornell]` |
| Composición compleja o exportación PDF | B — bloque `cornell-m` |
| Marginalia inline en flujo de texto | Sintaxis directa `%%> %%` |

---

## §4. Imágenes en el margen

Para evitar conflictos con el motor Markdown de Obsidian, las imágenes en el margen usan el prefijo `img:`.

**Sintaxis:**

```
%%> img:[[nombre_imagen.png]] %%
```

Al escribir `[[`, el autocompletado nativo de Obsidian sugiere archivos del vault normalmente.

**Comportamiento:**
- La imagen escala automáticamente al ancho del margen configurado.
- Al hacer hover sobre la imagen se activa zoom de lupa para ver detalles sin ocupar espacio.

---

## §5. Marginalia Explorer

Sidebar dedicado que lista todas las marginalia del vault. Se abre desde el ribbon o con `Alt+E`.

### Tabs disponibles

| Tab | Contenido |
|---|---|
| **Current** | Solo las marginalia de la nota activa |
| **Vault** | Todas las marginalia del vault agrupadas por color |
| **Threads** | Árbol de Margin Threads conectados (ver §9) |
| **Board** | Pinboard — colección manual de notas seleccionadas |

### Funcionalidades

- **Click-to-Scroll:** hacer clic en cualquier marginalia abre el archivo y hace scroll exactamente hasta esa línea (funciona en Live Preview y Reading View).
- **Filtro por color:** clic en un color pill filtra las marginalia por su tipo semántico.
- **Hover / X-Ray:** tecla `H` sobre un ítem abre popup de contexto con el texto circundante sin abrir el archivo.
- **Drag & Drop:** arrastrar una marginalia desde el Explorer hacia un Canvas o Excalidraw crea un nodo con Block ID vinculado (ver §9).

---

## §6. Reading View

Las marginalia renderizan en Reading View con el toggle activado.

**Activar/desactivar:**
- Settings → Enable in Reading View → ON/OFF
- O desde Command Palette: `Toggle Marginalia in Reading View`

Útil para revisar una nota terminada o preparar la exportación a PDF.

---

## §7. Active Recall — Blur

Modo de estudio que oculta las marginalia para forzar la recuperación activa.

**Activación:** ícono 👁️ en el ribbon → activa Study Mode en toda la sesión.

**Cómo funciona:**
- Cualquier marginalia que termine en `;; ` se difumina (blur).
- Pasar el cursor sobre la zona borrosa revela la respuesta.
- Funciona simultáneamente en Live Preview y Reading View.

**Sintaxis:**

```
La mitocondria produce ATP. %%> ¿Qué produce la mitocondria? ;; %%
```

En Study Mode, la marginalia se muestra borrosa. El texto principal permanece visible — solo se oculta la respuesta/clave.

**Configuración relacionada:** Settings → Blur Explanatory Marginalias → ON activa que las marginalia normales en la misma línea que una flashcard también se difuminen (evita spoilers cruzados).

---

## §8. Flashcard Generator

Convierte marginalia con `;; ` en tarjetas de repaso al final de la nota.

**Flujo:**

1. Escribir la marginalia terminando en `;; `:
   ```
   %%> ¿Cuál es la condición de convergencia de la Laplace? ;; %%
   ```
2. Command Palette → **"Flashcards Generation"**
3. El plugin genera automáticamente una sección `### Flashcards` al final de la nota con todas las marginalia marcadas con `;;`.

**Resultado:**

```markdown
### Flashcards

- ¿Cuál es la condición de convergencia de la Laplace?
```

> **Uso en Galaxy:** las flashcards se generan por nota. En `supernova` se crean durante la toma de notas. En `planet` y `comet` se heredan al copiar el subtítulo completo — el `;;` se copia junto con la marginalia y el comando se puede volver a ejecutar en la nota destino para regenerar la sección Flashcards.

---

## §9. Margin Threads

Sistema Zettelkasten en los márgenes: conecta marginalia de distintas notas en árboles de pensamiento jerárquicos.

### Cómo conectar

Desde el **Marginalia Explorer → Tab Threads:**

- **Stitch Button:** conectar una marginalia de un archivo con otra de otro archivo usando el botón en el sidebar.
- **Drag & Drop:** arrastrar una marginalia y soltarla encima de otra — el plugin escribe el código de conexión automáticamente.
- **Mass Stitch:** seleccionar varios ítems con `Spacebar` → `Alt+S` para conectarlos en lote.

### Visualización

El tab **Threads** renderiza árboles jerárquicos infinitos. Seguir un concepto en profundidad a través de múltiples notas.

### Técnica subyacente

Los threads usan Block IDs nativos de Obsidian (`[[Nota#^id]]`). Las conexiones sobreviven renombrados de archivos y aparecen en el Graph View nativo.

### Hover Peek

Cuando una marginalia es parte de un thread, aparece un botón `🔗` dentro de ella. Hover sobre ese botón abre un popup de previsualización de la nota conectada sin salir de la nota actual.

**Configuración relacionada:** Settings → Semantic Stitching UI → ON para que al conectar dos notas el plugin pida una razón semántica de la conexión (ej: "miden lo mismo").

---

## §10. Doodle Engine

Canvas de dibujo flotante para adjuntar bocetos a las marginalia.

**Activar:** Command Palette → `Draw a Doodle`

Se abre un canvas flotante libre. Soporta mouse y tableta/stylus.

Al hacer clic en **"Save to Margin"**:
1. El boceto se guarda como PNG en la carpeta configurada (por defecto: `Marginalia Attachments`).
2. La sintaxis de imagen se inyecta automáticamente en la nota activa.

**Addon Super Doodle** (activable en Settings → Addons): convierte el canvas en un espacio de tamaño ajustable con navegación panorámica, colores y herramienta de selección avanzada.

---

## §11. Omni-Capture

Capturador rápido global para ideas en cualquier momento sin abrir la nota destino.

**Activar:** `Alt+C` (configurar en Settings → Hotkeys) desde cualquier parte de Obsidian.

**Funcionalidades del modal:**
- Lee el portapapeles automáticamente como contexto.
- Pegar (`Ctrl+V`) screenshots o imágenes: genera preview y guarda la imagen en el vault.
- Canvas de doodle integrado: botón "Add Doodle" para adjuntar boceto.
- Autocompletado de archivos `.md` del vault como destino.
- Recuerda el último destino usado.

**Carpeta destino por defecto:** configurada en Settings → Omni-Capture Default Folder (actualmente: `Example: 00_Inbox`).

> **Nota — uso en vault:** pendiente de configuración. Requiere evaluar integración con PDF++ antes de definir flujo definitivo. Ver lista de pendientes en §15 del sistema Galaxy.

---

## §12. PDF Export

El motor de exportación nativo de Obsidian no maneja bien las notas flotantes al margen. El plugin incluye un motor de impresión dedicado.

**Flujo de exportación (3 pasos obligatorios):**

1. **Prepare:** Command Palette → **"Prepare Marginalia for PDF Print"**
   Las marginalia `%%> %%` se convierten temporalmente a etiquetas HTML seguras para impresión.

2. **Export:** usar el exportador nativo de Obsidian (**Export to PDF**).
   Las marginalia aparecen en layout Cornell clásico de columna izquierda, con el texto principal adaptado.

3. **Restore:** Command Palette → **"Restore Marginalia after PDF Print"**
   El archivo vuelve a su estado Markdown original limpio.

> ⚠️ **Siempre ejecutar Restore después de exportar.** Si no se restaura, el archivo queda con etiquetas HTML en lugar de sintaxis Markdown.

**Method B (`cornell-m`) es recomendado para PDF** — el entorno Flexbox garantiza alineación exacta durante la exportación.

---

## §13. Shortcuts completos

### Configuración de hotkeys

Settings → Hotkeys → buscar "Cornell Marginalia" → asignar atajos personalizados.

Atajos recomendados no asignados por defecto — configurar manualmente:

| Acción | Atajo recomendado |
|---|---|
| Insert Margin Note | `Ctrl+M` |
| Toggle Study Mode (Blur) | `Ctrl+Shift+B` |
| Omni-Capture | `Alt+C` |
| Toggle Explorer | `Alt+E` |

### Comandos globales

| Atajo | Acción |
|---|---|
| `Alt+E` | Abrir/cerrar Marginalia Explorer |
| `Alt+A` | Saltar al input "Add text" del Pinboard |
| `Alt+F` | Enfocar barra de búsqueda del Explorer |
| `Alt+S` | Mass Stitch — conectar nodos seleccionados |
| `Alt+R` | Refrescar escaneo del vault |
| `Alt+1` | Tab Current |
| `Alt+2` | Tab Vault |
| `Alt+3` | Tab Threads |
| `Alt+4` | Tab Board (Pinboard) |
| `Alt+↑↓←→` | Mover nodos en el Pinboard |

### Navegación en Explorer (tabs Current y Vault)

| Atajo | Acción |
|---|---|
| `↓` / `↑` | Navegar lista de marginalia |
| `Shift+↓/↑` | Mass Pinning — anclar múltiples ítems al Board |
| `Enter` o `P` | Anclar ítem al Pinboard |
| `Ctrl+Enter` | Abrir archivo y saltar a la línea exacta |
| `Spacebar` | Seleccionar/deseleccionar para Mass Stitch |
| `H` | Hover / X-Ray — preview de contexto sin abrir archivo |
| `Esc` | Cerrar popup de hover |

### Pinboard (tab Board)

| Atajo | Acción |
|---|---|
| `Enter` (sobre nodo) | Crear nodo hermano debajo |
| `Alt+Enter` (sobre nodo) | Crear nodo hijo (indentado) |
| `Enter` (dentro del input) | Guardar y continuar en modo entrada rápida |
| `-` al inicio del texto | Define nivel de indentación (`-` = hijo, `--` = nieto) |
| `↓` / `↑` | Navegar nodos del Board |

### Omni-Capture Modal

| Atajo | Acción |
|---|---|
| `Ctrl+Enter` | Guardar captura instantáneamente |

### Insert Margin Note — comportamiento inteligente

El comando "Insert Margin Note" detecta el contexto:
- **Sin selección:** inserta `%%>  %%` y posiciona el cursor dentro.
- **Con texto seleccionado:** envuelve la selección: `%%> texto seleccionado %%`.

---

las configuraciones te las entrego en forma de texto ojo si es una extraccion  
literal si solo una aclaracion en cada opcion la utloma [] es como se puede  
configurar, [1/0] on/off, [slider] para distintos valores a escoger, [valor x/valor y] entre dos o mas valores,  
[text=MMM] texto escrito en la configuracion solo esta "MMM" sin `text=`,  
[button=nombre del boton] solo aparece "nombre del boton" no "button=".

# Cornell Marginalia Settings

## 🎨 Appearance & Rendering

### Responsive Marginalia (Auto-Collapse) [1/0]

OPTIONAL: Automatically move marginalia inside the text when the  
note pane is too narrow (e.g. when you open the sidebar).

### Responsive Threshold (px) [Slider]

Set the width at which marginalia collapses into the text.  
(Requires Auto-Collapse to be ON).

### Adaptive Width (Theme Compatibility) [1/0]

🧠 Auto-calculates margin width based on empty screen space. Turn  
ON if you are having problems with your current theme to prevent overlap.

### Margin Alignment [Left/right]

### Margin Width (%) [slider]

### Margin Distance (Offset) [slider]

Adjust how close or far the marginalia sits from the main  
text. Higher values push it outwards, lower values pull it  
inwards.

### Font Size [text=0.85em]

### Font Family [text=inherit]

### Enable in Reading View [1/0]

Shows marginalia in reading mode. Turn this off if you prefer a clean  
view.

### Extract Highlights [1/0]

OPTIONAL: Include standard text highlights (==text==) in the  
Explorer and Pinboard.

### Blur Explanatory Marginalias [1/0]

🧠 Active Recall: Blurs regular marginalias that share a line with a  
flashcard, preventing spoilers.

##🏷️ Color Tags

- Tag 1 [text=!] [seleccion de color valores RGB] [button=eliminar]
- Tag 2 [text=?] [seleccion de color valores RGB] [button=eliminar]
- Tag 3 [text=X-] [seleccion de color valores RGB] [button=eliminar]
- Tag 4 [text=V-] [seleccion de color valores RGB] [button=eliminar]
- [button=Add Tag ]

##📁 Structural Box Colors

Asigna colores EXCLUSIVAMENTE a los recuadros de los Hilos Semánticos  
(ej: [#abuelo](app://obsidian.md/index.html#abuelo)). Esto NO alterará el color de tus marginalias en el texto.

[button=Add Box Color]

##✅ Task Management

### Auto-Delete Completed Tasks [1/0]

When you check a marginalia task (- [x]), it will be permanently  
deleted from the Markdown file to keep your vault clean.

### TaskNotes HTTP API Integration [1/0]

Shows a button on task marginalias to send them directly to the  
TaskNotes plugin.

##📁 File & Output Management

### Omni-Capture Default Folder [text=Example: 00_Inbox]

Folder where new marginalia files will be  
created (leave empty for root).

### Omni-Capture Template

[text=  
  
{{citation}}  
{{image}}

{{text}}

---

]  
Define the output format for your captures.  
Use {{text}}, {{citation}}, and {{image}}. Supports  
Templater (<% %>). If you want to use Flashcard  
mode, remember to include ';;' inside your text template.

### Zettelkasten Folder [text=Zettelkasten]

Where should your ZK notes be created?  
(Leave empty for root).

### Zettelkasten Template Path [text=]

Optional: Path to a markdown file to use as a  
template (e.g., Templates/ZK.md). Supports  
{{title}}, {{date}}, {{time}}.

### Doodles Folder[text=Marginalia Attachments]

Where should your hand-drawn images  
be saved? (Leave empty for root).

### Evidence Boards Folder [text=Evidence Boards]

Where should your Canvas files be exported?

### Pinboards Folder [textPinboards]

Where should your exported Pinboard  
Markdown files go?

### Pinboards Template Path [text=]

Optional: Path to a markdown file to use as a  
template for exported Boards.

### Pinboards Item Template Path [text=]

Optional: Template for each individual  
marginalia in the board. Supports {{text}},  
{{citation}}, and {{source_note}}.

### Canvas Item Template Path [text= ]

Optional: Template for the main marginalia  
node in the Evidence Board. Supports {{text}}  
and {{source_note}}.

### ✨ Clean Exports (Remove Tags) [1/0]

Automatically strip [#tags](app://obsidian.md/index.html#tags) from notes when exporting to Pinboard,  
Canvas, or Dragging to a note.

### ✨ Clean Exports (Remove Block IDs) [1/0]

Automatically strip ^block-ids from your notes when exporting.

### Drag & Drop Template (To Note)

[text=

- {{text}} {{source_note}}  
    ]

Format used when you drag a Semantic Thread  
box directly into a Markdown note. Supports  
{{text}}, {{citation}}, {{time}} and {{source_note}}.

## ⚙️ Advanced & Exclusions

### Show Syntax in Source Mode [1/0]

If enabled, Cornell Notes will show as raw Markdown syntax when  
using Source Mode, instead of rendering visual blocks.

### Ignored Folders [text=Templates]

Comma-separated list of folders to completely ignore.

### Ignored Folders for Highlights [text=Excalidraw]

Comma-separated list of folders to ignore ONLY  
for highlights (e.g., Excalidraw, Templates).

### Ignored Highlight Texts

[text=  
⚠ Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠  
]

Comma-separated list of exact texts or fragments  
to ignore (e.g., Switch to EXCALIDRAW VIEW).

### 🔗 Semantic Stitching UI [1/0]

When connecting (stitching) notes, ask for a semantic  
reason (e.g. "miden lo mismo").

## 🛠️ Addons & Modules

### Gamification & User Profile [1/0]

Turn your marginalia into a game! Earn XP, level up, and customize  
your profile sidebar.

### Custom Explorer Background [1/0]

Add a beautiful background image to your Marginalia Explorer.

### 🌱 Time Machine & Rhizome [1/0]

Explore your marginaliae on a chronological, full-screen interactive  
canvas with spaced repetition.

### Pdf Doodle & Harvest [1/0]

Enable temporary drawing mode on PDFs.

### Super Doodle 🎨 [1/0]

Transform Zen Doodle into an adjustable-size canvas with panoramic  
navigation, colors, and an advanced selection tool.

### 🧠 Blurting Mode (1-3-7) [1/0]

Turn your Marginalia Explorer into a Spaced Repetition study deck.

### 🍅 Margidoro Engine [1/0]

Knowledge-aware Pomodoro timer. Tracks your marginalias during  
study sessions and schedules reviews.

### Anki Advanced Sync [1/0]

Syncs marginalias to Anki with bidirectional support, native images,  
and PDF++ crops.

### 🔍 Zoom & Pan Doodles [1/0]

Haz clic en cualquier imagen o doodle en tus marginalias para  
expandirla a pantalla completa con controles de zoom y paneo.

### 🚀 Dashboard:Smart Study [1/0]

Linear calendar, routines, subjects, and dynamic spaced review.

### Cornell Board 🌌 [1/0]

Activate an infinite, freeform canvas to drag, connect, and visually  
materialize marginalias.




%%
galaxy-links
[[_galaxy-system]]
[[plugin_guide]]
[[obsidian_guide]]
[[latex_guide]]
%%
