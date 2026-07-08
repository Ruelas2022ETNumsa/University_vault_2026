<%*
const slug = await tp.system.prompt("Nombre del stitch (slug corto)");
if (slug) await tp.file.rename(slug);
%>---
title: "<% slug || tp.file.title %>"
galaxy_body: bridge
scope: stitch
slug: "<% slug || tp.file.title %>"
connected_notes: []
tags: [galaxy-bridge, stitch, zk]
date_created: <% tp.date.now("YYYY-MM-DD") %>
status: activo
---

---

%%
galaxy-links

%%
