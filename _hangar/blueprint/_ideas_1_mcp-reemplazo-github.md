---
galaxy_body: blueprint
status: evaluando
priority: media
date: 2026-08-08
---

# Ideas MCP — reemplazo GitHub

> **Relación:** MCPs personalizados candidatos a reemplazar el slot de GitHub MCP, liberándolo para una herramienta de mayor valor para el vault

---

## MCPs verificados (Claude.ai — sin instalación)

- [ ] Evaluar si aparece algún MCP oficial de búsqueda académica en el directorio de Claude.ai
- [ ] Revisar si Drive MCP ya cubre suficientemente el canal remoto y el slot de GitHub puede liberarse sin reemplazo

---

## MCPs comunitarios — requieren Claude Desktop + Node.js

- [ ] **MCPVault** (`@bitbonsai/mcpvault`) — reemplaza Filesystem MCP con 14 herramientas especializadas para Obsidian: `get_frontmatter`, `update_frontmatter`, `search_notes` (BM25), `append/prepend`, `manage_tags`, `get_vault_stats`. Evaluar si justifica migrar desde Filesystem.
- [ ] **Exa Search** — búsqueda semántica académica integrada en sesión. Útil para buscar papers y referencias mientras se trabaja en una materia sin salir del chat. Alternativa a Brave Search (gratuito, índice independiente).
- [ ] **Git MCP** (oficial Python) — operaciones git locales: `diff`, `log`, `blame`, historial. Útil para auditar cambios del vault sin abrir terminal. Complementa Obsidian Git.

---

## Decisiones previas registradas

- [ ] GitHub MCP actualmente en evaluación para eliminación — ocupa slot de MCP personalizado, su rol de lectura móvil fue reemplazado por Drive MCP (2026-08-08)
- [ ] Drive MCP funcionando bien — muestra imágenes como URL de Drive, flujo móvil validado (2026-08-08)

---

## A depurar

- MCPVault requiere Claude Desktop — verificar si está instalado antes de avanzar
- Exa Search tiene costo de API — evaluar si el uso académico justifica el gasto vs búsqueda web nativa de Claude
- Git MCP puede solaparse con lo que ya hace Obsidian Git automáticamente
