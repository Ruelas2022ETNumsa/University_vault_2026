---
galaxy_body: carrier
project: "tars-python"
date: 2026-09-05
status: docking
fleet: tars
blocked_by:
---

## Handoff

**Última sesión:** 2026-09-05-5
**Retomar desde:** Prueba 1 — crear PY_BASICO.hpprgm, convertir con tars-sync y ejecutar en CASE
**Completado esta sesión:** Carrier creado. Plan de 5 pruebas definido. Investigación del entorno MicroPython de la G2 completada. Los 5 dropships creados con programas completos listos para probar (PY_BASICO, PY_LOOPS, PY_EVAL, PY_GRAF, PY_NUMERICO).
**Próximo paso:** Tomar el código de dropship-py1.md, guardarlo como PY_BASICO.hpprgm en work/, correr el script y ejecutar en CASE
**Preguntas de cierre:** ninguna

---

## Tareas

- [ ] Prueba 1 — bloque #PYTHON básico: print, input(), math — confirmar que el pipeline genera un .hpprgm con Python embebido que CASE ejecuta
- [ ] Prueba 2 — loops e iteración: for, while, range(), listas nativas Python
- [ ] Prueba 3 — hpprime.eval(): llamar PPL desde Python (wait, ticks, msgbox)
- [ ] Prueba 4 — gráficos desde Python: pixon, line, fillrect, textout vía from hpprime import *
- [ ] Prueba 5 — cálculo numérico intensivo: Newton-Raphson o bisección — benchmark vs PPL equivalente
- [ ] Documentar limitaciones encontradas en guía PPL (sección Python)

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | este archivo — tareas activas |
| `dropship-py1.md` | dropship | pendiente | Prueba 1 — print, input, math básico |
| `dropship-py2.md` | dropship | pendiente | Prueba 2 — loops y listas |
| `dropship-py3.md` | dropship | pendiente | Prueba 3 — hpprime.eval() |
| `dropship-py4.md` | dropship | pendiente | Prueba 4 — gráficos desde Python |
| `dropship-py5.md` | dropship | pendiente | Prueba 5 — cálculo numérico intensivo |
