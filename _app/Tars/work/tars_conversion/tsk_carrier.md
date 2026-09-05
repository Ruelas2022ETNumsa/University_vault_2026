---
galaxy_body: carrier
project: "tars-hpprgm-conversion"
date: 2026-09-05
status: docking
fleet: tars
blocked_by:
---

## Handoff

**Última sesión:** 2026-09-05
**Retomar desde:** Pruebas con programas más complejos (múltiples funciones exportadas)
**Completado esta sesión:** CIRC_DC, TRIG_SOLV y CINEMAT actualizados con unidades en formato [unidades], corriente en mA en CIRC_DC, símbolo Ω confirmado compatible — los tres superaron pruebas en CASE
**Próximo paso:** pruebas con múltiples funciones EXPORT (requiere actualizar script para N exportados) y gráficos
**Preguntas de cierre:** ninguna

---

## Tareas

- [x] Investigar formato `.hpprgm`
- [x] Relevar antecedentes (PrimeComm, Xprime, TI-Planet, fakuivan)
- [x] Documentar opciones A, B y C
- [x] Crear estructura del carrier
- [x] Probar Opción A — binario moderno desde Python — **APROBADO 2026-09-04**
- [x] Documentar Opción B — descartada (incompleta, requiere paso manual)
- [x] Documentar Opción C — descartada (depende de plantilla preexistente, menos autónoma que A)
- [x] Prueba 1 del plan — función simple KMH_CONV — **SUPERADA 2026-09-04**
- [x] Prueba 2 del plan — archivos nuevos (VOL_CALC, FASOR_CALC) cargados en CASE — **SUPERADA 2026-09-05**
- [x] Prueba end-to-end desde Obsidian vía Shell Commands — **OPERATIVO 2026-09-05**
- [x] Integrar Opción A al script `tars-sync` — **HECHO 2026-09-05**
- [x] Actualizar CIRC_DC, TRIG_SOLV y CINEMAT — unidades [u], mA, Ω — **SUPERADO 2026-09-05**
- [ ] Prueba 3 del plan — INPUT + MSGBOX + lógica de menú (ej. calculadora de préstamo)
- [ ] Prueba 4 del plan — múltiples funciones EXPORT (requiere actualizar script para N exportados)
- [ ] Prueba 5 del plan — gráficos básicos (RECT + TEXTOUT_P)

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | este archivo — tareas activas |
| `conversion-opc_A.md` | dropship | activo | Opción A — binario moderno desde Python |
| `conversion-opc_B.md` | dropship | activo | Opción B — formato G1 (Xprime approach) |
| `conversion-opc_C.md` | dropship | activo | Opción C — header real como plantilla |
