---
galaxy_body: logbook
scope: tars-python
status: on-track
date_updated: 2026-09-05
---

## Visión general

Carrier para explorar y validar el uso de MicroPython embebido en programas `.hpprgm` para la HP Prime G2. Los programas PPL del vault (CIRC_DC, TRIG_SOLV, etc.) son 100% PPL — este carrier abre el territorio de Python, que corre más rápido en cálculo numérico intensivo y habilita lógica más expresiva. El criterio de éxito es confirmar qué categorías de programas Python son viables con el pipeline `tars-sync` existente, y documentar sus límites y diferencias con PPL.

---

## Estado actual

**Salud:** on-track
**Resumen:** Carrier creado. Los 5 dropships están completos con programas listos para copiar y probar.
**Último avance:** dropship-py1 a py5 creados con programas completos (PY_BASICO, PY_LOOPS, PY_EVAL, PY_GRAF, PY_NUMERICO). Ninguna prueba ejecutada aún.
**Próximo hito:** Prueba 1 — PY_BASICO ejecutado en CASE.

---

## Contexto técnico — MicroPython en la G2

### Lo que es
MicroPython embebido en el firmware (basado en Python 3.4 aproximadamente). No se puede actualizar independientemente — lo que hay está fijo hasta la próxima actualización de HP. No hay numpy, scipy ni matplotlib nativo.

### Sintaxis de un programa Python en .hpprgm
```
#PYTHON nombre_bloque
from math import *
from hpprime import *
# código Python acá
#end

EXPORT NOMBRE_PROG()
BEGIN
  PYTHON(nombre_bloque);
END;
```

### Módulos disponibles confirmados
`math`, `cmath`, `random`, `array`, `sys`, `json`, `re`, `gc`, `struct`, `collections` y el más importante: `hpprime` — la librería propia de HP.

### hpprime — funciones clave
- `eval("comando_ppl")` — ejecuta cualquier expresión PPL desde Python. Lento dentro de loops, útil para comandos puntuales.
- Gráficos nativos (más rápidos que via eval): `pixon`, `pixon_c`, `line`, `line_c`, `fillrect`, `fillrect_c`, `textout`, `textout_c`
- Control: `eval("wait()")`, `eval("ticks")`, `eval("keyboard")`
- Mouse/touch: `eval("mouse")` — devuelve coordenadas de toque

### Diferencias con PPL relevantes
- `input()` de Python funciona — muestra prompt en consola de texto
- `print()` funciona — salida a consola
- No hay `CHOOSE` ni `MSGBOX` nativos — se hacen vía `eval("CHOOSE(...)")` o `eval("MSGBOX(...)")`
- f-strings NO soportadas (Python 3.6+) — usar `.format()` o `%`
- Listas indexan desde 0 (distinto a PPL que indexa desde 1)
- Cada bloque `#PYTHON` consume 1MB fijo de memoria
- Python es más rápido que PPL en cálculo numérico intensivo — confirmado en benchmarks G2

### Dependencia
- Carrier `tars-hpprgm-conversion` (delivered) — el script `tars-sync/main.py` convierte el .hpprgm al binario que CASE acepta. No requiere cambios para archivos con bloques #PYTHON.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | archivo de trabajo activo |
| `dropship-py1.md` | dropship | pendiente | Prueba 1 — print, input, math básico |
| `dropship-py2.md` | dropship | pendiente | Prueba 2 — loops y listas |
| `dropship-py3.md` | dropship | pendiente | Prueba 3 — hpprime.eval() |
| `dropship-py4.md` | dropship | pendiente | Prueba 4 — gráficos desde Python |
| `dropship-py5.md` | dropship | pendiente | Prueba 5 — cálculo numérico intensivo |

---

## Hitos

- 2026-09-05-4 — carrier creado, plan de pruebas definido, contexto técnico documentado
- 2026-09-05-5 — 5 dropships creados con programas completos listos para ejecutar en CASE

---

## Riesgos y dependencias

- MicroPython en la G2 es Python ~3.4 — algunas sintaxis modernas no funcionan (f-strings, walrus operator, etc.)
- `hpprime.eval()` dentro de loops es lento — puede hacer que programas Python sean más lentos que PPL en ese caso
- Gráficos cartesianos (`_c`) tienen bugs conocidos en algunos firmwares — preferir pixel coords
- Python no disponible en CASE Android — solo CASE Windows y calc física
- Cada bloque #PYTHON usa 1MB fijo — limita cantidad de bloques simultáneos

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-09-05-4 | 5 pruebas progresivas en lugar de una sola | Cada prueba valida una categoría distinta de capacidad |
| 2026-09-05-4 | Usar pipeline tars-sync existente sin modificar | El script ya maneja #PYTHON correctamente — no requiere cambios |
| 2026-09-05-4 | Gráficos en coordenadas pixel (no cartesianas) | Coordenadas cartesianas tienen bugs en firmwares intermedios |

> [!note]- Descartadas
> - numpy/scipy — no disponibles, requieren librerías nativas no incluidas en firmware
> - f-strings — Python ~3.4, no soportadas
