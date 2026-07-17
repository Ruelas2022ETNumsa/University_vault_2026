<%*
const subject = await tp.system.prompt("Materia (ej: ETN901)");
const sem = await tp.system.prompt("Semestre (ej: 9)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const slug = await tp.system.prompt("Nombre del proyecto en español, guion_bajo (ej: filtro_pasa_bajos)");
const title = `tsk_${subject}_${slug}`;
const path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
await tp.file.move(path);
%>---
title: "<% title %>"
galaxy_body: workshop
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
tags: [<% subject %>, workshop, proyecto, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

# tsk — <% slug.replaceAll("_", " ") %> · <% subject %>

## Resumen y objetivo

%%
Una o dos líneas: ¿qué se quiere lograr y por qué?
%%

---

## Planificación

%%
Contexto, restricciones clave y razonamiento del enfoque elegido.
Si el proyecto fue replanificado, el plan anterior va en un callout colapsado:
> [!error]- Planificación abandonada (motivo)
%%

---

## Flujo de pasos

- [ ] 
- [ ] 

---

## Tareas

- [ ] 
- [ ] 

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |

> [!note]- Descartadas
> Enfoques considerados pero abandonados, con motivo.

---

## Recursos

%%
Herramientas, archivos del vault (con ruta relativa) y links externos necesarios.
%%

---

## Notas y pendientes

%%
galaxy-links

%%
