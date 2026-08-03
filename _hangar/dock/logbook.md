---
galaxy_body: logbook
scope: dock
date_updated: 2026-08-03
---

---

## Foco actual

Cola activa con 9 ships. El único P1 está bloqueado por el carrier anki — se retoma cuando ese proyecto entregue. Foco inmediato en P2: `tsk_operator_reload_display` y P3: `tsk_library_ETN825`.

---

%% COLA DE TSK: ships activos o pendientes de trabajo.
Columnas: Tsk (wikilink) | Prioridad | Status (docked/in-orbit/delayed) | Worker (worker activo o —) | Nota
Orden: por prioridad, dentro de la misma prioridad más antiguo arriba. %%

## Cola de tsk

| Tsk                             | Prioridad | Status | Worker | Nota |
| ------------------------------- | :-------: | :----: | :----: | ---- |
| [[tsk_operator_reload_display]] |    P2     | docked |   —    | —    |
| [[tsk_memory_matter]]           |    P3     | docked |   —    | —    |

---

%% IN-ORBIT: ships pausados sin dependencia externa — pueden retomarse en cualquier momento.
Columnas: Tsk (wikilink) | Prioridad | Worker | Nota (campo "Retomar desde" del Handoff si existe)
Orden: más antiguo arriba, más actual abajo. %%

## In-orbit

| Tsk                                  | Prioridad | Worker | Nota                             |
| ------------------------------------ | :-------: | :----: | -------------------------------- |
| [[tsk_Gemini_Helper_Vault]]          |    P3     |   —    | —                                |
| [[tsk_Mapa_IAs_vault_roles_APIs]]    |    P3     |   —    | —                                |
| [[tsk_pendientes_sistema_galaxy]]    |    P3     |   —    | —                                |
| [[tsk_script_extaction_integration]] |    P3     |   —    | documentación pendiente          |
| [[tsk_Wolfram_alpha_script]]         |    P3     |   —    | detalles finales + documentación |

---

%% DELAYED: ships bloqueados por una dependencia externa — no pueden avanzar hasta que se resuelva.
Columnas: Tsk (wikilink) | Prioridad | Bloqueado por | Worker
Orden: más antiguo arriba, más actual abajo. %%

## Delayed

| Tsk                       | Prioridad | Bloqueado por                     | Worker |
| ------------------------- | :-------: | --------------------------------- | :----: |
| [[tsk_pdf_marginalia_pp]] |    P1     | carrier anki                      |   —    |
| [[tsk_library_ETN825]]    |    P3     | temario completo 2026 del docente |   —    |

---

%% ARCHIVADOS: ver legacy/logbook.md para el historial completo de delivered y aborted. %%
