---
galaxy_body: operator
project: "Implementación física _hangar/"
date: 2026-07-30
status: busy
---

## Handoff

**Última sesión:** 2026-07-30
**Retomar desde:** lista de tareas pendientes abajo
**Completado esta sesión:** diseño completo del sistema `_hangar/`, documentación en `_galaxy-system.md`, `_projects_system.md`, `_claude-boot.md`, `_excalidraw-system.md`
**Próximo paso:** ejecutar tareas físicas del vault (renombrar carpeta, crear subcarpetas, crear templates, renombrar workers)
**Preguntas de cierre:** —

---

## Resumen y objetivo

Implementar físicamente el sistema `_hangar/` diseñado en sesión 2026-07-30. La documentación ya está hecha — lo que queda es ejecutar los cambios en disco y crear los templates faltantes.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-30 | `_projects/` → `_hangar/` | Nombre más consistente con la metáfora galaxy |
| 2026-07-30 | Workers sin prefijo `tsk_` | Distinguirlos visualmente de los ships |
| 2026-07-30 | `dock/` como sala de espera de ships | Separa proyectos en espera de los carriers activos |
| 2026-07-30 | `_legacy/` como archivo interno de `_hangar/` | Proyectos sin materia asociada se archivan aquí |
| 2026-07-30 | `_relics/` por materia en `semesters/ETNXXX/` | Proyectos académicos completados se archivan en su materia |
| 2026-07-30 | `void` pendiente de carpeta | Nombre decidido, carpeta no diseñada aún |
| 2026-07-30 | workshops no tocados esta sesión | Se pospone para sesión dedicada |

> [!note]- Descartadas
> `others/` como nombre de carpeta de espera — reemplazado por `dock/` para consistencia con la metáfora.

---

## Tareas

### Cambios físicos en disco

- [x] Renombrar carpeta `_projects/` → `_hangar/`
- [x] Renombrar workers (quitar prefijo `tsk_`):
  - [x] `tsk_alx-rul.md` → `alx-rul.md`
  - [x] `tsk_alxgml.md` → `alxgml.md`
  - [x] `tsk_alxhot.md` → `alxhot.md`
  - [x] `tsk_alxrul.md` → `alxrul.md`
  - [x] `tsk_emergn.md` → `emergn.md`
  - [x] `tsk_krajo.md` → `krajo.md`
  - [x] `tsk_standb.md` → `standb.md`
- [x] Crear carpeta `_hangar/dock/`
- [x] Crear `_hangar/dock/logbook.md`
- [x] Crear carpeta `_hangar/_legacy/`
- [x] Mover ships existentes a `dock/`:
  - [x] `tsk_pdf_marginalia_pp.md` → `dock/tsk_pdf_marginalia_pp.md`
- [x] Crear carpeta `anki/` dentro de `_hangar/` (ya existe manualmente — verificar)
- [ ] Crear `_hangar/anki/logbook.md`

### Templates nuevos a crear

- [x] `tpl-ship.md` — basado en `tsk_tpl.md` con YAML de ship (`galaxy_body: ship`, estados de ship)
- [x] `tpl-carrier.md` — YAML de carrier (`galaxy_body: carrier`, `fleet:`, `blocked_by:`)
- [x] `tpl-dropship.md` — YAML de dropship (`galaxy_body: dropship`, `carrier:`, `scope:`, `status:`)
- [ ] `tpl-logbook.md` — YAML de logbook (`galaxy_body: logbook`, `scope:`)
- [x] `tpl-blueprint.md` — YAML de blueprint (`galaxy_body: blueprint`, `status:`, `priority:`)

### Documentación pendiente

- [x] Actualizar `tsk_tpl.md` — cambiar `status: libre/creciente/llena` a `free/busy` para operators
- [ ] Documentar `void` en `_projects_system.md` — carpeta pendiente de diseño (opciones: `drift/`, `nebula/`, `debris/`, `static/`)
- [ ] Diseñar carpeta para `void` y tomar decisión de nombre
- [ ] Sesión dedicada a workshops — 4 tipos actuales + tareas docente + prácticas auxiliar
- [ ] Evaluar `tpl-w-project.md` — definir o eliminar
- [ ] Agregar `_relics/` en `_mindmap-system.md` si aplica

### Pendientes nombrados en la sesión (no perder)

- [ ] `_excalidraw-system.md` — `date_updated` corregido por el usuario, verificar que quedó bien
- [ ] Tabla "Tipos de cuerpo galaxy" en `_galaxy-system.md` — dice "Catorce tipos", actualizar a "Quince" (el usuario lo corrige)
- [ ] Revisar si `_claude-plan.md` necesita actualizarse con la nueva ruta `_hangar/` (referencia a `_projects/`)

---

## Preguntas abiertas

- ¿Nombre final para carpeta `void`? Opciones: `drift/`, `nebula/`, `debris/`, `static/`
- ¿`anki/` ya existe físicamente en `_hangar/` o está solo en `_projects/`? Verificar antes de crear.

---

## Recursos

- `E:\University_vault_2026\_hangar\_projects_system.md` — documentación completa del sistema (nota: beacon vive en `_app/_config/`)
- `E:\University_vault_2026\_app\_config\_projects_system.md` — beacon del sistema
- `E:\University_vault_2026\_app\_config\_galaxy-system.md` — referencia de galaxy_body de proyectos
- `E:\University_vault_2026\_templates\` — carpeta donde van los nuevos templates
