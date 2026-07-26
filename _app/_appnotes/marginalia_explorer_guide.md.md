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
  - [[#S1 DI — Título]]
  - [[#S2 DI — Omni-Capture]]
  - [[#S3 DI — Captura rápida]]
  - [[#S4 DI — Tabs de navegación]]
  - [[#S5 DI — Acciones]]
  - [[#S6 DI — Búsqueda]]
  - [[#S7 DI — Filtros]]
  - [[#S8 DI — Panel de resultados]]
- [[#2. Comportamiento por sección]]
  - [[#S2 CS — Omni-Capture]]
  - [[#S3 CS — Captura rápida]]
  - [[#S4 CS — Tabs de navegación]]
    - [[#S4 CS — Board]]
  - [[#S5 CS — Acciones]]
  - [[#S6 CS — Búsqueda]]
  - [[#S7 CS — Filtros]]
  - [[#S8 CS — Panel de resultados]]
  - [[#Board]]
- [[#3. Flujos de uso]]
  - [[#Flujo A — Explorar marginalia del archivo activo]]
  - [[#Flujo B — Explorar marginalia del vault]]
  - [[#Flujo C — Stitch (conectar notas)]]
  - [[#Flujo D — Omni-Capture]]
  - [[#Flujo E — Board (Pinboard)]]
- [[#4. Tareas pendientes de prueba]]

---

## 1. Descripción de la interfaz

### S1 DI — Título

Panel lateral con el título **"Marginalia Explorer"**. Se abre con `Alt+E` o desde el Command Palette.

---

### S2 DI — Omni-Capture
[[#Sección 2 — Omni-Capture]]

guía rápida:

| dest               | ZK (Toogle Zettelkasten mode) | Clear (Clear clipboard  & memory) | Doodle (Attach doodle) |
| ------------------ | ----------------------------- | --------------------------------- | ---------------------- |
| archivo de destino | carpeta Zettelkasten<br>1/0   | limpia portapapeles               | abre ventana Doodle    |

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
[[#S3 CS — Captura rápida]]

guía rápida:

| Recuadro de texto       | Trueno (save capture)        |
| ----------------------- | ---------------------------- |
| área de escritura libre | guarda la captura en `dest:` |

**Recuadro de texto** — área de escritura libre. Ícono en la esquina inferior derecha para expandir (arrastrando). Atajo de enfoque: `Alt+C` (requiere Explorer abierto con `Alt+E` primero).

**Botón trueno** — guarda la captura al archivo destino (`Ctrl+Enter`).

---

### S4 DI — Tabs de navegación
[[#S4 CS — Tabs de navegación]]

guía rápida:

| Tab | Tooltip | Función |
| --- | --- | --- |
| `current` | en archivo abierto | marginalia del archivo activo |
| `vault` | en todo el baúl | marginalia de todo el vault |
| `threads` | hilos | hilos entre archivos |
| `board` | your pinboard | modo Pinboard |

**`current`** — muestra todas las marginalia del archivo activo en S8, organizadas según [[#S7 DI — Filtros]]. Cada entrada se ve así:
```
nota_marginalia (arriba izquierda)     nombre_archivo · línea (abajo derecha)
```

**`vault`** — muestra marginalia de todo el vault respetando exclusiones configuradas. Misma visualización que `current`.

**`threads`** — muestra las marginalia agrupadas por `#tag`. Ejemplo de marginalia con tag:
```
%%> R- relacionada con Laplace #transformadas [[void 2#^v5f86v]] {stitch: estos se conectan con stitch masivo}  ^rsm3t9 %%
```
Las marginalia sin tag se agrupan bajo `UNTAGGED`.

**`board`** — cambia el Explorer a modo Pinboard. Reorganiza la interfaz completa:

#### Board (modo Pinboard)

Al activar `board` las secciones se reorganizan:
- **S2** → muestra subtítulo *"active board"* en lugar de controles Omni-Capture.
- **S3** → se mantiene pero el trueno cambia a `+` (*add to board / Enter*).
- **S4** → se mantiene. Tab `board` en morado, los demás en gris.
- **S5** → reemplazada por 7 botones de gestión:

| Ícono | Tooltip | Función |
|---|---|---|
| Copiar (dos rectángulos) | Copy board to clipboard | copia el board al portapapeles |
| Descarga (flecha → `]` girado) | Import skeleton from active note | importa esqueleto de la nota activa |
| Punta de bolígrafo | Zen doodle mode | abre modo doodle zen |
| Hoja con texto | Export to markdown note | exporta a nota markdown |
| Canvas | Export to canvas | exporta a canvas |
| Basurero | Clear board | limpia el board |
| Play + "auto" | Auto-add copied text to board | añade automáticamente texto copiado |

- **S7** → desaparece.
- **S8** → muestra *"Your board is empty. Paste a skeleton, add nodes, or pin notes!"* si está vacío.

Navegación del board por teclado:

| Atajo | Función |
|---|---|
| `↓/↑` | Navegar nodos |
| `Enter` | Insertar nodo hermano debajo |
| `Alt+Enter` | Insertar nodo hijo |
| `Alt+Flechas` | Mover nodos (Up/Down/Indent/Outdent) |
| `-`, `--`, `---` al inicio | Define nivel de indentación automáticamente |
---

### S5 DI — Acciones
[[#S5 CS — Acciones]]

Tres botones de acción:

| Botón     | Tooltip               | Función                                                                        |
| --------- | --------------------- | ------------------------------------------------------------------------------ |
| `stitch`  | Connect two notes     | Conecta dos marginalia entre archivos. Flujo de dos pasos.                     |
| `group`   | Group identical notes | Agrupa marginalia con contenido idéntico. Puede estar activo junto con stitch. |
| ↺ (ícono) | Refresh data          | Refresca el scan del vault/archivo activo. Acción instantánea.                 |

**`stitch`** — al presionar aparece un recuadro destacado en S8 indicando el paso actual. Flujo de dos pasos: seleccionar origen → seleccionar destino. Ver [[#S5 CS — Acciones]] para el comportamiento completo.

**`group`** — reordena S8 por número de línea y agrupa marginalia con contenido idéntico, sin importar tag-class ni presencia de Block ID. Compatible con los filtros de [[#S7 DI — Filtros]] y [[#S6 DI — Búsqueda]].

**Refresh** (↺) — solo ícono, sin tooltip visible. Recarga los datos del tab activo. Acción momentánea: el botón vuelve a estado apagado inmediatamente.

---

### S6 DI — Búsqueda
[[#S6 CS — Búsqueda]]

Campo de búsqueda con forma:
```
[🔍 search notes...]
```
Filtra las marginalia mostradas en S8 en tiempo real. Atajo: `Alt+F` (previo explorer debe estar abierto `Alt+E`). No disponible en el tab `board` (el campo desaparece).

---

### S7 DI — Filtros
[[#S7 CS — Filtros]]

| Filtro                | Tooltip / Significado           | Color           | Botón requerido |
| --------------------- | ------------------------------- | --------------- | --------------- |
| `!`                   | Importante / examen             | ámbar           | —               |
| `?`                   | Pregunta / duda                 | azul petróleo   | —               |
| `X-`                  | Error / corrección              | naranja quemado | —               |
| `V-`                  | Verificado                      | verde oliva     | —               |
| `C-`                  | Comentario neutro               | gris antracita  | —               |
| `F-`                  | Fórmula clave                   | morado          | —               |
| `R-`                  | Relación entre materias         | verde azulado   | —               |
| `T-`                  | Tarea docente                   | rojo            | —               |
| Reloj                 | Recientes                       | —               | —               |
| Libro cerrado         | Direct PDF mode                 | —               | —               |
| Mazo de cartas        | Show only flashcards (`;;`)     | —               | —               |
| Hoja + flecha         | Filtrar hilos de la nota actual | —               | `threads`       |
| Cerebro               | Active recall en PDF            | —               | —               |
| Globo de mensaje      | Overlay mode                    | —               | —               |
| 2 carpetas conectadas | Agrupar por carpetas y archivos | —               | `vault`         |

---

### S8 DI — Panel de resultados
[[#S8 CS — Panel de resultados]]

Muestra las marginalia según los filtros activos. Orden por defecto:

`sin tag` → `!` → `?` → `X-` → `V-` → `C-` → `F-` → `R-` → `T-` → imágenes → blur (`;;`)

Cada entrada muestra:
```
[nota marginalia (izquierda)                          ]
[                              nombre_archivo · L# (derecha)]
```

Al pasar el cursor: aparece un punto en el extremo derecho (sin tooltip) que al presionarlo envía la marginalia al Board. Notificación: *"added to board"*. También aparece hover con preview de la nota.

Navegación por teclado:

| Atajo | Función |
|---|---|
| `↓/↑` | Navegar entre notas |
| `Ctrl+Enter` | Saltar a la fuente |
| `H` | Hover/X-Ray: previsualiza el contexto sin abrir el archivo |
| `Spacebar` | Seleccionar para Stitch masivo |
| `Shift+↓/↑` | Mass pinning al Board |

---



## 2. Comportamiento por sección

### S2 CS — Omni-Capture
[[#S2 DI — Omni-Capture]]

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
[[#S3 DI — Captura rápida]]

**Formato de salida en `dest:` (ZK OFF):**
```
%%> texto del recuadro [[void 2#^v5f86v]] {stitch: estos se conectan con stitch masivo}  ^i6l0rf %%
contenido del portapapeles
---
```
- El separador `---` se agrega al final de cada captura (configurable).
- Si el portapapeles tiene texto: se añade como texto plano debajo de la marginalia.
- Si el portapapeles tiene imagen PNG: se añade como `![[nombre-renombrado.png]]`. El plugin de renombrado renombra automáticamente con formato `nombre_dest-fecha-hora.extension` y guarda en `_assets/`.
- Si se presionó `clear` antes: solo se añade `%%> texto  ^dazf59 %%` sin portapapeles.

**Drag & drop S8 → S3 (copiar al recuadro):**

Al arrastrar una marginalia de S8 al recuadro, se genera automáticamente un Block ID en el archivo fuente. El ID se crea con solo el acto de jalar, sin necesidad de soltar en el recuadro.

- **Marginalia simple:**
```
%%>! Entra en examen ^rxnisv%%
```

- **Grupo simple:**
```
[[void 2#^uqakdh|Group: ¿Qué forma tiene la ROC para señales causales?]]
```

- **Threads (desde tab `threads`):**
```
# UNTAGGED
- nota marginalia padre [[archivo1#^ltla01]]
	- nota marginalia hilo [[archivo2#^rxnisv]]
```
Se respeta la jerarquía padre-hilo con indentación.

**Drag & drop S8 → S8 (crear thread):**

Al arrastrar una marginalia sobre otra dentro de S8:
- La nota arrastrada se convierte en **hilo**, la nota destino en **padre**.
- Notificación inmediata: *"stitching 1 thread(s)..."*
- Notificación de éxito: *"Threads successfully connected! (press Ctrl+Shift+Z to undo)"*
- Sin tag: ambas notas se agrupan bajo `UNTAGGED` en el tab `threads`.

### S4 CS — Tabs de navegación
[[#S4 DI — Tabs de navegación]]

**`current`**
- El Explorer NO se actualiza automáticamente al cambiar de archivo. Requiere presionar **Refresh data** (S5).
- Cada entrada tiene un círculo en el extremo derecho — al presionarlo se marca y envía la marginalia al Board. Notificación: *"added to board"*.
- Al pasar el cursor sobre una entrada: hover con preview del contenido de la nota (no del archivo completo).
- Click en una entrada: abre el archivo y salta a la línea exacta.

**`vault`**
- Escaneo instantáneo. Si no aparecen marginalia esperadas, presionar Refresh data.
- Tiene un filtro exclusivo: **Agrupar por carpetas y archivos** (tooltip: *agrupar por carpetas y archivos*, ícono: dos carpetas conectadas). Al activarlo:
  - Archivos en la raíz se muestran agrupados como archivos.
  - Archivos en carpetas se agrupan bajo el nombre de la carpeta (ej: todo lo de `Zettelkasten/` aparece bajo `Zettelkasten`).
  - Aparece botón **Export full tree to board** (cuadrado azul con círculo blanco) para exportar todo el árbol al Board.
- Sin el filtro de agrupación: comportamiento igual a `current` con círculo individual por nota.

**`threads`**
- Al pasar el cursor: hover con preview del contenido (igual que `current`).
- Click en una entrada: abre el archivo y salta a la línea.
- Entre nota padre e hilo se muestra el tipo de conexión: ícono de cadena (2 argollas) + nombre del `connection_type` asignado en el Stitch.
- Cada grupo de tag tiene botón **Export full tree to board** (cuadrado azul con círculo blanco) para exportar todo el grupo.
- Las notas internas del grupo tienen círculo individual para exportar al Board una por una.

**`board`** — ver [[#S4 CS — Board]].

> [!note] Atajos de tab
> `Alt+1` = `current` · `Alt+2` = `vault` · `Alt+3` = `threads` · `Alt+4` = `board`
> Requieren `Alt+E` previo para que el Explorer esté abierto y con foco.

#### S4 CS — Board

**Agregar texto plano desde S3:**
- Escribir texto en el recuadro y presionar `+`. Se agrega al Board como nodo simple:
```
[texto plano                              x]
```

**Notas exportadas individualmente:**
```
[(color tag) marginalia #tag de carpeta       <> x]
                                nombre_archivo · línea
```
- `<` = outdent, `>` = indent (reorganizar jerarquía). No tienen efecto visible confirmado.
- `x` = elimina la nota del Board.

**Notas exportadas agrupadas (vault + agrupar / threads):**
```
UNTAGGED    x
[NOTA PADRE ...                    <> x]
              nombre_archivo · línea
  [nota hilo ...                   <> x]
                nombre_archivo · línea
```
- La indentación refleja la jerarquía padre-hilo del Stitch.
- Sin Stitch: no hay niveles, todas las notas quedan al mismo nivel.
- El tipo de conexión (cadena + connection_type) visible en `threads` **no aparece** en el Board.

### S5 CS — Acciones
[[#S5 DI — Acciones]]

> [!note] Dos tipos de tag en el plugin
> El plugin maneja dos tipos de tag independientes que pueden coexistir en la misma marginalia:
> - **tag-class** — prefijo de color que clasifica el tipo de marginalia (`!`, `?`, `X-`, `V-`…). Controla color y filtro en S7.
> - **tag-group** — agrupador de Threads (`#nombre`). Controla la carpeta del árbol en el tab `threads`.
> Ejemplo: `%%> ! Esto es importante #transformadas %%` tiene tag-class `!` y tag-group `#transformadas`.

**Estado visual de los botones:**
- **Activo** — fondo morado (color del tema), letras blancas.
- **Apagado** — fondo gris, letras blancas.
- `current`, `vault`, `threads` y `board` son mutuamente excluyentes.
- `stitch` y `group` son independientes entre sí y pueden estar ambos activos simultáneamente.
- **Refresh** (↺) es acción instantánea: se presiona, recarga, y vuelve a apagado.

---

**Caso 1 — solo Refresh (0 · 0 · 1)**

Presionar Refresh actualiza S8 con las marginalia actuales del tab activo. No activa ningún modo. Útil al cambiar de archivo con `current` activo, ya que el Explorer no se actualiza automáticamente al cambiar de pestaña.

---

**Caso 2 — solo stitch activo (1 · 0 · 0)**

Flujo de conexión en dos pasos:

1. Presionar `stitch` — aparece recuadro destacado en **morado** en S8: *"Step 1: click the ORIGIN note..."*
2. Click en la marginalia **padre** (origen) — el recuadro cambia a **verde claro**: *"Step 2: click the DESTINATION note..."*
3. Navegar al archivo del hilo si es necesario (cambiar pestaña + Refresh).
4. Click en la marginalia **hilo** (destino) — aparece ventana emergente:
   - Título: *"semantic connection (how is 'archivo1' related to 'archivo2')"*
   - Campo de texto para escribir el tipo de conexión.
   - Botones: `[cancel]` / `[stitch notes]`
5. Presionar `[stitch notes]` — la ventana se cierra y aparecen dos notificaciones:
   - *"stitching 1 notes"*
   - Indicación para deshacer: `to undo : Ctrl+Shift+Z`

**Resultado en los archivos:**
```
void 1 (padre): texto original [void 2 > ^id](void 2#^id) {stitch: tipo_conexión}
void 2 (hilo):  texto original ^id
```

**Resultado en `threads`:**
```
[UNTAGGED]
  [marginalia padre                    void 1 · línea]
    ⛓ tipo_conexión
  [marginalia hilo                     void 2 · línea]
```
Si ambas marginalia tienen el mismo tag-group, se agrupan bajo esa carpeta en lugar de `UNTAGGED`.

**Deshacer (`Ctrl+Shift+Z`):**
- Padre → vuelve al texto original sin residuos.
- Hilo → conserva el `^id` como único residuo.

**Alternativa — drag & drop S8 → S8 (sin ventana emergente):**

Desde el tab `vault`, arrastrar una marginalia sobre otra crea el stitch directamente sin pedir tipo de conexión:
- Nota arrastrada = **hilo**, nota destino = **padre**.
- Notificaciones: *"stitching 1 thread(s)..."* → *"Threads successfully connected! (press Ctrl+Shift+Z to undo)"*
- Si ambas comparten tag-group, el árbol de `threads` las reorganiza bajo la misma carpeta con jerarquía padre → hilo (no duplica la carpeta).
- Deshacer: igual que el flujo con ventana — padre limpio, hilo conserva `^id`.

---

**Caso 3 — solo group activo (0 · 1 · 0)**

- S8 se reordena por **número de línea** (posición en el archivo activo) en lugar del orden por tag-class.
- Las marginalia con contenido idéntico se **agrupan visualmente**, mostrando todas sus apariciones con archivo y línea:
```
[marginalia z          void 2 · L47
                       void 2 · L68]
```
- La agrupación es por **contenido exacto**, independiente de tag-class y de si alguna tiene Block ID.
- tag-group no interfiere en la agrupación de `group` — eso es territorio del tab `threads`.
- `group` activo en el tab `threads` no produce cambio visible (comportamiento no confirmado con suficientes datos).

---

**Caso 4 — stitch + group simultáneos (1 · 1 · 0)**

- El flujo de stitch es idéntico al caso 2.
- El ordenamiento de S8 durante el flujo es por número de línea (igual que group solo).
- La agrupación por contenido idéntico se mantiene activa mientras se seleccionan origen y destino.

### S6 CS — Búsqueda
[[#S6 DI — Búsqueda]]

Disponible en `current`, `vault` y `threads`. Desaparece en `board`.

Se puede combinar con los filtros de S7 activos — ambos se aplican simultáneamente.

Términos de búsqueda soportados:
- **Palabra o frase** — filtra por contenido de la marginalia.
- **tag-group** (`#nombre`) — filtra por el tag de agrupación de Threads.
- **`!`** — filtra marginalia que contienen imágenes embebidas (`![[imagen.xxx]]`).

### S7 CS — Filtros
[[#S7 DI — Filtros]]

**Tag-class** (`!` `?` `X-` `V-` `C-` `F-` `R-` `T-`) — al activar un filtro S8 muestra solo las marginalia de ese tipo. Se pueden combinar con S6 (búsqueda) y con `group` (S5).

**Reloj (Recientes)** — muestra las marginalia más recientes del tab activo.

**Libro cerrado (Direct PDF mode)**
- ON — notificación: *"modo pdf directo: activado"*
- OFF — notificación: *"modo pdf directo: desactivado"*
- Comportamiento exacto pendiente de prueba en PDF.

**Mazo de cartas (Show only flashcards `;;`)** — filtra y muestra solo las marginalia con blur activado (`;;`). Útil para repaso de tarjetas tipo examen.

**Cerebro (Active recall en PDF)**
- ON — notificación: *"active recall pdf: activado (pasa el ratón para revelar bloque completo)"*
- OFF — notificación: *"active recall pdf: desactivado"*
- Comportamiento exacto pendiente de prueba en PDF.

**Globo de mensaje (Overlay mode)**
- ON — notificación: *"hover mode: on"*
- OFF — notificación: *"hover mode: off"*
- Comportamiento exacto pendiente de prueba en PDF.

**2 carpetas conectadas (Agrupar por carpetas y archivos)** — disponible con `vault` activo. Agrupa S8 por archivo o carpeta:
- Archivos en raíz: `[nombre_archivo (N)]` donde N = cantidad de marginalia. Desplegable muestra las N marginalia.
- Archivos en carpeta: se agrupan bajo el nombre de la carpeta, ej. `[_projects]` → `[tsk_alx-rul (1)]`.

**Hoja + flecha (Filtrar hilos de la nota actual)** — disponible con `threads` activo. Filtra S8 mostrando solo los padres e hilos que pertenecen al archivo abierto.

### S8 CS — Panel de resultados
[[#S8 DI — Panel de resultados]]

**`current` y `vault`**

Ordenamiento por defecto según tag-class (ver [[#S7 DI — Filtros]]). Con `group` activo: se reordena por número de línea de menor a mayor; en `vault` prioriza el orden de línea a través de todos los archivos.

Click en una entrada: abre el archivo y salta a la línea exacta (Edit y Reading mode).

`Spacebar` sobre una entrada: la marca con marco azul para Mass Stitch. Ver [[#Flujo C2 — Mass Stitch (teclado)]].

> [!note] Métodos equivalentes — Pin to board
> `P` = `Enter` = `Shift+↓/↑` = `Menu key + Enter` — todos envían la marginalia enfocada al Board.
> `H` — abre hover/X-Ray de la marginalia enfocada sin abrir el archivo.
> `Ctrl+Enter` — no funciona en v4.9.0. Usar click directo para saltar a la fuente.

---

**`threads`**

Ordenamiento sin filtros: no confirmado. Las marginalia se agrupan por tag-group:

```
[nombre-tag-group]
[marginalia 1          nombre_archivo · L#]
[marginalia 2          nombre_archivo · L#]
```

Para padres e hilos (con stitch):
```
[nombre-tag-group]
[marginalia padre       nombre_archivo · L#]
  [marginalia hilo      nombre_archivo · L#]
```

Al pasar el cursor sobre el nombre del tag-group aparecen 3 botones a la derecha:

| Botón | Función |
|---|---|
| Pin (ícono pin) | Pin to top |
| Paleta de puntos | Paint box (saves to settings) |
| Cuadrado azul + círculo blanco | Export full tree to board |

Al presionar **Export full tree to board**: notificación *"[nombre-tag-group] fue exportada a board"*.

---

**Resultado en Board tras exportar desde `threads`:**

```
nombre-tag-group-1                    x
[marginalia                       ← → x]
nombre-tag-group-2                    x
[marginalia                       ← → x]
```

- Las notas pierden la jerarquía padre-hilo — todas quedan al mismo nivel.
- Las notas nuevas agregadas posteriormente se suman al final del grupo correspondiente.
- Tooltips de los botones por nota: `←` = outdent · `→` = indent · `x` = eliminar.
- Indent agrega un nivel de sangría a la nota (hasta ~15 niveles confirmados).

### Board
[[#S4 DI — Tabs de navegación]]

**Botones de gestión (los 7):**

---

**1. Copy board to clipboard**
- Notificación: *"mindmap copiado, ve a excalidraw y presiona ctrl+v"*
- Copia el board al portapapeles en formato lista markdown:
```
- [[archivo#^id|texto]]
	-  %%> texto ^id %%
```
- Cada nota incluye su Block ID link y la marginalia raw indentada debajo.
- En Excalidraw (`Ctrl+V`): los links funcionan como accesos directos a la nota origen.
- El indent aplicado en el board **sí se refleja** en la jerarquía de la lista copiada.

---

**2. Export to markdown note**
- Notificación: *"pinboard compiled successfully"*
- Crea archivo nuevo en `Pinboards/Pinboard_YYYY-MM-DD_HH-MM-SS.md` (carpeta automática).
- Formato del archivo:
```
# ● Pinboard Session
*Exported on: YYYY-MM-DD HH:MM*

---

texto de la marginalia

*— 🔗 [[archivo#^id|archivo]]*

---
```
- El tag-class (`!`, `?`, `F-`, `R-`…) **no aparece** — solo el texto limpio.
- El indent del board **no se refleja** — el archivo siempre aplana todo al mismo nivel.

---

**3. Export to canvas**
- Crea archivo nuevo en `Evidence Boards/EvidenceBoard_YYYY-MM-DD_HH-MM-SS.canvas` (carpeta automática distinta a `Pinboards/`).
- Cada nota = nodo tipo `text` con formato:
```
**Marginalia:**
texto

[[archivo#^id|🔗 Origin]]
```
- Color de nodo: morado (`"4"` en Canvas de Obsidian) para todas las notas.
- El tag-class **no aparece** — solo el texto limpio.
- El indent **sí afecta** el canvas:
  - Sin indent → todos los nodos en la misma columna (`x: 450`), sin edges.
  - Con indent → cada nivel desplaza el nodo en el eje X (`+450px` por nivel) y genera edges de izquierda a derecha conectando el nodo indentado con su padre.

---

**4. Zen doodle mode**
- Lanza la interfaz **SuperDoodle** (no el OCD de Omni-Capture — motores distintos).
- El lienzo **persiste** entre visitas — no se limpia al presionar "return to board".
- Interfaz de izquierda a derecha:

| Control | Tooltip | Función |
|---|---|---|
| `[←]` | Return to board | Vuelve al board sin borrar el lienzo |
| Mano | Hand tool (pan) | Paneo horizontal. Se activa con `Ctrl` si Pen está seleccionado |
| Pluma | Pen | Dibuja con cualquier botón del ratón (izq, der, rueda) |
| Goma | Eraser | Borra por área según grosor del slider (no borra trazos completos) |
| Rectángulo segmentado | Lasso / select tool | Selecciona área rectangular y permite arrastrarla |
| Selector de lienzo | `8x` / `4x` / `2x` / `1x` | Redimensiona el lienzo (default: `4x`). Se puede cambiar en código |
| Slider | — | Controla el grosor del trazo |
| 4 círculos de color | — | Selección de color del trazo. Configurables en código |
| Basurero | Clear canvas | Borra todos los trazos — lienzo desde cero |
| Pin + *attach to board* | Save and add to pinboard | Guarda el PNG en `_assets/superdoodle_YYYYMMDD_HHMMSS.png` y lo agrega al board |
| Trueno + *omni-capture* | Save instantly to omni-capture destination | Inyecta en `dest:` la marginalia `%%> img:[[doodle_...png]] %%` + contenido del portapapeles como `![[clip_...png]]` + `---` |

**Nodo doodle en el board:**
- Se muestra como texto plano con el nombre del archivo PNG (no renderiza imagen, sin miniatura).
- Sin hover/preview. Doble click → editable como texto.
- No tiene click-to-origin (a diferencia de las notas de texto).

**Nota sobre dest: en Zen doodle:** el destino de omni-capture está atado al último `dest:` confirmado desde S3. Para cambiarlo: hacer un envío previo desde S3 con el nuevo destino → luego volver a Zen doodle.

---

**5. Clear board**
- Notificación: *"board cleaned"*
- Borra todas las notas y doodles del board de forma instantánea.
- Sin confirmación previa. Irreversible.

---

**6. Import skeleton**
- Notificación: *"imported N skeleton nodes"*
- Importa la **estructura** de la nota activa como nodos del board. No importa marginalia.
- Extrae:
  - Headings (`#`, `##`, `###`…) — con jerarquía visual: `#` aparece en letras grandes y moradas (color del tema), subniveles en texto normal.
  - Listas con `- ` (guion) — incluyendo las del YAML frontmatter.
- **No** extrae listas numeradas (`1.`).
- **No** extrae marginalia `%%> %%`.
- **No** crea nodo raíz con el nombre del archivo.
- Caso especial: `%%# texto%%` también es capturado por tener sintaxis de heading del plugin.
- Uso previsto: importar el outline de la nota y luego pinear marginalia encima para armar un mindmap organizado por secciones.

---

**7. Auto-add copied text**
- Toggle con dos estados:
  - **ON** — notificación: *"auto-paste ON! copy text to see it appear"*
  - **OFF** — notificación: *"auto-paste desactivated"*
- Con el toggle ON: cualquier texto copiado al portapapeles se agrega automáticamente al board. Notificación por cada pegado: *"text auto-pasted"*.
- Todo llega como **texto plano** — sin formato, sin Block ID links, sin tag-class.
  - Marginalia `%%> texto %%` → texto plano.
  - Imágenes `![[img.png]]` → texto plano.

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

#### Flujo C1 — Stitch individual (UI)

> Probado.

1. Presionar botón `stitch` (Sección 5).
2. *"Step 1: click the origin note..."* — hacer click en la marginalia origen en Sección 8.
3. *"Step 2: click the destination note..."* — hacer click en la marginalia destino.
4. El plugin escribe automáticamente el Block ID link entre ambas notas.
5. El hilo queda visible en el tab `threads`.

---

#### Flujo C2 — Mass Stitch (teclado)

> Probado.

1. Abrir Explorer (`Alt+E`). Tab `current` o `vault` activo.
2. Navegar con `↓/↑` hasta la primera marginalia a conectar.
3. Presionar `Spacebar` — la marginalia se marca con marco azul (sin notificación). Repetir para cada marginalia adicional en cualquier orden.
4. La **última** marginalia seleccionada con `Spacebar` será el **hilo único** de todas las anteriores (que serán padres).
5. Presionar `Alt+S` — aparece ventana emergente pidiendo el tipo de conexión (único para todos los pares).
6. Escribir el tipo de conexión y confirmar.
7. Resultado en `threads`: cada padre queda conectado al hilo con el tipo de conexión entre ambos.

```
# UNTAGGED
* m1
   * [tipo de conexión]
   * m_último (hilo)
* m2
   * [tipo de conexión]
   * m_último (hilo)
* m3
   * [tipo de conexión]
   * m_último (hilo)
```

> [!warning] Limitación de navegación por teclado
> Las flechas `↓/↑` para navegar en S8 **no funcionan** con el botón `group` activo ni en el tab `threads`. Funcionan correctamente en `current` y `vault` sin `group`, incluyendo con `stitch` activo.

---

### Flujo D — Omni-Capture

> Pendiente de prueba.

1. Configurar destino en campo `dest:` (Sección 2).
2. Escribir el texto en el recuadro (Sección 3).
3. Opcional: agregar doodle con botón `doodle`.
4. Guardar con botón trueno o `Ctrl+Enter`.
5. La captura se appendea al archivo destino con el formato de la plantilla configurada.

> Probado. Ver documentación completa en [[_marginalia_system]] → A11.

---

### Flujo E — Board (Pinboard)

> Probado.

1. Presionar tab `board` (`Alt+4`).
2. Pinear notas desde `current` o `vault`: hover sobre la nota → punto derecho, o `Shift+↓/↑`.
3. Organizar jerarquía con botones `←` (outdent) y `→` (indent) por nota, o `Alt+Flechas`.
4. Exportar:
   - `Copy to clipboard` → pegar en Excalidraw con `Ctrl+V`.
   - `Export to markdown` → genera `Pinboards/Pinboard_fecha.md`.
   - `Export to canvas` → genera `Evidence Boards/EvidenceBoard_fecha.canvas`.
5. Limpiar con `Clear board` (instantáneo, sin confirmación).

---

### Flujo F — Drag & drop a Canvas

> Probado.

Dos métodos con comportamientos distintos.

**Método 1 — Drag directo S8 → Canvas**

1. Abrir canvas vacío en panel principal. Explorer visible en sidebar con tab `current` o `vault` activo.
2. Arrastrar una marginalia de S8 al canvas.
3. Se genera automáticamente un Block ID en el archivo fuente (si no tenía). Una vez creado, el ID es inmutable.
4. El canvas recibe **un único recuadro** con todo el contenido en markdown plano:
   - Marginalia simples: `texto [[archivo#^id]]`
   - Imágenes (`img:[[...]]`): `[[archivo#^id|Group: ![[_assets/imagen.png]]]]` — la imagen sí renderiza dentro del recuadro.
   - Grupos desde `threads` (drag por nombre de tag-group): markdown plano con jerarquía indentada, sin conexiones visuales.
5. Desde tab `vault`: comportamiento idéntico; solo cambia el nombre del archivo en el link.
6. También funciona soltando sobre una **nota markdown** abierta — el contenido se inserta como texto plano con el mismo formato.

> ⚠️ Todo el contenido draggeado llega en un solo recuadro. No genera conexiones visuales ni cajas individuales por nota.
> ✅ Conserva la jerarquía completa (incluyendo padres sin tag-group que se perderían en export to board).

**Método 2 — Export to board → Export to canvas** *(recomendado)*

1. Desde `threads`, presionar **Export full tree to board** (recuadro azul + círculo blanco al hover sobre el tag-group).
2. Verificar en board que todas las notas llegaron: el punto derecho pintado indica presencia en board.
3. Si alguna nota falta (ej. padre sin conexión al tag-group): ir a `threads`, encontrarla individualmente, presionar su punto derecho para agregarla al board manualmente.
4. Reordenar en board si es necesario (`Alt+Flechas` o botones `←` `→`).
5. Presionar **Export to canvas** → genera `Evidence Boards/EvidenceBoard_fecha.canvas`.
6. El canvas muestra nodos individuales con conexiones visuales (edges) y caja adicional con el texto de contexto de línea donde vive la marginalia.

> ⚠️ La conexión semántica del stitch (tipo de conexión) **no se exporta** al canvas.
> ⚠️ Padres sin tag-group pueden no llegar por export masivo — verificar y agregar manualmente desde paso 3.
> ✅ Mejor para visualización: nodos separados, edges, contexto de línea visible.

---

## 4. Tareas pendientes de prueba

- [x] **EXP-01** — Verificar agrupación por tag en tab `current` con void.md de A6.
- [x] **EXP-02** — Verificar tab `vault` con exclusiones configuradas.
- [x] **EXP-03** — Probar `stitch`: conectar marginalia de void.md con otra de otro archivo y verificar en tab `threads`.
- [x] **EXP-04** — Probar `group`: crear marginalia repetidas y verificar agrupación.
- [ ] **EXP-05** — Probar Omni-Capture: captura de texto simple al inbox.
- [ ] **EXP-06** — Probar Omni-Capture con doodle adjunto.
- [ ] **EXP-07** — Probar Omni-Capture modo `ZK`: verificar que crea nota atómica.
- [x] **EXP-08** — Probar Board: pinear notas, organizar, exportar a markdown.
- [x] **EXP-09** — Probar Board: exportar a Canvas y verificar links de Block ID.
- [x] **EXP-10** — Probar drag & drop desde Explorer a Canvas/Excalidraw.
- [x] **EXP-11** — Probar filtros especiales: flashcards (`;;`), active recall, overlay mode.
- [x] **EXP-12** — Probar navegación por teclado completa (`H`, `Spacebar`, `Ctrl+Enter`).

---

%%
# galaxy-links
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_appnotes/cornell_guide.md]]
[[_app/_config/_marginalia_system.md]]
%%