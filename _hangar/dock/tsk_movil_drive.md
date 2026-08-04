---
galaxy_body: ship
project: "Sistema de consulta móvil del vault via Google Drive MCP"
date: 2026-08-03
status: in-orbit
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-03
**Retomar desde:** Crear `_plan_movil.md` y `_repaso_movil.md`
**Completado esta sesión:**
- Pruebas de Drive MCP (lectura .md, galaxy-links, imágenes via viewUrl)
- Creación de `_skills/_claude-drive.md` (borrador inicial, puede revisarse)
- Creación de `_skills/_start_movil.md`
- Diseño del texto para "instrucciones para Claude" (móvil)
- Decisiones sobre Rclone, GitHub MCP y flujo de archivos desde móvil

**Próximo paso:** Crear `_repaso_movil.md` y `_plan_movil.md`, luego redactar el texto final para "instrucciones para Claude"
**Preguntas de cierre:** ¿Se mantiene `_claude-drive.md` como skill separado o se fusiona con `_start_movil.md`?

---

## Resumen y objetivo

Diseñar e implementar un sistema para usar Claude desde el celular (Galaxy) en modo consulta del vault universitario, usando el conector nativo de Google Drive de claude.ai como canal de acceso. Sin Filesystem MCP, sin edición de notas.

---

## Decisiones

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-08-03 | Drive MCP como canal principal en móvil | Filesystem no disponible en móvil; Drive ya sincronizado vía Rclone |
| 2026-08-03 | Solo lectura en móvil | Vault tiene PC como fuente de verdad; editar desde móvil genera conflictos |
| 2026-08-03 | Activación via `/drive` en instrucciones de Claude | Minimiza escritura en móvil; un comando activa todo el flujo |
| 2026-08-03 | `_start_movil.md` independiente de `_start.md` | Son sistemas distintos; no deben depender uno del otro |
| 2026-08-03 | Imágenes via viewUrl (sin compartir públicamente) | Funciona porque el usuario es propietario del Drive; comprobado en sesión |
| 2026-08-03 | GitHub MCP en standby | Se mantiene conectado hasta comprobar que el nuevo flujo funciona |
| 2026-08-03 | `_start.md` no se modifica | Si se pega el inicio de sesión PC, tiene prioridad total; separación limpia |

> [!note]- Descartadas
> - **Rclone `drive_s/` con copy inverso** — se descartó la idea de una carpeta especial sincronizada de Drive → PC. Rclone es unidireccional PC → Drive por diseño; agregar una tarea inversa rompe el principio de fuente de verdad única. El flujo de descarga manual es suficiente para los archivos creados desde móvil.
> - **Rclone para sincronizar `_assets/`** — pendiente de evaluar (ver Preguntas abiertas). No descartado definitivamente.

---

## Planificación

El sistema móvil opera en una capa separada del flujo de PC:

- **Canal:** Google Drive MCP (conector nativo de claude.ai, sin configuración adicional)
- **Activación:** comando `/drive` en "instrucciones para Claude" → Claude lee `_start_movil.md` desde Drive
- **Restricciones clave:** solo lectura, sin Filesystem, sin GitHub MCP activo
- **Separación de sistemas:** `_start_movil.md` no depende de `_start.md`; la configuración general cede control cuando detecta el inicio de sesión de PC

Modos de trabajo en móvil:
1. `repaso` — consulta de notas, ejercicios y teoría del vault
2. `plan` — planificación de estudio y organización

---

## Sugerencias

Antecedentes encontrados en sesión 2026-08-03:

- **Output styles de Claude Code** — archivos `.md` con frontmatter que modifican comportamiento por sesión, reutilizables. Patrón similar al de los skills del vault.
- **Prompts minimalistas para móvil** — la documentación de Anthropic confirma que el estilo del prompt influye directamente en el estilo de respuesta. Prompts cortos → respuestas más compactas, ideal para móvil.
- **CLAUDE.md (Claude Code)** — se carga al inicio de sesión automáticamente. Patrón análogo al `/drive` → `_start_movil.md`.

---

## Flujo de pasos

1. ✅ Probar Drive MCP: lectura de `.md`, galaxy-links, imágenes
2. ✅ Crear `_skills/_start_movil.md`
3. [ ] Crear `_skills/_repaso_movil.md`
4. [ ] Crear `_skills/_plan_movil.md`
5. [ ] Redactar texto para "instrucciones para Claude" (versión móvil)
6. [ ] Probar flujo completo desde Galaxy: `/drive` → selección de modo → consulta real
7. [ ] Decidir si `_claude-drive.md` se mantiene o se fusiona con `_start_movil.md`
8. [ ] Evaluar sync de `_assets/` con Rclone (pendiente)

---

## Tareas

- [x] Probar lectura de `.md` via Drive MCP
- [x] Probar navegación galaxy-links via Drive MCP
- [x] Probar imágenes via viewUrl desde Drive
- [x] Confirmar que Rclone no genera duplicados con archivos ya existentes
- [x] Crear `_skills/_claude-drive.md`
- [x] Crear `_skills/_start_movil.md`
- [ ] Crear `_skills/_repaso_movil.md`
- [ ] Crear `_skills/_plan_movil.md`
- [ ] Redactar "instrucciones para Claude" versión móvil
- [ ] Prueba end-to-end desde Galaxy
- [ ] Evaluar sync `_assets/` con Rclone

---

## Preguntas abiertas

- ¿Se mantiene `_claude-drive.md` como skill separado o se fusiona con `_start_movil.md`? (Si se fusiona, `_claude-drive.md` se elimina)
- ¿Rclone puede sincronizar `_assets/` sin problemas con imágenes pesadas? (Evaluar antes de activar)

---

## Recursos

**Archivos del vault:**
- `_skills/_start_movil.md` — skill de inicio sesión móvil
- `_skills/_claude-drive.md` — skill Drive (borrador, puede revisarse)
- `_skills/_repaso_movil.md` — pendiente de crear
- `_skills/_plan_movil.md` — pendiente de crear
- `_app/_config/_sync-system.md` — documentación del sistema de sync
- `_app/_appnotes/Rclone_guide.md` — guía Rclone

**Herramientas:**
- Google Drive MCP (conector nativo claude.ai)
- Rclone (sync PC → Drive, cada 5h)
- Obsidian Git (backup a GitHub, auto-commit)
