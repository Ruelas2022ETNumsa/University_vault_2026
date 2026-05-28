<%*
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
await tp.file.move("_app/Excalidraw/Constellations/" + title);
%>---
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
