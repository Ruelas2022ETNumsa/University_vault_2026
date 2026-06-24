<%*
const subject = await tp.system.prompt("Materia (ej: ETN901)");
const sem = await tp.system.prompt("Semestre (ej: 9)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const tipo = await tp.system.suggester(
  ["Class (nota de sesión individual)", "Supernova completa (tema fusionado)"],
  ["class", "supernova"],
  true,
  "¿Qué tipo de supernova es?"
);

let path;
let title;

let classNum = "";
if (tipo === "class") {
  classNum = await tp.system.prompt("Número de clase del semestre (ej: 001)");
  const fecha = await tp.system.prompt("Fecha de la clase (ej: jun15)");
  title = `${subject}-class${classNum}-P${partial}-${fecha}`;
  path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
  await tp.file.move(path);
} else {
  const topicNum = await tp.system.prompt("Número de tema (ej: T1)");
  const topicSlug = await tp.system.prompt("Nombre del tema en español, guion_bajo (ej: densidad_probabilidad_conjunta)");
  title = `${subject}-${topicNum}-${topicSlug}-P${partial}`;
  path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
  await tp.file.move(path);
}
%>---
title: "<% title %>"
galaxy_body: supernova
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
<%* if (tipo === "class") { %>class_number: <% classNum %>
class_date: <% tp.date.now("YYYY-MM-DD") %>
subtopics:
  - ""
related_planets: []
<%* } else { %>topic: 
topic_name: 
class_parts:
  - ""
related_planets: []
<%* } %>tags: [<% subject %>, galaxy-supernova, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: <%* if (tipo === "class") { %>en-proceso<%* } else { %>completo<%* } %>
---

<%* tp.file.cursor() %>

%%
galaxy-links

%%
