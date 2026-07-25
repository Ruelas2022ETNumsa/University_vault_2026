---
title: "Marginalia Explorer — Guía de uso"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[Marginalia_guide]]"
  - "[[cornell_guide]]"
  - "[[_marginalia_system]]"
tags: [beacon, obsidian, plugins, marginalia, explorer, infraestructura]
date_created: 2026-07-22
date_updated: 2026-07-24
status: en-progreso
---

# Marginalia Explorer — Guía de uso

> Documentación de la interfaz del panel lateral Marginalia Explorer y sus flujos de uso en Galaxy.
> Para integración Galaxy ver [[_marginalia_system]] sección A6.
> Para sintaxis del plugin ver [[Marginalia_guide]].

---

## Índice

- [[#1. Descripción de la interfaz]]
  - [[#Sección 1 — Título]]
  - [[#Sección 2 — Omni-Capture]]
  - [[#Sección 3 — Captura rápida]]
  - [[#Sección 4 — Tabs de navegación]]
  - [[#Sección 5 — Acciones]]
  - [[#Sección 6 — Búsqueda]]
  - [[#Sección 7 — Filtros]]
  - [[#Sección 8 — Panel de resultados]]
  - [[#Board — Descripción completa]]
- [[#2. Comportamiento por sección]]
- [[#3. Flujos de uso]]
  - [[#Flujo A — Explorar marginalia del archivo activo]]
  - [[#Flujo B — Explorar marginalia del vault]]
  - [[#Flujo C — Stitch (conectar notas)]]
  - [[#Flujo D — Omni-Capture]]
  - [[#Flujo E — Board (Pinboard)]]
- [[#3. Tareas pendientes de prueba]]

---

## 1. Descripción de la interfaz

### S1 DI — Título

Panel lateral con el título **"Marginalia Explorer"**. Se abre con `Alt+E` o desde el Command Palette.

---

### S2 DI — Omni-Capture

[[#Sección 2 — Omni-Capture]]
guía rápida:

| dest               | ZK                          | Clear               | Doodle              |
| ------------------ | --------------------------- | ------------------- | ------------------- |
| archivo de destino | carpeta Zettelkasten<br>1/0 | limpia portapapeles | abre ventana Doodle |

Cuatro controles para captura rápida con destino configurable:

**Campo `dest:`** — define el archivo destino de la captura. Por defecto apunta a `marginalia inbox` (archivo real en `_inbox/`). Se puede escribir directamente; tiene autocompletado por nombre de archivo (sin extensión, no busca rutas ni carpetas) y recuerda el último destino usado incluso al cerrar y reabrir Obsidian.
- Si se deja vacío y se presiona el trueno: guarda automáticamente en `marginalia inbox`.
- Si se escribe un archivo inexistente: lo crea en la raíz del vault (revisar configuración para redirigir a `_inbox/`).

**Botón `ZK`** — alterna entre modo añadir al final y modo Zettelkasten.
- **ZK OFF** (default): añade al final del archivo `dest:`. Nunca sobreescribe.
- **ZK ON**: crea una nota atómica nueva en `Zettelkasten/` usando `tpl-zk.md`.

**Botón `clear`** — limpia el portapapeles y la memoria del campo destino.

**Botón `doodle`** — abre el canvas OCD (Omni-Capture Doodle). Ver [[#Flujo — Doodle (OCD)]].

---

### S3 DI — Captura rápida

Dos controles para ingresar texto de captura:

- **Recuadro de texto** — área de escritura libre. Ícono en la esquina inferior derecha para expandir el área. Atajo de enfoque: `Alt+C` (requiere Explorer abierto).
- **Botón trueno (save capture)** — guarda la captura al archivo destino (`Ctrl+Enter`).

**Formato de salida en `dest:` (ZK OFF):**
```
%%> texto de S3 %%
contenido del portapapeles
```
- Si el portapapeles tiene texto: se appendea como texto plano debajo de la marginalia.
- Si el portapapeles tiene imagen PNG: se appendea como `![[nombre-renombrado.png]]`. El plugin de renombrado del vault renombra automáticamente (ej: `void-24-07-2026_11-45-46.png`) y guarda en `_assets/` la forma es (`nombre_en_dest-fecha-hora.extencion`).
- Si se presionó `clear` antes: solo se adjunta `%%> texto %%` sin portapapeles.
- El bloque completo se separa del contenido previo con `---`.

---

### S4 DI — Tabs de navegación

Cuatro tabs que controlan qué se muestra en la Sección 8:

| Tab       | Función                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| `current` | Muestra todas las marginalia del archivo activo, organizadas (por tag, recientes, ver [[#Sección 7 — Filtros]]) |
| `vault`   | Muestra marginalia de todo el vault respetando exclusiones configuradas                                         |
| `threads` | Muestra hilos de notas conectadas entre archivos (Zettelkasten en los márgenes)                                 |
| `board`   | Cambia el Explorer al modo Pinboard — ver [[#Board — Descripción completa]]                                     |

- `current` y `vault`— en la sección 8 se muestran las notas marginalia organizadas según [[#Sección 7 — Filtros]]. Sintaxis:(contenido , nombre del archivo , número de línea).
- `threads` — en la sección 8 se muestra las marginalias agrupadas según el #tag. Sintaxis:`\%\%> R- relacionada con Laplace #transformadas \%\%` si no tiene tag se agrupan en  "UNTAGGED"
---

### S5 DI — Acciones

Tres botones de acción:

| Botón    | Función                                                                      |
| -------- | ---------------------------------------------------------------------------- |
| `stitch` | Conectar dos marginalia entre archivos.                                      |
| `group`  | Agrupa marginalia repetidas. Puede estar activo simultáneamente con `stitch` |
| Recargar | Refresca el scan del vault/archivo en busca de nuevas marginalia             |
- `stitch`— falta detallar esta parte!!!
 Al presionar: *"Step 1: click the origin note..."* — flujo de dos pasos
 
 - `group`— agrupa notas marginalias según palabras repetidas (ej: "Entra en examen","Ecuación centra", etc), también se puede filtrar según [[#Sección 6 — Búsqueda]] y [[#Sección 7 — Filtros]].

---

### S6 DI — Búsqueda

Campo `search notes...` — filtra las marginalia mostradas en la Sección 8 en tiempo real. Atajo: `Alt+F`.

---

### S7 DI — Filtros

Botones circulares de color para filtrar por tag. Orden:

`!` `?` `X-` `V-` `C-` `F-` `R-` `T-`

Seguidos de 5 filtros especiales:
`reloj` `Libro` `Mazo de cartas` `Cerebro` `Globo de mensaje`

| Ícono            | Nombre                      | Función                                  |
| ---------------- | --------------------------- | ---------------------------------------- |
| Reloj            | Recientes                   | Muestra las marginalia más recientes     |
| Libro cerrado    | Direct PDF mode             | Activa modo PDF directo                  |
| Mazo de cartas   | Show only flashcards (`;;`) | Filtra solo marginalia con blur activado |
| Cerebro          | Active recall en PDF        | Oculta resaltados para repasar           |
| Globo de mensaje | Overlay mode                | Muestra marginalia sobre el PDF          |

> **Ordenamiento Sección 8** — el orden de las notas sigue el orden visto aca (de izquierda a derecha esta ves en sección 8 de arriba hacia abajo), colocando las marginalia sin tag en la cima.
 
> **Vault** — si esta activo este botón, aparece un botón al final (extremo derecha) el icono son 2 carpetas conectadas, (Agrupar por carpetas y archivos); al presionar este filtro se agrupa por nombre de los archivos.

>`threads`— Si esta activo este botón, aparece un botón entre `Mazo de cartas` y `cerebro`, el icono es de una hoja limpia y una flecha que le apunta al centro (horizontalmente), el nombre es "Filtrar hilos de la nota actual".

---

### S8 DI — Panel de resultados

Muestra las marginalia según los filtros activos. Orden por defecto:

`!` → `?` → `X-` → `V-` → `C-` → `F-` → `R-` → `T-`

Cada entrada muestra: contenido de la marginalia + nombre del archivo + línea. Click en cualquier entrada abre el archivo y salta a la línea exacta (funciona en Edit y Reading mode).

Navegación por teclado:

| Atajo | Función |
|---|---|
| `↓/↑` | Navegar entre notas |
| `Ctrl+Enter` | Saltar a la fuente |
| `H` | Hover/X-Ray: previsualiza el contexto sin abrir el archivo |
| `Spacebar` | Seleccionar para Stitch masivo |
| `Shift+↓/↑` | Mass pinning al Board |

---

### Board — Descripción completa

Al presionar el tab `board` el Explorer cambia a modo Pinboard. Las secciones se reorganizan:

**Sección 2** → muestra subtítulo *"active board"* en lugar de los controles de Omni-Capture.

**Sección 3** → se mantiene pero el botón trueno cambia a `+` (*add to board / Enter*).

**Sección 4** → se mantiene. El tab `board` aparece en morado, los demás en gris.

**Sección 5** → reemplazada por 7 botones de gestión del board:

| Ícono | Función |
|---|---|
| Copiar (dos rectángulos) | Copy board to clipboard |
| Descarga (flecha → `]` girado) | Import skeleton from active note |
| Punta de bolígrafo | Zen doodle mode |
| Hoja con texto | Export to markdown note |
| Canvas | Export to canvas |
| Basurero | Clear board |
| Play + "auto" | Auto-add copied text to board |

**Sección 7** → desaparece en modo board.

**Sección 8** → muestra *"Your board is empty. Paste a skeleton, add nodes, or pin notes!"* si el board está vacío.

Navegación del board por teclado:

| Atajo | Función |
|---|---|
| `↓/↑` | Navegar nodos |
| `Enter` | Insertar nodo hermano debajo |
| `Alt+Enter` | Insertar nodo hijo |
| `Alt+Flechas` | Mover nodos (Up/Down/Indent/Outdent) |
| `-`, `--`, `---` al inicio | Define nivel de indentación automáticamente |

---

## 2. Comportamiento por sección

### S1 CS — Título

### S2 CS — Omni-Capture

**Campo `dest:`**
- Si se deja vacío: guarda automáticamente en `marginalia inbox`.
- Si el archivo no existe: lo crea en la raíz del vault.
- Persiste entre sesiones de Obsidian.

**Botón `ZK`**
- **ZK OFF** — notificación: *"ZK mode: off (will append to destination)"*. Añade al final del archivo `dest:`, nunca sobreescribe.
- **ZK ON** — notificación: *"ZK mode: on (will create new notes)"*. Abre modal con campos en orden: `slug` → `materia` → `connection_type` → `partial`. Crea la nota con el template `tpl-zk.md` y genera el yaml con esos datos.
  > ⚠️ El template tiene un bug de nombramiento conocido — hay bk disponible. La corrección se hará vía script en otra sesión.

**Botón `clear`**
- Notificación: *"clipboard & memory clear"*.
- Limpia el portapapeles y resetea el campo `dest:`.
- Usar antes del trueno para evitar agregados indeseados al archivo destino.
  > ⚠️ Si no se sabe qué hay en el portapapeles, usar `clear` antes de capturar.

**Botón `doodle`** — ver [[#Sección 2 — Omni-Capture]] en Flujos.

### S3 CS — Captura rápida

### S4 CS — Tabs de navegación

### S5 CS — Acciones

### S6 CS — Búsqueda

### S7 CS — Filtros

### S8 CS — Panel de resultados

### Board

---

## 3. Flujos de uso

### Flujo A — Explorar marginalia del archivo activo

> Probado.

1. Abrir el archivo a explorar en Obsidian.
2. Abrir Explorer (`Alt+E`).
3. Presionar tab `current`.
4. Las marginalia aparecen en Sección 8 agrupadas por tag.
5. Click en cualquier entrada → salta a la línea exacta.
6. Usar filtros de Sección 7 para ver solo un tipo (ej. solo `!`).

---

### Flujo B — Explorar marginalia del vault

> Probado.

1. Abrir Explorer (`Alt+E`).
2. Presionar tab `vault`.
3. El Explorer escanea todo el vault respetando las exclusiones configuradas.
4. Usar `search notes...` (Sección 6) para filtrar por texto.
5. Usar filtros de Sección 7 para filtrar por tag.
6. Click en cualquier entrada → abre el archivo y salta a la línea.

---

### Flujo C — Stitch (conectar notas)

> Probado en sesión anterior — pendiente de redocumentar pasos exactos.

1. Presionar botón `stitch` (Sección 5).
2. *"Step 1: click the origin note..."* — hacer click en la marginalia origen en Sección 8.
3. *"Step 2: click the destination note..."* — hacer click en la marginalia destino.
4. El plugin escribe automáticamente el Block ID link entre ambas notas.
5. El hilo queda visible en el tab `threads`.

---

### Flujo D — Omni-Capture

> Pendiente de prueba.

1. Configurar destino en campo `dest:` (Sección 2).
2. Escribir el texto en el recuadro (Sección 3).
3. Opcional: agregar doodle con botón `doodle`.
4. Guardar con botón trueno o `Ctrl+Enter`.
5. La captura se appendea al archivo destino con el formato de la plantilla configurada.

---

### Flujo E — Board (Pinboard)

> Pendiente de prueba.

1. Presionar tab `board` (Sección 4).
2. Pinear notas desde `current` o `vault` con `Shift+↓/↑` o `Enter`.
3. Organizar nodos con `Alt+Flechas`.
4. Exportar con *"export to markdown note"* o *"export to canvas"*.

---

## 3. Tareas pendientes de prueba

- [ ] **EXP-01** — Verificar agrupación por tag en tab `current` con void.md de A6.
- [ ] **EXP-02** — Verificar tab `vault` con exclusiones configuradas.
- [ ] **EXP-03** — Probar `stitch`: conectar marginalia de void.md con otra de otro archivo y verificar en tab `threads`.
- [ ] **EXP-04** — Probar `group`: crear marginalia repetidas y verificar agrupación.
- [ ] **EXP-05** — Probar Omni-Capture: captura de texto simple al inbox.
- [ ] **EXP-06** — Probar Omni-Capture con doodle adjunto.
- [ ] **EXP-07** — Probar Omni-Capture modo `ZK`: verificar que crea nota atómica.
- [ ] **EXP-08** — Probar Board: pinear notas, organizar, exportar a markdown.
- [ ] **EXP-09** — Probar Board: exportar a Canvas y verificar links de Block ID.
- [ ] **EXP-10** — Probar drag & drop desde Explorer a Canvas/Excalidraw.
- [ ] **EXP-11** — Probar filtros especiales: flashcards (`;;`), active recall, overlay mode.
- [ ] **EXP-12** — Probar navegación por teclado completa (`H`, `Spacebar`, `Ctrl+Enter`).

---

%%
# galaxy-links
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_appnotes/cornell_guide.md]]
[[_app/_config/_marginalia_system.md]]
%%