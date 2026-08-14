---
galaxy_body: carrier
project: "NBLM_update — adaptación del sistema NotebookLM a la nueva notación matemática"
date: 2026-08-13
status: docking
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-13 | hora inicio: 19:05
**Retomar desde:** Tareas pendientes de registro y documentación
**Completado esta sesión:**
- Plugin `Fix Math for Obsidian` modificado (mod alx-rul) — soporte doble backslash Android + salto de línea en bloques `$$`
- `ship_fix-math-mod.md` creado en `_legacy` — plugin documentado
- `logbook.md` de `_legacy` actualizado con el ship
- Script `notebooklm_fix/main.py` actualizado — tikz (3 casos: `\usepackage{`, `\begin{tikzpicture}`, `\begin{axis}`), bloque LaTeX inactivo comentado
- `shellcmd_NBLM_fix.md` actualizado con documentación completa (todas las correcciones + configuración Shell Commands)

**Próximo paso:** Registrar `shellcmd_NBLM_fix.md` en `shellcmd_config_script.md` + documentar `ETN607-transcription-v2.md`
**Preguntas de cierre:** —

---

## Tareas

- [x] Documentar plugin de corrección LaTeX (nombre, ruta, funcionamiento)
- [x] Actualizar script `notebooklm_fix` a nueva notación `\(...\)` / `\[...\]` — sesión dedicada
- [x] Verificar qué correcciones del script siguen siendo válidas con la nueva notación
- [x] Registrar `shellcmd_NBLM_fix.md` en `shellcmd_config_script.md` o equivalente
- [ ] Documentar `ETN607-transcription-v2.md` en su propia nota de documentación
- [ ] Registrar `ETN607-transcription-v2.md` en `tsk_ini_ETN607.md`
- [ ] Evaluar si `ETN607_library.md` (guía pendiente) va en este carrier o en `tsk_ini_ETN607`

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `tsk_NBLM_update.md` | tsk | — | este archivo — tareas activas |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `NBLM_update-opc_script.md` | dropship | entregado | Actualización script notebooklm_fix — sesión dedicada |

---

## Referencias externas

| Archivo | Ubicación | Relación |
| ------- | --------- | -------- |
| `shellcmd_NBLM_fix.md` | `_app/shellcommands/` | Documentación de funcionamiento del script |
| `shellcommands_guide(scripts).md` | `_app/shellcommands/` | Registro del comando en Shell Commands — sección 3.1 |
| `ETN607-transcription-v2.md` | `_app/notebooklm/prompts/ETN607/` | Prompt actualizado con nueva notación |
| `notebooklm_fix/src/main.py` | `.obsidian/scripts/python/` | Script a actualizar |
