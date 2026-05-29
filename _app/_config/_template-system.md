---
title: "Sistema de Plantillas — University Vault"
galaxy_body: beacon
scope: vault
tool: templater
audience: [usuario, claude]
tags: [beacon, templater, plantillas, infraestructura]
date_created: 2026-05-28
status: activo
---

# Sistema de Plantillas — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Archivos físicos: `_templates/`

Este documento define el sistema de plantillas del vault. Todas las plantillas usan **Templater** y siguen la convención del Sistema Galaxy.

---

## Idea central

Cada tipo de cuerpo galaxy tiene su plantilla en `_templates/`. Al crear una nota nueva, el usuario usa el botón del ribbon para abrir el selector de Templater, elige la plantilla correspondiente, y responde las preguntas de ruta. Templater completa el YAML, inserta la fecha del día, mueve el archivo a la carpeta correcta y posiciona el cursor en el cuerpo.

---

## Inventario de plantillas

| Archivo | `galaxy_body` | Carpeta destino | Creación |
|---------|--------------|-----------------|----------|
| `tpl-star.md` | `star` | `MOC/` | Automático |
| `tpl-planet.md` | `planet` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-moon.md` | `moon` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-comet.md` | `comet` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-nebula.md` | `nebula` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-dwarf.md` | `dwarf` | `Semesters/.../Partial_N/` | Automático (Opción B) |
| `tpl-asteroid.md` | `asteroid` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-photon.md` | `photon` | `Semesters/.../Topic_NN.../` | Automático (Opción B) |
| `tpl-bridge.md` | `bridge` | `Semesters/Materia1-Materia2/` | Automático (Opción B) |
| `tpl-constellation.md` | `constellation` | `_app/Excalidraw/Constellations/` | Automático |
| `tpl-observatory.md` | `observatory` | `_app/Excalidraw/Observatory/` | Automático |

**Automático (Opción B)** = Templater pregunta materia, semestre, parcial, tema y nombre. Mueve el archivo a la ruta correcta automáticamente.
**Automático** = Templater pide solo el nombre y mueve el archivo a la carpeta fija correspondiente.

### Preguntas por plantilla

| Archivo | Preguntas al crear |
|---------|-------------------|
| `tpl-planet.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-moon.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-comet.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-nebula.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-dwarf.md` | Materia, semestre, parcial, nombre |
| `tpl-asteroid.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-photon.md` | Materia, semestre, parcial, tema, nombre |
| `tpl-bridge.md` | Materia 1, materia 2, nombre |
| `tpl-constellation.md` | Nombre |
| `tpl-observatory.md` | Nombre |

### Respaldo Opción A

Las plantillas originales (sin lógica de movimiento) están consolidadas en `_templates/alt-B/plantillas-A-respaldo.md` como referencia.

---

## Configuración de Templater

### Folder Templates activos

| Carpeta | Plantilla |
|---------|-----------|
| `_app/Excalidraw/Constellations` | `_templates/tpl-constellation` |
| `_app/Excalidraw/Observatory` | `_templates/tpl-observatory` |

> Importante: la ruta de la plantilla en Folder Templates se escribe **sin extensión `.md`**. Usar el selector de archivo de Templater, no escribir la ruta a mano.

### Carpetas ignoradas en file creation

`_templates`, `_app/_config`, `_app/_appnotes`, `borrar`

---

## Configuración de Commander

### Botón en Ribbon

| Botón | Comando | Notas |
|-------|---------|-------|
| Crear nota desde plantilla | `Templater: Create new note from template` | Abre selector — el usuario elige la plantilla |

> Se usa un solo botón en el ribbon que abre el selector de Templater. El usuario elige la plantilla correcta. Esto evita saturar el ribbon con un botón por tipo.

---

## Comportamiento de las plantillas tpl-constellation y tpl-observatory

Estas dos plantillas son especiales: generan archivos que Obsidian abre como lienzos de Excalidraw, no como notas de texto. Para lograrlo combinan tres partes:

1. **Lógica Templater** — pide el nombre del archivo y lo mueve a su carpeta destino
2. **YAML híbrido** — incluye `excalidraw-plugin: parsed` (requerido por el plugin) junto con los campos galaxy
3. **Cuerpo comprimido** — bloque `compressed-json` con el lienzo vacío inicial

```
<%*
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
await tp.file.move("_app/Excalidraw/Constellations/" + title);
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
```

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

### tpl-star

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

### tpl-planet

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

### tpl-moon

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

### tpl-comet

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

### tpl-nebula

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

### tpl-dwarf

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

### tpl-asteroid

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: asteroid
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
topic: 
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

> Para YAML extendido de asteroid con PDF ver [[_pdf-system]].

---

### tpl-photon

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: desmos
attached_to: ""
subject: <% subject %>
tags: [<% subject %>, galaxy-photon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

> `photon_type` puede ser: `desmos` | `image`. No incluye Excalidraw — para eso usar `tpl-constellation` o `tpl-observatory`.

---

### tpl-bridge

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

### tpl-constellation

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
> Carpeta destino: `_app/Excalidraw/Constellations/` — movimiento automático por Templater.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

---

### tpl-observatory

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
> Carpeta destino: `_app/Excalidraw/Observatory/` — movimiento automático por Templater.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| Un archivo por tipo de cuerpo | Cada tipo tiene campos YAML distintos. Una plantilla única con condicionales sería difícil de mantener. |
| Prefijo `tpl-` en todos los nombres | Distingue visualmente las plantillas del resto de notas en `_templates/`. |
| `tp.file.cursor()` en todas las plantillas | El cursor cae siempre en el cuerpo, listo para escribir sin tener que hacer clic. |
| Folder Templates solo para Constellations y Observatory | Son las únicas carpetas donde el tipo de nota es 100% predecible por carpeta. En `Semesters/` el tipo varía por nota, no por carpeta. |
| Opción B como sistema oficial para Semesters/ (2026-05-28) | Las plantillas B preguntan materia, semestre, parcial, tema y nombre, y mueven el archivo automáticamente. Elimina la necesidad de navegar manualmente a la carpeta destino. Las plantillas A originales quedan consolidadas como respaldo en `_templates/alt-B/plantillas-A-respaldo.md`. |
| YAML híbrido en constellation y observatory (2026-05-28) | El plugin de Excalidraw requiere `excalidraw-plugin: parsed` en el frontmatter para abrir el archivo como lienzo. Se unifica con los campos galaxy en un solo bloque YAML. Sin este campo el archivo se abre como nota de texto. |
| Extensión `.excalidraw.md` en lugar de `.excalidraw` | Mantener `.md` preserva compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar en excalidraw.com se exporta con el comando del plugin. |
| `contextogen.md` vive en `_templates/` pero no es una plantilla galaxy | Es una herramienta de infraestructura para generar contexto para Claude. Se mantiene ahí por conveniencia. |

%%
galaxy-links
[[_galaxy-system]]
[[_mindmap-system]]
%%
