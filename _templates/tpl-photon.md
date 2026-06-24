<%*
const subject = await tp.system.prompt("Materia (ej: ETN806)");
const sem = await tp.system.prompt("Semestre (ej: 8)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const photonType = await tp.system.suggester(["desmos", "tikzjax", "pdf-crop"], ["desmos", "tikzjax", "pdf-crop"], true, "¿Tipo de photon?");

let path;
let title;

if (photonType === "pdf-crop") {
  title = await tp.system.prompt("Nombre del archivo SIN extensión (ej: ETN806-T01-PDF-fig-tabla-verdad)");
  path = `_assets/${title}`;
} else {
  title = await tp.system.prompt("Nombre del archivo SIN extensión");
  const topic = await tp.system.prompt("Tema (ej: T01_joint-density)");
  path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/Topic_${topic}/${title}`;
}
await tp.file.move(path);
%>---
title: "<% tp.file.title %>"
galaxy_body: photon
photon_type: <% photonType %>
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
<%* if (photonType === "pdf-crop") { %>source_pdf: ""
source_page: 
attached_to: ""
<%* } else { %>attached_to: ""
<%* } %>tags: [<% subject %>, galaxy-photon, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
