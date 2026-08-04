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
**Retomar desde:** Prueba end-to-end desde Galaxy — `/drive` → selección de modo → consulta real
**Completado esta sesión:**
- Pruebas Drive MCP: lectura `.md`, galaxy-links, imágenes via viewUrl ✅
- Confirmado que Rclone no genera duplicados ✅
- Creado `_skills/_claude-drive.md` (borrador — evaluar si se fusiona con `_start_movil.md`)
- Creado `_skills/_start_movil.md`
- Creado `_skills/_repaso_movil.md` (renombrar a `_auxiliar_movil.md` o similar — "repaso" no describe bien el rol)
- Creado `_skills/_plan_movil.md`
- Redactado texto para "instrucciones para Claude" (móvil) — listo para pegar
- Creado este tsk

**Próximo paso:** Prueba end-to-end desde Galaxy con el flujo completo
**Preguntas de cierre:**
- ¿Se mantiene `_claude-drive.md` o se fusiona con `_start_movil.md`?
- ¿Renombrar `_repaso_movil.md` a algo que refleje mejor su rol de auxiliar?

---

## Resumen y objetivo

Diseñar e implementar un sistema para usar Claude desde el celular (Galaxy) en modo consulta y auxiliar del vault universitario, usando el conector nativo de Google Drive de claude.ai como canal de acceso. Sin Filesystem MCP, sin edición de notas del vault.

---

## Decisiones

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-08-03 | Drive MCP como canal principal en móvil | Filesystem no disponible en móvil; Drive ya sincronizado vía Rclone |
| 2026-08-03 | Solo lectura del vault en móvil | PC es fuente de verdad; editar desde móvil genera conflictos |
| 2026-08-03 | Activación via `/drive` en instrucciones de Claude | Minimiza escritura en móvil; un comando activa todo el flujo |
| 2026-08-03 | `_start_movil.md` independiente de `_start.md` | Son sistemas distintos; no deben depender uno del otro |
| 2026-08-03 | Si se pega inicio de sesión PC, `_start.md` tiene prioridad | La configuración general cede control — sin modificar `_start.md` |
| 2026-08-03 | Imágenes via viewUrl sin compartir públicamente | Funciona porque el usuario es propietario del Drive; comprobado PC y Galaxy |
| 2026-08-03 | GitHub MCP en standby | Se mantiene conectado hasta comprobar que el nuevo flujo funciona |
| 2026-08-03 | Archivos creados desde móvil van por chat → descarga manual | Rclone es unidireccional; no hay sync inverso Drive → PC |
| 2026-08-03 | Templates se leen desde Drive al crear ships/blueprints | Evita duplicar estructura en el skill; refleja cambios automáticamente |
| 2026-08-03 | `_repaso_movil.md` es un auxiliar, no un repaso | El modo resuelve ejercicios, explica conceptos y complementa NotebookLM |

> [!note]- Descartadas
> - **Rclone `drive_s/` con copy inverso** — carpeta especial Drive → PC descartada. Rclone es unidireccional por diseño; tarea inversa rompe principio de fuente de verdad única. Descarga manual es suficiente.
> - **Modo solo lectura estricto desde móvil** — se habilitó creación de archivos en el chat (ship, blueprint) para `_plan_movil.md`. El usuario los descarga y los ubica manualmente.

---

## Planificación

El sistema móvil opera en una capa separada del flujo de PC:

- **Canal:** Google Drive MCP (conector nativo de claude.ai)
- **Activación:** `/drive` en "instrucciones para Claude" → Claude lee `_start_movil.md` desde Drive sin pedir confirmación
- **Restricciones:** sin edición de archivos existentes, sin Filesystem, sin GitHub MCP activo
- **Separación:** `_start_movil.md` no depende de `_start.md`

Dos modos disponibles en móvil:
1. `repaso` → carga `_repaso_movil.md` — auxiliar de estudio: ejercicios, conceptos, código, NotebookLM
2. `plan` → carga `_plan_movil.md` — planificación: ships, blueprints, lista de proyectos

---

## Sugerencias

Antecedentes encontrados en sesión 2026-08-03:

- **Output styles de Claude Code** — archivos `.md` con frontmatter que modifican comportamiento por sesión. Patrón análogo al de los skills del vault.
- **Prompts minimalistas para móvil** — Anthropic confirma que el estilo del prompt influye directamente en el estilo de respuesta.
- **CLAUDE.md (Claude Code)** — se carga al inicio de sesión automáticamente sin intervención. Patrón análogo al `/drive` → `_start_movil.md`.
- **Active recall sobre re-lectura** — para el modo auxiliar, las explicaciones paso a paso son más efectivas que mostrar el contenido pasivamente.

---

## Flujo de pasos

1. - [x] Probar Drive MCP: lectura `.md`, galaxy-links, imágenes
2. - [x] Crear `_skills/_start_movil.md`
3. - [x] Crear `_skills/_repaso_movil.md`
4. - [x] Crear `_skills/_plan_movil.md`
5. - [x] Redactar texto para "instrucciones para Claude" versión móvil
6. - [ ] Pegar texto en "instrucciones para Claude" en la app
7. - [ ] Prueba end-to-end desde Galaxy: `/drive` → modo repaso → consulta real con una nota
8. - [ ] Prueba end-to-end desde Galaxy: `/drive` → modo plan → crear un ship
9. - [ ] Decidir si `_claude-drive.md` se mantiene o se fusiona con `_start_movil.md`
10. - [ ] Evaluar sync de `_assets/` con Rclone
11. - [ ] Crear `_claude_movil.md` — resumen del boot adaptado para contexto móvil
12. - [ ] Crear índice de materias/temas en `Semesters/` (pendiente separado — evaluar scope)
13. - [ ] Renombrar `_repaso_movil.md` si se aprueba un nombre más representativo

---

## Tareas

- [x] Probar lectura de `.md` via Drive MCP
- [x] Probar navegación galaxy-links via Drive MCP
- [x] Probar imágenes via viewUrl desde Drive (PC y Galaxy)
- [x] Confirmar comportamiento de Rclone con archivos ya existentes
- [x] Crear `_skills/_claude-drive.md`
- [x] Crear `_skills/_start_movil.md`
- [x] Crear `_skills/_repaso_movil.md`
- [x] Crear `_skills/_plan_movil.md`
- [x] Redactar texto "instrucciones para Claude" versión móvil
- [x] Crear `_hangar/dock/tsk_movil_drive.md`
- [ ] Pegar instrucciones en la app móvil
- [ ] Prueba end-to-end modo repaso desde Galaxy
- [ ] Prueba end-to-end modo plan desde Galaxy
- [ ] Decidir fusión `_claude-drive.md` + `_start_movil.md`
- [ ] Evaluar sync `_assets/` con Rclone
- [ ] Crear `_claude_movil.md`
- [ ] Evaluar índice de materias en `Semesters/`
- [ ] Evaluar renombre de `_repaso_movil.md`

---

## Preguntas abiertas

- ¿`_claude-drive.md` se mantiene como skill separado o se fusiona con `_start_movil.md`?
- ¿Rclone puede sincronizar `_assets/` sin problemas? (buscar en web antes de activar)
- ¿Renombrar `_repaso_movil.md`? Opciones: `_auxiliar_movil.md`, `_estudio_movil.md`
- ¿El índice de materias en `Semesters/` es un ship nuevo o una tarea dentro de este tsk?

---

## Recursos

**Archivos del vault:**
- `_skills/_start_movil.md` — inicio de sesión móvil
- `_skills/_repaso_movil.md` — auxiliar de estudio móvil
- `_skills/_plan_movil.md` — planificación desde móvil
- `_skills/_claude-drive.md` — skill Drive (borrador)
- `_hangar/template/tpl_ship.md` — template de ship
- `_hangar/template/tpl_blueprint.md` — template de blueprint
- `_hangar/bay/logbook.md` — logbook general del hangar
- `_hangar/dock/logbook.md` — cola de proyectos activos
- `_app/_config/_sync-system.md` — documentación del sistema de sync
- `_app/_appnotes/Rclone_guide.md` — guía Rclone

**Texto "instrucciones para Claude" (móvil) — listo para pegar:**
```
Si el usuario escribe /drive: buscá y leé el archivo _skills/_start_movil.md desde Google Drive usando el conector de Drive conectado. Ejecutá su flujo sin pedir confirmación. No hagas nada más hasta leerlo.

Si el usuario no escribe /drive: ignorá estas instrucciones y comportate normalmente.
```

**Herramientas:**
- Google Drive MCP (conector nativo claude.ai)
- Rclone (sync PC → Drive, unidireccional, cada 5h)
- Obsidian Git (backup a GitHub, auto-commit cada 5 min)
