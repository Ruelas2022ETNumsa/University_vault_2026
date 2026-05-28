<%*
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
await tp.file.move("MOC/" + title);
%>---
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

<%* tp.file.cursor() %>

%%
galaxy-links

%%
