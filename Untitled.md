## Snippet original (sin hora)
```
Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
```

---

## Solución: Template de Templater

Creá una nueva nota en tu carpeta de templates (ej. `_skills/_start-snippet.md`) con este contenido:

```
<%*
const hora = tp.date.now("HH:mm");
const texto = `Usá el MCP Filesystem y leé E:\\University_vault_2026\\_skills\\_start.md\nHora de inicio: ${hora}`;
await navigator.clipboard.writeText(texto);
tR += `✅ Copiado al portapapeles — ${hora}`;
%>
```

### Cómo usarlo

1. Guardás esa nota en tu carpeta de templates de Templater
2. Le asignás un hotkey en Obsidian:
   Settings → Hotkeys → buscar "Templater: Open Insert Template modal" → asignale una tecla
   O mejor: Settings → Community Plugins → Templater → Template Hotkeys → agregás el archivo y le ponés una tecla directa (ej. Alt+S)
3. Cuando querés iniciar sesión: presionás el hotkey → el texto con la hora ya está en tu portapapeles → pegás en Claude

### Resultado al pegar

```
Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
Hora de inicio: 14:35
```



