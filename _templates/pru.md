<%*
const hora = tp.date.now("HH:mm");
const texto = `Usá el MCP Filesystem y leé E:\\University_vault_2026\\_skills\\_start.md\nHora de inicio: ${hora}`;
await navigator.clipboard.writeText(texto);
tR += `✅ Copiado al portapapeles — ${hora}`;
%>