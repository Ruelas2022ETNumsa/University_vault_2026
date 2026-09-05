---
galaxy_body: logbook
scope: tars-hpprgm-conversion
status: on-track
date_updated: 2026-09-05
session: 2026-09-05-2
---

## Visión general

Carrier para resolver la conversión automática de archivos `.hpprgm` desde Obsidian hacia CASE (HP Prime virtual) sin drag and drop manual. El problema central es que el formato `.hpprgm` es binario (header + UTF-16 LE) y un fuente guardado como texto plano UTF-8 no es reconocido por CASE. Se evalúan tres opciones de conversión, una por dropship, hasta encontrar la que funcione de forma confiable.

---

## Estado actual

**Salud:** on-track
**Resumen:** CIRC_DC, TRIG_SOLV y CINEMAT cargados y probados en CASE. Unidades en formato [u] aplicadas. Corriente migrada a mA en CIRC_DC. Símbolo Ω confirmado compatible con CASE.
**Último avance:** Los tres programas pasaron pruebas en CASE con las actualizaciones de formato de unidades y símbolo Ω.
**Próximo hito:** Pruebas con múltiples funciones EXPORT y gráficos.

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

> [!note]- Descartadas
> - xcopy directo a `Calculadoras\CASE` — CASE reemplaza el archivo con binario compilado al abrir
> - copia simple UTF-8 a `HP Prime\Calculators\Prime` — CASE lo rechaza sin el header correcto
> - Opción B (formato G1) — Xprime no es open source, requiere paso manual "Check" en CASE
> - Opción C (plantilla binaria) — depende de que el programa ya exista en CASE, menos autónoma que A
