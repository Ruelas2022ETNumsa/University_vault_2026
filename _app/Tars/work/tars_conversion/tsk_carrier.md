---
galaxy_body: carrier
project: "tars-hpprgm-conversion"
date: 2026-09-05
status: delivered
fleet: tars
blocked_by:
---

## Handoff

**Última sesión:** 2026-09-05-4
**Retomar desde:** —
**Completado esta sesión:** Prueba 3 superada — CIRC_DC, TRIG_SOLV, CINEMAT (CHOOSE anidado + INPUT + MSGBOX + validación de errores) confirmados operativos. Numeración manual removida de todos los CHOOSE en los tres programas. Regla documentada en la guía. Carrier delivered.
**Próximo paso:** ninguno — carrier completo
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
- [x] Prueba 5 del plan — gráficos: GRAFICA_F, FASOR_G, BAR_CHART — **SUPERADA 2026-09-05**
- [x] Prueba 4 del plan — múltiples EXPORT: STAT_FIN (MEDIA, REGLIN, AMORT) — **SUPERADA 2026-09-05**
- [x] main.py v2 validado contra todos los programas del vault — **SIN ERRORES 2026-09-05**
- [x] Prueba 3 del plan — CHOOSE anidado + INPUT + MSGBOX + validación: CIRC_DC, TRIG_SOLV, CINEMAT — **SUPERADA 2026-09-05-4**
- [x] Remover numeración manual de CHOOSE en CIRC_DC, TRIG_SOLV, CINEMAT — **HECHO 2026-09-05-4**
- [x] Documentar regla CHOOSE sin numeración en guía PPL — **HECHO 2026-09-05-4**

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | este archivo — tareas activas |
| `conversion-opc_A.md` | dropship | activo | Opción A — binario moderno desde Python |
| `conversion-opc_B.md` | dropship | descartado | Opción B — formato G1 (Xprime approach) |
| `conversion-opc_C.md` | dropship | descartado | Opción C — header real como plantilla |
