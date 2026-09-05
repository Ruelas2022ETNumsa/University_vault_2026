---
galaxy_body: logbook
scope: tars-hpprgm-conversion
status: on-track
date_updated: 2026-09-05
session: 2026-09-05-4
---

## Visión general

Carrier para resolver la conversión automática de archivos `.hpprgm` desde Obsidian hacia CASE (HP Prime virtual) sin drag and drop manual. El problema central es que el formato `.hpprgm` es binario (header + UTF-16 LE) y un fuente guardado como texto plano UTF-8 no es reconocido por CASE. Se evalúan tres opciones de conversión, una por dropship, hasta encontrar la que funcione de forma confiable.

---

## Estado actual

**Salud:** on-track
**Resumen:** Prueba 4 superada. STAT_FIN (3 EXPORT: MEDIA, REGLIN, AMORT) cargado y ejecutado en CASE. main.py v2 validado contra todos los programas del vault — ninguno con errores.
**Último avance:** main.py v2 con detección dinámica de N funciones EXPORT confirmado operativo. Todos los programas existentes reprobados sin errores.
**Próximo hito:** Prueba 3 — INPUT + MSGBOX + lógica de menú compleja.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | archivo de trabajo activo |
| `conversion-opc_A.md` | dropship | activo | Opción A — binario moderno desde Python |
| `conversion-opc_B.md` | dropship | activo | Opción B — formato G1 (Xprime approach) |
| `conversion-opc_C.md` | dropship | activo | Opción C — header real como plantilla |

---

## Hitos

- 2026-09-04 — investigación del formato `.hpprgm` completada, tres opciones documentadas
- 2026-09-04 — Opción A validada: Python genera `.hpprgm` binario que CASE reconoce y ejecuta correctamente
- 2026-09-05 — Prueba 2 superada: VOL_CALC y FASOR_CALC (generados por IA, nunca vistos por CASE) cargados y ejecutados correctamente
- 2026-09-05 — Script actualizado para Obsidian: ruta dinámica con `os.path.expanduser()`, argumentos vía `{{file_path:absolute}}`, registrado en Shell Commands
- 2026-09-05 — Guía de programación PPL documentada en `hp_prime_g2_promgram_guide.md`
- 2026-09-05 — CIRC_DC, TRIG_SOLV y CINEMAT actualizados: unidades en formato [unidades], corriente en mA en CIRC_DC, símbolo Ω confirmado compatible con CASE — los tres programas superaron pruebas
- 2026-09-05 — Prueba 5 superada: GRAFICA_F, FASOR_G y BAR_CHART ejecutados correctamente en CASE — gráficos con LINE_P, PIXON_P, ARC_P y TEXTOUT_P confirmados operativos
- 2026-09-05 — Prueba 4 superada: STAT_FIN (MEDIA, REGLIN, AMORT — 3 EXPORT) cargado y ejecutado en CASE — main.py v2 con N EXPORT dinámico confirmado operativo
- 2026-09-05 — main.py v2 validado contra todos los programas del vault — ninguno con errores

---

## Riesgos y dependencias

- El formato moderno de `.hpprgm` puede tener bytes de metadata no documentados en TI-Planet que hagan fallar la Opción A
- La Opción B requiere un paso manual en CASE (hacer "Check") — puede ser aceptable o no según el flujo real
- La Opción C depende de tener un `.hpprgm` real generado por CASE disponible como plantilla

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-09-04 | Destino: `HP Prime\Calculators\Prime` | Ruta confirmada — CASE la detecta al abrir |
| 2026-09-04 | TARS física queda como drag and drop manual | No hay ruta de carpeta para calc física — requiere USB |
| 2026-09-04 | Opción A como camino principal | Prueba 1 exitosa, autónoma, no depende de plantilla preexistente |
| 2026-09-04 | Opciones B y C descartadas | B incompleta y requiere paso manual en CASE; C depende de plantilla preexistente |
| 2026-09-05 | Script movido a `tars-sync\main.py` | Consolidación en carpeta de scripts de Obsidian |
| 2026-09-05 | Ruta de usuario dinámica | `os.path.expanduser()` reemplaza el `C:\Users\USUARIO` hardcodeado |
| 2026-09-05 | `WAIT(0)` en lugar de `FREEZE` | `FREEZE` cerraba la pantalla gráfica prematuramente — `WAIT(0)` es estable |
| 2026-09-05 | Frecuencia útil en GRAFICA_F: 1–10 | Frecuencias altas producen aliasing (pantalla 319px) — documentado como limitación conocida |
| 2026-09-05 | main.py v2 como estándar | Detección dinámica de N EXPORT — backward compatible, validado contra todos los programas |

> [!note]- Descartadas
> - xcopy directo a `Calculadoras\CASE` — CASE reemplaza el archivo con binario compilado al abrir
> - copia simple UTF-8 a `HP Prime\Calculators\Prime` — CASE lo rechaza sin el header correcto
> - Opción B (formato G1) — Xprime no es open source, requiere paso manual "Check" en CASE
> - Opción C (plantilla binaria) — depende de que el programa ya exista en CASE, menos autónoma que A
