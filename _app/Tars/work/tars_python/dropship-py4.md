---
galaxy_body: dropship
carrier: "[[tsk_carrier.md]]"
scope: prueba-4
status: activo
date: 2026-09-05
---

## Propósito

Validar gráficos desde Python usando las funciones nativas del módulo `hpprime` — sin pasar por `eval()`. Confirmar que `pixon`, `line`, `fillrect` y `textout` funcionan directamente desde el bloque `#PYTHON` con coordenadas pixel.

---

## Concepto

El módulo `hpprime` expone funciones gráficas que escriben directamente en el buffer G0 (pantalla activa). Son más rápidas que hacer gráficos vía `hpprime.eval("LINE(...)")` porque evitan el parseo PPL. La pantalla es 320×240 px, origen (0,0) en esquina superior izquierda. Se usan coordenadas pixel (`pixon`, `line`, `fillrect`, `textout`) — las variantes cartesianas (`_c`) tienen bugs en firmwares intermedios.

---

## Programa propuesto — PY_GRAF

```python
#PYTHON graf
from hpprime import *

# Limpiar pantalla
fillrect(0, 0, 0, 320, 240, 0xFFFFFF, 0xFFFFFF)

# Título
textout(0, 10, 5, "PY_GRAF — grafico desde Python", 2, 0x000000)

# Cuadrícula de ejes
line(0, 20, 120, 300, 120, 0xAAAAAA)  # eje X
line(0, 160, 20, 160, 220, 0xAAAAAA)  # eje Y

# Graficar seno — 260 puntos entre x=20 y x=300
from math import sin, pi
for px in range(20, 301):
    angulo = (px - 20) / 280 * 2 * pi
    py = int(120 - sin(angulo) * 80)
    pixon(0, px, py, 0x0000FF)

# Etiqueta
textout(0, 25, 200, "sin(x) — 0 a 2pi", 1, 0x0000FF)

# Esperar tecla
eval("wait(0)")
#end

EXPORT PY_GRAF()
BEGIN
  PYTHON(graf);
END;
```

---

## Checklist antes de subir

- [ ] Pantalla 320×240 px — no exceder esos límites en coordenadas
- [ ] Usar coordenadas pixel — no variantes `_c` (cartesianas)
- [ ] `fillrect(G, x, y, w, h, color_borde, color_relleno)` — el primer arg es el objeto gráfico (0 = G0)
- [ ] `pixon(G, x, y, color)` — mismo patrón
- [ ] `line(G, x1, y1, x2, y2, color)` — mismo patrón
- [ ] `textout(G, x, y, texto, fuente, color)` — mismo patrón
- [ ] Colores en hex 0xRRGGBB

---

## Preguntas a validar

1. ¿`fillrect` limpia la pantalla correctamente desde Python?
2. ¿`pixon` en loop dibuja los puntos del seno correctamente?
3. ¿`line` dibuja los ejes?
4. ¿`textout` muestra texto en pantalla?
5. ¿La velocidad del loop de pixon es aceptable vs PPL equivalente?

---

## Resultados

| # | Descripción | Estado | Fecha |
|---|-------------|--------|-------|
| 1 | fillrect — limpiar pantalla | ⬜ | — |
| 2 | pixon en loop — curva seno | ⬜ | — |
| 3 | line — ejes | ⬜ | — |
| 4 | textout — etiqueta | ⬜ | — |
| 5 | velocidad aceptable | ⬜ | — |

---

## Notas
