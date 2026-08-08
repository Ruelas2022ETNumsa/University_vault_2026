---
galaxy_body: ship
project: "update-rclone"
date: 2026-08-08
status: delivered
fleet: infraestructura
---

## Handoff

**Última sesión:** 2026-08-08
**Retomar desde:** N/A — proyecto entregado
**Completado esta sesión:** Todo — ver Tareas
**Próximo paso:** Ninguno. Ship cerrado.
**Preguntas de cierre:** Ninguna.

---

## Resumen y objetivo

Actualizar la sincronización de Rclone para incluir `_assets/` (bug que la borraba intermitentemente en Drive), alinear el horario con Samsung Sync, y habilitar el acceso móvil al vault via Drive MCP con visualización de imágenes por URL.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-08 | Incluir `_assets/` en el sync de Rclone | Rclone la borraba intermitentemente en Drive al intentar `rmdir`. Causa: carpeta excluida pero presente en destino. Solución: eliminar la exclusión. |
| 2026-08-08 | Horario cambiado de 13:00 (cada 5h) a 12:05 (cada 5h) | Alineado con Samsung Sync (12:00, 17:00, 22:00) — rclone corre 5 min después para garantizar que las notas ya estén sincronizadas. |
| 2026-08-08 | Drive MCP documentado como canal de consulta móvil | Drive MCP reemplaza a GitHub MCP para lectura remota. GitHub queda para escritura sin PC. Las imágenes de `_assets/` se entregan como URL de Drive — el usuario las abre directamente como propietario. |
| 2026-08-08 | FolderSync tablet documentado como vault completo | La config antigua (4 pares: MOC, Semesters, Semestres, _PDF) fue reemplazada por sync completo del vault para garantizar que plugins y configuración de Obsidian lleguen a todos los dispositivos. |
| 2026-08-08 | Flujo Claude chat → tablet → vault validado | Archivo `.md` creado desde Claude en tablet, descargado, copiado al vault, sincronizado con FolderSync y verificado en PC escritorio. Flujo end-to-end confirmado. |

> [!note]- Descartadas
> Ninguna decisión descartada en este ship.

---

## Planificación

Ship iniciado a partir de un bug reportado: `_assets/` se borraba intermitentemente en Google Drive. La investigación confirmó que rclone intenta `rmdir` sobre carpetas excluidas presentes en el destino. La solución fue eliminar la exclusión. A partir de ahí se aprovechó la sesión para alinear el horario de sync, documentar el sistema completo de Drive MCP como canal móvil, y actualizar todos los beacons afectados.

---

## Flujo de pasos

1. Investigar causa del bug de `_assets/` en Drive
2. Editar comando rclone en Task Scheduler — eliminar `--exclude "_assets/**"`
3. Ejecutar sync manual y verificar que `_assets/` aparece en Drive
4. Ajustar horario de Task Scheduler a 12:05 (alineado con Samsung Sync)
5. Actualizar `Rclone_guide.md`
6. Actualizar `alx_hot.md` — punto 10 completado, decisiones y preguntas abiertas
7. Actualizar `_sync-system.md` — FolderSync tablet, Drive MCP, flujo validado
8. Actualizar `_galaxy-system.md` — registro de decisiones
9. Actualizar `_claude-boot.md` — Drive MCP en conectores, reglas, tabla de beacons
10. Crear este ship como documentación de cierre

---

## Tareas

- [x] Investigar bug `_assets/` borrada en Drive
- [x] Editar comando rclone — eliminar exclusión `_assets/**`
- [x] Verificar sync manual exitoso
- [x] Ajustar horario Task Scheduler a 12:05
- [x] Actualizar `Rclone_guide.md`
- [x] Actualizar `alx_hot.md`
- [x] Actualizar `_sync-system.md`
- [x] Actualizar `_galaxy-system.md`
- [x] Actualizar `_claude-boot.md`
- [x] Crear `tsk_update-rclone.md`

---

## Preguntas abiertas

- `_assets/` en fase de prueba — sync operativo, pendiente validar comportamiento con imágenes pesadas.

---

## Recursos

- `E:\University_vault_2026\_app\_appnotes\Rclone_guide.md`
- `E:\University_vault_2026\_app\_config\_sync-system.md`
- `E:\University_vault_2026\_app\_config\_claude-boot.md`
- `E:\University_vault_2026\_app\_config\_galaxy-system.md`
- `E:\University_vault_2026\_hangar\bay\alx_hot.md`
- Task Scheduler → tarea `rclone sync vault`
