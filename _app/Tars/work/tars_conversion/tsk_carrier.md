---
galaxy_body: carrier
project: "tars-hpprgm-conversion"
date: 2026-09-04
status: docking
fleet: tars
blocked_by:
---

## Handoff

**Última sesión:** 2026-09-04
**Retomar desde:** Prueba 2 Opción A — archivo nuevo nunca cargado en CASE
**Completado esta sesión:** investigación del formato, documentación de opciones A/B/C, prueba 1 de Opción A exitosa (KMH_CONV corrió en CASE), B y C descartadas
**Próximo paso:** crear un programa nuevo en Obsidian y verificar que la Opción A lo carga en CASE sin haberlo visto antes
**Preguntas de cierre:** ninguna — camino claro, seguimos con Opción A hasta integración final en tars-sync

---

## Tareas

- [x] Investigar formato `.hpprgm`
- [x] Relevar antecedentes (PrimeComm, Xprime, TI-Planet, fakuivan)
- [x] Documentar opciones A, B y C
- [x] Crear estructura del carrier
- [x] Probar Opción A — binario moderno desde Python — **APROBADO 2026-09-04**
- [x] Documentar Opción B — descartada (incompleta, requiere paso manual)
- [x] Documentar Opción C — descartada (depende de plantilla preexistente, menos autónoma que A)
- [ ] Prueba 2 Opción A — archivo nuevo nunca cargado en CASE
- [ ] Pruebas con programas más complejos (variables exportadas, múltiples funciones)
- [ ] Prueba end-to-end desde Obsidian vía Shell Commands
- [ ] Integrar Opción A al script `tars-sync`

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | este archivo — tareas activas |
| `conversion-opc_A.md` | dropship | activo | Opción A — binario moderno desde Python |
| `conversion-opc_B.md` | dropship | activo | Opción B — formato G1 (Xprime approach) |
| `conversion-opc_C.md` | dropship | activo | Opción C — header real como plantilla |
