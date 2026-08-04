---
galaxy_body: operator
project: "Sistema de consulta móvil del vault via Google Drive MCP"
date: 2026-08-03
status: busy
---
%%
status: free | busy
- free: worker disponible, sin proyecto asignado
- busy: worker cargado con un ship activo

project: nombre corto del ship que está cargado — dejar vacío si status: free
%%

## Handoff

**Última sesión:** 2026-08-03
**Retomar desde:** `_hangar/dock/tsk_movil_drive.md` — paso 6: prueba end-to-end desde Galaxy
**Completado esta sesión:**
- Pruebas Drive MCP: lectura `.md`, galaxy-links, imágenes via viewUrl ✅
- Creado `_skills/_start_movil.md`
- Creado `_skills/_repaso_movil.md` (rol: auxiliar de estudio, no repaso clásico)
- Creado `_skills/_plan_movil.md`
- Redactado texto para "instrucciones para Claude" versión móvil ✅
- Actualizado `_hangar/dock/tsk_movil_drive.md` con todo el estado actual
**Próximo paso:** Pegar instrucciones en la app móvil → prueba end-to-end desde Galaxy
**Preguntas de cierre:**
- ¿Fusionar `_claude-drive.md` con `_start_movil.md`?
- ¿Renombrar `_repaso_movil.md` a `_auxiliar_movil.md` o similar?

---

## Ship activo

**Ship:** `_hangar/dock/tsk_movil_drive.md`
**Origen:** dock/
**Bloqueado por:** —

---

## Decisiones

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-08-03 | Drive MCP como canal principal en móvil | Filesystem no disponible en móvil |
| 2026-08-03 | Activación via `/drive` en instrucciones de Claude | Minimiza escritura en móvil |
| 2026-08-03 | `_start_movil.md` independiente de `_start.md` | Sistemas distintos, sin dependencia |
| 2026-08-03 | Archivos nuevos desde móvil via chat → descarga manual | Rclone es unidireccional |
| 2026-08-03 | Templates se leen desde Drive al crear ships/blueprints | Evita duplicar estructura en el skill |

> [!note]- Descartadas
> - Rclone `drive_s/` con copy inverso — rompe fuente de verdad única
> - Modo solo lectura estricto — se habilitó creación de archivos en chat para `_plan_movil.md`

---

## Flujo de pasos

1. - [x] Probar Drive MCP
2. - [x] Crear `_start_movil.md`
3. - [x] Crear `_repaso_movil.md`
4. - [x] Crear `_plan_movil.md`
5. - [x] Redactar instrucciones para Claude (móvil)
6. - [ ] Pegar instrucciones en la app móvil
7. - [ ] Prueba end-to-end modo repaso desde Galaxy
8. - [ ] Prueba end-to-end modo plan desde Galaxy
9. - [ ] Decidir fusión `_claude-drive.md` + `_start_movil.md`
10. - [ ] Evaluar sync `_assets/` con Rclone
11. - [ ] Crear `_claude_movil.md`
12. - [ ] Evaluar índice de materias en `Semesters/`
13. - [ ] Evaluar renombre de `_repaso_movil.md`

---

## Tareas

- [x] Probar lectura `.md` via Drive MCP
- [x] Probar navegación galaxy-links via Drive MCP
- [x] Probar imágenes via viewUrl desde Drive
- [x] Confirmar comportamiento Rclone con archivos ya existentes
- [x] Crear `_skills/_claude-drive.md`
- [x] Crear `_skills/_start_movil.md`
- [x] Crear `_skills/_repaso_movil.md`
- [x] Crear `_skills/_plan_movil.md`
- [x] Redactar texto "instrucciones para Claude" versión móvil
- [x] Actualizar `tsk_movil_drive.md`
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

- ¿`_claude-drive.md` se mantiene o se fusiona con `_start_movil.md`?
- ¿Rclone puede sincronizar `_assets/` sin problemas con imágenes pesadas?
- ¿Renombrar `_repaso_movil.md`? Opciones: `_auxiliar_movil.md`, `_estudio_movil.md`
- ¿El índice de materias en `Semesters/` es ship nuevo o tarea dentro de este tsk?

---

## Recursos

- `_hangar/dock/tsk_movil_drive.md` — ship completo con toda la documentación
- `_skills/_start_movil.md` — inicio de sesión móvil
- `_skills/_repaso_movil.md` — auxiliar de estudio móvil
- `_skills/_plan_movil.md` — planificación desde móvil
- `_skills/_claude-drive.md` — skill Drive (borrador)
- `_hangar/template/tpl_ship.md` — template ship
- `_hangar/template/tpl_blueprint.md` — template blueprint

**Texto "instrucciones para Claude" (móvil):**
```
Si el usuario escribe /drive: buscá y leé el archivo _skills/_start_movil.md desde Google Drive usando el conector de Drive conectado. Ejecutá su flujo sin pedir confirmación. No hagas nada más hasta leerlo.

Si el usuario no escribe /drive: ignorá estas instrucciones y comportate normalmente.
```
