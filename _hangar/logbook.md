---
galaxy_body: logbook
scope: hangar
date_updated: 2026-08-01
---

# Logbook — _hangar/

> Sistema de proyectos completo: [[_app/_config/_projects_system.md]]

Índice de workers activos y estado de operaciones del hangar.

---

## Workers

| Worker | Status | Proyecto activo |
|---|---|---|
| `alx-rul.md` | 🔴 busy | Cornell Marginalia → Galaxy |
| `alx_gml.md` | 🔴 busy | Sistema de links, sync y organización de carpetas |
| `krajo.md` | 🔴 busy | Implementación física `_hangar/` |
| `alx_hot.md` | 🟢 free | — |
| `alxrul.md` | 🟢 free | — |
| `standb.md` | 🟢 free | — |
| `emergn.md` | 🟢 free | — |

---

## Schedule

%%
Estados posibles (columna Status):
🟡 activo — sesión en curso
🔴 agotado — cerró sesión antes de la recarga; handoff documentado en tsk o worker libre
🟢 recargado — pasaron las 5h desde Wake; puede volver a trabajar
⚫ dormido — no trabajó hoy

Regla: Recarga = Wake + 5:00h. Al iniciar sesión → actualizar Fecha, Wake, Recarga y Status. La tabla refleja solo el día actual.
%%

|    Worker    |   Fecha    | Wake  | Recarga |   Status   |
| :----------: | :--------: | :---: | :-----: | :--------: |
| `alx-rul.md` | 2026-07-31 | 20:48 |  01:48  | 🔴 agotado |
| `alx_gml.md` |     —      |   —   |    —    | ⚫ dormido  |
|  `krajo.md`  | 2026-08-01 | 18:05 |  23:05  | 🟡 activo  |
| `alx_hot.md` | 2026-08-01 | 15:10 |  20:10  | 🔴 agotado |
| `alxrul.md`  |     —      |   —   |    —    | ⚫ dormido  |
| `standb.md`  |     —      |   —   |    —    | ⚫ dormido  |
| `emergn.md`  |     —      |   —   |    —    | ⚫ dormido  |

---

## Ships en dock/

> Ver [[_hangar/dock/logbook.md]] para el detalle.

---

%%
# galaxy-links
[[_app/_config/_projects_system.md]]
[[_hangar/alx-rul.md]]
[[_hangar/alx_gml.md]]
[[_hangar/krajo.md]]
[[tsk_update_notebooklm_system]]
[[_hangar/alxrul.md]]
[[_hangar/standb.md]]
[[_hangar/emergn.md]]
[[_hangar/dock/logbook.md]]
%%
