---
galaxy_body: dropship
carrier: "[[tsk_carrier.md]]"
scope: prueba-2
status: activo
date: 2026-09-05
---

## Propósito

Validar loops (`for`, `while`), listas nativas Python, y control de flujo (`if/elif/else`). Confirmar que la lógica iterativa funciona correctamente y que las listas indexan desde 0 (diferencia clave con PPL).

---

## Concepto

Python en la G2 es más rápido que PPL en iteraciones intensivas. Esta prueba valida esa capacidad con algo útil: una tabla de conversión generada dinámicamente con un loop, y una lista de datos procesada con funciones built-in de Python (`sum`, `min`, `max`, `len`).

---

## Programa propuesto — PY_LOOPS

```python
#PYTHON loops
from math import sqrt

print("=== PY_LOOPS ===")

# --- Tabla de conversión km/h -> m/s ---
print("km/h   m/s")
print("----------")
for kmh in range(0, 121, 20):
    ms = round(kmh / 3.6, 2)
    print(str(kmh) + "     " + str(ms))

# --- Estadística básica con lista ---
datos = []
n = int(input("Cuantos datos? (max 10): "))
if n < 1 or n > 10:
    print("Error: ingresa entre 1 y 10")
else:
    for i in range(n):
        v = float(input("Dato " + str(i+1) + ": "))
        datos.append(v)

    media = sum(datos) / len(datos)
    varianza = sum((x - media)**2 for x in datos) / (len(datos) - 1)
    desv = sqrt(varianza)

    print("Media:", round(media, 4))
    print("Desv est:", round(desv, 4))
    print("Min:", min(datos))
    print("Max:", max(datos))

print("Listo.")
#end

EXPORT PY_LOOPS()
BEGIN
  PRINT();
  PYTHON(loops);
END;
```

---

## Checklist antes de subir

- [ ] Listas indexan desde 0 — no desde 1 como PPL
- [ ] `append()` disponible en MicroPython — confirmado
- [ ] Generator expressions en `sum()` — disponibles en MicroPython 3.4
- [ ] No usar f-strings

---

## Preguntas a validar

1. ¿`for` con `range()` y `step` funciona correctamente?
2. ¿`list.append()` funciona?
3. ¿`sum()`, `min()`, `max()`, `len()` disponibles?
4. ¿Generator expression dentro de `sum()` soportado?
5. ¿`while` con condición de usuario funciona?

---

## Resultados

| # | Descripción | Estado | Fecha |
|---|-------------|--------|-------|
| 1 | for/range/step | ⬜ | — |
| 2 | listas + append | ⬜ | — |
| 3 | sum/min/max/len | ⬜ | — |
| 4 | generator expression | ⬜ | — |
| 5 | estadística básica completa | ⬜ | — |

---

## Notas
