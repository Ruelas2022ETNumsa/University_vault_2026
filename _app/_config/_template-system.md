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

Cada tipo de cuerpo galaxy tiene su plantilla en `_templates/`. Al crear un archivo nuevo en la carpeta correcta, Templater aplica automáticamente la plantilla correspondiente con el YAML precargado, la fecha del día y el cursor posicionado en el cuerpo.

---

## Inventario de plantillas

| Archivo | `galaxy_body` | Carpeta destino | Creación |
|---------|--------------|-----------------|----------|
| `tpl-star.md` | `star` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-planet.md` | `planet` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-moon.md` | `moon` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-comet.md` | `comet` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-nebula.md` | `nebula` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-dwarf.md` | `dwarf` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-asteroid.md` | `asteroid` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-photon.md` | `photon` | `Semesters/.../Topic_NN.../` | Manual |
| `tpl-bridge.md` | `bridge` | `Semesters/.../` | Manual |
| `tpl-constellation.md` | `constellation` | `_app/Excalidraw/Constellations/` | Automático |
| `tpl-observatory.md` | `observatory` | `_app/Excalidraw/Observatory/` | Automático |

**Automático** = Templater aplica la plantilla al crear un archivo en esa carpeta (Folder Templates).
**Manual** = el usuario selecciona la plantilla desde la paleta de comandos o Commander.

---

## Configuración de Templater

### Folder Templates activos

| Carpeta | Plantilla |
|---------|-----------|
| `_app/Excalidraw/Constellations` | `_templates/tpl-constellation` |
| `_app/Excalidraw/Observatory` | `_templates/tpl-observatory` |

### Carpetas ignoradas en file creation

`_templates`, `_app/_config`, `_app/_appnotes`, `borrar`

---

## Variables Templater usadas

| Variable | Qué hace |
|----------|----------|
| `<% tp.file.title %>` | Inserta el nombre del archivo como título |
| `<% tp.date.now("YYYY-MM-DD") %>` | Inserta la fecha de creación |
| `<%* tp.file.cursor() %>` | Posiciona el cursor al abrir la nota |

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
subject: 
semester: 
partial: 
topic: 
star: ""
moons: []
comets: []
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

### tpl-moon

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: moon
subject: 
semester: 
partial: 
topic: 
orbits: ""
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-comet

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: comet
subject: 
semester: 
partial: 
topic: 
source: ""
concepts_used: []
status: pendiente
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-nebula

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: nebula
subject: 
semester: 
partial: 
session_date: <% tp.date.now("YYYY-MM-DD") %>
comets: []
tags: []
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-dwarf

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: dwarf
subject: 
semester: 
partial: 
covers: []
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-asteroid

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: asteroid
subject: 
semester: 
partial: 
topic: 
source_type: 
source_title: ""
source_author: ""
source_chapter: ""
pdf_file: ""
related_planets: []
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: en-proceso
---
```

> Para YAML extendido de asteroid con PDF ver [[_pdf-system]].

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-photon

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: desmos
attached_to: ""
subject: 
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

> `photon_type` puede ser: `desmos` | `image`. No incluye Excalidraw — para eso usar `tpl-constellation` o `tpl-observatory`.

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-bridge

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: bridge
subjects: []
semesters: []
connects: []
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-constellation

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: constellation
subject: 
semester: 
partial: 
topic: 
scope: partial
tools: [excalidraw, mindmap-builder]
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---
```

> `scope`: `partial` si cubre el parcial completo | `topic` si cubre un solo tema.
> Carpeta destino: `_app/Excalidraw/Constellations/` — Templater aplica esta plantilla automáticamente.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

### tpl-observatory

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: observatory
subject: 
semester: 
partial: 
topic: 
attached_to: ""
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---
```

> Carpeta destino: `_app/Excalidraw/Observatory/` — Templater aplica esta plantilla automáticamente.
> Ver [[_mindmap-system]] para convención de nombres y flujo de uso.

```
<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| Un archivo por tipo de cuerpo | Cada tipo tiene campos YAML distintos. Una plantilla única con condicionales sería difícil de mantener. |
| Prefijo `tpl-` en todos los nombres | Distingue visualmente las plantillas del resto de notas en `_templates/`. |
| `tp.file.cursor()` en todas las plantillas | El cursor cae siempre en el cuerpo, listo para escribir sin tener que hacer clic. |
| Folder Templates solo para Constellations y Observatory | Son las únicas carpetas donde el tipo de nota es 100% predecible por carpeta. En `Semesters/` el tipo varía por nota, no por carpeta. |
| `contextogen.md` vive en `_templates/` pero no es una plantilla galaxy | Es una herramienta de infraestructura para generar contexto para Claude. Se mantiene ahí por conveniencia. |

%%
galaxy-links
[[_galaxy-system]]
[[_mindmap-system]]
%%
