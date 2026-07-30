---
title: Sistema de Plantillas — University Vault
galaxy_body: beacon
scope: vault
tool: templater
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_mindmap-system]]"
  - "[[_note-system]]"
  - "[[_pdf_pp-system]]"
  - "[[_TAB_note-system]]"
  - "[[_ToDo-system]]"
tags:
  - beacon
  - templater
  - plantillas
  - infraestructura
date_created: 2026-05-28
date_updated: 2026-07-18
status: activo
---

# Sistema de Plantillas — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Convención de notas: [[_note-system]]
> Sistema PDF: [[_pdf_pp-system]]
> Pendientes: [[_ToDo-system]]
> Archivos físicos: `_templates/`

Este documento define el sistema de plantillas del vault. Todas las plantillas usan **Templater** y siguen la convención del Sistema Galaxy.

---

## Idea central

Cada tipo de cuerpo galaxy tiene su plantilla en `_templates/`. Al crear una nota nueva, el usuario usa el botón del ribbon para abrir el selector de Templater, elige la plantilla correspondiente, y responde las preguntas de ruta. Templater completa el YAML, inserta la fecha del día, mueve el archivo a la carpeta correcta y posiciona el cursor en el cuerpo.

---

## Inventario de plantillas

| Archivo                | `galaxy_body`   | Carpeta destino                                                           | Creación                                                 |
| ---------------------- | --------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| `tpl-star.md`          | `star`          | `MOC/`                                                                    | Automático                                               |
| `tpl-planet.md`        | `planet`        | `Semesters/.../Topic_NN.../`                                              | Automático (Opción B)                                    |
| `tpl-moon.md`          | `moon`          | `Semesters/.../Topic_NN.../`                                              | Automático (Opción B)                                    |
| `tpl-comet.md`         | `comet`         | `Semesters/.../Topic_NN.../`                                              | Automático (Opción B)                                    |
| `tpl-nebula.md`        | `nebula`        | `Semesters/.../Topic_NN.../`                                              | Automático (Opción B)                                    |
| `tpl-dwarf.md`         | `dwarf`         | `Semesters/.../Partial_N/`                                                | Automático (Opción B)                                    |
| `tpl-asteroid.md`      | `asteroid`      | Normal: `Semesters/.../Topic_NN.../` / PDF: `Semesters/.../Partial_N/`    | Automático (Opción B) — pregunta tipo al inicio          |
| `tpl-photon.md`        | `photon`        | `desmos`/`tikzjax`: `Semesters/.../Topic_NN.../` / `pdf-crop`: `_assets/` | Automático — pregunta tipo al inicio                     |
| `tpl-bridge.md`        | `bridge`        | `Semesters/Materia1-Materia2/`                                            | Automático (Opción B)                                    |
| `tpl-constellation.md` | `constellation` | `Excalidraw/Constellations/`                                         | Automático                                               |
| `tpl-observatory.md`   | `observatory`   | `Excalidraw/Observatory/`                                            | Automático                                               |
| `tpl-supernova.md`     | `supernova`     | `Semesters/.../Partial_N/`                                                | Automático — pregunta tipo al inicio (class / fusionada) |
| `tpl-w-initial.md`       | `workshop` | `Semesters/Sem_NN/ETNXXX/`              | Automático — pregunta materia y semestre                        |
| `tpl-w-transcription.md` | `workshop` | `Semesters/Sem_NN/ETNXXX/Partial_N/`   | Automático — pregunta materia, semestre, parcial y nro de temas |
| `tpl-w-study.md`         | `workshop` | `Semesters/Sem_NN/ETNXXX/Partial_N/`   | Automático — pregunta materia, semestre y parcial               |
| `tpl-w-project.md`       | `workshop` | `Semesters/Sem_NN/ETNXXX/Partial_N/`   | Automático — pregunta materia, semestre, parcial y slug         |


**Automático (Opción B)** = Templater pregunta materia, semestre, parcial, tema y nombre. Mueve el archivo a la ruta correcta automáticamente.
**Automático** = Templater pide solo el nombre y mueve el archivo a la carpeta fija correspondiente.

> `tsk_tpl.md` no es una plantilla de Templater — es un archivo de referencia en `_projects/`. Se copia y pega manualmente en el slot `tsk_alias.md` correspondiente. Incluye comentarios `%%` explicativos en cada sección.

### Preguntas por plantilla

| Archivo                  | Preguntas al crear                                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `tpl-planet.md`          | Materia, semestre, parcial, tema, nombre                                                                          |
| `tpl-moon.md`            | Materia, semestre, parcial, tema, nombre                                                                          |
| `tpl-comet.md`           | Materia, semestre, parcial, tema, nombre                                                                          |
| `tpl-nebula.md`          | Materia, semestre, parcial, tema, nombre                                                                          |
| `tpl-dwarf.md`           | Materia, semestre, parcial, nombre                                                                                |
| `tpl-asteroid.md`        | Materia, semestre, parcial, tipo (Normal/PDF); si PDF: número de tema + nombre; si Normal: tema + nombre          |
| `tpl-photon.md`          | Materia, semestre, parcial, tipo (desmos/tikzjax/pdf-crop); si pdf-crop: nombre; si otro: nombre + tema           |
| `tpl-bridge.md`          | Materia 1, materia 2, nombre                                                                                      |
| `tpl-constellation.md`   | Nombre                                                                                                            |
| `tpl-observatory.md`     | Nombre                                                                                                            |
| `tpl-supernova.md`       | Materia, semestre, parcial, tipo (class/fusionada); si class: número + fecha; si fusionada: número de tema + slug |
| `tpl-w-initial.md`       | Materia, semestre                                                                                                 |
| `tpl-w-transcription.md` | Materia, semestre, parcial, cantidad de temas del parcial                                                         |
| `tpl-w-study.md`         | Materia, semestre, parcial                                                                                        |
| `tpl-w-project.md`       | Materia, semestre, parcial, slug del proyecto (español, guion_bajo)                                               |

### Respaldo Opción A

Las plantillas originales (sin lógica de movimiento) están consolidadas en `_templates/alt-B/plantillas-A-respaldo.md` como referencia.

---

## Configuración de Templater

### Folder Templates activos

| Carpeta | Plantilla |
|---------|-----------|
| `Excalidraw/Constellations` | `_templates/tpl-constellation` |
| `Excalidraw/Observatory` | `_templates/tpl-observatory` |

> Importante: la ruta de la plantilla en Folder Templates se escribe **sin extensión `.md`**. Usar el selector de archivo de Templater, no escribir la ruta a mano.

### Carpetas ignoradas en file creation

`_templates`, `_app/_config`, `_app/_appnotes`, `borrar`

---

## Configuración de Commander

### Botón en Ribbon

| Botón                      | Comando                                    | Notas                                         |
| -------------------------- | ------------------------------------------ | --------------------------------------------- |
| Crear nota desde plantilla | `Templater: Create new note from template` | Abre selector — el usuario elige la plantilla |

> Se usa un solo botón en el ribbon que abre el selector de Templater. El usuario elige la plantilla correcta. Esto evita saturar el ribbon con un botón por tipo.

---

## Comportamiento de las plantillas tpl-constellation y tpl-observatory

Estas dos plantillas son especiales: generan archivos que Obsidian abre como lienzos de Excalidraw, no como notas de texto. Para lograrlo combinan tres partes:

1. **Lógica Templater** — pide el nombre del archivo y lo mueve a su carpeta destino
2. **YAML híbrido** — incluye `excalidraw-plugin: parsed` (requerido por el plugin) junto con los campos galaxy
3. **Cuerpo comprimido** — bloque `compressed-json` con el lienzo vacío inicial

````markdown
<%*
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
await tp.file.move("Excalidraw/Constellations/" + title);
%>---
excalidraw-plugin: parsed
tags: [excalidraw, galaxy-constellation]
galaxy_body: constellation
...
---
==⚠  Switch to EXCALIDRAW VIEW...==

## Drawing
```compressed-json
N4IgLg...
```
%%
galaxy-links

%%
````

> El campo `excalidraw-plugin: parsed` debe ser el primero del YAML — el plugin lo busca al abrir el archivo. Sin él, Obsidian abre el archivo como nota de texto normal.

> Los archivos se guardan como `.excalidraw.md` dentro del vault. Esto mantiene compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar un archivo en excalidraw.com, exportar desde el plugin con el comando "Export as .excalidraw".

> El bloque `<%* ... %>` puede aparecer visible al inicio de la nota si Templater no lo limpia del cuerpo — es cosmético y no afecta el funcionamiento.

---

## Variables Templater usadas

| Variable | Qué hace |
|----------|----------|
| `<% tp.file.title %>` | Inserta el nombre del archivo como título |
| `<% tp.date.now("YYYY-MM-DD") %>` | Inserta la fecha de creación |
| `<%* tp.file.cursor() %>` | Posiciona el cursor al abrir la nota |
| `<%* tp.system.prompt("...") %>` | Abre cuadro de texto para capturar input del usuario |
| `<%* tp.file.move(path) %>` | Mueve el archivo a la ruta construida dinámicamente |

---

## Plantillas YAML de referencia

### Notas galaxy

Plantillas para notas de contenido académico — teoría, ejercicios, transcripciones, referencias y visuales. Viven en `Semesters/` organizadas por materia, parcial y tema. Cada tipo corresponde a un `galaxy_body` del sistema galaxy.

#### tpl-star

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: star
subject: 
semester: 
partial: 
topic: 
topic_name: 
orbiting: []
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

#### tpl-planet

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: planet
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
star: ""
moons: []
comets: []
tags: [<% subject %>, galaxy-planet, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

---

#### tpl-moon

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: moon
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
orbits: ""
tags: [<% subject %>, galaxy-moon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

---

#### tpl-comet

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: comet
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
source: ""
concepts_used: []
status: pendiente
tags: [<% subject %>, galaxy-comet, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

---

#### tpl-nebula

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: nebula
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
session_date: <% tp.date.now("YYYY-MM-DD") %>
comets: []
tags: [<% subject %>, galaxy-nebula, P<% partial %>]
---
```

---

#### tpl-dwarf

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: dwarf
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
covers: []
tags: [<% subject %>, galaxy-dwarf, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

---

#### tpl-asteroid

Dos ramas según tipo — la plantilla pregunta al inicio cuál es.

**Rama Normal** (va a `Topic_NN.../`):
```yaml
---
title: "<% tp.file.title %>"
galaxy_body: asteroid
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
orbiting: []
tags: [<% subject %>, galaxy-asteroid, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: en-proceso
---
```

**Rama PDF** (va a `Partial_N/` directamente):
```yaml
---
title: "<% tp.file.title %>"
galaxy_body: asteroid
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: <% tnum %>
source_type: 
source_title: ""
source_author: ""
source_chapter: ""
pdf_file: ""
related_planets: []
tags: [<% subject %>, galaxy-asteroid, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: en-proceso
---
```

> Para YAML extendido de asteroid con PDF ver [[_pdf_pp-system]].

---

#### tpl-photon

Tres tipos — la plantilla pregunta al inicio cuál es.

**`desmos` / `tikzjax`** (va a `Topic_NN.../`):
```yaml
---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: <% photonType %>
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
attached_to: ""
tags: [<% subject %>, galaxy-photon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

**`pdf-crop`** (va a `_assets/`):
```yaml
---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: pdf-crop
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
source_pdf: ""
source_page: 
attached_to: ""
tags: [<% subject %>, galaxy-photon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

> `photon_type` válidos: `desmos` | `tikzjax` | `pdf-crop`. No incluye Excalidraw — para eso usar `tpl-constellation` o `tpl-observatory`.

---

#### tpl-bridge

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: bridge
subjects: [<% subject1 %>, <% subject2 %>]
semesters: []
connects: []
tags: [galaxy-bridge, <% subject1 %>, <% subject2 %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

---

#### tpl-constellation

```yaml
---
excalidraw-plugin: parsed
tags: [excalidraw, galaxy-constellation]
galaxy_body: constellation
title: "<% tp.file.title %>"
subject: 
semester: 
partial: 
topic: 
scope: partial
tools: [excalidraw, mindmap-builder]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> `excalidraw-plugin: parsed` debe ir primero — el plugin lo requiere para abrir el archivo como lienzo.
> `scope`: `partial` si cubre el parcial completo | `topic` si cubre un solo tema.
> Carpeta destino: `Excalidraw/Constellations/` — movimiento automático por Templater.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

---

#### tpl-observatory

```yaml
---
excalidraw-plugin: parsed
tags: [excalidraw, galaxy-observatory]
galaxy_body: observatory
title: "<% tp.file.title %>"
subject: 
semester: 
partial: 
topic: 
attached_to: ""
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

> `excalidraw-plugin: parsed` debe ir primero — el plugin lo requiere para abrir el archivo como lienzo.
> Carpeta destino: `Excalidraw/Observatory/` — movimiento automático por Templater.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

---

#### tpl-supernova

Dos variantes según ciclo de vida — la plantilla pregunta al inicio cuál es.

**Class individual** (`ETNXXX-classNNN-PN-mesdía.md`, va a `Partial_N/`):
```yaml
---
title: "<% title %>"
galaxy_body: supernova
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
class_number: <% classNum %>
class_date: <% tp.date.now("YYYY-MM-DD") %>
subtopics:
  - ""
related_planets: []
tags: [<% subject %>, galaxy-supernova, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: en-proceso
---
```

**Supernova fusionada** (`ETNXXX-TN-slug_del_tema-PN.md`, va a `Partial_N/`):
```yaml
---
title: "<% title %>"
galaxy_body: supernova
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
topic_name: 
class_parts:
  - ""
related_planets: []
tags: [<% subject %>, galaxy-supernova, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: completo
---
```

> Ver [[_TAB_note-system]] para el ciclo de vida completo y [[_galaxy-system]] para la convención de nombres.

---

### Workshop

Plantillas para seguimiento de tareas académicas por materia — no son notas de contenido sino archivos de gestión. Viven en `Semesters/` pero a nivel de materia o parcial, no de tema. Todas usan `galaxy_body: workshop`.

#### tpl-w-initial

```yaml
---
title: "tsk_ini_ETNXXX"
galaxy_body: workshop
subject: ETNXXX
semester: N
tags: [ETNXXX, workshop, inicio]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> Carpeta destino: `Semesters/Sem_NN/ETNXXX/` — movimiento automático por Templater.
> Pregunta: materia, semestre.

---

#### tpl-w-transcription

```yaml
---
title: "tsk_trans_ETNXXX_PN"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, transcripcion, PN]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> Carpeta destino: `Semesters/Sem_NN/ETNXXX/Partial_N/` — movimiento automático por Templater.
> Pregunta: materia, semestre, parcial, cantidad de temas. Genera bloques de tema dinámicamente.

---

#### tpl-w-study

```yaml
---
title: "tsk_study_ETNXXX_PN"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, estudio, PN]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> Carpeta destino: `Semesters/Sem_NN/ETNXXX/Partial_N/` — movimiento automático por Templater.
> Pregunta: materia, semestre, parcial.

---

#### tpl-w-project

```yaml
---
title: "tsk_ETNXXX_nombre_proyecto"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, proyecto, PN]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> Carpeta destino: `Semesters/Sem_NN/ETNXXX/Partial_N/` — movimiento automático por Templater.
> Pregunta: materia, semestre, parcial, slug del proyecto (español, guion_bajo).

---
## Registro de decisiones de diseño

| Decisión                                                         | Razón                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Un archivo por tipo de cuerpo                                    | Cada tipo tiene campos YAML distintos. Una plantilla única con condicionales sería difícil de mantener.                                                                                                                                                                                                                                              |
| Prefijo `tpl-` en todos los nombres                              | Distingue visualmente las plantillas del resto de notas en `_templates/`.                                                                                                                                                                                                                                                                            |
| `tp.file.cursor()` en todas las plantillas                       | El cursor cae siempre en el cuerpo, listo para escribir sin tener que hacer clic.                                                                                                                                                                                                                                                                    |
| Folder Templates solo para Constellations y Observatory          | Son las únicas carpetas donde el tipo de nota es 100% predecible por carpeta. En `Semesters/` el tipo varía por nota, no por carpeta.                                                                                                                                                                                                                |
| Opción B como sistema oficial para Semesters/ (2026-05-28)       | Las plantillas B preguntan materia, semestre, parcial, tema y nombre, y mueven el archivo automáticamente. Elimina la necesidad de navegar manualmente a la carpeta destino. Las plantillas A originales quedan consolidadas como respaldo en `_templates/alt-B/plantillas-A-respaldo.md`.                                                           |
| YAML híbrido en constellation y observatory (2026-05-28)         | El plugin de Excalidraw requiere `excalidraw-plugin: parsed` en el frontmatter para abrir el archivo como lienzo. Se unifica con los campos galaxy en un solo bloque YAML. Sin este campo el archivo se abre como nota de texto.                                                                                                                     |
| Extensión `.excalidraw.md` en lugar de `.excalidraw`             | Mantener `.md` preserva compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar en excalidraw.com se exporta con el comando del plugin.                                                                                                                                                                                                  |
| `tpl-asteroid.md` actualizado a dos ramas (2026-06-24)           | La plantilla original tenía solo los campos del YAML PDF — no reflejaba la rama Normal (sin PDF). Se agregó la rama Normal con `orbiting: []` y se corrige la ruta destino: Normal va a `Topic_NN.../`, PDF va directamente a `Partial_N/` para no obligar al usuario a elegir un tema para una referencia general.                                  |
| `tpl-photon.md` actualizado a tres ramas (2026-06-24)            | La plantilla original solo ofrecía `desmos` como tipo. Se agregan `tikzjax` y `pdf-crop` con lógica de ruta propia: `pdf-crop` va a `_assets/` (es una imagen exportada, no una nota de Semesters/); `desmos` y `tikzjax` van a `Topic_NN.../`. Se eliminan campos incorrectos de la versión anterior.                                               |
| `tpl-supernova.md` creado (2026-06-24)                           | Nuevo tipo #14 aprobado en [[_TAB_note-system]]. Una sola plantilla con dos ramas: `class` individual (por sesión) y fusionada (tema completo). Ambas van a la raíz de `Partial_N/` porque una class puede cubrir subtítulos de varios temas.                                                                                                         |
| `_claude-matter-boot.md` movido a `_app/_config/` (2026-06-25)   | Pasó de ser una herramienta informal en`_templates/`a beacon galaxy oficial. Genera el contexto de trabajo de Claude para materias específicas — protocolo derevisión de ejercicios, flujo de trabajo y guía de formulario por materia.                                                                                                              |
| 4 plantillas `tpl-w-*` creadas como tipo `workshop` (2026-07-18) | Necesidad de seguimiento estructurado de tareas académicas por materia. Cuatro variantes según etapa: `initial` (inicio de materia), `transcription` (seguimiento por parcial), `study` (estudio y repaso), `project` (proyecto puntual). Todas usan Templater con `tp.file.move()` automático a `Semesters/`. Ver [[_galaxy-system]] para tipo #15. |
| `tsk_tpl.md` como referencia en `_projects/` (2026-07-18) | No es una plantilla Templater — es un archivo de copia manual para los slots `tsk_alias.md`. Sin `galaxy_body`, sin lógica de movimiento. Más simple que las plantillas de `_templates/` — incluye comentarios `%%` explicativos por sección para guiar al usuario al copiar. |

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_mindmap-system.md]]
[[_app/_config/_note-system.md]]
[[_pdf_pp-system]]
[[_app/_config/_ToDo-system.md]]
%%
