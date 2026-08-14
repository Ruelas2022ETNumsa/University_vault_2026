---
galaxy_body: carrier
project: "NBLM_update — adaptación del sistema NotebookLM a la nueva notación matemática"
date: 2026-08-13
status: delivered
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-13 | hora inicio: 20:42
**Retomar desde:** —
**Completado esta sesión:**
- `ETN607-transcription-v3.md` creado — instrucciones de delimitadores eliminadas (resueltas por plugin + script)
- `ETN607_latex.md` creado en `_app/notebooklm/guides/ETN607/` — notación KaTeX de la materia
- `DOC-ETN607-transcription.md` creado en `_app/notebooklm/prompts/ETN607/` — documentación del prompt
- `tsk_ini_ETN607.md` actualizado — v3, DOC y ETN607_latex registrados
- `logbook.md` de NBLM_update actualizado

**Próximo paso:** carrier cerrado — pendientes de ETN607 (`ETN607-study.md`, `contexto_ETN607.md`) viven en `tsk_ini_ETN607.md`
**Preguntas de cierre:** —

---

## Tareas

- [x] Documentar plugin de corrección LaTeX (nombre, ruta, funcionamiento)
- [x] Actualizar script `notebooklm_fix` a nueva notación `\(...\)` / `\[...\]` — sesión dedicada
- [x] Verificar qué correcciones del script siguen siendo válidas con la nueva notación
- [x] Registrar `shellcmd_NBLM_fix.md` en `shellcmd_config_script.md` o equivalente
- [x] Documentar `ETN607-transcription-v3.md` en su propia nota de documentación
- [x] Registrar `ETN607-transcription-v3.md` en `tsk_ini_ETN607.md`
- [x] `ETN607_latex.md` creado en `_app/notebooklm/guides/ETN607/` — resuelve la guía pendiente

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `tsk_NBLM_update.md` | tsk | — | este archivo — tareas activas |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `NBLM_update-opc_script.md` | dropship | evaluado | Actualización script notebooklm_fix — completado |

---

## Referencias externas

| Archivo | Ubicación | Relación |
| ------- | --------- | -------- |
| `shellcmd_NBLM_fix.md` | `_app/shellcommands/` | Documentación de funcionamiento del script |
| `shellcommands_guide(scripts).md` | `_app/shellcommands/` | Registro del comando en Shell Commands — sección 3.1 |
| `ETN607-transcription-v2.md` | `_app/notebooklm/prompts/ETN607/` | Prompt actualizado con nueva notación |
| `notebooklm_fix/src/main.py` | `.obsidian/scripts/python/` | Script a actualizar |
