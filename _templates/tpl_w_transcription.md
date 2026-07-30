<%*
const subject = await tp.system.prompt("Materia (ej: ETN901)");
const sem = await tp.system.prompt("Semestre (ej: 9)");
const partial = await tp.system.prompt("Parcial (1, 2 o 3)");
const numTemas = parseInt(await tp.system.prompt("Cantidad de temas del parcial (ej: 3)"));
const title = `tsk_trans_${subject}_P${partial}`;
const path = `Semesters/Sem_0${sem}/${subject}/Partial_${partial}/${title}`;
await tp.file.move(path);

// Generar bloques de temas dinámicamente
let bloquesTemas = "";
for (let i = 1; i <= numTemas; i++) {
  const tNum = String(i).padStart(2, "0");
  bloquesTemas += `
### T${tNum} — *(completar título)*

#### Supernovas
- [ ] Classes individuales completadas
- [ ] Supernova fusionada creada → \`${subject}-T${tNum}-slug_del_tema-P${partial}.md\`

#### Galaxy bodies obligatorios
- [ ] \`star\` ☀️ → \`${subject}-T${tNum}-star.md\`
- [ ] \`planet\` 🪐 — listar uno por concepto:
  - [ ] 
- [ ] \`dwarf\` ⬛ tema → \`${subject}-T${tNum}-dwarf-P${partial}.md\`

#### Galaxy bodies opcionales
- [ ] \`moon\` 🌙
- [ ] \`comet\` ☄️
- [ ] \`nebula\` 🌫️
- [ ] \`asteroid\` 🪨
- [ ] \`photon\` 💡
- [ ] \`observatory\` 🔭

---
`;
}
%>---
title: "<% title %>"
galaxy_body: workshop
subject: <% subject %>
semester: <% sem %>
partial: <% partial %>
tags: [<% subject %>, workshop, transcripcion, P<% partial %>]
date_created: <% tp.date.now("YYYY-MM-DD") %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

# tsk — Transcripción P<% partial %> · <% subject %>

## Supernovas — seguimiento de clases

| class | fecha | subtítulos | status |
| ----- | ----- | ---------- | ------ |
|       |       |            | pendiente |

---

## Temas del parcial
<% bloquesTemas %>
## Cierre de parcial

- [ ] `dwarf` ⬛ parcial completo → `<% subject %>-T00-dwarf-P<% partial %>.md`
- [ ] `constellation` 🌌 → `Excalidraw/Constellations/<% subject %>-P<% partial %>-constellation.md`

---

## Notas y pendientes

%%
galaxy-links

%%
