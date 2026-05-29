---
title: "Plantillas Opción A — Respaldo"
scope: respaldo
status: inactivo
date_archived: 2026-05-28
note: "Plantillas Opción A originales. Reemplazadas por Opción B como oficiales. Conservadas como referencia."
---

# Plantillas Opción A — Respaldo

> Estas plantillas son la versión manual (Opción A). El usuario creaba el archivo en la carpeta correcta y seleccionaba la plantilla desde el selector de Templater. Sin lógica de movimiento automático.
> Reemplazadas el 2026-05-28 por las plantillas Opción B con ruta dinámica.

---

## tpl-planet (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-moon (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-comet (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-nebula (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-dwarf (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-asteroid (A)

```
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-photon (A)

```
---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: desmos
attached_to: ""
subject: 
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```

---

## tpl-bridge (A)

```
---
title: "<% tp.file.title %>"
galaxy_body: bridge
subjects: []
semesters: []
connects: []
tags: []
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
```
