---
project: "snippet inicio Claude via Templater"
galaxy_body: ship
date: 2026-07-31
status: aborted
fleet: infraestructura
---

# tsk — snippet inicio Claude via Templater

> Idea descartada. Se intentó usar Templater para copiar al portapapeles el snippet de inicio de sesión de Claude con la hora actual.

---

## Problema

Templater no puede ejecutar lógica pura sin crear un archivo nuevo. Al invocar el template, Obsidian genera una nota con el output del script en lugar de simplemente copiar al portapapeles y desaparecer.

## Solución adoptada

Script Python ejecutado desde **Shell Commands** (`start_snippet/main.py`). No crea archivos, copia directamente al portapapeles vía `Set-Clipboard` y se cierra. Ver: [[shellcmd_start_snippet]]

---

## Template descartado

```
<%*
const hora = tp.date.now("HH:mm");
const texto = `Usá el MCP Filesystem y leé E:\\University_vault_2026\\_skills\\_start.md\nHora de inicio: ${hora}`;
await navigator.clipboard.writeText(texto);
tR += `✅ Copiado al portapapeles — ${hora}`;
%>
```

---

%%
# galaxy-links
[[shellcmd_start_snippet]]
%%
