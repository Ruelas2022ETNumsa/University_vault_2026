---
alias: "SISTEMA DE LINKS — DOS CAPAS"
date: 
---

## Objetivo

El vault mantiene dos capas de conexión en cada nota. Son redundantes intencionalmente durante la fase de transición:

| Capa | Ubicación | Para quién | Estado |
|---|---|---|---|
| `related_notes` en YAML | Frontmatter | Obsidian + Claude | Activo — se elimina cuando se confirme que `galaxy-links` sostiene el grafo solo |
| `%% galaxy-links %%` | Pie del archivo | Obsidian + Claude | Activo — fuente principal a largo plazo |

> colocar la ruta completa puede ayudar a claude en como cada nota esta conectada con otras, almenos esa es la idea

---

## Pendientes

- [ ] actualizar los galaxy links a su ruta relativa o completa de todos los archivos.

> [!note]- Historial de pendientes
> **fecha** — 

---

## Completado

- [x] se comprobo que en yaml los archivos relacionados tambien crean conexiones en los grafos

> [!note]- Historial de sesiones
> **fecha** — 

---

## Preguntas abiertas

### Cómo Claude usa los galaxy-links

El Filesystem MCP tiene como raíz `E:\University_vault_2026`. Los `galaxy-links` usan ruta relativa desde esa raíz:

```
%%
galaxy-links
[[_app/_config/_galaxy-system]]
[[Semesters/Sem_09/ETN901/Partial_1/ETN901-T01-intro]]
%%
```

Si Claude necesita más contexto sobre un archivo enlazado, puede leerlo directamente usando la ruta del wikilink como ruta relativa desde la raíz del vault. No es necesario escribir la ruta absoluta en el link.



---

## Herramientas / plugins


---

## Archivos relacionados


---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |
