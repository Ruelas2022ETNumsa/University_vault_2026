<%*
const subject = await tp.system.prompt("Materia (ej: ETN806)");
const sem = await tp.system.prompt("Semestre (ej: 8)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const isPDF = await tp.system.suggester(["Normal (teoría, ejercicio)", "PDF (PDF++ o Annotator)"], [false, true], true, "¿Tipo de asteroid?");

let path;
let topic = "";
let tnum = "";

if (isPDF) {
  tnum = await tp.system.prompt("Número de tema (ej: T01) — T00 si es referencia general");
  const title = await tp.system.prompt("Nombre del archivo SIN extensión (ej: ETN806-T01-PDF-apuntes-conjunta)");
  path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
  await tp.file.move(path);
} else {
  topic = await tp.system.prompt("Tema (ej: T01_joint-density)");
  const title = await tp.system.prompt("Nombre del archivo SIN extensión");
  path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/Topic_${topic}/${title}`;
  await tp.file.move(path);
}
%>---
title: "<% tp.file.title %>"
galaxy_body: asteroid
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
<%* if (isPDF) { %>topic: <% tnum %>
source_type: 
source_title: ""
source_author: ""
source_chapter: ""
pdf_file: ""
related_planets: []
<%* } else { %>topic: 
orbiting: []
<%* } %>tags: [<% subject %>, galaxy-asteroid, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: en-proceso
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
