| PDF++ para texto, Annotator para EPUBs/escaneados | Cada plugin tiene su dominio sin solaparse. OmniSearch + Text Extractor cubren la búsqueda. |
| Opción B como sistema oficial para Semesters/ (2026-05-28) | Las plantillas B preguntan materia, semestre, parcial, tema y nombre, y mueven el archivo automáticamente. Elimina la necesidad de navegar manualmente a la carpeta destino. Las plantillas A quedan en `_templates/alt-B/plantillas-A-respaldo.md`. |
| YAML híbrido en constellation y observatory (2026-05-28) | El plugin de Excalidraw requiere `excalidraw-plugin: parsed` en el frontmatter para abrir el archivo como lienzo. Se unifica con los campos galaxy en un solo bloque YAML. Sin este campo el archivo se abre como nota de texto. |
| Extensión `.excalidraw.md` en lugar de `.excalidraw` | Mantener `.md` preserva compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar en excalidraw.com se exporta con el comando del plugin. |

%%
galaxy-links
[[_template-system]]
[[_pdf-system]]
[[_mindmap-system]]
[[_note-system]]
[[_graph-system]]
[[_ToDo-system]]
[[_notebooklm-system]]
%%