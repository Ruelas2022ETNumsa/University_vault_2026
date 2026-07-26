<%*
const slug = await tp.system.prompt("Nombre del stitch (slug corto)");
const subject = await tp.system.prompt("Materia(s) (ej: MAT101, ETN901)");
const connection_type = await tp.system.prompt("Tipo de conexión (ej: mismo concepto, contraste, continuación)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
%>---
title: "<% slug || tp.file.title %>"
galaxy_body: bridge
scope: stitch
slug: "<% slug || tp.file.title %>"
subject: <% subject %>
connection_type: "<% connection_type %>"
partial: <% partial %>
connected_notes: []
tags: [galaxy-bridge, stitch, zk, <% subject %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

## <% slug || tp.file.title %>

> Conexión: <% connection_type %> · Materia: <% subject %> · Parcial: <% partial %>

---

%%
galaxy-links

%%
