<%*
const subject = await tp.system.prompt("Materia (ej: ETN806)");
const sem = await tp.system.prompt("Semestre (ej: 8)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const topic = await tp.system.prompt("Tema (ej: T01_joint-density)");
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
const path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${topic}/${title}`;
await tp.file.move(path);
%>---
title: "<% tp.file.title %>"
galaxy_body: nebula
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
session_date: <% tp.date.now("YYYY-MM-DD") %>
comets: []
tags: [<% subject %>, galaxy-nebula, P<% partial %>]
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
