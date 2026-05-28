<%*
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
await tp.file.move("_app/Excalidraw/Observatory/" + title);
%>---
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
