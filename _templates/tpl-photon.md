<%*
const subject = await tp.system.prompt("Materia (ej: ETN806)");
const sem = await tp.system.prompt("Semestre (ej: 8)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const topic = await tp.system.prompt("Tema (ej: T01_joint-density)");
const title = await tp.system.prompt("Nombre del archivo (sin extensión)");
const path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/Topic_${topic}/${title}`;
await tp.file.move(path);
%>---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: desmos
attached_to: ""
subject: <% subject %>
tags: [<% subject %>, galaxy-photon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
