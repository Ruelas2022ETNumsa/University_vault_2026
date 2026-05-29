<%*
const subject1 = await tp.system.prompt("Primera materia (ej: ETN806)");
const subject2 = await tp.system.prompt("Segunda materia (ej: ETN302)");
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
const path = `Semesters/${subject1}-${subject2}/${title}`;
await tp.file.move(path);
%>---
title: "<% tp.file.title %>"
galaxy_body: bridge
subjects: [<% subject1 %>, <% subject2 %>]
semesters: []
connects: []
tags: [galaxy-bridge, <% subject1 %>, <% subject2 %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
