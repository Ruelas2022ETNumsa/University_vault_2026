---
galaxy_body: carrier
project: "NBLM_update — adaptación del sistema NotebookLM a la nueva notación matemática"
date: 2026-08-13
status: docking
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-13 | hora inicio: 14:50
**Retomar desde:** Creación del carrier — tareas definidas, sin dropships trabajados aún
**Completado esta sesión:**
- Carrier creado — carpeta `_hangar/NBLM_update/` activa
- Scope definido: actualización de script + plugin LaTeX + prompts de materia
- `ETN607-transcription-v2.md` creado y ajustado al tope de 10000 caracteres
- `shellcmd_NBLM_fix.md` creado — documentación de funcionamiento del script
- Dropship de actualización del script identificado — sesión separada

**Próximo paso:** Documentar el plugin de corrección LaTeX + crear su dropship
**Preguntas de cierre:** ¿El plugin LaTeX ya tiene nombre/ruta confirmada en el vault?

---

## Tareas

- [ ] Documentar plugin de corrección LaTeX (nombre, ruta, funcionamiento)
- [ ] Actualizar script `notebooklm_fix` a nueva notación `\(...\)` / `\[...\]` — sesión dedicada
- [ ] Verificar qué correcciones del script siguen siendo válidas con la nueva notación
- [ ] Documentar `ETN607-transcription-v2.md` en su propia nota de documentación
- [ ] Registrar `ETN607-transcription-v2.md` en `tsk_ini_ETN607.md`
- [ ] Registrar `shellcmd_NBLM_fix.md` en `shellcmd_config_script.md` o equivalente
- [ ] Evaluar si `ETN607_library.md` (guía pendiente) va en este carrier o en `tsk_ini_ETN607`

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `tsk_NBLM_update.md` | tsk | — | este archivo — tareas activas |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `NBLM_update-opc_script.md` | dropship | activo | Actualización script notebooklm_fix — sesión dedicada |

---

## Referencias externas

| Archivo | Ubicación | Relación |
| ------- | --------- | -------- |
| `shellcmd_NBLM_fix.md` | `_app/shellcommands/` | Documentación de funcionamiento del script |
| `ETN607-transcription-v2.md` | `_app/notebooklm/prompts/ETN607/` | Prompt actualizado con nueva notación |
| `notebooklm_fix/src/main.py` | `.obsidian/scripts/python/` | Script a actualizar |
