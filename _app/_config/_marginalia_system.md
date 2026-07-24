---
title: "Cornell Marginalia — Integración Galaxy"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[Marginalia_guide]]"
  - "[[_note-system]]"
  - "[[_template-system]]"
tags: [beacon, obsidian, plugins, infraestructura, marginalia, galaxy]
date_created: 2026-07-22
date_updated: 2026-07-23
status: activo
---

# Cornell Marginalia — Integración Galaxy

> Referencia de integración del plugin Cornell Marginalia en el Sistema Galaxy.
> Para el funcionamiento técnico del plugin ver [[Marginalia_guide]].
> Cada sección documenta: qué se probó, qué se notó, y dónde se usa en Galaxy.

> **Convención de este archivo:** los ejemplos de sintaxis se muestran
> en bloques de código fenced (\`\`\`) para evitar que el plugin los procese.
> El escape \%% se usa solo cuando la sintaxis aparece en línea dentro del texto.

---

## Índice

- [[#A1. Sintaxis core]]
- [[#A2. Semantic Highlighting]]
- [[#A3. Grouping Method A]]
- [[#A4. Grouping Method B]]
- [[#A5. Imágenes en el margen]]
- [[#A6. Marginalia Explorer]]
- [[#A7. Active Recall — Blur]]
- [[#A8. Flashcard Generator]]
- [[#A9. Margin Threads]]
- [[#A10. Doodle Engine]]
- [[#A11. Omni-Capture]]
- [[#A12. PDF Export]]
- [[#B. Configuración]]

---

## A1. Sintaxis core

> Sintaxis:
> ```
> %%> texto %%   → margen izquierdo
> %%< texto %%   → margen derecho
> ```
### Probado

- Inline izquierdo (\%%>) y derecho (\%%<) en medio de párrafo → renderiza correctamente en Live Preview y Reading View.
- Con fórmulas LaTeX dentro del margen → renderiza sin conflicto.
- Con escape `\%%`: usar `\%%>` y `\%%` en línea evita que el plugin procese la sintaxis — el texto permanece visible en el cuerpo. Para bloques de ejemplo usar fenced code (` ``` `). Convención estándar de este archivo para documentación.

### Notado

- Con escape `\%%` o bloque fenced, la sintaxis queda visible en Reading View sin ser procesada por el plugin — útil para documentación técnica (este archivo).
- Sin escape, la marginalia desaparece del cuerpo y aparece al margen — comportamiento normal de integración.
- Backticks solos (`` ` ``) no son suficientes: el contenido dentro de `%%...%%` igualmente desaparece del cuerpo en Reading View.

### Dónde se usa en Galaxy

| `galaxy_body` | Uso |
|---|---|
| `planet` / `moon` | Anotar dudas (`?`), referencias a otros planets, aclaraciones de fórmulas sin interrumpir el flujo del texto principal |
| `comet` | Marcar pasos clave de un ejercicio, errores detectados durante la resolución, observaciones del proceso |
| `supernova` | Anotaciones rápidas durante transcripción de clase — agregar contexto sin cortar el flujo bruto |
| `dwarf` | Claves de repaso al margen del resumen, referencias a planets relacionados |
| `beacon` (documentación) | Usar escape `\%%` o bloque fenced para mostrar la sintaxis como ejemplo sin que el plugin la procese |

---

## A2. Semantic Highlighting

> Sintaxis:  \%%> PREFIX- texto \%%
> Los prefijos activan color automático. Configurables en Settings → Color Tags (valores en RGB).

### Tags Galaxy

| Tag | Significado | Color | Hex | RGB |
|---|---|---|---|---|
| `!` | Importante / examen | ámbar | `#EE9B00` | 238, 155, 0 |
| `?` | Pregunta / duda | azul petróleo | `#005F73` | 0, 95, 115 |
| `X-` | Error / corrección | naranja quemado | `#BB3E03` | 187, 62, 3 |
| `V-` | Verificado | verde oliva | `#629900` | 98, 153, 0 |
| `C-` | Comentario neutro | gris antracita | `#474448` | 71, 68, 72 |
| `F-` | Fórmula clave | morado | `#5A189A` | 90, 24, 154 |
| `R-` | Relación entre materias | verde azulado | `#0A9396` | 10, 147, 150 |
| `T-` | Tarea docente | rojo | `#C1121F` | 193, 18, 31 |

> ⚠️ **`T-` es exclusivo de `supernova`** — no se copia a planet, comet ni dwarf. Los archivos derivados de supernova deben quedar limpios de tareas docentes.

### Probado

- Los 7 tags base probados en `void.md` — colores correctos en Live Preview y Reading View.
- Cada tag renderiza sin interferir con el texto circundante.

### Notado

- Los colores por defecto del plugin (naranja, amarillo, rojo, verde) fueron reemplazados por la paleta Galaxy — ingresar valores RGB en Settings → Color Tags.
- `T-` no se prueba en `void.md` — su uso queda restringido a `supernova` en contexto real.

### Dónde se usa en Galaxy

| Tag | `galaxy_body` | Uso |
|---|---|---|
| `!` | todos | Concepto de examen, definición central, fórmula que entra seguro |
| `?` | planet / comet / supernova | Duda activa durante la toma de notas o resolución |
| `X-` | comet / supernova | Error detectado en el proceso, corrección de signo o unidades |
| `V-` | planet / comet | Dato confirmado con fuente (libro, docente, ejercicio resuelto) |
| `C-` | todos | Comentario personal sin carga semántica — aclaración, contexto extra |
| `F-` | planet / moon / dwarf | Fórmula clave del tema — la ecuación central que define el concepto |
| `R-` | planet / bridge | Relación con otra materia o tema — señal para crear un `bridge` |
| `T-` | supernova únicamente | Tarea asignada por el docente — no hereda a ningún otro tipo |

---

## A3. Grouping Method A

> Sintaxis: `[!cornell]` callout

### Probado

- Párrafo simple, párrafo + lista, párrafo + imagen → descartado, no agrupa visualmente.
- Múltiples marginalia en el mismo callout → **funciona correctamente**, asigna espacio automático a cada nota.

### Notado

- **Descartado para contenido simple** — se comporta como marginalia inline, no toma el recuadro esperado.
- **Fuerte específico: múltiples marginalia.** El callout `[!cornell]` distribuye automáticamente el espacio entre notas — no requiere saltos de línea manuales a diferencia de A4.
- Complementario a A4: usar A3 cuando hay varias notas en un mismo bloque, A4 para el resto.

### Dónde se usa en Galaxy

| Caso | `galaxy_body` | Uso |
|---|---|---|
| Múltiples marginalia | planet / comet | Bloque con varias notas semánticas — el callout gestiona el espaciado automáticamente |
| Imagen + texto | planet / comet | Cuando el bloque incluye imagen — A4 no renderiza imagen correctamente |

---

## A4. Grouping Method B

> Sintaxis: bloque ` ```marginalia ` 
> Método principal de agrupación en Galaxy.

### Probado

- Párrafo simple → renderiza correctamente.
- Párrafo + lista → renderiza correctamente.
- Párrafo + imagen → renderiza correctamente.
- Párrafo + LaTeX → renderiza correctamente.
- Nota antes del texto → renderiza correctamente.
- Nota después del texto → renderiza correctamente.
- Múltiples marginalia en el mismo bloque → **requiere salto de línea entre cada elemento** para correcta alineación (se prefiere el A3 para este caso).
- Anidado dentro de bloque `cornell` (::cue / ::note) → flujo Galaxy real, renderiza correctamente.

### Notado

- **Regla de múltiples marginalia:** cada elemento con su propia marginalia debe estar separado por una línea en blanco dentro del bloque. Sin el salto, las notas se apilan o desalinean.
- **Regla del punto final:** cuando el último elemento es una lista, agregar `.` en la línea siguiente para que el último ítem tenga ancla de alineación.
- **Regla imagen:** A4 no renderiza imágenes correctamente dentro del bloque — usar A3 cuando el contenido incluye `img:[[...]]`.
- El bloque `marginalia` es superior a `[!cornell]` callout (A3) en todos los casos probados excepto imagen y múltiples marginalia.

### Dónde se usa en Galaxy

| Caso                     | `galaxy_body`         | Uso                                                                            |
| ------------------------ | --------------------- | ------------------------------------------------------------------------------ |
| Párrafo + lista          | planet / moon / dwarf | Concepto + puntos clave agrupados con nota al margen                           |
| Párrafo + LaTeX          | planet / comet        | Fórmula con sus propiedades y tag `F-`                                         |
| ~~Párrafo + imagen~~     | ~~planet / comet~~    | ~~Diagrama con referencia cruzada al margen~~                                  |
| ~~Múltiples marginalia~~ | ~~planet / comet~~    | ~~Bloque de desarrollo con varias notas semánticas — respetar salto de línea~~ |
| Anidado en `cornell`     | supernova / planet    | Flujo principal — \%%> \%% en ::cue, \%%< \%% en ::note                        |

---

## A5. Imágenes en el margen

> Sintaxis: `\%%> img:[[imagen.png]] \%%` / `\%%< img:[[imagen.png]] \%%`
> Hover zoom automático al pasar el cursor.

### Probado

- Inline izquierda → renderiza correctamente.
- Tag `C-` derecha → renderiza correctamente.
- A3 callout con imagen → renderiza correctamente.
- A4 bloque marginalia con imagen → **falla**, renderiza la imagen recortada.

### Notado

- Para imágenes en el margen usar **siempre A3** muestra imagen completa. A4 recorta la imagen.

### Dónde se usa en Galaxy

| Caso | `galaxy_body` | Uso |
|---|---|---|
| Imagen inline | planet / comet / supernova | Diagrama, gráfica o captura al margen con `img:[[...]]` |
| Imagen + comentario | planet / comet | A3 con `img:[[...]]` y tag `C-` al margen opuesto |

---

## A6. Marginalia Explorer

> Pendiente de prueba.

---

## A7. Active Recall — Blur

> Sintaxis: `;;` al final del texto de la marginalia.
> Activación: botón 👁️ **Toggle Active Recall Mode** en el ribbon.

### Probado

- Blur básico (`;;`) en margen izquierdo → renderiza correctamente en Live Preview y Reading View.
- Blur con tag semántico (`! ;;`) → renderiza correctamente.
- Blur Explanatory: pista normal + pregunta `;;` en misma línea → la pista también se difumina con setting ON.
- Blur en margen derecho (`%%<`) → renderiza correctamente.
- Múltiples blur en mismo párrafo → renderiza correctamente.
- Marginalia normal conviviendo con blur en misma línea → correcta distinción con Blur Explanatory OFF.

### Notado

- El modo se activa globalmente con el botón 👁️ **Toggle Active Recall Mode** en el ribbon — sin activarlo, ninguna marginalia se difumina.
- Hover sobre el texto borroso revela la respuesta en ambos modos.
- **Blur Explanatory Marginalias** (Settings → ON): difumina también las marginalia normales que comparten línea con una `;;`, evitando spoilers cruzados.

> [!warning] Bug visual pendiente
> En Reading View el marcador `;;` se muestra visible dentro del texto de la marginalia. En Live Preview no aparece — el blur funciona correctamente. El autor del plugin documenta que debería funcionar igual en ambos modos. Se revisará en `main.js` en una sesión futura. Por ahora se mantiene el comportamiento actual.

### Dónde se usa en Galaxy

| Caso | `galaxy_body` | Uso |
|---|---|---|
| Pregunta de repaso | dwarf / planet | Marginalia con `;;` para ocultar la respuesta clave durante el repaso |
| Pista + pregunta | dwarf | Marginalia normal como pista + `;;` en margen opuesto — Blur Explanatory ON oculta ambas |
| Active recall en flujo Cornell | dwarf / supernova | `;;` dentro de `::cue` para convertir las claves en preguntas de recuperación activa |

---

## A8. Flashcard Generator

> Comando: **"Flashcards Generation"** desde el Command Palette.
> Extrae todas las marginalia con `;;` de la nota activa y genera una sección `### Flashcards` al final.

### Probado

- Marginalia con `;;` una por línea → sección `### Flashcards` generada correctamente con formato `pregunta :: contexto`.
- Marginalia con tags semánticos (`! ;;`, `F- ;;`) → se incluyen en la sección con el tag prefijado.
- Bloque `::cue` / `::note` con `marginalia` anidado → las `;;` dentro del bloque se capturan correctamente.
- A3 callout con múltiples marginalia y `;;` → se capturan todas.
- Correr el comando dos veces → reemplaza la sección existente, no duplica.

### Notado

- El comando es un **colector**, no un generador de preguntas — extrae el texto de las `;;` que ya escribiste y los lista limpios al final.
- **Convención — una marginalia por línea:** si dos marginalia están en la misma línea dentro de un callout, el generador copia los `%%` intermedios en la tarjeta producida. No es un bug crítico, pero se evita poniendo cada marginalia en su propia línea.
- La sección generada es reutilizable: al copiar un subtítulo de `supernova` a `planet` o `comet`, el `;;` viaja con la marginalia y el comando puede volver a correrse en la nota destino.

### Dónde se usa en Galaxy

| Caso | `galaxy_body` | Uso |
|---|---|---|
| **Uso principal** | `supernova` | Las marginalia `;;` se anotan durante la transcripción de clase; correr el comando genera el mazo de repaso de esa sesión directamente en la supernova |
| Ejercicios y fórmulas de examen | `comet` | Marcar con `;;` los pasos clave, fórmulas críticas y errores frecuentes durante la resolución — el comando genera un mazo de repaso del ejercicio directamente en el comet |
| Herencia a notas derivadas | `planet` / `dwarf` | Al diseccionar la supernova, el `;;` se copia junto con la marginalia — correr el comando en la nota destino regenera la sección Flashcards allí |
| Repaso de tema | `dwarf` | Consolida todas las preguntas del resumen en una sección al final para sesión de active recall |

### Commander

- **Comando:** `Cornell Marginalia: Flashcards Generation`
- **Ícono:** `layers-2`
- **Posición sugerida:** barra de herramientas o ribbon — acceso rápido sin abrir el Command Palette
- **Uso:** correr desde cualquier nota con marginalia `;;` activa (supernova, comet, planet, dwarf)

---

## A9. Margin Threads

> Dos mecanismos distintos para conectar marginalia entre archivos: **agrupación por `#tag`** y **Stitch**.
> Visualización en el tab `threads` del Marginalia Explorer.

### Mecanismo 1 — Agrupación por `#tag`

**Sintaxis:** agregar `#nombre-grupo` dentro del texto de la marginalia.

```
%%> R- relacionada con Laplace #transformadas %%
```

**Comportamiento:**
- El plugin crea automáticamente el grupo `TRANSFORMADAS` en el tab Threads.
- Todas las marginalia con el mismo `#nombre-grupo` en cualquier archivo del vault quedan agrupadas bajo ese grupo.
- No requiere Stitch — la agrupación es automática por tag.
- El `#nombre-grupo` **no se muestra en Reading View** — es invisible en la nota renderizada. Solo visible en Live Preview (Edit mode).
- El grupo se crea en Settings → Structural Box Colors automáticamente — se le puede asignar color desde ahí o desde el botón `paint box` en el Explorer.

### Mecanismo 2 — Stitch

**Flujo:**
1. Explorer → tab `vault` o `current` → botón `stitch`
2. Click en la marginalia **origen** (padre)
3. Click en la marginalia **destino** (hijo)
4. Modal **Semantic Connection**: campo para escribir la razón de la conexión (dejar vacío = classic stitch)
5. Presionar `stitch notes`

**Sintaxis generada:**

Clásico (sin etiqueta semántica):
```
%%> ! definición base [[void2#^id]] ^czne0y %%           ← en origen
%%> R- relacionada #^id %%                               ← en destino
```

Semántico (con etiqueta):
```
%%> ! definición base [[void2#^id]] {stitch: herramienta matemática común} ^czne0y %%
```

**Comportamiento:**
- Crea jerarquía padre-hijo visible en el árbol del tab Threads.
- La etiqueta semántica aparece como texto conector entre las dos marginalia en el árbol.
- Usa Block IDs nativos de Obsidian (`^id`) — sobrevive renombrados y aparece en el Graph View.
- Sin etiqueta semántica → el grupo se llama `UNTAGGED`.
- El campo semántico del modal **no controla el nombre del grupo** — solo agrega `{stitch: texto}` como anotación.
- Para que un stitch quede dentro de un grupo nombrado, agregar `#nombre-grupo` manualmente en la marginalia origen junto con el link generado:
```
%%> ! definición base #transformadas [[void2#^id]] {stitch: herramienta matemática común} ^czne0y %%
```
- Combinando `#tag` + Stitch se obtiene lo mejor de ambos: grupo nombrado + jerarquía padre-hijo.

### Probado

- Stitch clásico entre `void.md` y `void2.md` → sintaxis correcta en ambos archivos, jerarquía visible en tab Threads.
- Stitch semántico → etiqueta `{stitch: ...}` visible entre las marginalia en el árbol.
- Agrupación por `#tag` sin stitch → grupo creado automáticamente en Threads, marginalia al mismo nivel (sin jerarquía).
- Hover Peek (botón 🔗 en la marginalia origen) → muestra tooltip con ruta del thread (`follow thread: void2^id`). En v4.9.0 es tooltip, no popup de preview como describe el README.
- Click en botón 🔗 → abre el archivo destino y salta a la línea.
- Graph View → las notas conectadas por stitch aparecen enlazadas.
- Export full tree to Board → árbol exportado al tab Board, cada marginalia con botones `←` (outdent) / `→` (indent) / `x`. Título del grupo editable con doble click desde el Board.

### Notado

- **`UNTAGGED` no es configurable** — es el identificador interno del plugin para stitches sin etiqueta semántica. Editar `#Untagged` en `data.json` o en Settings → Structural Box Colors no cambia el nombre en el Explorer — el plugin lo regenera. El workaround es siempre usar etiqueta semántica o `#tag` en la marginalia.
- **Structural Box Colors** (Settings): solo controla el color del grupo, no el nombre. El nombre del grupo se define exclusivamente por el `#tag` en la marginalia. El `paint box` del Explorer asigna color al grupo y lo registra en `data.json`.
- El `#tag` agrupador y el tag semántico (`R-`, `!`, etc.) coexisten en la misma marginalia sin conflicto.
- Drag & Drop y Mass Stitch (`Spacebar` + `Alt+S`) — no probados, considerados de uso avanzado no prioritario para Galaxy en esta fase.

### Convención Galaxy

**Cuándo usar `#tag` (agrupación temática):**
Para marcar marginalia de distintas notas que pertenecen al mismo concepto transversal — sin jerarquía explícita.
```
%%> R- relacionada con Fourier #transformadas-integrales %%
```

**Cuándo usar Stitch (conexión explícita):**
Para conectar una marginalia de una nota con su continuación o consecuencia directa en otra nota — con jerarquía padre-hijo.

**Nomenclatura de grupos Galaxy:**
- Usar kebab-case: `#transformadas-integrales`, `#circuitos-rc`, `#errores-frecuentes`
- Grupos por tema transversal, no por materia (para eso están los tags `R-`)
- Evitar `UNTAGGED` — siempre usar `#tag` o etiqueta semántica

### Dónde se usa en Galaxy

| Mecanismo        | `galaxy_body`      | Uso                                                                                            |
| ---------------- | ------------------ | ---------------------------------------------------------------------------------------------- |
| `#tag` agrupador | planet / bridge    | Marcar marginalia del mismo concepto en notas de materias distintas — señal visual de relación |
| `#tag` agrupador | comet / dwarf      | Agrupar errores frecuentes o fórmulas clave recurrentes entre parciales                        |
| Stitch+agrupador | planet → planet    | Conectar la definición base de un concepto con su desarrollo en otra nota                      |
| Stitch+agrupador | supernova → planet | Conectar la transcripción bruta con la nota procesada que la disecciona                        |

---

## A10. Doodle Engine

> Dos motores de dibujo: **OCD** (Omni-Capture Doodle) y **SuperDoodle** (Zen Doodle del Board).
> Ambos guardan el PNG en `assets/` y crean nota vía `tpl-zk.md`.

### OCD — Omni-Capture Doodle

**Triggers:**
- Comando `Cornell Marginalia: Open Sidebar Doodle Canvas`
- Explorer → botón `doodle` (sección Omni-Capture)

**Interfaz (4 secciones):**
- Botón cerrar (esquina superior derecha)
- Título "Omni-capture Doodle"
- Recuadro de dibujo libre (click izquierdo, derecho y rueda — sin zoom)
- 6 botones en la base: izquierda → lápiz / borrador / reset · derecha → cancel / attach / trueno

**Flujo probado:**
1. Dibujar en el recuadro
2. Presionar `attach` → notificación según trigger:
   - Comando: `"doodle in memory! press 'trueno' in the sidebar to save"` — el trueno a presionar está en el sidebar
   - Explorer: `"doodle attached! press 'trueno' to save"` — el trueno está en el mismo Explorer
3. Presionar trueno → pide slug, materia, connection\_type, partial (campos de `tpl-zk.md`)
4. Crea nota ZK en `Zettelkasten/` con nombre de timestamp (`20260723151036.md`) + PNG en `assets/`

### SuperDoodle — Zen Doodle del Board

**Flujo de acceso:**
Explorer → tab `board` → botón `zen doodle mode`

**Interfaz (7 secciones):**
- Título "Marginalia Explorer"
- Subtítulo "active board"
- Recuadro de texto + botón `+`
- Tabs (current / vault / threads / board)
- Barra de herramientas: ← return / hand / bolígrafo / borrador / lasso · selector de resolución (1x / 2x / 4x / 8x) · selector de grosor · paleta (negro, rojo, azul, verde)
- 3 botones de guardado: basurero (clear) / `attach to board` / `omni-capture`
- Recuadro de dibujo

**Botones de guardado probados:**
- `basurero` → borra el dibujo (reset)
- `attach to board` → guarda PNG en `assets/` con nombre `superdoodle_YYYYMMDD_HHMMSS` + lo muestra en el Board del Explorer. Notificación: `"superdoodle attach to board"`
- `omni-capture` → pide slug, materia, connection\_type, partial (vía `tpl-zk.md`) → crea nota ZK en `Zettelkasten/` con timestamp

### Notado

- OCD es canvas simple sin herramientas — útil para bocetos rápidos.
- SuperDoodle es canvas completo (resolución, grosor, colores, lasso) — útil para diagramas más elaborados.
- Ambos motores usan `tpl-zk.md` para el guardado final — el formulario (slug, materia, etc.) es infraestructura Galaxy, no del plugin.
- La diferencia entre los dos triggers de OCD está en la notificación: "in memory" (comando) vs "attached" (Explorer) — el resultado final es idéntico.
- El archivo ZK generado puede incluir contenido del portapapeles si hay algo copiado al momento de guardar — es el campo `{{citation}}` del Omni-Capture leyendo el clipboard automáticamente. Limpiar el portapapeles antes de guardar si no se quiere ese contenido.
- `tpl-zk.md` fue modificado: se comentó `tp.file.rename(slug)` para evitar que el archivo activo sea renombrado al guardar el doodle.

### Dónde se usa en Galaxy

| Caso | Motor | `galaxy_body` | Uso |
|---|---|---|---|
| Boceto rápido al margen | OCD | planet / comet / supernova | Diagrama o esquema simple para adjuntar a una nota activa |
| Diagrama elaborado | SuperDoodle | planet / comet | Canvas con colores y resolución alta para diagramas complejos |
| Boceto vinculado al Board | SuperDoodle → attach to board | cualquiera | Agregar imagen al Pinboard para síntesis visual |

---

## A11. Omni-Capture

> Activación: `Alt+C` (nombre oficial del comando: **Focus Omni-Capture Input**) — enfoca el recuadro de captura en el sidebar del Marginalia Explorer.
> Requiere que el Explorer esté abierto (`Alt+E` primero).

### Dos modos

**ZK ON** (botón `ZK` activo — notificación: *"ZK mode: on (will create new notes)"*)
→ trueno → formulario `tpl-zk.md` (slug, materia, connection_type, partial) → crea nota nueva en `Zettelkasten/` con nombre timestamp.

**ZK OFF** (botón `ZK` desactivado — notificación: *"ZK mode: off (will append to destination)"*)
→ trueno → appendea al archivo configurado en `dest:` sin preguntar nada.

### Probado

- `Alt+C` sin Explorer abierto → no hace nada.
- `Alt+C` con Explorer abierto → enfoca el recuadro de texto (Sección 3).
- ZK ON → texto del recuadro + clipboard automático → crea nota en `Zettelkasten/` con timestamp.
- ZK OFF → texto del recuadro convertido a `%%> texto %%` + clipboard como `{{citation}}` → appendea a `dest:` separado por `---`.
- Clipboard de texto → capturado automáticamente como `{{citation}}`.
- Clipboard de imagen → capturada y appendeada junto al texto.
- Appendeo sin borrar contenido previo — agrega al final separado por `---`.
- Campo `dest:` → recuerda el último destino usado; tiene buscador con autocompletado de archivos del vault (escribir `inbox` muestra todas las opciones disponibles).
- Doodle integrado (botón `doodle` en Sección 2) → cubierto por A10.

### Notado

- El "modal flotante" descrito en el README del plugin no existe en v4.9.0 — el Omni-Capture es el panel de captura integrado en el Explorer (Secciones 2 y 3).
- ZK OFF appendea el texto **como marginalia inline** (`%%> %%`), no como texto plano — el contenido queda listo para ser procesado por el plugin.
- El clipboard se captura automáticamente al guardar — limpiar portapapeles antes si no se quiere ese contenido como `{{citation}}`.
- `_inbox/` está excluido de los Ignored Folders del plugin (B6) — las capturas ahí no aparecen en el tab `vault` del Explorer.

### Convención Galaxy — destino

| Caso | `dest:` | Carpeta |
|---|---|---|
| Captura durante clase de ETN901 | `ETN901-inbox.md` | `_inbox/` |
| Captura sin materia específica | `inbox.md` | `_inbox/` |
| Nota atómica (ZK ON) | — | `Zettelkasten/` |

**Reglas:**
- Una nota `ETNXXX-inbox.md` por materia activa dentro de `_inbox/`.
- `inbox.md` para capturas sin materia o contexto cruzado.
- `_inbox/` excluido del scanner del Explorer — no contamina el tab `vault`.
- Los archivos en `_inbox/` son **material sin procesar** — se revisan y se diseccionan en notas Galaxy cuando corresponda.
- Screenshots y doodles → siempre a `_assets/`, sin excepción. No van al inbox.
- `Marginalia Inbox.md` (raíz) eliminado — reemplazado por esta convención.

### Dónde se usa en Galaxy

| Caso | ZK | `galaxy_body` destino | Uso |
|---|---|---|---|
| Captura rápida en clase | OFF | `_inbox/ETNXXX-inbox.md` | Idea, pregunta o fragmento que no se puede desarrollar en el momento |
| Captura sin contexto de materia | OFF | `_inbox/inbox.md` | Pensamiento genérico, referencia cruzada, pendiente |
| Nota atómica con doodle | ON | `Zettelkasten/` | Boceto + contexto que se convertirá en bridge o asteroid |

---

## A12. PDF Export

> Flujo: **Prepare → Export → Restore** vía Command Palette.
> Exportador: **Better Export PDF** (plugin instalado) — soporta activación de CSS snippets.

### Flujo probado

1. `Ctrl+P` → `Cornell Marginalia: Prepare Marginalia for PDF Print` — las `%%> %%` se convierten a HTML de print.
2. Exportar con Better Export PDF (`Ctrl+P` → `Better Export PDF: Export Current File to PDF`).
3. `Ctrl+P` → `Cornell Marginalia: Restore Marginalia after PDF Print` — el archivo vuelve al Markdown original.

### Probado

- Marginalia inline simples (`%%> %%`, `%%< %%`) en párrafo → exportan correctamente con layout de columna izquierda.
- Tags semánticos con colores → se preservan en el PDF.
- Prepare + Restore → el archivo vuelve limpio al formato original.

### Notado

- **Bloques `cornell` (::cue / ::note) no se exportan correctamente** — el Prepare convierte el bloque externo a HTML pero el contenido interno no renderiza en layout Cornell dentro de Better Export PDF. Los `::cue` y `::note` aparecen como texto plano. Limitación conocida por choque entre Cornell Notes y Cornell Marginalia en el motor de print.
- **Convención Galaxy para export:** usar solo marginalia inline simples (`%%> %%`) en notas destinadas a exportar. Evitar bloques `cornell` y bloque `marginalia` anidado en notas que se van a imprimir.
- Correr el comando **Flashcards Generation después del Restore**, nunca durante el estado de Prepare — el Prepare inyecta IDs temporales en el texto que contaminan las tarjetas generadas.

### Dónde se usa en Galaxy

| Caso | `galaxy_body` | Uso |
|---|---|---|
| Resumen de parcial imprimible | `dwarf` | Exportar el resumen con marginalia al margen en layout Cornell para estudio en papel o tablet |
| Ejercicio para revisión | `comet` | Exportar con pasos clave y fórmulas visibles al margen |

---

## B. Configuración

> Pendiente de revisión.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_config/_note-system.md]]
[[_app/_config/_template-system.md]]
%%
