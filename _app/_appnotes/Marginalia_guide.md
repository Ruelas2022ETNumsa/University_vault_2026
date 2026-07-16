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

> Plugin: [latazadehomero/marginaliaarginalia](https://github.com/latazadehomero/marginaliaarginalia) — instalado vía Community Plugins
> Versión actual: v4.9.0

---

## Índice

- [[#0. Instalación y parche]]
- [[#1. Sintaxis core]]
- [[#2. Semantic Highlighting]]
- [[#3. Grouping — Method A vs B]]
- [[#4. Imágenes en el margen]]
- [[#5. Marginalia Explorer]]
- [[#6. Reading View]]
- [[#7. Active Recall — Blur]]
- [[#8. Flashcard Generator]]
- [[#9. Margin Threads]]
- [[#10. Doodle Engine]]
- [[#11. Omni-Capture]]
- [[#12. PDF Export]]
- [[#13. Shortcuts completos]]
- [[#14. Configuración del plugin]]

---

## 0. Instalación y parche

### Instalación

El plugin está disponible en **Community Plugins** de Obsidian.

1. Settings → Community plugins → Browse → buscar **Cornell Marginalia**
2. Instalar y activar

### Parche obligatorio — coexistencia con Cornell Notes

Cornell Notes (`bytetiles/obsidian-cornell-notes`) y Cornell Marginalia registran el mismo bloque ` ```cornell ` (3 backticks por defecto). Obsidian desactiva uno si los dos están activos simultáneamente.

**Parche:** editar `.obsidian/plugins/cornell-marginalia/main.js`, línea donde aparece:

```
this.registerMarkdownCodeBlockProcessor("cornell", ...)
```

Cambiar `"cornell"` por `"marginalia"`:

```
this.registerMarkdownCodeBlockProcessor("marginalia", ...)
```

Esto hace que Marginalia use ` ```marginalia `,como bloque propio  dentro de Cornell notes puede usar 3 backicks o 4 (por defecto usa 4 con el script de python). Cornell Notes usa ` `````cornell ` (5 backticks) para contener mas bloques de códigos. Ambos plugins coexisten sin conflicto.

> ⚠️ **Mantenimiento:** si el plugin se actualiza desde Community Plugins, el `main.js` se sobreescribe y el parche se pierde. Reaplicar el cambio después de cada actualización.

---

## 1. Sintaxis core

### Inline — método principal

```
%%< Nota al margen derecha %%
%%> Nota al margen izquierda %%
```

%%> Nota al margen  izquierda %%
%%< Nota al margen derecha %%

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

## 2. Semantic Highlighting

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

%%> ? ¿Por qué se usa Re(s) > σ₀ como condición? %%
%%> ! Definición de examen %%
%%> X- La fórmula del libro tiene un error de signo %%
%%> V- Verificado con Kreyszig p.218 %%

Los prefijos y colores son completamente personalizables desde **Settings → Color Tags**.

---

## 3. Grouping — Method A vs B (se prefiere B)

Por defecto, Obsidian trata párrafos, listas e imágenes como bloques separados. Esto puede causar desalineación visual entre la marginalia y el contenido al que pertenece en Reading View.

> ⚠️ Los métodos A y B **solo renderizan en Reading View**. En Live Preview se ven como texto plano o callout normal.

### Method A — Callout invisible `[!cornell]`

Para agrupar contenido mixto (párrafo + lista, párrafo + imagen) de forma liviana y sin romper el Markdown estándar.

```markdown
> [!cornell]%%> Nota que cubre todo el grupo %%
> Párrafo introductorio del concepto.
> - Ítem 1
> - Ítem 2
> - Ítem 3
```

> [!cornell]%%> Nota que cubre todo el grupo %%
> Párrafo introductorio del concepto.
> - Ítem 1
> - Ítem 2
> - Ítem 3

El plugin oculta automáticamente el fondo, borde y título del callout. Se ve como texto normal pero la marginalia queda alineada con todo el grupo.

### Method B — Bloque `marginalia`

Para composiciones complejas que requieren alineación exacta o exportación a PDF.

````markdown
```marginalia
Texto principal con alineación estricta.  %%> Nota perfectamente alineada %%
- Puede contener listas
- Imágenes
- Múltiples párrafos
```
````

- Ejemplos

```marginalia
%%> Nota perfectamente alineada %%
MALA NOTA CORNELL!!!
Texto principal con alineación estricta.
- Puede contener listas
- Imágenes
- Múltiples párrafos
```

```marginalia
BUENA NOTA CORNELL  %%> Nota perfectamente alineada %%
Texto principal con alineación estricta.
- Puede contener listas
- Imágenes
- Múltiples párrafos
```

Crea un entorno Flexbox aislado que garantiza que texto y marginalia queden bloqueados entre sí sin importar la cantidad de contenido. Es el método recomendado para exportar a PDF.

> ⚡ **Atajo:** seleccionar texto → clic derecho → **"Insert Cornell Block"** (o Command Palette). El plugin envuelve el texto, inyecta `%%>  %%` y posiciona el cursor listo para escribir la nota.

### Cuándo usar cada método

| Situación | Método |
|---|---|
| Texto simple con lista o imagen | A — callout `[!cornell]` |
| Composición compleja o exportación PDF | B — bloque `marginalia` |
| Marginalia inline en flujo de texto | Sintaxis directa `%%> %%` |

---

## 4. Imágenes en el margen

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

## 5. Marginalia Explorer

Sidebar dedicado que lista todas las marginalia del vault. Se abre desde el ribbon o con `Alt+E`.

### Tabs disponibles

| Tab | Contenido |
|---|---|
| **Current** | Solo las marginalia de la nota activa |
| **Vault** | Todas las marginalia del vault agrupadas por color |
| **Threads** | Árbol de Margin Threads conectados (ver 9) |
| **Board** | Pinboard — colección manual de notas seleccionadas |

### Funcionalidades

- **Click-to-Scroll:** hacer clic en cualquier marginalia abre el archivo y hace scroll exactamente hasta esa línea (funciona en Live Preview y Reading View).
- **Filtro por color:** clic en un color pill filtra las marginalia por su tipo semántico.
- **Hover / X-Ray:** tecla `H` sobre un ítem abre popup de contexto con el texto circundante sin abrir el archivo.
- **Drag & Drop:** arrastrar una marginalia desde el Explorer hacia un Canvas o Excalidraw crea un nodo con Block ID vinculado (ver 9).

---

## 6. Reading View

Las marginalia renderizan en Reading View con el toggle activado.

**Activar/desactivar:**
- Settings → Enable in Reading View → ON/OFF
- O desde Command Palette: `Toggle Marginalia in Reading View`

Útil para revisar una nota terminada o preparar la exportación a PDF.

---

## 7. Active Recall — Blur

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

La mitocondria produce ATP. %%> ¿Qué produce la mitocondria?;;%%

En Study Mode, la marginalia se muestra borrosa. El texto principal permanece visible — solo se oculta la respuesta/clave.

**Configuración relacionada:** Settings → Blur Explanatory Marginalias → ON activa que las marginalia normales en la misma línea que una flashcard también se difuminen (evita spoilers cruzados).

---

## 8. Flashcard Generator

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

## 9. Margin Threads

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

## 10. Doodle Engine

Canvas de dibujo flotante para adjuntar bocetos a las marginalia.

**Activar:** Command Palette → `Draw a Doodle`

Se abre un canvas flotante libre. Soporta mouse y tableta/stylus.

Al hacer clic en **"Save to Margin"**:
1. El boceto se guarda como PNG en la carpeta configurada (por defecto: `Marginalia Attachments`).
2. La sintaxis de imagen se inyecta automáticamente en la nota activa.

**Addon Super Doodle** (activable en Settings → Addons): convierte el canvas en un espacio de tamaño ajustable con navegación panorámica, colores y herramienta de selección avanzada.

---

## 11. Omni-Capture

Capturador rápido global para ideas en cualquier momento sin abrir la nota destino.

**Activar:** `Alt+C` (configurar en Settings → Hotkeys) desde cualquier parte de Obsidian.

**Funcionalidades del modal:**
- Lee el portapapeles automáticamente como contexto.
- Pegar (`Ctrl+V`) screenshots o imágenes: genera preview y guarda la imagen en el vault.
- Canvas de doodle integrado: botón "Add Doodle" para adjuntar boceto.
- Autocompletado de archivos `.md` del vault como destino.
- Recuerda el último destino usado.

**Carpeta destino por defecto:** configurada en Settings → Omni-Capture Default Folder (actualmente: `Example: 00_Inbox`).

> **Nota — uso en vault:** pendiente de configuración. Requiere evaluar integración con PDF++ antes de definir flujo definitivo. Ver lista de pendientes en 15 del sistema Galaxy.

---

## 12. PDF Export

El motor de exportación nativo de Obsidian no maneja bien las notas flotantes al margen. El plugin incluye un motor de impresión dedicado.

**Flujo de exportación (3 pasos obligatorios):**

1. **Prepare:** Command Palette → **"Prepare Marginalia for PDF Print"**
   Las marginalia `%%> %%` se convierten temporalmente a etiquetas HTML seguras para impresión.

2. **Export:** usar el exportador nativo de Obsidian (**Export to PDF**).
   Las marginalia aparecen en layout Cornell clásico de columna izquierda, con el texto principal adaptado.

3. **Restore:** Command Palette → **"Restore Marginalia after PDF Print"**
   El archivo vuelve a su estado Markdown original limpio.

> ⚠️ **Siempre ejecutar Restore después de exportar.** Si no se restaura, el archivo queda con etiquetas HTML en lugar de sintaxis Markdown.

**Method B (`marginalia`) es recomendado para PDF** — el entorno Flexbox garantiza alineación exacta durante la exportación.

---

## 13. Shortcuts completos

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
- **Sin selección:** inserta `%%>  % %` y posiciona el cursor dentro.

- **Con texto seleccionado:** envuelve la selección: `%%> texto seleccionado %%`.

---

## 14. Configuración del plugin

> Referencia completa de Settings → Cornell Marginalia.
> `[1/0]` = toggle ON/OFF 
>  `[slider]` = valor numérico ajustable · `[Left/Right]` = selección entre opciones
>  `[text=...]` = valor actual del campo de texto.

---

### 🎨 Appearance & Rendering

#### Responsive Marginalia (Auto-Collapse) `[1/0]=1`

Mueve las marginalia dentro del texto cuando el panel de la nota es demasiado angosto (ej: al abrir el sidebar lateral).

> Sirve para evitar que las marginalia se superpongan con el contenido cuando el espacio horizontal es reducido.

#### Responsive Threshold (px) `[slider]=850`

Ancho en píxeles por debajo del cual se activa el colapso automático. Requiere Auto-Collapse ON.

> Sirve para calibrar en qué punto exacto colapsan las marginalia según el layout habitual de trabajo.

#### Adaptive Width (Theme Compatibility) `[1/0]=1`

Calcula automáticamente el ancho del margen en base al espacio libre en pantalla. Activar si el tema causa superposición visual.

> Sirve para compatibilidad con temas que tienen márgenes o sidebars propios que reducen el espacio disponible.
>
> **En Galaxy:** activar si el tema del vault genera solapamiento entre las marginalia y el contenido principal.

#### Margin Alignment `[Left / Right]=left`

Dirección por defecto del margen para todas las marginalia sin `%%<` o `%%>` explícito.

> Sirve para definir si las notas al margen aparecen a la izquierda o la derecha del texto principal de forma global.
>
> **En Galaxy:** configurado en `left` — las notas `%%<` van a la derecha, decisión visual.

#### Margin Width (%) `[slider]=30`

Ancho del margen como porcentaje del ancho total del panel de la nota.

> Sirve para controlar cuánto espacio horizontal ocupa la columna de marginalia.
>
> **En Galaxy:** ajustar para que el margen sea visible sin reducir demasiado el área de texto principal. Un valor entre 20–30% funciona bien con el layout Cornell.

#### Margin Distance (Offset) `[slider]=15`

Distancia entre el texto principal y el margen. Valores altos empujan el margen hacia afuera, valores bajos lo acercan.

> Sirve para ajuste visual fino de la separación entre texto y marginalia.

#### Font Size `[text=0.85em]`

Tamaño de fuente de las marginalia. Por defecto `0.85em` — ligeramente más pequeño que el texto principal.

> Sirve para diferenciar visualmente las notas al margen del contenido principal.
>
> **En Galaxy:** dejar en `0.85em` — la diferencia de tamaño refuerza la jerarquía visual entre nota y marginalia.

#### Font Family `[text=inherit]`

Familia tipográfica de las marginalia. `inherit` hereda la fuente del tema activo.

> Sirve para uniformar o diferenciar la tipografía de las marginalia respecto al texto principal.

#### Enable in Reading View `[1/0]=1`

Muestra las marginalia en modo lectura (Reading View).

> Sirve para ver las anotaciones al margen al revisar una nota terminada o al preparar la exportación a PDF.
>
> **En Galaxy:** ON. Necesario para el flujo de revisión de `supernova` y para exportación PDF (12).

#### Extract Highlights `[1/0]=1`

Incluye los textos con resaltado estándar (`==texto==`) en el Explorer y el Pinboard además de las marginalia.

> Sirve para centralizar en el Explorer tanto las marginalia como los highlights de Obsidian en una sola vista.

#### Blur Explanatory Marginalias `[1/0]=1`

Difumina las marginalia normales que comparten línea con una flashcard (`;;`), evitando que revelen la respuesta antes de que el usuario intente recordarla.

> Sirve para reforzar el Active Recall: la pregunta (`;;`) y la pista al margen quedan ambas ocultas hasta que el usuario hace hover.
>
> **En Galaxy:** ON si se usa el flujo de flashcards de 8. Previene spoilers cruzados al estudiar con blur activado.

---

### 🏷️ Color Tags

Define los prefijos semánticos y sus colores asociados. Cada tag tiene un texto de prefijo y un color RGB asignable. Botón **Add Tag** para agregar prefijos adicionales.

| Tag | Prefijo por defecto | Tipo |
|---|---|---|
| Tag 1 | `!` | Importante |
| Tag 2 | `?` | Pregunta |
| Tag 3 | `X-` | Error |
| Tag 4 | `V-` | Verificado |

> Sirve para categorizar visualmente las marginalia por tipo de anotación de un vistazo.
>
> **En Galaxy:** los 4 tags por defecto cubren los casos de uso del vault. No agregar tags adicionales salvo necesidad concreta. Ver 2 para uso detallado.

---

### 📁 Structural Box Colors

Asigna colores a los recuadros de los Margin Threads (9). No afecta el color de las marginalia inline. Botón **Add Box Color** para definir colores por hilo.

> Sirve para diferenciar visualmente distintos hilos temáticos en el tab Threads del Explorer.

---

### ✅ Task Management

#### Auto-Delete Completed Tasks `[1/0]`

Cuando se marca una marginalia de tarea como completada (`- [x]`), la elimina permanentemente del archivo Markdown.

> Sirve para mantener limpio el vault: las tareas completadas desaparecen sin dejar rastro en el archivo fuente.

#### TaskNotes HTTP API Integration `[1/0]`

Muestra un botón en las marginalia de tipo tarea para enviarlas directamente al plugin TaskNotes.

> Sirve para integración con TaskNotes si se usa ese plugin como gestor de tareas central.

---

### 📁 File & Output Management

#### Omni-Capture Default Folder `[text=Example: 00_Inbox]`

Carpeta donde se crean los archivos generados por Omni-Capture. Dejar vacío para guardar en la raíz del vault.

> Sirve para centralizar las capturas rápidas en un inbox antes de procesarlas.
>
> **En Galaxy:** pendiente de configuración — ver 11.

#### Omni-Capture Template

Define el formato de salida de las capturas. Soporta `{{text}}`, `{{citation}}`, `{{image}}` y sintaxis Templater (`<% %>`). Para usar flashcards, incluir `;;` dentro del template de texto.

Valor actual:
```
%%> {{text}} %%
{{citation}}
{{image}}

---
```

> Sirve para estandarizar cómo se guardan las capturas rápidas.
>
> **En Galaxy:** pendiente de configuración — ver 11.

#### Zettelkasten Folder `[text=Zettelkasten]`

Carpeta donde se crean las notas ZK generadas desde Margin Threads. Dejar vacío para raíz.

> Sirve para organizar las notas atómicas generadas desde los hilos de marginalia.

#### Zettelkasten Template Path `[text=]`

Ruta a un archivo `.md` que sirve de plantilla para las notas ZK. Soporta `{{title}}`, `{{date}}`, `{{time}}`.

> Sirve para dar estructura uniforme a las notas Zettelkasten generadas por el plugin.

#### Doodles Folder `[text=Marginalia Attachments]`

Carpeta donde se guardan los bocetos creados con el Doodle Engine (10).

> Sirve para centralizar las imágenes generadas por el canvas de dibujo.
>
> **En Galaxy:** evaluar mover a `_assets/doodles` para mantener consistencia con el sistema de attachments del vault — pendiente.

#### Evidence Boards Folder `[text=Evidence Boards]`

Carpeta donde se exportan los Canvas creados desde el Marginalia Explorer.

> Sirve para organizar los tableros de evidencia generados desde hilos de marginalia.

#### Pinboards Folder `[text=Pinboards]`

Carpeta donde se exportan los archivos Markdown del Pinboard.

> Sirve para guardar los tableros de trabajo exportados desde el tab Board del Explorer.

#### Pinboards Template Path `[text=]`

Plantilla para los archivos Markdown exportados del Pinboard.

> Sirve para dar estructura uniforme a los boards exportados.

#### Pinboards Item Template Path `[text=]`

Plantilla para cada ítem individual del Pinboard exportado. Soporta `{{text}}`, `{{citation}}`, `{{source_note}}`.

> Sirve para controlar el formato de cada marginalia dentro del board exportado.

#### Canvas Item Template Path `[text=]`

Plantilla para el nodo principal en el Evidence Board. Soporta `{{text}}` y `{{source_note}}`.

> Sirve para personalizar cómo aparece cada nodo de marginalia en el Canvas exportado.

#### ✨ Clean Exports (Remove Tags) `[1/0]`

Elimina automáticamente los `#tags` de las notas al exportar a Pinboard, Canvas o al arrastrar a otra nota.

> Sirve para exportaciones limpias sin ruido de tags.

#### ✨ Clean Exports (Remove Block IDs) `[1/0]`

Elimina automáticamente los `^block-ids` de las notas al exportar.

> Sirve para que las exportaciones no expongan los IDs internos de los Margin Threads.

#### Drag & Drop Template (To Note)

Formato usado al arrastrar un Semantic Thread box directamente a una nota Markdown. Soporta `{{text}}`, `{{citation}}`, `{{time}}`, `{{source_note}}`.

Valor actual:
```
- {{text}} {{source_note}}
```

> Sirve para controlar el formato del texto insertado al hacer drag & drop de un hilo a una nota.

---

### ⚙️ Advanced & Exclusions

#### Show Syntax in Source Mode `[1/0]=1`

Muestra la sintaxis Markdown cruda en Source Mode en lugar de renderizar los bloques visuales.

> Sirve para edición avanzada o depuración — ver el archivo fuente tal cual.

#### Ignored Folders `[text=Templates]`

Lista de carpetas separadas por coma que el plugin ignora completamente (no escanea ni renderiza marginalia en esas carpetas).

> Sirve para excluir carpetas de infraestructura del escaneo del vault.
>
> **En Galaxy:** agregar `_app,_templates,_PDF,Excalidraw` para que el plugin no procese las carpetas de sistema.

#### Ignored Folders for Highlights `[text=Excalidraw]`

Lista de carpetas ignoradas solo para highlights (`==texto==`), no para marginalia.

> Sirve para evitar que los highlights de archivos Excalidraw aparezcan en el Explorer.
>
> **En Galaxy:** dejar `Excalidraw` — los archivos `.excalidraw.md` contienen highlights internos que no son anotaciones de estudio.

#### Ignored Highlight Texts

Textos exactos o fragmentos a ignorar en la extracción de highlights.

Valor actual:
```
⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠
```

> Sirve para filtrar textos resaltados que son boilerplate de plugins y no son anotaciones reales.

#### 🔗 Semantic Stitching UI `[1/0]=1`

Al conectar dos notas con Stitch, el plugin pide una razón semántica de la conexión (ej: "miden lo mismo").

> Sirve para forzar reflexión explícita sobre por qué dos marginalia están conectadas — enriquece el Zettelkasten.
>
> **En Galaxy:** ON si se usa Margin Threads activamente para conectar conceptos entre materias.

---

### 🛠️ Addons & Modules

#### Gamification & User Profile `[1/0]`

Convierte las marginalia en un sistema de XP y niveles. Agrega perfil personalizable al sidebar.

> Sirve para motivación gamificada en el uso del plugin.

#### Custom Explorer Background `[1/0]`

Agrega una imagen de fondo al Marginalia Explorer.

> Sirve para personalización visual del sidebar.

#### 🌱 Time Machine & Rhizome `[1/0]`

Explora las marginalia en un canvas interactivo cronológico de pantalla completa con repetición espaciada.

> Sirve para revisión visual del historial de anotaciones en el tiempo.

#### Pdf Doodle & Harvest `[1/0]`

Activa el modo de dibujo temporal sobre PDFs abiertos en Obsidian.

> Sirve para anotar directamente sobre PDFs sin salir del vault.

#### Super Doodle 🎨 `[1/0]`

Amplía el Doodle Engine con canvas de tamaño ajustable, navegación panorámica, colores y herramienta de selección avanzada.

> Sirve para bocetos más complejos que requieren más espacio o herramientas de dibujo.

#### 🧠 Blurting Mode (1-3-7) `[1/0]`

Convierte el Marginalia Explorer en un deck de repetición espaciada.

> Sirve para sesiones de estudio activo directamente desde el sidebar sin abrir las notas.

#### 🍅 Margidoro Engine `[1/0]`

Pomodoro timer con awareness de marginalia. Rastrea las anotaciones durante la sesión de estudio y agenda revisiones.

> Sirve para combinar técnica Pomodoro con el sistema de marginalia en una sesión integrada.

#### Anki Advanced Sync `[1/0]`

Sincroniza las marginalia con Anki con soporte bidireccional, imágenes nativas y crops de PDF++.

> Sirve para exportar las marginalia como tarjetas Anki para repaso fuera de Obsidian.

#### 🔍 Zoom & Pan Doodles `[1/0]=1`

Clic en cualquier imagen o doodle en las marginalia para expandirla a pantalla completa con controles de zoom y paneo.

> Sirve para revisar imágenes o bocetos pequeños sin salir de la nota.
>
> **En Galaxy:** útil al usar `%%> img:[[...]] %%` con diagramas o gráficos — permite ver el detalle sin abrir el archivo de imagen.

#### 🚀 Dashboard:Smart Study `[1/0]`

Calendario lineal, rutinas, materias y repaso espaciado dinámico.

> Sirve como panel de control de estudio integrado al vault.

#### Cornell Board 🌌 `[1/0]`

Canvas infinito y de forma libre para arrastrar, conectar y materializar marginalia visualmente.

> Sirve para sesiones de síntesis visual — mapa conceptual libre construido desde las marginalia del vault.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_appnotes/plugin_guide.md]]
[[_app/_appnotes/obsidian_guide.md]]
[[_app/_appnotes/latex_guide.md]]
%%
