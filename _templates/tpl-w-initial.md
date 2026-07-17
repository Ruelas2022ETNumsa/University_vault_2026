<%*
const subject = await tp.system.prompt("Materia (ej: ETN901)");
const sem = await tp.system.prompt("Semestre (ej: 9)");
const title = `tsk_ini_${subject}`;
const path = `Semesters/Sem_0${sem}/${subject}/${title}`;
await tp.file.move(path);
%>---
title: "<% title %>"
galaxy_body: workshop
subject: <% subject %>
semester: <% sem %>
tags: [<% subject %>, workshop, inicio]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

# tsk — Inicio de materia · <% subject %>

## Libros

- [ ] Temario completo entregado a Claude
- [ ] Bibliografía sugerida por el docente evaluada
- [ ] Stack aprobado → ver `[[_app/_config/_library-system]]`
- [ ] `_library_<% subject %>.md` creado en `_app/_config/`

---

## NotebookLM — fuentes

- [ ] PDFs del stack subidos al notebook
- [ ] Índices extraídos y verificados visualmente
- [ ] `<% subject %>_library.md` creado en `_app/notebooklm/guides/<% subject %>/`
- [ ] Fuentes cargadas en NotebookLM

---

## NotebookLM — prompts

- [ ] `<% subject %>-P1-study.md` creado en `_app/notebooklm/prompts/<% subject %>/`
- [ ] `<% subject %>-P1-transcription.md` creado en `_app/notebooklm/prompts/<% subject %>/`
- [ ] Notebook configurado — fuentes + Instructions cargado

---

## Claude

- [ ] `contexto_<% subject %>.md` generado vía `[[_app/_config/_claude-matter-boot]]`

---

## Notas y pendientes

%%
galaxy-links

%%
