<%*
const subject = await tp.system.prompt("Materia (ej: ETN901)");
const sem = await tp.system.prompt("Semestre (ej: 9)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const title = `tsk_study_${subject}_P${partial}`;
const path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
await tp.file.move(path);
%>---
title: "<% title %>"
galaxy_body: workshop
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
tags: [<% subject %>, workshop, estudio, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

# tsk — Estudio P<% partial %> · <% subject %>

## NotebookLM — prompts y guías

- [ ] Prompt de estudio creado → `_app/notebooklm/prompts/<% subject %>/<% subject %>-P<% partial %>-study.md`
- [ ] Prompt de transcripción creado → `_app/notebooklm/prompts/<% subject %>/<% subject %>-P<% partial %>-transcription.md`
- [ ] Guías y fuentes del notebook actualizadas → `_app/notebooklm/guides/<% subject %>/`
- [ ] Notebook configurado — fuentes + Instructions cargado

---

## Prácticas

| práctica | archivo en vault | status |
| -------- | ---------------- | ------ |
|          |                  | pendiente |

---

## Exámenes pasados

| examen | año | archivo en vault | status |
| ------ | --- | ---------------- | ------ |
|        |     |                  | pendiente |

---

## Notas y pendientes

%%
galaxy-links

%%
