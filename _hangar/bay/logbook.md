---
galaxy_body: logbook
scope: hangar
date_updated: 2026-08-02
---

# Logbook — _hangar/

> Sistema de proyectos completo: [[_app/_config/_projects_system.md]]

Índice de workers activos y estado de operaciones del hangar.

---

## Panel de operaciones

|     Worker     | Status | Estamina | Proyecto activo                                   |   Fecha   | Wake  | Recarga |
| :------------: | :----: | :------: | :------------------------------------------------ | :-------: | :---: | :-----: |
| [[alx_hot.md]] |   ❌    |    🟡    | Sistema consulta móvil via Drive MCP              |           |       |         |
|  [[krajo.md]]  |   ❌    |    🟢    | Implementación física `_hangar/`                  |           |       |         |
| [[alx_gml.md]] |   ❌    |    🟢    | Sistema de links, sync y organización de carpetas |           |       |         |
| [[alxrul.md]]  |   ✔    |    🔴    | —                                                 | 2026-8-17 | 11:00 |  16:00  |
| [[alx-rul.md]] |   ❌    |    🔴    | Cornell Marginalia → Galaxy                       | 2026-8-17 | 11:10 |  16:10  |
| [[standb.md]]  |   ✔    |    🟢    | —                                                 |     —     |   —   |    —    |
| [[emergn.md]]  |   ✔    |    🟢    | —                                                 |     —     |   —   |    —    |

Estados de estamina:
🟡 active — sesión en curso
🔴 tired — cerró sesión; necesita recarga
🟢 ready — descansó 5h desde Wake; estamina completa

Regla: ready = Wake + 5:00h

Estados de status:
✔ free — worker disponible, sin proyecto asignado
❌ busy — worker cargado con un ship activo

---

## Ships en dock/

> Ver [[_hangar/dock/logbook.md]] para el detalle.

---

%%
# galaxy-links
[[_app/_config/_projects_system.md]]
[[alx-rul]]
[[alx_gml]]
[[krajo]]
[[tsk_update_notebooklm_system]]
[[alxrul]]
[[standb]]
[[emergn]]
[[_hangar/dock/logbook.md]]
%%
