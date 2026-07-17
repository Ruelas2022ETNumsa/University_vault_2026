---
alias: "SISTEMA DE LINKS — DOS CAPAS"
galaxy_body: workshop
date_created: 
date_updated: 2026-07-17
status: activo
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

- [x] actualizar los galaxy links a su ruta relativa o completa de todos los archivos.
- [x] P1 — Documentar sistema de dos capas en `_galaxy-system.md` (S1 y S2)
- [ ] P2 — Registrar `workshop` como tipo #15 en `_galaxy-system.md`
- [ ] P3 — Documentar plantillas workshop en beacons correspondientes (`_template-system`, `_notebooklm-system`, `_claude-boot`, `_galaxy-system`)
- [ ] P4 — Documentar guías MAT101 en beacon correspondiente (`_graph-system` o `_galaxy-system`)
- [ ] P5 — Script de merge de archivos `tsk` (baja prioridad)

> [!note]- Historial de pendientes
> **2026-07-17** — galaxy-links actualizados a ruta relativa en archivos del vault. Pendientes P1–P5 abiertos.

---

## Completado

- [x] se comprobó que en yaml los archivos relacionados también crean conexiones en los grafos
- [x] galaxy-links actualizados a ruta relativa desde la raíz del vault en archivos importantes
- [x] `_claude-boot.md` confirmado actualizado — sin cambios necesarios
- [x] Diseño y escritura de 4 plantillas workshop (`tpl-w-initial`, `tpl_w_transcription`, `tpl-w-study`, `tpl-w-project`)
- [x] `galaxy_body: workshop` aprobado como tipo #15 — símbolo 🔧 — para tareas académicas por materia

> [!note]- Historial de sesiones
> **2026-07-17** — Sesión de documentación del sistema de dos capas y diseño del sistema workshop.

---

## Preguntas abiertas

### Cómo Claude usa los galaxy-links

El Filesystem MCP tiene como raíz `E:\University_vault_2026`. Los `galaxy-links` usan ruta relativa desde esa raíz:

```
%%
galaxy-links
[[_app/_config/_galaxy-system.md]]
[[Semesters/Sem_09/ETN901/Partial_1/ETN901-T01-intro.md]]
%%
```

Si Claude necesita más contexto sobre un archivo enlazado, puede leerlo directamente usando la ruta del wikilink como ruta relativa desde la raíz del vault. No es necesario escribir la ruta absoluta en el link.

### Links a notas pendientes de crear

Un wikilink dentro del bloque `%%` puede apuntar a un archivo que aún no existe. Obsidian lo muestra en el grafo como nodo sin contenido. Es una forma válida de planificar notas antes de crearlas.

### Ícono para `galaxy_body: workshop`

🔧 aprobado en sesión 2026-07-17. Alternativas consideradas: 🪛 destornillador, 🔨 martillo, 📐 escuadra. Se eligió 🔧 por referencia directa a trabajo en marcha.

---

## Herramientas / plugins

- Filesystem MCP — lectura y escritura directa en el vault
- Templater — plantillas con prompts encadenados y `tp.file.move()`

---

## Archivos relacionados

- `_app/_config/_galaxy-system.md` — sistema completo de tipos y convenciones
- `_app/_config/_claude-boot.md` — punto de entrada de Claude
- `_app/_config/_notebooklm-system.md` — flujo de materia nueva
- `_app/_config/_template-system.md` — inventario de plantillas
- `_templates/tpl-w-initial.md`
- `_templates/tpl_w_transcription.md`
- `_templates/tpl-w-study.md`
- `_templates/tpl-w-project.md`

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-17 | galaxy-links usan ruta relativa completa desde raíz del vault | Permite a Claude leer archivos enlazados directamente sin ambigüedad |
| 2026-07-17 | `workshop` aprobado como tipo #15, símbolo 🔧 | Necesidad de monitorear tareas académicas por materia sin mezclar con galaxy bodies de contenido |
| 2026-07-17 | 4 plantillas workshop con Templater | Consistencia con el sistema de plantillas existente; preguntas encadenadas + `tp.file.move()` automático |


---

%%
# galaxy-links
%%