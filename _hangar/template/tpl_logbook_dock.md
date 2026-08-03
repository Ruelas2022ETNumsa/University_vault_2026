---
galaxy_body: logbook
scope: dock
date_updated: 
---

%%
# YAML — instrucciones de llenado

galaxy_body: logbook → siempre este valor, no cambiar
scope: dock → siempre este valor para el logbook de dock
date_updated: actualizar cada vez que se modifica este archivo (YYYY-MM-DD)

# Al actualizar este archivo
  1. Actualizar date_updated en el YAML
  2. Revisar y ajustar ## Foco actual si cambió la prioridad
  3. Actualizar la tabla de ## Cola de tsk — status, worker, notas
  4. Mover tsk delivered a ## Archivados con su fecha
%%

---

## Foco actual

%%
2-3 líneas que describen qué se está priorizando en este momento.
Actualizar al inicio de cada sesión si el foco cambió.
Responde: ¿qué se quiere avanzar ahora y por qué?
Límite recomendado: no más de 2-3 tsk en P1 simultáneamente.
%%

---

## Cola de tsk

%%
Tabla de todos los tsk en dock/ — incluyendo docked, in-orbit y delayed.
Los delivered se mueven a ## Archivados.

Columnas:
- Tsk        → nombre del archivo sin extensión, como wikilink
- Prioridad  → P1 (alta) | P2 (media) | P3 (baja)
- Status     → docked | in-orbit | delayed
- Worker     → wikilink al operator que lo tiene cargado, o — si ninguno
- Nota       → motivo de bloqueo si delayed, avance relevante si in-orbit, o —
%%

| Tsk | Prioridad | Status | Worker | Nota |
| --- | :-------: | :----: | :----: | ---- |
| `[[]]` | P | — | — | — |

---

## Archivados

%%
Lista de tsk completados — status: delivered.
Formato: - YYYY-MM-DD — [[nombre-tsk]] — descripción breve de qué se logró
No eliminar entradas, este bloque es el historial del dock.
%%

-
