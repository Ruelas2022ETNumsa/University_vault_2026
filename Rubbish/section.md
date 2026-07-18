--- _app\_config\_template-system.md ---
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

### tpl-photon

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

### tpl-supernova

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

> Ver [[_TABnote-system]] para el ciclo de vida completo y [[_galaxy-system]] para la convención de nombres.

---

### tpl-w-initial

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

### tpl-w-transcription

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

### tpl-w-study

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

### tpl-w-project

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

